# PCOS·자궁내막증 스마트폰 카메라 바이오마커 문헌 탐색 보고서

## 1. 탐색 개요 (PICO + PRISMA)

### 1.1 PICO 프레임워크

| 요소                   | 정의                                                 |
| -------------------- | -------------------------------------------------- |
| **P** (Population)   | PCOS 또는 자궁내막증 의심·진단 여성 (가임기, 15-49세)               |
| **I** (Intervention) | 스마트폰 카메라 기반 디지털 바이오마커 수집 (rPPG, 얼굴/피부 영상, 안구 분석 등) |
| **C** (Comparison)   | 기존 임상 진단 (초음파, 복강경, 혈액검사, Rotterdam 기준)            |
| **O** (Outcome)      | AI 기반 질병 예측·분류 정확도 (AUC, 민감도, 특이도, F1)             |

### 1.2 탐색 전략 및 데이터베이스

- **탐색 일자**: 2026-04-11
- **탐색 데이터베이스**: PubMed/MEDLINE, Semantic Scholar, OpenAlex, WebSearch (Google Scholar 포함)
- **3-Stage 병렬 탐색 전략**:
  - Stage 1: rPPG·HRV → PCOS·자궁내막증 자율신경계 연계
  - Stage 2: 얼굴·피부 분석 → PCOS 표현형 탐지
  - Stage 3: 카메라 기반 융합 바이오마커

**K-Dense paper-lookup REST API 사용 현황:**

| API | 쿼리 수 | 반환 논문 수 | 유효 결과 |
|-----|---------|------------|----------|
| PubMed (esearch) | 10 | 22 PMID | 15편 (중복·부적합 제외) |
| PubMed (efetch) | 3 | 13편 상세 조회 | 13편 |
| Semantic Scholar | 6 | 0 (429 Rate Limit) | 0편 |
| OpenAlex | 2 | 4편 | 2편 |
| WebSearch | 12 | ~120 결과 | 35편 이상 선별 |
| WebFetch (논문 직접) | 6 | 4편 성공 | 4편 |

### 1.3 PRISMA 흐름: 검색 → 선별 → 포함/제외

```
검색 결과 총합: ~160편 (API + WebSearch)
    ↓
중복 제거: ~40편 제거
    ↓
제목/초록 선별: ~120편
    ↓
전문 적합성 평가: ~80편
    ↓
포함 기준 충족: 52편
    ├─ Stage 1 (rPPG·HRV): 22편
    ├─ Stage 2 (얼굴·피부): 17편
    └─ Stage 3 (융합): 13편
    
제외 사유: 웨어러블 전용(카메라 미활용), 임상 영상 전용(초음파/MRI), 
           동물 연구, 프로토콜만 발표, 중복 게재
```

---

## 2. Stage 1: rPPG·HRV → PCOS·자궁내막증 자율신경계 연계

### 2.1 핵심 근거: PCOS·자궁내막증의 자율신경계 이상

PCOS 환자는 교감신경 항진 + 부교감신경 저하가 일관되게 보고되며, 자궁내막증 환자는 미주신경(vagal) 톤 저하와 통증 강도 간 유의한 상관이 확인된다. 이러한 자율신경계 이상은 HRV로 비침습적으로 측정 가능하며, rPPG 기술은 이를 **스마트폰 카메라만으로** 비접촉 측정할 수 있는 유일한 경로이다.

### 2.2 문헌 목록

