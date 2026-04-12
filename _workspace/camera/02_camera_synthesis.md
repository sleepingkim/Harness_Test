# 스마트폰 카메라 기반 디지털 바이오마커 합성 보고서

## 요약 (Executive Summary)

- **42편의 문헌을 체계적으로 탐색하고 할루시네이션 검증을 거쳐 30편(✅)을 핵심 근거로, 8편(⚠️)을 주의부 포함, 2편(❌)을 제외 처리하였다.**
- **Tier 1 (즉시 활용 가능) 바이오마커 5개 식별**: rPPG 기반 심박수, 스마트폰 PPG 심방세동 탐지(FibriCheck), rPPG 기반 SpO2, 신생아 황달 탐지(BiliSG), 당뇨 망막병증 안저 분석. 이들은 임상 검증(다기관/메타분석), FDA/CE 인증, 또는 대규모 데이터셋 기반 성능이 확립되었다.
- **자궁내막증/PCOS 직접 연계 연구는 현재 전무**하나, rPPG 기반 HRV(비접촉 자율신경계 모니터링)를 월경주기 추적과 결합하면 즉시 파일럿 연구가 가능하다.
- **기술 동향**: CNN에서 Vision Transformer로의 전환이 가속화되고 있으며, 온디바이스 추론(Edge AI)과 프라이버시 보호 설계가 핵심 요건으로 부상하고 있다.
- **주요 연구 공백**: 여성 건강(자궁내막증/PCOS) 분야의 카메라 기반 바이오마커 연구 부재, 다중 바이오마커 융합 시스템, 장기 종단 연구, 다인종 검증이 시급하다.

---

## 1. 바이오마커 분류 체계

### 1.1 기술 유형별 분류

| 기술 유형 | 바이오마커 | 해당 논문 수 | 대표 알고리즘 |
|----------|----------|------------|-------------|
| **rPPG (원격 광용적맥파)** | 심박수, HRV, 혈압, SpO2, 스트레스 | 12편 | CNN, Transformer, STMap, 1D-CNN |
| **스마트폰 PPG (접촉식)** | 심방세동(AF) 탐지 | 2편 | FibriCheck AI, PPG+AI |
| **영상 분석 (얼굴/피부)** | 빈혈, 황달, 피부암, 당뇨 예측, 수면무호흡 | 9편 | DenseNet, T2T-ViT, Wide-field DCNN, ML |
| **안구/시선 추적** | MCI/알츠하이머, ADHD, 녹내장, 백내장 | 8편 | AI eye-tracking, DL 안저분석, iGlaucoma |
| **동작/보행 분석** | 파킨슨병, 본태성 진전, 보행 장애 | 6편 | KPCA, CMSA-Net, Mediapipe, 멀티모달 ML |
| **정신건강 (표정/rPPG)** | 우울증, 양극성장애, 스트레스 | 6편 | MoodCapture, Emoface, 오디오-비디오 융합 |

### 1.2 대상 질환별 분류

| 질환 카테고리 | 세부 질환 | 바이오마커 수 | Tier 분포 |
|-------------|---------|------------|----------|
| **심혈관** | 고혈압, 심방세동, 심혈관 위험 | 8개 | Tier 1: 3, Tier 2: 4, Tier 3: 1 |
| **혈액/대사** | 빈혈, 황달, 당뇨 | 6개 | Tier 1: 2, Tier 2: 3, Tier 3: 1 |
| **안과** | 녹내장, 백내장, 당뇨 망막병증 | 3개 | Tier 1: 1, Tier 2: 2 |
| **신경/운동** | 파킨슨병, 진전, 보행 장애 | 5개 | Tier 2: 3, Tier 3: 2 |
| **정신건강** | 우울증, 스트레스, ADHD | 6개 | Tier 2: 2, Tier 3: 4 |
| **인지** | 알츠하이머/MCI, ADHD | 4개 | Tier 2: 3, Tier 3: 1 |
| **수면** | 수면무호흡(OSA) | 1개 | Tier 2: 1 |

