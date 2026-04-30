# 얼굴 영상 기반 질병 예측 디지털 바이오마커 문헌 탐색 보고서

**탐색 일자**: 2026-04-29
**탐색 DB**: PubMed, IEEE Xplore, Google Scholar, Semantic Scholar, arXiv, Nature/Springer, MDPI, Lancet Digital Health, Frontiers
**최종 선정 논문 수**: 32편
**작성자**: face-voice-research 하네스 (얼굴 영상 문헌 탐색 에이전트)

---

## 1. 탐색 개요

### 검색 전략

본 보고서는 14개 핵심 키워드 조합을 활용해 웹 검색(PubMed, Nature, Science Direct, IEEE Xplore, Lancet, Frontiers, MDPI, arXiv 등)으로 실제 논문을 탐색하고, 얼굴의 시각적 외형 특징(피부, 눈, 표정, 얼굴 기하학)을 AI로 분석해 질병을 예측·진단하는 연구를 체계적으로 수집하였다.

검색 키워드(영문, 본 탐색에서 실제 사용):
1. acne severity grading deep learning PCOS hormonal facial image
2. facial image disease prediction CNN dermatology multi-disease
3. conjunctiva anemia detection smartphone image deep learning
4. scleral jaundice detection deep learning bilirubin image
5. exophthalmos thyroid eye disease detection deep learning AI
6. facial hypomimia Parkinson disease detection facial expression deep learning
7. face photo biological age prediction deep learning health (FaceAge, IMDB-WIKI/UTKFace)
8. periorbital edema detection facial image deep learning hypothyroidism
9. facial expression depression detection action unit deep learning
10. skin lesion classification melanoma deep learning ISIC HAM10000
11. diabetes facial feature detection deep learning image
12. wrinkle analysis aging disease prediction deep learning skin
13. facial asymmetry stroke neurological detection deep learning
14. PCOS facial phenotype machine learning hirsutism detection
15. (추가) genetic syndrome facial recognition DeepGestalt Face2Gene
16. (추가) acromegaly Cushing syndrome facial recognition deep learning
17. (추가) facial dermatitis rosacea eczema deep learning CNN
18. (추가) cardiovascular disease facial image deep learning prediction
19. (추가) pain detection facial expression neural network newborn

### 포함/제외 기준

- **포함:**
  - 얼굴의 시각적 외형 특징(피부 상태, 여드름, 주름, 피부색, 눈/공막, 표정, 얼굴 기하학)을 AI(CNN, ResNet, EfficientNet, Vision Transformer 등) 또는 ML로 분석
  - 질병/생리학적 상태(PCOS, 갑상선 질환, 빈혈, 황달, 당뇨, 파킨슨, 우울, 피부암, 심혈관, 뇌졸중, 노화 등)와 연관된 예측·진단·중증도 평가
  - 디지털 카메라/스마트폰/임상 카메라로 촬영된 정지 이미지 또는 비디오
- **제외:**
  - rPPG(원격 광혈류측정) 기반 심박/HRV 측정 연구
  - 혈류 신호 기반 연구(헤모글로빈 분광 등)
  - 피부 외 부위(망막 fundus 단독 사용 연구는 비교 맥락에서만 언급)
  - 얼굴 외 부위만 다룬 연구(피부경 dermoscopy 단독은 멜라노마 섹션에 한해 비교 포함)

---

## 2. 피부 분석 기반 바이오마커

### 2.1 여드름/다모증 — 호르몬 관련 질환 (PCOS 등)

#### [논문 1] Automatic Acne Object Detection and Acne Severity Grading Using Smartphone Images and Artificial Intelligence (AcneDet)
- **저자/연도/게재지**: Huynh et al., 2022, Diagnostics (MDPI), 12(8):1879
- **바이오마커**: 4종 여드름 병변 객체(blackheads/whiteheads, papules/pustules, nodules/cysts, acne scars)의 개수·위치 + Investigator's Global Assessment(IGA) 5단계 중증도
- **데이터 수집**: iOS·Android 스마트폰으로 촬영, 다양한 조명, 임상·실생활 환경
- **데이터셋**: 1,572장 얼굴 이미지, 4명의 피부과 전문의가 라벨링
- **전처리**: Faster R-CNN 기반 객체 검출용 bounding box 라벨링
- **모델**: Faster R-CNN (객체 검출) + LightGBM (중증도 등급화)
- **학습**: 표준 Faster R-CNN 학습 절차, 사전학습 ImageNet
- **실험 설계**: train/val/test 분할 (구체적 비율 비공개), 다중 등급화
- **성능**: 4종 객체 mAP=0.54; 5단계 중증도 평균 AUC=0.85
- **코드/데이터 공개**: 아니오
- **한계점**: 단일 데이터셋, 외부 검증 부재, 다민족 다양성 부족
- **증거 수준**: Moderate
- 출처: https://www.mdpi.com/2075-4418/12/8/1879

#### [논문 2] Development and Accuracy of an Artificial Intelligence Algorithm for Acne Grading from Smartphone Photographs
- **저자/연도/게재지**: Seité et al., 2019, Clinical, Cosmetic and Investigational Dermatology
- **바이오마커**: 여드름 GEA(Global Evaluation of Acne) 척도, 병변 유형(comedones, papules, pustules)
- **데이터 수집**: 스마트폰 셀피, 실생활 환경
- **데이터셋**: 5,972장 (5,972 얼굴), 2명의 피부과 전문의 라벨
- **전처리**: 얼굴 검출, 정규화, 데이터 증강
- **모델**: CNN (구조 비공개)
- **성능**: 알고리즘과 피부과 전문의 간 GEA 등급 일치율 r=0.74
- **공개**: 아니오
- **한계점**: 스마트폰 이미지 품질 편차
- **증거 수준**: Moderate
- 출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC6972662/

#### [논문 3] A Deep Learning-Based Facial Acne Classification System
- **저자/연도/게재지**: Lim et al., 2022, Clinical, Cosmetic and Investigational Dermatology, 15:851-861
- **바이오마커**: Korean Acne Grading System(KAGS) 기반 여드름 중증도(4단계)
- **데이터 수집**: 임상 카메라 정면·측면 얼굴 사진
- **데이터셋**: 1,213장 얼굴 이미지(시리즈), 환자 등급 라벨
- **전처리**: 얼굴 검출(Dlib 등), ROI 크롭, ImageNet 정규화, 회전·반전 증강
- **모델**: ResNet-152, ImageNet 사전학습
- **학습**: Adam, lr=1e-4, batch=16
- **성능**: Top-1 accuracy ≈ 67%, Top-2 accuracy ≈ 92%
- **공개**: 아니오
- **한계점**: 단일 인종, 데이터셋 소규모
- **증거 수준**: Moderate
- 출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC9109724/