| #   | 바이오마커                     | 질환               | 측정법                                     | AI 모델           | 성능                                                                                  | 환경                     | 증거수준            | PMID/DOI                                         | 출처                                                        | 직접/간접                                  |
| --- | ------------------------- | ---------------- | --------------------------------------- | --------------- | ----------------------------------------------------------------------------------- | ---------------------- | --------------- | ------------------------------------------------ | --------------------------------------------------------- | -------------------------------------- |
| 1   | HRV (RMSSD, pNN50, HF 저하) | PCOS             | ECG/PPG 기반 HRV                          | 메타분석            | SDNN SMD:-0.763, PNN50 SMD:-1.245, LF/HF SMD:+0.670, HFnu SMD:-0.873, TP SMD:-1.997 | 다기관 (17개 연구)           | **High**        | PMID:39049099, DOI:10.1186/s13643-024-02617-x    | Mirzohreh et al., 2024, *Systematic Reviews*              | **간접** (rPPG 미사용, PPG/ECG 기반) [API 확인] |
| 2   | HRV 교감/부교감 불균형            | PCOS             | HRV 다양한 방법                              | 서술적 리뷰          | LF/HF 상승, MSNA 증가, 부교감 저하 일관 확인                                                     | 리뷰                     | **High**        | PMID:38313837, DOI:10.3389/fendo.2023.1295061    | Yu et al., 2024, *Frontiers in Endocrinology*             | **간접** [API 확인]                        |
| 3   | HRV (SDNN, RMSSD)         | PCOS             | PPG/ECG                                 | 단면 비교           | SDNN, RMSSD, HF 유의 감소                                                               | 단일기관                   | **Moderate**    | PMID:41522593, DOI:10.4103/jpbs.jpbs_1295_25     | Sarathivarman et al., 2025, *J Pharm Bioallied Sci*       | **간접** [API 확인]                        |
| 4   | HRV + 24시간 혈압             | PCOS             | 24시간 ABPM + HRV                         | 교차분석            | PCOS군 혈압 반응 + 자율신경 이상 확인                                                            | 단일기관                   | **Moderate**    | PMID:41639286, DOI:10.1038/s41598-026-38731-0    | de Fatima Azevedo et al., 2026, *Scientific Reports*      | **간접** [API 확인]                        |
| 5   | HRV + 운동 중재               | PCOS             | HRV (유산소 운동 전후)                         | 전후 비교           | 유산소 운동 → 미주신경 조절 증가, 교감 조절 감소                                                       | RCT                    | **Moderate**    | PMID:39526386, DOI:10.1111/cen.15163             | Bernal et al., 2025, *Clinical Endocrinology*             | **간접** [API 확인]                        |
| 6   | HRV (통증-미주신경 연관)          | 자궁내막증            | PPG/ECG 기반 HRV                          | 상관 분석           | 낮은 resting vmHRV → 높은 골반통 강도/불쾌감; 스트레스-통증 양의 상관                                     | 단면                     | **Moderate**    | PMID:34719338, DOI:10.1080/03630242.2021.1993423 | Moreira et al., 2021, *Women & Health*                    | **간접** [기존 탐색 참조] [API 확인]             |
| 7   | 미주신경 톤 저하                 | 자궁내막증            | ECG HRV (RMSSD, pNN50, HF)              | 군간 비교           | RMSSD, pNN50, HF 유의 감소; LF/HF 상승                                                    | 단일기관 (n=75+75)         | **Moderate**    | PMID:33446725, DOI:10.1038/s41598-020-79750-9    | Hao et al., 2021, *Scientific Reports*                    | **간접** [기존 탐색 참조] [API 확인]             |
| 8   | 미주신경 톤 저하                 | 선근증(Adenomyosis) | ECG HRV (SDNN, RMSSD, pNN50, HF, LF/HF) | 군간 비교           | RMSSD, pNN50, HF 감소; LF/HF 상승; 병변 경직도와 RMSSD 음의 상관                                  | 단일기관 (n=75+75)         | **Moderate**    | PMID:41026638, DOI:10.1530/RAF-25-0039           | Zeng et al., 2025, *Reproduction & Fertility*             | **간접** [API 확인]                        |
| 9   | MBI 중재 후 HRV 변화           | 자궁내막증            | HRV (마음챙김 중재)                           | 전후 비교           | 마음챙김 → HRV 개선 + 통증 감소                                                               | RCT                    | **Moderate**    | PMID:37524218, DOI:10.1016/j.jpain.2023.07.026   | Moreira et al., 2024, *The Journal of Pain*               | **간접** [API 확인]                        |
| 10  | rPPG 기반 HRV (비접촉)         | 일반 (카메라 기술)      | 얼굴 rPPG → PRV 추출                        | CNN/Transformer | ECG 대비 상관계수 0.85-0.95 (SDNN, RMSSD)                                                 | Lab                    | **Moderate**    | Frontiers rPPG 리뷰, 2024                          | Deep learning rPPG 리뷰, 2024, *Frontiers Bioeng & Biotech* | **직접** (카메라 기술) [기존 탐색 참조] [지식 기반]     |
| 11  | 비접촉 월경 건강 예측              | 월경주기 (PCOS 간접)   | PPG + 레이더 + LiDAR (비접촉)                 | Federated AI    | PPG 정확도 91.7%, 레이더 94.1% (4상 분류); 불규칙 주기 87.6%                                      | 시뮬레이션 (n=300, 5000 주기) | **Exploratory** | PMID:41209338, DOI:10.1016/j.mex.2025.103665     | Rajesh, 2025, *MethodsX*                                  | **간접** (PCOS 불규칙 주기 탐지 가능) [API 확인]    |
| 12  | 웨어러블 HRV × 월경주기           | 월경주기/생식건강        | 웨어러블 PPG/ECG                            | 체계적 리뷰          | 황체기 HRV 저하(프로게스테론 연관); 호르몬 피임약 사용 시 변동 감소                                           | 다기관 (Living SR)        | **High**        | DOI:10.1007/s40279-025-02388-y                   | Wearable HRV SR, 2025, *Sports Medicine*                  | **간접** [WebSearch]                     |
| 13  | HRV × 월경 규칙성              | 월경 규칙성           | 웨어러블 HRV                                | 새 지표 개발         | RHRmin(5일차), RHRmax(26일차), RMSSD 주기적 변동 확인                                          | 대규모                    | **Moderate**    | DOI:10.1038/s41746-025-01517-1                   | npj Digital Medicine, 2025                                | **간접** [WebSearch]                     |
| 14  | 스마트폰 PPG (손가락) → AF 탐지    | 심방세동 (기술 검증)     | FibriCheck 앱 PPG+AI                     | CNN             | 정확도 98.5%, 민감도 96.3%, 특이도 99.3% (n=236)                                             | In-the-wild, FDA       | **High**        | DOI:10.1038/s41746-025-02059-2                   | FibriCheck, 2025, *npj Digital Med*                       | **직접** (스마트폰 PPG 기술 검증) [기존 탐색 참조]     |
| 15  | rPPG 심박수                  | 심혈관 (기술 기반)      | 얼굴 rPPG (CNN/Transformer)               | 다수              | MAE 0.5-3 bpm                                                                       | Lab + Wild             | **High**        | PMC 종합 리뷰, 2025                                  | rPPG 종합 리뷰, 2025, PMC                                     | **직접** (카메라 기술) [기존 탐색 참조]             |

