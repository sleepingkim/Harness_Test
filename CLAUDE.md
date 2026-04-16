# 자궁내막증/PCOS 디지털 바이오마커 연구 프로젝트

AI 연구원의 공동연구 프로젝트. 자궁내막증(Endometriosis)과 다낭성난소증후군(PCOS)을 AI로 예측하기 위한 유의미한 디지털 바이오마커를 발굴하고, 데이터 제공 업체에게 공동연구를 제안하는 것이 현재 목표.

---

## 하네스: 디지털 바이오마커 연구

**목표:** 문헌 기반 Known 바이오마커 탐색 + 신규 바이오마커 제안 → 공동연구 데이터 제안서 작성

**에이전트 팀:**

| 에이전트 | 역할 |
|---------|------|
| literature-reviewer | 자궁내막증/PCOS 디지털 바이오마커 선행연구 체계적 탐색 |
| biomarker-synthesizer | Known 바이오마커 분류·평가·우선순위 카탈로그 작성 |
| novel-biomarker-proposer | 병태생리학 기반 신규 바이오마커 제안 |
| data-proposal-writer | 공동연구 데이터 제안서 작성 (한국어) |

**스킬:**

| 스킬 | 용도 | 사용 에이전트 |
|------|------|-------------|
| biomarker-research | 전체 파이프라인 오케스트레이터 | 전체 팀 조율 |

**실행 규칙:**
- 바이오마커 탐색, 데이터 제안서, 신규 마커 제안 등 연구 관련 작업 요청 시 `biomarker-research` 스킬을 통해 에이전트 팀으로 처리
- 단순 질문/개념 설명은 에이전트 팀 없이 직접 응답
- 모든 에이전트는 `model: "opus"` 사용
- 중간 산출물: `_workspace/` 디렉토리

**디렉토리 구조:**
```
.claude/
├── agents/
│   ├── literature-reviewer.md
│   ├── biomarker-synthesizer.md
│   ├── novel-biomarker-proposer.md
│   └── data-proposal-writer.md
└── skills/
    └── biomarker-research/
        └── SKILL.md
```

---

## 하네스: 스마트폰 카메라 바이오마커 연구 + IEEE 논문

**목표:** 스마트폰 카메라 기반 일상 디지털 바이오마커 수집 → AI 질병 예측 연구 탐색 → IEEE LaTeX 논문 작성

**에이전트 팀:**

| 에이전트 | 역할 |
|---------|------|
| camera-biomarker-reviewer | 스마트폰 카메라 기반 바이오마커 문헌 탐색 (rPPG, 얼굴 분석, 안구 추적 등) |
| camera-biomarker-synthesizer | 탐색 결과 합성·분류·평가, .md + .docx 저장 |
| ieee-paper-writer | IEEE 표준 LaTeX 형식 논문 작성 (main.tex + references.bib) |

**스킬:**

| 스킬 | 용도 |
|------|------|
| camera-biomarker-paper | 전체 파이프라인 오케스트레이터 (문헌 탐색 → 검증 → 합성 → 논문) |
| reference-hallucination-guard | 참고문헌 실존 여부 검증, 할루시네이션 탐지 (범용 스킬, 어느 연구에도 적용 가능) |

**실행 규칙:**
- 스마트폰 카메라 바이오마커 연구, IEEE 논문 작성 요청 시 `camera-biomarker-paper` 스킬 사용
- 참고문헌 검증 요청 시 `reference-hallucination-guard` 스킬 단독 사용 가능
- 모든 에이전트는 `model: "opus"` 사용
- 중간 산출물: `_workspace/camera/` 디렉토리

**파이프라인:**
```
Phase 1: camera-biomarker-reviewer → 01_camera_literature_review.md
Phase 1.5: reference-hallucination-guard → reference_validation_report.md
Phase 2: camera-biomarker-synthesizer → 02_camera_synthesis.md + .docx
Phase 3: ieee-paper-writer → ieee_paper/main.tex + references.bib
```

**디렉토리 구조:**
```
.claude/
├── agents/
│   ├── camera-biomarker-reviewer.md
│   ├── camera-biomarker-synthesizer.md
│   └── ieee-paper-writer.md
└── skills/
    ├── camera-biomarker-paper/SKILL.md
    └── reference-hallucination-guard/SKILL.md

_workspace/camera/
├── 01_camera_literature_review.md
├── reference_validation_report.md
├── 02_camera_synthesis.md
├── 스마트폰_카메라_바이오마커_합성보고서.docx
└── ieee_paper/
    ├── main.tex
    ├── references.bib
    └── README.md
```

