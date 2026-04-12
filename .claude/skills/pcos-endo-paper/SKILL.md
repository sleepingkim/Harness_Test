---
name: pcos-endo-paper
description: "PCOS·자궁내막증 스마트폰 카메라 바이오마커 연구 파이프라인 오케스트레이터. 문헌 탐색(K-Dense paper-lookup) → 할루시네이션 검증(reference-hallucination-guard) → 연구 합성(Harness100 research-designer) → IEEE LaTeX 논문(Harness100 paper-writer) 까지 실행. 'PCOS 논문', '자궁내막증 카메라 바이오마커', '스마트폰 여성건강 연구', 'PCOS endometriosis paper' 요청 시 이 스킬을 사용할 것."
---

# PCOS·Endometriosis Camera Paper — 파이프라인 오케스트레이터

스마트폰 카메라 기반 디지털 바이오마커로 PCOS·자궁내막증을 AI로 예측하는 연구의
전체 워크플로우를 에이전트 팀으로 조율한다.

## 팀 구성 및 활용 스킬

| 에이전트 | 역할 | 활용 외부 스킬 |
|---------|------|-------------|
| pcos-endo-camera-reviewer | 문헌 탐색 (3개 병렬 스테이지) | K-Dense: paper-lookup, literature-review / Skill3: sciomc 병렬 패턴 |
| (내장) reference-hallucination-guard | 참고문헌 할루시네이션 검증 | 기존 .claude/skills/ |
| pcos-endo-synthesizer | 연구 합성·설계서 작성 | Harness100: research-designer 패턴 / K-Dense: citation-management |
| pcos-endo-latex-writer | IEEE LaTeX 논문 작성 | Harness100: paper-writer(IMRaD), citation-standards(IEEE) / K-Dense: citation-management |

모든 에이전트: `model: "opus"` 사용

---

## Phase 0: 컨텍스트 확인

```bash
ls _workspace2/ 2>/dev/null && echo EXISTS || echo INIT
```

- **없음**: 초기 실행 → `mkdir -p _workspace2/ieee_paper` 후 Phase 1 전체 실행
- **있음 + 특정 단계 요청**:
  - "논문만 다시 써줘" → Phase 3만
  - "합성 보고서 수정해줘" → Phase 2 → 3
  - "할루시네이션 재검증" → Phase 1.5 → 2 → 3
- **있음 + 완전 새 실행**: `_workspace2/`를 `_workspace2_prev/`로 이동

---

## Phase 1: 문헌 탐색 (pcos-endo-camera-reviewer)

**sciomc 병렬 탐색 패턴 적용**: 3개 스테이지를 동시 실행하여 커버리지 확대

```
Agent(
  model: "opus",
  prompt: "
    당신은 pcos-endo-camera-reviewer 에이전트.
    [에이전트 정의 로드]
    
    sciomc 병렬 패턴으로 3개 탐색 스테이지를 실행:
    
    Stage 1 [HIGH]: rPPG·HRV → PCOS·자궁내막증 자율신경계 연계
    Stage 2 [HIGH]: 얼굴·피부 분석 → PCOS 표현형(다모증, 여드름) 탐지
    Stage 3 [MEDIUM]: 카메라 기반 융합 바이오마커 가능성
    
    K-Dense paper-lookup REST API 사용:
    - PubMed eutils API
    - Semantic Scholar graph API
    - OpenAlex API
    - Crossref API (DOI 검증)
    
    PICO 프레임워크:
    P: PCOS 또는 자궁내막증 여성
    I: 스마트폰 카메라 기반 바이오마커
    C: 기존 임상 진단
    O: AI 예측 정확도
    
    참조 파일:
    - _workspace/스마트폰 카메라 기반 질병 예측 연구.docx
    - _workspace/camera/01_camera_literature_review.md (기존 탐색, 중복 최소화)
    - _workspace/01_literature_review.md (PCOS·자궁내막증 기존 연구)
    
    출력: _workspace2/01_literature_review.md
  "
)
```

완료 조건: `_workspace2/01_literature_review.md` 생성

---

## Phase 1.5: 할루시네이션 검증 (reference-hallucination-guard)

```
# reference-hallucination-guard 적용
검증 대상: _workspace2/01_literature_review.md

실행:
1. 모든 참고문헌 추출
2. DOI → doi.org 직접 접근 (Crossref API)
3. 제목+저자 → PubMed/Semantic Scholar WebSearch
4. 분류: ✅ / ⚠️ / ❓ / ❌
5. 보고서: _workspace2/reference_validation_report.md
6. 원본 파일에 인라인 기호 추가

❌ 처리: [UNVERIFIED] 태그 + Phase 2·3 제외 권고
```

완료 조건: `_workspace2/reference_validation_report.md` 생성

---

## Phase 2: 연구 합성 (pcos-endo-synthesizer)

**Harness100 research-designer 패턴 + K-Dense citation-management 적용**

