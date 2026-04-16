---
name: soccer-tracking-research
description: "축구 영상 선수 식별 연구 파이프라인 오케스트레이터. 문헌 탐색(K-Dense paper-lookup) → 할루시네이션 검증(reference-hallucination-guard) → 기법 심층 분석 → 연구 설계서 작성까지 에이전트 팀으로 실행. '축구 선수 추적 연구', '선수 식별 연구', '가림 처리 연구', 'soccer tracking research' 등의 요청 시 이 스킬을 사용할 것."
---

# Soccer Tracking Research — 파이프라인 오케스트레이터

단일 카메라 축구 영상에서 선수 탐지·추적·등번호 인식 성능 개선 연구의 전체 워크플로우를 조율한다.

## 팀 구성 및 활용 스킬

| 에이전트 | 역할 | 활용 외부 스킬 | Phase |
|---------|------|-------------|-------|
| soccer-vision-reviewer | 문헌 탐색 (4개 병렬 스테이지) | K-Dense: paper-lookup, literature-review / Skill3: sciomc 병렬 패턴 | Phase 1 |
| (내장) reference-hallucination-guard | 참고문헌 할루시네이션 검증 | 기존 .claude/skills/ | Phase 1.5 |
| method-analyzer | 핵심 기법 심층 분석 | K-Dense: citation-management, research-lookup / Harness100: statistical-analyst | Phase 2 |
| research-designer | 연구 설계서 작성 | Harness100: research-designer, paper-writer(IMRaD), citation-standards / K-Dense: citation-management | Phase 3 |

**아키텍처**: 순차 파이프라인
`Phase 1` → `Phase 1.5 (검증)` → `Phase 2` → `Phase 3`

모든 에이전트는 `model: "opus"` 사용.

---

## Phase 0: 컨텍스트 확인

실행 전 `YoungScientist/_workspace/` 존재 여부 확인:

- **없음**: 초기 실행 → Phase 1부터 전체 실행
- **있음 + 특정 단계 재실행 요청**:
  - "연구 설계만 다시 해줘" → Phase 3만 실행 (기존 01, 02 파일 활용)
  - "기법 분석 다시 해줘" → Phase 2 → 3 재실행
  - "할루시네이션 검증 다시 해줘" → Phase 1.5 → 2 → 3 재실행
- **있음 + 완전 새 실행 요청**: 기존 파일을 `_prev/`로 이동 후 새 실행

```bash
# 디렉토리 준비
mkdir -p YoungScientist/_workspace
```

---

## Phase 1: 문헌 탐색 (soccer-vision-reviewer)

**sciomc 병렬 패턴 + K-Dense paper-lookup REST API 적용**

```
Agent(
  subagent_type: "soccer-vision-reviewer",
  model: "opus",
  prompt: "
    연구 주제: 단일 카메라 축구 경기 영상에서 선수 탐지 + 등번호 인식을 통한 개별 선수 식별.
    핵심 문제: 선수 간 가림(occlusion) 상황에서의 추적 성능 저하.
    
    sciomc 병렬 패턴으로 4개 탐색 스테이지를 실행:
    Stage 1 [HIGH]: 선수 탐지 + 다중 객체 추적 (MOT)
    Stage 2 [HIGH]: 가림 특화 기법 (Occlusion Handling)
    Stage 3 [HIGH]: 등번호 인식 (Jersey Number Recognition)
    Stage 4 [MEDIUM]: 선수 재식별 (Re-ID) + 통합 파이프라인
    
    K-Dense paper-lookup REST API 사용:
    - Semantic Scholar graph API
    - OpenAlex API
    - Crossref API (DOI 검증)
    - arXiv API (프리프린트)
    - PubMed eutils API (학제간)
    
    출력: YoungScientist/_workspace/01_literature_review.md
    형식: soccer-vision-reviewer 에이전트 정의의 출력 형식 준수
  "
)
```

완료 조건: `YoungScientist/_workspace/01_literature_review.md` 생성 확인

---

## Phase 1.5: 참고문헌 할루시네이션 검증 (reference-hallucination-guard)

Phase 1 완료 직후 자동 실행.

```
# reference-hallucination-guard 스킬 적용
검증 대상: YoungScientist/_workspace/01_literature_review.md

실행 순서:
1. 파일에서 모든 참고문헌 추출
2. DOI 직접 확인 (doi.org / Crossref API)
3. Semantic Scholar / IEEE Xplore / arXiv 제목+저자 검색
4. 결과 분류: ✅ / ⚠️ / ❓ / ❌
5. 검증 보고서 저장: YoungScientist/_workspace/reference_validation_report.md
6. 01_literature_review.md에 검증 기호 인라인 추가

❌ 항목 처리:
- 존재 확인 불가 논문은 [UNVERIFIED] 태그 추가
- Phase 2 및 Phase 3에서 해당 항목 제외 권고
```

완료 조건: `YoungScientist/_workspace/reference_validation_report.md` 생성 확인

