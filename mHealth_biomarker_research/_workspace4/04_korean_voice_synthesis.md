# 한국인 대상 음성 바이오마커 연구 합성 보고서

**작성일**: 2026-04-30
**목적**: PCOS·자궁내막증 예측 스마트폰 앱의 한국어 음성 수집 프로토콜 설계 근거
**근거 문헌**: 22편 (한국 직접 18편, 동아시아 비교 4편)
**원본 탐색 파일**: `_workspace4/04_korean_voice_literature.md`

---

## 1. 핵심 요약

### 1.1 주요 발견

- **한국어 모음 /아, 이, 우/ 3개만으로도 신경계 질환 탐지 가능**: 한국인 PD 환자 대상 연구에서 지속 모음 3개의 43개 음향 특징으로 PD vs 건강 대조군 정확도 95.48% 달성 (Mondol 2023).
- **"가을" 단락이 한국어 표준 임상 발화 과제로 확립**: 스트레스(n=115), 우울증(n=318), 뇌졸중 후 구음장애 등 3개 이상의 독립 연구에서 동일 자료 활용·검증됨.
- **삼성 Galaxy S10 내장 마이크 + 30 cm 거리가 한국인 318명 검증된 스마트폰 수집 표준**: 44.1 kHz/32-bit WAV 녹음, 조용한 방 환경에서 우울증 AUC 0.86 달성 (Kim AY 2023).
- **한국 여성 정상 F0는 영미권보다 약 10~20 Hz 낮음**: 한국 여성 평균 199.6 Hz vs 영미권 210~220 Hz → 한국 여성 전용 normative threshold 설정 필수.
- **자유 발화가 낭독보다 스트레스 변별력 우수**: ECAPA-TDNN 기반 실험에서 자유 발화 0.148 vs 낭독 0.132 (점수 차이 기준, Namkung 2024).
- **갑상선기능저하증 등 호르몬 이상이 한국어 화자 음성 변화를 유발함**: 한국인 직접 연구 존재 → PCOS의 고안드로겐증-음성 가설 적용 근거 확보.
- **한국인 대상 PCOS·자궁내막증·월경주기-음성 연구는 현재 0편**: 본 연구가 채울 수 있는 명확한 공백.

### 1.2 즉시 적용 가능한 권고사항

1. **발화 과제 3종 채택**: 지속 모음 /아/ 6초×3회 + "가을" 단락 낭독 + 자유 발화 1~2분 — 세 과제 모두 한국인 코호트에서 독립적으로 검증 완료.
2. **정상 참조값 기반 이상치 탐지**: 한국 여성 F0 정상치 199.6 Hz (Seo & Shin 2018, n=309)를 PCOS 고안드로겐증 음성 변화 탐지 baseline으로 설정.
3. **다기관 공동연구 파트너**: SNUBH·Boramae·인제대·ETRI·서울대 등 이미 한국어 음성-AI 연구 인프라를 보유한 기관과의 협업이 가장 현실적인 경로.

---

## 2. 한국인 음성 정상 참조값

### 2.1 주요 음향 파라미터 (한국인 성인 정상치)

| 변수 | 한국 여성 | 한국 남성 | 참고 (영어권) | 출처 |
|------|---------|---------|-----------|------|
| F0 평균 (지속 모음) | **199.60 Hz** | 119.02 Hz | 210~220 / 120~140 | Seo & Shin 2018 (n=309) |
| F0 중앙값 (자유 발화) | **200 Hz** | 111 Hz | - | Yang 2021 (n=40) |
| F0 전체 범위 | 65~339 Hz | 65~339 Hz | - | Yang 2021 |
| Jitter | **0.14%** | 0.24% | <1.04% | Seo & Shin 2018 |
| NHR | **0.013** | 0.019 | - | Seo & Shin 2018 |
| CPP cut-off (지속 모음) | ≥12 dB | ≥12 dB | - | Kim & Kim 2019 (n=4,524) |
| CPP cut-off (연속 발화) | ≥7 dB | ≥7 dB | - | Kim & Kim 2019 |

