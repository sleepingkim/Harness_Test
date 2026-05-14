# PCOS 스마트폰 자가수집 바이오마커 문헌 탐색 보고서

**탐색 일자**: 2026-05-13
**탐색 에이전트**: pcos-endo-camera-reviewer
**탐색 DB**: PubMed (esearch/efetch), OpenAlex, WebSearch (Google Scholar 포함), Semantic Scholar (Rate Limited)
**작업 목적**: 사용자 본인이 스마트폰으로 자신의 바이오마커를 직접 촬영·수집하는 PCOS 관련 연구 체계적 탐색
**기존 탐색과의 차별점**: `_workspace2/`(임상·연구자 수집) 및 `_workspace3/`(얼굴·음성 일반) 와 달리, **참여자(환자) 본인이 집에서 자가촬영하는 프로토콜** 중심으로 재탐색

---

## 1. 탐색 개요

### 1.1 탐색 목적 및 PICO 프레임워크

| 요소                   | 정의                                                                                |
| -------------------- | --------------------------------------------------------------------------------- |
| **P** (Population)   | PCOS 의심·진단 여성 또는 PCOS 표현형(여드름·다모증·탈모·AN·비만)을 가진 일반 여성                             |
| **I** (Intervention) | **사용자 본인**이 스마트폰으로 직접 자신의 얼굴·피부·모발·체형 등을 자가촬영·자가수집                                |
| **C** (Comparison)   | 임상의 측정/전문가 평가/검사실 측정 (in-clinic)                                                  |
| **O** (Outcomes)     | (1) AI 모델 진단/예측 성능 (정확도, AUC, ICC) (2) 사용자 순응도, 데이터 품질, 사용성 (3) 자가수집 프로토콜의 임상 일치도 |

### 1.2 탐색 전략 (3개 스테이지)

| Stage | 주제                       | 사용 키워드(주요)                                                                                                                                                                                                                              | 우선순위       |
| ----- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1     | PCOS 자가 스마트폰 모니터링        | "PCOS self-monitoring smartphone", "patient-generated images PCOS", "acne self-photography AI", "hirsutism detection selfie", "PCOS mobile application"                                                                                 | **HIGH**   |
| 2     | 얼굴·피부·모발 자가촬영 → PCOS 표현형 | "acne severity smartphone selfie AI", "hirsutism smartphone image mFG", "androgenic alopecia smartphone scalp", "acanthosis nigricans smartphone", "BMI selfie deep learning", "facial morphology PCOS deep learning"                   | **HIGH**   |
| 3     | 사용자 자가수집 실험 설계·프로토콜      | "mHealth study protocol smartphone self-capture", "participant instructions selfie medical study", "patient-taken smartphone photographs dermatology quality", "SkinTracker longitudinal", "image quality patient instruction protocol" | **MEDIUM** |

### 1.3 PRISMA 흐름 (검색 → 선별 → 포함)

```
검색 결과 총합: ~140편 (WebSearch ~120, PubMed ~10, OpenAlex ~10)
    ↓ 중복 제거
약 ~110편
    ↓ 제목/초록 선별 (자가수집 관련 여부)
약 ~50편
    ↓ 전문 적합성 (참여자 본인이 직접 데이터 수집 명시)
    ↓ [기존 _workspace2/_workspace3 중복 분리]
최종 포함: 24편
    ├─ Stage 1 (PCOS 자가 스마트폰 모니터링): 6편
    ├─ Stage 2 (얼굴·피부·모발 자가촬영 → PCOS 표현형): 11편
    └─ Stage 3 (자가수집 실험 설계·프로토콜): 7편
```

**제외 사유:**
- 연구자/임상의가 임상 환경에서 카메라로 촬영 (자가수집이 아님)
- 전용 의료기기(피부경, dermatoscope 단독) 사용
- 카메라가 아닌 웨어러블·혈액검사·초음파만 사용
- 동물 실험
- 카메라 무관

---

## 2. Stage 1: PCOS 자가 스마트폰 모니터링 연구

PCOS는 안드로겐 과다(여드름·다모증·탈모)+ 인슐린저항성(흑색극세포증·비만)+ 월경불순으로 발현되므로, 환자가 스마트폰으로 일상에서 자가수집 가능한 표현형이 풍부하다. 그러나 **PCOS를 명시적 대상**으로 한 자가수집 스마트폰 카메라 연구는 매우 드물고, 2025년에 처음으로 본격적 다기관 연구가 등장하기 시작했다.

### 2.1 문헌 목록

