# 참고문헌 할루시네이션 검증 보고서 — 음성 바이오마커 (Phase 1b)

**검증 대상**: `_workspace3/02_voice_biomarker_literature.md`  
**검증 일자**: 2026-04-29  
**검증 방법**: WebSearch (Google Scholar, PubMed, Nature, ScienceDirect, MDPI, ISCA, KISTI ScienceON, KCI, DBpia, earticle, PMC) + 직접 URL 형식 확인  
**총 참고문헌**: 43편 (한국어 7편: #5, #6, #10, #19, #28, #29, #43)

---

## 검증 통계

| 등급 | 기호 | 건수 | 비율 |
|------|------|------|------|
| 검증됨 | ✅ | 31 | 72% |
| 부분 검증 (세부 불일치) | ⚠️ | 12 | 28% |
| 미확인 (접근 불가/검색 미확인) | ❓ | 0 | 0% |
| 할루시네이션 의심 | ❌ | 0 | 0% |

**전체 평가**: 할루시네이션 의심 항목 없음. 43편 전부 실존 논문·보고서 확인. ⚠️ 항목 12편은 주로 **제1저자명 오기** 패턴으로, LLM이 유사 주제의 다른 저자 이름을 혼용한 것으로 판단됨.

---

## 검증 결과 상세

### ✅ 검증됨 (31편)

| # | 참고문헌 | 검증 근거 | 비고 |
|---|---------|---------|------|
| 1 | Naranjo 2025, Sci Rep, PD voice | PubMed 40204799, nature.com URL 확인 | |
| 2 | Quan 2025, Sci Rep, PD CNN | PubMed 40025201, nature.com URL 확인 | |
| 4 | Karaman 2022, Healthcare Informatics Research, PMC9388925 | PubMed 35982595, PMC URL 확인 | 실제 교신저자는 Tougui |
| 5 | 김지환·이종민 2022, 한국음향학회지, ART002901862 | KCI URL 확인 (교차 검색에서 URL 노출) | |
| 6 | 2016, 한국멀티미디어학회, JAKO201615453186206 | koreascience.kr URL 직접 확인 | |
| 7 | Luz 2020, ADReSS Challenge, INTERSPEECH 2020 | ISCA Archive, arXiv 2004.06833 확인 | |
| 9 | 2026, Wav2Vec IJST, Springer | link.springer.com URL 확인 | 2026년 실제 출판 |
| 10 | SNU 2024, AD thesis, 10371/210811 | s-space.snu.ac.kr URL 직접 확인 | |
| 13 | Tu 2023, JASA Express Lett, 015201 | PubMed 36725533, pubs.aip.org 확인 | |
| 15 | Rusz 2020, Clin Neurophysiology, PubMed 32146096 | PubMed 32146096, ScienceDirect 확인 | 제1저자 Hlavnička; Rusz는 교신저자 |
| 19 | SNU 2022, 우울증·자살위험 thesis, 10371/183406 | s-space.snu.ac.kr URL 직접 확인 | |
| 20 | Voice of Mind 2025, J Voice, PubMed 40998607 | PubMed 40998607, ScienceDirect 확인 | |
| 21 | Faurholt-Jepsen 2016, Translational Psychiatry | PubMed 27434490, nature.com 확인 | |
| 24 | 2024, psychological stress speech, Healthcare Analytics, S2772671124002870 | ScienceDirect URL 확인 | |
| 26 | Orlandic 2021, COUGHVID, Scientific Data | PubMed 34162883, arXiv 2009.11644, nature.com 확인 | |
| 27 | Hamdi 2023, CovidCoughNet, PMC10249348 | PMC URL, ScienceDirect 확인 | |
| 28 | 한밭대 2022, 기침소리 COVID-19, DBpia T16613002 | dbpia.co.kr URL 직접 확인 | |
| 29 | EfficientNet 기침 소리 감지, earticle A409384 | earticle.net URL 직접 확인 | |
| 30 | Kim 2021, respiratory sounds, Sci Rep, s41598-021-96724-7 | PubMed 34433880, nature.com 확인 | |
| 31 | HeAR asthma, arXiv 2504.20124 | arXiv URL 확인 | |
| 32 | Wang 2022, OSA, Nature and Science of Sleep, NSS.S373367 | PubMed 36394068, tandfonline.com 확인 | |
| 33 | Aydin 2024, PCOS voice, Egyptian J Otolaryngology | link.springer.com URL 확인 | |
| 34 | Aydin 2010, PCOS vocal changes, J Voice, PubMed 20537860 | PubMed 20537860, ScienceDirect 확인 | |
| 35 | 2022, Voice changes reproductive/thyroid, Endocrine Connections, PMC8942322 | PubMed 35148272, PMC 확인 | |
| 37 | SVD voice pathology, MDPI 2021, 2076-3417/11/15/7149 | MDPI URL 직접 확인; Springer chapter도 확인 | |
| 38 | arXiv 2412.16267, laryngeal cancer benchmark | arXiv URL 확인 | |
| 39 | Kim 2020, laryngeal cancer CNN, PMC7692693 | PubMed 33113785, PMC 확인 | |
| 40 | 2024, laryngeal diseases, Sci Rep, s41598-024-58817-x | nature.com URL 확인 | |
| 41 | Maor 2020, Heart Failure, JAHA, JAHA.119.013359 | PubMed 32233754, ahajournals.org 확인 | |
| 42 | 2023, Infant Cry Diagnostics, PMC10297367 | PubMed 37371002, MDPI 확인 | |
| 43 | KISTI AcoustoSleepMask, TRKO202100015466 | scienceon.kisti.re.kr URL 직접 확인 | |

---

### ⚠️ 부분 검증 — 논문 실재하나 세부 정보 불일치 (12편)

| # | 참고문헌 | 불일치 내용 | 실제 정보 |
|---|---------|---------|---------|
| 3 | "Favaro, A. et al., 2025, Bioengineering 12(7):728" | **제1저자 오기**: 해당 URL(MDPI)의 실제 저자는 Sedigh Malekroodi, H. et al. "Favaro"는 유사 PD 음성 연구자로 혼동된 것으로 추정 | Sedigh Malekroodi, H., Madusanka, N., Lee, B.-i., Yi, M. (2025). Bioengineering 12(7):728. DOI 10.3390/bioengineering12070728 |
| 8 | "Pappagari, R. et al., 2021, Frontiers in Aging Neuroscience, fnagi.2021.623607" | **제1저자 오기**: DOI fnagi.2021.623607의 실제 저자는 Mahajan, P. & Baths, V. Pappagari는 ISCA 2020/2021 ADReSS 연구자로 별도 논문 존재 | Mahajan, P. & Baths, V. (2021). Front. Aging Neurosci. DOI 10.3389/fnagi.2021.623607. PubMed 33613269 |
| 11 | "Ortiz-Perez, D. et al., 2024, Sci Rep, s41598-024-64438-1" | **제1저자 오기**: 동일 URL의 실제 저자는 Lin, K. & Washington, P.Y. | Lin, K. & Washington, P.Y. (2024). Sci Rep 14:13887. DOI 10.1038/s41598-024-64438-1. PubMed 38880810 |
| 12 | "Stegmann, G. et al., 2025, npj Digital Medicine, s41746-025-01654-7" | **제1저자 오기**: 실제 제1저자는 Merler, M. & Agurto, C. (IBM Research). Stegmann은 공저자 |  Merler, M., Agurto, C. et al. (2025). npj Digit Med 8:260. PubMed 40341287 |
| 14 | "Velasco Garcia 2010, Journal of Voice, PubMed 20137889" | **연도 소기**: PMID 20137889의 실제 인쇄 출판은 J Voice 2011 Mar;25(2):208-17. 2010은 epub ahead-of-print 날짜 | 출판년도: 2011 (인쇄판); epub: 2010 |
| 16 | "Yang, X. et al., 2024, Sci Rep, s41598-024-63556-0" | **제1저자 오기**: 동일 URL의 실제 저자는 Huang, X., Wang, F., Gao, Y. et al. | Huang, X. et al. (2024). Sci Rep 14. DOI 10.1038/s41598-024-63556-0. PubMed 38830969 |
| 17 | "Bao, R. et al., 2024, JAMIA, 31(10):2394" | **제1저자 오기**: 동일 논문의 실제 저자는 Liu, M. et al. (JAMIA 2024 확인) | Liu, M. et al. (2024). JAMIA 31(10):2394-2404. Oxford Academic URL 확인 |
| 18 | "Lam, G. et al., 2023, JMIR, e34474" | **제1저자 오기**: 동일 논문(JMIR e34474)의 실제 저자는 Kim, A.Y., Jang, E.H., Lee, S.H. et al. | Kim, A.Y. et al. (2023). JMIR 25:e34474. PubMed 36696160 |
| 22 | "de Boer 2021, Psychol Med, 환자 86명+대조군 80명" | **연도 소기 + 피험자 수 오기**: 실제 인쇄 출판 2023 (Psychol Med 53(4):1302-1312); 2021은 epub ahead-of-print. 피험자 수: 환자 142명 + 대조군 142명 | de Boer, J.N. et al. (2023). Psychol Med 53(4):1302-1312. epub 2021-08-04. PubMed 34344490 |
| 23 | "2025, PMC12237691 (Schizophrenia Research)" | **저널명 오기**: 실제 게재 저널은 *NPP—Digital Psychiatry and Neuroscience* (Nature portfolio). "Schizophrenia Research"와 전혀 다른 저널 | NPP—Digital Psychiatry and Neuroscience (2025). PMC12237691. DOI 10.1038/s44277-025-00040-1 |
| 25 | "Sharma, N. et al., 2021, INTERSPEECH 2020 (arXiv 2005.10548)" | **연도 소기**: 연도 2021로 기재되나 INTERSPEECH 2020 proceedings는 2020년 출판. arXiv 게시 및 학회 발표 모두 2020 | Sharma, N. et al. (2020). INTERSPEECH 2020, pp.4811-4815. arXiv 2005.10548 (2020년 5월) |
| 36 | "Kaufman 2023, Mayo Clinic Proc Digital Health, 여성 Acc=89%, 남성 Acc=86%" | **성능 수치 과장**: 실제 논문 보고 최적 accuracy: 여성 0.75±0.22, 남성 0.70±0.10 (5-fold CV). 89%/86%는 위험요인 결합 최대치 오독 가능성 | Kaufman, J.M. et al. (2023). Mayo Clin Proc Digit Health. PMC11975753. 실제 성능 75%/70% 수준 |

---

## 불일치 유형 분류

| 유형 | 해당 논문 # | 건수 |
|------|-----------|------|
| 제1저자명 오기 | 3, 8, 11, 12, 16, 17, 18 | 7건 |
| 연도 소기 (epub vs. 인쇄판) | 14, 22, 25 | 3건 |
| 저널명 오기 | 23 | 1건 |
| 성능 수치 과장 / 피험자 수 오기 | 22, 36 | 2건 (중복 포함) |

> **주목할 패턴**: 제1저자명 오기 7건은 해당 분야의 유명 연구자 이름(Favaro, Pappagari 등)이 같은 주제의 다른 논문에 잘못 배정된 것으로, LLM의 연상 기반 생성 오류의 전형적 패턴. 논문 자체는 모두 실존하며 내용은 정확히 서술됨.

---

## 즉시 수정 권장 (⚠️ 항목)

### 저자명 수정 (7건)
1. **Paper #3**: "Favaro, A. et al." → "Sedigh Malekroodi, H. et al." (Bioengineering 12(7):728)
2. **Paper #8**: "Pappagari, R. et al." → "Mahajan, P. & Baths, V." (Frontiers fnagi.2021.623607)
3. **Paper #11**: "Ortiz-Perez, D. et al." → "Lin, K. & Washington, P.Y." (Sci Rep s41598-024-64438-1)
4. **Paper #12**: "Stegmann, G. et al." → "Merler, M., Agurto, C. et al." (npj Digit Med s41746-025-01654-7)
5. **Paper #16**: "Yang, X. et al." → "Huang, X. et al." (Sci Rep s41598-024-63556-0)
6. **Paper #17**: "Bao, R. et al." → "Liu, M. et al." (JAMIA 31(10):2394)
7. **Paper #18**: "Lam, G. et al." → "Kim, A.Y. et al." (JMIR e34474)

### 연도 수정 (3건)
8. **Paper #14**: 연도 2010 → 2011 (J Voice 인쇄판 기준)
9. **Paper #22**: 연도 2021 → 2023 (Psychol Med 인쇄 권호 기준); 피험자 수 86+80 → 142+142
10. **Paper #25**: 연도 2021 → 2020 (INTERSPEECH 2020 기준)

### 저널명 수정 (1건)
11. **Paper #23**: "Schizophrenia Research" → "NPP—Digital Psychiatry and Neuroscience"

### 성능 수치 수정 (1건)
12. **Paper #36**: "여성 Acc=89%, 남성 Acc=86%" → "여성 Acc=75%, 남성 Acc=70%" (5-fold CV)

---

## 종합 신뢰도 평가

| 항목 | 건수 | 비율 |
|------|------|------|
| Phase 2 및 Excel 정리에 활용 적합 (✅) | 31편 | 72% |
| 저자/연도/저널 수정 후 활용 (⚠️) | 12편 | 28% |
| 제외 권장 (❌) | 0편 | 0% |

**결론**: 43편 전부 실존하는 논문/보고서임이 확인됨. 할루시네이션은 없으나 저자명 오기가 7건으로 많음. 이는 Phase 2 Excel 정리 및 논문 작성 시 반드시 수정 필요.

---

## 인라인 기호 범례
- ✅ : DOI/URL/PubMed 직접 확인됨
- ⚠️ : 논문 실재하나 저자·저널·연도·수치 불일치
- ❓ : 검증 미수행 (해당 없음)
- ❌ : 할루시네이션 의심 (해당 없음)
