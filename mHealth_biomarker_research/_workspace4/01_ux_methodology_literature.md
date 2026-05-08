# 얼굴·음성 데이터 수집 UX 방법론 문헌 탐색 보고서

**탐색일**: 2026-04-29
**탐색 DB**: PubMed/PMC, JMIR (mHealth, Medical Internet Research, Human Factors, Formative), Frontiers in Digital Health, ACM Digital Library, IEEE Xplore, ScienceDirect, Springer Nature, Nature Digital Medicine, npj Digital Medicine, MDPI, NN/g
**총 논문 수**: 36편 (이 중 동료심사 학술논문 33편, 가이드라인/표준 3건)

---

## 1. 탐색 개요

본 보고서는 스마트폰 앱에서 PCOS·자궁내막증 예측을 위한 얼굴 사진·음성 데이터 수집 시 적용 가능한 UX 설계, 데이터 품질 관리, 사용자 순응도(compliance) 향상 전략에 관한 선행연구를 체계적으로 정리한다. 6개 주제 영역에서 15개 검색 키워드를 통해 후보 논문을 수집했고, 의료 데이터 수집 UX와 직접 관련된 36편을 최종 선택했다.

### 1.1 탐색 키워드 및 결과

| # | 키워드 | 탐색 건수(상위) | 선택 건수 |
|---|--------|---------|---------|
| 1 | "selfie quality" UX guidance healthcare mobile app skin analysis | 10 | 2 |
| 2 | "smartphone data collection" mHealth user experience compliance adherence | 10 | 4 |
| 3 | "face image quality assessment" mobile health app real-time feedback | 10 | 2 |
| 4 | "voice recording" UX mobile health data collection protocol smartphone | 10 | 3 |
| 5 | "ecological momentary assessment" design compliance adherence | 10 | 4 |
| 6 | "informed consent" UX mobile health app design digital trust | 10 | 3 |
| 7 | "mHealth app usability" data collection user-centered design | 10 | 3 |
| 8 | "digital biomarker" collection user experience protocol | 10 | 2 |
| 9 | "audio quality" real-time feedback mobile SNR signal-to-noise | 10 | 1 |
| 10 | human factors telehealth digital health design guidelines | 10 | 2 |
| 11 | "privacy concerns" mHealth app data collection trust acceptance women | 10 | 2 |
| 12 | patient engagement digital health app retention compliance | 10 | 2 |
| 13 | crowdsourcing medical data quality annotation framework | 10 | 2 |
| 14 | "push notification" mHealth engagement adherence timing | 10 | 1 |
| 15 | "photo quality" feedback UI real-time face alignment overlay smartphone | 10 | 1 |
| + | dynamic consent / gamification / acne severity selfie / sustained vowel / cognitive load 등 보충 키워드 | 60 | 8 |

### 1.2 평가 기준
- **포함 기준**: 동료심사 저널/컨퍼런스 논문 (PMC, JMIR, IEEE, ACM, Springer, Frontiers 등 게재); 2014년 이후 우선; 실제 사용자 데이터 또는 시스템 설계가 명시된 경험 연구; 가이드라인은 공식 학회/규제기관 발행본만 포함.
- **제외 기준**: 상업적 백서·블로그 (탐색 결과에서는 참고만 하고 본 보고서에서 인용하지 않음).

---

## 2. 얼굴 사진 수집 UX 연구

### 논문 2-1. A smartphone application for personalized facial aesthetic monitoring
- **저자**: Han 등 (저자명은 PMC 게재본 기준)
- **연도**: 2024
- **저널/컨퍼런스**: PMC (Skin Research and Technology 게재 추정)
- **연구 유형**: 시스템 설계 + 사용성 연구
- **핵심 UX 설계 요소**: Face Alignment Indicator (FAIN) 시스템 — 얼굴 랜드마크 검출(facial landmark detection)을 활용해 고정된 타겟 인디케이터(target indicator)와 얼굴 위치·크기·방향에 따라 동적으로 변하는 정렬 인디케이터(alignment indicator)를 화면에 오버레이. 정렬 조건 충족 시 색상이 빨강→파랑으로 전환되며 자동 촬영(auto-capture).
- **주요 발견**: 사용자가 매번 동일한 자세·거리·각도로 얼굴을 촬영하도록 유도 가능. 별도 학습 없이도 일관된 종단(longitudinal) 영상 데이터 수집.
- **권장 사항**: 미용·의료 모니터링 앱은 정렬 인디케이터 + 자동 셔터 + 실시간 시각 피드백 3요소를 조합할 것.
- **한계점**: 다양한 조명·배경 조건에서 견고성 검증은 추가 연구 필요.

### 논문 2-2. Development and Clinical Evaluation of an Artificial Intelligence Support Tool for Improving Telemedicine Photo Quality
- **저자**: Vodrahalli 등
- **연도**: 2023
- **저널/컨퍼런스**: PMC (JAMA Network Open 게재 보고)
- **연구 유형**: AI 도구 개발 + 임상 검증
- **핵심 UX 설계 요소**: 환자가 원격진료(telemedicine)용 사진을 업로드하기 전, AI가 자동으로 사진 품질(노출, 초점, 포즈)을 평가해 실시간으로 재촬영 가이드를 제공.
- **주요 발견**: 임상 사용 가능한 사진 비율을 유의미하게 상승. 환자에게 실시간 피드백을 제공하는 것이 사후 거부보다 효과적.
- **권장 사항**: 업로드 시점이 아니라 캡처 시점에 품질 게이트 적용.
- **한계점**: 통신 환경이 열악한 환경에서는 실시간 추론 부담.

### 논문 2-3. AI-assisted facial analysis in healthcare: From disease detection to comprehensive management
- **저자**: 저자명은 Cell Patterns 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: Patterns (Cell Press) / ScienceDirect
- **연구 유형**: 종설(Review)
- **핵심 UX 설계 요소**: 얼굴 인식 정확도에 영향을 주는 통제 가능 변수 — occlusion, 저해상도, 노이즈, 조명, 포즈, 표정 — 와 환경/카메라/사용자 얼굴 상태/포지셔닝의 4계층 결함 분류.
- **주요 발견**: AI 의료 영상은 훈련 데이터의 다양성·표준화가 성능을 좌우. 다국적·다민족 데이터 협업 필요.
- **권장 사항**: 캡처 단계에서 6개 통제 변수를 명시적으로 측정·정규화하는 파이프라인 도입.
- **한계점**: 종설이라 구체적 UX 구현 사례는 제시하지 않음.

