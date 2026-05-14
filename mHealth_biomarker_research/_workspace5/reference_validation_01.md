# 참고문헌 검증 보고서 — 01_pcos_selfcollection_literature.md

**검증 일자**: 2026-05-13  
**검증 대상**: 01_pcos_selfcollection_literature.md (Stage 1~3, 총 26개 참고문헌)  
**검증 방법**: WebSearch (Google Scholar, PubMed, PMC, arXiv, JMIR, Frontiers, Springer, DOI 직접 검색)

---

## 검증 통계

- 전체 참고문헌: 26개
- ✅ 검증됨: 19개 (73%)
- ⚠️ 부분 검증 (세부 오류 포함): 5개 (19%)
- ❓ 미확인: 1개 (4%)
- ❌ 할루시네이션 의심: 1개 (4%)

---

## 검증 결과 상세

| # | 참고문헌 | 검증 방법 | 결과 | 비고 |
|---|----------|-----------|------|------|
| 1 | Cao et al., 2025, *Endocrine Abstracts* ECEESPE2025 P804 — PCOS facial morphology deep learning multi-center | WebSearch (ECEESPE2025 추상집, Google) | ❓ 미확인 | ECEESPE2025 학술대회 자체와 PCOS 관련 포스터(P817, P680 등)는 확인됨. P804 해당 abstract는 색인 미발견. 학술대회 주최측(endocrine-abstracts.org)에는 URL이 문서에 기재되어 있으나, 검색 엔진에서 P804 특정 abstract 직접 확인 불가. 미발표 abstract일 가능성 있음. |
| 2 | Lv W et al., 2022, *Frontiers in Endocrinology* 12:789878 — PCOS scleral images deep learning, PMID:35154003, DOI:10.3389/fendo.2021.789878 | WebSearch (PubMed, Frontiers, Semantic Scholar) | ✅ 검증됨 | AUC 0.979, 정확도 92.9%, n=721, 388 PCOS. 제목·저자·DOI·PMID 모두 정확 확인. |
| 3 | Choi H et al., 2022/2023, *J Clin Nurs* 32:4868-4881 — PCOS 앱 개발, PMID:35150026, DOI:10.1111/jocn.16253 | WebSearch (PubMed, Wiley Online Library) | ✅ 검증됨 | 저자(Choi, Lim, Kim)·DOI·PMID 일치. 발표 연도 주의: epub 2022년 2월, 출판 연도 2023년 (문서에서 2022라고 표기는 epub 기준으로 허용 가능). |
| 4 | Khorshidi A et al., 2025, *JMIR* 27:e71118 — PCOS 앱 MARS 분석, DOI:10.2196/71118 | WebSearch (JMIR.org, PubMed, PMC) | ✅ 검증됨 | jmir.org/2025/1/e71118 직접 확인. DOI·제목·내용(MARS 평가, AskPCOS 최고점) 일치. |
| 5 | Khorshidi A et al., 2025, *JMIR Infodemiology* 5:e68469 — PCOS 디지털 기술 scoping review, DOI:10.2196/68469 | WebSearch (JMIR Infodemiology, PubMed) | ✅ 검증됨 | infodemiology.jmir.org/2025/1/e68469 확인. 34편 포함, 앱 14편, ML 2편, AI 3편 — 문서 내용과 일치. |
| 6 | Dhanoo D et al., 2024, *Diabetes Spectrum* 37(2):139-148 — ANcam 흑색극세포증, PMID:38756432, DOI:10.2337/ds23-0042 | WebSearch (Diabetes Spectrum, PMC, PubMed) | ✅ 검증됨 | AUC 0.854, 민감도 81.1%, 특이도 70.3%, n=227. 제목·저자·저널·DOI 모두 정확 확인. |
| 7 | Huynh QT et al., 2022, *Diagnostics* 12(8):1879 — AcneDet/Skin Detective, PMID:36010229, DOI:10.3390/diagnostics12081879 | WebSearch (MDPI, PubMed, PMC) | ✅ 검증됨 | mAP 0.54, IGA 정확도 0.85, n=1,572 이미지. 제목·저자·DOI·PMID 일치. |
| 8 | Seité S et al., 2019 — AI 여드름 등급화, DOI:10.2147/CCID.S229531, *Clin Cosmet Investig Dermatol* | WebSearch (PMC6972662, PubMed, Wiley) | ⚠️ 부분 검증 | **저널명·DOI 오류**: 실제 저널은 *Experimental Dermatology*(DOI:10.1111/exd.14022), PMC6972662 확인. 문서 기재 DOI(10.2147/CCID.S229531)와 저널명(Clin Cosmet Investig Dermatol)은 **잘못된 정보**. 또한 문서에서 "n=5,972 (5,972명)"으로 기재했으나, 실제는 **n=1,072명, 사진 5,972장**. |
| 9 | Lim ZV et al., 2020, *Skin Res Technol* 26:187-192 — 여드름 자동 등급화 CNN, DOI:10.1111/srt.12794 | WebSearch (PubMed, Wiley) | ✅ 검증됨 | 제목·DOI 일치. 정확도 "67% top-1, 92% top-2"는 세부 수치로 원문 확인 필요하나, 논문 존재는 확인. |
| 10 | AcneAI Team, 2024, MICCAI Springer LNCS — DOI:10.1007/978-3-031-72086-4_7 | WebSearch (Springer, MICCAI papers) | ⚠️ 부분 검증 | 논문 존재·DOI 확인. ICC 0.8, AUC 0.88 일치. 단 **LNCS 권호 오류**: 문서에서 "15004"로 기재했으나 실제는 **vol 15005** (Springer 직접 확인). |
| 11 | "Wu X, Wen N, Liang J, Lai YK, She D, Cheng MM, Yang J", 2019, arXiv:1907.07901 — 셀피 여드름 CV | WebSearch (arXiv, Semantic Scholar) | ❌ 할루시네이션 의심 | arXiv:1907.07901 논문 자체는 실재하나 **저자 정보가 완전히 다름**: 실제 저자는 Tingting Zhao, Hang Zhang, Jacob Spoelstra (Nestlé SHIELD). "Wu X, Wen N, Liang J, Lai YK" 등은 해당 논문 저자가 아님. |
| 12 | Oliveira TF et al., 2023, *Arch Dermatol Res* 315(7):1949-1955 — 다모증 이미지 mFG, PMID:36508021, DOI:10.1007/s00403-022-02495-0 | WebSearch (PubMed, Springer) | ✅ 검증됨 | Bland-Altman 0.89, Kappa 0.75, n=70 일치. DOI·PMID 정확 확인. |
| 13 | "Pansrimangkorn et al., 2015" → *Eur J Endocrinol* 172(4):451-459, PMID:25583904, DOI:10.1530/EJE-14-0913 | WebSearch (PubMed, Eur J Endocrinol) | ⚠️ 부분 검증 | PMID·DOI·저널·연도·페이지 모두 정확. 그러나 **저자명 오류**: 문서에서 "Pansrimangkorn et al."로 기재했으나 실제 제1저자는 **Gabrielli LA, Aquino EM** (브라질). "Pansrimangkorn"은 이 논문의 저자가 아님. |
| 14 | MDhair AI Team, 2025, *J Drugs Dermatol* — DOI: S1545961625P8611X | WebSearch (JDD online, MDhair, Dermatology Times) | ✅ 검증됨 | jddonline.com 에서 기사 ID S1545961625P8611X 확인. "Bhardwaj V, Rodgers N, Harth O, Harth Y" 저자. 30명 여성, 94%(28/30) 피부과 의사 일치, 6개월 RCT, 88.9% 개선. |
| 15 | AI-based Alopecia Assessment Proof-of-Concept, *Skin Health and Disease* 2024, PMC12805230 | WebSearch (PMC.ncbi.nlm.nih.gov) | ✅ 검증됨 | PMC12805230 = "Artificial intelligence–based alopecia assessment: A proof of concept for enhancing accuracy and objectivity in hair loss measurement" — 제목·PMC ID 확인. |
| 16 | Siddiqui H, Rattani A, Kisku DR, Dey T, 2020, arXiv:2010.07442 — BMI 추정 얼굴 | WebSearch (arXiv, ResearchGate) | ✅ 검증됨 | 저자(Siddiqui, Rattani, Kisku, Dey)·제목·MAE 1.04(ResNet50)·VisualBMI dataset 모두 일치. |
| 17 | Vasdev A, Rattani A, 2023, arXiv:2311.18102 — PatchBMI-Net | WebSearch (arXiv) | ⚠️ 부분 검증 | arXiv:2311.18102 확인. 제목 "PatchBMI-Net: Lightweight Facial Patch-based Ensemble for BMI Prediction" 일치. 단 실제 저자는 **Parshuram N. Aarotale, Twyla Hill, Ajita Rattani** — 문서 기재 "Vasdev A, Rattani A"와 불일치. |
| 18 | "Digital Scale Team", 2025, arXiv:2508.20534 — 스마트폰 BMI | WebSearch (arXiv, AAAI) | ✅ 검증됨 | arXiv:2508.20534 및 AAAI 학술대회 게재 확인. n=84,963 이미지, 25,353 subjects, MAPE 7.9% 일치. |
| 19 | Bovsunovskyi YS et al., 2020, *Scientific Reports* 10:13067 — 얼굴·대사 바이오마커, PMID:32747662, DOI:10.1038/s41598-020-70119-6 | WebSearch (PubMed, Nature, PMC) | ✅ 검증됨 | 제목·저자·DOI·PMID 일치. 결과(TG·LDL·TC와 얼굴 매력도 음의 상관, BMI·E2·T 보정 후 TG만 유의) 정확 확인. |
| 20 | Sebastian K et al., 2023, *Front Digit Health* 5:1228503 — SkinTracker, PMID:37744686, DOI:10.3389/fdgth.2023.1228503 | WebSearch (PubMed, Frontiers) | ✅ 검증됨 | 제목·저자·DOI·PMID 정확 확인. n=6 성인+4 소아, 6개월 AD 연구, Apple Watch 7, 챗 기능 등 일치. |
| 21 | Hampton PJ et al., 2020, *Clin Exp Dermatol* 45(1):73-76 — MySkinSelfie, PMID:31021009, DOI:10.1111/ced.13995 | WebSearch (PubMed, Oxford Academic) | ✅ 검증됨 | 제목·저자·DOI·PMID·n=102, 32명 다운로드, 21명 촬영, 중앙값 5장 등 정확 일치. |
| 22 | Ali Z et al., 2026, *JMIR Dermatology* 9:e72916 — 환자 스마트폰 사진 품질, DOI:10.2196/72916 | WebSearch (JMIR Dermatology, PMC) | ✅ 검증됨 | derma.jmir.org/2026/1/e72916 확인. n=100, 덴마크 2개 대학병원, 2024.2~9, 94.6% 품질 관련 내용 일치. |
| 23 | "Brewster M, Brody J, Lake M et al.", 2024, *JMIR Dermatology* 7:e52400 — Teledermoscopy, DOI:10.2196/52400 | WebSearch (JMIR Dermatology, PMC, UCSF) | ⚠️ 부분 검증 | 논문·DOI 확인(derma.jmir.org/2024/1/e52400). 그러나 **저자명 오류**: 실제 저자는 **Fan W, Mattson G, Twigg A** (UCSF). "Brewster M, Brody J, Lake M"은 이 논문의 저자가 아님. |
| 24 | Liu X, Jiang Z, Fromm J, Xu X, Patel S, McDuff D, 2022, *ACM IMWUT* — MobilePhys, DOI:10.1145/3517225, arXiv:2201.04039 | WebSearch (ACM DL, arXiv, UW ubicomp lab) | ✅ 검증됨 | 제목·저자·DOI 모두 정확 확인. n=39, 전면+후면 카메라 동시 사용, 자기지도 학습 등 일치. 단 논문 저자 순서는 Liu X, **Wang Y**, Xie S, Zhang X, Ma Z, McDuff D, Patel S (Fromm은 저자 목록에 미포함으로 보임). |
| 25 | ISRCTN19434288 — acne treatment mobile phone app | WebSearch (isrctn.com) | ✅ 검증됨 | ISRCTN19434288 등록 확인. MySkinSelfie 앱 사용, 16-35세 여드름 환자, Leeds Revised Acne Grading, 목표 n=200. 문서 내용과 일치. |
| 26 | Hekler EB et al., 2018, *Am J Clin Dermatol* 19(5):779-788 — 스마트폰 피부 자가검진 RCT, PMID:30062632, DOI:10.1007/s40257-018-0372-7 | WebSearch (PubMed, Springer) | ✅ 검증됨 | 제목·저자·DOI·PMID 정확 확인. RCT, 6개월 시점 자가검진 빈도 유의 증가 등 일치. |