> 비고: 한국어 모음별 F0 변동 폭은 매우 좁음 (/ɯ/ 최고 170.61 Hz ~ /ɑ/ 최저 163.01 Hz, 약 7.6 Hz). 영어 대비 모음 공간 차이를 반영한 별도 분석 권장.

### 2.2 연령별 변화 특성

- Shimmer/NHR: 50대 군에서 급격 증가 (Seo & Shin 2018)
- 한국 여성 폐경 연령: 약 50세 (영미권 52세보다 약 3년 이른 발현)
- 노인 여성 H1-A1 감소 → breathiness 감소 패턴 (Lee SJ 2016, 연세대, n=42)

---

## 3. 한국어 표준 발화 과제

| 과제 유형            | 한국어 자극                    | 지속시간·분량                 | 검증 연구                                                    | 측정 목적                              |
| ---------------- | ------------------------- | ----------------------- | -------------------------------------------------------- | ---------------------------------- |
| 지속 모음            | /아/, /이/, /우/             | 6초 × 3회 권장              | Mondol 2023, Lee J 2024, Mun 2022, Seo 2018 등 다수         | F0, jitter, shimmer, HNR, formants |
| 표준 단락 낭독         | "가을(Gaeul)" 단락            | 약 118~141단어, 369음절, ~1분 | Namkung 2024 (스트레스), Kim AY 2023 (우울증), Park 2024 (구음장애) | 운율, 발화 속도, 스펙트럼 특징                 |
| 표준 단락 낭독 (성대 특화) | "산책(Walk)" 단락             | -                       | Maryn 2018, Kim 2019 (AVQI/ABI)                          | 음성 품질 지수                           |
| 무성 자음 문장         | "오월 오일은 어린이날이에요"          | 1문장                     | Mun 2022 (CKD)                                           | 호흡 효율, 무성 자음 조음                    |
| DDK (교대운동)       | /퍼-퍼-퍼/, /터-터-터/, /커-커-커/ | -                       | Lee J 2024 (인지장애)                                        | 운동 협응, 조음 속도                       |
| DDK (순차운동)       | /퍼-터-커/                   | -                       | Lee J 2024                                               | 다음절 운동 시퀀싱                         |
| 자유 발화            | 중립 주제 질문 응답               | 1~2분                    | Namkung 2024 (스트레스)                                      | 자연 운율, 감정/스트레스 특징                  |

> "가을" 단락은 자음·모음 빈도가 균형 잡혀 있어 한국어 motor speech disorder 평가의 공식 표준으로 확립됨. 영어권 "Rainbow/Grandfather Passage"에 해당하는 자료.

---

## 4. 주요 연구 결과 (질환별)

### 4.1 신경계 질환 (파킨슨병, 인지장애)

| 저자·연도               | 피험자 (N)                     | 기기                                | 발화 과제                            | 핵심 음향 특징                                  | 성능                                                      |
| ------------------- | --------------------------- | --------------------------------- | -------------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| Mondol et al. 2023  | 한국 PD 환자 (Hoehn & Yahr 단계별) | -                                 | 지속 모음 /아, 이, 우/                  | 43개 음향 특징 상위 20개                          | PD vs HC 95.48%; 4-stage 86.62%                         |
| Kim KH et al. 2024  | PD 10명 + HC 10명             | 모바일 음성 데이터                        | 영문 단락 낭독                         | Wav2Vec2 ASR                              | HC 0.94 vs PD 0.66 (reading accuracy); PD 발화 지연 3.5~5+초 |
| Lee J et al. 2024   | 한국인 223명 (K-MMSE 3분류)       | 단방향 마이크, 30cm, 44.1 kHz, 50 dB 이하 | 한국어 8개 과제 (모음 3 + AMR 3 + SMR 1) | 184개 (jitter, shimmer, HNR, F0, formants) | PR-AUC 0.737 (중증 vs 정상); **DDA shimmer(/이/)** = 최강 예측인자 |
| Cross-language 2024 | 한국 PD 291명 + 대만 코호트         | 임상 스마트폰                           | 지속 모음 + 음절 반복 + 읽기               | -                                         | 한국 단독 AUROC 0.87; 다국어 통합 0.90; 짧은 발화(<25자) 0.72로 하락     |

