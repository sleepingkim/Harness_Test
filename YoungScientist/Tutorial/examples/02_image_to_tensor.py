"""
Tutorial 02 — 이미지가 텐서가 되기까지

목표: "JPG 파일"이 "신경망이 먹을 수 있는 숫자 배열"이 되는 전 과정을 본다.
FOOTPASS의 `TAAD_Dataset._get_clip()`이 내부적으로 하는 일과 동일하다.

실행:
    python examples/02_image_to_tensor.py

요구 라이브러리: numpy, pillow, matplotlib
"""
from _common import setup_utf8; setup_utf8()

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "outputs"
DATA = HERE.parent / "data"
OUT.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)


# ───────────────────────────────────────────────────────────────
# 개념 1. 이미지 파일은 그 자체로는 신경망에 못 넣는다
# ───────────────────────────────────────────────────────────────
# 파일이 JPG든 PNG든, 컴퓨터 입장에선 '압축된 바이트'일 뿐.
# 우리가 꺼내고 싶은 건 '픽셀 격자'(2D 또는 3D 배열).
# 이 변환을 PIL(Pillow)이 해준다.

print("=" * 60)
print("STEP 1: 더미 이미지 생성 (축구 영상 한 프레임 흉내)")
print("=" * 60)

# 320x180 녹색 경기장 위에 선수 두 명 박스를 그린 가짜 프레임 생성
img = Image.new("RGB", (320, 180), color=(60, 140, 60))
d = ImageDraw.Draw(img)
# 선수 1: 파란 박스
d.rectangle([(80, 60), (100, 120)], fill=(40, 80, 200))
# 선수 2: 빨간 박스
d.rectangle([(200, 70), (220, 130)], fill=(200, 40, 40))
# 공: 흰 원
d.ellipse([(150, 90), (160, 100)], fill=(250, 250, 250))

dummy_path = DATA / "dummy_frame.png"
img.save(dummy_path)
print(f"더미 이미지 저장: {dummy_path}")
print(f"  (실제 FOOTPASS에선 decord.VideoReader가 영상에서 한 프레임씩 꺼낸다)")


# ───────────────────────────────────────────────────────────────
# 개념 2. PIL Image → numpy 배열
# ───────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 2: PIL → numpy (픽셀 숫자로)")
print("=" * 60)

pil = Image.open(dummy_path)
arr = np.array(pil)                         # (H, W, C) = (180, 320, 3)
print(f"PIL Image → np.array()")
print(f"  shape = {arr.shape}   ← 주의: PIL/OpenCV 관례는 (H, W, C)")
print(f"  dtype = {arr.dtype}    ← 픽셀 값은 0~255 범위의 uint8")
print(f"  min   = {arr.min()}, max = {arr.max()}")
print()
print(f"한 픽셀 예: arr[90, 160] = {arr[90, 160]}  # (중앙 공 픽셀, 흰색)")
print(f"            arr[80, 80]  = {arr[80, 80]}   # (왼쪽 선수 박스 안쪽)")


# ───────────────────────────────────────────────────────────────
# 개념 3. 신경망용 전처리 — 정규화 (normalization)
# ───────────────────────────────────────────────────────────────
# 왜 정규화하나?
#   (a) 값의 스케일을 맞추면 학습이 안정된다
#   (b) 사전학습된 모델은 "이런 통계를 가진 입력"을 가정함 → 맞춰줘야 함
#
# FOOTPASS TAAD_Dataset의 기본값: norm_m_std = (0.45, 0.225)
#   의미: "먼저 0~1로 만들고, 평균 0.45를 빼고 표준편차 0.225로 나눠라"
#
# x_normalized = (x / 255.0 - mean) / std

print("\n" + "=" * 60)
print("STEP 3: 정규화 (FOOTPASS와 동일: mean=0.45, std=0.225)")
print("=" * 60)

x01 = arr.astype(np.float32) / 255.0        # [0,1] 범위
mean, std = 0.45, 0.225
x_norm = (x01 - mean) / std
print(f"0~255 uint8       →  {arr.dtype}, min={arr.min()}, max={arr.max()}")
print(f"0~1 float32       →  {x01.dtype}, min={x01.min():.3f}, max={x01.max():.3f}")
print(f"정규화 후          →  {x_norm.dtype}, min={x_norm.min():.3f}, max={x_norm.max():.3f}")
print(f"  ← 평균 근처가 0, 스케일이 대체로 [-2, 2] 범위로 들어온다")