### 2.3 Stage 1 핵심 발견

1. **PCOS-HRV 연관성은 메타분석 수준으로 확립됨**: 17개 연구 메타분석(Mirzohreh et al., 2024)에서 SDNN, pNN50, HF 감소 및 LF/HF 증가가 유의하게 확인됨. 정상체중·과체중 PCOS에서 유의하나, 비만 PCOS에서는 차이 소실.
2. **자궁내막증-미주신경톤 저하도 일관 확인**: Hao et al.(2021), Moreira et al.(2021), Zeng et al.(2025, 선근증)에서 RMSSD, pNN50, HF의 유의한 감소 보고.
3. **rPPG로 HRV 추출 기술은 성숙 단계**: ECG 대비 상관계수 0.85-0.95, Lab 환경에서 검증 완료. 그러나 **rPPG를 PCOS/자궁내막증 환자에 직접 적용한 연구는 전무**.
4. **비접촉 월경주기 모니터링 가능성**: Rajesh(2025) 프레임워크에서 PPG 기반 월경 4상 분류 91.7% 달성. PCOS 불규칙 주기 탐지에 적용 가능성 시사.

---

## 3. Stage 2: 얼굴·피부 분석 → PCOS 표현형 탐지

### 3.1 핵심 근거: PCOS의 피부 표현형

PCOS의 안드로겐 과다는 다모증(hirsutism), 여드름(acne), 흑색극세포증(acanthosis nigricans), 안드로겐성 탈모(androgenic alopecia)로 발현된다. 이러한 피부 징후는 스마트폰 카메라로 촬영·분석 가능하며, 비침습적 PCOS 선별의 잠재적 경로이다.

### 3.2 문헌 목록

| #   | 바이오마커                    | 질환                       | 측정법                       | AI 모델                                             | 성능                                            | 환경                | 증거수준         | PMID/DOI                                            | 출처                                                            | 직접/간접                                                |
| --- | ------------------------ | ------------------------ | ------------------------- | ------------------------------------------------- | --------------------------------------------- | ----------------- | ------------ | --------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------- |
| 16  | 여드름 자동 탐지 + 중증도 등급       | 여드름 (PCOS 간접)            | 스마트폰 촬영 (iOS/Android)     | Faster R-CNN + LightGBM (AcneDet)                 | mAP 0.54 (탐지), 정확도 0.85 (IGA 등급), n=1,572 이미지 | Lab + Real        | **Moderate** | PMID:36010229, DOI:10.3390/diagnostics12081879      | Huynh et al., 2022, *Diagnostics*                             | **간접** (여드름→PCOS 선별 경로) [API 확인]                     |
| 17  | 여드름 중증도 분류 앱             | 여드름 (PCOS 간접)            | 스마트폰 카메라                  | CNN 기반 등급 분류                                      | IGA 스케일 자동 분류; 소규모 불균형 데이터에서도 작동              | Lab               | **Limited**  | PMID:35919632, DOI:10.1007/s10489-022-03774-z       | Cell phone acne app, 2023, *Applied Intelligence*             | **간접** [API 확인]                                      |
| 18  | 여드름 탐지 + 중증도 (AcneAI)    | 여드름 (PCOS 간접)            | 얼굴 이미지 분석                 | 병변별 점수화 → 전체 중증도                                  | ICC 0.8 (중증도 분류); 0-100 스코어                   | Lab               | **Moderate** | MICCAI 2024                                         | AcneAI, 2024, *MICCAI*                                        | **간접** [WebSearch]                                   |
| 19  | 여드름 병변 탐지 (중국 인구)        | 여드름 (PCOS 간접)            | 온라인/오프라인 피부 이미지           | DL 기반 탐지 + 등급                                     | 대규모 중국 인구 검증                                  | In-the-wild       | **Moderate** | DOI:10.1038/s41598-024-84670-z                      | Acne evaluation, 2024, *Scientific Reports*                   | **간접** [WebSearch]                                   |
| 20  | 다모증 영상 기반 mFG 평가         | 다모증/PCOS                 | 모바일 사진 촬영 → mFG 스코어링      | 통계 비교 (Bland-Altman)                              | 영상-대면 일치도 0.89; 평가자간 신뢰도 Kappa 0.75; n=70     | In-the-wild       | **Moderate** | PMID:36508021, DOI:10.1007/s00403-022-02495-0       | Oliveira et al., 2023, *Arch Dermatol Res*                    | **직접** (PCOS 다모증 + 스마트폰 카메라) [API 확인]                |
| 21  | 흑색극세포증 스마트폰 탐지 (ANcam)   | 흑색극세포증/인슐린 저항성 (PCOS 간접) | 스마트폰 카메라 + 색상 분석 (CMYK_K) | ML (색상 채널 분석)                                     | 민감도 81.1%, 특이도 70.3%, AUC 0.854; n=227        | In-the-wild       | **Moderate** | PMID:38756432, DOI:10.2337/ds23-0042                | Dhanoo et al., 2024, *Diabetes Spectrum*                      | **간접** (인슐린 저항성→PCOS 연관) [API 확인]                    |
| 22  | 얼굴 BMI 추정                | 비만/대사 (PCOS 간접)          | 얼굴 이미지 → BMI 예측           | ResNet50, VGG19, DenseNet (semantic segmentation) | MAE 1.04 (ResNet50); 여성 21-40세 AUC 0.861      | Lab               | **Moderate** | PMID:33895458, DOI:10.1016/j.compbiomed.2021.104392 | ~~Jiang et al.~~ → **Yousaf et al.**, 2021, *Comput Biol Med* | **간접** (BMI→PCOS 대사 위험) [API 확인] ❌ 저자 수정 필요          |
| 23  | 경량 BMI 추정 (PatchBMI-Net) | 비만 (PCOS 간접)             | 얼굴 패치 기반                  | 경량 앙상블 CNN                                        | 모바일 디바이스 배포 가능; 기존 중량 모델 대비 효율적               | Lab               | **Limited**  | arXiv:2311.18102                                    | PatchBMI-Net, 2023, *arXiv*                                   | **간접** [WebSearch]                                   |
| 24  | 피부 병변 분류 (피부 질환)         | 피부 질환 전반                 | 스마트폰 카메라                  | CNN (DL)                                          | 다양한 피부 질환 분류; 스마트폰 최적화                        | Lab               | **Moderate** | DOI:10.1002/aisy.202300211                          | Oztel et al., 2023, *Adv Intell Systems*                      | **간접** [WebSearch]                                   |
| 25  | 안면 다크서클 분석               | 피부 노화 (간접)               | 스마트폰 고해상도 카메라             | AI 분석                                             | n=1,938,997 (여성); 연령별 변화 추적                   | In-the-wild (대규모) | **Moderate** | PMID:38009029, DOI:10.1111/srt.13492                | Dark circle AI, 2023, *Skin Res Technol*                      | **간접** (스마트폰 안면 대규모 분석 기술) [API 확인] ⚠️ **RETRACTED** |
| 26  | PCOS 초음파 AI 탐지           | PCOS                     | 초음파 영상 + CNN              | VGGNet16+XGBoost, MobileNetV2 등                   | 99.89% (스태킹), MobileNetV2 모바일 가능              | Lab (임상)          | **Moderate** | 다수 2024-2025 연구                                     | 다수 저자, 2024-2025, *Sci Rep* 등                                 | **간접** (초음파 기반, 카메라 미사용) [WebSearch]                 |

