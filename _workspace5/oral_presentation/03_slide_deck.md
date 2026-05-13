# 03_slide_deck.md — 3분 학술 구두 발표 슬라이드 덱

> 발표 제목: Semantic Standardization of Unstructured Categorical Data Using Local LLMs and RAG: A Case Study on Industrial Tool Names
> 행사: KIST School, UST 2026 Academic Workshop
> 발표자: Hongchul Shin
> 총 슬라이드: 6장 / 총 시간: 180초
> 작성일: 2026-05-11

---

## Slide 1: The Problem — A Public Database Full of Aliases
> ⏱ 30초 | 핵심 메시지: 3,352개 공구명, 160개 표준명 — 동일 공구가 수십 이름으로 존재한다.

### [RADIAL-CLUSTER + HIGHLIGHT-BOX]

**One tool. Dozens of names. One broken database.**

```
                    [RED] 기리셋트          [RED] 드릴비트 set
                         \                      /
        [RED] giri set ───── [BLUE] 드릴비트세트 ────── [RED] 기리 세트
                         /                      \
               [RED] drill bit SET          [RED] 기리셑트

                    [RED] 함마드릴          [RED] 해머 드릴
                         \                      /
          [RED] 함마 드릴 ───── [BLUE] 해머드릴 ────── [RED] HAMMER DRILL
                         /
               [RED] 함마드릴기

                    [RED] PIPE렌치
                         \
          [RED] 파이프 렌치 ───── [BLUE] 파이프렌치 ────── [RED] pipe wrench
```

|                            |                                   |
| -------------------------- | --------------------------------- |
| [RED] Non-standard entries | **3,352**                         |
| [BLUE] Standard names      | **160**                           |
| Ratio                      | **~21 aliases per standard name** |

> [HIGHLIGHT-BOX] Broken standardization → broken inventory, broken search, broken statistics.

[Footer: Hongchul Shin | UST 2026 Academic Workshop | Slide 1/6]

### 발표자 지시사항 (비가시)
- 클러스터 다이어그램의 중심 표준명([BLUE])을 먼저 포인팅하고, 주변 비표준 표기들로 손을 뻗으며 "all the same tool"이라고 강조할 것
- "21 aliases per standard name"을 읽을 때 잠깐 멈춰 청중이 숫자를 흡수하게 할 것
- 마지막 HIGHLIGHT-BOX를 포인팅하며 "...but the problem is more complex than simple typos."로 슬라이드 2 전환

---

## Slide 2: Why Is This Hard? — Five Error Patterns
> ⏱ 25초 | 핵심 메시지: 5가지 유형이 오류의 78% — 규칙 기반 불가, 특히 일본어 잔재.

### [HORIZONTAL-BAR + HIGHLIGHT-BOX]

**78% of errors fall into 5 systematic patterns — none fixable by simple rules.**

```
Error Pattern           Share    Example

Typos            ████████████████████  33.9%   경랑몽키, 스판너
Brand Inclusion  █████████             15.5%   보쉬전동드릴
Power Source     ██████                10.9%   유선전동드릴
English / Abbrev █████                  9.0%   HSS드릴비트
Attribute        █████                  8.8%   180mm그라인더
─────────────────────────────────────────────────────────
                                       78.1%   ← Top 5 combined

[RED] Japanese-derived     ██           4.6%   기리 / 뺀치 / 함마
```

> [HIGHLIGHT-BOX / RED] Japanese-derived terms: phonetic discontinuity → automation impossible without a thesaurus.

[Footer: Hongchul Shin | UST 2026 Academic Workshop | Slide 2/6]

### 발표자 지시사항 (비가시)
- 막대 차트를 위에서 아래로 훑으며 빠르게 진행 (각 항목 1~2초)
- Japanese-derived HIGHLIGHT-BOX에서 속도를 늦추고 "기리, 뺀치, 함마"를 또렷하게 발음할 것
- "...that's why we designed a three-component RAG pipeline."으로 슬라이드 3 전환

---

## Slide 3: Our Approach — RAG v2 Pipeline
> ⏱ 35초 | 핵심 메시지: BGE-m3-ko + BM25/FAISS 하이브리드 + Fallback — 세 가지 설계 결정이 성능을 결정한다.

### [DIAGRAM: 4-STAGE PIPELINE + TWO-COLUMN UPGRADE TABLE]

