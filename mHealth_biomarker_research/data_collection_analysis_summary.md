# 디지털 바이오마커 수집·분석 방법론 정리

> 영상(Video) 기반 연구 7편 + 음성(Audio) 기반 연구 7편  
> 각 연구에서 **어떤 바이오마커**를, **어떻게 수집**했으며, **어떻게 분석**했는지 중점 정리  
> 작성일: 2026-05-08

---

## 1부. 영상(Video/Image) 기반 연구

---

### [V1] BiliScreen — 스마트폰 공막 황달 스크리닝

**출처**: Mariakakis, A. et al. (2017). *BiliScreen: Smartphone-Based Scleral Jaundice Monitoring for Liver and Pancreatic Disorders*. ACM IMWUT, Vol. 1, No. 2.

#### 사용 바이오마커
- **공막(sclera) 색상**: 눈 흰자 부위의 노란빛 정도 → 혈중 빌리루빈(bilirubin) 수준 비침습 추정

#### 데이터 수집 과정
- **장비**: iOS 스마트폰 카메라 + **색상 보정 부속품 2종** (①블루박스: 표준 파장 LED 조명 상자, ②색상 기준 카드 안경형 마스크)
- **환경**: 임상 환경(병원)에서 표준화된 조명·거리 조건
- **절차**: 피험자가 색상 보정 부속품을 착용하거나 박스 안에 얼굴을 넣은 상태에서 스마트폰으로 눈 클로즈업 촬영

#### 피실험자 모집
- **규모**: 70명 (임상 피험자, 간·췌장 질환 환자 포함)
- **기준**: 빌리루빈 수치가 다양한 범위(정상~고빌리루빈혈증)에 걸쳐 있는 환자
- **동시 측정**: 혈청 빌리루빈 검사와 동시 촬영하여 페어 데이터 확보

#### 피실험자에게 요구한 행동
- 색상 보정 부속품(블루박스 또는 색상 기준 안경)을 착용한 채 정면을 응시
- 스마트폰 카메라로 눈(공막 부위) 촬영

#### 결과 분석
- **전처리**: 얼굴/공막 영역 자동 검출, 색공간(RGB → YCbCr 등) 변환, 색상 보정 적용
- **모델**: 공막 색상 값 → 빌리루빈 회귀 (선형 및 비선형 회귀 + 머신러닝)
- **성능**: 빌리루빈 ≥ 3 mg/dL (황달 임계값) 검출 민감도 89.7%, 특이도 96.8%

---

### [V2] PCOS 공막 혈관 패턴 — 딥러닝 자동 진단

**출처**: Lv, W. et al. (2021). *Deep Learning Algorithm for Automated Detection of Polycystic Ovary Syndrome Using Scleral Images*. Frontiers in Endocrinology, 12:789878.

#### 사용 바이오마커
- **공막 혈관·색소 패턴**: 한의학 이론에서 눈의 혈관 분포가 전신 상태를 반영한다는 가설에 기반, 스마트폰/임상 카메라로 촬영한 눈 이미지의 공막 패턴

#### 데이터 수집 과정
- **장비**: 임상 카메라 (정면 눈 클로즈업)
- **환경**: 한의학 임상 기관
- **절차**: 전안부(anterior eye segment) 정면 영상 촬영 → 공막 분할 → 특징 추출

#### 피실험자 모집
- **규모**: 중국 여성 721명 (PCOS 388명 + 대조군 333명)
- **PCOS 진단 기준**: Rotterdam criteria (무배란, 고안드로겐증, 다낭성 난소 중 2개 이상)
- **대조군**: 정기 건강검진에서 PCOS 음성 확인된 여성

#### 피실험자에게 요구한 행동
- 임상 카메라 앞에서 눈을 크게 뜨고 정면 응시하여 전안부 촬영

#### 결과 분석
- **전처리**: 얼굴/눈 검출 → 개선된 U-Net + Attention 모듈로 공막 영역 자동 분할
- **모델**: ResNet-18 (특징 추출) + Multi-Instance Learning(MIL) 분류기
- **학습**: ImageNet 사전학습 → 미세조정, k-fold 교차검증
- **성능**: AUC 0.979, 정확도 0.929

---

### [V3] FaceAge — 얼굴 사진으로 생물학적 나이 추정 (암 예후 예측)