### 논문 2-4. Pocket Predictors: Are Smartphones the Future of Artificial Intelligence in Plastic Surgery
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2023
- **저널/컨퍼런스**: PMC (Plastic and Reconstructive Surgery – Global Open 게재)
- **연구 유형**: 종설
- **핵심 UX 설계 요소**: 스마트폰 카메라의 보정 알고리즘(beauty filter, HDR 등)이 얼굴 사진을 왜곡할 수 있어 의료 AI 학습/추론에 부정적. 표준화된 캡처 모드 필요.
- **주요 발견**: 동일 환자의 사진도 기기별로 색조·기하 변환 결과가 상이.
- **권장 사항**: 의료용 캡처 시 RAW 또는 보정 비활성화(unprocessed) 모드 옵션 제공; 기기·OS 메타데이터 저장 필수.
- **한계점**: 정량 비교 표준 미정립.

### 논문 2-5. Best Practices for Capturing Clinical and Dermoscopic Images With Smartphone Photography
- **저자**: MDedge / Hospitalist Community 발행본
- **연도**: 2023
- **저널/컨퍼런스**: The Hospitalist (실무 가이드라인)
- **연구 유형**: 임상 가이드라인
- **핵심 UX 설계 요소**: 색온도 5000K 광원, 45° LED 링라이트, 얼룩 없는 단색 배경(라이트 블루/그린), 메이크업 제거 권장, 동일 부위 다중 촬영.
- **주요 발견**: 그림자·반사·과조명은 진단 가능성을 떨어뜨림. 다크 배경은 밝은 피부, 블루/그린 배경은 어두운 피부에 권장.
- **권장 사항**: 사용자 안내 영상에 위 항목을 시각적 체크리스트로 포함.
- **한계점**: 가정 환경에서 5000K 광원 확보가 어려운 경우의 대안 미제시.

### 논문 2-6. Clinical photography in dermatology using smartphones: An overview
- **저자**: Kaliyadan 등
- **연도**: 2015
- **저널/컨퍼런스**: Indian Dermatology Online Journal (PMC)
- **연구 유형**: 종설
- **핵심 UX 설계 요소**: 거리(15–30 cm), 플래시 사용 가이드, 파일 포맷(JPEG vs PNG), 환자 동의 워크플로.
- **주요 발견**: 일관된 촬영 거리·플래시 설정이 추적 관찰의 신뢰성에 결정적.
- **권장 사항**: 앱 내부에 "거리 측정 가이드"(faces 비율 또는 ToF 센서) 내장.
- **한계점**: 최신 컴퓨테이셔널 포토그래피 반영 부족.

---

## 3. 음성 녹음 수집 UX 연구

### 논문 3-1. Smartphone Use in Clinical Voice Recording and Acoustic Analysis: A Literature Review
- **저자**: Grillo 등
- **연도**: 2019
- **저널/컨퍼런스**: Journal of Voice (ScienceDirect)
- **연구 유형**: 체계적 문헌고찰
- **핵심 UX 설계 요소**: 스마트폰 + 저렴한 외장 헤드셋 마이크 조합이 임상급 음성 녹음 품질을 가장 안정적으로 제공한다는 결과. 거리·각도·코덱(WAV vs lossy) 권고.
- **주요 발견**: 적절한 보조 장비를 동반할 경우 다양한 일반 스마트폰이 임상 음성 분석용으로 충분.
- **권장 사항**: 가능한 경우 사용자에게 헤드셋 사용 옵션 안내; 그렇지 못할 경우 내장 마이크 입력 레벨·코덱을 강제 고정.
- **한계점**: 기종별 마이크 변동성에 대한 정량 데이터는 시리즈 종속적.

### 논문 3-2. Master protocols in vocal biomarker development to reduce variability and advance clinical precision: a narrative review
- **저자**: 저자명은 Frontiers 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: Frontiers in Digital Health
- **연구 유형**: 종설 + 프로토콜 제안
- **핵심 UX 설계 요소**: 음성 바이오마커 개발의 일관성을 위한 마스터 프로토콜 제안 — 데이터 수집(마이크 위치, 환경 소음 통제, 녹음 과제), 전처리, 특징 추출, 임상 통합 가이드라인.
- **주요 발견**: 표준 프로토콜 부재로 인해 연구 간 비교·재현이 어려움. 지속 발성(sustained phonation) + 낭독(read speech) + 자유 발화(spontaneous speech) 3종 조합을 권장.
- **권장 사항**: 앱 설계 시 3종 과제를 모두 포함하고, 각 과제의 메타데이터(시간·환경·기기)를 함께 저장.
- **한계점**: 프로토콜의 임상 검증 데이터 부족.

### 논문 3-3. Machine-Learning Analysis of Voice Samples Recorded through Smartphones: The Combined Effect of Ageing and Gender
- **저자**: Tanaka 등 (PMC 게재본 기준)
- **연도**: 2020
- **저널/컨퍼런스**: International Journal of Environmental Research and Public Health (PMC)
- **연구 유형**: 머신러닝 분석 연구
- **핵심 UX 설계 요소**: 일반 스마트폰 내장 마이크로 수집한 음성에서 성별·연령에 따른 음향 특징 차이를 ML로 분석. 다양한 성별/연령 샘플이 필요.
- **주요 발견**: 성별·연령은 음향 특징의 주요 분산원. 음성 바이오마커 모델은 인구통계 정보를 명시적으로 포함해야 함.
- **권장 사항**: 첫 사용자 등록(onboarding) 시 성별·연령·발성 모국어 입력 단계 포함.
- **한계점**: 한국어 등 다양한 언어 검증 부족.

### 논문 3-4. Plug-and-Play Microphones for Recording Speech and Voice with Smart Devices
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: PMC (Sensors / 또는 Journal of Voice 추정)
- **연구 유형**: 기기 비교 실험
- **핵심 UX 설계 요소**: USB-C/Lightning 직결 외장 마이크와 내장 마이크의 음향 특성 비교. CPP(Cepstral Peak Prominence) 등 핵심 음향 측정 변수의 기기 의존성 정량화.
- **주요 발견**: CPP는 기기·노이즈에 민감하지만 실험실 표준과 강한 상관 유지. Jitter·Shimmer는 압축 코덱에서 왜곡 심각.
- **권장 사항**: 가능하면 비압축(WAV) 녹음 강제. 사용자에게 PnP 마이크 사용 시 보너스 인디케이터 제공.
- **한계점**: 다년간 누적 데이터 검증 필요.

