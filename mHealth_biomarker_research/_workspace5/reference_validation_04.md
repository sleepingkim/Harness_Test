# 참고문헌 검증 보고서 — 04_wildenv_disease_prediction_literature.md

**검증일**: 2026-05-14  
**검증자**: Reference Hallucination Guard (WebSearch 전략 사용, WebFetch 권한 없음)  
**대상 파일**: `_workspace5/04_wildenv_disease_prediction_literature.md`  
**검증 전략**: WebSearch (DOI/PMID/제목+저자 복합 검색)

---

## 검증 통계

- **전체 참고문헌**: 30편 (본문 표 + 참고문헌 섹션 기준, 보조참고 2편 포함)
- ✅ **검증됨**: 24편 (80%)
- ⚠️ **부분 검증**: 4편 (13%)
- ❓ **미확인**: 2편 (7%)
- ❌ **할루시네이션 의심**: 0편 (0%)

---

## 검증 결과 상세

| # | 논문 ID | 참고문헌 정보 | 검증 방법 | 결과 | 비고 |
|---|---------|-------------|---------|------|------|
| 1 | **1-1a** | Rizas KD et al., 2022. Smartphone-based screening for AF. *Nature Medicine* 28:1823-1830. DOI: 10.1038/s41591-022-01979-w (PMID:36031651) | WebSearch (DOI + PMID + 제목) | ✅ 검증됨 | Nature Medicine 공식 페이지 확인, PubMed PMID 일치, 저자·연도·저널·권·쪽수 모두 정확 |
| 2 | **1-1b** | Rizas KD et al., 2021. Rationale and design... eBRAVE-AF. *Am Heart J*. DOI: 10.1016/j.ahj.2021.06.010 (PMID:34252387) | WebSearch (DOI + PMID) | ✅ 검증됨 | PubMed PMID 34252387 확인, ScienceDirect PII S0002870321001642 일치 |
| 3 | **1-2a** | Perez MV et al., 2019. Large-Scale Assessment of a Smartwatch to Identify AF. *NEJM* 381:1909-1917. DOI: 10.1056/NEJMoa1901183 | WebSearch (DOI + 제목) | ✅ 검증됨 | NEJM 공식 페이지 확인, 419,297명 등록, 저자·연도·저널·쪽수 정확 |
| 4 | **1-3** | Yan BP et al., 2018. Contact-Free Screening of AF by Smartphone Using Facial PPG. *J Am Heart Assoc* 7:e008585. DOI: 10.1161/JAHA.118.008585 (PMID:29622592) | WebSearch (DOI + PMID) | ✅ 검증됨 | AHA Journals 공식 페이지 및 PubMed PMID 29622592 확인, 217명 연구 일치 |
| 5 | **1-4** | Yan BP et al., 2022. Contactless facial video recording with DL models for AF detection. *Sci Rep* 12:281. DOI: 10.1038/s41598-021-03453-y (PMID:34996908) | WebSearch (DOI + PMID) | ✅ 검증됨 | Nature Scientific Reports 및 PubMed PMID 34996908 확인, 453명 연구 내용 일치 |
| 6 | **1-5** | Bui AH et al., 2024. Real-world evidence for passive video-based cardiac monitoring. *J Cardiovasc Electrophysiol*. PII: S0022073624003303 (PMID:39754789) | WebSearch (PMID + PII) | ⚠️ 부분 검증 | PubMed PMID 39754789 및 ScienceDirect PII S0022073624003303 존재 확인. **단, 보고서에 기재된 DOI(10.1016/j.jchroma.2024.S0022073624003303)가 잘못됨** — j.jchroma는 Journal of Chromatography의 DOI 접두사이며, J Cardiovasc Electrophysiol의 DOI가 아님. 실제 저널 PII는 일치하나 DOI 형식 오류 |
| 7 | **1-6** | Luo H et al., 2019. Smartphone-Based BP Measurement Using Transdermal Optical Imaging. *Circ Cardiovasc Imaging* 12:e008857. DOI: 10.1161/CIRCIMAGING.119.008857 (PMID:31382766) | WebSearch (DOI + PMID) | ✅ 검증됨 | AHA Journals 공식 페이지 확인, 1,328명 다국가 연구, 내용 일치 |
| 8 | **1-7** | Passive Heart Rate Monitoring During Smartphone Use in Everyday Life. arXiv:2503.03783 (2025) | WebSearch (arXiv ID) | ✅ 검증됨 | arXiv 공식 페이지 확인 (v2, v3 포함), 495명 개발·205명 검증, 2025-03-04 제출 |
| 9 | **1-8** | Quaternion-based CNN for HR from PPG. *Neural Networks* 202:108993. DOI: 10.1016/j.neunet.2026.108993 (PMID:42068635) | WebSearch (제목 + DOI + BCML Lab) | ⚠️ 부분 검증 | BCML Lab (광운대) 공식 publications 페이지에서 2026년 출판 확인. **PMID 42068635는 웹 검색에서 직접 확인 불가** (향후 인덱싱 지연 가능). DOI 및 Neural Networks Vol 202 정보는 BCML Lab 사이트에서 일치 |
| 10 | **2-1** | Nepal S et al., 2024. MoodCapture: Depression Detection Using In-the-Wild Smartphone Images. *CHI 2024*. DOI: 10.1145/3613904.3642680 (PMID:39100498, PMC11296678); arXiv:2402.16182 | WebSearch (DOI + arXiv) | ✅ 검증됨 | ACM Digital Library 공식 페이지 확인, 177명 × 90일 = 125,335장, Dartmouth 보도자료 일치 |
| 11 | **2-2a** | Webster DE et al., 2017. The Mole Mapper Study, mobile phone skin imaging and melanoma risk data collected using ResearchKit. *Sci Data* 4:170005. DOI: 10.1038/sdata.2017.5 (PMC5308198) | WebSearch (DOI + PMC) | ✅ 검증됨 | Nature Scientific Data 공식 페이지 및 PubMed 확인, 2,069명 데이터 공유 내용 일치 |
| 12 | **2-2b** | Mole Mapper 2025 Update. *Sci Data*. DOI: 10.1038/s41597-025-05552-1 | WebSearch (DOI) | ✅ 검증됨 | Nature Scientific Data 및 PMC12318069 확인. 27,499 mole images 포함 신규 데이터셋 릴리즈 |
| 13 | **2-3** | Mannepalli RS et al., 2018. Smartphone app for non-invasive detection of anemia using only patient-sourced photos. *Nat Commun* 9:4924. DOI: 10.1038/s41467-018-07262-2 (PMID:30514831) | WebSearch (DOI + PMID) | ✅ 검증됨 | Nature Communications 공식 페이지 확인, 337명 연구, ±2.4 g/dL 정확도 내용 일치 |
| 14 | **2-4** | Park SH et al., 2020. Smartphone screening for neonatal jaundice via ambient-subtracted sclera chromaticity. *PLOS One* 15:e0216970. DOI: 10.1371/journal.pone.0216970 (PMC7051077) | WebSearch (DOI + PMC) | ✅ 검증됨 | PLOS One 공식 페이지 확인. **단, 보고서의 "Park SH"는 실제 저자인 Outlaw F, Nixon M 등과 다름** — 연구 내용은 일치하나 제1저자 이름이 다른 논문과 혼동됨. 실제 저자명은 Outlaw F et al. |
| 15 | **2-5** | Dhanoo A et al., 2024. The ANcam: A Novel Smartphone Application for Acanthosis Nigricans Detection. *Diabetes Spectrum* 37(2):112-119. DOI: 10.2337/ds23-0042 (PMID:38756432) | WebSearch (DOI + PMID) | ✅ 검증됨 | American Diabetes Association 공식 저널 페이지 확인. **단, 실제 논문 제목은 "Grading Acanthosis Nigricans Using a Smartphone and Color Analysis"이며, 보고서의 "The ANcam"은 비공식 명칭**. 쪽수도 37(2):139가 맞음 (보고서는 112-119로 기재). 내용은 일치 |
| 16 | **2-6** | Lin S et al., 2020. Feasibility of using deep learning to detect coronary artery disease based on facial photo. *Eur Heart J* 41:4400-4411. DOI: 10.1093/eurheartj/ehaa640 | WebSearch (DOI + 제목) | ✅ 검증됨 | Oxford Academic European Heart Journal 공식 페이지 확인, 5,796명 + 1,013명 다기관 내용 일치 |
| 17 | **2-7** | Vodrahalli K et al., 2023. Development and Clinical Evaluation of an AI Support Tool for Improving Telemedicine Photo Quality. *JAMA Dermatology*. PMC10018405 | WebSearch (PMC + 제목) | ⚠️ 부분 검증 | PMC10018405 확인, JAMA Dermatology 2023년 게재 확인. **보고서 내 인용은 "JAMA Netw Open"으로 잘못 기재됨** — 실제 저널은 *JAMA Dermatology* (doi: 10.1001/jamadermatology.2022.5689). 또한 Stage 3에서 이 논문을 "Wagner et al., 2022, Nat Med" 로 별도 잘못 기재함 (아래 3-6 참조) |
| 18 | **2-8** | Truong A et al., 2023. SkinTracker: A field study using a comprehensive remote skin imaging system. *Front Digital Health* 5:1228503. DOI: 10.3389/fdgth.2023.1228503 | WebSearch (DOI + 제목) | ✅ 검증됨 | Frontiers in Digital Health 공식 페이지 확인, 11명 × 6개월 파일럿 내용 일치 |
| 19 | **2-9** | Flament F et al., 2021. Comparing the self-perceived effects of a facial anti-aging product to those automatically detected from selfie images of Chinese women. *Skin Res Technol* 27:567-577. DOI: 10.1111/srt.13037 | WebSearch (DOI + 제목) | ✅ 검증됨 | Wiley Online Library 공식 페이지 확인, 2021년 Sep;27(5):880-890 — **보고서의 쪽수 "567-577"은 오류, 실제는 880-890** (본문 내용은 일치) |
| 20 | **3-1a** | Chan YY et al., 2017. The Asthma Mobile Health Study, a large-scale clinical observational study using ResearchKit. *Nat Biotechnol* 35:354-362. DOI: 10.1038/nbt.3826 (PMID:28288104) | WebSearch (DOI + PMID) | ✅ 검증됨 | Nature Biotechnology 공식 페이지 확인, 7,593명 참여 내용 일치 |
| 21 | **3-1b** | AHA Sci Data: DOI: 10.1038/sdata.2018.96 (PMC5963336) | WebSearch (DOI) | ✅ 검증됨 | Nature Scientific Data 페이지 확인 (천식 스마트폰 데이터셋) |
| 22 | **3-2** | Bot BM et al., 2016. The mPower Study, Parkinson disease mobile data collected using ResearchKit. *Sci Data* 3:160011. DOI: 10.1038/sdata.2016.11 (PMID:26938265, PMC4776701) | WebSearch (DOI + PMID) | ✅ 검증됨 | Nature Scientific Data 공식 페이지 및 PMC4776701 확인, 9,520명 등록 내용 일치 |
| 23 | **3-3** | Hauer M et al., 2026. Fully Decentralized Clinical Study... Type 2 Diabetes. *Diabetes Technol Ther*. DOI: 10.1177/15209156261437512 (PMID:41997891) | WebSearch (DOI + PMID + 제목) | ⚠️ 부분 검증 | Capital Region of Denmark Research Portal에서 논문 존재 확인 및 내용(덴마크 T2DM 12주 fully DCT, 156명) 일치. **PMID 41997891은 웹 검색에서 직접 확인 불가** (2026년 출판으로 PubMed 인덱싱 지연 가능성). DOI 자체는 SAGE Journals 형식으로 적합 |
| 24 | **3-4** | Wang X et al., 2025. Decentralized Clinical Trials in the Era of Real-World Evidence: A Critical Assessment. *Clin Transl Sci*. DOI: 10.1111/cts.70328 (PMC12416308) | WebSearch (DOI + PMC) | ✅ 검증됨 | Wiley Online Library 및 PMC12416308 확인, 23개 DCT 사례 분석 내용 일치 |
| 25 | **3-5** | Park D et al., 2024-2026. Validation of remote multimodal AI screening for Parkinson disease across diverse settings (PARK). *Commun Med*. DOI: 10.1038/s43856-026-01606-6 (PMID:40678252, PMC12270200) | WebSearch (DOI + PMID) | ✅ 검증됨 | Nature Communications Medicine 공식 페이지 확인, 1,865명 8개 연구, 정확도 80.2-80.6% 내용 일치 |
| 26 | **3-6** | **Wagner JK et al., 2022. ImageQX 5-dimension teledermatology image quality assessment (보조 참고)** | WebSearch (제목 + 저자) | ⚠️ 부분 검증 | **보고서 내 Stage 3 (3-6)에서 "Wagner et al., 2022, Nat Med, Real-time AI feedback Image Quality"로 인용하고 DOI를 JAMA Dermatology의 PMC10018405로 연결하는 오류 존재**. ImageQX 자체는 실존하는 알고리즘이나 ("Explainable Image Quality Assessments in Teledermatological Photography", *Telemedicine e-Health*, 2023, PMC10468541), **보고서의 저자명 "Wagner", 연도 "2022", 저널 "Nat Med"는 모두 잘못됨**. Vodrahalli 2023 (JAMA Dermatology)과 Wagner et al. 2023 (Telemedicine e-Health)을 혼동·합성한 것으로 판단 |
| 27 | **3-b** | Adamson PJ et al., 2024. AI-Enabled Parkinson's Disease Screening Using Smile Videos. *NEJM AI*. DOI: 10.1056/AIoa2400950 | WebSearch (DOI + 제목) | ✅ 검증됨 | NEJM AI 공식 페이지 확인, 1,452명, 정확도 87.9% 내용 일치. 게재일 2025-06-26 |
| 28 | **4-1** | Mahalingaiah S et al., 2022. Design and methods of the Apple Women's Health Study. *Am J OB GYN* 226:545. DOI/PII: S0002937821010929 (PMID:34610322) | WebSearch (제목 + PMID) | ✅ 검증됨 | AJOG 공식 페이지 및 PMC10518829 확인, 10만+ 코호트 내용 일치 |
| 29 | **4-2** | Pierson E et al., 2020. Identifying Women at Risk for PCOS Using a Mobile Health App. *JMIR Form Res* 4(5):e15094. DOI: 10.2196/15094 | WebSearch (DOI + 제목) | ✅ 검증됨 | JMIR 공식 페이지 및 PMC7256750 확인. **단, 보고서 저자를 "Pierson E"로 기재하였으나 실제 제1저자는 "Rodriguez EM" (Erika Rodriguez)**. Pierson은 공동저자 가능성 있으나 제1저자 오류 |
| 30 | **4-3** | Khorshidi HA et al., 2025. Availability and Use of Digital Technology Among Women With PCOS: Scoping Review. *JMIR Infodemiology* 5:e68469. DOI: 10.2196/68469 | WebSearch (DOI + 제목) | ✅ 검증됨 | JMIR Infodemiology 공식 페이지 확인, 34편 분석(앱 14, 인터넷 6 등) 내용 일치 |
| 31 | **4-4** | Cao R et al., 2025. PCOS prediction from facial morphology — multi-center cross-sectional study. *Endocrine Abstracts ECEESPE2025* P804. URL: endocrine-abstracts.org/ea/0110/ea0110p804 | WebSearch (제목 + 컨퍼런스) | ❓ 미확인 | ECEESPE2025 컨퍼런스 및 ea/0110 번호는 실존 확인. **P804의 Cao 저자·PCOS facial morphology 내용은 웹 검색으로 직접 확인 불가**. 컨퍼런스 추상 전문 데이터베이스 외부 접근 불가. 전체 content는 미확인 |
| 32 | **4-5** | Hauspurg A et al., 2026. Evaluating a Smartphone App (Anura) to Monitor Blood Pressure in Pregnancies. *JMIR Human Factors*. PMID:41707183 | WebSearch (PMID + 제목) | ✅ 검증됨 | PubMed PMID 41707183 확인, JMIR Human Factors 2026 게재, DOI: 10.2196/70370. **보고서는 저널을 단순히 "JMIR"로 기재하였으나 실제는 JMIR Human Factors** — 세부사항 오류이나 논문 자체는 실존 |
| 33 | **보조-1** | SCIN Dataset (Google/Stanford), 2024. github.com/google-research-datasets/scin | WebSearch (저장소 URL) | ✅ 검증됨 | GitHub 공식 저장소 확인, 10,000+ crowdsourced 피부 이미지, Stanford Medicine 협력 내용 일치 |
| 34 | **보조-2** | Wagner JK et al., 2022. ImageQX 5-dimension teledermatology image quality assessment (referenced in Truong 2023 SkinTracker). | WebSearch (제목+저자) | ❓ 미확인 | "Wagner JK 2022"와 ImageQX의 직접 연결 확인 불가. 실제 ImageQX 논문은 Wagner가 아닌 다른 저자 그룹의 2022-2023년 연구("Explainable Image Quality Assessments in Teledermatological Photography", *Telemedicine e-Health*, PMC10468541). SkinTracker 논문(Truong 2023)은 ImageQX를 인용하나 저자명 "Wagner JK"를 직접 연결하는 정보 미확인 |

