"""Static validation tests (no PyTorch required).

These tests verify that the AmoUni-SoccerTrack source files parse correctly
and expose the expected public API. They do NOT run any neural network forward
pass — use `test_forward.py` in a proper PyTorch environment for that.

Run:
    cd YoungScientist/FOOTPASS-ext
    python -m tests.test_static
"""
from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PKG = ROOT / "amoni_soccer"

EXPECTED_MODULES = {
    "amodal_head": [
        "SoccerAmodalHead", "amodal_bce_dice_loss", "consistency_loss",
        "uncertainty_calibration_loss", "total_amodal_loss",
    ],
    "uniform_aware_reid": [
        "UniformAwareReID", "intra_team_contrastive_loss",
        "uniform_reid_total_loss",
    ],
    "uncertainty_graph": [
        "UncertaintyPropagation", "uncertainty_weighted_distance",
        "expected_calibration_error",
    ],
    "extended_taad": [
        "ExtendedTAAD", "load_pretrained_taad_weights",
    ],
    "footpass_loader": [
        "load_taad_baseline", "add_footpass_to_path",
        "footpass_data_dir", "footpass_videos_dir",
    ],
}


def _parse_file(path: Path) -> ast.Module:
    src = path.read_text(encoding="utf-8")
    return ast.parse(src, filename=str(path))


def _public_names(tree: ast.Module) -> set[str]:
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if not node.name.startswith("_"):
                names.add(node.name)
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and not tgt.id.startswith("_"):
                    names.add(tgt.id)
    return names


def test_modules_parse():
    print("=== test_modules_parse ===")
    for mod_name in EXPECTED_MODULES:
        path = PKG / f"{mod_name}.py"
        assert path.exists(), f"Missing source: {path}"
        tree = _parse_file(path)  # raises SyntaxError on failure
        print(f"  {mod_name}.py parsed OK ({len(tree.body)} top-level stmts)")
    print("  PASS")


def test_public_api():
    print("=== test_public_api ===")
    missing = []
    for mod_name, expected in EXPECTED_MODULES.items():
        tree = _parse_file(PKG / f"{mod_name}.py")
        got = _public_names(tree)
        miss = [n for n in expected if n not in got]
        if miss:
            missing.append((mod_name, miss))
        else:
            print(f"  {mod_name}: {len(expected)} symbols OK ({sorted(expected)})")
    assert not missing, f"Missing public symbols: {missing}"
    print("  PASS")


def test_init_exports():
    print("=== test_init_exports ===")
    tree = _parse_file(PKG / "__init__.py")
    all_targets = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        all_targets = [e.value for e in node.value.elts
                                       if isinstance(e, ast.Constant)]
    expected = {"SoccerAmodalHead", "UniformAwareReID", "intra_team_contrastive_loss",
                "UncertaintyPropagation", "uncertainty_weighted_distance",
                "ExtendedTAAD"}
    assert set(all_targets) >= expected, (
        f"__all__ missing entries. expected>={sorted(expected)}, got={all_targets}")
    print(f"  __all__ contains {len(all_targets)} symbols: {all_targets}")
    print("  PASS")


def test_extended_taad_signature():
    """Ensure ExtendedTAAD.forward has (x, roi, mask_binary, ...) to match FOOTPASS."""
    print("=== test_extended_taad_signature ===")
    tree = _parse_file(PKG / "extended_taad.py")
    found = False
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "ExtendedTAAD":
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "forward":
                    arg_names = [a.arg for a in item.args.args]
                    assert arg_names[:4] == ["self", "x", "roi", "mask_binary"], (
                        f"Unexpected forward signature: {arg_names}")
                    print(f"  forward args: {arg_names}")
                    found = True
    assert found, "ExtendedTAAD.forward not found"
    print("  PASS")


def test_footpass_main_sibling():
    print("=== test_footpass_main_sibling ===")
    fp_main = ROOT.parent / "FOOTPASS-main"
    taad_file = fp_main / "models" / "model_TAAD_baseline.py"
    assert fp_main.exists(), f"Missing sibling FOOTPASS-main at {fp_main}"
    assert taad_file.exists(), f"Missing {taad_file}"
    print(f"  FOOTPASS-main: {fp_main}")
    print(f"  TAAD baseline file present: {taad_file.name}")
    print("  PASS")


def test_config_yaml():
    print("=== test_config_yaml ===")
    cfg = ROOT / "configs" / "default.yaml"
    assert cfg.exists()
    content = cfg.read_text(encoding="utf-8")
    for key in ["use_amodal", "use_uncertainty", "clip_length", "batch_size",
                "lambda_action", "lambda_consistency", "confidence_threshold"]:
        assert key in content, f"Config missing key: {key}"
    print(f"  default.yaml has all required keys")
    print("  PASS")


def test_scripts_parse():
    print("=== test_scripts_parse ===")
    for script in ["train_amoni_taad.py", "eval_amoni_taad.py"]:
        path = ROOT / "scripts" / script
        assert path.exists(), f"Missing {path}"
        _parse_file(path)
        print(f"  {script} parsed OK")
    print("  PASS")


def main():
    print("Running static validation (no PyTorch required)...\n")
    test_modules_parse()
    print()
    test_public_api()
    print()
    test_init_exports()
    print()
    test_extended_taad_signature()
    print()
    test_footpass_main_sibling()
    print()
    test_config_yaml()
    print()
    test_scripts_parse()
    print("\n[OK] All static checks passed.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        sys.exit(2)