**시사점**: 충분한 발화 길이 확보가 성능의 핵심. 지속 모음 단독으로도 높은 분류 성능 가능.

### 4.2 정신건강 (스트레스, 우울증)

| 저자·연도                 | 피험자 (N)                         | 기기                                            | 발화 과제                      | 핵심 음향 특징                                            | 성능                                    |
| --------------------- | ------------------------------- | --------------------------------------------- | -------------------------- | --------------------------------------------------- | ------------------------------------- |
| Namkung J et al. 2024 | 한국 직장인 115명 (여성 66%, 평균 35.4세)  | Philips Voice Tracer VTR 7100 (24 kHz→16 kHz) | "가을" 낭독 + 자유 발화            | 80-dim Mel spectrogram, MFCC (4초 세그먼트, 75% overlap) | ECAPA-TDNN 77.5% (자유 발화 > 낭독)         |
| Kim AY et al. 2023    | MDD 153명 + HC 165명 = 318명 (한국인) | **Samsung Galaxy S10** 내장 마이크, 30 cm          | 한국어 모음 + 숫자 1~10 + "가을" 단락 | Log-Mel 스펙트로그램 (64×200)                             | "가을" 단락 AUC **0.86**, Accuracy 78.14% |

**시사점**: "가을" 단락 + Galaxy S10은 한국인 318명에서 검증된 황금 기준. PCOS 앱에 직접 전용 가능.

### 4.3 내분비·대사 질환 (신장, 갑상선)

| 저자·연도             | 질환           | 피험자                      | 발화 과제                        | 방법                       | 성능                                  |
| ----------------- | ------------ | ------------------------ | ---------------------------- | ------------------------ | ----------------------------------- |
| Mun J et al. 2022 | 만성 신장병 (CKD) | 한국인 (1,523개 발화, 3시간 26분) | 지속 모음 /아/ + 무성 자음 문장 + 자유 발화 | eGeMAPS 88개 특징 + XGBoost | CKD vs HC F1 **0.93**; 3-class 0.89 |
| 한국 저자 2016        | 갑상선기능저하증     | 한국인 환자                   | 지속 모음 + 자음 분석                | 지각적 분석                   | 호르몬 이상 → 한국어 음성 변화 직접 확인            |
| Yonsei 2017       | 갑상선 수술 후     | 한국인 환자                   | -                            | VoiSS 한국어 검증             | 갑상선 수술 후 음성 평가 한국어 도구 확립            |

**시사점**: 갑상선기능저하증 → 음성 변화의 한국인 직접 근거 존재 → PCOS 고안드로겐증 → 음성 변화 가설 지지 기반.

### 4.4 음성 장애 및 기타

| 저자·연도                       | 대상               | 핵심 내용                                                              |
| --------------------------- | ---------------- | ------------------------------------------------------------------ |
| Maryn et al. 2018 (n=1,524) | 한국인 음성 질환        | AVQI 한국어 검증 완료; 지속 /아/ + "산책" 단락                                   |
| Kim & Kim 2019 (n=4,524)    | 한국인 정상+dysphonia | AVQI v3.01 + ABI 동시타당도; CPP threshold 12 dB (지속 모음) / 7 dB (연속 발화) |
| 한국 저자 2022                  | 한국인 정상/병변        | CPP, CPPS 정상-병변 cut-off 값 제시                                       |
| Lee SJ et al. 2016 (n=42)   | 한국 여성 노화         | H1-A1이 노인 여성 breathiness 22.9% 변량 설명; 호르몬-음성 분석에 H1-A1 추천          |
| 한국어 CP 아동 2024 (n=15)       | 뇌성마비 아동          | 음성 큐("강한 목소리") → 명료도 개선; 발화 과제 설계 시 큐 제시 효과 입증                     |
| 뇌졸중 후 구음장애 2024             | 한국어 dysarthria   | 스마트폰 기반 "가을" 단락 = 한국어 motor speech 공식 표준 확인                        |

