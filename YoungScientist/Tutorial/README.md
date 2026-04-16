# Tutorial — FOOTPASS/AmoUni-SoccerTrack 기술 학습 실습

**목적:** 이론은 알지만 구현이 익숙하지 않은 사람을 위한 점진적 학습 코드.
FOOTPASS와 `FOOTPASS-ext/amoni_soccer/*.py`에서 실제로 사용하는 기술들을 **작은 단위로 분해**해서 직접 손으로 만들어보고, 최종적으로 원본 코드로 돌아왔을 때 "아, 이게 그 뜻이구나" 하고 연결되도록 설계되었다.

## 학습 원칙

1. **작게 시작**: 한 파일 = 한 개념. 50줄 이하 유지.
2. **NumPy 우선**: PyTorch 설치 없이도 돌아가는 예제가 대부분. 이론과 shape의 흐름을 먼저 이해한 뒤 PyTorch로 옮긴다.
3. **shape 추적**: 모든 텐서에 주석으로 shape 표기. 데이터가 **어떤 모양으로 다음 모듈로 전달되는지**가 구현의 전부다.
4. **원본 연결**: 각 튜토리얼 끝에 "FOOTPASS에서는 어떻게 쓰이는가" 포인터가 있음.

## 학습 로드맵 (총 7개 예제)

| # | 파일 | 배울 것 | 연결되는 FOOTPASS 코드 |
|---|------|---------|----------------------|
| 01 | `01_tensors_and_shapes.py` | 텐서/배치/channel 개념, shape 변환(reshape, permute) | 모든 모듈 |
| 02 | `02_image_to_tensor.py` | 이미지 파일 → 텐서로 바꾸는 전 과정 | `TAAD_Dataset._get_clip` |
| 03 | `03_bounding_box_basics.py` | BBox 표현 3가지, IoU 계산 | `amodal_head.py`, FOOTPASS ROI |
| 04 | `04_roi_align_from_scratch.py` | RoIAlign을 직접 구현해서 원리 이해 | `model_TAAD_baseline.py` line 63 |
| 05 | `05_binary_vs_soft_mask.py` | Binary mask vs continuous mask 차이 시각화 | FOOTPASS mask gating (우리 확장 포인트) |
| 06 | `06_simple_iou_tracker.py` | 최소 MOT 구현 (SORT의 기본 아이디어) | SORT, ByteTrack, OC-SORT 관련 |
| 07 | `07_footpass_taad_walkthrough.py` | 원본 `X3D_TAAD_Baseline.forward`를 단계별로 주석과 함께 실행 | 최종 목표 |

## 실행 방법

```bash
cd YoungScientist/Tutorial
python examples/01_tensors_and_shapes.py
python examples/02_image_to_tensor.py
# ...
```

각 파일은 **독립적**으로 실행 가능하며, 중요한 중간 결과는 `outputs/` 폴더에 PNG로 저장된다.
실행 시 콘솔에 "어떤 shape인지, 무슨 의미인지" 설명이 출력되도록 만들었다.

## 필요 환경

- **01~06**: Python + numpy + pillow + matplotlib (이미 설치됨)
- **07**: PyTorch + torchvision (FOOTPASS 환경: Python 3.11.5 + PyTorch 2.1.0)
  - 07은 현재 개발 기기에서는 **코드를 읽으며 학습**하는 용도. 실행은 FOOTPASS 환경에서.

## 핵심 질문 체크리스트 (학습 후 스스로 답할 수 있어야 함)

다음 질문에 답하지 못하면 해당 튜토리얼을 다시 보기 바란다.

### 튜토리얼 1 후
- [ ] `(B, C, T, H, W)` 텐서에서 각 축이 뭘 의미하나?
- [ ] `reshape`와 `permute`의 차이는?
- [ ] 왜 딥러닝에선 첫 차원이 Batch인가?

### 튜토리얼 2 후
- [ ] 이미지 정규화에서 `mean=0.45, std=0.225`를 왜 빼고 나누나?
- [ ] `(H, W, C)`와 `(C, H, W)` 중 PyTorch는 왜 후자를 쓰나?

### 튜토리얼 3 후
- [ ] `[x1,y1,x2,y2]`, `[x,y,w,h]`, `[cx,cy,w,h]` 세 가지 표현을 서로 변환할 수 있나?
- [ ] IoU가 0.5라는 말이 geometry 상으로 무슨 의미인가?

### 튜토리얼 4 후
- [ ] RoIAlign이 RoIPool과 뭐가 다른가?
- [ ] FOOTPASS 코드의 `roi_align(x, roi, (4,2), 0.125)`에서 0.125는 뭔가?

### 튜토리얼 5 후
- [ ] FOOTPASS의 binary mask를 continuous로 바꿨을 때 forward pass가 어떻게 달라지나?
- [ ] Soft mask 값이 0.3이면 feature는 어떻게 변하는가?

### 튜토리얼 6 후
- [ ] Tracking-by-detection의 3단계는?
- [ ] Hungarian algorithm이 MOT에서 무슨 역할을 하나?

### 튜토리얼 7 후
- [ ] FOOTPASS TAAD forward의 입력 3개와 출력 1개의 shape?
- [ ] X3D backbone 다음에 왜 `roi_align`이 오나?
- [ ] 우리가 설계한 `ExtendedTAAD`가 정확히 어느 줄을 바꿨나?

## 다음 단계

이 7개 튜토리얼을 모두 따라한 뒤에는:
1. `../FOOTPASS-main/models/model_TAAD_baseline.py` 70줄이 **한 번에 읽힌다**
2. `../FOOTPASS-ext/amoni_soccer/*.py`의 각 모듈이 어떤 자리에 끼어드는지 이해된다
3. 자신만의 아이디어를 코드로 실험해볼 수 있다

---

**Tip**: 이해 안 되는 줄은 그 텐서의 `.shape`를 `print()`로 찍어보라. 실무자가 매일 하는 일이다.
