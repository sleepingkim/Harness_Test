# 음성 바이오마커 특징 종류 및 추출 방법론 종합 보고서

**작성일**: 2026-05-06
**작성자**: voice-biomarker-reviewer (특징·추출 방법론 전문 라운드)
**대상 시나리오**: 한국어 PCOS·자궁내막증 예측 스마트폰 음성 바이오마커 수집·분석 파이프라인
**참조 산출물**:
- `_workspace4/04_korean_voice_literature.md` (한국인 음성 바이오마커 22편) → 임상 근거 인용
- `_workspace4/02_ux_synthesis.md` (얼굴·음성 수집 UX 가이드라인) → UX 설계 연계
- 본 보고서 범위: **특징(feature) 종류 + 추출 방법론(signal processing + ML pipeline) + UX 수집 프로토콜** 에 집중

> **할루시네이션 방지 원칙**: 본 보고서의 인용 논문·DOI·정상치 수치는 모두 `04_korean_voice_literature.md`에 검증 수록된 원전 또는 PubMed/PMC/MDPI/KCI 검색으로 확인된 원전에서 가져왔다. 학술적 통념(예: F0 정의, MFCC 계산 절차)은 별도 인용 없이 정리하되, 특정 수치·임상 컷오프·연구 결과는 모두 출처와 함께 표기한다.

---

## 0. Executive Summary — 한 페이지로 보는 음성 특징 체계

### 0.1 4-카테고리 특징 분류 체계

```
[A. 전통 음향 특징]                  [B. 고급 음성 품질 지수]
   │  주파수계: F0(평균/SD/range)        │  AVQI v3.01 (지속모음+연속발화 결합)
   │  음질계: Jitter/Shimmer/HNR/NHR/GNE │  ABI (호흡성 음질)
   │  포르만트: F1-F4 (모음공간)         │  CPP/CPPS (켑스트럼 정점)
   │  켑스트럼: MFCC(13~40), CPP        │  DSI (발성중증도)
   │  스펙트럼: 경사도/LPC/에너지        │  Voice Range Profile (VRP)
   │  운율·시간: 발화속도/Pause/리듬     │
   ▼                                    ▼
   해석가능성 ↑↑↑                       임상 직관성 ↑↑↑
   임상의 친숙도 ↑                      (정성 평가 CAPE-V 연동)

[C. 딥러닝 임베딩 특징]              [D. 발화 과제별 특징]
   │  Wav2Vec2 / XLS-R (768~1024d)      │  지속 모음 (/아/, /이/, /우/) → 음질
   │  HuBERT / WavLM (768~1024d)        │  DDK/AMR/SMR (/퍼터커/) → 신경계
   │  ECAPA-TDNN (192d 화자 임베딩)     │  표준 단락 낭독 ("가을") → 운율·유창성
   │  OpenSMILE: IS09/10/13 / eGeMAPS   │  자유 발화 → 정서·인지·스트레스
   │  x-vector / d-vector              │
   ▼                                    ▼
   대규모 데이터에서 SOTA              임상 해석·재현성 ↑↑↑
   해석가능성 낮음 → SHAP 보완         과제별 특화 정보
```

### 0.2 PCOS·자궁내막증 음성 바이오마커 가설 핵심 메커니즘

| 호르몬 변화 | 성대 조직 영향 | 측정 가능 음성 특징 | 우선순위 |
|----------|------------|----------------|------|
| 안드로겐 ↑ (DHT, T) | 성대 점막 비후, 진동 질량 ↑ | **F0 ↓**, F0 SD ↓ | ★★★ |
| 프로게스테론 변동 | 성대 점막 부종, 탈수 | Shimmer ↑, NHR ↑ | ★★ |
| 에스트로겐 변동 | 점막 습도, 성대 진폭 | HNR ↓, CPP ↓ | ★★ |
| 자율신경 / 통증 / 스트레스 | 후두 긴장, 호흡 변화 | MFCC 분포, 발화속도 ↓, Pause ↑, ECAPA 임베딩 | ★★ |

> **메커니즘 가설**: 고안드로겐증(PCOS)은 성대 근육·점막에 직접 작용해 진동 질량과 강성을 변화시킨다. 음성 바이오마커는 *direct biomechanical proxy* 로서, 자궁내막증의 만성통증·자율신경·우울 동반증상은 *indirect prosodic/emotional proxy* 로서 작동한다.

---

## 1. 음성 특징 분류 체계 (A 카테고리 상세 — 4 부 구조)

### 1.A. 전통 음향 특징 (Traditional Acoustic Features)

#### 1.A.1 기본 주파수 (Fundamental Frequency, F0 / Pitch)

| 파라미터              | 정의              | 측정 방법                                   | 한국인 참조값                                    | 출처                   |
| ----------------- | --------------- | --------------------------------------- | ------------------------------------------ | -------------------- |
| F0 평균 (Hz)        | 성대 진동 평균 주기의 역수 | Praat autocorrelation, RAPT, YIN, CREPE | 여성 **199.60 Hz**, 남성 **119.02 Hz** (지속 모음) | Seo & Shin 2018 [16] |
| F0 중앙값            | 자유 발화 F0 분포 중앙값 | 동일                                      | 여성 200 Hz, 남성 111 Hz                       | Yang 2021 [17]       |
| F0 SD / Range     | 억양 변동성          | F0 트랙의 표준편차/범위                          | 우울증·파킨슨에서 감소                               | (일반)                 |
| Jitter (local, %) | 인접 주기 간 F0 변동   | Praat: pitch period perturbation        | 한국 남 0.24% > 여 0.14%                       | Seo & Shin 2018 [16] |
| F0 SD (semitone)  | 음역 변동성, 옥타브 정규화 | log2 변환                                 | 임상에서 ST 단위 권장                              |                      |
|                   |                 |                                         |                                            |                      |

**측정 알고리즘 비교:**
- **Praat (autocorrelation)**: 표준 임상 도구, 75-500 Hz 범위, time-step 0.01s. 한국 임상 논문 95% 이상이 채택.
- **CREPE (DNN 기반 pitch estimator)**: 잡음 환경에서 우월, 0-500 Hz, GPU 권장. 스마트폰 환경에서 권장.
- **YIN/pYIN (librosa)**: 무료 Python, 실시간 가능.

#### 1.A.2 음질 파라미터 (Voice Quality / Perturbation Measures)