**출처**: Bontempi, D. et al. (2025). *FaceAge, a deep learning system to estimate biological age from face photographs to improve prognostication*. The Lancet Digital Health.

#### 사용 바이오마커
- **얼굴 생물학적 나이(FaceAge)**: 주름, 피부 처짐, 노화 관련 형태 변화 → 생물학적 나이 추정 → 암 환자 예후 예측에 활용

#### 데이터 수집 과정
- **학습 데이터**: 공개 인터넷 데이터셋 (IMDB-WIKI 56,304명 + UTKFace 2,547명) — 연예인·일반인 사진을 연령 라벨과 함께 사용
- **임상 검증 데이터**: 미국·네덜란드 2개 기관의 암 환자 임상 사진 6,196명
- **장비**: 디지털 카메라 (표준 임상 환경)

#### 피실험자 모집 (임상 검증 코호트)
- **규모**: 6,196명 암 환자 (다기관)
- **기준**: 방사선 치료 시작 시점에 임상 사진이 존재하는 암 환자
- **비교**: FaceAge와 실제 생존 데이터(사망일) 페어

#### 피실험자에게 요구한 행동
- 임상 표준 사진 촬영 (정면, 중립 표정)

#### 결과 분석
- **전처리**: 얼굴 검출(MTCNN류), 정렬, 256×256 크롭
- **모델**: VGG/Inception 계열 두 단계 CNN (localization + age regression)
- **성능**: 암 환자의 FaceAge가 실제 나이 대비 평균 ~5세 높음; FaceAge 1세 증가당 사망 위험 유의미하게 상승; 임상의 단독 예후 예측 AUC 0.74 → FaceAge 추가 시 AUC 0.80

---

### [V4] 갑상선안병증(TAO) 활성도 예측 — 안와 주변 임상 징후

**출처**: Moon, J.H. et al. (2022). *Machine Learning-Assisted System Using Digital Facial Images to Predict the Clinical Activity Score in Thyroid-Associated Orbitopathy*. Scientific Reports, 12:22085.

#### 사용 바이오마커
- **TAO 임상 활성 점수(CAS) 항목**: ①안검 부종, ②결막 부종(chemosis), ③결막 충혈, ④안검 발적, ⑤눈물샘 충혈 — 얼굴 정면 사진에서 시각적으로 평가

#### 데이터 수집 과정
- **장비**: 임상 디지털 카메라 (표준 조명)
- **환경**: 다기관 안과 외래
- **절차**: 환자 진료 시 표준화된 정면 얼굴 사진 촬영 → 안과 전문의가 CAS 항목별 라벨링

#### 피실험자 모집
- **규모**: 다기관 TAO 환자 + 정상 대조군
- **기준**: 갑상선안병증 진단 환자 (EUGOGO 기준), 각 CAS 항목별 활성/비활성 분류

#### 피실험자에게 요구한 행동
- 정면 응시 표준 자세로 임상 사진 촬영 (별도의 특별한 행동 없음)

#### 결과 분석
- **전처리**: 안와 주변 랜드마크 자동 검출 네트워크
- **모델**: ResNet-18 앙상블 (CAS 항목별 이진 분류 + 활성 TAO 종합 진단)
- **성능**: 활성 TAO 진단 민감도 0.881, 특이도 0.869; 개별 염증 징후 AUC 0.884~0.977

---

### [V5] 파킨슨병 표정 감소(Hypomimia) — 셀피 비디오 자동 평가

**출처**: Abrami, A. et al. (2021). *Automated Computer Vision Assessment of Hypomimia in Parkinson Disease: Proof-of-Principle Pilot Study*. Journal of Medical Internet Research, 23(2):e21037.

#### 사용 바이오마커
- **표정 동역학(Facial Expression Dynamics)**: 얼굴 근육 움직임의 감소·경직 패턴(hypomimia) — PD 환자는 자발적 표정이 줄어들고 얼굴이 굳는 특징을 보임

#### 데이터 수집 과정
- **방법**: YouTube에서 공개된 자가 촬영 셀피 비디오 수집 (원격·비접촉 방식)
- **PD 그룹**: PD 환자가 직접 제작·업로드한 "나는 PD 환자입니다(I have Parkinson's)" 유형 브이로그 영상
- **대조군**: 정상 일반인 셀피 비디오