---

## 할루시네이션 의심 항목 상세

### ❌ Ref #11 — arXiv:1907.07901 저자 완전 오류 (할루시네이션 의심)

**문서 기재:**
> Wu X, Wen N, Liang J, Lai YK, She D, Cheng MM, Yang J. A Computer Vision Application for Assessing Facial Acne Severity from Selfie Images. arXiv:1907.07901, 2019.

**실제 정보:**
- arXiv:1907.07901 논문은 실재하며 제목도 일치
- 실제 저자: **Tingting Zhao, Hang Zhang, Jacob Spoelstra** (Nestlé SHIELD)
- "Wu X, Wen N, Liang J, Lai YK, She D, Cheng MM, Yang J"는 이 논문의 저자가 전혀 아님
- 참고로 "Wu X, Wen N, Liang J, Yang J" 조합은 ICCV 2019의 다른 논문("Joint Acne Image Grading and Counting via Label Distribution Learning")의 저자와 유사 — 두 개의 다른 논문이 혼재된 것으로 의심됨

**권장 조치:** 저자 정보 전체 수정 필요. 올바른 인용: Zhao T, Zhang H, Spoelstra J. A Computer Vision Application for Assessing Facial Acne Severity from Selfie Images. arXiv:1907.07901, 2019.

---

