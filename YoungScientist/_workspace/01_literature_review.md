# 축구 영상 선수 식별 + 가림 처리 문헌 탐색 보고서

**작성일:** 2026-04-16  
**작성자:** soccer-vision-reviewer 에이전트  
**목적:** 단일 카메라 축구 영상에서 선수 탐지·추적·등번호 인식 연구의 문헌 기반 마련. 특히 가림(occlusion) 문제는 축구뿐 아니라 보행자 추적, 자율주행, 군중 분석 등 범용 도메인을 포괄하여 탐색.

---

## 1. 탐색 개요

### 1.1 탐색 범위
- **Stage 1 (HIGH):** 축구/스포츠 선수 탐지 + 다중 객체 추적 (MOT)
- **Stage 2 (HIGH):** 가림(Occlusion) 처리 — 축구에 국한하지 않고 보행자 추적, 자율주행, 군중 분석, 일반 MOT, 재식별 등 범용 도메인 포함
- **Stage 3 (HIGH):** 등번호 인식 (Jersey Number Recognition)
- **Stage 4 (MEDIUM):** 선수 재식별 (Re-ID) + 통합 파이프라인

### 1.2 탐색 방법
- **Semantic Scholar API** (graph/v1/paper/search)
- **OpenAlex API**
- **WebSearch** (arxiv, CVF Open Access, Springer, IEEE Xplore, MDPI, Nature Scientific Reports 등 학술 소스 우선)
- 주요 학회: CVPR, ICCV, ECCV, CVPR-Workshops (CVSports, CVsports), WACV, AAAI, IROS, ICRA
- 주요 저널: IJCV, PAMI, TMM, Pattern Recognition, The Visual Computer, Scientific Reports, MDPI Applied Sciences

### 1.3 수집 규모
- **총 수집 논문: 48편** (Stage 1: 12, Stage 2: 15, Stage 3: 9, Stage 4: 8, 데이터셋/서베이: 4)

### 1.4 핵심 발견
1. 축구 특화 MOT는 **빠른 비선형 동작, 균일한 유니폼, 빈번한 가림**으로 일반 MOT(MOT17/20)보다 협회(association)가 훨씬 어렵다.
2. 최신 SOTA 트래커는 **BoT-SORT / OC-SORT / StrongSORT / Deep-EIoU + GTA** 계열이며, 2023년 이후는 Global Tracklet Association과 GNN 기반 후처리가 대세다.
3. Occlusion 처리는 (i) 탐지 단계의 **repulsion loss / attention / head-body joint detection**, (ii) 추적 단계의 **observation-centric motion recovery / occlusion-aware Kalman gain**, (iii) 재식별 단계의 **pose-guided feature alignment / mask suppression** 세 축으로 구성된다.
4. **Amodal instance segmentation**은 가려진 부분까지 복원하는 연구 분야로 축구 적용 사례는 아직 거의 없으며, 본 연구의 신규성 확보 기회.
5. 등번호 인식은 tracklet 수준 통합 (keyframe identification + scene text recognition + temporal aggregation)이 SoccerNet 2023에서 **~91% accuracy**를 달성했고, 2025 CVPRW에서 uncertainty-aware single-stage 접근이 등장.

---

## 2. Stage 1: 축구/스포츠 선수 탐지 + MOT

### [P1-1] Cioppa et al., 2022 — SoccerNet-Tracking
- **제목:** SoccerNet-Tracking: Multiple Object Tracking Dataset and Benchmark in Soccer Videos
- **저자:** Anthony Cioppa, Silvio Giancola et al.
- **학회:** CVPR 2022 Workshop (CVSports)
- **연구분야:** Stage 1 (축구 MOT 벤치마크)
- **문제정의:** 축구 영상에서 선수·심판·공의 다중 객체 추적을 위한 대규모 공개 벤치마크 부재.
- **접근법:** 200개 시퀀스(각 30초) + 1개 45분 하프타임 시퀀스. 8개 클래스(left/right player, goalkeeper, 심판, 부심, 스태프, 공) 바운딩 박스 + tracklet ID 주석.
- **모델:** ByteTrack, StrongSORT 등 기존 트래커 베이스라인 평가.
- **데이터셋:** SoccerNet-Tracking (1080p).
- **성능지표:** 주 메트릭 HOTA (DetA + AssA 분해). ByteTrack baseline HOTA ~72% 수준.
- **기여점:** 축구 MOT 공식 벤치마크 수립, fast motion · 심각한 가림 상황에서 성능 부족 문제 정량화.
- **Occlusion 관련성:** 직접 (severe occlusion 시나리오 포함).
- **URL:** https://arxiv.org/abs/2204.06918

### [P1-2] Cui et al., 2023 — SportsMOT
- **제목:** SportsMOT: A Large Multi-Object Tracking Dataset in Multiple Sports Scenes
- **저자:** Yutao Cui et al.
- **학회:** ICCV 2023
- **연구분야:** Stage 1 (스포츠 MOT 벤치마크)
- **문제정의:** 농구·배구·축구를 포괄하는 대규모 MOT 데이터셋 부재, 빠르고 가변적인 움직임 + 비슷한 외관이라는 고유 난제.
- **접근법:** 240개 시퀀스, 150K+ 프레임, 1.6M+ 바운딩 박스. 학습/검증/테스트 = 45/45/150.
- **모델:** MixSort (MixFormer-like auxiliary association).
- **데이터셋:** SportsMOT.
- **성능지표:** HOTA, IDF1. MixSort가 SportsMOT·MOT17에서 SOTA.
- **기여점:** "객체 연관(association)"이 sports MOT의 핵심 난제임을 정량 증명.
- **Occlusion 관련성:** 직접 (선수 간 가림 빈번).
- **URL:** https://arxiv.org/abs/2304.05170

