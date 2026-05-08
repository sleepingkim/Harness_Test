# 얼굴·음성 기반 질병 예측 바이오마커 합성 보고서

**작성 일자**: 2026-04-29
**작성**: face-voice-research 하네스 / face-voice-synthesizer 에이전트
**대상 입력**: `_workspace3/01_face_biomarker_literature.md` (얼굴 50편), `_workspace3/02_voice_biomarker_literature.md` (음성 43편, 한국어 7편)

---

## 1. 탐색 요약

### 1.1 수집 규모
- **얼굴 바이오마커 논문**: 50편 (본문 상세 항목 42편 + 참고문헌 추가 8편)
  - 검증됨 ✅ 37편(74%), 부분 일치 ⚠️ 5편(10%), 미확인 ❓ 8편(16%), 할루시네이션 ❌ 0편
- **음성 바이오마커 논문**: 43편 (한국어 7편 포함)
  - 검증됨 ✅ 31편, 부분 일치 ⚠️ 10편, 할루시네이션 ❌ 0편
  - 한국어 논문 7편: #5, #6, #10, #19, #28, #29, #43

### 1.2 탐색 DB
- **얼굴**: PubMed, IEEE Xplore, Google Scholar, Semantic Scholar, arXiv, Nature/Springer, MDPI, Lancet Digital Health, Frontiers
- **음성**: 위 + JMIR, ScienceDirect, RISS, DBpia, KCI, KoreaScience, KISTI ScienceON, SNU OAK

### 1.3 탐색 일자
2026-04-29 (단일 일자)

### 1.4 도메인 분포
- 얼굴 50편 — 피부/여드름 6편, 황달 5편, 노화/주름 5편, 결막/공막(빈혈) 5편, 갑상선안병증 3편, 표정/PD/우울 8편, 통증 1편, 비대칭/뇌졸중 3편, 유전증후군/내분비 5편, PCOS 1편(직접), 심혈관/당뇨/피부질환/멜라노마 8편
- 음성 43편 — 신경계 15편, 정신건강 9편, 호흡기 8편, 호르몬 4편, 음성질환·후두암 4편, 신생아·심혈관·기타 3편

---

## 2. 얼굴 바이오마커 주요 연구 요약

### 2.1 피부/여드름/호르몬 (PCOS, 갑상선 등)
스마트폰 셀피 또는 임상 카메라로 촬영한 얼굴 사진에서 **여드름 병변 객체 검출 + 중증도 등급화**가 가장 활발한 영역이다. AcneDet (Huynh 2022, Faster R-CNN+LightGBM, mAP=0.54, 중증도 AUC=0.85), Seité 2019 (5,972장 GEA r=0.74), Lim 2022 (KAGS 4단계, ResNet-152 Top-1=67%, Top-2=92%), Wu 2019 (Pillsbury 4단계, ResNet-50 Acc=81%) 등이 대표적이다. 호르몬 관련 의의는 **안드로겐성 여드름이 PCOS의 임상적 cardinal manifestation**이라는 점에서 기인하나, 여드름 ↔ PCOS 직접 연계 모델은 부재하다. 다모증(Hirsutism) Ferriman-Gallwey 점수 자동화는 거의 미개척이다.

### 2.2 눈/결막 분석 (황달, 빈혈, 갑상선 안병증)
- **빈혈(결막 창백)**: 스마트폰 안검 결막 이미지로 헤모글로빈 추정. 2025 Sci Rep ViT 모델 Acc=98.47%, HIR 2025 stacking ensemble AUC=0.97, 2026 EfficientNet-B3 검증정확도 94-97%.
- **황달(공막 황달)**: BiliScreen (Mariakakis 2017, sens 89.7%/spec 96.8%) 이래로 ResNet 회귀(Kim 2021), DeepSets R²=0.782 (2025), 신생아 ViT(2026) 등으로 발전. 색보정 액세서리(A4 화이트밸런스, blue box) 의존이 핵심 한계.
- **갑상선안병증(TED)**: 2025 Am J Ophthalmol AUC=0.997 / sens 99.7%/spec 94.5%, Ophthalmol Sci 2025 Hertel 안구돌출 회귀 MAE=1.27mm, Moon 2022 ResNet-18 ensemble TAO CAS 항목별 AUC 0.884-0.977 — 임상 점수와 직접 매핑되는 강력한 성능을 보인다.

