# 단일 카메라 축구 영상 가림 상황 선수 식별 성능 개선 연구 설계서

**작성일:** 2026-04-16
**작성자:** research-designer 에이전트
**연구 방향:** 방향 A — Amodal + Uniform-aware Soccer Tracker (조합 3 기반, 연구 공백 ①②③ 동시 해결)
**프레임워크:** Harness100 research-designer + IMRaD 인지 설계

---

## Executive Summary

본 연구는 단일 카메라로 촬영된 축구 영상에서 **가림(occlusion) 상황의 선수 식별 성능**을 근본적으로 개선하는 것을 목표로 한다. Phase 1~2의 문헌(51편) 및 기법(20개) 분석을 통해 **세 개의 명확한 연구 공백** — ① 축구 특화 amodal perception 부재, ② uniform-aware occlusion disambiguation 부재, ③ tracklet-level uncertainty propagation 부재 — 를 확인하였고, 이를 동시에 해결하는 **AmoUni-SoccerTrack** 프레임워크를 제안한다.

핵심 아이디어는 세 가지다. 첫째, SAMEO foundation model로 SoccerNet 영상에 amodal pseudo-label을 자동 생성하고 UOAIS 스타일 Soccer-Amodal Head로 finetuning하여 가려진 선수의 visible/amodal/occlusion mask를 계층적으로 추정한다(모듈 1). 둘째, 같은 팀 선수 간 식별력을 확보하기 위해 pose-guided part embedding + jersey-region branch + intra-team contrastive loss를 결합한 Uniform-aware Re-ID를 설계한다(모듈 2). 셋째, amodal → Re-ID → jersey → tracklet으로 이어지는 전 파이프라인에 uncertainty를 **graph-propagation 형태로 전파**하는 end-to-end 학습 체계를 제안한다(모듈 3).

평가는 SoccerNet-Tracking, SoccerNet-ReID, SoccerNet-Jersey, SoccerNet-GSR, SportsMOT을 주 벤치마크로 하며, Deep-EIoU+GTA-Link(SoccerTrack 2025 우승)·ByteTrack·OC-SORT·StrongSORT+AFLink·Deep OC-SORT·SoccerNet GSR 2025 winner 등 **6개 이상의 강력한 baseline**과 비교한다. 신규 평가 지표로 **Occluded-HOTA**(가림율 ≥50% 구간 전용), **Recovery rate**(가림 복귀 후 ID 복원율), **ECE**(Expected Calibration Error)을 도입한다. 12개월 로드맵으로 진행하며 CVPR 2027 CVSports Workshop을 1차 투고 목표로 한다.

예상 기여도: 심각한 가림(50~80%) 구간에서 기존 SOTA 대비 **IDF1 +5~10%**, Jersey accuracy +3~5%, Long-clip(45분) ID consistency +10%+, 그리고 축구 도메인 최초 amodal 벤치마크 공개.

---

## 1. 연구 배경 및 동기

### 1.1 문제의 중요성
축구 영상 분석은 전술 분석, 선수 평가, 방송 증강, 게임 재구성(Game State Reconstruction, GSR) 등 스포츠 산업의 핵심 파이프라인이다. 이 중에서도 **선수별 고유 ID를 일관되게 유지하고 등번호를 정확히 인식**하는 것은 모든 downstream task의 전제 조건이다. 그러나 축구 경기의 고유 특성 — **22명 동시 활동, 빠른 비선형 움직임, 유사 유니폼, 빈번한 가림** — 때문에 일반 MOT 분야의 기법들은 직접 적용 시 상당한 성능 저하를 보인다(문헌 P1-1, P1-2, P1-4).

### 1.2 가림(Occlusion)의 특수성
축구에서의 가림은 단순한 부분 가림을 넘어, (i) **같은 팀 선수 간 가림**(유니폼 색이 동일해 appearance로 구별 불가), (ii) **몸싸움 중 복잡한 중첩**(공 경합, 코너킥, 페널티 상황), (iii) **롱샷에서의 원거리 가림**(픽셀 해상도 저하)이 동시에 일어난다. 기존 MOT(MOT17/20)의 보행자 가림은 주로 수직 방향이지만, 축구는 수평·비스듬한 가림이 빈번하다는 구조적 차이도 존재한다.

### 1.3 기존 연구의 한계
Phase 1~2 분석(51편 문헌, 20개 기법 심층 분석) 결과, 현재 SOTA인 **Deep-EIoU + GTA-Link**(SoccerTrack 2025 우승, P1-11/P1-12)조차 50% 이상 가림 구간에서는 ID switch와 jersey 인식 실패가 급증한다. 또한 최신 기법들이 개별 단계(detection, tracking, Re-ID, jersey)의 개선에 집중되어 있으며, **각 단계의 불확실성을 체계적으로 downstream에 전파하는 구조는 부재**하다.

### 1.4 연구의 학술적·산업적 의의
본 연구는 (i) 축구 도메인에 amodal perception을 최초로 통합하여 가려진 부분까지 추론 가능한 프레임워크를 제시하고, (ii) 유사 유니폼 조건에서 작동하는 새로운 Re-ID 패러다임(Uniform-aware)을 정립하며, (iii) 불확실성 전파라는 아직 MOT 분야에 본격 도입되지 않은 개념을 실증한다. 산업적으로는 경기 분석 자동화, 전술 리포트 생성, 방송 중계 증강의 기반 기술이 된다.

---

## 2. 문제 정의 (Harness100 프레임워크)

### 2.1 형식적 정의

**입력**:
$$\mathcal{I} = \{I_1, I_2, \ldots, I_T\}, \quad I_t \in \mathbb{R}^{H \times W \times 3}$$
- 단일 카메라 축구 영상 시퀀스(broadcast 또는 fixed-camera)
- 프레임률: 25~30 FPS, 해상도: 1080p 이상(fisheye의 경우 4096×1080)
- 시퀀스 길이 T: 30초(~750 frames) ~ 45분(~67500 frames)

**출력**: 각 프레임 $t$의 각 검출 객체 $i$에 대해
$$O_t^i = \{b_t^i, \text{ID}_t^i, n_t^i, c_t^i, M_t^{i,\text{vis}}, M_t^{i,\text{amo}}, M_t^{i,\text{occ}}, u_t^i\}$$
여기서
- $b_t^i \in \mathbb{R}^4$: 바운딩 박스 $(x, y, w, h)$
- $\text{ID}_t^i \in \mathbb{N}$: 전역 고유 트랙 ID
- $n_t^i \in \{0, 1, \ldots, 99\} \cup \{\varnothing\}$: 등번호(미식별 시 $\varnothing$)
- $c_t^i \in \{\text{left team}, \text{right team}, \text{GK-L}, \text{GK-R}, \text{referee}, \text{other}\}$: 팀/역할
- $M_t^{i,\text{vis}}, M_t^{i,\text{amo}}, M_t^{i,\text{occ}}$: 가시/amodal/가림 마스크
- $u_t^i \in [0,1]$: 종합 불확실성 스칼라(세부 항목 모듈 3에서 정의)