| 파라미터                               | 정의                              | 임상 의미               | 정상 컷오프                                   |
| ---------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| Jitter (local)                     | 주기 길이의 평균 절대 차이 (%)             | 성대 진동 불규칙성          | < 1.04% (Praat 기본)                       |
| Jitter (RAP, PPQ5)                 | 3-period / 5-period 평활화         | 노이즈 강건              |                                          |
| Shimmer (local, %)                 | 주기 진폭의 평균 절대 차이                 | 성대 폐쇄 균일성           | < 3.81%                                  |
| Shimmer (APQ3, APQ5, APQ11, dB)    | 평활화 윈도우 크기별                     | 다단계 진폭 안정성          |                                          |
| **DDA Shimmer (모음 /이/)**           | 3-period 평균 차이의 평균 (Shimmer 계열) | 한국인 인지장애 분류 최강 예측인자 | (논문값) Lee et al. 2024 [3]                |
| HNR (Harmonics-to-Noise Ratio, dB) | 주기 신호 대 잡음 비율                   | 음성 청결도 / 기식성 반대 지표  | > 20 dB (정상)                             |
| NHR (Noise-to-Harmonics Ratio)     | HNR의 역지표                        | 한국 남 0.019, 여 0.013 | Seo & Shin 2018 [16]                     |
| GNE (Glottal-to-Noise Excitation)  | 성문 vs 난류 잡음                     | 기식음성 검출             | > 0.5 (정상)                               |
| CPP (Cepstral Peak Prominence, dB) | 캡스트럼 첫 정점 두드러짐                  | 음성장애 가장 강건한 지표      | 한국 화자: **지속모음 ≈ 12 dB, 연속발화 ≈ 7 dB** [9] |

#### 1.A.3 포르만트 (Formants F1-F4)

| 포르만트              | 해부학적 의미                    | 임상 응용                        |
| ----------------- | -------------------------- | ---------------------------- |
| F1 (300-1000 Hz)  | 입 개방도 (jaw, tongue height) | 모음 분류, 조음 정확도                |
| F2 (850-2500 Hz)  | 혀 전후 위치                    | 모음 공간 면적(VSA), dysarthria 평가 |
| F3 (2000-3500 Hz) | 입술 둥글림, 혀끝                 | /r/, /l/ 변별, 화자 특성           |
| F4 (3000-4500 Hz) | 인두강 공명                     | 음성 품질, 성대 길이 (성호르몬 영향 가능)    |

**파생 지표:**
- **Vowel Space Area (VSA)**: F1-F2 평면에서 코너 모음(/이/, /아/, /우/) 삼각형 면적 → 파킨슨·dysarthria에서 축소.
- **Formant Centralization Ratio (FCR)**: (F2u + F2a + F1i + F1u) / (F2i + F1a). 1.0에 가까울수록 dysarthria.
- **F2 slope (transition)**: 자음→모음 전이 기울기. 신경계 질환 민감.

**추출 도구**: Praat Burg LPC (성인 5 formants 5500 Hz), Wavesurfer, openSMILE. 측정 신뢰도: 모음 안정 구간 30 ms 평균.

#### 1.A.4 켑스트럼 특징 (Cepstral Features)

##### MFCC (Mel-Frequency Cepstral Coefficients)
**계산 절차** (표준 ETSI ES 201 108 기반):
```
1. Pre-emphasis (1 - 0.97 z⁻¹)
2. Frame blocking (25 ms 윈도우, 10 ms hop)
3. Windowing (Hamming)
4. FFT (N=512)
5. Mel filter bank (40 triangular filters, 0-8 kHz)
6. log( |·|² )
7. DCT-II → 첫 13개 계수 (또는 20-40)
8. Δ, Δ² (1차/2차 미분, ±2 frame)
```
- **차원**: 표준 13 / 일반 20 / 정밀 40. Δ+Δ² 결합 시 39/60/120 차원.
- **변형**: PLP (Perceptual Linear Prediction), GFCC (Gammatone), LPCC.
- **한국 논문 사용**: Kim et al. 2023 [6]은 64×200 Log-Mel spectrogram, Mun et al. 2022 [7]은 MFCC + eGeMAPS 결합.

##### CPP / CPPS (Cepstral Peak Prominence / Smoothed)
- 캡스트럼 영역의 첫 ralidization 정점과 회귀선 간 dB 차이.
- AVQI 핵심 구성 요소. **한국어 컷오프 12 dB(지속모음) / 7 dB(연속발화)** 로 검증됨 [9].

#### 1.A.5 스펙트럼 특징 (Spectral Features)

| 특징                             | 정의                  | 응용              |
| ------------------------------ | ------------------- | --------------- |
| Spectral Centroid              | 파워 가중 주파수 평균        | 음색 밝기           |
| Spectral Slope / Tilt          | 회귀 기울기 (예: 1-5 kHz) | 음성 강도, 기식성      |
| Spectral Flux                  | 프레임 간 변화량           | 발화 활동 검출        |
| Spectral Rolloff               | 누적 에너지 85% 점        | 무성음/유성음         |
| LPC (Linear Predictive Coding) | AR(p=10-16) 모델 계수   | 성도 모델링, 포르만트 추정 |
| Energy / RMS                   | 프레임 단위 신호 강도        | 발화량, 강도 변화      |
| ZCR (Zero-Crossing Rate)       | 부호 변화 비율            | 무성/유성 변별        |

#### 1.A.6 운율·시간적 특징 (Prosodic & Temporal Features)

| 특징 | 측정 | 임상 응용 |
|----|------|--------|
| Speech rate (음절/초, syllables-per-second) | 음절 자동 분할 + 시간 | 우울증·파킨슨 ↓ |
| Articulation rate | 무음 제외 발화 시간 기준 | 운동성 평가 |
| Pause duration / ratio | VAD 기반 무음 분할 | 우울증 ↑, 인지장애 ↑ |
| Phonation time ratio | 발화 시간 / 전체 시간 | 호흡 효율 |
| Intonation contour (F0 발화 곡선) | F0 트랙 정규화 후 통계 | 정서·운율 |
| Rhythm metrics (PVI, %V, ΔC, ΔV) | 자모 길이 변동성 | 언어·dysarthria |
| Maximum Phonation Time (MPT) | /아/ 최장 지속 시간 (s) | 호흡·성대 효율 (정상 남>15 s, 여>10 s) |

---

### 1.B. 고급/복합 음성 품질 지수 (Advanced Voice Quality Indices)

#### 1.B.1 AVQI v3.01 (Acoustic Voice Quality Index)
- **정의**: 6개 음향 특징의 가중합으로 *전반적 음성장애 중증도*를 0-10 점수로 표현.
- **구성**: CPPS + HNR + Shimmer local + Shimmer dB + Slope + Tilt
- **공식 (v3.01)**:
  ```
  AVQI = 9.072 - (CPPS × 0.245) - (HNR × 0.161) - (Shimmer local × 0.470)
       + (Shimmer dB × 0.183) - (Slope × 0.111) - (Tilt × 0.110)
  ```
  Reynolds et al. 형식, Maryn 표준화. 한국어 검증: **Maryn, Kim HT, Kim J 2018** [8] (1,524명) + **Kim HT, Kim J 등 2019** [9] (4,524명, AVQI v3.01 + ABI).
