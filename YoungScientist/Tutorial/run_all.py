"""7개 튜토리얼을 순서대로 실행하는 launcher.

사용:
    python run_all.py              # 전체 실행
    python run_all.py 03           # 03만 실행
    python run_all.py 01 02 03     # 여러 개 실행
"""
import io
import subprocess
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
EX = HERE / "examples"

titles = {
    "01": "텐서와 shape — 딥러닝의 알파벳",
    "02": "이미지가 텐서가 되기까지",
    "03": "Bounding Box 3가지 표현과 IoU",
    "04": "RoIAlign 직접 구현",
    "05": "Binary vs Soft Mask (AmoUni 핵심)",
    "06": "최소 MOT 직접 구현",
    "07": "FOOTPASS TAAD forward 한 줄씩",
}


def run_one(idx: str) -> bool:
    files = sorted(EX.glob(f"{idx}_*.py"))
    if not files:
        print(f"[SKIP] {idx} : 파일 없음")
        return False
    script = files[0]
    print(f"\n{'='*78}")
    print(f"▶ Tutorial {idx}: {titles.get(idx, script.stem)}")
    print(f"   파일: {script.name}")
    print("=" * 78)
    r = subprocess.run([sys.executable, str(script)], cwd=str(EX))
    return r.returncode == 0


def main():
    args = sys.argv[1:]
    if not args:
        targets = list(titles.keys())
    else:
        targets = args

    ok = 0
    for idx in targets:
        if run_one(idx):
            ok += 1

    print(f"\n{'='*78}")
    print(f"결과: {ok}/{len(targets)} 튜토리얼 성공")
    print(f"시각화: {HERE/'outputs'}")
    print("=" * 78)


if __name__ == "__main__":
    main()
