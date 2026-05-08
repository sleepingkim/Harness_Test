# 스마트폰 카메라 기반 디지털 바이오마커 문헌 탐색 보고서

## 1. 탐색 개요

- **탐색 일자**: 2026-04-11
- **탐색 데이터베이스**: PubMed, PMC, IEEE Xplore, Google Scholar, arXiv, Semantic Scholar, Nature, JMIR, Springer, MDPI, Wiley, JAMA Network
- **검색 키워드**:
  - "remote photoplethysmography rPPG smartphone heart rate"
  - "camera-based vital signs detection deep learning"
  - "smartphone camera blood pressure estimation"
  - "facial video SpO2 estimation"
  - "contactless HRV smartphone camera"
  - "anemia detection smartphone conjunctiva camera"
  - "jaundice detection smartphone camera neonatal"
  - "skin cancer detection smartphone deep learning"
  - "eye tracking smartphone cognitive impairment"
  - "gait analysis smartphone camera Parkinson"
  - "depression detection facial video AI"
  - "stress detection smartphone camera"
  - "diabetes prediction facial analysis"
  - "smartphone PPG atrial fibrillation"
  - "smartphone camera ADHD detection eye tracking"
  - "smartphone camera tremor detection movement disorder"
  - "smartphone camera eye disease glaucoma cataract"
  - "sleep apnea detection smartphone camera facial analysis"
  - "disease prediction smartphone camera eye skin voice scoping review"
- **포함 기준**: 2015년 이후, 스마트폰 카메라 또는 일반 RGB 카메라 활용, 질병 예측/탐지/생체신호 추정 목적
- **제외 기준**: 전용 의료기기(CT/MRI/초음파) 단독 사용, 웨어러블 전용(PPG 패치/반지), 임상 영상 전용
- **총 검색 횟수**: 19회 웹 검색 + 10회 이상 논문 직접 확인(WebFetch)

---

## 2. rPPG 기반 심혈관/생체신호 바이오마커

원격 광용적맥파(remote Photoplethysmography, rPPG)는 스마트폰 또는 웹캠의 RGB 카메라로 피부 표면의 미세한 색상 변화를 감지하여 심박수, 심박변이도(HRV), 혈압, SpO2 등을 비접촉으로 측정하는 기술이다. 최근 딥러닝 기법(CNN, Transformer)의 발전으로 정확도가 크게 향상되었다.

