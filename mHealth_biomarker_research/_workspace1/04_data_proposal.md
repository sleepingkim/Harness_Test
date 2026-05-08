# 디지털 바이오마커 기반 자궁내막증·PCOS 조기 예측 공동연구 제안서

> **문서 버전**: v1.0  
> **작성일**: 2026-04-06  
> **문서 성격**: 데이터 제공 업체 대상 공동연구 제안서 (내부 검토용 초안)  
> **대상 업체**: 생리 추적 앱 (Clue, Flo 등), 웨어러블 기기 제조사 (Oura, Apple, Garmin, Fitbit 등)

---

## 1. 연구 배경 및 필요성

### 1-1. 자궁내막증과 PCOS의 사회적 부담

자궁내막증(Endometriosis)과 다낭성난소증후군(PCOS)은 가임기 여성에게 가장 광범위한 영향을 미치는 두 가지 부인과 질환이다.

**자궁내막증**은 전 세계 가임기 여성의 약 10%(약 1억 9천만 명)에게 영향을 미치며, 만성 골반통, 월경통, 불임의 주요 원인이다. 가장 심각한 문제는 **진단 지연**이다. 증상 발현부터 확정 진단까지 평균 **7-10년**이 소요되며, 이 기간 동안 환자는 반복적인 응급실 방문, 부적절한 치료, 삶의 질 저하를 경험한다. 확정 진단에 복강경 수술이 필요한 침습적 특성이 지연의 핵심 원인이다.

**PCOS**는 가임기 여성의 약 6-13%에게 영향을 미치며, 배란 장애, 안드로겐 과다, 대사 이상(인슐린 저항성, 제2형 당뇨 위험 증가)을 동반한다. Rotterdam 진단 기준이 혈액검사와 초음파를 요구하므로, 의료 접근성이 낮은 환경에서는 진단이 지연되거나 누락된다. 특히 비만이 없는 PCOS(lean PCOS)는 임상 증상이 비전형적이어서 간과되기 쉽다.

양 질환 모두 **조기 발견이 예후를 결정적으로 개선**하지만, 현재의 진단 경로는 환자의 자발적 병원 방문과 침습적 검사에 의존하고 있어 구조적 한계가 존재한다.

### 1-2. 디지털 바이오마커 기반 조기 예측의 가능성

최근 5년간 디지털 건강 기술의 발전으로 **생리 추적 앱**과 **소비자용 웨어러블 기기**가 대규모 인구의 여성 건강 데이터를 수동적으로 수집하고 있다. Clue 앱은 1억 1,700만 건 이상의 자가 추적 이벤트를, Flo 앱은 157만 명 이상의 사용자 코호트를 보유하고 있으며 [10, 11], Oura Ring과 Apple Watch는 심박변이도(HRV), 피부 온도, 활동량을 24시간 연속 측정한다.

이러한 데이터를 머신러닝(ML)/인공지능(AI)으로 분석하여 질환을 예측하는 연구가 이미 의미 있는 성과를 보이고 있다:

- **자궁내막증**: 앱 기반 자가보고 증상 데이터로 XGBoost 모델이 정확도 89%, F1=0.92를 달성 [1]. 다른 연구에서는 AUC 0.94, 민감도 0.93, 특이도 0.95가 보고됨 [2].
- **PCOS**: 월경주기 추적 데이터에서 주기 길이 >35일이 주요 예측 인자로 확인되었고 [10, 11], EHR 기반 ML 모델은 XGBoost 정확도 93.15%를 달성 [14].
- **웨어러블 기반 종단 연구**: Hillman et al. (2025)은 스마트워치 기반 4-6주 액티그래피로 자궁내막증 증상 궤적과 활동/수면 패턴의 강한 상관을 확인 [5].

이는 **일상적으로 수집되는 디지털 데이터만으로도 침습적 검사를 대체하는 조기 선별이 가능**함을 시사한다.

### 1-3. 공동연구의 의의

본 연구는 데이터 제공 업체와 AI 연구팀의 **상호보완적 강점**을 결합하는 공동연구를 제안한다.

**데이터 제공 업체의 강점:**
- 수십만~수백만 규모의 실세계 사용자 데이터 보유
- 종단적(longitudinal) 데이터 수집 인프라 운영 중
- 사용자 인터페이스 및 데이터 수집 모듈 개발 역량

**AI 연구팀의 강점:**
- 디지털 바이오마커 발굴 및 ML 모델 개발 전문성
- 임상 검증 네트워크 및 연구 설계 역량
- 학술 출판 및 규제 과학(regulatory science) 경험

이 공동연구를 통해 업체는 **자사 데이터의 의학적 가치를 객관적으로 입증**할 수 있으며, 이는 제품 차별화, 사용자 신뢰도 향상, 그리고 디지털 치료제(DTx)/디지털 헬스 시장에서의 경쟁 우위로 직결된다. 연구 성과는 업체의 앱/기기에 "AI 기반 건강 인사이트" 기능으로 환원될 수 있어, **연구 투자가 곧 제품 혁신으로 이어지는 구조**이다.

---

## 2. 연구 목표

### 2-1. 주요 목표

**자궁내막증과 PCOS의 조기 예측을 위한 AI 기반 다중 바이오마커 모델 개발**

- 생리 추적 앱 데이터, 웨어러블 센서 데이터, 자가보고 증상 데이터를 통합하여 자궁내막증과 PCOS 각각의 위험도를 예측하는 머신러닝 모델을 개발한다.
- 목표 성능: AUC >= 0.90, 민감도 >= 0.85, 특이도 >= 0.85 (기존 최고 성과인 자가보고 단독 AUC 0.94 [1]를 다중 모달 입력으로 재현 또는 초과).
- 두 질환을 동시에 감별하는 **통합 분류 모델**(자궁내막증 vs. PCOS vs. 정상)을 최초로 개발한다. 현재까지 이러한 통합 모델은 보고된 바 없다.

### 2-2. 세부 목표

