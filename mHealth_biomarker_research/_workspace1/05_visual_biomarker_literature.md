# 영상 이미지 기반 디지털 바이오마커 문헌 탐색

## 탐색 개요

### 목적
자궁내막증(Endometriosis)과 다낭성난소증후군(PCOS) 예측을 위한 **영상 및 이미지 기반 디지털 바이오마커**의 선행연구를 체계적으로 탐색하고, 스마트폰 카메라 및 컴퓨터 비전 기술을 활용한 비침습적 바이오마커의 가능성을 평가한다.

### 검색 전략
- **탐색 기간**: 2018~2025년
- **탐색 데이터베이스**: PubMed, Google Scholar, Semantic Scholar, arXiv, MDPI, Nature Digital Medicine, Frontiers
- **검색 키워드**: rPPG menstrual cycle, facial skin analysis PCOS acne, smartphone body composition, video gait analysis chronic pelvic pain, facial expression pain recognition, sleep video contactless monitoring, pupillometry PCOS autonomic dysfunction, thermal imaging endometriosis, digital phenotyping women health 등
- **포함 기준**: 영상/이미지/카메라 기반 측정, AI/ML 활용, 여성 건강 또는 자궁내막증/PCOS 관련성
- **제외 기준**: 초음파 영상(기존 임상 진단 도구), 순수 유전체학 연구, 약물 개발 연구

### 증거 수준 기준
| 등급 | 정의 | 기준 |
|------|------|------|
| Strong | 높은 수준의 근거 | 메타분석, 대규모 코호트, 임상 검증 완료 |
| Moderate | 중간 수준의 근거 | 소규모 임상 연구, 파일럿 검증, 복수 연구 존재 |
| Limited | 제한적 근거 | 단일 연구, 개념 증명 수준 |
| Exploratory | 탐색적 근거 | 직접 연구 부재, 인접 분야 기술 이전 추론 |

---

## 1. 얼굴 피부 분석 기반 바이오마커

### 1-1. 원격 광혈류측정(rPPG: Remote Photoplethysmography)