### [P1-3] Scott et al., 2024 — TeamTrack
- **제목:** TeamTrack: A Dataset for Multi-Sport Multi-Object Tracking in Full-pitch Videos
- **저자:** Atom Scott, Uchida et al.
- **학회:** CVPR 2024 Workshop (CVsports)
- **연구분야:** Stage 1 (team sport MOT, trajectory GNN)
- **문제정의:** 축구·농구·핸드볼 풀 핏치(top-view drone + fisheye side view) 전역 추적 부재.
- **접근법:** 4M+ 바운딩 박스. GNN 기반 trajectory forecasting을 MOT에 통합.
- **모델:** YOLOv8 + LSTM/GNN forecaster.
- **데이터셋:** TeamTrack.
- **성능지표:** HOTA, IDF1, MOTA (논문 내 벤치마크 표 제공).
- **기여점:** 다중 종목 · 다중 시점 · 전체 필드 대상 벤치마크, GNN 궤적 예측 통합.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/2404.13868

### [P1-4] Naik et al., 2024 — Soccer Tracking Survey
- **제목:** A Survey on Soccer Player Detection and Tracking with Videos
- **학회/저널:** The Visual Computer (Springer), 2024
- **연구분야:** Stage 1 (서베이)
- **문제정의:** 축구 영상 탐지·추적 기법 체계적 정리 필요.
- **접근법:** Detection 방법(YOLO, Faster R-CNN 등) + Tracking 방법(DeepSORT, ByteTrack, SportsMOT, TeamTrack) 분류, preprocessing/postprocessing 체계화.
- **기여점:** 축구 영상 MOT의 challenge를 정리 — 선수들이 비슷한 유니폼과 예측 불가능한 동작으로 tracking 난이도를 높임.
- **Occlusion 관련성:** 직접 (리뷰).
- **URL:** https://link.springer.com/article/10.1007/s00371-024-03367-6

### [P1-5] Wang, 2025 — YOLOv5 + DeepSORT 축구 추적
- **제목:** Enhancing the Performance and Accuracy in Real-Time Football and Player Detection Using Upgraded YOLOv5 Architecture
- **저자:** Wang
- **저널:** International Journal of Computational Intelligence Systems (Springer), 2024/2025
- **연구분야:** Stage 1
- **문제정의:** 축구 방송 영상에서 낮은 해상도, motion blur, occlusion 상황에서 선수/공 탐지 정확도 저하.
- **접근법:** YOLOv5에 attention mechanism 추가 + DeepSORT 통합.
- **성능지표:** 선수 탐지 mAP 97.7%, 공 탐지 mAP 65.3% (dual-model framework).
- **Occlusion 관련성:** 직접.
- **URL:** https://link.springer.com/article/10.1007/s44196-024-00565-x

### [P1-6] Enhanced Dual-Model Framework, 2025
- **제목:** Enhanced Dual-Model Framework for Precision Player Tracking and Ball Detection in Soccer Videos
- **저널:** The Visual Computer (Springer), 2025
- **연구분야:** Stage 1
- **문제정의:** 선수와 공은 크기·속도가 달라 단일 모델로 동시 탐지 시 성능 저하.
- **접근법:** 선수용과 공용 별도 모델 + 공유 특징 추출.
- **성능지표:** 선수 mAP 97.7%, 공 mAP 65.3%.
- **Occlusion 관련성:** 직접.
- **URL:** https://link.springer.com/article/10.1007/s00371-025-04118-x

### [P1-7] Self-Supervised Small Soccer Player Detection, 2020
- **제목:** Self-Supervised Small Soccer Player Detection and Tracking
- **학회:** ACM MMSports 2020
- **연구분야:** Stage 1
- **문제정의:** 작은 선수 객체(먼 거리) 탐지 시 라벨 비용 큼.
- **접근법:** 자기지도 학습으로 레이블 없이 작은 선수 탐지 학습.
- **Occlusion 관련성:** 간접.
- **URL:** https://dl.acm.org/doi/10.1145/3422844.3423054

### [P1-8] Zhang et al., 2021 — FairMOT
- **제목:** FairMOT: On the Fairness of Detection and Re-Identification in Multi-Object Tracking
- **저자:** Yifu Zhang, Chunyu Wang, Xinggang Wang et al.
- **저널:** International Journal of Computer Vision (IJCV), 2021
- **연구분야:** Stage 1 / 4
- **문제정의:** JDE(Joint Detection & Embedding) 프레임워크에서 탐지와 Re-ID가 경쟁, 공정한 학습 필요.
- **접근법:** CenterNet(anchor-free) + multi-layer feature fusion + low-dim appearance embedding + multi-task learning.
- **성능지표:** MOT17 MOTA 73.7, IDF1 72.3.
- **기여점:** Anchor ambiguity 감소, scale-aware competition 완화.
- **Occlusion 관련성:** 간접.
- **URL:** https://github.com/ifzhang/FairMOT

