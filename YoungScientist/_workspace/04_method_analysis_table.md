# Phase 2 기법 심층 분석 정리표

**작성일:** 2026-04-16  
**선별 기법:** 20개  
**조합 파이프라인:** 4개  
**연구 공백 매핑:** 4개  

> 본 문서는 `03_method_analysis.md` 본문의 데이터를 표로 재정리한 것. 엑셀 버전은 `04_method_analysis_table.xlsx`.

---

## 1. 선별 기법 20개 (5차원 평가)

| ID | 기법명 | 카테고리 | 원논문 | 핵심 아이디어 | 축구 전이성 | 정확도 | 가림 | 실시간 | 단일카메라 | 조합성 | **총점** |
|----|--------|---------|-------|--------------|-----------|--------|------|-------|-----------|--------|---------|
| M1 | Repulsion Loss | A. Detection | P2-8 | RepGT+RepBox loss로 인접 객체 혼동 감소 | ★★★★ | 4 | 5 | 5 | 5 | 5 | **24** |
| M2 | Head-focus Joint Detector | A. Detection | P2-12 | 머리+몸 joint detection + SoftNMS | ★★★ | 4 | 5 | 3 | 5 | 4 | 21 |
| M3 | Occlusion-Aware Spatial Attn Transformer | A. Detection | P2-13 | Spatial attention으로 가림 영역 억제 | ★★★ | 3 | 4 | 3 | 5 | 5 | 20 |
| M4 | OC-SORT | B. Motion | P2-5 | Observation-centric re-update, virtual trajectory 재구성 | ★★★★★ | 5 | 5 | 5 | 5 | 5 | **25** |
| M5 | OATrack | B. Motion | P2-11 | Occlusion rate 추정 → adaptive Kalman gain/cue weight | ★★★★★ | 4 | 5 | 4 | 5 | 5 | 23 |
| M6 | BoT-SORT CMC | B. Motion | P2-4 | Camera Motion Compensation + 확장 Kalman state | ★★★★ | 4 | 3 | 4 | 5 | 5 | 21 |
| M7 | ByteTrack BYTE | C. Association | P2-3 | 모든 detection box 활용 (low-score 부활) | ★★★★★ | 5 | 5 | 5 | 5 | 5 | **25** |
| M8 | GCN Association | C. Association | P2-14 | GCN affinity + pose feature | ★★★★ | 4 | 4 | 3 | 5 | 4 | 20 |
| M9 | Occlusion-Related GCN | C. Association | P2-15 | Graph edge에 occlusion attribute | ★★★★ | 4 | 5 | 3 | 5 | 4 | 21 |
| M10 | Deep-EIoU | C. Association | P1-11 | Expansion IoU + deep Re-ID (motion-agnostic) | ★★★★★ | 5 | 4 | 4 | 5 | 5 | 23 |
| M11 | DeepSORT | D. Re-ID | P2-2 | CNN appearance + cascade matching | ★★★ | 3 | 3 | 4 | 5 | 5 | 20 |
| M12 | Deep OC-SORT | D. Re-ID | P2-7 | OC-SORT + adaptive Re-ID weight | ★★★★★ | 5 | 5 | 4 | 5 | 5 | **24** |
| M13 | PGFA | D. Re-ID | P4-5 | Pose keypoint로 가림 영역 attention 억제 | ★★★★ | 4 | 5 | 3 | 5 | 5 | 22 |
| M14 | Sports Re-ID Part+Pose+Multi-task | D. Re-ID | P4-2,P4-3,P4-4 | Part-based + team-aware + pose alignment + multi-task | ★★★★★ | 5 | 4 | 3 | 5 | 5 | 22 |
| M15 | UOAIS Hierarchical Amodal | E. Amodal | P2-16 | Visible/Amodal/Occlusion 3-mask 계층 예측 | ★★★ | 3 | 5 | 2 | 5 | 4 | 19 |
| M16 | SAMEO | E. Amodal | P2-17 | SAM foundation + Amodal-LVIS 300K | ★★★ | 4 | 5 | 2 | 5 | 4 | 20 |
| M17 | Sequential Amodal Diffusion | E. Amodal | P2-18 | Diffusion iterative + cumulative mask + uncertainty | ★★★ | 3 | 5 | 1 | 5 | 5 | 19 |
| M18 | StrongSORT + AFLink + GSI | F. Post-processing | P2-6 | Offline tracklet linking + Gaussian interpolation | ★★★★★ | 5 | 5 | 4 | 5 | 5 | **24** |
| M19 | GTA-Link | F/G. Post+Integrated | P1-12 | Appearance + spatio-temporal global tracklet clustering | ★★★★★ | 5 | 5 | 4 | 5 | 5 | **24** |
| M20 | SoccerNet GSR Integrated | G. Integrated | P4-6,P4-7,P4-3,P3-6,P3-4 | 통합 파이프라인 (detect+track+Re-ID+jersey+team) | ★★★★★ | 5 | 4 | 3 | 5 | 5 | 22 |

