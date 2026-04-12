# PCOS·자궁내막증 스마트폰 카메라 AI 예측 연구 설계서

**버전**: 1.0
**작성일**: 2026-04-11
**패턴 적용**: Harness100 research-designer + K-Dense citation-management

---

## 1. 연구 배경 및 필요성

### 1.1 진단 지연 문제

자궁내막증은 증상 발현부터 확진(복강경)까지 평균 **7-10년**이 소요되며, PCOS는 진단 기준(Rotterdam)에 대한 인식 부족과 초음파·호르몬 검사 접근성 제한으로 상당수 환자가 미진단 상태로 남아 있다. 두 질환 모두 조기 개입이 장기 합병증(불임, 심혈관 질환, 대사증후군, 만성 통증)을 예방하는 데 핵심적이나, 현재의 진단 경로는 침습적이고 비용이 높으며 접근성이 낮다.

### 1.2 디지털 바이오마커의 가능성

스마트폰 카메라 기반 디지털 바이오마커는 다음과 같은 이점을 제공한다:

- **비침습성**: 혈액 채취나 영상 검사 없이 측정 가능
- **접근성**: 전 세계 스마트폰 보급률 > 80%
- **연속성**: 일일 반복 측정으로 종단 패턴 포착 가능
- **비용 효율**: 추가 하드웨어 불필요

### 1.3 근거 기반

본 연구의 근거는 세 갈래의 수렴적 증거에 기반한다:

1. **PCOS-HRV 연관성 확립**: 17개 연구 메타분석에서 SDNN SMD: -0.763, LF/HF SMD: +0.670, HFnu SMD: -0.873 확인 [Mirzohreh et al., 2024, PMID:39049099]
2. **자궁내막증-미주신경톤 저하 확인**: RMSSD, pNN50, HF의 유의한 감소 [Hao et al., 2021, PMID:33446725; Moreira et al., 2021, PMID:34719338]
3. **rPPG 기술 성숙**: 비접촉 HRV 측정이 ECG 대비 상관계수 0.85-0.95 달성; 스마트폰 PPG AF 탐지 정확도 98.5% (FDA 인증) [FibriCheck, Sollee et al., 2025]

**핵심 공백**: rPPG를 PCOS/자궁내막증 환자에 직접 적용한 연구는 **전무**하다.

---

## 2. 연구 질문

### 2.1 Primary Research Question

> **스마트폰 카메라 기반 디지털 바이오마커(rPPG-HRV, 얼굴 피부 분석, 월경 패턴)가 PCOS 및 자궁내막증을 임상 진단 수준(AUC >= 0.80)으로 예측할 수 있는가?**

### 2.2 Secondary Research Questions

**SRQ1 (질환별 특이성)**: PCOS와 자궁내막증은 서로 다른 rPPG-HRV 시그니처를 보이는가? 구체적으로, PCOS의 교감신경 항진(LF/HF 상승)과 자궁내막증의 미주신경 저하(RMSSD 감소)가 비접촉 rPPG로 감별 가능한가?

**SRQ2 (기술별 기여도)**: 멀티모달 접근(rPPG-HRV + 얼굴 피부 분석 + 월경 추적 데이터)이 단일 모달리티 대비 얼마나 예측 성능을 향상시키는가?

**SRQ3 (실용성 평가)**: 일상 환경(다양한 조명, 스마트폰 기종, 피부색)에서의 rPPG 신호 품질이 임상적으로 유의미한 HRV 차이를 탐지하기에 충분한가?

---

## 3. 가설 (H1~H5)

### H1: rPPG-HRV는 PCOS를 건강 대조군과 감별할 수 있다

- **조작적 정의**: 스마트폰 전면 카메라 60초 촬영 -> rPPG 신호 추출 -> HRV 지표(LF/HF, RMSSD, HFnu) 산출
- **근거**: PCOS의 LF/HF SMD +0.670 (메타분석, 17개 연구) [1]; rPPG-HRV vs ECG r=0.85-0.95 [10]
- **귀무가설**: PCOS군과 대조군의 rPPG-HRV 지표 차이 = 0
- **대립가설**: PCOS군의 LF/HF가 대조군 대비 유의하게 높고, RMSSD/HFnu가 유의하게 낮다 (단측 검정, alpha=0.05)
- **예상 AUC**: 0.70-0.80
- **성공 기준**: AUC >= 0.70, p < 0.05

