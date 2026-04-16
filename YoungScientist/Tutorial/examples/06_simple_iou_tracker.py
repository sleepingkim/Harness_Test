"""
Tutorial 06 — 최소 MOT (Multi-Object Tracking) 직접 구현

목표: 'tracking-by-detection'이라는 표준 패러다임을 손으로 만든다.
SORT/ByteTrack/OC-SORT 같은 SOTA tracker도 본질은 이 세 단계이다:
    (1) Predict   — 이전 위치에서 다음 위치 예측 (Kalman filter)
    (2) Match     — 예측과 새 detection을 bbox로 매칭 (Hungarian)
    (3) Update    — 매칭된 건 update, 안 된 건 새 track 시작 / 죽음

이 튜토리얼은 그 중에서도 **가장 간단한 IoU 매칭 tracker**를 30줄 이내로
만든다. 실제 FOOTPASS의 tracklet은 이미 주어진 것이지만, 이 개념이 있어야
"가림 시 ID switch" 문제의 본질을 안다.

실행:
    python examples/06_simple_iou_tracker.py
"""
from _common import setup_utf8; setup_utf8()

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "outputs"
OUT.mkdir(exist_ok=True)


# ───────────────────────────────────────────────────────────────
# 가짜 시나리오: 선수 2명이 화면을 가로지르며 3 프레임 이동
# ───────────────────────────────────────────────────────────────
# 각 프레임에 detector가 bbox를 몇 개 뱉어준다고 가정. 우리 일은 "같은
# 선수의 박스를 프레임 간 연결해 ID를 붙이는 것".

def iou_xyxy(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    a_area = (ax2 - ax1) * (ay2 - ay1)
    b_area = (bx2 - bx1) * (by2 - by1)
    u = a_area + b_area - inter
    return inter / u if u > 0 else 0.0


# 프레임별 detection (xyxy)
# Frame 0: 선수 A, B 멀리 떨어져 있음
# Frame 1: 살짝 이동
# Frame 2: B가 A에게 접근 (겹치기 직전)
# Frame 3: 겹쳐서 한 박스로만 탐지됨 (가림!) ← 여기서 ID 혼동 위험
# Frame 4: 분리됐지만 누가 누군지 애매
detections_per_frame = [
    [(50, 50, 90, 130), (200, 60, 240, 140)],          # frame 0: 2 detections
    [(55, 55, 95, 135), (180, 62, 220, 142)],          # frame 1
    [(60, 60, 100, 140), (140, 64, 180, 144)],         # frame 2
    [(100, 62, 160, 142)],                              # frame 3: 가림으로 한 개
    [(95, 65, 135, 145), (155, 65, 195, 145)],          # frame 4: 다시 분리
]


# ───────────────────────────────────────────────────────────────
# 간단한 IoU-only tracker (SORT의 핵심만 추출)
# ───────────────────────────────────────────────────────────────
class SimpleTracker:
    """IoU 매칭만 쓰는 최소 tracker.

    - Kalman 예측은 생략하고 '지난 프레임의 bbox 자체'를 다음 예측으로 사용
      (실제 SORT는 constant-velocity Kalman으로 더 정확)
    - Hungarian 대신 greedy 매칭 (가장 IoU 높은 쌍부터 차례로)
    - 매칭 실패한 detection은 새 ID로 시작
    - 매칭 실패한 track은 max_age 프레임 동안 살아있다가 죽음
    """

    def __init__(self, iou_threshold=0.3, max_age=2):
        self.iou_th = iou_threshold
        self.max_age = max_age
        self.tracks = {}       # id → {'bbox': xyxy, 'age_since_seen': int}
        self._next_id = 1
        self.history = []       # 프레임별 (id, bbox) 기록 (시각화용)

    def _new_id(self):
        i = self._next_id
        self._next_id += 1
        return i

    def update(self, detections):
        # 1) 매칭: 모든 (track, detection) 쌍의 IoU 계산
        unmatched_dets = set(range(len(detections)))
        matches = []
        # IoU 내림차순 greedy
        pairs = []
        for tid, t in self.tracks.items():
            for di, d in enumerate(detections):
                pairs.append((iou_xyxy(t["bbox"], d), tid, di))
        pairs.sort(reverse=True)

        used_tids = set()
        for iou, tid, di in pairs:
            if iou < self.iou_th:
                break
            if tid in used_tids or di not in unmatched_dets:
                continue
            matches.append((tid, di))
            used_tids.add(tid)
            unmatched_dets.discard(di)

        # 2) Update matched tracks
        for tid, di in matches:
            self.tracks[tid]["bbox"] = detections[di]
            self.tracks[tid]["age_since_seen"] = 0

        # 3) Unmatched tracks: age up, delete if too old
        for tid in list(self.tracks.keys()):
            if tid not in used_tids:
                self.tracks[tid]["age_since_seen"] += 1
                if self.tracks[tid]["age_since_seen"] > self.max_age:
                    del self.tracks[tid]

        # 4) Unmatched detections → new tracks
        for di in unmatched_dets:
            new_id = self._new_id()
            self.tracks[new_id] = {"bbox": detections[di], "age_since_seen": 0}

        # 현재 프레임의 결과 반환
        return {tid: info["bbox"] for tid, info in self.tracks.items()
                if info["age_since_seen"] == 0}


# ───────────────────────────────────────────────────────────────
# 실행
# ───────────────────────────────────────────────────────────────
tracker = SimpleTracker(iou_threshold=0.3, max_age=2)

print("=" * 60)
print("SimpleTracker 동작 로그")
print("=" * 60)
all_results = []
for t, dets in enumerate(detections_per_frame):
    active = tracker.update(dets)
    all_results.append(active)
    print(f"\nFrame {t}: {len(dets)} detections")
    for i, d in enumerate(dets):
        print(f"  det[{i}] = {d}")
    for tid, bb in active.items():
        print(f"  ▶ track #{tid}: {bb}")


# ───────────────────────────────────────────────────────────────
# 관찰 포인트: 가림이 발생한 Frame 3 → Frame 4 전이
# ───────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("관찰: Frame 3 → Frame 4 (가림으로 detection 개수 변화)")
print("=" * 60)
print("""
Frame 2: 두 track (#1, #2)이 살아있음.
Frame 3: detection이 1개 → 하나는 매칭되지만 나머지는 '미매칭 track'으로
         max_age 카운트가 올라간다.
Frame 4: detection 2개가 다시 등장.
         - 살아있는 두 track과 매칭을 시도.
         - IoU가 기준 이하면? 새 ID가 발급된다 = **ID SWITCH 발생!**

이것이 가림 상황의 고질적 문제다. OC-SORT의 'observation-centric re-update',
ByteTrack의 'low-score box 부활' 등은 모두 이 구간을 구제하려는 설계이다.
AmoUni-SoccerTrack의 amodal perception은 **가림 구간에서도 feature를 유지**
함으로써 appearance cue로 재매칭을 돕는 방향의 해법이다.
""")


# ───────────────────────────────────────────────────────────────
# 시각화: 프레임별 박스 & ID
# ───────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, len(detections_per_frame),
                         figsize=(4 * len(detections_per_frame), 4),
                         sharey=True)