# ───────────────────────────────────────────────────────────────
# 개념 4. PyTorch 관례로 변환 — (H,W,C) → (C,H,W)
# ───────────────────────────────────────────────────────────────
# 컴퓨터 비전 라이브러리의 두 가지 관례:
#   - PIL, OpenCV, numpy의 기본: (H, W, C) — 이미지를 눈으로 보는 순서
#   - PyTorch, 딥러닝 모델:        (C, H, W) — 채널을 맨 앞
# PyTorch가 후자를 쓰는 이유: CNN의 conv 연산이 'C' 축에 대해 행렬곱을 하기
# 때문에, 같은 채널이 메모리상 연속되면 훨씬 빠르다.

print("\n" + "=" * 60)
print("STEP 4: (H,W,C) → (C,H,W) — PyTorch 관례로 축 전치")
print("=" * 60)

tensor_like = x_norm.transpose(2, 0, 1)     # (C, H, W)
print(f"변환 전 shape (H,W,C) = {x_norm.shape}")
print(f"변환 후 shape (C,H,W) = {tensor_like.shape}")
print("(FOOTPASS에선 이 후 decord + cv2.resize로 (352,640)까지 바꾼 뒤 stack해서 (T,H,W,C)가 되고,")
print(" 최종적으로 torch tensor가 되어 (B, 3, T, 352, 640)으로 모델에 들어간다)")


# ───────────────────────────────────────────────────────────────
# 개념 5. 여러 프레임 → 비디오 클립 (T축 생성)
# ───────────────────────────────────────────────────────────────
# FOOTPASS의 _get_clip은 `decord.VideoReader.get_batch(프레임_인덱스_리스트)`
# 를 호출해서 여러 프레임을 한번에 numpy로 받아온다. 그러면 shape은
# (T, H, W, 3)이 된다. 이걸 transpose해서 (3, T, H, W), 그 뒤 batch를 붙이면
# (B, 3, T, H, W) 가 완성된다.

print("\n" + "=" * 60)
print("STEP 5: T개 프레임을 묶어 비디오 클립 만들기")
print("=" * 60)

# 가짜로 같은 프레임을 T=8번 복제
T = 8
clip = np.stack([arr] * T, axis=0)          # (T, H, W, 3)
print(f"T 프레임 stack    shape = {clip.shape}  ← (T, H, W, C)")

clip = clip.transpose(3, 0, 1, 2)           # (C, T, H, W)
print(f"transpose로 축 정리 shape = {clip.shape}  ← (C, T, H, W)")

clip = clip[np.newaxis, ...]                # (1, C, T, H, W)
print(f"batch 차원 추가    shape = {clip.shape}  ← (B=1, C=3, T={T}, H, W)")
print(f"이게 바로 FOOTPASS TAAD의 첫 번째 입력 x 와 똑같은 포맷이다.")


# ───────────────────────────────────────────────────────────────
# 시각화: 각 단계를 PNG로 저장
# ───────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(arr)
axes[0].set_title(f"Original (H,W,C)={arr.shape}")
axes[0].axis("off")

axes[1].imshow(x01)
axes[1].set_title(f"Normalized to [0,1]\nmin={x01.min():.2f}, max={x01.max():.2f}")
axes[1].axis("off")

axes[2].imshow(np.clip(x_norm * std + mean, 0, 1))
axes[2].set_title(f"After mean/std norm\nmin={x_norm.min():.2f}, max={x_norm.max():.2f}\n(복원해서 표시)")
axes[2].axis("off")
fig.suptitle("이미지 → 정규화된 텐서가 되는 과정")
fig.tight_layout()
out_png = OUT / "02_normalization_steps.png"
plt.savefig(out_png, dpi=100)
plt.close(fig)
print(f"\n시각화 저장: {out_png}")


# ───────────────────────────────────────────────────────────────
# FOOTPASS 코드와의 연결
# ───────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("★ FOOTPASS 코드와의 연결")
print("=" * 60)
print("""
FOOTPASS-main/utils/TAAD_Dataset.py, line 133~150 (_get_clip 함수):

    vr = VideoReader(vidfilename, ctx=cpu(0))               # 비디오 파일 열기
    frames = vr.get_batch(np.asarray(frame_range)).asnumpy() # 지정 프레임 꺼냄
    # frames: (T, H, W, 3)  uint8
    if w != 640 or h != 352:
        resized = [cv2.resize(fr, (640, 352), ...) for fr in frames]
        clip = np.stack(resized, axis=0)                     # (T, 352, 640, 3)
    return clip

위 흐름을 우리가 오늘 step 1~5에서 손으로 따라한 것이다.
정규화는 나중에 Dataset.__getitem__에서, 배치 차원은 DataLoader가 붙인다.
""")

print("✅ Tutorial 02 완료. 다음: 03_bounding_box_basics.py")
