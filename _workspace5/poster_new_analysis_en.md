# Dirty Data Type Analysis and LLM-only Baseline for Tool Name Standardization Using LLM+RAG

> **Seoul Public Tool Lending Dataset — RAG v2 Improved: Additional Analysis**  
> Ground Truth v2 (GT 457 pairs) | Evaluation Date: 2026-05-09

---

## Abstract

An LLM+RAG pipeline (RAG v2 Improved, gemma4:e4b) for standardizing non-uniform tool names in Seoul public tool lending data achieved **88.5%** exact-match accuracy. This poster reports two follow-up analyses: (1) accuracy breakdown across 11 automatically classified dirty-data types to identify strong and weak patterns, and (2) a LLM-only zero-shot experiment to quantify RAG's isolated contribution. Key findings: LLM-alone accuracy is only 9–27%; RAG contributes **+61–70 percentage points (pp)**. Japanese loanword entries (47.1%) constitute the primary weakness and require synonym dictionary augmentation.

---

## 1. Background

- RAG v2 Improved: BGE-m3-ko embedding + BM25(40%)/FAISS(60%) hybrid retrieval, k=15, category injection
- Best model: gemma4:e4b — **88.5%** on GT v2 (457 pairs)
- Two research questions addressed in this poster:
  - **"Which dirty-data types does the system handle well, and which does it fail on?"** → Type-level accuracy analysis
  - **"How much does RAG actually contribute?"** → LLM-only zero-shot comparison

---

## 2. Dirty Data Type Analysis

### 2.1 Type Distribution in GT 457 Pairs (Top Types)

| Rank | Type | Count | Share | Difficulty |
|:----:|------|:-----:|:-----:|:----------:|
| 1 | **Typos / misspellings** | 155 | **33.9%** | Medium |
| 2 | Brand name embedded | 71 | 15.5% | Medium |
| 3 | Power source specified | 50 | 10.9% | Easy |
| 4 | English / abbreviation | 41 | 9.0% | Medium |
| 5 | Attribute notation | 40 | 8.8% | Easy |
| — | (6 other types) | 100 | 21.9% | Varied |

> Top 5 types account for **78.1%** of all samples — their accuracy dominates the overall score.

### 2.2 gemma4:e4b Accuracy by Type

| Type | Accuracy | Correct / Total | Assessment |
|------|:--------:|:---------------:|------------|
| Special symbols | **100.0%** | 6/6 | Perfect (small n) |
| Power source specified | **96.4%** | 53/55 | Excellent |
| Metadata / tags | **95.5%** | 21/22 | Excellent |
| Attribute notation | **95.0%** | 38/40 | Excellent |
| **Typos / misspellings** | **93.8%** | 136/145 | Excellent — most frequent type |
| Brand name embedded | 87.5% | 63/72 | Good |
| Set / components | 84.6% | 22/26 | Good |
| English / abbreviation | 82.5% | 33/40 | Good |
| Other | 66.7% | 18/27 | Weak |
| **Japanese loanwords** | **47.1%** | 8/17 | **Critical — primary weakness** |

> 80% threshold: 7 types pass, **2 types below** (Other and Japanese loanwords)  
> Japanese loanword errors: 9 out of 52 total errors (17.3%), disproportionate to its 4.6% share

### 2.3 Cross-Model Anomalies (9 Models × Type Heatmap)

| Observation | Detail |
|-------------|--------|
| exaone3.5:7.8b on Set/Components | Ranks 5th overall (79.2%) but **1st in this type at 96.2%** — reflects EXAONE's Korean industrial vocabulary advantage |
| granite4.1:3b on Attribute Notation | Only **50.0%** while all other models reach 80–95% — small 3B model limitation |
| gemma3:4b on Japanese Loanwords | Highest among all models at **52.9%** — likely due to broader Japanese-derived term coverage in training data |

### 2.4 Mechanism Interpretation

**Why typos score 93.8%:**
- BGE-m3-ko (1024-dim) encodes single-syllable Korean spelling variants into nearby embedding vectors
- BM25 syllable unigram/bigram index assigns score when dirty and standard name share common n-grams
- Examples: "경랑몽키" → "경량몽키렌치" (consonant error), "스판너" → "스패너" (vowel error)

**Why Japanese loanwords score only 47.1% — triple barrier:**

| Failure Mode | Description |
|-------------|-------------|
| Embedding failure | "기리" vs. "드릴비트": phonetically and morphologically disjoint — embedding vectors are fully separated |
| BM25 complete mismatch | Zero shared syllable n-grams → lexical retrieval completely disabled |
| LLM knowledge gap | Even if RAG includes the correct candidate in top-k, LLM cannot recognize the mapping |