- **임상 적용**: 컷오프 ≥ 2.95 또는 3.07 → dysphonia.
- **장점**: 지속모음(3 s) + 연속 발화(읽기) 결합 → 단일 모음 한계 극복.

#### 1.B.2 ABI (Acoustic Breathiness Index)
- **정의**: 9개 음향 파라미터로 *기식성(breathy)* 만 분리 정량화.
- **구성**: CPP smoothed, HNR-D, GNE, shimmer local, shimmer dB, slope, tilt 등.
- **한국어 검증**: Kim HT, Kim J 등 2019 [9].
- **PCOS 시사점**: 호르몬에 따른 점막 변화 → 기식성 → ABI에 민감 가능.

#### 1.B.3 CAPE-V 연동 음향 파라미터
- CAPE-V (Consensus Auditory-Perceptual Evaluation of Voice): 청지각 평가 (Roughness, Breathiness, Strain, Pitch, Loudness, Overall) 0-100 mm VAS.
- 음향 매핑:
  - Roughness ↔ Jitter, Shimmer
  - Breathiness ↔ CPP, GNE, ABI
  - Strain ↔ F0, Spectral tilt
  - Overall severity ↔ AVQI

#### 1.B.4 DSI (Dysphonia Severity Index)
- **공식**: DSI = 0.13 × MPT + 0.0053 × F0_high - 0.26 × I_low - 1.18 × Jitter(%) + 12.4
  - MPT: 최장 발성시간(s), F0_high: 가능한 최고음, I_low: 가능한 최저강도(dB), Jitter: 지속모음 측정.
- **해석**: +5 (정상) → -5 (중증). 다차원 발성 능력 평가.
- **PCOS 시사점**: F0_high·F0 range는 안드로겐 효과(음역 좁아짐) 직접 측정.

#### 1.B.5 Voice Range Profile (VRP) / Phonetogram
- F0 × Intensity 평면에서 사용자가 도달 가능한 영역 매핑.
- 측정: 가장 낮은/높은 F0를 약하게/강하게 발성 → 영역 면적·둘레.
- 임상 도구: KayPENTAX VRP, Voice Studio. 스마트폰 가용.
- **PCOS/호르몬 적용**: 안드로겐 노출 → F0 상한 ↓, VRP 면적 축소 가설.

---

### 1.C. 딥러닝 임베딩 특징 (Deep Learning Features)

#### 1.C.1 Wav2Vec2 / XLS-R
- **모델**: Facebook AI, self-supervised, raw waveform 입력 → 768/1024-d 컨텍스트 임베딩.
- **사전학습**: LibriSpeech 960 h (영어), XLS-R 128 언어 436k h (한국어 포함).
- **의료 적용**: Kim et al. 2024 [2] (한국 PD), Cross-language PD 2024 [4].
- **활용 방식**:
  - **Frozen feature extractor**: 마지막 레이어 평균 풀링 → SVM/MLP.
  - **Fine-tuning**: 도메인 small-data → 학습률 1e-5, freeze 12층, head 학습.
  - **Layer probing**: 어느 층이 어떤 특징(음소·운율·정서) 인코딩하는지 확인.

#### 1.C.2 ECAPA-TDNN
- **구조**: TDNN (Time-Delay NN) + Squeeze-Excitation + Attention Statistics Pooling.
- **출력**: 192-d 화자 임베딩 (또는 256-d).
- **사전학습**: VoxCeleb1+2 화자 인식.
- **한국어 의료 적용**: **Namkung et al. 2024** [5] — 한국인 115명 스트레스 검출 77.5% 정확도, Conformer/CNN 대비 우월.
- **장점**: 짧은 발화(4 s)에도 강건, 화자 특성·정서 분리 가능.

#### 1.C.3 HuBERT / WavLM
- **HuBERT** (Facebook): masked prediction + k-means clustering, 음소·정서 인코딩 강함.
- **WavLM** (Microsoft): HuBERT + denoising + utterance mixing → noisy 환경 강건.
- **의료 활용**: 우울증·치매 감별에 SOTA 보고 (Bayerl et al. 2022, Pérez-Toro et al. 2024 류).

#### 1.C.4 OpenSMILE 대형 특징셋
| 특징셋 | 차원 | 용도 |
|------|----|----|
| **IS09 Emotion** | 384 | INTERSPEECH 2009 paralinguistic challenge baseline |
| **IS10 Paralinguistic** | 1,582 | 정서·연령·성별 |
| **IS13 ComParE** | 6,373 | 가장 광범위, 모든 paralinguistic 과제 표준 |
| **eGeMAPS v2** | 88 | Eyben et al. 2016, 임상 권장 — *최소 표준 특징셋* |
| **GeMAPS** | 62 | eGeMAPS의 축소판 |

- **eGeMAPS 88 차원 구성**: F0 (8) + Loudness (5) + Spectral (24) + Voice quality jitter/shimmer (15) + MFCC 0-4 (12) + 시간(rate/pause) (4) + 등.
- **한국 적용**: **Mun et al. 2022 (CKD)** [7]에서 eGeMAPS 88을 SVM/XGBoost 입력으로 사용.

#### 1.C.5 x-vector / d-vector (화자 임베딩)
- **x-vector** (Snyder 2018): TDNN + statistics pooling, 512-d.
- **d-vector** (Variani 2014): RNN/LSTM 평균.
- **활용**: 스피커 검증, 동일인 추적(longitudinal). PCOS 앱에서 화자 일관성 검증.

---

### 1.D. 발화 과제별 특징 (Task-specific Features)

#### 1.D.1 지속 모음(Sustained Vowel)
- **목적**: 성대 진동 정상상태(steady state) 분리 측정.
- **표준**: /아(a)/, /이(i)/, /우(u)/ 각 3-5 s, 편안한 음높이/강도.
- **추출 가능**: Jitter, Shimmer, HNR, F0 stability, Formants, MPT, CPP.
- **한국 표준**: Seo & Shin 2018 [16] (309명), Lee et al. 2024 [3] (223명, /α/ /i/ /u/), Mondol et al. 2023 [1] (PD).
- **PCOS 권장**: **/이/ 5 s**가 한국인 인지장애 DDA Shimmer 최강 예측자 [3] → 성대 진동 측정 최적.

#### 1.D.2 교대운동속도 (DDK / AMR / SMR)
- **AMR (Alternating Motion Rate)**: /퍼-퍼-퍼/, /터-터-터/, /커-커-커/ 각 5 s 빠르게.
- **SMR (Sequential Motion Rate)**: /퍼-터-커/ 반복.
- **측정 지표**:
  - **DDK rate** (음절/초): 정상 ≥6.0/s
  - DDK regularity (CV%): 안정성
  - VOT (Voice Onset Time): 자음-모음 전이 ms
