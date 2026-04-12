# 참고문헌 검증 보고서 (Reference Hallucination Guard)

**검증 대상**: _workspace2/01_literature_review.md
**검증 일자**: 2026-04-12
**검증 도구**: PubMed PMID 직접 조회, Crossref DOI API, WebSearch (Google Scholar/PubMed)

---

## 검증 통계

- 전체 참고문헌: **37개**
- ✅ 검증됨: **28개** (75.7%)
- ⚠️ 부분 검증: **4개** (10.8%)
- ❓ 미확인: **3개** (8.1%)
- ❌ 할루시네이션 의심: **2개** (5.4%)

---

## 검증 결과 상세

| # | 논문 (저자, 연도) | 검증 방법 | 결과 | 비고 |
|---|------------------|----------|------|------|
| 1 | Mirzohreh et al., 2024, *Systematic Reviews* | PMID:39049099 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 2 | Yu et al., 2024, *Frontiers in Endocrinology* | PMID:38313837 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 3 | Sarathivarman et al., 2025, *JPBS* | PMID:41522593 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 4 | de Fatima Azevedo et al., 2026, *Scientific Reports* | PMID:41639286 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 5 | Bernal et al., 2025, *Clinical Endocrinology* | PMID:39526386 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 6 | Moreira et al., 2021, *Women & Health* | PMID:34719338 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 7 | Hao et al., 2021, *Scientific Reports* | PMID:33446725 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 8 | Zeng et al., 2025, *Reproduction & Fertility* | PMID:41026638 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 9 | Moreira et al., 2024, *The Journal of Pain* | PMID:37524218 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 10 | Rajesh, 2025, *MethodsX* | PMID:41209338 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 11 | Wearable HRV SR, 2025, *Sports Medicine* | DOI Crossref | ✅ | de Jager et al., 2026 (published 2026-01-17). 연도 약간 차이(2025→2026 온라인) |
| 12 | HRV and menstrual regularity, 2025, *npj Digital Medicine* | DOI Crossref | ✅ | Heydari et al., 2025. 제목·저널·DOI 일치 |
| 13 | Huynh et al., 2022, *Diagnostics* | PMID:36010229 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 14 | Cell phone acne app, 2023, *Applied Intelligence* | PMID:35919632 | ✅ | Wang et al., 2023. 제목·저널·DOI 일치 |
| 15 | AcneAI, 2024, *MICCAI* | WebSearch | ✅ | DOI:10.1007/978-3-031-72086-4_7 확인. MICCAI 2024 LNCS vol 15005 |
| 16 | Acne evaluation, 2024, *Scientific Reports* | DOI Crossref | ✅ | Gao et al., 2025 (online 2025-01). DOI 일치 |
| 17 | Oliveira et al., 2023, *Arch Dermatol Res* | PMID:36508021 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 18 | Dhanoo et al., 2024, *Diabetes Spectrum* | PMID:38756432 | ✅ | 제목·저자·저널·DOI 모두 일치 |
| 19 | Jiang et al., 2021, *Comput Biol Med* | PMID:33895458 | ❌ **저자 불일치** | **실제 저자: Yousaf, Hussein, Sultani** (Jiang이 아님). DOI·저널·연도는 일치하나 저자명이 완전히 다름. 할루시네이션 의심 |
| 20 | PatchBMI-Net, 2023, *arXiv* | arXiv:2311.18102 | ✅ | Aarotale et al., 2023. arXiv 확인 완료 |
| 21 | Oztel et al., 2023, *Adv Intell Systems* | DOI WebSearch | ✅ | Yolcu Oztel & Sahin, 2023. DOI:10.1002/aisy.202300211 확인 |
| 22 | Dark circle AI, 2023, *Skin Res Technol* | PMID:38009029 | ⚠️ **철회(Retracted)** | 논문 존재 확인되나, **2025년 10월 철회됨** (Retraction PMID:41059760). 인용 부적절 |
| 23 | AI in PCOS 리뷰, 2025, *La Radiologia Medica* | DOI Crossref | ✅ | Wang et al., 2025. 제목·저널·DOI 일치 |
| 24 | PCOS 앱 리뷰, 2025, *JMIR* | DOI Crossref | ✅ | Arabkermani et al., 2025. DOI:10.2196/71118 확인 |
| 25 | Endo digital tech SR, 2025, *JMIR Human Factors* | DOI Crossref | ✅ | Pavic et al., 2025. DOI:10.2196/71859 확인 |
| 26 | Endo ML 메타분석, 2025, *Front Endocrinol* | DOI Crossref | ✅ | Zhang et al., 2026 (online). DOI 일치 |
| 27 | 염증 바이오마커 ML, 2025, *Scientific Reports* | DOI Crossref | ✅ | Liu et al., 2025. DOI 일치 |
| 28 | Rahmawati et al., 2025, *Scientific Reports* | DOI Crossref | ❌ **저자 불일치** | **실제 저자: Agirsoy & Oehlschlaeger** (Rahmawati가 아님). DOI:10.1038/s41598-025-10453-9는 존재하나 저자명 완전 불일치. 할루시네이션 의심 |
| 29 | ML menstrual cycle phase, 2025, *Comput Biol Med* | WebSearch+PubMed | ⚠️ **DOI 불일치** | 논문 존재 확인 (Masuda et al., 2025, PMID:39889448). 실제 DOI: 10.1016/j.compbiomed.2025.109705. 파일 기재 DOI `10.1016/S0010-4825(25)00055-1`은 Crossref 404 반환 |
| 30 | Biomonitoring women's health, 2025, *Nature Communications* | DOI Crossref | ✅ | Moghimikandelousi et al., 2025. DOI 일치 |
| 31 | Menstrual cycle vital sign, 2024, *F&S Reviews* | WebSearch | ⚠️ **DOI 불일치** | 논문 존재 확인 (Rosen Vollmar et al., 2024). 실제 DOI: 10.1016/j.xfnr.2024.100081. 파일 기재 DOI `10.1016/S2666-5719(24)00038-0`은 Crossref 404 반환 (ISSN 기반 URL이지 DOI가 아님) |
| 32 | rPPG 종합 리뷰, 2025, PMC | WebSearch | ❓ | 다수 rPPG 리뷰 존재하나, 특정 논문 특정 불가. PMID/DOI 미기재로 정확한 대응 논문 불명 |
| 33 | FibriCheck FDA-AF, 2025, *npj Digital Medicine* | DOI Crossref | ✅ | Sollee et al., 2025. DOI:10.1038/s41746-025-02059-2. 본문 #14와 동일 논문 |
| 34 | rPPG SpO2, Cheng et al., 2024, *Bioengineering* | WebSearch | ✅ | Cheng et al., 2024. DOI:10.3390/bioengineering11030251 확인 |
| 35 | rPPG 혈압, Luo et al., 2019, *Circ Cardiovasc Imaging* | WebSearch+PubMed | ✅ | Luo et al., 2019. DOI:10.1161/CIRCIMAGING.119.008857 확인. PMID:31382766 |
| 36 | rPPG HRV 리뷰, 2024, *Frontiers Bioeng & Biotech* | WebSearch | ⚠️ | "Deep learning and rPPG powered advancements" (2024, Front Bioeng Biotech) 존재 확인. 그러나 파일에 저자명·DOI 미기재로 정확한 매핑은 부분적 |
| 37 | 피부암 DL, 2023, *Diagnostics* | WebSearch | ❓ | 피부암 DL 관련 2023 Diagnostics 논문 다수 존재하나, 저자·제목·DOI 미기재로 특정 불가 |