### H2: rPPG-HRV 월경주기 패턴은 PCOS 불규칙 주기를 탐지할 수 있다

- **조작적 정의**: 3주기 이상 일일 rPPG 촬영 -> 주기별 HRV 변동 진폭(amplitude) 및 주기성(periodicity) 추출
- **근거**: 정상 월경주기에서 HRV는 규칙적 변동(RHRmin 5일차, RHRmax 26일차) [12]; PCOS에서 이 패턴 소실 예상
- **귀무가설**: PCOS군과 대조군의 HRV 주기 변동 패턴 차이 = 0
- **대립가설**: PCOS군에서 HRV 주기 변동 진폭이 유의하게 감소하고, 주기 예측 정확도가 유의하게 낮다
- **예상 정확도**: 주기 이상 탐지 > 85%
- **성공 기준**: 불규칙 주기 탐지 민감도 >= 80%

### H3: 스마트폰 카메라 기반 PCOS 피부 표현형 복합 점수는 Rotterdam 기준과 유의하게 상관한다

- **조작적 정의**: 얼굴/목/팔 사진 -> (1) 여드름 등급(IGA), (2) 다모증 점수(mFG), (3) 흑색극세포증 유무(AN), (4) 얼굴 BMI -> 복합 PCOS-DermScore 산출
- **근거**: 여드름 IGA 정확도 0.85 [13], 다모증 mFG 일치도 0.89 [17], AN AUC 0.854 [18], 얼굴 BMI MAE 1.04 [19]
- **귀무가설**: PCOS-DermScore와 Rotterdam 기준 확진 간 상관 = 0
- **대립가설**: PCOS-DermScore가 Rotterdam 기준 PCOS 진단과 유의하게 양의 상관을 보인다
- **예상 AUC**: 0.75-0.85
- **성공 기준**: AUC >= 0.75, Spearman rho >= 0.50

### H4: rPPG-HRV 저하는 자궁내막증 환자의 통증 중증도와 음의 상관을 보인다

- **조작적 정의**: 자궁내막증 환자 일일 rPPG 촬영 + 통증 VAS (0-100mm) 동시 기록 -> RMSSD-VAS 상관 분석
- **근거**: vmHRV-통증 상관 [6]; 미주신경톤 저하 [7]; MBI 후 HRV 개선 + 통증 감소 [9]
- **귀무가설**: RMSSD와 통증 VAS 간 상관계수 = 0
- **대립가설**: RMSSD와 통증 VAS 간 유의한 음의 상관 (r < 0)
- **예상 상관**: r = -0.30 ~ -0.50
- **성공 기준**: r <= -0.25, p < 0.05

### H5: rPPG-HRV + 얼굴 표현형 + 월경 패턴 멀티모달 모델은 PCOS/자궁내막증/건강을 동시 감별할 수 있다

- **조작적 정의**: 3-모달 입력(rPPG-HRV + 얼굴 AI + 앱 데이터) -> 3-class 분류 모델 -> 매크로 AUC 평가
- **근거**: 각 모달리티 독립 성능 확인; PCOS(교감 항진 + 피부 표현형) vs. 자궁내막증(미주신경 저하 + 통증 패턴) 차별적 프로파일
- **귀무가설**: 멀티모달 모델의 3-class AUC <= 단일 모달 최고 AUC
- **대립가설**: 멀티모달 모델의 3-class 매크로 AUC가 단일 모달 최고 AUC보다 유의하게 높다
- **예상 AUC**: 0.80-0.90
- **성공 기준**: 매크로 AUC >= 0.80, 단일 모달 대비 AUC 향상 >= 0.05

---

## 4. 연구 설계

### 4.1 연구 유형

**전향적 다기관 코호트 연구** (Phase I: 탐색적 파일럿 -> Phase II: 검증 코호트)