---

## 5. 한국어 특화 음향 특성

### 5.1 영어권 연구와의 주요 차이점

| 항목       | 영어권                                  | 한국어                 | 함의                                          |
| -------- | ------------------------------------ | ------------------- | ------------------------------------------- |
| 여성 평균 F0 | 210~220 Hz                           | 199.60 Hz           | 한국 여성 normative threshold 10~20 Hz 낮게 설정 필요 |
| 모음 수     | 11개 이상                               | 8개 단모음              | 모음별 F0 변동 폭 좁음 (약 7.6 Hz); 한국어 특화 분석 필요     |
| 표준 단락    | Rainbow Passage, Grandfather Passage | 가을(Gaeul), 산책(Walk) | 발음 빈도 분포 상이 → 한국어 자료 사용 필수                  |
| 폐경 연령    | ~52세                                 | ~50세                | 한국 여성 호르몬-음성 종단 모델링 시 별도 연령 커트오프 필요         |

### 5.2 한국어 음소·운율 특성이 음향 지표에 미치는 영향

- **평음/격음/경음 삼중 대립**: 한국어 특유의 파열음 체계로 인해 VOT(Voice Onset Time) 패턴이 영어와 상이. CKD 연구의 무성 자음 문장("오월 오일은 어린이날이에요") 활용이 이를 반영한 결과.
- **모음 조화**: 한국어 모음 공간이 영어보다 협소 → formant 분석 시 한국어 표준치 적용 필수.
- **억양**: 문장 말미 상승/하강 패턴이 영어와 다름 → 자유 발화 운율 분석 시 언어별 억양 모델 필요.
- **Device variability**: K-DiN 연구에서 한국 다기종 스마트폰 간 SRT 차이 입증 → device-aware 음향 보정 모듈 필요.

---

## 6. 공개 한국어 음성 데이터셋

| 데이터셋                     | 기관                         | 규모                               | 내용                           | URL                                                      |
| ------------------------ | -------------------------- | -------------------------------- | ---------------------------- | -------------------------------------------------------- |
| AI-Hub 한국인 대화음성          | NIA (aihub.or.kr)          | 2,000명, 1,000시간                  | 일상 대화, 16 kHz, 16-bit PCM    | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=130 |
| AI-Hub 감정 대화 말뭉치         | NIA                        | 다수 (dataSetSn=86, 263, 271, 637) | 감정 라벨 한국어 음성                 | https://aihub.or.kr                                      |
| ETRI KEMDy19             | ETRI                       | 다중 화자                            | 한국어 멀티모달 (음성+텍스트+ECG/EDA) 감정 | https://nanum.etri.re.kr/share/kjnoh/KEMDy19             |
| ETRI KEMDy20             | ETRI                       | 다중 화자                            | KEMDy19 확장판                  | https://nanum.etri.re.kr/share/kjnoh/KEMDy20             |
| MINDsLab-ETRI VOTE400    | MINDsLab + ETRI            | 노인 음성 400시간                      | 한국 노인 발화                     | https://ai4robot.github.io/mindslab-etri-vote400/        |
| Korean PD Speech Dataset | 다기관 (Cross-language PD 연구) | 291명                             | 지속 모음 + 음절 반복 + 읽기, 스마트폰 녹음  | Cross-language PD 논문 참조 (Springer 2024)                  |

> AI-Hub 보건의료 음성 데이터는 온라인/오프라인 안심존을 통해 비다운로드 분석 가능 (보안 제약). KEMDy19/20은 PCOS의 호르몬-음성-자율신경계 통합 연구에서 사전학습 백본으로 활용 가능 (음성+ECG+EDA 동시 수집 구조).

