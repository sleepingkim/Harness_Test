# _workspace 연구 프로세스 문서

이 폴더에서 수행된 연구 과정을 기록한 문서입니다.

---

## 프로젝트 개요

**연구 1**: 자궁내막증·PCOS 디지털 바이오마커 탐색 → 공동연구 데이터 제안서  
**연구 2**: 스마트폰 카메라 기반 디지털 바이오마커 → AI 질병 예측 (범용) → IEEE LaTeX 논문  
**수행 일자**: 2026-04-06 ~ 2026-04-11  
**사용 에이전트**: 모두 `model: opus`

---

## 연구 1: 자궁내막증·PCOS 디지털 바이오마커 연구

### 파이프라인
```
Phase 1  literature-reviewer        → 01_literature_review.md
Phase 2a biomarker-synthesizer      → 02_biomarker_catalog.md
Phase 2b novel-biomarker-proposer   → 03_novel_proposals.md
Phase 3  data-proposal-writer       → 04_data_proposal.md
                                    → 디지털_바이오마커_공동연구_제안서.docx
```

### 사용 스킬
| 스킬 | 위치 | 역할 |
|------|------|------|
| `biomarker-research` | `.claude/skills/biomarker-research/` | 전체 파이프라인 오케스트레이터 |

### 산출물 요약
| 파일 | 내용 |
|------|------|
| `01_literature_review.md` | 자궁내막증·PCOS 디지털 바이오마커 문헌 탐색. 웹 기반 학술 검색(PubMed, Nature, Frontiers 등). 자궁내막증 7개, PCOS 7개, 공통 5개 바이오마커 정리. 증거 수준 평가 포함 |
| `02_biomarker_catalog.md` | Known 바이오마커 분류·평가·우선순위 카탈로그. Layer별(생리추적 앱, 웨어러블, 임상) 분류 |
| `03_novel_proposals.md` | 병태생리학 기반 신규 바이오마커 제안. 데이터 갭 분석 기반 |
| `04_data_proposal.md` | 데이터 제공 업체 대상 공동연구 제안서 (한국어) |
| `디지털_바이오마커_공동연구_제안서.docx` | 04_data_proposal.md의 Word 형식 버전 |

---

## 연구 2: 스마트폰 카메라 기반 범용 질병 예측 — IEEE 논문

### 파이프라인
```
Phase 0    디렉토리 준비             → _workspace/camera/ 생성
Phase 1    camera-biomarker-reviewer → camera/01_camera_literature_review.md
Phase 1.5  reference-hallucination-guard → camera/reference_validation_report.md
Phase 2    camera-biomarker-synthesizer  → camera/02_camera_synthesis.md
                                         → camera/스마트폰_카메라_바이오마커_합성보고서.docx
Phase 3    ieee-paper-writer         → camera/ieee_paper/main.tex
                                     → camera/ieee_paper/references.bib
                                     → camera/ieee_paper/README.md
```

### 사용 스킬
| 스킬 | 위치 | 역할 |
|------|------|------|
| `camera-biomarker-paper` | `.claude/skills/camera-biomarker-paper/` | 전체 파이프라인 오케스트레이터 |
| `reference-hallucination-guard` | `.claude/skills/reference-hallucination-guard/` | 참고문헌 실존 여부 검증 (범용) |

### 외부 스킬 활용
이 연구에서는 Skill1/2/3 외부 컬렉션 스킬을 **활용하지 않음**.  
에이전트 정의와 스킬은 모두 `.claude/` 내부에서 새로 구성.

### 산출물 요약 (`camera/` 하위)
| 파일 | 내용 |
|------|------|
| `01_camera_literature_review.md` | 스마트폰 카메라 기반 바이오마커 문헌 탐색. 19회 웹 검색 + 10회 이상 WebFetch 직접 확인. 총 42개 논문 정리. rPPG(10건), 얼굴/피부(10건), 안구(7건), 동작(5건), 정신건강(5건) |
| `reference_validation_report.md` | 42개 참고문헌 할루시네이션 검증 결과. ✅ 30개(71.4%) / ⚠️ 8개 / ❓ 2개 / ❌ 2개. 할루시네이션 탐지: PMC11854623 빈혈 ViT(모델·수치 불일치), JMIR e58187 OSA(내용 완전 불일치) |
| `02_camera_synthesis.md` | Tier 1(5개) / Tier 2(13개) / Tier 3(11개) 우선순위 분류. 5차원 매트릭스. Tier 1 상위: rPPG 심박수(23점), FibriCheck AF(22점) |
| `스마트폰_카메라_바이오마커_합성보고서.docx` | 02_camera_synthesis.md의 Word 형식 버전 (pandoc 생성) |
| `ieee_paper/main.tex` | IEEE conference LaTeX 논문 (IEEEtran). 제목: "Smartphone Camera-Based Digital Biomarker Collection for AI-Driven Disease Prediction: A Systematic Review and Tiered Evaluation Framework". 300줄, 6섹션, TABLE I~III, 34개 인용 |
| `ieee_paper/references.bib` | BibTeX 34개. ✅ 항목만 포함. ❌ 2개 제외 |
| `ieee_paper/README.md` | 컴파일 방법: `pdflatex main.tex && bibtex main && pdflatex main.tex` |

### 주요 발견
- 스마트폰 카메라 기반 바이오마커 중 **Tier 1** (즉시 활용 가능): rPPG 심박수, FibriCheck AF 탐지(FDA 다기관 검증), 당뇨망막병증 안저 분석, BiliSG 황달, rPPG SpO2
- **여성 건강 연구 공백**: 스마트폰 카메라 × 자궁내막증·PCOS = 전무 → 논문의 핵심 contribution으로 포함
- **할루시네이션 2건 탐지 및 제거**

---

## 에이전트 구성 위치

```
.claude/
├── agents/
│   ├── literature-reviewer.md          (연구 1)
│   ├── biomarker-synthesizer.md        (연구 1)
│   ├── novel-biomarker-proposer.md     (연구 1)
│   ├── data-proposal-writer.md         (연구 1)
│   ├── camera-biomarker-reviewer.md    (연구 2)
│   ├── camera-biomarker-synthesizer.md (연구 2)
│   └── ieee-paper-writer.md            (연구 2)
└── skills/
    ├── biomarker-research/SKILL.md           (연구 1 오케스트레이터)
    ├── camera-biomarker-paper/SKILL.md       (연구 2 오케스트레이터)
    └── reference-hallucination-guard/SKILL.md (범용 인용 검증)
```

---

## 재실행 방법

```
# 연구 1 전체 재실행
"바이오마커 연구 파이프라인 실행해줘"

# 연구 2 전체 재실행
"스마트폰 카메라 바이오마커 연구 파이프라인 실행해줘"

# 논문만 재작성
"논문만 다시 써줘"

# 할루시네이션 재검증
/reference-hallucination-guard _workspace/camera/01_camera_literature_review.md
```
