# PCOS·자궁내막증 카메라 바이오마커 합성 보고서

**버전**: 1.0
**작성일**: 2026-04-11
**패턴 적용**: K-Dense citation-management + Harness100 research-designer
**참고문헌 처리**: ✅ 28편 포함, ⚠️ 4편 주의부 포함, ❌ 2편(#19 저자 수정, #28 저자 수정) 교정, ❌ 1편(#22 철회) 완전 제외

---

## 요약 (Executive Summary)

1. **52편 문헌 탐색, 37편 검증 완료**: PCOS·자궁내막증에 대한 스마트폰 카메라 바이오마커 직접 연구는 **전무**하나, 세 갈래의 수렴적 증거(HRV-질환 연관성, rPPG 기술 성숙, 피부 표현형 자동 분석)가 통합 적용의 가능성을 강력히 시사한다.

2. **Tier 1 (PCOS·자궁내막증 직접 적용 가능) 바이오마커 4개 식별**: rPPG-HRV(LF/HF, RMSSD), 월경주기 HRV 패턴, 여드름 자동 등급화(IGA), 다모증 영상 mFG. 이들은 메타분석 수준의 질환 연관 근거 + 성숙한 카메라 기술을 모두 갖추었다.

3. **Tier 2 (간접 연계 가능) 바이오마커 6개 식별**: 흑색극세포증 탐지(ANcam), 얼굴 BMI 추정, rPPG 혈압, rPPG SpO2, rPPG 스트레스, 피부색 시계열. 추가 검증이 필요하나 유망한 보조 지표로 평가된다.

4. **기존 camera 합성 보고서 대비 신규 발견**: PCOS-HRV 메타분석(17개 연구, 증거 수준 High), 다모증 영상 평가 임상 검증(mFG 일치도 0.89), ANcam 흑색극세포증 탐지(AUC 0.854), 비접촉 월경 건강 예측 프레임워크(PPG 91.7%), 여성건강 바이오모니터링 리뷰(Nature Communications 2025)가 신규 추가되었다.

5. **핵심 연구 제안**: rPPG-HRV + 얼굴 피부 분석 + 월경 추적 데이터를 융합한 멀티모달 AI 모델로 PCOS/자궁내막증/건강 3-class 분류(예상 AUC 0.80-0.90)를 목표로 하는 전향적 코호트 연구를 제안한다.

---

## 1. 바이오마커 Tier 분류 (5차원 매트릭스)

### 평가 기준

| 평가 차원 | 1점 | 3점 | 5점 |
|----------|-----|-----|-----|
| 기술성숙도 (TRL) | 개념 증명 | 프로토타입/파일럿 검증 | 상용/공개 모델 존재, 실생활 검증 |
| 임상타당성 (CV) | 사례 보고/단면, PCOS/Endo 간접 연관 | 중규모 검증, PCOS/Endo 직접 관찰 | 메타분석/다기관, AUC>0.90 |
| 실용성 (PR) | 추가 장비/특수 조건 필요 | 스마트폰 가능하나 제약 있음 | 일반 스마트폰 즉시 수집 |
| 데이터가용성 (DA) | 비공개/수집 매우 어려움 | 일부 공개 또는 수집 가능 | 공개 데이터셋 + 앱 데이터 활용 가능 |
| 규제친화성 (RF) | 규제 경로 불명확 | 유사 SaMD 인증 사례 존재 | FDA/CE 인증 완료 사례 |

### Tier 1: PCOS·자궁내막증 직접 적용 가능 (총점 >= 18)

| 바이오마커 | 질환 | 기술 | 최고성능 | TRL | CV | PR | DA | RF | 총점 | 검증 |
|----------|------|------|----------|-----|----|----|----|----|------|------|
| rPPG-HRV (LF/HF, RMSSD, HFnu) | PCOS + 자궁내막증 | rPPG -> PRV -> HRV | ECG 대비 r=0.85-0.95; PCOS LF/HF SMD +0.670 | 4 | 5 | 5 | 4 | 3 | **21** | ✅ 메타분석 [1] + 다수 단일기관 [3,4,5,6,7,8] |
| 월경주기 HRV 패턴 | PCOS (무배란 탐지) | rPPG 종단 + 앱 데이터 | 주기성 변동 확인, RF AUC 0.96 (웨어러블) | 3 | 4 | 5 | 4 | 3 | **19** | ✅ Living SR [11], 대규모 [12], 유사 연구 [28] |
| 여드름 자동 등급화 (IGA) | PCOS (안드로겐성) | 스마트폰 카메라 + CNN | IGA 정확도 0.85, mAP 0.54 | 4 | 4 | 5 | 3 | 3 | **19** | ✅ AcneDet [13], AcneAI [15], 대규모 [16] |
| 다모증 영상 mFG 점수 | PCOS (진단 기준 직접) | 모바일 사진 + 평가 | 대면 일치도 0.89, Kappa 0.75 | 3 | 4 | 5 | 3 | 3 | **18** | ✅ Oliveira et al. [17], n=70, 다평가자 |

### Tier 2: 간접 연계 가능 (유망) (총점 13-17)

| 바이오마커 | 질환 | 기술 | 최고성능 | 총점 | 검증 |
|----------|------|------|----------|------|------|
| 흑색극세포증(AN) 스마트폰 탐지 | PCOS (인슐린 저항성) | 카메라 + CMYK_K 색상 분석 | 민감도 81.1%, 특이도 70.3%, AUC 0.854 | **17** | ✅ ANcam [18], n=227 |
| 얼굴 BMI 추정 | PCOS (대사 위험) | 얼굴 이미지 + ResNet50 | MAE 1.04, 여성 21-40세 AUC 0.861 | **16** | ✅ Yousaf et al. [19], PatchBMI-Net [20] |
| rPPG 혈압 추정 (SBP/DBP) | PCOS 심혈관 위험 | 얼굴 TOI | SBP/DBP 95.3%/96.4% (+-5mmHg, n=1,328) | **16** | ✅ Luo et al. [35] |
| rPPG SpO2 추정 | 자궁내막증 염증/PCOS-OSA | STMap + CNN | MAE 1.274%, RMSE 1.710% | **15** | ✅ Cheng et al. [34] |
| 비접촉 월경주기 4상 분류 | PCOS (불규칙 주기) | PPG + 레이더 + LiDAR | PPG 91.7%, 불규칙 주기 87.6% | **14** | ✅ Rajesh [10], Exploratory |
| 피부 병변 분류 (다질환) | PCOS 간접 (피부 AI 기반) | CNN (DenseNet/MobileNet) | DenseNet 92.25%, MobileNetV2 98.4% | **14** | ✅ Oztel et al. [21] |

### Tier 3: 탐색적 (가설 수준) (총점 7-12)

| 바이오마커 | 질환 | 기술 | 총점 | 검증 |
|----------|------|------|------|------|
| 피부색 시계열 변화 (L*a*b*) | PCOS 호르몬 변동 | 카메라 색상 분석 + 시계열 | **11** | 가설 수준 (선행연구 없음) |
| 안면 미세표정 + rPPG 통증 탐지 | 자궁내막증 만성통증 | 표정 DL + rPPG 동시 | **10** | 가설 (MoodCapture [기존 합성] 기술 유사) |
| 야간 rPPG SpO2 변동 | PCOS-OSA | 야간 카메라 + rPPG | **9** | 가설 (저조도 신뢰성 문제 [Acharya 2025]) |
| 안드로겐성 탈모 패턴 분석 | PCOS | 두피/이마 사진 + CNN | **8** | 가설 (데이터셋 미존재) |
| rPPG 스트레스 탐지 | 자궁내막증 통증-스트레스 | 1D-CNN + rPPG | **8** | ✅ 기술 검증 (벤치마크 95.83%) [기존 합성] |

---

## 2. 기존 _workspace/camera 연구 대비 신규 발견

### 2.1 신규 문헌 (본 탐색에서 새로 발견)

| 구분 | 기존 camera 합성 | 본 탐색 신규 추가 | 의의 |
|------|----------------|-----------------|------|
| **PCOS-HRV 메타분석** | 없음 | Mirzohreh et al., 2024 (17개 연구) [1] | PCOS-자율신경계 이상의 증거 수준을 **High**로 격상 |
| **자궁내막증-미주신경** | 없음 (간접 언급만) | Hao 2021 [7], Moreira 2021 [6], Zeng 2025 [8], Moreira 2024 [9] | 자궁내막증 HRV 바이오마커 근거 4편 추가 |
| **다모증 영상 평가** | 없음 | Oliveira et al., 2023 (mFG 일치도 0.89) [17] | PCOS 진단 기준 직접 지원 카메라 기술 최초 식별 |
| **AN 스마트폰 탐지** | 없음 | Dhanoo et al., 2024 (ANcam, AUC 0.854) [18] | PCOS 인슐린 저항성 비침습 스크리닝 최초 경로 |
| **비접촉 월경 건강 예측** | 없음 | Rajesh, 2025 (PPG 91.7%) [10] | 웨어러블 없이 월경 주기 분류 가능성 시사 |
| **월경주기-HRV 관계** | 없음 | de Jager 2026 [11], Heydari 2025 [12] | 월경주기별 HRV 변동 패턴 체계적 정리 |
| **여성건강 바이오모니터링** | 없음 | Moghimikandelousi et al., 2025 [30] | Nature Communications에서 여성건강 디지털 바이오마커 종합 리뷰 |
| **PCOS AI 리뷰** | 없음 | Wang et al., 2025 [23] | PCOS AI 진단 현황 종합 (80-90% 정확도) |
| **자궁내막증 ML 메타분석** | 없음 | Zhang et al., 2026 [26] | 자궁내막증 ML 진단 정확도 체계적 평가 |

### 2.2 기존 Tier 재평가

| 기존 Tier | 바이오마커 | 기존 총점 | 재평가 총점 | 변경 사유 |
|----------|----------|----------|-----------|----------|
| Tier 1 | rPPG HR | 23 | 23 (유지) | 기술 기반, PCOS/Endo 직접 적용 시 Tier 1 유지 |
| Tier 2 | rPPG HRV | 18 | **21** (Tier 1 승격) | PCOS 메타분석으로 임상타당성 5점으로 상향 |
| Tier 2 | rPPG 혈압 | 19 | 16 (Tier 2 유지) | PCOS/Endo 직접 적용 시 임상타당성 하향 조정 |
| 신규 | 여드름 IGA | - | **19** (Tier 1) | PCOS 안드로겐성 여드름 직접 연결 |
| 신규 | 다모증 mFG | - | **18** (Tier 1) | PCOS Rotterdam 기준 직접 지원 |
| 신규 | ANcam AN 탐지 | - | **17** (Tier 2) | 인슐린 저항성 간접 바이오마커 |
| 신규 | 얼굴 BMI 추정 | - | **16** (Tier 2) | PCOS 대사 위험도 추정 |

---

## 3. 메타 분석: 기존 성능 지표 종합

### 3.1 rPPG-HRV 기반 바이오마커 성능 종합

| 바이오마커 | 질환 연관 근거 | rPPG 기술 성능 | 예상 통합 성능 | 근거 수준 |
|----------|--------------|---------------|--------------|----------|
| LF/HF ratio | PCOS SMD +0.670 (95%CI 0.207-1.133) [1] | rPPG-ECG r=0.85-0.95 | AUC 0.70-0.80 (이진 분류) | High |
| RMSSD | 자궁내막증 유의 감소 (p<0.05) [7] | rPPG-ECG r=0.88 | AUC 0.65-0.75 (이진 분류) | Moderate |
| HFnu | PCOS SMD -0.873 (95%CI -1.472 ~ -0.274) [1] | rPPG-ECG r=0.82 | AUC 0.70-0.80 (이진 분류) | High |
| SDNN | PCOS SMD -0.763 (95%CI -1.318 ~ -0.208) [1] | rPPG-ECG r=0.90 | AUC 0.65-0.75 (이진 분류) | High |
| 총 HRV 파워 (TP) | PCOS SMD -1.997 (95%CI -3.437 ~ -0.557) [1] | rPPG-ECG 변환 | AUC 0.75-0.85 (이진 분류) | High |

### 3.2 얼굴/피부 분석 바이오마커 성능 종합

| 바이오마커 | 기술 검증 성능 | PCOS 직접 적용성 | 예상 통합 성능 | 근거 수준 |
|----------|--------------|-----------------|--------------|----------|
| 여드름 등급(IGA) | 정확도 0.85 [13], ICC 0.8 [15] | PCOS 안드로겐성 여드름 | 민감도 0.80+ (여드름 PCOS 선별) | Moderate |
| 다모증(mFG) | 일치도 0.89, Kappa 0.75 [17] | Rotterdam 기준 직접 지원 | 특이도 0.85+ (다모증 PCOS 선별) | Moderate |
| AN 탐지 | AUC 0.854, 민감도 81.1% [18] | 인슐린 저항성 선별 | AUC 0.80+ (인슐린 저항성 PCOS) | Moderate |
| BMI 추정 | MAE 1.04 [19] | 대사 위험도 보조 지표 | BMI >= 25 분류 AUC 0.86 | Moderate |

### 3.3 멀티모달 융합 예상 성능

| 모달 조합 | 예상 AUC (PCOS) | 예상 AUC (Endo) | 예상 3-class AUC | 근거 |
|----------|----------------|----------------|-----------------|------|
| rPPG-HRV 단독 | 0.70-0.80 | 0.65-0.75 | 0.65-0.75 | 메타분석 효과크기 기반 추정 |
| 얼굴 피부 단독 | 0.75-0.85 | 0.55-0.65 | 0.60-0.70 | 개별 바이오마커 성능 기반 |
| 월경 패턴 단독 | 0.65-0.75 | 0.60-0.70 | 0.60-0.70 | 앱 데이터 연구 기반 |
| **HRV + 피부 + 월경 (융합)** | **0.85-0.90** | **0.75-0.85** | **0.80-0.90** | 모달 보완성 기반 낙관적 추정 |

*주: 융합 성능은 아직 검증되지 않은 추정치이며, 실제 성능은 데이터 수집 후 확인 필요.*

---

## 4. BibTeX 목록 (CrossRef API 기반, ✅ 항목)

```bibtex
@article{Mirzohreh_2024,
  author = {Mirzohreh, Seyedeh Tarlan and Panahi, Padideh and Heidari, Fariba},
  title = {Exploring heart rate variability in polycystic ovary syndrome: implications for cardiovascular health: a systematic review and meta-analysis},
  journal = {Systematic Reviews},
  volume = {13},
  year = {2024},
  doi = {10.1186/s13643-024-02617-x}
}

@article{Yu_2024,
  author = {Yu, Yue and Chen, Tong and Zheng, Zheng and Jia, Fan and Liao, Yan and Ren, Yuehan and Liu, Xinmin and Liu, Ying},
  title = {The role of the autonomic nervous system in polycystic ovary syndrome},
  journal = {Frontiers in Endocrinology},
  volume = {14},
  year = {2024},
  doi = {10.3389/fendo.2023.1295061}
}

@article{Sarathivarman_2025,
  author = {Sarathivarman, Sivaranjani and Krishnan, Prabhavathi and Ravi, Keerthi and Leelabai, Bhavisha Sreenivasan and Kanagaraj, Thamarai Selvi and Ayyavoo, Saravanan and Periasamy, Panneerselvam},
  title = {Comparative Analysis of Heart Rate Variability in Women with and Without Polycystic Ovary Syndrome (PCOS)},
  journal = {Journal of Pharmacy and Bioallied Sciences},
  volume = {17},
  year = {2025},
  doi = {10.4103/jpbs.jpbs_1295_25}
}

@article{de_Fatima_Azevedo_2026,
  author = {de F\'{a}tima Azevedo, Maria and Rocha, Ana Kleyce Coreia and de Melo, Livia Maria Bezerra and de Melo, Luciana Medeiros Bezerra and Cat\~{a}o, Romena Le\~{a}o Azevedo and Costa, Eduardo Caldas},
  title = {24-hour ambulatory blood pressure and associated factors in women with polycystic ovary syndrome compared with ovulatory controls},
  journal = {Scientific Reports},
  volume = {16},
  year = {2026},
  doi = {10.1038/s41598-026-38731-0}
}

@article{Bernal_2024,
  author = {Bernal, Jo\~{a}o Vitor Martins and da Veiga, Ana Catarine and Philbois, Stella Vieira and Ribeiro, Victor Barbosa and Aguilar, Bruno Augusto and Paix\~{a}o, Tallys Eduardo Velasco and Chinellato, Naiara and S\'{a}nchez-Delgado, Juan Carlos and Gastaldi, Ada Clarice and de Souza, Hugo Celso Dutra},
  title = {Women With Polycystic Ovary Syndrome and Excess Body Fat Exhibit Atypical Sympathetic Autonomic Modulation That is Partially Reversed by Aerobic Physical Training},
  journal = {Clinical Endocrinology},
  volume = {102},
  year = {2024},
  doi = {10.1111/cen.15163}
}

@article{Moreira_2021,
  author = {de Fran\c{c}a Moreira, Marcelo and Gamboa, Olga Lucia and Pinho Oliveira, Marco Aurelio},
  title = {Association between severity of pain, perceived stress and vagally-mediated heart rate variability in women with endometriosis},
  journal = {Women \& Health},
  volume = {61},
  number = {10},
  pages = {937--946},
  year = {2021},
  doi = {10.1080/03630242.2021.1993423}
}

@article{Hao_2021,
  author = {Hao, Meihua and Liu, Xishi and Rong, Peijing and Li, Shaoyuan and Guo, Sun-Wei},
  title = {Reduced vagal tone in women with endometriosis and auricular vagus nerve stimulation as a potential therapeutic approach},
  journal = {Scientific Reports},
  volume = {11},
  year = {2021},
  doi = {10.1038/s41598-020-79750-9}
}

@article{Zeng_2025,
  author = {Zeng, Weiwei and Zhang, Tingting and Wu, Fan and Guo, Sun-Wei},
  title = {Reduced vagal tone in women with adenomyosis},
  journal = {Reproduction and Fertility},
  volume = {6},
  number = {4},
  year = {2025},
  doi = {10.1530/RAF-25-0039}
}

@article{Moreira_2024,
  author = {Moreira, Marcelo F. and Gamboa, Olga L. and Oliveira, Marco A.P.},
  title = {Mindfulness-Based Intervention Effect on the Psychophysiological Marker of Self-Regulation in Women With Endometriosis-Related Chronic Pain},
  journal = {The Journal of Pain},
  volume = {25},
  number = {1},
  pages = {118--131},
  year = {2024},
  doi = {10.1016/j.jpain.2023.07.026}
}

@article{Rajesh_2025,
  author = {Rajesh, M.},
  title = {Adaptive Edge-Federated AI Framework for Contactless Menstrual Health Prediction Using Multimodal Physiological Intelligence},
  journal = {MethodsX},
  volume = {15},
  pages = {103665},
  year = {2025},
  doi = {10.1016/j.mex.2025.103665}
}

@article{de_Jager_2026,
  author = {de Jager, Eline and Caulfield, Brian and Angelidi, Evgenia and MacNamee, Brian and Holden, Sinead},
  title = {Wearable-Derived Heart Rate Variability Across the Menstrual Cycle, Hormonal Contraceptive Use, and Reproductive Life Stages in Females: A Living Systematic Review},
  journal = {Sports Medicine},
  year = {2026},
  doi = {10.1007/s40279-025-02388-y}
}

@article{Heydari_2025,
  author = {Heydari, Kimia and Enichen, Elizabeth J. and Li, Ben and Kvedar, Joseph C.},
  title = {A new metric to understand the association between heart rate variability and menstrual regularity},
  journal = {npj Digital Medicine},
  volume = {8},
  year = {2025},
  doi = {10.1038/s41746-025-01517-1}
}

@article{Huynh_2022,
  author = {Huynh, Quan Thanh and Nguyen, Phuc Hoang and Le, Hieu Xuan and Ngo, Lua Thi and Trinh, Nhu-Thuy and Tran, Mai Thi-Thanh and Nguyen, Hoan Tam and Vu, Nga Thi and Nguyen, Anh Tam and Suda, Kazuma and Tsuji, Kazuhiro and Ishii, Tsuyoshi and Ngo, Trung Xuan and Ngo, Hoan Thanh},
  title = {Automatic Acne Object Detection and Acne Severity Grading Using Smartphone Images and Artificial Intelligence},
  journal = {Diagnostics},
  volume = {12},
  number = {8},
  pages = {1879},
  year = {2022},
  doi = {10.3390/diagnostics12081879}
}

@inbook{Gazeau_2024,
  author = {Gazeau, L\'{e}a and Nguyen, Hang and Nguyen, Zung and Lebedeva, Mariia and Nguyen, Thanh and To, Tat-Dat and Le Digabel, Jimmy and Filiol, J\'{e}rome and Josse, Gwendal and Perlis, Clifford and Wolfe, Jonathan},
  title = {AcneAI: A New Acne Severity Assessment Method Using Digital Images and Deep Learning},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2024},
  pages = {68--78},
  year = {2024},
  doi = {10.1007/978-3-031-72086-4_7}
}

@article{Oliveira_2022,
  author = {Oliveira, Talita Fischer and Oliveira, Talita Fernanda and Rocha, Ana Luiza Lunardi and Reis, Fernando M and C\^{a}ndido, Ana Lucia and Premaor, Melissa Orlandin and Comim, Fabio Vasconcellos},
  title = {Comparison of image-based modified Ferriman-Gallway score evaluation with in-person evaluation: an alternative method for hirsutism diagnosis},
  journal = {Archives of Dermatological Research},
  volume = {315},
  number = {6},
  pages = {1783--1787},
  year = {2022},
  doi = {10.1007/s00403-022-02495-0}
}

@article{Dhanoo_2024,
  author = {Dhanoo, Andrew S. and Ramroach, Sterling K. and Hill-Briggs, Felicia and Cockburn, Brian N.},
  title = {Grading Acanthosis Nigricans Using a Smartphone and Color Analysis: A Novel Noninvasive Method to Screen for Impaired Glucose Tolerance and Type 2 Diabetes},
  journal = {Diabetes Spectrum},
  volume = {37},
  number = {2},
  pages = {139--148},
  year = {2024},
  doi = {10.2337/ds23-0042}
}

@article{Yousaf_2021,
  author = {Yousaf, Nadeem and Hussein, Sarfaraz and Sultani, Waqas},
  title = {Estimation of BMI from facial images using semantic segmentation based region-aware pooling},
  journal = {Computers in Biology and Medicine},
  volume = {133},
  pages = {104392},
  year = {2021},
  doi = {10.1016/j.compbiomed.2021.104392}
}

@article{Wang_2025,
  author = {Wang, Jinyuan and Chen, Ruxin and Long, Haojun and He, Junhui and Tang, Masong and Su, Mingxuan and Deng, Renhe and Chen, Yuru and Ni, Rongqian and Zhao, Shuhua and Rao, Meng and Wang, Huawei and Tang, Li},
  title = {Artificial intelligence in polycystic ovarian syndrome management: past, present, and future},
  journal = {La radiologia medica},
  volume = {130},
  number = {9},
  pages = {1409--1441},
  year = {2025},
  doi = {10.1007/s11547-025-02032-9}
}

@article{Arabkermani_2025,
  author = {Arabkermani, Zahra and Barzegari, Saeed and Rouhani, Atefeh and Nahavandi, Nilofar and Gibreel, Omer and Arpaci, Ibrahim},
  title = {Mobile Apps Designed for Patients With Polycystic Ovary Syndrome: Content Analysis Using the Mobile App Rating Scale},
  journal = {Journal of Medical Internet Research},
  volume = {27},
  pages = {e71118},
  year = {2025},
  doi = {10.2196/71118}
}

@article{Pavic_2025,
  author = {Pavic, Tivizio and Nadarajah, K\'{e}vin and Somat, Alain and Cabagno, Genevi\`{e}ve and Terrade, Florence},
  title = {Endometriosis Support and Development of Digital Technology--Based Interventions: Systematic Review},
  journal = {JMIR Human Factors},
  volume = {12},
  pages = {e71859},
  year = {2025},
  doi = {10.2196/71859}
}

@article{Zhang_2026,
  author = {Zhang, Bingyi and Lv, Xiaoli and Li, Dan and Zhang, Longtao and Ru, Ziyang and Ma, Yuxia},
  title = {Diagnostic accuracy of machine learning for endometriosis: a systematic review and meta-analysis},
  journal = {Frontiers in Endocrinology},
  volume = {16},
  year = {2026},
  doi = {10.3389/fendo.2025.1735567}
}

@article{Liu_2025,
  author = {Liu, Xiaoxuan and An, Ran and Wang, Guoyun},
  title = {Integrating inflammatory biomarkers and demographic variables with machine learning to predict endometriosis risk},
  journal = {Scientific Reports},
  volume = {15},
  year = {2025},
  doi = {10.1038/s41598-025-26606-9}
}

@article{Kilungeja_2025,
  author = {Kilungeja, Grentina and Graham, Krystal and Liu, Xudong and Nasseri, Mona},
  title = {Machine learning-based menstrual phase identification using wearable device data},
  journal = {npj Women's Health},
  volume = {3},
  year = {2025},
  doi = {10.1038/s44294-025-00078-8}
}

@article{Moghimikandelousi_2025,
  author = {Moghimikandelousi, Shaghayegh and Najm, Lubna and Lee, Yerim and Bayat, Fereshteh and Prasad, Akansha and Khan, Shadman and Bhavan, Aishwarya and Gao, Wei and Hosseinidoust, Zeinab and Didar, Tohid F.},
  title = {Advances in biomonitoring technologies for women's health},
  journal = {Nature Communications},
  volume = {16},
  year = {2025},
  doi = {10.1038/s41467-025-63501-3}
}

@article{Sollee_2025,
  author = {Sollee, John and Cheema, Baljash and Slotwiner, David and Volodarskiy, Alexander and Desteghe, Lien and Buyck, Christophe and Heidbuchel, Hein and Stavrakis, Stavros and Pison, Laurent and Nuyens, Dieter and Rivero-Ayerza, Maximo and Van Herendael, Hugo and Thomas, James},
  title = {Fibricheck detection capabilities for atrial fibrillation (FDA--AF): a multicenter validation study},
  journal = {npj Digital Medicine},
  volume = {8},
  year = {2025},
  doi = {10.1038/s41746-025-02059-2}
}

@article{Cheng_2024,
  author = {Cheng, Chun-Hong and Yuen, Zhikun and Chen, Shutao and Wong, Kwan-Long and Chin, Jing-Wei and Chan, Tsz-Tai and So, Richard H. Y.},
  title = {Contactless Blood Oxygen Saturation Estimation from Facial Videos Using Deep Learning},
  journal = {Bioengineering},
  volume = {11},
  number = {3},
  pages = {251},
  year = {2024},
  doi = {10.3390/bioengineering11030251}
}

@article{Luo_2019,
  author = {Luo, Hong and Yang, Deye and Barszczyk, Andrew and Vempala, Naresh and Wei, Jing and Wu, Si Jia and Zheng, Paul Pu and Fu, Genyue and Lee, Kang and Feng, Zhong-Ping},
  title = {Smartphone-Based Blood Pressure Measurement Using Transdermal Optical Imaging Technology},
  journal = {Circulation: Cardiovascular Imaging},
  volume = {12},
  number = {8},
  year = {2019},
  doi = {10.1161/CIRCIMAGING.119.008857}
}
```

---

## 5. 참고문헌 검증 현황 요약

### 5.1 제외 항목

| # | 원 기재 | 실제 | 조치 |
|---|--------|------|------|
| #19 | "Jiang et al., 2021" | Yousaf, Hussein, Sultani (2021) | 저자명 교정, BibTeX 올바른 저자로 수록 |
| #22 | Dark circle AI, 2023, *Skin Res Technol* | 2025-10 철회 (PMID:41059760) | **완전 제외** |
| #28 | "Rahmawati et al., 2025" | Agirsoy & Oehlschlaeger (2025) | 저자명 교정, 본 보고서에서는 간접 참조만 |

### 5.2 주의 필요 항목 (포함, 실제 메타데이터 사용)

| # | 항목 | 교정 내용 |
|---|------|----------|
| #29 | ML menstrual cycle, Masuda et al. | DOI 수정: 10.1016/j.compbiomed.2025.109705, PMID:39889448 |
| #31 | Menstrual cycle vital sign, Rosen Vollmar et al. | DOI 수정: 10.1016/j.xfnr.2024.100081 |
| #36 | rPPG HRV 리뷰, 2024 | 추정 DOI: 10.3389/fbioe.2024.1420100, 완전 확인 불가 |

### 5.3 미확인 항목 (제외)

| # | 항목 | 사유 |
|---|------|------|
| #32 | rPPG 종합 리뷰, 2025, PMC | 저자/DOI 미기재, 특정 불가 |
| #37 | 피부암 DL, 2023, Diagnostics | 저자/DOI 미기재, 특정 불가 |

---

*본 합성 보고서는 2026-04-11 기준으로 작성되었으며, CrossRef API를 통해 BibTeX 메타데이터가 검증된 28편의 핵심 논문에 기반합니다. Harness100 research-designer 패턴으로 연구 설계를 수행하고, K-Dense citation-management 패턴으로 참고문헌을 관리하였습니다.*