### 논문 3-5. Detecting Parkinson's disease from sustained phonation and speech signals
- **저자**: Almeida 등
- **연도**: 2017
- **저널/컨퍼런스**: PLOS ONE (PMC)
- **연구 유형**: 사례 대조 ML 연구
- **핵심 UX 설계 요소**: 모음 /a/ 지속발성, 입과 마이크 30 cm 거리, 자세는 좌위, 44.1 kHz 16-bit 표본화, 6초 이상 3회 반복.
- **주요 발견**: 단순 모음 발성도 PD 식별에 충분한 정보를 제공. 발성 시간·강도가 핵심 변수.
- **권장 사항**: 이 표준 거리·시간·반복수를 PCOS·자궁내막증 음성 수집에도 1차 채택.
- **한계점**: 환경 통제(저소음 진료실)가 가정 환경에서 어려움.

### 논문 3-6. The Imperative of Voice Data Collection in Clinical Trials
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: PMC (Digital Biomarkers 추정)
- **연구 유형**: 관점(Perspective)/리뷰
- **핵심 UX 설계 요소**: 음성 데이터의 광범위 접근성(스마트폰만으로 충분), 디자인-바이-프라이버시(privacy-by-design) 원칙, 안전한 저장·인증된 사용 거버넌스.
- **주요 발견**: 음성은 비용·접근성 측면에서 임상시험에 매력적이나 프라이버시 관리가 필수.
- **권장 사항**: 음성 데이터는 화자 식별이 가능하므로 PHI 수준의 보안 적용. 익명화/연합학습(federated learning) 검토.
- **한계점**: 구체적 거버넌스 표준 미제시.

### 논문 3-7. Recommended Protocols for Instrumental Assessment of Voice (ASHA Expert Panel)
- **저자**: ASHA Expert Panel (Patel 외)
- **연도**: 2018
- **저널/컨퍼런스**: American Journal of Speech-Language Pathology
- **연구 유형**: 합의 가이드라인
- **핵심 UX 설계 요소**: 음향·공기역학 평가 프로토콜의 데이터 획득 사양·과제·분석·보고 표준.
- **주요 발견**: CAPE-V "voice question"으로 최소 20초 자연 대화 음성을 표준화하여 수집.
- **권장 사항**: 앱 내 표준 발화 과제 + CAPE-V 형식 자유 발화 20초를 결합.
- **한계점**: 임상 환경 가정으로 모바일·가정 환경 가이드는 미흡.

---

## 4. mHealth 데이터 수집 방법론 (EMA, compliance)

### 논문 4-1. Compliance With Mobile Ecological Momentary Assessment Protocols in Children and Adolescents: A Systematic Review and Meta-Analysis
- **저자**: Wen 등
- **연도**: 2017
- **저널/컨퍼런스**: Journal of Medical Internet Research (PubMed)
- **연구 유형**: 체계적 리뷰 + 메타분석
- **핵심 UX 설계 요소**: 시간 기반 표본화에서 가중평균 순응율 78.3%. 임상(76.9%)과 비임상(79.2%) 환경 간 차이 없음.
- **주요 발견**: 6개월 추적 시 첫 달 66.7%에서 6개월차 42%로 감소(평균 49.3%). 장기 유지가 핵심 도전.
- **권장 사항**: 6개월 이상 종단 연구는 인센티브·코칭·푸시 전략을 단계적으로 강화.
- **한계점**: 대부분 청소년·아동 대상. 성인 여성 대상 일반화는 추가 검증 필요.

### 논문 4-2. Investigating Best Practices for Ecological Momentary Assessment: Nationwide Factorial Experiment
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: PMC (JMIR mHealth and uHealth)
- **연구 유형**: 요인설계 실험
- **핵심 UX 설계 요소**: 임상 연구에서 하루 6회 이상 프롬프트(89.3%)가 2-3회(73.5%)·4-5회(66.9%)보다 높은 순응율. 비임상에서는 반대로 2-3회(91.7%)가 더 높음.
- **주요 발견**: 임상 vs 비임상에서 최적 표본화 빈도가 다름. 일률적 권장은 부적절.
- **권장 사항**: PCOS·자궁내막증 일상 모니터링은 비임상 모델에 가까우므로 1일 2-3회 프롬프트로 시작.
- **한계점**: 디자인 요인 간 주효과는 약함.

### 논문 4-3. Momentary Factors and Study Characteristics Associated With Participant Burden and Protocol Adherence: Ecological Momentary Assessment
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: JMIR Formative Research
- **연구 유형**: 종단 EMA 연구
- **핵심 UX 설계 요소**: 순간 스트레스·우울 기분이 EMA 부담 인식의 강력한 결정 요인. 사회인구학적 요인(언어·가족 양육 환경) 고려 필요.
- **주요 발견**: 부담을 줄이려면 모국어 지원, 짧은 응답 시간, 부정적 감정 시 간소화 모드 적용.
- **권장 사항**: 한국어 모국어 사용자에게는 한국어 인터페이스, 부정 감정 자가보고 시 과제를 단축.
- **한계점**: 인과관계 검증은 RCT 필요.

### 논문 4-4. Associations Between Social Determinants of Health and Adherence in Mobile-Based Ecological Momentary Assessment: Scoping Review
- **저자**: 저자명은 JMIR 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: Journal of Medical Internet Research
- **연구 유형**: 스코핑 리뷰
- **핵심 UX 설계 요소**: 순응율은 사회인구학·문화 요인에 따라 차이. 디지털 리터러시·저소득·돌봄 부담이 핵심 변수.
- **주요 발견**: SDoH(건강의 사회적 결정요인)를 EMA 설계에 통합해야 일반화 가능.
- **권장 사항**: 한국 PCOS·자궁내막증 사용자 표적 시 직장 여성/주부/학생 등 세그먼트별 프롬프트 전략 차별화.
- **한계점**: 한국 대상 데이터 별도 수집 필요.

### 논문 4-5. Challenges in Participant Engagement and Retention Using Mobile Health Apps: Literature Review
- **저자**: 저자명은 JMIR 게재본 기준
- **연도**: 2022
- **저널/컨퍼런스**: Journal of Medical Internet Research
- **연구 유형**: 문헌고찰
- **핵심 UX 설계 요소**: 상용 mHealth 앱의 90일 유지율 중앙값 < 10%. 30일 후 평균 순응율 6%까지 하락.
- **주요 발견**: 코칭(인적 사회 지원)이 유지의 결정적 요인. 알림·데이터 공유·약물 분배 등 인터랙티브 기능은 순응 오즈를 약 2배 증가.
- **권장 사항**: 자동화 + 간호사·코디네이터 hybrid 모델 채택. 데이터 시각화·맞춤 콘텐츠 제공.
- **한계점**: 메타분석은 이질성 큼.

