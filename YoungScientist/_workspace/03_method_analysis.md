# 단일 카메라 가림 상황 선수 식별 기법 심층 분석

**작성일:** 2026-04-16
**작성자:** method-analyzer 에이전트
**입력:** `01_literature_review.md` (51편), `02_literature_table.md`
**제약 조건:** 단일 카메라 영상 데이터 / 선수 간 가림(occlusion) 상황 식별 성능 향상

---

## 0. 분석 개요

### 0.1 필터링 기준
다음 4가지 기준으로 51편 중 유망 기법을 선별:

| 기준 | 설명 |
|------|------|
| **C1. 단일 카메라 적용 가능** | Multi-camera 전용 기법(예: P4-1) 제외. Broadcast 단일 시점, fixed single camera, fisheye(1대) 포함 |
| **C2. 가림 관련성** | "직접" 표기된 논문 우선, "간접"은 기여도 명확한 경우만 포함 |
| **C3. 실증된 성능 개선** | MOT17/20/DanceTrack/SportsMOT/SoccerNet 등 공개 벤치마크 수치 제공 |
| **C4. 재현 가능성** | 코드/데이터/사전학습 가중치 공개, 또는 재구현 난이도가 낮은 구조 |

### 0.2 제외 목록 (필터링 결과)
- **P4-1** (Multi-camera Multi-player, Li 2020): 다중 카메라 전용 → 제외 (비교용 언급만)
- **P1-3** (TeamTrack, Scott 2024): top-view drone + fisheye side view **조합(2대)** 이므로 단일 카메라 요건에 부적합 → 데이터셋으로만 참고
- **P2-21** (MCTrack, 2024): 3D LiDAR+BEV+이미지 융합 → 단일 2D 카메라엔 직접 적용 불가 → **개념(BEV↔image dual matching)만 차용**
- **P1-7** (Self-Supervised Small Soccer): 가림 처리 기여 약함 → 제외
- **P3-2, P3-9** (초기 CNN, ResNet+LSTM): SOTA 대비 열위 → 제외
- **P2-9, P2-10, P4-8** (서베이): 기법 자체가 아님 → 배경 자료로만 활용

### 0.3 선별 결과
- **최종 선별:** 20개 기법
- **카테고리 분포:** Detection-level 3, Motion-level 3, Association-level 4, Appearance/Re-ID 4, Amodal 3, Post-processing 1, Integrated 2

### 0.4 분석 방법론
각 기법에 대해 (A) 3줄 에센스 + (B) 5차원 정량 평가(1~5점) + (C) 축구 도메인 전이 도전과제를 제시. 카테고리별 강약점 비교 후 통계적 비교 표와 조합 파이프라인을 도출.

---

## 1. 선별 기법 목록 (최종 20개)

| ID | 기법명 | 카테고리 | 핵심 아이디어 | 원 도메인 | 축구 전이 |
|----|-------|---------|--------------|----------|----------|
| M1 | Repulsion Loss (P2-8) | A. Detection | RepGT+RepBox loss로 인접 객체 혼동 감소 | 보행자 군중 | ★★★★ |
| M2 | Head-focus Joint Detector (P2-12) | A. Detection | 머리+몸 joint detection + SoftNMS | 군중 | ★★★ |
| M3 | Occlusion-Aware Spatial Attention Transformer (P2-13) | A. Detection | Spatial attention으로 가림 영역 억제 | 일반 객체 | ★★★ |
| M4 | OC-SORT (P2-5) | B. Motion | Observation-centric re-update, virtual trajectory | 보행자/댄스 | ★★★★★ |
| M5 | OATrack (P2-11) | B. Motion | Occlusion rate 추정 → adaptive Kalman gain | 보행자 | ★★★★★ |
| M6 | BoT-SORT CMC (P2-4, motion 부분) | B. Motion | Camera Motion Compensation + 확장 Kalman state | 보행자 | ★★★★ |
| M7 | ByteTrack BYTE (P2-3) | C. Association | 모든 detection box 활용 (low-score 부활) | 일반 MOT | ★★★★★ |
| M8 | GCN-based Association (P2-14) | C. Association | GCN affinity + pose feature | 일반 MOT | ★★★★ |
| M9 | Occlusion-Related GCN (P2-15) | C. Association | Graph edge에 occlusion attribute | 일반 MOT | ★★★★ |
| M10 | Deep-EIoU (P1-11) | C. Association | Expansion IoU + deep Re-ID (motion-agnostic) | 스포츠 | ★★★★★ |
| M11 | DeepSORT (P2-2) | D. Re-ID | CNN appearance + cascade matching | 일반 MOT | ★★★ |
| M12 | Deep OC-SORT (P2-7) | D. Re-ID | OC-SORT + adaptive Re-ID weight | 보행자 | ★★★★★ |
| M13 | PGFA (P4-5) | D. Re-ID | Pose keypoint로 가림 영역 attention 억제 | 가림 Re-ID | ★★★★ |
| M14 | Sports Re-ID Part-based (P4-2) + Pose-alignment (P4-4) | D. Re-ID | Part-based + team-aware sampling | 축구 방송 | ★★★★★ |
| M15 | UOAIS Hierarchical Amodal (P2-16) | E. Amodal | Visible/Amodal/Occlusion 3-mask 계층 | 로봇 scene | ★★★ |
| M16 | SAMEO (P2-17) | E. Amodal | SAM foundation + Amodal-LVIS 300K | 일반 amodal | ★★★ |
| M17 | Sequential Amodal Diffusion (P2-18) | E. Amodal | Diffusion iterative + cumulative mask + uncertainty | 일반 amodal | ★★★ |
| M18 | StrongSORT + AFLink + GSI (P2-6) | F. Post-processing | Offline tracklet linking + Gaussian interpolation | 보행자 | ★★★★★ |
| M19 | GTA-Link (P1-12) | F/G. Post+Integrated | Appearance + spatio-temporal global tracklet clustering | 축구 fisheye | ★★★★★ |
| M20 | SoccerNet GSR Pipeline (P4-6, P4-7) + Multi-task Re-ID (P4-3) + Single-Stage Uncertainty Jersey (P3-6) + Keyframe Jersey (P3-4) | G. Integrated | 통합 파이프라인 (detect + track + Re-ID + jersey + team) | 축구 broadcast | ★★★★★ |