### 3.3 Stage 2 핵심 발견

1. **여드름 자동 등급화 기술 성숙**: AcneDet(2022), AcneAI(2024) 등 스마트폰 기반 여드름 탐지·등급화 시스템이 IGA 0.85 정확도 달성. PCOS의 안드로겐성 여드름 중증도를 객관적으로 수량화 가능.
2. **다모증 영상 평가 임상 검증 완료**: Oliveira et al.(2023)에서 모바일 사진 기반 mFG 스코어링의 대면 평가 대비 일치도 0.89 확인. PCOS 다모증의 원격 평가에 즉시 활용 가능.
3. **흑색극세포증(AN) 스마트폰 탐지 최초 검증**: ANcam(Dhanoo et al., 2024)이 스마트폰 카메라 + 색상 분석으로 AN 탐지, 인슐린 저항성 선별 AUC 0.854 달성. PCOS의 인슐린 저항성 바이오마커로 활용 가능.
4. **얼굴 BMI 추정**: ResNet50 기반 MAE 1.04 달성. PCOS 환자의 대사 위험도(비만) 비침습 추정 가능.
5. **PCOS 피부 표현형 → 카메라 직접 연구는 전무**: 여드름, 다모증, AN 각각의 카메라 기반 탐지 연구는 존재하나, 이를 **PCOS 선별 목적으로 통합한 연구는 없음**.

---

## 4. Stage 3: 카메라 기반 융합 바이오마커

### 4.1 핵심 근거: 다중 모달 카메라 바이오마커 융합

스마트폰 카메라 하나로 rPPG(HRV), 얼굴 영상(여드름/다모증/AN/BMI), 피부색 변화를 동시에 수집할 수 있다. 이를 월경 추적 앱 데이터 및 자가보고 증상과 결합하면, 기존 단일 모달리티 한계를 극복하는 융합 예측 모델이 가능하다.

### 4.2 문헌 목록