1. **유의미한 디지털 바이오마커 발굴 및 검증**: 문헌 기반 Known 바이오마커 10종의 예측력을 실데이터로 검증하고, 신규 제안 바이오마커 7종의 탐색적 타당성을 평가한다.
2. **질환 감별 피처 발견**: 공통 바이오마커(HRV, 월경주기 패턴, 피부 온도 등)가 두 질환을 어떻게 다르게 반영하는지 분석하여, 감별 진단에 유용한 피처 조합을 식별한다.
3. **멀티모달 융합 모델 설계**: 앱 데이터(Layer 1) + 웨어러블 데이터(Layer 2) + 자가보고(Layer 3)의 최적 결합 방법론을 탐색한다.
4. **다양한 인구 집단에서의 타당성 평가**: 한국인 코호트를 포함하여 기존 서구권 중심 연구의 일반화 가능성을 검토한다.
5. **사전예측(Presymptomatic Prediction) 가능성 탐색**: 종단 데이터에서 진단 전 잠복기의 디지털 패턴 변화를 사후 분석한다.

---

## 3. 요청 데이터 명세

본 절에서는 요청 데이터를 두 범주로 구분한다. **핵심 요청 데이터(3-1)**는 문헌에서 이미 예측력이 검증된 Known 바이오마커 기반이며, **추가 제안 데이터(3-2)**는 병태생리학적 추론에 기반한 탐색적 신규 제안이다. 모든 데이터 항목에 근거 문헌 번호를 명시한다.

### 3-1. 핵심 요청 데이터 (Known 바이오마커 기반)

아래 10개 항목은 바이오마커 카탈로그 [02_biomarker_catalog.md]의 우선순위 Top 10에 해당하며, 4축 평가(근거 강도, 측정 가능성, AI 피처 적합성, 공동연구 실현성)에서 총점 14-19점(20점 만점)을 기록한 항목들이다.

#### (1) 월경주기 패턴 (총점 19/20) -- 최우선 요청

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 월경주기 길이(일), 주기 간 변동성(SD, CV), 규칙성 지수, 연속 6회 이상 주기 데이터 |
| **형식** | 시계열 (일 단위), CSV 또는 JSON. 각 주기의 시작일-종료일, 주기 길이(일) |
| **수집 기간** | 최소 6개월 (6주기 이상), 이상적으로 12-24개월 |
| **필요 이유** | 양 질환의 가장 강력한 단일 디지털 바이오마커. PCOS에서 주기 길이 >35일이 주요 예측 인자이며, 자궁내막증에서는 주기 내 증상 패턴과 결합 시 분류 보조 역할. ML 모델의 핵심 앵커 변수 |
| **근거** | Bull et al. (2019) -- Clue 앱 378,694명 코호트에서 주기 길이 분포 및 변동성 특성화 [10]; Urteaga et al. (2020) -- Flo 앱 데이터 기반 PCOS 리스크 스코어 생성 [11]; Li et al. (2020) -- 월경주기 특성이 자궁내막증 표현형 분류 보조 [4] |
| **요청 대상 업체** | Clue, Flo, Natural Cycles, Apple Health |

#### (2) 출혈 기간 및 양 (총점 17/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 출혈 일수, 일일 출혈량 등급 (light/medium/heavy/spotting), 부정출혈 유무 |
| **형식** | 시계열 (일 단위), 주기별 출혈 프로파일 |
| **수집 기간** | 최소 6개월 |
| **필요 이유** | 자궁내막증의 과다월경(heavy menstrual bleeding) 패턴과 PCOS의 과소월경/무월경 패턴이 방향성에서 대조적이어서 두 질환 감별에 특히 유용. 앱 기본 추적 항목으로 추가 비용 없이 기존 데이터 활용 가능 |
| **근거** | Bull et al. (2019) [10] -- 대규모 주기 데이터에서 출혈 패턴 분포 분석; Urteaga et al. (2020) [11] -- PCOS 리스크 스코어에 출혈 특성 포함 |
| **요청 대상 업체** | Clue, Flo |

#### (3) 심박변이도 -- HRV (총점 17/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 시간 도메인: SDNN, RMSSD, pNN50 (5분 에포크 단위). 주파수 도메인: LF power, HF power, LF/HF ratio (가용 시). 야간 수면 중 HRV 및 주간 안정 시 HRV 구분 |
| **형식** | 시계열 (5분 에포크 또는 일일 요약), CSV/Parquet |
| **수집 기간** | 최소 3개월 (3주기 이상), 이상적으로 6개월 |
| **필요 이유** | 양 질환에서 자율신경계 불균형이 확인됨. 자궁내막증에서는 미주신경 매개 HRV 저하가 골반통 강도/불쾌감 증가와 상관되며 [8], PCOS에서는 SDNN, RMSSD, HF power의 유의한 감소가 다수 연구에서 일관되게 보고됨 [12, 13]. 연속형 고해상도 시계열로 AI 모델 입력에 최적 |
| **근거** | Hellman et al. (2021) -- 자궁내막증 환자 HRV와 골반통 상관 [8]; Saranya et al. (2018) -- PCOS 환자 HRV 특성 [12]; Jha et al. (2025) -- PCOS vs. 정상 HRV 비교 분석 [13] |
| **요청 대상 업체** | Oura, Apple (HealthKit), Garmin, Whoop |

#### (4) 자가보고 증상 -- 골반통/월경통 (총점 16/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 일일 통증 점수 (NRS 0-10 또는 앱 자체 등급), 통증 유형 (경련통, 둔통, 찌르는 통증), 통증 위치 (하복부, 골반, 허리, 기타), 통증 지속 시간 |
| **형식** | 시계열 (일 단위), 주기별 통증 프로파일 |
| **수집 기간** | 최소 6개월 |
| **필요 이유** | 자궁내막증 ML 모델에서 가장 높은 예측력을 보이는 핵심 변수 (XGBoost F1=0.92, AUC 0.94 달성 [1]). FDA PRO 기반 표준화 도구(ESD)가 이미 존재하여 규제 관점에서도 강점 [18] |
| **근거** | Sivajohan et al. (2023) -- 자가보고 증상 기반 ML 분류 [1]; FEMaLe Study (2024) -- 다기관 n=10,000 목표 연구 [2]; Deal et al. (2020) -- ESD/EIS 개발 및 검증 [18] |
| **요청 대상 업체** | Clue, Flo, Phendo |