**제약**:
- C1 (실시간성): ≥25 FPS (online 구성) / ≥5 FPS (full pipeline)
- C2 (단일 카메라): 1개 카메라 입력 전제
- C3 (가림 강건성): 가림율 ≥50% 상황에서도 ID 유지·번호 인식 성능 저하 최소화
- C4 (재현성): 공개 데이터셋 + 공개 코드 + 단일 GPU 추론 가능

### 2.2 핵심 도전과제

| 도전과제 | 세부 내용 | 관련 공백 |
|--------|----------|----------|
| D1. 가려진 선수의 형태 복원 | 축구 특화 amodal annotation 부재, pseudo-label 품질 확보 필요 | ① |
| D2. 같은 팀 선수 구별 | 유니폼 동일 → appearance 변별력 낮음, 번호·pose 조합 필요 | ② |
| D3. 불확실성 downstream 전파 | 각 단계의 confidence가 독립적으로 처리됨, 체인 간 결합 부재 | ③ |
| D4. 실시간성 유지 | Amodal(SAMEO, Diffusion) 계열은 느림 → online/offline 이중 설계 필요 | - |
| D5. 도메인 gap | MOT17/20, Occluded-Duke, Amodal-LVIS 등 원천 데이터는 축구와 이질적 | ①② |

---

## 3. 연구 질문 및 가설

### 3.1 Primary Research Question (PRQ)

> **PRQ**: 단일 카메라 축구 영상에서 amodal perception, uniform-aware Re-ID, uncertainty propagation을 통합한 프레임워크가 **심각한 가림(occlusion ≥50%) 구간의 선수 식별 성능**을 기존 SOTA 대비 **IDF1 ≥5%, Jersey accuracy ≥3%** 개선할 수 있는가?

### 3.2 Secondary Research Questions (SRQs)

- **SRQ1 (공백 ①)**: SAMEO 기반 pseudo-label + UOAIS 스타일 계층적 학습으로 축구 선수의 amodal mask를 얼마나 정확하게 예측할 수 있는가? (측정: amodal mIoU, visible-amodal IoU gap)
- **SRQ2 (공백 ②)**: Jersey-region branch와 intra-team contrastive loss를 추가한 Uniform-aware Re-ID가 같은 팀 선수 가림 상황에서 기존 Sports Re-ID 대비 **intra-team Rank-1 accuracy**를 얼마나 개선하는가?
- **SRQ3 (공백 ③)**: Amodal uncertainty → Re-ID uncertainty → Jersey uncertainty로 이어지는 graph propagation이 **ECE**(Expected Calibration Error)와 **AURC**(Area Under Risk-Coverage)를 유의하게 낮추는가?
- **SRQ4 (공백 ④, 보조)**: Uncertainty-weighted GTA-Link가 45분 long-clip에서 ID consistency(IDF1)을 얼마나 유지하는가?
- **SRQ5**: 제안 프레임워크의 각 모듈(amodal, uniform-aware, uncertainty)이 개별적으로 기여하는 정도는? (Ablation)

### 3.3 Hypotheses (검증 가능한 형태)

| 가설     | 진술                                                                                                                       | 검증 지표                              | 유의 수준                   |
| ------ | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- | ----------------------- |
| **H1** | Soccer-Amodal Head는 가림율 30% 이상 선수에 대해 amodal mIoU ≥ 0.65를 달성한다                                                           | amodal mIoU, visible mIoU, 가림율 구간별 | p < 0.05                |
| **H2** | Uniform-aware Re-ID는 Sports Re-ID Multi-task (P4-3) 대비 intra-team 조건에서 Rank-1이 **+3%p 이상** 향상된다                          | Intra-team Rank-1, mAP             | paired t-test, p < 0.05 |
| **H3** | Uncertainty propagation은 Tracklet-level jersey accuracy의 ECE를 **0.10 이하**로 감소시킨다 (baseline ECE > 0.15)                   | ECE, AURC, Brier score             | McNemar's test          |
| **H4** | 제안 전체 프레임워크는 SoccerNet-Tracking에서 Deep-EIoU+GTA-Link 대비 **HOTA +2%, IDF1 +3%**, 심각한 가림(50~80%) 구간에서 **IDF1 +5~10%** 달성한다 | HOTA, IDF1, Occluded-HOTA          | paired t-test, 95% CI   |
| **H5** | Amodal 모듈 제거(w/o amodal)는 Occluded-HOTA를 **3%p 이상 감소**시킨다                                                                | Occluded-HOTA delta                | ablation test           |
| **H6** | Intra-team contrastive loss는 Rank-1 intra-team을 **2%p 이상** 향상시킨다                                                         | Rank-1 intra-team                  | paired t-test           |
| **H7** | 제안 프레임워크는 45분 long-clip에서 ID switches를 Deep-EIoU+GTA 대비 **30% 이상 감소**시킨다                                                 | ID Switch count, long-IDF1         | Wilcoxon signed-rank    |

### 3.4 변수 정의

**독립변수 (IV)**:
| 변수명 | 수준 | 의미 |
|-------|------|------|
| IV1 | Amodal module | {off, UOAIS-head, SAMEO-adapt, Diffusion-offline} |
| IV2 | Uniform-aware Re-ID | {Sports Re-ID baseline, +Jersey region, +Intra-team CL, 전체} |
| IV3 | Uncertainty propagation | {off, amodal→Re-ID only, amodal→Re-ID→Jersey, full graph} |
| IV4 | Occlusion rate | {0~20%, 20~50%, 50~80%, 80%+} (시나리오 C에서 분할) |
| IV5 | Intra-team contrastive | {off, on} |
| IV6 | Amodal pseudo-label 검수 비율 | {0%, 10%, 30%, 100% manual} |

**종속변수 (DV)**:
| 변수명 | 단위 | 측정 방식 |
|-------|------|----------|
| DV1 | HOTA | [0,1] | TrackEval 공식 구현 |
| DV2 | IDF1 | [0,1] | TrackEval |
| DV3 | ID Switches | count | TrackEval |
| DV4 | AssA / DetA | [0,1] | HOTA 분해 |
| DV5 | MOTA | [-∞,1] | TrackEval |
| DV6 | Jersey Accuracy (top-1/top-3) | [0,1] | Tracklet level |
| DV7 | Re-ID mAP, Rank-1 | [0,1] | 표준 Re-ID 프로토콜 |
| DV8 | Occluded-HOTA (신규) | [0,1] | 본 연구 정의(5.2절) |
| DV9 | Recovery rate (신규) | [0,1] | 본 연구 정의 |
| DV10 | ECE, AURC, Brier (신규) | [0,1] | Calibration 메트릭 |
| DV11 | amodal mIoU | [0,1] | COCO-style mask IoU |

