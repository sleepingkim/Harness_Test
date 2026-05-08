# 논문 의학용어·평가지표·줄임말 가이드

**대상 논문:** "Smartphone Camera-Based Multimodal Biomarker Framework for AI-Driven Prediction of PCOS and Endometriosis"  
**작성일:** 2026-04-16  
**목적:** 논문에 등장하는 전문 용어를 비전문가도 이해할 수 있도록 의미·쓰임새·맥락 설명

---

## 1. 질환 관련 의학용어

| 용어               | 원문                                | 설명                                                                            |
| ---------------- | --------------------------------- | ----------------------------------------------------------------------------- |
| **다낭성난소증후군**     | PCOS (Polycystic Ovary Syndrome)  | 배란 장애·안드로겐 과잉·다낭성 난소 소견 중 2개 이상을 만족하는 흔한 내분비 질환. 가임기 여성의 8-13% 이환             |
| **자궁내막증**        | Endometriosis                     | 자궁 내막 조직이 자궁 외부(복막, 난소 등)에 자라는 질환. 만성 골반통·불임의 주요 원인, 가임기 여성의 6-10% 이환         |
| **선근증**          | Adenomyosis                       | 자궁 내막 조직이 자궁근층 내부로 침투하는 질환. 자궁내막증과 유사한 자율신경계 변화 동반                            |
| **Rotterdam 기준** | Rotterdam Criteria                | PCOS 진단 국제 표준. ① 희발배란 또는 무배란, ② 임상적·생화학적 고안드로겐혈증, ③ 다낭성 난소 소견 중 2개 이상 충족 시 진단 |
| **rASRM 병기**     | rASRM Stages I-IV                 | 미국생식의학회(ASRM)가 제정한 자궁내막증 병기 분류. I (최소) → II (경증) → III (중등도) → IV (중증)        |
| **고안드로겐혈증**      | Hyperandrogenism                  | 남성호르몬(안드로겐) 과잉 상태. PCOS의 대표 증상으로 여드름·다모증·탈모 유발                                |
| **인슐린 저항성**      | Insulin Resistance                | 인슐린에 대한 세포 반응 저하. PCOS 환자의 주요 대사 이상으로, 흑색극세포증과 밀접히 연관                         |
| **흑색극세포증**       | Acanthosis Nigricans (AN)         | 목·겨드랑이·사타구니 피부가 검게 두꺼워지는 현상. 인슐린 저항성의 피부 징후로 PCOS에서 자주 관찰                     |
| **다모증**          | Hirsutism                         | 여성에게 남성형 체모(얼굴·턱·배 등)가 과도하게 자라는 증상. 안드로겐 과잉의 대표적 임상 징후                        |
| **자율신경계**        | ANS (Autonomic Nervous System)    | 의식적 제어 없이 심박·혈압·소화 등을 조절하는 신경계. 교감신경(긴장·각성)과 부교감신경(이완·회복)으로 구성                |
| **교감신경 항진**      | Sympathetic Overactivation        | 스트레스 반응("fight or flight") 시스템이 과도하게 활성화된 상태. PCOS에서 LF/HF 상승으로 확인            |
| **미주신경 저하**      | Vagal Tone Reduction              | 부교감신경(미주신경) 활성도 감소. 자궁내막증에서 RMSSD·HF 감소로 확인                                   |
| **복강경**          | Laparoscopy                       | 자궁내막증의 금표준 진단법. 전신마취 후 복부에 소형 카메라를 삽입해 병변을 직접 확인                              |
| **혈압 SBP/DBP**   | Systolic/Diastolic Blood Pressure | 수축기 혈압(심장이 뛸 때) / 이완기 혈압(심장이 쉴 때). 논문에서 rPPG로 측정 시도                           |

---

## 2. 기술 및 공학 용어