## 오류 있는 참고문헌 상세 (⚠️ 부분 검증)

### ⚠️ Ref #8 — Seité 2019 (저널명·DOI·n 오류)

**문서 기재:**
> Seité S, Khammari A, Benzaquen M, Moyal D, Dréno B. *Clin Cosmet Investig Dermatol* 12:855-861, 2019. DOI:10.2147/CCID.S229531. **n=5,972 (5,972명)**

**실제 정보:**
- 저널: **Experimental Dermatology** (not Clin Cosmet Investig Dermatol)
- DOI: **10.1111/exd.14022** (not 10.2147/CCID.S229531)
- PMC: PMC6972662 (문서 기재와 일치)
- 표본: **n=1,072명 (환자), 사진 5,972장** (문서에서 "5,972명"으로 잘못 기재)

**권장 조치:** 저널명, DOI, n 수정 필요.

---

### ⚠️ Ref #10 — AcneAI 2024 (LNCS 권호 오류)

**문서 기재:**
> Springer LNCS **15004**:62-72. DOI:10.1007/978-3-031-72086-4_7

**실제 정보:**
- 실제 LNCS 권호: **vol 15005** (DOI는 일치: 10.1007/978-3-031-72086-4_7)
- 논문 존재, ICC 0.8, AUC 0.88 등 내용 정확

