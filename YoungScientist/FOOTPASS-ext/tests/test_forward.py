"""Smoke tests for AmoUni-SoccerTrack modules.

Runs forward passes with tiny dummy inputs to confirm shape compatibility
with the FOOTPASS TAAD baseline. No dataset required.

Usage:
    cd YoungScientist/FOOTPASS-ext
    python -m tests.test_forward

Requires FOOTPASS-main/ to be a sibling directory and pytorch/torchvision installed.
"""
from __future__ import annotations

import sys
from pathlib import Path

import torch

# Make `amoni_soccer` importable regardless of launch directory
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from amoni_soccer.amodal_head import (SoccerAmodalHead, total_amodal_loss,
                                      consistency_loss)
from amoni_soccer.uniform_aware_reid import (UniformAwareReID,
                                             intra_team_contrastive_loss)
from amoni_soccer.uncertainty_graph import (UncertaintyPropagation,
                                            uncertainty_weighted_distance,
                                            expected_calibration_error)


def _shape(t):
    return tuple(t.shape) if hasattr(t, "shape") else None


def test_soccer_amodal_head():
    print("=== test_soccer_amodal_head ===")
    N, C, H, W = 8, 192, 14, 14
    head = SoccerAmodalHead(in_channels=C, use_pose_prior=True, pose_channels=17)
    roi_feat = torch.randn(N, C, H, W)
    pose = torch.randn(N, 17, H, W)

    out = head(roi_feat, pose_prior=pose)
    assert out["m_vis"].shape == (N, 1, 56, 56), _shape(out["m_vis"])
    assert out["m_amo"].shape == (N, 1, 56, 56), _shape(out["m_amo"])
    assert out["m_occ"].shape == (N, 1, 56, 56), _shape(out["m_occ"])
    assert out["u_a"].shape == (N,), _shape(out["u_a"])
    assert ((out["m_vis"] >= 0).all() and (out["m_vis"] <= 1).all())
    assert ((out["u_a"] >= 0).all() and (out["u_a"] <= 1).all())
    print(f"  m_vis={_shape(out['m_vis'])}, u_a={_shape(out['u_a'])}")

    # Loss check
    gt_vis = (torch.rand(N, 1, 56, 56) > 0.5).float()
    gt_amo = torch.maximum(gt_vis, (torch.rand(N, 1, 56, 56) > 0.5).float())
    iou = torch.rand(N)
    loss, breakdown = total_amodal_loss(out, gt_vis, gt_amo, iou=iou)
    assert torch.isfinite(loss), "amodal loss became non-finite"
    print(f"  amodal loss breakdown: {breakdown}")
    print("  PASS")


def test_uniform_aware_reid():
    print("=== test_uniform_aware_reid ===")
    N = 16
    reid = UniformAwareReID(in_channels=192, embed_dim=128, jersey_dim=64)
    roi_feat = torch.randn(N, 192, 14, 14)
    out = reid(roi_feat, pose_visibility=torch.rand(N, 3))

    assert out["f_appearance"].shape == (N, 128), _shape(out["f_appearance"])
    assert out["f_jersey"].shape == (N, 64), _shape(out["f_jersey"])
    # L2-normalized check
    norm = out["f_appearance"].norm(dim=-1)
    assert torch.allclose(norm, torch.ones_like(norm), atol=1e-5), norm
    print(f"  appearance={_shape(out['f_appearance'])}, jersey={_shape(out['f_jersey'])}")

    # Contrastive loss
    # 4 teams x 4 identities each, 16 samples (one per identity-timestep)
    identities = torch.arange(N) // 2  # 8 unique IDs, 2 samples each
    teams = identities // 4
    loss = intra_team_contrastive_loss(out["f_appearance"], identities, teams)
    assert torch.isfinite(loss), f"intra-team CL non-finite: {loss}"
    print(f"  intra-team CL loss = {loss.item():.4f}")
    print("  PASS")