---

## 2. 카테고리별 기법 심층 분석

### 2.A Detection-level

#### M1. Repulsion Loss (P2-8)
**A. 에센스**
- 핵심: Attraction(GT) + RepGT(다른 GT로부터 멀어짐) + RepBox(다른 예측과 분리) loss를 결합.
- 혁신: NMS 이전 단계에서 인접 객체 간 경계를 학습에 주입.
- 축구 전이: 같은 팀 선수 박스가 서로 밀착될 때 IoU-NMS 오제거 방지에 즉시 활용 가능.

**B. 5차원 평가**
| 차원 | 점수 | 근거 |
|------|------|------|
| 정확도 | 4 | CityPersons, CrowdHuman 가림 구간 SOTA (당시) |
| 가림 강건성 | 5 | 가림 대응이 loss의 명시적 목표 |
| 실시간성 | 5 | Loss만 수정, 추론 비용 동일 |
| 단일카메라 | 5 | Detector 학습 단계만 수정 |
| 조합성 | 5 | YOLOv5/8, RT-DETR 모든 detector에 적용 가능 |
| **총점** | **24/25** | |

**C. 축구 전이 도전과제**
- **데이터 차이**: 보행자는 주로 수직 방향 가림, 축구는 수평·비스듬 가림이 많음 → RepGT threshold 재튜닝 필요.
- **수정 필요**: 공 탐지에는 반대로 가까운 선수 박스가 ball을 포함하는 경우가 많아 RepBox를 클래스별 분리.
- **예상 성능**: SoccerNet-Tracking detection mAP +1.5~3%, 밀집 상황 missed detection -10~20%.

---

#### M2. Head-focus Joint Detector (P2-12)
**A. 에센스**
- 핵심: 몸통은 심하게 가려지지만 머리는 상대적으로 덜 가려짐을 이용 → anchor-free joint head-body detection + SoftNMS.
- 혁신: 머리 박스를 body 박스의 보조 단서로 활용.
- 축구 전이: 코너킥, 페널티 박스 내 스크럼 상황에 특히 유효.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 4 (MOT20, HT21 개선) |
| 가림 강건성 | 5 |
| 실시간성 | 3 (head branch 추가 비용) |
| 단일카메라 | 5 |
| 조합성 | 4 (detector 구조 수정 필요) |
| **총점** | **21/25** |

**C. 축구 전이 도전과제**
- **데이터 차이**: 축구 방송 영상에서 머리 해상도가 보행자 영상보다 작음(롱샷) → head proposal 재학습 필요.
- **수정 필요**: 축구는 헤더 동작 시 머리끼리도 가림 → head-to-head repulsion 추가.
- **예상 성능**: 방송 카메라 원거리 샷에서 head cue 효과 제한적(~+1%). 홈경기 고정카메라에서는 +3~5% 기대.

---

#### M3. Occlusion-Aware Spatial Attention Transformer (P2-13)
**A. 에센스**
- 핵심: Spatial attention이 가림 영역에 낮은 weight 부여하도록 occlusion-aware loss로 지도.
- 혁신: Attention 자체를 가림 감지에 활용.
- 축구 전이: detector backbone이나 Re-ID backbone 어느 쪽에도 plug-in 가능.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 3 (벤치마크 수치 제한적) |
| 가림 강건성 | 4 |
| 실시간성 | 3 |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **20/25** |

**C. 축구 전이 도전과제**
- 가림 영역 GT(ground truth) 생성이 축구 데이터셋에 없음 → self-supervised 또는 amodal mask(M15~17) 기반 pseudo-GT 생성이 선결과제.

---

### 2.B Motion-level

#### M4. OC-SORT (P2-5)
**A. 에센스**
- 핵심: 가림 구간 동안 누적되는 Kalman 예측 오류를, 가림 복귀 직후 관측을 기준으로 virtual trajectory를 역추적해 상태를 복원 (observation-centric re-update).
- 혁신: Process noise 의존도 감소, 비선형·fast motion에 강건.
- 축구 전이: 선수의 급가속/방향 전환 + 가림 복합 상황에 직접 적용 가능.