| 단계 | 목적 | 기간 | 대상 수 |
|------|------|------|---------|
| Phase I (파일럿) | 기술 타당성 + 예비 효과크기 추정 | 6개월 | 각 군 50명 (총 150명) |
| Phase II (검증) | 가설 검증 + 모델 개발/검증 | 12-18개월 | 각 군 200명 (총 600명) |
| Phase III (외부 검증) | 독립 코호트 외부 검증 | 6개월 | 각 군 100명 (총 300명) |

### 4.2 대상 및 표본 크기

**대상 선정 기준**:
- 가임기 여성 (18-45세)
- 스마트폰 소유 (iOS 15+ / Android 11+, 전면 카메라 8MP 이상)
- PCOS군: Rotterdam 기준 확진 (초음파 + 호르몬)
- 자궁내막증군: 복강경/MRI/초음파 확진 (rASRM stage I-IV)
- 대조군: 정기 월경, 부인과 질환력 없음

**제외 기준**:
- 양 질환 공존 (PCOS + 자궁내막증)
- 호르몬 피임약/GnRH 작용제 사용 (과거 3개월 이내)
- 심혈관 질환, 자율신경 질환
- 피부과 질환 (여드름, 다모증 이외)으로 활성 치료 중

**표본 크기 산정 (Phase II)**:

H1 기준: 메타분석에서 PCOS vs. 대조군 LF/HF SMD = 0.670 [1]. rPPG 변환에 따른 감쇠율 15% 적용 시 예상 효과크기 d = 0.57. 양측 검정 alpha=0.05, power=0.80, t-test 기준:
- n = 2 x (1.96 + 0.84)^2 / 0.57^2 = 2 x 7.84 / 0.325 = 48.2 -> **최소 50명/군**

H5(3-class 분류) 기준: AUC 0.80 달성을 위한 머신러닝 모델의 경험적 규칙(특성 수 30-50, 10배 이상 사례 필요):
- 50개 특성 x 10 = 500 -> **최소 500명 (총)**
- 드롭아웃 20% 감안: **600명 (각 군 200명)**

### 4.3 독립변수, 종속변수, 통제변수

**독립변수 (Predictors)**:

| 모달리티 | 변수 | 수집 방법 | 빈도 |
|---------|------|----------|------|
| **rPPG-HRV** | SDNN, RMSSD, pNN50, LF, HF, LF/HF, HFnu, meanRR | 전면 카메라 60초 얼굴 촬영 | 일 1회 (아침) |
| **얼굴 피부 분석** | 여드름 등급(IGA), 다모증 점수(mFG), AN 유무, 피부색(L*a*b*), 얼굴 BMI | 표준화 셀피 (3장: 정면, 좌측 45도, 우측 45도) | 주 1회 |
| **월경 패턴** | 주기 길이, 출혈 기간, 통증 VAS, 기분, 에너지 수준 | 앱 자가보고 | 일 1회 |
| **rPPG 부가** | SpO2 추정값, 혈압(SBP/DBP) 추정값 | rPPG 동일 세션에서 추출 | 일 1회 |

**종속변수 (Outcomes)**:

- 일차: 3-class 분류(PCOS / 자궁내막증 / 건강) 매크로 AUC
- 이차: 각 이진 분류 AUC, 민감도, 특이도, F1-score
- 탐색적: 통증-HRV 상관, 주기 이상 탐지 정확도

**통제변수 (Covariates)**:

| 변수 | 근거 | 수집 방법 |
|------|------|----------|
| 연령 | HRV의 연령 의존성 | 등록 시 |
| BMI | 비만 PCOS에서 HRV 차이 소실 [1] | 등록 시 + 얼굴 BMI 추정 |
| Fitzpatrick 피부 유형 (I-VI) | rPPG 피부색 편향 [FibriCheck 2025] | 등록 시 자가보고 + 피부 사진 |
| 스마트폰 기종/OS | 카메라 센서 차이 | 자동 수집 |
| 조명 조건 | rPPG 신호 품질 영향 | 촬영 시 자동 측정 (lux 센서) |
| 카페인/운동/수면 | HRV 급성 변동 요인 | 촬영 전 간단 설문 |
| 월경주기 위상 | HRV의 호르몬 의존적 변동 [11, 12] | 앱 자동 추정 + 배란 테스트(Phase I) |

