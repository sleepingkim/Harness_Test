# Smartphone Camera-Based Multimodal Biomarker Framework for AI-Driven Prediction of PCOS and Endometriosis

## IEEE Conference Paper

### File Structure

```
ieee_paper/
├── main.tex          -- Main LaTeX document (IEEEtran conference format)
├── references.bib    -- BibTeX references (31 verified entries)
└── README.md         -- This file
```

### Compilation

Requires a LaTeX distribution with IEEEtran class (included in TeX Live and MiKTeX).

```bash
# Standard compilation sequence
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

Or using `latexmk`:

```bash
latexmk -pdf main.tex
```

### Required LaTeX Packages

All packages are standard and included in TeX Live / MiKTeX:

- `IEEEtran` (document class, conference mode)
- `cite`
- `amsmath`, `amssymb`, `amsfonts`
- `algorithmic`
- `graphicx`
- `textcomp`
- `xcolor`
- `booktabs`
- `hyperref`
- `multirow`
- `array`

### References

- 31 BibTeX entries, all verified via PMID, DOI (Crossref API), or WebSearch
- Excluded: #22 (retracted paper), #32/#37 (unverifiable)
- Corrected: #19 (author corrected to Yousaf et al.), #28 (author corrected to Agirsoy et al., not directly cited in this paper)

### Paper Specifications

- Format: IEEE Conference (8 pages target)
- Language: English
- Sections: I. Introduction, II. Related Work, III. Proposed Multimodal Framework, IV. Biomarker Evaluation Results, V. Discussion, VI. Conclusion
- Tables: TABLE I (Tier classification), TABLE II (Priority matrix), TABLE III (Meta-analysis)
- Citations: IEEE numeric style [1], [2], etc.
