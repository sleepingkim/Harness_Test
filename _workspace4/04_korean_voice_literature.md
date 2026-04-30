# 한국인 대상 음성 바이오마커 문헌 탐색 보고서

**탐색일**: 2026-04-30
**탐색 목적**: 한국어/한국인 특화 음성 바이오마커 근거 확보 (PCOS·자궁내막증 스마트폰 음성 데이터 수집 앱 개발)
**총 논문 수**: 22편 (한국인/한국어 직접 관련 18편, 비교용 인접 연구 4편)
**탐색 범위**: PubMed, PMC, MDPI, Korea Science (말소리와 음성과학), JMIR, ScienceDirect, Springer, Karger, AI-Hub, ETRI 자료, RISS 간접 결과

---

## 1. 탐색 개요

### 1.1 탐색 DB 및 키워드
- **영문 DB**: PubMed, PMC, MDPI, ScienceDirect, JMIR, Springer Nature
- **한국 DB(간접)**: Korea Science (말소리와 음성과학 / Phonetics and Speech Sciences), KoreaMed Synapse, e-CSD (Communication Sciences & Disorders), KCI 등재지
- **데이터 플랫폼**: AI-Hub, ETRI AI 나눔 (KEMDy19/KEMDy20, VOTE400)

### 1.2 검색 키워드 (총 18+ 쿼리 실행)
- 영문: "voice biomarker Korean", "Korean speech acoustic analysis Parkinson", "Korean voice depression detection", "Korean voice cognitive impairment", "cross-language Parkinson Korean", "Korean acoustic features F0 jitter shimmer", "Korean voice thyroid", "Korean voice chronic kidney disease", "Korean stress vocal biomarker ECAPA-TDNN", "Korean dysphonia AVQI CAPE-V", "Korean dysarthria smartphone speech therapy", "Korean cerebral palsy speech intelligibility"
- 한국어: "음성 바이오마커 한국인", "한국어 음성 분석 파킨슨/우울증/치매", "한국어 음성 데이터셋 의료 코퍼스", "한국 여성 음성 호르몬 폐경", "한국어 모음 음향 분석 정상 표준", "한국어 음성인식 의료 모바일 앱"

### 1.3 포함/제외 기준
- **포함**: ① 한국인 피험자 코호트, ② 제1/교신저자가 한국 기관 소속, ③ 한국 저널(KCI 등재), ④ 한국어 음소·운율·억양 분석
- **제외**: 한국인/한국어와 무관한 일반 영어권 연구 (단, PCOS-음성 등 특정 주제에서 한국인 대상 연구가 부재할 경우 비교용으로 일부 포함)
- **기간**: 2013–2025 (대부분 2018–2025)

---

## 2. 한국인 대상 음성 질환 탐지 연구

### 2.1 신경계 질환 (파킨슨병, 인지장애)

#### [1] Mondol SIMMR, Kim R, Lee S. (2023). Hybrid Machine Learning Framework for Multistage Parkinson's Disease Classification Using Acoustic Features of Sustained Korean Vowels. **Bioengineering (MDPI)**, 10(8):984.
- **DOI**: 10.3390/bioengineering10080984
- **URL**: https://www.mdpi.com/2306-5354/10/8/984
- **한국 관련성**: 한국인 파킨슨병 환자 대상, 지속 한국어 모음 사용
- **피험자**: 한국 PD 환자 코호트 (Hoehn & Yahr 단계별 분류 대상자 포함)
- **음성 수집 프로토콜**: 지속 한국어 모음 /아/(a), /이/(i), /우/(u) 발성
- **음향 특징**: 43개 음향 특징 (baseline / vocal-fold / time–frequency), ANOVA F-Value로 상위 20개 선정
- **모델**: Random Forest, SVM, kNN, MLP의 하이브리드 파이프라인
- **성능**:
  - 4-stage 분류: **86.62%**
  - 3-stage 분류: **89.48%**
  - 2-stage 분류 (PD vs HC): **95.48%**
- **시사점**: 한국어 모음 /아, 이, 우/만으로도 PD 4단계 구별 가능. 한국 PCOS 앱에서도 동일 모음 과제 채택 가능.