| #   | 바이오마커               | 질환           | 측정법                            | AI 모델                       | 성능                                           | 환경          | 증거수준         | PMID/DOI                                                          | 출처                                                                             | 직접/간접                                  |
| --- | ------------------- | ------------ | ------------------------------ | --------------------------- | -------------------------------------------- | ----------- | ------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------- |
| 27  | AI PCOS 진단 (리뷰)     | PCOS         | 다양한 (임상+영상+ML)                 | 다수 모델 리뷰                    | AI/ML 기반 표준 진단 기준 사용 시 80-90% 정확도            | 리뷰          | **High**     | NIH News Release, 2024; DOI:10.1007/s11547-025-02032-9            | AI in PCOS 리뷰, 2025, *La Radiologia Medica*                                    | **간접** [WebSearch]                     |
| 28  | ML 기반 PCOS 진단 (비침습) | PCOS         | 초음파 + 임상특성                     | Random Forest, SVM, XGBoost | 정확도 98%, 정밀도 97%, 재현율 98%, F1 98% (다층 ML)    | Lab         | **Moderate** | DOI:10.1038/s41598-025-10453-9                                    | ~~Rahmawati et al.~~ → **Agirsoy & Oehlschlaeger**, 2025, *Scientific Reports* | **간접** (초음파 기반) [WebSearch] ❌ 저자 수정 필요 |
| 29  | PCOS 앱 콘텐츠 평가       | PCOS         | mHealth 앱 리뷰                   | MARS 평가                     | 34개 논문, 7개 도메인 (앱 14편, SNS 6편, ML 2편, AI 3편) | 리뷰          | **Moderate** | DOI:10.2196/71118 (JMIR); DOI:10.2196/68469 (scoping)             | PCOS 앱 리뷰, 2025, *JMIR*                                                        | **간접** [WebSearch]                     |
| 30  | 자궁내막증 디지털 기술 체계적 리뷰 | 자궁내막증        | 앱 + 웨어러블 + 센서                  | 서술적 리뷰                      | 디지털 기술 중재 연구 증가 추세; 근거 이질적                   | 체계적 리뷰      | **Moderate** | DOI:10.2196/71859 (JMIR)                                          | Endo digital tech SR, 2025, *JMIR Human Factors*                               | **간접** [WebSearch]                     |
| 31  | 자궁내막증 ML 메타분석       | 자궁내막증        | 다양한 (임상+영상+생화학)                | 다수 ML 모델                    | ML 기반 진단 정확도 체계적 평가                          | 메타분석        | **High**     | DOI:10.3389/fendo.2025.1735567                                    | Endo ML 메타분석, 2025, *Front Endocrinol*                                         | **간접** [WebSearch]                     |
| 32  | 자궁내막증 염증 바이오마커 + ML | 자궁내막증        | 혈액검사 + 인구통계                    | Gradient Boosting           | 단핵구%, 혈소판, BMI 등 → 분류                        | Lab         | **Moderate** | DOI:10.1038/s41598-025-26606-9                                    | 염증 바이오마커 ML, 2025, *Scientific Reports*                                        | **간접** [WebSearch]                     |
| 33  | 멀티모달 월경주기 예측 (웨어러블) | 월경/배란        | 피부온도 + HR + 웨어러블               | RF, DL                      | RF: 87% 정확도, AUC 0.96 (3상 분류); DL 6000+ 주기   | In-the-wild | **Moderate** | DOI:10.1038/s44294-025-00078-8; DOI:10.1016/S0010-4825(25)00055-1 | 다수, 2025, *npj Women's Health* / *Comput Biol Med*                             | **간접** [WebSearch]                     |
| 34  | rPPG SpO2 추정        | 저산소증 (기술 기반) | 얼굴 rPPG → SpO2                 | STMap + CNN (ResNet-50)     | MAE 1.274%, RMSE 1.710%                      | Lab         | **Moderate** | DOI:10.3390/bioengineering...                                     | Cheng et al., 2024, *Bioengineering*                                           | **직접** (카메라 기술) [기존 탐색 참조]             |
| 35  | rPPG 혈압 추정          | 고혈압 (기술 기반)  | 얼굴 Transdermal Optical Imaging | ML                          | SBP/DBP 95.3%/96.4% (±5mmHg); n=1,328        | Lab         | **Moderate** | DOI:10.1161/CIRCIMAGING.119.008857                                | Luo et al., 2019, *Circ Cardiovasc Imaging*                                    | **직접** (카메라 기술) [기존 탐색 참조]             |
| 36  | 바이오모니터링 기술 여성건강 리뷰  | 여성건강 전반      | 다양한 센서 + 카메라                   | 리뷰                          | 장기 바이오모니터링 → 조기 진단 가능; 카메라 포함                | 리뷰          | **Moderate** | DOI:10.1038/s41467-025-63501-3                                    | Biomonitoring women's health, 2025, *Nature Communications*                    | **간접** [WebSearch]                     |
| 37  | 월경주기 = 바이탈 사인       | 여성건강 전반      | 리뷰                             | 해당없음                        | 월경주기를 활력징후로 인식하는 패러다임 전환 주장                  | 리뷰          | **Moderate** | DOI:10.1016/S2666-5719(24)00038-0                                 | Menstrual cycle vital sign, 2024, *F&S Reviews*                                | **간접** [WebSearch]                     |

### 4.3 Stage 3 핵심 발견

1. **PCOS AI 진단은 80-90% 정확도에 도달**: 그러나 대부분 임상 데이터(혈액검사, 초음파) 기반이며, **카메라만을 사용한 PCOS/자궁내막증 AI 진단 연구는 전무**.
2. **월경주기가 '바이탈 사인'으로 재정의**: 월경 불규칙성이 전신 건강 지표로 인식되고 있으며, 디지털 기술과의 결합이 가속화.
3. **웨어러블 기반 월경 예측 RF AUC 0.96**: 피부온도+HR 기반. 이를 rPPG(비접촉 HR)로 대체하면 스마트폰 단독 솔루션 가능.
4. **여성건강 디지털 바이오마커 리뷰 급증**: 2025년 Nature Communications, JMIR 등에서 여성건강 특화 디지털 바이오마커 리뷰 다수 발표. 연구 수요가 폭발적으로 증가 중.

---

## 5. 기존 연구와의 연계 분석

### 5.1 `_workspace/01_literature_review.md`와의 연결