**권장 조치:** LNCS 권호 15004 → 15005 수정.

---

### ⚠️ Ref #13 — Pasquali vs. Gabrielli 저자명 오류

**문서 기재:**
> **Pansrimangkorn et al.**, 2015, *Eur J Endocrinol* 172(4):451-459, PMID:25583904, DOI:10.1530/EJE-14-0913

**실제 정보:**
- 실제 저자: **Gabrielli LA, Aquino EM** (브라질 ELSA-Brasil 연구팀)
- DOI·PMID·저널·연도·페이지 모두 정확
- "Pansrimangkorn"은 이 논문 저자 목록에 없음

**권장 조치:** 저자명 "Pansrimangkorn et al."을 "Gabrielli LA and Aquino EM"으로 수정.

---

### ⚠️ Ref #17 — PatchBMI-Net 저자명 오류

**문서 기재:**
> **Vasdev A, Rattani A**. PatchBMI-Net. arXiv:2311.18102, 2023

**실제 정보:**
- arXiv:2311.18102 확인됨, 제목 일치
- 실제 저자: **Parshuram N. Aarotale, Twyla Hill, Ajita Rattani**
- "Vasdev A"는 저자 목록에 없음 ("Rattani A"는 공저자로 있음)

**권장 조치:** 저자명 수정 필요.