### [P1-9] Meinhardt et al., 2022 — TrackFormer
- **제목:** TrackFormer: Multi-Object Tracking with Transformers
- **저자:** Tim Meinhardt, Alexander Kirillov et al.
- **학회:** CVPR 2022
- **연구분야:** Stage 1 (일반 MOT)
- **문제정의:** 전통적 tracking-by-detection의 motion/appearance 수동 모델링 한계.
- **접근법:** Encoder-decoder Transformer, frame-to-frame set prediction. Track query를 프레임마다 autoregressive하게 전달.
- **성능지표:** MOT17 MOTA 65.0%.
- **Occlusion 관련성:** 간접 (attention으로 가림 완화).
- **URL:** https://arxiv.org/abs/2101.02702

### [P1-10] Zeng et al., 2022 — MOTR
- **제목:** MOTR: End-to-End Multiple-Object Tracking with Transformer
- **학회:** ECCV 2022
- **연구분야:** Stage 1
- **문제정의:** 완전 end-to-end MOT framework 부재.
- **접근법:** DETR 기반, track query를 프레임 단위 iterative 업데이트. Collective Average Loss (CAL), Temporal Aggregation Network (TAN).
- **성능지표:** DanceTrack HOTA 기준 ByteTrack 대비 +6.5%, AssA +8.1%. MOT17 MOTA 71.9%.
- **Occlusion 관련성:** 간접.
- **URL:** https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870648.pdf

### [P1-11] Huang et al., 2024 — Iterative Scale-Up ExpansionIoU (Deep-EIoU)
- **제목:** Iterative Scale-Up ExpansionIoU and Deep Features Association for Multi-Object Tracking in Sports
- **학회:** WACV 2024 Workshop (RWS)
- **연구분야:** Stage 1
- **문제정의:** Sports MOT에서 IoU 기반 연관이 빠른 비선형 움직임에 취약.
- **접근법:** Expansion IoU + deep Re-ID 특징 결합으로 motion-agnostic 연관.
- **성능지표:** SportsMOT HOTA 77.2%, SoccerNet-Tracking 85.4%.
- **Occlusion 관련성:** 직접.
- **URL:** https://openaccess.thecvf.com/content/WACV2024W/RWS/papers/Huang_Iterative_Scale-Up_ExpansionIoU_and_Deep_Features_Association_for_Multi-Object_Tracking_WACVW_2024_paper.pdf

### [P1-12] GTATrack, 2025 — SoccerTrack Winner
- **제목:** GTATrack: Winner Solution to SoccerTrack 2025 with Deep-EIoU and Global Tracklet Association
- **학회/저널:** arXiv 2025 (SoccerTrack 2025 Winner)
- **연구분야:** Stage 1
- **문제정의:** Fisheye 4096×1080, 22명 동시 · 심한 distortion · 빈번한 가림 상황 tracking.
- **접근법:** Deep-EIoU (online) + GTA-Link (offline tracklet clustering, appearance + spatio-temporal).
- **성능지표:** HOTA SORT 대비 +6.84%, Deep-EIoU 대비 +3.7% (SoccerNet).
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/html/2602.00484

---

## 3. Stage 2: 가림(Occlusion) 처리 — 범용 + 스포츠

### [P2-1] Bewley et al., 2016 — SORT
- **제목:** Simple Online and Realtime Tracking
- **저자:** Alex Bewley, Zongyuan Ge, Lionel Ott, Fabio Ramos, Ben Upcroft
- **학회:** ICIP 2016
- **연구분야:** Stage 2 (MOT 기초)
- **접근법:** Kalman Filter + Hungarian algorithm.
- **성능지표:** 260 Hz, 당시 SOTA 대비 20배 빠름.
- **Occlusion 관련성:** 간접 (짧은 가림만 회복).
- **URL:** https://arxiv.org/abs/1602.00763

### [P2-2] Wojke et al., 2017 — DeepSORT
- **제목:** Simple Online and Realtime Tracking with a Deep Association Metric
- **저자:** Nicolai Wojke, Alex Bewley, Dietrich Paulus
- **학회:** ICIP 2017
- **연구분야:** Stage 2 (MOT, 가림 회복)
- **접근법:** SORT + CNN appearance feature, Mahalanobis distance + cosine similarity cascade matching.
- **성능지표:** ID switch 45% 감소.
- **Occlusion 관련성:** 직접 (가림 기간 길수록 re-identification).
- **URL:** https://arxiv.org/abs/1703.07402

### [P2-3] Zhang et al., 2022 — ByteTrack
- **제목:** ByteTrack: Multi-Object Tracking by Associating Every Detection Box
- **저자:** Yifu Zhang et al.
- **학회:** ECCV 2022
- **연구분야:** Stage 2 (가림 회복 핵심)
- **문제정의:** 가림된 객체는 detection score가 낮아 고 threshold 방식에서 누락됨.
- **접근법:** BYTE — 모든 detection box를 연관. 낮은 score box는 tracklet과의 유사도로 부활 vs 배경 필터링.
- **성능지표:** MOT17 MOTA 80.3, IDF1 77.3, HOTA 63.1. 9개 SOTA 트래커에 적용 시 IDF1 +1~10.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/2110.06864

### [P2-4] Aharon et al., 2022 — BoT-SORT
- **제목:** BoT-SORT: Robust Associations Multi-Pedestrian Tracking
- **저자:** Nir Aharon, Roy Orfaig, Ben-Zion Bobrovsky
- **학회:** arXiv / later publications, 2022
- **연구분야:** Stage 2
- **접근법:** Camera Motion Compensation (CMC) + 개선된 Kalman state vector + IoU + Re-ID appearance 융합.
- **성능지표:** MOT17 MOTA 80.5, IDF1 80.2, HOTA 65.0.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/2206.14651