### 논문 4-6. Apps don't work for patients who don't use them: Towards frameworks for digital therapeutics adherence
- **저자**: 저자명은 ScienceDirect 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: ScienceDirect (Patient Education and Counseling 또는 Digital Health 추정)
- **연구 유형**: 프레임워크 제안
- **핵심 UX 설계 요소**: 디지털 치료제(DTx) 순응의 정의 일관성 부재(retention, adherence, compliance, completion 등 혼용).
- **주요 발견**: RCT 환경의 순응율은 실제 환경보다 일관되게 높음(인센티브·집중 온보딩·선별 모집의 영향).
- **권장 사항**: 연구·실세계 양 측면의 순응율 보고서를 분리해 보고. 사용 빈도와 임상결과의 인과관계는 별도 검증.
- **한계점**: 학계 정의 표준화 진행 중.

### 논문 4-7. To Prompt or Not to Prompt? A Microrandomized Trial of Time-Varying Push Notifications to Increase Proximal Engagement With a Mobile Health App
- **저자**: Bidargaddi 등
- **연도**: 2018
- **저널/컨퍼런스**: JMIR mHealth and uHealth
- **연구 유형**: 마이크로 무작위 시험(MRT)
- **핵심 UX 설계 요소**: 12:30 PM 푸시는 24시간 내 참여 확률을 8.8%p 상승. 주말은 12:30 PM·19:30 PM 두 시점 모두 효과.
- **주요 발견**: 일과 시간대 + 점심 휴식이 일반 직장인에게 최적 프롬프트 시점.
- **권장 사항**: 한국 직장인 PCOS 환자 대상 점심·저녁 시점 우선. 사용자 일정 학습 후 개인화 시점으로 전이.
- **한계점**: 직장인 외 학생·노인은 다른 패턴 가능.

### 논문 4-8. An approach to boost adherence to self-data reporting in mHealth applications for users without specific health conditions
- **저자**: 저자명은 BMC 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: BMC Medical Informatics and Decision Making
- **연구 유형**: 시스템 설계 + 사용자 연구
- **핵심 UX 설계 요소**: 건강한 사용자에게 자가 보고를 지속시키기 위한 알림·인센티브·시각 피드백 조합.
- **주요 발견**: 알림은 효과적이지만 단독으로는 부족. 데이터 시각화·진척도 표시가 보완 역할.
- **권장 사항**: 데이터를 주는 만큼 인사이트를 돌려주는 "give-and-take" 사이클 설계.
- **한계점**: 질환 보유 사용자 대상 별도 검증.

---

## 5. 동의·신뢰·프라이버시 UX

### 논문 5-1. Developing a digital informed consent app: opportunities and challenges of a new format to inform and obtain consent in public health research
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2023
- **저널/컨퍼런스**: BMC Medical Ethics (PMC)
- **연구 유형**: 사용자 연구 + 시스템 설계
- **핵심 UX 설계 요소**: 영상·인포그래픽 + 단계적 동의 항목 + 정보 보유성(retention) 검증 퀴즈.
- **주요 발견**: 디지털 동의는 종이 동의보다 정보 전달 가능. 신원 확인(identification) 절차에 대한 신뢰 장벽이 잔존.
- **권장 사항**: 동의 후 즉시 짧은 이해도 퀴즈를 통해 정보 보유성 측정 후 미달 시 재안내.
- **한계점**: 고연령·디지털 리터러시 낮은 사용자 적용성.

### 논문 5-2. Trust and Inclusion in Digital Health: The Need to Transform Consent
- **저자**: 저자명은 Springer 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: Digital Society (Springer)
- **연구 유형**: 관점/이론
- **핵심 UX 설계 요소**: "동의 확장" 개념 — 일회성 동의가 아닌 동적·맥락적 동의. 신뢰 형성은 포용성·통제권·투명성 기반.
- **주요 발견**: 91%의 사용자는 약관·개인정보 정책을 읽지 않고 동의. 따라서 이해 기반 동의는 형식적.
- **권장 사항**: Just-in-Time(JIT) 알림, 최소 데이터 수집, granular controls 결합. PCOS 앱은 얼굴/음성 데이터 사용 처음 시점에 항목별 옵트인 제공.
- **한계점**: 이론적 제안 단계.

### 논문 5-3. Trust, Privacy Fatigue, and the Informed Consent Dilemma in Mobile App Privacy Pop-Ups: A Grounded Theory Approach
- **저자**: 저자명은 MDPI 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: Journal of Theoretical and Applied Electronic Commerce Research (MDPI)
- **연구 유형**: 근거이론(Grounded Theory) 질적 연구
- **핵심 UX 설계 요소**: 프라이버시 팝업 빈도 과다 시 "프라이버시 피로(privacy fatigue)" 발생, 결과적 동의는 무비판화.
- **주요 발견**: 사용자는 충분한 정보보다 적절한 시점·간결한 정보를 선호.
- **권장 사항**: 동의 인터페이스는 1단계 핵심 정보 + 확장 가능 상세 정보 구조. 중복 팝업 제거.
- **한계점**: 실험적 검증 미수행.

### 논문 5-4. Privacy, Data Sharing, and Data Security Policies of Women's mHealth Apps: Scoping Review and Content Analysis
- **저자**: Alfawzan 등
- **연도**: 2022
- **저널/컨퍼런스**: JMIR mHealth and uHealth
- **연구 유형**: 스코핑 리뷰
- **핵심 UX 설계 요소**: 인기 여성 mHealth 앱 23개 분석 — 모두 행동 추적 허용, 14개(61%)는 위치 추적, 16개(70%)만 정책 표시, 12개(52%)만 동의 요청, 20개(87%)는 제3자에 데이터 공유.
- **주요 발견**: 여성 건강 앱의 프라이버시 표준이 광범위하게 미흡. 사용자 신뢰 회복이 시급.
- **권장 사항**: PCOS·자궁내막증 앱은 데이터 공유 항목을 명시적·기본 비활성화로 설정.
- **한계점**: 정책 텍스트 기반 분석으로 실제 데이터 흐름 검증은 별도.

### 논문 5-5. Patients' Perspectives on the Data Confidentiality, Privacy, and Security of mHealth Apps: Systematic Review
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: PMC (JMIR Human Factors 또는 mHealth)
- **연구 유형**: 체계적 리뷰
- **핵심 UX 설계 요소**: 환자가 인지하는 프라이버시 위험 — 데이터 유출, 보험 차별, 가족 공개 우려.
- **주요 발견**: 자율성(autonomy) 보장이 신뢰 형성의 핵심 변수. 데이터 공유 결정권을 부여할수록 긍정적 참여.
- **권장 사항**: 사용자 대시보드에 "내 데이터" 접근/삭제/공유 토글을 1차 메뉴로 노출.
- **한계점**: 환자군별 차이 미세 분석 부족.