**통제변수 (CV)**:
| 변수명 | 고정값 |
|-------|-------|
| CV1. Detector backbone | YOLOv8-X |
| CV2. Input resolution | 1280 (SoccerNet standard) |
| CV3. FPS | 25 (SoccerNet standard) |
| CV4. 학습 데이터 split | SoccerNet 공식 train/val/test |
| CV5. Optimizer | AdamW, lr=1e-4, cosine schedule |
| CV6. Seed | 3개 seed(42, 123, 2024) 반복 실험 평균 |
| CV7. Pose estimator | HRNet-W48 (fine-tuned on SoccerNet) |
| CV8. Hardware | NVIDIA A100 40GB 동일 GPU |

---

## 4. 제안 방법론

### 4.1 전체 아키텍처

```
Input Video I = {I_1, ..., I_T}
    │
    ▼
[Detection]    YOLOv8-X + Repulsion Loss (RepGT + RepBox, 클래스별 분리)
    │          출력: {b_t^i, s_t^i} — detection box + confidence
    ▼
[Amodal Perception]  Soccer-Amodal Head
    │                (SAMEO pseudo-label + UOAIS-style finetune on SoccerNet)
    │                입력: RoI feature + pose prior(HRNet keypoints)
    │                출력: {M_vis, M_amo, M_occ, u_a}
    ▼
[Motion Estimation]  OATrack
    │                occlusion rate r_t^i = area(M_occ) / area(M_amo)
    │                → adaptive Kalman innovation gain: K' = K · exp(-α·r)
    ▼
[Association]    Occlusion-Related GCN (OR-GCN)
    │            nodes: detection boxes
    │            edges: affinity + occlusion attribute
    │                   e_ij = [iou(b_i,b_j), appearance_sim, occ_rel_ij, team_same]
    ▼
[Uniform-aware Re-ID]
    │    (a) Part-based embedding (Sports Re-ID baseline)
    │    (b) Pose-guided visibility mask (PGFA 확장)
    │    (c) Jersey-region branch (신규)
    │    (d) Intra-team contrastive loss (신규)
    │    출력: {f_appearance, f_jersey_region, u_r}
    ▼
[Jersey Recognition]  Keyframe ID + Single-Stage Uncertainty STR
    │                  출력: {n_t^i, p(n_t^i), u_j}
    ▼
[Uncertainty Propagation]  Tracklet Uncertainty Graph
    │                      s = f(u_a, u_r, u_j)
    │                      = w_a·(1-u_a) + w_r·(1-u_r) + w_j·(1-u_j)
    │                      (weights 학습, temperature scaling)
    ▼
[Offline Global Linking]  GTA-Link (uncertainty-weighted)
    │                     d_ij = λ_1·d_app + λ_2·d_jersey + λ_3·d_team + λ_4·d_motion
    │                     (λ is uncertainty-adaptive)
    ▼
[Consistency Resolver]  22 ID cap + Hungarian global assignment
    │
    ▼
Output: {b_t^i, ID_t^i, n_t^i, c_t^i, M_vis, M_amo, u_t^i} per (t, i)
```

### 4.2 모듈 1: Soccer-Amodal Head (공백 ①)

#### 4.2.1 입력/출력 Spec
- **입력**:
  - RoI feature: $F_{\text{RoI}} \in \mathbb{R}^{256 \times 14 \times 14}$ (YOLOv8 backbone에서 RoIAlign)
  - Pose prior: HRNet keypoints $P \in \mathbb{R}^{17 \times 3}$ (x, y, visibility) → $28 \times 28$ heatmap으로 encode
  - 크롭 이미지: $I_{\text{crop}} \in \mathbb{R}^{3 \times 256 \times 128}$
- **출력**:
  - $M_{\text{vis}} \in [0,1]^{56 \times 56}$: visible mask
  - $M_{\text{amo}} \in [0,1]^{56 \times 56}$: amodal mask (전체 형태)
  - $M_{\text{occ}} \in [0,1]^{56 \times 56}$: occlusion mask (가려진 영역)
  - $u_a \in [0,1]$: amodal uncertainty (mask entropy 기반)

#### 4.2.2 네트워크 구조
UOAIS의 hierarchical occlusion modeling(P2-16)을 축구에 맞춰 경량화 + pose prior 주입:

```
         RoI feature (256x14x14)
              │
        ┌─────┴──────┐
        ▼            ▼
  [Visible Head]  [Amodal Head]
  4 Conv + Up      4 Conv + Up
        │            │
     M_vis         M_amo
        │            │
        └──→ M_occ = max(0, M_amo - M_vis)
              │
              ▼
        [Pose Prior Fusion]
        (concat with pose heatmap)
              │
              ▼
        [Uncertainty Head]
        (GAP + MLP)
              │
             u_a = H(M_amo) - H(M_vis)  # entropy difference
```

Pose prior는 Amodal Head의 중간 feature(2번째 conv 뒤)에 channel-wise concatenation으로 투입되며, 이는 축구 선수의 비정형 자세(슬라이딩, 점프)에서 amodal 형태 추정을 안정화한다.

#### 4.2.3 학습 손실

$$\mathcal{L}_{\text{amodal}} = \mathcal{L}_{\text{vis}} + \mathcal{L}_{\text{amo}} + \mathcal{L}_{\text{occ}} + \lambda_{\text{cons}} \mathcal{L}_{\text{cons}} + \lambda_u \mathcal{L}_u$$

- $\mathcal{L}_{\text{vis}}, \mathcal{L}_{\text{amo}}$: Binary Cross-Entropy + Dice loss
- $\mathcal{L}_{\text{occ}} = \text{BCE}(M_{\text{occ}}, \max(0, M_{\text{amo}}^{\text{GT}} - M_{\text{vis}}^{\text{GT}}))$
- $\mathcal{L}_{\text{cons}}$: Consistency — $M_{\text{amo}} \geq M_{\text{vis}}$ (pixel-wise)
- $\mathcal{L}_u$: Uncertainty calibration — $|u_a - \text{IoU}(M_{\text{amo}}, M_{\text{amo}}^{\text{GT}})|$

기본값: $\lambda_{\text{cons}} = 0.5$, $\lambda_u = 0.3$.

#### 4.2.4 Pseudo-label 생성 전략

1. **Stage 1 (Bootstrap)**: SAMEO(P2-17)를 SoccerNet-Tracking 영상의 선수 박스에 zero-shot 적용 → initial amodal mask.
2. **Stage 2 (Consensus filtering)**: UOAIS(P2-16, pretrained)과 SAMEO의 예측 IoU ≥ 0.7인 경우에만 pseudo-label 채택. 나머지는 discard.
3. **Stage 3 (Manual curation)**: 10~30% 샘플 수동 검수(가림율 50%+ 중심 샘플링) → high-quality subset 구축.
4. **Stage 4 (Domain-specific finetune)**: Soccer-Amodal Head를 consensus pseudo + curated subset으로 finetuning(2-stage: pseudo 80% epoch → curated 20% epoch).
5. **Stage 5 (Self-training)**: 학습된 Soccer-Amodal Head로 재추론 → confidence 상위 pseudo label로 재학습(1회 반복).

