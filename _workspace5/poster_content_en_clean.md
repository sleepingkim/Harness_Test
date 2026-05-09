# Poster Content (English) — Tool Name Standardization: LLM+RAG Experiment

> **File scope:** Practicum-independent. GT v2 new experiments only.
> **Experiments:** RAG v2 pipeline (12 models) + LLM-only Zero-shot (4 models)
> **Date:** 2026-05-09

---

## [Title]

**Automated Standardization of Tool Names in Seoul Public Tool Rental Data: An Open-Source LLM + RAG Pipeline Evaluation**

---

## [1] Problem Definition

Seoul operates a municipality-run public tool rental service that allows citizens to borrow tools from district offices across the city. The dataset underlying this service contains 3,352 tool name entries, yet only approximately 160 distinct standard tool names are intended to be represented. Because field staff enter tool names freely without a controlled vocabulary, each physical tool type accumulates dozens of divergent surface forms in the database. Representative examples include 유선전동드릴 (Wired Power Drill) being recorded instead of the standard 전동드릴 (Power Drill), 기리셋트 (a phonetic corruption of the Japanese loanword for drill bit set) in place of 드릴비트세트 (Drill Bit Set), and 함마드릴 (a mixed Japanese–Korean romanization) instead of 해머드릴 (Hammer Drill).

The practical consequences of this inconsistency are severe. Without name standardization, inventory reconciliation across district offices is unreliable, cross-district statistical aggregation is impossible, and any automated reporting or demand-forecasting system is rendered invalid. Manual cleaning is not scalable given the ongoing nature of data entry. This work therefore investigates whether an open-source large language model (LLM) augmented with retrieval-augmented generation (RAG) can automate the normalization of these non-standard tool names to their canonical standard forms.

---

## [2] Dirty Data Taxonomy

To characterize the scope and structure of the problem, 457 non-standard tool name entries were labeled according to the type of deviation from the standard form. Typos and misspellings constitute the single largest category at 155 instances (33.9%), exemplified by 경랑몽키 (incorrect vowel substitution) and 막치 (dropped consonant). Brand names embedded in the tool name account for 71 cases (15.5%), such as 보쉬전동드릴 (Bosch Power Drill), which conflates a manufacturer identifier with the generic tool name. Power source specifications add 50 cases (10.9%), for example 유선전동드릴, where a wired/cordless qualifier obscures the base tool identity. English abbreviations appear in 41 entries (9.0%), including HSS드릴비트 and PIPE렌치, while attribute values such as 180mm그라인더 account for 40 cases (8.8%). The remaining four categories — Japanese loanwords, metadata tags, set/kit names, and symbol-containing entries — together comprise 100 cases (21.9%). Collectively, the top five categories account for 78.1% of all labeled samples, establishing a clear hierarchy of error types that any standardization system must address in priority order.

---

## [3] RAG v2 Pipeline

The RAG v2 pipeline was designed to supply small open-source LLMs with a constrained candidate set of standard tool names, thereby transforming the problem from open-ended text generation into candidate selection. The pipeline begins by encoding each non-standard input using dragonkue/BGE-m3-ko, a 1,024-dimensional Korean embedding model that ranked first on the KURE Korean retrieval benchmark. Candidate retrieval employs a hybrid strategy combining BM25 syllable bigram matching (weighted 40%) with FAISS dense semantic search (weighted 60%), returning k=15 candidates per query. Tool category and subcategory metadata are then injected into the LLM prompt to provide structural context. The LLM selects the single best standard name from the candidate list, and a fallback rule automatically replaces any output that falls outside the candidate pool with the RAG top-1 result, eliminating hallucination of entirely novel names.

The baseline configuration used for comparison employs paraphrase-multilingual-MiniLM-L12-v2 (384-dimensional embeddings), FAISS-only retrieval without BM25, and k=5 candidates. Holding the LLM constant (deepseek-r1:8b), upgrading from the baseline to the improved pipeline yields an accuracy gain of +22.6 percentage points (55.21% to 77.83%), demonstrating that the retrieval infrastructure itself — independent of LLM choice — is the dominant performance driver.

---

## [4] Results

### 4.1 Overall Model Performance (12 Models)

Twelve model configurations were evaluated on 451 test samples drawn from the GT v2 ground-truth set. All nine improved-configuration models outperformed every baseline-configuration model, confirming that the BGE-m3-ko embedding and expanded candidate pool are consistently beneficial across LLM architectures. Among improved models, gemma4:e4b achieved the highest accuracy at 88.47% (399/451), followed by gemma3:4b at 84.48% (381/451) and granite4.1:8b at 82.48% (372/451). The remaining improved models ranged from 80.93% (gemma4:e2b) down to 67.85% (granite4.1:3b). Notably, deepseek-r1:1.5b achieved 78.05% (352/451) under the improved configuration, with 85.2% of its correct answers attributable to the fallback mechanism. Both baseline configurations (granite4.1:8b and deepseek-r1:8b) plateaued at 55.21%, while qwen3.5:9b under baseline produced a 0.00% accuracy rate due to 100% output errors, reflecting catastrophic incompatibility between the baseline retrieval configuration and that model's decoding behavior.

### 4.2 Performance by Dirty Data Type