**총점 24+ 기법:** M4 OC-SORT (25), M7 ByteTrack (25), M1 Repulsion Loss (24), M12 Deep OC-SORT (24), M18 StrongSORT+AFLink (24), M19 GTA-Link (24)

### 1.1 축구 전이 도전과제 (상세)

| ID | 기법명 | 축구 전이 도전과제 | 예상 성능 |
|----|--------|-------------------|----------|
| M1 | Repulsion Loss | 보행자는 수직 가림 / 축구는 수평·비스듬 가림 → RepGT threshold 재튜닝. 공 탐지는 RepBox를 클래스별 분리. | SoccerNet Det mAP +1.5~3%, missed det -10~20% |
| M2 | Head-focus Joint Detector | 방송 롱샷에서 머리 해상도 작음 → head proposal 재학습. 헤더 동작에서 head-to-head repulsion 추가. | 홈경기 고정카메라 +3~5%, 방송 원거리 +1% |
| M3 | Occlusion-Aware Spatial Attn Transformer | Detector/Re-ID 양쪽 plug-in 가능. 계산 비용 증가 유의. | 정성적 개선, 정량 수치 제한적 |
| M4 | OC-SORT | 즉시 적용 가능. DanceTrack 등 비선형 동작 검증됨 → 축구 fast motion에 적합. | SoccerNet HOTA +3~5% 기대, 700+ FPS CPU |
| M5 | OATrack | Occlusion rate 추정기 학습 필요. 축구 기울어진 가림에 retrain. | IDF1 +2~4% 기대 |
| M6 | BoT-SORT CMC | Broadcast 축구에 즉시 유효. 홈 고정카메라에는 CMC 불필요. | Broadcast IDF1 +1~3% |
| M7 | ByteTrack BYTE | 즉시 적용. 낮은 threshold 설정이 축구 ball 탐지에도 유리. | SoccerNet HOTA +2~4%, IDF1 +3~5% |
| M8 | GCN Association | Graph 구성 비용 크나 정확도 높음. 실시간 요구 시 경량화 필요. | MOT17 HOTA 65 수준 |
| M9 | Occlusion-Related GCN | M8과 유사하나 occlusion edge 특화. 축구 amodal mask와 결합하면 강력. | 가림 구간 IDF1 +3~5% |
| M10 | Deep-EIoU | SportsMOT/SoccerNet에서 SOTA 검증. 즉시 baseline으로 사용. | SoccerNet HOTA 85.4% 보장 |
| M11 | DeepSORT | 기본 baseline. 더 강한 Re-ID로 대체 권장. | 기준선 |
| M12 | Deep OC-SORT | OC-SORT + adaptive Re-ID = 장기 가림 복구 우수. | MOT17/20 HOTA SOTA, 축구 적용 시 유망 |
| M13 | PGFA | 축구 pose estimator 품질 중요. HRNet 등 사용 시 효과적. | Occluded Re-ID mAP 개선, 축구 Re-ID +3~5% |
| M14 | Sports Re-ID Part+Pose+Multi-task | 이미 축구 Re-ID SOTA. Jersey embedding과 결합 가능성 큼. | mAP 86.0, R1 81.5 (SoccerNet 2022) |
| M15 | UOAIS Hierarchical Amodal | 축구 amodal annotation 부재 → pseudo-label 필요. 학습 비용 큼. | 신규성 높음, 실험 난이도 ★★★★ |
| M16 | SAMEO | SoccerNet 영상에 zero-shot pseudo-label 생성 후 UOAIS로 finetune 전략. | Pseudo-label 품질 70~85% 기대 |
| M17 | Sequential Amodal Diffusion | 추론 속도 매우 느림(offline). Uncertainty를 Re-ID/Jersey로 전파 가능. | Uncertainty propagation 신규 기여 가능 |
| M18 | StrongSORT + AFLink + GSI | 후처리만으로 큰 개선. 축구 full-match에 즉시 적용 가능. | HOTA +1~3%, IDF1 +2~5% |
| M19 | GTA-Link | SoccerTrack 2025 우승 검증. 확장하여 multi-modal distance 적용 가능. | SoccerNet HOTA +3~7% |
| M20 | SoccerNet GSR Integrated | 가장 완성도 높은 축구 파이프라인. 개별 모듈 교체로 연구 가능. | GS-HOTA SOTA, +1~3% 개선 여지 |