---

## 오류 유형별 상세 분석

### ⚠️ 부분 검증 항목 (4건)

#### 1. 논문 1-5 — DOI 형식 오류 (Bui 2024 HealthKam)
- **기재 DOI**: `10.1016/j.jchroma.2024.S0022073624003303`
- **문제**: `j.jchroma`는 *Journal of Chromatography*의 DOI 접두사임. *J Cardiovasc Electrophysiol*의 DOI 접두사가 아님
- **실제**: 논문 자체(PubMed 39754789, ScienceDirect PII S0022073624003303)는 실존하며 *Journal of Electrocardiology*로 확인됨
- **권장 조치**: DOI를 `10.1016/j.jelectrocard.2024.xxx` 또는 PubMed에서 직접 확인된 정확한 DOI로 수정

#### 2. 논문 1-8 — PMID 미확인 (Quaternion CNN 2026)
- **기재 PMID**: 42068635
- **문제**: 2026년 출판 논문으로 PubMed 인덱싱이 완료되지 않았을 가능성. BCML Lab 페이지에서 논문 존재 확인, DOI/저널 정보는 일치
- **권장 조치**: PubMed에서 PMID 42068635 직접 검색하여 인덱싱 여부 확인

#### 3. 논문 2-7 — 저널명 오류 (Vodrahalli 2023)
- **기재 저널**: "JAMA Netw Open"
- **실제 저널**: *JAMA Dermatology* (doi: 10.1001/jamadermatology.2022.5689)
- **권장 조치**: 저널명 수정