Pseudo-label 품질 목표: mIoU ≥ 0.75 (검수 기준), pixel accuracy ≥ 85%.

### 4.3 모듈 2: Uniform-aware Re-ID (공백 ②)

#### 4.3.1 구성
Sports Re-ID Multi-task(P4-3) baseline을 확장:

**(a) Part-based embedding** (기존 P4-2/P4-4)
- 선수 crop을 6개 horizontal part로 분할 + HRNet pose-aligned parts
- 각 part마다 $f_p \in \mathbb{R}^{128}$

**(b) Pose-guided visibility mask** (PGFA 확장, P4-5)
- Keypoint visibility $v_k \in [0,1]$로 part attention weight 결정
- $w_p = \text{softmax}(v_p / \tau)$

**(c) Jersey-region branch** (신규)
- Amodal mask $M_{\text{amo}}$ + pose keypoints(shoulder/hip)로 jersey region $R_j$ 추출
- $R_j$에 별도 encoder(ResNet50 경량 branch): $f_j \in \mathbb{R}^{128}$
- Jersey region이 가려졌을 경우 $M_{\text{amo}}$ 내 예측 pixel로부터 inpainted feature 추출

**(d) Intra-team contrastive loss** (신규, 핵심 기여)
- Same-player / same-team-different-player / different-team 3-way margin
- 같은 팀에서도 선수 간 embedding을 분리하도록 강제

#### 4.3.2 수식

**Final embedding**:
$$f = \text{concat}(f_{\text{global}}, \sum_p w_p f_p, f_j)$$
$$f \in \mathbb{R}^{128+128+128} = \mathbb{R}^{384}$$

**Intra-team contrastive loss** (InfoNCE 확장):
$$\mathcal{L}_{\text{intra}} = -\log \frac{\exp(f_a \cdot f_p^+ / \tau)}{\exp(f_a \cdot f_p^+ / \tau) + \sum_{n \in \mathcal{N}_{\text{intra}}} \exp(f_a \cdot f_n / \tau) + \sum_{n \in \mathcal{N}_{\text{inter}}} \exp(f_a \cdot f_n / \tau)}$$

- $f_a$: anchor (선수 A의 프레임 $t$)
- $f_p^+$: positive (선수 A의 다른 프레임)
- $\mathcal{N}_{\text{intra}}$: same-team, different-player (hard negative)
- $\mathcal{N}_{\text{inter}}$: different-team (easy negative)

**가중 마진 스케줄링**: intra-team negative의 temperature $\tau_{\text{intra}} < \tau_{\text{inter}}$로 설정(기본 0.07 vs 0.2)하여 intra-team 구별에 더 집중.

**Multi-task 종합 손실**:
$$\mathcal{L}_{\text{ReID}} = \mathcal{L}_{\text{ID}} + \mathcal{L}_{\text{triplet}} + \lambda_j \mathcal{L}_{\text{jersey}} + \lambda_t \mathcal{L}_{\text{team}} + \lambda_{\text{intra}} \mathcal{L}_{\text{intra}} + \lambda_r \mathcal{L}_{\text{role}}$$

기본값: $\lambda_j = 0.5$, $\lambda_t = 0.3$, $\lambda_{\text{intra}} = 0.5$, $\lambda_r = 0.2$.

#### 4.3.3 학습 전략
1. **Warm-up (5 epoch)**: inter-team loss만 활성화, intra-team off (embedding 공간 기초 형성)
2. **Curriculum (5~20 epoch)**: intra-team loss를 0→0.5로 linear scheduling
3. **Full training (20~60 epoch)**: 전체 손실 활성

Re-ID uncertainty $u_r$은 tracklet 내 embedding variance로 측정:
$$u_r = \frac{1}{|T|}\sum_{t \in T} ||f_t - \bar{f}||_2^2$$

### 4.4 모듈 3: Uncertainty Propagation (공백 ③)

#### 4.4.1 구성 요소
- Amodal uncertainty $u_a$: mask entropy (4.2.3)
- Re-ID uncertainty $u_r$: tracklet embedding variance (4.3.3)
- Jersey uncertainty $u_j$: Single-Stage Uncertainty STR(P3-6)의 예측 variance
- Motion uncertainty $u_m$: Kalman innovation norm (OATrack)
- Association uncertainty $u_c$: OR-GCN edge softmax entropy

#### 4.4.2 수식

**Tracklet-level integrated score** (log-linear opinion pooling):
$$s = \sigma\left(\sum_k w_k \log(1 - u_k)\right), \quad k \in \{a, r, j, m, c\}$$

Weights $w_k$는 validation set에서 tracklet-level identity accuracy를 최대화하도록 gradient descent로 학습(학습 파라미터 5개).

**Calibration (Temperature scaling)**:
각 uncertainty를 temperature $T_k$로 post-hoc 보정:
$$u_k' = \text{softmax}(\text{logits}_k / T_k)$$
$T_k$는 held-out validation set에서 ECE 최소화로 optimize.

**Graph propagation (신규)**:
Amodal uncertainty를 downstream에 가중치로 전파:
$$u_r' = u_r + \beta_{ar} \cdot u_a, \quad u_j' = u_j + \beta_{aj} \cdot u_a + \beta_{rj} \cdot u_r$$

$\beta$는 학습되는 scalar로, amodal이 불확실할수록 Re-ID/jersey 신뢰도도 낮아지는 구조.

#### 4.4.3 GTA-Link 확장

기존 GTA-Link(P1-12)의 tracklet distance:
$$d_{ij} = \lambda_1 d_{\text{app}} + \lambda_2 d_{\text{spatio}} + \lambda_3 d_{\text{temp}}$$

제안 확장:
$$d_{ij}^{\text{uw}} = \sum_k \lambda_k \cdot (1 - \max(u_{i,k}, u_{j,k})) \cdot d_k$$

- 불확실한 tracklet 쌍은 distance 가중치 낮춤 → linking conservativeness
- 22명 ID cap을 Hungarian global assignment 제약으로 통합

---

## 5. 실험 설계

### 5.1 데이터셋

