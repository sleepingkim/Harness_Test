# 3-Minute Presentation Script (English)
## Semantic Standardization of Unstructured Categorical Data Using Local LLMs and RAG
> KIST School, UST 2026 Academic Workshop | Hongchul Shin

---

> **How to read this script**
> - `[ pause ]` → Hold 1–2 seconds, make eye contact with the audience
> - `*italics*` → Slow down, speak clearly
> - **bold** → Emphasize
> - `// action //` → Stage direction (do not read aloud)
> - `⏱` on the right → Cumulative target time for that slide

---

## 🎤 Slide 0 — Title

// Once the slide appears, scan the audience slowly, then begin //

Hello, everyone.
I'm Hongchul Shin from the HDI Lab at UST-KIST.

In the next three minutes, I'll show you how we used open-source LLMs and RAG
to automatically standardize messy tool-name records in a public dataset.

---

## 🎤 Slide 1 — The Problem `⏱ 0:30`

// Point to the blue standard names at the center of the cluster diagram //

Seoul's public tool-rental service has **160** standard tool names in its database.

But the actual records contain **3,352** distinct entries.

[ pause ]

// Slowly sweep your hand toward the surrounding red non-standard labels //

The same physical tool exists under dozens of different names.

Take "drill bit set" alone —
*giri-set, giri set, giri-sset* — all referring to the exact same item.

This lack of standardization breaks inventory tracking, usage statistics, and search — entirely.

// Point to the warning highlight box //

...but the problem is more complex than simple typos.

---

## 🎤 Slide 2 — Five Error Patterns `⏱ 0:55`

// Scan the bar chart from top to bottom //

We analyzed 457 non-standard entries in full.
The top five error types account for **78%** of all cases.

Typos, brand inclusion, power-source labels, English abbreviations, and embedded attributes.

None of these can be fixed by simple rule-based methods.

// Move to the red highlight box — slow down //

Most critically: *giri, ppaenchi, hamma* —

These are Japanese loanwords that entered Korean industrial settings decades ago.
The phonetic gap between them and their Korean equivalents is so large
that no embedding or BM25 index can bridge it without an explicit thesaurus.

...that's why we designed an enhanced RAG pipeline.

---

## 🎤 Slide 3 — RAG v2 Pipeline `⏱ 1:30`

// Trace the pipeline arrows left to right with your hand //

Our pipeline works as follows.
A raw tool name comes in.
The retrieval stage fetches the top **15** candidate standard names
using a hybrid of BGE-m3-ko embeddings and BM25-FAISS search.
The local LLM then selects the best match.
If the LLM fails, a Fallback mechanism automatically returns the top-ranked candidate.

// Point to the ★ next to BGE-m3-ko in the comparison table //

The single biggest difference from the baseline is right here.
We replaced MiniLM at 384 dimensions
with BGE-m3-ko at **1,024 dimensions**,
added category-label injection into the prompt,
and expanded candidates from 5 to 15.

That combination is the key.

...let me show you what this pipeline achieved.

---

## 🎤 Slide 4 — The Verdict `⏱ 2:10`

// After the slide transitions, hold for 1–2 seconds of silence, make eye contact //

[ pause ]

***88.47 percent.***

// Slow and clear //

That is the exact-match accuracy achieved by gemma4:e4b —
a model with only **4 billion parameters**.

// Point to the gray bars //

Without RAG, LLM-only exact-match accuracy was just *9 to 27 percent*.

// Point to the blue bars and the bracket //

The moment we add RAG, accuracy jumps by ***61 to 78 percentage points***.

RAG is not optional — it is **essential**.

// Move to the DeepSeek highlight box //


One more thing.
The DeepSeek-r1 1.5B model had **zero percent** Korean generation capability on its own.
It literally output Chinese characters instead of Korean.

Yet with RAG, it reached *78.05 percent*.

RAG doesn't just improve performance —
it can compensate for a model's complete absence of language capability.

...and the key driver is not the LLM size — it's the embedding.

---

## 🎤 Slide 5 — Embedding Matters Most `⏱ 2:40`

// Trace the before-and-after arrows in the comparison table //

Same LLM. Same data. Only the pipeline changed.

The granite4.1:8b model went from *55 percent to 82 percent*.
DeepSeek-r1:8b went from *55 percent to 78 percent*.

That is a gain of *22 to 27 percentage points*.

// Point to the longest bar in the factor decomposition diagram //

And roughly **15 to 20 percentage points** of that gain
comes from the embedding swap alone.

Choose your embedding before you tune your LLM.

...so here's what we've learned.

---

## 🎤 Slide 6 — Conclusion `⏱ 3:00`

// Point to each bullet one by one, crisp and clear //

Three things to take away.

**RAG is essential** — accuracy gain of 61 to 78 percentage points over LLM-only.

**Small models are sufficient** — a 4B gemma4 achieves 88 percent exact match.

**Embedding comes first** — swapping to BGE-m3-ko alone gives you 22 to 27 points.

// Briefly point to the red box, one sentence only //

Japanese-derived terms remain at 47 percent error — a synonym dictionary is still needed.

[ pause ]

// Point to the green closing box. Slow. Clear. No "Thank you." //

*"Privacy-safe, cost-effective, and fully deployable on-premise."*

---

---