---

## 2. 조합 파이프라인 4개

| 조합명 | 파이프라인 구성 | 기대 시너지 | 예상 성능 | 난이도 | 필요 자원 |
|--------|----------------|------------|----------|--------|----------|
| 조합 1. 경량-실시간형 (Real-time Broadcast) | YOLOv8 + Repulsion Loss → OC-SORT + ByteTrack + CMC → Sports Re-ID + Team color → Single-Stage Uncertainty Jersey | Repulsion 감소 + ByteTrack low-score 부활 + OC-SORT 가림 복구 + CMC pan/tilt + Re-ID long-term | SoccerNet HOTA 80~82%, 25~30 FPS (V100) | ★★ | V100 1장, SoccerNet-Tracking + SportsMOT pretrain |
| 조합 2. 고성능-오프라인형 (Post-match Analysis) | RT-DETR+Repulsion+Head-focus → Deep-EIoU+BoT-SORT → PGFA+Multi-task Re-ID → GTA-Link+AFLink+GSI → Keyframe Jersey + Amodal(선택) | Online + offline 이중 구조, amodal이 가림 재구성 | HOTA 85~88%, GS-HOTA SOTA+1~3% | ★★★★ | A100×2, SoccerNet-Tracking+GSR, 자체 amodal pseudo-label |
| 조합 3. 신규성 강조형 (Amodal + Uniform-aware + Uncertainty) | YOLOv8+Repulsion → SAMEO Amodal → OATrack(occ rate from amodal) → Occlusion-Related GCN → Uniform-aware Re-ID(PGFA+jersey region) → Uncertainty propagation → GTA-Link(uncertainty-weighted) | 공백 ①②③ 동시 해결, 축구 최초 amodal 통합 | 심각한 가림 구간 IDF1 +5~10% | ★★★★★ | A100×4, amodal 일부 annotation+검수, 긴 학습 일정 |
| 조합 4. Long-term Identity Consistency형 (공백 ④) | Deep-EIoU+ByteTrack → AFLink+GSI → Tracklet galleries (jersey+team+pose+appearance) → GTA-Link multi-modal → 22 ID cap + Hungarian global | Multi-modal gallery로 full-match 일관성 | 45min clip IDF1 60→75%+ | ★★★★ | A100×2, SoccerNet 45min clip + 자체 annotation |

---

## 3. 연구 공백 × 기법 매핑

| 연구 공백 | 상세 설명 | 적용 가능 기법 | 결합 전략 |
|----------|----------|--------------|----------|
| 공백 ① 축구 amodal perception 부재 | 축구에서 가려진 번호·몸통의 완전 형태 복원 연구 부재 | UOAIS (M15), SAMEO (M16), Sequential Amodal Diffusion (M17) | SAMEO로 pseudo-label 생성 → UOAIS-like head로 finetune → pose prior 투입 |
| 공백 ② Uniform-aware occlusion disambiguation | 같은 팀 선수 가림 시 team color만으로는 구별 불가 | Sports Re-ID Part-based (M14), Multi-task Re-ID (P4-3), PGFA (M13), Contrastive Team (P4-9) | Part + pose + jersey region + intra-team contrastive loss 결합 |
| 공백 ③ Tracklet-level uncertainty propagation | 가림 구간 confidence를 downstream(jersey, GSR)으로 전파하는 end-to-end 부재 | Single-Stage Uncertainty Jersey (P3-6), OATrack (M5), Amodal Diffusion (M17), Deep OC-SORT adaptive (M12) | 5종 uncertainty를 end-to-end graph로 전파하는 프레임워크 |
| 공백 ④ Long-term (full-match) identity consistency | 45분 전체 선수 ID 일관성 부재, 대부분 30초 clip에 국한 | GTA-Link (M19), AFLink+GSI (M18), Multi-task Re-ID (P4-3), Jersey majority vote (P3-7), Contrastive Team (P4-9) | Multi-modal gallery + global linking + 22 ID cap |

---

## 4. Phase 3 권장 연구 방향

| 순위 | 방향 | 조합 기반 | 해결 공백 |
|------|------|----------|----------|
| 1순위 | **Amodal + Uniform-aware Soccer Tracker** | 조합 3 | ①②③ 동시 |
| 보조 | Occlusion-Aware Tracklet Uncertainty Propagation | 조합 3 흡수 | ③ |
| 대안 | Long-term Identity Consistency via Multi-modal Gallery | 조합 4 | ④ |