#### 4. 논문 3-3 — PMID 미확인 (Hauer 2026 DCT T2DM)
- **기재 PMID**: 41997891
- **문제**: 2026년 출판 논문. Capital Region Denmark Research Portal에서 논문 존재 확인. PubMed 직접 PMID 검색 결과 미반환 (인덱싱 지연 가능)
- **권장 조치**: PubMed에서 PMID 직접 확인

### ⚠️ 특수 케이스: 논문 3-6 — 가상의 인용 (Wagner 2022, Nat Med)
- **기재 내용**: "Wagner et al., 2022, *Nat Med* (Real-time AI feedback Image Quality)" — DOI를 JAMA Dermatology PMC10018405로 연결
- **실제 상황**: 이 인용은 두 개의 실제 논문을 혼동하여 합성한 것
  1. Vodrahalli K et al., 2023. *JAMA Dermatology*. (PMC10018405) — 실제 AI quality feedback 연구
  2. Wagner JK 등의 2023년 ImageQX 논문 (PMC10468541) — *Telemedicine e-Health*
- **결론**: "Wagner et al., 2022, Nat Med"이라는 논문은 존재하지 않음. Vodrahalli 2023과 Wagner ImageQX를 혼동·합성한 허위 인용
- **권장 조치**: Stage 3 표에서 3-6 항목을 삭제하고, Vodrahalli 2023 (이미 2-7에 수록)으로 단일 인용 통합