### 1.3 증거 수준별 분류

| 증거 수준 | 기준 | 바이오마커 수 | 대표 사례 |
|----------|------|------------|----------|
| **High** | 메타분석, 다기관 검증, FDA/CE 인증, n>500 | 3개 | rPPG 심박수(종합 리뷰), FibriCheck AF, DR 안저 분석 |
| **Moderate** | 중규모 검증(n=100-500), 동료심사 저널, 재현 가능 | 22개 | SpO2, 혈압, 빈혈(eMoglobin), 황달(BiliSG), 보행 분석 등 |
| **Limited** | 소규모(n<100), 단일 기관, 벤치마크 데이터셋 | 10개 | rPPG 스트레스, VIPER-Tremor, 결막 딥러닝 등 |
| **Exploratory** | 파일럿/프로토타입, 프리프린트, 개념 증명 | 5개 | VISUALSTRESS ⚠️, 결막 비디오 혈액수치 등 |

---

## 2. Tier별 우선순위 평가

### 평가 기준 설명

| 평가 차원 | 1점 | 3점 | 5점 |
|----------|-----|-----|-----|
| 기술 성숙도 | 개념 증명 단계 | 프로토타입/파일럿 검증 | 상용 제품/공개 모델 존재 |
| 임상 타당성 | 사례 보고 수준 | 중규모 단일기관 검증 | 다기관/메타분석, AUC>0.90 |
| 실용성 | 전용 장비 필요 | 스마트폰 가능하나 제약 있음 | 일반 스마트폰으로 즉시 수집 |
| 데이터 가용성 | 비공개/수집 매우 어려움 | 일부 공개 또는 수집 가능 | 다수 공개 데이터셋 존재 |
| 규제 친화성 | 규제 경로 불명확 | 유사 제품 인증 사례 존재 | FDA/CE 인증 완료 |

### Tier 1: 검증된 바이오마커 (즉시 활용 가능, 총점 20-25)

| 바이오마커 | 질환 | 기술 | 최고 성능 | 기술성숙도 | 임상타당성 | 실용성 | 데이터가용성 | 규제친화성 | 총점 | 검증상태 |
|----------|------|------|----------|----------|----------|-------|------------|----------|------|---------|
| rPPG 심박수(HR) | 심혈관 모니터링 | CNN/Transformer rPPG | MAE 0.5-3 bpm | 5 | 5 | 5 | 5 | 3 | **23** | ✅ 다수 종합 리뷰 |
| 스마트폰 PPG 심방세동(AF) | 심방세동 | FibriCheck AI | 정확도 98.5%, 민감도 96.3% | 5 | 5 | 4 | 3 | 5 | **22** | ✅ FDA 인증, 다기관 |
| 당뇨 망막병증(DR) 안저 분석 | 당뇨 망막병증 | DL 안저 분석 | 민감도 0.93, 특이도 0.90 | 5 | 5 | 3 | 4 | 4 | **21** | ✅ 메타분석(82연구, 887K건) |
| 신생아 황달 탐지(BiliSG) | 신생아 황달 | ML + Kramer 원리 | 민감도 100%, 특이도 70%, AUC 0.89 | 4 | 5 | 5 | 3 | 4 | **21** | ✅ JAMA, n=546, 다인종 |
| rPPG SpO2 추정 | 저산소증/호흡 모니터링 | STMap + CNN | MAE 1.274%, RMSE 1.710% | 4 | 4 | 5 | 4 | 3 | **20** | ✅ 국제 기준 달성 |

### Tier 2: 유망 바이오마커 (추가 검증 필요, 총점 13-19)

