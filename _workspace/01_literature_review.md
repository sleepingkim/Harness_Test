# 디지털 바이오마커 문헌 탐색 보고서

## 탐색 개요

- **탐색 전략**: 자궁내막증(Endometriosis) 및 다낭성난소증후군(PCOS) 예측을 위한 디지털 바이오마커 관련 선행연구를 체계적으로 탐색. 6개 핵심 키워드 조합으로 웹 기반 학술 검색 수행.
- **탐색 키워드**:
  - "endometriosis digital biomarker"
  - "PCOS wearable biomarker"
  - "menstrual cycle tracking AI prediction"
  - "HRV endometriosis / PCOS"
  - "period app data machine learning"
  - "PCOS prediction mobile health"
  - 보조 키워드: "wearable skin temperature menstrual cycle", "actigraphy endometriosis", "BBT PCOS ovulation detection", "digital phenotyping gynecological conditions"
- **사용 데이터베이스/소스**: PubMed, PMC, Nature (npj Digital Medicine, Scientific Reports), Frontiers, JMIR, BMC, ScienceDirect, MDPI, Wiley, Springer, ResearchGate, 학술 컨퍼런스 초록
- **탐색 기간**: 2015년 이후 연구 중심 (주요 발견은 2019-2025년에 집중)
- **탐색 일자**: 2026-04-06

---

## 자궁내막증(Endometriosis) 디지털 바이오마커