Analyzing the top-performing model (gemma4:e4b) across dirty data categories reveals that the RAG pipeline provides the greatest absolute benefit precisely where LLM-only generation fails most severely. For entries specifying power source, RAG accuracy reached 96.4% compared to 8.0% for LLM-only generation, a gain of +88.4 percentage points. Typos and misspellings — the most frequent category at 33.9% of the data — achieved 93.8% under RAG versus 21.9% LLM-only (+71.9pp). Brand-name entries improved from 28.2% to 87.5% (+59.3pp), and English abbreviations from 24.4% to 82.5% (+58.1pp). The one category where RAG accuracy remains structurally limited is Japanese loanwords, which reached only 47.1% despite a +28.0pp improvement over the 19.0% LLM-only baseline. This ceiling reflects a phonetic discontinuity problem: terms such as 기리 (from Japanese 錐, kiri) bear no syllabic resemblance to their standard Korean equivalent 드릴비트 (drill bit), causing both embedding cosine similarity and BM25 bigram overlap to fail in retrieval.

### 4.3 LLM-only Zero-shot Comparison

To isolate the contribution of RAG from LLM capability, four models were evaluated under both zero-shot LLM-only and full RAG conditions. Without RAG, exact-match accuracy ranges from 9.4% (exaone3.5:7.8b) to 27.4% (gemma4:e4b), establishing that even the strongest model in this study cannot reliably produce standard tool name spellings from open-ended generation alone. However, nearest-match accuracy — which credits the model when it produces a semantically proximate but non-identical form — reaches 60–63% across models, indicating that LLMs do possess the conceptual knowledge of what the correct tool is, but lack the ability to reproduce the exact canonical surface form. RAG resolves this gap by anchoring generation to a constrained candidate pool: gemma4:e4b improves from 27.4% to 88.5% (+61.1pp), gemma3:4b from 23.0% to 84.5% (+61.5pp), and exaone3.5:7.8b from 9.4% to 79.2% (+69.7pp). The deepseek-r1:1.5b model is a particularly instructive case: LLM-only accuracy is 0.0% not because of an API error but because the model lacks Korean free-generation capability and produces Chinese-language output. Under RAG, candidate selection replaces generation entirely, and the model achieves 78.4% accuracy — demonstrating that RAG can bypass fundamental language generation limitations of small models.

---

## [5] Key Findings

The most consequential finding of this study is that RAG is not merely beneficial but essential for production viability. LLM-only zero-shot accuracy spans 9–27% across evaluated models, a range that is entirely unsuitable for operational deployment. The addition of the RAG pipeline raises accuracy to 79–88%, a gain of +61 to +70 percentage points that crosses the threshold from non-viable to practically deployable. This finding holds uniformly across all four architectures tested, regardless of model size or family.

The mechanism by which RAG achieves this gain is output anchoring rather than knowledge augmentation. The nearest-match accuracy of 60–63% demonstrates that LLMs correctly understand which tool a non-standard name refers to; the failure is in surface-form reproduction, not semantic comprehension. RAG supplies the candidate pool that bridges semantic understanding to exact string matching, functioning as a spelling-correction oracle rather than a knowledge source. This distinction has architectural implications: the quality of retrieval — specifically the ability to surface the correct standard name among k candidates — is the binding constraint on system performance.

The embedding model is accordingly identified as the single most impactful design variable. Replacing MiniLM (384-dim) with BGE-m3-ko (1,024-dim) produces a +22 to +27 percentage point improvement across model configurations, a larger gain than any LLM architecture choice within this study. The practical mechanism is Korean morphological sensitivity: BGE-m3-ko's training on Korean corpora enables it to recognize that 경랑몽키 and 경량멍키 are corrupted forms of the same standard tool name, while MiniLM's multilingual embedding space conflates superficially similar but semantically distinct Korean syllable sequences. Japanese loanwords represent the structural ceiling of the current system at 47.1%, because phonetic discontinuity between loanword forms (기리, 함마, 뺀치, 니빠) and their standard Korean equivalents (드릴비트, 해머, 펜치, 니퍼) places correct candidates entirely outside the effective retrieval range of both embedding similarity and BM25 bigram overlap. An explicit synonym dictionary is the only viable remedy for this category.

---

## [6] Future Directions

Three targeted improvements are proposed based on the structural failure modes identified in this study. First, a Japanese-origin loanword synonym dictionary covering approximately 20–30 phonetic pairs (기리→드릴비트, 함마→해머, 뺀치→펜치, 니빠→니퍼, and related terms) would be injected directly into the retrieval index, bypassing the embedding similarity gap. This intervention is expected to raise Japanese loanword accuracy from its current 47.1% ceiling by +30 to +40 percentage points. Second, introducing an English subword tokenizer into the BM25 component would enable cross-lingual lexical matching between English abbreviation tokens (e.g., PIPE, HSS) and their Korean phonetic equivalents (파이프, 에이치에스에스), addressing a category currently limited to 82.5% accuracy at an estimated +5 to +10 percentage point gain. Third, a Human-in-the-Loop review queue based on model confidence scores would route low-confidence predictions — particularly from the heterogeneous "Other" category currently at 66.7% accuracy — to expert review, providing a systematic quality assurance mechanism for edge cases that fall outside the taxonomy's defined categories.

---

*Evaluation set: GT v2 (457 labeled pairs, 451 test items) | Pipeline: BGE-m3-ko (1024-dim) + BM25 syllable bigram / FAISS hybrid + k=15 | Date: 2026-05-09*