| 용어 | 원문 | 설명 |
|------|------|------|
| **원격 광혈류 측정법** | rPPG (Remote Photoplethysmography) | 카메라로 얼굴 피부색의 미세 변화를 감지해 비접촉으로 심박·혈류 신호를 추출하는 기술. 일반 스마트폰 카메라로 구현 가능 |
| **심박변이도** | HRV (Heart Rate Variability) | 연속 심박 간격(R-R interval)의 변동성. 자율신경계 기능의 비침습적 지표. 높을수록 건강한 자율신경 반응 |
| **심전도** | ECG (Electrocardiogram) | 심장의 전기 신호를 기록하는 표준 검사. 논문에서 rPPG의 정확도 비교 기준으로 사용 |
| **광혈류 측정법** | PPG (Photoplethysmography) | 피부에 빛을 쏘아 혈류량 변화를 측정하는 방식. 스마트워치·핏빗의 심박 측정 원리 |
| **심박 간격** | IBI (Inter-Beat Interval) | 연속적인 두 심박 사이의 시간 간격. HRV 계산의 기초 단위 |
| **신호 품질 지수** | SQI (Signal Quality Index) | rPPG 신호의 신뢰도를 0-1로 수치화한 지표. 논문에서 SQI < 0.6이면 재촬영 권고 |
| **크로미넌스 기반 방법** | CHROM (Chrominance-based method) | 피부 반사율의 색조 성분(크로미넌스)을 이용해 rPPG 신호를 분리하는 알고리즘. 조명 변화에 강건함 |
| **독립성분분석** | ICA (Independent Component Analysis) | 여러 혼합 신호에서 독립적인 원천 신호를 분리하는 통계 방법. 초기 rPPG 처리에 사용 |
| **공간-시간 맵** | Spatial-Temporal Map | 비디오에서 피부 영역의 색상 변화를 공간(x축: 위치)×시간(y축: 프레임) 행렬로 변환한 표현 |
| **관심 영역** | ROI (Region of Interest) | rPPG 신호 추출 시 분석 대상으로 삼는 피부 영역(이마·양 볼). MediaPipe 랜드마크로 자동 추출 |
| **DermScore** | PCOS-DermScore | 논문이 제안하는 피부 표현형 복합 점수. 여드름(IGA) + 다모증(mFG) + AN + 얼굴BMI를 합산한 16차원 벡터 |
| **Cross-Attention Fusion** | Cross-Attention Fusion | 서로 다른 모달리티(HRV·피부·월경) 간 쌍방향 어텐션으로 상호작용을 학습하는 딥러닝 융합 기법 |
| **연합 학습** | Federated Learning | 원본 데이터를 서버로 보내지 않고 모델 파라미터(가중치)만 공유해 여러 기관이 협력 학습하는 방식 |
| **온디바이스 처리** | On-device Processing | 클라우드 서버로 전송하지 않고 스마트폰 내부에서 직접 신호 처리·추론하는 방식. 프라이버시 보호에 핵심 |
| **Privacy-by-Design** | Privacy-by-Design | 시스템 설계 단계부터 개인정보 보호를 내재화하는 원칙 (사후 추가가 아닌 기본값으로 적용) |
| **전달학습** | Transfer Learning | 공개 데이터셋으로 사전학습된 모델을 새 과제(PCOS 분류 등)에 미세조정(fine-tuning)하는 방법 |
| **의료 소프트웨어** | SaMD (Software as Medical Device) | 독립적으로 의료 목적을 수행하는 소프트웨어. FDA·CE 등의 규제 대상 |

---

## 3. HRV 지표 (심박변이도 세부 측정값)

### 시간영역 지표

| 지표 | 원문 | 설명 | 논문 내 의미 |
|------|------|------|------------|
| **SDNN** | Standard Deviation of NN intervals | 전체 심박 간격의 표준편차. 전반적인 자율신경 기능 반영 | PCOS에서 SMD -0.763 (유의하게 감소) |
| **RMSSD** | Root Mean Square of Successive Differences | 연속 심박 간격 차이의 제곱평균제곱근. 부교감신경(미주신경) 활성도의 주요 지표 | 자궁내막증에서 유의하게 감소 |
| **pNN50** | Percentage of NN intervals > 50ms | 연속 심박 간격 차이가 50ms 초과인 비율. 부교감신경 활성 반영 | 자궁내막증에서 감소 |
| **meanRR** | Mean RR Interval | 평균 심박 간격(ms). 평균 심박수의 역수 | 기저 심박수 파악에 활용 |

### 주파수영역 지표

| 지표 | 원문 | 설명 | 논문 내 의미 |
|------|------|------|------------|
| **LF** | Low Frequency Power (0.04-0.15 Hz) | 저주파 성분. 교감신경과 부교감신경이 혼재, 주로 압반사 활성 반영 | PCOS에서 상승 |
| **HF** | High Frequency Power (0.15-0.4 Hz) | 고주파 성분. 순수 부교감신경(호흡 리듬) 반영 | PCOS·자궁내막증에서 감소 |
| **LF/HF** | LF to HF Ratio | 교감-부교감 신경 균형 지표. 높을수록 교감신경 우세 | PCOS에서 SMD +0.670 (유의하게 상승) |
| **HFnu** | HF Normalized Units | HF를 전체 파워로 나눈 정규화값. 부교감신경 기여 비율 | PCOS에서 SMD -0.873 (유의하게 감소) |

---

## 4. AI·통계 평가지표