- **임상 응용**: 파킨슨, ALS, dysarthria, **인지장애 (DDK 감속)**.
- **한국 표준**: Lee et al. 2024 [3]가 8개 한국어 과제 중 AMR/SMR 포함.
- **자동 추출**: Speech Pause Detection + 피크 검출 (librosa onset detection) 또는 wav2vec2 음소 정렬.

#### 1.D.3 표준 단락 낭독 (Reading Task)
**한국어 표준 단락:**

| 단락명 | 음절수 | 특성 | 사용 논문 |
|------|------|----|--------|
| **"가을(Autumn)"** | 369 음절, 141 단어 (변형) | 자음·모음 빈도 균형 | Kim AY 2023 [6] (한국 318명), Namkung 2024 [5] (한국 115명), Smartphone Dysarthria 2024 [15] |
| **"산책(Walk)"** | ~150 단어 | AVQI 표준 | Maryn 2018 [8], 2019 [9] (한국 4,524명) |
| **"오월 오일은 어린이날이에요"** | 무성 자음 풍부 | CKD 검출 | Mun 2022 [7] |

- **추출 가능**: 운율, 발화 속도, 일시 정지 패턴, 유창성, 모음 공간 (단락 내 코너 모음).
- **장점**: 텍스트 내용 통제 → 화자 간 비교 가능. ASR 정렬 후 음소 단위 분석 가능.

#### 1.D.4 자유 발화(Spontaneous Speech)
- **유도 방법**:
  - **Picture description** (예: Cookie Theft Picture): 인지장애 평가 표준.
  - **자유 답변**: "오늘 하루를 말씀해주세요", "취미를 설명해주세요".
  - **TAT 그림**: 정서적 반응 유도.
- **한국 적용**: Namkung 2024 [5]에서 자유 발화가 낭독보다 스트레스 변별력 우수 (0.148 vs 0.132 p<0.05).
- **추출**: 어휘 다양성(TTR), 발화 fluency, MFCC, ECAPA-TDNN 임베딩.
- **주의**: 텍스트 내용 차이 → 정규화 필요 (단어 수, 발화 시간으로 정규화).

---

## 2. 질환별 유효 특징 매핑 표 (Feature × Disease Matrix)

### 2.1 핵심 매트릭스

| 질환                   | F0              | Jitter | Shimmer                   | HNR  | CPP  | Formant/VSA | MFCC       | 발화속도 | Pause | DDK | DL Embed            | 핵심 발화 과제        | 대표 한국 논문                                           |
| -------------------- | --------------- | ------ | ------------------------- | ---- | ---- | ----------- | ---------- | ---- | ----- | --- | ------------------- | --------------- | -------------------------------------------------- |
| **파킨슨병**             | ↓ range         | ↑↑     | ↑↑                        | ↓    | ↓    | VSA↓, FCR↑  | ★          | ↓    | ↑     | ↓↓  | Wav2Vec2 ★★         | 지속모음 + AMR + 낭독 | Mondol 2023 [1], Kim 2024 [2], Cross-lang 2024 [4] |
| **인지장애/치매**          | (변동)            | ↑      | **DDA Shimmer (/이/) ★★★** | ↓    | ↓    | —           | ★          | ↓↓   | ↑↑    | ↓   | HuBERT              | 8과제 종합          | Lee 2024 [3]                                       |
| **우울증**              | ↓ range         | (소폭 ↑) | (소폭 ↑)                    | (변동) | (변동) | —           | ★★         | ↓↓   | ↑↑↑   | —   | CNN, ECAPA          | 낭독("가을") + 자유발화 | Kim AY 2023 [6]                                    |
| **스트레스/불안**          | F0 변동성 ↑        | (변동)   | (변동)                      | (변동) | —    | —           | ★★         | ↑/↓  | (변동)  | —   | **ECAPA-TDNN ★★★**  | 자유 발화           | Namkung 2024 [5]                                   |
| **CKD/대사질환**         | (변동)            | ★      | ★                         | ★    | ★    | —           | ★★         | —    | —     | —   | eGeMAPS+CNN         | 모음/+/오월…/+/자유발화 | Mun 2022 [7]                                       |
| **갑상선저하**            | F0 ↓, monotonic | ↑      | ↑                         | ↓    | ↓    | —           | ★          | ↓    | —     | —   | 지속모음+낭독             | 한국 2016 [12]    |                                                    |
| **dysphonia / 성대질환** | F0 변동           | ★★★    | ★★★                       | ★★★  | ★★★  | —           | ★          | —    | —     | —   | **AVQI/ABI**        | /아/+산책 단락       | Maryn 2018/2019 [8,9]                              |
| **노화 (여성)**          | F0 ↓ (폐경 후)     | ↑      | ↑                         | ↓    | ↓    | —           | —          | (변동) | —     | —   | H1-A1 ↓ (덜 breathy) | 지속모음            | Lee SJ 2016 [13]                                   |
| **PCOS (가설)**        | **F0 ↓ ★★★**    | (?)    | ↑ ?                       | ↓ ?  | ↓ ?  | F2-F3 변화 ?  | —          | —    | —     | —   | eGeMAPS+SHAP        | 지속모음 + 낭독       | (직접 한국 연구 없음, 가설)                                  |
| **자궁내막증 (가설)**       | (직접 효과 약)       | —      | —                         | —    | —    | —           | ★★ (통증·정서) | ↓?   | ↑?    | —   | ECAPA (스트레스 proxy)  | 자유 발화           | (가설)                                               |

> **DDA Shimmer**: Shimmer 계열 중 3-period 평균 차이 측정. `04_korean_voice_literature.md` [3]에서 한국인 인지장애 분류 최강 예측자로 보고.

### 2.2 PCOS·자궁내막증 가설 우선순위 특징 (TOP 10)