### [P2-5] Cao et al., 2023 — OC-SORT
- **제목:** Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking
- **저자:** Jinkun Cao et al.
- **학회:** CVPR 2023
- **연구분야:** Stage 2 (비선형 동작 + 가림)
- **문제정의:** 가림 구간에서 누적되는 Kalman 추정 노이즈.
- **접근법:** Observation-centric re-update. 가림 기간 동안 virtual trajectory를 관측 기반으로 재구성.
- **성능지표:** MOT17/20, KITTI, DanceTrack SOTA. 700+ FPS (CPU).
- **Occlusion 관련성:** 직접 (핵심).
- **URL:** https://arxiv.org/abs/2203.14360

### [P2-6] Du et al., 2023 — StrongSORT
- **제목:** StrongSORT: Make DeepSORT Great Again
- **저자:** Yunhao Du, Zhicheng Zhao, Yang Song et al.
- **저널:** IEEE Transactions on Multimedia, 2023
- **연구분야:** Stage 2
- **접근법:** DeepSORT 업그레이드 + AFLink (appearance-free tracklet link) + GSI (Gaussian-Smoothed Interpolation).
- **성능지표:** MOT17/20 HOTA·IDF1 1위, 2위 대비 +1.3~2.2.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/2202.13514

### [P2-7] Maggiolino et al., 2023 — Deep OC-SORT
- **제목:** Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-identification
- **학회/저널:** arXiv 2023
- **연구분야:** Stage 2
- **접근법:** OC-SORT + adaptive Re-ID weight (appearance confidence 기반).
- **성능지표:** MOT17/MOT20 HOTA SOTA.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/pdf/2302.11813

### [P2-8] Wang et al., 2018 — Repulsion Loss
- **제목:** Repulsion Loss: Detecting Pedestrians in a Crowd
- **저자:** Xinlong Wang, Tete Xiao et al.
- **학회:** CVPR 2018
- **연구분야:** Stage 2 (가림된 보행자 탐지)
- **접근법:** Attraction (target) + Repulsion (RepGT: 다른 GT와 거리, RepBox: 다른 예측과 거리) 결합 손실.
- **성능지표:** CityPersons, CrowdHuman에서 가림 상황 SOTA.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/1711.07752

### [P2-9] Chu et al., 2022 — Occlusion Handling Review
- **제목:** Occlusion Handling in Generic Object Detection: A Review
- **학회/저널:** arXiv / Survey 2021-2022
- **연구분야:** Stage 2 (서베이)
- **접근법:** 가림 분류(intra-class vs inter-class) 및 기법 체계화 (loss-based, feature-based, part-based, GAN-based).
- **Occlusion 관련성:** 직접 (리뷰).
- **URL:** https://arxiv.org/pdf/2101.08845

### [P2-10] Pedestrian MOT Survey, 2022 — Occlusion-Handling
- **제목:** Occlusion Handling and Multi-Scale Pedestrian Detection Based on Deep Learning: A Review
- **저널:** IEEE Access, 2022
- **연구분야:** Stage 2 (보행자 탐지 리뷰)
- **Occlusion 관련성:** 직접.
- **URL:** https://ieeexplore.ieee.org/document/9718221/

### [P2-11] OATrack, 2024 — Occlusion-Aware Pedestrian MOT
- **제목:** Towards Occlusion-Aware Multi-Pedestrian Tracking
- **저널:** MDPI Applied Sciences, 2024
- **연구분야:** Stage 2
- **접근법:** Occlusion Perception Module → occlusion rate 추정. Kalman innovation gain을 가림율에 따라 adaptive suppression, association cue weight도 adaptive.
- **Occlusion 관련성:** 직접 (핵심 설계).
- **URL:** https://www.mdpi.com/2076-3417/15/24/13045

### [P2-12] Zhu et al., 2023 — Handling Heavy Occlusion in Dense Crowd
- **제목:** Handling Heavy Occlusion in Dense Crowd Tracking by Focusing on the Heads
- **학회:** arXiv 2023 / Springer 2024
- **연구분야:** Stage 2 (군중)
- **접근법:** Joint head-body detector (anchor-free) + SoftNMS. 머리 위치는 몸보다 가림이 적음을 이용.
- **성능지표:** MOT20, HT21 성능 향상.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/2304.07705

### [P2-13] Occlusion-Aware Spatial Attention Transformer, 2022
- **제목:** Occlusion-Aware Spatial Attention Transformer for Occluded Object Recognition
- **저널:** Pattern Recognition Letters, 2022
- **연구분야:** Stage 2 (가림 객체 인식)
- **접근법:** Spatial attention + occlusion-aware loss. Transformer가 가림 영역을 식별·무시.
- **Occlusion 관련성:** 직접.
- **URL:** https://www.sciencedirect.com/science/article/abs/pii/S0167865522001581

### [P2-14] GCN-based Data Association for Online MOT, 2021
- **제목:** Graph Convolution Neural Network-Based Data Association for Online Multi-Object Tracking
- **저널:** IEEE Access, 2021
- **연구분야:** Stage 2 (GNN association)
- **접근법:** GCN으로 객체 간 affinity 추정. Pose feature 활용 → 부분 가림에도 안정.
- **성능지표:** MOT16 MOTA 80.6 / MOT17 81.1, HOTA 65.3/65.1.
- **Occlusion 관련성:** 직접.
- **URL:** https://ieeexplore.ieee.org/document/9514568/