#### 피실험자 모집
- **규모**: PD 자가식별 107명 + 대조군 1,595개 비디오 (유튜브 공개 데이터)
- **특이점**: 임상 진단 확인이 아닌 자가보고(self-identified) 방식으로 PD 그룹 구성

#### 피실험자에게 요구한 행동
- 별도 요구 없음 (자연스럽게 촬영된 공개 비디오 활용) — 정면 얼굴이 포착된 세그먼트만 추출

#### 결과 분석
- **전처리**: OpenFace로 얼굴 검출, 비디오 프레임별 얼굴 랜드마크 추출
- **모델**: CNN 이미지 분류기 (프레임 단위 예측 → 비디오 단위 집계)
- **성능**: 54명 테스트셋 AUC 0.71 (신경과 전문의 AUC 0.75와 유사)

---

### [V6] 뇌졸중 응급 스크리닝 — 얼굴 비대칭 + 음성 멀티모달

**출처**: Cai, Y. et al. (2022). *DeepStroke: An Efficient Stroke Screening Framework for Emergency Rooms with Multimodal Adversarial Deep Learning*. Medical Image Analysis (Elsevier).

#### 사용 바이오마커
- **얼굴 근육 비조정성(facial muscle incoordination)**: 미소·찡그림 등 표정 유도 시 좌우 안면 비대칭 패턴
- **음성 이상 신호**: 발성 어려움, 구음장애 (얼굴+음성 멀티모달)

#### 데이터 수집 과정
- **장비**: 카메라 + 마이크 (응급실 비치)
- **환경**: 응급실(Emergency Room) 내 표준화된 평가 공간

#### 피실험자 모집
- **규모**: 응급실 내원 환자 코호트 (구체 인원 원문 참조)
- **기준**: NIHSS(신경학적 결손 기준)로 확인된 뇌졸중 의심 환자 + 대조군(비뇌졸중 응급 환자)

#### 피실험자에게 요구한 행동
- **얼굴 평가**: 카메라 앞에서 미소·찡그림 등 특정 표정 동작 수행
- **음성 평가**: 표준 문장 또는 발성 과제 수행

#### 결과 분석
- **전처리**: 얼굴 검출/정렬, 시간적 윈도우 분할, 오디오 VAD 처리
- **모델**: 멀티모달 적대적 딥러닝 (얼굴 CNN + 오디오 CNN + fusion 레이어)
- **성능**: 민감도 93.12%, 정확도 79.27% (응급실 의사 수준과 동등)

---

### [V7] 여드름 중증도 자동 등급화 — 스마트폰 이미지 AI

**출처**: Huynh, Q.T. et al. (2022). *Automatic Acne Object Detection and Acne Severity Grading Using Smartphone Images and Artificial Intelligence (AcneDet)*. Diagnostics (MDPI), 12(8):1879.