**B. 5차원 평가**
| 차원 | 점수 | 근거 |
|------|------|------|
| 정확도 | 5 | MOT17/20, DanceTrack SOTA |
| 가림 강건성 | 5 | 가림 구간 복구가 설계 목표 |
| 실시간성 | 5 | 700+ FPS (CPU) |
| 단일카메라 | 5 | 단일 카메라 설계 |
| 조합성 | 5 | ByteTrack/Deep OC-SORT 조합 표준화됨 |
| **총점** | **25/25** |

**C. 축구 전이 도전과제**
- **데이터 차이**: DanceTrack의 댄서 궤적과 축구 선수 궤적이 유사(비선형·가림) → 전이 부담 낮음.
- **수정 필요**: 공 근처에서의 군집 + 방송 카메라 pan/tilt → CMC(M6) 병용 권장.
- **예상 성능**: SoccerNet-Tracking HOTA +2~4% vs SORT baseline.

---

#### M5. OATrack (P2-11)
**A. 에센스**
- 핵심: Occlusion Perception Module이 가림율을 예측 → Kalman innovation gain과 association cue weight를 adaptively 조정.
- 혁신: 가림율을 **연속 변수로** 다루어 SORT 계열의 binary 매칭 한계 극복.
- 축구 전이: 같은 팀 선수끼리의 부분 가림이 많은 축구에 가림율 기반 weighting이 적합.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 4 |
| 가림 강건성 | 5 (핵심 설계) |
| 실시간성 | 4 |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **23/25** |

**C. 축구 전이 도전과제**
- Occlusion rate GT가 축구에 없어 self-supervised 또는 amodal 기반 pseudo-label이 필요.
- Jersey recognition의 uncertainty(P3-6)와 직접 결합 가능성 높음 → **신규성 ③과 직결**.

---

#### M6. BoT-SORT Camera Motion Compensation (P2-4, motion 부분)
**A. 에센스**
- 핵심: ORB-like keypoint + RANSAC로 카메라 motion을 매 프레임 보상 + Kalman state vector 확장(w, h 포함).
- 혁신: 팬/틸트 방송 카메라의 apparent motion을 제거.
- 축구 전이: 방송 시점(pan·zoom·tilt)에서 필수.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 4 |
| 가림 강건성 | 3 (가림 직접 대응 아님, 간접) |
| 실시간성 | 4 |
| 단일카메라 | 5 (방송 카메라에 특히 유용) |
| 조합성 | 5 |
| **총점** | **21/25** |

**C. 축구 전이 도전과제**
- 관중석·광고판 keypoint가 잘못된 motion 추정을 유발할 수 있음 → 필드 homography 제한으로 보강.

---

### 2.C Association-level

#### M7. ByteTrack BYTE (P2-3)
**A. 에센스**
- 핵심: 모든 detection box를 활용 — high-score로 primary match 후, low-score로 unmatched tracklet 보충 (가림 객체는 low-score일 가능성 큼).
- 혁신: Detector threshold에 민감했던 기존 관행 타파.
- 축구 전이: 선수 부분 가림 시 confidence 하락 → BYTE가 자연스럽게 회복.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 5 (MOT17 HOTA 63.1, IDF1 77.3) |
| 가림 강건성 | 5 |
| 실시간성 | 5 (추가 비용 거의 없음) |
| 단일카메라 | 5 |
| 조합성 | 5 (9개 SOTA tracker에 적용 시 IDF1 +1~10) |
| **총점** | **25/25** |

**C. 축구 전이 도전과제**
- **데이터 차이**: 축구는 배경 false positive(광고판 로고 등)가 많아 low-score에 noise 혼입 가능 → secondary matching에 pose/team color 필터 추가 권장.
- **예상 성능**: SoccerNet-Tracking HOTA 72% → 80%+ 기대(이미 baseline).

---

#### M8. GCN-based Association (P2-14)
**A. 에센스**
- 핵심: 탐지 객체를 노드로, affinity를 edge로 한 GCN으로 association matrix를 학습. Pose feature가 부분 가림에 강건.
- 혁신: Hungarian 휴리스틱 대신 end-to-end 학습된 association.
- 축구 전이: 팀 구조(4-4-2 포메이션) 등 선수 간 공간 관계를 그래프로 표현 가능.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 4 (MOT16 MOTA 80.6, MOT17 HOTA 65.3) |
| 가림 강건성 | 4 |
| 실시간성 | 3 (GCN 추가 비용) |
| 단일카메라 | 5 |
| 조합성 | 4 |
| **총점** | **20/25** |

**C. 축구 전이 도전과제**
- 축구 특화 **팀 그래프**(같은 팀 노드 간 edge 가중) 추가 시 잠재력 큼 → 공백 ②와 연결.

---

#### M9. Occlusion-Related GCN (P2-15)
**A. 에센스**
- 핵심: 그래프 edge에 "occlusion attribute"를 명시적으로 부여 — 가림 관계가 있는 쌍은 별도 attention.
- 혁신: Occlusion을 association graph의 first-class citizen으로 승격.
- 축구 전이: 가림 관계를 명시한 최신 GNN을 축구에 적용한 사례 없음 → 신규성 기회.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 4 |
| 가림 강건성 | 5 |
| 실시간성 | 3 |
| 단일카메라 | 5 |
| 조합성 | 4 |
| **총점** | **21/25** |

**C. 축구 전이 도전과제**
- Occlusion edge label을 축구 데이터에 부여하는 비용 → amodal module(M15~17)로 pseudo-label 생성.