**Three targeted upgrades over the baseline.**

```
┌─────────────┐     ┌──────────────────────┐     ┌─────────────────┐     ┌──────────────┐
│  Raw Input  │────▶│  Retrieval (Top-k)   │────▶│   LLM Judgment  │────▶│ Standard Name│
│ (tool name) │     │ [BLUE] BGE-m3-ko     │     │ (local model)   │     │   Output     │
│             │     │ [BLUE] BM25 + FAISS  │     │                 │     │              │
└─────────────┘     │ [BLUE] k = 15        │     └────────┬────────┘     └──────────────┘
                    └──────────────────────┘              │ LLM fails?
                                                          ▼
                                                  [BLUE] Fallback:
                                                  return RAG rank-1
```

```
Component        [GRAY] Baseline              [BLUE] RAG v2 (Improved)
─────────────────────────────────────────────────────────────────────
Embedding        MiniLM  (384d)               BGE-m3-ko  (1024d)   ★
Retrieval        FAISS only,  k=5             BM25 40% + FAISS 60%, k=15
Safety net       —                            Fallback (rank-1 auto-return)
Knowledge DB     160 standard names           160 standard names (same)
Eval set         457 ground-truth pairs       457 ground-truth pairs (same)
```

[Footer: Hongchul Shin | UST 2026 Academic Workshop | Slide 3/6]

### 발표자 지시사항 (비가시)
- 파이프라인 화살표를 왼쪽에서 오른쪽으로 손으로 따라가며 설명
- Upgrade Table에서 BGE-m3-ko 행의 ★을 포인팅하며 "this single swap is the biggest driver — I'll show you why in a moment"
- "...let me show you what this pipeline achieved."로 슬라이드 4 전환

---

## Slide 4: The Verdict — RAG Transforms Accuracy
> ⏱ 40초 | 핵심 메시지: LLM-only 9~27% → RAG 79~88% — RAG는 선택이 아니라 필수다.

### [GROUPED-BAR + HIGHLIGHT-BOX]

**RAG is not optional — it is the difference between 9% and 88%.**

```
                [GRAY] LLM-only          [BLUE] RAG v2
                Exact Match %            Exact Match %
                ─────────────            ─────────────
gemma4:e4b       ████                     ████████████████████████████████  88.47% ★ BEST
                  27.4%                   
                  ◄──────────────── +61.1pp ──────────────────►

gemma3:4b        ████                     ███████████████████████████████   84.48%
                  23.0%
                  ◄──────────────── +61.5pp ──────────────────►

exaone3.5:7.8b   ██                       ██████████████████████████████    79.16%
                   9.4%
                  ◄──────────────── +69.8pp ──────────────────►
```

> [HIGHLIGHT-BOX / GREEN] gemma4:e4b — only 4B parameters → **88.47%** exact match accuracy

> [HIGHLIGHT-BOX / BLUE] DeepSeek paradox: Korean generation = 0% (LLM-only) → **78.05%** with RAG
> → RAG compensates for absent language capability.

*451 test samples · Exact Match Accuracy*

[Footer: Hongchul Shin | UST 2026 Academic Workshop | Slide 4/6]

### 발표자 지시사항 (비가시)
- 막대 그래프 결과를 제시하기 전 1~2초 침묵 — 그런 다음 "88.47%" 천천히 또렷하게 발화
- 브래킷(+61~70pp)을 포인팅하며 "sixty to seventy percentage points" 강조
- DeepSeek 역설 박스에서 "Korean generation zero percent" vs "78.4% with RAG" 대비 강조
- "...and the key driver is not the LLM size — it's the embedding."으로 슬라이드 5 전환

---

## Slide 5: What Drives Performance? — Embedding Matters Most
> ⏱ 30초 | 핵심 메시지: MiniLM→BGE-m3-ko 교체 하나만으로 +22~27pp — 모델 크기보다 임베딩이 먼저다.

### [ARROW-DECOMPOSITION DIAGRAM + TWO-COLUMN]

**Same LLM. Different pipeline. +22~27 percentage points.**

