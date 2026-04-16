"""
Tutorial 05 — Binary Mask vs Continuous/Soft Mask

목표: 우리 연구(AmoUni-SoccerTrack)의 **핵심 변경점**을 손으로 체험한다.
FOOTPASS TAAD는 binary mask(0/1)로 선수의 feature를 gating한다.
우리는 이걸 continuous [0,1] + uncertainty로 바꿔서 부분 가림 상황을
더 잘 다루려 한다. 이 튜토리얼은 그 차이를 숫자와 그림으로 보여준다.

실행:
    python examples/05_binary_vs_soft_mask.py
"""
from _common import setup_utf8; setup_utf8()

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "outputs"
OUT.mkdir(exist_ok=True)


# ───────────────────────────────────────────────────────────────
# 상황 설정
# ───────────────────────────────────────────────────────────────
# 한 선수가 T=20 프레임 동안 등장. 중간에 다른 선수에게 가려짐.
# 각 프레임에서 "선수가 실제로 얼마나 보이는가"를 visibility로 둔다.

T = 20
np.random.seed(42)

true_visibility = np.array([
    1.0, 1.0, 1.0, 0.9, 0.7,    # 프레임 0~4: 완전히 보임 → 약간 가림 시작
    0.4, 0.2, 0.0, 0.0, 0.1,    # 프레임 5~9: 심한 가림 구간
    0.3, 0.6, 0.8, 0.95, 1.0,   # 프레임 10~14: 점점 다시 보임
    1.0, 1.0, 1.0, 1.0, 1.0,    # 프레임 15~19: 완전 가시
])
assert len(true_visibility) == T

# 실제 FOOTPASS의 binary mask는 "bbox 기록이 존재하면 1, 없으면 0"
# 가시성 0.2 이상이면 tracker가 기록을 남겼다고 가정하고 binary로 만든다.
binary_mask = (true_visibility > 0.2).astype(np.float32)

# 우리 amodal head는 continuous visibility를 직접 추정 + uncertainty도 추정
# 여기선 간단히 "true_visibility + 약간의 노이즈"를 '예측값'으로 가정
pred_visibility = np.clip(
    true_visibility + np.random.normal(0, 0.08, T), 0, 1).astype(np.float32)
# uncertainty는 "true와 pred의 차이"에 비례하도록 흉내 (실제론 모델이 직접 출력)
uncertainty = np.clip(np.abs(true_visibility - pred_visibility) * 2, 0, 1)

# 우리 soft mask = visibility × (1 - uncertainty)
soft_mask = pred_visibility * (1 - uncertainty)

print("=" * 78)
print("프레임별 상태 (T=20)")
print("=" * 78)
print(f"{'frame':>5} | {'true_vis':>8} | {'binary':>7} | {'pred_vis':>8} | {'unc':>5} | {'soft':>5}")
print("-" * 78)
for t in range(T):
    print(f"{t:5d} | {true_visibility[t]:8.2f} | {binary_mask[t]:7.1f} | "
          f"{pred_visibility[t]:8.2f} | {uncertainty[t]:5.2f} | {soft_mask[t]:5.2f}")


# ───────────────────────────────────────────────────────────────
# 개념 1. FOOTPASS의 gating 연산 — binary 버전
# ───────────────────────────────────────────────────────────────
# FOOTPASS line 65:  x = x * mask   (mask ∈ {0,1})
#
# 해석:
#   mask=1 → 그 프레임의 feature를 '그대로' 써라
#   mask=0 → 그 프레임의 feature를 '완전히 무시'해라
#
# 문제: 가림이 0.7 수준이면 binary로는 "보인다(1)"로 처리돼서, 모델이
#       일부만 보이는 불완전한 feature를 온전한 것으로 착각할 수 있다.

print("\n" + "=" * 60)
print("개념 1: binary gating 시뮬레이션")
print("=" * 60)

# 가짜 feature: 각 프레임의 feature 강도 (실제로는 192차원이지만 스칼라로 단순화)
feature_strength = np.random.uniform(0.5, 1.0, T).astype(np.float32)

binary_gated = feature_strength * binary_mask
print("binary gating 후:")
for t in [4, 5, 6, 7, 10, 11]:
    status = "✅ 보존" if binary_mask[t] > 0 else "❌ 제거"
    print(f"  frame {t:2d}: feat={feature_strength[t]:.2f} × mask={binary_mask[t]:.1f}"
          f" = {binary_gated[t]:.2f}  ({status})")


