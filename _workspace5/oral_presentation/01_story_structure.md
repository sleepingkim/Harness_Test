# 01_story_structure.md — 3분 학술 구두 발표 스토리 구조

> 작성자: Storyteller  
> 대상 발표: Semantic Standardization of Unstructured Categorical Data Using Local LLMs and RAG  
> 작성일: 2026-05-11

---

## 1. 프레젠테이션 개요

| 항목 | 내용 |
|------|------|
| **발표 제목** | Semantic Standardization of Unstructured Categorical Data Using Local LLMs and RAG: A Case Study on Industrial Tool Names |
| **핵심 메시지 (1문장)** | RAG가 LLM의 한국어 도메인 지식 부재를 보정하여, 4B 소형 오픈소스 모델로 공공 데이터 표준화 정확도 88%를 달성할 수 있다. |
| **슬라이드 수** | 6장 |
| **총 발표 시간** | 180초 (3분) |

---

## 2. 청중 분석

| 항목 | 분석 |
|------|------|
| **구성** | UST/KIST 교수진 + 연구원 동료 |
| **배경 지식** | 머신러닝·NLP 기본 개념 숙지. RAG, FAISS, BM25 용어 별도 설명 불필요 |
| **한국어 이해** | 가능 — 슬라이드는 영어, 구어 설명은 한국어 가능 |
| **Q&A** | 없음 — 청중은 수동적 수신자. 논쟁 유발보다 임팩트 전달 우선 |
| **관심 포인트** | "이 방법이 실제로 작동하는가?", "어떤 구성이 결정적이었나?" |
| **잠재 회의감** | "공구명 같은 좁은 도메인에 LLM이 필요한가?" → 슬라이드 1에서 선제 해소 필요 |

---

## 3. 스토리 아크 (Barba Minto 피라미드 구조)

### 전체 흐름 요약

```
문제 제기(긴장) → 해결 시도의 실패(반전) → 해결책 제시 → 증거 → 의미 확대
```

3분이라는 극도로 짧은 시간에서 청중의 집중을 유지하는 열쇠는  
**슬라이드마다 하나의 주장(claim)만 전달**하고,  
**결론(88%)을 앞에 보여준 뒤 근거로 내려오는 역피라미드** 구조를 따르는 것이다.

---

### 슬라이드별 설계

#### Slide 1 — The Problem: A Public Database Full of Aliases
- **배정 시간**: 30초
- **역할**: Hook + 문제 제기. 청중이 "왜 이 문제가 중요한가?"를 즉각 납득하게 만든다.
- **핵심 메시지 1줄**: 3,352개 공구명에 160개 표준명 — 동일 공구가 수십 가지 이름으로 존재한다.
- **전달 순서**:
  1. 서울시 공구대여 서비스 = 공공 인프라 데이터 (1문장, 맥락 설정)
  2. 시각 자극: 동의어 클러스터 예시 3개 (기리셋트 → 드릴비트세트 / 함마드릴 → 해머드릴 / PIPE렌치 → 파이프렌치)
  3. 문제 선언: 이 비표준화가 재고·통계·검색을 망가뜨린다
- **감정 목표**: 문제의 구체성으로 인한 공감 + 가벼운 놀라움

---

#### Slide 2 — Why Is This Hard? Five Error Patterns
- **배정 시간**: 25초
- **역할**: 문제 심화. "단순 오탈자 수정이 아니다"는 점을 설득한다.
- **핵심 메시지 1줄**: 오류 유형이 5가지 이상(오탈자·브랜드·동력원·영문·일본어 잔재) — 규칙 기반으로는 해결 불가.
- **전달 순서**:
  1. 457건 분석 결과: 상위 5개 유형이 78% 점유 (숫자 제시)
  2. 하이라이트: 일본어 잔재 — 음운 단절로 자동화 가장 어려움 (뺀치, 기리, 함마)
  3. 함의: 규칙 기반 접근의 한계 → LLM+RAG 필요
- **감정 목표**: 문제의 복잡성에 대한 인식 → 해결의 필요성 수용

---

