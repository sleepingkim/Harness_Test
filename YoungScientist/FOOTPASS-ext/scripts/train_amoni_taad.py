"""Training entrypoint for AmoUni-SoccerTrack Extended TAAD.

Usage:
    python scripts/train_amoni_taad.py --config configs/default.yaml

The script wraps FOOTPASS-main/utils/TAAD_Dataset without modifying upstream.
If amodal GT masks are unavailable (common in current FOOTPASS release), the
amodal branch is trained self-supervised via consistency loss only.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import yaml
from torch.utils.data import DataLoader

# Allow `import amoni_soccer.*` when launched from FOOTPASS-ext root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from amoni_soccer.extended_taad import ExtendedTAAD
from amoni_soccer.amodal_head import consistency_loss
from amoni_soccer.footpass_loader import add_footpass_to_path


def seed_all(seed: int) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_dataloaders(cfg: dict):
    """Use FOOTPASS upstream TAAD_Dataset as-is."""
    add_footpass_to_path()
    from utils.TAAD_Dataset import TAAD_Dataset  # type: ignore

    d = cfg["data"]
    train_ds = TAAD_Dataset(
        data_root=d["data_root"],
        set_status="train",
        clip_length=d["clip_length"],
        max_nb_samples_per_class=d["max_nb_samples_per_class"],
        nb_tracklets=d["nb_tracklets"],
        label_dilation=d["label_dilation"],
        norm_m_std=(d["norm_mean"], d["norm_std"]),
    )
    val_ds = TAAD_Dataset(
        data_root=d["data_root"],
        set_status="val",
        clip_length=d["clip_length"],
        max_nb_samples_per_class=d["max_nb_samples_per_class"],
        nb_tracklets=d["nb_tracklets"],
        label_dilation=d["label_dilation"],
        norm_m_std=(d["norm_mean"], d["norm_std"]),
    )
    train_dl = DataLoader(train_ds, batch_size=cfg["train"]["batch_size"],
                          shuffle=True, num_workers=cfg["train"]["num_workers"],
                          drop_last=True, pin_memory=True)
    val_dl = DataLoader(val_ds, batch_size=cfg["train"]["batch_size"],
                        shuffle=False, num_workers=cfg["train"]["num_workers"],
                        drop_last=False, pin_memory=True)
    return train_dl, val_dl


def build_model_and_optim(cfg: dict, device: torch.device):
    model = ExtendedTAAD(
        use_amodal=cfg["model"]["use_amodal"],
        use_uncertainty=cfg["model"]["use_uncertainty"],
        amodal_channels=cfg["model"]["amodal_channels"],
        pose_channels=cfg["model"]["pose_channels"],
    ).to(device)

    t = cfg["train"]
    optim = torch.optim.AdamW(model.parameters(), lr=t["lr"],
                              weight_decay=t["weight_decay"])
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(
        optim, T_max=t["epochs"], eta_min=t["lr"] * 0.01)
    return model, optim, sched


def action_loss(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    """Cross-entropy on (B, 9, M, T) logits against (B, M, T) integer labels."""
    B, C, M, T = logits.shape
    logits_flat = logits.permute(0, 2, 3, 1).reshape(-1, C)  # (B*M*T, C)
    labels_flat = labels.reshape(-1).long()
    return F.cross_entropy(logits_flat, labels_flat)


def one_epoch(model: nn.Module, loader, optim, device, cfg: dict,
              train: bool = True) -> dict:
    model.train(train)
    total = {"action": 0.0, "consistency": 0.0, "n": 0}

    for batch in loader:
        # The upstream TAAD_Dataset returns a tuple; defensive unpacking
        # Expected: (clip, rois, masks, labels, ...)
        if isinstance(batch, (list, tuple)) and len(batch) >= 4:
            clip, rois, masks, labels = batch[:4]
        else:
            # Unknown format — keep placeholder to unblock forward tests
            raise ValueError("Unexpected TAAD_Dataset batch format; "
                             "inspect upstream and adapt unpacking.")

        clip = clip.to(device, non_blocking=True)
        rois = rois.to(device, non_blocking=True)
        masks = masks.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        if train:
            optim.zero_grad(set_to_none=True)

        logits, extras = model(clip, rois, masks, return_extras=True)
        L_action = action_loss(logits, labels)

        loss = cfg["train"]["lambda_action"] * L_action
        total["action"] += L_action.item() * clip.size(0)

        if extras and "m_vis" in extras and "m_amo" in extras:
            L_cons = consistency_loss(extras["m_vis"], extras["m_amo"])
            loss = loss + cfg["train"]["lambda_consistency"] * L_cons
            total["consistency"] += L_cons.item() * clip.size(0)

        if train:
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(),
                                           cfg["train"]["grad_clip"])
            optim.step()

        total["n"] += clip.size(0)

    return {k: (v / max(total["n"], 1)) if k != "n" else v
            for k, v in total.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/default.yaml")
    parser.add_argument("--smoke", action="store_true",
                        help="Run 1 iteration without full epoch (for debugging).")
    args = parser.parse_args()

    cfg = load_config(args.config)
    seed_all(cfg["experiment"]["seed"])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[train_amoni_taad] device={device}")

    output_dir = Path(cfg["experiment"]["output_dir"]) / cfg["experiment"]["name"]
    output_dir.mkdir(parents=True, exist_ok=True)

    train_dl, val_dl = build_dataloaders(cfg)
    model, optim, sched = build_model_and_optim(cfg, device)

    best_val = float("inf")
    for epoch in range(cfg["train"]["epochs"]):
        if args.smoke and epoch > 0:
            break
        train_stats = one_epoch(model, train_dl, optim, device, cfg, train=True)
        val_stats = one_epoch(model, val_dl, optim, device, cfg, train=False)
        sched.step()

        print(f"[epoch {epoch:03d}] train={train_stats} val={val_stats}")

        if val_stats["action"] < best_val:
            best_val = val_stats["action"]
            torch.save({"model": model.state_dict(), "epoch": epoch, "cfg": cfg},
                       output_dir / "best.pt")
            print(f"  -> saved best ({best_val:.4f}) to {output_dir/'best.pt'}")


if __name__ == "__main__":
    main()