### [P2-15] Occlusion-Related GCN for MOT, 2024
- **제목:** Occlusion-Related Graph Convolutional Neural Network for Multi-Object Tracking
- **저널:** Image and Vision Computing (Elsevier), 2024
- **연구분야:** Stage 2
- **접근법:** 그래프에 명시적 occlusion edge attribute를 부여하여 association 모델링.
- **Occlusion 관련성:** 직접.
- **URL:** https://www.sciencedirect.com/science/article/abs/pii/S0262885624004220

### [P2-16] Back et al., 2022 — UOAIS (Amodal)
- **제목:** Unseen Object Amodal Instance Segmentation via Hierarchical Occlusion Modeling
- **학회:** ICRA 2022
- **연구분야:** Stage 2 (amodal perception)
- **접근법:** Visible mask + Amodal mask + Occlusion mask 계층적 예측.
- **Occlusion 관련성:** 직접 (가려진 부분 복원).
- **URL:** https://arxiv.org/abs/2109.11103

### [P2-17] SAMEO / Amodal-LVIS, 2025
- **제목:** Segment Anything, Even Occluded
- **학회/저널:** arXiv 2025
- **연구분야:** Stage 2 (amodal + foundation model)
- **접근법:** SAM 기반 아모달 segmentation. 300K Amodal-LVIS 데이터셋.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/html/2503.06261v1

### [P2-18] Sequential Amodal Segmentation via Cumulative Occlusion, 2024
- **제목:** Sequential Amodal Segmentation via Cumulative Occlusion Learning
- **학회/저널:** arXiv 2024
- **연구분야:** Stage 2 (diffusion 기반 amodal)
- **접근법:** Diffusion 모델 iterative refinement + cumulative mask. Invisible 영역 uncertainty 포착.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/html/2405.05791v1

### [P2-19] Dendorfer et al., 2020 — MOT20 Benchmark
- **제목:** MOT20: A Benchmark for Multi Object Tracking in Crowded Scenes
- **학회/저널:** arXiv 2020
- **연구분야:** Stage 2 (군중 MOT 벤치마크)
- **접근법:** 프레임당 최대 246명, MOT17 대비 4배 밀집.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/2003.09003

### [P2-20] CrowdTrack, 2025
- **제목:** CrowdTrack: A Benchmark for Difficult Multiple Pedestrian Tracking
- **학회/저널:** arXiv 2025
- **연구분야:** Stage 2
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/pdf/2507.02479

### [P2-21] MCTrack, 2024 — 3D MOT for AV
- **제목:** MCTrack: A Unified 3D Multi-Object Tracking Framework for Autonomous Driving
- **학회:** IROS 2025
- **연구분야:** Stage 2 (자율주행 3D MOT)
- **접근법:** BEV-plane 1차 매칭 → image-plane 2차 매칭 (unmatched 보완).
- **성능지표:** KITTI, nuScenes, Waymo SOTA.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/abs/2409.16149

---

## 4. Stage 3: 등번호 인식

### [P3-1] Liu & Bhanu, 2019 — Pose-Guided R-CNN
- **제목:** Pose-Guided R-CNN for Jersey Number Recognition in Sports
- **학회:** CVPR 2019 Workshop (CVSports)
- **연구분야:** Stage 3
- **문제정의:** 선수 자세와 시점 변화 → 등번호 가림/왜곡.
- **접근법:** Pose 키포인트로 등번호 ROI 정렬 후 R-CNN 인식.
- **URL:** https://openaccess.thecvf.com/content_CVPRW_2019/papers/CVSports/Liu_Pose-Guided_R-CNN_for_Jersey_Number_Recognition_in_Sports_CVPRW_2019_paper.pdf

### [P3-2] Gerke et al., 2015/2016 — CNN Jersey Recognition
- **제목:** Soccer Jersey Number Recognition Using Convolutional Neural Networks
- **학회:** ICCV Workshops 2015 / IEEE 2016
- **연구분야:** Stage 3 (초기 CNN)
- **접근법:** CNN으로 등번호 분류.
- **URL:** https://ieeexplore.ieee.org/document/7406449/

### [P3-3] Vats et al., 2021 — Multi-task Ice Hockey
- **제목:** Multi-task Learning for Jersey Number Recognition in Ice Hockey
- **학회:** ACM MMSports 2021
- **연구분야:** Stage 3 / 4
- **접근법:** Jersey number + team + position 공동 학습.
- **URL:** https://dl.acm.org/doi/10.1145/3475722.3482794

### [P3-4] Balaji et al., 2023 — Keyframe Identification
- **제목:** Jersey Number Recognition using Keyframe Identification from Low-Resolution Broadcast Videos
- **학회:** ACM MMSports 2023
- **연구분야:** Stage 3
- **문제정의:** 방송 영상에서 등번호는 극소수 프레임에서만 보임.
- **접근법:** Keyframe identification module로 번호가 잘 보이는 프레임 선별 → STR.
- **성능지표:** 정확도 +37.81%, +37.70% (도메인 갭 있는 두 테스트셋).
- **URL:** https://dl.acm.org/doi/10.1145/3606038.3616162

### [P3-5] Koshkina & Elder, 2024 — General Framework
- **제목:** A General Framework for Jersey Number Recognition in Sports Video
- **학회/저널:** arXiv 2024 (2405.13896)
- **연구분야:** Stage 3
- **접근법:** YOLOv4 player detection → jersey number localization → 4-stage scene text recognition.
- **URL:** https://arxiv.org/abs/2405.13896