---

## 5. 제안 바이오마커 세트 (우선순위)

### 5.1 Priority 1: 즉시 적용 가능 (기존 기술 + PCOS/자궁내막증 직접 근거)

| # | 바이오마커 | 질환 | 근거 강도 | 기술 성숙도 | 예상 효과크기 |
|---|----------|------|----------|-----------|-------------|
| P1-1 | rPPG-HRV (LF/HF, RMSSD, HFnu) | PCOS + 자궁내막증 | High (메타분석) | High (ECG r=0.85-0.95) | d=0.57 (PCOS), d=0.45 (Endo) |
| P1-2 | 월경주기 HRV 패턴 (종단 변동) | PCOS | Moderate | High | 주기 이상 탐지 >85% |
| P1-3 | 여드름 자동 등급화 (IGA) | PCOS | Moderate (IGA 0.85) | High | PCOS 스크리닝 보조 |
| P1-4 | 다모증 영상 mFG 점수 | PCOS | Moderate (일치도 0.89) | High | Rotterdam 기준 직접 지원 |

### 5.2 Priority 2: 유망 (간접 근거, 추가 검증 필요)

| # | 바이오마커 | 질환 | 근거 강도 | 기술 성숙도 | 비고 |
|---|----------|------|----------|-----------|------|
| P2-1 | 흑색극세포증(AN) 탐지 | PCOS (인슐린 저항성) | Moderate (AUC 0.854) | Moderate | ANcam 기술 활용 |
| P2-2 | 얼굴 BMI 추정 | PCOS (대사 위험) | Moderate (MAE 1.04) | Moderate | 대사 공변수로 활용 |
| P2-3 | rPPG 혈압 추정 (SBP/DBP) | PCOS 심혈관 위험 | Moderate (95.3%/96.4%) | Moderate | Luo et al. 기술 |
| P2-4 | rPPG SpO2 추정 | 자궁내막증 염증 | Moderate (MAE 1.27%) | Moderate | 미세 변화 탐지 가능성 |

### 5.3 Priority 3: 탐색적 (가설 수준, 신규 제안)

| # | 바이오마커 | 질환 | 가설 | 필요 연구 |
|---|----------|------|------|----------|
| P3-1 | 피부색 시계열 변화 (L*a*b*) | PCOS | 호르몬 변동에 따른 미세 피부색 변화 포착 | 종단 파일럿 |
| P3-2 | 안면 미세표정 + rPPG 통증 탐지 | 자궁내막증 | 만성 통증의 무의식적 표정 반응 + 자율신경 반응 동시 측정 | 탐색적 코호트 |
| P3-3 | 야간 rPPG SpO2 변동 | PCOS-OSA | 수면 중 산소포화도 변동으로 OSA 스크리닝 | 기술 검증 필요 |
| P3-4 | 안드로겐성 탈모 패턴 분석 | PCOS | 두피/이마선 사진에서 탈모 패턴 자동 분류 | 데이터셋 구축 필요 |

---

## 6. AI 모델 아키텍처 제안

### 6.1 전체 구조: 멀티모달 rPPG + 얼굴 분석 + 주기 데이터 융합

```
입력 계층                      특성 추출 계층              융합 계층           출력 계층
-----------                   ---------------            ----------         ----------

[60초 얼굴 영상]  -> rPPG 신호 추출 -> 1D-CNN/Transformer -> HRV 특성 벡터 (dim=32)  ─┐
                     (CHROM + DeepPhys)                                              │
                                                                                     │
[표준화 셀피 x3] -> 얼굴 분석 CNN  -> EfficientNet-B0   -> DermScore 벡터 (dim=16)   ─┼─> Cross-Attention -> FC -> Softmax
                     (여드름/AN/mFG/BMI)                                              │    Fusion Layer     층    3-class
                                                                                     │    (dim=64)              (PCOS/Endo/Healthy)
[월경 앱 데이터]  -> 시계열 임베딩  -> LSTM/TCN          -> 주기 특성 벡터 (dim=16)   ─┘
                     (주기/통증/증상)
```

