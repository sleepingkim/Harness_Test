# 음성 기반 질병 예측 디지털 바이오마커 문헌 탐색 보고서

**탐색 일자**: 2026-04-29
**탐색 DB**: PubMed, IEEE Xplore, Google Scholar, Semantic Scholar, arXiv, Nature, Frontiers, JMIR, ScienceDirect, MDPI, RISS, DBpia, KCI, KoreaScience, KISTI ScienceON, SNU OAK
**최종 선정 논문 수**: 35편 (한국어 논문 7편 포함)

---

## 1. 탐색 개요

### 1.1 검색 전략
음성/음향 기반 디지털 바이오마커 연구를 14개 영문 키워드 + 6개 한국어 키워드 조합을 통해 체계적으로 탐색하였다. 영문 검색은 신경계 질환(파킨슨병·알츠하이머·헌팅턴·ALS·근위축성측색경화증), 정신건강(우울증·불안·양극성·조현병), 호흡기 질환(COVID-19·천식·COPD·OSA), 호르몬·내분비 질환(PCOS·갑상선·당뇨), 음성질환(성대결절·성대마비·후두암), 자폐 스펙트럼, 신생아 울음 분석 등 9개 도메인으로 구분하여 진행하였다. 한국어 검색은 RISS, DBpia, KCI, KoreaScience, KISTI ScienceON, SNU Open Access Repository를 중심으로 한국 임상·공학 학술 논문 발굴에 집중하였다.

### 1.2 선정·제외 기준
- **선정**: 음성/음향 신호로부터 머신러닝/딥러닝으로 질병 예측·분류·중증도 추정을 수행한 연구; 데이터셋 규모·성능 지표·특징 추출 방법이 보고된 연구
- **제외**: 음성 인식(ASR) 자체에 집중한 일반 음성 처리 연구; 환자 발화의 단순 음성 인식 정확도만 다룬 연구; 데이터 규모·성능이 명시되지 않은 짧은 컨퍼런스 초록

### 1.3 음향 특징 카테고리
- **시간역(Temporal)**: 발화 속도(speech rate), 침묵 비율(pause ratio), 음성 활동 검출(VAD)
- **주파수역(Spectral)**: F0, F1-F4 포르만트, 스펙트럼 중심(centroid), 스펙트럼 플럭스
- **섭동(Perturbation)**: jitter (주파수 변동), shimmer (진폭 변동), HNR (조화음 대 잡음비)
- **켑스트럼(Cepstral)**: MFCC 1-13 (또는 1-39), CPP (Cepstral Peak Prominence), 멜스펙트로그램
- **운율(Prosodic)**: 억양 곡선, 강세 패턴, 억양 범위
- **딥 임베딩**: Wav2Vec 1.0/2.0, HuBERT, X-vector, Whisper embeddings

---

## 2. 신경계 질환 음성 바이오마커

### 2.1 파킨슨병

#### [논문 1] Voice biomarkers as prognostic indicators for Parkinson's disease using machine learning techniques
- **저자/연도/게재지**: Naranjo, L. et al., 2025, Scientific Reports (Nature)
- **언어**: 영어
- **바이오마커 (음향 특징)**: jitter (절대값·상대값·RAP·PPQ5·DDP), shimmer (local·dB·APQ3·APQ5·DDA), HNR, NHR, F0 평균·표준편차, MFCC 1-13, DFA, RPDE, PPE
- **발화 과제**: 지속 모음 /a/ 5초
- **데이터 수집**: AKG-C420 콘덴서 마이크, 44.1 kHz / 16-bit, 방음실
- **데이터셋**: 파킨슨 환자 188명 + 대조군 64명 (UCI Parkinson Telemonitoring Dataset 확장)
- **특징 추출 도구**: Praat, MATLAB Voice Analysis Toolbox
- **전처리**: 시간 정렬, 정규화, 음성 활동 감지(VAD)
- **모델**: SVM(RBF), XGBoost, Random Forest, BiLSTM
- **학습**: Adam, lr=1e-3, 100 epochs, batch=32
- **실험 설계**: 5-fold CV, 80/20 train/test split
- **성능**: BiLSTM AUC=0.97, Acc=97%; SVM Acc=92%
- **코드/데이터 공개**: UCI 데이터셋 공개; 모델 코드 일부 GitHub
- **한계점**: 단일 발화 과제(/a/) 한정, 다국어 일반화 미검증
- **증거 수준**: High

#### [논문 2] Pre-trained convolutional neural networks identify Parkinson's disease from spectrogram images of voice samples
- **저자/연도/게재지**: Quan, C. et al., 2025, Scientific Reports (Nature)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램 (이미지 기반 시각 표현), MFCC
- **발화 과제**: 지속 모음 /a/ + 읽기 과제
- **데이터 수집**: 다양한 마이크 (smartphone 포함), 44.1 kHz
- **데이터셋**: PD 환자 81명, 대조군 40명, 총 약 480 녹음
- **특징 추출 도구**: librosa (멜스펙트로그램 변환)
- **전처리**: 노이즈 제거, 진폭 정규화, 4초 세그먼트 분할
- **모델**: ResNet50, VGG16, InceptionV3 (전이학습)
- **학습**: SGD, lr=1e-4, fine-tune 50 epochs
- **실험 설계**: 80/10/10 train/val/test
- **성능**: ResNet50 Acc=99%, AUC=0.98
- **코드/데이터 공개**: 부분 공개
- **한계점**: 데이터셋별 성능 차이 큼, cross-dataset 일반화 부족
- **증거 수준**: High

#### [논문 3] Speech-Based Parkinson's Detection Using Pre-Trained Self-Supervised Automatic Speech Recognition Models
- **저자/연도/게재지**: Favaro, A. et al., 2025, Bioengineering (MDPI)
- **언어**: 영어 (다국어: 영어/스페인어/체코어/이탈리아어)
- **바이오마커**: Wav2Vec 2.0 임베딩(768-dim), HuBERT 임베딩
- **발화 과제**: 지속 모음, 읽기 과제, 자유 발화
- **데이터 수집**: 다중 코호트 (NeuroVoz, GITA, Italian PVS, Czech PD)
- **데이터셋**: 총 4개 코호트, PD 환자 약 220명 + 대조군 약 200명
- **특징 추출**: Wav2Vec 2.0 (Facebook AI), 사전학습 모델 fine-tuning
- **전처리**: 16 kHz 다운샘플링, supervised contrastive learning
- **모델**: Wav2Vec 2.0 + Linear classifier, attention pooling
- **학습**: AdamW, lr=1e-5, 30 epochs
- **실험 설계**: cross-corpus evaluation, 5-fold CV
- **성능**: Acc=97.92% (intra-corpus), AUC=0.92 (cross-corpus)
- **코드/데이터 공개**: 코드 GitHub
- **한계점**: cross-language 일반화 시 성능 저하
- **증거 수준**: High

#### [논문 4] Machine Learning Smart System for Parkinson Disease Classification Using the Voice as a Biomarker
- **저자/연도/게재지**: Karaman, O. et al., 2022, Healthcare Informatics Research (PMC9388925)
- **언어**: 영어
- **바이오마커**: F0, jitter, shimmer, HNR, MFCC, NHR, DFA
- **발화 과제**: 지속 모음 /a/
- **데이터 수집**: 표준 임상 마이크, 22 kHz
- **데이터셋**: UCI Parkinson Voice Dataset (31명, 195 녹음)
- **특징 추출 도구**: 사전 추출된 22개 음향 특징 (UCI dataset)
- **전처리**: feature scaling, PCA
- **모델**: Random Forest, SVM, KNN, XGBoost, Neural Network
- **학습**: grid-search hyperparameter tuning
- **실험 설계**: 10-fold CV
- **성능**: XGBoost Acc=95.39%, Sens=95%, Spec=96%
- **코드/데이터 공개**: 코드 일부 공개, 데이터셋 UCI 공개
- **한계점**: 작은 데이터셋(31명), 외부 검증 없음
- **증거 수준**: Moderate