### 2.3 표정/얼굴 근육 (파킨슨, 우울, 뇌졸중)
- **파킨슨 hypomimia**: Abrami 2021 셀피 비디오 AUC=0.71 (전문의 0.75), 미소 비디오 ML 81-90%, 2025 npj Park Dis는 FACS Action Units (AU1, AU4, AU6, AU12)와 MDS-UPDRS-III 상관 분석.
- **우울증**: Sensors 2023 LSTM+attention F1=88.89%, FacialPulse 2024 RNN+landmark, MDPI 2024 AU 시퀀스 LSTM/Transformer.
- **뇌졸중/안면마비**: DeepStroke 2022 멀티모달(얼굴+음성) sens=93.12%, Front Neurol 2022 89.7% (패러메딕 동등), Pattern Recognit 2024 multi-task stroke vs Bell's palsy 88%.

### 2.4 얼굴 형태/랜드마크 (유전증후군, 내분비 질환)
- **DeepGestalt/Face2Gene** (Gurovich 2019, Nat Med): 200+ 유전증후군 분류 Top-10 sens 91% — 얼굴 형태학 AI의 기념비적 성과로, 상용화(Face2Gene)된 유일한 사례.
- **Acromegaly/Cushing**: Neuroendocrinology 2019 Acc 92-100% (전문의 능가), DINOv2 (2025) AUC 0.96+, Eur J Endocrinol 2023 (Kong) AUC 0.965 (Cushing) / 0.956 (acromegaly).

### 2.5 생물학적 나이/심혈관
- **FaceAge** (Bontempi 2025 Lancet Digit Health): IMDB-WIKI+UTKFace 58,851명 학습, 6,196 암 환자 검증; 임상의 단독 AUC 0.74 → +FaceAge 0.80, FaceAge 1년 증가당 사망 HR 유의 — 코드 공개(GitHub AIM-Harvard/FaceAge).
- **심혈관**: Lin 2020 Eur Heart J — 얼굴 사진으로 관상동맥질환 검출 가능성 입증.
- **고혈압**: 2025 Sci Rep 다양한 얼굴 영역 비교 분석.
- **당뇨**: 얼굴 피부 영역 ML (2023 PMC10547572), 고혈당/저혈당 검출 (2025 BSPC).

---

## 3. 음성 바이오마커 주요 연구 요약

### 3.1 신경계 질환 (파킨슨, 알츠하이머, ALS, HD)
- **파킨슨**: 가장 성숙한 영역. UCI Parkinson Voice (31명/195녹음)·UCI Telemonitoring·mPower(9,520+) 데이터셋 기반. 전통 음향 특징(jitter, shimmer, HNR, MFCC, F0)으로 SVM/RF/XGBoost가 95% 이상; 멜스펙트로그램 + ResNet50 (Quan 2025) Acc=99%; **Wav2Vec 2.0/HuBERT** (Favaro 2025) intra=97.92%/ cross-corpus AUC=0.92. 한국어: 김지환 2022 Globalformer ASR CER 22.15% (분류는 미보고), 2016 한국멀티미디어학회 J48 Acc=88.72%.
- **알츠하이머/MCI**: ADReSS Challenge (Luz 2020, AD 78+78) 기준선; 멀티모달(BERT 텍스트 + x-vector 음성) Acc=89.6%; Wav2Vec layer-wise (2026) MCI 조기검출 Acc=71%/F1=74%; **서울대 박사학위 2024**가 한국 노인 AD 비언어학적 모델로 사실상 유일.
- **ALS/dysarthria**: Stegmann 2025 npj Digit Med — attention CNN-Transformer로 ALS severity R²=0.92, RMSE=6.78. JASA Express Letters 2023 — 임상 해석 가능 layer로 음소별 distortion map.
- **헌팅턴병/Vocal tremor**: Velasco García 2010 (n=13) Acc=94%, Rusz 2020 Clin Neurophysiol — HD 65%, ET 50%, MSA 40%에서 비정상 vocal tremor.

### 3.2 정신건강 (우울증, 불안, 양극성, 조현병)
- **우울증**: DAIC-WOZ 기반 연구가 지배적. Wav2Vec 2.0 (2024 Sci Rep) F1=0.88, RMSE=4.3 (PHQ-8 회귀); JAMIA 2024 메타분석(25개 연구) pooled sens=0.81, spec=0.81, AUC=0.87; Voice of Mind (2025 J Voice) 음향+어휘 멀티모달.
- **양극성**: Faurholt-Jepsen 2016 Transl Psychiatry — 환자 28명, 121일 일상 통화 음성, 조증 AUC=0.89, 우울 AUC=0.78. **종단 일상 모니터링의 모범**.
- **조현병**: de Boer 2021 Psychol Med — 86+80 화자, F0/formant/침묵으로 Acc=81-94%; PMC12237691 2025 melspec CNN Acc=87.8%/AUC=0.86.
- **한국어**: 서울대 박사 2022 — M.I.N.I. 한국어판 인터뷰, 음성 AUC=0.806 / 텍스트 AUC=0.905 / 자살위험 ensemble AUC=0.800.

