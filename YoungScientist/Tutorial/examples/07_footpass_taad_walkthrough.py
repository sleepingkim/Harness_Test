"""
Tutorial 07 — FOOTPASS TAAD의 forward를 한 줄 한 줄 따라가기

목표: 이 튜토리얼에서 우리는 FOOTPASS-main/models/model_TAAD_baseline.py의
70줄짜리 forward 함수를 **시뮬레이션**한다. 실제 PyTorch / X3D 없이도 각
텐서의 shape과 의미를 확인할 수 있도록, 각 단계를 numpy로 재현했다.

이게 가능한 이유: CNN의 본질은 "shape 변환의 연쇄"이기 때문이다.
실제 수치는 달라도 shape은 결정적이다. shape만 쫓으면 모델이 한눈에 보인다.

실행:
    python examples/07_footpass_taad_walkthrough.py

실제 forward pass 검증은 PyTorch 환경에서:
    python -m tests.test_forward    (FOOTPASS-ext/tests/)
"""
from _common import setup_utf8; setup_utf8()

import numpy as np


# ───────────────────────────────────────────────────────────────
# 입력 정의 — FOOTPASS TAAD의 forward( (x, roi, mask) )
# ───────────────────────────────────────────────────────────────
# FOOTPASS-main/models/model_TAAD_baseline.py line 12~15 주석:
#   Inputs : sequences of T frames, M sequences of ROIs, M sequences of masks
#       [(B,3,T,352,640), (B,M,T,5), (B,M,T)]

B = 2       # batch size
T = 50      # clip length (FOOTPASS 기본값)
M = 5       # number of tracklets per sample (nb_tracklets + 1 = 4+1)
C = 3
H, W = 352, 640

print("=" * 70)
print("INPUT tensors (FOOTPASS TAAD baseline)")
print("=" * 70)

x = np.random.randn(B, C, T, H, W).astype(np.float32)
roi = np.random.randn(B, M, T, 5).astype(np.float32)
mask = np.random.randint(0, 2, size=(B, M, T)).astype(np.float32)
print(f"x:    {x.shape}   ← (B, C={C}, T, H, W)  normalized video clip")
print(f"roi:  {roi.shape} ← (B, M, T, 5)  [frame_idx, x1, y1, x2, y2]")
print(f"mask: {mask.shape} ← (B, M, T)    binary visibility")


# ───────────────────────────────────────────────────────────────
# STEP 1. X3D backbone — feature map 축소
# ───────────────────────────────────────────────────────────────
# 원본 코드:
#   line 39:  w = self.x3d_L4(x)              # (B, 48, T, 88, 160)
#   line 40:  z = self.x3d.blocks[2](w)       # (B, 48, T, 44, 80)
#   line 41:  y = self.x3d.blocks[3](z)       # (B, 96, T, 22, 40)
#   line 42:  x = self.x3d.blocks[4](y)       # (B, 192, T, 11, 20)
#
# 왜 점점 작아지나? 각 block에 stride=2 conv가 있어서 공간 해상도가 절반씩
# 준다. 대신 채널 수는 점점 늘어나 복잡한 패턴을 포착.

print("\n" + "=" * 70)
print("STEP 1: X3D backbone — 공간 해상도는 작아지고 채널은 늘어남")
print("=" * 70)