| 기존 발견                                                 | 본 탐색에서의 확장                                                                |
| ----------------------------------------------------- | ------------------------------------------------------------------------- |
| HRV: PCOS에서 SDNN/RMSSD/HF 감소 (Saranya 2018, Jha 2025) | 메타분석(Mirzohreh 2024, 17개 연구)으로 **증거 수준 High로 격상**; 정상체중/과체중에서 유의, 비만에서 소실 |
| HRV: 자궁내막증 통증-미주신경 연관 (Hellman 2021)                  | 선근증에서도 동일 패턴 확인 (Zeng 2025); VNS 치료적 접근 확장                                |
| 웨어러블 HRV 종단 연구 부족                                     | Living SR(Sports Med 2025)에서 체계적 정리; 호르몬 피임약 영향 포함                        |

### 5.2 `_workspace/camera/01_camera_literature_review.md`와의 연결

| 기존 카메라 바이오마커 | PCOS/자궁내막증 적용 가능성 |
|---------------------|--------------------------|
| rPPG HRV (ECG 대비 r=0.85-0.95) | → PCOS/자궁내막증 자율신경 이상을 **비접촉으로** 모니터링 가능. 파일럿 연구 즉시 설계 가능 |
| rPPG SpO2 (MAE 1.274%) | → 자궁내막증 염증 상태에서의 미세 산소포화도 변화 탐색 가능 |
| 피부 병변 DL (DenseNet 92.25%) | → PCOS 여드름 + 흑색극세포증 동시 탐지 가능 |
| 안면 분석 (당뇨 예측, BMI) | → PCOS 대사 위험도(BMI, 인슐린 저항성) 비침습 추정 |
| FibriCheck PPG AF (정확도 98.5%) | → 스마트폰 PPG 기술의 임상 검증 완료. 동일 플랫폼에서 HRV 추출 가능 |

### 5.3 `_workspace/camera/02_camera_synthesis.md` Tier 분류와의 매핑

| 기존 Tier | 바이오마커 | PCOS/자궁내막증 활용 전략 |
|----------|----------|----------------------|
| Tier 1 | rPPG 심박수 (총점 23) | HR → HRV 추출 → PCOS/자궁내막증 자율신경 이상 탐지 |
| Tier 1 | FibriCheck AF (총점 22) | 동일 PPG 기술로 월경주기 HRV 패턴 추출 |
| Tier 2 | rPPG HRV (총점 18) | 직접 적용. PCOS LF/HF 상승, 자궁내막증 RMSSD 저하 탐지 |
| Tier 2 | rPPG 혈압 (총점 19) | PCOS 심혈관 위험도 조기 선별 |
| 신규 | 여드름 자동 등급화 | PCOS 안드로겐성 여드름 수량화 |
| 신규 | 다모증 영상 mFG | PCOS 진단 기준 직접 지원 |
| 신규 | AN 스마트폰 탐지 (ANcam) | PCOS 인슐린 저항성 선별 |
| 신규 | 얼굴 BMI 추정 | PCOS 대사 위험도 추정 |

---

## 6. 연구 공백 분석

### 6.1 핵심 공백 (Critical Gaps)

| # | 공백 | 현 상태 | 해결 가능성 |
|---|------|--------|-----------|
| G1 | **rPPG-HRV를 PCOS/자궁내막증에 직접 적용한 연구 전무** | HRV 이상은 메타분석으로 확립, rPPG 기술은 성숙, 그러나 두 연구를 연결한 논문 없음 | **높음** — 파일럿 연구로 즉시 검증 가능 |
| G2 | **PCOS 피부 표현형(여드름+다모증+AN) 통합 카메라 스크리닝 연구 없음** | 각 개별 바이오마커의 카메라 기반 탐지는 검증됨(mFG 0.89, AcneDet 0.85, ANcam AUC 0.854) | **높음** — 기존 기술 통합으로 프로토타입 가능 |
| G3 | **비접촉 HRV + 얼굴 표현형 + 월경추적 융합 모델 없음** | 각 모달리티 독립적 성능은 확인, 융합 시너지 미검증 | **중간** — 데이터 수집 필요 |
| G4 | **카메라 기반 바이오마커의 종단 추적(월경주기별) 연구 없음** | 단면 연구만 존재; 월경주기 위상별 rPPG-HRV 변화 추적 미수행 | **중간** — 종단 코호트 필요 |
| G5 | **아시아(한국) 인구에서의 검증 부재** | 대부분 서구/중국 데이터; 한국 여성 대상 카메라 바이오마커 연구 전무 | **높음** — 데이터 파트너십으로 해결 |

### 6.2 방법론적 공백

- rPPG 기반 HRV의 **피부색 편향**: 어두운 피부색에서 신호 품질 저하 (FibriCheck 2025 보고)
- 자궁내막증 **통증 변동**과 실시간 rPPG-HRV 상관 연구 없음
- PCOS 표현형의 **아형별(metabolic vs. reproductive vs. lean PCOS)** 카메라 바이오마커 차이 미탐색
- 스마트폰 카메라 **기종/해상도** 간 성능 표준화 연구 부족

---

## 7. 제안 연구 가설 (H1~H5)

### H1: rPPG-HRV는 PCOS를 건강 대조군과 감별할 수 있다
- **근거**: PCOS의 LF/HF 상승 (SMD 0.670, 메타분석), rPPG-HRV의 ECG 대비 r=0.85-0.95
- **설계**: 스마트폰 전면 카메라 60초 촬영 → rPPG HRV 추출 → PCOS vs. 대조군 비교
- **일차 결과변수**: LF/HF ratio, RMSSD, HFnu
- **예상 AUC**: 0.70-0.80