### 3.3 호흡기 (COVID-19, 천식, COPD, OSA)
- **COVID-19**: Coswara(2,746명, 9개 과제), COUGHVID(27,550 녹음/1,156 양성)가 양대 데이터셋; intra-dataset Acc 70-97%이나 **cross-dataset AUC 0.43-0.68로 급락** — 일반화 실패가 가장 큰 한계. 한국어: 한밭대 석사 2022, EfficientNet 기반 기침 검출 시스템 Acc=76.67%.
- **호흡음(폐렴/COPD/천식)**: Kim 2021 Sci Rep — 871명 청진음 mel-spec ResNet Acc=86.5%, AUC=0.93; HeAR (2025 Google) 소아 천식 Acc>95%.
- **수면무호흡(OSA)**: OSAnet (Wang 2022) — 비접촉 야간 음성 mel-spec CNN+LSTM, 호흡사건 Acc=95.3%, OSAHS 중증도 3분류 81.6%.

### 3.4 호르몬/내분비 (PCOS, 갑상선, 당뇨)
- **PCOS**: Aydin 2010 J Voice (n=34+30), Aydin 2024 Egypt J Otolaryngol — F0 감소·MPT 감소·throat-clearing 76.5% vs 4.8% 등 **통계적 음성 변화는 입증되었으나 ML 분류 정확도는 미보고**. 안드로겐 → vocal fold 근비대 → F0 감소 메커니즘이 일관되게 보고됨.
- **갑상선**: Endocrine Connections 2022 리뷰 — 갑상선저하증 → vocal fold 부종 → F0 감소·hoarseness; 갑상선항진증 → tremulous voice; 정상화 후 3-6개월 내 음성 회복 가능.
- **당뇨(T2DM)**: Kaufman 2023 Mayo Clin Proc Digital Health — 267명 18,000+ 음성, 위험요인 결합 시 여성 Acc=89%/남성=86% (단, 검증 보고서에서 실제 75%/70%로 정정).

### 3.5 음성질환·후두암·신생아·심혈관
- **SVD(Saarbrücken)**: 2,043명 독일어 발화. SVM Acc=99.5%(여)/99.19%(남), OpenL3 transfer 99.44% — intra-DB 과적합 우려.
- **후두암**: arXiv 2024 benchmark balanced Acc=83.7%/AUROC=91.8%; Kim 2020 J Clin Med 1D-CNN Acc=85% (laryngologist 69.9% 능가); 2024 Sci Rep 5-class(후두암/양성/성대마비/정상) Acc=66.9%.
- **심부전**: Maor 2020 JAHA — 만성 심부전 10,583명, Beyond Verbal 음성 risk score Q4 vs Q1 사망률 54% vs 23%.
- **신생아 울음**: 2023 Diagnostics — 청각저하·질식·갑상선저하·고빌리루빈·구개열 등 다질환 분류 Acc=97.5% (mel-spec+GFCC+HR 융합).

### 3.6 한국어 논문 특이사항
한국어 음성 임상 데이터셋의 **절대적 빈곤**이 두드러진다. 7편 중 박사학위논문 2편(서울대 AD 2024, 우울/자살 2022), 석사학위 1편(한밭대 COVID-19 2022), 학회지 2편(파킨슨 2022/2016), earticle 1편, KISTI 정부 보고서 1편이며 **PCOS/갑상선/당뇨/심부전 한국어 음성 데이터셋은 전무**. AIHub 구음장애 데이터(1,200+명, 5,000-5,250시간)가 가장 큰 공개 한국어 임상 음성. 이는 본 하네스가 한국 코호트 구축으로 기여할 핵심 공백이다.

---

## 4. 데이터 수집 방법론 비교

