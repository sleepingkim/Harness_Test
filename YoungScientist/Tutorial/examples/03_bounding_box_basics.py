"""
Tutorial 03 — Bounding Box의 3가지 표현과 IoU

목표: 모든 객체 탐지/추적 코드의 기본 단위 "bbox"를 이해한다.
FOOTPASS의 HDF5 파일 안에 들어있는 ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT가
어떤 관례인지 파악하고, 직접 IoU를 계산해본다.

실행:
    python examples/03_bounding_box_basics.py
"""
from _common import setup_utf8; setup_utf8()

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "outputs"
OUT.mkdir(exist_ok=True)


# ───────────────────────────────────────────────────────────────
# 개념 1. BBox의 3가지 표현 — 혼동하면 모델이 통째로 망가진다
# ───────────────────────────────────────────────────────────────
# 같은 박스를 표현하는 방식이 최소 3가지.
#
#  (a) XYXY:    (x1, y1, x2, y2)       — 좌상단, 우하단. torchvision RoIAlign이 쓰는 형식.
#  (b) XYWH:    (x, y, w, h)           — 좌상단 + 너비/높이. FOOTPASS HDF5가 쓰는 형식.
#  (c) CXCYWH:  (cx, cy, w, h)         — 중심점 + 너비/높이. YOLO 출력 형식.
#
# 변환은 간단하지만 실수하면 bbox가 엉뚱한 곳을 가리킨다.

print("=" * 60)
print("개념 1: 같은 박스 → 3가지 표현")
print("=" * 60)

# 원본: 이미지 (100,80)에서 시작해 너비 60, 높이 120인 박스
xywh = np.array([100, 80, 60, 120])        # x, y, w, h
xyxy = np.array([100, 80, 160, 200])        # x1, y1, x2, y2
cxcywh = np.array([130, 140, 60, 120])       # cx, cy, w, h

print(f"XYWH  (FOOTPASS 포맷):       {xywh.tolist()}  의미: 좌상단(100,80), 크기 60x120")
print(f"XYXY  (torchvision 포맷):    {xyxy.tolist()}  의미: 좌상단(100,80), 우하단(160,200)")
print(f"CXCYWH (YOLO 포맷):           {cxcywh.tolist()}  의미: 중심(130,140), 크기 60x120")


# ───────────────────────────────────────────────────────────────
# 개념 2. 변환 함수 — 직접 작성해보자
# ───────────────────────────────────────────────────────────────
def xywh_to_xyxy(box):
    x, y, w, h = box
    return np.array([x, y, x + w, y + h])


def xyxy_to_xywh(box):
    x1, y1, x2, y2 = box
    return np.array([x1, y1, x2 - x1, y2 - y1])


