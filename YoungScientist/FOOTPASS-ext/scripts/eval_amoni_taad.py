"""Evaluation entrypoint for AmoUni-SoccerTrack Extended TAAD.

Produces predictions in the FOOTPASS JSON format and invokes the upstream
`evaluation.py` script for F1@0.15 computation (tolerance ±12 frames).
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import torch
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from amoni_soccer.extended_taad import ExtendedTAAD
from amoni_soccer.footpass_loader import _footpass_main_root


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True,
                        help="Path to trained .pt checkpoint")
    parser.add_argument("--config", type=str, default="configs/default.yaml")
    parser.add_argument("--split", type=str, choices=["val", "test"], default="val")
    parser.add_argument("--output", type=str, default="runs/predictions.json")
    parser.add_argument("--run-evaluation", action="store_true",
                        help="Invoke FOOTPASS-main/evaluation.py after writing JSON")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = ExtendedTAAD(
        use_amodal=cfg["model"]["use_amodal"],
        use_uncertainty=cfg["model"]["use_uncertainty"],
    ).to(device)
    state = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(state.get("model", state))
    model.eval()

    # TODO: iterate through val/test split, run model, write predictions in
    # FOOTPASS JSON format (see FOOTPASS-main/README.md: {frame, team, jersey,
    # class, confidence}). The upstream run_TAAD_on_matches.py + NPpreds2JSON.py
    # can be reused; wrap them here once we have trained weights.
    print("[eval_amoni_taad] Prediction loop not yet implemented. "
          "This script currently loads the checkpoint only.")

    if args.run_evaluation:
        fp_root = _footpass_main_root()
        gt = fp_root / "playbyplay_GT" / f"playbyplay_{args.split}.json"
        pred = Path(args.output).resolve()
        eval_cmd = [
            sys.executable, str(fp_root / "evaluation.py"),
            "--predictions_file", str(pred),
            "--ground_truth_file", str(gt),
        ]
        print("[eval_amoni_taad] running:", " ".join(eval_cmd))
        subprocess.run(eval_cmd, check=True)


if __name__ == "__main__":
    main()