| 항목          | 얼굴 바이오마커                                                                                                       | 음성 바이오마커                                                                                                                                                           |
| ----------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 주요 수집 장비    | 스마트폰 카메라(iOS/Android), 임상 카메라(정면·측면), LC-OCT(특수), 청진기 비유                                                       | 콘덴서 마이크(AKG-C420 등), 스마트폰 마이크, 임상 인터뷰 마이크, 청진기, 비접촉 수면실 마이크, 전화 통화                                                                                                 |
| 수집 환경       | 임상실 표준 조명, 환자 셀피(실생활), 다양한 조명·플래시·실내외 변동, A4/색보정 액세서리 동반                                                       | 방음실(임상 표준), 가정 환경(스마트폰), 일상 통화(자연 환경), NICU, 수면실                                                                                                                   |
| 촬영/발화 과제    | 정면 얼굴 정지 사진(주로), 표정 비디오(PD/우울/뇌졸중), 미소·찡그림 동작, 안검 외번(결막)                                                       | 지속 모음 /a/ (5초+, 가장 표준), 음절 반복(/pa-ta-ka/), 표준 문장 읽기, 그림 묘사(Cookie Theft), 자유 발화 인터뷰, 기침·호흡, 신생아 울음                                                                 |
| 일반적 데이터셋 규모 | 수백 ~ 수천 장 (대부분 1k-10k), FaceAge 58,851명·HAM10000 10,015장·DeepGestalt 17,000+장은 예외                              | 31명-수백명이 표준; mPower 9,520+, COUGHVID 27,550, Coswarad 2,746, SVD 2,043이 대규모                                                                                        |
| 주요 전처리      | 얼굴 검출(MTCNN/Dlib/Faster R-CNN), 정렬·랜드마크, 256×256 정규화, ROI 크롭(공막·결막·안와), 화이트밸런스 보정, ImageNet 정규화                | VAD(음성 활동 감지), 노이즈 제거, 리샘플링(주로 16 kHz), 침묵 제거, 진폭 정규화, 4-5초 세그먼트 분할, SNR 필터링                                                                                       |
| 주요 특징 추출    | CNN 표현(ResNet/EfficientNet/ViT), Action Units(OpenFace), 얼굴 임베딩(FaRL/DINOv2), 픽셀 분할(U-Net 주름·공막), 색공간 회귀(빌리루빈) | 전통 음향: F0, jitter, shimmer, HNR, MFCC 1-13/39, formant F1-F4, eGeMAPS, ComParE 6373; 딥 임베딩: Wav2Vec 1.0/2.0, HuBERT, x-vector, Whisper, HeAR; 시각화: 멜스펙트로그램(이미지 변환) |

**핵심 통찰**: 얼굴은 "한 장의 정지 이미지로 충분한 진단"이 가능한 영역(여드름·황달·빈혈·acromegaly)과 "비디오/시간 동역학이 필요"한 영역(PD·우울·뇌졸중)으로 양분된다. 음성은 거의 모든 영역이 "수 초~수 분의 시간 신호"를 필요로 하지만, **발화 과제 표준화 부재**가 메타분석의 가장 큰 장벽이다.

---

## 5. 모델 아키텍처 동향

### 5.1 얼굴 분석에서 주로 사용된 모델
- **CNN 백본**: ResNet-18/50/152 (TED·우울·여드름·노화), VGG-16/Inception (FaceAge prelim·PD), EfficientNet-B3/B4 (빈혈·다중 피부질환).
- **객체 검출/분할**: Faster R-CNN (AcneDet 4종 병변), U-Net + Attention (공막 분할 PCOS, 주름 분할 WriNet), MTCNN (얼굴/눈 검출).
- **Vision Transformer**: 빈혈 ViT (Sci Rep 2025 Acc=98.47%), 신생아 황달 ViT (Sci Rep 2026), DINOv2 자가지도 (Cushing 2025).
- **앙상블/지식증류**: stacking (VGG+ResNet+Inception 빈혈 AUC=0.97), Knowledge distillation DED 여드름.
- **시간 동역학**: LSTM + attention fusion (우울증 AU sequences), RNN on landmark trajectories (FacialPulse), Multimodal adversarial DL (DeepStroke 얼굴+음성).

**트렌드**: ImageNet 사전학습 CNN → **얼굴 도메인 자가지도(FaRL, DINOv2) + 멀티태스크/멀티모달**로 이동 중. Attention map 등 설명가능성(XAI)이 임상 채택 핵심 요건으로 부상.