### [P3-6] Grad et al., 2025 — Single-Stage Uncertainty-Aware
- **제목:** Single-Stage Uncertainty-Aware Jersey Number Recognition in Soccer
- **학회:** CVPR 2025 Workshop (CVSports)
- **연구분야:** Stage 3
- **접근법:** Detection과 number recognition을 단일 단계로 통합 + uncertainty estimation.
- **URL:** https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/papers/Grad_Single-Stage_Uncertainty-Aware_Jersey_Number_Recognition_in_Soccer_CVPRW_2025_paper.pdf

### [P3-7] SoccerNet Jersey Challenge 2023 — Top Submission
- **제목:** SoccerNet 2023 Challenges Results (Jersey Number Recognition track)
- **학회/저널:** arXiv 2023, Sports Engineering 2024
- **접근법:** Tracklet 수준 majority voting + STR.
- **성능지표:** Test 90.09%, Challenge 90.95%.
- **URL:** https://arxiv.org/pdf/2309.06006

### [P3-8] Vats et al., 2022 — Transformer Ice Hockey ID
- **제목:** Ice Hockey Player Identification via Transformers and Weakly Supervised Learning
- **학회:** CVPR 2022 Workshop
- **연구분야:** Stage 3 / 4
- **접근법:** Weakly supervised transformer on tracklets.
- **URL:** (CVPRW 2022)

### [P3-9] ResNet+LSTM Spatio-Temporal Jersey Number
- **제목:** Spatio-Temporal Jersey Number Recognition (ResNet+LSTM)
- **연구분야:** Stage 3
- **접근법:** End-to-end ResNet backbone + LSTM for temporal aggregation across tracklet.
- **URL:** (referenced in SoccerNet baselines)

---

## 5. Stage 4: Re-ID + 통합 파이프라인

### [P4-1] Senocak et al., 2018 → Li et al., 2020 — Multi-camera Multi-player Tracking
- **제목:** Multi-camera Multi-player Tracking with Deep Player Identification in Sports Video
- **저널:** Pattern Recognition, 2020
- **연구분야:** Stage 4
- **접근법:** 다중 카메라 + 선수 식별 embedding.
- **URL:** https://dl.acm.org/doi/10.1016/j.patcog.2020.107260

### [P4-2] Habel et al., 2022 — Sports Re-ID
- **제목:** Sports Re-ID: Improving Re-Identification Of Players In Broadcast Videos Of Team Sports
- **학회/저널:** arXiv 2022 (2206.02373)
- **연구분야:** Stage 4
- **접근법:** Part-based embedding + team-aware sampling.
- **URL:** https://arxiv.org/abs/2206.02373

### [P4-3] SoccerNet Re-ID Challenge 2022 Winner
- **제목:** Multi-task Learning for Joint Re-identification, Team Affiliation, and Role Classification for Sports Visual Tracking
- **학회:** ACM MMSports 2023 (arXiv 2401.09942)
- **연구분야:** Stage 4
- **접근법:** Jersey number + team class + pose estimation 공동 학습.
- **성능지표:** mAP 86.0, Rank-1 81.5 (SoccerNet Re-ID 2022).
- **URL:** https://arxiv.org/html/2401.09942v1

### [P4-4] Akan & Varlı, 2023 — Pose-based Body Feature Alignment
- **제목:** Reidentifying Soccer Players in Broadcast Videos Using Body Feature Alignment Based on Pose
- **학회:** CNIOT 2023
- **연구분야:** Stage 4
- **접근법:** Pose 기반 body part alignment → part-wise 임베딩.
- **URL:** https://dl.acm.org/doi/abs/10.1145/3603781.3603860

### [P4-5] Miao et al., 2019 — PGFA (Pose-Guided Feature Alignment)
- **제목:** Pose-Guided Feature Alignment for Occluded Person Re-Identification
- **학회:** ICCV 2019
- **연구분야:** Stage 4 (가림 Re-ID 기초)
- **접근법:** Pose keypoint로 가림 영역 attention 억제.
- **URL:** https://openaccess.thecvf.com/content_ICCV_2019/html/Miao_Pose-Guided_Feature_Alignment_for_Occluded_Person_Re-Identification_ICCV_2019_paper.html

### [P4-6] Somers et al., 2024 — SoccerNet Game State Reconstruction
- **제목:** SoccerNet Game State Reconstruction: End-to-End Athlete Tracking and Identification on a Minimap
- **학회:** CVPR 2024 Workshop (CVsports)
- **연구분야:** Stage 4 (통합 파이프라인)
- **접근법:** 단일 방송 카메라 → 2D minimap. 선수 위치·역할·팀·번호 전체를 재구성.
- **URL:** https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Somers_SoccerNet_Game_State_Reconstruction_End-to-End_Athlete_Tracking_and_Identification_on_CVPRW_2024_paper.pdf

### [P4-7] SoccerNet 2025 Challenge GSR Winner
- **제목:** From Broadcast to Minimap: Achieving State-of-the-Art SoccerNet Game State Reconstruction
- **학회:** CVPR 2025
- **연구분야:** Stage 4
- **접근법:** YOLOv5m detection + SegFormer camera parameter + DeepSORT + Re-ID + Jersey number.
- **URL:** https://cvpr.thecvf.com/virtual/2025/35501

