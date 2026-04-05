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

**변경 이력:**

| 날짜 | 변경 내용 | 대상 | 사유 |
|------|----------|------|------|
| 2026-04-06 | 초기 구성 | 전체 | 공동연구 데이터 제안서 작성 목적으로 하네스 신규 구축 |