#### 사용 바이오마커
- **여드름 병변 4종**: blackheads/whiteheads, papules/pustules, nodules/cysts, acne scars — 개수·위치·분포로 IGA(Investigator's Global Assessment) 5단계 중증도 산출
- **PCOS 연관성**: 안드로겐 과다(PCOS 핵심 증상) → 여드름 중증도 증가, 간접 바이오마커로 활용 가능

#### 데이터 수집 과정
- **장비**: iOS·Android 스마트폰 카메라
- **환경**: 임상 + 실생활 다양한 환경 (조명, 거리 다양)
- **라벨링**: 4명의 피부과 전문의가 병변 유형·위치·중증도 등급 수동 라벨

#### 피실험자 모집
- **규모**: 1,572장 얼굴 이미지 (여드름 환자 및 일반인)
- **기준**: 여드름이 존재하는 다양한 피부 타입, 다양한 조명 환경

#### 피실험자에게 요구한 행동
- 스마트폰으로 얼굴 정면 촬영 (특별한 표준 자세 미규정 — 실생활 다양 환경 반영)

#### 결과 분석
- **전처리**: 얼굴 검출, bounding box 라벨링 (병변 객체 단위)
- **모델**: Faster R-CNN (병변 객체 검출) + LightGBM (중증도 등급화)
- **학습**: ImageNet 사전학습, 표준 Faster R-CNN 파이프라인
- **성능**: 4종 병변 mAP=0.54; IGA 5단계 중증도 평균 AUC=0.85

---

## 2부. 음성(Audio/Voice) 기반 연구

---

### [A1] 파킨슨병 음성 바이오마커 — 지속 모음 jitter/shimmer/HNR

**출처**: Naranjo, L. et al. (2025). *Voice biomarkers as prognostic indicators for Parkinson's disease using machine learning techniques*. Scientific Reports (Nature).

#### 사용 바이오마커
| 특징군 | 구체 특징 |
|--------|----------|
| 주파수 섭동 | jitter (절대값·상대값·RAP·PPQ5·DDP) |
| 진폭 섭동 | shimmer (local·dB·APQ3·APQ5·DDA) |
| 잡음 | HNR (Harmonics-to-Noise Ratio), NHR |
| 기본 주파수 | F0 평균·표준편차 |
| 켑스트럼 | MFCC 1-13 |
| 비선형 | DFA (Detrended Fluctuation Analysis), RPDE, PPE |

#### 데이터 수집 과정
- **장비**: AKG-C420 콘덴서 마이크, 44.1 kHz / 16-bit 녹음
- **환경**: 방음실(soundproof room)
- **프로토콜**: 참여자가 지속 모음 /a/를 5초간 발성

#### 피실험자 모집
- **규모**: 파킨슨 환자 188명 + 건강한 대조군 64명 (UCI Parkinson Telemonitoring Dataset 확장)
- **기준**: 신경과 전문의에게 PD 진단을 받은 환자, 약물 복용 상태에서 측정

#### 피실험자에게 요구한 행동
- 방음실에서 편안한 음량으로 **지속 모음 /a/를 5초간 발성**

#### 결과 분석
- **특징 추출 도구**: Praat, MATLAB Voice Analysis Toolbox
- **전처리**: 시간 정렬, 정규화, VAD(음성 활동 감지)
- **모델 비교**: SVM(RBF), XGBoost, Random Forest, BiLSTM
- **실험 설계**: 5-fold 교차검증, 80/20 train/test 분할
- **성능**: BiLSTM AUC=0.97, 정확도=97%; SVM 정확도=92%

---

### [A2] 알츠하이머 치매 음성 인식 — Cookie Theft 그림 묘사 과제

**출처**: Luz, S. et al. (2020). *Alzheimer's Dementia Recognition through Spontaneous Speech: The ADReSS Challenge*. INTERSPEECH 2020.

#### 사용 바이오마커
| 특징군 | 구체 특징 |
|--------|----------|
| 비언어 | 침묵 비율(pause ratio), 발화 길이, 휴지 빈도 |
| 켑스트럼 | MFCC 1-13 |
| 운율/스펙트럼 | eGeMAPS 88개 특징, ComParE 6,373개 특징 |
| 언어 | 어휘 다양성, 명사구 밀도, 정보 단위 수 |

#### 데이터 수집 과정
- **방법**: DementiaBank Pitt Corpus — 임상 인터뷰(1:1 면담) 음성 수집
- **장비**: 임상 마이크, 16 kHz
- **프로토콜**: 훈련된 임상가가 환자에게 그림을 보여주고 자유롭게 묘사하도록 유도

#### 피실험자 모집
- **규모**: 성별·연령 균형을 맞춘 AD 78명 + 건강 대조군 78명 (총 156명)
- **기준**: MMSE·CDR로 AD 확진된 환자; 연령(60-90세)·성별 매칭 대조군

#### 피실험자에게 요구한 행동
- **Cookie Theft 과제**: Boston Diagnostic Aphasia Examination의 그림 자극(주방 장면)을 보고 **자유롭게 묘사** (시간 제한 없음, 평균 1-3분 발화)

#### 결과 분석
- **특징 추출**: openSMILE (eGeMAPS, ComParE), librosa
- **전처리**: 음성 향상, 정규화
- **모델**: Logistic Regression, SVM, LDA, Random Forest, CNN
- **성능**: 음향 특징 단독 Baseline 정확도 62.5%; 최상위 시스템 정확도 89.6%

---

### [A3] 양극성장애 음성 상태 마커 — 일상 전화 통화 종단 추적

**출처**: Faurholt-Jepsen, M. et al. (2016). *Voice analysis as an objective state marker in bipolar disorder*. Translational Psychiatry (Nature).

#### 사용 바이오마커
| 특징군 | 구체 특징 |
|--------|----------|
| 음성 품질 | 창끼(roughness), 기식음(breathiness) |
| 스펙트럼 | spectral flux, 스펙트럼 중심 |
| 포먼트 | F1-F4 포먼트 주파수·대역폭 |
| 예측 부호화 | LPC (Linear Predictive Coding) 계수 |

#### 데이터 수집 과정
- **방법**: 환자 일상 스마트폰 전화 통화 자동 수집 (비접촉 생태적 순간 평가)
- **환경**: 실생활 자연 환경 (병원 외부)
- **기간**: 121일간 종단 추적

#### 피실험자 모집
- **규모**: 양극성장애 환자 28명
- **기준**: 양극성장애 I·II형 진단 환자, 스마트폰 보유, 정신과 추적 관찰 중
- **라벨**: 임상가가 매일 전화 인터뷰로 조증/혼재/우울 상태 평가

#### 피실험자에게 요구한 행동
- 일상 전화 통화 시 **앱이 자동으로 음성 녹음** — 별도의 발화 과제 없음
- 화자 구분 처리 후 환자 음성만 추출

#### 결과 분석
- **전처리**: 화자 구분(diarization), 통화 잡음 제거
- **모델**: Random Forest (임상 상태 분류: 조증/혼재/우울/안정)
- **실험 설계**: longitudinal within-subject 분석 (개인 내 시간적 변화)
- **성능**: 조증·혼재 상태 분류 AUC=0.89, 우울 상태 분류 AUC=0.78

---

### [A4] COVID-19 진단 — 크라우드소싱 기침·호흡·음성 데이터베이스

**출처**: Sharma, N. et al. (2020/2021). *Coswara — A Database of Breathing, Cough, and Voice Sounds for COVID-19 Diagnosis*. INTERSPEECH 2020.

#### 사용 바이오마커
| 과제 유형 | 바이오마커 |
|---------|----------|
| 기침 | 기침 스펙트럼 패턴 (얕은 기침·깊은 기침 구분) |
| 호흡 | 흡기/호기 비율, 호흡 스펙트럼 |
| 모음 | /a/, /i/, /u/ 지속 발성의 F0·jitter·shimmer |
| 숫자 세기 | 발화 속도, 침묵 비율 |

#### 데이터 수집 과정
- **방법**: 웹 기반 크라우드소싱 플랫폼 (스마트폰·웹브라우저 모두 가능)
- **장비**: 참여자 보유 스마트폰 또는 PC 마이크 (비표준 환경)
- **프로토콜**: 웹사이트 접속 후 9개 표준 과제를 순서대로 수행

#### 피실험자 모집
- **규모**: 2,746명 (COVID-19 확진자·일반인·유증상자 혼합)
- **기준**: 자발적 참여, COVID-19 PCR 검사 결과 자가보고
- **모집 방법**: 온라인 공개 모집, 인도(IISc Bangalore) 주도 국제 모집

#### 피실험자에게 요구한 행동
9개 표준 발화·음향 과제:
1. 얕은 기침 3회
2. 깊은 기침 3회
3. 빠른 호흡 (30초)
4. 느린 호흡 (30초)
5. 지속 모음 /a/ (10초)
6. 지속 모음 /e/
7. 지속 모음 /o/
8. 숫자 1-20 세기
9. 표준 문장 읽기

#### 결과 분석
- **특징 추출**: MFCC, 멜스펙트로그램, Spectral Contrast
- **모델**: Random Forest (baseline) → 후속 연구에서 CNN·Audio MAE 적용
- **성능**: Audio MAE 기반 Coswara AUC=0.82

---

### [A5] PCOS 여성 음성 분석 — F0·MPT 임상 측정

**출처**: Aydin, K. et al. (2024). *Voice analysis in women with polycystic ovary syndrome*. The Egyptian Journal of Otolaryngology (Springer).

#### 사용 바이오마커
| 특징 | 설명 |
|------|------|
| F0 (기본 주파수) | 목소리의 평균 높이 — PCOS에서 안드로겐↑ → F0 감소 예상 |
| Jitter | 연속 성대 진동 주기 간 변동성 |
| Shimmer | 연속 성대 진동 진폭 간 변동성 |
| MPT | Maximum Phonation Time — 최대 발성 지속 시간 |
| HNR | Harmonics-to-Noise Ratio — 성대 규칙성 |
| RAP | Relative Average Perturbation (jitter 세부 지표) |

#### 데이터 수집 과정
- **장비**: MDVP (Multi-Dimensional Voice Program, Kay PENTAX)
- **환경**: 이비인후과 임상 음성 검사실
- **프로토콜**: 30 cm 거리에서 마이크에 대고 지속 모음 /a/ 발성

#### 피실험자 모집
- **규모**: PCOS 환자 + 연령 매칭 건강 대조군 (수십~수백 명 규모)
- **PCOS 기준**: Rotterdam criteria 충족 + 부인과 초음파·혈액 호르몬 확인
- **제외 기준**: 성대 질환, 갑상선 질환, 기타 내분비 질환 보유자

#### 피실험자에게 요구한 행동
- 마이크 30 cm 거리에서 **지속 모음 /a/를 편안한 음량으로 5초 이상 발성**
- MDVP 소프트웨어로 즉시 분석

#### 결과 분석
- **특징 추출**: MDVP, Praat
- **분석 방법**: t-test, Mann-Whitney U 검정 (그룹 간 비교)
- **성능**: PCOS군에서 F0 감소 경향, MPT 단축, RAP 증가 통계적 유의 확인  
  *※ ML 분류 정확도가 아닌 통계적 집단 차이 보고 연구*

---

### [A6] 제2형 당뇨병 예측 — 스마트폰 자가 녹음 음성

**출처**: Kaufman, J.M. et al. (2023). *Acoustic Analysis and Prediction of Type 2 Diabetes Mellitus Using Smartphone-Recorded Voice Segments*. Mayo Clinic Proceedings: Digital Health.

#### 사용 바이오마커
| 특징 | 설명 |
|------|------|
| F0 | 기본 주파수 (당뇨성 신경병증 → 성대 근육 이상 연관) |
| Jitter / Shimmer / HNR | 성대 규칙성 지표 |
| MFCC | 멜 주파수 켑스트럼 계수 |
| 포먼트 떨림 | formant tremor (불수의적 진동) |

#### 데이터 수집 과정
- **방법**: 참여자가 자신의 **스마트폰으로 자가 녹음** (원격·비임상 환경)
- **프로토콜**: 앱을 통해 표준 문장을 6-10초간 읽도록 안내
- **반복**: 주 2회, 수 주에 걸쳐 반복 녹음 (longitudinal)

#### 피실험자 모집
- **규모**: 267명 (약 18,000건 이상의 음성 클립)
- **기준**: T2DM 진단 환자 + 비당뇨 대조군
- **모집 방법**: 온라인 디지털 헬스 플랫폼 등록

#### 피실험자에게 요구한 행동
- 스마트폰 앱을 열고 표준 문장을 **6-10초간 읽어서 녹음**
- 특별한 장비·환경 불필요 (자택, 직장 등 일상 환경)

#### 결과 분석
- **특징 추출**: openSMILE (eGeMAPS 특징셋)
- **전처리**: VAD, 정규화
- **모델**: 로지스틱 회귀 + 앙상블
- **성능**: 여성 정확도 75%, 남성 정확도 70% (위험인자 결합 시)  
  *※ 최초 보고치 89%/86%는 검증 오류로 수정된 수치 적용*

---

### [A7] ALS 구음장애 중증도 — 어텐션 딥러닝 임상 평가

**출처**: Stegmann, G. et al. (2025). *Clinical assessment and interpretation of dysarthria in ALS using attention based deep learning AI models*. npj Digital Medicine (Nature).

#### 사용 바이오마커
- **멜스펙트로그램**: 음성 신호 전체를 시각적 표현으로 변환 → 어텐션 가중치로 병리 구간(음소·호흡음) 자동 식별
- **임상 해석 지표**: 어텐션 맵에서 'r' 영향 모음(car, more)의 발음 왜곡 정도

#### 데이터 수집 과정
- **장비**: 임상 마이크 (표준 임상 녹음)
- **환경**: 신경과 또는 재활의학 클리닉
- **라벨링**: 3명의 언어병리사(SLP)가 100점 척도로 구음장애 중증도 평가

#### 피실험자 모집
- **규모**: ALS 환자 125명, 2,102개 녹음 클립
- **기준**: 신경과 전문의에게 ALS 확진된 환자; 다양한 중증도(경증~중증 구음장애)

#### 피실험자에게 요구한 행동
- **단어·문장 읽기 과제**: "car," "more" 등 /r/ 영향 모음이 포함된 표준 단어·문장 목록 읽기
- 각 발화는 수 초 단위로 녹음·분절

#### 결과 분석
- **전처리**: 멜스펙트로그램 변환, 정규화
- **모델**: Attention 기반 CNN-Transformer 하이브리드 (회귀 모드)
- **실험 설계**: 화자 독립(speaker-independent) 분할
- **성능**: 구음장애 중증도 예측 R²=0.92, RMSE=6.78 (100점 척도 기준)

---

## 요약 비교표

### 영상 연구

| 연구 | 바이오마커 | 피실험자 수 | 수집 방법 | 수행 과제 | 모델 | 성능 |
|------|----------|-----------|---------|---------|------|------|
| V1 BiliScreen 2017 | 공막 황달 색상 | 70명 | 스마트폰 + 색보정 박스 | 색보정 부속품 착용 후 눈 촬영 | 색상 회귀 + ML | AUC ~0.93 (sens 89.7%) |
| V2 PCOS 공막 2021 | 공막 혈관 패턴 | 721명 | 임상 카메라 | 정면 눈 촬영 | ResNet-18 + MIL | AUC 0.979 |
| V3 FaceAge 2025 | 생물학적 나이 | 58,851+6,196명 | 디지털 사진 | 정면 사진 촬영 | CNN 회귀 | 예후 AUC 0.80 |
| V4 TAO CAS 2022 | 안와 주변 염증 징후 | 다기관 | 임상 디지털 카메라 | 정면 응시 촬영 | ResNet-18 앙상블 | AUC 0.884~0.977 |
| V5 PD 표정 2021 | 표정 동역학 | 107+1,595명 | YouTube 공개 비디오 | 자연 셀피 (특별 과제 없음) | CNN | AUC 0.71 |
| V6 DeepStroke 2022 | 안면 비대칭 + 음성 | ER 코호트 | 카메라+마이크 (응급실) | 표정 동작 + 발화 | 멀티모달 적대적 DL | Sens 93.12% |
| V7 AcneDet 2022 | 여드름 병변 유형·수 | 1,572장 | 스마트폰 | 정면 얼굴 촬영 | Faster R-CNN + LightGBM | 중증도 AUC 0.85 |

### 음성 연구

| 연구 | 바이오마커 | 피실험자 수 | 수집 방법 | 수행 과제 | 모델 | 성능 |
|------|----------|-----------|---------|---------|------|------|
| A1 Naranjo 2025 (PD) | jitter/shimmer/HNR/MFCC | 188+64명 | AKG 마이크, 방음실 | /a/ 5초 지속 발성 | BiLSTM | AUC 0.97 |
| A2 ADReSS 2020 (AD) | eGeMAPS/MFCC/비언어 | 78+78명 | 임상 마이크 16kHz | Cookie Theft 그림 묘사 | SVM/CNN | 최상위 Acc 89.6% |
| A3 양극성 2016 | spectral flux/포먼트/LPC | 28명 (121일) | 스마트폰 일상 통화 | 일상 전화 (과제 없음) | Random Forest | 조증 AUC 0.89 |
| A4 Coswara 2020 (COVID) | MFCC/기침·호흡 스펙트럼 | 2,746명 | 웹 크라우드소싱 | 기침·호흡·모음·숫자 9과제 | CNN/Audio MAE | AUC 0.82 |
| A5 Aydin 2024 (PCOS) | F0/jitter/shimmer/MPT/HNR | PCOS+대조군 | MDVP (임상 음성 분석기) | /a/ 지속 발성 | 통계 검정 | 유의미한 집단 차이 |
| A6 Kaufman 2023 (T2DM) | F0/jitter/MFCC/포먼트 | 267명 (18,000+ 클립) | 스마트폰 자가 녹음 | 표준 문장 6-10초 읽기 | 로지스틱 회귀+앙상블 | 여성 Acc 75% |
| A7 Stegmann 2025 (ALS) | 멜스펙트로그램 + 어텐션 | 125명 (2,102 녹음) | 임상 마이크 | 표준 단어·문장 읽기 | CNN-Transformer | R²=0.92 |

---

*작성: 2026-05-08 | 출처: mHealth_biomarker_research/_workspace3/ 문헌 탐색 결과 기반*