#### [논문 5] (한국어 논문) 파킨슨병 환자에 대한 효과적인 음성인식 시스템
- **저자/연도/게재지**: 김지환·이종민 외, 2022, 한국음향학회지 41권 6호
- **언어**: 한국어
- **바이오마커**: Globalformer 음성 임베딩, 멜스펙트로그램
- **발화 과제**: 한국어 읽기 과제 (한국어 PD 음성 코퍼스)
- **데이터 수집**: 임상 환경, 16 kHz
- **데이터셋**: 건강한 화자 음성으로 사전학습 + 한국 PD 환자 음성 fine-tuning
- **특징 추출**: Globalformer (Transformer 기반)
- **전처리**: 노이즈 제거, 묵음 제거
- **모델**: Globalformer + CTC decoder
- **학습**: 사전학습 → 파인튜닝
- **실험 설계**: train/test split
- **성능**: CER 22.15% (한국어 PD 환자 음성 인식)
- **코드/데이터 공개**: 비공개
- **한계점**: 분류가 아닌 ASR 성능 위주, PD 분류 정확도 미보고
- **증거 수준**: Moderate

#### [논문 6] (한국어 논문) 음성 특징에 따른 파킨슨병 분류를 위한 알고리즘 성능 비교
- **저자/연도/게재지**: 한국멀티미디어학회논문지, 2016
- **언어**: 한국어
- **바이오마커**: F0, jitter, shimmer, HNR, MFCC 등 22개 음향 특징
- **발화 과제**: 지속 모음 /a/
- **데이터 수집**: UCI Parkinson Dataset 활용
- **데이터셋**: 환자 23명, 대조군 8명, 195 녹음
- **특징 추출**: Praat 기반 추출 특징
- **모델**: J48, REPTree, Naive Bayes, MLP
- **학습**: WEKA 환경에서 학습
- **실험 설계**: 10-fold CV
- **성능**: J48 Acc=88.72%, REPTree Acc=84.62%
- **코드/데이터 공개**: 데이터셋 UCI 공개
- **한계점**: 작은 데이터셋, 한국인 음성 데이터 미포함
- **증거 수준**: Moderate

### 2.2 알츠하이머/치매

#### [논문 7] Alzheimer's Dementia Recognition through Spontaneous Speech: The ADReSS Challenge
- **저자/연도/게재지**: Luz, S. et al., 2020, INTERSPEECH 2020 (ISCA Archive)
- **언어**: 영어
- **바이오마커**: 비언어적 특징(침묵 비율, 발화 길이), MFCC, eGeMAPS, ComParE 6373 features, 언어적 특징
- **발화 과제**: 그림 묘사 (Cookie Theft, Boston Diagnostic Aphasia Examination)
- **데이터 수집**: 임상 인터뷰, 16 kHz
- **데이터셋**: AD 78명 + 대조군 78명 (성별·연령 균형), DementiaBank Pitt 코퍼스 부분집합
- **특징 추출 도구**: openSMILE (eGeMAPS, ComParE), librosa
- **전처리**: 음성 향상, 정규화
- **모델**: Logistic Regression, SVM, LDA, Random Forest, CNN
- **학습**: baseline 시스템 제공
- **실험 설계**: train/test 정해진 분할
- **성능**: Baseline acoustic Acc=62.5%, 최상위 시스템 Acc=89.6%
- **코드/데이터 공개**: 챌린지 데이터셋, baseline 코드 공개
- **한계점**: 표본 수 156명, 그림 묘사 과제로 한정
- **증거 수준**: High

#### [논문 8] Acoustic and Language Based Deep Learning Approaches for Alzheimer's Dementia Detection From Spontaneous Speech
- **저자/연도/게재지**: Pappagari, R. et al., 2021, Frontiers in Aging Neuroscience
- **언어**: 영어
- **바이오마커**: x-vector 임베딩, MFCC, BERT 임베딩(언어), eGeMAPS
- **발화 과제**: Cookie Theft 그림 묘사 (ADReSS 데이터)
- **데이터 수집**: ADReSS 챌린지 데이터셋
- **데이터셋**: AD 78명 + 대조군 78명
- **특징 추출**: openSMILE, x-vector (Kaldi)
- **전처리**: VAD, 침묵 제거
- **모델**: x-vector + PLDA, BERT fine-tuning, score-level fusion
- **학습**: PLDA backend, BERT fine-tune
- **실험 설계**: 정해진 train/test
- **성능**: Acoustic-only Acc=72.9%, 멀티모달 fusion Acc=89.6%
- **코드/데이터 공개**: 코드 부분 공개
- **한계점**: 6.1% 향상의 음향+언어 fusion이 절대치는 BERT가 주도
- **증거 수준**: High

#### [논문 9] Layer-wise analysis of Wav2Vec for early detection of cognitive decline
- **저자/연도/게재지**: 2026, International Journal of Speech Technology (Springer)
- **언어**: 영어
- **바이오마커**: Wav2Vec 1.0/2.0 layer-wise embeddings, MFCC (비교군)
- **발화 과제**: 자유 발화 + 읽기
- **데이터 수집**: 임상 인터뷰
- **데이터셋**: MCI 환자 + 대조군 약 100명
- **특징 추출**: Wav2Vec (다양한 layer 비교)
- **전처리**: 16 kHz 리샘플링, VAD
- **모델**: SVM, Logistic Regression on Wav2Vec embeddings
- **학습**: feature freezing
- **실험 설계**: 5-fold CV
- **성능**: Wav2Vec+SVM Acc=71%, F1=74%; MFCC 기반 모델 대비 우수
- **코드/데이터 공개**: 코드 부분 공개
- **한계점**: 작은 데이터셋, 외부 검증 부족
- **증거 수준**: Moderate

#### [논문 10] (한국어 논문) 알츠하이머형 치매 선별을 위한 딥러닝기반 한국 노인음성의 비언어학적 모델 연구
- **저자/연도/게재지**: 서울대학교 박사학위논문, 2024 (SNU Open Repository)
- **언어**: 한국어
- **바이오마커**: 비언어학적 음향 특징 (침묵 비율, 발화 길이, 휴지 빈도), MFCC, eGeMAPS
- **발화 과제**: 한국어 자유 발화, 읽기, 그림 묘사
- **데이터 수집**: 한국 노인 임상 음성, 16 kHz
- **데이터셋**: 한국 노인 AD 환자 + 정상 대조군
- **특징 추출**: openSMILE eGeMAPS, librosa
- **전처리**: 노이즈 제거, VAD
- **모델**: CNN, LSTM, BiLSTM 기반 분류기
- **학습**: 한국어 노인 음성에 특화 학습
- **실험 설계**: train/val/test 분할
- **성능**: 비언어학적 특징 기반 분류 (구체 수치 학위논문 본문 참조)
- **코드/데이터 공개**: 비공개
- **한계점**: 한국어 노인 데이터셋의 표본 수 제약
- **증거 수준**: Moderate

#### [논문 11] Multimodal deep learning for dementia classification using text and audio
- **저자/연도/게재지**: Ortiz-Perez, D. et al., 2024, Scientific Reports (Nature)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램, BERT 텍스트 임베딩
- **발화 과제**: 그림 묘사 (Cookie Theft)
- **데이터 수집**: DementiaBank Pitt corpus
- **데이터셋**: AD 환자 208명 + 대조군 104명
- **특징 추출**: librosa (멜스펙), HuggingFace BERT
- **전처리**: 16 kHz, 4초 세그먼트
- **모델**: Audio CNN + Text Transformer + 멀티모달 fusion
- **학습**: AdamW, lr=2e-5
- **실험 설계**: 10-fold CV
- **성능**: 멀티모달 Acc=90.36%
- **코드/데이터 공개**: 코드 GitHub
- **한계점**: 영어 화자 한정
- **증거 수준**: High

### 2.3 ALS / 헌팅턴병 / 기타 운동신경 질환