---

## 할루시네이션 의심 항목 상세 분석

### ❌ #19: "Jiang et al., 2021" → 실제 Yousaf, Hussein, Sultani (2021)

- **파일 기재**: Jiang M et al. (2021). BMI estimation from facial images. *Comput Biol Med*. PMID:33895458
- **실제 논문**: Yousaf N, Hussein S, Sultani W. (2021). "Estimation of BMI from Facial Images using Semantic Segmentation based Region-Aware Pooling." *Computers in Biology and Medicine*. PMID:33895458, DOI:10.1016/j.compbiomed.2021.104392
- **분석**: PMID, DOI, 저널, 연도, 제목 내용은 모두 일치하나, **저자명이 완전히 다름**. "Jiang"이라는 저자는 이 논문에 존재하지 않음. LLM이 논문 메타데이터를 혼합한 전형적 할루시네이션 패턴.
- **권장 조치**: 저자를 "Yousaf N, Hussein S, Sultani W"로 수정

### ❌ #28: "Rahmawati et al., 2025" → 실제 Agirsoy & Oehlschlaeger (2025)

- **파일 기재**: Rahmawati et al., 2025, *Scientific Reports*. DOI:10.1038/s41598-025-10453-9
- **실제 논문**: Agirsoy M, Oehlschlaeger MA. (2025). "A machine learning approach for non-invasive PCOS diagnosis from ultrasound and clinical features." *Scientific Reports*. DOI:10.1038/s41598-025-10453-9
- **분석**: DOI, 저널, 연도, 주제는 일치하나, **저자명이 완전히 다름**. "Rahmawati"는 이 논문의 저자가 아님. LLM이 PCOS ML 관련 다른 논문의 저자를 혼합한 것으로 추정.
- **권장 조치**: 저자를 "Agirsoy M, Oehlschlaeger MA"로 수정. 또는 실제 Rahmawati et al.의 PCOS 관련 논문이 별도로 존재하는지 확인 후 교체.

---

## 검증 완료 목록 (✅) — 28편