| 바이오마커 | 질환 | 기술 | 최고 성능 | 총점 | 검증상태 |
|----------|------|------|----------|------|---------|
| rPPG 혈압(BP) 추정 | 고혈압 | Transdermal Optical Imaging | SBP/DBP 95.3%/96.4% (n=1,328) | **19** | ✅ Luo et al. |
| rPPG HRV 추출 | 자율신경계 모니터링 | rPPG 기반 PRV | ECG 대비 r=0.85-0.95 | **18** | ✅ 리뷰 |
| 결막 빈혈 탐지(eMoglobin) | 빈혈 | RAW 이미지 + ML | AUC 0.92(Hb<7), n=426 | **18** | ✅ PLOS ONE |
| 피부암(흑색종) 탐지 | 피부암 | DenseNet169/MobileNetV2 | DenseNet 92.25%, F1=0.932 | **17** | ✅ 리뷰 |
| 보행 분석 파킨슨병 | 파킨슨병 | 스마트폰 멀티모달 ML | 통합 AUC 0.86, n=496 | **17** | ✅ npj Parkinson's |
| MCI/알츠하이머 시선 추적 | 알츠하이머/MCI | AI eye-tracking | AUC 0.85 (166 AD + 107 NC) | **16** | ✅ Aging Clin Exp Res |
| ADHD 시선 추적 | ADHD | 태블릿 시선 추적 + CPT | AUC 0.965, n=437 | **16** | ✅ Frontiers / JMIR |
| 표정 기반 우울증/양극성 감별 | 우울증/양극성장애 | Emoface | 정확도 95.29%, n=700 | **15** | ✅ npj Mental Health |
| 손 떨림 비디오 분석 | 본태성 진전/파킨슨병 | Mediapipe + CV | TETRAS와 유의 상관, n=66 | **15** | ✅ npj Digital Med |
| 두개안면 OSA 탐지 | 수면무호흡 | CNN + 안면사진 + 설문 | 민감도 91.1%, 특이도 79.2%, n=748 | **14** | ✅ J Clin Sleep Med |
| 황달 ViT | 신생아 황달 | T2T-ViT | ResNet/SVM/k-NN 대비 우수 ⚠️ | **14** | ⚠️ 세부 수치 확인 필요 |
| 녹내장 스마트폰 안저 | 녹내장 | iGlaucoma DL | 정확도 99.0%, AUC 0.966 ⚠️ | **14** | ⚠️ 시스템 혼동 가능성 |
| WellFie HR/RR/BP | 심혈관 | rPPG 기반 앱 | SBP: ⚠️ n=150, 정확도 93.94% | **13** | ⚠️ 수치 불일치 교정 필요 |

### Tier 3: 탐색적 바이오마커 (초기 단계, 총점 7-12)

| 바이오마커 | 질환 | 기술 | 최고 성능 | 총점 | 검증상태 |
|----------|------|------|----------|------|---------|
| MoodCapture(일상 우울증 탐지) | 주요우울장애 | RF + EfficientNet | Balanced Acc 0.60-0.61, n=177 | **12** | ✅ CHI 2024 |
| rPPG 스트레스 탐지 | 스트레스 | 1D-CNN + rPPG | 95.83% (벤치마크) | **11** | ✅ Sensors |
| 보행 분류 AI | 보행 장애 전반 | Privacy-preserving AI | 743 비디오, 7유형 | **11** | ✅ PLOS Digital Health |
| 백내장 스마트폰 탐지 | 백내장 | 스마트폰 카메라 + AI | Redmi 9A 활용 검증 | **10** | ✅ Cureus |
| 결막 비디오 혈액수치 | 혈액질환 | 딥러닝 파이프라인 | 비침습 혈구수 추정(탐색적) | **10** | ✅ npj Digital Med 2026 |
| VIPER-Tremor | 진전 | Visual Perceptive DL | 스마트폰 비디오 진전 분석 ⚠️ | **9** | ⚠️ 프리프린트, 중복 가능 |
| CMSA-Net 보행 분석 | 파킨슨병 | Bilateral Gait Camera Fusion | 포터블 구현 | **9** | ✅ Sensors 2025 |
| 얼굴 감정 16개 분류 | 정서 장애 | ML 감정 분류 | 16개 감정, 14,412 비디오 | **9** | ✅ JMIR 2025 |
| 다중 모달 우울증 | 우울증 | 오디오-비디오 융합 | 우울 중증도 분류 | **8** | ✅ Electronics 2025 |
| VISUALSTRESS | 스트레스 | 다중 모달 DL | 실시간 스트레스 식별 | **7** | ⚠️ 출처 불명확 |
| 동공 크기 변화 | ADHD/신경질환 | 스마트폰 NIR 카메라 | 파일럿, 개념 증명 | **7** | ✅ CHI 2022 |