#### 기술 개요
rPPG는 일반 카메라(스마트폰 포함)로 촬영한 얼굴 영상에서 피부 아래 혈류량의 미세 변화를 감지하여 심박수, 심박변이도(HRV), 호흡수, SpO2 등을 비접촉으로 측정하는 기술이다. 피부 표면의 RGB 채널 변화가 혈액량 변동(blood volume pulse)을 반영하며, 딥러닝 모델(VGG-16, ResNet-50 등)을 통해 신호를 추출한다.

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 심박수(HR) | 스마트폰 카메라 rPPG | MAE 1-3 BPM (안정 시) | 양 질환 공통 (자율신경계 변화 감지) | Moderate | [Nature Comm. Med. 2024](https://www.nature.com/articles/s43856-024-00519-6) |
| HRV (RMSSD, SDNN) | 웨어러블 rPPG 연속 측정 | 황체기 HRV 4.65ms 감소, 안정시 심박수 2.73 BPM 증가 | PCOS (자율신경 이상), 자궁내막증 (통증-HRV 연관) | Strong | [Sports Med. 2025 Living Systematic Review](https://link.springer.com/article/10.1007/s40279-025-02388-y) |
| SpO2 | 스마트폰 카메라 (얼굴 영상) | MAE 5.00% SpO2 (CNN 기반), 저산소증 감지 79% | 제한적 (직접 관련성 낮음) | Limited | [npj Digital Med. 2022](https://www.nature.com/articles/s41746-022-00665-y) |

#### 자궁내막증/PCOS 적용 가능성 분석

**HRV와 생리주기 연동**: 프로게스테론 수치가 높은 황체기에 미주신경 매개 HRV(vagally-mediated HRV)가 유의하게 감소하며, 이는 프로게스테론과 강한 상관관계를 보인다 (r값 유의). 자연 배란 여성에서 RMSSD와 SDNN이 주기 초반에 높고 황체기에 감소하는 패턴이 확인되었다.

**PCOS 적용**: PCOS 환자는 자율신경계 기능 이상이 보고되며, HRV 패턴의 비정상적 변화가 진단 보조 지표가 될 수 있다. 정상 주기의 HRV 패턴과 무배란 주기의 HRV 패턴 차이를 rPPG로 감지할 가능성이 있다.

**자궁내막증 적용**: 만성 골반통으로 인한 교감신경 항진 상태가 HRV에 반영될 수 있으며, 통증 에피소드와 HRV 변화의 시간적 연관성을 추적할 수 있다.

**기술적 한계**: rPPG는 조명 변화와 움직임에 민감하며, HRV의 정밀 측정(ms 단위)을 위해서는 아직 접촉식 센서(PPG) 대비 정확도가 낮다. 그러나 2024-2025년 연구에서 딥러닝 기반 rPPG의 정확도가 빠르게 향상되고 있다.

#### 피부 혈류와 호르몬 변화

생리주기에 따른 피부 혈류 변화가 문헌으로 확인된다:
- 에스트로겐과 프로게스테론은 산화질소(NO) 수치를 높여 혈관을 확장시키고 혈관 저항을 감소시킨다
- 황체기에 프로게스테론 수치 상승으로 피부 혈류량이 증가하고 피부 온도가 상승한다
- 이러한 변화가 rPPG 신호의 진폭(amplitude)과 파형(waveform) 변화로 감지될 가능성이 있다 [초록 기반 추정]

---

### 1-2. 안면 피부 상태 분석 (여드름, 다모증)

#### 기술 개요
스마트폰 카메라로 촬영한 얼굴 이미지에서 여드름 병변을 자동 감지하고 심각도를 분류하는 AI 시스템이 다수 개발되어 있다. PCOS의 주요 표현형인 안드로겐 과다 증상(여드름, 다모증)을 객관적으로 추적할 수 있는 잠재력이 있다.

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 여드름 병변 감지 | Faster R-CNN + LightGBM (AcneDet) | 4종 병변 감지, 심각도 분류 정확도 85% | PCOS (안드로겐 과다의 피부 지표) | Moderate | [Diagnostics 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9406819/) |
| 여드름 심각도 분류 | DeepLabV3 + InceptionV3 하이브리드 | 검증 정확도 97%, F1 0.97 | PCOS (호르몬성 여드름 추적) | Moderate | [Springer Discover Computing 2025](https://link.springer.com/article/10.1007/s10791-025-09609-y) |
| 여드름 분류 (GEA 스케일) | CNN 기반 스마트폰 앱 | 면포성/염증성/색소침착 구분 | PCOS (여드름 유형별 호르몬 연관성) | Moderate | [Exp. Dermatol. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC6972662/) |
| 여드름 분류 (AcneDGNet) | 딥러닝 온라인 진료 데이터 | 심각도 분류 정확도 89.5% | PCOS (원격 모니터링) | Moderate | [Sci. Rep. 2024](https://www.nature.com/articles/s41598-024-84670-z) |
| 다모증 평가 (mFG 점수) | 시각적 평가 (현재 수동) | mFG >= 8이면 임상적 다모증 | PCOS (65-75% 환자에서 다모증) | Limited [AI 자동화 미개발] | [PMC Review 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2792145/) |

#### 자궁내막증/PCOS 적용 가능성 분석

**PCOS 직접 적용 (높은 가능성)**:
- PCOS 환자의 65-75%에서 다모증이 나타나며, 이는 안드로겐 과다의 주요 임상 지표이다
- 여드름 심각도가 안드로겐 수치와 상관관계를 가지며, 스마트폰 기반 자동 추적이 가능하다
- 여드름의 유형(면포성 vs 염증성 vs 결절성)이 호르몬 프로필과 연관될 수 있다
- **핵심 갭**: 여드름 심각도 변화의 시간적 패턴(생리주기 연동)과 PCOS 진단의 직접적 연관성을 검증한 연구는 부재

**자궁내막증 적용 (제한적)**:
- 자궁내막증은 주로 피부 증상을 동반하지 않아 안면 피부 분석의 직접 적용이 어렵다
- 다만, 자궁내막증 동반 피로 및 수면 장애로 인한 피부 상태 변화(다크서클, 혈색 등)는 탐색적 지표가 될 수 있다 [초록 기반 추정]

**다모증 AI 자동화 갭**:
- Ferriman-Gallwey 점수(mFG)는 현재 의사의 주관적 시각 평가에 의존한다
- 환자가 미용 제모 후 내원하면 평가가 어려운 한계가 있다
- 스마트폰 카메라 기반 자동 다모증 등급 시스템은 아직 개발되지 않았으며, 이는 중요한 **연구 공백**이다

---

### 1-3. 안면 혈류 혈색 패턴 및 부종

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 안면 부종(edema) 정량화 | 스마트폰/태블릿 카메라 얼굴 사진 분석 | 부종 정도 및 체중 변화 추정 가능 | PMS/PCOS (호르몬성 부종 추적) | Limited | [NEC Research 2022](https://www.nec.com/en/global/rd/technologies/202206/index.html) |
| 안면 부종 디지털 측정 | 디지털 이미지 처리 (개구장애, 홍조, 온도, 염증) | 4가지 부종 변수 동시 측정 | 자궁내막증/PCOS (염증 반응 추적) | Limited | [Discrete Dyn. Nat. Soc. 2013](https://onlinelibrary.wiley.com/doi/10.1155/2013/927843) |
| 월경전 부종 분포 | 임상 평가 | 91.7%에서 PMS 확인, 65%에서 부종 증상 | PCOS/PMS (부종이 흔한 증상) | Moderate | [Int. J. Women's Health 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4362892/) |

#### 적용 가능성 분석
- 월경 전 안면 부종은 PMS의 흔한 증상(65%)이며, PCOS 환자에서 인슐린 저항성과 관련된 체액 저류가 더 심할 수 있다
- NEC의 기술은 투석 환자용으로 개발되었으나, 호르몬 변화에 따른 안면 부종 추적에 전용 가능하다
- 생리주기 연동 안면 사진 촬영 + AI 분석으로 호르몬 상태를 간접 추정하는 것이 가능하나, 직접 검증 연구는 없다 [Exploratory]

---

## 2. 체형 시각적 분석

### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 허리-엉덩이 둘레비(WHR) | 스마트폰 카메라 CNN (MeasureNet) | MAE ~0.015, MAPE ~1.4% (자가 측정 대비 2배 정확) | PCOS (복부비만 = 인슐린 저항성 대리 지표) | Strong | [npj Digital Med. 2023](https://www.nature.com/articles/s41746-023-00909-5) |
| 체지방률 추정 | 스마트폰 4장 사진 → 3D 모델 (3D BodyShape) | DXA 대비 Pearson r = 0.90, TEM 0.5-0.7% | PCOS (대사 이상 모니터링) | Strong | [Cambridge Univ. / npj Digital Med. 2022](https://www.nature.com/articles/s41746-022-00628-3) |
| 3D 체형 재구성 | 스마트폰 3D 스캔 (비강체 아바타) | ICC 0.996-0.997 (신뢰도), DXA 대비 +-2% 등가 | PCOS (종단적 체형 변화 추적) | Moderate | [Front. Med. 2024](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1485450/full) |
| 체형 치수 (허리, 엉덩이, 허벅지) | 스마트폰 카메라 측정 | 평균 정확도 95.59% | PCOS (인체 측정 간소화) | Moderate | [Electronics 2021](https://www.mdpi.com/2079-9292/10/11/1338) |
| 종합 체성분 분석 | 상용 앱 (BodyScan) | 97.5% 정확도 (WHR, WHtR 등) | PCOS (자가 모니터링) | Moderate | [AHI Tech](https://www.ahi.tech/products/bodyscan) |

#### 자궁내막증/PCOS 적용 가능성 분석

**PCOS 직접 적용 (매우 높은 가능성)**:
- PCOS 환자의 40-80%에서 과체중/비만이 동반되며, 특히 복부 비만(android obesity)이 인슐린 저항성의 핵심 지표이다
- WHR > 0.85는 PCOS의 대사 위험 증가와 강하게 연관된다
- 스마트폰 기반 WHR 측정 기술(MeasureNet)은 이미 임상 수준의 정확도(MAE 0.015)를 달성했다
- 3D BodyShape 앱은 4장의 사진만으로 체지방률을 DXA와 높은 상관관계(r=0.90)로 추정한다
- **종단적 모니터링**: 체형 변화의 시간적 추이를 추적하면 PCOS의 대사 악화/개선을 조기 감지할 수 있다

**자궁내막증 적용 (제한적)**:
- 자궁내막증 자체는 체형 변화와 직접 관련이 적다
- 다만, 복부 팽만(bloating)은 자궁내막증의 흔한 증상이며, 복부 둘레 변화의 일간/주간 패턴이 바이오마커가 될 수 있다 [Exploratory]
- 호르몬 치료(GnRH agonist 등)에 따른 체중 변화 모니터링 용도는 가능하다

---

## 3. 움직임 자세 보행 분석

### 3-1. 보행 분석 (Gait Analysis)

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 보행 속도, 보폭, 케이던스 | 스마트폰 가속도계 | 보행 속도 ICC 우수, 골드 표준 대비 양호한 일치도 | 자궁내막증 (만성 통증으로 인한 보행 변화) | Moderate | [Sensors 2024](https://www.mdpi.com/2076-3417/14/23/11321) |
| 통증 관련 보행 비대칭 | 웨어러블 가속도계 + ML (OA-Pain-Sense) | 통증 수준 예측 정확도: DT 86.79%, SVM 83.57% | 자궁내막증 (골반통 유발 보행 이상) | Limited | [Systematic Review 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015829/) |
| 비디오 기반 보행 분석 | 스마트폰 카메라 영상 + 포즈 추정 | 무릎 굴곡각, 보행 속도 측정 검증 | 자궁내막증 (수술 후 회복 모니터링) | Limited | [Sensors 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11644766/) |

#### 근골격계 만성 통증과 보행 변화

근골격계 질환과 만성 통증에서 보행 분석의 정확도가 가장 낮았다는 보고가 있다. 이는 보행 변화가 골관절염 등에 비해 덜 뚜렷하기 때문이다. 그러나 자궁내막증의 만성 골반통은 특유의 보행/자세 패턴을 유발할 수 있다.

### 3-2. 자세 분석 (Posture Analysis)

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 흉추 후만각 (thoracic kyphosis) | 래스터 입체사진법 (raster stereography) | 만성 골반통 환자에서 자세 후만증 확인, 8주 운동 후 유의한 감소 | 자궁내막증 (통증-자세 연관) | Moderate | [PMC 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5890212/) |
| 운동 패턴, 근 병리, 신체 인식 | 임상 평가 (운동 분석) | CPP 환자에서 통증-자세-운동-근병리-신체 인식의 정형화된 패턴 확인 | 자궁내막증 (만성 골반통 표현형) | Moderate | [J Reprod Med. 2006](https://pubmed.ncbi.nlm.nih.gov/17084141/) |
| 족저압 분석 (baropodometry) | 압력 센서 매트 | 만성 골반통 환자의 체중 분포 이상 | 자궁내막증 (통증 보상 패턴) | Limited | [PMC 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3228674/) |

#### 자궁내막증/PCOS 적용 가능성 분석

**자궁내막증 (중간~높은 가능성)**:
- 만성 골반통(CPP) 환자에서 자세 후만증, 비정상적 운동 패턴, 체중 분포 이상이 반복적으로 보고된다
- 특히 월경통(dysmenorrhea) 기간 중 보호 자세(guarding posture)의 출현을 스마트폰 자세 추정 기술로 추적 가능
- 스마트폰 카메라 기반 포즈 추정(MediaPipe, OpenPose)의 발전으로 보행/자세 분석이 임상 외 환경에서도 가능해지고 있다
- **핵심 갭**: 자궁내막증 환자 대상으로 디지털 보행/자세 분석을 수행한 연구는 부재

**PCOS (낮은 가능성)**:
- PCOS 자체는 보행/자세 이상을 유발하지 않는다
- 비만 동반 시 보행 패턴 변화가 있을 수 있으나, PCOS 특이적이지 않다

---

## 4. 행동 패턴 시각적 신호

### 4-1. 통증 표정 인식 (Pain Facial Expression Recognition)

#### 기술 개요
컴퓨터 비전을 활용한 얼굴 표정 기반 자동 통증 평가는 2015년 이후 급격히 발전한 분야이다. FACS(Facial Action Coding System) 기반의 Action Unit(AU) 분석과 딥러닝을 결합하여 통증 유무 및 강도를 자동으로 감지한다.

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 통증 강도 자동 평가 | CNN + RNN 시공간 분석 | 최대 98.7% 정확도 (UNBC-McMaster 데이터셋) | 자궁내막증 (월경통/골반통 정량화) | Strong | [Systematic Review, Comput. Methods Programs Biomed. 2023](https://www.sciencedirect.com/science/article/pii/S0169260723000329) |
| 실시간 통증 감지 | 다중 모달 융합 (얼굴 특징 + 비디오) | 실시간 통증 평가 프레임워크 | 자궁내막증 (일상 통증 모니터링) | Moderate | [Academia 2024](https://www.academia.edu/136892290/) |
| 수술 후 통증 평가 | 자동 얼굴 표정 측정 + ML | 자가 보고 통증 점수와 양의 상관관계 | 자궁내막증 (수술 후 모니터링) | Moderate | [JMIR AI 2025](https://ai.jmir.org/2025/1/e53026) |
| EmoPain 챌린지 | VGG-16, ResNet-50 기반 (만성 통증 데이터) | 만성 통증의 시간적 얼굴 역동성 분석 | 자궁내막증 (만성 통증 표현형) | Moderate | [Technologies 2024](https://www.mdpi.com/2227-7080/12/6/92) |

#### 자궁내막증/PCOS 적용 가능성 분석

**자궁내막증 (높은 가능성)**:
- 월경통(dysmenorrhea)은 자궁내막증 환자의 75%에서 나타나는 핵심 증상이다
- 자동 통증 표정 인식은 최대 98.7% 정확도에 도달했으며, 특히 시공간(spatio-temporal) 분석이 만성 통증에 적합하다
- 현재 통증 일기(pain diary)는 주관적 자가 보고에 의존하나, 얼굴 표정 분석으로 객관적 통증 강도 정량화가 가능하다
- **핵심 기회**: 월경통 발작 중 자동 촬영 → 통증 강도 자동 기록 → 통증 패턴의 종단적 추적
- **한계**: 만성 통증 환자는 급성 통증과 다른 표정 패턴을 보이며, 통증 억제(pain suppression) 행동이 감지를 어렵게 할 수 있다

**PCOS (낮은 가능성)**:
- PCOS는 급성 통증 증상이 주요 표현형이 아니므로 직접 적용이 어렵다

---

### 4-2. 수면 중 움직임 분석 (Contactless Sleep Monitoring)

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 수면 중 움직임/뒤척임 | 적외선 카메라 + 영상 분석 | 수면 질 및 수면 단계 추정 가능 | 양 질환 공통 (수면 장애 추적) | Moderate | [Biosengineering 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9855193/) |
| 수면 무호흡 + 하지불안 감지 | 3D 카메라 야간 촬영 | OSA 민감도 90%, 특이도 71.4%; PLM 72.8% 감지 | 양 질환 (수면 장애 동반) | Moderate | [Sci. Rep. 2019](https://www.nature.com/articles/s41598-019-53050-3) |
| 심박수 + 호흡수 (수면 중) | 비디오 분석 (적외선) | 50명 성인에서 검증, PCA/ICA 기반 추출 | 양 질환 (야간 생리 신호) | Moderate | [PMC 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6889941/) |
| 프라이버시 보호 수면 모니터링 | 디포커스 카메라 | 심박수, 호흡수, 수면 자세, 움직임 측정 (피험자 식별 불가) | 양 질환 (가정용 수면 모니터링) | Limited | [PubMed 2024](https://pubmed.ncbi.nlm.nih.gov/38696292/) |

#### 자궁내막증/PCOS 적용 가능성 분석

**양 질환 공통 (중간 가능성)**:
- PCOS 환자에서 수면 무호흡 유병률이 일반 인구 대비 5-30배 높다 (비만 및 안드로겐 과다 관련)
- 자궁내막증 환자의 수면 질 저하는 통증, 불안, 야간 통증 각성과 관련된다
- 비접촉 수면 모니터링으로 수면 중 움직임 빈도, 자세 변환 횟수, 각성 시점 등을 추적하면 질환 활성도의 간접 지표가 될 수 있다
- 프라이버시 보호 디포커스 카메라 기술은 가정 환경에서의 실용성을 높인다

---

### 4-3. 눈 깜빡임 시선 추적 및 동공 반응

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 동공 반응 (pupillometry) - PCOS | 자동 동공계측기 | PCOS 환자에서 초기 동공 직경, 수축 진폭, 수축 속도 유의하게 감소; 확장 지속시간 유의하게 연장 | PCOS (자율신경 기능 이상 직접 증거) | **Limited (단일 연구이나 직접적)** | [PubMed 2025](https://pubmed.ncbi.nlm.nih.gov/41810641/) |
| 동공 반응 - 통증 | 동공계측기 | 통증이 자율신경 반응으로 동공 확장 유발, 자가 보고와 독립적으로 통증 반영 | 자궁내막증 (객관적 통증 평가) | Moderate | [PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11182876/) |
| 눈 깜빡임률 - 피로 | 컴퓨터 비전 (Eye Aspect Ratio) | 깜빡임 횟수 증가, 간격 감소가 피로와 유의 상관 | 양 질환 (피로 정량화) | Moderate | [ScienceDirect 2022](https://www.sciencedirect.com/science/article/pii/S2667241322000039) |
| 동공 - 자율신경 기능 | 적외선 동공계측기 | COVID-19 후 자율신경 이상 감지 | 전이 가능 기술 (자율신경 평가) | Moderate | [PMC 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8078384/) |

#### 자궁내막증/PCOS 적용 가능성 분석

**PCOS (높은 가능성 - 핵심 발견)**:
- 2025년 연구에서 **비비만 젊은 PCOS 여성**에서 동공 반응의 유의한 변화가 확인되었다. 이는 PCOS의 자율신경계 기능 이상을 시사하며, 동공계측이 PCOS의 비침습적 바이오마커로 활용될 수 있음을 보여준다.
- 교감신경과 부교감신경 활성 모두 감소하는 "전반적 자율신경 저하" 패턴이 관찰되었다
- 스마트폰 전면 카메라의 발전으로 동공 크기 추적이 점차 가능해지고 있다

**자궁내막증 (중간 가능성)**:
- 통증은 동공 확장을 유발하며, 동공 반응은 자가 보고 통증 점수와 독립적으로 통증을 반영한다
- 월경통 에피소드 중 동공 변화를 추적하면 객관적 통증 강도 지표가 될 수 있다

---

## 5. 인접 분야 이전 가능 기술

### 5-1. 우울증/정신건강 영상 바이오마커

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 전이 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|-----------|----------|------|
| 다중 모달 우울증 스크리닝 | EEG + 안구 운동 + 비디오/오디오 + 보행 | 다중 모달 AUC 0.95, 단일 모달 AUC 0.84-0.92 | 높음 (PCOS 동반 우울증, 자궁내막증 동반 정서 변화) | Strong | [npj Digital Med. 2025](https://www.nature.com/articles/s41746-025-01933-3) |
| 디지털 표현형 (수면, 활동, GPS) | 스마트폰 수동 센싱 | 행동, 감정, 건강 관련 결과 추정/예측 가능 | 높음 (여성 건강 수동 모니터링) | Strong | [Springer AI Review 2024](https://link.springer.com/article/10.1007/s10462-024-11009-5) |
| 피로 디지털 바이오마커 | 웨어러블 + 스마트폰 (만성 질환) | 만성 질환 피로의 디지털 바이오마커 체계적 고찰 | 높음 (자궁내막증 피로, PCOS 피로) | Moderate | [npj Digital Med. 2025](https://www.nature.com/articles/s41746-025-01939-x) |

#### 전이 가능성 분석
- 우울증 영상 바이오마커(얼굴 표정, 음성, 보행)는 자궁내막증/PCOS 동반 정서 장애 감지에 직접 전용 가능
- 특히 다중 모달 접근(비디오 + 음성 + 활동)이 단일 모달 대비 AUC 0.11 이상 향상되는 결과는, 자궁내막증/PCOS 예측에도 다중 영상 바이오마커 융합이 효과적일 수 있음을 시사

### 5-2. 당뇨/내분비 질환 시각적 감지

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 전이 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|-----------|----------|------|
| 당뇨 망막병증 | 스마트폰 안저 촬영 + AI (Medios AI) | 민감도 100%, 특이도 88.4% | 중간 (PCOS의 대사 합병증 조기 감지) | Strong | [npj Digital Med. 2022](https://www.nature.com/articles/s41433-018-0064-9) |
| 피부 영상 자가면역 질환 | AI 이미지 인식 (습진, 건선 등) | 분류 성능 진전, 다중 모달 통합 | 중간 (자궁내막증 = 면역 관련 질환) | Moderate | [PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12133082/) |

### 5-3. 적외선 열화상 (Infrared Thermography)

#### 선행연구 요약

| 바이오마커 | 측정 방법 | 주요 결과 | 질환 적용 가능성 | 증거 수준 | 출처 |
|-----------|----------|----------|----------------|----------|------|
| 복벽 자궁내막증 열화상 | 적외선 열화상 카메라 | 자궁내막증 병변부의 온도 상승 패턴 확인 | 자궁내막증 (표재성 병변 감지) | Limited | [ResearchGate 2018](https://www.researchgate.net/publication/324712452) |
| 염증 추적 (일반) | 적외선 열화상 | 염증, 혈관 변화의 비침습적 감지 | 양 질환 (염증 반응 모니터링) | Moderate | [PMC 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9462595/) |
| 휴대형/웨어러블 열화상 | 소형 적외선 카메라 | 웨어러블 열화상 센서 소형화 진행 중 | 양 질환 (가정용 모니터링) | Limited | [PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12836124/) |

---

## 6. 종합 평가 및 데이터 갭

### 6-1. 바이오마커 우선순위 종합 평가

| 순위 | 바이오마커 | 대상 질환 | 기술 성숙도 | 증거 수준 | 데이터 확보 용이성 | 종합 우선순위 |
|------|-----------|----------|-----------|----------|-----------------|------------|
| 1 | 체형/WHR 시각적 측정 | PCOS | 높음 (상용 앱 존재) | Strong | 높음 (스마트폰 사진) | **최우선** |
| 2 | 여드름 심각도 자동 분류 | PCOS | 높음 (다수 모델) | Moderate | 높음 (스마트폰 셀피) | **최우선** |
| 3 | 통증 표정 자동 인식 | 자궁내막증 | 높음 (범용 기술) | Strong (범용) | 중간 (동의 기반 촬영) | **높음** |
| 4 | rPPG 기반 HRV | 양 질환 | 중간 (정밀도 개선 중) | Strong (HRV 자체) | 높음 (스마트폰 카메라) | **높음** |
| 5 | 동공 반응 (pupillometry) | PCOS | 중간 (전용 장비 필요) | Limited (직접 근거) | 낮음 (전용 동공계측기) | **중간** |
| 6 | 수면 중 움직임 분석 | 양 질환 | 중간 (IR 카메라 필요) | Moderate | 중간 (가정 설치) | **중간** |
| 7 | 보행/자세 분석 | 자궁내막증 | 중간 (포즈 추정 발전) | Limited (직접 근거 없음) | 높음 (스마트폰 영상) | **중간** |
| 8 | 안면 부종 추적 | PCOS/PMS | 낮음 (연구 초기) | Limited | 높음 (스마트폰 사진) | **낮음** |
| 9 | 다모증 자동 등급 | PCOS | 매우 낮음 (미개발) | Limited (수동 평가만) | 높음 (스마트폰 사진) | **갭 기회** |
| 10 | 적외선 열화상 | 자궁내막증 | 중간 (장비 필요) | Limited | 낮음 (전용 장비) | **낮음** |

### 6-2. 핵심 연구 갭 (Research Gaps)

#### 갭 1: 안면 피부 변화의 종단적 추적과 PCOS 진단 연관성
- 여드름 AI 자동 분류 기술은 성숙했으나, 여드름 심각도의 **시간적 패턴**(생리주기 연동, 월별 추이)과 PCOS 진단의 직접적 연관성을 검증한 종단 연구가 없다
- **제안**: 생리 추적 앱과 연동하여 일간 안면 사진 촬영 → 여드름 패턴 + 생리주기 패턴의 상관관계 분석

#### 갭 2: 다모증(Hirsutism) 자동 분류 시스템 부재
- Ferriman-Gallwey 점수의 주관성과 한계가 지적되고 있으나, AI 기반 자동 다모증 등급 시스템은 아직 개발되지 않았다
- PCOS 환자의 65-75%에서 다모증이 나타나므로, 스마트폰 기반 자동 mFG 점수 산출은 높은 임상 가치를 가진다
- **제안**: 신체 9개 부위의 표준화된 사진 촬영 프로토콜 + CNN 기반 모발 밀도/길이 분류 모델 개발

#### 갭 3: 자궁내막증 환자의 디지털 보행/자세 분석
- 만성 골반통으로 인한 자세 후만증과 보행 패턴 변화가 임상 연구로 확인되었으나, 디지털 기기를 활용한 자동 분석 연구는 전무하다
- MediaPipe/OpenPose 등 포즈 추정 기술이 스마트폰에서 실시간 구동 가능해진 시점에서, 연구 기회가 크다
- **제안**: 스마트폰 영상 기반 일상 보행 패턴 추적 → 생리 주기 중 통증 기간의 보행 변화 감지

#### 갭 4: rPPG의 생리주기 연동 바이오마커 검증
- HRV의 생리주기별 변화는 잘 확립되어 있고, rPPG 기술도 빠르게 발전하고 있으나, rPPG로 측정한 HRV가 생리주기 변화를 감지할 수 있는지 직접 검증한 연구가 없다
- **제안**: rPPG 기반 HRV 연속 측정 → 생리주기 phase 예측 → PCOS(무배란 주기) vs 정상 주기 구분 가능성 평가

#### 갭 5: 동공 반응과 PCOS 후속 연구
- 2025년 단일 연구에서 PCOS 환자의 동공 반응 이상이 확인되었으나, 대규모 검증이 필요하다
- 스마트폰 전면 카메라를 활용한 간이 동공계측의 가능성 평가도 필요하다

#### 갭 6: 다중 모달 영상 바이오마커 융합
- 우울증 연구에서 다중 모달(비디오 + 음성 + 활동)이 단일 모달 대비 AUC 0.11 이상 향상되었다
- 자궁내막증/PCOS에서도 얼굴 분석 + 체형 분석 + 보행 분석 + 수면 분석의 다중 모달 융합이 진단 성능을 크게 향상시킬 수 있으나, 이를 시도한 연구는 전무하다

### 6-3. 자궁내막증 vs PCOS 적용 가능성 비교

| 영역 | 자궁내막증 | PCOS |
|------|----------|------|
| 얼굴/피부 분석 | 제한적 (피부 증상 비특이적) | **높음** (여드름, 다모증 = 안드로겐 지표) |
| 체형 분석 | 제한적 (복부 팽만 정도) | **매우 높음** (복부 비만 = 인슐린 저항성) |
| 보행/자세 분석 | **높음** (만성 골반통 반영) | 제한적 |
| 통증 표정 인식 | **매우 높음** (월경통, 골반통 정량화) | 제한적 |
| 수면 분석 | 중간 (통증성 수면 장애) | 중간 (수면 무호흡 동반) |
| 동공 반응 | 중간 (통증 객관화) | **높음** (자율신경 이상 직접 근거) |
| rPPG/HRV | 중간 (통증-자율신경 연관) | **높음** (주기 이상 감지) |

### 6-4. 데이터 확보 전략 제안

**스마트폰 기반 (가장 확보 용이)**:
1. 일간 안면 셀피 → 여드름 분류, 혈색 변화, 부종 추적
2. 전신 사진 (전면/측면) → WHR, 체형 변화 추적
3. 스마트폰 전면 카메라 rPPG → 심박수, HRV 추출
4. 스마트폰 영상 보행 촬영 → 포즈 추정 기반 보행/자세 분석

**전용 기기 기반 (연구 환경)**:
1. 적외선 카메라 수면 모니터링 → 수면 중 움직임, 호흡, 심박 추출
2. 자동 동공계측기 → 동공 반응 평가
3. 적외선 열화상 카메라 → 복부/골반 표면 온도 패턴

**상용 앱/플랫폼 연동 가능**:
- 생리 추적 앱 (Clue, Flo 등)의 증상 데이터와 영상 바이오마커 동기화
- 수면 추적 앱 (Sleep Cycle 등)의 수면 데이터 연동
- 피트니스 앱의 활동량/체중 데이터 연동

---

## 참고문헌

### 얼굴/피부 분석
1. [A machine learning-based approach for constructing rPPG signals from video cameras](https://www.nature.com/articles/s43856-024-00519-6) - Communications Medicine, 2024
2. [Wearable-Derived HRV Across the Menstrual Cycle: A Living Systematic Review](https://link.springer.com/article/10.1007/s40279-025-02388-y) - Sports Medicine, 2025
3. [Smartphone camera oximetry in an induced hypoxemia study](https://www.nature.com/articles/s41746-022-00665-y) - npj Digital Medicine, 2022
4. [Automatic Acne Object Detection and Severity Grading Using Smartphone Images](https://pmc.ncbi.nlm.nih.gov/articles/PMC9406819/) - Diagnostics, 2022
5. [An automatic acne detection framework using GAN with DNN](https://link.springer.com/article/10.1007/s10791-025-09609-y) - Discover Computing, 2025
6. [Visually scoring hirsutism](https://pmc.ncbi.nlm.nih.gov/articles/PMC2792145/) - PMC, 2009
7. [Physiological Changes in Women's Skin During the Menstrual Cycle: A Scoping Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11703644/) - PMC, 2024
8. [Estimating swelling and body weight from faces captured in images](https://www.nec.com/en/global/rd/technologies/202206/index.html) - NEC Research, 2022
9. [Characterization of symptoms and edema distribution in PMS](https://pmc.ncbi.nlm.nih.gov/articles/PMC4362892/) - Int J Women's Health, 2015

### 체형 분석
10. [Development and validation of smartphone WHR measurement (MeasureNet)](https://www.nature.com/articles/s41746-023-00909-5) - npj Digital Medicine, 2023
11. [Smartphone camera based assessment of adiposity (3D BodyShape)](https://www.nature.com/articles/s41746-022-00628-3) - npj Digital Medicine, 2022
12. [Smartphone 3D imaging for body composition (non-rigid avatar)](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1485450/full) - Frontiers in Medicine, 2024
13. [Body Size Measurement Using a Smartphone](https://www.mdpi.com/2079-9292/10/11/1338) - Electronics, 2021

### 보행/자세 분석
14. [Efficacy of exercise on pelvic pain and posture in endometriosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC5890212/) - PMC, 2018
15. [Posture, movement patterns, and body awareness in women with CPP](https://pubmed.ncbi.nlm.nih.gov/17084141/) - J Reprod Med, 2006
16. [Baropodometry in women with chronic pelvic pain](https://pmc.ncbi.nlm.nih.gov/articles/PMC3228674/) - PMC, 2011
17. [Smartphone Accelerometer for Gait Assessment](https://www.mdpi.com/2076-3417/14/23/11321) - Applied Sciences, 2024
18. [Psychometric Characteristics of Smartphone-Based Gait Analyses](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015829/) - PMC, 2025

### 통증/행동 분석
19. [Automatic assessment of pain based on deep learning: A systematic review](https://www.sciencedirect.com/science/article/pii/S0169260723000329) - Comput Methods Programs Biomed, 2023
20. [A Review of Automatic Pain Assessment from Facial Information](https://www.mdpi.com/2227-7080/12/6/92) - Technologies, 2024
21. [AI for pain assessment via facial expression recognition (2015-2025)](https://www.explorationpub.com/Journals/em/Article/1001370) - Exploration of Medicine, 2025
22. [Survey on Pain Detection Using Machine Learning](https://ai.jmir.org/2025/1/e53026) - JMIR AI, 2025

### 수면 모니터링
23. [Contactless Camera-Based Sleep Staging: The HealthBed Study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9855193/) - Bioengineering, 2023
24. [Contactless recording of sleep apnea and PLM by 3D-video](https://www.nature.com/articles/s41598-019-53050-3) - Scientific Reports, 2019
25. [Privacy-Protected Contactless Sleep Parameters Using Defocused Camera](https://pubmed.ncbi.nlm.nih.gov/38696292/) - PubMed, 2024

### 눈/동공 분석
26. [Evaluation of autonomic dysfunction with pupillometry in PCOS](https://pubmed.ncbi.nlm.nih.gov/41810641/) - PubMed, 2025
27. [Pupillometry as Potential Objective Measurement of Pain](https://pmc.ncbi.nlm.nih.gov/articles/PMC11182876/) - PMC, 2024
28. [Pupillometry: Psychology, Physiology, and Function](https://pmc.ncbi.nlm.nih.gov/articles/PMC6634360/) - J Cognition, 2019
29. [Autonomic dysfunction detection by pupillometer in COVID-19](https://pmc.ncbi.nlm.nih.gov/articles/PMC8078384/) - PMC, 2021

### 인접 분야/전이 기술
30. [AI-assisted multi-modal depression screening: systematic review and meta-analysis](https://www.nature.com/articles/s41746-025-01933-3) - npj Digital Medicine, 2025
31. [Digital phenotypes and biomarkers: systematic review of ML approaches](https://link.springer.com/article/10.1007/s10462-024-11009-5) - AI Review, 2024
32. [Systematic review: digital biomarkers of fatigue in chronic diseases](https://www.nature.com/articles/s41746-025-01939-x) - npj Digital Medicine, 2025
33. [AI-enabled precision medicine for inflammatory skin diseases](https://pmc.ncbi.nlm.nih.gov/articles/PMC12133082/) - PMC, 2025
34. [Automated diabetic retinopathy detection in smartphone fundus photography](https://www.nature.com/articles/s41433-018-0064-9) - Eye, 2018
35. [AI and ML can successfully diagnose PCOS](https://www.nih.gov/news-events/news-releases/ai-machine-learning-can-successfully-diagnose-polycystic-ovary-syndrome) - NIH, 2024
36. [Infrared Thermography Appearance of Abdominal Wall Endometriosis](https://www.researchgate.net/publication/324712452) - ResearchGate, 2018

---

*이 문서는 literature-reviewer 에이전트가 2026-04-06에 생성한 영상/이미지 기반 디지털 바이오마커 문헌 탐색 결과이다. [지식 기반] 및 웹 탐색 결과를 종합하였으며, 직접 전문(full-text) 확인이 불가한 논문은 [초록 기반 추정]으로 표기하였다.*