#### Slide 3 — Our Approach: RAG v2 Pipeline
- **배정 시간**: 35초
- **역할**: 방법 제시. 파이프라인의 핵심 설계 결정 3가지를 명확히 전달.
- **핵심 메시지 1줄**: BGE-m3-ko 임베딩 + BM25/FAISS 하이브리드 검색 + Fallback — 세 가지 설계 결정이 성능을 결정한다.
- **전달 순서**:
  1. 파이프라인 다이어그램 (입력 → 검색 → LLM 판단 → 출력, 화살표 4단계)
  2. 핵심 업그레이드 3가지 강조 (Baseline 대비 변경점만):
     - 임베딩: MiniLM(384d) → BGE-m3-ko(1024d)
     - 검색: FAISS k=5 → BM25+FAISS 하이브리드, k=15
     - 안전장치: Fallback (LLM 오류 시 RAG 1위 후보 자동 반환)
- **감정 목표**: "합리적이고 체계적인 접근" — 신뢰감

---

#### Slide 4 — The Verdict: RAG Transforms Accuracy
- **배정 시간**: 40초
- **역할**: 핵심 결과 전달. 발표 전체의 클라이맥스.
- **핵심 메시지 1줄**: LLM-only 9~27% → RAG 79~88% — RAG는 선택이 아니라 필수다.
- **전달 순서**:
  1. 좌우 대비 시각: LLM-only 바(9~27%) vs RAG 바(79~88%) — 격차 시각화
  2. 최우수 결과 강조: gemma4:e4b 88.47% — 4B 소형 모델
  3. 역설 사례: deepseek-r1:1.5b — 한국어 생성 능력 0% → RAG로 78.4% 달성
     → "RAG가 언어 능력 부재를 보정한다"는 핵심 인사이트 전달
- **감정 목표**: 놀라움 + 확신 (숫자의 극적 대비가 메시지를 각인)

---

#### Slide 5 — What Drives Performance? Embedding Matters Most
- **배정 시간**: 30초
- **역할**: 인사이트 심화. "무엇이 결정적이었나?"에 답한다.
- **핵심 메시지 1줄**: 임베딩 교체(MiniLM→BGE-m3-ko) 하나만으로 +22~27pp — 모델 크기보다 임베딩이 먼저다.
- **전달 순서**:
  1. 동일 LLM, 파이프라인만 교체한 비교 쌍 제시:
     - granite4.1:8b: baseline 55% → improved 82% (+27pp)
     - deepseek-r1:8b: baseline 55% → improved 78% (+23pp)
  2. 요인 분해 (추정):
     - 임베딩 교체: ~15~20pp / k 확대: ~3~5pp / BM25 추가: ~3~5pp
  3. 한 줄 결론: "임베딩 선택이 파이프라인 성능을 지배한다"
- **감정 목표**: "이 연구에서 배울 수 있는 실용적 교훈이 있다" — 지적 만족감

---

#### Slide 6 — Conclusion & Takeaways
- **배정 시간**: 20초
- **역할**: 마무리 + 기억 포인트 고정. Q&A가 없으므로 임팩트 있는 클로징이 마지막 인상을 결정한다.
- **핵심 메시지 1줄**: 로컬 LLM + 도메인 특화 RAG로, 클라우드 없이 공공 데이터 표준화가 가능하다.
- **전달 순서**:
  1. 3가지 핵심 발견 불릿 (짧고 굵게):
     - RAG is essential: +61~70pp accuracy gain
     - Small model wins: 4B gemma4:e4b → 88.47%
     - Embedding first: BGE-m3-ko swap alone → +22~27pp
  2. 한계 및 향후 과제: 일본어 잔재 47% → 동의어 사전 통합 필요
  3. 클로징 문장: "Privacy-safe, cost-effective, and deployable on-premise."
- **감정 목표**: 명료함 + 기억 가능성 (3개 불릿이 남는 인상)

---

## 4. 감정 곡선 표

```
감정 강도
  HIGH │                           ★ Slide 4
       │                          /  (RAG 효과 폭발)
       │               ▲ Slide 3 /
  MID  │  ▲ Slide 1  / (방법 제시)  \  ▲ Slide 5
       │  (문제 공감) /               \ (인사이트)
       │             ▼ Slide 2         \
  LOW  │         (복잡성 인식)          ▼ Slide 6
       │         [긴장 고조]             (안도 + 명료)
       └────────────────────────────────────────────▶ 시간
            :30s    :55s    1:30s   2:10s  2:40s  3:00s
```