#### [논문 4] Evaluation of an Acne Lesion Detection and Severity Grading Model for Chinese Population in Online and Offline Healthcare Scenarios
- **저자/연도/게재지**: 2024/2025, Scientific Reports (Nature)
- **바이오마커**: 여드름 병변 검출 + 중증도 등급
- **데이터 수집**: 온/오프라인 의료 환경 모두; 스마트폰 + 임상 카메라
- **데이터셋**: 다중 수천 장(원문 기재); 중국인 인구
- **모델**: CNN 기반 객체 검출 + 분류
- **성능**: 임상 시나리오에서 dermatologist 수준의 일치도 보고
- **공개**: 아니오
- **한계점**: 단일 인종(중국), 외부 검증 제한
- **증거 수준**: Moderate
- 출처: https://www.nature.com/articles/s41598-024-84670-z

#### [논문 5] Automated Grading of Acne Vulgaris by Deep Learning with Convolutional Neural Networks
- **저자/연도/게재지**: Wu et al., 2019, Skin Research and Technology
- **바이오마커**: Pillsbury 4단계 여드름 중증도
- **데이터 수집**: 표준화된 임상 사진
- **데이터셋**: 5,871장 얼굴 이미지(중국 환자)
- **모델**: ResNet-50, ImageNet 사전학습
- **성능**: Top-1 accuracy ~81%, Cohen's κ 전문의 수준
- **한계점**: 외부 검증 필요
- **증거 수준**: Moderate
- 출처: https://pubmed.ncbi.nlm.nih.gov/31565821/

#### [논문 6] DED: Diagnostic Evidence Distillation for Acne Severity Grading on Face Images
- **저자/연도/게재지**: 2024, Pattern Recognition (Elsevier)
- **바이오마커**: 병변 카운트 기반 IGA 등급
- **모델**: Knowledge distillation; teacher-student CNN
- **성능**: 기존 CNN baseline 대비 정확도 향상
- **공개**: 일부
- **증거 수준**: Moderate
- 출처: https://www.sciencedirect.com/science/article/abs/pii/S095741742300814X

### 2.2 피부색/황달 분석

#### [논문 7] BiliScreen: Smartphone-Based Scleral Jaundice Monitoring for Liver and Pancreatic Disorders
- **저자/연도/게재지**: Mariakakis et al., 2017, ACM IMWUT, Vol. 1, No. 2
- **바이오마커**: 공막(sclera) 색상(노란빛) → 빌리루빈 수준 추정
- **데이터 수집**: 스마트폰 카메라 + 색보정 부속품(블루박스, 종이 글래스)
- **데이터셋**: 70명의 임상 피험자
- **전처리**: 얼굴/공막 검출, 색공간 변환, 색보정 액세서리
- **모델**: 색공간 회귀(linear/nonlinear regression) + 머신러닝
- **성능**: 임상 기준 빌리루빈 ≥ 3 mg/dL 검출 sens 89.7%, spec 96.8% (정상 vs 환자)
- **공개**: 아니오(시스템 설명서 공개)
- **한계점**: 색보정 부속품 필요
- **증거 수준**: Moderate-High
- 출처: https://dl.acm.org/doi/abs/10.1145/3090085

#### [논문 8] Deep-Learning-Based Smartphone Application for Self-Diagnosis of Scleral Jaundice in Patients with Hepatobiliary and Pancreatic Diseases
- **저자/연도/게재지**: Kim et al., 2021, Journal of Personalized Medicine, 11(9):928
- **바이오마커**: 스마트폰 공막 사진 → 총 빌리루빈 회귀 예측
- **데이터 수집**: 스마트폰, 표준 조명/색보정
- **데이터셋**: 입원 환자 사진 + 혈청 빌리루빈 페어
- **전처리**: 얼굴/눈 검출(MTCNN), 공막 ROI 분할(U-Net), A4 화이트밸런스 보정
- **모델**: ResNet 기반 회귀(딥 회귀)
- **성능**: 스마트폰 기반 빌리루빈 추정과 혈청값 간 강한 상관(r 보고)
- **공개**: 아니오
- **한계점**: 병원 환경 검증
- **증거 수준**: Moderate
- 출처: https://www.mdpi.com/2075-4426/11/9/928

#### [논문 9] Non-Invasive Jaundice Screening Using AI: Machine Learning Analysis of Sclera and Urine Images
- **저자/연도/게재지**: 2025, Journal of Clinical Medicine, MDPI
- **바이오마커**: 공막 황달 + 소변 색상 + 결합
- **모델 비교**: Decision Tree, Random Forest, XGBoost, DeepSets, ResNet
- **성능**: DeepSets 빌리루빈 회귀 R²=0.782; 황달 검출 acc=87.1%, AUC=0.869, precision=90.2%, recall=88.1%
- **공개**: 아니오
- **증거 수준**: Moderate
- 출처: https://www.mdpi.com/2077-0383/14/9/3125

#### [논문 10] AI-Based Non-Invasive Bilirubin Prediction for Neonatal Jaundice Using 1D CNN
- **저자/연도/게재지**: 2025, Scientific Reports
- **바이오마커**: 신생아 얼굴(피부) 색상 → 빌리루빈
- **모델**: 1D CNN (color channel signals)
- **성능**: 임상 빌리루빈 회귀 정확도 보고
- **증거 수준**: Moderate
- 출처: https://www.nature.com/articles/s41598-025-96100-9

#### [논문 11] Neonatal Jaundice Detection Using a Vision Transformer-Based Deep Learning Model
- **저자/연도/게재지**: 2026, Scientific Reports
- **바이오마커**: 신생아 얼굴 사진 → 황달 이진 분류
- **모델**: Vision Transformer (ViT)
- **성능**: 정확도/민감도/특이도 보고(원문 참조)
- **증거 수준**: Moderate
- 출처: https://www.nature.com/articles/s41598-026-40515-5

### 2.3 피부 노화/주름