### 5.2 음성 분석에서 주로 사용된 모델
- **전통 ML**: SVM(RBF), Random Forest, XGBoost, LightGBM, KNN, J48, Naive Bayes — 핸드크래프티드 음향 특징(eGeMAPS, MDVP, openSMILE) 위에 가장 널리 사용.
- **CNN/RNN**: 1D-CNN(1차원 신호), 2D-CNN(멜스펙트로그램), CNN+LSTM hybrid(OSAnet, 신생아 울음), BiLSTM(파킨슨 음성).
- **이미지 전이학습 from melspec**: ResNet50/VGG16/InceptionV3로 멜스펙트로그램 분류 (Quan 2025 PD Acc=99%, EfficientNet 한국 기침).
- **Self-supervised speech**: **Wav2Vec 1.0/2.0, HuBERT** (Favaro 2025 PD, Yang 2024 우울, MCI 조기검출), x-vector + PLDA (AD), Whisper embeddings, HeAR (Google 3억 오디오 사전학습).
- **Transformer/멀티모달**: Attention CNN-Transformer hybrid (ALS Stegmann 2025), BERT 텍스트 + 음향 fusion (AD, 우울, 한국 우울/자살).

**트렌드**: 핸드크래프티드 → **Wav2Vec/HuBERT 자가지도 임베딩**이 표준 백본으로 부상. 임상 해석가능 layer(JASA 2023 음소별 distortion map), 멀티모달 fusion(텍스트·생체·영상)이 차세대 방향.

**얼굴 vs 음성 공통 트렌드**: (1) 자가지도 사전학습(DINOv2 / Wav2Vec 2.0)이 ImageNet/eGeMAPS 핸드크래프티드를 빠르게 대체. (2) Attention 기반 설명가능성이 임상 채택 필수. (3) Cross-domain/cross-corpus 일반화가 공통 미해결 과제.

---

## 6. 질환별 최적 바이오마커 추천

| 질환 | 추천 얼굴 바이오마커 | 추천 음성 바이오마커 | 증거 수준 |
|------|-----------------|-----------------|---------|
| PCOS | 안드로겐성 여드름 중증도(IGA/GEA), 다모증(Ferriman-Gallwey 상순·턱), 공막 패턴(Lv 2021 AUC=0.979), FaceAge(생물학적 노화) | F0 감소(안드로겐 vocal fold 근비대), MPT 감소, jitter/RAP 증가, throat-clearing 빈도 | Moderate (얼굴 공막 단일 코호트, 음성 통계만, ML 분류기 미흡) |
| 자궁내막증 | **연구 부재** — 가설: 만성 통증 표정(AU), 만성염증 피부 표현형, 호르몬 주기성 노화 | **연구 부재** — 가설: 호르몬 주기 F0 변동, 통증 발성 패턴 | Limited (직접 연구 사실상 없음, 본 하네스 핵심 공백) |
| 갑상선 질환 | 안구 돌출(Hertel 회귀 MAE=1.27mm), TED CAS 5항목(Moon 2022 AUC 0.884-0.977), TED 진단(2025 AUC=0.997) | 갑상선저하증: F0 감소·hoarseness, vocal fold 부종 효과; 갑상선항진증: tremulous voice (Endocrine Connections 2022 리뷰) | High (얼굴), Moderate (음성) |
| 빈혈 | 안검 결막 RGB/HSV → Hb 추정 (2025 ViT Acc=98.47%, HIR 2025 AUC=0.97, EfficientNet-B3 94-97%) | (직접 연구 없음) | High (얼굴) |
| 황달 | 공막 색상 → 빌리루빈 회귀 (BiliScreen sens 89.7%/spec 96.8%, Kim 2021 ResNet, 2025 DeepSets R²=0.782, 2026 신생아 ViT) | 신생아 울음(고빌리루빈 분류, 2023 Diagnostics Acc=97.5%) | High (얼굴), Moderate (음성 신생아) |
| 파킨슨병 | Hypomimia 비디오(Abrami 2021 AUC=0.71), FACS AU(2025 npj Park Dis MDS-UPDRS-III 상관), 미소 비디오 ML 81-90% | 지속 모음 jitter/shimmer/HNR/MFCC + BiLSTM (Naranjo 2025 AUC=0.97), Wav2Vec 2.0 (Favaro 2025 cross-corpus AUC=0.92), 멜스펙+ResNet50 (Quan 2025 Acc=99%) | High (양 모달리티 모두) |
| 알츠하이머/치매 | (직접 연구 미흡, FaceAge 노화 간접 지표) | ADReSS 멀티모달 Acc=89.6%, BERT+x-vector, Wav2Vec layer-wise(MCI Acc=71%) | High (음성), Limited (얼굴) |
| 우울증 | AU 시퀀스(LSTM Sensors 2023 F1=88.89%), 얼굴 랜드마크 동역학(FacialPulse), DCNN 정지 이미지 Acc=80% | DAIC-WOZ Wav2Vec 2.0 F1=0.88, JAMIA 2024 메타 AUC=0.87, 음향+어휘 fusion | High (양 모달리티, 멀티모달이 우세) |
| 당뇨 | 얼굴 피부 영역 ML, 고혈당/저혈당 얼굴 검출 (2025 BSPC) | T2DM 스마트폰 음성 + 위험요인 결합 여성 75-89%/남성 70-86% (Mayo 2023) | Moderate |