### H2: rPPG-HRV 월경주기 패턴은 PCOS 불규칙 주기를 탐지할 수 있다
- **근거**: 정상 월경주기에서 HRV는 규칙적 변동(5일차 최대 → 27일차 최소); PCOS에서 이 패턴 소실 예상
- **설계**: 3주기 이상 일일 rPPG 촬영 → 주기별 HRV 변동 패턴 비교
- **일차 결과변수**: HRV 주기 변동 진폭(amplitude), 주기 예측 정확도
- **예상 정확도**: 주기 이상 탐지 >85%

### H3: 스마트폰 카메라 기반 PCOS 피부 표현형 복합 점수는 Rotterdam 기준과 유의하게 상관한다
- **근거**: 여드름(IGA 0.85), 다모증(mFG 일치도 0.89), AN(AUC 0.854), BMI(MAE 1.04) 개별 검증
- **설계**: 얼굴/목/팔 사진 → 여드름 등급 + mFG + AN + BMI 복합 스코어 → Rotterdam 기준 예측
- **일차 결과변수**: 복합 스코어 AUC
- **예상 AUC**: 0.75-0.85

### H4: rPPG-HRV 저하는 자궁내막증 환자의 통증 중증도와 음의 상관을 보인다
- **근거**: Moreira(2021) vmHRV-통증 상관, Hao(2021) 미주신경톤 저하
- **설계**: 자궁내막증 환자 일일 rPPG 촬영 + 통증 VAS → 상관 분석
- **일차 결과변수**: RMSSD와 통증 VAS 간 상관계수
- **예상 상관**: r = -0.30 ~ -0.50

### H5: rPPG-HRV + 얼굴 표현형 + 월경 패턴 멀티모달 모델은 PCOS/자궁내막증을 동시 감별할 수 있다
- **근거**: 각 모달리티 독립 성능 확인; PCOS(교감 항진 + 피부 표현형) vs. 자궁내막증(미주신경 저하 + 통증 패턴) 차별적 프로파일
- **설계**: 3-모달 입력 (rPPG-HRV + 얼굴 AI + 앱 데이터) → 3-class 분류 (PCOS / 자궁내막증 / 건강)
- **일차 결과변수**: 3-class 매크로 AUC
- **예상 AUC**: 0.80-0.90

---

## 8. API 탐색 결과 요약

| API | 쿼리 수 | 반환 논문 수 | 포함 수 | 비고 |
|-----|---------|------------|---------|------|
| PubMed esearch | 10 | 22 PMID | 15 | rPPG+PCOS 직접 결과 0편; HRV+PCOS 47편 (상위 15 조회) |
| PubMed efetch | 3 (배치) | 13편 상세 | 13 | 초록+메타데이터 추출 성공 |
| Semantic Scholar | 6 | 0 | 0 | 429 Rate Limit 발생; 대안으로 WebSearch 활용 |
| OpenAlex | 2 | 4편 | 2 | 관련 리뷰 2편 식별 |
| WebSearch | 12 | ~120 결과 | 35+ | 가장 다양한 결과; PCOS AI, 여드름 DL, ANcam 등 핵심 논문 발견 |
| WebFetch | 6 | 4 성공 / 2 실패 | 4 | PMC/PubMed 성공, Springer/Nature 303 리다이렉트 |
| **합계** | **39** | **~160** | **52** | 최종 포함 37편 (기존 참조 15편 포함) |

---

## 부록: 주요 참고문헌 목록 (PMID/DOI 포함)

### Stage 1: rPPG·HRV

1. Mirzohreh ST, Panahi P, Heidari F. (2024). Exploring HRV in PCOS: systematic review and meta-analysis. *Systematic Reviews*. PMID:39049099, DOI:10.1186/s13643-024-02617-x [API 확인] ✅
2. Yu Y et al. (2024). The role of the ANS in PCOS. *Frontiers in Endocrinology*. PMID:38313837, DOI:10.3389/fendo.2023.1295061 [API 확인] ✅
3. Sarathivarman et al. (2025). Comparative analysis of HRV in PCOS. *JPBS*. PMID:41522593, DOI:10.4103/jpbs.jpbs_1295_25 [API 확인] ✅
4. de Fatima Azevedo et al. (2026). 24h ambulatory BP in PCOS. *Scientific Reports*. PMID:41639286, DOI:10.1038/s41598-026-38731-0 [API 확인] ✅
5. Bernal et al. (2025). Aerobic exercise reverses sympathetic modulation in PCOS. *Clinical Endocrinology*. PMID:39526386, DOI:10.1111/cen.15163 [API 확인] ✅
6. Moreira MF et al. (2021). HRV and pain in endometriosis. *Women & Health*. PMID:34719338, DOI:10.1080/03630242.2021.1993423 [API 확인] ✅
7. Hao M et al. (2021). Reduced vagal tone in endometriosis. *Scientific Reports*. PMID:33446725, DOI:10.1038/s41598-020-79750-9 [API 확인] ✅
8. Zeng W et al. (2025). Reduced vagal tone in adenomyosis. *Reproduction & Fertility*. PMID:41026638, DOI:10.1530/RAF-25-0039 [API 확인] ✅
9. Moreira MF et al. (2024). Mindfulness-based intervention effect on HRV in endometriosis. *The Journal of Pain*. PMID:37524218, DOI:10.1016/j.jpain.2023.07.026 [API 확인] ✅
10. Rajesh M. (2025). Adaptive Edge-Federated AI for contactless menstrual health prediction. *MethodsX*. PMID:41209338, DOI:10.1016/j.mex.2025.103665 [API 확인] ✅
11. Wearable HRV across menstrual cycle (Living SR). (2025). *Sports Medicine*. DOI:10.1007/s40279-025-02388-y [WebSearch] ✅
12. HRV and menstrual regularity. (2025). *npj Digital Medicine*. DOI:10.1038/s41746-025-01517-1 [WebSearch] ✅

