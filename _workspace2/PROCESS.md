# _workspace2 연구 프로세스 문서

이 폴더에서 수행된 연구 과정을 기록한 문서입니다.

---

## 프로젝트 개요

**연구 주제**: 스마트폰 카메라 기반 디지털 바이오마커를 활용한 PCOS·자궁내막증 AI 예측 — 멀티모달 프레임워크 제안  
**수행 일자**: 2026-04-12  
**_workspace 대비 차별점**: 질환 특화(PCOS·자궁내막증), 외부 스킬 컬렉션(Skill1/2/3) 통합 활용, REST API 기반 문헌 탐색, Harness100 IMRaD 논문 구조

---

## 파이프라인

```
Phase 0    디렉토리 준비                  → _workspace2/ + ieee_paper/ 생성
Phase 1    pcos-endo-camera-reviewer      → 01_literature_review.md
           (K-Dense paper-lookup REST API + sciomc 3개 병렬 스테이지)
Phase 1.5  reference-hallucination-guard  → reference_validation_report.md
Phase 2    pcos-endo-synthesizer          → 02_research_design.md
           (Harness100 research-designer  → 03_biomarker_synthesis.md
            + K-Dense citation-management)
Phase 3    pcos-endo-latex-writer         → ieee_paper/main.tex
           (Harness100 paper-writer IMRaD → ieee_paper/references.bib
            + citation-standards IEEE     → ieee_paper/README.md
            + K-Dense citation-management)
```

---

## 활용 외부 스킬 매핑

| 단계 | 에이전트 | 활용 스킬 | 출처 |
|------|---------|---------|------|
| Phase 1 | pcos-endo-camera-reviewer | `paper-lookup` (PubMed/Semantic Scholar/OpenAlex REST API) | **Skill1 K-Dense** |
| Phase 1 | pcos-endo-camera-reviewer | `literature-review` (PICO·PRISMA 프로토콜) | **Skill1 K-Dense** |
| Phase 1 | pcos-endo-camera-reviewer | `sciomc` 병렬 탐색 패턴 (3개 스테이지 동시 실행) | **Skill3 oh-my-claudecode** |
| Phase 1.5 | (내장) | `reference-hallucination-guard` | 기존 `.claude/skills/` |
| Phase 2 | pcos-endo-synthesizer | `research-designer` 패턴 (연구 질문·가설·PICO) | **Skill2 Harness100** (98-academic-paper) |
| Phase 2 | pcos-endo-synthesizer | `citation-management` (CrossRef API BibTeX 추출) | **Skill1 K-Dense** |
| Phase 3 | pcos-endo-latex-writer | `paper-writer` (IMRaD 구조) | **Skill2 Harness100** (98-academic-paper) |
| Phase 3 | pcos-endo-latex-writer | `citation-standards` (IEEE 형식) | **Skill2 Harness100** (98-academic-paper) |
| Phase 3 | pcos-endo-latex-writer | `citation-management` (CrossRef API 최종 검증) | **Skill1 K-Dense** |

---

## 산출물 요약