| 순위 | 특징 | 측정 과제 | 가설 메커니즘 | 우선순위 근거 |
|----|------|--------|------------|----------|
| 1 | **F0 평균 (지속모음)** | /아/ 5 s | 안드로겐 → 성대 비후 → F0 ↓ | 한국 정상 여성 199.6 Hz 기준선 [16] |
| 2 | **F0 상한 (도약)** | "최대한 높은 음" 발성 | 음역 상한 좁아짐 | DSI 구성 요소 |
| 3 | **F0 SD (semitone, 자유발화)** | 자유 발화 30 s | 단조로움 (depression 동반) | Yang 2021 [17] 분포 비교 |
| 4 | **CPP (지속모음)** | /아/ 3 s | 점막 부종 → 음질 저하 | 한국 cutoff 12 dB [9] |
| 5 | **HNR** | /아/ 3 s | 점막 변화 → 잡음 ↑ | 한국 여 NHR 0.013 [16] |
| 6 | **Shimmer (local)** | /아/, /이/ | 점막 진동 안정성 | 인지장애 DDA shimmer [3] |
| 7 | **AVQI v3.01 통합** | 모음 + "산책" 낭독 | 종합 음성장애 지수 | 한국 4,524명 검증 [9] |
| 8 | **Formant F1·F2 (모음 공간)** | /아/ /이/ /우/ | 성대 길이 변화 → 공명 변화 | 가설 |
| 9 | **eGeMAPS 88 + SHAP** | 모음 + 낭독 + 자유발화 | 다차원 통계 | Mun CKD [7] |
| 10 | **ECAPA-TDNN 임베딩** | 자유 발화 30 s | 스트레스·통증 동반 | Namkung 스트레스 [5] |

---

## 3. 추출 파이프라인 (Signal Processing + ML Pipeline)

### 3.1 5-Stage 표준 파이프라인

```
[Stage 1: 신호 획득]
   스마트폰 마이크 → WAV 16 kHz·16-bit (또는 44.1 kHz)
   ↓
[Stage 2: 전처리]
   ① Resampling 16 kHz
   ② Pre-emphasis (1 - 0.97 z⁻¹)
   ③ DC offset 제거
   ④ Loudness normalization (LUFS -23) — 단, jitter/shimmer는 미정규 원본에서 측정
   ⑤ Noise suppression: RNNoise / SpeechBrain SepFormer / Spectral subtraction (선택적)
   ⑥ VAD: WebRTC VAD / Silero VAD / pyannote
   ⑦ Segmentation: 4 s 윈도우 (75% overlap, Namkung 방식 [5]) 또는 발화 단위
   ↓
[Stage 3: 특징 추출] — 4 트랙 병렬
   Track A: Praat Parselmouth → F0/Jitter/Shimmer/HNR/Formants/CPP
   Track B: openSMILE eGeMAPS-v02 (88-d) / IS13 ComParE (6373-d)
   Track C: librosa → MFCC(40)+Δ+Δ², Mel-spec(128×T), Chroma, Spectral
   Track D: 사전학습 임베딩 (Wav2Vec2 / HuBERT / ECAPA-TDNN)
   ↓
[Stage 4: 특징 선택 / 차원 축소]
   ① Univariate: ANOVA F-value, mutual information
   ② Embedded: L1-Lasso, Tree feature importance
   ③ Wrapper: mRMR, Sequential Feature Selection
   ④ 차원 축소: PCA, t-SNE (시각화), UMAP
   ⑤ 해석: SHAP (TreeExplainer / KernelExplainer / DeepExplainer)
   ↓
[Stage 5: 모델링 + 검증]
   Classical: SVM (RBF), RF, XGBoost, LightGBM, Logistic Regression
   Deep: CNN (Mel-spec), LSTM/GRU, Transformer, ECAPA-TDNN, Conformer
   Transfer: Wav2Vec2 finetune, HuBERT linear probing
   검증: 화자독립 분할 (subject-wise CV), 5-fold / LOSO, 외부 검증 코호트
   평가: Accuracy, F1, AUC, Sensitivity/Specificity, EER, Brier
```

### 3.2 단계별 도구 카탈로그

| Stage | 도구 / 라이브러리 | 라이선스 | 특징 |
|------|---------------|------|----|
| 전처리 | **WebRTC VAD** | BSD | 가볍고 빠름, 모바일 |
| | **Silero VAD** | MIT | DNN 기반, 강건 |
| | pyannote.audio | MIT | speaker diarization 통합 |
| | RNNoise | BSD | 실시간 잡음 제거 |
| | torchaudio | BSD | PyTorch 통합 |
| 음향 특징 | **Praat / Parselmouth** | GPL/MIT | 임상 표준, F0/Jitter/Shimmer/HNR |
| | **openSMILE 3.x** | GPL/상업 | eGeMAPS, IS13, 전통 표준 |
| | **librosa** | ISC | MFCC, Mel-spec, beat, chroma |
| | **Surfboard** | Apache 2 | 의료 음성 특징 통합 |
| | DisVoice | MIT | 파킨슨·dysarthria 특화 |
| 임베딩 | **SpeechBrain** | Apache 2 | ECAPA-TDNN, x-vector pretrained |
| | **Hugging Face transformers** | Apache 2 | Wav2Vec2, HuBERT, WavLM |
| | NeMo (NVIDIA) | Apache 2 | TitaNet, Conformer-CTC |
| | pyAudioAnalysis | Apache 2 | 통합 분석 |
| 모델링 | scikit-learn, XGBoost, LightGBM | BSD/Apache | 전통 ML |
| | PyTorch, PyTorch Lightning | BSD/Apache | DL 프레임워크 |
| | TensorFlow / Keras | Apache | DL |
| | AutoML: H2O AutoML, AutoGluon | — | Lee 2024 [3]에서 사용 |
| 해석 | **SHAP** | MIT | 모델 무관 해석 |
| | LIME | BSD | local 설명 |
| | Captum (PyTorch) | BSD | DL 어트리뷰션 |
| 라벨·정렬 | Montreal Forced Aligner (MFA) | MIT | 음소 단위 정렬 |
| | Whisper / Whisper-X | MIT | ASR + 정렬 |

### 3.3 모델 아키텍처별 권장 입력

| 모델 | 권장 입력 | 차원 | 학습 전략 |
|----|--------|----|--------|
| **SVM (RBF)** | eGeMAPS 88 / Praat 50 | 50-200 | StandardScaler + GridSearch (C, γ) |
| **XGBoost** | 핸드크래프트 + eGeMAPS 결합 | 100-500 | early stopping, max_depth 3-7 |
| **CNN 2D** | Mel-spectrogram 64-128 × T | 64×200 (Kim 2023 [6]) | Adam 1e-3, BatchNorm, Dropout 0.3 |
| **LSTM/BiLSTM** | MFCC 40-d × T | 40×T | masking, Adam 1e-3 |
| **ECAPA-TDNN** | Raw waveform / Mel | 16k Hz / 80-mel | AAM-Softmax loss, BCE |
| **Wav2Vec2 (frozen)** | Raw 16 kHz | → 768-d | mean pool + MLP head |
| **Wav2Vec2 (finetune)** | Raw 16 kHz | → task | LR 1e-5, freeze 8-12 layers, layer-wise LR decay |
| **HuBERT (probing)** | Raw 16 kHz | → 1024-d | SUPERB 프로토콜 |

### 3.4 평가 프로토콜 — 의료 음성 분류 표준