### 6.2 모듈별 상세

**Module A: rPPG-HRV 추출기**

| 구성 요소 | 선택지 | 근거 |
|----------|--------|------|
| 얼굴 탐지 | MediaPipe Face Mesh (468 랜드마크) | 모바일 최적화, 실시간 |
| ROI 선택 | 이마 + 양 볼 (RGB 3채널) | 문헌 표준 |
| rPPG 신호 추출 | CHROM (기본) + DeepPhys (DL 보완) | CHROM: 견고성, DeepPhys: 저조도 대응 |
| HRV 산출 | IBI 검출 -> 시간영역(SDNN, RMSSD) + 주파수영역(LF, HF, LF/HF) | 표준 HRV 분석 |
| 신호 품질 평가 | SQI (Signal Quality Index) 자동 산출 -> SQI < 0.6 시 재촬영 요청 | 노이즈 데이터 배제 |

**Module B: 얼굴 피부 분석기 (PCOS-DermScore)**

| 하위 모듈 | 모델 | 입력 | 출력 |
|----------|------|------|------|
| 여드름 탐지/등급화 | Faster R-CNN + LightGBM [13] 또는 AcneAI [15] | 얼굴 정면 | IGA 등급 (0-4) |
| 다모증 스코어링 | ResNet50 + 회귀 | 상순/턱/목 사진 | mFG 점수 (0-36) |
| 흑색극세포증 탐지 | 색상 채널(CMYK_K) + ML [18] | 목/겨드랑이 사진 | AN 유무 + 등급 |
| BMI 추정 | ResNet50 세그멘테이션 [19] 또는 PatchBMI-Net [20] | 얼굴 정면 | BMI 연속값 |

**Module C: 월경 패턴 분석기**

| 입력 | 처리 | 출력 |
|------|------|------|
| 주기 길이 시계열 (과거 6-12주기) | LSTM (hidden=64, 2층) | 주기 규칙성 점수 |
| 일일 통증 VAS 시계열 | TCN (Temporal Convolutional Network) | 통증 패턴 특성 |
| 증상 동반 기록 (다변량) | Transformer Encoder | 증상 프로파일 임베딩 |

**Module D: 멀티모달 융합**

| 전략 | 방법 | 장점 |
|------|------|------|
| Early Fusion | 특성 벡터 연결 (concat) | 단순, 해석 용이 |
| **Cross-Attention Fusion** (권장) | 모달 간 교차 주의 메커니즘 | 모달 간 상호작용 학습, 누락 모달 대응 가능 |
| Late Fusion | 각 모달 독립 예측 후 앙상블 | 모달 독립성 보장, 부분 데이터 활용 가능 |

### 6.3 학습 전략

- **사전학습**: 각 모듈 독립적으로 공개 데이터셋에서 사전학습 (UBFC-rPPG, ACNE04, CelebA-BMI)
- **미세조정**: 수집 코호트 데이터로 end-to-end 미세조정
- **교차검증**: 5-fold stratified cross-validation + 독립 테스트 세트 (20%)
- **해석 가능성**: SHAP/Grad-CAM으로 바이오마커별 기여도 시각화
- **온디바이스 배포**: TFLite/CoreML로 모바일 최적화 (개인정보 보호)

### 6.4 개인정보 보호 설계 (Privacy-by-Design)

- rPPG 신호 추출 후 원본 영상 즉시 삭제 (온디바이스)
- 피부 분석 시 특성 벡터만 서버 전송, 원본 사진 미전송
- Federated Learning 옵션: 모델 파라미터만 교환, 원시 데이터 미이동

---

## 7. 평가 지표

### 7.1 일차 평가 지표