---

#### M10. Deep-EIoU (P1-11)
**A. 에센스**
- 핵심: ExpansionIoU를 iterative하게 확장하며 deep Re-ID feature와 결합 → motion에 둔감한 매칭.
- 혁신: 선수의 빠른 비선형 움직임으로 IoU가 0이 되는 구간을 EIoU로 연장.
- 축구 전이: SportsMOT HOTA 77.2%, SoccerNet-Tracking 85.4% — **축구 도메인 실증 검증됨**.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 5 (SportsMOT/SoccerNet SOTA) |
| 가림 강건성 | 4 |
| 실시간성 | 4 |
| 단일카메라 | 5 |
| 조합성 | 5 (GTA-Link과 표준 조합) |
| **총점** | **23/25** |

**C. 축구 전이 도전과제**
- 이미 축구 도메인에서 검증되었으므로 전이 부담 최소. Expansion ratio의 hyperparameter tuning만 필요.

---

### 2.D Appearance / Re-ID

#### M11. DeepSORT (P2-2)
**A. 에센스**
- 핵심: SORT에 CNN appearance embedding + cascade matching 추가. Mahalanobis + cosine similarity 결합.
- 혁신: 짧은 가림 시에도 appearance feature가 identity 유지.
- 축구 전이: 같은 유니폼 → appearance 변별력 낮음이라는 **구조적 한계** 존재.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 3 (현재 SOTA 대비 하위) |
| 가림 강건성 | 3 (축구 유니폼 유사성 문제) |
| 실시간성 | 4 |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **20/25** |

**C. 축구 전이 도전과제**
- Sports Re-ID(M14)로 교체 또는 fine-tuning 필수.

---

#### M12. Deep OC-SORT (P2-7)
**A. 에센스**
- 핵심: OC-SORT motion에 adaptive Re-ID weight 추가 — appearance confidence가 높을 때만 Re-ID feature를 강하게 반영.
- 혁신: Noise 상황에서 appearance 오용 방지.
- 축구 전이: 유사 유니폼 상황에서 Re-ID confidence를 team/jersey로 조정 가능.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 5 (MOT17/20 HOTA SOTA) |
| 가림 강건성 | 5 |
| 실시간성 | 4 |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **24/25** |

**C. 축구 전이 도전과제**
- Adaptive weight 함수를 jersey uncertainty(P3-6)와 결합 → 축구 특화 확장.

---

#### M13. PGFA (P4-5)
**A. 에센스**
- 핵심: Pose keypoint visibility로 가림 영역 attention을 억제하여 visible part만 매칭.
- 혁신: Occluded-Duke 등 가림 Re-ID 벤치마크의 baseline.
- 축구 전이: 축구는 관중석·광고판·선수-선수 가림이 모두 발생 → pose-guided masking 유효.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 4 |
| 가림 강건성 | 5 |
| 실시간성 | 3 (pose estimator 추가) |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **22/25** |

**C. 축구 전이 도전과제**
- 축구 선수의 격렬한 자세(슬라이딩, 점프)에서 pose estimator 실패율 증가 → sports-specific pose(예: MMPose sport) 필요.

---

#### M14. Sports Re-ID Part-based (P4-2) + Pose Alignment (P4-4) + Multi-task (P4-3)
**A. 에센스**
- 핵심 (통합): Part-based embedding + team-aware sampling + pose-based alignment + jersey·team·role multi-task head. SoccerNet Re-ID 2022 mAP 86.0 / Rank-1 81.5.
- 혁신: 축구 도메인에 맞춘 Re-ID 전용 조합.
- 축구 전이: 이미 축구에서 검증됨. Uniform-aware로의 확장이 연구 공백 ②의 중심.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 5 |
| 가림 강건성 | 4 |
| 실시간성 | 3 |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **22/25** |

**C. 축구 전이 도전과제**
- Uniform 색상 외 번호, 신발 색, 머리 색 등 fine-grained 단서 통합이 미흡. Hand/arm pose 동적 단서를 결합한 확장 연구 공백.

---

### 2.E Amodal Perception

#### M15. UOAIS Hierarchical Amodal (P2-16)
**A. 에센스**
- 핵심: Visible mask + Amodal mask + Occlusion mask를 계층적으로 예측 — 가려진 영역의 형태를 복원.
- 혁신: 가림 처리를 **생성 문제**로 재정의.
- 축구 전이: 축구 amodal 적용 사례 없음 → **공백 ①의 핵심 후보**.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 3 (로봇 tabletop에서 SOTA, 축구 미검증) |
| 가림 강건성 | 5 |
| 실시간성 | 2 (추가 mask head 비용) |
| 단일카메라 | 5 |
| 조합성 | 4 |
| **총점** | **19/25** |

**C. 축구 전이 도전과제**
- **데이터 차이**: Tabletop(정적 object) ↔ 축구(deformable human) → 도메인 갭 매우 큼.
- **수정 필요**: Pose-aware amodal — pose skeleton을 prior로 투입 시 효과적.
- **예상 성능**: Pseudo-label 생성 도구로서의 가치가 직접 segmentation 성능보다 큼.

---