1. **Subject-independent split** (필수): 동일 화자 train/test 동시 등장 금지. → Speaker-disjoint k-fold.
2. **k-fold CV**: 5-fold / 10-fold / **LOSO (Leave-One-Subject-Out)** for 소표본.
3. **Stratified sampling**: 클래스 + 인구통계(성·연령) 균형.
4. **External validation**: 다른 기관·다른 마이크 코호트에서 재현.
5. **Reporting**: Accuracy + Macro-F1 + AUC + Sensitivity/Specificity + 95% CI (bootstrap 1000).
6. **TRIPOD-AI** 가이드라인 준수: model 발표 시 데이터, 전처리, 특징, 학습, 검증 모두 보고.

---

## 4. UX 수집 프로토콜 (스마트폰 기반)

> 본 절은 `_workspace4/02_ux_synthesis.md` 의 UX 가이드라인과 정합한다. 본 절의 초점은 **신호 품질을 보장하는 음성 데이터 수집 UX** 이다.

### 4.1 발화 과제 마스터 프로토콜 (3-Track, 약 3.5분)

| Track           | 과제                                    | 시간     | 추출 특징                                        | 임상 근거                                             |
| --------------- | ------------------------------------- | ------ | -------------------------------------------- | ------------------------------------------------- |
| **A. 지속 모음**    | /아/ 5 s × 3, /이/ 5 s × 3, /우/ 5 s × 3 | 90 s   | F0, Jitter, Shimmer, HNR, CPP, Formants, MPT | Lee 2024 [3], Maryn 2018/2019 [8,9]               |
| **B. 표준 낭독**    | "가을" 단락 (369 음절) 1회                   | 약 60 s | 운율, 속도, pause, MFCC, AVQI                    | Kim AY 2023 [6], Namkung 2024 [5], JMIR 2024 [15] |
| **C. 자유 발화**    | 중립 질문 ("오늘 어떻게 지내셨어요?") 30 s          | 30 s   | 정서·스트레스 임베딩 (ECAPA), 어휘 다양성                  | Namkung 2024 [5]                                  |
| (선택) D. AMR/SMR | /퍼퍼퍼/, /터터터/, /커커커/ 각 5 s + /퍼터커/     | 30 s   | DDK rate, regularity                         | Lee 2024 [3]                                      |

총 시간: 3.5분 (선택 포함 4분).

### 4.2 캡처 시점 품질 게이트 (Capture-time Quality Gate)

```
[녹음 시작 전 사전 점검 — 5 s 캘리브레이션]
   ① 환경 SNR 측정: 첫 2 s 무음 측정 → 노이즈 floor < -50 dBFS 통과
   ② 마이크 거리 검출: 첫 발성 RMS → 적정 영역 (-30 ~ -15 dBFS)
   ③ 클리핑 사전 경고: peak > -3 dBFS 시 "조금 멀리" 알림
   ④ 환경 클래스 분류 (선택): YAMNet 임베딩 → "조용함/시끄러움/음악 있음"
   ↓
[녹음 중 실시간 모니터링]
   ⑤ Live VAD: 발화 시작 자동 감지 (0.3 s 무음 감지 후 종료)
   ⑥ Live SNR HUD: 상단 게이지 색상 코드 (녹/노/빨)
   ⑦ Pitch 안정성 (지속 모음): F0 SD > 5 ST → "더 일정하게"
   ⑧ 클리핑 즉시 경고: -1 dBFS 도달 시 화면 빨강 + 햅틱
   ↓
[녹음 후 자동 검증]
   ⑨ Re-take 트리거: SNR < 20 dB OR 길이 < 목표 80% OR 클리핑 비율 > 1%
   ⑩ Pass 판정: 4-게이트(SNR/길이/클리핑/F0 안정) 통과 시 다음 과제
```

### 4.3 녹음 포맷·하드웨어 권장 사양

| 항목 | 권장 (필수) | 허용 (대체) | 비권장 |
|----|---------|----------|----|
| 샘플링율 | **16 kHz** (음성 분석 표준) | 22.05 kHz, 44.1 kHz, 48 kHz | < 16 kHz |
| 비트 심도 | **16-bit PCM** | 24-bit PCM | 8-bit |
| 채널 | **mono** | (스테레오 → mono 다운믹스) | 스테레오 그대로 |
| 포맷 | **WAV (LPCM 비압축)** | FLAC | **MP3/AAC/Opus 압축 (jitter/shimmer 왜곡)** |
| 마이크 | 스마트폰 내장 또는 유선 헤드셋 | 고급 USB 콘덴서 | 블루투스 (지연·압축) |
| 거리 | 입에서 **15-30 cm** | 30-50 cm | < 5 cm (popping), > 50 cm (S/N ↓) |
| 환경 노이즈 | < 50 dB(A) | < 60 dB(A) | > 65 dB(A) |
| 프리앰프 | 자동 게인 OFF | — | AGC ON (Jitter/Shimmer 왜곡) |
| 가속 매끄럽게 | iOS: AVAudioSession `.measurement` mode | Android: `MediaRecorder.AudioSource.UNPROCESSED` | 보이스 인핸스먼트 ON |

> **중요**: 안드로이드 표준 `MIC` 소스는 자동 게인·노이즈 억제·에코 제거가 활성화되어 jitter/shimmer가 왜곡된다. 의료급 분석은 반드시 **`UNPROCESSED`** 또는 iOS `measurement` 모드 사용.

### 4.4 기기 간 정규화 (Cross-device Calibration)

| 문제 | 영향 | 대응 |
|----|----|----|
| 마이크 주파수 응답 차이 | F0·formant 시프트 | 기기 모델별 보정 테이블 + 화이트노이즈 캘리브레이션 |
| 마이크 위치(상하단) 차이 | SPL 5-10 dB 변동 | 화면 안내로 "마이크 위치를 입 쪽으로" |
| OS 오디오 처리 | jitter/shimmer 왜곡 | `UNPROCESSED` / `.measurement` 강제 |
| 거리 변동 | RMS 변동 | 자동 거리 추정 (얼굴-카메라 거리) + 가이드 |
| 다중 화자 등록 | 화자 동일성 | x-vector / ECAPA로 등록 시점 임베딩 저장, 매 회 cosine sim 검증 |

### 4.5 종단 수집 — EMA 프로토콜

`02_ux_synthesis.md` 7번째 원칙(부담 적응형 EMA) 준용.

| 항목 | 권장 |
|----|----|
| 빈도 | 1일 1-2회 (월경주기 추적 위해 매일 또는 격일) |
| 시점 | 기상 후 60분 이내 (호르몬/정서 baseline 안정) |
| 회수 동기화 | 기초 체온, 월경 단계, 수면 자가보고와 동시 수집 |
| 부담 적응 | 부정 정서 점수 > threshold → 자유 발화 생략 (지속 모음만) |
| 휴지일 | 주 1회 휴지 권장 (피로 누적 방지) |
| 알림 | 지능형 시간 슬롯 (사용자 활동 패턴 학습) |
| 데이터 보존 | 로컬 → 매일 0시 클라우드 동기화, 사용자 30일 회수 가능 |