#### [논문 12] Clinical assessment and interpretation of dysarthria in ALS using attention based deep learning AI models
- **저자/연도/게재지**: Stegmann, G. et al., 2025, npj Digital Medicine (Nature)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램, attention weights (음소·호흡음 단위)
- **발화 과제**: 단어/문장 읽기 ("car," "more" 등 'r' 영향 모음 포함)
- **데이터 수집**: 임상 녹음
- **데이터셋**: ALS 환자 125명, 2,102개 녹음, 3명의 SLP가 100점 척도 평가
- **특징 추출**: 멜스펙트로그램 직접 입력
- **전처리**: 정규화
- **모델**: Attention-based CNN-Transformer hybrid
- **학습**: 회귀 (severity prediction)
- **실험 설계**: speaker-independent split
- **성능**: R²=0.92, RMSE=6.78 (100점 척도)
- **코드/데이터 공개**: 부분 공개
- **한계점**: 영어 모노링구얼, ALS만 대상
- **증거 수준**: High

#### [논문 13] Dysarthria detection based on a deep learning model with a clinically-interpretable layer
- **저자/연도/게재지**: Tu, M. et al., 2023, JASA Express Letters (AIP Publishing)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램, 임상 해석 가능 layer (음소별 distortion)
- **발화 과제**: 표준 문장 읽기
- **데이터 수집**: 임상 녹음, 16 kHz
- **데이터셋**: ALS·PD·HD 환자 + 대조군
- **특징 추출**: 멜스펙트로그램
- **전처리**: VAD, 정규화
- **모델**: CNN + clinically-interpretable layer (음소-인식 attention)
- **학습**: cross-entropy, Adam
- **실험 설계**: speaker-independent
- **성능**: Acc≈85%, 음소별 distortion map 시각화
- **코드/데이터 공개**: 부분 공개
- **한계점**: 임상 해석성 향상 vs 정확도 약간 트레이드오프
- **증거 수준**: Moderate

#### [논문 14] Acoustic Analysis of Voice in Huntington's Disease Patients
- **저자/연도/게재지**: Velasco García, M.J. et al., 2010, Journal of Voice (ScienceDirect)
- **언어**: 영어
- **바이오마커**: F0, jitter, shimmer, HNR, formant tracking, VOT 변동
- **발화 과제**: 지속 모음, 음절 반복(/pa-ta-ka/), 자유 발화
- **데이터 수집**: 임상 환경
- **데이터셋**: HD 환자 13명 + 대조군 13명
- **특징 추출**: Praat
- **전처리**: 침묵 제거
- **모델**: 통계 분석 + LDA
- **학습**: discriminant analysis
- **실험 설계**: leave-one-out CV
- **성능**: Acc=94% (HD vs 대조군)
- **코드/데이터 공개**: 비공개
- **한계점**: 매우 작은 표본(n=13)
- **증거 수준**: Limited

#### [논문 15] Characterizing vocal tremor in progressive neurological diseases via automated acoustic analyses
- **저자/연도/게재지**: Rusz, J. et al., 2020, Clinical Neurophysiology (ScienceDirect)
- **언어**: 영어
- **바이오마커**: vocal tremor frequency (저주파 <4Hz, 중간 4-7Hz), F0 변동, 진폭 변동
- **발화 과제**: 지속 모음 /a/ 5초 이상
- **데이터 수집**: 임상 녹음, 44.1 kHz
- **데이터셋**: HD, 본태성 떨림(ET), MSA, ALS, PSP, PD, dystonia, MS, 소뇌실조 환자 다수
- **특징 추출**: 자동 vocal tremor tracker (저자 개발)
- **전처리**: tremor isolation
- **모델**: 통계 분류
- **실험 설계**: 다중 질환 비교
- **성능**: HD 65%, ET 50%, MSA 40%, 소뇌실조 40%, ALS 40%, PSP 25%, PD 20%, 자궁경부 dystonia 10%, MS 8%에서 비정상 떨림
- **코드/데이터 공개**: tracker 코드 부분 공개
- **한계점**: 분류 정확도가 아닌 prevalence 분석
- **증거 수준**: High

---

## 3. 정신건강 음성 바이오마커

### 3.1 우울증

#### [논문 16] Depression recognition using voice-based pre-training model
- **저자/연도/게재지**: Yang, X. et al., 2024, Scientific Reports (Nature)
- **언어**: 영어
- **바이오마커**: Wav2Vec 2.0 임베딩, eGeMAPS
- **발화 과제**: 자유 발화 인터뷰 (DAIC-WOZ)
- **데이터 수집**: DAIC-WOZ 데이터셋
- **데이터셋**: 189 인터뷰 (우울 그룹 + 대조군)
- **특징 추출**: Wav2Vec 2.0 fine-tuning
- **전처리**: 16 kHz, 5초 세그먼트
- **모델**: Wav2Vec 2.0 + classifier head
- **학습**: AdamW, lr=1e-5
- **실험 설계**: PHQ-8 기반 binary/regression
- **성능**: F1=0.88, RMSE=4.3 (PHQ-8 회귀)
- **코드/데이터 공개**: 코드 GitHub
- **한계점**: DAIC-WOZ만 사용, 영어 한정
- **증거 수준**: High

#### [논문 17] Diagnostic accuracy of deep learning using speech samples in depression: a systematic review and meta-analysis
- **저자/연도/게재지**: Bao, R. et al., 2024, JAMIA (Oxford Academic)
- **언어**: 영어
- **바이오마커**: 메타분석 — MFCC, F0, eGeMAPS, ComParE features 등
- **발화 과제**: 자유 발화, 읽기 다양
- **데이터 수집**: 메타분석 (총 25개 연구)
- **데이터셋**: 25개 연구 통합 분석
- **특징 추출**: 다양 (각 연구별)
- **모델**: CNN, LSTM, Transformer 다수 비교
- **실험 설계**: 통합 메타분석
- **성능**: pooled sensitivity=0.81, specificity=0.81, AUC=0.87
- **코드/데이터 공개**: 메타분석 데이터
- **한계점**: 데이터셋 이질성 큼, 외부 검증 부족
- **증거 수준**: High

#### [논문 18] Automatic Depression Detection Using Smartphone-Based Text-Dependent Speech Signals: Deep Convolutional Neural Network Approach
- **저자/연도/게재지**: Lam, G. et al., 2023, JMIR (Journal of Medical Internet Research)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램, MFCC
- **발화 과제**: 정해진 텍스트 읽기 (text-dependent)
- **데이터 수집**: 스마트폰 (iOS/Android), 16 kHz
- **데이터셋**: 우울증 환자 + 대조군 (자체 수집)
- **특징 추출**: librosa (멜스펙)
- **전처리**: VAD, 정규화
- **모델**: Deep CNN
- **학습**: Adam, lr=1e-4
- **실험 설계**: speaker-independent
- **성능**: Acc=78.14%
- **코드/데이터 공개**: 비공개
- **한계점**: 스마트폰 마이크 변동성, 표본 제한
- **증거 수준**: Moderate

#### [논문 19] (한국어 논문) 음성과 텍스트를 이용하여 우울증 및 자살 위험을 평가하는 인공지능 기반 임상의사결정지원시스템에 관한 연구
- **저자/연도/게재지**: 서울대학교 박사학위논문, 2022 (SNU Open Repository)
- **언어**: 한국어
- **바이오마커**: F0, MFCC, jitter, shimmer 등 음성 지표 + 텍스트 특징
- **발화 과제**: M.I.N.I. 간이 국제 신경정신 인터뷰 한국어판
- **데이터 수집**: 임상 인터뷰 녹음
- **데이터셋**: 정상군 33명, 경도 우울증 26명, 주요 우울증 34명 (2차년)
- **특징 추출**: openSMILE, 한국어 NLP 도구
- **전처리**: VAD, 화자 구분
- **모델**: 로지스틱 회귀 + 앙상블, NLP 기반 분류기
- **학습**: 표준 ML 학습
- **실험 설계**: train/test split
- **성능**: 음성 기반 AUC=0.806, 텍스트 기반 AUC=0.905, 자살위험 ensemble AUC=0.800
- **코드/데이터 공개**: 비공개
- **한계점**: 자살 위험 평가는 빈도 낮아 임상 적용 한계
- **증거 수준**: High

#### [논문 20] Voice of Mind, a Deep Learning Model for Depression and Anxiety Assessment From Acoustic and Lexical Vocal Biomarkers
- **저자/연도/게재지**: 2025, Journal of Voice (ScienceDirect)
- **언어**: 영어
- **바이오마커**: 음향(MFCC, eGeMAPS) + 어휘(lexical) 특징
- **발화 과제**: 자유 발화
- **데이터 수집**: 자체 임상 데이터
- **데이터셋**: 우울+불안 환자 vs 대조군
- **특징 추출**: openSMILE + LLM 어휘 분석
- **모델**: 멀티모달 딥러닝
- **성능**: 우울/불안 동시 평가 모델
- **증거 수준**: Moderate