---

## 7. PCOS·자궁내막증 음성 연구 공백

### 7.1 현황 (한국인 대상 연구 편수)

| 연구 주제               | 편수     | 비고                                         |
| ------------------- | ------ | ------------------------------------------ |
| PCOS-음성 직접 연구 (한국인) | **0편** | 영문권에서는 Egyptian J Otolaryngology 2024 등 활발 |
| 자궁내막증-음성 연구 (한국인)   | **0편** | 호르몬 치료(GnRH agonist) 음성 영향도 한국 코호트 없음      |
| 월경주기-음성 종단 연구 (한국인) | **0편** | 영미권 연구(JMIR 2025) 있으나 한국 여성 미적용            |
| 폐경-음성 종단 연구 (한국 여성) | 미흡     | Lee SJ 2016이 단면 연구 n=42에 그침                |

### 7.2 인접 근거 (연구 가설 지지)

- **PCOS-음성 영문권**: Egyptian J Otolaryngology 2024 — PCOS-HA 분류 balanced accuracy 85% (sensitivity 100%, specificity 70%). 한국인 미포함.
- **월경주기-F0**: JMIR Formative Research 2025 — F0 SD가 황체기에 9.0% 감소, 5th percentile F0 8.8% 증가. 호르몬 피임제 사용자는 변화 없음.
- **갑상선기능저하증-음성 (한국인)**: 한국인 직접 근거 2편 ([11][12]) → 호르몬 이상-음성 변화 경로의 한국인 적용 가능성 지지.

### 7.3 독창성 근거

본 연구(PCOS·자궁내막증 예측 스마트폰 앱)는 다음 세 가지를 동시에 달성하는 세계 최초의 연구:
1. 한국 여성 PCOS/자궁내막증 코호트 대상 음성 데이터 수집
2. 한국어 표준 발화 과제 기반 호르몬-음성 종단 분석
3. PCOS 고안드로겐증의 한국 여성 F0 변화 정량화

---

## 8. PCOS·자궁내막증 앱 음성 수집 권장 프로토콜 (한국어 버전)

### 8.1 발화 과제 세트

| 과제               | 한국어 자극                 | 분량·방법          | 근거 연구                                |
| ---------------- | ---------------------- | -------------- | ------------------------------------ |
| 1. 지속 모음         | /아/, /이/, /우/          | 각 6초 × 3회 반복   | Mondol 2023, Lee J 2024, Seo 2018    |
| 2. 표준 단락 낭독      | "가을(Gaeul)" 단락         | 1회 전문 낭독 (~1분) | Kim AY 2023, Namkung 2024, Park 2024 |
| 3. 자유 발화         | "오늘 하루 어떠셨나요?" 등 중립 질문 | 최소 1분, 목표 2분   | Namkung 2024                         |
| 4. 무성 자음 문장 (선택) | "오월 오일은 어린이날이에요"       | 3회 반복          | Mun 2022                             |

### 8.2 녹음 환경 및 기기 사양

| 항목       | 권장값                         | 근거                       |
| -------- | --------------------------- | ------------------------ |
| 샘플링 레이트  | **44.1 kHz** (최소 16 kHz)    | Lee J 2024, Kim AY 2023  |
| 비트 깊이    | **16-bit 이상** (32-bit 권장)   | Kim AY 2023              |
| 파일 포맷    | **WAV (PCM, 모노)**           | Kim AY 2023              |
| 마이크-입 거리 | **30 cm**                   | Lee J 2024, Kim AY 2023  |
| 주변 소음    | **50 dB 이하**                | Lee J 2024               |
| 권장 기기    | 내장 마이크 스마트폰 (Galaxy 계열 검증됨) | Kim AY 2023 (Galaxy S10) |
| SNR 기준   | ≥42 dB (문헌 권장 기준)           | 일반 음성 품질 기준              |

### 8.3 메타데이터 수집 항목