### [P4-8] Occluded Person Re-ID Survey, 2023
- **제목:** Occluded Person Re-Identification with Deep Learning: A Survey and Perspectives
- **학회/저널:** arXiv 2023 (2311.00603)
- **연구분야:** Stage 4 (가림 Re-ID 서베이)
- **접근법:** Part-based, pose-guided, semantic-guided, Transformer-based 분류.
- **Occlusion 관련성:** 직접.
- **URL:** https://arxiv.org/pdf/2311.00603

### [P4-9] Koshkina et al., 2021 — Contrastive Sports Video
- **제목:** Contrastive Learning for Sports Video: Unsupervised Player Classification
- **학회:** CVPR 2021 Workshop (CVSports)
- **연구분야:** Stage 4 (자기지도)
- **접근법:** 같은 팀 선수 간 거리 최소화, 다른 팀 간 거리 최대화 — 레이블 없음.
- **성능지표:** 단일 프레임 학습 후 94%, 500 프레임(17초) 후 97% 팀 분류 정확도.
- **URL:** https://arxiv.org/abs/2104.10068

---

## 6. 공개 데이터셋 현황

| 데이터셋 | 연도 | 도메인 | 규모 | 주 메트릭 | 용도 | URL |
|---------|------|--------|------|----------|------|-----|
| **SoccerNet-Tracking** | 2022 | 축구 MOT | 200×30s + 1×45min | HOTA | Stage 1, 2 | https://www.soccer-net.org/tasks/tracking |
| **SoccerNet-ReID** | 2022 | 축구 Re-ID | tracklet 기반 | mAP, R1 | Stage 4 | https://github.com/SoccerNet/sn-reid |
| **SoccerNet Jersey Number** | 2023 | 축구 등번호 | 2,853 tracklet + 1,211 challenge | Accuracy | Stage 3 | https://github.com/SoccerNet/sn-jersey |
| **SoccerNet-GSR** | 2024 | 축구 통합 | broadcast→2D minimap | GS-HOTA | Stage 4 | https://github.com/SoccerNet/sn-gamestate |
| **SportsMOT** | 2023 | 농구·배구·축구 | 240 seq, 150K frame, 1.6M box | HOTA | Stage 1 | https://github.com/MCG-NJU/SportsMOT |
| **TeamTrack** | 2024 | 축구·농구·핸드볼 | 4M+ box, drone top + fisheye | HOTA | Stage 1 | https://github.com/AtomScott/TeamTrack |
| **SoccerTrack** | 2024/2025 | 축구 fisheye | 4096×1080, 22명 | HOTA | Stage 1, 2 | (SoccerTrack Challenge) |
| **MOT17/MOT20** | 2017/2020 | 일반 보행자 | 7+8 seq | HOTA, MOTA, IDF1 | Stage 2 | https://motchallenge.net |
| **DanceTrack** | 2022 | 비선형 동작 | 100 seq | HOTA | Stage 2 | (DanceTrack) |
| **CrowdHuman** | 2018 | 군중 탐지 | 15k image | mAP | Stage 2 | https://www.crowdhuman.org |
| **HT21** | 2021 | 머리 추적 | 9 seq | HOTA | Stage 2 | (MOTChallenge HT21) |
| **CrowdTrack** | 2025 | 난이도 높은 군중 | 최신 | HOTA | Stage 2 | https://arxiv.org/abs/2507.02479 |
| **KITTI / nuScenes / Waymo** | 2012~ | 자율주행 3D | 대규모 | mAP, NDS | Stage 2 (cross-domain) | - |
| **Market-1501 / MSMT17** | - | 일반 Re-ID | - | mAP, R1 | Stage 4 (cross-domain) | - |
| **Occluded-Duke / Occluded-ReID** | 2019~ | 가림 Re-ID | - | mAP, R1 | Stage 4 | - |

---

## 7. 연구 공백 분석

### 7.1 명확히 확인된 공백
1. **축구 특화 amodal perception 부재** — amodal instance segmentation (UOAIS, SAMEO, Sequential Amodal 등)은 로봇·일반 scene에 집중. 축구의 몸 가림(선수-선수, 선수-공-심판) 상황에 amodal 마스크를 예측한 연구는 **현재까지 미확인**. 신규성 ①.
2. **Uniform-aware occlusion disambiguation 부재** — 같은 팀 선수가 가려졌을 때 team color 만으로는 식별 불가. 등번호·pose·동작 패턴을 결합한 **occlusion-time identity recovery** 모듈이 본격적으로 통합된 사례 드묾. 신규성 ②.
3. **Tracklet-level uncertainty propagation** — occlusion 구간에 대한 confidence/uncertainty를 downstream (jersey recognition, GSR)으로 전파하는 end-to-end 프레임워크 미흡. 2025 CVPRW "Single-Stage Uncertainty-Aware"가 단일 단계에 한정. 신규성 ③.
4. **Long-term (full-match) identity consistency** — 45분 전체 하프타임에 대한 전체 선수 일관 ID 부여 문제. SoccerNet-Tracking이 1개 long clip을 제공하지만, 대부분 연구는 30초 clip에 국한. 신규성 ④.
5. **Single fixed-camera + fisheye distortion + severe density 동시 해결** — GTATrack 2025가 초기 해법 제시했으나 후속 연구 부족.

