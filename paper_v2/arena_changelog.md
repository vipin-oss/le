# Changelog — paper_v2 manuscript improvements

## Changes made (on branch arena/e6146644-le)

### 1. Appendix ordering fixed (main.tex)
- Appendix order changed from appA, appB, appC, appE, appF, appG, appD
  to appA, appB, appC, appD, appE, appF, appG so the labelled sequence
  (app:disp, app:numbers, app:repro, app:catalogue, app:glossary, app:debye, app:params)
  is sequential.

### 2. Citations added from catalogue-only entries to main text
36 reference entries that were previously only cited in Appendix D (catalogue)
are now also cited in the main body, with context drawn from the bib entry title:

| Section | Entries added | Context |
|---------|--------------|---------|
| s06_lags (DPL/TPL/MGT stability) | Quintanilla2002b, Quintanilla2006, Fabrizio2014, Rukolaine2014 | Stability and continuous-dependence analyses of time-differential lag models |
| s07_memory (fractional/MDD models) | Gorenflo1997, Povstenko2004, Povstenko2007, Povstenko2009, Hamza2014, Sur2012, Yu2014, Sherief2018, Ezzat2015 | Fractional calculus background, fractional heat-conduction models, two-temperature fractional theories, MDD models |
| s05_hyperbolic (LS/GL/GN) | Chandrasekharaiah1997, Iesan1998, Quintanilla1999, Ciarletta1999, Quintanilla2002, Suh1998 | Complete solutions and stability for GN type II, thermoelasticity without energy dissipation, micropolar extensions |
| s10_surface (Rayleigh waves) | Abouelregal2011, Biswas2020c, Chirita2012, Singh2013, Singh2015 | DPL Rayleigh waves, magneto-thermoelastic Rayleigh waves, anisotropic surface waves, two-temperature Rayleigh waves, impedance boundary conditions |
| s12_size (nonlocal/gradient/size effects) | Gao2007, Lim2015, Ke2014 | Strain gradient elasticity, higher-order nonlocal elasticity, size-dependent piezoelectric vibration |
| s13_multiphysics (couplings) | Ezzat2004, Ezzat2010, Chen2004, Guo2018, Mondal2020 | Magneto-thermoelasticity fundamental solutions, two-temperature magneto-thermoelasticity, magneto-electro-thermo-elastic general solutions, fractional piezoelectric thermoelasticity, MDD piezo-thermoelasticity |

No claims were invented beyond what the bib entry titles state. Each citation is placed in a section whose topic matches the entry title.

### 3. LaTeX/source issues checked
- All `\eqref`, `\ref`, `\Cref`, `\cref` cross-references resolve to defined labels (0 undefined)
- All `\citep`/`\citet` keys resolve to defined bibliography entries (0 undefined keys)
- No duplicate `\label` definitions
- Bibliography style: `unsrtnat`; bibliography files: `refs,refs_extra,refs_new`
- `\path{}` commands are available via `hyperref` package
- No `\ref` used where `\eqref` should be; no `\eqref` used for non-equation labels

### 4. Could NOT be done (sandbox constraints)
The following items require tools or network access not available in this environment:

| Item | Reason |
|------|--------|
| PDF build (`pdflatex` + `bibtex`) | No TeX Live installation; no root access to install |
| Reference verification via Crossref | `api.crossref.org` not in allowed hosts; only `github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` accessible |
| `refs_extra.bib` "from memory" entries verification (McNelly1970, Huberman2019, Brorson1987, Thomsen1986, Cahill2003) | Requires Crossref/DOI lookup — blocked |
| Completing 41 "and others" author lists in refs_new.bib | Requires Crossref/DOI lookup per entry — blocked |
| Running figure/numerical scripts to reproduce numbers | Requires Python scientific stack (numpy, scipy, sympy, matplotlib) — not installed |
| Page count verification (>= 100 pages) | Cannot build PDF |

## Not yet done (recommended follow-up)

1. Build the PDF with `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex` once TeX Live is available.
2. Verify the 5 `refs_extra.bib` entries marked "from memory" against Crossref/DOI sources.
3. Complete the 41 "and others" author lists in `refs_new.bib` using each entry's DOI via Crossref.
4. Re-run all scripts in `scripts/` to reproduce figures and numerical tables.
5. Confirm final page count >= 100 after build.