---

## 하네스: 축구 영상 선수 식별 연구 (YoungScientist)

**목표:** 단일 카메라 축구 영상에서 선수 탐지·추적·등번호 인식 성능 개선, 특히 가림(occlusion) 상황 해결

**에이전트 팀:**

| 에이전트 | 역할 |
|---------|------|
| soccer-vision-reviewer | 선수 탐지·추적·등번호 인식·가림 처리 선행연구 체계적 탐색 |
| method-analyzer | 핵심 기법 심층 분석, 기법 비교·조합 가능성 평가 |
| research-designer | 문제 정의, 연구 설계, 실험 계획 수립 |

**스킬:**

| 스킬 | 용도 |
|------|------|
| soccer-tracking-research | 전체 파이프라인 오케스트레이터 (문헌 탐색 → 검증 → 기법 분석 → 연구 설계) |

**활용 외부 스킬:**

| 외부 스킬 | 출처 | 적용 에이전트 |
|----------|------|-------------|
| paper-lookup (REST API) | Skill1_K-Dense | soccer-vision-reviewer |
| sciomc 병렬 탐색 패턴 | Skill3_oh-my-claudecode | soccer-vision-reviewer |
| reference-hallucination-guard | Skill3 (설치됨) | Phase 1.5 내장 |
| citation-management | Skill1_K-Dense | method-analyzer, research-designer |
| research-designer 패턴 | Skill2_Harness100 | research-designer |
| paper-writer IMRaD 패턴 | Skill2_Harness100 | research-designer |
| statistical-analyst 패턴 | Skill2_Harness100 | method-analyzer |

**실행 규칙:**
- 축구 선수 추적, 가림 처리, 등번호 인식 등 관련 연구 작업 요청 시 `soccer-tracking-research` 스킬 사용
- 단순 질문/개념 설명은 에이전트 팀 없이 직접 응답
- 모든 에이전트는 `model: "opus"` 사용
- 중간 산출물: `YoungScientist/_workspace/` 디렉토리

**파이프라인:**
```
Phase 1: soccer-vision-reviewer → 01_literature_review.md (K-Dense API + sciomc 4-stage 병렬)
Phase 1.5: reference-hallucination-guard → reference_validation_report.md
Phase 2: method-analyzer → 02_method_analysis.md (citation-management + statistical-analyst)
Phase 3: research-designer → 03_research_design.md (research-designer + IMRaD 패턴)
```

**디렉토리 구조:**
```
.claude/
├── agents/
│   ├── soccer-vision-reviewer.md
│   ├── method-analyzer.md
│   └── research-designer.md
└── skills/
    └── soccer-tracking-research/
        └── SKILL.md

YoungScientist/_workspace/
├── 01_literature_review.md          — 문헌 탐색 보고서 (검증 기호 포함)
├── reference_validation_report.md   — 참고문헌 할루시네이션 검증
├── 02_method_analysis.md            — 기법 심층 분석 보고서
└── 03_research_design.md            — 연구 설계서
```

---

**변경 이력:**

| 날짜 | 변경 내용 | 대상 | 사유 |
|------|----------|------|------|
| 2026-04-06 | 초기 구성 | 전체 | 공동연구 데이터 제안서 작성 목적으로 하네스 신규 구축 |
| 2026-04-11 | 카메라 바이오마커 하네스 추가 | 에이전트 3개 + 스킬 2개 | 스마트폰 카메라 기반 질병 예측 연구 → IEEE 논문 작성 파이프라인 구축 |
| 2026-04-12 | PCOS·자궁내막증 특화 하네스 추가 | 에이전트 3개 + 스킬 1개 | Skill1/2/3 스킬 통합 활용, _workspace2/ 기반 질환 특화 IEEE 논문 파이프라인 |
| 2026-04-16 | 축구 영상 선수 식별 하네스 추가 | 에이전트 3개 + 스킬 1개 | 단일 카메라 축구 영상 선수 탐지·추적·등번호 인식 연구, YoungScientist/ 기반 |