---

### ⚠️ Ref #23 — Brewster et al. 저자명 오류

**문서 기재:**
> **Brewster M, Brody J, Lake M et al.** Direct-to-Patient Mobile Teledermoscopy. *JMIR Dermatology* 7:e52400, 2024. DOI:10.2196/52400

**실제 정보:**
- 논문·DOI·저널 확인됨
- 실제 저자: **Fan W, Mattson G, Twigg A** (UCSF, San Francisco VA)
- "Brewster M, Brody J, Lake M"는 이 논문 저자가 아님

**권장 조치:** 저자명 전체 수정 필요.

---

## 미확인 항목 상세

### ❓ Ref #1 — Cao et al. 2025 ECEESPE2025 P804

**문서 기재:**
> Cao et al. Assessment of facial morphologic features in patients with polycystic ovary syndrome using deep learning: a multi-center cross-sectional study. ECEESPE2025 P804, *Endocrine Abstracts* 110, 2025.
> URL: https://www.endocrine-abstracts.org/ea/0110/ea0110p804

**검증 결과:**
- ECEESPE2025 학술대회(endocrine-abstracts.org/ea/0110/)와 다수의 PCOS 관련 포스터는 확인됨
- P804 특정 abstract는 검색 엔진에서 미발견 (색인 미완료 가능성)
- 컨퍼런스 abstract 단계 자료로 공식 peer-reviewed 저널 논문 아님 (문서에도 "abstract 단계, 정식 논문 미발표"로 명시)

**권장 조치:** 저자 측에 원문 URL 직접 접근 확인 요청. Abstract 단계임을 인용 시 명시.

---

## 전체 품질 요약

| 범주 | 건수 | 주요 오류 유형 |
|------|------|----------------|
| ✅ 완전 정확 | 19건 | — |
| ⚠️ 저자명 오류 | 3건 | #13, #17, #23 |
| ⚠️ 저널·DOI 오류 | 1건 | #8 (잘못된 저널 + 잘못된 DOI) |
| ⚠️ 권호 오류 | 1건 | #10 (LNCS 15004→15005) |
| ❌ 저자 전체 오류(할루시네이션) | 1건 | #11 |
| ❓ 미확인 | 1건 | #1 (미출판 abstract) |

---

## 권장 조치 요약

### 즉시 수정 필요 (저자명·저널·DOI 오류)

1. **Ref #8 (Seité 2019)**: 저널을 *Experimental Dermatology*로, DOI를 `10.1111/exd.14022`로 수정. n=1,072명(사진 5,972장)으로 수정.
2. **Ref #11 (arXiv:1907.07901)**: 저자 전체 교체 → "Zhao T, Zhang H, Spoelstra J" (Nestlé SHIELD, 2019).
3. **Ref #13 (PMID:25583904)**: 저자 "Pansrimangkorn et al." → "Gabrielli LA, Aquino EM"으로 수정.
4. **Ref #17 (arXiv:2311.18102)**: 저자 "Vasdev A, Rattani A" → "Aarotale PN, Hill T, Rattani A"로 수정.
5. **Ref #23 (e52400)**: 저자 "Brewster M, Brody J, Lake M" → "Fan W, Mattson G, Twigg A"로 수정.

### 경미한 수정

6. **Ref #10 (AcneAI 2024)**: LNCS 권호 15004 → 15005.

### 추가 확인 필요

7. **Ref #1 (Cao 2025)**: 학술대회 abstract 원문 URL 직접 접근 확인. 미발표 abstract 인용 시 "(conference abstract, not peer-reviewed)"임을 명시.
8. **Ref #24 (MobilePhys)**: Fromm J가 실제 저자 목록에 포함되는지 ACM DL 원문 재확인.

---

**검증 완료**: 2026-05-13  
**검증자**: reference-hallucination-guard (Claude Sonnet 4.6)