def fake_conv3d(x_shape, new_c, stride=(1, 2, 2)):
    """stride를 반영한 가짜 3D conv. shape만 변환."""
    b, c, t, h, w = x_shape
    sh, sw = stride[1], stride[2]
    st = stride[0]
    return (b, new_c, t // st, h // sh, w // sw)

shape = x.shape
print(f"x 입력:                      {shape}")

# Layer 1~2 (x3d_L4): stride 유지하며 채널 변환
shape = fake_conv3d(shape, 48, stride=(1, 4, 4))   # 실제로는 stem+layer1 두 단계 합쳐 1/4
print(f"x3d_L4 (stem+layer1):        {shape}   ← 공간 1/4, 채널 48")

shape = fake_conv3d(shape, 48, stride=(1, 2, 2))
print(f"x3d.blocks[2]:               {shape}   ← 공간 추가 1/2, 채널 48")
z_shape = shape

shape = fake_conv3d(shape, 96, stride=(1, 2, 2))
print(f"x3d.blocks[3]:               {shape}   ← 공간 1/2, 채널 96")
y_shape = shape

shape = fake_conv3d(shape, 192, stride=(1, 2, 2))
print(f"x3d.blocks[4]:               {shape}   ← 공간 1/2, 채널 192")


# ───────────────────────────────────────────────────────────────
# STEP 2. FPN-style upsample + concat — multi-scale fusion
# ───────────────────────────────────────────────────────────────
# 원본 코드 line 43~50:
#   x = self.up_L32(x)                 # upsample 2x
#   x = torch.concat((x,y), dim=1)     # skip connection
#   x = self.conv_L16_32(x)            # channel reduction
#   ...
#
# 효과: 작지만 의미가 깊은 feature를 다시 키워서 중간 스케일 feature(y,z)와
# 섞는다. 탐지/인식에서 '작은 객체와 큰 객체를 동시에' 보기 위한 표준 트릭.
# (FPN = Feature Pyramid Network)

print("\n" + "=" * 70)
print("STEP 2: Upsample + concat — 스케일 피라미드 fusion")
print("=" * 70)

b, c, t, h, w = shape
shape = (b, c, t, h * 2, w * 2)
print(f"up_L32 (2x upsample):       {shape}   ← 공간 2x, 채널 유지")
# concat with y (same spatial size now)
shape = (b, c + y_shape[1], t, shape[3], shape[4])
print(f"concat with y:              {shape}   ← 채널 192+96=288")
shape = (b, 192, t, shape[3], shape[4])
print(f"conv_L16_32 (채널 축소):     {shape}   ← 192로 복원")

shape = (b, 192, t, shape[3] * 2, shape[4] * 2)
print(f"up_L16 (2x upsample):        {shape}   ← 공간 다시 2x")
shape = (b, 192 + z_shape[1], t, shape[3], shape[4])
print(f"concat with z:              {shape}   ← 채널 192+48=240")
shape = (b, 192, t, shape[3], shape[4])
print(f"conv_L8_16 (채널 축소):      {shape}   ← 최종 (B, 192, T, 44, 80)")


# ───────────────────────────────────────────────────────────────
# STEP 3. permute + reshape — 시간 축을 배치로 펼치기
# ───────────────────────────────────────────────────────────────
# 원본 line 52~54:
#   _,_,_,fh,fw = x.shape
#   x = x.permute(0,2,1,3,4).reshape(-1,192,fh,fw)   # (B*T, 192, 44, 80)
#
# 이 한 줄은 Tutorial 01에서 배운 그 트릭이다. 이후 단계(RoIAlign)는 2D
# 연산이므로 시간 축을 배치처럼 펼쳐야 한다.

print("\n" + "=" * 70)
print("STEP 3: permute+reshape — (B, 192, T, 44, 80) → (B*T, 192, 44, 80)")
print("=" * 70)
BT = B * T
shape = (BT, 192, 44, 80)
print(f"결과 shape: {shape}   ← 이제 일반 2D feature map처럼 다룰 수 있다")


# ───────────────────────────────────────────────────────────────
# STEP 4. RoIAlign — 각 선수 bbox 영역을 feature에서 잘라오기
# ───────────────────────────────────────────────────────────────
# 원본 line 55~63:
#   _,M,_,_ = roi.shape
#   roi = roi.permute(0,2,1,3).reshape(-1,5)          # (B*T*M, 5)
#   f_num = roi[:,0]
#   batch_indices = torch.arange(b).repeat_interleave(l * M)
#   adjusted_frame_numbers = f_num + batch_indices * l
#   roi[:,0] = adjusted_frame_numbers
#   x = roi_align(x, roi, (4,2), 0.125)               # (B*T*M, 192, 4, 2)
#
# 포인트:
#   - roi의 첫 칸 'frame_idx'는 어느 feature map에서 자를지 지정
#   - batch까지 고려해 frame_idx를 '전역 인덱스'로 보정
#   - spatial_scale=0.125 = feature가 이미지의 1/8 이므로 좌표도 1/8로

print("\n" + "=" * 70)
print("STEP 4: RoIAlign — 각 선수 bbox 영역 추출")
print("=" * 70)
BTM = BT * M
print(f"roi reshape:             ({BTM}, 5)   ← (B*T*M, 5)")
print(f"roi_align 입력 feat:      {shape}       (B*T, 192, 44, 80)")
print(f"roi_align 출력:           ({BTM}, 192, 4, 2)")
print(f"\n해석:")
print(f"  - 각 (batch b, frame t, tracklet m) 조합에 대해 4x2 feature 조각")
print(f"  - 이게 '그 선수가 그 프레임에서 무슨 feature를 가지나'의 표현")


# ───────────────────────────────────────────────────────────────
# STEP 5. avg pool + temporal conv — 시간 축 분석
# ───────────────────────────────────────────────────────────────
# 원본 line 64~66:
#   x = self.avgpool2D(x).squeeze(-1).squeeze(-1)   # (B*T*M, 192, 1, 1) → (B*T*M, 192)
#   x = x.reshape(b,l,M,192).permute(0,2,3,1).reshape(b*M,192,l)   # (B*M, 192, T)
#   x = x*(mask.reshape(b*M,l).unsqueeze(1))        # ★ 여기가 우리가 확장한 지점!
#   x = F.gelu(self.bn1(self.conv1(x)))              # (B*M, 512, T)
#
# 포인트:
#   - avg pool로 공간 정보를 하나의 벡터로 압축
#   - 다시 (B*M, 192, T)로 재배열해서 **시간 축을 인식**하는 1D temporal conv
#   - 그 중간에 mask gating!  ← 이 한 줄에서 우리 확장이 개입한다.

print("\n" + "=" * 70)
print("STEP 5: avg pool + mask gating + temporal conv")
print("=" * 70)
shape = (BTM, 192)
print(f"avgpool2D 후:            {shape}")
shape = (B * M, 192, T)
print(f"reshape (B*M, 192, T):   {shape}")
print(f"★ mask gating: x = x * mask.unsqueeze(1)")
print(f"   FOOTPASS 원본: mask ∈ {{0,1}}^({B},{M},{T})")
print(f"   AmoUni-Ext:   mask ∈ [0,1]^({B},{M},{T}) (amodal-derived soft)")
shape = (B * M, 512, T)
print(f"conv1 (192→512) 후:       {shape}")


# ───────────────────────────────────────────────────────────────
# STEP 6. FC + reshape — 최종 action logit
# ───────────────────────────────────────────────────────────────
# 원본 line 68~70:
#   x = self.fc1(x.permute(0,2,1))       # (B*M, T, 9)
#   return x.reshape(b,M,l,9).permute(0,3,1,2)  # (B, 9, M, T)
#
# 9 = 8 action classes + 1 background

print("\n" + "=" * 70)
print("STEP 6: FC + reshape — 최종 출력")
print("=" * 70)
shape = (B * M, T, 9)
print(f"fc1 후:                  {shape}")
shape = (B, 9, M, T)
print(f"최종 출력 (B, 9, M, T):   {shape}")
print(f"\n의미: 각 (batch, player, frame)마다 9개 class에 대한 logit")
print(f"      9 = {{Drive, Pass, Cross, Shot, Header, Throw-in, Tackle, Block, BG}}")


# ───────────────────────────────────────────────────────────────
# 전체 shape 흐름 요약
# ───────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("★ FOOTPASS TAAD forward 전체 shape flow 요약")
print("=" * 70)
flow = [
    ("입력 x",                       "(B, 3, T, 352, 640)",  "비디오 클립"),
    ("X3D backbone 최종",            "(B, 192, T, 44, 80)",  "공간 1/8, 채널 192"),
    ("permute+reshape",              "(B*T, 192, 44, 80)",   "2D 배치로 펼침"),
    ("RoIAlign",                      "(B*T*M, 192, 4, 2)",   "선수 bbox 영역"),
    ("avgpool + reshape",             "(B*M, 192, T)",        "선수별 시간 시퀀스"),
    ("★ mask gating (우리 확장 지점)", "(B*M, 192, T)",        "visibility 반영"),
    ("conv1D temporal",               "(B*M, 512, T)",        "시간 패턴 학습"),
    ("fc1",                           "(B*M, T, 9)",          "action class logit"),
    ("reshape+permute",               "(B, 9, M, T)",         "최종 출력"),
]
print(f"{'단계':<30}{'shape':<30}{'의미'}")
print("-" * 70)
for name, s, meaning in flow:
    print(f"{name:<30}{s:<30}{meaning}")


print("\n" + "=" * 70)
print("★ AmoUni-SoccerTrack의 확장 포인트")
print("=" * 70)
print("""
FOOTPASS-ext/amoni_soccer/extended_taad.py는 위 흐름을 **그대로** 재현하되
★ 표시된 mask gating 단계만 다음과 같이 바꾼다:

  원본:  x = x * mask_binary  (mask ∈ {0,1})
  확장:  soft = visibility * (1 - amodal_uncertainty)
         x = x * soft          (soft ∈ [0,1])

visibility와 amodal_uncertainty는 `amoni_soccer/amodal_head.py`의
SoccerAmodalHead가 RoIAlign 출력에서 바로 추정한다.
즉 우리가 확장한 forward는:

  X3D backbone → permute+reshape → RoIAlign
      → [Soccer-Amodal Head가 여기서 추가 계산] → avgpool → soft mask gating
      → conv1D → fc1 → 출력

이 튜토리얼을 이해했으면 이제 FOOTPASS-main/models/model_TAAD_baseline.py
(70줄)와 FOOTPASS-ext/amoni_soccer/extended_taad.py (200여 줄)를 나란히
띄워놓고 읽어보라. 전에는 추상적이던 모든 줄이 의미를 가질 것이다.
""")

print("✅ Tutorial 07 완료. 모든 튜토리얼 종료!")
print("\n이제 FOOTPASS-main/README.md 환경 조건을 갖추면 실제 모델을 돌릴 수 있다.")