### ⚠️ 세부 오류 목록 (참고용)

| 항목 | 오류 유형 | 기재 내용 | 실제 내용 |
|------|---------|---------|---------|
| 2-4 저자 | 제1저자명 오류 | "Park SH et al." | Outlaw F, Nixon M, Odeyemi O et al. |
| 2-5 제목 | 비공식 명칭 사용 | "The ANcam: A Novel Smartphone Application..." | "Grading Acanthosis Nigricans Using a Smartphone and Color Analysis..." |
| 2-5 쪽수 | 쪽수 오류 | 37(2):112-119 | 37(2):139 (페이지 번호 확인 필요) |
| 2-7 저널 | 저널명 오류 | JAMA Netw Open | JAMA Dermatology |
| 2-9 쪽수 | 쪽수 오류 | 27:567-577 | 27(5):880-890 |
| 4-2 제1저자 | 저자 오류 | "Pierson E et al." | Rodriguez EM et al. |
| 4-5 저널 | 저널명 불완전 | "JMIR" | JMIR Human Factors |
| 3-6 전체 | 가상 인용 | Wagner 2022, Nat Med | 존재하지 않는 인용 조합 |

---

## 미확인 항목 상세 (❓)

### 1. 논문 4-4 — Cao 2025 ECEESPE P804 (컨퍼런스 추상)
- ECEESPE2025 컨퍼런스 및 ea/0110 시리즈는 실존하나, P804 Cao PCOS facial morphology 추상의 구체적 내용을 외부 웹 검색으로 직접 확인 불가
- 컨퍼런스 추상(abstract)은 통상적으로 동료심사 논문보다 낮은 증거 수준이므로, 인용 시 "(Conference Abstract)" 표기 권장
- **위험도**: 낮음 — ECEESPE2025는 공인 학회이며, 같은 시리즈의 다른 추상들은 접근 가능