#### [논문 12] FaceAge: A Deep Learning System to Estimate Biological Age from Face Photographs to Improve Prognostication
- **저자/연도/게재지**: Bontempi et al., 2025, The Lancet Digital Health
- **바이오마커**: 얼굴 사진 기반 생물학적 나이(FaceAge) → 예후 예측
- **데이터 수집**: 디지털 사진(공개 + 임상)
- **데이터셋**: 학습 58,851명(IMDB-WIKI 56,304 + UTKFace 2,547); 임상 검증 6,196 암 환자(미국·네덜란드 2개 기관)
- **전처리**: 얼굴 검출 CNN(MTCNN 류), 정렬, 256×256
- **모델**: VGG/Inception 류 기반 두 단계 CNN(localization + age regression)
- **학습**: ImageNet 사전학습 → 회귀(L1/L2)
- **성능**: 암 환자 평균 FaceAge가 실제 연령보다 ~5세 높음; FaceAge 1년 증가당 사망 위험 HR 의미 있게 상승; 임상의 단독 예측 AUC 0.74 → +FaceAge 0.80
- **공개**: 코드 공개 (GitHub: AIM-Harvard/FaceAge)
- **한계점**: 인종/조명 편향, 화장·필터 영향
- **증거 수준**: High
- 출처: https://www.thelancet.com/journals/landig/article/PIIS2589-7500(25)00042-1/fulltext, https://github.com/AIM-Harvard/FaceAge

#### [논문 13] Decoding Biological Age from Face Photographs Using Deep Learning (FaceAge prelim)
- **저자/연도/게재지**: 2023, eLife / preprint then PMC10516042
- **바이오마커**: 얼굴 → 생물학적 나이
- **모델**: CNN regression(VGG-16 fine-tuned)
- **성능**: MAE ~ 4-5세
- **공개**: 모델 일부 공개
- **증거 수준**: High
- 출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC10516042/

#### [논문 14] A Deep Learning-Based Detection of Wrinkles on Skin
- **저자/연도/게재지**: 2022, Springer Lecture Notes
- **바이오마커**: 주름 픽셀 분할/계수 → 노화·피부 건강 등급
- **모델**: U-Net 변형
- **성능**: Pixel-wise IoU 보고
- **증거 수준**: Limited-Moderate
- 출처: https://link.springer.com/chapter/10.1007/978-981-16-9573-5_2

#### [논문 15] Striped WriNet: Automatic Wrinkle Segmentation Based on Striped Attention Module
- **저자/연도/게재지**: 2024, Biomedical Signal Processing and Control
- **바이오마커**: 깊은 주름 + 얇은 잔주름 분할
- **모델**: U-Net + Striped Attention
- **성능**: 분할 IoU/F1 향상
- **증거 수준**: Moderate
- 출처: https://www.sciencedirect.com/science/article/abs/pii/S1746809423012508

#### [논문 16] Evaluating Facial Dermis Aging in Healthy Caucasian Females with LC-OCT and Deep Learning
- **저자/연도/게재지**: 2024, Scientific Reports
- **바이오마커**: LC-OCT 영상 기반 진피 노화 → 시간적 나이 회귀
- **데이터셋**: 100명 (백인 여성 20-70세)
- **모델**: 3D ResNet-18
- **성능**: MAE = 4.2년, Pearson r = 0.93
- **증거 수준**: Moderate (모달리티가 LC-OCT라 일반 카메라와 차별)
- 출처: https://www.nature.com/articles/s41598-024-74370-z

---

## 3. 눈/결막 분석 기반 바이오마커

### 3.1 빈혈 — 결막 창백

#### [논문 17] Detection of Anemia Using Conjunctiva Images: A Smartphone Application Approach
- **저자/연도/게재지**: 2023, Smart Health (Elsevier)
- **바이오마커**: 안검 결막(palpebral conjunctiva) RGB·HSV 색상 → 헤모글로빈 추정
- **데이터 수집**: 스마트폰 카메라, 눈꺼풀 외번
- **데이터셋**: 임상 코호트(원문에 환자 N 명시); 결막 이미지
- **전처리**: 결막 ROI 분할, 색보정
- **모델**: CNN + 분류기 스택
- **성능**: 민감도 90%, 특이도 95%, 정확도 92.5%
- **공개**: 앱 시연 공개
- **한계점**: 멜라닌 영향 적으나 조명 변동 민감
- **증거 수준**: Moderate-High
- 출처: https://www.sciencedirect.com/science/article/pii/S2590093523000322

#### [논문 18] Deep Learning Model-Based Detection of Anemia from Conjunctiva Images
- **저자/연도/게재지**: 2025, Healthcare Informatics Research, 31(1):57
- **바이오마커**: 결막 이미지 → 빈혈(이진)
- **데이터셋**: 764장 → DCGAN 증강 4,315장
- **모델**: Stacking ensemble (VGG-16, ResNet-50, InceptionV3)
- **성능**: AUC = 0.97
- **공개**: 아니오
- **증거 수준**: Moderate
- 출처: https://e-hir.org/journal/view.php?number=1237

#### [논문 19] Non-Invasive Anemia Detection from Conjunctiva and Sclera Images Using Vision Transformer with Attention Map Explainability
- **저자/연도/게재지**: 2025, Scientific Reports
- **바이오마커**: 결막+공막 ROI 색상
- **모델**: Vision Transformer + transfer learning
- **성능**: 전체 정확도 98.47%
- **공개**: attention map 설명 제공
- **증거 수준**: Moderate-High
- 출처: https://www.nature.com/articles/s41598-025-32343-w

#### [논문 20] AnemiaVision: Non-Invasive Anemia Detection via Smartphone Imagery Using EfficientNet-B3
- **저자/연도/게재지**: 2026, arXiv:2604.22964
- **모델**: EfficientNet-B3 + TrivialAugmentWide + Mixup + RandomErasing
- **성능**: validation accuracy 94-97%
- **공개**: 코드 공개
- **증거 수준**: Moderate
- 출처: https://arxiv.org/html/2604.22964

#### [논문 21] Prediction of Anemia in Real-Time Using a Smartphone Camera Processing Conjunctival Images
- **저자/연도/게재지**: 2024, PLOS One
- **바이오마커**: 결막 이미지 헤모글로빈 회귀
- **모델**: CNN + ML
- **성능**: 헤모글로빈 추정 r 보고
- **증거 수준**: Moderate
- 출처: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0302883

### 3.2 황달 — 공막 황달
(2.2의 BiliScreen[7], DeepSets/ResNet[9], 신생아 ViT[11]가 본 항목과 중복 — 위 참조)

### 3.3 갑상선 질환 — 안구 돌출/안검 부종