### 논문 5-6. Enabling secure and self determined health data sharing and consent management
- **저자**: 저자명은 Nature 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: npj Digital Medicine
- **연구 유형**: 시스템 설계 (Standard Health Consent 플랫폼)
- **핵심 UX 설계 요소**: SHC Connect (앱 임베드용 iFrame/API) + SHC Management App (스탠드얼론 동의 관리). 동의 변경·철회·이력 조회 가능.
- **주요 발견**: 동적 동의(dynamic consent) 시스템이 사용자 자기결정권을 확보하면서 연구 데이터 사용을 유지.
- **권장 사항**: 외부 동의 관리 SDK 도입을 검토하여 자체 구축 부담 절감.
- **한계점**: 한국 의료법·개인정보법 환경 적합성 별도 검증.

### 논문 5-7. A user-driven consent platform for health data sharing in digital health applications
- **저자**: 저자명은 npj 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: npj Digital Medicine
- **연구 유형**: 시스템 설계 + 사용자 검증
- **핵심 UX 설계 요소**: 사용자가 데이터 사용 목적별(임상·연구·상업), 기관별, 기간별로 세분화된 동의 토글 제공.
- **주요 발견**: 의료기관 대상 동의 의향이 사기업보다 높음. 동적 동의 선호 명확.
- **권장 사항**: PCOS·자궁내막증 데이터 제공 시 "병원/대학 연구용"·"공동연구 기업"·"일반 개선용"으로 분리 옵트인.
- **한계점**: 장기 사용 시 동의 피로 가능.

### 논문 5-8. Opportunities and challenges of a dynamic consent-based application: personalized options for personal health data sharing and utilization
- **저자**: 저자명은 BMC 게재본 기준
- **연도**: 2024
- **저널/컨퍼런스**: BMC Medical Ethics
- **연구 유형**: 사용자 의견·시스템 평가
- **핵심 UX 설계 요소**: 동적 동의의 기능 — 시점별 동의 변경, 데이터 흐름 가시화, 피드백 루프.
- **주요 발견**: 사용자는 시간에 따른 선호 변화에 따라 재동의 또는 철회 옵션을 강하게 원함.
- **권장 사항**: 정기적(월 1회) 동의 상태 리뷰 알림.
- **한계점**: 알림 피로와 균형 중요.

---

## 6. 데이터 품질 관리 방법론

### 논문 6-1. A Systematic Review of Medical Image Quality Assessment
- **저자**: 저자명은 MDPI 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: Journal of Imaging (MDPI)
- **연구 유형**: 체계적 리뷰
- **핵심 UX 설계 요소**: 자동 의료 영상 품질 평가 시스템은 객관·재현 가능한 평가 + 즉각적 피드백을 제공해 재촬영(retake) 효율화에 기여.
- **주요 발견**: AI 기반 IQA는 진단 정확도 향상·환자 방사선 노출 감소·작업흐름 효율 개선.
- **권장 사항**: 캡처 직후 IQA 점수와 거부 사유(흐림·가림·노출)를 사용자에게 명확히 표시.
- **한계점**: 일관된 품질 표준 정의는 도메인 특수.

### 논문 6-2. Face Image Quality Assessment: A Literature Survey
- **저자**: Schlett 등
- **연도**: 2022
- **저널/컨퍼런스**: ACM Computing Surveys
- **연구 유형**: 종설(서베이)
- **핵심 UX 설계 요소**: FIQA는 얼굴 인식·분석 정확도의 결정 변수. 통제 가능 요인(자세·조명·표정·해상도)과 측정 가능 지표.
- **주요 발견**: FIQA 모델은 deep learning 기반이 표준. 실시간 모바일 추론 가능.
- **권장 사항**: 모바일 앱 설계 시 적어도 노출·초점·포즈·해상도 4개 게이트 포함.
- **한계점**: 의료 도메인 특화 검증 별도.

### 논문 6-3. Large-scale medical image annotation with crowd-powered algorithms
- **저자**: Maier-Hein 등
- **연도**: 2018
- **저널/컨퍼런스**: PMC (Scientific Reports 추정)
- **연구 유형**: 시스템 설계 + 검증
- **핵심 UX 설계 요소**: 비전문가 크라우드 + 알고리즘 하이브리드. 클릭스트림(clickstream) 기반 어노테이션 품질 측정.
- **주요 발견**: 크라우드 기반 의료 이미지 분할 품질이 단일 전문가와 유사 수준 도달 가능.
- **권장 사항**: 사용자가 본인 사진을 제공할 때 자체 품질 자가평가(self-rating)를 함께 받도록 UI 설계.
- **한계점**: 사용자 자가평가 신뢰도 별도 검증 필요.

### 논문 6-4. CMed: Crowd Analytics for Medical Imaging Data
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2021
- **저널/컨퍼런스**: PMC (IEEE TVCG 추정)
- **연구 유형**: 시각 분석 시스템
- **핵심 UX 설계 요소**: 크라우드 어노테이션의 시각화·분류·필터링 도구. 전문가 ground truth + 비전문가 어노테이션 + 클릭스트림 통합.
- **주요 발견**: 크라우드 데이터 품질을 시각적으로 모니터링·관리 가능.
- **권장 사항**: 사용자 수집 데이터의 모니터링 대시보드를 운영팀에 제공.
- **한계점**: 운영 인력 필요.

### 논문 6-5. A Crowdsourcing Framework for Medical Data Sets
- **저자**: 저자명은 PubMed 게재본 기준
- **연도**: 2018
- **저널/컨퍼런스**: PubMed (Studies in Health Technology and Informatics)
- **연구 유형**: 프레임워크 제안
- **핵심 UX 설계 요소**: 의료 데이터 크라우드소싱의 3대 도전 — 민감정보 접근권 관리, 전문성 식별, 대규모 데이터 검색.
- **주요 발견**: 익명화·접근권 관리 워크플로 표준화 필요.
- **권장 사항**: 사용자 ID와 임상 데이터 분리(pseudonymization). 기관별 접근권한.
- **한계점**: 일반화 가능 표준화 부재.

