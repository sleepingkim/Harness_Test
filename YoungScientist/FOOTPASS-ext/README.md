# FOOTPASS-ext: AmoUni-SoccerTrack Extension of FOOTPASS

**Author:** YoungScientist (single-camera soccer occlusion research)
**Upstream:** `../FOOTPASS-main` (원본 FOOTPASS Player-Centric Ball-Action Spotting 2026 challenge code, **수정하지 않음**)
**Research design:** `../_workspace/05_research_design.md`

## Purpose

이 폴더는 FOOTPASS-main 원본을 **import만 하여 확장**하는 연구용 구현체이다. 본 연구(AmoUni-SoccerTrack)의 3가지 모듈을 FOOTPASS의 TAAD 파이프라인에 주입하여, **가림(occlusion) 상황의 선수 식별 성능 → action spotting F1@0.15 개선**을 목표로 한다.

### 핵심 통찰 (Integration Point)
FOOTPASS의 `X3D_TAAD_Baseline.forward` (원본 파일: `../FOOTPASS-main/models/model_TAAD_baseline.py` line 65) 는 입력으로 `(x, roi, mask)`를 받으며, 여기서 **`mask`는 binary visibility**(선수가 프레임에 있으면 1, 없으면 0)이다. 이 binary mask는 가림/부분 가시성 같은 연속적 상태를 표현하지 못한다.

본 확장은 이 binary mask를 **continuous visibility + uncertainty**(`1 - u_a`)로 대체하여 action spotting 정확도를 높인다. 구체적으로:

```
원본 TAAD:         mask ∈ {0, 1}^{B×M×T}
AmoUni-SoccerTrack: mask ∈ [0, 1]^{B×M×T×2}
                   # channel 0: visibility (amodal head에서 유도)
                   # channel 1: 1 - amodal uncertainty
```

## Folder Structure

```
FOOTPASS-ext/
├── README.md                    # 이 파일
├── amoni_soccer/
│   ├── __init__.py
│   ├── amodal_head.py           # Module 1: Soccer-Amodal Head
│   ├── uniform_aware_reid.py    # Module 2: Uniform-aware Re-ID
│   ├── uncertainty_graph.py     # Module 3: Uncertainty propagation
│   ├── extended_taad.py         # FOOTPASS TAAD 래핑 + 확장
│   └── footpass_loader.py       # FOOTPASS-main import helper
├── configs/
│   └── default.yaml             # 하이퍼파라미터
├── scripts/
│   ├── train_amoni_taad.py      # 학습 엔트리포인트
│   └── eval_amoni_taad.py       # 평가 엔트리포인트 (FOOTPASS evaluation.py 호출)
├── tests/
│   └── test_forward.py          # 더미 입력 forward 스모크 테스트
└── notes/
    └── integration_plan.md      # 통합 전략 상세 노트
```

## Installation

```bash
# 환경은 FOOTPASS-main README.md 참고 (Python 3.11.5, PyTorch 2.1.0)
cd YoungScientist/FOOTPASS-ext
pip install pyyaml  # 추가 의존성 (설정 파일)
```

FOOTPASS-main의 패키지(X3D, decord, h5py, albumentations 등)를 그대로 사용하며 추가 설치는 `pyyaml`뿐이다.

## Quick Start

### 0. 정적 검증 (PyTorch 불필요)
```bash
cd YoungScientist/FOOTPASS-ext
python -m tests.test_static
```

코드의 구조·API·설정 파일 정합성을 AST 레벨에서 검증한다. **Python만 있으면 동작**하며 현재 본 레포에서 통과 확인됨(2026-04-16).

### 1. Forward smoke test (데이터 불필요, PyTorch 필요)
```bash
# FOOTPASS-main README와 동일한 환경을 구성한 후
# Python 3.11.5 + PyTorch 2.1.0 + torchvision 0.16.0
cd YoungScientist/FOOTPASS-ext
python -m tests.test_forward
```

더미 텐서로 Extended TAAD의 forward pass를 검증한다. GPU 없이도 CPU에서 실행 가능(느림, X3D 가중치 다운로드 필요).

> 주의: 현재 개발 기기의 Python 3.14는 PyTorch 공식 휠이 아직 없으므로 FOOTPASS 권장 환경(Python 3.11.5)에서 실행해야 한다.

### 2. 학습 (데이터 필요)
FOOTPASS 데이터셋(NDA 승인 후)을 `../FOOTPASS-main/videos/` 및 `../FOOTPASS-main/data/`에 배치한 후:

```bash
python scripts/train_amoni_taad.py --config configs/default.yaml
```