# Full Continuous Script (Memorization & Timing Practice)

> Pure spoken text only — no stage directions.
> Read aloud and check your timing. Target: 2 minutes 50 seconds to 3 minutes flat.

---

Hello, everyone. I'm Hongchul Shin from the HDI Lab at UST-KIST.
In the next three minutes, I'll show you how we used open-source LLMs and RAG to automatically standardize messy tool-name records in a public dataset.

Seoul's public tool-rental service has 160 standard tool names in its database.
But the actual records contain 3,352 distinct entries.
The same physical tool exists under dozens of different names.
Take "drill bit set" alone — giri-set, giri set, giri-sset — all referring to the exact same item.
This lack of standardization breaks inventory tracking, usage statistics, and search — entirely.
...but the problem is more complex than simple typos.

We analyzed 457 non-standard entries in full.
The top five error types account for 78% of all cases.
Typos, brand inclusion, power-source labels, English abbreviations, and embedded attributes.
None of these can be fixed by simple rule-based methods.
Most critically: giri, ppaenchi, hamma — Japanese loanwords with a phonetic gap so large
that no embedding or BM25 index can bridge it without an explicit thesaurus.
...that's why we designed an enhanced RAG pipeline.

Our pipeline works as follows.
A raw tool name comes in. The retrieval stage fetches the top 15 candidate standard names
using a hybrid of BGE-m3-ko embeddings and BM25-FAISS search.
The local LLM then selects the best match.
If the LLM fails, a Fallback mechanism automatically returns the top-ranked candidate.
The single biggest difference from the baseline: we replaced MiniLM at 384 dimensions
with BGE-m3-ko at 1,024 dimensions. That one swap is the key.
...let me show you what this pipeline achieved.

(1–2 seconds of silence)

88.47 percent.

That is the exact-match accuracy achieved by gemma4:e4b — a model with only 4 billion parameters.
Without RAG, LLM-only accuracy was just 9 to 27 percent.
The moment we add RAG, accuracy jumps by 61 to 78 percentage points.
RAG is not optional — it is essential.
One more thing. The DeepSeek-r1 1.5B model had zero percent Korean generation capability on its own.
Yet with RAG, it reached 78.05 percent.
RAG doesn't just improve performance — it can compensate for a model's complete absence of language capability.
...and the key driver is not the LLM size — it's the embedding.

Same LLM. Same data. Only the pipeline changed.
Granite4.1:8b went from 55 percent to 82 percent. DeepSeek-r1:8b went from 55 to 78 percent.
That is a gain of 22 to 27 percentage points.
And roughly 15 to 20 points of that gain comes from the embedding swap alone.
Choose your embedding before you tune your LLM.
...so here's what we've learned.

Three things to take away.
RAG is essential — accuracy gain of 61 to 78 percentage points over LLM-only.
Small models are sufficient — a 4B gemma4 achieves 88 percent exact match.
Embedding comes first — swapping to BGE-m3-ko alone gives you 22 to 27 points.
Japanese-derived terms remain at 47 percent error — a synonym dictionary is still needed.

"Privacy-safe, cost-effective, and fully deployable on-premise."

---

# Timing Guide

| Slide | Target window | Key number | Warning sign |
|-------|--------------|------------|--------------|
| Slide 0 (Title) | 0:00 – 0:08 | — | If intro exceeds 10s, pressure builds |
| Slide 1 (Problem) | 0:08 – 0:33 | 3,352 / 160 | — |
| Slide 2 (Patterns) | 0:33 – 0:58 | 78% | — |
| Slide 3 (Method) | 0:58 – 1:33 | 1,024-dim | Easiest slide to over-explain |
| Slide 4 (Results) | 1:33 – 2:13 | **88.47%** / **+61–70pp** | Climax — do not run over |
| Slide 5 (Embedding) | 2:13 – 2:43 | +22–27pp | If past 2:45, skip factor breakdown |
| Slide 6 (Conclusion) | 2:43 – 3:00 | Three bullets | Always read the closing line |

**Emergency plan if you're still on Slide 5 at 2:45:**
→ Skip the factor decomposition entirely.
→ Say "...so here's what we've learned." and advance immediately.

---

# Transition Line Cue Cards

> Memorize these 5 lines and your delivery will never lose its flow.

```
Slide 1 → 2    "...but the problem is more complex than simple typos."
Slide 2 → 3    "...that's why we designed an enhanced RAG pipeline."
Slide 3 → 4    "...let me show you what this pipeline achieved."
Slide 4 → 5    "...and the key driver is not the LLM size — it's the embedding."
Slide 5 → 6    "...so here's what we've learned."
Closing        "Privacy-safe, cost-effective, and fully deployable on-premise."
```

---

# Delivery Checklist

- [ ] **Slide 4 entry** — Transition, hold silence 1–2 sec, then say "88.47 percent" slowly
- [ ] **"61 to 78 percentage points"** — Say it in full, no abbreviation
- [ ] **DeepSeek paradox** — Pause briefly before "zero percent" for effect
- [ ] **Closing line** — Do NOT say "Thank you." End on the closing sentence.
- [ ] **Speed** — Speak 20% slower than feels natural. The room acoustics and adrenaline demand it.
- [ ] **Pointer direction** — Always face the audience when pointing. Never turn your back.