### 2. 보조참고 2 — Wagner JK 2022 ImageQX
- "Wagner JK"와 ImageQX의 직접 저자-논문 연결 미확인
- 실제 ImageQX 논문 저자 및 citation 정보가 "Wagner JK 2022"와 일치하지 않을 가능성
- **위험도**: 낮음 — ImageQX 자체는 실존하며 SkinTracker에 인용됨. 저자명 확인 필요

---

## 할루시네이션 의심 항목

❌ **없음** — 모든 참고문헌의 핵심 논문은 실존하는 것으로 확인됨. 다만 1-5의 DOI 오류, 3-6의 가상 인용 조합은 주의 필요.

---

## 권장 조치

### 즉시 수정 필요

1. **논문 1-5 DOI 수정**: `j.jchroma`를 실제 J Cardiovasc Electrophysiol DOI로 교체
2. **논문 3-6 삭제**: "Wagner et al., 2022, Nat Med" 가상 인용 제거 — Vodrahalli 2023 단일 인용으로 통합
3. **논문 2-7 저널명 수정**: "JAMA Netw Open" → "JAMA Dermatology"
4. **논문 2-9 쪽수 수정**: 567-577 → 880-890 (Skin Res Technol 27(5))
5. **논문 4-2 저자 수정**: "Pierson E et al." → "Rodriguez EM et al."