---

## 7. PCOS/자궁내막증 적용 가능성 평가

### 7.1 얼굴 바이오마커 — PCOS
- **여드름**: AcneDet/KAGS/GEA 등급화 모델은 임상 수준 도달(전문의 일치 r=0.74, AUC=0.85)했으나 **PCOS 호르몬 프로파일과 직접 연계된 모델은 부재**. 안드로겐성 여드름의 분포 특성(턱·하악각·등)이 PCOS의 hyperandrogenism marker로 작동할 가능성이 높음.
- **다모증(Hirsutism)**: 컴퓨터비전 기반 자동 Ferriman-Gallwey 점수화 연구는 매우 제한적. **상순·턱 ROI 모발 분할 + 점수 회귀**가 본 하네스의 우선 신규 과제.
- **공막 패턴**: Lv 2021 (Front Endocrinol, AUC=0.979) — 단일 코호트(중국 721명) 외부 검증 부재이나 **유일한 얼굴 단독 PCOS 분류 모델**.
- **FaceAge**: 생물학적 노화 가속 가설(인슐린 저항성·만성 염증) — PCOS에서 FaceAge gap이 클 가능성을 본 하네스가 검증할 수 있음.
- **호르몬성 피부 변화**: seborrhea, hyperpigmentation(acanthosis nigricans) 등 PCOS 동반 피부 표현형 자동 검출은 미개척.

### 7.2 음성 바이오마커 — PCOS
- **F0 감소**: Aydin 2010, Aydin 2024 등에서 PCOS 군의 F0 감소·MPT 감소·throat-clearing 증가가 일관 보고. 메커니즘은 안드로겐 → vocal fold 근비대.
- **분류 ML 모델 부재**: 통계적 변화는 입증되었으나 AUC/Sens/Spec을 보고한 ML/DL 분류기는 거의 없음.
- **본 하네스 기회**: 한국 PCOS 환자 한국어 음성 코호트 + Wav2Vec 2.0/eGeMAPS 기반 분류기 개발이 즉각 가능한 신규 연구.

### 7.3 자궁내막증
- **얼굴 직접 연구 전무**.
- **음성 직접 연구 전무**.
- **가설 경로**: (1) 만성 골반통 → 표정 AU 패턴(통증 객관화), (2) 호르몬 변화(GnRH agonist 치료) → vocal fold 영향, (3) 만성 염증 → 피부 표현형(FaceAge, 여드름 패턴), (4) 우울/불안 동반 → 표정+음성 정신건강 마커.

### 7.4 멀티모달 융합 가능성
가장 강력한 차별점이 될 가능성이 높은 영역. 후보 조합:
- **얼굴(여드름+다모증+공막+FaceAge) + 음성(F0+MPT+jitter+Wav2Vec) → PCOS Multi-task 분류기**
- **얼굴(AU 통증 표정) + 음성(통증 발성 변화) → 자궁내막증 만성통증 객관 평가**
- **얼굴(AU 우울) + 음성(우울 음향) → 자궁내막증/PCOS 동반 정신건강 통합 평가**

이는 본 하네스 후속 데이터 제안서의 핵심 차별 가치(novel contribution)로 활용 가능하다.

---

## 8. 공개 데이터셋 종합 목록