def xyxy_to_cxcywh(box):
    x1, y1, x2, y2 = box
    return np.array([(x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1])


print("\n" + "=" * 60)
print("개념 2: 변환 함수 검증")
print("=" * 60)
print(f"xywh → xyxy:   {xywh_to_xyxy(xywh).tolist()}  (기대: {xyxy.tolist()})")
print(f"xyxy → xywh:   {xyxy_to_xywh(xyxy).tolist()}  (기대: {xywh.tolist()})")
print(f"xyxy → cxcywh: {xyxy_to_cxcywh(xyxy).tolist()}  (기대: {cxcywh.tolist()})")


# ───────────────────────────────────────────────────────────────
# 개념 3. IoU (Intersection over Union)
# ───────────────────────────────────────────────────────────────
# "두 박스가 얼마나 겹치나?"를 [0,1] 숫자로 나타낸다.
#
#   IoU = 교집합 면적 / 합집합 면적
#
# 해석:
#   IoU = 0    → 전혀 겹치지 않음
#   IoU = 0.5  → 절반 겹침 (객체 탐지에서 '맞힌 것'으로 치는 경계선)
#   IoU = 1.0  → 완전히 일치
#
# FOOTPASS에선 직접 쓰진 않지만, 모든 tracker(SORT, ByteTrack)의 핵심.

def iou_xyxy(a, b):
    """두 박스의 IoU — xyxy 포맷 기준."""
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    # 교집합 박스
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw = max(0, ix2 - ix1)
    ih = max(0, iy2 - iy1)
    inter = iw * ih
    # 합집합
    a_area = (ax2 - ax1) * (ay2 - ay1)
    b_area = (bx2 - bx1) * (by2 - by1)
    union = a_area + b_area - inter
    return inter / union if union > 0 else 0.0


print("\n" + "=" * 60)
print("개념 3: IoU 계산 예시")
print("=" * 60)

box1 = np.array([100, 100, 200, 200])   # 100x100 박스
box2 = np.array([150, 150, 250, 250])   # 50 픽셀씩 오른쪽/아래 이동
box3 = np.array([300, 300, 400, 400])   # 겹치지 않음
box4 = np.array([100, 100, 200, 200])   # 완전 일치

for name, b in [("절반 겹침", box2), ("겹치지 않음", box3), ("완전 일치", box4)]:
    v = iou_xyxy(box1, b)
    print(f"  IoU(box1, {name:12s}) = {v:.4f}  (box = {b.tolist()})")


# ───────────────────────────────────────────────────────────────
# 시각화
# ───────────────────────────────────────────────────────────────
def draw_boxes_and_iou():
    img = Image.new("RGB", (500, 300), color=(40, 40, 40))
    d = ImageDraw.Draw(img)
    # 여러 박스 쌍을 그리고 IoU를 표시
    pairs = [
        ("절반 겹침", (30, 30, 130, 130), (80, 60, 180, 160)),
        ("많이 겹침", (220, 30, 320, 130), (235, 45, 335, 145)),
        ("안 겹침",   (30, 170, 130, 270), (200, 170, 300, 270)),
    ]
    colors = [(255, 100, 100), (100, 255, 100)]
    for title, a, b in pairs:
        # 원본 a, b: xyxy
        iou = iou_xyxy(np.array(a), np.array(b))
        d.rectangle(a, outline=colors[0], width=3)
        d.rectangle(b, outline=colors[1], width=3)
        cx = (a[0] + b[2]) // 2
        cy = max(a[1], b[1]) - 8
        d.text((a[0], a[1] - 14), f"{title}: IoU={iou:.2f}",
               fill=(255, 255, 255))
    out = OUT / "03_iou_visualization.png"
    img.save(out)
    return out

out = draw_boxes_and_iou()
print(f"\n시각화 저장: {out}")


# ───────────────────────────────────────────────────────────────
# 개념 4. FOOTPASS의 실제 bbox 처리 — 스케일 조정
# ───────────────────────────────────────────────────────────────
# FOOTPASS-main/utils/TAAD_Dataset.py line 271~278:
#
#   tlx = int(max(min(1920, bbox[0,ROI_X] - (coeff-1)*bbox[0,ROI_WIDTH]//2), 0) / 3)
#   tly = int(max(min(1080, bbox[0,ROI_Y] - (coeff-1)*bbox[0,ROI_HEIGHT]//2), 0) / 3.068)
#   brx = int(max(min(1920, bbox[0,ROI_X] + coeff*bbox[0,ROI_WIDTH]), 0) / 3)
#   bry = int(max(min(1080, bbox[0,ROI_Y] + coeff*bbox[0,ROI_HEIGHT]), 0) / 3.068)
#
# 해설:
#   - 원본 비디오는 1920x1080(Full HD). 모델 입력은 640x352.
#   - 1920/640 = 3,   1080/352 ≈ 3.068
#   → 따라서 픽셀 좌표를 /3, /3.068로 나눠 축소
#   - coeff=1.125 는 박스를 12.5% 확장 (선수 주변 컨텍스트 포함)
#   - xywh → xyxy 변환도 같이 이루어짐
#
# 이 한 줄에 세 가지가 얽혀 있다: 표현 변환, 스케일 조정, 확장 padding.

print("\n" + "=" * 60)
print("개념 4: FOOTPASS의 ROI 스케일 조정 흉내내기")
print("=" * 60)

def footpass_roi_convert(roi_xywh, coeff=1.125, src=(1920, 1080), dst=(640, 352)):
    """FOOTPASS Dataset의 ROI 변환을 간단히 재현."""
    x, y, w, h = roi_xywh
    sx, sy = src[0] / dst[0], src[1] / dst[1]

    tlx = max(min(src[0], x - (coeff - 1) * w / 2), 0) / sx
    tly = max(min(src[1], y - (coeff - 1) * h / 2), 0) / sy
    brx = max(min(src[0], x + coeff * w), 0) / sx
    bry = max(min(src[1], y + coeff * h), 0) / sy

    return np.array([tlx, tly, brx, bry])  # xyxy in model input space


original_roi = np.array([800, 500, 60, 120])   # FullHD XYWH
converted = footpass_roi_convert(original_roi)
print(f"원본 ROI (FullHD, XYWH):    {original_roi.tolist()}")
print(f"변환 후 ROI (640x352, XYXY): {converted.round(1).tolist()}")
print(f"축 변환: 1920/640 = 3,  1080/352 ≈ 3.068")
print(f"이렇게 모델 입력 공간으로 내려온 xyxy 좌표가 roi_align의 입력이 된다.")


print("\n✅ Tutorial 03 완료. 다음: 04_roi_align_from_scratch.py")
