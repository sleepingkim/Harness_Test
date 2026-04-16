"""
Tutorial 01 — 텐서와 shape: 딥러닝의 알파벳

목표: 딥러닝 코드를 읽는 가장 기초. '텐서'와 'shape'이 뭐고 왜 모두가 shape에
집착하는지 이해한다. 이 파일을 실행해서 shape이 변하는 모습을 눈으로 보라.

실행:
    python examples/01_tensors_and_shapes.py

요구 라이브러리: numpy (PyTorch 불필요)
"""
import sys, io
# Windows 콘솔에서 한글 출력이 깨지지 않도록 UTF-8로 재설정
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import numpy as np


# ───────────────────────────────────────────────────────────────
# 개념 1. 텐서는 '여러 차원을 가진 숫자 배열'이다
# ───────────────────────────────────────────────────────────────
# 스칼라(scalar):   shape = ()         예: 5
# 벡터(vector):    shape = (N,)        예: [1, 2, 3]
# 행렬(matrix):    shape = (H, W)      예: 흑백 이미지 한 장
# 3D 텐서:         shape = (C, H, W)   예: RGB 이미지 한 장 (C=3 채널)
# 4D 텐서:         shape = (B, C, H, W) 예: 이미지 여러 장 (Batch)
# 5D 텐서:         shape = (B, C, T, H, W) 예: 비디오 여러 개 (T=시간축)

print("=" * 60)
print("개념 1: 차원이 하나씩 늘어나는 모습")
print("=" * 60)

scalar = np.array(5.0)
vec = np.array([1.0, 2.0, 3.0])
mat = np.array([[1, 2, 3], [4, 5, 6]])
img = np.random.rand(3, 4, 5)             # (C=3, H=4, W=5)
batch = np.random.rand(2, 3, 4, 5)         # (B=2, C=3, H=4, W=5)
video = np.random.rand(2, 3, 10, 4, 5)     # (B=2, C=3, T=10, H=4, W=5)

for name, t in [("스칼라", scalar), ("벡터", vec), ("행렬", mat),
                ("이미지(C,H,W)", img), ("배치 이미지", batch), ("비디오 배치", video)]:
    print(f"{name:20s} shape={t.shape}  ndim={t.ndim}")


# ───────────────────────────────────────────────────────────────
# 개념 2. 왜 첫 차원이 Batch인가?
# ───────────────────────────────────────────────────────────────
# 딥러닝에선 **데이터를 여러 개 묶어서** 한 번에 처리한다. 왜?
# - GPU가 병렬 처리에 강함 → 묶어 보내야 효율 나옴
# - 평균적 gradient가 학습을 안정시킴
#
# FOOTPASS TAAD의 입력 shape: (B, 3, T, 352, 640)
#   B=1  이면 영상 1개
#   B=4  이면 영상 4개 묶음 학습
# 배치 크기는 학습 시 매우 자주 바뀌므로 항상 "첫 차원"에 둔다.

print("\n" + "=" * 60)
print("개념 2: Batch 차원 — 데이터 여러 개를 한 번에")
print("=" * 60)

one_image = np.random.rand(3, 352, 640)        # 이미지 한 장
batch_of_4 = np.stack([one_image] * 4, axis=0)  # 배치로 묶기
print(f"이미지 한 장            shape={one_image.shape}")
print(f"4장 묶음 (np.stack)     shape={batch_of_4.shape}")
print(f"→ 앞에 차원 하나가 생겼다. 이게 batch다.")


# ───────────────────────────────────────────────────────────────
# 개념 3. reshape vs permute(transpose): 절대 헷갈리지 말 것
# ───────────────────────────────────────────────────────────────
# reshape: "데이터 순서 그대로, 모양만 다르게 본다"
#          - 개수만 맞으면 됨 (총 원소 수 동일)
#          - 메모리 안에서 값의 순서는 그대로
# permute/transpose: "축을 바꾼다"
#          - 개수는 같지만 값의 배치가 달라짐
#          - (C,H,W) ↔ (H,W,C) 같은 변환에 씀

print("\n" + "=" * 60)
print("개념 3: reshape vs permute — 초보자 가장 자주 실수하는 부분")
print("=" * 60)

a = np.arange(12).reshape(3, 4)   # 3x4 행렬, 값은 0..11
print("원본 (3,4):")
print(a)

r = a.reshape(2, 6)
print("\na.reshape(2,6) — 값 순서 그대로 재배치:")
print(r)