| 지표 | 원문 | 설명 | 논문 내 맥락 |
|------|------|------|------------|
| **AUC** | Area Under the ROC Curve | ROC 곡선 아래 면적. 0.5(무작위) ~ 1.0(완벽). 0.8 이상이면 임상적으로 유용 | 융합 모델 목표 macro-AUC 0.80-0.90 |
| **민감도** | Sensitivity (Recall) | 실제 환자 중 검사가 양성으로 잡아내는 비율. 높을수록 환자를 놓치지 않음 | AN 탐지 81.1% |
| **특이도** | Specificity | 실제 정상인 중 검사가 음성으로 정확히 판별하는 비율. 높을수록 과잉진단 없음 | AN 탐지 70.3% |
| **MAE** | Mean Absolute Error | 예측값과 실제값 차이의 절댓값 평균. 낮을수록 정확 | 얼굴 BMI MAE 1.04 |
| **RMSE** | Root Mean Square Error | 오차 제곱의 평균에 제곱근. MAE보다 큰 오차에 더 민감 | rPPG SpO₂ RMSE 1.710% |
| **SMD** | Standardized Mean Difference | 두 집단 평균 차이를 표준편차로 나눈 표준화 효과 크기. |SMD| > 0.5이면 중간 효과 | PCOS LF/HF SMD +0.670 |
| **ICC** | Intraclass Correlation Coefficient | 동일 대상을 반복 측정할 때의 일관성(급내 상관계수). 1에 가까울수록 신뢰도 높음 | 여드름 AI ICC 0.8 |
| **Cohen's κ** | Cohen's Kappa | 우연 일치를 보정한 평가자 간 일치도. 0.6 이상이면 실질적 일치 | 다모증 mFG κ=0.75 |
| **mAP** | mean Average Precision | 물체 탐지 모델의 정밀도-재현율 곡선 아래 면적 평균. 높을수록 탐지 성능 우수 | 여드름 탐지 mAP 0.54 |
| **F1** | F1 Score | 정밀도(Precision)와 재현율(Recall)의 조화평균. 불균형 클래스에서 정확도보다 신뢰성 있음 | 모델 평가지표로 언급 |
| **macro-AUC** | Macro-averaged AUC | 다중 클래스 분류에서 클래스별 AUC를 단순 평균한 값 | 3-class 목표 0.80-0.90 |
| **SHAP** | SHapley Additive exPlanations | 게임이론 기반 특성 중요도 설명법. 모델의 예측에 각 특성이 얼마나 기여했는지 수치화 | 모델 해석가능성 확보 |
| **Grad-CAM** | Gradient-weighted Class Activation Mapping | CNN의 어떤 공간 영역이 예측에 중요했는지 열지도로 시각화하는 기법 | 피부 분석 모듈 어텐션 시각화 |

---

## 5. 임상 평가 척도

| 척도 | 원문 | 설명 | 논문 내 사용 |
|------|------|------|------------|
| **IGA** | Investigator's Global Assessment | 여드름 중증도 5단계 평가(0=정상, 4=중증). 피부과 임상 표준 | 스마트폰 AI의 여드름 등급화 성능 기준 |
| **mFG 점수** | Modified Ferriman-Gallwey Score | 신체 9개 부위의 체모를 0-4점으로 평가해 합산(≥8점=다모증). 국제 표준 다모증 측정법 | 이미지 기반 다모증 점수화의 비교 기준 |
| **VAS** | Visual Analog Scale | 통증 강도를 0-100mm 선 위에 표시하는 자기보고 척도. 자궁내막증 통증 정량화에 사용 | Module C 월경 데이터 수집 항목 |
| **Fitzpatrick 유형** | Fitzpatrick Skin Type | 피부색을 I(매우 밝음)~VI(매우 어두움)으로 분류하는 국제 표준. rPPG 정확도는 V-VI에서 저하 | 피부색 편향 분석·완화 기준 |

---

## 6. 연구 방법론 줄임말

| 줄임말 | 원문 | 설명 |
|-------|------|------|
| **PICO** | Population, Intervention, Comparison, Outcome | 체계적 문헌 탐색의 표준 프레임워크. 연구 질문을 4요소로 구조화 |
| **PRISMA** | Preferred Reporting Items for Systematic Reviews and Meta-Analyses | 체계적 문헌 고찰 보고 국제 표준 지침 |
| **SR** | Systematic Review | 체계적 문헌 고찰. 사전 정의된 기준으로 모든 관련 연구를 포괄적으로 검토 |
| **RCT** | Randomized Controlled Trial | 무작위 대조 시험. 임상 증거 최고 수준 |
| **CI** | Confidence Interval | 신뢰구간. 모수의 참값이 해당 범위에 포함될 확률(보통 95%) |
| **d** | Cohen's d | 효과 크기 지표. 0.2=소, 0.5=중간, 0.8=대 효과 |

---

## 7. AI 모델 구성요소

