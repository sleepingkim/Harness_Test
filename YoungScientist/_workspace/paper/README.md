# AmoUni-SoccerTrack — IEEE Conference Paper (Draft)

This folder contains the LaTeX sources for the CVPR 2027 CVSports Workshop submission titled:

**"AmoUni-SoccerTrack: Amodal Perception, Uniform-Aware Re-Identification, and Uncertainty Propagation for Robust Single-Camera Soccer Player Identification under Occlusion"**

The paper targets the IEEE Conference two-column format (IEEEtran) and is designed to compile to approximately 8 pages (6 pages main text + 2 pages references).

---

## 1. Files

| File            | Purpose                                                      |
|-----------------|--------------------------------------------------------------|
| `main.tex`      | Main LaTeX document (all sections I–VI + abstract + biblio). |
| `references.bib`| BibTeX database (35+ entries, IEEE style).                   |
| `README.md`     | This file — compilation, dependencies, TODO lists.           |

No figures are shipped; the draft uses `\framebox` placeholders (see Section 3 below for the figure TODO list).

---

## 2. Compilation

The document uses the standard IEEEtran conference class. Any recent TeX Live / MiKTeX distribution ships with `IEEEtran.cls` — no manual download required.

### 2.1 Quick path (latexmk, recommended)
```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

To clean aux files:
```bash
latexmk -C
```

### 2.2 Manual path (pdflatex + bibtex)
```bash
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Two `pdflatex` passes after `bibtex` are needed for cross-references and the IEEE bibliography style to settle.

### 2.3 Overleaf
Upload `main.tex` and `references.bib` into a new Overleaf project, select compiler **pdfLaTeX**, and ensure `IEEEtran.cls` + `IEEEtran.bst` are available (default on Overleaf).

---

## 3. Dependencies (LaTeX packages)

Used in `main.tex`:

- `IEEEtran` (document class, conference mode)
- `cite`
- `amsmath`, `amssymb`, `amsfonts`
- `algorithmic`
- `graphicx`
- `textcomp`
- `xcolor`
- `booktabs`
- `array`
- `multirow`
- `url`

All are part of a standard TeX Live install. No custom `.sty` files are required.

`hyperref` is optional and is currently commented out — enable it only if the target venue allows PDF links in the submission PDF (CVPR CVSports typically allows it for the camera-ready version).

---

## 4. Figure TODO list

Each `\framebox[\linewidth][c]{...}` placeholder in `main.tex` must be replaced with a real figure before submission. Target files live under `figs/`:

| Ref         | Placeholder file             | Content                                                                                                                                       |
|-------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `fig:arch`      | `figs/architecture.pdf`         | Fig. 2 — Overall AmoUni-SoccerTrack architecture (detector → amodal head → motion/association → uniform Re-ID → jersey → uncertainty fusion). |
| `fig:amodal`    | `figs/amodal_head.pdf`          | Fig. 3 — Soccer-Amodal Head internal structure with pose-prior injection and uncertainty regression.                                          |
| `fig:reid`      | `figs/uniform_reid.pdf`         | Fig. 4 — Uniform-aware Re-ID diagram (global + part + jersey-region branches; intra-team contrastive triplet sampling).                       |
| `fig:unc`       | `figs/uncertainty_graph.pdf`    | Fig. 5 — Tracklet uncertainty graph (β edges + log-linear opinion pooling).                                                                    |
| `fig:qual`      | `figs/qualitative.pdf`          | Fig. 6 — Qualitative comparison vs Deep-EIoU+GTA on three occlusion scenarios (tackle / corner-kick scrum / long recovery).                   |
| `fig:footpass`  | `figs/footpass_f1_curve.pdf`    | Fig. 7 — FOOTPASS F1@τ=0.15 vs occlusion rate; TAAD (binary mask) vs TAAD + Ours (continuous mask + uncertainty).                             |

Also consider a **Fig. 1 (graphical abstract)** on page 1 summarizing the three contributions (amodal + uniform + uncertainty). Insert it above `\section{Introduction}` with `\begin{figure}[t]\centering...\end{figure}`.