#### M16. SAMEO (P2-17)
**A. 에센스**
- 핵심: SAM foundation model에 Amodal-LVIS 300K로 fine-tuning하여 가림 영역까지 세그먼트.
- 혁신: Foundation model 스케일로 일반화.
- 축구 전이: Zero/few-shot으로 축구 선수 amodal mask 생성 잠재력.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 4 |
| 가림 강건성 | 5 |
| 실시간성 | 2 (SAM 무거움) |
| 단일카메라 | 5 |
| 조합성 | 4 |
| **총점** | **20/25** |

**C. 축구 전이 도전과제**
- 실시간 요구사항과 상충 → **오프라인 pseudo-label 생성**에 활용 권장.
- MobileSAM 등 경량화 버전 사용 고려.

---

#### M17. Sequential Amodal Diffusion (P2-18)
**A. 에센스**
- 핵심: Diffusion 모델의 iterative refinement + cumulative mask로 invisible 영역의 **uncertainty를 명시적으로 모델링**.
- 혁신: Amodal에 uncertainty 개념 도입.
- 축구 전이: Jersey recognition uncertainty(P3-6)와 결합 → **공백 ③의 유력 후보**.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 3 |
| 가림 강건성 | 5 |
| 실시간성 | 1 (diffusion은 매우 느림) |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **19/25** |

**C. 축구 전이 도전과제**
- 실시간 불가 → 오프라인 tracklet-level 보조 모듈로 활용.
- Uncertainty가 downstream uncertainty propagation의 입력이 됨.

---

### 2.F Post-processing

#### M18. StrongSORT + AFLink + GSI (P2-6)
**A. 에센스**
- 핵심: Online DeepSORT → offline AFLink(appearance-free tracklet linking) → GSI(Gaussian-Smoothed Interpolation)로 ID switch 회복 + 궤적 평활화.
- 혁신: Online/offline 분리 설계로 실시간성과 정확도 양립.
- 축구 전이: 경기 후 분석(post-match analysis)에 직접 유용.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 5 (MOT17/20 HOTA·IDF1 1위) |
| 가림 강건성 | 5 (AFLink이 장기 가림 복구) |
| 실시간성 | 4 (online 부분 실시간) |
| 단일카메라 | 5 |
| 조합성 | 5 |
| **총점** | **24/25** |

**C. 축구 전이 도전과제**
- AFLink은 appearance-free(motion+time만)이라 축구의 유사 유니폼 환경에 강점 → 즉시 전이 가능.

---

### 2.G Integrated

#### M19. GTA-Link (P1-12)
**A. 에센스**
- 핵심: Deep-EIoU online tracking 후 offline에서 appearance + spatio-temporal feature로 tracklet clustering → SoccerTrack 2025 우승.
- 혁신: Global 관점의 tracklet association.
- 축구 전이: 이미 축구 fisheye 단일 카메라 환경에서 SOTA.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 5 (SoccerTrack SORT 대비 +6.84%) |
| 가림 강건성 | 5 |
| 실시간성 | 4 (offline) |
| 단일카메라 | 5 (fisheye 단일 카메라에서 검증) |
| 조합성 | 5 |
| **총점** | **24/25** |

**C. 축구 전이 도전과제**
- 이미 축구. 확장 방향: GTA-Link에 jersey number, team classification, uncertainty를 추가하는 멀티모달 링킹.

---

#### M20. Integrated SoccerNet GSR Pipeline
구성: GSR baseline (P4-6) + 2025 Winner (P4-7) + Multi-task Re-ID (P4-3) + Single-Stage Uncertainty Jersey (P3-6) + Keyframe Jersey (P3-4) + Contrastive Team (P4-9)

**A. 에센스**
- 핵심: Detection(YOLOv5m) + camera calib(SegFormer) + tracking(DeepSORT/Deep-EIoU) + Re-ID + jersey + team 전 모듈 통합.
- 혁신: 모든 서브태스크가 end-to-end 가치 체인에 연결.
- 축구 전이: **이 연구의 기본 backbone으로 채택**.

**B. 5차원 평가**
| 차원 | 점수 |
|------|------|
| 정확도 | 5 (SoccerNet GSR SOTA) |
| 가림 강건성 | 4 (개별 모듈 강도에 의존) |
| 실시간성 | 3 |
| 단일카메라 | 5 (Broadcast 단일 카메라) |
| 조합성 | 5 |
| **총점** | **22/25** |

**C. 축구 전이 도전과제**
- 각 모듈을 **가림 인식 버전으로 업그레이드**해야 occlusion 강건성 ↑ → 본 연구의 기여 지점.

---

## 3. 기법 정량 비교 (Statistical Analysis)

### 3.1 벤치마크 성능 표

#### MOT17/MOT20 (일반 보행자)
| 기법 | MOTA | IDF1 | HOTA | FPS | Occlusion 전용 |
|------|------|------|------|-----|----------------|
| SORT (P2-1) | - | - | - | 260 | ✗ |
| DeepSORT (P2-2) | - | - | - | ~50 | ○ |
| ByteTrack (P2-3) | **80.3** | 77.3 | 63.1 | ~30 | ○ |
| BoT-SORT (P2-4) | **80.5** | 80.2 | 65.0 | ~25 | ○ |
| OC-SORT (P2-5) | - | - | - | **700** | ◎ |
| StrongSORT (P2-6) | - | SOTA+1.3~2.2 | SOTA | ~15 | ◎ |
| Deep OC-SORT (P2-7) | - | - | SOTA | ~20 | ◎ |
| GCN Association (P2-14) | 81.1 (MOT17) | - | 65.3/65.1 | - | ○ |
| FairMOT (P1-8) | 73.7 | 72.3 | - | ~25 | △ |

