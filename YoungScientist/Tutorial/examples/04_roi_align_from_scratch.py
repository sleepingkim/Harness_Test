"""
Tutorial 04 — RoIAlign을 직접 구현해서 원리 이해하기

목표: FOOTPASS TAAD의 핵심 연산 `roi_align(x, roi, (4,2), 0.125)`의 의미를
몸으로 익힌다. 개념만 알면 "bbox로 feature의 일부를 잘라와 고정 크기로
resize한다"인데, 실제로 해보면 세 가지 디테일을 만난다:
    (1) spatial_scale — feature map이 원본 이미지보다 작을 때 좌표 변환
    (2) output_size   — 어떤 크기로 자를까
    (3) bilinear      — 경계 픽셀은 보간

실행:
    python examples/04_roi_align_from_scratch.py
"""
from _common import setup_utf8; setup_utf8()

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "outputs"
OUT.mkdir(exist_ok=True)


# ───────────────────────────────────────────────────────────────
# 개념 1. Feature map은 원본보다 작다
# ───────────────────────────────────────────────────────────────
# CNN을 거치면 feature map은 점점 작아진다 (stride 때문).
# FOOTPASS의 경우:
#   입력 이미지:  640 x 352
#   backbone 후 feature: 80 x 44   (1/8 크기)
#
# bbox 좌표는 입력 이미지 공간(640x352)에서 주어지지만, feature map에서
# 자르려면 좌표를 1/8로 줄여야 한다. 이 '줄임 비율'이 spatial_scale 이다.
#
#   torchvision.roi_align(..., spatial_scale=0.125)
#   ← 0.125 = 1/8.   "bbox 좌표에 0.125를 곱해서 feature 좌표로 바꿔라"

print("=" * 60)
print("개념 1: feature map 스케일 이해")
print("=" * 60)

IMG_H, IMG_W = 32, 64           # 튜토리얼용 작은 이미지 (실제: 352, 640)
FEAT_H, FEAT_W = 4, 8           # stride=8 이므로 feature는 1/8 크기
SCALE = FEAT_W / IMG_W          # 0.125
print(f"입력 이미지:     ({IMG_H}, {IMG_W})")
print(f"feature map:    ({FEAT_H}, {FEAT_W})")
print(f"spatial_scale:  {SCALE}   ← bbox 좌표에 곱할 축소 비율")


# ───────────────────────────────────────────────────────────────
# 개념 2. 가짜 feature map 생성
# ───────────────────────────────────────────────────────────────
# 실제론 CNN이 만들어주지만, 여기선 눈에 보이게 숫자 채운 배열을 feature로
# 가정한다. 채널 차원은 1로 둬서 시각화가 쉽게.

np.random.seed(0)
feat = np.arange(FEAT_H * FEAT_W, dtype=np.float32).reshape(FEAT_H, FEAT_W)
# (H=4, W=8) 로 값은 0..31
print("\n가짜 feature map (4x8):")
print(feat.astype(int))


# ───────────────────────────────────────────────────────────────
# 개념 3. RoIAlign 스텝 1 — bbox 좌표를 feature 공간으로 변환
# ───────────────────────────────────────────────────────────────
# 이미지 공간의 xyxy bbox를 feature 공간으로 스케일 다운.

bbox_img = np.array([10, 5, 50, 25], dtype=np.float32)   # 이미지 공간 xyxy
bbox_feat = bbox_img * SCALE
print("\n" + "=" * 60)
print("개념 3: bbox 좌표 스케일")
print("=" * 60)
print(f"이미지 공간 bbox    = {bbox_img.tolist()}")
print(f"  → feature 공간   = {bbox_feat.tolist()}")
print(f"     (feature 위에서 x=1.25 ~ 6.25, y=0.625 ~ 3.125 영역)")


# ───────────────────────────────────────────────────────────────
# 개념 4. RoIAlign 스텝 2 — 원하는 output 크기로 sampling grid 만들기
# ───────────────────────────────────────────────────────────────
# output_size = (out_h, out_w). FOOTPASS는 (4, 2) 를 쓴다.
# bbox를 out_h × out_w 개의 칸으로 균등 분할하고, 각 칸의 중심을 샘플링
# 지점으로 한다.

def make_sampling_grid(bbox, out_size):
    x1, y1, x2, y2 = bbox
    out_h, out_w = out_size
    # 각 칸 하나의 폭/높이 (feature 공간 기준)
    bin_h = (y2 - y1) / out_h
    bin_w = (x2 - x1) / out_w
    ys = np.array([y1 + (i + 0.5) * bin_h for i in range(out_h)])
    xs = np.array([x1 + (j + 0.5) * bin_w for j in range(out_w)])
    return xs, ys  # 1D 좌표


out_size = (2, 4)       # 출력 크기 (H, W)
xs, ys = make_sampling_grid(bbox_feat, out_size)
print("\n" + "=" * 60)
print(f"개념 4: 출력 크기 {out_size} 로 sampling grid 만들기")
print("=" * 60)
print(f"bbox_feat = {bbox_feat.tolist()}")
print(f"출력 y 좌표 (feature 공간): {ys.round(3).tolist()}")
print(f"출력 x 좌표 (feature 공간): {xs.round(3).tolist()}")
print("각 격자 중심에서 feature 값을 'bilinear interpolation'으로 샘플한다.")