#### (5) 연속 피부/체온 (총점 16/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 야간 수면 중 연속 피부 온도 (1분 또는 5분 간격), 일일 평균/최소/최대 피부 온도, 온도 변화율 (일별 delta) |
| **형식** | 시계열 (분 단위 또는 일 단위 요약), CSV/Parquet |
| **수집 기간** | 최소 3개월 (3주기 이상) |
| **필요 이유** | 배란 탐지 민감도 62% (손목 기반, 구강 BBT 23% 대비 우수) [15]. PCOS 환자에서 배란 시 온도 상승 지연 패턴이 확인됨 [16]. 야간 연속 데이터로 월경주기 위상 추정이 가능하며, 무배란/지연배란의 객관적 지표 |
| **근거** | Webster et al. (2021) -- 손목 피부 온도 배란 탐지 정확도 [15]; Shilaih et al. (2018) -- 웨어러블 기반 체온 월경주기 추적 [16]; Gombert-Labedens et al. (2024) -- 피부 온도와 주기 위상 상관 [17] |
| **요청 대상 업체** | Oura, Ava, femSense, Apple (HealthKit) |

#### (6) 액티그래피 -- 신체활동/수면 (총점 16/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 일일 걸음 수, 활동 칼로리, 활동 강도 분포 (sedentary/light/moderate/vigorous 분 단위), 수면 시작/종료 시각, 수면 단계 (light/deep/REM), 수면 효율, 각성 횟수 |
| **형식** | 시계열 (1분 에포크 또는 일 단위 요약), CSV/Parquet |
| **수집 기간** | 최소 6개월 |
| **필요 이유** | 자궁내막증 환자에서 피로-활동의 강한 음의 상관, 증상 중증도 궤적과 수면 장애의 연관이 종단 연구로 확인됨 [5]. 동일 센서로 활동과 수면 데이터를 동시 추출 가능하여 추가 비용 없음. PCOS에서는 수면무호흡 유병률 증가와 대사 지표-활동량의 간접 연관이 보고됨 |
| **근거** | Hillman et al. (2025) -- 68명 자궁내막증 환자 4-6주 액티그래피 종단 연구 [5]; Li et al. (2020) -- 자궁내막증 표현형의 증상-활동 궤적 [4] |
| **요청 대상 업체** | Apple (HealthKit), Fitbit, Garmin, Oura |

#### (7) 배란 예측 데이터 (총점 16/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 앱 알고리즘의 배란 예측일, 가임 창(fertile window) 추정 기간, 실제 배란 확인 여부 (LH 검사 등 활용 시), 배란 미발생(anovulation) 표지 |
| **형식** | 이벤트 데이터 (날짜별), CSV |
| **수집 기간** | 최소 6개월 |
| **필요 이유** | PCOS 환자에서 무배란/지연배란이 핵심 진단 기준. 주기 길이 >35일이 PCOS의 주요 예측 인자로 확인됨 [10, 11]. 배란 예측 알고리즘의 출력값 자체가 배란 장애의 디지털 지표로 활용 가능 |
| **근거** | Bull et al. (2019) [10]; Urteaga et al. (2020) [11] |
| **요청 대상 업체** | Clue, Flo, OvuSense, Natural Cycles |

#### (8) 수면 패턴 및 질 (총점 15/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 총 수면 시간, 수면 효율 (%), 입면 잠복기(sleep onset latency), REM/deep/light 수면 비율, 야간 각성 횟수 및 시간, 수면 중 심박수/HRV (가용 시) |
| **형식** | 일 단위 요약 + 야간 시계열 (가용 시), CSV/Parquet |
| **수집 기간** | 최소 3개월 |
| **필요 이유** | 자궁내막증에서 수면 장애와 증상 중증도 간 상관 확인 [5]. PCOS에서 수면무호흡 유병률 증가. 액티그래피(항목 6)와 동일 센서에서 추출 가능하여 추가 비용 없이 양 질환 수면 패턴 분석 가능 |
| **근거** | Hillman et al. (2025) [5]; 지식 기반 -- PCOS 수면무호흡 연관 |
| **요청 대상 업체** | Oura, Apple (HealthKit), Fitbit, Whoop |

#### (9) 일일 통증 일지 -- ESD/EIS (총점 15/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | ESD(Endometriosis Symptom Diary) 형식의 일일 통증 기록: 골반통, 월경통, 성교통, 배변통, 배뇨통 각각의 일일 점수 + 종합 점수. EIS(Endometriosis Impact Scale) 형식의 주간 삶의 질 영향 평가 |
| **형식** | 일 단위 + 주 단위 요약, 표준 PRO 형식 |
| **수집 기간** | 최소 3개월 |
| **필요 이유** | FDA PRO(Patient-Reported Outcome) 가이드라인을 준수하여 개발된 표준화 도구. 임상시험 결과변수로 활용된 이력이 있어, 향후 규제 제출 시 데이터의 규제 수용성을 높임 |
| **근거** | Deal et al. (2020) -- ESD/EIS 개발 및 검증 [18] |
| **요청 대상 업체** | Phendo, ESD 개발팀, Clue/Flo (증상 기록 모듈) |