```
Agent(
  model: "opus",
  prompt: "
    당신은 pcos-endo-synthesizer 에이전트.
    [에이전트 정의 로드]
    
    Harness100 research-designer 패턴으로:
    1. 연구 질문 및 가설 수립 (H1~H5)
    2. PCOS·자궁내막증 특이적 바이오마커 Tier 분류
    3. 5차원 우선순위 매트릭스 적용
    
    K-Dense citation-management로:
    - CrossRef API 호출하여 ✅ 항목 BibTeX 메타데이터 추출
    
    입력:
    - _workspace2/01_literature_review.md
    - _workspace2/reference_validation_report.md
    - _workspace/camera/02_camera_synthesis.md (기존 합성 참조)
    - _workspace/01_literature_review.md (PCOS·자궁내막증 연구)
    
    출력:
    - _workspace2/02_research_design.md (연구 설계서)
    - _workspace2/03_biomarker_synthesis.md (합성 보고서)
  "
)
```

완료 조건: `_workspace2/02_research_design.md` + `_workspace2/03_biomarker_synthesis.md` 생성

---

## Phase 3: IEEE LaTeX 논문 (pcos-endo-latex-writer)

**Harness100 paper-writer(IMRaD) + citation-standards(IEEE) + K-Dense citation-management 적용**

```
Agent(
  model: "opus",
  prompt: "
    당신은 pcos-endo-latex-writer 에이전트.
    [에이전트 정의 로드]
    
    Harness100 paper-writer IMRaD 구조:
    I. Introduction (진단 지연 문제 → 연구 공백 → contribution)
    II. Related Work (rPPG, 얼굴 분석, PCOS·자궁내막증 바이오마커)
    III. Proposed Framework (수집 프로토콜, AI 파이프라인)
    IV. Results & Discussion (Tier 분류, 메타 분석, 연구 기회)
    V. Conclusion
    
    Harness100 citation-standards IEEE 형식 엄수:
    [1], [2] 인용 / IEEEtran BibTeX
    
    K-Dense citation-management:
    CrossRef API로 BibTeX 최종 검증
    
    입력:
    - _workspace2/02_research_design.md
    - _workspace2/03_biomarker_synthesis.md
    - _workspace2/reference_validation_report.md
    - _workspace/camera/ieee_paper/main.tex (직전 논문 참조)
    - _workspace/camera/ieee_paper/references.bib (기존 BibTeX 재활용)
    
    논문 차별화:
    - 질환 특이적 (PCOS·자궁내막증 집중)
    - 진단 지연 7-10년 문제 강조
    - 여성 건강 형평성 관점
    - 실제 수집 프로토콜 포함
    
    출력:
    - _workspace2/ieee_paper/main.tex
    - _workspace2/ieee_paper/references.bib
    - _workspace2/ieee_paper/README.md
  "
)
```

완료 조건:
- `_workspace2/ieee_paper/main.tex` 생성
- `_workspace2/ieee_paper/references.bib` 생성

---

## 최종 산출물 구조

```
_workspace2/
├── 01_literature_review.md          — PCOS·자궁내막증 카메라 바이오마커 문헌 탐색
│                                      (K-Dense paper-lookup API 기반, sciomc 3개 스테이지)
├── reference_validation_report.md   — 참고문헌 할루시네이션 검증
├── 02_research_design.md            — 연구 설계서 (Harness100 research-designer 패턴)
├── 03_biomarker_synthesis.md        — 바이오마커 합성 + Tier 분류
└── ieee_paper/
    ├── main.tex                     — IEEE LaTeX 논문 (Harness100 paper-writer IMRaD)
    ├── references.bib               — BibTeX (K-Dense citation-management 검증)
    └── README.md                    — 컴파일 안내
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| paper-lookup API 응답 없음 | WebSearch 대체, [API 불가] 표기 |
| Phase 1.5 검증 불가 | ❓ 처리 후 진행 |
| CrossRef API 실패 | 기존 BibTeX 정보 활용, [수동 확인 필요] 표기 |
| ❌ 비율 > 30% | 사용자에게 보고 후 진행 여부 확인 |
| Phase 3 LaTeX 오류 | pcos-endo-latex-writer 1회 재실행 |

---

## 직전 연구 대비 차별점

| 항목 | _workspace/camera/ (이전) | _workspace2/ (이번) |
|------|--------------------------|---------------------|
| 연구 범위 | 범용 질환 리뷰 | PCOS·자궁내막증 특화 |
| 문헌 탐색 | WebSearch 기반 | K-Dense paper-lookup REST API |
| 병렬 탐색 | 없음 | sciomc 3개 스테이지 병렬 |
| 연구 설계 | 없음 | Harness100 research-designer |
| 논문 구조 | 직접 작성 | Harness100 paper-writer IMRaD |
| 인용 검증 | WebSearch | CrossRef API + citation-management |
