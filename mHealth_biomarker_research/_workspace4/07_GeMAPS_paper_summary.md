# 논문 요약: The Geneva Minimalistic Acoustic Parameter Set (GeMAPS) for Voice Research and Affective Computing

**작성일**: 2026-05-06
**원본 논문**: Eyben F, Scherer KR, Schuller BW, Sundberg J, André E, Busso C, Devillers L, Epps J, Näränen P, Narayanan S, Schuller BW, Tian L, Weninger F. (2016).
**게재지**: IEEE Transactions on Affective Computing, 7(2), 190–202.
**DOI**: [10.1109/TAFFC.2015.2457417](https://doi.org/10.1109/TAFFC.2015.2457417)
**인용 현황**: 6,000+ citations (2025 기준), 음성 감성·의료 AI 분야 표준 참조 논문

---

## 1. 논문 제안 배경 및 동기

### 1.1 문제 인식

2010년대 이전까지 음성 연구자들은 각자 다른 특징셋을 사용했다.

- **초대형 특징셋** (IS13 ComParE: 6,373차원): 소표본 의료 연구에서 심각한 과적합 유발
- **연구자별 임의 특징 선택**: 재현성 없음, 메타분석 불가
- **생물학적·언어학적 근거 부재**: 통계적으로 살아남은 특징이 무엇을 의미하는지 불명확

> "There is a disconcerting lack of a standard set of features that researchers agree upon."

### 1.2 해결책

음성·감성·언어·의학·심리 분야 **12명의 국제 전문가 합의(expert consensus)**를 통해 이론적으로 정당화된, 최소한의 해석 가능한 표준 특징셋을 제안.

---

## 2. GeMAPS 특징셋 구조

### 2.1 두 가지 버전

| 버전                                 | 차원       | 특성                      |
| ---------------------------------- | -------- | ----------------------- |
| **GeMAPS** (v01)                   | **62차원** | 핵심 최소 특징셋 — 소표본·해석 우선   |
| **eGeMAPS** (extended, v01b / v02) | **88차원** | GeMAPS 확장 — 정밀 분석·임상 권장 |

### 2.2 LLD (Low-Level Descriptor, 저수준 기술자) 목록

GeMAPS는 18개 LLD를 정의하고, 이에 통계적 함수(functional)를 적용하여 최종 특징 벡터를 생성한다.

#### 주파수 관련 (Frequency)
| LLD                           | 설명                    | 임상 의미                                 |
| ----------------------------- | --------------------- | ------------------------------------- |
| **F0 (semitone, 27.5 Hz 기준)** | 기본 주파수 (반음 단위 로그 스케일) | 음높이, 성대 진동 주기. 안드로겐 영향으로 PCOS에서 감소 가설 |
| **Jitter (local)**            | 인접 F0 주기 간 변동률 (%)    | 성대 진동 불규칙성. 신경계·음성장애 지표               |

#### 에너지/강도 관련 (Energy/Amplitude)
| LLD | 설명 | 임상 의미 |
|-----|------|---------|
| **Shimmer (local)** | 인접 진폭 주기 간 변동률 (%) | 성대 폐쇄 균일성. 점막 변화 반영 |
| **Loudness** | 등청감 곡선(equal-loudness) 기반 상대 음량 | 발화 에너지, 호흡 효율 |

#### 스펙트럼 균형 관련 (Spectral Balance)
| LLD | 설명 | 임상 의미 |
|-----|------|---------|
| **Alpha ratio** | 50–1,000 Hz 대역 에너지 / 1,000–5,000 Hz 대역 에너지 비율 | 발화 명료도, 성도 설정 |
| **Hammarberg index** | 0–2 kHz 최대 에너지 / 2–5 kHz 최대 에너지 | 음성 전반적 활력도 |
| **Spectral slope 0–500 Hz** | 해당 구간 스펙트럼 기울기 | 성대 활동 기식성(breathiness) 관련 |
| **Spectral slope 500–1,500 Hz** | 해당 구간 스펙트럼 기울기 | 고주파 에너지 감쇠 패턴 |

#### 포르만트 (Formants)
| LLD | 설명 | 임상 의미 |
|-----|------|---------|
| **F1 주파수** | 1번 포르만트 중심 주파수 | 모음 개방도 (혀 높이) |
| **F1 대역폭** | F1의 공명 폭 | 성도 감쇠 특성 |
| **F2 주파수** | 2번 포르만트 중심 주파수 | 혀 전후 위치. 모음 공간 지표 |
| **F3 주파수** | 3번 포르만트 중심 주파수 | 화자 개인 특성, 성도 길이 |
| **F1 진폭 (H1 대비)** | F1 대역 하모닉 에너지 상대강도 | 성대 음원 특성 |
| **F2 진폭 (H1 대비)** | F2 대역 하모닉 에너지 상대강도 | 조음 효율 |
| **F3 진폭 (H1 대비)** | F3 대역 하모닉 에너지 상대강도 | — |

#### 음성 품질 (Voice Quality)
| LLD | 설명 | 임상 의미 |
|-----|------|---------|
| **HNR (Harmonics-to-Noise Ratio)** | 주기 신호 대 잡음 비율 (dB) | 음성 청결도. 높을수록 건강한 음성 |

#### 켑스트럼 (Cepstral)
| LLD | 설명 | 임상 의미 |
|-----|------|---------|
| **MFCC 1–4** | Mel-주파수 켑스트럼 계수 1~4번 (4개 LLD) | 성도 모양 요약. 화자 특성·감정·건강 상태 인코딩 |

> GeMAPS v01 기준 18개 LLD. eGeMAPS에서는 스펙트럼 플럭스(Spectral Flux), 추가 MFCC 등이 보완됨.

---

## 3. 특징 생성 방법 (LLD → 최종 벡터)

### 3.1 처리 흐름

```
원시 음성 (WAV)
   ↓
프레임 분할 (25 ms 윈도우, 10 ms hop)
   ↓
18개 LLD 추출 (프레임 단위)
   ↓
Voiced / Unvoiced 구간 분리
   ↓
Functionals 적용 (통계 집계)
   ↓
최종 벡터 (GeMAPS: 62-d / eGeMAPS: 88-d)
```

### 3.2 Functional (통계 함수) 종류

LLD 시계열에 다음 함수들을 적용하여 고정 크기 벡터를 생성한다:

| Functional | 설명 |
|-----------|------|
| 평균 (mean) | 기본 수준 |
| 표준편차 (std) | 변동성 |
| 20/50/80 백분위수 | 분포 형태 |
| 상승/하강 기울기 | 시간적 추세 |
| voiced/unvoiced 구간 통계 | 발화 구조 |

### 3.3 eGeMAPS v02 (88차원) 세부 구성

| 그룹 | 차원 수 | 포함 특징 |
|------|--------|---------|
| 주파수 (F0, Jitter) | ~8 | F0 mean/std/percentile, Jitter mean |
| 에너지 (Shimmer, Loudness) | ~8 | Shimmer, Loudness functionals |
| 스펙트럼 균형 (Alpha, Hammarberg, Slope) | ~20 | 각 functionals |
| 포르만트 | ~20 | F1/F2/F3 freq+BW+amp functionals |
| HNR | ~4 | Mean, std |
| MFCC 1–4 | ~16 | 각 mean + std |
| 시간·율동 특징 | ~12 | Rate of loudness peaks, voiced/unvoiced ratio, speech rate 등 |

> 정확한 구성은 openSMILE의 `eGeMAPSv02.conf` 파일 참조.

---

## 4. 논문의 핵심 기여

### 4.1 표준 최소 특징셋 제안
대규모 특징셋 없이도 의미 있는 성능을 보이는 62-d / 88-d 공통 기준선 제공.

### 4.2 이론적 정당화
- 각 특징의 **생물학적·음성학적·심리음향학적 근거** 명시
- 단순 통계 생존 특징이 아닌, 전문가가 합의한 해석 가능한 특징

### 4.3 소표본 연구에서의 실용성
6,373차원 IS13 대비 88차원 eGeMAPS는:
- 과적합 위험 대폭 감소
- SVM·LR 등 선형 모델과 궁합 우수
- 의료 데이터(n=수십~수백)에 최적

### 4.4 재현성·비교 가능성 확보
동일 특징셋 사용 → 논문 간 직접 성능 비교 가능

---

## 5. GeMAPS vs eGeMAPS vs IS13 비교

| 항목 | GeMAPS | eGeMAPS | IS13 ComParE |
|------|--------|---------|-------------|
| 차원 | 62 | 88 | 6,373 |
| 과적합 위험 | 낮음 | 낮음 | 높음 (소표본 시) |
| 해석 가능성 | 높음 | 높음 | 낮음 |
| 성능 (충분한 데이터) | 중간 | 중간~상 | 상 |
| 성능 (소표본 n<200) | 상 | 상 | 하 |
| 권장 모델 | SVM, LR, RF | SVM, XGBoost | 딥러닝, AutoML |
| 의료 연구 권장 | ★★★ | ★★★★ | 조건부 |

---

## 6. openSMILE을 통한 추출

GeMAPS/eGeMAPS는 **openSMILE** 라이브러리로 표준화된 추출이 가능하다.

### Python 예시 코드

```python
import opensmile

# eGeMAPS v02 추출 (권장)
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals
)

features = smile.process_file("audio.wav")
# → DataFrame, shape: (1, 88)
```

```python
# GeMAPS v01 (62차원) 추출
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.GeMAPSv01a,
    feature_level=opensmile.FeatureLevel.Functionals
)
```

### 주요 파라미터 설명

| openSMILE 파라미터 명 | 의미 |
|---------------------|------|
| `F0semitoneFrom27.5Hz_sma3nz_amean` | F0 반음 단위 평균 (비유성음 구간 제외) |
| `jitterLocal_sma3nz_amean` | Jitter 평균 |
| `shimmerLocaldB_sma3nz_amean` | Shimmer (dB) 평균 |
| `HNRdBACF_sma3nz_amean` | HNR 평균 (dB) |
| `loudness_sma3_amean` | Loudness 평균 |
| `alphaRatioV_sma3nz_amean` | Alpha ratio (유성음 구간) |
| `mfcc1_sma3_amean` | MFCC 1번 계수 평균 |
| `F1frequency_sma3nz_amean` | F1 주파수 평균 |
| `VoicedSegmentsPerSec` | 초당 유성음 구간 수 |
| `MeanVoicedSegmentLengthSec` | 평균 유성음 구간 길이 |

---

## 7. 의료·질환 예측 분야 적용 사례

| 질환 | 연구 | GeMAPS/eGeMAPS 활용 방식 |
|------|------|------------------------|
| 만성 신장병 (CKD) | Mun et al. 2022 (한국, 1,523발화) | eGeMAPS 88 + XGBoost → CKD vs HC F1=0.93 |
| 우울증 | 다수 INTERSPEECH 논문 | eGeMAPS + SVM → AVEC 챌린지 표준 |
| 파킨슨병 | 다수 연구 | eGeMAPS + RF, SVM |
| 감성/스트레스 | AVEC 2013~2019 챌린지 | IS10/eGeMAPS 기준선 |
| PCOS (가설) | 현재 연구 | eGeMAPS 88 + SHAP → F0 저하 탐지 |

---

## 8. 본 프로젝트(PCOS·자궁내막증) 적용 전략

### 8.1 권장 특징셋

```
1차 사용: eGeMAPS v02 (88차원) — 소표본 최적, 해석 가능
2차 보완: eGeMAPS 내 F0·Jitter·Shimmer·HNR·Formants 특징 SHAP 분석
```

### 8.2 PCOS 특화 해석 가능 특징 (eGeMAPS 내)

| eGeMAPS 특징 | PCOS 가설 메커니즘 |
|------------|----------------|
| `F0semitoneFrom27.5Hz_sma3nz_amean` | 안드로겐 ↑ → 성대 비후 → F0 ↓ |
| `F0semitoneFrom27.5Hz_sma3nz_stddevNorm` | 음역 변동성 ↓ (단조로운 음성) |
| `shimmerLocaldB_sma3nz_amean` | 성대 점막 부종 → 진폭 불안정 ↑ |
| `HNRdBACF_sma3nz_amean` | 점막 변화 → 잡음 ↑ → HNR ↓ |
| `F1frequency_sma3nz_amean` | 성도 공명 변화 |
| `VoicedSegmentsPerSec` | 발화 패턴 변화 |

### 8.3 분류 파이프라인

```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf', C=1.0, probability=True))
])

# eGeMAPS 88-d → SVM → PCOS 예측
# Subject-independent 5-fold CV 필수
```

---

## 9. 논문 한계 및 후속 발전

### 9.1 GeMAPS의 한계
- 딥러닝 시대 이전 설계 → 원시 파형(raw waveform) 학습 기반 모델(Wav2Vec2, HuBERT)에는 적용 불가
- 발화 내용(텍스트)이 다른 자유 발화 비교 시 신뢰도 제한
- 개인 간 기저치 차이 (화자 정규화 필요)

### 9.2 후속 발전
- **eGeMAPS v02** (2016 이후): 일부 특징 정의 정교화, openSMILE 공식 지원
- **ComParE 2023**: GeMAPS를 기반으로 한 최신 챌린지 기준선
- **GeMAPS + 전이학습 결합**: eGeMAPS를 보조 특징으로, Wav2Vec2 임베딩과 융합하는 hybrid 접근

---

## 10. 참고

- **원문**: Eyben et al. (2016). IEEE Trans Affect Comput. DOI: [10.1109/TAFFC.2015.2457417](https://doi.org/10.1109/TAFFC.2015.2457417)
- **openSMILE 공식 문서**: [https://audeering.github.io/opensmile/](https://audeering.github.io/opensmile/)
- **eGeMAPS 설정 파일**: openSMILE `config/egemaps/v02/eGeMAPSv02.conf`
- **관련 파일**: `_workspace4/06_voice_feature_extraction.md` §1.C.4 (OpenSMILE 특징셋 비교표)
