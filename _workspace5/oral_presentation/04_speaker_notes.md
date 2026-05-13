# 04_speaker_notes.md — 3분 발표 노트

> 발표 제목: Semantic Standardization of Unstructured Categorical Data Using Local LLMs and RAG
> 행사: KIST School, UST 2026 Academic Workshop
> 발표자: Hongchul Shin (신홍철)
> 총 시간: 180초 (3분) / 슬라이드 6장
> 작성일: 2026-05-11

---

## 타이밍 맵

| 슬라이드 | 시작  | 종료  | 배정  | 누적  |
|---------|-------|-------|-------|-------|
| Slide 1 | 0:00  | 0:30  | 30초  | 30초  |
| Slide 2 | 0:30  | 0:55  | 25초  | 55초  |
| Slide 3 | 0:55  | 1:30  | 35초  | 90초  |
| Slide 4 | 1:30  | 2:10  | 40초  | 130초 |
| Slide 5 | 2:10  | 2:40  | 30초  | 160초 |
| Slide 6 | 2:40  | 3:00  | 20초  | 180초 |

> 총 대본 분량 목표: 540~600자 (한국어 180~200자/분 × 3분)

---

## Slide 1 [0:00–0:30]

**슬라이드 제목**: The Problem: A Public Database Full of Aliases

### 발표 대본

서울시 공구대여 서비스의 데이터베이스에는 **160개**의 표준 공구명이 있습니다. 그런데 실제 입력된 공구명은 **3,352개**입니다. [침묵] 같은 공구가 수십 가지 이름으로 존재하는 겁니다. '드릴비트세트' 하나만 봐도, *기리셋트, giri set, 기리셑트* — 전부 같은 도구입니다. 이 비표준화는 재고 관리와 통계, 검색 전체를 망가뜨립니다. ...but the problem is more complex than simple typos.

### 발표 포인팅 지시
- 방사형 클러스터 다이어그램의 중심 파란색 표준명([BLUE])을 먼저 포인팅
- 이후 주변의 빨간 비표준 표기들로 손을 뻗으며 "all the same tool" 강조
- "3,352" 숫자 언급 시 잠시 멈춰 청중이 규모를 흡수하게 할 것
- 마지막에 HIGHLIGHT-BOX를 포인팅하며 전환 문장으로 마무리

### 전환 문장 (다음 슬라이드로)
"...but the problem is more complex than simple typos."

---

## Slide 2 [0:30–0:55]

**슬라이드 제목**: Why Is This Hard? — Five Error Patterns

### 발표 대본

457건의 오류를 분석하니, 상위 5개 유형이 **78%**를 차지했습니다. 오탈자, 브랜드 포함, 동력원, 영문 표기, 속성 정보. 그런데 이 중 어느 것도 단순한 규칙으로는 잡히지 않습니다. 특히 *기리, 뺀치, 함마* — 이건 일본어에서 들어온 음운 잔재로, 동의어 사전 없이는 자동화가 불가능합니다. ...that's why we designed a three-component RAG pipeline.

### 발표 포인팅 지시
- 막대 차트를 위에서 아래로 훑으며 빠르게 진행 (항목당 1~2초)
- Japanese-derived HIGHLIGHT-BOX에서 속도를 늦추고 "기리, 뺀치, 함마" 또렷하게 발음
- "78%" 수치를 언급할 때 막대 차트 전체를 손으로 포괄하며 강조

### 전환 문장 (다음 슬라이드로)
"...that's why we designed a three-component RAG pipeline."

---

## Slide 3 [0:55–1:30]

**슬라이드 제목**: Our Approach — RAG v2 Pipeline

### 발표 대본

저희 파이프라인은 세 가지 핵심 업그레이드로 설계되었습니다. 입력된 공구명이 들어오면, 검색 단계에서 **BGE-m3-ko** 임베딩과 BM25-FAISS 하이브리드 검색으로 후보를 찾고, LLM이 최종 판단합니다. LLM이 실패할 경우 Fallback이 자동으로 상위 후보를 반환합니다. 베이스라인과 가장 큰 차이는 임베딩입니다 — MiniLM 384차원에서 BGE-m3-ko 1024차원으로. 이 하나의 교체가 핵심입니다. 결과를 보여드리겠습니다. ...let me show you what this pipeline achieved.

### 발표 포인팅 지시
- 파이프라인 4단계 화살표를 왼쪽에서 오른쪽으로 손으로 따라가며 설명
- Upgrade Table에서 BGE-m3-ko 행의 ★ 기호를 포인팅하며 "this single swap is the biggest driver" 강조
- Fallback 분기 화살표를 짚으며 안전장치 개념 간략히 언급

### 전환 문장 (다음 슬라이드로)
"...let me show you what this pipeline achieved."

---

## Slide 4 [1:30–2:10]