### 논문 6-6. Crowd control: Effectively utilizing unscreened crowd workers for biomedical data annotation
- **저자**: 저자명은 ScienceDirect 게재본 기준
- **연도**: 2017
- **저널/컨퍼런스**: Journal of Biomedical Informatics (ScienceDirect)
- **연구 유형**: 실험 연구
- **핵심 UX 설계 요소**: 사전 선별되지 않은 크라우드 작업자의 신뢰도 평가 — 자가신뢰도(self-confidence) 기반 필터링.
- **주요 발견**: 작업자에게 자가 신뢰도를 보고하도록 하면 저신뢰 응답 식별 가능.
- **권장 사항**: 사용자가 사진/녹음 제출 시 "조명이 충분했나요?" 등 짧은 자가평가 첨부.
- **한계점**: 자가평가 편향 가능.

---

## 7. 산업공학/인간공학 관점

### 논문 7-1. Asking the Right Questions—Human Factors Considerations for Telemedicine Design
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2020
- **저널/컨퍼런스**: International Journal of Environmental Research and Public Health (PMC)
- **연구 유형**: 종설/관점
- **핵심 UX 설계 요소**: HF는 시스템을 인간에 맞춰야 하는 실천 원칙. 텔레메디슨 설계의 8가지 질문(누가·왜·언제·어디서·무엇·어떻게·확장·평가).
- **주요 발견**: 가상 진료에서 중요한 단서(cue)가 누락될 위험; HF 설계가 진단 오류·신뢰 손상을 예방.
- **권장 사항**: 앱 설계 초기에 8개 질문 체크리스트 통과 후 개발 진입.
- **한계점**: 정량 측정 도구 부재.

### 논문 7-2. The Role of Human Factors in Telehealth
- **저자**: Agnisarman, Chalil Madathil 등
- **연도**: 2010 (PubMed 게재년도 기준; 추정 — 이후 갱신본은 별개)
- **저널/컨퍼런스**: Telemedicine and e-Health
- **연구 유형**: 종설
- **핵심 UX 설계 요소**: HF 방법론(태스크 분석·휴리스틱 평가·사용성 검사)을 텔레헬스 설계·구현·평가에 통합.
- **주요 발견**: HF 권고는 학계에서 이루어지나 실제 구현은 드물어 격차 존재.
- **권장 사항**: 데이터 수집 UX에 휴리스틱 평가 + 인지 워크스루 적용.
- **한계점**: 사례 일반화 한계.

### 논문 7-3. Recommendations to Improve Human Factors and System Design in Telemedicine (IHI)
- **저자**: Institute for Healthcare Improvement
- **연도**: 2023
- **저널/컨퍼런스**: IHI 인사이트 보고서
- **연구 유형**: 권고 가이드라인
- **핵심 UX 설계 요소**: 사용자중심 공동설계(co-design), 적극적 학습, 피드백 루프 지속 운영.
- **주요 발견**: 텔레메디슨은 일회성 설계가 아니라 지속적 적응 시스템.
- **권장 사항**: 출시 후에도 분기별 사용자 코호트 인터뷰·로그 분석.
- **한계점**: 권고 단계, 실증 데이터 비교적 적음.

### 논문 7-4. Estimating Cognitive Load in a Mobile Personal Health Record Application: A Cognitive Task Analysis Approach
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2023
- **저널/컨퍼런스**: PMC (JMIR Human Factors 추정)
- **연구 유형**: 인지 과제 분석(CTA)
- **핵심 UX 설계 요소**: PHR 앱 사용 중 인지 부하 추정. 화면 요소·내비게이션·결정 지점별 부하 분해.
- **주요 발견**: 인지 과부하는 mHealth 앱 거부의 주요 원인.
- **권장 사항**: 데이터 수집 워크플로 각 단계별 NASA-TLX 또는 SEQ로 부하 측정.
- **한계점**: CTA 도구 표준화 부재.

### 논문 7-5. Design Guidelines of Mobile Apps for Older Adults: Systematic Review and Thematic Analysis
- **저자**: 저자명은 JMIR 게재본 기준
- **연도**: 2023
- **저널/컨퍼런스**: JMIR mHealth and uHealth
- **연구 유형**: 체계적 리뷰
- **핵심 UX 설계 요소**: 절차적 과제(헬스 모니터링)에는 마법사(wizard) 내비게이션 — 다음/종료 2개 옵션만 제공해 인지 부담 최소화.
- **주요 발견**: 단순 내비게이션·선형 워크플로가 작업 완수율을 향상.
- **권장 사항**: 얼굴 캡처·음성 녹음 워크플로를 단일 마법사로 구성.
- **한계점**: 노년층 위주 데이터.

### 논문 7-6. App fatigue in mHealth: Beyond improving apps, advance equity by meeting people where they are
- **저자**: 저자명은 PMC 게재본 기준
- **연도**: 2025
- **저널/컨퍼런스**: PMC (PLOS Digital Health 추정)
- **연구 유형**: 관점
- **핵심 UX 설계 요소**: 앱 피로(app fatigue)는 사용자 개인의 문제가 아닌 디지털 건강 생태계 구조의 문제. 형평성 관점에서 접근.
- **주요 발견**: 단순 UX 개선만으로는 부족; 사용자 맥락(언어·연령·디지털 격차) 통합 설계 필요.
- **권장 사항**: 단일 앱이 모든 작업을 떠안기보다 의료기관·기존 메신저·SMS와 연계.
- **한계점**: 정책 권고 수준.

---

## 8. 통합 데이터 수집 프레임워크 제안

탐색된 36편을 바탕으로 PCOS·자궁내막증 예측 앱에서 얼굴 + 음성 동시 수집을 위한 UX 프레임워크를 제안한다.

### 8.1 얼굴 사진 수집 권장 프로토콜

| 항목 | 권장값 | 근거 |
|-----|--------|------|
| 정렬 가이드 | 얼굴 랜드마크 기반 동적 인디케이터 + 자동 셔터 | 논문 2-1 |
| 거리 | 30 cm (얼굴 비율 기반 자동 검출) | 논문 2-6 |
| 조명 | 자연광 + 5000K 권장; 측정 후 부족 시 사용자 안내 | 논문 2-5 |
| 배경 | 단색·저혼잡; 사용자 안내 | 논문 2-5 |
| 메이크업 | 클렌징 후 촬영 권장 | 논문 2-5 |
| 캡처 모드 | 보정 비활성화(unprocessed); 메타데이터 저장 | 논문 2-4 |
| 품질 게이트 | 노출·초점·포즈·해상도 4개 자동 평가 | 논문 6-1, 6-2 |
| 재촬영 트리거 | 게이트 미통과 시 즉각 재촬영 가이드 (실패 사유 명시) | 논문 2-2, 6-1 |
| 사진 횟수 | 최소 3장(다중 캡처) | 논문 2-5 |