| 데이터셋 | 용도 | 규모 | 비고 |
|---------|------|------|------|
| **SoccerNet-Tracking** (Primary) | Tracking main exp | 200×30s + 1×45min | HOTA 공식 벤치마크 |
| **SoccerNet-ReID** | Re-ID 평가 | tracklet-based | mAP/R1 평가 |
| **SoccerNet-Jersey** | Jersey recognition | 2853 train + 1211 challenge | Accuracy |
| **SoccerNet-GSR** | GSR 통합 평가 | broadcast→minimap | GS-HOTA |
| **SportsMOT** | Cross-sport 일반화 | 240 seq, 150K frame | HOTA (축구 부분) |
| **SoccerTrack (2025)** | Fisheye 시나리오 | 4096×1080 | 보조 평가 |
| **MOT17/20** | Cross-domain 일반화 | 보행자 | 모듈 독립성 검증 |
| **Occluded-Duke** | Re-ID 가림 성능 검증 | - | Cross-domain |
| **Amodal-LVIS** | Amodal pretrain | 300K | SAMEO origin |
| **Soccer-Amodal (자체, 신규)** | Amodal 검수 subset | 5000 instance 목표 | Pseudo 85% + manual 15% |

#### 5.1.1 데이터 분할
- **Train**: SoccerNet 공식 train split + Soccer-Amodal train
- **Val**: 공식 val split (hyperparameter tuning, temperature scaling)
- **Test**: 공식 test split (최종 성능 보고만, one-shot evaluation)
- **Challenge**: (가능 시) SoccerNet 2026 Challenge 제출