| 데이터셋명 | 모달리티 | 대상 질환 | 데이터 규모 | 수집 방법 | 언어 | 공개 여부 | 접근 방법 |
|----------|--------|---------|---------|---------|------|---------|---------|
| HAM10000 | 얼굴/피부 이미지 | 7종 색소성 피부병변 | 10,015 dermoscopic | 임상 더모스코피 | - | 공개 | ISIC archive |
| ISIC 2017/2018/2019 | 더모스코피 | 멜라노마/skin lesion | 25,000+ | 임상 더모스코피 | - | 공개 | ISIC challenge |
| IMDB-WIKI | 얼굴 이미지 | 나이/성별 | 500K+ | 인터넷 크롤링 | - | 공개 | ETH Zurich CVL |
| UTKFace | 얼굴 이미지 | 나이/성별/인종 | 23,000+ | 인터넷 크롤링 | - | 공개 | UTKFace.git |
| Xiangya-Derm | 얼굴 이미지 | 6종 얼굴 피부병 | 2,656 | 임상 카메라 | - | 일부 공개 | IEEE Access |
| AVEC | 비디오+오디오 | 우울/감정 | 다수 | 인터뷰 비디오 | - | 연구 신청 | avec2014.cs.nott.ac.uk |
| Face2Gene 코호트 | 얼굴 이미지 | 200+ 유전 증후군 | 17,000+ | 임상 사진 | - | 비공개(상용) | face2gene.com |
| FaceAge / AIM-Harvard | 얼굴 이미지 | 생물학적 나이/예후 | 58,851+6,196 | 공개+임상 | - | 모델 공개 | github.com/AIM-Harvard/FaceAge |
| N-CNN NICU (iCOPE) | 얼굴 비디오 | 신생아 통증 | 수백명 | NICU | - | 일부 공개 | iCOPE 류 |
| AcneDet 1572 | 얼굴 이미지 | 여드름 등급 | 1,572 | 스마트폰 | - | 비공개 | MDPI Diagnostics 2022 |
| TAO multicenter | 얼굴 이미지 | 갑상선안병증 | 다기관 | 임상 사진 | - | 비공개 | Sci Rep 2022 |
| Conjunctiva 764→4315 | 얼굴 이미지 | 빈혈 | 4,315(증강) | 스마트폰 | - | 비공개 | HIR 2025 |
| UCI Parkinson Voice | 음성 | PD | 31명/195 녹음 | 임상실 | 영어 | 공개 | UCI ML Repo |
| UCI Parkinson Telemonitoring | 음성 | PD | 42명/5,875 녹음 | 가정 | 영어 | 공개 | UCI ML Repo |
| mPower (Sage Bionetworks) | 음성 | PD | 9,520+ | iPhone | 영어 | 공개(등록) | Synapse |
| Saarbrücken Voice DB (SVD) | 음성 | 음성장애 다수 | 2,043명 | 임상실 | 독일어 | 공개 | Saarland Univ |
| DementiaBank Pitt | 음성+텍스트 | AD/MCI | 397+ | 임상실 | 영어 | 학술 신청 | TalkBank |
| ADReSS / ADReSSo | 음성 | AD | 156+ | 임상실 | 영어 | 챌린지 | Edinburgh |
| DAIC-WOZ / E-DAIC | 음성+영상 | 우울증·PTSD·불안 | 189/275 | WoZ 인터뷰 | 영어 | 학술 신청 | USC ICT |
| Coswara | 음성 | COVID-19 | 2,746명 | 웹 크라우드 | 다국어 | 공개 | IISc Bangalore |
| COUGHVID | 기침음 | COVID-19 | 27,550 녹음 | 웹 크라우드 | 다국어 | 공개 | EPFL |
| ICBHI 2017 | 호흡음 | COPD/천식/폐렴 | 920 녹음/126명 | 청진기 | - | 공개 | ICBHI |
| AIHub 구음장애 | 음성 | 구음장애 | 1,200+명/5,000h+ | 임상 | 한국어 | 공개 | aihub.or.kr |

---

## 9. 연구 공백 및 향후 과제

| 공백 영역 | 설명 | 본 하네스 기회 |
|----------|------|---------|
| **자궁내막증 얼굴/음성 직접 연구** | 양 모달리티에서 직접 분류 연구 사실상 부재 | 만성통증 표정 AU + 호르몬성 음성 변화 통합 모델 |
| **PCOS 얼굴 단독 멀티 표현형** | 공막(Lv 2021) 또는 여드름 단독, 통합 모델 부재 | 여드름+다모증+공막+FaceAge 멀티헤드 |
| **PCOS 음성 ML 분류기** | 통계 음성 변화는 입증, ML AUC 보고 부재 | Wav2Vec 2.0 / eGeMAPS 한국 PCOS 코호트 분류기 |
| **Hirsutism 자동 점수화** | Ferriman-Gallwey 얼굴 영역 자동 점수 ML 거의 없음 | 모발·턱·상순 픽셀 분할 + 점수 회귀 |
| **얼굴+음성 멀티모달** | 단일 모달리티 연구가 다수 | PCOS·자궁내막증·정신건강 통합 평가 멀티모달 |
| **종단(Longitudinal) 모니터링** | 단발 진단이 다수, 변화 추적 부재 | 셀피+음성 timeseries로 호르몬 주기·치료 효과 추적 |
| **한국어 임상 음성 데이터셋** | PCOS/갑상선/당뇨/심부전 한국어 음성 전무 | 한국 코호트 구축 자체가 데이터 제안서 핵심 가치 |
| **다민족 검증** | 단일 인종 코호트 우세 | 한국 + 다인종 비교 검증 |
| **Cross-corpus 일반화** | COVID-19 cough AUC 0.43-0.68 등 일반화 실패 | 데이터셋 아티팩트 vs 질병 신호 분리 방법론 |
| **임상 해석가능성(XAI)** | Black-box CNN/Transformer 임상 채택 장벽 | Attention map + 음소별 distortion + AU explanation 결합 |
| **환경 잡음 강건성** | 대부분 임상실 녹음·표준 조명 | 가정·차량·실생활 환경 강건 모델 |
| **장기 모니터링 라벨 신뢰성** | 자가 보고 라벨(PHQ-8, 자가식별 PD) noisy | 임상 진단 페어 + 장기 추적 코호트 |