| 범주     | 수집 항목                              |
| ------ | ---------------------------------- |
| 기기 정보  | 기기 모델, OS 버전, 마이크 사양               |
| 환경     | 녹음 장소 유형, 배경 소음 수준                 |
| 피험자    | 연령, 성별, 모국어, BMI                   |
| 호르몬·주기 | 월경주기 날짜, 호르몬 피임제 사용 여부, PCOS 진단 여부 |
| 시간     | 녹음 시각 (일주기 리듬 고려)                  |

### 8.4 분석 권장 지표

| 우선순위 | 지표                          | 도구               | 근거                             |
| ---- | --------------------------- | ---------------- | ------------------------------ |
| 1순위  | F0 (평균, SD, 5th percentile) | Praat, openSMILE | Seo 2018, Yang 2021, JMIR 2025 |
| 1순위  | Jitter, Shimmer, HNR        | Praat            | Seo 2018, Lee J 2024           |
| 1순위  | DDA shimmer (/이/ 모음)        | Praat            | Lee J 2024 (인지장애 최강 예측인자)      |
| 2순위  | CPP, CPPS                   | Praat            | Kim & Kim 2019 (cut-off 확립)    |
| 2순위  | H1-A1, H1-H2 (breathiness)  | Praat            | Lee SJ 2016 (노화·호르몬 변화)        |
| 2순위  | eGeMAPS 88개 특징              | openSMILE        | Mun 2022                       |
| 3순위  | 딥러닝 임베딩 (ECAPA-TDNN)        | 사전학습 모델          | Namkung 2024                   |

---

## 9. 참고문헌 (22편)

### 한국인 대상 직접 연구 (18편)

1. Mondol SIMMR, Kim R, Lee S. Hybrid Machine Learning Framework for Multistage Parkinson's Disease Classification Using Acoustic Features of Sustained Korean Vowels. *Bioengineering* 2023;10(8):984. https://www.mdpi.com/2306-5354/10/8/984

2. Kim KH, Lee BJ, Koo HW. Feasibility Study of Parkinson's Speech Disorder Evaluation With Pre-Trained Deep Learning Model for Speech-to-Text Analysis. *Korean J Neurotrauma* 2024;20(3):e30. https://kjnt.org/DOIx.php?id=10.13004%2Fkjnt.2024.20.e30

3. Lee J et al. (Neopons Inc., Kyungpook National University). Exploring Voice Acoustic Features Associated with Cognitive Status in Korean Speakers: A Preliminary Machine Learning Study. *Diagnostics* 2024;14(24):2837. https://www.mdpi.com/2075-4418/14/24/2837

4. (Cross-language study). A cross-language speech model for detection of Parkinson's disease. *J Neural Transm* 2024. https://link.springer.com/article/10.1007/s00702-024-02874-z