| 지표 | 정의 | 목표 값 | 적용 가설 |
|------|------|--------|----------|
| **매크로 AUC** | 3-class OvR AUC 평균 | >= 0.80 | H5 |
| **이진 AUC (PCOS vs. 대조)** | ROC AUC | >= 0.75 | H1, H3 |
| **이진 AUC (Endo vs. 대조)** | ROC AUC | >= 0.70 | H4 |
| **민감도 (Sensitivity)** | TP / (TP + FN) | >= 0.80 (스크리닝 목적) | H1-H5 |
| **특이도 (Specificity)** | TN / (TN + FP) | >= 0.70 | H1-H5 |

### 7.2 이차 평가 지표

| 지표 | 정의 | 적용 |
|------|------|------|
| F1-score (매크로) | 정밀도-재현율 조화 평균 | 클래스 불균형 대응 |
| PPV / NPV | 양성/음성 예측도 | 임상 유용성 |
| Cohen's Kappa | 평가자 간 일치도 (mFG, IGA) | H3 신뢰도 |
| Pearson/Spearman r | HRV-통증 상관 | H4 |
| DeLong test | AUC 간 유의차 검정 | H5 (단일 vs. 멀티모달) |
| Calibration plot | 예측 확률 교정 | 모델 신뢰도 |

### 7.3 기술 평가 지표

| 지표 | 정의 | 목표 값 |
|------|------|--------|
| rPPG SQI (Signal Quality Index) | 유효 세션 비율 | >= 85% |
| rPPG-ECG 상관 (검증 서브셋) | 동시 ECG 대비 HRV 일치도 | r >= 0.80 |
| 추론 속도 | 온디바이스 처리 시간 | < 5초/세션 |
| Fitzpatrick 편향 | 피부 유형별 AUC 차이 | delta-AUC < 0.05 |

---

## 8. 예상 한계 및 편향 통제

### 8.1 예상 한계

| 한계 | 설명 | 완화 전략 |
|------|------|----------|
| **rPPG 신호 품질** | 자연광/저조도/움직임에 의한 노이즈 | SQI 기반 품질 필터링; CHROM+DeepPhys 하이브리드; 재촬영 프롬프트 |
| **피부색 편향** | Fitzpatrick V-VI에서 rPPG 정확도 저하 [FibriCheck 2025] | 피부 유형별 계층화 분석; 데이터 증강; 적응적 ROI 선택 |
| **자가보고 편향** | 월경/증상 기록의 주관성 및 누락 | 다중 데이터 소스 교차 검증; 최소 기록률 기준(주기당 >= 70%) 설정 |
| **선택 편향** | 스마트폰 소유/기술 친화적 대상 편중 | 다기관 모집; 사회경제적 계층 다변화; 기종 다양성 확보 |
| **진단 기준 이질성** | PCOS Rotterdam vs. AE-PCOS; 자궁내막증 확진 방법 차이 | 표준화된 진단 프로토콜; Gold standard 명시; 하위그룹 분석 |
| **단일 국가 검증** | 한국 인구 대상 초기 검증 | Phase III에서 다국적 외부 검증 계획 |

### 8.2 편향 통제 전략

**모집 단계**:
- 계층화 무작위 모집 (연령, BMI, 피부 유형)
- PCOS 아형별 균등 배분 (hyperandrogenic, metabolic, lean PCOS)
- 자궁내막증 rASRM 단계별 균등 배분

**데이터 수집 단계**:
- 촬영 프로토콜 표준화: 실내, 자연광/LED, 30-50cm 거리, 정면 응시
- 이중 맹검: rPPG 분석자가 진단 상태를 모르는 상태에서 분석
- rPPG-ECG 동시 측정 서브셋 (n=50): 기술 검증용 gold standard

**분석 단계**:
- 다중 비교 보정 (Bonferroni / FDR)
- 교란변수 보정 회귀분석 (연령, BMI, 피부 유형, 스마트폰 기종)
- Bootstrap 95% CI for AUC
- TRIPOD 체크리스트 준수 (예측 모델 보고 표준)

### 8.3 윤리적 고려사항

- IRB 승인 필수 (다기관 공동 IRB)
- 동의서: 얼굴 영상 수집 목적, 보관 기간, 삭제 절차 명시
- 데이터 보호: GDPR/개인정보보호법 준수; 비식별화; 암호화 저장
- 취약 집단 보호: 정신건강 동반 시 적절한 의뢰 체계