| # | 저자/출처 | 검증 방법 |
|---|----------|----------|
| 1 | Mirzohreh et al., 2024 | PMID |
| 2 | Yu et al., 2024 | PMID |
| 3 | Sarathivarman et al., 2025 | PMID |
| 4 | de Fatima Azevedo et al., 2026 | PMID |
| 5 | Bernal et al., 2025 | PMID |
| 6 | Moreira et al., 2021 | PMID |
| 7 | Hao et al., 2021 | PMID |
| 8 | Zeng et al., 2025 | PMID |
| 9 | Moreira et al., 2024 | PMID |
| 10 | Rajesh, 2025 | PMID |
| 11 | de Jager et al., 2026 (Sports Med) | DOI |
| 12 | Heydari et al., 2025 (npj Dig Med) | DOI |
| 13 | Huynh et al., 2022 | PMID |
| 14 | Wang et al., 2023 (Applied Intelligence) | PMID |
| 15 | AcneAI, 2024 (MICCAI) | DOI |
| 16 | Gao et al., 2025 (Sci Rep, acne) | DOI |
| 17 | Oliveira et al., 2023 | PMID |
| 18 | Dhanoo et al., 2024 | PMID |
| 20 | PatchBMI-Net, 2023 (arXiv) | arXiv |
| 21 | Yolcu Oztel & Sahin, 2023 | DOI |
| 23 | Wang et al., 2025 (La Radiol Med) | DOI |
| 24 | Arabkermani et al., 2025 (JMIR) | DOI |
| 25 | Pavic et al., 2025 (JMIR HF) | DOI |
| 26 | Zhang et al., 2026 (Front Endocrinol) | DOI |
| 27 | Liu et al., 2025 (Sci Rep, endo) | DOI |
| 30 | Moghimikandelousi et al., 2025 (Nat Commun) | DOI |
| 33/14 | FibriCheck, Sollee et al., 2025 | DOI |
| 34 | Cheng et al., 2024 (Bioengineering) | DOI+WebSearch |
| 35 | Luo et al., 2019 (Circ CV Imaging) | DOI+PMID |

---

## 제외 권장 목록 (❌)

| # | 항목 | 사유 | 권장 조치 |
|---|------|------|----------|
| 19 | "Jiang et al., 2021" | 저자 할루시네이션. 실제 저자 Yousaf, Hussein, Sultani | 저자명 수정 → Yousaf N, Hussein S, Sultani W |
| 28 | "Rahmawati et al., 2025" | 저자 할루시네이션. 실제 저자 Agirsoy M, Oehlschlaeger MA | 저자명 수정 → Agirsoy M, Oehlschlaeger MA |

---

## 주의 필요 목록 (⚠️, ❓)

| # | 항목 | 등급 | 사유 | 권장 조치 |
|---|------|------|------|----------|
| 22 | Dark circle AI, 2023, *Skin Res Technol* | ⚠️ | **철회 논문 (Retracted Oct 2025)**. PMID:41059760 참조 | 인용 제거 또는 철회 사실 명시 |
| 29 | ML menstrual cycle, *Comput Biol Med* | ⚠️ | DOI 불일치. 기재: `10.1016/S0010-4825(25)00055-1` (404). 실제: `10.1016/j.compbiomed.2025.109705` | DOI 수정, 저자 "Masuda et al." 추가 |
| 31 | Menstrual cycle vital sign, *F&S Reviews* | ⚠️ | DOI 불일치. 기재: `10.1016/S2666-5719(24)00038-0` (404). 실제: `10.1016/j.xfnr.2024.100081`. 저자: Rosen Vollmar et al. | DOI 수정, 저자 추가 |
| 36 | rPPG HRV 리뷰, 2024, *Front Bioeng Biotech* | ⚠️ | 논문 존재 추정되나 저자·DOI 미기재. 추정 DOI: 10.3389/fbioe.2024.1420100 | DOI·저자 보충 필요 |
| 32 | rPPG 종합 리뷰, 2025, PMC | ❓ | 저자·제목·DOI 미기재. 2025년 rPPG 리뷰 다수 존재하여 특정 불가 | 구체적 논문 정보 보충 필요 |
| 37 | 피부암 DL, 2023, *Diagnostics* | ❓ | 저자·제목·DOI 미기재. 해당 저널에 유사 주제 논문 다수 | 구체적 논문 정보 보충 필요 |
| 28 (menstrual wearable) | npj Women's Health, 2025 | ❓ | Kilungeja et al., 2025 DOI 확인됨. 본문 #33에 2개 DOI 나열 중 하나만 검증 | 두 번째 DOI(Comput Biol Med) 별도 검증 필요 |

---

## 검증 방법론 요약

1. **PMID 직접 조회** (16편): PubMed 페이지에서 제목·저자·저널·DOI 직접 대조
2. **DOI Crossref API** (12편): `api.crossref.org/works/{DOI}`에서 메타데이터 추출·대조
3. **WebSearch** (9편): Google Scholar/PubMed 검색으로 논문 존재 및 메타데이터 확인
4. **arXiv 검증** (1편): arXiv ID로 직접 확인

**신뢰도 순서**: PMID > DOI Crossref > WebSearch > 미기재(검증 불가)