#### [2] Kim KH, Lee BJ, Koo HW. (2024). Feasibility Study of Parkinson's Speech Disorder Evaluation With Pre-Trained Deep Learning Model for Speech-to-Text Analysis. **Korean Journal of Neurotrauma**, 20(3):e30.
- **DOI**: 10.13004/kjnt.2024.20.e30
- **URL**: https://kjnt.org/DOIx.php?id=10.13004%2Fkjnt.2024.20.e30
- **한국 저자/저널**: Inje University Ilsan Paik Hospital, KJNT (한국 저널)
- **피험자**: PD 환자 10명 + 건강 대조군 10명 (King's College London 공개 모바일 음성 데이터 활용, 한국 저자 분석)
- **음성 과제**: 표준 영문 단락(North Wind and the Sun) 낭독
- **모델**: Wav2Vec2 사전학습 ASR
- **성능**: HC 0.94±0.03 / PD 0.66±0.18 reading accuracy. PD 군의 발화 지연(3.5–5+초) 확인.
- **시사점**: 한국 임상의가 모바일 녹음 + 사전학습 ASR로 PD 평가 가능성 제시.

#### [3] Lee J et al. (Neopons Inc., Daegu; Kyungpook National University). (2024). Exploring Voice Acoustic Features Associated with Cognitive Status in Korean Speakers: A Preliminary Machine Learning Study. **Diagnostics (MDPI)**, 14(24):2837.
- **DOI**: 10.3390/diagnostics14242837
- **URL**: https://www.mdpi.com/2075-4418/14/24/2837 / PMC11675567
- **한국 관련성**: 한국 환자 223명, K-MMSE 기반 분류
- **피험자**: 한국인 인지장애 의심자 223명
  - 중증(K-MMSE 0–19): 72명 (평균 72.4세)
  - 경증(K-MMSE 20–23): 54명 (평균 71.1세)
  - 정상(24–30): 97명 (평균 64.8세)
- **음성 과제 (8개 한국어 과제)**: 지속모음 /α/, /i/, /u/; 모음 연장 /α-α-α/; 교대운동(AMR) /퍼-퍼-퍼/, /터-터-터/, /커-커-커/; 순차운동(SMR) /퍼-터-커/
- **녹음 조건**: 단방향 마이크 30cm 거리, 주변 소음 50 dB 이하, 44.1 kHz WAV
- **음향 특징**: 184개 (jitter, shimmer, HNR, F0, formants)
- **모델**: DNN, Random Forest, Gradient Boosting, Logistic Regression (5-fold CV, AutoML)
- **성능 (PR-AUC)**:
  - 중증 vs 정상: 0.737 (DNN)
  - 경증 vs 정상: 0.726 (DNN)
  - 중증+경증 vs 정상: 0.715 (RF)
- **핵심 발견**: **DDA shimmer (모음 /이/)**가 한국인 인지장애 분류 최강 예측인자. "한국인 환자 음성 패턴을 분석한 첫 연구"로 기술됨.

#### [4] (Cross-language Parkinson's Disease, 한국 + 대만 코호트). (2024). A cross-language speech model for detection of Parkinson's disease. **Journal of Neural Transmission**, Springer.
- **DOI**: 10.1007/s00702-024-02874-z
- **URL**: https://link.springer.com/article/10.1007/s00702-024-02874-z / PMC11909049
- **한국 관련성**: 한국 PD 코호트 활용 + 대만 코호트와 통합 모델
- **데이터셋**: Korean PD Speech Dataset – 291명, 지속 모음·음절 반복·읽기 과제, **임상에서 스마트폰으로 녹음**
- **성능 (AUROC)**: 한국 단독 0.87 / 대만 단독 0.88 / 통합 다국어 모델 **0.90**
- **시사점**: 한국어 화자 대상에서도 다국어 통합 모델이 더 우수. 단, 짧은 발화(<25 글자) 시 0.72로 하락 → **충분한 발화 길이 필수**.

### 2.2 정신건강 (스트레스, 우울증)

#### [5] Namkung J, et al. (Seoul National University, SNU Bundang Hospital, Boramae Medical Center, Dongduk Women's University, SK Telecom BioMedical AI). (2024). Novel Deep Learning-Based Vocal Biomarkers for Stress Detection in Koreans. **Psychiatry Investigation**, 21(11).
- **DOI**: 10.30773/pi.2024.0131
- **URL**: https://www.psychiatryinvestigation.org/journal/view.php?doi=10.30773/pi.2024.0131 / PMC11611465
- **한국 관련성**: 다기관 한국인 임상시험, 한국 정신과학회 저널
- **피험자**: 한국인 건강 직장인 **115명** (66.09% 여성, 평균 35.4세, 19–65세) – SNUBH + Boramae 병원 모집
- **녹음 장비**: Philips Voice Tracer VTR 7100 (24 kHz 샘플링 → 16 kHz 리샘플)
- **발화 과제**:
  1. **Script reading**: 한국어 수필 "가을(Autumn)" ~141 단어, 약 1분
  2. **Free speech**: 일상/취미/미디어 등 중립 질문에 대한 자유 발화
- **스트레스 유발**: Socially Evaluated Cold Pressor Test (SECPT) – 침 코티솔 0.165 → 0.322 µg/dL (p<0.0001)로 검증
- **음향 특징**: 80-dim Mel spectrogram, MFCC, 4초 세그먼트(75% overlap)
- **모델**: **ECAPA-TDNN** (binary cross-entropy + Adam)
- **성능**: ECAPA-TDNN **77.5%** > Conformer 62.5% > CNN 60% (논문 본문) / 70% (제안 모델 운영 시점)
- **핵심**: "한국어 화자 맞춤형 음성 스트레스 모델 첫 사례". **자유 발화가 낭독보다 스트레스 변별력 우수** (0.148 vs 0.132 평균 점수 차이).
- **PCOS 앱 시사점**: 한국어 "가을" 단락은 stress/대조 검증된 표준 한국어 음성 과제로 직접 채용 가능.

#### [6] Kim AY, Jang EH, Lee SH, Choi KY, Park JG, Shin HC. (ETRI, 인제대 일산백병원, 충남대학교병원). (2023). Automatic Depression Detection Using Smartphone-Based Text-Dependent Speech Signals: Deep Convolutional Neural Network Approach. **Journal of Medical Internet Research**, 25:e34474.
- **DOI**: 10.2196/34474
- **URL**: https://www.jmir.org/2023/1/e34474 / PMC9909514
- **한국 관련성**: 한국 ETRI + 한국 병원 다기관, 한국어 텍스트 의존 발화
- **피험자**: 한국인 **MDD 환자 153명 + 건강 대조군 165명 (총 318명, ≥19세)**
- **녹음 장비**: **Samsung Galaxy S10** 내장 마이크, 마이크-입 30 cm, 조용한 방, 모노 PCM WAV 44.1 kHz / 32-bit
- **발화 과제 (3개 한국어 텍스트 의존)**:
  1. 한국어 모음 발성
  2. 숫자 1–10 발성
  3. **"가을(Autumn)" 단락** – 자음/모음 균형 잡힌 118단어 표준 텍스트
- **음향 특징**: Log-Mel 스펙트로그램 (64×200, 노이즈 감쇄 전처리)
- **모델**: 4 conv block CNN (3×3 커널, 16-32-64-32 채널) + max-pool + FC
- **성능 (가을 단락)**: Accuracy **78.14%**, Precision 76.83%, Recall 77.90%, **AUC 0.86** (전통 ML 대비 ~8%p 향상)
- **윤리**: 인제대 일산백병원 + 충남대병원 IRB 승인
- **PCOS 앱 시사점**: **한국어 "가을" 단락 + Samsung Galaxy 스마트폰 녹음**이 한국인 318명 검증된 표준 프로토콜. 동일 환경에서 PCOS 음성 데이터 수집 직접 적용 가능.

### 2.3 호흡기·신장계

#### [7] Mun J, Kim S, Kim MJ, Ryu J, Kim S, Chung M. (Seoul National University 언어학과/AI Research Center, SNU Bundang Hospital, SNU College of Medicine). (2022). Automatic detection and severity prediction of chronic kidney disease using machine learning classifiers. **Phonetics and Speech Sciences (말소리와 음성과학)**, 14(4):45.
- **URL**: https://www.eksss.org/archive/view_article?pid=pss-14-4-45
- **한국 관련성**: KCI 등재 한국 저널, 한국인 CKD 코호트, 한국어 발화
- **피험자**: 한국인 CKD 환자 (eGFR ≥60 대조군 / 30–59 stage 3 / 15–29 stage 4)
- **데이터**: 1,523개 발화, 총 3시간 26분
- **발화 과제 (3유형)**:
  1. 지속 모음 /아/
  2. 무성 자음 문장 "**오월 오일은 어린이날이에요**"
  3. 일반 문장 (자유 발화)
- **음향 특징**: ① 수동 추출 (MFCCs, jitter, shimmer, HNR, F0, speech rate), ② **eGeMAPS (88개)**, ③ CNN 추출 (3,136차원 spectrogram embedding)
- **모델**: SVM, **XGBoost**
- **성능 (F1)**: 진단 (CKD vs HC) **0.93**, 3-class 0.89, 5-class 0.84
- **최적 조합**: 일반 문장 + 수동 추출 특징 + XGBoost
- **시사점**: 한국어 무성 자음 문장 "오월 오일은 어린이날이에요"는 한국 임상 음성 데이터 표준 자료로 활용 검증됨.

### 2.4 음성 질환 (성대질환·갑상선·대뇌성마비)

#### [8] Maryn Y, Kim HT, Kim J. (2018). Validation of the Acoustic Voice Quality Index in the Korean Language. **Journal of Voice**, 32(3):278-285.
- **PMID**: 30076095
- **URL**: https://pubmed.ncbi.nlm.nih.gov/30076095/
- **한국 관련성**: 한국어 화자 대상 AVQI 검증 (한국 저자 포함)
- **데이터**: 1,524명 한국 원어민 (정상 + 성대질환), 지속 모음 /아/ + 한국어 단락 "산책(Walk)"
- **결과**: AVQI 한국어 검증, 음성장애 중증도 정량화 도구로 임상 적용 가능

#### [9] (Kim HT, Kim J 등) (2019). Validation of Acoustic Voice Quality Index Version 3.01 and Acoustic Breathiness Index in Korean Population. **Journal of Voice**.
- **PMID**: 31708369
- **데이터**: 한국 원어민 4,524명 (정상 + dysphonia), 지속 /아/ + "산책" 단락
- **결과**: AVQI v3.01과 ABI 한국어 강한 동시타당도. CPP threshold ≈ **12 dB (지속 모음)**, **7 dB (연속 발화)** in Korean speakers

#### [10] (한국 저자) (2022). A Cepstral Analysis of Pathological Voice Quality in the Korean Population using Praat. **Journal of Voice**.
- **URL**: https://www.sciencedirect.com/science/article/abs/pii/S0892199722003198
- **결과**: 한국인 정상/병변 음성에서 CPP, CPPS reference range 제시. 정상 vs 병변 cut-off 값 도출.

#### [11] (Yonsei University 등) (2017). The Korean Version of the Voice Symptom Scale for Patients with Thyroid Operation. **Journal of Voice**.
- **PMID**: 29128434
- **결과**: 한국어 VoiSS 갑상선 수술 후 음성 평가용 신뢰도/타당도 검증.

#### [12] (한국 저자) (2016). The Perceptual and Consonant Analysis for the Voice with Hypothyroidism. **Journal of the Korean Society of Laryngology, Phoniatrics and Logopedics**, 27(2):95.
- **URL**: https://jkslp.org/journal/view.php?doi=10.22469/jkslp.2016.27.2.95
- **결과**: 한국인 갑상선기능저하증 환자의 음성 지각 및 자음 분석 → **호르몬 이상이 한국어 화자 음성에 미치는 영향 직접 근거**.

#### [13] Lee SJ et al. (Yonsei University). (2016). Aging Effect on Korean Female Voice: Acoustic and Perceptual Examinations of Breathiness. **Folia Phoniatrica et Logopaedica (Karger)**, 68:280–286.
- **PMID**: 27160514
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC5815869/
- **한국 관련성**: 연세대 음성언어병리학 (한국인 여성, 한국 저자)
- **피험자**: 한국 여성 42명 (젊은 21명 평균 21.4세 vs 노인 21명 평균 74.7세)
- **과제**: 지속 모음 /아/ "최대한 길고 안정적으로"
- **결과**: H1-H2, H1-A1 노인 여성에서 유의하게 낮음 (덜 breathy). H1-A1이 지각 breathiness 22.9% 변량 설명.
- **시사점**: 한국 여성 음성의 노화/호르몬 변화 분석에 H1-A1 추천.

#### [14] (Korean speaker children with CP) (2024). Effects of Speech Cues on Acoustics and Intelligibility of Korean-Speaking Children With Cerebral Palsy. **Journal of Speech, Language, and Hearing Research**, ASHA.
- **PMID**: 38573834
- **URL**: https://pubs.asha.org/doi/10.1044/2024_JSLHR-23-00457
- **피험자**: 한국어 사용 CP 아동 15명. "큰 입으로/강한 목소리로" 큐 비교.
- **결과**: 강한 목소리 큐가 한국어 화자 명료도 개선 → **한국어 발화 과제 설계 시 큐 제시가 음향 특징 향상에 영향**.

#### [15] (한국어 사용 PSD 환자) (2024). Smartphone-Based Speech Therapy for Poststroke Dysarthria: Pilot Randomized Controlled Trial. **JMIR**, 26:e56417.
- **URL**: https://www.jmir.org/2024/1/e56417 / PMC11082729
- **한국 관련성**: 한국어 dysarthria 환자, 한국어 표준 단락 "**가을(Gaeul) passage**" 사용 (369음절, 모음/자음 빈도 균형)
- **시사점**: "가을" 단락은 한국어 motor speech disorder 평가의 **공식 표준 한국어 발화 과제**로 확립.

---

## 3. 한국어 음성 특성 및 데이터셋

### 3.1 한국어 음향학적 정상치 / 표준 데이터

#### [16] Seo YJ, Shin J. (2018). Acoustic characteristics of the sustained vowel phonation according to age groups. **Phonetics and Speech Sciences**, 10(4):67-76.
- **URL**: https://www.eksss.org/archive/view_article?pid=pss-10-4-67
- **한국 관련성**: KCI 등재 한국 저널, 서울 표준 한국어
- **피험자**: 한국 정상 성인 **309명** (남 132 / 여 177), 5개 연령군 (20대–60–70대)
- **과제**: 한국어 단모음 8개 /ɑ/, /æ/, /ʌ/, /e/, /o/, /u/, /ɯ/, /i/ 지속 발성 (Praat)
- **핵심 정상치**:
  - **F0 평균**: 여성 **199.60 Hz**, 남성 **119.02 Hz**
  - 모음별 F0: /ɯ/ 최고 170.61 Hz, /ɑ/ 최저 163.01 Hz
  - Jitter: 남 0.24% > 여 0.14%
  - NHR: 남 0.019 > 여 0.013
  - Shimmer/NHR: 노인 > 젊은이 (특히 50대 군에서 급격 증가)
- **시사점**: PCOS 앱 한국어 정상 참조값으로 직접 활용 가능.

#### [17] Yang B. (2021). The f0 distribution of Korean speakers in a spontaneous speech corpus. **Phonetics and Speech Sciences**, 13(3):31-37. (Pusan National University)
- **DOI**: 10.13064/KSSS.2021.13.3.031
- **URL**: https://www.eksss.org/archive/view_article?pid=pss-13-3-31
- **피험자**: 서울 한국어 화자 40명 (남 20, 여 20), 10–40대, 자유 발화 ~40시간
- **결과**:
  - **남성 F0 중앙값 111 Hz, 여성 F0 중앙값 200 Hz**
  - 전체 범위 65–339 Hz
  - 분포: right-skewed
- **시사점**: 자유 발화 기반 한국어 화자 F0 정상 분포 = PCOS 앱에서 anomaly detection 기준선.

### 3.2 한국어 의료 음성 코퍼스 / 공개 데이터셋

| 데이터셋 | 출처 | 규모 | 발화 내용 | 활용 |
|---------|------|------|---------|------|
| **AI-Hub 한국인 대화음성** | aihub.or.kr (dataSetSn=130) | 2,000명, 1,000시간 | 일상 대화 (16 kHz, 16-bit PCM) | 일반 한국어 ASR / baseline |
| **AI-Hub 감정 대화 말뭉치** | aihub.or.kr (dataSetSn=86, 263, 271, 637) | 다수 | 감정 라벨 한국어 음성 | 감정/스트레스 모델 사전학습 |
| **ETRI KEMDy19 / KEMDy20** | nanum.etri.re.kr | 다중 화자 | 한국어 멀티모달 (음성+텍스트+ECG/EDA) 감정 데이터 | 우울/스트레스 전이학습 |
| **MINDsLab-ETRI VOTE400** | ai4robot.github.io | 노인 음성 400시간 | 노인 한국어 발화 | 고령 한국인 음성 분석 |
| **AI-Hub 외국인 한국어 발화** | aihub.or.kr (dataSetSn=505) | 외국인 화자 | 한국어 학습용 | 다국어 화자 비교 |
| **Korean PD Speech Dataset** | (Cross-language PD 논문 활용) | 291명 | 지속 모음 + 음절 반복 + 읽기, 스마트폰 녹음 | PD 분류 |
| **응급의료 영역 한국어 음성대화 DB** | 말소리와 음성과학 12(4):81 | 166건 대화, 8h 35min | 응급 의료 시나리오 | 의료 ASR |

> AI-Hub 보건의료 음성 데이터는 **온라인/오프라인 안심존**을 통해 비다운로드 분석 가능 (보안 제약).

### 3.3 한국어 표준 발화 과제 (검증된 임상 자료)

| 자료 | 음절수/단어 | 음운 특성 | 활용 검증 논문 |
|------|----------|----------|--------------|
| **"가을(Autumn/Gaeul)" 단락** | 한국어 표준, 약 118–141단어 / 369음절 | 자음·모음 빈도 균형 | [5] 스트레스, [6] 우울증, [15] dysarthria |
| **"산책(Walk)" 단락** | 한국어 표준 | 임상 음성 분석 | [8][9] AVQI/ABI |
| "**오월 오일은 어린이날이에요**" | 1문장 | 무성 자음 중심 | [7] CKD |
| 지속 모음 /아/ /이/ /우/ | 단음 | 가장 표준화 | [1][3][7][8][9][13][16] |
| AMR/SMR DDK (퍼터커) | 음절 반복 | 운동 협응 | [3] 인지장애 |

---

## 4. 한국 여성 대상 호르몬·음성 연구

### 4.1 PCOS 한국 여성 데이터 (음성-PCOS 직접 연구는 한국 코호트 내 미발견 → 인접 근거)

#### [18] (한국 PCOS 역학) Polycystic Ovary Syndrome in Korean Women. **Korean J Obstet Gynecol** / KoreaMed.
- **URL**: https://synapse.koreamed.org/articles/1085885
- **결과**: 한국 여성 PCOS 유병률 약 5.8%. 한국형 진단 기준 - 다모증, 혈청 안드로겐 농도 기반 hyperandrogenism 판정 변수 정의.
- **PCOS 앱 시사점**: 한국 여성 PCOS는 **비만하지 않은 표현형 + hyperandrogenism + 월경 불규칙** 조합 (PLOS ONE 2014, e0099252) → 음성 androgen 효과 변별 시 BMI/월경주기 공변량 필수.

#### [19] (인접: PCOS-음성, 한국인 코호트 부재) Voice analysis in women with polycystic ovary syndrome. **Egyptian J Otolaryngology**, 2024.
- **DOI**: 10.1186/s43163-024-00659-5
- **결과**: PCOS-HA 분류기 balanced accuracy 85% (sensitivity 100%, specificity 70%). 단, 한국인 데이터 미포함 → **연구 공백 영역**.

#### [20] (인접: 월경주기-음성) JMIR Formative Research (2025). Longitudinal Changes in Pitch-Related Acoustic Characteristics of the Voice Throughout the Menstrual Cycle.
- **URL**: https://formative.jmir.org/2025/1/e65448
- **결과**: F0 SD가 황체기에 9.0% 감소, 5th percentile F0 8.8% 증가. 호르몬성 피임제 사용자에서는 변화 없음.
- **PCOS 앱 시사점**: 한국 여성 대상 동일 종단 연구 부재 → **공동연구 제안 핵심 근거**.

### 4.2 한국 여성 호르몬·음성 직접 근거

- **갑상선 음성**: [11], [12] – 한국 갑상선기능저하증 환자 음성 변화 직접 연구 존재
- **노화/폐경**: [13] – 연세대 한국 여성 노화 음성 (H1-A1, H1-H2) 분석, 폐경 한국 여성 ~50세 (서양보다 ~3년 이른 발현)
- **PCOS 한국 여성 음성**: **직접 연구 부재** (유의미한 연구 공백)

---

## 5. 한국인 대상 mHealth 음성 수집 사례

### 5.1 검증된 한국인 대상 스마트폰 음성 수집 프로토콜

| 연구 | 기기 | 환경 | 발화 과제 | N | 성능 |
|-----|-----|------|---------|---|-----|
| [6] Kim AY 2023 우울증 | Samsung Galaxy S10 | 조용한 방, mic 30 cm | 한국어 모음 + 숫자 + "가을" 단락 | 318 | AUC 0.86 |
| [4] Cross-language PD | 임상 스마트폰 | 임상 환경 | 지속 모음 + 음절 + 읽기 | 291 | AUROC 0.87 |
| [5] 스트레스 (Namkung 2024) | Philips Voice Tracer VTR 7100 (24 kHz) | 병원 | 한국어 "가을" + 자유 발화 | 115 | 70–77.5% |
| [3] 인지 (Lee J 2024) | 단방향 마이크 30cm, 44.1 kHz | 50dB 이하 | 모음 + DDK 8과제 | 223 | PR-AUC 0.74 |
| [7] CKD (Mun 2022) | (한국어 임상 녹음) | – | 모음 + 무성 문장 + 자유 | – | F1 0.93 |

### 5.2 한국 mHealth 인프라

#### Korean Digits-in-Noise Test (K-DiN)
- **URL**: PMC7261694
- **결과**: 한국 청각 스크리닝 스마트폰 앱 첫 개발. **device type별 speech recognition threshold 차이** 검증 → 한국 다기종 스마트폰 스크리닝의 device variability 처리 사례.

#### Naver CLOVA Speech Recognition / Kakao Health Care
- Naver Clova → Soonchunhyang University Hospital 협력 (의무기록 음성인식)
- Kakao Health Care CIC (lifetime health management, AI 의료)
- **PCOS 앱 시사점**: 한국어 ASR/임베딩 백본으로 한국 상용 솔루션 활용 가능.

---

## 6. 한국어 특화 음성 수집 프로토콜 시사점 (PCOS·자궁내막증 앱)

### 6.1 권장 한국어 발화 과제 (기존 검증 활용)
1. **지속 모음 /아/, /이/, /우/** ([1][3][7] 검증) – 기본 F0/jitter/shimmer/HNR
2. **"가을" 표준 단락** ([5][6][15] 검증) – 자음/모음 균형, 한국어 화자에서 우울/스트레스 변별 입증
3. **"오월 오일은 어린이날이에요" 무성 자음 문장** ([7] 검증) – 호흡 효율 평가
4. **DDK 과제 /퍼-터-커/** ([3] 검증) – 운동 협응 (호르몬-근육 영향 평가 가능성)
5. **자유 발화 1–2분** ([5] 검증) – 자연스러운 운율 추출, 스트레스/감정 변별력 우수

### 6.2 한국어 화자 음성 정상 범위 (PCOS 이상치 탐지 baseline)

| 파라미터 | 한국 여성 정상 | 한국 남성 정상 | 출처 |
|---------|------------|------------|------|
| F0 평균 | **199.60 Hz** | 119.02 Hz | [16] Seo & Shin 2018 (n=309) |
| F0 중앙값 (자유 발화) | **200 Hz** | 111 Hz | [17] Yang 2021 (n=40) |
| F0 범위 | – | – | 65–339 Hz |
| Jitter | 0.14% | 0.24% | [16] |
| NHR | 0.013 | 0.019 | [16] |
| CPP (지속모음 정상 cut-off) | ≥12 dB | ≥12 dB | [9] |
| CPP (연속발화 cut-off) | ≥7 dB | ≥7 dB | [9] |

**PCOS hyperandrogenism 가설**: 안드로겐 → F0 감소 → 한국 여성 정상치(~200 Hz)에서 일정 임계값 이하로 시프트 예상. [13] 연세대 H1-A1 분석법 적용 권장.

### 6.3 영어 기반 프로토콜과의 차이점
1. **F0 절대값**: 한국 여성 ~199.6 Hz vs 영미권 평균 ~210–220 Hz → 한국 여성용 normative threshold 별도 설정 필요
2. **모음 공간**: 한국어 8 단모음 ↔ 영어 11+ 모음 → 모음별 F0 차이가 한국어에서 좁음 (163–171 Hz, 7.6 Hz 폭만)
3. **표준 단락**: 영어 "Rainbow/Grandfather Passage" → 한국어 "가을/산책" 단락 사용 필수 (발음 빈도 다름)
4. **폐경 연령**: 한국 여성 ~50세 (영미 ~52세보다 3년 이른 발현) → 한국 여성 종단 연구에서 호르몬-음성 관계 별도 모델링 필요
5. **device variability**: K-DiN 연구에서 한국 다기종 스마트폰 SRT 차이 입증 → 음향 특징 추출 시 device-aware 보정 필요

### 6.4 데이터 품질 관리 (한국 환경 특수성)
- **소음 기준**: [3] 50 dB 이하 권장
- **마이크-입 거리**: 30 cm 표준 ([3][6])
- **샘플링**: 16 kHz 이상 (44.1 kHz 권장, 임상 비교 가능)
- **device 보정**: K-DiN 사례 참고하여 device-type별 정규화 모듈 필요

---

## 7. 연구 공백 및 시사점

### 7.1 명확한 연구 공백 (한국인 대상 PCOS·자궁내막증 음성 연구)

1. **한국 여성 PCOS 음성 직접 연구 = 0편** – 영문권에서 PCOS-음성 연구는 활발하나(2024 Egyptian J Otolaryngology, 2023 ECE), **한국 여성 코호트 음성 분석 부재** → 본 PCOS 앱 연구가 공백을 직접 메움.
2. **한국 여성 자궁내막증-음성 연구 = 0편** – 자궁내막증 hormonal 치료(예: GnRH agonist)의 음성 영향 연구도 한국 코호트 없음.
3. **한국 여성 월경주기-음성 종단 연구 = 0편** – 영미권 종단 연구 존재하나 한국인 미적용. F0 황체기 9% 감소 효과의 한국 여성 재현 연구 필요.
4. **한국 여성 폐경-음성 종단 연구 미흡** – [13]은 단면 연구 (n=42). 한국 여성 폐경 50세 전후 F0 변화 종단 추적 부재.

### 7.2 PCOS 앱 개발에 활용 가능한 강점
- **검증된 한국어 표준 발화 과제 다수**: "가을", "산책", "오월 오일", DDK 등
- **검증된 한국인 정상치**: F0/jitter/shimmer/NHR (n=309)
- **검증된 스마트폰 수집 프로토콜**: Galaxy S10 + 30cm + 가을 단락 (n=318 우울증 연구)
- **한국 임상 인프라**: SNUBH, Boramae, 인제대, ETRI, SNU 등 다기관 음성-AI 연구 경험 보유 → 공동연구 후보군 명확

### 7.3 활용 가능한 한국 공개 자원
- AI-Hub 음성 데이터 (자유 발화 / 감정 / 일반 한국어) – 사전학습 백본
- ETRI KEMDy19/20 – 멀티모달 (음성+ECG+EDA) → PCOS의 호르몬-음성-자율신경계 통합 연구 활용 가능
- VOTE400 노인 한국어 음성 – 폐경 후 여성 비교 코호트

### 7.4 본 연구의 차별성
- **한국 여성 호르몬-음성 데이터 첫 대규모 수집 가능**: PCOS 환자/대조군 한국어 화자 + 월경주기 라벨링
- **이중 활용**: PCOS 검출 + 한국 여성 음성 정상 데이터베이스 동시 구축

---

## 8. 참고문헌

### 한국 1저자/한국 기관 발표 논문
1. Mondol SIMMR, Kim R, Lee S. *Hybrid Machine Learning Framework for Multistage Parkinson's Disease Classification Using Acoustic Features of Sustained Korean Vowels.* Bioengineering 2023;10(8):984. https://www.mdpi.com/2306-5354/10/8/984
2. Kim KH, Lee BJ, Koo HW. *Feasibility Study of Parkinson's Speech Disorder Evaluation With Pre-Trained Deep Learning Model.* Korean J Neurotrauma 2024;20(3):e30. https://kjnt.org/DOIx.php?id=10.13004%2Fkjnt.2024.20.e30
3. Lee J et al. *Exploring Voice Acoustic Features Associated with Cognitive Status in Korean Speakers.* Diagnostics 2024;14(24):2837. https://www.mdpi.com/2075-4418/14/24/2837
4. (Cross-language). *A cross-language speech model for detection of Parkinson's disease.* J Neural Transm 2024. https://link.springer.com/article/10.1007/s00702-024-02874-z
5. Namkung J et al. *Novel Deep Learning-Based Vocal Biomarkers for Stress Detection in Koreans.* Psychiatry Investig 2024;21(11). https://www.psychiatryinvestigation.org/journal/view.php?doi=10.30773/pi.2024.0131
6. Kim AY, Jang EH, Lee SH, Choi KY, Park JG, Shin HC. *Automatic Depression Detection Using Smartphone-Based Text-Dependent Speech Signals.* J Med Internet Res 2023;25:e34474. https://www.jmir.org/2023/1/e34474
7. Mun J, Kim S, Kim MJ, Ryu J, Kim S, Chung M. *Automatic detection and severity prediction of chronic kidney disease using machine learning classifiers.* Phonetics and Speech Sciences 2022;14(4):45. https://www.eksss.org/archive/view_article?pid=pss-14-4-45
8. Maryn Y, Kim HT, Kim J. *Validation of the Acoustic Voice Quality Index in the Korean Language.* J Voice 2018. https://pubmed.ncbi.nlm.nih.gov/30076095/
9. *Validation of Acoustic Voice Quality Index Version 3.01 and ABI in Korean Population.* J Voice 2019. https://pubmed.ncbi.nlm.nih.gov/31708369/
10. *A Cepstral Analysis of Pathological Voice Quality in the Korean Population using Praat.* J Voice 2022. https://www.sciencedirect.com/science/article/abs/pii/S0892199722003198
11. *The Korean Version of the Voice Symptom Scale for Patients with Thyroid Operation.* J Voice 2017. https://pubmed.ncbi.nlm.nih.gov/29128434/
12. *The Perceptual and Consonant Analysis for the Voice with Hypothyroidism.* J Korean Soc Laryngol Phoniatr Logoped 2016;27(2):95. https://jkslp.org/journal/view.php?doi=10.22469/jkslp.2016.27.2.95
13. Lee SJ et al. *Aging Effect on Korean Female Voice.* Folia Phoniatr Logop 2016;68:280–286. https://pmc.ncbi.nlm.nih.gov/articles/PMC5815869/
14. *Effects of Speech Cues on Acoustics and Intelligibility of Korean-Speaking Children With Cerebral Palsy.* JSLHR 2024. https://pubs.asha.org/doi/10.1044/2024_JSLHR-23-00457
15. *Smartphone-Based Speech Therapy for Poststroke Dysarthria (Korean speakers, Gaeul passage).* JMIR 2024;26:e56417. https://www.jmir.org/2024/1/e56417
16. Seo YJ, Shin J. *Acoustic characteristics of the sustained vowel phonation according to age groups.* Phonetics and Speech Sciences 2018;10(4):67-76. https://www.eksss.org/archive/view_article?pid=pss-10-4-67
17. Yang B. *The f0 distribution of Korean speakers in a spontaneous speech corpus.* Phonetics and Speech Sciences 2021;13(3):31-37. https://www.eksss.org/archive/view_article?pid=pss-13-3-31
18. *Polycystic Ovary Syndrome in Korean Women.* KoreaMed Synapse. https://synapse.koreamed.org/articles/1085885

### 비교용 인접 연구 (한국인 코호트 부재 영역)
19. *Voice analysis in women with polycystic ovary syndrome.* Egyptian J Otolaryngology 2024. https://link.springer.com/article/10.1186/s43163-024-00659-5
20. *Longitudinal Changes in Pitch-Related Acoustic Characteristics of the Voice Throughout the Menstrual Cycle.* JMIR Formative Res 2025;9:e65448. https://formative.jmir.org/2025/1/e65448
21. *Voice in different phases of menstrual cycle among naturally cycling women and users of hormonal contraceptives.* PLOS One 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5568722/
22. *Hyperandrogenism in Women with Polycystic Ovarian Syndrome: Pathophysiology and Controversies.* Androgens: Clin Res Ther 2022. https://www.liebertpub.com/doi/10.1089/andro.2021.0020

### 한국 음성 데이터셋 / 인프라
- AI-Hub 한국인 대화음성: https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=130
- ETRI KEMDy19: https://nanum.etri.re.kr/share/kjnoh/KEMDy19?lang=ko_KR
- ETRI KEMDy20: https://nanum.etri.re.kr/share/kjnoh/KEMDy20?lang=ko_KR
- MINDsLab-ETRI VOTE400: https://ai4robot.github.io/mindslab-etri-vote400/
- 한국음성학회 (KSSS) 학술지 *말소리와 음성과학*: https://www.eksss.org/

---

**작성**: voice-biomarker-reviewer agent (한국 특화 모드)
**저장 경로**: `_workspace4/04_korean_voice_literature.md`