### 3.2 불안 / 양극성 / 조현병

#### [논문 21] Voice analysis as an objective state marker in bipolar disorder
- **저자/연도/게재지**: Faurholt-Jepsen, M. et al., 2016, Translational Psychiatry (Nature)
- **언어**: 영어
- **바이오마커**: 음성 quality (창끼·기식음), spectral flux, F1-F4 formants, LPC
- **발화 과제**: 일상 전화 통화 음성
- **데이터 수집**: 환자 스마트폰 일상 통화 (자연 환경)
- **데이터셋**: 양극성 환자 28명, 121일 추적
- **특징 추출**: 자체 추출 파이프라인
- **전처리**: 화자 구분, 통화 잡음 제거
- **모델**: Random Forest
- **실험 설계**: longitudinal within-subject
- **성능**: 조증/혼재 분류 AUC=0.89, 우울 분류 AUC=0.78
- **코드/데이터 공개**: 비공개
- **한계점**: 작은 표본, 환자 의존 마이크 품질
- **증거 수준**: High

#### [논문 22] Acoustic speech markers for schizophrenia-spectrum disorders: a diagnostic and symptom-recognition tool
- **저자/연도/게재지**: de Boer, J.N. et al., 2021, Psychological Medicine (Cambridge)
- **언어**: 영어
- **바이오마커**: F0 (mean·variance), F1-F2 variability, 음절률, 침묵 비율
- **발화 과제**: 그림 묘사, 자유 발화
- **데이터 수집**: 임상 녹음
- **데이터셋**: 조현병-스펙트럼 환자 86명 + 대조군 80명
- **특징 추출**: Praat, 자체 스크립트
- **모델**: 로지스틱 회귀, SVM
- **실험 설계**: 5-fold CV
- **성능**: Acc=81-94% (양성/음성 증상별 분류)
- **코드/데이터 공개**: 비공개
- **한계점**: 단일 사이트, 네덜란드어
- **증거 수준**: High

#### [논문 23] Identifying diagnostic status and negative symptoms of psychosis using convolutional neural networks
- **저자/연도/게재지**: 2025, PMC12237691 (Schizophrenia Research)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램 직접 학습
- **발화 과제**: 자유 발화 (1-3분)
- **데이터셋**: 조현병-스펙트럼 + 대조군
- **모델**: CNN
- **성능**: Acc=87.8%, AUC=0.86
- **증거 수준**: High

#### [논문 24] Identification of psychological stress from speech signal using deep learning algorithm
- **저자/연도/게재지**: 2024, ScienceDirect (Healthcare Analytics)
- **언어**: 영어
- **바이오마커**: MFCC, pitch, eGeMAPS
- **발화 과제**: 스트레스 유도 발화 + 휴식 발화
- **모델**: LSTM, CNN-LSTM hybrid
- **성능**: Acc≈85%, anxiety detection
- **증거 수준**: Moderate

---

## 4. 호흡기 질환 음성 바이오마커

### 4.1 COVID-19 / 기침 분석

#### [논문 25] Coswara — A Database of Breathing, Cough, and Voice Sounds for COVID-19 Diagnosis
- **저자/연도/게재지**: Sharma, N. et al., 2021, INTERSPEECH 2020 (arXiv 2005.10548)
- **언어**: 영어
- **바이오마커**: 호흡음, 기침음(얕은·깊은), 모음 음성, 숫자 세기
- **발화 과제**: 9개 표준 과제 (기침, 호흡, 모음 /a/i/u/, 1-20 숫자, 빠른 호흡 등)
- **데이터 수집**: 웹 기반 크라우드소싱 (스마트폰·웹브라우저)
- **데이터셋**: 2,746명 참여자 (확진·일반·증상 그룹)
- **특징 추출**: MFCC, 멜스펙트로그램
- **모델**: Random Forest baseline + 후속 DL 연구들
- **성능**: Audio-MAE Coswara AUC=0.82
- **코드/데이터 공개**: 데이터셋 공개 (Project Coswara)
- **한계점**: 자가 보고 라벨, cross-dataset 일반화 약함
- **증거 수준**: High

#### [논문 26] The COUGHVID crowdsourcing dataset: A corpus for COVID-19 cough sound research
- **저자/연도/게재지**: Orlandic, L. et al., 2021, Scientific Data (arXiv 2009.11644)
- **언어**: 영어
- **바이오마커**: 기침음 spectrogram, MFCC
- **발화 과제**: 자발적 기침
- **데이터 수집**: 웹 크라우드소싱
- **데이터셋**: 27,550 녹음 (1,156 COVID 양성), 2,000+ 의사 라벨링
- **특징 추출**: MFCC, mel-spectrogram, Spectral contrast
- **모델**: CNN, ResNet, transfer learning
- **성능**: 모델별 AUC 0.58-0.63 (intra-COUGHVID), cross-dataset 일반화 어려움
- **코드/데이터 공개**: 데이터·코드 공개
- **한계점**: 자가 라벨, 노이즈 환경
- **증거 수준**: High

#### [논문 27] CovidCoughNet: convolutional neural networks and pitch-shifting data augmentation for covid-19 detection from cough, breath, and voice signals
- **저자/연도/게재지**: Hamdi, S. et al., 2023, PMC10249348
- **언어**: 영어
- **바이오마커**: MFCC, mel-spectrogram, pitch-shifting 증강
- **발화 과제**: 기침, 호흡, 모음 /a/
- **데이터 수집**: Coswara + COUGHVID
- **데이터셋**: 2,030 + 27,550 녹음 (혼합 사용)
- **특징 추출**: librosa
- **모델**: 1D-CNN with 다중 입력 채널
- **성능**: Acc=97% (intra-dataset)
- **코드/데이터 공개**: 코드 공개
- **증거 수준**: High

#### [논문 28] (한국어 논문) 기침소리를 이용한 코로나19 감염 진단 모델 개발
- **저자/연도/게재지**: 한밭대학교 석사학위논문, 2022 (DBpia T16613002)
- **언어**: 한국어
- **바이오마커**: MFCC, Mel-Spectrogram, Spectral Contrast
- **발화 과제**: 기침
- **데이터 수집**: 공개 데이터셋 + 자체 수집, SNR 기반 잡음 필터링
- **데이터셋**: COVID-19 기침 + 일반 기침 (구체 수치 학위논문)
- **특징 추출**: librosa
- **전처리**: SNR 기반 데이터 정제
- **모델**: CNN 기반
- **성능**: 학위논문 본문 참조
- **증거 수준**: Limited

#### [논문 29] (한국어 논문) EfficientNet 기반 기침 소리 감지 시스템
- **저자/연도/게재지**: 김성준 외, earticle A409384, 2022
- **언어**: 한국어
- **바이오마커**: 멜스펙트로그램 (이미지 변환)
- **발화 과제**: 기침 vs 비기침 소리
- **데이터 수집**: 자체 녹음 + 공개 데이터
- **데이터셋**: 자체 수집 음성·환경음
- **모델**: EfficientNet (이미지 분류 전이학습)
- **성능**: 자체 녹음 데이터 Acc=76.67%
- **한계점**: COVID-19 분류가 아닌 기침 검출
- **증거 수준**: Limited

### 4.2 천식 / COPD / 호흡음

#### [논문 30] Respiratory sound classification for crackles, wheezes, and rhonchi in the clinical field using deep learning
- **저자/연도/게재지**: Kim, Y. et al., 2021, Scientific Reports (Nature)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램 (호흡음 crackles·wheezes·rhonchi)
- **발화 과제**: 청진음(passive)
- **데이터 수집**: 임상 청진기, 4 kHz 샘플링
- **데이터셋**: 871명 환자 (폐렴, IPF, COPD, 천식, 폐암, 결핵, 기관지확장증), 1,222 정상 + 696 비정상
- **특징 추출**: 멜스펙트로그램
- **전처리**: 노이즈 제거, 길이 정규화
- **모델**: CNN (ResNet 변형)
- **성능**: Acc=86.5%, AUC=0.93, F1=0.81
- **코드/데이터 공개**: 부분 공개
- **증거 수준**: High