#### (10) 증상 동반 기록 -- 통증, 기분, 에너지 (총점 14/20)

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 일일 기분 (등급 또는 이모지), 에너지 수준, 소화 증상 (팽만감, 변비, 설사), 두통, 유방 통증, 피부 상태 (여드름, 건조) 등 앱 내 추적 가능한 동반 증상 전체 |
| **형식** | 일 단위, 앱 자체 형식 (범주형/등급형) |
| **수집 기간** | 최소 6개월 |
| **필요 이유** | Layer 1-2 데이터와 결합 시 ML 모델 성능 향상에 기여. Sivajohan et al. (2023)에서 자가보고 증상 데이터로 AUC 0.94 달성 시 통증 외 동반 증상이 보조 변수로 활용됨 [1] |
| **근거** | Sivajohan et al. (2023) [1]; Healio (2021) -- Clue PCOS 리스크 스코어에 팽만감, 다모증 등 동반 증상 포함 |
| **요청 대상 업체** | Clue, Flo |

#### 핵심 요청 데이터 종합표

| # | 데이터 항목 | Layer | 형식 | 수집 기간 | 근거 문헌 | 요청 대상 |
|---|---|---|---|---|---|---|
| 1 | 월경주기 패턴 | L1 | 일 단위 시계열 | 6-24개월 | [4, 10, 11] | Clue, Flo, Natural Cycles |
| 2 | 출혈 기간/양 | L1 | 일 단위 시계열 | 6개월+ | [10, 11] | Clue, Flo |
| 3 | HRV | L2 | 5분 에포크 시계열 | 3-6개월 | [8, 12, 13] | Oura, Apple, Garmin, Whoop |
| 4 | 골반통/월경통 | L3 | 일 단위 점수 | 6개월+ | [1, 2, 18] | Clue, Flo, Phendo |
| 5 | 연속 피부/체온 | L2 | 분/일 단위 시계열 | 3개월+ | [15, 16, 17] | Oura, Ava, femSense |
| 6 | 액티그래피 | L2 | 1분 에포크/일 요약 | 6개월+ | [4, 5] | Apple, Fitbit, Garmin, Oura |
| 7 | 배란 예측 데이터 | L1 | 이벤트 데이터 | 6개월+ | [10, 11] | Clue, Flo, OvuSense |
| 8 | 수면 패턴/질 | L2 | 일 단위 + 야간 시계열 | 3개월+ | [5] | Oura, Apple, Fitbit, Whoop |
| 9 | 통증 일지 (ESD/EIS) | L3 | PRO 표준 형식 | 3개월+ | [18] | Phendo, ESD 개발팀 |
| 10 | 증상 동반 기록 | L1/L3 | 일 단위 범주형 | 6개월+ | [1] | Clue, Flo |

### 3-2. 추가 제안 데이터 (Novel 바이오마커 기반)

아래 항목들은 병태생리학적 역방향 추론, 인접 질환 전이, 기술 역방향 추론에 기반한 **신규 제안**이다. 직접적인 자궁내막증/PCOS 예측 근거가 아직 부재하거나 제한적이므로 **탐색적 성격**임을 명시한다. 단, 기존 데이터의 재분석으로 파일럿이 가능한 항목(우선순위 1-4)은 추가 비용이 거의 없으며, 성공 시 기존 Known 마커의 한계를 보완하는 독립적 정보를 제공할 수 있다.

#### 우선순위 1: 기존 데이터 재분석으로 즉시 파일럿 가능

**(1) 생리 전 활동량 급감 패턴 -- PADS (Premenstrual Activity Drop Signature)**

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 월경 시작일 기준 전후 7일간의 일일 걸음 수, 활동 칼로리, 활동 강도 분포. 핵심 파생 피처: 생리 전 활동량 감소 기울기(slope), 감소 시작 시점, 최저점 깊이, 회복 시간 |
| **형식** | 액티그래피 데이터(항목 6)와 월경 시작일 데이터(항목 1)의 연동. 별도 수집 불필요 |
| **수집 기간** | 액티그래피 + 주기 데이터 6개월 이상 |
| **기대 가치** | 자궁내막증 환자에서 "활동량 급감(activity cliff)" 패턴이 건강한 여성 대비 감소 폭 더 크고, 시작이 더 빠르며(생리 3-5일 전부터), 회복이 느릴 것으로 예상. 원발성 월경통과의 감별, 중증도 추정에 독립적 정보 제공 |
| **탐색 수준** | 완전 신규 제안. 인접 근거: Hillman et al. (2025) 피로-활동 상관 확인 [5], 류마티스 관절염에서 flare 전 활동 감소 패턴 보고 |
| **업체 부담** | **최소** -- 기존 보유 데이터의 파생 변수 산출. 추가 수집/개발 불필요 |

**(2) 식후 심박수 반응 패턴 -- PHRR (Postprandial Heart Rate Response)**

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 연속 심박수 데이터에서 식사 시간대(자가보고 또는 식이 추적 앱 연동) 기준 식후 30-120분간의 심박수 상승 크기(delta HR), 피크 도달 시간, 기저선 회복 시간 |
| **형식** | HRV 데이터(항목 3)의 재분석 + 식사 시점 데이터 연동 |
| **수집 기간** | 심박수 연속 측정 + 식사 시점 기록 3개월 이상 |
| **기대 가치** | PCOS 환자 40-70%에서 동반되는 인슐린 저항성의 비침습 대리 지표. 혈액검사(HOMA-IR) 없이 대사 하위유형(metabolic phenotype)을 식별하여, 비만이 없는 PCOS(lean PCOS)에서도 감지 가능 |
| **탐색 수준** | 완전 신규 제안. 인접 근거: 제2형 당뇨병에서 식후 심박수 반응-인슐린 저항성 상관 확인 (Valensi et al., 2011) |
| **업체 부담** | **낮음** -- 심박수 데이터는 기존 보유. 식사 시점만 자가보고 또는 식이 앱 연동 필요 |