### 3. 평가
```bash
python scripts/eval_amoni_taad.py --checkpoint runs/best.pt --split val
# 내부적으로 FOOTPASS-main/evaluation.py와 동일 metric 계산
```

## Module Mapping (연구 설계서 ↔ 코드)

| 연구 설계 | 코드 위치 | 설명 |
|----------|----------|------|
| Module 1: Soccer-Amodal Head | `amoni_soccer/amodal_head.py` | RoI feature → (M_vis, M_amo, M_occ, u_a) |
| Module 2: Uniform-aware Re-ID | `amoni_soccer/uniform_aware_reid.py` | Part-based + jersey-region + intra-team CL |
| Module 3: Uncertainty Propagation | `amoni_soccer/uncertainty_graph.py` | u_a → u_r → u_j → tracklet score |
| FOOTPASS 통합 | `amoni_soccer/extended_taad.py` | binary mask → [vis, 1-u_a] 2-channel |
| 학습/평가 | `scripts/` | 전체 파이프라인 엔트리포인트 |

## Design Principles

1. **원본 불변**: `FOOTPASS-main/` 의 어떤 파일도 수정하지 않는다. 오직 `import` 만 사용.
2. **Opt-in 확장**: 각 모듈은 config로 on/off 가능 → baseline 재현 / ablation 용이.
3. **Reproducibility**: seed 고정(42, 123, 2024) / YAML 설정 / checkpoint 저장 프로토콜.
4. **단계별 구현**: 현재는 **스켈레톤 단계**이며, 실제 학습 전에 다음이 필요:
   - FOOTPASS 데이터셋 NDA 승인 및 다운로드
   - SAMEO pretrained weights 확보
   - HRNet pose estimator 통합
   - A100 GPU 시간 확보

## Current Status (2026-04-16)

| 구성 요소 | 상태 | 비고 |
|----------|------|------|
| Extended TAAD wrapper | ✅ 코드 완성 | `(x, roi, mask_binary)` → `(B,9,M,T)` logit. Forward 로직 FOOTPASS line-by-line 재현 + amodal gate 주입 |
| Soccer-Amodal Head | ✅ 코드 완성 | UOAIS-style 계층적 mask + entropy-based uncertainty. 학습 손실 4종 구현 |
| Uniform-aware Re-ID | ✅ 코드 완성 | Part + jersey-region + intra-team contrastive. L2-normalized embedding |
| Uncertainty Propagation | ✅ 코드 완성 | Learnable fusion weights + uncertainty-weighted distance + ECE |
| 학습 스크립트 | ✅ 코드 완성 | YAML config + cosine LR + gradient clip |
| 평가 스크립트 | ✅ 코드 완성 | FOOTPASS `evaluation.py` 위임 (subprocess) |
| **정적 테스트** | ✅ **통과** | `tests/test_static.py` — AST 레벨 API·시그니처 검증 |
| Forward 스모크 테스트 | ⏳ 환경 대기 | `tests/test_forward.py` 준비됨, Python 3.11+PyTorch 환경에서 실행 필요 |
| Pseudo-label 파이프라인 | ⬜ 미구현 | SAMEO checkpoint 확보 후 추가 |
| Pose estimator 통합 | ⬜ 미구현 | HRNet SoccerNet finetune 후 추가 |

**다음 단계**: 데이터 확보 후 P1 (baseline 재현) → P2 (Amodal head 학습) → … (05_research_design.md roadmap 참고)

## Upstream Reference

FOOTPASS-main 구조 (읽기 전용):
- `models/model_TAAD_baseline.py` — X3D_TAAD_Baseline (확장 대상)
- `models/model_GNN.py` — TAAD+GNN
- `models/model_DST.py` — TAAD+DST
- `utils/TAAD_Dataset.py` — HDF5 기반 데이터 로더
- `utils/metric_utils.py` — 평가 지표
- `train_TAAD_Baseline.py` — 원본 학습 스크립트
- `evaluation.py` — F1@0.15 계산

## Citation

본 확장을 사용할 경우 FOOTPASS 및 본 연구를 인용해주세요:
```bibtex
@article{Ochin2025FOOTPASS,
  title   = {FOOTPASS: A Multi-Modal Multi-Agent Tactical Context Dataset for Play-by-Play Action Spotting in Soccer Broadcast Videos},
  author  = {Ochin, Jérémy and Chekroun, Raphael and Stanciulescu, Bogdan and Manitsaris, Sotiris},
  journal = {Submitted to CVIU},
  year    = {2025}
}
```

## License

FOOTPASS-main은 원 저자의 라이선스(CC BY-NC 4.0) 하에 있다. 본 확장 코드는 동일 조건으로 재배포 가능하나, FOOTPASS 데이터셋(비디오)은 NDA에 의해 재배포 불가.