---

## 5. PCOS·자궁내막증 특화 음성 특징 가설 (메커니즘 기반)

### 5.1 PCOS 음성 변화 메커니즘 가설

**1차 직접 효과 (Biomechanical Direct):**
```
고안드로겐증 (testosterone, DHT ↑)
        ↓ androgen receptor (성대 점막·근육)
   ┌────┴────┬─────────────┐
   ↓         ↓             ↓
성대 점막   thyroarytenoid  vocalis muscle
점성↑        근비후         hypertrophy
   ↓         ↓             ↓
진동 질량 ↑  cycle period ↑ stiffness ↑
        ↓
   ────────────────────────
   F0 ↓ (가장 강한 신호)
   F0 상한 ↓ (음역 좁아짐)
   Shimmer ↑ (점막 진동 비균질)
   HNR ↓, CPP ↓ (잡음 성분 ↑)
```

**2차 간접 효과 (Indirect):**
- 인슐린 저항 / 비만 → 호흡근 변화 → MPT 단축, 호흡 효율 ↓
- 정서 (PCOS-우울 동반) → 운율, 발화 속도 변화

### 5.2 자궁내막증 음성 변화 메커니즘 가설

**자궁내막증은 직접 호르몬 효과가 약하나, 다음 경로로 음성에 영향:**

| 경로 | 임상 특징 | 음성 변화 가설 | 측정 권장 |
|----|--------|------------|--------|
| 만성 골반통 | 24시간 통증 | 자율신경 변동 → F0 SD 변동, 발화 속도 변동 | F0 통계 + 발화 속도 |
| 우울·불안 동반 (50-70%) | depression score ↑ | 운율 단조, pause ↑ | "가을" 단락 + 자유 발화 |
| 만성 피로 | fatigue VAS ↑ | 음성 강도 ↓, 발화 속도 ↓, MPT ↓ | RMS, 속도, MPT |
| 수면 장애 | PSQI ↑ | 발화 fluency ↓, MFCC 분포 변화 | MFCC + ECAPA |
| 호르몬 치료 (GnRH agonist 등) | 약리적 폐경 상태 | 폐경 후 여성 음성 변화와 유사 → F0 변동, breathiness ↑/↓ | AVQI, ABI |

### 5.3 PCOS·자궁내막증 검출 권장 음향 특징셋 (V1)

```
[Tier 1: 핵심 (필수)] — 12 features
F0_mean (모음 /아/), F0_mean (자유발화), F0_max (도약 발성)
F0_SD (semitone, 자유발화), F0_range
Jitter_local (모음 /아/), Shimmer_local (모음 /이/), HNR (모음 /아/)
CPP (모음 /아/), CPP (낭독)
AVQI v3.01 (모음+낭독)
MPT (모음 /아/ 최장)

[Tier 2: 확장 (권장)] — eGeMAPS 88 + 시간특징 12
eGeMAPS-v02 88
Speech_rate, Articulation_rate, Pause_ratio, Long_pause_count
Vowel_Space_Area (F1-F2 of /a/i/u/), F2_slope
Loudness_mean, Loudness_SD
H1-A1 (Lee SJ 2016 [13] 한국 여성 노화/호르몬 마커)

[Tier 3: 임베딩 (탐색적)] — 1,152-d 통합
ECAPA-TDNN 192-d (낭독)
ECAPA-TDNN 192-d (자유발화)
Wav2Vec2 layer-9 mean 768-d (낭독)
```

총: Tier1 12 + Tier2 100 + Tier3 1,152 = 약 1,264-d. SHAP 기반 특징 선택으로 최종 50-100-d 권장.

### 5.4 검증 우선순위 가설 (실험 설계)

| 가설 H# | 가설 | 통계 검정 | 표본 추정 (α=0.05, β=0.2, d=0.5) |
|----|----|--------|----------|
| H1 | PCOS 환자 F0 평균 < 한국 정상 여성 199.6 Hz | One-sample t-test | n ≈ 64 |
| H2 | PCOS 환자 F0 상한 < 정상 여성 | Welch t-test | n ≈ 64/group |
| H3 | PCOS 음성 검출 SVM(eGeMAPS) AUC > 0.75 | Bootstrap CI | n ≈ 100/group |
| H4 | 자궁내막증 통증 점수와 F0 SD 상관 | Pearson r | n ≈ 80 |
| H5 | 자궁내막증 정서 동반 시 ECAPA 임베딩 분리 | Cohen d > 0.5 | n ≈ 64/group |

---

## 6. 참고문헌

> 본 보고서에 사용된 모든 한국 임상 논문은 `04_korean_voice_literature.md` 의 검증된 [번호]로 인용되었다. 추가 학술 통념(MFCC 절차, eGeMAPS 정의 등)은 인용 없이 정리.

### 6.1 한국 논문 (`04_korean_voice_literature.md` 인용)

[1] Mondol SIMMR, Kim R, Lee S. (2023). Hybrid ML Framework for Multistage Parkinson's Disease Classification Using Acoustic Features of Sustained Korean Vowels. **Bioengineering** 10(8):984. DOI: 10.3390/bioengineering10080984

[2] Kim KH, Lee BJ, Koo HW. (2024). Feasibility Study of Parkinson's Speech Disorder Evaluation With Pre-Trained Deep Learning Model. **Korean Journal of Neurotrauma** 20(3):e30. DOI: 10.13004/kjnt.2024.20.e30

[3] Lee J et al. (2024). Exploring Voice Acoustic Features Associated with Cognitive Status in Korean Speakers. **Diagnostics (MDPI)** 14(24):2837. DOI: 10.3390/diagnostics14242837

[4] (Cross-language PD, 한국+대만). (2024). A cross-language speech model for detection of Parkinson's disease. **J Neural Transm**. DOI: 10.1007/s00702-024-02874-z

[5] Namkung J et al. (2024). Novel Deep Learning-Based Vocal Biomarkers for Stress Detection in Koreans. **Psychiatry Investigation** 21(11). DOI: 10.30773/pi.2024.0131

[6] Kim AY, Jang EH, Lee SH, Choi KY, Park JG, Shin HC. (2023). Automatic Depression Detection Using Smartphone-Based Text-Dependent Speech Signals. **JMIR** 25:e34474. DOI: 10.2196/34474

[7] Mun J, Kim S, Kim MJ, Ryu J, Kim S, Chung M. (2022). Automatic detection and severity prediction of CKD using ML classifiers. **Phonetics and Speech Sciences** 14(4):45.