Recommended export: vector PDF (tikz or Inkscape); minimum 300 dpi if raster is unavoidable; keep each figure ≤ column-width (3.33 in) where possible for readability.

---

## 5. Where to fill in experimental numbers

The draft uses `TBD` as a placeholder for every quantitative result. The numbers to be filled in once the runs finish:

| Location in `main.tex` | What to fill                                                                                        | Source runs                                   |
|------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Sec. IV-D `Table \ref{tab:main-track}` (Comparison with Baselines) | HOTA, IDF1, AssA, Occ-HOTA for B1–B6 and our two variants | SoccerNet-Tracking test split; 3 seeds (42, 123, 2024); TrackEval |
| Sec. IV-D `Table \ref{tab:main-footpass}`                           | F1@τ=0.15 val / challenge for TAAD, TAAD+GNN, TAAD+DST with/without our mask | FOOTPASS `evaluation.py` (val) + Codabench server (challenge) |
| Sec. IV-E `Table \ref{tab:ablation}`                                 | HOTA / Occ-HOTA / ECE for Full, A1, A2, A3, A5, A10 | SoccerNet-Tracking val split; same seeds |
| Sec. V (Discussion) — "Expected numerical gains" paragraph          | Replace "expected" phrasing once real numbers land | Same as Tables 1–3 |
| Abstract — `$\Delta\text{F1} \geq +2\%$` and `+5$\sim$10\%`         | Update abstract with measured values if they differ meaningfully | Same as Table 2 and Occ-HOTA column |

Until those runs are done, keep the wording "expected" / "target" to avoid overclaiming. All target figures currently in the draft are explicitly marked as expected (see `\label{sec:discussion}`), which matches the reviewing norms for workshop papers.

Suggested extra tables (move into supplementary if page budget is tight):
- Per-occlusion-bin HOTA/IDF1 (0–20 / 20–50 / 50–80 / 80+ %).
- Calibration curve (ECE vs bin count) for the full system vs A5 (w/o uncertainty propagation).
- Cross-domain transfer: Occluded-Duke mAP/Rank-1 for Uniform-aware Re-ID vs baseline.
- Long-clip (45-min) ID switch count on SoccerNet-Tracking half-time sequence.

---

## 6. FOOTPASS-specific notes (Section III-F)

The integration recipe in Sec. III-F relies on:

1. Training TAAD with FOOTPASS `train_TAAD_Baseline.py` unchanged, but consuming a 2-channel mask tensor `[M_vis, 1 - u_a]` instead of the original binary mask.
2. Generating the new mask tensor offline with the frozen AmoUni-SoccerTrack checkpoint.
3. Running `python run_TAAD_on_matches.py` on val/challenge sets with `--mask-source ours` (to be added to the fork of FOOTPASS).
4. Converting predictions via `NPpreds2JSON.py` and evaluating with `evaluation.py --predictions_file ours.json --ground_truth_file playbyplay_gt.json` for the val split.
5. Uploading `ours_challenge.json` to the Codabench server for the hidden challenge split.

Video access requires the SoccerNet NDA. The paper mentions that pre-computed mask tensors will be released separately under a more permissive license to aid reproducibility.

---

## 7. Style / submission checklist

- [ ] Figures 1–7 inserted and captioned.
- [ ] All `TBD` entries replaced with numbers or clearly marked as "expected".
- [ ] Author block revealed (single-blind / camera-ready only).
- [ ] Page count ≤ 8 (6 + 2 refs) verified with `\pageref`.
- [ ] Grammar / spelling pass (Grammarly, Hemingway, or co-author review).
- [ ] `references.bib` sanity-checked for duplicates and missing fields.
- [ ] `\cite{...}` coverage audit: every bib entry is cited at least once.
- [ ] Reference hallucination pass (using the `reference-hallucination-guard` skill) before submission.
- [ ] PDF passes IEEE PDF eXpress (embedded fonts, no bookmarks issue).
- [ ] Supplementary material (video + code link) prepared separately if allowed.

---

## 8. Versioning

- **Draft v0.1** (2026-04-16): initial draft covering Sections I–VI; 8-page skeleton with all equations and placeholder figures/tables. Numerical results pending Phase 5 runs.