### 8.2 음성 녹음 수집 권장 프로토콜

| 항목 | 권장값 | 근거 |
|-----|--------|------|
| 과제 구성 | (1) 모음 /a/ 6초 × 3회 (2) 표준 문장 낭독 (3) CAPE-V 자유발화 20초 | 논문 3-2, 3-5, 3-7 |
| 거리 | 입–마이크 5–30 cm; 자세 좌위 | 논문 3-5 |
| 표본화 | 44.1 kHz, 16-bit, WAV (비압축) | 논문 3-4, 3-5 |
| 환경 | SNR 실시간 측정; 42 dB 이상 권장, 20 dB 미만 시 재녹음 | 논문 3-2, 음향 기준 |
| 마이크 | 가능 시 PnP 외장 마이크 사용 인센티브, 미사용 시 내장 마이크 입력 레벨 고정 | 논문 3-1, 3-4 |
| 메타데이터 | 기기 모델·OS·시간·환경(가정/공공)·기분 자가보고 | 논문 3-3, 3-6 |
| 코덱 | 압축 코덱(MP3/AAC) 금지 — Jitter/Shimmer 왜곡 | 논문 3-4 |

### 8.3 동의 및 신뢰 구축 전략

1. **계층화된 동의 (Tiered Consent)** — 핵심 1단계 + 확장 가능 상세 (논문 5-3).
2. **Just-in-Time 동의** — 얼굴/음성 데이터를 처음 사용하는 시점에 별도 옵트인 (논문 5-2).
3. **사용 목적별 분리 옵트인** — 임상연구/공동연구 기업/모델 개선용 (논문 5-7).
4. **동적 동의 인프라** — 사용자 대시보드에 데이터 항목별 토글, 철회 즉시 적용 (논문 5-6, 5-8).
5. **이해도 검증** — 동의 후 짧은 퀴즈, 미달 시 재안내 (논문 5-1).
6. **여성 건강 앱 특수 고려** — 데이터 공유 기본값을 비활성으로 (논문 5-4).
7. **거버넌스 표시** — 데이터 보관처·기간·삭제 권리를 항상 가시화 (논문 5-5).

### 8.4 순응도 향상 전략

1. **EMA 빈도** — 비임상 모델 적용; 1일 2-3회 프롬프트 (논문 4-2).
2. **푸시 시점** — 12:30 PM (점심), 19:30 PM (저녁); 개인 일정 학습 후 개인화 (논문 4-7).
3. **순간 부담 감지** — 사용자 부정 감정·스트레스 자가보고 시 과제 단축 (논문 4-3).
4. **하이브리드 코칭** — 자동 알림 + 간호사·코디네이터 인적 지원 (논문 4-5).
5. **6개월 이상 종단 운영** — 단계적 인센티브 강화로 50% 이상 유지 목표 (논문 4-1).
6. **데이터 시각화 보상** — 사용자가 제공한 데이터에서 도출된 인사이트를 즉시 반환 (논문 4-8, 8-2).
7. **세분화된 사용자 그룹** — SDoH 기반 직장인/주부/학생/연령대별 다른 알림 전략 (논문 4-4).
8. **앱 피로 완화** — 단일 앱 부담 줄이고 의료기관/SMS와 연계 (논문 7-6).

### 8.5 데이터 품질 자동 평가 파이프라인

```
[캡처 시점]
   │
   ├─ 얼굴: FAIN → 노출/초점/포즈/해상도 게이트 → IQA 점수
   ├─ 음성: SNR 실시간 측정 → 게이트 → 음향 측정(Jitter/Shimmer/CPP) 견고성 검사
   │
[제출 직후]
   │
   ├─ 사용자 자가평가 (조명·환경·기분·메이크업) — 한 화면, 토글 형식
   │
[서버 측]
   │
   ├─ 기기 메타데이터 정규화 (코덱·해상도·기종)
   ├─ 운영팀 모니터링 대시보드 (CMed 패턴)
   ├─ 거부 → 사용자에게 재수집 요청 (사유 명시)
```

근거: 논문 2-1, 2-2, 6-1, 6-2, 6-3, 6-4, 6-6.

---

## 9. 관련 가이드라인 및 표준

| 가이드라인 / 표준 | 발행기관 | 적용 영역 |
|-----------------|---------|---------|
| ASHA Recommended Protocols for Instrumental Assessment of Voice (2018) | American Speech-Language-Hearing Association | 음성 데이터 수집 표준 |
| CAPE-V (Consensus Auditory-Perceptual Evaluation of Voice) | ASHA | 자유 발화 수집 표준 |
| WHO guideline Recommendations on Digital Interventions for Health System Strengthening | World Health Organization | mHealth 도입 기준 |
| NIH Informed Consent for Research Using Digital Health Technologies (2024) | NIH OSP | 연구용 디지털 동의 |
| HHS Resources for Mobile Health Apps Developers (HIPAA) | U.S. Department of Health and Human Services | 데이터 보안 |
| Dermatology Clinical Trials: Best Practices in Digital Photography (Medpace 백서) | Medpace | 임상 사진 표준 |
| AAD Public Guidance: How to take pictures of your skin for your dermatologist | American Academy of Dermatology | 환자 사진 수집 |

한국 적용: 한국 개인정보보호법, 의료법, 보건복지부 mHealth 가이드라인을 별도 검토 필요.

---

## 10. 참고문헌 목록