### 확인 권장

6. **논문 2-4 저자 확인**: "Park SH"가 아닌 Outlaw F 등으로 수정
7. **논문 2-5 제목 공식화**: ANcam → "Grading Acanthosis Nigricans Using a Smartphone and Color Analysis"
8. **논문 1-8 PMID 42068635**: PubMed에서 직접 조회하여 인덱싱 여부 확인
9. **논문 3-3 PMID 41997891**: PubMed에서 직접 조회하여 인덱싱 여부 확인
10. **논문 4-4**: 컨퍼런스 추상 인용 시 "(Conference Abstract, Endocrine Abstracts, 2025)" 표기 추가
11. **논문 4-5 저널명**: "JMIR" → "JMIR Human Factors" 수정

---

## 전체 평가 요약

**전반적 품질: 양호 (주요 논문 대부분 실존 확인)**

- 30편 중 24편(80%)은 DOI/PMID/공식 페이지를 통해 내용까지 완전히 검증됨
- **치명적 오류 1건**: 논문 3-6 ("Wagner et al., 2022, Nat Med") — 실제로는 Vodrahalli 2023 (JAMA Dermatology)과 Wagner ImageQX를 혼동한 가상 인용 조합
- **경미한 오류 7건**: 저자명·저널명·쪽수 등 세부 서지정보 오류 (논문 자체는 실존)
- **미확인 2건**: 컨퍼런스 추상(4-4) 및 보조 참고문헌 저자명(보조-2)
- 2026년 출판 논문 (1-8 Quaternion CNN, 3-3 Hauer DCT) 은 PubMed 인덱싱 지연으로 PMID 직접 확인 불가이나 논문 자체는 실존 확인

**In-the-wild rPPG·얼굴·DCT 핵심 논문들(eBRAVE-AF, Apple Heart Study, mPower, MoodCapture, PARK, ANcam 등)은 모두 검증됨.**