---

## 참고문헌 (번호-논문 매핑)

[1] Mirzohreh et al., 2024. *Systematic Reviews*. DOI:10.1186/s13643-024-02617-x
[2] Yu et al., 2024. *Frontiers in Endocrinology*. DOI:10.3389/fendo.2023.1295061
[3] Sarathivarman et al., 2025. *JPBS*. DOI:10.4103/jpbs.jpbs_1295_25
[4] de Fatima Azevedo et al., 2026. *Scientific Reports*. DOI:10.1038/s41598-026-38731-0
[5] Bernal et al., 2025. *Clinical Endocrinology*. DOI:10.1111/cen.15163
[6] Moreira et al., 2021. *Women & Health*. DOI:10.1080/03630242.2021.1993423
[7] Hao et al., 2021. *Scientific Reports*. DOI:10.1038/s41598-020-79750-9
[8] Zeng et al., 2025. *Reproduction & Fertility*. DOI:10.1530/RAF-25-0039
[9] Moreira et al., 2024. *The Journal of Pain*. DOI:10.1016/j.jpain.2023.07.026
[10] rPPG HRV 리뷰, 2024. *Frontiers Bioeng & Biotech*. 추정 DOI:10.3389/fbioe.2024.1420100
[11] de Jager et al., 2026. *Sports Medicine*. DOI:10.1007/s40279-025-02388-y
[12] Heydari et al., 2025. *npj Digital Medicine*. DOI:10.1038/s41746-025-01517-1
[13] Huynh et al., 2022. *Diagnostics*. DOI:10.3390/diagnostics12081879
[14] Cell phone acne app, 2023. *Applied Intelligence*. DOI:10.1007/s10489-022-03774-z
[15] AcneAI, 2024. *MICCAI*. DOI:10.1007/978-3-031-72086-4_7
[16] Gao et al., 2025. *Scientific Reports*. DOI:10.1038/s41598-024-84670-z
[17] Oliveira et al., 2023. *Arch Dermatol Res*. DOI:10.1007/s00403-022-02495-0
[18] Dhanoo et al., 2024. *Diabetes Spectrum*. DOI:10.2337/ds23-0042
[19] Yousaf et al., 2021. *Comput Biol Med*. DOI:10.1016/j.compbiomed.2021.104392
[20] PatchBMI-Net, 2023. *arXiv*. arXiv:2311.18102
[21] Oztel et al., 2023. *Adv Intell Systems*. DOI:10.1002/aisy.202300211
[23] Wang et al., 2025. *La Radiologia Medica*. DOI:10.1007/s11547-025-02032-9
[24] Arabkermani et al., 2025. *JMIR*. DOI:10.2196/71118
[25] Pavic et al., 2025. *JMIR Human Factors*. DOI:10.2196/71859
[26] Zhang et al., 2026. *Frontiers in Endocrinology*. DOI:10.3389/fendo.2025.1735567
[27] Liu et al., 2025. *Scientific Reports*. DOI:10.1038/s41598-025-26606-9
[28] Kilungeja et al., 2025. *npj Women's Health*. DOI:10.1038/s44294-025-00078-8
[30] Moghimikandelousi et al., 2025. *Nature Communications*. DOI:10.1038/s41467-025-63501-3
[33] Sollee et al. (FibriCheck), 2025. *npj Digital Medicine*. DOI:10.1038/s41746-025-02059-2
[34] Cheng et al., 2024. *Bioengineering*. DOI:10.3390/bioengineering11030251
[35] Luo et al., 2019. *Circ Cardiovasc Imaging*. DOI:10.1161/CIRCIMAGING.119.008857

---

*본 연구 설계서는 2026-04-11 기준으로 작성되었으며, 검증된 문헌(28편 + 4편 부분 검증)에 기반합니다. #19(저자 수정: Yousaf et al.), #22(철회), #28(저자 수정: Agirsoy et al.)은 처리 지침에 따라 반영하였습니다.*