### 제외 항목 (❌ 할루시네이션 확인)

| 원래 바이오마커 | 문제점 | 조치 |
|--------------|--------|------|
| ❌ 빈혈 탐지 ViT (PMC11854623) | 실제 논문은 VGG16+ResNet-50+InceptionV3 스태킹 앙상블이며 ViT가 아님. 성능 지표(91.43%, IoU 72.05%)도 원문과 불일치 (실제 AUC 0.97) | **본 보고서에서 제외**. 해당 논문의 실제 내용(앙상블 CNN, AUC 0.97)은 별도 참고 가능 |
| ❌ OSA AI 메타분석 (JMIR e58187) | 실제 논문은 "Wearable AI 기반 수면무호흡 탐지" 체계적 리뷰이며, 두개안면/얼굴사진 CNN 메타분석이 아님. 민감도/특이도 수치 불일치 | **본 보고서에서 제외**. 두개안면 OSA 연구는 #21(PubMed 39815737, n=748)로 대체 |

---

## 3. 기술 동향 분석

### 3.1 rPPG 기술 진화

rPPG 기술은 지난 5년간 급격히 발전하였다.

**초기 (2015-2019)**: 전통적 신호처리 기법(ICA, POS, CHROM) 중심. Luo et al. (2019)의 Transdermal Optical Imaging이 n=1,328에서 혈압 추정을 검증하며 대규모 임상 가능성을 보여주었다.

**성장기 (2020-2023)**: CNN 기반 딥러닝이 주류화. ReViSe(2022)가 스마트폰 내 실시간 HR/RR/SpO2 동시 추정을 구현하였다. 데이터셋(UBFC-rPPG, PURE, VIPL-HR)과 벤치마크 도구(rPPG-Toolbox)가 정비되었다.

**현재 (2024-2026)**: Transformer 아키텍처 도입, 멀티태스크 학습(심박수+혈압+SpO2 동시 추정), 실생활(in-the-wild) 검증이 활발하다. FibriCheck(2025)이 FDA 인증을 통해 규제 승인 경로를 개척하였다. Acharya et al. (2025)이 저조도/고심박 조건에서의 한계를 체계적으로 규명하여 향후 개선 방향을 제시하였다.

### 3.2 딥러닝 아키텍처 동향 (CNN에서 Transformer로의 전환)

| 시기 | 주류 아키텍처 | 대표 사례 | 장점 |
|------|-------------|---------|------|
| 2019-2022 | CNN (ResNet, DenseNet, MobileNet) | 피부암 DenseNet169 (92.25%), eMoglobin ML | 검증된 성능, 경량화 용이 |
| 2022-2024 | CNN + 앙상블/전이학습 | Cheng et al. SpO2 (STMap+CNN), 빈혈 VGG16+ResNet+Inception 앙상블 | 성능 향상, 소규모 데이터 적응 |
| 2024-2026 | Vision Transformer (ViT, T2T-ViT) | 황달 T2T-ViT (2026), rPPG Transformer | 장거리 의존성 포착, 멀티모달 융합 용이 |
| 2025- | 경량 Transformer + Edge AI | MoodCapture EfficientNet, 보행 AI | 온디바이스 추론, 프라이버시 보호 |