### 7.2 기법 측면 공백
- **GNN 기반 temporal-spatial association**은 pedestrian/UAV에는 적용되었으나 축구 도메인에는 부분적. 팀 구조(전술 그룹)를 명시적 모델링한 GNN 미흡.
- **Diffusion-based amodal**의 sports 응용 전무.
- **Foundation model (SAM, SAMEO) 적응**으로 축구 데이터 label 부담 완화 가능성 미탐.

### 7.3 데이터 측면 공백
- SoccerNet 2024에서 Jersey Number track 중단 → 공식 벤치마크 모멘텀 약화.
- Fisheye / static-camera 기반 대규모 데이터 부족 (TeamTrack, SoccerTrack 외).

---

## 8. 기술 동향 요약

### 8.1 탐지 (Detection)
- 2018-2020: Faster R-CNN / YOLOv3 → 2020-2023: YOLOv5 → 2023-2025: YOLOv8, anchor-free (CenterNet, FCOS), DETR 계열.
- 축구 특화: 작은 객체(먼 선수, 공) → multi-scale feature pyramid + self-supervised pretraining 추세.
- 가림 대응: repulsion loss → SoftNMS → joint head-body detector → attention (CBAM, GOA) → transformer.

### 8.2 추적 (Tracking)
- Tracking-by-detection이 여전히 주류: **SORT(2016) → DeepSORT(2017) → FairMOT(2021) → ByteTrack(2022) → BoT-SORT(2022) → OC-SORT(2023) → StrongSORT(2023) → Deep-EIoU + GTA(2024-2025)**.
- End-to-end Transformer (TrackFormer, MOTR)는 일반 MOT에서는 경쟁력 있지만 sports에서는 여전히 OC-SORT/Deep-EIoU 계열에 미치지 못함.
- 2024-2025 트렌드: **global tracklet association (offline post-processing)** + **observation-centric motion recovery** + **camera motion compensation (CMC)**.

### 8.3 가림 처리
- **Loss-level:** Repulsion loss (2018).
- **Feature-level:** Part-based, pose-guided (PGFA, 2019 → 2025).
- **Attention-level:** Occlusion-aware spatial attention transformer (2022).
- **Motion-level:** OC-SORT (2023) — observation-centric re-update.
- **Association-level:** GNN-based, occlusion-edge graph (2024).
- **Perception-level:** Amodal segmentation (UOAIS 2022, SAMEO 2025, Sequential Amodal 2024).
- **Head-focus:** Dense crowd head tracker (2023).

### 8.4 등번호 인식
- 2015-2019: CNN 분류 → Pose-guided R-CNN.
- 2021-2023: Tracklet-level temporal aggregation (ResNet+LSTM, TCN).
- 2023-2024: Keyframe identification → STR pipeline, Multi-task learning (number + team + role).
- 2025: Single-stage uncertainty-aware (CVPR 2025 CVSports).

### 8.5 통합 파이프라인 (Game State Reconstruction)
- 단일 방송 카메라 → 2D minimap 재구성이 2024-2025 핵심 과제.
- 구성 요소: YOLO 계열 detection + camera calibration (SegFormer) + DeepSORT/Deep-EIoU tracking + Re-ID + jersey recognition + team classification.
- 평가: SoccerNet GS-HOTA.

### 8.6 일반 도메인에서 축구로의 전이 가능 기법
| 원천 도메인 | 기법 | 축구 적용 가능성 |
|-----------|------|----------------|
| 보행자 MOT20 / CrowdTrack | OATrack의 occlusion-aware Kalman gain | 直 |
| 군중 head tracking | Head-focused joint detector | 공중볼·스크럼에 유효 |
| 자율주행 MCTrack | BEV-plane + image-plane dual matching | Fisheye/단일카메라에 응용 가능 |
| 로봇 UOAIS | Amodal hierarchical modeling | 가려진 번호/몸통 복원 |
| Occluded Re-ID (PGFA, Point-level Transformer) | Pose-guided partial features | 직접 (이미 일부 적용) |
| Diffusion Sequential Amodal | 불확실성 기반 invisible 영역 복원 | Jersey number 불확실성 추정과 결합 잠재력 |

---

## 부록: 추가 참고 논문 (데이터셋·서베이)

- **[S-1]** Dendorfer et al., 2020 — MOT20 benchmark (arXiv:2003.09003). [이미 P2-19]
- **[S-2]** Naik et al., 2024 — Soccer Tracking Survey (Visual Computer). [이미 P1-4]
- **[S-3]** Deng et al., 2024 — Deep Learning in Crowd Counting: A Survey (CAAI TIT).
- **[S-4]** Long et al., 2020 — Scene Text Detection and Recognition: The Deep Learning Era (IJCV).
- **[S-5]** Computer Vision for Sports Analytics (Springer Chapter, 2025).

---

**탐색 결론:**  
본 문헌 탐색은 축구 영상 선수 탐지·추적·등번호 인식을 위한 48편의 핵심 논문을 Stage 1~4 및 데이터셋·서베이 축으로 체계화했다. 특히 **가림 처리(Stage 2)는 축구 도메인을 넘어 보행자·자율주행·군중·amodal 인식 등 광범위한 영역의 15편을 확보**하여, 후속 연구(설계, 신규 기법 제안, 실험)에서 축구 특화 문제 해결에 다학제적 아이디어를 활용할 기반을 마련했다. 핵심 공백은 (i) 축구 amodal perception, (ii) uniform-aware occlusion disambiguation, (iii) tracklet-level uncertainty propagation, (iv) long-term identity consistency로 정리된다.