| 슬라이드 | 감정 | 강도 | 설계 의도 |
|---------|------|------|----------|
| Slide 1 | 공감·놀라움 | 중 | 청중을 문제 안으로 끌어들임 |
| Slide 2 | 긴장·인식 | 중-하 | 해결의 어려움을 납득시킴 (과잉 설명 금지) |
| Slide 3 | 신뢰·기대 | 중 | 합리적 접근에 대한 믿음 형성 |
| Slide 4 | 놀라움·확신 | 최고 | 숫자 대비로 핵심 주장을 각인 |
| Slide 5 | 지적 만족 | 중-고 | "무엇을 배울 수 있나"에 답함 |
| Slide 6 | 명료·기억 | 중 | 깔끔한 마무리, 3개 포인트만 남김 |

---

## 5. 후속 에이전트 전달 사항

### 정보설계자 (Info-Architect) 에게

- 각 슬라이드당 데이터 밀도를 엄격히 제한할 것: **1슬라이드 = 1주장 + 1시각 증거**
- Slide 4 (결과)는 발표의 클라이맥스이므로, 12개 모델 전체 표를 넣지 말 것. LLM-only vs RAG 대비와 gemma4:e4b 최우수 사례 2개만 집중.
- Slide 5 (임베딩 효과)는 요인 분해를 막대 차트나 화살표 분해 다이어그램으로 표현할 것 (텍스트 불릿 금지).
- 슬라이드 번호와 제목 외에 텍스트 요소는 슬라이드당 최대 5개 항목.
- 데이터 출처 표기: "451 test samples, Exact Match Accuracy" — 슬라이드 4 하단 각주로.

### 비주얼 디자이너 (Visual Designer) 에게

- **색상 체계**: 두 가지 포인트 컬러만 — RAG(파랑 계열), LLM-only(회색). Baseline은 회색으로 죽이고 Improved만 색을 살릴 것.
- **Slide 4 핵심 시각**: 수평 막대 2개 그룹(LLM-only vs RAG) — 격차(+61~70pp)를 브래킷으로 강조.
- **Slide 1 시각**: 공구명 클러스터를 거미줄/방사형으로 표현 (중심: 표준명, 주변: 비표준 표기들).
- **Slide 3 파이프라인 다이어그램**: 4단계 화살표. Baseline과 Improved의 차이 포인트를 색상 하이라이트로 구분.
- 폰트: 제목 24pt 이상, 본문 18pt 이상 (3분 발표 = 먼 거리 청중 고려).
- 배경: 흰색 또는 매우 연한 회색. 학술 포스터와 동일 색상 계열 유지.

### 발표 코치 (Presentation Coach) 에게

- **속도**: 180초 / 6슬라이드 = 슬라이드당 평균 30초. Slide 4에서는 40초까지 쓰되, Slide 6에서 회수.
- **전환 언어 설계**: 각 슬라이드 마지막 문장이 다음 슬라이드의 첫 단어를 예고해야 함.
  - Slide 1 → 2: "...but the problem is more complex than simple typos."
  - Slide 2 → 3: "...that's why we designed a three-component RAG pipeline."
  - Slide 3 → 4: "...let me show you what this pipeline achieved."
  - Slide 4 → 5: "...and the key driver is not the LLM size — it's the embedding."
  - Slide 5 → 6: "...so here's what we've learned."
- **강조 단어**: "88.47%", "4 billion parameters", "61 to 70 percentage points" — 천천히, 또렷하게.
- **비언어**: Slide 4 결과 제시 시 1~2초 침묵 후 숫자 발화 — 극적 효과.
- Q&A 없으므로 마지막 문장은 "Thank you"가 아닌 결론 문장으로 끝낼 것: "Privacy-safe, cost-effective, and fully deployable on-premise."

---

*다음 단계: 02_slide_content.md (Info-Architect) → 03_visual_spec.md (Visual Designer) → 04_speaker_notes.md (Presentation Coach)*