# ───────────────────────────────────────────────────────────────
# 개념 5. RoIAlign 스텝 3 — bilinear interpolation
# ───────────────────────────────────────────────────────────────
# 격자 중심은 실수 좌표라서 정수 픽셀 위가 아니다. 주변 4개 픽셀을 가중치로
# 섞어서 매끄러운 값을 얻는다. (RoIPool은 그냥 반올림해서 '끊김'이 생기므로
# RoIAlign이 더 정확하다는 것이 Mask R-CNN 논문의 핵심.)

def bilinear_sample(feat, x, y):
    """feature (H,W)에서 실수 좌표 (x,y)의 값을 bilinear로 샘플."""
    H, W = feat.shape
    # 범위 clamp
    x = np.clip(x, 0, W - 1)
    y = np.clip(y, 0, H - 1)
    x0, y0 = int(np.floor(x)), int(np.floor(y))
    x1_, y1_ = min(x0 + 1, W - 1), min(y0 + 1, H - 1)
    wx = x - x0
    wy = y - y0
    top = (1 - wx) * feat[y0, x0] + wx * feat[y0, x1_]
    bot = (1 - wx) * feat[y1_, x0] + wx * feat[y1_, x1_]
    return (1 - wy) * top + wy * bot


def my_roi_align(feat, bbox_img, spatial_scale, out_size):
    """직접 구현한 RoIAlign (1채널, 배치 없음)."""
    bbox_feat = bbox_img * spatial_scale
    xs, ys = make_sampling_grid(bbox_feat, out_size)
    out = np.zeros(out_size, dtype=np.float32)
    for i, y in enumerate(ys):
        for j, x in enumerate(xs):
            out[i, j] = bilinear_sample(feat, x, y)
    return out


pooled = my_roi_align(feat, bbox_img, SCALE, out_size)
print("\n" + "=" * 60)
print("개념 5: 직접 구현한 RoIAlign의 결과")
print("=" * 60)
print(f"입력 feature (4x8):\n{feat.astype(int)}")
print(f"\n출력 pooled {out_size}:\n{pooled.round(2)}")
print("출력의 각 값은 feature 상의 해당 격자 중심에서 샘플된 (보간된) 값이다.")


# ───────────────────────────────────────────────────────────────
# 시각화
# ───────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].imshow(feat, cmap="viridis")
axes[0].set_title(f"Feature map {feat.shape}")
# bbox_feat를 겹쳐 그리기
x1, y1, x2, y2 = bbox_feat
axes[0].plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], color="red", lw=2)
# sampling grid 점 찍기
xs_g, ys_g = make_sampling_grid(bbox_feat, out_size)
for y in ys_g:
    for x in xs_g:
        axes[0].plot(x, y, "wx", markersize=10, mew=2)
axes[0].set_xlabel("x (feature space)")
axes[0].set_ylabel("y (feature space)")

axes[1].imshow(pooled, cmap="viridis")
axes[1].set_title(f"RoIAligned output {pooled.shape}")
for (j, i), v in np.ndenumerate(pooled):
    axes[1].text(i, j, f"{v:.1f}", ha="center", va="center",
                  color="white")

fig.suptitle("RoIAlign: 빨간 bbox 안에서 × 지점들을 샘플 → 오른쪽")
fig.tight_layout()
out_png = OUT / "04_roi_align_demo.png"
plt.savefig(out_png, dpi=100)
plt.close(fig)
print(f"\n시각화 저장: {out_png}")


# ───────────────────────────────────────────────────────────────
# FOOTPASS 코드와 연결
# ───────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("★ FOOTPASS 코드와의 연결")
print("=" * 60)
print("""
FOOTPASS-main/models/model_TAAD_baseline.py, line 63:

    x = roi_align(x, roi, (4,2), 0.125)     # (B*T*M, 192, 4, 2)
                ↑       ↑      ↑     ↑
                |       |      |     └─ spatial_scale (feature가 이미지의 1/8)
                |       |      └─ output_size (H=4, W=2): 작은 feature 조각
                |       └─ bbox 리스트 [frame_idx, x1, y1, x2, y2]
                └─ feature map (B*T, 192, 44, 80)

즉 한 줄로 "각 선수 박스 영역을 feature 위에서 4x2 격자로 잘라오기"를 한다.
잘려온 조각은 이후 avgpool → conv → FC로 흘러서 각 선수의 action logit이 된다.

FOOTPASS-ext/amoni_soccer/extended_taad.py 는 이 roi_align을 그대로 재사용
하므로 (줄 83) 이 튜토리얼을 이해하면 우리 확장 코드도 한 줄 한 줄 보인다.
""")

print("✅ Tutorial 04 완료. 다음: 05_binary_vs_soft_mask.py")