#### [논문 22] Explainable Deep Learning System for Automatic Detection of Thyroid Eye Disease Using Facial Images
- **저자/연도/게재지**: 2025, American Journal of Ophthalmology
- **바이오마커**: 안와 주변 랜드마크 + TED 활성 임상 징후(눈꺼풀 부종, 결막 부종, 결막 충혈 등)
- **데이터 수집**: 임상 정면 얼굴 사진
- **데이터셋**: 다기관 환자/대조군 코호트
- **전처리**: Periocular landmark localization network
- **모델**: 두 단계 — landmark net + binary classification net (CNN)
- **성능**: AUC 0.997, sensitivity 99.7%, specificity 94.5%
- **공개**: 아니오
- **한계점**: 인종 편향, 화장 영향
- **증거 수준**: High
- 출처: https://www.sciencedirect.com/science/article/pii/S0002939425002582

#### [논문 23] Deep Learning–Driven Exophthalmometry Through Facial Photographs in Thyroid Eye Disease
- **저자/연도/게재지**: 2025, Ophthalmology Science
- **바이오마커**: Hertel 안구 돌출 mm 회귀
- **데이터셋**: 얼굴 사진 + Hertel 측정 페어 코호트
- **전처리**: 얼굴 정렬, 안와 ROI 크롭
- **모델**: Dual-stream ResNet-18
- **성능**: MAE 1.27 mm, Pearson r = 0.82
- **공개**: 아니오
- **증거 수준**: High
- 출처: https://www.ophthalmologyscience.org/article/S2666-9145(25)00089-2/fulltext

#### [논문 24] Machine Learning-Assisted System Using Digital Facial Images to Predict the Clinical Activity Score in Thyroid-Associated Orbitopathy
- **저자/연도/게재지**: Moon et al., 2022, Scientific Reports, 12:22085
- **바이오마커**: TAO Clinical Activity Score(CAS) 항목별 — 안검 부종, 결막 부종, 결막 충혈, 안검 발적, 카룬쿨/플리카 부종
- **데이터셋**: 다기관 임상 정면 얼굴 사진
- **모델**: ResNet-18 ensemble
- **성능**: Active TAO 진단 sens 0.881, spec 0.869; 각 염증 징후 AUC 0.884-0.977
- **공개**: 아니오
- **증거 수준**: High
- 출처: https://www.nature.com/articles/s41598-022-25887-8

---

## 4. 표정/얼굴 근육 분석 기반 바이오마커

### 4.1 파킨슨병 — 표정 감소(Hypomimia)

#### [논문 25] Automated Computer Vision Assessment of Hypomimia in Parkinson Disease: Proof-of-Principle Pilot Study
- **저자/연도/게재지**: Abrami et al., 2021, Journal of Medical Internet Research, 23(2):e21037
- **바이오마커**: 얼굴 모방·표정 비디오에서 hypomimia 신호
- **데이터 수집**: 일반인 셀피 비디오(YouTube 등)
- **데이터셋**: PD 자가식별자 107명 + 대조군 1,595개 비디오
- **전처리**: OpenFace 등으로 얼굴 검출, 비디오 프레임 추출
- **모델**: CNN (image classification)
- **성능**: 54명 테스트셋 AUC 0.71 (vs 신경과 전문의 AUC 0.75)
- **공개**: 아니오
- **한계점**: 자가식별 PD, 비디오 품질 편차
- **증거 수준**: Moderate
- 출처: https://www.jmir.org/2021/2/e21037/

#### [논문 26] Detection of Hypomimia in Patients with Parkinson's Disease via Smile Videos
- **저자/연도/게재지**: 2021, Frontiers in Neurology / PMC8422154
- **바이오마커**: 미소 동작 동안의 얼굴 기하·텍스처 변화
- **데이터셋**: PD 환자 + 대조군 미소 비디오
- **모델**: 머신러닝(SVM, RF, Bayesian, DT) + 핸드크래프티드 기하·텍스처 특징
- **성능**: 정확도 81-90% 보고
- **공개**: 아니오
- **증거 수준**: Moderate
- 출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC8422154/

#### [논문 27] Explaining Facial Action Units' Correlation with Hypomimia and Clinical Scores in Parkinson's Disease
- **저자/연도/게재지**: 2025, npj Parkinson's Disease
- **바이오마커**: FACS Action Units(AU1, AU4, AU6, AU12 등) 강도 → MDS-UPDRS-III, hypomimia 임상 점수와의 상관
- **데이터셋**: 환자 + 대조군 비디오
- **모델**: OpenFace AU 추출 + 통계 + ML
- **성능**: 임상 점수 예측 r/F1 보고
- **공개**: 일부
- **증거 수준**: Moderate
- 출처: https://www.nature.com/articles/s41531-025-00895-3

#### [논문 28] A Study on the Possible Diagnosis of Parkinson's Disease on the Basis of Facial Image Analysis
- **저자/연도/게재지**: 2021, Electronics (MDPI), 10(22):2832
- **바이오마커**: 정면 얼굴 사진의 표정 분류
- **데이터셋**: 환자 + 대조군 사진
- **모델**: VGG/Inception 변형
- **성능**: 분류 정확도 보고
- **증거 수준**: Limited-Moderate
- 출처: https://www.mdpi.com/2079-9292/10/22/2832

### 4.2 우울증/정신건강

#### [논문 29] Explainable Depression Detection Based on Facial Expression Using LSTM on Attentional Intermediate Feature Fusion with Label Smoothing
- **저자/연도/게재지**: 2023, Sensors (MDPI), 23(23):9402
- **바이오마커**: 인터뷰 비디오의 AU intensity, 시간적 표정 동역학
- **데이터셋**: AVEC depression challenge 류 비디오
- **모델**: OpenFace AU + LSTM + attention fusion
- **성능**: F1 88.89%, recall 87.03%, accuracy 91.67%, precision 91.40%
- **공개**: 아니오
- **증거 수준**: Moderate
- 출처: https://www.mdpi.com/1424-8220/23/23/9402

#### [논문 30] Automatic Identification of Depression Using Facial Images with Deep Convolutional Neural Network
- **저자/연도/게재지**: 2022, Computational Intelligence and Neuroscience / PMC9281460
- **바이오마커**: 정지 얼굴 이미지 → 우울 여부
- **모델**: DCNN
- **성능**: 분류 정확도 ~80% 보고
- **증거 수준**: Limited-Moderate
- 출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC9281460/