**(3) 일주기 리듬 안정성 지수 -- CRSI (Circadian Rhythm Stability Index)**

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 기존 웨어러블 데이터(가속도계, 피부 온도, 심박수)에서 파생: 수면-각성 중심점(midpoint), 일간 안정성(IS), 일내 변동성(IV), 활동 시작/종료 시각 SD, 체온 나디르 시각 안정성. 이들의 복합 지수 |
| **형식** | 항목 3, 5, 6 데이터의 재분석으로 산출. 별도 수집 불필요 |
| **수집 기간** | 연속 웨어러블 데이터 최소 4주, 이상적으로 3개월 |
| **기대 가치** | PCOS의 인슐린-코르티솔 일주기 리듬 교란, 자궁내막증의 만성 통증 기반 수면 구조 파괴를 "24시간 전체 생체리듬 안정성"이라는 상위 개념으로 정량화. 두 질환의 감별에도 기여 가능(PCOS: 대사 기반 리듬 교란 vs. 자궁내막증: 통증 기반 리듬 교란) |
| **탐색 수준** | 완전 신규 제안. 인접 근거: Simon et al. (2019) PCOS 일주기 리듬 교란-대사 악화 상관; 제2형 당뇨병 연구 IS/IV 지표 유용성 |
| **업체 부담** | **최소** -- 기존 보유 데이터의 파생 변수 산출 |

**(4) 진통제/약물 복용 패턴 시계열**

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 월경주기 내 진통제 복용 시작일(주기 몇 일째), 연속 복용 일수, 일 복용 횟수, 약물 종류(NSAIDs, 아세트아미노펜, 처방 진통제), 월별 총 복용량 추세 |
| **형식** | 이벤트 데이터 (날짜별), 앱 내 약물 기록 기능 데이터 |
| **수집 기간** | 최소 6개월 |
| **기대 가치** | 자궁내막증의 "조기 시작, 장기 지속" 진통제 패턴 vs. 원발성 월경통의 "월경 시작 시 단기 복용" 패턴의 감별. 진통제 에스컬레이션(NSAIDs에서 처방약으로)이 중증도 진행의 지표. 진단 전 잠복기(7-10년)에 축적된 패턴의 사후 분석 가능 |
| **탐색 수준** | 검증 미흡한 기존 마커. 데이터 자체는 Clue, Flo, Apple Health에서 수집 중이나 자궁내막증 예측 맥락의 시계열 분석은 미수행 |
| **업체 부담** | **낮음** -- 기존 약물 기록 기능 데이터 활용 |

#### 우선순위 2: 앱 모듈 추가 개발로 수집 가능

**(5) 음성 특성 기반 호르몬 상태 추정**

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 일일 음성 샘플(30초-1분)에서 추출: 기본 주파수(F0), 포먼트(F1-F4), 지터, 시머, HNR, MFCC |
| **형식** | 음향 특징 벡터 (일 단위), 원본 오디오는 비식별화 후 보관 |
| **수집 기간** | 최소 3개월 (3주기 이상) |
| **기대 가치** | PCOS 안드로겐 과다의 비침습 추적. 월경주기 내 호르몬 변동의 간접 평가. Known 마커(주기 패턴, HRV)와 독립적 정보 축(호르몬 상태) 제공 |
| **탐색 수준** | 검증 미흡 [탐색적]. 소규모 근거: Gugatschka et al. (2013) PCOS 환자 음성 변화; Pisanski et al. (2014) 배란기 음성 주파수 변화 |
| **업체 부담** | **중간** -- 앱 내 음성 녹음 모듈 개발 필요 |

**(6) 스마트폰 카메라 기반 안면 피부 상태 추적**

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 주 1-2회 안면 셀피에서 딥러닝 추출: 여드름 병변 수/분포, 다모증 정도, 피부 유분도, 안면 부종, 흑색극세포증 |
| **형식** | 피처 벡터 (주 1-2회), 원본 이미지는 비식별화 파이프라인 적용 후 보관 |
| **수집 기간** | 최소 3개월 |
| **기대 가치** | PCOS 안드로겐 과다 표현형을 혈액검사 없이 연속 추적. 자가보고(여드름/다모증 유무)의 이진 변수를 연속형 중증도 점수로 확장 |
| **탐색 수준** | 완전 신규 제안 [탐색적]. 인접 근거: 딥러닝 여드름 중증도 평가 피부과 전문의 수준 달성; Kosilek et al. (2015) 안면 AI 호르몬 이상 탐지 |
| **업체 부담** | **중간-높음** -- 촬영 모듈 + 비식별화 파이프라인 개발, IRB 승인 필요 |

#### 우선순위 3: 별도 인프라/파트너십 필요

**(7) 타이핑/터치스크린 상호작용 패턴**

| 항목 | 상세 |
|------|------|
| **데이터 항목** | 타이핑 속도(WPM), 키 간 간격, 오타율, 터치 압력, 스크롤 속도, 터치 정밀도 |
| **형식** | 시계열 (세션별/일 단위 요약) |
| **수집 기간** | 최소 3개월 |
| **기대 가치** | 자가보고 편향을 보완하는 수동적(passive) 통증 대리 지표. 진단 지연 기간 무의식적 행동 변화 패턴 포착 가능 |
| **탐색 수준** | 완전 신규 제안 [탐색적]. 인접 근거: 우울증에서 타이핑 패턴-PHQ-9 상관 (Zulueta et al., 2018); 파킨슨병 키 입력 역학 바이오마커 (Arora et al., 2015) |
| **업체 부담** | **높음** -- 키보드 SDK 또는 별도 앱 개발, 프라이버시 고강도 프로토콜 필요 |

#### 추가 제안 데이터 종합표