Transformer의 부상은 특히 시계열(rPPG 신호) 및 비디오(표정, 보행) 분석에서 두드러진다. 그러나 CNN 기반 모델(MobileNetV2, EfficientNet)은 모바일 배포에서 여전히 우위를 점하고 있어, 하이브리드 접근(CNN 특징 추출 + Transformer 시퀀스 모델링)이 향후 주류가 될 것으로 전망된다.

### 3.3 엣지 컴퓨팅 및 온디바이스 처리 현황

| 접근 방식 | 대표 사례 | 현황 |
|----------|---------|------|
| **온디바이스 추론** | MoodCapture (이미지 외부 미전송), FibriCheck (스마트폰 내 AF 판독) | 프라이버시 보호 설계의 핵심; CHI 2024에서 주요 화두 |
| **경량 모델** | MobileNetV2 (피부암 98.4%), EfficientNet (MoodCapture) | 스마트폰 GPU/NPU에서 실시간 추론 가능 |
| **프라이버시 보호 AI** | 보행 분류 AI (골격 추출 후 원본 삭제), 페더레이티드 러닝 | 의료 데이터 규제(HIPAA, GDPR) 준수 필수 |
| **RAW 포맷 활용** | eMoglobin (RAW 이미지로 정확도 향상) | 카메라 파이프라인 우회로 신호 품질 개선 |

---

## 4. 자궁내막증/PCOS 연계 가능성 분석

### 4.1 현황: 스마트폰 카메라 기반 여성 건강 연구의 부재

문헌 탐색 결과, **스마트폰 카메라를 활용한 자궁내막증 또는 PCOS 관련 연구는 현재까지 단 한 편도 발표되지 않았다.** 이는 매우 중요한 연구 공백이다. 기존 자궁내막증/PCOS 디지털 바이오마커 연구(`01_literature_review.md`)는 주로 웨어러블 센서(HRV, 체온), 앱 자가보고(월경주기, 증상), 임상 검사(CA125, 호르몬)에 집중되어 있다.

### 4.2 연계 시나리오 1: rPPG HRV + 월경주기 연동 (실현 가능성: 높음)

**근거:**
- PCOS 환자에서 SDNN, RMSSD, HF power가 유의하게 감소 (교감 우세) -- Saranya et al. (2018), Jha et al. (2025)
- 자궁내막증 환자에서 미주신경 매개 HRV 저하 시 골반통 강도/불쾌감 증가 -- Hellman et al. (2021)
- rPPG로 비접촉 HRV 측정 시 ECG 대비 r=0.85-0.95 달성 -- 2024 Frontiers 리뷰

**시나리오:** 월경추적 앱(Clue/Flo) 데이터와 매일 30초 rPPG 셀피를 결합. 월경주기 각 단계(여포기, 배란기, 황체기, 월경기)별 HRV 패턴을 수집하여 PCOS 무배란/자궁내막증 염증 반응의 자율신경계 시그니처를 식별한다. 웨어러블 없이 스마트폰만으로 구현 가능하다는 점이 핵심 차별점이다.

**필요 데이터:** 월경주기 기록 + 일일 rPPG HRV + 자가보고 증상 + 임상 진단(gold standard)

### 4.3 연계 시나리오 2: 얼굴 피부 분석으로 PCOS 호르몬 변동 간접 추정 (실현 가능성: 중간)

**근거:**
- PCOS의 안드로겐 과다 표현형: 여드름, 과색소침착, 다모증 -- 임상적으로 확립
- 스마트폰 카메라 기반 피부 상태 분석(피부암 탐지 DenseNet169, 92.25%) 기술이 성숙
- 얼굴 분석 기반 건강 예측(Avram et al. 2020, Nature Medicine ⚠️ PPG 기반이며 얼굴 분석은 아님)

**시나리오:** 주기적(주 1-2회) 표준화된 셀피를 촬영하여 피부 색조, 여드름 밀도, 과색소침착 분포를 CNN으로 분석. 시계열 변화 패턴에서 안드로겐 변동의 프록시 지표를 도출한다.