#### [논문 31] Demystifying Mental Health by Decoding Facial Action Unit Sequences
- **저자/연도/게재지**: 2024, Big Data and Cognitive Computing (MDPI), 8(7):78
- **바이오마커**: AU 시퀀스의 시간적 패턴
- **모델**: LSTM/Transformer on AU sequences
- **성능**: 우울/불안 다중 분류 정확도
- **증거 수준**: Moderate
- 출처: https://www.mdpi.com/2504-2289/8/7/78

#### [논문 32] FacialPulse: An Efficient RNN-Based Depression Detection via Temporal Facial Landmarks
- **저자/연도/게재지**: 2024, arXiv:2408.03499
- **바이오마커**: 시간적 얼굴 랜드마크 동역학
- **모델**: RNN + landmark sequence
- **성능**: 우울 분류 SOTA 갱신
- **증거 수준**: Moderate
- 출처: https://arxiv.org/html/2408.03499v1

### 4.3 통증 평가 (참고: 신생아·임상 환경)

#### [논문 33] Pain Assessment from Facial Expression: Neonatal Convolutional Neural Network (N-CNN)
- **저자/연도/게재지**: Zamzmi et al., 2019, IEEE EMBC
- **바이오마커**: 신생아 얼굴 표정(이마 주름, 눈 짜기, 비순구 깊어짐, 입 열림)
- **데이터셋**: NICU 신생아 비디오/이미지
- **모델**: 전용 N-CNN(전이학습 미사용)
- **성능**: 정확도 ~91%
- **공개**: 아니오
- **증거 수준**: Moderate
- 출처: https://ieeexplore.ieee.org/document/8851879/

---

## 5. 얼굴 형태/랜드마크 분석 기반 바이오마커

### 5.1 얼굴 비대칭 — 신경계 질환(뇌졸중·안면신경마비)

#### [논문 34] Human vs. Machine Learning Based Detection of Facial Weakness Using Video Analysis
- **저자/연도/게재지**: 2022, Frontiers in Neurology / PMC9284117
- **바이오마커**: 얼굴 가중치(asymmetry), 미소·찡그림 시 좌우 차이
- **데이터셋**: 공개 비디오(뇌졸중 vs 대조군)
- **모델**: Landmark + HoG + SVM (랜드마크 기반); CNN 비교
- **성능**: 정확도 89.7%, 패러메딕과 동등
- **공개**: 아니오
- **증거 수준**: Moderate
- 출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC9284117/

#### [논문 35] DeepStroke: An Efficient Stroke Screening Framework for Emergency Rooms with Multimodal Adversarial Deep Learning
- **저자/연도/게재지**: Cai et al., 2022, Medical Image Analysis (Elsevier)
- **바이오마커**: 얼굴 동영상의 미세 근육 비조정성 + 음성
- **데이터셋**: ER 환자 비디오·오디오 코호트
- **전처리**: 얼굴 검출/정렬, 시간적 윈도우
- **모델**: Multimodal adversarial DL(facial CNN + audio + 융합)
- **성능**: sens 93.12%, accuracy 79.27%, ER 의사와 동등
- **공개**: 아니오
- **증거 수준**: Moderate-High
- 출처: https://www.sciencedirect.com/science/article/abs/pii/S1361841522001694