| 파일 | 내용 |
|------|------|
| `01_literature_review.md` | PCOS·자궁내막증 스마트폰 카메라 바이오마커 문헌 탐색. PICO 프레임워크 + PRISMA 흐름. PubMed API(10쿼리, 22 PMID), OpenAlex API(2쿼리, 4편) 직접 호출. 총 37개 논문. Stage별 분류: rPPG·HRV(Stage 1), 얼굴·피부 분석(Stage 2), 융합 바이오마커(Stage 3). 연구 가설 H1~H5 도출 |
| `reference_validation_report.md` | 37개 참고문헌 할루시네이션 검증. ✅ 28개(75.7%) / ⚠️ 4개 / ❓ 3개 / ❌ 2개. 주요 탐지: #19 Jiang et al. BMI(저자 완전 불일치→실제 Yousaf et al.), #28 Rahmawati PCOS ML(저자 불일치→실제 Agirsoy et al.), #22 Dark circle AI(2025년 10월 철회된 논문) |
| `02_research_design.md` | Harness100 research-designer 패턴 적용 연구 설계서. Primary RQ + Secondary RQs 3개. 가설 H1~H5(측정 가능한 형태). 전향적 다기관 코호트 3단계(파일럿 150명→검증 600명→외부 검증 300명). 멀티모달 AI 아키텍처: rPPG-HRV(1D-CNN/Transformer) + 얼굴 피부(EfficientNet-B0) + 월경 패턴(LSTM/TCN) → Cross-Attention Fusion → 3-class 분류. Privacy-by-Design(온디바이스 처리) |
| `03_biomarker_synthesis.md` | Harness100 statistical-analyst 패턴 + CrossRef API BibTeX. Tier 1(4개): rPPG-HRV, 월경주기 HRV 패턴, 여드름 IGA, 다모증 mFG. Tier 2(6개): ANcam, 얼굴 BMI, rPPG 혈압/SpO2, 비접촉 월경 분류, 피부 병변. Tier 3(5개): 피부색 시계열 등. BibTeX 28건 포함 |
| `ieee_paper/main.tex` | IEEE conference LaTeX 논문 (IEEEtran). 제목: "Smartphone Camera-Based Multimodal Biomarker Framework for AI-Driven Prediction of PCOS and Endometriosis". 266줄, 6섹션(I~VI), TABLE I~III(booktabs), 27개 \cite{}, Abstract 212단어. Harness100 paper-writer IMRaD 구조 적용 |
| `ieee_paper/references.bib` | BibTeX 31개. ✅ 항목만 포함. ❌(#19/#28/#22) 완전 제외. 저자 교정 완료. CrossRef API 기반 메타데이터. `_workspace/camera/ieee_paper/references.bib`의 공통 항목 재활용 |
| `ieee_paper/README.md` | 컴파일 방법: `pdflatex main.tex && bibtex main && pdflatex main.tex` |

---

## _workspace/camera 논문 대비 차별화

| 항목 | `_workspace/camera/` (범용) | `_workspace2/` (질환 특화) |
|------|---------------------------|--------------------------|
| 연구 범위 | 스마트폰 카메라 기반 모든 질환 리뷰 | PCOS·자궁내막증 두 질환 집중 |
| 문헌 탐색 | WebSearch 기반 | **K-Dense paper-lookup REST API** (PubMed/OpenAlex 직접 호출) |
| 탐색 구조 | 단일 탐색 | **sciomc 3개 병렬 스테이지** (자율신경계/얼굴표현형/융합) |
| 연구 설계 | 없음 | **Harness100 research-designer** (가설, 코호트 프로토콜) |
| AI 아키텍처 | 설명 없음 | **Cross-Attention Fusion 멀티모달** 구체적 제안 |
| 논문 구조 | 직접 작성 | **Harness100 paper-writer IMRaD** 패턴 |
| 인용 검증 | WebSearch | **CrossRef API + citation-management** |
| 핵심 서사 | 기술 분류 중심 | **진단 7-10년 지연 + 여성 건강 형평성** |

---

## 에이전트 구성 위치

```
.claude/
├── agents/
│   ├── pcos-endo-camera-reviewer.md    (Phase 1 — K-Dense + sciomc 패턴)
│   ├── pcos-endo-synthesizer.md        (Phase 2 — Harness100 + K-Dense)
│   └── pcos-endo-latex-writer.md       (Phase 3 — Harness100 + K-Dense)
└── skills/
    ├── pcos-endo-paper/SKILL.md              (전체 오케스트레이터)
    └── reference-hallucination-guard/SKILL.md (범용 인용 검증, 재사용)
```

---

## 재실행 방법

```
# 전체 파이프라인 재실행
"PCOS 논문 파이프라인 실행해줘"
또는
"자궁내막증 카메라 바이오마커 연구 실행해줘"

# 특정 단계만 재실행
"논문만 다시 써줘"            → Phase 3만
"합성 보고서 수정해줘"        → Phase 2 → 3
"할루시네이션 재검증해줘"     → Phase 1.5 → 2 → 3

# 참고문헌 검증 단독 실행
/reference-hallucination-guard _workspace2/01_literature_review.md
```

---

## 참고 자료 경로

| 자료 | 경로 |
|------|------|
| 스마트폰 카메라 기반 질병 예측 연구 참고자료 | `_workspace/스마트폰 카메라 기반 질병 예측 연구.docx` |
| 범용 카메라 바이오마커 논문 (직전) | `_workspace/camera/ieee_paper/main.tex` |
| PCOS·자궁내막증 기존 바이오마커 연구 | `_workspace/01_literature_review.md` |
| K-Dense 스킬 컬렉션 | `Skill1_K-Dense/claude-scientific-skills/scientific-skills/` |
| Harness100 한국어 하네스 | `Skill2_Harness100/harness-100/ko/` |
| oh-my-claudecode 스킬 | `Skill3_oh-my-claudecode/oh-my-claudecode/skills/` |