---

## Phase 2: 기법 심층 분석 (method-analyzer)

**K-Dense citation-management + Harness100 statistical-analyst 패턴 적용**

```
Agent(
  subagent_type: "method-analyzer",
  model: "opus",
  prompt: "
    입력 파일:
    - YoungScientist/_workspace/01_literature_review.md (문헌 탐색 결과, 검증 기호 포함)
    - YoungScientist/_workspace/reference_validation_report.md (할루시네이션 검증 결과)
    
    작업:
    1. ✅ 검증된 논문 기반으로 핵심 기법 선별
    2. 기법별 아키텍처·학습 전략·손실 함수 상세 비교
    3. 가림 상황 특화 기법의 메커니즘 심층 분석
    4. 기법 간 조합 가능성 평가
    5. Harness100 statistical-analyst 패턴으로 성능 지표 정량 비교
    6. CrossRef/Semantic Scholar API로 인용 수 및 BibTeX 추출
    7. 단일 카메라 축구 영상 조건에서의 적용 가능성 판단
    8. 권장 파이프라인 구성 제안
    
    ❌/❓ 항목은 분석에서 제외하거나 [미검증] 표기.
    
    출력: YoungScientist/_workspace/02_method_analysis.md
    형식: method-analyzer 에이전트 정의의 출력 형식 준수
  "
)
```

완료 조건: `YoungScientist/_workspace/02_method_analysis.md` 생성 확인

---

## Phase 3: 연구 설계 (research-designer)

**Harness100 research-designer + paper-writer(IMRaD) + K-Dense citation-management 적용**

```
Agent(
  subagent_type: "research-designer",
  model: "opus",
  prompt: "
    입력 파일:
    - YoungScientist/_workspace/01_literature_review.md (문헌 탐색 결과)
    - YoungScientist/_workspace/02_method_analysis.md (기법 분석 결과)
    - YoungScientist/_workspace/reference_validation_report.md (검증 결과)
    
    작업 (Harness100 research-designer 프레임워크):
    1. 연구 문제 형식적 정의 (입력/출력/제약)
    2. 연구 질문 (RQ1, RQ2, ...) 및 가설 (H1, H2, ...) 수립
    3. 변수 정의 (독립/종속/통제)
    4. 선행연구 대비 연구 공백 명확화
    5. 제안 방법론 설계 (기법 분석 기반)
    6. 실험 설계 (데이터셋, 평가 지표, baselines, ablation)
    7. IMRaD 논문 구조를 고려한 연구 로드맵
    8. 학회 투고 전략 (CVPR, ECCV, ICCV 등)
    9. CrossRef API로 참고문헌 BibTeX 최종 검증
    
    출력: YoungScientist/_workspace/03_research_design.md
    형식: research-designer 에이전트 정의의 출력 형식 준수
  "
)
```

완료 조건: `YoungScientist/_workspace/03_research_design.md` 생성 확인

---

## 최종 산출물 구조

```
YoungScientist/_workspace/
├── 01_literature_review.md          — 문헌 탐색 (K-Dense API, sciomc 4-stage 병렬, 검증 기호 포함)
├── reference_validation_report.md   — 참고문헌 할루시네이션 검증 보고서
├── 02_method_analysis.md            — 기법 심층 분석 (statistical-analyst 정량 비교 포함)
└── 03_research_design.md            — 연구 설계서 (Harness100 research-designer, IMRaD 인지)
```

---

## 직전 하네스 대비 차별점

| 항목 | 초기 구성 | 업그레이드 후 |
|------|----------|-------------|
| 문헌 탐색 | WebSearch 기반 | K-Dense paper-lookup REST API (5개 학술 DB) |
| 탐색 전략 | 순차 단일 | sciomc 4-stage 병렬 |
| 할루시네이션 검증 | 없음 | Phase 1.5 reference-hallucination-guard |
| 성능 비교 | 정성적 | Harness100 statistical-analyst 정량 비교 |
| 연구 설계 | 자유 형식 | Harness100 research-designer (RQ/가설/변수) |
| 논문 구조 인지 | 없음 | IMRaD paper-writer 패턴 |
| 참고문헌 관리 | 없음 | K-Dense citation-management (CrossRef API) |

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| paper-lookup API 응답 없음 | WebSearch 대체, [API 불가] 표기 |
| Phase 1 산출물 미생성 | soccer-vision-reviewer 1회 재실행 |
| Phase 1.5 검증 불가 | ❓ 처리 후 진행 |
| ❌ 비율 > 30% | 사용자에게 보고 후 진행 여부 확인 |
| CrossRef API 실패 | 기존 BibTeX 정보 활용, [수동 확인 필요] 표기 |
| Phase 2 분석 대상 부족 | Phase 1 결과에서 최소 10개 기법 확보 후 진행 |
| Phase 3 설계 불완전 | 부족한 부분 명시 후 사용자 피드백 요청 |