#### [논문 36] Deep Learning-Driven Diagnosis: A Multi-Task Approach for Segmenting Stroke and Bell's Palsy
- **저자/연도/게재지**: 2024, Pattern Recognition (Elsevier)
- **바이오마커**: 안면마비 부위 분할 + 원인 분류
- **모델**: Multi-task CNN
- **성능**: 정확도 ~88% (뇌졸중 vs Bell's palsy 구분)
- **공개**: 아니오
- **증거 수준**: Moderate
- 출처: https://www.sciencedirect.com/science/article/pii/S0031320323005642

### 5.2 생물학적 나이/예후 — FaceAge (논문 12, 13 참조)

### 5.3 유전 증후군 — 얼굴 표현형(Phenotype)

#### [논문 37] Identifying Facial Phenotypes of Genetic Disorders Using Deep Learning (DeepGestalt / Face2Gene)
- **저자/연도/게재지**: Gurovich et al., 2019, Nature Medicine, 25:60-64
- **바이오마커**: 얼굴 사진의 형태학적 특징 → 200+ 유전 증후군 분류
- **데이터셋**: 17,000+ 사진, 200+ 증후군
- **전처리**: 얼굴 검출/정렬
- **모델**: 깊은 CNN(syndrome gestalt classifier) + SVM 후처리
- **성능**: Top-10 sens 91% (295/323); Noonan syndrome 아형 구분도 임상의 능가
- **공개**: 상용(Face2Gene); 알고리즘 설명만 공개
- **한계점**: 인종/연령 편향(소아 우세), 데이터 부유
- **증거 수준**: High
- 출처: https://www.nature.com/articles/s41591-018-0279-0

#### [논문 38] Efficiency of Computer-Aided Facial Phenotyping (DeepGestalt) in Individuals With and Without a Genetic Syndrome: Diagnostic Accuracy Study
- **저자/연도/게재지**: Pantel et al., 2020, JMIR (Journal of Medical Internet Research)
- **바이오마커**: 얼굴 → 증후군 vs 비증후군 분리
- **데이터셋**: 인디비주얼 코호트
- **모델**: DeepGestalt + SVM 후처리
- **성능**: 분리 능력 SVM 후 큰 폭 향상
- **공개**: 아니오(상용)
- **증거 수준**: Moderate
- 출처: https://www.jmir.org/2020/10/e19263/

### 5.4 내분비 질환 — Acromegaly / Cushing Syndrome

#### [논문 39] Deep-Learning Approach to Automatic Identification of Facial Anomalies in Endocrine Disorders
- **저자/연도/게재지**: 2019, Neuroendocrinology (Karger)
- **바이오마커**: 얼굴 기하·텍스처 → acromegaly + Cushing
- **모델**: CNN 분류기
- **성능**: 92.3-100% 정확도, 내분비 전문의 능가
- **공개**: 아니오
- **증거 수준**: Moderate-High
- 출처: https://pubmed.ncbi.nlm.nih.gov/31319415/

#### [논문 40] Comparative Analysis of Pre-trained Deep Learning Models and DINOv2 for Cushing's Syndrome Diagnosis in Facial Analysis
- **저자/연도/게재지**: 2025, arXiv:2501.12023
- **바이오마커**: 얼굴 → Cushing 진단(이진)
- **모델**: ImageNet 사전학습 CNN 다수 + DINOv2 자가지도 비교
- **성능**: AUC 0.96+ 보고
- **공개**: 일부
- **증거 수준**: Moderate
- 출처: https://arxiv.org/html/2501.12023v1

#### [논문 41] Real-Time Detection of Acromegaly from Facial Images with Artificial Intelligence
- **저자/연도/게재지**: Kong et al., 2023, Endocrine
- **바이오마커**: 코·광대·입술 thickening, 주름
- **데이터셋**: Acromegaly + 대조군 사진
- **모델**: 얼굴 ID 임베딩 + 분류기(FaRL 비교)
- **성능**: AUC 0.965 (Cushing), 0.956 (acromegaly), 정확도 0.95-0.96
- **공개**: 아니오
- **증거 수준**: Moderate-High
- 출처: https://pubmed.ncbi.nlm.nih.gov/36747333/

---

## 6. PCOS/자궁내막증 특화 연구 (별도 강조)

본 보고서의 핵심 주제 중 하나로, PCOS 표현형의 **얼굴 시각 바이오마커**는 (a) 안드로겐성 여드름, (b) 다모증(hirsutism), (c) 공막 표현, (d) 호르몬성 피부 변화로 나뉘며, 직접적 얼굴 이미지 단독 PCOS 분류 연구는 아직 제한적이다.

#### [논문 42] Deep Learning Algorithm for Automated Detection of Polycystic Ovary Syndrome Using Scleral Images
- **저자/연도/게재지**: Lv et al., 2021, Frontiers in Endocrinology, 12:789878
- **바이오마커**: 공막의 혈관·색소 패턴(중의학적 이론에서 영감)
- **데이터 수집**: 임상 카메라, 정면 눈 클로즈업
- **데이터셋**: 중국 여성 721명 (PCOS 388 + 대조군 333), full-eye images
- **전처리**: 얼굴/눈 검출 → 개선 U-Net + Attention 모듈로 공막 분할
- **모델**: ResNet-18 (특징 추출) + Multi-Instance Learning(MIL) 분류기
- **학습**: ImageNet 사전학습 → 미세조정
- **실험 설계**: 학습/테스트 분할, k-fold cross-validation
- **성능**: AUC 0.979, accuracy 0.929
- **공개**: 아니오
- **한계점**: 단일 인종(중국), 외부 검증 부재, 인과 메커니즘 불명확
- **증거 수준**: Moderate (단일 코호트, 메커니즘 미해명)
- **PCOS 본 연구 시사점**: 본 연구는 "공막 이미지 단독으로 PCOS 분류 가능성"을 처음 제시했다는 점에서 중요. 그러나 안드로겐성 여드름·다모증·생물학적 노화(FaceAge)와의 멀티모달 결합이 본 하네스 후속 연구의 차별점이 될 수 있음.
- 출처: https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2021.789878/full

#### PCOS 관련 얼굴 표현형 — 간접 증거 모음
- **여드름 중증도 + PCOS 호르몬 분석 연계**: 1,156,703 중국 성인 여성 셀피 + 식이·환경 데이터로 안드로겐성 여드름 분석 (검색결과 [참고1] 참조 — 단일 논문 아닌 SCMP 등 코호트)
- **Hirsutism**: 2023 international evidence-based PCOS guideline에서 cardinal manifestation으로 인용; 컴퓨터비전 기반 hirsutism 자동 점수화는 Ferriman-Gallwey 9개 부위 중 얼굴(상순·턱)에 집중되어야 하나 단독 딥러닝 연구는 매우 제한적
- **자궁내막증 얼굴 바이오마커**: 현재 시점에서 직접적 얼굴 이미지 기반 자궁내막증 AI 예측 논문은 발견되지 않음 → **연구 공백(gap)**

---

## 7. 공개 데이터셋 현황

| 데이터셋명 | 수집 방법 | 대상 질환/태스크 | 규모 | 공개 여부 | 출처 |
|----------|---------|---------|------|---------|------|
| **HAM10000** | 임상 더모스코피 | 7종 색소성 피부병변(멜라노마 등) | 10,015 dermoscopic images | 공개 (ISIC archive) | https://www.nature.com/articles/sdata2018161 |
| **ISIC 2017/2018/2019** | 더모스코피 | 멜라노마/skin lesion | 25,000+ | 공개 | ISIC challenge 사이트 |
| **IMDB-WIKI** | 인터넷 크롤링(연예인) | 얼굴 나이/성별 | 500K+ | 공개 | https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/ |
| **UTKFace** | 인터넷 크롤링 | 얼굴 나이/성별/인종 | 23,000+ | 공개 | UTKFace.git |
| **Xiangya-Derm** | 임상 얼굴 카메라 | 6종 얼굴 피부병 | 2,656 | 일부 공개 | Wu et al., IEEE Access |
| **AVEC (Audio-Visual Emotion Challenge)** | 인터뷰 비디오 | 우울/감정 | 다수 | 연구 신청 | http://avec2014.cs.nott.ac.uk/ |
| **Face2Gene 코호트** | 임상 얼굴 사진 | 200+ 유전 증후군 | 17,000+ | 비공개(상용) | https://www.face2gene.com/ |
| **FaceAge / AIM-Harvard** | 공개 + 임상 | 생물학적 나이 | 58,851(학습) + 6,196(검증) | 모델 공개, 데이터 일부 | https://github.com/AIM-Harvard/FaceAge |
| **N-CNN NICU dataset (iCOPE)** | NICU 비디오 | 신생아 통증 | ~수백명 | 일부 공개 | iCOPE/NICU 류 |
| **AcneDet 1572** | 스마트폰 | 여드름 등급 | 1,572 | 비공개 | MDPI Diagnostics 2022 |
| **TAO multicenter** | 임상 얼굴 사진 | 갑상선안병증 활성도 | 다기관 | 비공개 | Sci Rep 2022 |
| **Conjunctiva 764→4315 (DCGAN)** | 스마트폰 | 빈혈 | 4,315(증강) | 비공개 | HIR 2025 |

---

## 8. 기술적 도전과제 및 한계

### 8.1 데이터 측면
- **인종 편향**: 대부분 중국·한국·백인 코호트, 다인종 검증 부족
- **레이블 신뢰도**: 자가식별(예: PD), 주관적 임상 척도(IGA, GEA, FACS) 기반
- **표본 크기**: 1천-1만 단위가 일반적, 외부 검증 코호트 희박
- **조명·카메라 가변성**: 스마트폰 종류·플래시·실내외 차이로 색상·텍스처 변동
- **화이트밸런스/색상 보정**: BiliScreen·DeepSets 류 빌리루빈 회귀에서 핵심 — A4 종이/색카드 부속품 의존

### 8.2 모델 측면
- **사전학습 도메인 갭**: ImageNet은 일반 객체 → 의료 얼굴 텍스처 특이성 부족(FaRL/DINOv2 대안 부상)
- **시간적 정보 활용 부족**: 정지 이미지 위주, 비디오·동역학 분석은 PD/우울/뇌졸중에서만 일부 활용
- **설명가능성**: Black-box CNN은 임상 채택 장벽 → Attention map, AU explanation 도입 중

### 8.3 임상·윤리 측면
- **민감 데이터**: 얼굴은 강력한 식별자 → 비식별화·연합학습 필요
- **차별 위험**: 특히 우울·PD 자동 진단의 사회적 영향
- **규제**: FDA/CE 승인된 얼굴 의료 AI는 제한적(주로 피부병변)
- **메이크업·필터·수염**: 실생활 셀피 노이즈 요소

---

## 9. 연구 공백 분석

| 공백 | 설명 | 본 하네스 연구 기회 |
|------|------|---------------------|
| **자궁내막증 얼굴 바이오마커** | 직접 얼굴 이미지 → 자궁내막증 분류 연구 부재 | 통증·표정·만성염증 피부 표현형 + 홀몬 변화 결합 연구 가능 |
| **PCOS 멀티모달 얼굴** | 공막(Lv 2021) 단독 또는 여드름 단독, 통합 모델 부재 | 여드름 + 다모증 + 공막 + FaceAge 멀티헤드 모델 |
| **Hirsutism 자동 점수화** | Ferriman-Gallwey 얼굴 영역 자동 점수 딥러닝 거의 없음 | 모발·턱·상순 픽셀 분할 + 점수 회귀 |
| **장기 모니터링** | 대부분 single-shot 진단, 변화 추적 부재 | 셀피 timeseries로 호르몬 주기 추적 |
| **다민족 검증** | 단일 인종 코호트 우세 | 한국 + 다인종 비교 검증 |
| **여러 질병 동시 스크리닝** | 얼굴 1장으로 다중 질환 스크리닝 통합 모델 부재 | Multi-task: PCOS + 갑상선 + 빈혈 + 노화 |
| **자궁내막증 만성통증 표정** | 표정 기반 만성골반통 객관 평가 부재 | AU 기반 통증·우울 동시 평가 |

---

## 10. 참고문헌 목록

1. Huynh QT, Nguyen PH, Le HX, et al. Automatic Acne Object Detection and Acne Severity Grading Using Smartphone Images and Artificial Intelligence. Diagnostics. 2022;12(8):1879. https://www.mdpi.com/2075-4418/12/8/1879 ✅
2. Seité S, Khammari A, Benzaquen M, et al. Development and Accuracy of an Artificial Intelligence Algorithm for Acne Grading from Smartphone Photographs. Clin Cosmet Investig Dermatol. 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6972662/ ⚠️ (저널명 불일치 가능: Experimental Dermatology DOI 10.1111/exd.14022 vs CCID, 논문 자체 실재)
3. Lim ZV, Akram F, Ngo CP, et al. A Deep Learning-Based Facial Acne Classification System. Clin Cosmet Investig Dermatol. 2022;15:851-861. https://pmc.ncbi.nlm.nih.gov/articles/PMC9109724/ ✅
4. Evaluation of an acne lesion detection and severity grading model for Chinese population. Sci Rep. 2024/2025. https://www.nature.com/articles/s41598-024-84670-z ✅
5. Wu X, Wen C, Yang J, et al. Automated Grading of Acne Vulgaris by Deep Learning. 2019. https://pubmed.ncbi.nlm.nih.gov/31565821/ ✅
6. DED: Diagnostic Evidence Distillation for acne severity grading. Pattern Recognition. 2024. https://www.sciencedirect.com/science/article/abs/pii/S095741742300814X ❓
7. Mariakakis A, Banks MA, Phillipi L, et al. BiliScreen: Smartphone-Based Scleral Jaundice Monitoring. Proc ACM IMWUT. 2017;1(2). https://dl.acm.org/doi/abs/10.1145/3090085 ✅
8. Kim G, Lee S, Park J, et al. Deep-Learning-Based Smartphone Application for Self-Diagnosis of Scleral Jaundice. J Pers Med. 2021;11(9):928. https://www.mdpi.com/2075-4426/11/9/928 ✅
9. Non-Invasive Jaundice Screening Using AI: ML Analysis of Sclera and Urine Images. J Clin Med. 2025. https://www.mdpi.com/2077-0383/14/9/3125 ✅
10. AI-based non-invasive bilirubin prediction for neonatal jaundice using 1D CNN. Sci Rep. 2025. https://www.nature.com/articles/s41598-025-96100-9 ✅
11. Neonatal jaundice detection using a vision transformer-based deep learning model. Sci Rep. 2026. https://www.nature.com/articles/s41598-026-40515-5 ✅ (PMC13000152, 2026년 실제 출판)
12. Bontempi D, Schoenfeld JD, Bitterman DS, et al. FaceAge, a deep learning system to estimate biological age from face photographs to improve prognostication. Lancet Digit Health. 2025. https://www.thelancet.com/journals/landig/article/PIIS2589-7500(25)00042-1/fulltext ✅
13. Decoding biological age from face photographs using deep learning. 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10516042/ ✅ (eLife 2023, PubMed 37745558)
14. A Deep Learning-Based Detection of Wrinkles on Skin. Springer LNNS. 2022. https://link.springer.com/chapter/10.1007/978-981-16-9573-5_2 ✅
15. Striped WriNet: Automatic wrinkle segmentation. Biomed Signal Process Control. 2024. https://www.sciencedirect.com/science/article/abs/pii/S1746809423012508 ✅
16. Evaluating facial dermis aging with LC-OCT and deep learning. Sci Rep. 2024. https://www.nature.com/articles/s41598-024-74370-z ❓
17. Detection of anemia using conjunctiva images: A smartphone application approach. Smart Health. 2023. https://www.sciencedirect.com/science/article/pii/S2590093523000322 ❓
18. Deep Learning Model-Based Detection of Anemia from Conjunctiva Images. Healthc Inform Res. 2025;31(1):57. https://e-hir.org/journal/view.php?number=1237 ✅
19. Non-invasive anemia detection from conjunctiva and sclera images using ViT. Sci Rep. 2025. https://www.nature.com/articles/s41598-025-32343-w ✅
20. AnemiaVision: Non-Invasive Anemia Detection via Smartphone Imagery (EfficientNet-B3). arXiv:2604.22964. 2026. https://arxiv.org/html/2604.22964 ✅
21. Prediction of anemia in real-time using a smartphone camera processing conjunctival images. PLOS One. 2024. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0302883 ❓
22. Explainable Deep Learning System for Automatic Detection of Thyroid Eye Disease Using Facial Images. Am J Ophthalmol. 2025. https://www.sciencedirect.com/science/article/pii/S0002939425002582 ✅
23. Deep Learning–Driven Exophthalmometry through Facial Photographs. Ophthalmol Sci. 2025. https://www.ophthalmologyscience.org/article/S2666-9145(25)00089-2/fulltext ✅
24. Moon JH, Shin K, Lee GM, et al. Machine learning-assisted system using digital facial images to predict CAS in TAO. Sci Rep. 2022;12:22085. https://www.nature.com/articles/s41598-022-25887-8 ✅
25. Abrami A, Gunzler S, Kilbane C, et al. Automated Computer Vision Assessment of Hypomimia in PD. JMIR. 2021;23(2):e21037. https://www.jmir.org/2021/2/e21037/ ✅
26. Detection of hypomimia in patients with PD via smile videos. Front Neurol. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8422154/ ❓
27. Explaining facial action units' correlation with hypomimia in PD. npj Park Dis. 2025. https://www.nature.com/articles/s41531-025-00895-3 ✅
28. A Study on the Possible Diagnosis of PD on the Basis of Facial Image Analysis. Electronics. 2021;10(22):2832. https://www.mdpi.com/2079-9292/10/22/2832 ❓
29. Explainable Depression Detection Based on Facial Expression Using LSTM. Sensors. 2023;23(23):9402. https://www.mdpi.com/1424-8220/23/23/9402 ✅
30. Automatic Identification of Depression Using Facial Images with DCNN. Comput Intell Neurosci. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9281460/ ❓
31. Demystifying Mental Health by Decoding Facial Action Unit Sequences. Big Data Cogn Comput. 2024;8(7):78. https://www.mdpi.com/2504-2289/8/7/78 ❓
32. FacialPulse: An Efficient RNN-based Depression Detection. arXiv:2408.03499. 2024. https://arxiv.org/html/2408.03499v1 ✅ (ACM MM 2024 oral, DOI 10.1145/3664647.3681546)
33. Zamzmi G, Pai CY, Goldgof D, et al. Pain Assessment From Facial Expression: N-CNN. IEEE EMBC. 2019. https://ieeexplore.ieee.org/document/8851879/ ⚠️ (컨퍼런스명 오기: IEEE IJCNN 2019, 논문 자체 실재)
34. Human vs. Machine Learning Based Detection of Facial Weakness Using Video. Front Neurol. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9284117/ ✅
35. Cai Y, Zhang Y, Cai H, et al. DeepStroke: Stroke Screening Framework with Multimodal Adversarial DL. Med Image Anal. 2022. https://www.sciencedirect.com/science/article/abs/pii/S1361841522001694 ✅
36. Deep learning-driven diagnosis: A multi-task approach for segmenting stroke and Bell's palsy. Pattern Recognit. 2024. https://www.sciencedirect.com/science/article/pii/S0031320323005642 ✅
37. Gurovich Y, Hanani Y, Bar O, et al. Identifying facial phenotypes of genetic disorders using deep learning. Nat Med. 2019;25:60-64. https://www.nature.com/articles/s41591-018-0279-0 ✅
38. Pantel JT, Hertzberg J, Danyel M, et al. Efficiency of Computer-Aided Facial Phenotyping (DeepGestalt). JMIR. 2020. https://www.jmir.org/2020/10/e19263/ ✅
39. Deep-Learning Approach to Automatic Identification of Facial Anomalies in Endocrine Disorders. Neuroendocrinology. 2019. https://pubmed.ncbi.nlm.nih.gov/31319415/ ⚠️ (연도 오기: epub 2019이나 최종 출판 Neuroendocrinology 2020;110(5):328-337)
40. Comparative Analysis of Pre-trained DL Models and DINOv2 for Cushing's Syndrome Diagnosis. arXiv:2501.12023. 2025. https://arxiv.org/html/2501.12023v1 ✅
41. Real-time detection of acromegaly from facial images with AI. Endocrine. 2023. https://pubmed.ncbi.nlm.nih.gov/36747333/ ⚠️ (저널명 오기: European Journal of Endocrinology 2023;188(1):158-166, PubMed 36747333 확인)
42. Lv W, Song Y, Fu R, et al. Deep Learning Algorithm for Automated Detection of PCOS Using Scleral Images. Front Endocrinol. 2021;12:789878. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2021.789878/full ✅
43. Lin S, Li Z, Fu B, et al. Feasibility of using deep learning to detect coronary artery disease based on facial photo. Eur Heart J. 2020;41(46):4400-4411. https://academic.oup.com/eurheartj/article/41/46/4400/5895010 ✅
44. Application and accuracy analysis of different facial regions based on deep learning in the diagnosis of hypertension. Sci Rep. 2025. https://www.nature.com/articles/s41598-025-30936-z ✅
45. Type 1 and Type 2 Diabetes Measurement Using Human Face Skin Region. 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10547572/ ✅
46. Detection of hyperglycemia and hypoglycemia using deep learning from facial images. Biomed Signal Process Control. 2025. https://www.sciencedirect.com/science/article/abs/pii/S1746809425008626 ❓
47. A Novel Convolutional Neural Network for the Diagnosis and Classification of Rosacea: Usability Study. JMIR Med Inform. 2021. https://medinform.jmir.org/2021/3/e23415/ ✅
48. A Deep Learning Based Framework for Diagnosing Multiple Skin Diseases (EfficientNet-B4). Front Med. 2021. https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2021.626369/full ✅
49. The HAM10000 dataset. Sci Data. 2018;5:180161. https://www.nature.com/articles/sdata2018161 ✅
50. Skin Cancer Classification With Deep Learning: A Systematic Review. Cancer. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9327733/ ❓

---

**보고서 종료** | 작성: face-voice-research 하네스 / 얼굴 영상 문헌 탐색 에이전트