| # | 데이터 항목 | 대상 질환 | 제안 타입 | 수집 가능성 | 업체 부담 | 탐색 수준 |
|---|---|---|---|---|---|---|
| N1 | 생리 전 활동량 급감 패턴 (PADS) | 자궁내막증 | 완전 신규 | 높음 (기존 데이터) | 최소 | 인접 근거 |
| N2 | 식후 심박수 반응 패턴 (PHRR) | PCOS | 완전 신규 | 높음 (기존 데이터) | 낮음 | 인접 근거 |
| N3 | 일주기 리듬 안정성 지수 (CRSI) | 공통 | 완전 신규 | 높음 (기존 데이터) | 최소 | 인접 근거 |
| N4 | 진통제 복용 패턴 시계열 | 자궁내막증 | 검증 미흡 | 중간-높음 | 낮음 | 인접 근거 |
| N5 | 음성 기반 호르몬 추정 | PCOS | 검증 미흡 [탐색적] | 중간-높음 | 중간 | 소규모 연구 |
| N6 | 안면 피부 상태 추적 | PCOS | 완전 신규 [탐색적] | 중간 | 중간-높음 | 기술 근거 |
| N7 | 타이핑/터치 패턴 | 자궁내막증 | 완전 신규 [탐색적] | 중간 | 높음 | 인접 질환 전이 |

#### 멀티모달 조합 모델 제안

위의 Known 및 Novel 바이오마커를 조합한 두 가지 멀티모달 모델을 제안한다.

**자궁내막증 조기 탐지 복합 지수 (EEDC)**
- 구성: 월경주기 패턴(Known) + PADS(Novel) + HRV 주기 내 변동(Known) + 진통제 패턴(Novel) + 골반통 점수(Known)
- 기대: 기존 최고 성능(자가보고 단독 XGBoost F1=0.92)을 초과하며, 특히 통증이 경미한 초기 자궁내막증 사례에서 민감도 향상

**PCOS 대사-내분비 디지털 프로파일 (PMEDP)**
- 구성: 월경주기 패턴(Known) + PHRR(Novel) + CRSI(Novel) + 연속 피부 체온(Known) + 안면 피부 상태(Novel)
- 기대: 월경주기 단독 대비 특이도 향상, PCOS 네 가지 표현형(classic, ovulatory, non-hyperandrogenic, non-insulin resistant) 감별 가능

---

## 4. 데이터 활용 계획

### 4-1. 분석 방법론 개요

본 연구는 3단계 분석 파이프라인을 적용한다.

**1단계: 탐색적 분석 및 피처 엔지니어링**
- 각 바이오마커의 기술 통계, 분포 특성, 결측치 패턴 분석
- 시계열 데이터의 주기성(periodicity), 추세(trend), 변동성(variability) 피처 추출
- 월경주기 위상(follicular/ovulatory/luteal/menstrual)에 따른 층화 분석
- Novel 바이오마커(PADS, PHRR, CRSI 등)의 파생 변수 산출 및 탐색적 타당성 평가

**2단계: 예측 모델 개발**
- 단일 모달 모델: 각 Layer(L1, L2, L3)별 독립 모델 성능 평가
- 멀티모달 융합 모델: Early fusion (피처 연결) 및 Late fusion (모델 앙상블) 비교
- 알고리즘: Gradient Boosting (XGBoost, LightGBM), Random Forest, LSTM/Transformer (시계열), 그리고 해석 가능한 모델(SHAP 기반 피처 중요도 분석)
- 분류 목표: (a) 자궁내막증 vs. 정상, (b) PCOS vs. 정상, (c) 자궁내막증 vs. PCOS vs. 정상 (3-class)
- 교차 검증: 환자 단위(patient-level) K-fold 교차 검증, 시간적 분할(temporal split) 검증

**3단계: 검증 및 해석**
- 외부 검증: 학습 데이터와 독립적인 코호트에서 모델 성능 재현
- 서브그룹 분석: 연령, BMI, 인종/민족, 질환 중증도별 성능 평가
- 해석 가능성: SHAP values를 활용하여 각 바이오마커의 예측 기여도를 정량화하고, 임상적으로 해석 가능한 결과 제시
- 사전예측 분석: 진단 전 데이터에서 잠복기 패턴 변화의 사후 분석 (가용 시)

### 4-2. 개인정보 보호 방안

본 연구는 최고 수준의 데이터 보호 프로토콜을 적용한다.

**비식별화 (De-identification)**
- 모든 데이터는 업체 측에서 비식별화 처리 후 연구팀에 전달
- 직접 식별자(이름, 이메일, 기기 ID 등) 완전 제거
- 준식별자(생년월일, 지역 등)는 일반화(generalization) 처리 (예: 생년월일 -> 5세 단위 연령 구간)
- 안면 이미지 데이터(Novel 제안 6)는 피처 벡터만 전달하거나, 전달 시 얼굴 비식별화 처리(facial de-identification) 적용

**접근 통제 (Access Control)**
- 연구팀 내 데이터 접근 권한 최소 부여 원칙(need-to-know basis)
- 데이터 접근 로그 기록 및 주기적 감사(audit)
- 암호화된 저장소(AES-256)에 데이터 보관, 전송 시 TLS 1.3 이상 적용
- VPN/전용 네트워크를 통한 원격 분석 환경 제공 (데이터 외부 반출 금지)

**법적/윤리적 준수**
- 업체 소재국 및 연구팀 소재국의 개인정보보호법 준수 (GDPR, 개인정보보호법 등)
- 기관생명윤리위원회(IRB) 승인 후 연구 착수
- 데이터 사용 동의: 업체의 기존 사용자 동의 범위 확인 후, 필요 시 추가 동의 절차 설계
- 연구 결과 발표 시 개인 식별 불가능한 집계 통계만 공개

### 4-3. 데이터 보존 및 폐기 정책

- **보존 기간**: 연구 종료 후 3년 (학술 출판 검증 기간)
- **보존 형태**: 비식별화된 분석 데이터셋만 보존, 원본 데이터는 연구 종료 시 반환 또는 폐기
- **폐기 방법**: NIST SP 800-88 가이드라인에 따른 안전 삭제
- **데이터 소유권**: 원본 데이터의 소유권은 업체에 귀속. 파생 변수 및 분석 결과물의 소유권은 공동연구 계약에 따라 협의

---

## 5. 공동연구 기대 성과

### 5-1. 학술 성과

본 연구는 다음과 같은 학술 기여를 목표로 한다.

