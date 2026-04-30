---
name: ux-methodology-research
description: "얼굴·음성 데이터 수집 UX 방법론 연구 파이프라인 오케스트레이터. 문헌 탐색 → 할루시네이션 검증 → 합성 보고서 작성. '데이터 수집 UX', '얼굴 음성 수집 방법론', 'mHealth UX' 요청 시 이 스킬을 사용할 것."
---

# UX Methodology Research — 파이프라인 오케스트레이터

사용자로부터 얼굴 사진·음성을 수집하기 위한 UX 설계 방법론 연구의 전체 워크플로우를 조율한다.

## 팀 구성

| 에이전트 | 역할 | 실행 Phase |
|---------|------|-----------|
| ux-methodology-reviewer | HCI/mHealth/산업공학 UX 문헌 탐색 | Phase 1 |
| reference-hallucination-guard | 참고문헌 할루시네이션 검증 | Phase 1.5 |
| ux-methodology-synthesizer | 탐색 결과 합성, 설계 가이드라인 작성 | Phase 2 |

**아키텍처**: Phase 1 → Phase 1.5 → Phase 2 (순차 실행)

---

## Phase 0: 디렉토리 준비

```bash
mkdir -p _workspace4
```

---

## Phase 1: 문헌 탐색

```
Agent(
  subagent_type: "ux-methodology-reviewer",
  model: "opus",
  prompt: "..."
)
```

완료 조건: `_workspace4/01_ux_methodology_literature.md` 생성

---

## Phase 1.5: 할루시네이션 검증

```
/reference-hallucination-guard _workspace4/01_ux_methodology_literature.md
```

검증 보고서: `_workspace4/reference_validation_ux.md`

---

## Phase 2: 합성 보고서

```
Agent(
  subagent_type: "ux-methodology-synthesizer",
  model: "opus"
)
```

완료 조건: `_workspace4/02_ux_synthesis.md` 생성

---

## 최종 산출물

```
_workspace4/
├── 01_ux_methodology_literature.md   — UX 방법론 문헌 탐색 결과
├── reference_validation_ux.md         — 참고문헌 할루시네이션 검증
└── 02_ux_synthesis.md                 — 합성 보고서 + 설계 가이드라인
```