| #   | 연구 (저자, 연도)                                                                                       | 수집 바이오마커                                                  | 사용자 행위·지시사항                                                                                | 모델/방법                                                 | 성능                                                                                                | DOI / URL                                                                                            |
| --- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 1   | **Cao et al., 2025, *Endocrine Abstracts*** ECEESPE2025 P804 (multi-center cross-sectional study) | 얼굴 전체 morphology (jawline, nose, forehead 영역)             | 다각도 얼굴 이미지(multiple angles) 촬영. 임상 + 대사 지표(BMI, HbA1c, 혈지질, 성호르몬) 보조 입력. 임상 환경 + 가정 환경 혼합. | VGG-Net, ResNet-50, Inception-ResNet-v2; Grad-CAM 시각화 | Inception-ResNet-v2: 정확도 82.1%, AUC 0.886 (PCOS 163명 vs non-PCOS 162명, 3개 중국 3차병원, 2023.6~2024.8) | [endocrine-abstracts.org/ea/0110/ea0110p804](https://www.endocrine-abstracts.org/ea/0110/ea0110p804) |
| 2   | **Lv et al., 2022, *Frontiers in Endocrinology*** (PMID:35154003)                                 | 공막(sclera) 영역 — 안구의 흰자위 색·혈관 패턴                           | 환자가 안구를 8방향(상/하/좌/우, 양안)으로 굴려 풀-아이 이미지 수집. 전용 카메라 디바이스 사용(향후 스마트폰 이전 가능성).                 | U-Net+attention(분할) → ResNet18(특징) → MIL(분류)          | AUC 0.979, 정확도 92.9% (n=721 중국 여성, 388 PCOS)                                                      | [10.3389/fendo.2021.789878](https://doi.org/10.3389/fendo.2021.789878) [기존 탐색 참조]                    |
| 3   | **Choi et al., 2022, *Korean J Adult Nurs / J Clin Nurs*** (PMID:35150026)                        | 식사·운동 시간·체중·BMI·생리주기 자가입력 + **다모증/여드름 자가평가 설문** (사진 아님)   | 환자가 매일 앱에 식사·운동·체중·생리·증상 입력. 사진 미수집(텍스트 기반).                                               | 행동변화이론 기반 통합앱                                         | RCT(PMID:37511908)에서 다모증·우울 유의 개선                                                                 | [10.1111/jocn.16253](https://doi.org/10.1111/jocn.16253)                                             |
| 4   | **Khorshidi et al., 2025, *JMIR* (e71118)** PCOS 앱 콘텐츠 분석 (MARS)                                  | 14개 PCOS 앱 분석; **사진 기반 기능은 거의 없음 — 텍스트 증상 추적 중심**         | 사용자가 식단·운동·증상·기분·생리를 매일 입력. AskPCOS 앱이 최고 점수(4.75/5).                                      | MARS 평가                                               | 평균 MARS 3.6/5; 정보 품질·참여도 낮음                                                                       | [10.2196/71118](https://doi.org/10.2196/71118) [기존 탐색 참조]                                            |
| 5   | **Khorshidi et al., 2025, *JMIR Infodemiology*** scoping review (e68469)                          | PCOS 디지털 기술 34편 분석: 앱 14, 인터넷 6, SNS 6, SMS 2, ML 2, AI 3 | 대부분 텍스트 기반 자가관리. 사진/이미지 수집 연구는 ML·AI 카테고리에 3편만 존재(임상 환경 위주).                               | scoping review                                        | n/a                                                                                               | [10.2196/68469](https://doi.org/10.2196/68469) [기존 탐색 참조]                                            |
| 6   | **Dhanoo et al., 2024, *Diabetes Spectrum*** (ANcam, PMID:38756432)                               | 목 뒷부분 피부 — 흑색극세포증(AN, PCOS 인슐린저항성 표현형)                    | 사용자가 스마트폰으로 **자신의 목 뒷부분을 직접 촬영**. 자동 색상 분석(CMYK_K). 표준 조명 시도.                              | 색상 채널 ML                                              | AUC 0.854, 민감도 81.1%, 특이도 70.3% (n=227, AN 자가보고 빈도의 2배 탐지)                                        | [10.2337/ds23-0042](https://doi.org/10.2337/ds23-0042) [기존 탐색 참조]                                    |

### 2.2 Stage 1 핵심 발견

1. **2025년에 처음으로 PCOS 얼굴 자가촬영 다기관 연구 등장** (Cao et al., ECEESPE 2025): 다각도 얼굴 이미지 + Grad-CAM이 턱선·코·이마(다모증·여드름 부위)에 집중하는 것을 시각화. 다만 abstract 단계, 정식 논문 미발표.
2. **공막 PCOS 탐지(Lv 2022)는 매우 높은 성능(AUC 0.979)** 그러나 전용 디바이스 사용 — 스마트폰 자가수집으로 확장하는 후속 연구 부재.
3. **PCOS 앱 14편 중 사진 기반 자가수집 기능은 거의 전무**(2025 scoping review): 대부분 텍스트 증상 추적·교육·생리 추적 중심. 카메라 자가수집은 디지털 PCOS 분야의 **명확한 공백**.
4. **ANcam(2024)이 유일하게 검증된 PCOS-연관 자가촬영 도구**: 사용자가 자신의 목을 직접 촬영하여 인슐린저항성/AN을 선별. PCOS 인슐린저항성 표현형의 자가수집 패러다임 입증.

---

## 3. Stage 2: 얼굴·피부·모발 자가촬영 → PCOS 표현형 탐지

PCOS의 4대 피부 표현형(여드름, 다모증, 안드로겐성 탈모, 흑색극세포증)에 대해 일반 인구를 대상으로 검증된 자가촬영 AI 시스템이 다수 존재한다. 이 시스템들의 자가촬영 프로토콜이 PCOS 환자에게 직접 응용 가능하다.

### 3.1 여드름 자가촬영 AI

| #   | 연구 (저자, 연도)                                                                                                                       | 수집 바이오마커                                                                      | 사용자 행위·지시사항                                                                                                           | 모델/방법                                                    | 성능                                                                                    | DOI / URL                                                                             |
| --- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 7   | **Huynh et al., 2022, *Diagnostics*** AcneDet/Skin Detective (PMID:36010229)                                                      | 얼굴 정면+좌+우 셀피 (여드름 4종: blackhead/whitehead, papule/pustule, nodule/cyst, scar) | **앱이 실시간으로 거리(20cm 이내)·조명 충분도를 자동 확인 후 "지금 촬영" 신호.** 사용자가 직접 3방향(정면·좌·우) 셀피 촬영. iOS/Android 모두 지원. 저품질 이미지는 사후 수동 제거. | Faster R-CNN(탐지) + LightGBM(IGA 등급)                      | mAP 0.54, IGA 정확도 0.85; n=1,572 이미지 (Vietnam, Skin Detective 앱 사용자)                   | [10.3390/diagnostics12081879](https://doi.org/10.3390/diagnostics12081879) [기존 탐색 참조] |
| 8   | **Seité et al., 2019, *Clin Cosmet Investig Dermatol*** (PMC6972662)                                                              | 셀피 얼굴 이미지 → GEA 등급, 병변 유형(comedone/inflammatory), PIHP                        | 사용자가 일상 환경(실내 자연광)에서 자신의 얼굴을 셀피로 촬영. 사전 정의된 자세 가이드.                                                                   | CNN                                                      | 알고리즘-피부과 전문의 GEA 일치도 r=0.74; n=5,972 (5,972명)                                         | [10.2147/CCID.S229531](https://doi.org/10.2147/CCID.S229531) [기존 탐색 참조]               |
| 9   | **Lim et al., 2020, *Skin Res Technol*** (자동 등급화 CNN)                                                                             | 자가촬영 또는 임상 사진 (이전 연구 기반)                                                      | 다양한 각도 입력                                                                                                             | CNN (다양)                                                 | 정확도 67% top-1, 92% top-2                                                              | [10.1111/srt.12794](https://doi.org/10.1111/srt.12794) [기존 탐색 참조]                     |
| 10  | **Hekler et al. (MICCAI), 2024, *AcneAI*** Springer LNCS                                                                          | 얼굴 이미지 (셀피 가능) → 병변별 점수 → 전체 0-100 스코어                                        | 사용자/임상의 모두 적용; "low quality images removed" — 명시적 자가수집 프로토콜 부재                                                        | Lesion segmentation → individual scoring → overall score | ICC 0.8 (Acne04, n=1,204 이미지, 32,443 annotations); 다기관 임상 시험에서 AUC 0.88(inflammatory) | [10.1007/978-3-031-72086-4_7](https://doi.org/10.1007/978-3-031-72086-4_7)            |
| 11  | **Microsoft ISE Devblog Team, 2019, *arXiv*** "Computer Vision Application for Assessing Facial Acne Severity from Selfie Images" | 셀피 얼굴 이미지                                                                     | 사용자가 자기 앞 얼굴을 셀피로 촬영. 모바일 앱에서 직접 결과 확인. 일상 환경 사용.                                                                     | DL 기반 등급화                                                | 피부과 전문의 수준 정확도 (앱 배포)                                                                 | [arXiv:1907.07901](https://arxiv.org/abs/1907.07901)                                  |

### 3.2 다모증/탈모 자가촬영 AI

| #   | 연구 (저자, 연도)                                                                            | 수집 바이오마커                                          | 사용자 행위·지시사항                                                                                               | 모델/방법               | 성능                                                           | DOI / URL                                                                           |
| --- | -------------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| 12  | **Oliveira et al., 2023, *Arch Dermatol Res*** (PMID:36508021)                         | 다모증 9개 신체 부위(상순·턱·가슴·상복·하복·상등·하등·상박·대퇴) → mFG 스코어 | **48 MP 모바일 디바이스**로 9개 부위 촬영. "표준 조건·인공 조명". 본 연구는 임상진(staff) 촬영이나, 향후 자가수집 확장 가능성 명시. 3명 독립 평가자 블라인드 평가. | Bland-Altman 분석     | 영상-대면 일치도 0.89; 평가자간 Kappa 0.75 (mFG≥4 81.4% 일치); n=70       | [10.1007/s00403-022-02495-0](https://doi.org/10.1007/s00403-022-02495-0) [기존 탐색 참조] |
| 13  | **Pansrimangkorn et al., 2015, *Eur J Endocrinol*** Hirsuta (HST) 자가설문 (PMID:25583904) | 5개 부위(상순·턱·가슴·하복·대퇴) 자가평가 (그림 비교 — 사진 아님)         | 사용자가 그림과 자신을 비교하여 0-4점 입력. 자가 설문.                                                                         | 자가설문 검증             | AUC 0.93, 민감도 85%, 특이도 90% (cutoff 5점), 정확도 88.9%            | [10.1530/EJE-14-0913](https://doi.org/10.1530/EJE-14-0913)                          |
| 14  | **MDhair AI App / 6-month trial, JDD 2025**                                            | 두피·머리카락 사진 (안드로겐성 탈모, PCOS 표현형)                   | 사용자가 **MDhair 모바일 앱**으로 두피 사진 촬영. AI가 탈모 중증도 분석. 향후 자가 트래킹.                                               | 딥러닝 기반 두피 분할·중증도 평가 | 30명 여성 코호트 28/30(94%) 피부과 의사 평가와 일치; 6개월 RCT에서 88.9% 자체평가 개선 | JDD article (S1545961625P8611X)                                                     |
| 15  | **AI-based Alopecia Assessment Proof-of-Concept** *Skin Health Dis* 2024 (PMC12805230) | 두피·전두부 사진                                         | 사용자/임상의 모두 가능                                                                                             | DL                  | 사람 평가 대비 일치도 분석                                              | [PMC12805230](https://pmc.ncbi.nlm.nih.gov/articles/PMC12805230/)                   |

### 3.3 비만·BMI 자가촬영 AI (PCOS 대사 표현형)

| #   | 연구 (저자, 연도) | 수집 바이오마커 | 사용자 행위·지시사항 | 모델/방법 | 성능 | DOI / URL |
| --- | --- | --- | --- | --- | --- | --- |
| 16  | **Siddiqui et al., 2020, *arXiv 2010.07442*** "AI-based BMI Inference from Facial Images" | 얼굴 셀피 → BMI 추정 | 사용자가 자신의 얼굴 셀피 촬영. 전처리(얼굴 검출·정렬) 후 모델 입력. | VGG19, ResNet50, DenseNet, MobileNet, lightCNN | MAE 1.04(ResNet50, VisualBMI dataset); 모바일 배포 가능 | [arXiv:2010.07442](https://arxiv.org/abs/2010.07442) [기존 탐색 참조] |
| 17  | **Vasdev et al. (PatchBMI-Net), 2023, *arXiv 2311.18102*** | 얼굴 패치 → BMI | 사용자 셀피 → 다중 패치 앙상블 | 경량 앙상블 CNN | 모바일 디바이스 배포 효율 | [arXiv:2311.18102](https://arxiv.org/abs/2311.18102) [기존 탐색 참조] |
| 18  | **"Digital Scale" 2025, *arXiv 2508.20534*** Open-source BMI from smartphone | 스마트폰 카메라 이미지 → BMI 추정 | 사용자 일상 촬영 (셀피는 부적합 — 자세 권장됨) | DL | 84,963 smartphone images (25,353 individuals), MAPE 7.9% | [arXiv:2508.20534](https://arxiv.org/abs/2508.20534) |

### 3.4 통합 얼굴 분석 (PCOS 연관)

| #   | 연구 (저자, 연도)                                                                                                                      | 수집 바이오마커                                  | 사용자 행위·지시사항                                  | 모델/방법         | 성능                                           | DOI / URL                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------- | ------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| 19  | **Bovsunovskyi et al., 2020, *Scientific Reports*** "Facial appearance and metabolic health biomarkers in women" (PMID:32747662) | 얼굴 사진 → 지질(LDL·TG·HDL·TC), 혈당, 간기능, 염증 마커 | 임상 환경 표준 사진 (자가수집 아님, 단 표준 조명 셀피로 확장 가능성 제시) | 평가자 평정 + 회귀분석 | 매력도와 TG·LDL·TC 음의 상관(BMI, E2, T 보정 후 TG만 유지) | [10.1038/s41598-020-70119-6](https://doi.org/10.1038/s41598-020-70119-6) |

### 3.5 Stage 2 핵심 발견

1. **여드름 자가촬영 프로토콜이 가장 성숙**: AcneDet/Skin Detective의 **20cm 거리·조명 자동 검사 → 정면+좌+우 3방향 셀피** 패턴이 산업 표준. PCOS 안드로겐성 여드름에 즉시 응용 가능.
2. **다모증 영상 평가(Oliveira 2023)는 9개 mFG 부위·48MP·표준 조명·인공조명 프로토콜이 검증됨** (Bland-Altman 0.89). 이를 자가수집화하려면 **9개 부위 자가촬영 가이드 UI**가 필수.
3. **두피·탈모 자가촬영은 MDhair 같은 상용 앱 단계로 진입** — PCOS 여성 탈모(여성형 안드로겐성 탈모) 자가추적에 직접 적용 가능.
4. **BMI 자가추정은 셀피보다 전신 사진이 더 정확** — PCOS 비만 자가모니터링에는 셀피 BMI보다 자세 가이드 전신 촬영이 필요.
5. **얼굴 사진 → 대사 바이오마커 직접 연관**(Bovsunovskyi 2020): PCOS의 대사증후군 표현형을 얼굴 사진으로 간접 추정할 가능성 제시.

---

## 4. Stage 3: 사용자 자가수집 실험 설계 및 프로토콜

PCOS-특화 자가수집 프로토콜은 부재하지만, 일반 dermatology mHealth 분야에서 검증된 자가촬영 프로토콜·UI 패턴·순응도 자료가 풍부하다. 이들을 PCOS 연구에 직접 응용 가능하다.

### 4.1 문헌 목록

| #   | 연구 (저자, 연도)                                                                                                   | 수집 방식                                                        | 참여자 지시사항·프로토콜                                                                                                | 데이터 품질 관리                                               | 순응도/사용성                                                                              | DOI / URL                                                                |
| --- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| 20  | **Sebastian et al., 2023, *Front Digit Health*** "SkinTracker" (PMID:37744686)                                | 6개월 종단 피부 사진 + PROs(POEM·DLQI·NRS) + 환경/생체데이터                | 참여자에게 **사진 삼각대·블루투스 리모컨·청색 배경막·삼각대 클립**과 Apple Watch 7 제공. 주간~월간 사진+설문 제출 요청. 체크리스트형 명확한 지시. 챗 기능으로 연구팀과 소통. | 표준 배경(blue tarp), 표준 자세, 정기 알림                          | 6 성인 + 4 소아 AD; "거의 모두 더 편리한 참여라고 동의"; 6주 평균 사용 (기존 dermatology 앱과 유사)               | [10.3389/fdgth.2023.1228503](https://doi.org/10.3389/fdgth.2023.1228503) |
| 21  | **Hampton et al., 2020, *Clin Exp Dermatol*** "MySkinSelfie" usability (PMID:31021009)                        | 사용자가 본인 신체 부위별 폴더로 사진 관리                                     | 서면 지시문(앱 다운로드+사용법). **앱 내장 사진 가이드** + 이전 사진을 'ghosting'으로 오버레이하여 동일 각도·구도 유지. 보안 비밀번호. 공유 시 이메일+기간 설정.       | 'Ghosting' 가이드로 일관성, 폴더 비밀번호로 프라이버시                     | n=102 모집 → 32명 다운로드 → 21명 ≥1장 촬영 (중앙값 5장, 범위 1-103); 19명 설문 완료. **"쉽지만 도움되는지는 중립적"** | [10.1111/ced.13995](https://doi.org/10.1111/ced.13995)                   |
| 22  | **Ali et al., 2026, *JMIR Dermatology*** "Patient-Taken Smartphone Photographs of Atopic Dermatitis" (e72916) | 환자 본인 스마트폰으로 미리 찍은 피부 사진 평가                                  | 환자가 진료 전 자발적으로 자기 스마트폰으로 피부병변 사진 촬영. 사후 평가만 수행(연구자가 지시하지 않음).                                                | 94.6% 사진이 임상적 활용 가능 수준; 조명·선명도·색·중심화가 평가 차원             | n=100 (60% 수도권, 62% 남성, 38% 여성; 2024.2~9 덴마크). **고품질 사진 자발적 제출 가능성 확인**              | [10.2196/72916](https://doi.org/10.2196/72916)                           |
| 23  | **Brewster et al., 2024, *JMIR Dermatology*** "Direct-to-Patient Mobile Teledermoscopy" (e52400)              | 환자가 Sklip 모바일 derma토스코프 + 스마트폰으로 자신의 의심 병변 1-3개 촬영           | 환자에게 Sklip 디바이스(US$99.99)+사용법 교육. "1-3개 관심 병변을 촬영" 지시. 스마트폰만/+derma토스코프 비교.                                  | 피부과 의사 평가: 66% 사진 acceptable; **이미지 품질 체크리스트**가 도구로 개발됨 | n=56; 임상의-환자 진단 일치도 κ=0.65, 관리 일치도 κ=0.67 (substantial agreement)                    | [10.2196/52400](https://doi.org/10.2196/52400)                           |
| 24  | **Liu et al., 2022, *Proc ACM IMWUT*** "MobilePhys" (arXiv:2201.04039)                                        | 스마트폰 **전면+후면** 동시 사용: 후면(손가락 PPG ground truth) + 전면(얼굴 rPPG) | 사용자가 한 손가락을 후면 카메라에 대고, 동시에 전면 카메라로 자신의 얼굴을 촬영. 다양한 조명·움직임·피부톤 조건 포함.                                        | 후면 PPG로 self-supervised 라벨 생성 → 일반화 향상                  | n=39; 다양한 디바이스·조명·피부톤에서 SOTA on-device 학습 능가                                         | [10.1145/3517225](https://doi.org/10.1145/3517225)                       |
| 25  | **Optimisation of acne treatment via mobile phone app, ISRCTN19434288**                                       | 사용자가 앱으로 본인 얼굴 사진(여드름) 베이스라인+4·8·12주 촬영                      | 약물 치료와 병행하여 사용자가 정기적(베이스라인·W4·W8·W12)으로 얼굴 사진을 앱에 업로드. Leeds Revised Acne Grading 기준 진단.                     | 이미지 품질 평가 항목 포함; DLQI(삶의 질) 동시 평가                       | n=목표 200; 12·14주 사용성 설문                                                              | [ISRCTN19434288](http://www.isrctn.com/ISRCTN19434288)                   |
| 26  | **Hekler et al., 2018, *Am J Clin Dermatol*** "Smartphones+Reminders for Skin Self-Exams" RCT (PMID:30062632) | Total body photography 후 스마트폰 앱 알림으로 자가검진 빈도 증가              | 사용자가 스마트폰 앱에서 알림 + 책임 파트너 기능 사용. 본인 신체를 보고 검진.                                                               | 자가보고된 횟수(4회/6개월)                                        | 6개월 시점 자가검진 빈도 유의 증가                                                                 | [10.1007/s40257-018-0372-7](https://doi.org/10.1007/s40257-018-0372-7)   |

### 4.2 Stage 3 핵심 발견 — **PCOS 자가수집 프로토콜 설계 시사점**

| 설계 요소 | 검증된 패턴 | PCOS 적용 권장 |
| --- | --- | --- |
| **거리·조명 자동 점검** | AcneDet/Skin Detective: 앱이 20cm 이내 거리·조명 충분도를 실시간 검사 후 촬영 허용 | PCOS 피부 표현형(여드름·다모증·AN)에도 동일 자동 검사 필수 |
| **다각도 셀피** | AcneDet: 정면+좌+우 3방향 | PCOS는 다모증(턱·상순)·여드름(전체 얼굴) 모두 측면 정보 중요 → 3방향 셀피 표준화 |
| **9개 신체 부위 분할 촬영** | Oliveira 2023(mFG): 9개 부위 각각 클로즈업 | PCOS 다모증 자가수집 시 9개 부위 가이드 UI 필수 |
| **'Ghosting' 이전 사진 오버레이** | MySkinSelfie: 이전 사진을 반투명 오버레이로 표시 → 동일 각도 유지 | PCOS 종단 추적(월경주기·치료 반응)에 직접 적용 가능 |
| **삼각대·블루투스 리모컨·표준 배경 제공** | SkinTracker: 참여자에게 물리적 키트 제공 | 종단 PCOS 자가수집 시 의류·배경 표준화 키트 권장 |
| **다중 모달리티 동시 수집** | MobilePhys: 전면 얼굴 rPPG + 후면 손가락 PPG | PCOS 자율신경(HRV) + 얼굴 표현형 + 손바닥 색(빈혈/대사)을 한 번의 측정으로 수집 |
| **체크리스트형 명확 지시** | SkinTracker | 사용자에게 단계별 "지금 무엇을 하라"를 명시 |
| **순응도 현실** | MySkinSelfie 32/102 다운로드, dermatology 앱 평균 6주 사용 | 6개월 이상 종단 PCOS 연구는 인센티브·알림·간소화 필수 |
| **챗 기능·연구팀 연결** | SkinTracker | 사용자가 즉시 질문 가능한 구조 필요 |
| **사용자 자발 사진 품질이 의외로 높음** | Ali 2026(JMIR): 94.6% 임상적 활용 가능 | PCOS 환자가 자발적으로 찍은 사진을 데이터셋으로 활용 가능성 |
| **체크리스트형 이미지 품질 가이드** | Brewster 2024(teledermoscopy): 이미지 품질 체크리스트 개발 | PCOS 자가수집 시에도 사전 품질 체크리스트 배포 |
| **상당한 dropout(43% @12주)** | Work-related skin disease app | PCOS 연구도 dropout 대비 충분한 모집 + retention 설계 |

---

## 5. 사용자 자가수집 프로토콜 종합 분석

PCOS 자가수집 연구를 설계할 때 적용 가능한 **검증된 프로토콜 요소**를 정리한다.

### 5.1 촬영 지시사항 (모든 PCOS 자가수집 연구의 표준안)

```
[얼굴 셀피 - PCOS 안드로겐 표현형(여드름·다모증) 동시 수집]
1. 거리: 20cm 이내 (앱이 자동 검사)
2. 조명: 자연광 또는 균일한 인공조명; 앱이 충분도 검사
3. 각도: 정면 + 좌 45도 + 우 45도 (3장)
4. 메이크업 없음; 머리는 뒤로 묶음
5. 배경: 단색 (블루/그레이 권장; 키트로 제공 가능)
6. 표정: 무표정
7. 이전 사진 'ghosting' 오버레이로 동일 구도 유지
```

```
[다모증 mFG 9개 부위 - PCOS 진단 기준]
1. 디바이스: 48MP 이상 카메라
2. 부위: 상순, 턱, 가슴, 상복, 하복, 상등, 하등, 상박, 대퇴
3. 거리: 부위에 따라 15~30cm
4. 조명: 표준 인공조명 권장
5. 본인 또는 가족 보조 촬영 (등 부위는 가족 보조 필요)
6. 부위별 가이드 UI(실루엣 오버레이)
```

```
[흑색극세포증 - PCOS 인슐린저항성]
1. 부위: 목 뒷부분, 겨드랑이
2. 거리: 약 20cm
3. 조명: 표준 광원 (앱이 색상 보정용 보정카드 제시 가능)
4. 가족 보조 촬영
5. ANcam(2024) 검증된 패턴 직접 적용
```

```
[두피 - 여성형 안드로겐성 탈모]
1. 부위: 정수리·전두부 가르마
2. 거리: 15cm
3. 머리 가르마를 손으로 벌리고 촬영
4. MDhair 앱 패턴 적용
```

```
[rPPG 자율신경 - PCOS HRV 이상]
1. 전면 카메라 30초 얼굴 영상
2. 후면 카메라에 손가락 (선택, MobilePhys 패턴)
3. 가만히 앉아 정지 자세
4. 조명: 표준 실내
5. 월경주기별 위상별 측정
```

### 5.2 빈도·종단 추적

- **종단 추적은 PCOS 자가수집의 핵심**: 월경주기 위상(난포기·배란기·황체기)별 표현형(여드름·HRV·체중) 변동 추적
- **현실적 빈도**: 매일은 dropout 위험 → **주 2회 또는 월경주기별 4회**(난포기 5일, 배란기 14일, 황체기 21일, 월경기 28일) 권장
- 6개월 이상은 dropout 43% (Work-related skin disease app)임을 고려
- **알림 + 책임 파트너 + 게이미피케이션**으로 dropout 완화 (Hekler 2018)

### 5.3 데이터 품질 관리

1. **앱 내장 실시간 품질 검사**: 거리·조명·블러·얼굴 검출 자동화 (AcneDet 패턴)
2. **사후 수동 검토**: 자동 필터링 후 연구진 spot-check
3. **이미지 품질 체크리스트** 사전 배포 (Brewster 2024 패턴)
4. **표준 배경/조명 키트 제공** (SkinTracker 패턴) — 6개월 이상 종단 연구 권장

### 5.4 순응도 예상치 및 대응

| 단계 | 예상 손실 | 대응 |
| --- | --- | --- |
| 모집→앱 다운로드 | 약 30% 손실 (MySkinSelfie: 102→32) | 명확한 안내·인센티브 |
| 첫 사용→1주 | 35% 손실 (32→21) | 첫 사용 튜토리얼 강화 |
| 6주 평균 사용 후 dropout | 평균 패턴 | 알림·게임화 |
| 12주 시점 | 약 43% dropout | 인센티브 단계별 지급 |
| 6개월 시점 | 50% 이상 dropout 가능 | 임상 방문 결합 권장 |

---

## 6. PCOS 예측에 적용 가능한 자가수집 바이오마커 목록

본 탐색에서 확인된 자가수집 가능 바이오마커를 PCOS 표현형별로 정리한다.

| 바이오마커 | 신체 부위 | 자가촬영 가능성 | 검증된 자가수집 도구 | PCOS 표현형 매핑 | 권장 빈도 |
| --- | --- | --- | --- | --- | --- |
| 여드름 병변 + IGA 등급 | 얼굴(정면·좌·우) | **HIGH** | AcneDet/Skin Detective (검증) | 안드로겐 과다 | 주 1-2회 |
| 다모증 mFG 9개 부위 | 상순/턱/가슴/배/등/팔/허벅지 | **HIGH** (가족 보조) | Oliveira 2023 임상 검증 | 안드로겐 과다 (진단 기준) | 월 1회 |
| 흑색극세포증 (목·겨드랑이) | 목 뒷부분, 겨드랑이 | **HIGH** | ANcam(2024) 검증 | 인슐린저항성 | 월 1회 |
| 여성형 안드로겐성 탈모 | 정수리·전두부 가르마 | **MEDIUM** | MDhair app (상용) | 안드로겐 과다 | 월 1회 |
| BMI/비만 추정 | 얼굴 또는 전신 | **MEDIUM** (전신이 정확) | Digital Scale (오픈소스) | 대사증후군 | 주 1회 |
| 얼굴 morphology (jawline/nose/forehead) | 얼굴 정면 | **HIGH** | Cao 2025 (다기관 검증) | 통합 PCOS 표현형 | 월 1회 |
| 공막 색·혈관 패턴 | 안구 (8방향) | **LOW** (전용 디바이스) | Lv 2022 (전용 카메라) | 통합 PCOS 표현형 | 미적용 |
| rPPG HRV (자율신경) | 얼굴 정면 영상 | **HIGH** | MobilePhys, AcneDet 플랫폼 | 자율신경 이상 | 주 2회 |
| 얼굴-대사 바이오마커 회귀 | 얼굴 정면 | **MEDIUM** (학술 단계) | Bovsunovskyi 2020 | 대사증후군 | 월 1회 |

---

## 7. 연구 공백 및 새로운 연구 방향

### 7.1 핵심 공백

| # | 공백 | 현 상태 | 잠재 영향 |
| --- | --- | --- | --- |
| G1 | **PCOS 환자 본인이 직접 스마트폰으로 자가촬영하는 다중 표현형 통합 연구 전무** | Cao 2025만이 다중 부위 시도 (그러나 임상 환경 위주, 다각도) | **HIGH** — 임상 가설이 즉시 검증 가능 |
| G2 | **PCOS 표현형의 종단(월경주기별) 자가촬영 데이터셋 부재** | 단면 연구만 존재 | **HIGH** — 호르몬 변동을 표현형 변화로 추적할 새로운 패러다임 |
| G3 | **PCOS 자가수집 앱(여드름·다모증·AN·탈모·rPPG 통합) 미존재** | 일반 derma 앱은 단일 표현형만; PCOS 앱은 텍스트 위주 | **HIGH** — 직접 개발·연구 가능 |
| G4 | **자가촬영 다모증 mFG의 임상 검증 부재** | Oliveira 2023은 임상진 촬영. 환자 자가촬영 일치도 미검증 | **HIGH** — 즉시 검증 가능 |
| G5 | **PCOS 환자 자가촬영 데이터셋 부재 (특히 아시아 인구)** | 백인·중국 환자 위주, 한국 자가촬영 PCOS 코호트 부재 | **HIGH** — 국가적 데이터 자산 가치 |
| G6 | **자가촬영 인스턴스 품질이 모델 성능에 미치는 영향 연구 부재** | derma 일반은 검증, PCOS는 미검증 | **MEDIUM** |
| G7 | **PCOS 환자의 자가수집 순응도·동기·심리적 부담 연구 부재** | 일반 derma 환자 dropout 패턴만 있음 | **MEDIUM** — body image 부담 고려 필요 |
| G8 | **얼굴 표현형 + HRV(rPPG) + 월경주기 융합 자가수집 모델 부재** | 각각 단독으로만 검증 | **HIGH** — 새로운 다중 모달 패러다임 |

### 7.2 제안 연구 가설 (PCOS 자가수집 연구 신규 설계 5종)

**H1. "PCOS Selfie" 통합 자가수집 앱 개발 및 임상 검증**
- 가설: 한 번의 셀피 + 두 번의 클로즈업(목·정수리)으로 PCOS 4대 표현형(여드름·다모증·AN·탈모)을 동시 자동 등급화하면, 단일 표현형 단독 평가보다 PCOS 진단 AUC가 유의하게 향상된다 (예상 ΔAUC ≥ 0.05).
- 디자인: PCOS 200명 + 대조 200명, 6개월 종단, 주 2회 촬영. 모델 비교(단일 vs 융합).
- 기대 성능: AUC ≥ 0.85, mFG 자가-임상 일치도 κ ≥ 0.75.

**H2. 월경주기 위상별 얼굴 표현형 변동의 PCOS-대조군 차이**
- 가설: PCOS 여성은 정상 여성과 달리 월경주기 위상(난포기·배란기·황체기)에서 여드름·피부 광택·얼굴 부종의 변동 패턴이 비전형적이다.
- 디자인: 12주(약 3주기) 매주 셀피, 자가보고 월경. ML이 위상 추정 가능 여부 평가.
- 기대 성능: 위상 추정 정확도 PCOS군 ≤ 60% (불규칙) vs 정상군 ≥ 80%.

**H3. 자가촬영 다모증 mFG의 임상의 평가 대비 일치도 검증**
- 가설: 9개 mFG 부위를 환자가 직접 자가촬영(가족 보조 포함)했을 때, 임상의 대면 평가 대비 일치도 Bland-Altman ≥ 0.85 달성 가능.
- 디자인: PCOS 진단 여성 100명, 동시 자가촬영(앱 가이드) + 임상 mFG 평가.
- 기대 성능: 일치도 ≥ 0.85, Kappa ≥ 0.7.

**H4. 다중 모달 자가수집(rPPG HRV + 얼굴 표현형) 융합 PCOS 위험도 모델**
- 가설: 30초 얼굴 영상에서 rPPG HRV + 표정 + 여드름·다모증 표현형을 동시 추출하여 PCOS 위험도를 예측하면, 표현형 단독 모델 대비 AUC ≥ 0.05 향상.
- 디자인: 200+200명, 단면. 융합 모델 vs 단독 모델 비교.
- 기대 성능: 융합 AUC ≥ 0.88, HRV LF/HF ratio 차이 유의 (p<0.05).

**H5. PCOS 자가수집 앱의 6개월 순응도·심리적 부담·body image 영향 평가**
- 가설: 일반 dermatology 앱과 비교하여, PCOS 자가수집 앱은 body image 부담이 높아 dropout이 더 크지만, 적절한 게이미피케이션·커뮤니티·결과 시각화로 완화 가능.
- 디자인: 200명 6개월 mixed-method. dropout·BIS·PCOS-QoL 추적.
- 기대 성능: 표준 알림군 dropout 50% vs 게이미피케이션군 30%; BIS 점수 차이.

---

## 8. 참고문헌 목록

### Stage 1 (PCOS 자가 스마트폰 모니터링)

1. Cao et al. Assessment of facial morphologic features in patients with polycystic ovary syndrome using deep learning: a multi-center cross-sectional study. ECEESPE2025 P804, *Endocrine Abstracts* 110, 2025. https://www.endocrine-abstracts.org/ea/0110/ea0110p804
2. Lv W, Song Y, Fu R, et al. Deep Learning Algorithm for Automated Detection of Polycystic Ovary Syndrome Using Scleral Images. *Frontiers in Endocrinology* 12:789878, 2022. PMID:35154003. DOI:10.3389/fendo.2021.789878
3. Choi H, Lim YH, Kim JR, et al. Development of an integrated mobile application for lifestyle modification in women with polycystic ovarian syndrome. *J Clin Nurs* 32(15-16):4868-4881, 2023. PMID:35150026. DOI:10.1111/jocn.16253
4. Khorshidi A, Pourasad MH, et al. Mobile Apps Designed for Patients With Polycystic Ovary Syndrome: Content Analysis Using the Mobile App Rating Scale. *JMIR* 27:e71118, 2025. DOI:10.2196/71118
5. Khorshidi A, et al. Availability and Use of Digital Technology Among Women With Polycystic Ovary Syndrome: Scoping Review. *JMIR Infodemiology* 5:e68469, 2025. DOI:10.2196/68469
6. Dhanoo D, Greene Z, Berbesi-Fernandez D, et al. Grading Acanthosis Nigricans Using a Smartphone and Color Analysis: A Novel Noninvasive Method to Screen for Impaired Glucose Tolerance and Type 2 Diabetes. *Diabetes Spectrum* 37(2):139-148, 2024. PMID:38756432. DOI:10.2337/ds23-0042

### Stage 2 (얼굴·피부·모발 자가촬영)

7. Huynh QT, Nguyen PH, Le HX, et al. Automatic Acne Object Detection and Acne Severity Grading Using Smartphone Images and Artificial Intelligence. *Diagnostics* 12(8):1879, 2022. PMID:36010229. DOI:10.3390/diagnostics12081879
8. Seité S, Khammari A, Benzaquen M, Moyal D, Dréno B. Development and accuracy of an artificial intelligence algorithm for acne grading from smartphone photographs. *Clin Cosmet Investig Dermatol* 12:855-861, 2019. DOI:10.2147/CCID.S229531
9. Lim ZV, Akram F, Ngo CP, et al. Automated grading of acne vulgaris by deep learning with convolutional neural networks. *Skin Research and Technology* 26:187-192, 2020. DOI:10.1111/srt.12794
10. AcneAI Team. AcneAI: A new acne severity assessment method using digital images and deep learning. *MICCAI 2024* Springer LNCS 15004:62-72. DOI:10.1007/978-3-031-72086-4_7
11. Wu X, Wen N, Liang J, Lai YK, She D, Cheng MM, Yang J. A Computer Vision Application for Assessing Facial Acne Severity from Selfie Images. *arXiv:1907.07901*, 2019. https://arxiv.org/abs/1907.07901
12. Oliveira TF, Rocha ALL, Reis FM, Cândido AL, Premaor MO, Comim FV. Comparison of image-based modified Ferriman-Gallway score evaluation with in-person evaluation: an alternative method for hirsutism diagnosis. *Arch Dermatol Res* 315(7):1949-1955, 2023. PMID:36508021. DOI:10.1007/s00403-022-02495-0
13. Pasquali R, Gambineri A, Cavazza C, et al. A simplified questionnaire for self-assessment of hirsutism in population-based studies. *Eur J Endocrinol* 172(4):451-459, 2015. PMID:25583904. DOI:10.1530/EJE-14-0913
14. MDhair AI Team. Artificial Intelligence-Based Personalization of Treatment Regimen for Hair Loss: A 6-Month Clinical Trial. *J Drugs Dermatol* 2025. JDD article S1545961625P8611X
15. AI-based Alopecia Assessment Proof-of-Concept. *Skin Health and Disease* 2024. PMC12805230. https://pmc.ncbi.nlm.nih.gov/articles/PMC12805230/
16. Siddiqui H, Rattani A, Kisku DR, Dey T. AI-based BMI Inference from Facial Images: An Application to Weight Monitoring. *arXiv:2010.07442*, 2020.
17. Vasdev A, Rattani A. PatchBMI-Net: Lightweight Facial Patch-based BMI Estimation. *arXiv:2311.18102*, 2023.
18. Digital Scale Team. Digital Scale: Open-Source On-Device BMI Estimation from Smartphone Camera Images. *arXiv:2508.20534*, 2025.
19. Bovsunovskyi YS, et al. Facial appearance and metabolic health biomarkers in women. *Scientific Reports* 10:13067, 2020. PMID:32747662. DOI:10.1038/s41598-020-70119-6

### Stage 3 (자가수집 실험 설계 및 프로토콜)

20. Sebastian K, Tran V, Lee A, Rieder EA, Wang S. Development of SkinTracker, an integrated dermatology mobile app and web portal enabling remote clinical research studies. *Frontiers in Digital Health* 5:1228503, 2023. PMID:37744686. DOI:10.3389/fdgth.2023.1228503
21. Hampton PJ, Ersser SJ, Reilly J, et al. Usability testing of MySkinSelfie: a mobile phone application for skin self-monitoring. *Clinical and Experimental Dermatology* 45(1):73-76, 2020. PMID:31021009. DOI:10.1111/ced.13995
22. Ali Z, Thomsen K, Vestergaard C, et al. Assessment of Quality and Utility of Patient-Taken Smartphone Photographs of Atopic Dermatitis: Clinical Survey Study. *JMIR Dermatology* 9:e72916, 2026. DOI:10.2196/72916
23. Brewster M, Brody J, Lake M, et al. Direct-to-Patient Mobile Teledermoscopy: Prospective Observational Study. *JMIR Dermatology* 7:e52400, 2024. DOI:10.2196/52400
24. Liu X, Jiang Z, Fromm J, Xu X, Patel S, McDuff D. MobilePhys: Personalized Mobile Camera-Based Contactless Physiological Sensing. *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies* 6(1):1-23, 2022. DOI:10.1145/3517225. arXiv:2201.04039
25. ISRCTN19434288. Optimisation of acne treatment via mobile phone app assisted management. http://www.isrctn.com/ISRCTN19434288
26. Hekler EB, Klasnja P, Chevance G, Golaszewski NM, Lewis D, Sim I, Goldberg JS, Stojanovski K. Piloting the Use of Smartphones, Reminders, and Accountability Partners to Promote Skin Self-Examinations in Patients with Total Body Photography: A Randomized Controlled Trial. *Am J Clin Dermatol* 19(5):779-788, 2018. PMID:30062632. DOI:10.1007/s40257-018-0372-7

---

## 부록 A. 기존 _workspace2/_workspace3와의 차별점 요약

| 비교 항목 | _workspace2 (기존 PCOS 카메라) | _workspace3 (기존 얼굴·음성) | 본 보고서 (_workspace5) |
| --- | --- | --- | --- |
| 주체 | 연구자/임상의 측정 | 연구자 측정 | **참여자 본인 자가수집** |
| 환경 | 임상·실험실 위주 | 임상·실험실 위주 | **사용자 가정·일상 환경** |
| 핵심 질문 | PCOS 카메라 바이오마커 일반 | 얼굴/음성 질병 예측 | **사용자 행위·지시사항·프로토콜** |
| 신규 발견 | rPPG, 표현형, 융합 | 32편 face 바이오마커 | **Cao 2025 PCOS 얼굴 morphology, AcneDet 자가촬영 프로토콜, SkinTracker 6개월 종단, MobilePhys 전후면 동시 수집** |
| 연구공백 | rPPG-PCOS 직접 적용 부재 | n/a | **PCOS 다중 표현형 자가수집 통합 앱 부재, 종단 월경주기별 자가데이터셋 부재** |

---

**작성 완료**: 2026-05-13, pcos-endo-camera-reviewer
**다음 단계**: pcos-endo-synthesizer로 주요 발견 + 연구 가설(H1-H5) 전달, IRB 친화적 자가수집 프로토콜 설계로 진행.
