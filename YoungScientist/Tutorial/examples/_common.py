"""공통 헬퍼: Windows 콘솔에서 한글이 깨지지 않도록 UTF-8 출력 재설정.

각 튜토리얼 맨 위에 다음 한 줄만 넣으면 됩니다:
    from _common import setup_utf8; setup_utf8()
"""
import io
import sys


def setup_utf8() -> None:
    """Windows cp1252 환경에서 stdout을 UTF-8로 재설정한다."""
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        except Exception:
            pass  # 이미 재설정되었거나 buffer가 없으면 조용히 패스

    # matplotlib 한글 폰트 설정 (Windows 기본 폰트 우선)
    try:
        import matplotlib
        import matplotlib.font_manager as fm

        candidates = ["Malgun Gothic", "NanumGothic", "AppleGothic", "Noto Sans CJK KR"]
        available = {f.name for f in fm.fontManager.ttflist}
        for c in candidates:
            if c in available:
                matplotlib.rcParams["font.family"] = c
                matplotlib.rcParams["axes.unicode_minus"] = False
                break
    except Exception:
        pass