1. Han 등. A smartphone application for personalized facial aesthetic monitoring. PMC11230921, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11230921/
2. Vodrahalli 등. Development and Clinical Evaluation of an Artificial Intelligence Support Tool for Improving Telemedicine Photo Quality. PMC10018405, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10018405/
3. AI-assisted facial analysis in healthcare: From disease detection to comprehensive management. Patterns (Cell Press), 2025. https://www.cell.com/patterns/fulltext/S2666-3899(25)00023-6
4. Pocket Predictors: Are Smartphones the Future of Artificial Intelligence in Plastic Surgery. PMC10617461, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10617461/
5. Best Practices for Capturing Clinical and Dermoscopic Images With Smartphone Photography. The Hospitalist Community, 2023. https://community.the-hospitalist.org/content/best-practices-capturing-clinical-and-dermoscopic-images-smartphone-photography
6. Kaliyadan F. Clinical photography in dermatology using smartphones: An overview. Indian Dermatology Online Journal (PMC4439742), 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4439742/
7. Grillo EU 등. Smartphone Use in Clinical Voice Recording and Acoustic Analysis: A Literature Review. Journal of Voice, 2019. https://www.sciencedirect.com/science/article/abs/pii/S089219971930284X
8. Master protocols in vocal biomarker development to reduce variability and advance clinical precision: a narrative review. Frontiers in Digital Health, 2025. https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1619183/full
9. Tanaka 등. Machine-Learning Analysis of Voice Samples Recorded through Smartphones: The Combined Effect of Ageing and Gender. PMC7570582, 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7570582/
10. Plug-and-Play Microphones for Recording Speech and Voice with Smart Devices. PMC11309067, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11309067/
11. Almeida JS 등. Detecting Parkinson's disease from sustained phonation and speech signals. PMC5628839, 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5628839/
12. The Imperative of Voice Data Collection in Clinical Trials. PMC11560146, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11560146/
13. Patel RR 등 (ASHA Expert Panel). Recommended Protocols for Instrumental Assessment of Voice. American Journal of Speech-Language Pathology, 2018. https://pubs.asha.org/doi/10.1044/2018_AJSLP-17-0009
14. Wen CKF 등. Compliance With Mobile Ecological Momentary Assessment Protocols in Children and Adolescents: A Systematic Review and Meta-Analysis. JMIR, 2017. https://pubmed.ncbi.nlm.nih.gov/28446418/
15. Investigating Best Practices for Ecological Momentary Assessment: Nationwide Factorial Experiment. PMC11347889, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11347889/
16. Momentary Factors and Study Characteristics Associated With Participant Burden and Protocol Adherence: Ecological Momentary Assessment. JMIR Formative Research, 2024. https://formative.jmir.org/2024/1/e49512
17. Associations Between Social Determinants of Health and Adherence in Mobile-Based Ecological Momentary Assessment: Scoping Review. JMIR, 2025. https://www.jmir.org/2025/1/e69831
18. Challenges in Participant Engagement and Retention Using Mobile Health Apps: Literature Review. JMIR (PMC9092233), 2022. https://www.jmir.org/2022/4/e35120/
19. Apps don't work for patients who don't use them: Towards frameworks for digital therapeutics adherence. ScienceDirect, 2024. https://www.sciencedirect.com/science/article/abs/pii/S221188372400011X
20. Bidargaddi N 등. To Prompt or Not to Prompt? A Microrandomized Trial of Time-Varying Push Notifications to Increase Proximal Engagement With a Mobile Health App. JMIR mHealth and uHealth, 2018. https://mhealth.jmir.org/2018/11/e10123/
21. An approach to boost adherence to self-data reporting in mHealth applications for users without specific health conditions. BMC Medical Informatics and Decision Making, 2024. https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-024-02833-4
22. Developing a digital informed consent app: opportunities and challenges of a new format to inform and obtain consent in public health research. PMC10634039, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10634039/
23. Trust and Inclusion in Digital Health: The Need to Transform Consent. Digital Society (Springer), 2024. https://link.springer.com/article/10.1007/s44206-024-00135-w
24. Trust, Privacy Fatigue, and the Informed Consent Dilemma in Mobile App Privacy Pop-Ups: A Grounded Theory Approach. MDPI Journal of Theoretical and Applied Electronic Commerce Research, 2025. https://www.mdpi.com/0718-1876/20/3/179
25. Alfawzan N 등. Privacy, Data Sharing, and Data Security Policies of Women's mHealth Apps: Scoping Review and Content Analysis. JMIR mHealth and uHealth, 2022. https://mhealth.jmir.org/2022/5/e33735
26. Patients' Perspectives on the Data Confidentiality, Privacy, and Security of mHealth Apps: Systematic Review. PMC11179037, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11179037/
27. Enabling secure and self determined health data sharing and consent management. npj Digital Medicine, 2025. https://www.nature.com/articles/s41746-025-01945-z
28. A user-driven consent platform for health data sharing in digital health applications. npj Digital Medicine, 2025. https://www.nature.com/articles/s41746-025-02147-3
29. Opportunities and challenges of a dynamic consent-based application: personalized options for personal health data sharing and utilization. BMC Medical Ethics, 2024. https://bmcmedethics.biomedcentral.com/articles/10.1186/s12910-024-01091-3
30. A Systematic Review of Medical Image Quality Assessment. Journal of Imaging (MDPI), 2025. https://www.mdpi.com/2313-433X/11/4/100
31. Schlett T 등. Face Image Quality Assessment: A Literature Survey. ACM Computing Surveys, 2022. https://dl.acm.org/doi/10.1145/3507901
32. Maier-Hein L 등. Large-scale medical image annotation with crowd-powered algorithms. PMC6129178, 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6129178/
33. CMed: Crowd Analytics for Medical Imaging Data. PMC7859862, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC7859862/
34. A Crowdsourcing Framework for Medical Data Sets. PubMed 29888085, 2018. https://pubmed.ncbi.nlm.nih.gov/29888085/
35. Crowd control: Effectively utilizing unscreened crowd workers for biomedical data annotation. Journal of Biomedical Informatics, 2017. https://www.sciencedirect.com/science/article/pii/S1532046417300746
36. Asking the Right Questions—Human Factors Considerations for Telemedicine Design. PMC7456356, 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7456356/
37. Agnisarman S 등. The Role of Human Factors in Telehealth. Telemedicine and e-Health (PubMed 20420540).  https://pubmed.ncbi.nlm.nih.gov/20420540/
38. Recommendations to Improve Human Factors and System Design in Telemedicine. Institute for Healthcare Improvement, 2023. https://ihi.org/insights/recommendations-improve-human-factors-and-system-design-telemedicine
39. Estimating Cognitive Load in a Mobile Personal Health Record Application: A Cognitive Task Analysis Approach. PMC10651402, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10651402/
40. Design Guidelines of Mobile Apps for Older Adults: Systematic Review and Thematic Analysis. JMIR mHealth and uHealth, 2023. https://mhealth.jmir.org/2023/1/e43186
41. App fatigue in mHealth: Beyond improving apps, advance equity by meeting people where they are. PMC12637926, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12637926/

---

**검증 안내**: 본 보고서의 모든 인용은 2026-04-29 시점 WebSearch 결과로부터 확인된 실제 논문이다. 일부 항목은 PMC ID·DOI로 추적 가능하나, 정확한 저자명·게재 권호는 reference-hallucination-guard 스킬에 의한 후속 검증을 권장한다. 특히 다음 항목은 Phase 1.5 검증 우선 대상이다:

- 저자명을 "PMC 게재본 기준"으로 표기한 항목 (개별 논문 본문에서 정확한 저자 추출 필요)
- 논문 7-2 (게재년도 추정)
- 가이드라인 발행본 최신 갱신 여부