#### SportsMOT / SoccerNet-Tracking (스포츠 특화)
| 기법 | SportsMOT HOTA | SoccerNet-Tracking HOTA | 비고 |
|------|----------------|-------------------------|------|
| ByteTrack baseline | - | ~72% | P1-1 |
| MixSort (P1-2) | SOTA | - | Sports SOTA (2023) |
| Deep-EIoU (P1-11) | **77.2** | 85.4 | Sports SOTA (2024) |
| GTATrack (P1-12) | - | SORT +6.84%, Deep-EIoU +3.7% | SoccerTrack 2025 Winner |

#### SoccerNet Jersey / Re-ID
| 기법 | 지표 | 성능 |
|------|------|------|
| Balaji Keyframe (P3-4) | Accuracy | +37.81% vs baseline |
| SoccerNet 2023 Top (P3-7) | Accuracy | 90.09 / 90.95 |
| Multi-task Re-ID Winner (P4-3) | mAP / R1 | 86.0 / 81.5 |
| Contrastive Team (P4-9) | Team class Acc | 94% (1 frame) → 97% (500 frame) |

### 3.2 FPS vs 정확도 트레이드오프
```
[FPS 기준 분류]
- Real-time 초고속 (≥100 FPS):   OC-SORT, SORT
- Real-time (30~100 FPS):         ByteTrack, BoT-SORT, Deep OC-SORT
- Near real-time (10~30 FPS):     Deep-EIoU, StrongSORT, DeepSORT, FairMOT
- Offline/Slow (<10 FPS):         GTA-Link, Amodal modules, Diffusion Amodal
```

단일 카메라 실시간 축구 응용 권장 영역: **30~100 FPS 구간의 ByteTrack/BoT-SORT/Deep OC-SORT + OC-SORT motion module + online Deep-EIoU**.

### 3.3 가림 구간 성능 (정성 추정)

| 기법 | 부분 가림(<50%) | 심각한 가림(50~80%) | 완전 가림(>80%) |
|------|-----------------|---------------------|-------------------|
| SORT | △ | ✗ | ✗ |
| DeepSORT | ○ | △ | ✗ |
| ByteTrack | ○ | ○ | △ |
| OC-SORT | ○ | ○ | ○ (observation-centric 복구) |
| OATrack | ◎ | ○ | △ |
| StrongSORT + AFLink | ◎ | ◎ | ○ |
| Deep-EIoU + GTA | ◎ | ◎ | ○ |
| + Amodal/PGFA | ◎ | ◎ | ◎ (잠재적) |

**관찰**: 기법 조합 없이 단독으로 80%+ 가림을 견디는 기법은 존재하지 않음 → **조합 파이프라인이 필수**.

---

## 4. 조합 파이프라인 제안 (4개)

### 조합 1. 경량-실시간형 (Real-time Broadcast)
```
입력 영상 (Broadcast 1대 카메라)
    │
    ▼
[Detection]  YOLOv8 + Repulsion Loss (M1)
    │
    ▼
[Motion/Association]  OC-SORT (M4) + ByteTrack BYTE (M7) + CMC (M6)
    │
    ▼
[Re-ID]  Sports Re-ID Part-based (M14 경량 버전) + Team color
    │
    ▼
[Jersey]  Single-Stage Uncertainty-Aware (P3-6)
    │
    ▼
출력 (실시간 선수 ID + 번호)
```

- **기대 시너지**: Repulsion Loss로 detection missed 감소 → ByteTrack이 low-score까지 활용 → OC-SORT가 가림 구간 복구 → CMC가 pan/tilt 보상 → Re-ID로 long-term 유지.
- **예상 성능**: SoccerNet-Tracking HOTA 80~82%, 25~30 FPS (GPU V100).
- **구현 난이도**: ★★ (모든 구성 요소 오픈소스).
- **필요 자원**: V100 1장 + SoccerNet-Tracking + SportsMOT pretrain.

---

### 조합 2. 고성능-오프라인형 (Post-match Analysis)
```
입력 영상 (Full 45min 단일 카메라)
    │
    ▼
[Detection]  RT-DETR + Repulsion Loss (M1) + Head-focus head (M2)
    │
    ▼
[Online Tracking]  Deep-EIoU (M10) + BoT-SORT CMC (M6)
    │
    ▼
[Occlusion-aware Re-ID]  Sports Re-ID + PGFA (M13) + Multi-task head (M14)
    │
    ▼
[Offline Linking]  GTA-Link (M19) + AFLink/GSI (M18)
    │
    ▼
[Jersey]  Keyframe identification (P3-4) + Tracklet majority voting (P3-7)
    │
    ▼
[Amodal Refinement (optional)]  SAMEO (M16) + Sequential Amodal Diffusion (M17, uncertainty)
    │
    ▼
출력 (Tracklet ID + jersey + team + uncertainty)
```