---

## 10. 핵심 논문 Top 10 추천 (얼굴 5 + 음성 5)

### 얼굴 바이오마커 Top 5

1. **Bontempi et al., 2025, Lancet Digit Health — FaceAge** ✅
   - 생물학적 나이 추정의 임상 표준. 코드 공개(GitHub AIM-Harvard/FaceAge), 6,196 암 환자 외부 검증, 임상의 AUC 0.74→0.80 향상. PCOS 만성 노화 가설 검증의 인프라.
2. **Lv et al., 2021, Front Endocrinol — Scleral Images for PCOS** ✅
   - 얼굴 이미지 단독 PCOS 분류의 사실상 유일한 모델. AUC=0.979, accuracy=0.929. 본 하네스의 직접 비교군.
3. **Gurovich et al., 2019, Nat Med — DeepGestalt/Face2Gene** ✅
   - 얼굴 형태학 AI의 기념비. 200+ 유전 증후군, Top-10 sens 91%. 상용화된 유일한 얼굴 의료 AI.
4. **TED Detection, 2025, Am J Ophthalmol** ✅
   - 갑상선안병증 검출의 SOTA. AUC=0.997, sens 99.7%, spec 94.5%. 갑상선 ↔ PCOS 동반 가능성 연결고리.
5. **Mariakakis et al., 2017, ACM IMWUT — BiliScreen** ✅
   - 스마트폰 색보정 + 공막 황달 검출의 원조. sens 89.7%, spec 96.8%. 얼굴 색상 기반 비침습 진단 패러다임.

### 음성 바이오마커 Top 5

1. **Favaro et al., 2025, Bioengineering — Wav2Vec 2.0 PD Detection** ⚠️
   - 자가지도 음성 임베딩의 cross-corpus 일반화 실증. 4개 다국어 코호트 cross-corpus AUC=0.92.
2. **Luz et al., 2020, INTERSPEECH — ADReSS Challenge** ✅
   - AD 음성 연구의 표준 벤치마크. 156명 데이터셋·baseline 코드·정해진 train/test로 메타비교 가능.
3. **Yang/Huang et al., 2024, Sci Rep — Depression Wav2Vec 2.0** ⚠️
   - DAIC-WOZ Wav2Vec 2.0 fine-tuning F1=0.88, RMSE=4.3 (PHQ-8). 우울증 음성 SOTA.
4. **Faurholt-Jepsen et al., 2016, Transl Psychiatry — Bipolar Daily Calls** ✅
   - 일상 통화 종단 모니터링의 모범. 28명·121일·조증 AUC=0.89·우울 AUC=0.78. 본 하네스 종단 설계의 참조 표준.
5. **Aydin et al., 2010 + 2024, J Voice / Egypt J Otolaryngol — PCOS Voice** ✅
   - PCOS 음성 변화의 임상 근거. F0 감소·MPT 감소·throat-clearing 증가. ML 분류기 미개발 — 본 하네스의 직접 후속.

**보너스 (한국어)**:
- **서울대 박사학위 2024 (AD)** + **서울대 박사학위 2022 (우울/자살, 음성 AUC=0.806)** — 한국어 임상 음성 ML의 사실상 유일한 박사급 연구. 본 하네스 한국 코호트 설계 시 IRB·발화과제·전처리 파이프라인 참조처.

---

**보고서 종료** | face-voice-research 하네스 / face-voice-synthesizer