t = a.transpose(1, 0)              # == a.T
print("\na.transpose(1,0) — 축 교환 (행↔열):")
print(t)

# 같은 숫자 개수지만 의미가 완전히 다르다는 것이 핵심!
# 실수 주의: 3채널 이미지 (3,224,224)를 그냥 reshape(224,224,3)하면 **깨진다**.
#           반드시 .transpose(1,2,0) 또는 .permute(1,2,0)을 써야 한다.

bad = img.reshape(4, 5, 3)        # 값 순서를 바꿔버림 (잘못된 변환)
good = img.transpose(1, 2, 0)      # (C,H,W) → (H,W,C) 정석
print(f"\n이미지(C,H,W)={img.shape}")
print(f"  잘못된: reshape(H,W,C)={bad.shape}    첫 픽셀 값들 비교:")
print(f"    원본 img[0,0,0]   = {img[0,0,0]:.3f}")
print(f"    bad[0,0,0]        = {bad[0,0,0]:.3f}  (원본 첫 픽셀 값과 다를 수 있음)")
print(f"  정석:   transpose(1,2,0)={good.shape}   첫 픽셀 값들 비교:")
print(f"    good[0,0,0]       = {good[0,0,0]:.3f}  == img[0,0,0]? {np.isclose(good[0,0,0], img[0,0,0])}")


# ───────────────────────────────────────────────────────────────
# 개념 4. FOOTPASS TAAD에서 실제로 일어나는 shape 변환
# ───────────────────────────────────────────────────────────────
# 원본 forward() 내부 (줄 번호는 model_TAAD_baseline.py 기준):
#   line 36: x, roi, mask = in_x
#   line 37: b,c,l,h,w = x.shape      # B, C=3, T=L, H=352, W=640
#   ...
#   line 54: x = x.permute(0,2,1,3,4).reshape(-1,192,fh,fw)   # <-- 이게 오늘 배운 것
#   line 56: _,M,_,_ = roi.shape       # B*M*T 형태로 펼치려고 shape 분해
#
# 즉 "시간 축을 배치처럼 펼쳐서 2D conv를 T번 동시에" 하는 트릭이다.
# 처음엔 충격이지만 이 한 줄이 3D 모델 코드의 90%를 설명한다.

print("\n" + "=" * 60)
print("개념 4: FOOTPASS의 실제 trick — 시간 차원을 배치로 펼치기")
print("=" * 60)

# 가상의 feature: (B=2, C=192, T=10, H=44, W=80)
feat = np.random.rand(2, 192, 10, 44, 80)
print(f"입력 feature      shape={feat.shape}   의미: (B, C, T, H, W)")

# Step 1: permute로 T를 B 뒤로 이동
step1 = feat.transpose(0, 2, 1, 3, 4)
print(f"permute(0,2,1,3,4) shape={step1.shape}   의미: (B, T, C, H, W)")

# Step 2: reshape로 B와 T를 합침 (-1은 '남은 거 알아서')
step2 = step1.reshape(-1, 192, 44, 80)
print(f"reshape(-1,C,H,W) shape={step2.shape}   의미: (B*T, C, H, W) — 2D 배치로 바뀜!")
print(f"이제 이걸 2D Conv에 넣으면 T번의 프레임을 한번에 처리하는 셈.")


# ───────────────────────────────────────────────────────────────
# 연습 문제 (정답을 보지 말고 스스로 풀어보기)
# ───────────────────────────────────────────────────────────────
# Q1. shape (4, 3, 224, 224)는 무엇을 의미하나?
# Q2. 만약 채널을 마지막으로 보내려면? (답: .transpose(0,2,3,1) → (4,224,224,3))
# Q3. FOOTPASS의 mask가 (B, M, T)인데 이를 (B*M, 1, T)로 만들려면?
#     (답: mask.reshape(B*M, T).reshape(B*M, 1, T))  ← FOOTPASS line 65

print("\n" + "=" * 60)
print("연습 문제 Q3: mask (B=2, M=3, T=10) → (B*M, 1, T)")
print("=" * 60)
mask = np.random.randint(0, 2, size=(2, 3, 10))
print(f"원본 mask shape = {mask.shape}")
answer = mask.reshape(2 * 3, 10)[:, np.newaxis, :]   # (B*M, 1, T)
print(f"정답 shape    = {answer.shape}  <-- FOOTPASS line 65의 처리와 동일")


print("\n✅ Tutorial 01 완료. 다음: 02_image_to_tensor.py")