```
   Model              [GRAY] Baseline          [BLUE] RAG v2 Improved
                      (MiniLM + FAISS k=5)     (BGE-m3-ko + BM25+FAISS k=15)
   ──────────────────────────────────────────────────────────────────────────
   granite4.1:8b      55.21%  ──────────────────────────────▶  82.48%  (+27.3pp)
   deepseek-r1:8b     55.21%  ──────────────────────────────▶  77.83%  (+22.6pp)
```

```
  Performance gain decomposition (estimated):

  Total gain  ████████████████████████████  ~25pp

  Breakdown:
  ┌─ Embedding swap  (MiniLM → BGE-m3-ko)  ██████████████  ~15–20pp  ← DOMINANT
  ├─ k expansion     (k=5 → k=15)          ████             ~3–5pp
  └─ BM25 hybrid     (FAISS → BM25+FAISS)  ████             ~3–5pp
```

> [HIGHLIGHT-BOX / BLUE] **Embedding selection dominates pipeline performance.**
> Choose your embedding before tuning your LLM.

[Footer: Hongchul Shin | UST 2026 Academic Workshop | Slide 5/6]

### 발표자 지시사항 (비가시)
- 상단 비교 표에서 두 모델의 화살표(55% → 82%, 55% → 78%)를 손으로 따라가며 "same LLM, same data, only the pipeline changed"
- 요인 분해 막대에서 Embedding 막대를 포인팅하며 "this is where the gain comes from"
- "...so here's what we've learned."으로 슬라이드 6 전환

---

## Slide 6: Conclusion & Takeaways
> ⏱ 20초 | 핵심 메시지: 로컬 LLM + 도메인 특화 RAG로, 클라우드 없이 공공 데이터 표준화 가능.

### [BULLETS + HIGHLIGHT-BOX]

**Three things to remember.**

```
  [BLUE]  ① RAG is essential       +61–70pp accuracy gain over LLM-only

  [GREEN] ② Small model wins       4B gemma4:e4b → 88.47% exact match

  [BLUE]  ③ Embedding first        BGE-m3-ko swap alone → +22–27pp
```

```
  [RED]  Remaining challenge:
         Japanese-derived terms → 47.1% error rate
         → Synonym dictionary integration needed
```

> [HIGHLIGHT-BOX / GREEN]
> **"Privacy-safe, cost-effective, and fully deployable on-premise."**

[Footer: Hongchul Shin | UST 2026 Academic Workshop | Slide 6/6]

### 발표자 지시사항 (비가시)
- 세 불릿을 하나씩 포인팅하며 빠르고 명료하게 읽기 (각 1~2초)
- [RED] 한계 박스는 간략히 언급 — 과잉 설명 금지
- 마지막 HIGHLIGHT-BOX 문장을 천천히, 또렷하게 발화하며 마무리 ("Thank you" 생략)
- 발표 종료 후 슬라이드를 그대로 두고 청중 시선을 유지할 것

---

## 전체 슬라이드 흐름 요약

| 슬라이드 | 제목 | 시간 | 레이아웃 | 핵심 시각 요소 |
|---------|------|------|---------|-------------|
| 1 | The Problem | 30s | RADIAL-CLUSTER | 공구명 동의어 클러스터 (방사형) |
| 2 | Why Is This Hard? | 25s | HORIZONTAL-BAR | 오류 유형 막대 차트 |
| 3 | Our Approach | 35s | PIPELINE DIAGRAM | 4단계 화살표 + 업그레이드 비교표 |
| 4 | The Verdict | 40s | GROUPED-BAR | LLM-only vs RAG 대비 막대 + 브래킷 |
| 5 | What Drives Performance? | 30s | ARROW-DECOMPOSITION | 요인 분해 다이어그램 |
| 6 | Conclusion | 20s | BULLETS | 3개 핵심 불릿 + 클로징 문장 |

**색상 체계:**
- [BLUE] = RAG / Improved / 핵심 강조
- [GRAY] = Baseline / LLM-only
- [GREEN] = 긍정 결과 / 성공 사례
- [RED] = 한계 / 문제 / 주의

**전환 언어 (발표자 참고):**
- Slide 1→2: "...but the problem is more complex than simple typos."
- Slide 2→3: "...that's why we designed a three-component RAG pipeline."
- Slide 3→4: "...let me show you what this pipeline achieved."
- Slide 4→5: "...and the key driver is not the LLM size — it's the embedding."
- Slide 5→6: "...so here's what we've learned."