**슬라이드 제목**: The Verdict — RAG Transforms Accuracy

### 발표 대본

[침묵] **88.47%.** 4B 소형 모델인 gemma4:e4b가 달성한 정확도입니다. LLM만 단독으로 쓸 때는 9에서 27%에 불과했습니다. RAG를 붙이는 순간 *61에서 70 퍼센트포인트*가 뛰었습니다. RAG는 선택이 아닙니다, 필수입니다. 한 가지 더 — DeepSeek 모델은 한국어 생성 능력이 **0%**였습니다. 그런데 RAG를 붙이자 **78.4%**를 달성했습니다. RAG가 언어 능력 자체의 한계를 우회한 겁니다. ...and the key driver is not the LLM size — it's the embedding.

### 발표 포인팅 지시
- 결과 제시 전 1~2초 침묵 — 청중의 시선이 그래프로 향하게 유도
- "88.47%" 발화 시 천천히, 또렷하게 (가장 중요한 숫자)
- 브래킷(+61~70pp)을 포인팅하며 "sixty to seventy percentage points" 강조
- DeepSeek HIGHLIGHT-BOX에서 "0%" vs "78.05%" 두 수치를 손으로 대비시키며 강조

### 전환 문장 (다음 슬라이드로)
"...and the key driver is not the LLM size — it's the embedding."

---

## Slide 5 [2:10–2:40]

**슬라이드 제목**: What Drives Performance? — Embedding Matters Most

### 발표 대본

같은 LLM, 같은 데이터, 파이프라인만 바꿨습니다. granite 모델은 55%에서 **82%**로, deepseek-r1:8b는 55%에서 **78%**로. *22에서 27 퍼센트포인트* 상승입니다. 이 중 약 15~20pp는 임베딩 교체 하나에서 옵니다. 모델 크기보다 임베딩 선택이 먼저입니다. ...so here's what we've learned.

### 발표 포인팅 지시
- 상단 비교표에서 두 모델의 화살표(55%→82%, 55%→78%)를 손으로 따라가며 "same LLM, same data, only the pipeline changed" 강조
- 요인 분해 막대에서 Embedding 막대(가장 긴 것)를 포인팅하며 "this is where the gain comes from"
- HIGHLIGHT-BOX 결론 문장 읽기

### 전환 문장 (다음 슬라이드로)
"...so here's what we've learned."

---

## Slide 6 [2:40–3:00]

**슬라이드 제목**: Conclusion & Takeaways

### 발표 대본

세 가지만 기억해 주십시오. **RAG는 필수** — 정확도가 61~70pp 상승합니다. **소형 모델로 충분** — 4B gemma4가 88%를 달성합니다. **임베딩이 먼저** — BGE-m3-ko 교체만으로 22~27pp. 일본어 잔재 오류율 47%는 아직 과제로 남아 있습니다. "Privacy-safe, *cost-effective, and fully deployable on-premise.*"

### 발표 포인팅 지시
- 세 개의 불릿을 하나씩 포인팅하며 빠르고 명료하게 읽기 (각 1~2초)
- [RED] 한계 박스는 간략히 언급 — 과잉 설명 없이 한 문장으로 처리
- 마지막 HIGHLIGHT-BOX 문장을 *천천히, 또렷하게* 발화하며 마무리
- "Thank you" 없이 클로징 문장으로 완전히 마침. 발표 종료 후 슬라이드를 그대로 두고 청중 시선 유지

### 전환 문장 (다음 슬라이드로)
(마지막 슬라이드 — 전환 없음. 클로징 문장으로 마무리)

---

## 전체 대본 (연속 읽기용)

> 아래 대본은 슬라이드 전환 없이 이어 읽기 위한 통합본입니다. 타이밍 연습 시 활용하세요.

---

**[Slide 1 — 0:00]**
서울시 공구대여 서비스의 데이터베이스에는 160개의 표준 공구명이 있습니다. 그런데 실제 입력된 공구명은 3,352개입니다. [침묵] 같은 공구가 수십 가지 이름으로 존재하는 겁니다. '드릴비트세트' 하나만 봐도, 기리셋트, giri set, 기리셑트 — 전부 같은 도구입니다. 이 비표준화는 재고 관리와 통계, 검색 전체를 망가뜨립니다. ...but the problem is more complex than simple typos.

**[Slide 2 — 0:30]**
457건의 오류를 분석하니, 상위 5개 유형이 78%를 차지했습니다. 오탈자, 브랜드 포함, 동력원, 영문 표기, 속성 정보. 그런데 이 중 어느 것도 단순한 규칙으로는 잡히지 않습니다. 특히 기리, 뺀치, 함마 — 이건 일본어에서 들어온 음운 잔재로, 동의어 사전 없이는 자동화가 불가능합니다. ...that's why we designed a three-component RAG pipeline.