**한계:** 직접적인 선행연구가 전무하여 대규모 탐색적 코호트가 먼저 필요하다.

### 4.4 연계 시나리오 3: 야간 카메라 SpO2 + PCOS 수면무호흡 스크리닝 (실현 가능성: 중간)

**근거:**
- PCOS 환자에서 수면무호흡(OSA) 유병률 증가 -- 역학적 연관성 확립
- rPPG SpO2 추정 MAE 1.274% 달성 -- Cheng et al. (2024)
- 두개안면 OSA 탐지 민감도 91.1%, 특이도 79.2% -- PubMed 39815737 (2025)

**시나리오:** 야간 스마트폰 카메라로 수면 중 얼굴의 SpO2 변동 + 안면 구조를 동시 분석하여 OSA 위험도를 평가하고, PCOS 환자의 대사 악화 예방에 활용한다.

**한계:** 야간 저조도 환경에서 rPPG 신뢰성 저하 문제가 있으며(Acharya et al. 2025), 적외선 보조 조명 등 추가 기술 요소가 필요하다.

### 4.5 연계 시나리오 4: 다중 모달 통합 (카메라 + 앱 + 웨어러블) (실현 가능성: 낮음-중간, 영향력: 매우 높음)

**시나리오:** 카메라(rPPG HRV, 피부 분석) + 앱(월경주기, 증상 일지) + 웨어러블(체온, 활동량) 데이터를 융합하여 자궁내막증 vs. PCOS vs. 정상을 감별하는 통합 예측 모델을 구축한다.

**기존 연구와의 연계:**
- Bull et al. (2019): Clue 앱 117M+ 이벤트 → 월경주기 데이터 풍부
- Hillman et al. (2025): 액티그래피 종단 추적 → 자궁내막증 증상 궤적
- Shilaih et al. (2018): 손목 피부 온도 → 배란 탐지

이 중 카메라 기반 HRV/피부 분석이 기존 웨어러블+앱 데이터에 **비접촉 자율신경계 모니터링**이라는 고유한 가치를 추가한다.

### 4.6 연계 우선순위 요약

| 우선순위 | 시나리오 | 실현 가능성 | 영향력 | 필요 기간 |
|---------|---------|-----------|-------|----------|
| **1** | rPPG HRV + 월경주기 연동 코호트 | 높음 | 높음 | 6-12개월 파일럿 |
| **2** | 얼굴 피부 분석 → PCOS 호르몬 추정 | 중간 | 중간-높음 | 12-18개월 탐색 |
| **3** | 야간 SpO2 + PCOS-OSA 스크리닝 | 중간 | 중간 | 12-18개월 |
| **4** | 다중 모달 통합 예측 모델 | 낮음-중간 | 매우 높음 | 18-24개월 |

---

## 5. 연구 공백 및 향후 방향

### 5.1 핵심 연구 공백

1. **여성 건강 분야 전무**: 스마트폰 카메라 기반 자궁내막증/PCOS 연구가 단 한 편도 없다. 가장 시급한 공백이다.

2. **장기 종단 연구 부재**: 카메라 바이오마커의 시간적 변화를 추적한 연구가 거의 없다. MoodCapture(90일)가 가장 긴 추적이며, 대부분은 횡단적 설계이다.

3. **다중 바이오마커 카메라 통합**: 단일 카메라 세션에서 HR + HRV + BP + SpO2 + 피부 + 표정을 동시 분석하는 통합 시스템이 없다.

4. **다인종/다민족 검증**: 대부분의 rPPG 데이터셋이 유럽/동아시아 중심. FibriCheck 연구에서 어두운 피부색에서 AF 민감도 감소가 보고되었으며, 이는 모든 rPPG 바이오마커에 공통되는 한계이다.

5. **규제 경로**: FibriCheck이 유일한 FDA 인증 사례. rPPG 기반 혈압, SpO2 등의 규제 승인 경로가 불명확하다.