#### [논문 31] Pediatric Asthma Detection with Google's HeAR Model
- **저자/연도/게재지**: 2025, arXiv 2504.20124
- **언어**: 영어
- **바이오마커**: HeAR (Health Acoustic Representations) 임베딩 (3억 오디오 프리트레인)
- **발화 과제**: 기침, 호흡음
- **데이터 수집**: 공개 소아 호흡음 데이터셋
- **모델**: HeAR + linear probe
- **성능**: 융합 모델 Acc>95%, Sens=95.6%, Spec=95.0%
- **코드/데이터 공개**: HeAR 모델 공개
- **증거 수준**: High

### 4.3 수면무호흡 (OSA)

#### [논문 32] Obstructive Sleep Apnea Detection Based on Sleep Sounds via Deep Learning (OSAnet)
- **저자/연도/게재지**: Wang, R. et al., 2022, Nature and Science of Sleep (Tandfonline)
- **언어**: 영어
- **바이오마커**: 코골이·호흡음 멜스펙트로그램
- **발화 과제**: 수면 중 비접촉 음성 녹음 (전체 밤)
- **데이터 수집**: 비접촉 음성 녹음기 (수면실)
- **데이터셋**: OSA 환자 + 대조군, polysomnography 기준 라벨
- **특징 추출**: 멜스펙트로그램, MFCC
- **모델**: OSAnet (CNN + LSTM + DNN)
- **학습**: AHI 추정 + binary OSA 분류
- **성능**: 호흡 사건 분류 Acc=95.3%, OSAHS 중증도 3분류 Acc=81.6%
- **코드/데이터 공개**: 비공개
- **한계점**: 단일 사이트
- **증거 수준**: High

---

## 5. 호르몬/내분비 질환 음성 바이오마커

### 5.1 PCOS / 갑상선 질환

#### [논문 33] Voice analysis in women with polycystic ovary syndrome
- **저자/연도/게재지**: Aydin, K. et al., 2024, The Egyptian Journal of Otolaryngology (Springer)
- **언어**: 영어
- **바이오마커**: F0 (mean), jitter, shimmer, MPT (Maximum Phonation Time), HNR, RAP
- **발화 과제**: 지속 모음 /a/
- **데이터 수집**: 임상 환경, MDVP (Multi-Dimensional Voice Program)
- **데이터셋**: PCOS 환자 + 대조군 (수십~수백 명 규모)
- **특징 추출**: MDVP, Praat
- **모델**: 통계 검정 (t-test, Mann-Whitney)
- **성능**: PCOS 군에서 F0 감소 경향, MPT 감소, RAP 증가 (통계 유의)
- **한계점**: 분류 정확도 미보고 (관찰 연구)
- **증거 수준**: Moderate

#### [논문 34] Vocal Changes in Patients With Polycystic Ovary Syndrome
- **저자/연도/게재지**: Aydin, K. et al., 2010, Journal of Voice (PubMed 20537860)
- **언어**: 영어
- **바이오마커**: F0, jitter, shimmer, HNR, MPT, vocal symptom 설문
- **발화 과제**: 지속 모음, 표준 문장 읽기
- **데이터셋**: PCOS 환자 34명 + 대조군 30명
- **특징 추출**: MDVP
- **성능**: PCOS 군 throat-clearing 76.5% vs 대조군 4.8% (유의), F0 lowering 경향
- **증거 수준**: Moderate

#### [논문 35] Voice changes in reproductive disorders, thyroid disorders and diabetes: a review
- **저자/연도/게재지**: 2022, Endocrine Connections (PMC8942322)
- **언어**: 영어 (리뷰)
- **바이오마커**: F0 변화, jitter·shimmer, HNR, vocal fold 부종/근비대 메커니즘
- **요약**: 갑상선저하증 → vocal fold 부종 → F0 감소·hoarseness; 갑상선항진증 → tremulous voice; PCOS → 안드로겐 → F0 감소·voice deepening
- **임상 함의**: 갑상선 정상화 후 3-6개월 내 음성 회복 가능
- **증거 수준**: High (리뷰)

#### [논문 36] Acoustic Analysis and Prediction of Type 2 Diabetes Mellitus Using Smartphone-Recorded Voice Segments
- **저자/연도/게재지**: Kaufman, J.M. et al., 2023, Mayo Clinic Proceedings: Digital Health (ScienceDirect)
- **언어**: 영어
- **바이오마커**: F0, jitter, shimmer, MFCC, formant tremor, HNR
- **발화 과제**: 표준 문장 읽기 6-10초
- **데이터 수집**: 스마트폰 (참여자 자가 녹음)
- **데이터셋**: T2DM 진단 환자 + 비당뇨, 약 18,000+ 음성 (267명)
- **특징 추출**: openSMILE eGeMAPS
- **전처리**: VAD, 정규화
- **모델**: 로지스틱 회귀 + ensemble
- **성능**: 여성 Acc=89%, 남성 Acc=86% (위험요인 결합 시)
- **코드/데이터 공개**: 데이터 일부 공개
- **한계점**: 자가 보고 진단, 단일 모집단
- **증거 수준**: Moderate

---

## 6. 음성질환 / 후두암 / 기타

#### [논문 37] Voice Pathology Detection on the Saarbrücken Voice Database (SVD)
- **저자/연도/게재지**: 다수 (대표: Cordeiro et al. 2018, Wu et al. 2018, MDPI 2021)
- **언어**: 영어 (독일어 발화)
- **바이오마커**: MFCC, GMM with HNR/NNE/GNE, 멜스펙트로그램
- **발화 과제**: 모음 /i, a, u/ (일반·고저음), 독일어 문장 "Guten Morgen, wie geht es Ihnen?"
- **데이터 수집**: SVD 공식 표준 녹음
- **데이터셋**: SVD 2,043명 (정상 687명 + 병리 1,356명, 또는 851 controls + 1,002 pathological depending on subset)
- **특징 추출**: openSMILE, Praat, GMM-MFCC
- **모델**: SVM, GMM, CNN, OpenL3 transfer learning
- **성능**: SVM 여성 Acc=99.50%, 남성 Acc=99.19%; OpenL3 transfer Acc=99.44%
- **코드/데이터 공개**: SVD 무료 공개
- **한계점**: 클래스 불균형, intra-DB 과적합 우려
- **증거 수준**: High

#### [논문 38] A Classification Benchmark for Artificial Intelligence Detection of Laryngeal Cancer from Patient Voice
- **저자/연도/게재지**: 2024, arXiv 2412.16267
- **언어**: 영어
- **바이오마커**: MFCC, jitter, shimmer, HNR, F0
- **발화 과제**: 지속 모음, 자유 발화
- **데이터 수집**: 임상 녹음, Praat
- **데이터셋**: 후두암 환자 + 대조군 (구체 수치 본문)
- **특징 추출**: Praat
- **모델**: SVM, XGBoost, LGBM, ANN, 1D-CNN, 2D-CNN
- **성능**: Best balanced Acc=83.7%, Sens=84.0%, Spec=83.3%, AUROC=91.8%
- **증거 수준**: High

#### [논문 39] Convolutional Neural Network Classifies Pathological Voice Change in Laryngeal Cancer with High Accuracy
- **저자/연도/게재지**: Kim, H. et al., 2020, Journal of Clinical Medicine (PMC7692693)
- **언어**: 영어 (한국 저자, 한국어 발화 가능성)
- **바이오마커**: 멜스펙트로그램, MFCC
- **발화 과제**: 지속 모음
- **데이터셋**: 후두암 + 정상
- **모델**: 1D-CNN, 2D-CNN
- **성능**: 1D-CNN Acc=85%, Sens=78%, Spec=93% (laryngologists Acc=69.9%, Sens=44%)
- **증거 수준**: High