- **기대 시너지**: Online + offline 이중 구조로 최대 정확도, amodal이 가림 구간 재구성.
- **예상 성능**: SoccerNet-Tracking HOTA 85~88%, SoccerNet-GSR GS-HOTA SOTA+1~3%.
- **구현 난이도**: ★★★★ (amodal 파인튜닝 필요).
- **필요 자원**: A100 × 2 + SoccerNet-Tracking + SoccerNet-GSR + 자체 amodal pseudo-label 생성.

---

### 조합 3. 신규성 강조형 (Novel Amodal + Uniform-aware)
```
입력 영상
    │
    ▼
[Detection]  YOLOv8 + Repulsion Loss
    │
    ▼
[Amodal Perception]  SAMEO (M16) → Amodal mask + occlusion mask
    │                                  │
    ▼                                  ▼ (uncertainty)
[Motion]  OATrack (M5, occlusion rate = amodal에서 유도)
    │
    ▼
[Association]  Occlusion-Related GCN (M9, edge = amodal occlusion mask)
    │
    ▼
[Uniform-aware Re-ID]  Sports Re-ID Multi-task + Jersey-embedding fusion
                       (PGFA에 pose + jersey number region 모두 투입)
    │
    ▼
[Uncertainty Propagation]  Amodal uncertainty → Re-ID confidence →
                           Jersey uncertainty (P3-6) → Tracklet score
    │
    ▼
[Offline Linking]  GTA-Link (uncertainty-weighted)
    │
    ▼
출력 (Identity + uncertainty-aware prediction)
```

- **기대 시너지**: 축구 amodal(공백 ①) + uniform-aware Re-ID(공백 ②) + uncertainty propagation(공백 ③)을 한 번에 해결.
- **예상 성능**: 기존 대비 심각한 가림(50~80%) 구간 IDF1 +5~10%.
- **구현 난이도**: ★★★★★ (학술적 기여도 최대).
- **필요 자원**: A100 × 4 + 자체 amodal annotation 일부(SAMEO pseudo + 검수) + 긴 학습 일정.

---

### 조합 4. Long-term Identity Consistency형 (공백 ④)
```
입력: Full-match (45분 half) 단일 방송 카메라
    │
    ▼
[Online Backbone]  Deep-EIoU + ByteTrack
    │
    ▼
[Mid-term Recovery]  AFLink + GSI (5~15초 단위)
    │
    ▼
[Long-term Re-ID Galleries]  Tracklet galleries (선수별)
    │     ├─ Jersey number (majority vote from P3-7)
    │     ├─ Team color (contrastive P4-9)
    │     ├─ Body pose fingerprint (P4-4)
    │     └─ Appearance (Sports Re-ID)
    │
    ▼
[Global Linking]  GTA-Link (M19) with multi-modal distance
                  d = w1·appearance + w2·jersey + w3·team + w4·pose
    │
    ▼
[Consistency Resolver]  22 ID cap (한 팀 11명 제약) + Hungarian global assignment
    │
    ▼
출력 (Full-match 22 consistent IDs)
```

- **기대 시너지**: 개별 tracklet은 불완전해도 multi-modal gallery가 full-match 일관성 제공.
- **예상 성능**: 공식 long clip (SoccerNet-Tracking의 1×45min) 에서 IDF1 60→75%+ 기대.
- **구현 난이도**: ★★★★ (데이터 파이프라인·평가 설계 난이도).
- **필요 자원**: A100 × 2 + SoccerNet-Tracking long clip + 자체 45분 annotation 확보 필요(부분).

---

## 5. 신규성 기회 (4개 공백 × 기법 매핑)

### 공백 ① 축구 amodal perception 부재
| 후보 기법 | 어떻게 적용 |
|----------|-------------|
| UOAIS (M15) | Hierarchical visible/amodal/occlusion mask를 선수 segmentation에 확장 |
| SAMEO (M16) | SAM 기반 zero-shot amodal → SoccerNet 영상에 pseudo-label 생성 |
| Sequential Amodal Diffusion (M17) | 가림 구간 번호/몸통의 uncertainty aware 복원 |
| **결합**: SAMEO로 pseudo-label 생성 → UOAIS-like head로 finetune → pose prior 투입 | 축구 특화 amodal 모델 |

### 공백 ② Uniform-aware occlusion disambiguation
| 후보 기법 | 어떻게 확장 |
|----------|-------------|
| Sports Re-ID Part-based (M14, P4-2) | Part 중 "jersey number region"을 별도 head로 강조 |
| Multi-task Re-ID (P4-3) | 기존 jersey+team+role에 "occlusion state"를 추가 head로 |
| PGFA (M13) | Pose-guided masking에 **jersey visibility** 추가 |
| Contrastive Team (P4-9) | Same-team 선수 구별을 위한 intra-team contrastive loss 설계 |
| **결합**: Part-based + pose + jersey region + intra-team contrastive | Uniform-aware Re-ID |

### 공백 ③ Tracklet-level uncertainty propagation
| 후보 기법 | 어떻게 연결 |
|----------|-------------|
| Single-Stage Uncertainty Jersey (P3-6) | Jersey confidence를 tracklet score로 전달 |
| OATrack (M5) | Occlusion rate를 uncertainty로 사용 |
| Sequential Amodal Diffusion (M17) | Mask uncertainty → Re-ID weight |
| Deep OC-SORT adaptive (M12) | Appearance confidence adaptive weight |
| **결합**: 5종 uncertainty를 end-to-end graph로 전파 | Tracklet uncertainty framework |