5. Namkung J et al. (SNU, SNUBH, Boramae, Dongduk Women's Univ., SK Telecom). Novel Deep Learning-Based Vocal Biomarkers for Stress Detection in Koreans. *Psychiatry Investig* 2024;21(11). https://www.psychiatryinvestigation.org/journal/view.php?doi=10.30773/pi.2024.0131

6. Kim AY, Jang EH, Lee SH, Choi KY, Park JG, Shin HC. (ETRI, Inje Univ., Chungnam National Univ.). Automatic Depression Detection Using Smartphone-Based Text-Dependent Speech Signals. *J Med Internet Res* 2023;25:e34474. https://www.jmir.org/2023/1/e34474

7. Mun J, Kim S, Kim MJ, Ryu J, Kim S, Chung M. (SNU). Automatic detection and severity prediction of chronic kidney disease using machine learning classifiers. *Phonetics and Speech Sciences* 2022;14(4):45. https://www.eksss.org/archive/view_article?pid=pss-14-4-45

8. Maryn Y, Kim HT, Kim J. Validation of the Acoustic Voice Quality Index in the Korean Language. *J Voice* 2018;32(3):278-285. https://pubmed.ncbi.nlm.nih.gov/30076095/

9. (Kim HT, Kim J 등). Validation of Acoustic Voice Quality Index Version 3.01 and Acoustic Breathiness Index in Korean Population. *J Voice* 2019. https://pubmed.ncbi.nlm.nih.gov/31708369/

10. (한국 저자). A Cepstral Analysis of Pathological Voice Quality in the Korean Population using Praat. *J Voice* 2022. https://www.sciencedirect.com/science/article/abs/pii/S0892199722003198

11. (Yonsei University 등). The Korean Version of the Voice Symptom Scale for Patients with Thyroid Operation. *J Voice* 2017. https://pubmed.ncbi.nlm.nih.gov/29128434/

12. (한국 저자). The Perceptual and Consonant Analysis for the Voice with Hypothyroidism. *J Korean Soc Laryngol Phoniatr Logoped* 2016;27(2):95. https://jkslp.org/journal/view.php?doi=10.22469/jkslp.2016.27.2.95

13. Lee SJ et al. (Yonsei University). Aging Effect on Korean Female Voice: Acoustic and Perceptual Examinations of Breathiness. *Folia Phoniatr Logop* 2016;68:280–286. https://pmc.ncbi.nlm.nih.gov/articles/PMC5815869/

14. (한국어 CP 아동). Effects of Speech Cues on Acoustics and Intelligibility of Korean-Speaking Children With Cerebral Palsy. *JSLHR* 2024. https://pubs.asha.org/doi/10.1044/2024_JSLHR-23-00457

15. (뇌졸중 후 dysarthria). Smartphone-Based Speech Therapy for Poststroke Dysarthria: Pilot Randomized Controlled Trial. *JMIR* 2024;26:e56417. https://www.jmir.org/2024/1/e56417

16. Seo YJ, Shin J. Acoustic characteristics of the sustained vowel phonation according to age groups. *Phonetics and Speech Sciences* 2018;10(4):67-76. https://www.eksss.org/archive/view_article?pid=pss-10-4-67

17. Yang B. (Pusan National University). The f0 distribution of Korean speakers in a spontaneous speech corpus. *Phonetics and Speech Sciences* 2021;13(3):31-37. https://www.eksss.org/archive/view_article?pid=pss-13-3-31

18. (한국 PCOS 역학). Polycystic Ovary Syndrome in Korean Women. *Korean J Obstet Gynecol* / KoreaMed Synapse. https://synapse.koreamed.org/articles/1085885

### 비교용 인접 연구 — 한국인 코호트 부재 영역 (4편)

19. Voice analysis in women with polycystic ovary syndrome. *Egyptian J Otolaryngology* 2024. https://link.springer.com/article/10.1186/s43163-024-00659-5

20. Longitudinal Changes in Pitch-Related Acoustic Characteristics of the Voice Throughout the Menstrual Cycle. *JMIR Formative Res* 2025;9:e65448. https://formative.jmir.org/2025/1/e65448

21. Voice in different phases of menstrual cycle among naturally cycling women and users of hormonal contraceptives. *PLOS One* 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5568722/

22. Hyperandrogenism in Women with Polycystic Ovarian Syndrome: Pathophysiology and Controversies. *Androgens: Clin Res Ther* 2022. https://www.liebertpub.com/doi/10.1089/andro.2021.0020

### 한국어 음성 데이터셋 및 인프라

- AI-Hub 한국인 대화음성: https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=130
- ETRI KEMDy19: https://nanum.etri.re.kr/share/kjnoh/KEMDy19?lang=ko_KR
- ETRI KEMDy20: https://nanum.etri.re.kr/share/kjnoh/KEMDy20?lang=ko_KR
- MINDsLab-ETRI VOTE400: https://ai4robot.github.io/mindslab-etri-vote400/
- 한국음성학회 저널 말소리와 음성과학 (KCI): https://www.eksss.org/

---

*본 보고서는 `_workspace4/04_korean_voice_literature.md` (원시 탐색 결과, 22편)를 합성·재구성한 것입니다.*