| 용어 | 원문 | 설명 |
|------|------|------|
| **1D-CNN** | 1D Convolutional Neural Network | 1차원 시계열(HRV 신호) 특징 추출에 사용하는 합성곱 신경망 |
| **Transformer** | Transformer Encoder | 어텐션 메커니즘 기반 시퀀스 모델. 시계열 HRV 패턴 인코딩에 사용 |
| **LSTM** | Long Short-Term Memory | 장기 의존성을 처리하는 순환 신경망. 월경 주기 패턴 학습에 사용 |
| **TCN** | Temporal Convolutional Network | 확장 인과 합성곱으로 장기 시계열 패턴을 효율적으로 처리. 통증 패턴 인코딩에 사용 |
| **EfficientNet-B0** | EfficientNet-B0 | 계산 효율과 정확도를 균형 있게 최적화한 CNN 아키텍처. 피부 분석에 사용 |
| **ResNet50** | Residual Network 50 layers | 잔차 연결로 학습을 안정화한 50층 CNN. 다모증·BMI 추정에 사용 |
| **LightGBM** | Light Gradient Boosting Machine | 빠른 속도와 낮은 메모리 사용의 그래디언트 부스팅 모델. 여드름 등급 분류에 사용 |
| **Faster R-CNN** | Faster Region-based CNN | 영역 제안 네트워크 기반 실시간 물체 탐지 모델. 여드름 병변 위치 탐지에 사용 |
| **MediaPipe** | MediaPipe Face Mesh | Google의 실시간 얼굴 랜드마크 468개 추출 프레임워크. ROI 선택에 사용 |
| **TensorFlow Lite** | TensorFlow Lite | 모바일 기기용 경량 TensorFlow. Android 온디바이스 추론 |
| **Core ML** | Core ML | Apple의 모바일 머신러닝 프레임워크. iOS 온디바이스 추론 |
| **Dropout** | Dropout | 훈련 중 무작위로 뉴런을 비활성화해 과적합을 방지하는 정규화 기법 (p=0.3 적용) |

---

## 8. 공개 데이터셋

| 데이터셋 | 용도 | 설명 |
|---------|------|------|
| **UBFC-rPPG** | rPPG 사전학습 | rPPG 벤치마크 공개 데이터셋. Module A 사전학습에 사용 |
| **ACNE04** | 여드름 탐지 사전학습 | 4단계 여드름 등급 레이블이 있는 공개 데이터셋 |
| **CelebA** | BMI 추정 사전학습 | 20만 장 이상의 유명인 얼굴 이미지 데이터셋 |
| **PURE** | rPPG 벤치마크 | 다양한 움직임 조건의 얼굴 rPPG 공개 데이터셋 |

---

## 9. 규제·법률 용어

| 줄임말 | 원문 | 설명 |
|-------|------|------|
| **FDA** | U.S. Food and Drug Administration | 미국 식품의약국. SaMD 허가 기관 |
| **GDPR** | General Data Protection Regulation | EU 일반 개인정보 보호 규정. 생체 데이터 처리에 엄격한 규제 |
| **PIPA** | Personal Information Protection Act | 한국 개인정보 보호법 |
| **HIPAA** | Health Insurance Portability and Accountability Act | 미국 의료정보 보호법 |
| **AF** | Atrial Fibrillation | 심방세동. FibriCheck이 FDA 승인 받은 적응증 |

---

## 10. 바이오마커 평가 기준 (5차원 매트릭스)

| 차원 | 약어 | 설명 | 평가 기준 (1-5점) |
|------|------|------|-----------------|
| **기술 준비도** | TRL (Technology Readiness Level) | 기술의 성숙 정도 (1=개념, 5=실제 검증) | 5=임상 검증 완료, 1=이론 단계 |
| **임상 타당성** | CV (Clinical Validity) | 질환과의 연관성 근거 강도 | 5=메타분석 근거, 1=가설 수준 |
| **실용성** | PR (Practicality) | 일상 환경 측정 가능성, 사용자 부담 | 5=완전 비침습·스마트폰 가능, 1=입원 필요 |
| **데이터 가용성** | DA (Data Availability) | 공개 데이터셋·사전학습 자원 유무 | 5=대규모 공개 데이터 존재, 1=없음 |
| **규제 친화성** | RF (Regulatory Friendliness) | FDA·CE 허가 경로의 용이성 | 5=기존 승인 경로 명확, 1=규제 불확실 |

**Tier 분류 기준:**
- **Tier 1** (≥18점): 즉시 적용 가능한 핵심 바이오마커
- **Tier 2** (13-17점): 추가 검증 필요한 유망 바이오마커  
- **Tier 3** (7-12점): 탐색적 연구 단계의 바이오마커