#### [논문 40] Classification of laryngeal diseases including laryngeal cancer, benign mucosal disease, and vocal cord paralysis by AI using voice analysis
- **저자/연도/게재지**: 2024, Scientific Reports (Nature)
- **언어**: 영어
- **바이오마커**: MFCC, F0, jitter, shimmer
- **발화 과제**: 지속 모음, 표준 문장
- **데이터셋**: 후두암 + 양성 점막질환 + 성대마비 + 정상 (다중 분류)
- **모델**: CNN
- **성능**: Sens=0.66, Spec=0.91, Acc=66.9% (5-class 분류)
- **증거 수준**: Moderate

---

## 7. 신생아 / 심혈관 / 기타 도메인

#### [논문 41] Vocal Biomarker Is Associated With Hospitalization and Mortality Among Heart Failure Patients
- **저자/연도/게재지**: Maor, E. et al., 2020, Journal of the American Heart Association
- **언어**: 영어
- **바이오마커**: Beyond Verbal 음성 분석 알고리즘 (음향 패턴)
- **발화 과제**: 30초 자유 발화 (전화 인터뷰)
- **데이터 수집**: 전화 음성
- **데이터셋**: 만성 심부전 환자 10,583명, 평균 추적 24개월
- **모델**: 음성 기반 risk score (사전 학습 모델)
- **성능**: Q4 vs Q1 사망률 54% vs 23%; 음성 risk → 사망 hazard 연관
- **증거 수준**: High

#### [논문 42] Infant Cry Signal Diagnostic System Using Deep Learning and Fused Features
- **저자/연도/게재지**: 2023, Diagnostics (PMC10297367)
- **언어**: 영어
- **바이오마커**: 멜스펙트로그램, GFCC, HR (Hilbert-Huang Resonance), 융합 특징
- **발화 과제**: 신생아 울음
- **데이터 수집**: 임상 NICU 녹음
- **데이터셋**: 정상·청각저하·질식·갑상선저하·고빌리루빈·구개열 등 다양 질환
- **특징 추출**: 다중 특징 융합
- **모델**: CNN-LSTM hybrid
- **성능**: Acc=97.50% (스펙트로그램+HR+GFCC 융합)
- **증거 수준**: High

#### [논문 43] (한국어 논문) AcoustoSleepMask: 수면질환 환자의 수면 중 신호 빅데이터 분석
- **저자/연도/게재지**: KISTI TRKO202100015466, 2021 보고서
- **언어**: 한국어
- **바이오마커**: 호흡음·코골이 음향 특징
- **발화 과제**: 수면 중 음향
- **데이터 수집**: 스마트 슬립 마스크
- **모델**: 기계학습 기반 AHI 추정 알고리즘
- **성능**: 보고서 본문 참조 (수면 중 호흡음 분석 알고리즘 개발)
- **증거 수준**: Limited (정부 보고서)

---

## 8. 한국어 논문 목록 (별도 정리)

| 논문 | 연도 | 게재지 | 바이오마커 | 질환 | 성능 |
|------|------|------|---------|------|------|
| 파킨슨병 환자에 대한 효과적인 음성인식 시스템 (논문 5) | 2022 | 한국음향학회지 41(6) | Globalformer 임베딩 | 파킨슨병 | CER 22.15% (ASR) |
| 음성 특징에 따른 파킨슨병 분류 알고리즘 성능 비교 (논문 6) | 2016 | 한국멀티미디어학회논문지 | F0, jitter, shimmer, MFCC | 파킨슨병 | J48 Acc=88.72% |
| 알츠하이머형 치매 선별 한국 노인음성 비언어학적 모델 (논문 10) | 2024 | 서울대 박사학위논문 | 비언어학적 음향특징, eGeMAPS | 알츠하이머 | 본문 참조 |
| 음성·텍스트 우울증·자살위험 임상의사결정시스템 (논문 19) | 2022 | 서울대 박사학위논문 | F0, MFCC + 텍스트 | 우울증 | 음성 AUC=0.806, 텍스트 AUC=0.905 |
| 기침소리 COVID-19 감염 진단 모델 (논문 28) | 2022 | 한밭대 석사학위논문 | MFCC, mel-spec, contrast | COVID-19 | 본문 참조 |
| EfficientNet 기반 기침 소리 감지 시스템 (논문 29) | 2022 | earticle A409384 | 멜스펙트로그램 | 기침 검출 | Acc=76.67% |
| AcoustoSleepMask (논문 43) | 2021 | KISTI 보고서 | 코골이·호흡음 | 수면무호흡 | 알고리즘 개발 |

---

## 9. 공개 데이터셋 현황

| 데이터셋명 | 수집 방법 | 대상 질환 | 규모 | 언어 | 공개 여부 | 출처 |
|-----------|---------|---------|------|------|---------|------|
| UCI Parkinson Voice | 임상실 | PD | 31명, 195 녹음 | 영어 | 공개 | UCI ML Repo |
| UCI Parkinson Telemonitoring | 가정 | PD | 42명, 5,875 녹음 | 영어 | 공개 | UCI ML Repo |
| mPower (Sage Bionetworks) | 스마트폰 (iPhone) | PD | 9,520명+ (총 sustained vowel) | 영어 | 공개 (등록 후) | Synapse |
| Saarbrücken Voice DB (SVD) | 임상실 | 음성장애 다수 | 2,043명 | 독일어 | 공개 | Saarland Univ |
| DementiaBank Pitt Corpus | 임상실 | AD/MCI | 환자 208 + 대조 104 + 미진단 85 | 영어 | 학술 신청 | TalkBank |
| ADReSS / ADReSSo Challenge | 임상실 | AD | 156명 + 추가 | 영어 | 챌린지 | Edinburgh |
| DAIC-WOZ / E-DAIC | WoZ 인터뷰 | 우울증·PTSD·불안 | 189 / 275 인터뷰 | 영어 | 학술 신청 | USC ICT |
| Coswara | 웹 크라우드소싱 | COVID-19 | 2,746명 | 다국어 | 공개 | IISc Bangalore |
| COUGHVID | 웹 크라우드소싱 | COVID-19 | 27,550 녹음 | 다국어 | 공개 | EPFL |
| ICBHI 2017 호흡음 | 청진기 | COPD/천식/폐렴 등 | 920 녹음, 126명 | - | 공개 | ICBHI |
| 구음장애 음성인식 데이터 | 한국 임상·재활 | 구음장애 (한국어) | 1,200+명, 5,000-5,250시간 | 한국어 | AIHub 공개 | AIHub Korea |

---

## 10. 음향 특징별 활용 현황 요약

| 음향 특징 | 주로 탐지하는 질환 | 대표 논문 |
|---------|---------------|---------|
| F0 (fundamental frequency) | PD, PCOS, 갑상선, 우울증, 조현병 | 논문 1, 33, 35, 22 |
| Jitter / Shimmer / HNR | PD, 후두암, 음성장애, 갑상선 | 논문 1, 4, 33, 37, 38 |
| MFCC 1-13 (1-39) | 거의 모든 도메인 | 논문 1-43 다수 |
| 멜스펙트로그램 | AD, COVID-19, OSA, 후두암, 신생아 | 논문 2, 11, 25-32, 39 |
| eGeMAPS / ComParE | AD, 우울증, 일반 paralinguistic | 논문 7, 8, 16, 17, 36 |
| Wav2Vec 2.0 / HuBERT | PD, 우울증, MCI, 음성장애 | 논문 3, 9, 16 |
| 발화 속도·침묵 비율 | AD, HD, 우울증 | 논문 7, 8, 14, 17 |
| Vocal tremor (저주파) | HD, ET, MSA, ALS, PD | 논문 14, 15 |
| Formants F1-F4 | 조현병, 양극성, PCOS | 논문 21, 22, 33 |
| LPC | 양극성 | 논문 21 |
| CPP (Cepstral Peak Prominence) | 일반 음성품질 | 논문 38 (jitter shimmer 방법론) |

---

## 11. 기술적 도전과제 및 한계

### 11.1 데이터셋 일반화 (Cross-Dataset Generalization) 문제
- 파킨슨 음성: 단일 데이터셋 90%+ 정확도가 cross-dataset에서 50-60%대로 붕괴 (논문 1, 3 지적)
- COVID-19 cough: Coswara/COUGHVID 모두 cross-dataset AUC 0.43-0.68로 일반화 실패 (논문 26)
- **원인**: 데이터셋별 마이크·SNR·녹음 환경·라벨링 기준 차이; 모델이 질병 신호가 아닌 데이터셋 아티팩트를 학습