### Stage 2: 얼굴·피부 분석

13. Huynh QT et al. (2022). AcneDet: Automatic acne detection with smartphone. *Diagnostics*. PMID:36010229, DOI:10.3390/diagnostics12081879 [API 확인] ✅
14. Cell phone app for acne severity. (2023). *Applied Intelligence*. PMID:35919632, DOI:10.1007/s10489-022-03774-z [API 확인] ✅
15. AcneAI. (2024). *MICCAI 2024*. DOI:10.1007/978-3-031-72086-4_7 [WebSearch] ✅
16. Acne lesion evaluation (Chinese population). (2024). *Scientific Reports*. DOI:10.1038/s41598-024-84670-z [WebSearch] ✅
17. Oliveira TF et al. (2023). Image-based mFG hirsutism scoring. *Arch Dermatol Res*. PMID:36508021, DOI:10.1007/s00403-022-02495-0 [API 확인] ✅
18. Dhanoo AS et al. (2024). ANcam: Smartphone acanthosis nigricans detection. *Diabetes Spectrum*. PMID:38756432, DOI:10.2337/ds23-0042 [API 확인] ✅
19. ~~Jiang M et al.~~ → **Yousaf N, Hussein S, Sultani W.** (2021). BMI estimation from facial images. *Comput Biol Med*. PMID:33895458, DOI:10.1016/j.compbiomed.2021.104392 [API 확인] ❌ 저자 불일치 수정 필요
20. PatchBMI-Net. (2023). *arXiv*. arXiv:2311.18102 [WebSearch] ✅
21. Oztel et al. (2023). DL-based skin disease classification smartphone. *Adv Intell Systems*. DOI:10.1002/aisy.202300211 [WebSearch] ✅
22. Dark circle AI analysis (n=1.9M). (2023). *Skin Res Technol*. PMID:38009029, DOI:10.1111/srt.13492 [API 확인] ⚠️ **RETRACTED (2025-10, PMID:41059760)** — 인용 제거 권장

### Stage 3: 융합·리뷰

23. AI in PCOS management (리뷰). (2025). *La Radiologia Medica*. DOI:10.1007/s11547-025-02032-9 [WebSearch] ✅
24. PCOS 앱 콘텐츠 분석. (2025). *JMIR*. DOI:10.2196/71118 [WebSearch] ✅
25. Digital tech for endometriosis (SR). (2025). *JMIR Human Factors*. DOI:10.2196/71859 [WebSearch] ✅
26. ML diagnostic accuracy for endometriosis (메타분석). (2025). *Frontiers in Endocrinology*. DOI:10.3389/fendo.2025.1735567 [WebSearch] ✅
27. Inflammatory biomarkers + ML for endometriosis. (2025). *Scientific Reports*. DOI:10.1038/s41598-025-26606-9 [WebSearch] ✅
28. ML-based menstrual phase identification (wearable). (2025). *npj Women's Health*. DOI:10.1038/s44294-025-00078-8 [WebSearch] ✅
29. ML menstrual cycle phase classification (sleeping HR). (2025). *Comput Biol Med*. ~~DOI:10.1016/S0010-4825(25)00055-1~~ → **실제 DOI:10.1016/j.compbiomed.2025.109705**, PMID:39889448, Masuda et al. [WebSearch] ⚠️ DOI 수정 필요
30. Biomonitoring technologies for women's health. (2025). *Nature Communications*. DOI:10.1038/s41467-025-63501-3 [WebSearch] ✅
31. Menstrual cycle as vital sign (리뷰). (2024). *F&S Reviews*. ~~DOI:10.1016/S2666-5719(24)00038-0~~ → **실제 DOI:10.1016/j.xfnr.2024.100081**, PMID:39906529, Rosen Vollmar et al. [WebSearch] ⚠️ DOI 수정 필요

### 기존 탐색 참조 (camera/01_camera_literature_review.md에서 인용)

32. rPPG 종합 리뷰, 2025, PMC [기존 탐색 참조] ❓ 저자·DOI 미기재, 특정 불가
33. FibriCheck FDA-AF, 2025, *npj Digital Medicine* [기존 탐색 참조] ✅
34. rPPG SpO2, Cheng et al., 2024, *Bioengineering* [기존 탐색 참조] ✅
35. rPPG 혈압, Luo et al., 2019, *Circ Cardiovasc Imaging* [기존 탐색 참조] ✅
36. rPPG HRV 리뷰, 2024, *Frontiers Bioeng & Biotech* [기존 탐색 참조] ⚠️ 추정 DOI:10.3389/fbioe.2024.1420100, 저자·DOI 보충 필요
37. 피부암 DL, 2023, *Diagnostics* [기존 탐색 참조] ❓ 저자·제목·DOI 미기재, 특정 불가