colors = {1: "red", 2: "blue", 3: "orange", 4: "purple", 5: "cyan"}
for ax, (t, (dets, tracks)) in zip(
    axes, enumerate(zip(detections_per_frame, all_results))
):
    ax.set_xlim(0, 300)
    ax.set_ylim(200, 0)
    ax.set_facecolor("#f5f5f5")
    for d in dets:
        x1, y1, x2, y2 = d
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1],
                color="gray", lw=1, linestyle=":")
    for tid, bb in tracks.items():
        x1, y1, x2, y2 = bb
        c = colors.get(tid, "black")
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1],
                color=c, lw=2)
        ax.text(x1, y1 - 3, f"#{tid}", color=c, fontsize=12,
                fontweight="bold")
    ax.set_title(f"Frame {t}")
    ax.set_xticks([])
    ax.set_yticks([])

fig.suptitle("IoU tracker: 회색 점선=detection, 색=track ID")
fig.tight_layout()
out_png = OUT / "06_simple_tracker.png"
plt.savefig(out_png, dpi=100)
plt.close(fig)
print(f"시각화 저장: {out_png}")


# ───────────────────────────────────────────────────────────────
# 우리 연구와의 연결
# ───────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("★ 연구 설계서와의 연결")
print("=" * 60)
print("""
SimpleTracker의 3단계 (Predict / Match / Update)는 문헌 조사에서 나온 모든
tracker의 '뼈대'이다:

  - P2-1 SORT       : Predict를 Kalman Filter로 정교화
  - P2-2 DeepSORT   : Match에 appearance feature 추가
  - P2-3 ByteTrack  : Match 단계에서 low-score detection까지 재시도
  - P2-5 OC-SORT    : 가림 구간에 대해 Predict를 관측 기반으로 재조정
  - P2-11 OATrack   : Predict에서 occlusion rate에 따라 Kalman gain 조정

우리 AmoUni-SoccerTrack은 Match 단계에 amodal-derived visibility와
uncertainty를 주입한다 (조합 3 파이프라인). 이 튜토리얼에서 IoU만 쓰는
SimpleTracker가 Frame 3~4에서 ID switch를 낸 것처럼, FOOTPASS의 tracklet도
가림 구간에서 같은 실패를 한다 — 그래서 본 연구가 의미 있는 것이다.
""")

print("✅ Tutorial 06 완료. 다음: 07_footpass_taad_walkthrough.py")
