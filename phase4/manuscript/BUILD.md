# LaTeX Build Instructions

## Build Environment

The manuscript requires a complete LaTeX distribution with the following packages:

- `amsmath`, `amssymb`, `amsthm`, `mathtools`
- `booktabs`, `array`, `tabularx`, `longtable`
- `graphicx`, `xcolor`
- `todonotes`, `hyperref`, `cleveref`
- `natbib`, `setspace`, `titlesec`, `caption`, `subcaption`, `enumitem`
- `geometry`, `inputenc`, `fontenc`

## Compilation Commands

From the `phase4/manuscript/` directory:

```bash
# First pass (generates .aux for BibTeX)
pdflatex -interaction=nonstopmode main.tex

# Bibliography
bibtex main

# Second pass (resolves citations)
pdflatex -interaction=nonstopmode main.tex

# Third pass (resolves cross-references)
pdflatex -interaction=nonstopmode main.tex
```

Or use `latexmk` for automated multi-pass compilation:

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

## Output

- `main.pdf` — compiled manuscript
- `main.log` — compilation log (check for warnings/errors)
- `main.blg` — BibTeX log (check for missing references)

## Error Checking

After compilation, check:

1. **Undefined references:** `grep "Undefined reference" main.log`
2. **Undefined control sequences:** `grep "Undefined control sequence" main.log`
3. **Missing bibliography references:** `grep "undefined" main.blg`
4. **Overfull/underfull boxes:** `grep "Overfull" main.log`

## CI Build

A GitHub Actions workflow is configured at `.github/workflows/latex-build.yml` that:
- Installs TeX Live on Ubuntu
- Compiles the manuscript with three passes
- Checks for undefined references and missing bibliography entries
- Uploads the PDF and logs as artifacts

## Current Limitation

No TeX engine is available in the current build environment (no root access for `apt-get install`). Local compilation is not possible until a TeX distribution is installed. The CI workflow provides the automated build route when pushed to GitHub.

## File Structure

```
phase4/manuscript/
├── main.tex              # Main LaTeX file
├── frontmatter/          # Title page, abstract, notation, acronyms
├── sections/             # 17 manuscript sections (sec01-sec17)
├── appendices/           # 6 appendices (appA-appF)
├── tables/               # LaTeX table source files
│   └── source/           # T1-T8 comparison tables
├── references/
│   └── library.bib       # 67-entry validated BibTeX library
└── BUILD.md              # This file
```
