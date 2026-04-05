---
name: biomarker-research
description: "자궁내막증/PCOS 디지털 바이오마커 연구 오케스트레이터. 문헌 탐색 → 바이오마커 합성 → 신규 제안 → 데이터 제안서 작성까지 전체 파이프라인을 에이전트 팀으로 실행. '바이오마커 연구', '데이터 제안서 작성', '디지털 바이오마커 탐색', '자궁내막증/PCOS 연구', '공동연구 제안', '바이오마커 제안서', '다시 실행', '제안서 업데이트', '바이오마커 추가' 등의 요청 시 이 스킬을 사용할 것."
---

# Biomarker Research Orchestrator

자궁내막증(Endometriosis)과 PCOS 예측을 위한 디지털 바이오마커 연구의 전체 워크플로우를 조율한다.

## 팀 구성

| 에이전트 | 역할 | 실행 방식 |
|---------|------|---------|
| literature-reviewer | 선행연구 체계적 탐색 | 서브 에이전트 (Phase 1) |
| biomarker-synthesizer | Known 바이오마커 합성·평가 | 에이전트 팀 (Phase 2) |
| novel-biomarker-proposer | 신규 바이오마커 제안 | 에이전트 팀 (Phase 2) |
| data-proposal-writer | 공동연구 데이터 제안서 작성 | 서브 에이전트 (Phase 3) |

**아키텍처**: 파이프라인 + 팬아웃
`Phase 1 (단독)` → `Phase 2 (팬아웃: 두 에이전트 병렬)` → `Phase 3 (단독)`

모든 에이전트는 `model: "opus"` 사용.

---

## Phase 0: 컨텍스트 확인

실행 전 `_workspace/` 존재 여부를 확인한다:

- `_workspace/` **없음** → 초기 실행 (Phase 1부터 전체 실행)
- `_workspace/` **있음 + 특정 산출물 수정 요청** → 해당 Phase만 재실행
  - "제안서만 다시 써줘" → Phase 3만 실행 (기존 01~03 파일 활용)
  - "신규 마커 보완해줘" → Phase 2의 novel-proposer만 재실행 → Phase 3 재실행
- `_workspace/` **있음 + 완전 새 실행 요청** → 기존 `_workspace/`를 `_workspace_prev/`로 이동 후 새 실행

---

## Phase 1: 문헌 탐색 (literature-reviewer)

```
Agent(
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "[literature-reviewer 에이전트 정의 로드]
           연구 맥락: 자궁내막증/PCOS AI 예측을 위한 디지털 바이오마커 탐색.
           공동연구 목적의 데이터 제안서 작성이 최종 목표.
           _workspace/ 디렉토리 생성 후 01_literature_review.md 작성."
)
```

완료 조건: `_workspace/01_literature_review.md` 생성 확인

---

## Phase 2: 병렬 분석 (에이전트 팀)

Phase 1 완료 후 팀 구성:

```
TeamCreate(
  team_name: "biomarker-analysis-team",
  members: [
    {
      name: "biomarker-synthesizer",
      prompt: "[biomarker-synthesizer 에이전트 정의 로드]
               _workspace/01_literature_review.md를 읽고
               Known 바이오마커 카탈로그 작성.
               novel-biomarker-proposer와 SendMessage로 소통하며
               Known/Novel 경계 조율."
    },
    {
      name: "novel-biomarker-proposer",
      prompt: "[novel-biomarker-proposer 에이전트 정의 로드]
               _workspace/01_literature_review.md의 데이터 갭 섹션을 참고하여
               신규 바이오마커 제안.
               biomarker-synthesizer와 SendMessage로 중복 확인."
    }
  ]
)

TaskCreate(tasks: [
  { title: "Known 바이오마커 카탈로그 작성", assignee: "biomarker-synthesizer" },
  { title: "신규 바이오마커 제안서 작성", assignee: "novel-biomarker-proposer" }
])
```

완료 조건: `_workspace/02_biomarker_catalog.md` + `_workspace/03_novel_proposals.md` 생성 확인

팀 정리 후 Phase 3 진행.

---

## Phase 3: 제안서 작성 (data-proposal-writer)

```
Agent(
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "[data-proposal-writer 에이전트 정의 로드]
           _workspace/의 01~03 파일을 모두 읽고
           공동연구 데이터 제안서(04_data_proposal.md) 작성.
           언어: 한국어."
)
```

완료 조건: `_workspace/04_data_proposal.md` 생성 확인

---

## 산출물

```
_workspace/
├── 01_literature_review.md      — 문헌 탐색 결과 (바이오마커별 근거)
├── 02_biomarker_catalog.md      — Known 바이오마커 카탈로그 + 우선순위
├── 03_novel_proposals.md        — 신규 제안 바이오마커
└── 04_data_proposal.md          — 데이터 제공 업체 제안서 (최종 산출물)
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| Phase 1 산출물 미생성 | literature-reviewer 1회 재실행. 재실패 시 지식 기반으로 대체하고 [지식 기반] 명시 |
| Phase 2 에이전트 중 1개 실패 | 완료된 에이전트 산출물만으로 Phase 3 진행, 보고서에 누락 명시 |
| Phase 2 두 에이전트 간 마커 중복 | biomarker-synthesizer 카탈로그에 [Novel] 태그로 통합, 중복 항목 삭제 |
| Phase 3 산출물 미생성 | data-proposal-writer 1회 재실행 |

---

## 테스트 시나리오

**정상 흐름:**
- 입력: "자궁내막증과 PCOS AI 예측 연구를 위한 데이터 제안서 작성해줘"
- 기대 출력: `_workspace/` 내 4개 파일 순차 생성, 한국어 제안서 완성

**에러 흐름:**
- Phase 2에서 novel-proposer만 실패 시 → `02_biomarker_catalog.md` 기반으로 제안서 작성 진행, 03 누락 명시

**후속 작업:**
- "신규 마커 보완해줘" → Phase 2 novel-proposer 재실행 → Phase 3 재실행
- "제안서 영어로도 작성해줘" → data-proposal-writer에게 영어 버전 추가 요청
