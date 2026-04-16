"""Helper to import FOOTPASS-main modules without modifying the upstream repository.

FOOTPASS-main is a sibling directory (not a pip-installable package), so we
add it to sys.path lazily. All imports from FOOTPASS-main are centralized here.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path


def _footpass_main_root() -> Path:
    """Return the path to the sibling FOOTPASS-main directory."""
    here = Path(__file__).resolve()
    # FOOTPASS-ext/amoni_soccer/footpass_loader.py
    # FOOTPASS-ext/..
    # └── FOOTPASS-main
    root = here.parent.parent.parent / "FOOTPASS-main"
    if not root.exists():
        raise FileNotFoundError(
            f"FOOTPASS-main not found at {root}. "
            "Ensure the upstream repo is placed as a sibling of FOOTPASS-ext."
        )
    return root


def add_footpass_to_path() -> str:
    """Append FOOTPASS-main to sys.path. Returns the path added."""
    root = str(_footpass_main_root())
    if root not in sys.path:
        sys.path.insert(0, root)
    return root


def load_taad_baseline():
    """Import and return FOOTPASS-main/models/model_TAAD_baseline.X3D_TAAD_Baseline."""
    add_footpass_to_path()
    from models.model_TAAD_baseline import X3D_TAAD_Baseline  # type: ignore
    return X3D_TAAD_Baseline


def load_gnn_model():
    """Import TAAD+GNN model (optional, requires torch_geometric)."""
    add_footpass_to_path()
    from models.model_GNN import TAAD_GNN  # type: ignore  # noqa: F401
    return TAAD_GNN


def load_dst_model():
    """Import TAAD+DST model."""
    add_footpass_to_path()
    from models.model_DST import DST  # type: ignore  # noqa: F401
    return DST


def footpass_data_dir() -> Path:
    """Return FOOTPASS-main/data path."""
    return _footpass_main_root() / "data"


def footpass_videos_dir() -> Path:
    """Return FOOTPASS-main/videos path."""
    return _footpass_main_root() / "videos"