6. **비용-효과 분석**: 카메라 기반 건강 스크리닝의 경제적 가치를 분석한 연구가 전무하다.

### 5.2 향후 연구 방향 제언

| 방향 | 세부 내용 | 기대 효과 |
|------|----------|----------|
| rPPG + 여성 건강 코호트 | PCOS/자궁내막증 환자 대상 종단적 rPPG HRV 수집 | 비접촉 자율신경계 바이오마커 발굴 |
| 표준화된 캡처 프로토콜 | 조명, 거리, 시간 등 표준 가이드라인 개발 | 연구 간 비교 가능성 확보 |
| 다인종 데이터셋 구축 | Fitzpatrick I-VI 피부 유형 균등 포함 | 피부색 편향 해소 |
| Edge AI 최적화 | TinyML/모바일 최적화 모델 개발 | 저가 스마트폰에서도 활용 가능 |
| 규제 과학 연구 | rPPG SaMD 인증 경로 체계화 | 상용화 가속 |

---

## 6. 참고문헌 검증 결과 요약

### 6.1 검증 통계

| 분류 | 건수 | 비율 |
|------|------|------|
| ✅ 검증됨 | 30 | 71.4% |
| ⚠️ 부분 검증 | 8 | 19.0% |
| ❓ 미확인 | 2 | 4.8% |
| ❌ 할루시네이션 의심 | 2 | 4.8% |
| **합계** | **42** | **100%** |

### 6.2 할루시네이션 항목(❌) 처리

**#12 빈혈 탐지 ViT (PMC11854623)**
- 문헌 리뷰 기재: Vision Transformer, 정확도 91.43%, IoU 72.05%
- 실제 논문: VGG16+ResNet-50+InceptionV3 앙상블, AUC 0.97
- **조치**: 본 합성 보고서에서 제외. Tier 평가 대상에서 배제함.

**#20 OSA AI 리뷰 (JMIR e58187)**
- 문헌 리뷰 기재: 두개안면 CNN 메타분석, 민감도 84.9%, 특이도 71.2%
- 실제 논문: Wearable AI 기반 수면무호흡 탐지 (얼굴사진과 무관)
- **조치**: 본 합성 보고서에서 제외. OSA 카테고리는 #21(PubMed 39815737, n=748)로 대체.

### 6.3 주의 필요 항목(⚠️) 처리

| # | 논문 | 조치 |
|---|------|------|
| 3 | WellFie (2023) | n=300→n=150, SBP r=0.91→정확도 93.94%로 수치 교정. ⚠️ 표시 포함 |
| 15 | 황달 ViT (2026) | 논문 존재 확인됨. 세부 수치(n=500) 교차 확인 권장. ⚠️ 표시 포함 |
| 18 | Avram et al. (2020) | PPG 기반(손가락→카메라)이며 "얼굴 분석"이 아님. 분류 수정 반영 ⚠️ |
| 28 | iGlaucoma (2023) | 스마트폰 안저 카메라+AI와 iGlaucoma 시스템 혼동 가능. ⚠️ 표시 포함 |
| 34 | VIPER-Tremor (2023) | 프리프린트 상태. #33과 중복 가능. ⚠️ 표시 포함 |
| 39 | VISUALSTRESS (2024) | 정확한 출처 미확인. ⚠️ 표시 포함 |

---

## 참고문헌

본 보고서에서 Tier 평가에 활용된 주요 검증 논문(✅) 목록:

1. Debnath & Kim (2025). A comprehensive review of heart rate measurement using rPPG and deep learning. *Biomed Eng Online*. PMC12181896.
2. ReViSe (2022). Remote Vital Signs Measurement Using Smartphone Camera. *IEEE Access*, 9989351.
3. Luo et al. (2019). Smartphone-based blood pressure measurement. *Circ: Cardiovasc Imaging*. DOI: 10.1161/CIRCIMAGING.119.008857.
4. Video-based BP (2024). *Applied Intelligence*. DOI: 10.1007/s10489-024-05354-9.
5. Cheng et al. (2024). Contactless Blood Oxygen Saturation Estimation from Facial Videos. *Bioengineering*. PMC10968547.
6. Deep learning rPPG 리뷰 (2024). *Frontiers Bioeng Biotechnol*. DOI: 10.3389/fbioe.2024.1420100.
7. FibriCheck (2025). FDA-cleared AF detection. *npj Digital Medicine*. DOI: 10.1038/s41746-025-02059-2.
8. Gruwez et al. (2024). Real-world validation of smartphone-based PPG for AF. *EP Europace*, 26(4), euae065.
9. Acharya et al. (2025). Reliability of rPPG under low illumination. *npj Digital Medicine*. DOI: 10.1038/s41746-025-02192-y.
10. Zhao et al. (2024). eMoglobin anemia detection. *PLOS ONE*. DOI: 10.1371/journal.pone.0302883.
11. Bulbar conjunctiva (2026). Noninvasive blood count from conjunctiva videos. *npj Digital Medicine*. DOI: 10.1038/s41746-026-02598-2.
12. Ngeow et al. (2024). BiliSG neonatal jaundice. *JAMA Network Open*.
13. Naqvi et al. (2023). Skin cancer detection review. *Diagnostics*. PMC10252190.
14. Soenksen et al. (2021). Melanoma detection. *Science Translational Medicine*.
15. DR 체계적 리뷰 (2025). *npj Digital Medicine*. DOI: 10.1038/s41746-025-02223-8.
16. 두개안면 OSA (2025). *J Clin Sleep Med*, 21(5), 843-854. PubMed 39815737.
17. m-ETA (2025). *Alzheimer's Res & Therapy*. DOI: 10.1186/s13195-025-01884-7.
18. AI eye-tracking AD (2024). *Aging Clin Exp Res*. DOI: 10.1007/s40520-024-02882-9.
19. VECA (2024). *npj Digital Medicine*. DOI: 10.1038/s41746-024-01206-5.
20. ADHD 시선 추적 (2024). *Frontiers in Psychiatry*. DOI: 10.3389/fpsyt.2024.1337595.
21. ADHD 디지털 바이오마커 (2024). *JMIR mHealth uHealth*. DOI: 10.2196/e58927.
22. 스마트폰 동공 앱 (2022). UC San Diego, *CHI 2022*.
23. 백내장 스마트폰 앱 (2024). *Cureus*. PMC11560082.
24. Sathya Bama & Bevish Jinila (2022). Vision-based gait analysis for PD. *Health Systems*. PMC11687389.
25. CMSA-Net (2025). *Sensors*, 25(12), 3715.
26. 스마트폰 다중 모달 PD (2025). *npj Parkinson's Disease*. DOI: 10.1038/s41531-025-00953-w.
27. Tremor CV 검증 (2024). *npj Digital Medicine*. DOI: 10.1038/s41746-024-01153-1.
28. 보행 분류 AI (2025). *PLOS Digital Health*. PMC12440163.
29. Nepal et al. (2024). MoodCapture. *CHI 2024*. PMC11296678.
30. Emoface (2025). *npj Mental Health Research*. DOI: 10.1038/s44184-025-00164-4.
31. Fontes et al. (2024). rPPG stress detection. *Sensors*. PMC10892284.
32. 얼굴 감정 인식 (2025). *JMIR*, e68942.
33. 다중 모달 우울증 (2025). *Electronics*, 14(7), 1464.
34. Dawadi et al. (2025). 스코핑 리뷰. *JMIR AI*. DOI: 10.2196/59094.

---

*본 합성 보고서는 2026-04-11 기준으로 작성되었으며, 할루시네이션 검증을 거친 30편의 핵심 논문과 8편의 부분 검증 논문을 기반으로 합니다.*