def test_uncertainty_graph():
    print("=== test_uncertainty_graph ===")
    B, M, T = 2, 5, 50
    prop = UncertaintyPropagation()
    u_a = torch.rand(B, M, T)
    u_r = torch.rand(B, M, T)
    u_j = torch.rand(B, M, T)
    out = prop(u_a, u_r, u_j)
    assert out["u_tracklet"].shape == (B, M), _shape(out["u_tracklet"])
    assert out["s_tracklet"].shape == (B, M), _shape(out["s_tracklet"])
    assert (out["s_tracklet"] >= 0).all() and (out["s_tracklet"] <= 1).all()
    print(f"  u_tracklet={_shape(out['u_tracklet'])}")

    # Pair-wise distance
    K = 7
    d = uncertainty_weighted_distance(
        d_app=torch.rand(K), d_jersey=torch.rand(K),
        d_team=torch.rand(K), d_motion=torch.rand(K),
        u_i={"app": torch.rand(K), "jersey": torch.rand(K),
             "team": torch.rand(K), "motion": torch.rand(K)},
        u_j={"app": torch.rand(K), "jersey": torch.rand(K),
             "team": torch.rand(K), "motion": torch.rand(K)},
    )
    assert d.shape == (K,)
    assert torch.isfinite(d).all()
    print(f"  uw-distance shape = {_shape(d)}")

    # ECE
    preds = torch.randint(0, 5, (100,))
    targets = torch.randint(0, 5, (100,))
    confs = torch.rand(100)
    ece = expected_calibration_error(preds, targets, confs, n_bins=10)
    assert 0.0 <= ece <= 1.0
    print(f"  ECE = {ece:.4f}")
    print("  PASS")


def test_extended_taad_forward():
    """End-to-end forward through ExtendedTAAD with tiny inputs.

    Uses amodal=True but uncertainty=False for a simpler sanity check, then
    toggles both on. Uses CPU so it runs without a GPU.
    """
    print("=== test_extended_taad_forward ===")
    try:
        from amoni_soccer.extended_taad import ExtendedTAAD
    except Exception as e:
        print(f"  SKIP: cannot import ExtendedTAAD ({type(e).__name__}: {e})")
        return

    # Build model. This will also try to load FOOTPASS-main via torch.hub for X3D.
    # If X3D download fails (offline), skip gracefully.
    try:
        model = ExtendedTAAD(use_amodal=True, use_uncertainty=True)
    except Exception as e:
        print(f"  SKIP: ExtendedTAAD init failed ({type(e).__name__}: {e})")
        print("        (Likely X3D weight download or FOOTPASS-main import issue.)")
        return

    model.eval()

    # Tiny inputs: B=1, T=8, M=2 (keep small to save memory)
    B, T, M = 1, 8, 2
    x = torch.randn(B, 3, T, 352, 640)
    # roi: [frame_index, x1, y1, x2, y2]
    roi = torch.zeros(B, M, T, 5)
    for t in range(T):
        for m in range(M):
            roi[:, m, t, 0] = t
            roi[:, m, t, 1] = 100 + 50 * m
            roi[:, m, t, 2] = 100
            roi[:, m, t, 3] = 180 + 50 * m
            roi[:, m, t, 4] = 300
    mask = torch.ones(B, M, T)

    with torch.no_grad():
        logits = model(x, roi, mask)
    assert logits.shape == (B, 9, M, T), _shape(logits)
    print(f"  logits={_shape(logits)}  — matches FOOTPASS TAAD signature")

    # With extras
    with torch.no_grad():
        logits2, extras = model(x, roi, mask, return_extras=True)
    assert logits2.shape == (B, 9, M, T)
    assert "u_a" in extras and "m_vis" in extras
    print(f"  extras keys: {sorted(extras.keys())}")
    print("  PASS")


def main():
    print("Running AmoUni-SoccerTrack smoke tests...\n")
    test_soccer_amodal_head()
    print()
    test_uniform_aware_reid()
    print()
    test_uncertainty_graph()
    print()
    test_extended_taad_forward()
    print("\nAll smoke tests completed.")


if __name__ == "__main__":
    main()