**[Slide 3 — 0:55]**
저희 파이프라인은 세 가지 핵심 업그레이드로 설계되었습니다. 입력된 공구명이 들어오면, 검색 단계에서 BGE-m3-ko 임베딩과 BM25-FAISS 하이브리드 검색으로 후보를 찾고, LLM이 최종 판단합니다. LLM이 실패할 경우 Fallback이 자동으로 상위 후보를 반환합니다. 베이스라인과 가장 큰 차이는 임베딩입니다 — MiniLM 384차원에서 BGE-m3-ko 1024차원으로. 이 하나의 교체가 핵심입니다. 결과를 보여드리겠습니다. ...let me show you what this pipeline achieved.

**[Slide 4 — 1:30]**
[침묵] 88.47%. 4B 소형 모델인 gemma4:e4b가 달성한 정확도입니다. LLM만 단독으로 쓸 때는 9에서 27%에 불과했습니다. RAG를 붙이는 순간 61에서 70 퍼센트포인트가 뛰었습니다. RAG는 선택이 아닙니다, 필수입니다. 한 가지 더 — DeepSeek 모델은 한국어 생성 능력이 0%였습니다. 그런데 RAG를 붙이자 78.05%를 달성했습니다. RAG가 언어 능력 자체의 한계를 우회한 겁니다. ...and the key driver is not the LLM size — it's the embedding.

**[Slide 5 — 2:10]**
같은 LLM, 같은 데이터, 파이프라인만 바꿨습니다. granite 모델은 55%에서 82%로, deepseek-r1:8b는 55%에서 78%로. 22에서 27 퍼센트포인트 상승입니다. 이 중 약 15~20pp는 임베딩 교체 하나에서 옵니다. 모델 크기보다 임베딩 선택이 먼저입니다. ...so here's what we've learned.

**[Slide 6 — 2:40]**
세 가지만 기억해 주십시오. RAG는 필수 — 정확도가 61~70pp 상승합니다. 소형 모델로 충분 — 4B gemma4가 88%를 달성합니다. 임베딩이 먼저 — BGE-m3-ko 교체만으로 22~27pp. 일본어 잔재 오류율 47%는 아직 과제로 남아 있습니다. "Privacy-safe, cost-effective, and fully deployable on-premise."

---

## 연습 팁

### 타이밍 연습 방법

1. **스톱워치 분할 측정**: 첫 연습 때는 각 슬라이드마다 스톱워치를 눌러 실제 소요 시간을 기록하세요. Slide 4가 40초를 초과하면 DeepSeek 역설 설명을 1문장으로 압축합니다.

2. **붉은 불빛 시뮬레이션**: 실제 발표 홀에서는 타이머 불빛이 들어옵니다. 2:45 시점에 Slide 6으로 넘어가지 못했다면, Slide 5 요인 분해 설명을 즉시 생략하고 HIGHLIGHT-BOX 결론 한 줄만 읽으세요.

3. **전환 문장 암기 우선**: 6개의 전환 문장(Slide 1→2, 2→3, 3→4, 4→5, 5→6, 클로징)은 대본 없이도 자연스럽게 나와야 합니다. 전환 문장만 따로 반복 암기하세요.

### 강조 포인트 체크리스트

| 슬라이드 | 반드시 강조할 숫자/표현 | 방법 |
|---------|----------------------|------|
| Slide 1 | 3,352 / 160 / ~21 aliases | 잠깐 멈춤 후 발화 |
| Slide 2 | 78% / 기리, 뺀치, 함마 | 속도 감소 |
| Slide 3 | BGE-m3-ko / ★ | 포인팅 + "핵심" 강조 |
| Slide 4 | **88.47%** / 61~70pp / 0%→78.4% | 1~2초 침묵 선행, 천천히 |
| Slide 5 | +22~27pp / 임베딩 교체 | 요인 분해 막대 포인팅 |
| Slide 6 | 3개 불릿 / 47% / 클로징 문장 | 불릿 각 포인팅, 천천히 마무리 |

### 비언어 행동 주의사항

- **Slide 4 진입 시**: 슬라이드가 전환된 후 1~2초 청중과 눈을 맞추며 침묵 → 그 다음 "88.47%"를 또렷이 발화. 이 침묵이 극적 효과를 만듭니다.
- **포인팅 방향**: 항상 청중을 향한 채로 포인팅. 슬라이드를 등지지 말 것.
- **마지막 문장**: "Thank you"로 끝내지 말고 클로징 문장 — "Privacy-safe, cost-effective, and fully deployable on-premise." — 으로 완전히 마칩니다. 그 후 슬라이드를 그대로 두고 청중 시선을 유지하세요.
- **속도 기준**: 평소보다 20% 느리게. 발표장 음향 특성과 긴장감으로 인해 스스로 느리다 싶은 속도가 청중에게는 적당합니다.
