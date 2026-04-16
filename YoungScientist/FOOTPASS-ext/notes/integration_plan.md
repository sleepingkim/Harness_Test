# FOOTPASS ↔ AmoUni-SoccerTrack 통합 전략

## 1. FOOTPASS TAAD 아키텍처 분석

### 1.1 입력 signature
```python
# FOOTPASS-main/models/model_TAAD_baseline.py:34
def forward(self, in_x):
    x, roi, mask = in_x
    # x:    (B, 3, T, 352, 640)  — 비디오 클립
    # roi:  (B, M, T, 5)          — [frame_idx, x1, y1, x2, y2] for each player m in {0..M-1}
    # mask: (B, M, T)              — binary (1 if player visible at frame t)
```

### 1.2 Mask 사용 위치 (line 65)
```python
x = x*(mask.reshape(b*M,l).unsqueeze(1))  # (B*M,192,T)
```

**관찰**: mask는 ROI feature에 element-wise 곱해져 **가려진 시점의 feature를 0으로 만든다**. 이것이 binary gating이다.

### 1.3 출력
```python
# shape: (B, 9, M, T)  — 9개 class logit (8 actions + bg) × M players × T frames
```

## 2. 우리의 확장 전략

### 2.1 Mask를 continuous 2-channel로 대체
```python
# 기존: mask ∈ {0,1}^{B×M×T}
# 확장: mask ∈ [0,1]^{B×M×T×2}
#   channel 0: visibility v = amodal_visible_area / amodal_total_area ∈ [0,1]
#   channel 1: 1 - u_a   where u_a is amodal uncertainty ∈ [0,1]
```

### 2.2 Gating 변경
```python
# 기존 (binary gating):
x = x * mask  # 0이면 완전 제거, 1이면 그대로

# 확장 (soft gating with uncertainty discount):
v = mask[..., 0]           # visibility
c = mask[..., 1]           # confidence (1 - u_a)
gate = v * c               # 가시성 × 확신도
x = x * gate               # soft gating
```

### 2.3 Amodal head 위치
ROI feature를 그대로 쓰지 않고, **amodal head가 먼저 visibility/uncertainty를 추정**한 뒤 TAAD에 전달한다:

```
Input Video + RoI
    │
    ▼
[YOLO / Pre-computed] → ROI features (RoIAlign)
    │
    ▼
[Soccer-Amodal Head] → M_vis, M_amo, u_a
    │
    ▼
[visibility v = area(M_vis)/area(M_amo)]
[confidence c = 1 - u_a]
    │
    ▼
[Extended TAAD] (x, roi, mask_continuous)
    │
    ▼
Action logits (B, 9, M, T)
```

### 2.4 학습 체계
- **Stage 1**: Amodal head 단독 학습 (SAMEO pseudo-label)
- **Stage 2**: TAAD 단독 학습 (원본 재현, binary mask)
- **Stage 3**: End-to-end finetune (Amodal + Extended TAAD, joint loss)

Stage 3 loss:
```
L_total = λ_action · L_action + λ_amodal · L_amodal + λ_cons · L_consistency
        + λ_u · L_uncertainty_calibration
```

## 3. Uncertainty Propagation 적용 지점

| 단계 | Uncertainty 신호 | 주입 방식 |
|-----|------------------|----------|
| Amodal | $u_a$ = entropy(M_amo) - entropy(M_vis) | mask channel 1 |
| Re-ID | $u_r$ = feature variance | Re-ID distance weight |
| Jersey | $u_j$ = softmax entropy | Tracklet aggregation weight |
| Action | $u_{act}$ = predictive entropy | Post-hoc NMS threshold |

이 4가지를 tracklet-level graph로 결합 (uncertainty_graph.py 참조).

## 4. Uniform-aware Re-ID 적용 지점

FOOTPASS 자체는 Re-ID 학습이 없고 tracklet이 이미 주어진다. 하지만 우리는:
- **TAAD 이전 단계의 tracking**(별도 모듈)에서 ID switch를 줄이는 용도로 Uniform-aware Re-ID 사용
- **당장 FOOTPASS 통합에서는 Re-ID 학습보다 Amodal + Uncertainty 먼저 검증**
- Re-ID는 SoccerNet-Tracking 실험(본 논문 Table 1)에서 주로 평가

## 5. 구현 단계 (M1~M12 roadmap 연동)

| Milestone | 작업 | 산출물 | 관련 코드 |
|-----------|------|-------|----------|
| M1~M2 | FOOTPASS baseline 재현 | TAAD val F1 | `../FOOTPASS-main` 그대로 |
| M3 | Amodal head skeleton + forward | unit test 통과 | `amodal_head.py` ✅ (현재 단계) |
| M4 | SAMEO pseudo-label 파이프라인 | pseudo dataset | `scripts/generate_pseudo_labels.py` (미구현) |
| M5 | Amodal head 학습 | amodal mIoU | `scripts/train_amodal.py` (미구현) |
| M6 | Extended TAAD wrapper | forward 통과 | `extended_taad.py` ✅ (현재 단계) |
| M7 | End-to-end 학습 | val F1 개선 확인 | `scripts/train_amoni_taad.py` ✅ |
| M8 | Uncertainty propagation + calibration | ECE < 0.10 | `uncertainty_graph.py` ✅ |
| M9~M10 | 전체 ablation + 분석 | 실험 테이블 | - |
| M11~M12 | 논문 작성 | `paper/main.tex` ✅ (draft) | - |

## 6. 현재 스켈레톤의 한계

- **실제 데이터 학습 불가**: FOOTPASS NDA 승인 필요
- **Amodal pretrained 없음**: SAMEO checkpoint 다운로드 필요
- **Pose estimator 미통합**: HRNet 설치 + soccer fine-tune 필요
- **Re-ID 학습 미구현**: 별도 Phase (현 단계 focus 아님)

**현 단계 목표**: 모든 모듈의 **forward pass가 동작**하고, FOOTPASS TAAD와 shape 호환성이 증명되는 스모크 테스트 통과.

## 7. 확장 후 예상 변경 사항 (참고용)

원본 FOOTPASS TAAD_Dataset는 binary mask를 반환:
```python
# 원본 (line 267): bbox가 있으면 mask = 1
```

우리는 `FOOTPASSDatasetWithAmodal` 래퍼를 만들어:
1. 원본 dataset의 `__getitem__`을 호출
2. 반환된 clip+ROI에 amodal head를 적용하여 `mask_continuous` 생성
3. 원본 mask 대신 `mask_continuous` 반환

이렇게 하면 **FOOTPASS-main의 dataset 코드를 전혀 수정하지 않고** 확장 가능하다.