# ───────────────────────────────────────────────────────────────
# 개념 2. AmoUni-SoccerTrack의 gating — soft 버전
# ───────────────────────────────────────────────────────────────
# 우리: x = x * soft_mask    (soft ∈ [0,1])
#
# soft=0.3 → feature를 30%만 반영. "부분적으로 신뢰한다".
# 추가로 uncertainty가 크면 다시 깎는다.

print("\n" + "=" * 60)
print("개념 2: soft gating 시뮬레이션 (AmoUni)")
print("=" * 60)

soft_gated = feature_strength * soft_mask
print("soft gating 후:")
for t in [4, 5, 6, 7, 10, 11]:
    loss_pct = 100 * (1 - soft_mask[t])
    print(f"  frame {t:2d}: feat={feature_strength[t]:.2f} × soft={soft_mask[t]:.2f}"
          f" = {soft_gated[t]:.2f}  (해석: {loss_pct:.0f}% 감쇠)")


# ───────────────────────────────────────────────────────────────
# 개념 3. 차이가 모델 출력에 어떻게 영향을 주나?
# ───────────────────────────────────────────────────────────────
# TAAD는 시간 축으로 Conv1D를 돌린다. 즉 (mask gated feature) 시퀀스를
# 1차원 temporal conv에 넣어 "이 선수가 지금 Pass하려 하는가?"를 판단.
# 가림 구간에서 binary는 갑자기 feature를 0으로 만들어 '경계 아티팩트'를
# 유발할 수 있다. soft는 부드럽게 감쇠 → conv kernel이 더 자연스럽게 학습.
#
# 아래는 간단한 3-tap 평균 필터로 temporal smoothing을 흉내.

def temporal_smooth(x, k=3):
    kernel = np.ones(k) / k
    return np.convolve(x, kernel, mode="same")

binary_smoothed = temporal_smooth(binary_gated)
soft_smoothed = temporal_smooth(soft_gated)


# ───────────────────────────────────────────────────────────────
# 시각화
# ───────────────────────────────────────────────────────────────
fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)

frames = np.arange(T)
ax = axes[0]
ax.plot(frames, true_visibility, "o-", color="black", label="true visibility")
ax.step(frames, binary_mask, where="mid", color="red", label="binary mask (FOOTPASS)")
ax.plot(frames, soft_mask, "s-", color="green", label="soft mask (AmoUni = vis × (1-unc))")
ax.fill_between(frames, pred_visibility - uncertainty, pred_visibility + uncertainty,
                 alpha=0.2, color="green", label="±uncertainty")
ax.set_ylabel("mask value")
ax.set_ylim(-0.1, 1.2)
ax.set_title("Frame-by-frame visibility: binary vs soft")
ax.legend()
ax.grid(alpha=0.3)

ax = axes[1]
ax.bar(frames - 0.15, binary_gated, width=0.3, color="red", alpha=0.7,
       label="binary-gated feature")
ax.bar(frames + 0.15, soft_gated, width=0.3, color="green", alpha=0.7,
       label="soft-gated feature")
ax.plot(frames, feature_strength, "o-", color="black", alpha=0.4,
         label="raw feature strength")
ax.set_ylabel("gated feature value")
ax.set_title("Gating 후 feature: 가림 구간(5~9)에서 binary는 0, soft는 점진적 감쇠")
ax.legend()
ax.grid(alpha=0.3)

ax = axes[2]
ax.plot(frames, binary_smoothed, "-", color="red",
         label="binary after temporal smoothing (3-tap)")
ax.plot(frames, soft_smoothed, "-", color="green",
         label="soft after temporal smoothing")
ax.set_xlabel("frame")
ax.set_ylabel("smoothed feature")
ax.set_title("Temporal conv(1D) 흉내: soft가 더 '부드러운' 신호를 유지")
ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()
out_png = OUT / "05_binary_vs_soft_mask.png"
plt.savefig(out_png, dpi=100)
plt.close(fig)
print(f"\n시각화 저장: {out_png}")


# ───────────────────────────────────────────────────────────────
# 핵심 요약
# ───────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("★ 핵심 요약")
print("=" * 60)
print("""
1. FOOTPASS TAAD의 mask는 {0,1}. 가림 구간을 통째로 0 처리 → 정보 손실.
2. 우리 amodal head는 continuous visibility와 uncertainty를 출력.
3. soft_mask = visibility × (1 - uncertainty) 로 gating.
4. Temporal conv 입장에서 soft signal이 더 부드러워 학습에 유리.

FOOTPASS-ext/amoni_soccer/extended_taad.py 의 `_compute_soft_mask` 함수가
정확히 이 계산을 한다. 실제 코드와 이 튜토리얼을 번갈아 보면 머리에 박힐
것이다.
""")

print("✅ Tutorial 05 완료. 다음: 06_simple_iou_tracker.py")