**논문 출판 (예상 3-5편)**
1. **주요 논문**: "멀티모달 디지털 바이오마커 기반 자궁내막증·PCOS 동시 예측 모델" -- 자궁내막증과 PCOS를 동시에 감별하는 통합 분류 모델은 현재까지 보고된 바 없어 **세계 최초** 수준의 연구. 목표 저널: npj Digital Medicine, The Lancet Digital Health, Nature Medicine
2. **Novel 바이오마커 검증 논문**: PADS, PHRR, CRSI 등 신규 제안 마커의 탐색적 타당성 검증. 목표 저널: JMIR mHealth and uHealth, Frontiers in Digital Health
3. **데이터 논문(Data Paper)**: 대규모 디지털 바이오마커 코호트 데이터셋 기술 및 공개(비식별화). 목표 저널: Scientific Data (Nature)
4. **방법론 논문**: 멀티모달 시계열 융합 방법론 및 월경주기 동기화(cycle-synchronized) 피처 엔지니어링 기법
5. **임상 해석 논문**: 디지털 바이오마커의 임상적 의의 및 조기 선별 가이드라인 제안

**학회 발표**
- ESHRE (European Society of Human Reproduction and Embryology)
- ASRM (American Society for Reproductive Medicine)
- IEEE EMBC (Engineering in Medicine and Biology Conference)
- AMIA (American Medical Informatics Association)

### 5-2. 실용적 성과 -- 업체를 위한 가치 제안

본 공동연구는 데이터 제공 업체에게 다음과 같은 **직접적 비즈니스 가치**를 제공한다.

**제품 차별화**
- 연구 성과를 업체 앱/기기에 "AI 건강 인사이트" 기능으로 통합 가능 (예: "자궁내막증 위험도 알림", "PCOS 스크리닝 리포트")
- 경쟁 앱/기기 대비 **임상 근거 기반(evidence-based)** 기능 제공으로 차별화
- 여성 건강 시장에서 의학적 신뢰도 확보

**사용자 참여 및 리텐션**
- 건강 인사이트 기능은 앱 사용 빈도와 장기 리텐션을 높이는 핵심 동기
- 자가보고 데이터 완결성 향상 (입력 동기 부여)

**시장 포지셔닝**
- 디지털 치료제(DTx) 및 FDA SaMD(Software as a Medical Device) 규제 환경에서의 선제적 포지셔닝
- B2B 가치: 보험사, 제약사, 의료기관과의 파트너십 기반 마련
- ESG/임팩트: 여성 건강 형평성(Health Equity) 기여에 대한 사회적 인정

**데이터 가치 입증**
- 자사 데이터가 의학 연구에 활용 가능하다는 **객관적 근거** 확보
- 학술 논문 출판으로 데이터 품질 및 규모의 공식적 인증
- 후속 연구 및 투자 유치 시 레퍼런스로 활용

### 5-3. 데이터 제공 업체 크레딧 및 공동저자 방침

- **공동저자**: 데이터 제공, 연구 설계 참여, 원고 검토에 기여한 업체 연구원은 ICMJE(International Committee of Medical Journal Editors) 기준에 따라 공동저자로 포함
- **기관 크레딧**: 모든 출판물에 데이터 제공 업체를 공동연구 기관으로 명시
- **감사의 글**: 데이터 인프라 제공 기여를 Acknowledgments에 기재
- **연구 결과 사전 공유**: 출판 전 업체에 결과를 사전 공유하여 검토 기회 제공
- **언론/마케팅 활용**: 출판된 연구 결과를 업체의 마케팅/PR에 활용할 수 있도록 상호 합의

---

## 6. 연구팀 소개

> [이 섹션은 실제 연구 책임자 정보로 대체해야 합니다]

| 역할 | 성명 | 소속 | 전문 분야 |
|------|------|------|----------|
| 연구 책임자 (PI) | [입력 필요] | [입력 필요] | 디지털 헬스 / AI / 여성 건강 |
| 공동 연구원 | [입력 필요] | [입력 필요] | 산부인과학 / 자궁내막증 |
| 공동 연구원 | [입력 필요] | [입력 필요] | 내분비학 / PCOS |
| 데이터 사이언티스트 | [입력 필요] | [입력 필요] | ML/AI / 시계열 분석 |
| 생명윤리 자문 | [입력 필요] | [입력 필요] | 연구 윤리 / 개인정보보호 |

**연구팀 역량 요약:**
- [연구팀의 관련 연구 이력, 출판 실적, 기존 협업 경험 등을 기술]

---

## 7. 일정 계획 (안)

| 단계 | 기간 | 주요 활동 | 산출물 |
|------|------|----------|--------|
| **Phase 0: 협약** | 0-2개월 | 공동연구 계약 체결, IRB 승인, 데이터 전달 프로토콜 합의 | MOU/협약서, IRB 승인서 |
| **Phase 1: 데이터 준비** | 2-4개월 | 비식별화 데이터 수령, 품질 검증, 탐색적 분석, 코호트 정의 | 데이터 품질 보고서, 코호트 프로파일 |
| **Phase 2: Known 마커 검증** | 4-8개월 | Top 10 Known 바이오마커의 단일 모달 모델 개발 및 검증 | Known 마커 성능 보고서, 중간 논문 초고 |
| **Phase 3: Novel 마커 탐색** | 6-10개월 | PADS, PHRR, CRSI 등 파생 변수 산출 및 탐색적 검증 | Novel 마커 타당성 보고서 |
| **Phase 4: 멀티모달 융합** | 8-12개월 | EEDC/PMEDP 멀티모달 모델 개발, 교차 검증 | 통합 모델 성능 보고서 |
| **Phase 5: 외부 검증** | 10-14개월 | 독립 코호트 검증, 서브그룹 분석, 해석 가능성 분석 | 외부 검증 보고서 |
| **Phase 6: 논문화** | 12-18개월 | 주요 논문 작성, 학회 발표, 업체 기능 통합 논의 | 논문 투고, 학회 발표, 기술 이전 논의 |