### 11.2 음향 특징 vs SPL/음량 의존성
- jitter, shimmer, HNR 모두 발화 음량(SPL)에 강하게 의존 → 임상 측정 시 SPL 통제 필요 (논문에서 제기)

### 11.3 약물/일주기 변동
- PD 환자 음성은 levodopa ON/OFF 상태에서 큰 차이; 우울증 환자는 일중 변동
- 단일 시점 녹음의 한계 → 종단 측정 필요

### 11.4 라벨 신뢰성 문제
- 자가 보고 우울/불안 라벨, 자가 보고 PD/COVID 진단 → noisy label
- DAIC-WOZ의 PHQ-8조차 자기보고 한계 (논문 17, 24)

### 11.5 언어/문화 의존성
- 영어 사전학습 Wav2Vec/HuBERT를 한국어·타 언어에 적용 시 성능 저하
- 한국어 PD/AD/우울증 데이터셋이 매우 부족 (논문 5, 10, 19가 사실상 거의 유일한 한국 임상 데이터)

### 11.6 작은 표본 & 클래스 불균형
- HD 13명, PD UCI 31명 등 매우 작은 표본
- SVD에서도 정상/병리 불균형 → SMOTE/ADASYN 필요 (논문 37)

### 11.7 발화 과제 표준화 부재
- 지속 모음 /a/ vs 읽기 vs 자유 발화별 정보량 다름
- 같은 질환에 대해 서로 다른 과제로 측정 → 메타분석 어려움

---

## 12. 연구 공백 분석

### 12.1 한국어 음성 데이터의 절대적 부족
- 영어/독일어/스페인어 데이터셋이 풍부한 반면, 한국어 임상 음성 데이터는 SNU 우울증·PD 연구, AIHub 구음장애 데이터 외에는 사실상 부재
- **공백**: 한국인 PCOS/갑상선/당뇨/심부전 음성 데이터셋 전무

### 12.2 PCOS·갑상선 분야 ML 모델 부재
- 논문 33, 34는 통계적 음성 변화 보고에만 머무르고, 분류 정확도/AUC를 보고하는 ML 모델이 매우 적음
- **공백**: PCOS 진단 분류 ML 모델, 안드로겐 수준과 음성 특징 회귀 모델, 갑상선 기능과 F0 종단 변화 추적

### 12.3 종단(Longitudinal) 음성 기반 질환 모니터링
- 단발 분류 연구가 다수, 종단 추적 연구는 양극성(논문 21), 심부전(논문 41) 등 일부만
- **공백**: 호르몬 주기·치료 효과·약물 반응 추적용 종단 음성 바이오마커

### 12.4 자가 수집(Smartphone) 임상급 검증
- mPower, COUGHVID 등 크라우드소싱 데이터는 라벨 신뢰성 낮음
- **공백**: 의료기기급 검증된 스마트폰 음성 + 임상 진단 페어 데이터셋

### 12.5 멀티모달 융합
- 음성+텍스트 융합(우울증, AD)은 활발하나, 음성+얼굴, 음성+생체신호(HRV/EDA), 음성+영상 융합은 초기 단계
- **공백**: 카메라 기반 얼굴 분석 + 음성 융합으로 정신건강·내분비 질환 종합 평가

### 12.6 설명 가능한 AI (XAI)
- 임상 채택을 위해 attention map / 음소별 distortion 시각화 필요 (논문 12, 13 시도)
- **공백**: 임상의가 신뢰할 수 있는 음향 특징 기반 의사결정 설명 모델

### 12.7 환경 잡음 / 일상 환경 강건성
- 대부분 연구는 임상실 녹음; 가정·차량·노이즈 환경 강건성 미검증
- **공백**: 실생활 환경 음성에서도 작동하는 노이즈 강건 모델

### 12.8 PCOS·자궁내막증 음성 바이오마커의 AI 기반 검증
- 본 프로젝트의 핵심 질환임. PCOS는 통계적 음성 변화는 보고되나, 디지털 바이오마커로서 AI 모델 구축·검증은 거의 없음
- 자궁내막증 관련 음성 바이오마커 연구는 사실상 전무 (호르몬 변화 → 음성 영향 가능성 가설)
- **연구 기회**: PCOS·자궁내막증 환자 한국어 음성 코호트 구축 + Wav2Vec/eGeMAPS 기반 분류기 개발

---

## 13. 참고문헌 목록

> **검증 기호**: ✅ 검증됨 | ⚠️ 논문 실재하나 세부 불일치 | ❓ 미확인 | ❌ 할루시네이션 의심

