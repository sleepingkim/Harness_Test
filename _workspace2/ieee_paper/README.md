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

### Version History

| Version | Date | File | Description |
|---------|------|------|-------------|
| v1.0 | 2026-04-12 | `main.tex` | Initial IEEE paper (Anonymous Authors) |
| v1.1 | 2026-04-12 | `main_v1.1_tikz-figures.tex` / `한국실용인공지능학술지_v1.2_largefont.docx` | TikZ 시스템 구조도 추가; 한국어 저자 더미(홍길동·김철수) |
| v1.2 | 2026-04-16 | `main_v1.2_author-info.tex` / `한국실용인공지능학술지_v1.3_author-info.docx` | 저자 정보 업데이트: 신홍철 (Hongchul Shin), 과학기술연합대학원대학교(U.S.T) / University of Science and Technology, neohc@ust.ac.kr |

### Paper Specifications

- Format: IEEE Conference (8 pages target)
- Language: English
- Sections: I. Introduction, II. Related Work, III. Proposed Multimodal Framework, IV. Biomarker Evaluation Results, V. Discussion, VI. Conclusion
- Tables: TABLE I (Tier classification), TABLE II (Priority matrix), TABLE III (Meta-analysis)
- Citations: IEEE numeric style [1], [2], etc.