#### 5.1.2 Amodal pseudo-label pipeline
1. SoccerNet-Tracking 전 시퀀스 + SoccerNet-GSR 영상에서 detection 추출
2. SAMEO zero-shot → UOAIS consensus filter (IoU ≥ 0.7)
3. 가림율 50%+ sample을 우선 선별하여 15% 수동 검수(annotator 2명, Cohen's kappa ≥ 0.8 요구)
4. Soccer-Amodal dataset 공개 예정(정책 승인 시)

### 5.2 평가 지표

#### 5.2.1 기존 표준 지표
- **Tracking**: HOTA, MOTA, IDF1, AssA, DetA, ID Switch (TrackEval 공식 구현)
- **Jersey**: Accuracy, Top-1, Top-3 (SoccerNet Jersey 프로토콜)
- **Re-ID**: mAP, Rank-1, Rank-5, Rank-10 (표준 Re-ID 프로토콜)
- **GSR**: GS-HOTA (SoccerNet-GSR 공식)

#### 5.2.2 신규 평가 지표 (본 연구 기여)

**(a) Occluded-HOTA**
$$\text{Occ-HOTA} = \text{HOTA}|_{\mathcal{O}_{0.5}}$$
- $\mathcal{O}_{0.5}$: 선수의 amodal/visible ratio가 0.5 이하(가림 50% 이상)인 프레임·객체만 선별
- 가림율은 amodal GT(검수 subset)가 있는 경우 GT 사용, 없는 경우 Soccer-Amodal Head 예측 사용

**(b) Recovery rate**
$$\text{RR} = \frac{\#\{\text{가림 후 ID 복구된 tracklet}\}}{\#\{\text{가림 발생 tracklet}\}}$$
- "가림 발생": 연속 5프레임 이상 visible ratio < 0.3
- "복구": 가림 종료 후 10프레임 내 원래 ID 재부여

**(c) Calibration metrics**
- **ECE** (Expected Calibration Error, 15 bins)
- **AURC** (Area Under Risk-Coverage curve)
- **Brier score** (jersey prediction)

**(d) Intra-team Rank-1** (Re-ID 특화)
- Gallery를 동일 팀으로 제한 후 Rank-1 측정

### 5.3 Baselines (6개 이상, 재현 후 공정 비교)

| Baseline | 출처 | 유형 | 비교 포인트 |
|---------|------|------|------------|
| **B1. ByteTrack** | P2-3 (ECCV 2022) | Online MOT | 기본 강력 baseline, BYTE association |
| **B2. OC-SORT** | P2-5 (CVPR 2023) | Online MOT | Observation-centric, 비선형 강건 |
| **B3. Deep OC-SORT** | P2-7 (2023) | Online + Re-ID | Adaptive Re-ID weight |
| **B4. StrongSORT+AFLink+GSI** | P2-6 (TMM 2023) | Online + Offline | Offline linking 비교 |
| **B5. Deep-EIoU + GTA-Link** | P1-11 + P1-12 (WACV 2024 + 2025) | Sports SOTA | 축구 SOTA, 주요 경쟁자 |
| **B6. SoccerNet GSR 2025 Winner** | P4-7 | Integrated SOTA | 통합 파이프라인 |
| **B7. Sports Re-ID Multi-task** | P4-3 | Re-ID baseline | Uniform-aware 비교 대상 |
| **B8. Single-Stage Uncertainty Jersey** | P3-6 | Jersey SOTA | Jersey 비교 대상 |

모든 baseline은 저자 공개 코드(또는 신뢰 가능한 재구현)로 **동일 환경(A100, 동일 데이터 split, 동일 detector CV1)**에서 재현하여 공정 비교.

### 5.4 Ablation Study 계획

| Ablation | 제거/변경 요소 | 검증 목표 |
|----------|--------------|----------|
| A1. w/o Amodal | Soccer-Amodal Head 제거 | 공백 ① 기여도 (H5) |
| A2. w/o Uniform-aware | Sports Re-ID baseline으로 교체 | 공백 ② 기여도 |
| A3. w/o Intra-team CL | Intra-team contrastive만 제거 | 세부 기여 (H6) |
| A4. w/o Jersey region branch | Jersey branch만 제거 | 세부 기여 |
| A5. w/o Uncertainty prop | Uncertainty 전파 off, 독립 사용 | 공백 ③ 기여도 |
| A6. w/o Pose prior (amodal) | Amodal head에서 pose input 제거 | Pose prior 효과 |
| A7. Amodal head 구조 비교 | UOAIS-head vs SAMEO-adapter vs Diffusion-offline | 최적 구조 선택 |
| A8. Pseudo-label 품질 변화 | 수동 검수 비율 {0, 10, 30, 100}% | 검수 비용 trade-off |
| A9. Uncertainty weight 학습 vs 고정 | 학습 $w_k$ vs uniform $w_k$ | 학습 효과 |
| A10. OR-GCN w/o occlusion edge | GCN edge attribute에서 occlusion 제거 | OR-GCN 기여 |

각 ablation은 3개 seed 반복 평균.

### 5.5 실험 시나리오

#### 시나리오 A: Broadcast 영상 (SoccerNet 공식 test)
- 200×30s test split 평가
- Primary metric: HOTA, IDF1, Jersey accuracy

#### 시나리오 B: Static/Fisheye 카메라 (SoccerTrack)
- 4096×1080 fisheye 영상
- 22명 전체 + heavy distortion 조건
- 도메인 generalization 검증

#### 시나리오 C: 가림율 구간별 성능
- 각 test 영상을 tracklet 단위로 가림율 분할
  - 0~20% (light)
  - 20~50% (moderate)
  - 50~80% (severe)
  - 80%+ (extreme)
- 구간별 HOTA, IDF1, Recovery rate 보고
- 제안 프레임워크의 가림 강건성 곡선 시각화

#### 시나리오 D: Long-clip (45분) ID consistency
- SoccerNet-Tracking의 공식 45분 하프타임 시퀀스
- 평가: long-IDF1, ID switch count, 최장 ID 유지 시간
- 가능 시 자체 annotation 확장

#### 시나리오 E: Cross-domain 일반화
- MOT17/20에서 amodal, uniform-aware 제거 후 베이스만 평가 → 모듈 독립성
- Occluded-Duke에서 uniform-aware Re-ID 적용 → 가림 Re-ID generality

### 5.6 통계적 유의성

- **반복 실험**: 각 실험 3개 seed(42, 123, 2024)로 반복 → 평균 ± 표준편차 보고
- **검정**:
  - 제안 vs baseline: Paired t-test (seed-wise)
  - 순서 효과 의심 시: Wilcoxon signed-rank test
  - 다중 비교 보정: Bonferroni correction(baseline 6~8개)
- **신뢰구간**: 95% bootstrap CI (1000 resamples)
- **Effect size**: Cohen's d 병기 (작음 0.2, 중간 0.5, 큼 0.8)
- **Pre-registration**: 주요 hypotheses(H1~H7)를 OSF에 실험 시작 전 등록(선택 사항, 투명성)

### 5.7 Hyperparameter 설정 (재현성)

| 항목 | 값 |
|------|-----|
| Detector | YOLOv8-X, input 1280, conf 0.25, IoU 0.45 |
| Detector train | 50 epoch, AdamW 1e-4, SoccerNet train |
| Amodal head train | 30 epoch (pseudo 24 + curated 6), batch 16, lr 5e-5 |
| Re-ID train | 60 epoch, triplet margin 0.3, $\tau_{\text{intra}}=0.07$, $\tau_{\text{inter}}=0.2$ |
| OR-GCN | 3 layer, hidden 128, edge MLP 2 layer |
| Association threshold | IoU 0.5 (high), 0.1 (low), appearance 0.2 |
| Uncertainty temperature | held-out val ECE 최소화로 결정 |
| GTA-Link | window 5~15s, min tracklet length 10 frames |
| Hardware | NVIDIA A100 40GB × 4 (학습), × 1 (추론) |

---

## 6. 연구 로드맵

| Phase | 기간 | 주요 작업 | 산출물 | 마일스톤 |
|-------|------|----------|--------|---------|
| **P1. 기반 구축** | M1~M2 (2026-05 ~ 06) | (a) Codebase 설계 (b) 데이터 전처리 (c) Baseline B1~B6 재현 | Baseline reproduction report | 재현 HOTA가 논문 대비 ±1% 이내 |
| **P2. Amodal 모듈** | M3~M4 (2026-07 ~ 08) | (a) SAMEO pseudo-label pipeline (b) Soccer-Amodal Head 학습 (c) H1 검증 | Amodal module v1 + Soccer-Amodal pseudo dataset | amodal mIoU ≥ 0.65 |
| **P3. Uniform-aware Re-ID** | M5~M6 (2026-09 ~ 10) | (a) Jersey region branch (b) Intra-team CL (c) H2, H6 검증 | Re-ID module v1 | Intra-team Rank-1 +3%p |
| **P4. Uncertainty Propagation** | M7~M8 (2026-11 ~ 12) | (a) 5개 uncertainty 통합 (b) Graph propagation (c) Calibration (d) H3 검증 | Full pipeline v1 | ECE ≤ 0.10 |
| **P5. Full 실험** | M9~M10 (2027-01 ~ 02) | (a) 전체 experiments A~E (b) Ablation A1~A10 (c) H4, H5, H7 검증 | 실험 결과 + Occ-HOTA/RR 수치 | SoccerNet HOTA +2%, IDF1 +3%, Occ-IDF1 +5~10% |
| **P6. 논문 작성** | M11~M12 (2027-03 ~ 04) | IMRaD 논문 작성 (Introduction→Method→Experiments→Discussion→Conclusion), 공동저자 검토, 투고 | CVPR 2027 Workshop 원고 | CVSports 투고 |

### 6.1 IMRaD 인지 매핑
- **Introduction**: §1 (배경), §2 (문제 정의), §3 (RQ/H)
- **Method**: §4 (제안 방법론) — 모듈 1/2/3 순차 기술
- **Results**: §5의 실험 결과(로드맵 P5 산출)
- **Discussion**: §7 (기여점), §8 (리스크/한계)
- **Abstract/Conclusion**: §Executive Summary + §9 (투고 전략) 참고

### 6.2 중간 산출물 (Deliverable)

| 시기 | 산출물 |
|------|-------|
| M2 말 | Baseline reproduction 보고서, data preprocessing 코드 |
| M4 말 | Soccer-Amodal pseudo dataset (v1), Amodal head weights |
| M6 말 | Uniform-aware Re-ID weights, Intra-team benchmark |
| M8 말 | Full pipeline integration, uncertainty calibration |
| M10 말 | 전체 실험 표 (Tracking/Jersey/Re-ID/GSR/Occ-HOTA/RR) + ablation 표 |
| M12 말 | Paper draft v1 → v2(공동저자 revision) → 투고 |

---

## 7. 예상 기여점 (Expected Contributions)

1. **[공백 ①] 축구 도메인 최초 Amodal Perception 통합**
   - SAMEO → UOAIS-style Soccer-Amodal Head, pose-aware amodal 복원
   - Pseudo-label pipeline으로 annotation 비용 완화 (consensus + 선택적 검수)
   - 축구 선수 가림 상황에 직접 적용된 최초 연구

2. **[공백 ②] Uniform-aware Re-ID 신규 설계**
   - Jersey-region branch (M_amo + pose로 번호 영역 fine-grained encoding)
   - Intra-team contrastive loss (같은 팀 hard negative에 집중)
   - 유사 유니폼 문제의 새로운 해법 제시

3. **[공백 ③] End-to-end Uncertainty Propagation**
   - 5개 uncertainty(amodal, Re-ID, jersey, motion, association)의 graph propagation
   - Detection→tracking→Re-ID→jersey 전 파이프라인의 신뢰도 연결
   - Uncertainty-weighted GTA-Link로 global linking 강화

4. **신규 평가 지표 3종**
   - **Occluded-HOTA**: 가림율 ≥50% 구간의 HOTA
   - **Recovery rate**: 가림 후 ID 복원율
   - **ECE / AURC**: 축구 MOT 최초 calibration metric 적용

5. **축구 Amodal 벤치마크 (일부) 공개**
   - 검수된 15% Soccer-Amodal subset annotation 공개(정책 승인 시)
   - 공개 pseudo-label pipeline + Soccer-Amodal Head weights

6. **이론 + 재현 가능 시스템**
   - 전 파이프라인 오픈소스 공개 (PyTorch, Docker)
   - SoccerNet-Tracking/Jersey/GSR에서 검증된 end-to-end tracker

---

## 8. 리스크 및 대응

| # | 리스크 | 영향도 | 발생 확률 | 대응 전략 |
|---|-------|-------|----------|----------|
| R1 | SAMEO pseudo-label 품질 낮음 | ★★★ | 중 | 이중 모델(SAMEO+UOAIS) consensus filter + 가림율 우선 15% 수동 검수 + self-training 반복 |
| R2 | Amodal annotation 비용 과다 | ★★★ | 중 | 전수 annotation 없이 10~30% curated subset 고수, active learning으로 중요 샘플 우선 |
| R3 | Uniform-aware Re-ID 학습 불안정 | ★★ | 중 | Curriculum learning(intra-team loss schedule) + warm-up, gradient clipping |
| R4 | Uncertainty calibration 난이도 | ★★ | 중 | Temperature scaling(post-hoc) + 각 단계 independent validation, Platt scaling 병행 |
| R5 | GPU 자원 제약 (A100×4 확보 실패) | ★★ | 낮~중 | 모듈별 단계 학습(amodal → Re-ID → end-to-end), checkpoint/mixed-precision 활용, cloud 대체 |
| R6 | SoccerNet 라이선스·데이터 접근 | ★ | 낮 | SoccerNet 공식 절차 준수, 대체 데이터(SoccerTrack, SportsMOT) 백업 |
| R7 | Baseline 재현 실패 (성능 차이 >1%) | ★★ | 중 | 저자 코드 우선 사용, 차이가 클 경우 저자 직접 문의, 최소 3회 재현 시도 |
| R8 | 학회 일정 미달 | ★★ | 중 | CVPR 1차 실패 시 ICCV/BMVC/WACV로 전환, workshop+main 이중 전략 |
| R9 | Amodal head가 실시간성 저해 | ★★ | 높 | Online은 경량 head, offline은 full head(post-processing) 이중 구조 |
| R10 | 유의미한 IDF1 gain 달성 실패 | ★★★ | 낮~중 | 각 모듈 개별 논문으로 분리(Plan B) — amodal paper + uniform-aware paper + uncertainty paper |

---

## 9. 학회 투고 전략

### 9.1 Target 학회 비교

| 학회 | 일정 | Track | 적합도 | Target | 비고 |
|------|------|-------|--------|--------|------|
| **CVPR 2027** | 2026-11 마감 | **CVSports Workshop** | ★★★★★ | **1순위** | 축구 MOT/Re-ID 주류, 동 workshop에 P1-1, P3-6 게재 |
| **ICCV 2027** | 2027-03 마감 | Main / Sports | ★★★★ | 2순위 | Main track은 amodal novelty 강조 |
| **ECCV 2026** | 2026-03 마감 | Workshop | ★★★★ | 빠르게 진행 시 검토 | 일정 타이트 |
| **BMVC 2026** | 2026-07 마감 | Main | ★★★ | 중간 투고 | 중형 학회, workshop 대안 |
| **WACV 2027** | 2026-08 마감 | RWS Workshop | ★★★★ | 2순위 | Application 강조, P1-11 게재 실적 |
| **AAAI 2027** | 2026-08 마감 | Main | ★★★ | 3순위 | Uncertainty 측면 강조 가능 |
| **IEEE TMM / PAMI** | 연중 | Journal | ★★★★ | 확장 버전 | 전체 기여 통합 확장판 |

### 9.2 투고 전략
**Dual-track 전략**:
- **Track 1 (primary)**: CVPR 2027 CVSports Workshop에 **전체 프레임워크 논문** 투고(M12, 2027-04 전 제출)
- **Track 2 (extension)**: CVPR main 또는 IJCV/PAMI journal로 확장(additional experiments + 더 깊은 분석)

**Plan B (모듈 분리 투고)**:
- 전체 통합 실험이 지연될 경우, 아래 순서로 개별 발표:
  1. Soccer-Amodal Head 단독 → CVPR CVSports
  2. Uniform-aware Re-ID 단독 → BMVC/WACV
  3. Uncertainty propagation 단독 → ICCV Main / Pattern Recognition

### 9.3 홍보 및 재현성 전략
- Code + Docker image 공개 (GitHub + HuggingFace Models)
- 실험 로그(wandb public), hyperparameter YAML 공개
- 3-minute supplementary video (가림 구간 시각화)
- Blog post (한글·영문) + Twitter/X 공유
- SoccerNet 공식 채널 언급 요청(데이터 제공자 협업)

---

## 10. 참고문헌 요약 (주요 인용)

본 연구의 주요 근거가 되는 **핵심 17편**을 4개 축으로 요약한다. 전체 51편 목록은 `01_literature_review.md`, `02_literature_table.md` 참고.

### 10.1 축구 MOT / 통합 파이프라인 축 (Baseline SOTA)
- **[P1-1]** Cioppa et al., *SoccerNet-Tracking*, CVPR 2022 Workshop — 축구 MOT 공식 벤치마크.
- **[P1-11]** Huang et al., *Iterative Scale-Up ExpansionIoU (Deep-EIoU)*, WACV 2024 W — SportsMOT HOTA 77.2, SoccerNet 85.4, 축구 SOTA baseline.
- **[P1-12]** *GTATrack: Winner Solution to SoccerTrack 2025* — Deep-EIoU + GTA-Link, 축구 fisheye 단일 카메라 SOTA.
- **[P4-6]** Somers et al., *SoccerNet Game State Reconstruction*, CVPR 2024 W — GSR 벤치마크 도입.
- **[P4-7]** *From Broadcast to Minimap*, CVPR 2025 — SoccerNet GSR 2025 Winner, 통합 SOTA.

### 10.2 Occlusion / Tracking 축
- **[P2-3]** Zhang et al., *ByteTrack*, ECCV 2022 — BYTE association, low-score 부활.
- **[P2-5]** Cao et al., *Observation-Centric SORT*, CVPR 2023 — OC-SORT, 가림 구간 motion recovery.
- **[P2-6]** Du et al., *StrongSORT + AFLink + GSI*, IEEE TMM 2023 — Offline post-processing.
- **[P2-7]** Maggiolino et al., *Deep OC-SORT*, 2023 — Adaptive Re-ID weight.
- **[P2-8]** Wang et al., *Repulsion Loss*, CVPR 2018 — 가림 detection loss.
- **[P2-11]** *OATrack: Occlusion-Aware MPT*, MDPI Applied Sciences 2024 — Occlusion rate adaptive Kalman gain, 본 연구 motion 모듈 기반.
- **[P2-15]** *Occlusion-Related GCN for MOT*, IVC 2024 — OR-GCN, 본 연구 association 모듈 기반.

### 10.3 Amodal Perception 축 (모듈 1 근거)
- **[P2-16]** Back et al., *UOAIS: Unseen Object Amodal Instance Segmentation*, ICRA 2022 — Hierarchical visible/amodal/occlusion, Soccer-Amodal Head 구조 기반.
- **[P2-17]** *SAMEO: Segment Anything, Even Occluded*, 2025 — SAM foundation + Amodal-LVIS 300K, pseudo-label 생성 도구.
- **[P2-18]** *Sequential Amodal Diffusion*, 2024 — Uncertainty-aware amodal, offline 보조 모듈 후보.

### 10.4 Re-ID / Jersey 축 (모듈 2·3 근거)
- **[P4-3]** *SoccerNet Re-ID 2022 Winner (Multi-task)*, MMSports 2023 — mAP 86.0, R1 81.5, Uniform-aware Re-ID baseline.
- **[P4-5]** Miao et al., *PGFA: Pose-Guided Feature Alignment*, ICCV 2019 — Pose-guided masking 기반.
- **[P3-4]** Balaji et al., *Keyframe Identification for Jersey*, MMSports 2023 — Keyframe 선별 + STR.
- **[P3-6]** Grad et al., *Single-Stage Uncertainty-Aware Jersey*, CVPR 2025 W — Jersey uncertainty 도입, 모듈 3의 jersey 부분 기반.
- **[P4-9]** Koshkina et al., *Contrastive Learning for Sports Video*, CVPR 2021 W — Team contrastive, 본 연구 intra-team 확장 기반.

---

## 부록 A. 주요 수식 요약

### A.1 Soccer-Amodal Head
$$\mathcal{L}_{\text{amodal}} = \mathcal{L}_{\text{vis}} + \mathcal{L}_{\text{amo}} + \mathcal{L}_{\text{occ}} + 0.5\,\mathcal{L}_{\text{cons}} + 0.3\,\mathcal{L}_u$$
$$u_a = H(M_{\text{amo}}) - H(M_{\text{vis}}), \quad H(M) = -\sum_p M_p \log M_p$$

### A.2 Uniform-aware Re-ID
$$f = \text{concat}(f_{\text{global}}, \sum_p w_p f_p, f_j), \quad w_p = \text{softmax}(v_p/\tau)$$
$$\mathcal{L}_{\text{ReID}} = \mathcal{L}_{\text{ID}} + \mathcal{L}_{\text{triplet}} + 0.5\,\mathcal{L}_{\text{jersey}} + 0.3\,\mathcal{L}_{\text{team}} + 0.5\,\mathcal{L}_{\text{intra}} + 0.2\,\mathcal{L}_{\text{role}}$$

### A.3 Uncertainty Propagation
$$s = \sigma\left(\sum_k w_k \log(1 - u_k)\right), \quad u_k' = \text{softmax}(\text{logits}_k / T_k)$$
$$u_r' = u_r + \beta_{ar} u_a, \quad u_j' = u_j + \beta_{aj} u_a + \beta_{rj} u_r$$
$$d_{ij}^{\text{uw}} = \sum_k \lambda_k (1 - \max(u_{i,k}, u_{j,k})) d_k$$

### A.4 신규 평가 지표
$$\text{Occ-HOTA} = \text{HOTA}|_{\{(t,i): \text{vis-ratio}_{t,i} \le 0.5\}}$$
$$\text{RR} = \frac{|\{\text{가림 후 ID 복구된 tracklet}\}|}{|\{\text{가림 발생 tracklet}\}|}$$
$$\text{ECE} = \sum_{b=1}^{B} \frac{|S_b|}{N} |\text{acc}(S_b) - \text{conf}(S_b)|$$

---

## 부록 B. 실현 가능성 자체 평가 (과대 주장 방지)

본 설계서의 주요 주장에 대해 **과대 주장 여부와 실현 가능성**을 자체 평가한다.

| 주장 | 근거 | 실현 가능성 | 위험 요소 |
|------|------|-----------|----------|
| SoccerNet HOTA +2%, IDF1 +3% | Deep-EIoU+GTA baseline(HOTA 85.4) 기준, 3개 모듈 기여 누적 | 중상 | 모듈 간 간섭 가능 |
| Occ-IDF1 +5~10% (50~80% 가림) | Amodal 기반 가림 구간 특화 설계 | 중 | Occluded-HOTA GT 확보 필요 |
| ECE ≤ 0.10 | Temperature scaling의 보편적 성능 + uncertainty 전파 | 중상 | Graph propagation calibration 난이도 |
| 축구 최초 Amodal 통합 | 문헌 탐색 결과 동일 주제 논문 부재 | 높음 | - |
| 45분 ID switch -30% | Multi-modal gallery + uncertainty-weighted linking | 중 | Long-clip annotation 제약 |
| amodal mIoU ≥ 0.65 | UOAIS mIoU 0.70~0.75(tabletop) 도메인 전이 고려 | 중 | 축구 deformable human gap |

**과대 주장 방지 원칙**: 모든 수치는 **3개 seed 반복, paired t-test, 95% CI**로 보고. 통계적 유의성 없는 차이는 "경향" 수준으로만 기술. Ablation 없이 단일 모듈 효과 강조하지 않음.

---

## 부록 C. 체크리스트 (Harness100 research-designer 프레임워크)

- [x] 입력·출력 형식적 정의
- [x] 제약 조건 명시
- [x] Primary RQ 1개
- [x] Secondary RQs 5개
- [x] 측정 가능 가설 7개 (검증 지표 + 유의 수준)
- [x] 독립·종속·통제 변수 정의
- [x] 전체 아키텍처 다이어그램
- [x] 3개 핵심 기여 모듈 상세 설계 (입출력, 구조, 손실, 수식)
- [x] 데이터셋 (Primary + Secondary + Cross-domain + 자체)
- [x] 표준 + 신규 평가 지표
- [x] Baselines 6개+ (재현 프로토콜)
- [x] Ablation 10개
- [x] 실험 시나리오 5개
- [x] 통계적 유의성 검정
- [x] Hyperparameter 재현성
- [x] 12개월 로드맵 (IMRaD 매핑)
- [x] 예상 기여점 6개
- [x] 리스크·대응 10개
- [x] 학회 투고 전략
- [x] 참고문헌 요약 17편
- [x] 실현 가능성 자체 평가 (과대 주장 방지)

---

**작성 완료.**
본 설계서는 Phase 1~2 산출물(51편 문헌, 20개 기법 분석, 4개 조합 파이프라인)에서 권장된 **방향 A (조합 3 기반)**를 중심축으로, Harness100 research-designer 프레임워크와 IMRaD 인지 설계를 적용하여 축구 영상 가림 상황 선수 식별 성능 개선을 위한 **AmoUni-SoccerTrack** 연구 설계를 구체화한다. 다음 Phase 4(실험 수행 및 논문 작성) 단계에서 본 설계서를 기반으로 12개월 로드맵을 실행한다.