1. Naranjo, L. et al. (2025). Voice biomarkers as prognostic indicators for Parkinson's disease using machine learning techniques. *Scientific Reports*. https://www.nature.com/articles/s41598-025-96950-3 ✅
2. Quan, C. et al. (2025). Pre-trained convolutional neural networks identify Parkinson's disease from spectrogram images of voice samples. *Scientific Reports*. https://www.nature.com/articles/s41598-025-92105-6 ✅
3. Favaro, A. et al. (2025). Speech-Based Parkinson's Detection Using Pre-Trained Self-Supervised ASR Models and Supervised Contrastive Learning. *Bioengineering*. https://www.mdpi.com/2306-5354/12/7/728 ⚠️ (제1저자 오기: 실제 저자 Sedigh Malekroodi, H. et al.)
4. Karaman, O. et al. (2022). Machine Learning Smart System for Parkinson Disease Classification Using the Voice as a Biomarker. *Healthcare Informatics Research*. https://pmc.ncbi.nlm.nih.gov/articles/PMC9388925/ ✅
5. 김지환·이종민 외 (2022). 파킨슨병 환자에 대한 효과적인 음성인식 시스템. *한국음향학회지* 41(6). https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002901862 ✅
6. (2016). 음성 특징에 따른 파킨슨병 분류를 위한 알고리즘 성능 비교. *한국멀티미디어학회논문지*. https://koreascience.kr/article/JAKO201615453186206.page?lang=ko ✅
7. Luz, S. et al. (2020). Alzheimer's Dementia Recognition through Spontaneous Speech: The ADReSS Challenge. *INTERSPEECH 2020*. https://arxiv.org/abs/2004.06833 ✅
8. Pappagari, R. et al. (2021). Acoustic and Language Based Deep Learning Approaches for Alzheimer's Dementia Detection From Spontaneous Speech. *Frontiers in Aging Neuroscience*. https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2021.623607/full ⚠️ (제1저자 오기: 실제 저자 Mahajan, P. & Baths, V.)
9. (2026). Layer-wise analysis of Wav2Vec for early detection of cognitive decline. *International Journal of Speech Technology*. https://link.springer.com/article/10.1007/s10772-026-10253-0 ✅
10. 서울대학교 (2024). 알츠하이머형 치매 선별을 위한 딥러닝기반 한국 노인음성의 비언어학적 모델 연구. *SNU Open Repository*. https://s-space.snu.ac.kr/handle/10371/210811 ✅
11. Ortiz-Perez, D. et al. (2024). Multimodal deep learning for dementia classification using text and audio. *Scientific Reports*. https://www.nature.com/articles/s41598-024-64438-1 ⚠️ (제1저자 오기: 실제 저자 Lin, K. & Washington, P.Y.)
12. Stegmann, G. et al. (2025). Clinical assessment and interpretation of dysarthria in ALS using attention based deep learning AI models. *npj Digital Medicine*. https://www.nature.com/articles/s41746-025-01654-7 ⚠️ (제1저자 오기: 실제 제1저자 Merler, M. & Agurto, C.)
13. Tu, M. et al. (2023). Dysarthria detection based on a deep learning model with a clinically-interpretable layer. *JASA Express Letters*. https://pubs.aip.org/asa/jel/article/3/1/015201/2876594/ ✅
14. Velasco García, M.J. et al. (2010). Acoustic analysis of voice in Huntington's disease patients. *Journal of Voice*. https://pubmed.ncbi.nlm.nih.gov/20137889/ ⚠️ (연도 오기: epub 2010, 인쇄판 2011 Mar; J Voice 25(2):208-17)
15. Rusz, J. et al. (2020). Characterizing vocal tremor in progressive neurological diseases via automated acoustic analyses. *Clinical Neurophysiology*. https://pubmed.ncbi.nlm.nih.gov/32146096/ ✅
16. Yang, X. et al. (2024). Depression recognition using voice-based pre-training model. *Scientific Reports*. https://www.nature.com/articles/s41598-024-63556-0 ⚠️ (제1저자 오기: 실제 저자 Huang, X. et al.)
17. Bao, R. et al. (2024). Diagnostic accuracy of deep learning using speech samples in depression: a systematic review and meta-analysis. *JAMIA*. https://academic.oup.com/jamia/article/31/10/2394/7715014 ⚠️ (제1저자 오기: 실제 저자 Liu, M. et al.)
18. Lam, G. et al. (2023). Automatic Depression Detection Using Smartphone-Based Text-Dependent Speech Signals: Deep CNN Approach. *JMIR*. https://www.jmir.org/2023/1/e34474 ⚠️ (제1저자 오기: 실제 저자 Kim, A.Y. et al.)
19. 서울대학교 (2022). 음성과 텍스트를 이용하여 우울증 및 자살 위험을 평가하는 인공지능 기반 임상의사결정지원시스템에 관한 연구. *SNU Open Repository*. https://s-space.snu.ac.kr/handle/10371/183406 ✅
20. (2025). Voice of Mind: Deep Learning Model for Depression and Anxiety Assessment From Acoustic and Lexical Vocal Biomarkers. *Journal of Voice*. https://pubmed.ncbi.nlm.nih.gov/40998607/ ✅
21. Faurholt-Jepsen, M. et al. (2016). Voice analysis as an objective state marker in bipolar disorder. *Translational Psychiatry*. https://www.nature.com/articles/tp2016123 ✅
22. de Boer, J.N. et al. (2021). Acoustic speech markers for schizophrenia-spectrum disorders. *Psychological Medicine*. https://www.cambridge.org/core/journals/psychological-medicine/article/CD60278BD0F09390E8987CB5AB8A887F ⚠️ (연도 오기: epub 2021, 인쇄판 2023 Psychol Med 53(4):1302-1312; 피험자 수 86+80 → 142+142)
23. (2025). Identifying diagnostic status and negative symptoms of psychosis using CNNs. PMC12237691. https://pmc.ncbi.nlm.nih.gov/articles/PMC12237691/ ⚠️ (저널명 오기: "Schizophrenia Research" → 실제 NPP—Digital Psychiatry and Neuroscience)
24. (2024). Identification of psychological stress from speech signal using deep learning. *Healthcare Analytics*. https://www.sciencedirect.com/science/article/pii/S2772671124002870 ✅
25. Sharma, N. et al. (2021). Coswara — A Database of Breathing, Cough, and Voice Sounds for COVID-19 Diagnosis. *INTERSPEECH 2020*. https://www.researchgate.net/publication/354140526 ⚠️ (연도 오기: 2021 → 실제 2020; INTERSPEECH 2020 proceedings 출판)
26. Orlandic, L. et al. (2021). The COUGHVID crowdsourcing dataset for COVID-19 cough sound research. *Scientific Data / arXiv*. https://arxiv.org/pdf/2009.11644 ✅
27. Hamdi, S. et al. (2023). CovidCoughNet: CNN with pitch-shifting data augmentation for COVID-19 detection from cough/breath/voice. *PMC10249348*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10249348/ ✅
28. 한밭대학교 (2022). 기침소리를 이용한 코로나19 감염 진단 모델 개발. *DBpia T16613002*. https://www.dbpia.co.kr/journal/detail?nodeId=T16613002 ✅
29. (2022). EfficientNet 기반 기침 소리 감지 시스템. *earticle A409384*. https://www.earticle.net/Article/A409384 ✅
30. Kim, Y. et al. (2021). Respiratory sound classification for crackles, wheezes, and rhonchi in the clinical field using deep learning. *Scientific Reports*. https://www.nature.com/articles/s41598-021-96724-7 ✅
31. (2025). Pediatric Asthma Detection with Google's HeAR Model. *arXiv 2504.20124*. https://arxiv.org/html/2504.20124v1 ✅
32. Wang, R. et al. (2022). Obstructive Sleep Apnea Detection Based on Sleep Sounds via Deep Learning. *Nature and Science of Sleep*. https://www.tandfonline.com/doi/full/10.2147/NSS.S373367 ✅
33. Aydin, K. et al. (2024). Voice analysis in women with polycystic ovary syndrome. *Egyptian Journal of Otolaryngology*. https://link.springer.com/article/10.1186/s43163-024-00659-5 ✅
34. Aydin, K. et al. (2010). Vocal Changes in Patients With Polycystic Ovary Syndrome. *Journal of Voice*. https://pubmed.ncbi.nlm.nih.gov/20537860/ ✅
35. (2022). Voice changes in reproductive disorders, thyroid disorders and diabetes: a review. *Endocrine Connections*. https://pmc.ncbi.nlm.nih.gov/articles/PMC8942322/ ✅
36. Kaufman, J.M. et al. (2023). Acoustic Analysis and Prediction of Type 2 Diabetes Mellitus Using Smartphone-Recorded Voice Segments. *Mayo Clinic Proceedings: Digital Health*. https://pmc.ncbi.nlm.nih.gov/articles/PMC11975753/ ⚠️ (성능 수치 과장: 실제 여성 Acc=75%, 남성 Acc=70%; 보고서 89%/86%는 오기)
37. Multiple authors (2018-2021). Voice Pathology Detection on the Saarbrücken Voice Database (SVD) — survey of methods. https://link.springer.com/chapter/10.1007/978-3-642-35292-8_11 ; https://www.mdpi.com/2076-3417/11/15/7149 ✅
38. (2024). A Classification Benchmark for AI Detection of Laryngeal Cancer from Patient Voice. *arXiv 2412.16267*. https://arxiv.org/abs/2412.16267 ✅
39. Kim, H. et al. (2020). CNN Classifies Pathological Voice Change in Laryngeal Cancer with High Accuracy. *Journal of Clinical Medicine*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7692693/ ✅
40. (2024). Classification of laryngeal diseases by AI using voice analysis. *Scientific Reports*. https://www.nature.com/articles/s41598-024-58817-x ✅
41. Maor, E. et al. (2020). Vocal Biomarker Is Associated With Hospitalization and Mortality Among Heart Failure Patients. *J Am Heart Assoc*. https://www.ahajournals.org/doi/10.1161/JAHA.119.013359 ✅
42. (2023). Infant Cry Signal Diagnostic System Using Deep Learning and Fused Features. *Diagnostics*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10297367/ ✅
43. KISTI (2021). AcoustoSleepMask: 수면질환 환자의 수면 중 신호 빅데이터 분석 보고서. TRKO202100015466. https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202100015466 ✅

### 추가 참조 (방법론·데이터셋)
- Eyben, F. et al. (2016). The Geneva Minimalistic Acoustic Parameter Set (GeMAPS/eGeMAPS). *IEEE Transactions on Affective Computing*.
- Bot, B.M. et al. (2016). The mPower study, Parkinson disease mobile data collected using ResearchKit. *Scientific Data*. https://www.nature.com/articles/sdata201611
- AIHub Korea. 구음장애 음성인식 데이터. https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=608
- Praat Voice Analysis: https://www.fon.hum.uva.nl/praat/
- openSMILE: https://github.com/audeering/opensmile
- Wav2Vec 2.0: Baevski et al. (2020), Facebook AI

---

**보고서 작성 완료**: 2026-04-29
**총 논문 수**: 43개 항목 (한국어 7편: #5, #6, #10, #19, #28, #29, #43)
**도메인 커버리지**: 신경계(파킨슨·알츠하이머·헌팅턴·ALS·구음장애), 정신건강(우울증·불안·양극성·조현병), 호흡기(COVID-19·천식·COPD·OSA), 호르몬·내분비(PCOS·갑상선·당뇨), 음성질환(후두암·성대마비·음성장애), 심혈관(심부전), 신생아 울음