[8] Maryn Y, Kim HT, Kim J. (2018). Validation of the Acoustic Voice Quality Index in the Korean Language. **J Voice** 32(3):278-285. PMID: 30076095

[9] (Kim HT, Kim J 등). (2019). Validation of AVQI v3.01 and ABI in Korean Population. **J Voice**. PMID: 31708369

[12] (한국 저자). (2016). Perceptual and Consonant Analysis for the Voice with Hypothyroidism. **J Korean Soc Laryngol Phoniatr Logop** 27(2):95.

[13] Lee SJ et al. (2016). Aging Effect on Korean Female Voice. **Folia Phoniatrica et Logopaedica** 68:280-286. PMID: 27160514

[15] Smartphone-Based Speech Therapy for Poststroke Dysarthria. (2024). **JMIR** 26:e56417.

[16] Seo YJ, Shin J. (2018). Acoustic characteristics of the sustained vowel phonation according to age groups. **Phonetics and Speech Sciences** 10(4):67-76.

[17] Yang B. (2021). The f0 distribution of Korean speakers in a spontaneous speech corpus. **Phonetics and Speech Sciences** 13(3):31-37. DOI: 10.13064/KSSS.2021.13.3.031

### 6.2 방법론 표준 (학술 통념·기술 표준 — 외부 인용)

- Eyben F, Scherer KR, Schuller BW, et al. (2016). The Geneva Minimalistic Acoustic Parameter Set (GeMAPS) for Voice Research and Affective Computing. **IEEE Trans Affect Comput** 7(2):190-202. DOI: 10.1109/TAFFC.2015.2457417 — **eGeMAPS 표준 정의**.
- Boersma P, Weenink D. (2024). **Praat: doing phonetics by computer (v6.4.x)**. www.praat.org — F0/Jitter/Shimmer/HNR/Formant 임상 표준.
- Eyben F, Wöllmer M, Schuller B. (2010). **openSMILE — The Munich Versatile and Fast Open-Source Audio Feature Extractor**. ACM MM. — IS09/10/13 / eGeMAPS 추출 도구.
- Baevski A, Zhou H, Mohamed A, Auli M. (2020). **wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations**. NeurIPS. — Wav2Vec2 원전.
- Hsu WN, Bolte B, Tsai YHH, et al. (2021). **HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units**. IEEE/ACM TASLP. — HuBERT 원전.
- Desplanques B, Thienpondt J, Demuynck K. (2020). **ECAPA-TDNN: Emphasized Channel Attention, Propagation and Aggregation in TDNN Based Speaker Verification**. INTERSPEECH. — ECAPA-TDNN 원전.
- Maryn Y, De Bodt M, Roy N. (2010). **The Acoustic Voice Quality Index: Toward improved treatment outcomes assessment in voice disorders**. J Commun Disord 43(3):161-174. — AVQI 원전.
- Maryn Y, Roy N, De Bodt M, et al. (2009). **Acoustic measurement of overall voice quality: A meta-analysis**. JASA 126(5):2619-2634. — AVQI 메타분석.
- Lundberg SM, Lee SI. (2017). **A Unified Approach to Interpreting Model Predictions**. NIPS. — SHAP 원전.

### 6.3 PCOS·여성호르몬·음성 관련 (가설 근거 문헌 — 추가 검증 필요)

> 아래는 본 보고서 가설을 뒷받침하는 일반 학술 통념 영역. 본 라운드에서 직접 검증되지 않은 항목은 **[추가 검증 권장]** 표기.

- Abitbol J, Abitbol P, Abitbol B. (1999). **Sex hormones and the female voice**. J Voice 13(3):424-446. — 여성호르몬-음성 핵심 리뷰. **[추가 검증 권장 — 본 라운드 미검색]**
- 안드로겐/PCOS 음성 직접 연구: 본 라운드 한국 코호트 부재 확인. → 향후 *paper-lookup*/*reference-hallucination-guard* 라운드에서 별도 검증 필요.

---

## 7. 부록 — 즉시 적용 권장 코드 골격 (의사코드)

```python
# ───── Stage 1: 신호 획득 (Android UNPROCESSED 권장) ─────
# Android: AudioSource.UNPROCESSED, 16 kHz, 16-bit PCM, mono
# iOS: AVAudioSession .measurement mode

# ───── Stage 2: 전처리 ─────
import librosa, numpy as np
y, sr = librosa.load("vowel_a.wav", sr=16000, mono=True)
y = np.append(y[0], y[1:] - 0.97 * y[:-1])      # pre-emphasis
y = y - y.mean()                                  # DC offset

# VAD
import torch
silero, utils = torch.hub.load('snakers4/silero-vad', 'silero_vad')
get_speech, _, _, _, _ = utils
speech_ts = get_speech(torch.tensor(y), silero, sampling_rate=sr)

# ───── Stage 3-A: Praat (Parselmouth) ─────
import parselmouth as pm
snd = pm.Sound("vowel_a.wav")
pitch = snd.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=500)
F0_mean = pm.praat.call(pitch, "Get mean", 0, 0, "Hertz")
pp = pm.praat.call(snd, "To PointProcess (periodic, cc)", 75, 500)
jitter = pm.praat.call(pp, "Get jitter (local)", 0,0, 0.0001, 0.02, 1.3)
shimmer = pm.praat.call([snd, pp], "Get shimmer (local)", 0,0, 0.0001, 0.02, 1.3, 1.6)
harmonicity = snd.to_harmonicity()
HNR = harmonicity.values[harmonicity.values != -200].mean()

# ───── Stage 3-B: openSMILE eGeMAPS-v02 ─────
import opensmile
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals
)
egemaps = smile.process_file("vowel_a.wav")  # → 88 features

# ───── Stage 3-D: SpeechBrain ECAPA-TDNN ─────
from speechbrain.inference.speaker import EncoderClassifier
ecapa = EncoderClassifier.from_hparams("speechbrain/spkrec-ecapa-voxceleb")
emb = ecapa.encode_batch(torch.tensor(y).unsqueeze(0)).squeeze().numpy()  # → 192-d

# ───── Stage 4-5: 학습 + SHAP ─────
import xgboost as xgb, shap
X = np.concatenate([[F0_mean, jitter, shimmer, HNR],
                    egemaps.values.flatten(), emb])
# 다수 화자 X/y 구축 후
model = xgb.XGBClassifier(max_depth=4, n_estimators=300, learning_rate=0.05)
model.fit(X_train, y_train)
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)
shap.summary_plot(shap_values, X_test)
```

---

**End of Report.**
**파일 경로**: `C:\Users\neohc\Desktop\ClaudeCode\_workspace4\06_voice_feature_extraction.md`
**작성 완료**: 2026-05-06