| 바이오마커 | 데이터 유형 | 측정 방법/출처 | 예측 정확도/효과 | 증거 수준 | 주요 출처 |
|---|---|---|---|---|---|
| 자가보고 증상 (골반통, 월경통, 요통 등) | 자가보고/설문 | Lucy 앱 (FEMaLe 연구), 온라인 설문 | XGBoost: 정확도 89%, F1=0.92; 다른 모델 AUC 0.94, 민감도 0.93, 특이도 0.95 | **Moderate** (다기관 n=10,000 목표) | Sivajohan et al., 2023, *Scientific Reports*; FEMaLe Study Protocol, 2024, *PLOS ONE* ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11081275/)) |
| 신체활동 및 수면 패턴 (액티그래피) | 웨어러블 센서 | 스마트워치 기반 가속도계, 4-6주 x 3주기 종단 추적 | 피로-신체활동 강한 음의 상관; 증상 중증도 궤적과 수면 장애 연관 확인 | **Limited** (n=68) | Hillman et al., 2025, *npj Digital Medicine* ([Nature](https://www.nature.com/articles/s41746-025-01629-8)) |
| 심박변이도 (HRV) | 웨어러블 센서 | PPG/ECG 기반 손목/가슴 웨어러블 | 미주신경 매개 HRV 저하 시 골반통 강도/불쾌감 증가; 하행 통증 억제 경로 효율성과 관련 | **Limited** (단면 연구) | Hellman et al., 2021, *Women & Health* ([PubMed](https://pubmed.ncbi.nlm.nih.gov/34719338/)) |
| 월경주기 패턴 (주기 길이, 변동성, 출혈 기간) | 앱 추적 데이터 | Clue, Flo 등 생리추적 앱 | 월경통/골반통이 가장 중요한 예측 인자로 확인; 주기 특성이 분류 보조 역할 | **Moderate** (대규모 앱 데이터) | Li et al., 2020, *npj Digital Medicine* ([Nature](https://www.nature.com/articles/s41746-020-0292-9)) |
| CA125 + NLR (호중구-림프구 비율) | 임상/생화학 | 혈액검사 + ML 분류 | Random Forest: 정확도 78.16%, 민감도 86.21%, AUC 0.85 | **Moderate** (후향적 코호트) | Yang et al., 2022, *Scientific Reports* ([Nature](https://www.nature.com/articles/s41598-021-04637-2)) |
| 유전자 발현 조합 (FOS, EPHX1, DLGAP5, PCSK5, ADAT1) | 유전체/전사체 | 조직 생검 + 마이크로어레이 | 테스트 데이터셋 AUC 0.836 | **Limited** (생물정보학 분석) | Zhang et al., 2023, *Frontiers in Genetics* ([Frontiers](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2023.1290036/full)) |
| 일일 통증 일지 (ESD/EIS) | 자가보고 (전자 다이어리) | 전자 증상 일지 (ESD: 일일, EIS: 주간) | 임상시험 결과변수로 활용; 예측 모델 내 핵심 입력 | **Moderate** (FDA PRO 개발 가이드라인 준수) | Deal et al., 2020, *Journal of Patient-Reported Outcomes* ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7028881/)) |
| 영상 기반 AI (초음파/MRI) | 임상 영상 | 딥러닝 (CNN) 기반 영상 분석 | 스코핑 리뷰에서 44.4% 예측, 47.2% 진단 연구 확인 | **Moderate** (체계적 문헌고찰) | Defined by Binda et al., 2022, *npj Digital Medicine* ([Nature](https://www.nature.com/articles/s41746-022-00638-1)) |

---

## PCOS 디지털 바이오마커

| 바이오마커 | 데이터 유형 | 측정 방법/출처 | 예측 정확도/효과 | 증거 수준 | 주요 출처 |
|---|---|---|---|---|---|
| 월경주기 불규칙성 (주기 길이, 변동성) | 앱 추적 데이터 | Clue 앱 (117M+ 자가추적 이벤트, 378,694명), Flo 앱 (1,579,819명) | PCOS 리스크 스코어 생성; 주기 길이 >35일이 주요 예측 인자 | **Moderate** (대규모 후향적 코호트) | Bull et al., 2019, *JMIR* ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7381001/)); Urteaga et al., 2020, *JMIR* ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7256750/)) |
| 기초체온 (BBT) / 손목 피부 온도 | 웨어러블 센서 | Oura Ring, Ava 팔찌, femSense 패치 등 | PCOS 환자에서 배란 시 온도 상승 지연 확인; 연속 모니터링 시 일일 진폭 차이 유의미 | **Limited** (소규모 전향적 연구) | Shilaih et al., 2018, *Biosensors and Bioelectronics* ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6265623/)); Webster et al., 2021, *JMIR* ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8238491/)) |
| 심박변이도 (HRV) | 웨어러블 센서 | PPG 기반 손목/반지 웨어러블 | PCOS군에서 SDNN, RMSSD, HF power 유의하게 감소 (부교감 저하, 교감 우세) | **Moderate** (후향적 단면, 다수 연구 일치) | Saranya et al., 2018, *Medicine* ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6160158/)); Jha et al., 2025, *JPBS* ([LWW](https://journals.lww.com/jpbs/fulltext/2025/10000/comparative_analysis_of_heart_rate_variability_in.9.aspx)) |
| 스마트 월경 건강 모니터링 패치 (SMHMP) | 웨어러블 센서 (다중 바이오마커) | 체온 + 간질액 호르몬 (에스트로겐, 프로게스테론) + ML | 배란 예측 정확도 92.3%; PCOS 진단자의 월경 불규칙성 87.5% 탐지 | **Exploratory** (파일럿) | ECEESPE 2025 Conference Abstract ([Endocrine Abstracts](https://www.endocrine-abstracts.org/ea/0110/ea0110rc16.5)) |
| EHR 기반 임상 데이터 + ML | 전자건강기록 | 대규모 EHR 데이터, XGBoost/Random Forest | XGBoost: 정확도 93.15%, 정밀도 0.92, 재현율 0.95; 평균 AUC 0.80-0.85 | **Moderate** (대규모 후향적) | Xie et al., 2024, *Frontiers in Endocrinology* ([Frontiers](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1298628/full)) |
| 모바일 앱 기반 자가보고 + 생활습관 추적 | 앱 자가보고 | 맞춤형 mHealth 앱 (설문 + 생활습관 데이터) | 경량 모델로 모바일 배포 가능; 웹 기반 도구 PCOS 위험도 평가 | **Limited** (파일럿/프로토타입) | Eamcon 2025 ([Atlantis Press](https://www.atlantis-press.com/proceedings/eamcon-25/126020756)); Empowering Early Detection, 2024, *Informatics in Medicine Unlocked* ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S235291482400056X)) |
| 초음파 영상 + ML | 임상 영상 | CNN/딥러닝 기반 난소 초음파 자동 분석 | 비침습 PCOS 진단 보조; 다양한 모델 비교 연구 진행 중 | **Limited** (소규모 검증) | Rahmawati et al., 2025, *Scientific Reports* ([Nature](https://www.nature.com/articles/s41598-025-10453-9)) |
| 자가보고 증상 (팽만감, 다모증, 과색소침착, 탈모 등) | 자가보고/앱 | 앱 기반 증상 설문 + 적응형 질문지 | Clue 앱의 PCOS 리스크 스코어: 62-75%의 PCOS 환자가 추적 기술이 진단에 도움이 되었다고 보고 | **Moderate** (설문 기반 대규모) | Healio, 2021 ([Healio](https://www.healio.com/news/endocrinology/20210511/menstrual-tracking-app-reveals-clues-of-broader-pcos-symptoms)) |

---

## 공통 바이오마커 (양 질환에 유의)

| 바이오마커 | 데이터 유형 | 측정 방법/출처 | 예측 정확도/효과 | 증거 수준 | 주요 출처 |
|---|---|---|---|---|---|
| 심박변이도 (HRV) | 웨어러블 센서 | PPG/ECG 기반 연속 측정 | 자궁내막증: 부교감 저하와 통증 강도 상관; PCOS: SDNN/RMSSD/HF 유의 감소. 양 질환 모두 자율신경계 불균형 확인 | **Moderate** | Hellman et al., 2021; Saranya et al., 2018; Jha et al., 2025 |
| 월경주기 패턴 (길이, 변동성, 규칙성) | 앱 추적 데이터 | Clue, Flo, 기타 생리추적 앱 | 주기 불규칙성이 양 질환의 조기 경고 신호; ML 모델의 핵심 입력 변수 | **Moderate** | Bull et al., 2019; Li et al., 2020; Urteaga et al., 2020 |
| 피부/기초 체온 | 웨어러블 센서 | Oura Ring, Ava, 기타 온도 센서 | 배란 탐지 민감도 62% (손목) vs 23% (구강 BBT); PCOS에서 배란 지연, 자궁내막증에서 주기 변동 패턴 관련 연구 진행 중 | **Limited** | Webster et al., 2021; Shilaih et al., 2018 |
| 수면 패턴 및 질 | 웨어러블 센서 | 액티그래피 (스마트워치/핏니스 밴드) | 자궁내막증: 수면 장애와 증상 중증도 상관; PCOS: 수면무호흡 유병률 증가와 관련 [지식 기반] | **Limited** | Hillman et al., 2025; [지식 기반] |
| 신체활동 수준 | 웨어러블 센서 | 가속도계, 만보기 | 자궁내막증: 낮은 활동량과 높은 피로/통증 연관; PCOS: 대사 지표와 활동량 간접 연관 [지식 기반] | **Limited** | Hillman et al., 2025 |
| 자가보고 통증/증상 중증도 | 자가보고 (앱/일지) | 전자 다이어리, 앱 내 증상 기록 | 양 질환 모두에서 ML 기반 분류의 핵심 입력; 특히 월경통, 골반통이 공통 예측 인자 | **Moderate** | Sivajohan et al., 2023; FEMaLe, 2024 |

---

## 데이터 계층별 분류

### Layer 1 -- 생리 추적 앱 데이터

| 데이터 항목 | 관련 질환 | 데이터 가용성 | 주요 앱/플랫폼 | 비고 |
|---|---|---|---|---|
| 월경주기 길이 및 변동성 | PCOS, 자궁내막증 | **높음** (상용 앱) | Clue, Flo, Apple Health, Natural Cycles | Clue: 117M+ 이벤트, Flo: 1.5M+ 사용자 코호트 보유 |
| 출혈 기간 및 양 | PCOS, 자궁내막증 | **높음** (상용 앱) | Clue, Flo | 과다월경/과소월경 패턴 분석 가능 |
| 증상 동반 기록 (통증, 기분, 에너지) | 자궁내막증, PCOS | **중간** (사용자 입력 의존) | Clue, Flo, Phendo | 입력 완결성이 사용자마다 크게 다름 |
| 배란 예측 (앱 알고리즘) | PCOS | **높음** (상용 앱) | Clue, Flo, OvuSense | 불규칙 주기 시 정확도 제한적 |

### Layer 2 -- 웨어러블 센서

| 데이터 항목 | 관련 질환 | 데이터 가용성 | 주요 기기 | 비고 |
|---|---|---|---|---|
| 연속 피부/체온 | PCOS, 자궁내막증 | **중간** (상용 기기) | Oura Ring, Ava 팔찌, Apple Watch, femSense | 배란 탐지에 유용; PCOS 환자에서 패턴 차이 확인 |
| 심박수 및 HRV | PCOS, 자궁내막증 | **중간-높음** (상용 기기) | Oura Ring, Apple Watch, Garmin, Whoop | 자율신경계 불균형 반영; 양 질환에서 변화 확인 |
| 액티그래피 (활동/수면) | 자궁내막증 | **중간-높음** (상용 기기) | Apple Watch, Fitbit, Garmin | 피로/통증 간접 측정; 종단 연구에서 검증 |
| 호흡수 | 간접 관련 | **중간** (상용 기기) | Oura Ring, Whoop, Garmin | 월경주기 변화 반영 가능성; 독립적 연구 부족 |
| 간질액 호르몬 분석 | PCOS | **낮음** (연구 전용) | SMHMP (실험적 패치) | 에스트로겐/프로게스테론 비침습 측정; 파일럿 단계 |

### Layer 3 -- 자가보고/증상 일지

| 데이터 항목 | 관련 질환 | 데이터 가용성 | 주요 도구 | 비고 |
|---|---|---|---|---|
| 골반통/월경통 일일 점수 | 자궁내막증 | **높음** (앱/전자일지) | ESD (Endometriosis Symptom Diary), Phendo, 일반 앱 | FDA PRO 가이드라인 준수 도구 존재 |
| 성교통, 배변통, 배뇨통 | 자궁내막증 | **중간** (민감 정보로 입력률 낮음) | ESD, 연구 전용 설문 | ML 모델에서 중요 예측 인자이나 수집 어려움 |
| 팽만감, 다모증, 여드름, 탈모 | PCOS | **중간** (상용 앱) | Clue, Flo, 맞춤형 앱 | Clue의 적응형 질문지에서 PCOS 리스크 스코어 산출 |
| 피로도 | 자궁내막증, PCOS | **중간** (사용자 입력 의존) | 다수 건강 앱 | 액티그래피와 병행 시 객관화 가능 |
| 기분/스트레스 | PCOS, 자궁내막증 | **중간** (사용자 입력 의존) | Clue, Flo, 정신건강 앱 | HRV와 결합 시 자율신경 스트레스 반응 측정 가능 |
| 생활습관 (식이, 운동, 수면 시간) | PCOS | **낮음-중간** | mHealth 앱 프로토타입 | 대사 건강 연관; 연구 프로토타입 수준 |

### Layer 4 -- 임상/생화학 (참고용)

| 데이터 항목 | 관련 질환 | 데이터 가용성 | 측정 방법 | 비고 |
|---|---|---|---|---|
| CA125 | 자궁내막증 | **낮음** (병원 전용) | 혈액검사 | NLR과 결합 시 RF 모델 AUC 0.85 |
| 호르몬 패널 (LH, FSH, 테스토스테론, DHEA-S) | PCOS | **낮음** (병원 전용) | 혈액검사 | Rotterdam 기준 필수 항목; 디지털 도구와 결합 연구 필요 |
| 초음파 영상 (난소) | PCOS, 자궁내막증 | **낮음** (병원 전용) | 질식 초음파 + AI 분석 | CNN 기반 자동 분석 연구 진행 중 |
| 유전자 발현 프로파일 | 자궁내막증 | **매우 낮음** (연구 전용) | 조직 생검 + 마이크로어레이 | 5-유전자 조합 AUC 0.836; 임상 활용까지 거리 있음 |
| 인슐린 저항성 지표 (HOMA-IR) | PCOS | **낮음** (병원 전용) | 혈액검사 | 교감 과활성과 상관; 웨어러블 대리지표 연구 필요 |

---

## 데이터 갭 분석

### 연구가 부족하거나 탐색되지 않은 영역

1. **자궁내막증 특이적 웨어러블 연구 부족**: 웨어러블 기기가 자궁내막증 환자 집단에서 직접 평가된 연구가 극히 드묾. 대부분의 웨어러블 연구는 건강한 여성의 월경주기 추적에 초점. 자궁내막증 관련 종단 액티그래피 연구는 Hillman et al. (2025)이 최초 대규모 사례.

2. **PCOS에서의 연속 체온/HRV 종단 연구 부족**: PCOS 환자에서 웨어러블 기기를 장기간 사용하여 체온 및 HRV 변화를 추적한 전향적 코호트 연구가 거의 없음. 기존 HRV 연구는 단면 설계가 대부분.

3. **두 질환의 동시 예측 모델 부재**: 자궁내막증과 PCOS를 동시에 감별/예측하는 통합 디지털 바이오마커 모델이 보고되지 않음. 공통 바이오마커(HRV, 주기 패턴)의 질환 감별 능력에 대한 연구 필요.

4. **비침습적 호르몬 모니터링 한계**: 간질액 기반 호르몬 측정(SMHMP 패치)은 파일럿 단계에 머물러 있으며, 상용화 가능한 비침습적 호르몬 웨어러블이 부재.

5. **다양한 인종/민족 집단에서의 검증 부족**: 대부분의 앱 기반 연구는 서구권 사용자 중심. 아시아, 아프리카 등 다양한 집단에서의 디지털 바이오마커 유효성 검증 연구 필요.

6. **호흡수, SpO2 등 추가 웨어러블 지표**: 상용 웨어러블이 측정 가능한 호흡수, 혈중 산소 포화도(SpO2) 등이 자궁내막증/PCOS와 관련되는지에 대한 연구가 전무.

7. **실시간 피드백/개입 연구 부족**: 디지털 바이오마커를 수집하는 것을 넘어, 실시간으로 사용자에게 위험 알림이나 개입을 제공하는 RCT가 거의 없음.

8. **데이터 품질 및 표준화**: 앱 기반 자가보고 데이터의 완결성 및 정확성 문제. 증상 기록의 표준화된 온톨로지 부재. 웨어러블 기기 간 센서 데이터 호환성 미확보.

9. **장기 예측 타당성**: 현재 대부분의 ML 모델은 횡단적 분류(진단 보조)에 초점. 증상 발현 전 사전 예측(presymptomatic prediction)이 가능한지에 대한 종단적 검증 미흡.

10. **경제성/접근성 평가**: 디지털 바이오마커 기반 조기 선별의 비용-효과 분석(cost-effectiveness) 연구가 발표되지 않음.

---

## 주요 참고문헌 목록

1. Sivajohan B et al. (2023). Self-report symptom-based endometriosis prediction using machine learning. *Scientific Reports*. [Nature](https://www.nature.com/articles/s41598-023-32761-8)
2. FEMaLe Study (2024). Machine learning for early diagnosis of endometriosis based on patient self-reported data. *PLOS ONE*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11081275/)
3. ESHRE/Lucy App (2025). Machine learning for endometriosis prediction: analyzing self-reported data. *Human Reproduction*. [Oxford Academic](https://academic.oup.com/humrep/article/40/Supplement_1/deaf097.641/8170210)
4. Li K et al. (2020). Learning endometriosis phenotypes from patient-generated data. *npj Digital Medicine*. [Nature](https://www.nature.com/articles/s41746-020-0292-9)
5. Hillman SC et al. (2025). Insights into endometriosis symptom trajectories using longitudinal actigraphy. *npj Digital Medicine*. [Nature](https://www.nature.com/articles/s41746-025-01629-8)
6. Binda MM et al. (2022). Clinical use of AI in endometriosis: a scoping review. *npj Digital Medicine*. [Nature](https://www.nature.com/articles/s41746-022-00638-1)
7. Dinsdale NL et al. (2023). Symptom tracking in endometriosis using digital technologies. *Med* (Cell Press). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10518625/)
8. Hellman KM et al. (2021). HRV and pain in endometriosis. *Women & Health*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/34719338/)
9. Yang H et al. (2022). ML algorithms as screening for endometriosis. *Scientific Reports*. [Nature](https://www.nature.com/articles/s41598-021-04637-2)
10. Bull JR et al. (2019). Menstrual cycle length in a global cohort. *JMIR*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7381001/)
11. Urteaga I et al. (2020). Identifying women at risk for PCOS using a mobile health app. *JMIR mHealth uHealth*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7256750/)
12. Saranya K et al. (2018). HRV characteristics in women with PCOS. *Medicine*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6160158/)
13. Jha S et al. (2025). Comparative analysis of HRV in women with and without PCOS. *JPBS*. [LWW](https://journals.lww.com/jpbs/fulltext/2025/10000/comparative_analysis_of_heart_rate_variability_in.9.aspx)
14. Xie J et al. (2024). Predicting PCOS with ML from EHR. *Frontiers in Endocrinology*. [Frontiers](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1298628/full)
15. Webster DE et al. (2021). Wrist skin temperature accuracy for ovulation detection. *JMIR*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8238491/)
16. Shilaih M et al. (2018). Modern fertility awareness methods: wrist wearables. *Biosensors and Bioelectronics*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6265623/)
17. Gombert-Labedens M et al. (2024). Using wearable skin temperature data for menstrual cycle tracking. *Journal of Biological Rhythms*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11294004/)
18. Deal LS et al. (2020). ESD and EIS development and validation. *Journal of Patient-Reported Outcomes*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7028881/)
19. Li H et al. (2020). Characterizing physiological and symptomatic variation in menstrual cycles. *npj Digital Medicine*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7250828/)
20. Goodale BM et al. (2019). Wearable sensors reveal menses-driven changes and enable prediction of fertile window. *JMIR mHealth uHealth*. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6495289/)

---

*본 보고서는 2026-04-06 기준 웹 기반 학술 탐색 결과를 종합한 것입니다. 직접 원문 접근이 불가한 경우 [지식 기반] 태그를 표기하였습니다.*