**총 소요 기간**: 약 18개월 (Phase 간 일부 병행 수행)

**마일스톤:**
- M1 (4개월): 데이터 수령 완료 및 품질 확인
- M2 (8개월): Known 마커 기반 단일 모달 모델 AUC >= 0.85 달성
- M3 (12개월): 멀티모달 융합 모델 AUC >= 0.90 달성
- M4 (15개월): 주요 논문 투고
- M5 (18개월): 연구 종료 및 업체 기능 통합 권고안 제출

---

## 8. 참고문헌

1. Sivajohan B et al. (2023). Self-report symptom-based endometriosis prediction using machine learning. *Scientific Reports*. https://www.nature.com/articles/s41598-023-32761-8
2. FEMaLe Study (2024). Machine learning for early diagnosis of endometriosis based on patient self-reported data. *PLOS ONE*. https://pmc.ncbi.nlm.nih.gov/articles/PMC11081275/
3. ESHRE/Lucy App (2025). Machine learning for endometriosis prediction: analyzing self-reported data. *Human Reproduction*. https://academic.oup.com/humrep/article/40/Supplement_1/deaf097.641/8170210
4. Li K et al. (2020). Learning endometriosis phenotypes from patient-generated data. *npj Digital Medicine*. https://www.nature.com/articles/s41746-020-0292-9
5. Hillman SC et al. (2025). Insights into endometriosis symptom trajectories using longitudinal actigraphy. *npj Digital Medicine*. https://www.nature.com/articles/s41746-025-01629-8
6. Binda MM et al. (2022). Clinical use of AI in endometriosis: a scoping review. *npj Digital Medicine*. https://www.nature.com/articles/s41746-022-00638-1
7. Dinsdale NL et al. (2023). Symptom tracking in endometriosis using digital technologies. *Med* (Cell Press). https://pmc.ncbi.nlm.nih.gov/articles/PMC10518625/
8. Hellman KM et al. (2021). HRV and pain in endometriosis. *Women & Health*. https://pubmed.ncbi.nlm.nih.gov/34719338/
9. Yang H et al. (2022). ML algorithms as screening for endometriosis. *Scientific Reports*. https://www.nature.com/articles/s41598-021-04637-2
10. Bull JR et al. (2019). Menstrual cycle length in a global cohort. *JMIR*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7381001/
11. Urteaga I et al. (2020). Identifying women at risk for PCOS using a mobile health app. *JMIR mHealth uHealth*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7256750/
12. Saranya K et al. (2018). HRV characteristics in women with PCOS. *Medicine*. https://pmc.ncbi.nlm.nih.gov/articles/PMC6160158/
13. Jha S et al. (2025). Comparative analysis of HRV in women with and without PCOS. *JPBS*. https://journals.lww.com/jpbs/fulltext/2025/10000/comparative_analysis_of_heart_rate_variability_in.9.aspx
14. Xie J et al. (2024). Predicting PCOS with ML from EHR. *Frontiers in Endocrinology*. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1298628/full
15. Webster DE et al. (2021). Wrist skin temperature accuracy for ovulation detection. *JMIR*. https://pmc.ncbi.nlm.nih.gov/articles/PMC8238491/
16. Shilaih M et al. (2018). Modern fertility awareness methods: wrist wearables. *Biosensors and Bioelectronics*. https://pmc.ncbi.nlm.nih.gov/articles/PMC6265623/
17. Gombert-Labedens M et al. (2024). Using wearable skin temperature data for menstrual cycle tracking. *Journal of Biological Rhythms*. https://pmc.ncbi.nlm.nih.gov/articles/PMC11294004/
18. Deal LS et al. (2020). ESD and EIS development and validation. *Journal of Patient-Reported Outcomes*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7028881/
19. Li H et al. (2020). Characterizing physiological and symptomatic variation in menstrual cycles. *npj Digital Medicine*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7250828/
20. Goodale BM et al. (2019). Wearable sensors reveal menses-driven changes and enable prediction of fertile window. *JMIR mHealth uHealth*. https://pmc.ncbi.nlm.nih.gov/articles/PMC6495289/

**Novel 바이오마커 제안 관련 추가 참고문헌:**

21. Valensi P et al. (2011). Postprandial heart rate response and insulin resistance. *Diabetes & Metabolism*. (PHRR 근거)
22. Zulueta J et al. (2018). Predicting mood disturbance severity from smartphone typing dynamics. *JMIR*. (타이핑 패턴 근거)
23. Arora S et al. (2015). Detecting and monitoring the symptoms of Parkinson's disease using smartphones. *Movement Disorders*. (키 입력 역학 근거)
24. Gugatschka M et al. (2013). Voice characteristics in women with PCOS. *Fertility and Sterility*. (음성-PCOS 근거)
25. Pisanski K et al. (2014). Voice pitch modulation across the menstrual cycle. *PLoS ONE*. (음성-월경주기 근거)
26. Simon SL et al. (2019). Circadian disruption and PCOS metabolic outcomes. *Sleep*. (CRSI 근거)
27. Stocker LJ et al. (2014). Shift work and reproductive outcomes. *International Journal of Occupational Medicine*. (일주기 리듬-생식 건강 근거)
28. Lipton RB et al. (2015). Medication overuse headache progression patterns. *Headache*. (진통제 패턴 근거)
29. Abitbol J et al. (1999). Voice changes in the premenstrual period. *Journal of Voice*. (음성-호르몬 근거)
30. Kosilek RP et al. (2015). Automatic face classification of Cushing's syndrome. *JCEM*. (안면 AI-호르몬 근거)

---

*본 제안서는 2026-04-06 기준으로 작성된 내부 검토용 초안입니다. 연구팀 정보(6절), 예산 계획 등은 최종본에서 보완이 필요합니다. 본 제안서의 모든 데이터 요청은 IRB 승인 및 데이터 사용 계약 체결을 전제로 합니다.*