### 공백 ④ Long-term identity consistency
| 후보 기법 | 어떻게 활용 |
|----------|-------------|
| GTA-Link (M19) | Full-match tracklet clustering |
| AFLink + GSI (M18) | 중기 tracklet linking |
| Multi-task Re-ID (P4-3) | Multi-modal gallery |
| Tracklet-level jersey majority vote (P3-7) | Gallery identity anchor |
| Contrastive Team (P4-9) | Team identity stable |
| **결합**: 조합 4 파이프라인 | Full-match 22 IDs |

---

## 6. 다음 단계 제언 (Phase 3 연구 설계 후보)

### 후보 방향 A. **Amodal + Uniform-aware Soccer Tracker** (조합 3 기반)
- **학술 기여**: 축구 최초 amodal perception 통합 + uniform-aware Re-ID.
- **실험 계획**: SAMEO pseudo-label + SoccerNet-Tracking, baseline = Deep-EIoU + GTA.
- **위험**: Amodal annotation 비용, 학습 일정.
- **예상 임팩트**: CVPR/ICCV-Workshop (CVSports) target, 2편 분리 발표 가능.

### 후보 방향 B. **Occlusion-Aware Tracklet Uncertainty Propagation** (공백 ③)
- **학술 기여**: 처음으로 detection-tracking-Re-ID-jersey 전 파이프라인에 uncertainty를 전파.
- **실험 계획**: OATrack + Deep OC-SORT + Single-Stage Uncertainty Jersey 통합.
- **위험**: Uncertainty calibration 복잡.
- **예상 임팩트**: 신뢰성 있는 경기 분석에 직접 응용, 중형 학회/저널 (Pattern Recognition, IEEE TMM).

### 후보 방향 C. **Long-term Identity Consistency via Multi-modal Gallery** (조합 4 / 공백 ④)
- **학술 기여**: Full-match 22명 일관 ID 공식 벤치마크 수립 제안.
- **실험 계획**: SoccerNet-Tracking 45분 clip + 자체 annotation + GTA-Link 확장.
- **위험**: Annotation 비용 최대.
- **예상 임팩트**: 스포츠 분석 산업에 직접 활용 가치 큼, CVPR Workshop target.

**권장**: **방향 A (조합 3)**이 학술적 참신성과 실현 가능성의 균형이 가장 우수. 방향 B를 공동연구(부가) 목표로 묶어 상호 보완 설계 권장.

---

## 부록: 5차원 평가 전체 표

| ID | 기법명 | 정확도 | 가림강건성 | 실시간성 | 단일카메라 | 조합성 | 총점 |
|----|--------|--------|-----------|---------|-----------|--------|------|
| M1 | Repulsion Loss | 4 | 5 | 5 | 5 | 5 | **24** |
| M2 | Head-focus Joint Detector | 4 | 5 | 3 | 5 | 4 | 21 |
| M3 | Occlusion-Aware Spatial Attn Transformer | 3 | 4 | 3 | 5 | 5 | 20 |
| M4 | OC-SORT | 5 | 5 | 5 | 5 | 5 | **25** |
| M5 | OATrack | 4 | 5 | 4 | 5 | 5 | 23 |
| M6 | BoT-SORT CMC | 4 | 3 | 4 | 5 | 5 | 21 |
| M7 | ByteTrack BYTE | 5 | 5 | 5 | 5 | 5 | **25** |
| M8 | GCN Association | 4 | 4 | 3 | 5 | 4 | 20 |
| M9 | Occlusion-Related GCN | 4 | 5 | 3 | 5 | 4 | 21 |
| M10 | Deep-EIoU | 5 | 4 | 4 | 5 | 5 | 23 |
| M11 | DeepSORT | 3 | 3 | 4 | 5 | 5 | 20 |
| M12 | Deep OC-SORT | 5 | 5 | 4 | 5 | 5 | **24** |
| M13 | PGFA | 4 | 5 | 3 | 5 | 5 | 22 |
| M14 | Sports Re-ID Part+Pose+Multi-task | 5 | 4 | 3 | 5 | 5 | 22 |
| M15 | UOAIS Hierarchical Amodal | 3 | 5 | 2 | 5 | 4 | 19 |
| M16 | SAMEO | 4 | 5 | 2 | 5 | 4 | 20 |
| M17 | Sequential Amodal Diffusion | 3 | 5 | 1 | 5 | 5 | 19 |
| M18 | StrongSORT + AFLink + GSI | 5 | 5 | 4 | 5 | 5 | **24** |
| M19 | GTA-Link | 5 | 5 | 4 | 5 | 5 | **24** |
| M20 | SoccerNet GSR Integrated | 5 | 4 | 3 | 5 | 5 | 22 |

**총점 상위 5개 (조합 추천)**: M4 OC-SORT, M7 ByteTrack (공동 25점) > M1 Repulsion Loss, M12 Deep OC-SORT, M18 StrongSORT, M19 GTA-Link (공동 24점)

---

**작성 완료.** 본 분석은 Phase 3 연구 설계에서 후보 방향 A (Amodal + Uniform-aware Soccer Tracker) 를 1순위로 권장하며, 조합 3 파이프라인을 출발점으로 삼아 3개의 연구 공백(①②③)을 동시에 다루는 통합 연구 설계를 제안한다.
