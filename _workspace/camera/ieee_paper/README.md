# IEEE Paper: Smartphone Camera-Based Digital Biomarkers

## File Structure

```
ieee_paper/
├── main.tex        -- Main LaTeX source (IEEEtran conference format)
├── references.bib  -- BibTeX references (34 verified entries)
└── README.md       -- This file
```

## Compilation

### Requirements

- TeX distribution: TeX Live 2022+ or MiKTeX
- Required packages (included in standard TeX Live):
  - `IEEEtran` document class
  - `cite`, `amsmath`, `amssymb`, `amsfonts`
  - `graphicx`, `textcomp`, `xcolor`
  - `booktabs`, `hyperref`, `multirow`, `array`

### Build Commands

Using `pdflatex` + `bibtex`:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

Or using `latexmk` (recommended):

```bash
latexmk -pdf main.tex
```

### Clean Build

```bash
latexmk -C
```

## Notes

- The paper follows IEEE conference format (2-column, 8 pages).
- All 34 references have been verified against the reference validation report.
- Two hallucinated references (#12 anemia ViT, #20 OSA JMIR) are excluded.
- Eight partially verified (caution) references are noted in the validation report but included with corrected metrics where applicable.