---

## 3. LLM-only Baseline Experiment

### 3.1 Experimental Design

- **LLM-only (zero-shot)**: LLM generates a standard name freely without any retrieved candidates
- Same GT 457 pairs; 4 models evaluated
- Metrics: **exact match** (verbatim agreement) / **nearest match** (LLM output mapped to closest standard name in list, then checked)

### 3.2 Main Results

| Model | LLM-only (exact) | LLM-only (nearest) | RAG v2 Improved | RAG Contribution |
|-------|:---:|:---:|:---:|:---:|
| gemma4:e4b | 27.4% | 63.2% | **88.5%** | **+61.1 pp** |
| gemma3:4b | 23.0% | 60.8% | **84.5%** | **+61.5 pp** |
| exaone3.5:7.8b | 9.4% | 60.4% | **79.2%** | **+69.7 pp** |
| deepseek-r1:1.5b | 0.0%* | 0.7% | **78.4%** | **+78.4 pp** |

> *deepseek-r1:1.5b: Korean free-text generation is fundamentally absent. Output is a mixture of Chinese, English, and malformed Korean. 0% reflects a **model limitation**, not an API failure.

### 3.3 RAG Contribution by Type (gemma4:e4b)

| Type | LLM-only | RAG | Gain |
|------|:---:|:---:|:---:|
| Power source specified | 8.0% | 96.4% | **+88.4 pp** |
| Typos / misspellings | 21.9% | 93.8% | **+71.9 pp** |
| Brand name embedded | 28.2% | 87.5% | +59.3 pp |
| Japanese loanwords | 19.0% | 47.1% | +28.0 pp |

### 3.4 Three Key Findings

**Finding 1 — RAG as a Notation Anchor (not merely a knowledge supplement)**

```
exact match 27%  vs.  nearest match 63%  →  35 pp gap
```

LLMs know the concept of "drill," but cannot decide whether to write "전동드릴," "드릴," or "충전 드릴." Only when RAG supplies a candidate pool do outputs converge to the correct notation. **RAG's role is notation anchoring, not knowledge injection.**

**Finding 2 — Circumventing Language Limitations**

deepseek-r1:1.5b cannot generate Korean text at all (exact 0%, nearest 0.7%). With RAG, it achieves **78.4%**. RAG converts an impossible task (Korean free generation) into a tractable one (Korean candidate selection), demonstrating RAG's role beyond mere precision improvement.

**Finding 3 — Refuting the RAG Backfire Hypothesis for Japanese Loanwords**

LLM-only: 19.0% → RAG: 47.1% (**+28 pp**). RAG does help. The low absolute accuracy (47.1%) is caused by the LLM's knowledge gap (19.0% baseline), not by retrieval degradation. The solution is synonym dictionary augmentation — not removing RAG.

---

## 4. Conclusions

### Summary

| Item | Result |
|------|--------|
| RAG contribution | **+61–70 pp** — LLM alone (9–27%) is not production-viable |
| RAG's role | **Notation anchoring** — determines the exact standard form, not just domain knowledge |
| Strongest type | Typos 93.8% — enabled by BGE-m3-ko syllable-level embeddings |
| Weakest type | Japanese loanwords 47.1% — triple retrieval and generation barrier |

### Improvement Roadmap

| Priority | Target | Current | Approach |
|:--------:|--------|:-------:|----------|
| 1 | Japanese loanwords | 47.1% | Add synonym mapping table (기리→드릴비트, 함마→해머, etc.) to RAG knowledge base |
| 2 | Other | 66.7% | Human-in-the-loop queuing for uncertain cases |
| 3 | English / abbreviations | 82.5% | Add BPE-based English sub-word tokenizer to BM25 index |

### Implications

- **Type-level error analysis** enables targeted improvement prioritization — aggregate accuracy alone cannot reveal these insights
- RAG's ability to elevate a model with zero Korean generation capability (deepseek-r1:1.5b) to 78.4% suggests strong potential for **edge-device deployment** with small models

---

*Evaluation basis: RAG v2 Improved × 9 models × GT v2 (457 pairs) | LLM-only zero-shot × 4 models × GT v2 (457 pairs)*  
*Outputs: `dirty_type_analysis_report.md` / `llm_only_vs_rag_comparison.md` / `type_accuracy_analysis.xlsx`*