| 바이오마커 | 측정 부위 | 사용 모델/알고리즘 | 성능 지표 | 실험 환경 | 증거 수준 | DOI/URL | 출처(저자, 연도, 저널) |
|---|---|---|---|---|---|---|---|
| 심박수(HR) | 얼굴 | rPPG + Deep Learning (CNN, Transformer) | MAE 0.5-3 bpm (데이터셋 의존); 기존 대비 정확도 크게 향상 | Lab + In-the-wild | **High** (종합 리뷰, 다수 연구) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12181896/) | 종합 리뷰, 2025, PMC ✅ |
| 심박수(HR) | 얼굴 | ReViSe (CNN 기반 스마트폰 앱) | 기기 내 실시간 추정; HR, RR, SpO2 동시 측정 | Lab | **Moderate** | [IEEE Xplore](https://ieeexplore.ieee.org/document/9989351/) | ReViSe, 2022, IEEE Access [지식 기반] |
| 심박수(HR) + 호흡수(RR) + 혈압(BP) | 얼굴 | WellFie 앱 (rPPG 기반) | SBP: r=0.91, DBP: r=0.85 (n=300, 참조 대비) | Lab (임상 검증) | **Moderate** (n=300) | [medRxiv](https://www.medrxiv.org/content/10.1101/2023.01.14.23284548v1.full) | WellFie 검증 연구, 2023, medRxiv ✓ |
| 혈압(BP) | 얼굴 | Transdermal Optical Imaging + ML | SBP/DBP 95.3%/96.4% 정확도 (±5 mmHg 이내); n=1,328 | Lab | **Moderate** (n=1,328, 정상 혈압만) | [AHA Journals](https://www.ahajournals.org/doi/10.1161/CIRCIMAGING.119.008857) | Luo et al., 2019, *Circ: Cardiovasc Imaging* ✓ |
| 혈압(BP) | 얼굴 | rPPG + Transfer Learning | MAE: SBP 7-12 mmHg, DBP 5-8 mmHg (연구에 따라 상이) | Lab + 외래환자 | **Moderate** | [Springer](https://link.springer.com/article/10.1007/s10489-024-05354-9) | Video-based BP, 2024, *Applied Intelligence* [지식 기반] |
| SpO2 | 얼굴 | STMap + CNN (ResNet-50, DenseNet-121, EfficientNet-B3) | MAE 1.274%, RMSE 1.710% (국제 기준 4% 초과 달성) | Lab (VIPL-HR 데이터셋) | **Moderate** (n=107) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10968547/) | Cheng et al., 2024, *Bioengineering* ✓ |
| 심박변이도(HRV) | 얼굴 | rPPG 기반 PRV(Pulse Rate Variability) 추출 | SDNN, RMSSD 등 HRV 지표 추출; ECG 대비 상관계수 0.85-0.95 | Lab | **Moderate** | [Frontiers](https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2024.1420100/full) | Deep learning rPPG 리뷰, 2024, *Frontiers* [지식 기반] |
| 심방세동(AF) 탐지 | 손가락 → 카메라 | FibriCheck 앱 (PPG + AI) | 정확도 98.5%, 민감도 96.3%, 특이도 99.3% (n=236, 10개 스마트폰) | In-the-wild (다기관) | **High** (다기관, FDA 검증) | [npj Digital Med](https://www.nature.com/articles/s41746-025-02059-2) | FibriCheck FDA-AF 연구, 2025, *npj Digital Medicine* ✓ |
| 심방세동(AF) 탐지 | 손가락 → 카메라 | 스마트폰 PPG + AI | 민감도 98.3%, 특이도 99.9%, PPV 99.6%, NPV 99.6% (n=50, 3,407 측정) | In-the-wild (실세계) | **Moderate** (n=50) | [Europace](https://academic.oup.com/europace/article/26/4/euae065/7648812) | Gruwez et al., 2024, *EP Europace* ✓ |
| rPPG 신뢰성 (저조도/고심박) | 얼굴 | rPPG 다양한 알고리즘 | 저조도 및 고심박 조건에서 신뢰도 평가 | Lab (controlled) | **Moderate** | [npj Digital Med](https://www.nature.com/articles/s41746-025-02192-y) | rPPG 신뢰성 연구, 2025, *npj Digital Medicine* [지식 기반] |

---

## 3. 얼굴/피부 영상 분석 바이오마커

| 바이오마커 | 탐지 질환 | 사용 모델 | 성능 지표 | 실험 환경 | 증거 수준 | DOI/URL | 출처 |
|---|---|---|---|---|---|---|---|
| 결막 색상 (헤모글로빈 추정) | 빈혈 | eMoglobin 앱 (RAW 이미지 + ML) | 정확도 75.4%; AUC 0.92 (Hb<7), 0.90 (Hb<9); 중증 빈혈 100% 탐지 (n=426) | In-the-wild (응급실) | **Moderate** (n=426) | [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0302883) | Zhao et al., 2024, *PLOS ONE* ✓ |
| 결막 영상 + 딥러닝 | 빈혈 | Vision Transformer (ViT) + Transfer Learning | 분류 정확도 91.43%; IoU 72.05% | Lab | **Limited** (소규모) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11854623/) | Deep Learning 빈혈 탐지, 2025, *Healthc Inform Res* ✓ |
| 결막 비디오 → 혈액 수치 | 빈혈/혈액 질환 | 딥러닝 파이프라인 (비침습적 혈액 수치) | 비침습적 혈구 수 추정; 연속 모니터링 가능 | Lab | **Exploratory** | [npj Digital Med](https://www.nature.com/articles/s41746-026-02598-2) | Bulbar conjunctiva 연구, 2026, *npj Digital Medicine* [지식 기반] |
| 피부 색상 (황달 바이오마커) | 신생아 황달 | BiliSG 앱 (ML + Kramer 원리) | Pearson r=0.84, 민감도 100%, 특이도 70%, AUC 0.89 (n=546) | In-the-wild (다인종) | **High** (n=546, JAMA) | [JAMA Network Open](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2827752) | Ngeow et al., 2024, *JAMA Network Open* ✓ |
| 피부 색상 (황달) | 신생아 황달 | Vision Transformer (T2T-ViT) | ResNet, SVM, k-NN 대비 우수; n=500 | Lab (임상) | **Moderate** (n=500) | [Nature](https://www.nature.com/articles/s41598-026-40515-5) | 황달 ViT 연구, 2026, *Scientific Reports* [지식 기반] |
| 피부 병변 이미지 | 피부암 (흑색종) | DenseNet169, Inception v3, MobileNetV2 | DenseNet169: 92.25%, F1=0.932; MobileNetV2: 98.4% (HAM10000) | Lab (공개 데이터셋) | **Moderate** (대규모 데이터셋) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10252190/) | 피부암 리뷰, 2023, *Diagnostics* [지식 기반] |
| 피부 병변 이미지 | 피부암 (흑색종) | Wide-field DCNN (MIT) | 전신 촬영 후 병변 자동 탐지; 조기 흑색종 선별 | In-the-wild | **Moderate** | [MIT News](https://news.mit.edu/2021/artificial-intelligence-tool-can-help-detect-melanoma-0402) | MIT 흑색종 탐지, 2021 [지식 기반] |
| 얼굴 분석 (당뇨 예측) | 당뇨병 | 스마트폰 PPG → 혈관 신호 분석 | 디지털 바이오마커 도출; Nature Medicine 게재 | Lab + In-the-wild | **Moderate** | [지식 기반] | Avram et al., 2020, *Nature Medicine* [지식 기반] |
| 안저 촬영 (스마트폰) | 당뇨 망막병증 | DL 기반 안저 분석 (다수 알고리즘) | 민감도 0.93, 특이도 0.90 (메타분석, 82개 연구, 887,244건) | In-the-wild (현장) | **High** (메타분석) | [npj Digital Med](https://www.nature.com/articles/s41746-025-02223-8) | 체계적 리뷰, 2025, *npj Digital Medicine* ✓ |
| 두개안면 구조 분석 | 수면무호흡(OSA) | CNN + 설문 결합 ML | 민감도 84.9%, 특이도 71.2% (메타분석, 6개 연구, n=2,400) | Lab + In-the-wild | **Moderate** (메타분석) | [JMIR](https://www.jmir.org/2024/1/e58187) | OSA AI 리뷰, 2024, *JMIR* [지식 기반] |
| 두개안면 구조 분석 | 수면무호흡(OSA) | CNN + 안면사진 + 설문 | n=748, PSG 검증; DL CNN 91.1% 민감도, 79.2% 특이도 | Lab (PSG 검증) | **Moderate** (n=748) | [PubMed](https://pubmed.ncbi.nlm.nih.gov/39815737/) | 두개안면 OSA, 2025, *PubMed* [지식 기반] |

---

## 4. 안구/동공 분석 바이오마커

| 바이오마커                | 탐지 질환             | 사용 모델                         | 성능 지표                                      | 실험 환경              | 증거 수준                | DOI/URL                                                                                               | 출처                                                     |
| -------------------- | ----------------- | ----------------------------- | ------------------------------------------ | ------------------ | -------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| 시선 추적 (Eye Tracking) | 경도인지장애(MCI)/알츠하이머 | AI 기반 태블릿 시선 추적 (m-ETA)       | MCI 선별 도구로 유망; 커뮤니티 기반 대규모 선별 가능           | In-the-wild (커뮤니티) | **Moderate**         | [Alzheimer's Res & Ther](https://link.springer.com/article/10.1186/s13195-025-01884-7)                | m-ETA 중국 연구, 2025, *Alzheimer's Res & Therapy* [지식 기반] |
| 시선 추적 (Eye Tracking) | 알츠하이머/MCI         | AI 시선 추적 + 모바일                | 모바일 기기 기반 AD 예측 모델 구축                      | Lab                | **Limited**          | [Springer](https://link.springer.com/article/10.1007/s40520-024-02882-9)                              | AI eye-tracking AD, 2024, *Aging Clin Exp Res* [지식 기반] |
| 시선 추적 + VR           | 치매 선별             | Eye tracking + ML + VR (VECA) | 비침습적, 효율적 선별 도구; n=다수                      | Lab                | **Moderate**         | [npj Digital Med](https://www.nature.com/articles/s41746-024-01206-5)                                 | VECA 연구, 2024, *npj Digital Medicine* [지식 기반]          |
| 시선 추적 + CPT          | ADHD              | AI 기반 시선 추적 (태블릿)             | 112 ADHD + 325 정상 아동; 기존 CPT 대비 진단 정확도 향상  | Lab (학교/커뮤니티)      | **Moderate** (n=437) | [Frontiers](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2024.1337595/full) | ADHD 시선 추적, 2024, *Frontiers in Psychiatry* [지식 기반]    |
| 시선 추적 + AI           | ADHD              | 태블릿/스마트폰 시선 추적                | 시선 추적 + CPT 통합 시 단독 CPT 대비 진단력 향상          | Lab                | **Moderate**         | [JMIR mHealth](https://mhealth.jmir.org/2024/1/e58927)                                                | ADHD 디지털 바이오마커, 2024, *JMIR mHealth uHealth* [지식 기반]   |
| 동공 크기 변화             | ADHD              | 스마트폰 근적외선 카메라 + 셀피 카메라        | 동공 반응으로 신경학적 질환 선별 가능                      | Lab (파일럿)          | **Exploratory**      | [ScienceDaily](https://www.sciencedaily.com/releases/2022/04/220429144904.htm)                        | 스마트폰 동공 앱, 2022, *ScienceDaily* [지식 기반]                |
| 안저 촬영 (스마트폰)         | 녹내장               | iGlaucoma (DL 기반)             | 정확도 99.0%, AUC 0.966, 민감도 95.4%, 특이도 87.3% | Lab (임상)           | **Moderate**         | [Nature Eye](https://www.nature.com/articles/s41433-023-02826-z)                                      | iGlaucoma, 2023, *Eye* [지식 기반]                         |
| 안저 촬영 (스마트폰)         | 백내장               | 스마트폰 카메라 + AI                 | Redmi 9A 13MP 카메라 활용; 임상 검증 진행             | In-the-wild (현장)   | **Moderate**         | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11560082/)                                             | 백내장 스마트폰 앱, 2024, *PMC* [지식 기반]                        |

---

## 5. 동작/보행 분석 바이오마커

| 바이오마커 | 탐지 질환 | 사용 모델 | 성능 지표 | 실험 환경 | 증거 수준 | DOI/URL | 출처 |
|---|---|---|---|---|---|---|---|
| 보행 패턴 (비디오 기반) | 파킨슨병 | KPCA + Feature-weighted 최소거리 분류기 | 정확도 93.6% (n=70 보행 시퀀스) | Lab | **Limited** (n=70) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11687389/) | Sathya Bama & Bevish Jinila, 2022, *Health Systems* ✓ |
| 보행 패턴 (카메라 센서) | 파킨슨병 | CMSA-Net (Bilateral Gait Camera Fusion) | 휴대용 기기 구현; 카메라 센서 기반 PD 탐지 | Lab + 포터블 | **Limited** | [PubMed](https://pubmed.ncbi.nlm.nih.gov/40573601/) | CMSA-Net, 2025, *Sensors* [지식 기반] |
| 다중 모달 (음성+손동작+보행) | 파킨슨병 (조기) | 스마트폰 멀티모달 ML | 음성 AUC 0.88, 보행 AUC 0.81, 통합 AUC 0.86; off-phase 조기 PD 식별 | In-the-wild | **Moderate** | [npj Parkinson's](https://www.nature.com/articles/s41531-025-00953-w) | 스마트폰 다중 모달 PD, 2025, *npj Parkinson's Disease* ✓ |
| 손 떨림 (비디오 분석) | 본태성 진전/파킨슨병 | Mediapipe + Computer Vision (Google), Vision (Apple) | 진전 주파수 정확 측정; TETRAS 점수와 유의한 상관 (n=66 ET 환자) | Lab (임상) | **Moderate** (n=66) | [npj Digital Med](https://www.nature.com/articles/s41746-024-01153-1) | Tremor CV 검증, 2024, *npj Digital Medicine* [지식 기반] |
| 손 떨림 (비디오 분석) | 본태성 진전/파킨슨병 | VIPER-Tremor (Visual Perceptive DL) | 스마트폰 비디오 기반 진전 분석; 접촉 없이 측정 | Lab | **Limited** | [ResearchSquare](https://www.researchsquare.com/article/rs-3692906/v1) | VIPER-Tremor, 2023, *Research Square* [지식 기반] |
| 보행 분류 (모바일 비디오) | 다양한 보행 장애 | Privacy-preserving AI + 모바일 비디오 | 743 비디오, 7가지 보행 유형 분류 | In-the-wild | **Moderate** (n=743) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440163/) | 보행 분류 AI, 2025, *PMC* [지식 기반] |

---

## 6. 정신건강 바이오마커

| 바이오마커 | 탐지 질환 | 사용 모델 | 성능 지표 | 실험 환경 | 증거 수준 | DOI/URL | 출처 |
|---|---|---|---|---|---|---|---|
| 자연스러운 얼굴 이미지 (전면 카메라) | 주요우울장애(MDD) | MoodCapture (RF + EfficientNet) | Balanced Acc 0.60-0.61, MCC 0.14 (n=177, 125,000+ 이미지, 90일) | **In-the-wild** (일상 자동 촬영) | **Moderate** (n=177, CHI 2024) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11296678/) | Nepal et al., 2024, *CHI 2024* ✓ |
| 표정 분석 (정서 자극 비디오) | MDD vs 양극성장애 | Emoface (얼굴 디지털 바이오마커) | 진단 정확도 95.29% (n=353+347) | Lab (임상) | **Moderate** (n=700) | [npj Mental Health](https://www.nature.com/articles/s44184-025-00164-4) | Emoface, 2025, *npj Mental Health Research* [지식 기반] |
| rPPG 기반 스트레스 신호 | 스트레스 | 1D-CNN + rPPG | 정확도 95.83% (UBFC-Phys 데이터셋) | Lab | **Limited** (벤치마크 데이터셋) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10892284/) | Fontes et al., 2024, *Sensors* ✓ |
| 얼굴 표정 + rPPG + 열화상 | 스트레스 | VISUALSTRESS (다중 모달 DL) | 실시간 스트레스 상태 식별 | Lab | **Exploratory** | [지식 기반] | VISUALSTRESS 프레임워크, 2024 [지식 기반] |
| 얼굴 감정 인식 (비디오) | 정서 장애 (정신건강 전반) | ML 기반 16개 감정 분류 | 스마트폰 비디오에서 16개 감정 분류; 인간 수행과 비교 | Lab | **Limited** | [JMIR](https://www.jmir.org/2025/1/e68942) | 얼굴 감정 인식, 2025, *JMIR* [지식 기반] |
| 다중 모달 (오디오 + 비디오) | 우울증 중증도 | 오디오-비디오 융합 AI | 우울증 중증도 수준 분류 | Lab | **Limited** | [MDPI](https://www.mdpi.com/2079-9292/14/7/1464) | 다중 모달 우울증, 2025, *Electronics* [지식 기반] |

---

## 7. 기술적 도전과제 및 한계

### 7.1 조명 조건 (Illumination)
- rPPG 신호는 조명 변화에 매우 민감. 저조도 환경에서 SNR(신호 대 잡음비) 급격히 저하
- 2025년 npj Digital Medicine 연구에서 저조도 및 고심박 조건에서 rPPG 신뢰성이 유의하게 감소함을 확인
- 자연광/인공광/혼합 조건에 따른 성능 변동이 큼
- **대응**: 적응형 조명 보정 알고리즘, 다중 색 공간(YCrCb, CIELAB) 활용

### 7.2 피부색 편향 (Skin Tone Bias)
- FibriCheck FDA-AF 연구(2025)에서 어두운 피부색에서 AF 탐지 민감도가 유의하게 감소함을 보고
- 대부분의 rPPG 학습 데이터셋이 밝은 피부색 중심으로 구성
- 빈혈 탐지, 황달 탐지에서도 피부색이 성능에 영향
- **대응**: 다양한 인종 포함 데이터셋 확보, Fitzpatrick 피부 유형별 성능 평가 의무화 필요

### 7.3 움직임 아티팩트 (Motion Artifact)
- 두부 움직임, 표정 변화가 rPPG 신호에 잡음 유발
- PURE 데이터셋은 6가지 움직임 조건(안정, 대화, 느린/빠른 이동, 소/중 회전)에서 평가
- 보행 분석에서는 카메라 흔들림이 추가적 문제
- **대응**: 모션 보상 알고리즘, 얼굴 안정화, 다중 ROI 추적

### 7.4 카메라 품질 및 기기 차이
- 스마트폰 기종별 카메라 해상도, 프레임레이트, 색 재현력 차이
- FibriCheck 연구에서 10개 스마트폰 기종 간 일관된 성능 확인 → 기기 독립성 가능
- MoodCapture 연구에서 87개 Android 기종에서 데이터 수집
- **대응**: 기기 캘리브레이션, RAW 포맷 활용(eMoglobin 앱), 표준화된 캡처 프로토콜

### 7.5 프라이버시 및 윤리
- 얼굴 이미지 기반 건강 분석은 개인정보 민감도 높음
- MoodCapture: 기기 내(on-device) 처리로 이미지 외부 전송 방지 설계
- 보행 분석: Privacy-preserving AI 기법 적용(골격 추출 후 원본 삭제)
- **대응**: 페더레이티드 러닝, 온디바이스 추론, 차등 프라이버시

### 7.6 임상 검증의 한계
- 대부분의 연구가 소규모(n<200) 파일럿 단계
- Lab 환경과 실생활(in-the-wild) 간 성능 격차 큼
- FDA/CE 인증을 받은 앱은 소수(FibriCheck, 일부 황달 앱)
- 종단 연구(longitudinal) 부족; 대부분 횡단적(cross-sectional) 설계

### 7.7 질환 특이성 vs. 일반화
- rPPG 기반 바이오마커(HR, HRV, BP)는 범용적이나 특정 질환 감별력 제한적
- 얼굴 분석 기반 우울증 탐지 정확도(~60%)는 임상 활용에 부족
- 다중 바이오마커 융합(multimodal) 접근이 필수

---

## 8. 공개 데이터셋 현황

| 데이터셋명 | 수집 방법 | 대상 측정 | 피험자 수 | 공개 여부 | URL |
|---|---|---|---|---|---|
| UBFC-rPPG | 웹캠 (640x480, 30fps, RAW RGB) | HR (PPG 참조) | 42명 | 공개 | [UBFC-rPPG](https://sites.google.com/view/ybenezeth/ubfcrppg) |
| PURE | 에코 카메라 (640x480, 30Hz) | HR, 6가지 움직임 조건 | 10명 (60 시퀀스) | 공개 | [지식 기반] |
| VIPL-HR | RGB + NIR 카메라, 다양한 조건 | HR, SpO2 | 107명 (2,378 RGB + 752 NIR 비디오) | 공개 | [지식 기반] |
| UBFC-Phys | 웹캠 | HR, 스트레스 | 56명 | 공개 | [지식 기반] |
| iBVP | RGB + 열화상 카메라 | HR, rPPG | 다수 | 공개 | [MDPI](https://www.mdpi.com/2079-9292/13/7/1334) |
| HAM10000 | 피부경 + 디지털 카메라 | 피부 병변 (7 유형) | 10,015 이미지 | 공개 | [지식 기반] |
| MoodCapture | 스마트폰 전면 카메라 (자동 촬영) | 우울증 (PHQ-8) | 177명 (125,000+ 이미지) | 비공개 (연구용) | [ACM](https://dl.acm.org/doi/10.1145/3613904.3642680) |
| ISIC Archive | 피부경 이미지 | 피부암/피부 병변 | 수만 장 | 공개 | [지식 기반] |
| Largest rPPG Evaluation | 다양한 카메라 | HR | 1,000+ 피험자 | 공개 (GitHub) | [GitHub](https://github.com/Health-HCI-Group/Largest_rPPG_Dataset_Evaluation) |
| rPPG-Toolbox | 다양한 데이터셋 통합 벤치마크 | HR, rPPG | 11개 데이터셋 통합 | 공개 (GitHub) | [GitHub](https://github.com/ubicomplab/rPPG-Toolbox) |

---

## 9. 연구 공백 분석

### 9.1 충분히 탐구되지 않은 질환/기술 조합

1. **여성 건강 (자궁내막증/PCOS)**: 스마트폰 카메라를 활용한 자궁내막증/PCOS 관련 연구가 전무. rPPG 기반 HRV, 얼굴 색상 변화(호르몬 영향), 피부 상태 변화 등을 통한 비접촉 모니터링 가능성 미탐구.

2. **rPPG 기반 대사질환 예측**: rPPG로 추출한 혈관 신호에서 당뇨병, 인슐린 저항성 등 대사 상태를 예측하는 연구가 초기 단계. Avram et al. (2020)의 Nature Medicine 연구 이후 후속 대규모 검증 부족.

3. **정신건강 In-the-wild 검증**: MoodCapture(2024)가 최초의 in-the-wild 우울증 탐지이나 정확도(~60%)가 낮음. 불안장애, PTSD, 양극성장애 등 다른 정신건강 질환의 일상 환경 탐지 연구 부족.

4. **소아/노인 특화 연구**: 대부분의 rPPG 연구가 성인 중심. 소아(특히 신생아 이외), 노인에서의 카메라 기반 바이오마커 검증 부족.

5. **다중 바이오마커 융합 (Camera-only)**: 카메라 단독으로 HR + HRV + BP + SpO2 + 피부 + 표정을 동시 분석하는 통합 시스템 연구 부족. 대부분 단일 바이오마커에 집중.

6. **장기 종단 연구**: 카메라 기반 바이오마커의 시간에 따른 변화 추적, 질병 발병 전 예측(presymptomatic detection) 연구 전무.

7. **호흡기 질환 (SpO2 기반)**: rPPG 기반 SpO2 측정은 가능하나, 수면무호흡, COPD 등 호흡기 질환과의 직접 연결 연구 부족. 야간 SpO2 모니터링을 카메라로 구현한 연구 없음.

8. **표준화 및 규제**: rPPG 기반 건강 도구의 FDA/CE 인증 경로가 불명확. FibriCheck이 유일한 규제 승인 사례.

### 9.2 기술적 공백

1. **실생활 조건에서의 강건성**: 대부분의 고성능 결과가 통제된 Lab 환경에서 달성. 조명, 움직임, 거리 변동이 심한 실생활에서의 체계적 검증 부족.

2. **Edge AI / 온디바이스 추론**: 스마트폰 내에서 실시간 rPPG 처리를 위한 경량 모델(MobileNet, TinyML) 연구는 있으나 임상 수준 정확도 달성 사례 제한적.

3. **Multi-ethnic 검증**: 대부분의 데이터셋이 유럽/동아시아 중심. 아프리카, 남아시아, 라틴아메리카 등 다양한 인종에서의 체계적 검증 부족.

---

## 10. 자궁내막증/PCOS 연계 가능성

기존 문헌 리뷰(`01_literature_review.md`)에서 확인된 자궁내막증/PCOS 디지털 바이오마커와 스마트폰 카메라 기반 바이오마커의 연계 가능성을 분석한다.

### 10.1 직접 연계 가능한 바이오마커

| 카메라 바이오마커 | 자궁내막증/PCOS 관련성 | 근거 | 연계 실현 가능성 |
|---|---|---|---|
| **rPPG 기반 HRV** | PCOS: SDNN, RMSSD, HF power 유의 감소 (교감 우세); 자궁내막증: 부교감 저하와 통증 강도 상관 | Saranya et al., 2018; Hellman et al., 2021 | **높음** -- rPPG로 비접촉 HRV 측정 → 월경주기 중 자율신경계 변화 추적 가능 |
| **rPPG 기반 심박수/스트레스** | PCOS/자궁내막증 환자의 만성 스트레스 반응, 교감 과활성 | HRV 연구들에서 일관 | **높음** -- 일상 스트레스 모니터링과 증상 악화 패턴 연관 분석 가능 |
| **얼굴 피부 색상 변화** | PCOS: 안드로겐 과다로 인한 여드름, 과색소침착, 다모증 | 임상적으로 확립된 PCOS 표현형 | **중간** -- 얼굴 피부 상태 변화를 주기적으로 모니터링하여 호르몬 변동 간접 추정 가능; 연구 전무 |
| **얼굴 혈류 패턴 (rPPG 부산물)** | 호르몬 주기에 따른 미세 혈관 변화; 에스트로겐/프로게스테론이 혈관 반응성에 영향 | 생리학적 근거 확립, 직접 연구 없음 | **중간-낮음** -- 탐색적 연구 필요 |
| **SpO2 모니터링** | PCOS: 수면무호흡 유병률 증가 → 야간 SpO2 저하 관련 | 역학적 연관성 확립 | **중간** -- 카메라 기반 SpO2로 수면 관련 호흡 이상 선별 보조 가능 |

### 10.2 간접 연계 및 신규 제안

1. **월경주기 연동 rPPG 모니터링**: 월경추적 앱 데이터 + 매일 rPPG 셀피 → 주기별 HRV/HR/BP 변화 패턴 수집. PCOS 환자의 배란 지연/무배란 시 자율신경계 패턴 변화 탐지 가능성.

2. **얼굴 부종/피부 변화 추적**: 자궁내막증 환자의 염증 관련 얼굴 부종, PCOS 환자의 안드로겐 관련 피부 변화를 종단적으로 카메라 모니터링.

3. **수면 + 호흡 카메라 분석**: 야간 스마트폰 카메라로 수면 중 얼굴 + SpO2 + 호흡 패턴 동시 모니터링 → PCOS 관련 수면무호흡 위험 평가.

4. **다중 모달 통합**: 카메라(rPPG, 얼굴 분석) + 앱(월경 추적, 증상 일지) + 웨어러블(체온, 활동) 데이터 융합 → 자궁내막증/PCOS 감별 예측 모델.

### 10.3 연구 제안 우선순위

| 우선순위 | 연구 주제 | 실현 가능성 | 예상 영향력 |
|---|---|---|---|
| 1 | rPPG 기반 HRV + 월경주기 앱 연동 코호트 연구 (PCOS vs. 정상 vs. 자궁내막증) | 높음 (기존 기술 활용) | 높음 |
| 2 | 스마트폰 얼굴 피부 분석 → PCOS 호르몬 변동 간접 추정 | 중간 | 중간-높음 |
| 3 | 야간 카메라 SpO2 + PCOS 수면무호흡 연관 연구 | 중간 | 중간 |
| 4 | 카메라 + 웨어러블 + 앱 다중 모달 통합 예측 모델 | 낮음-중간 (데이터 수집 복잡) | 매우 높음 |

---

## 부록: 스코핑 리뷰 참고

Dawadi et al. (2025)의 스코핑 리뷰(*JMIR AI*, DOI: 10.2196/59094)에서 스마트폰 기반 눈/피부/음성 데이터를 활용한 질병 예측 ML 연구 49편을 체계적으로 분석하였다. 주요 질환으로 파킨슨병(12편), COVID-19(4편), 우울증(4편), 당뇨 망막병증(3편) 등이 포함되었으며, CNN이 눈(41.2%)/피부(30%) 분석에서, Random Forest가 음성 분석(18.5%)에서 가장 많이 사용되었다. ✓

---

*본 보고서는 2026-04-11 기준 웹 기반 학술 탐색 결과를 종합한 것입니다. ✓ 표시는 WebFetch로 직접 원문/초록을 확인한 논문이며, [지식 기반] 표시는 검색 결과 요약 또는 기존 지식에 기반한 정보입니다. DOI/URL은 검색 시 확인된 것이나, 일부 접근 제한 논문은 완전한 본문 검증이 불가하였습니다.*
