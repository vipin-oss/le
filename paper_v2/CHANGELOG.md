# Manuscript audit — 2026-10-30 (incomplete)

**Not submission-ready.** This is a partial reproducibility and bibliography
audit, not the requested comprehensive technical review. The PDF is the
unchanged 119-page build from `review-paper-v2` (commit `3fd9e228`), not a
build of the updated source archive. It does not reflect the source and script changes below.

## Reproducibility

- The supplied ZIP had no `figs/` directory, despite 23 figure PDFs being
  referenced. Ran the figure/numerical scripts and included all 23 generated
  PDFs and corresponding PNGs in the revised archive. No comparison with the
  original PDF's embedded figures has been made.
- Ran 35 check, benchmark, figure, table and standalone scripts with Python
  3.11.2 and the versions recorded in `README_REPRODUCE.md`. All 35 initially
  exited zero, but this is **not** evidence that every calculation passed:
  several scripts only print results, and the Lamb scripts masked errors.
  Captured outputs are in `audit_logs/`; `initial-status.txt` refers to the initial run. After the changes, all 35 scripts exited zero in the final run, with the limitations above.
- All three generated TeX tables match the originals byte-for-byte. The
  symbolic dispersion check printed `det - mine = 0`; reduction checks printed
  OK. Other numbers and every manuscript claim have not been independently
  checked against the scripts or primary sources.
- The original `lamb_te.py` converged to a nonpropagating root rather than
  the claimed elastic Rayleigh–Lamb root. Replaced the one-point Muller search
  with a secant search and added an independently evaluated antisymmetric
  Rayleigh–Lamb secular equation: at `kh=0.3`, `eps=1e-8` the determinant
  yields `0.04426280007608594 - 1.40e-12 i`, versus `0.04426280007606225`
  from the elastic equation. This is one case, not a validation over the
  entire parameter space.
- The original Lamb-figure script silently produced NaN at `kh=3.16979` (one
  of 46 points). A linear-continuation fallback finds a finite root there and
  reports its use; any remaining missing root makes the script fail. Full
  branch tracking is not independently verified. The manuscript source now
  qualifies these results; its new figure is not in the old PDF.
- Added `scripts/reproduce.py`, which runs scripts in their intended working
  directory and saves logs; the figure-saving helper now creates `figs/`.
- LaTeX/BibTeX were not installed. Debian package servers and the GitHub
  release-asset download were inaccessible from the sandbox; therefore the
  requested four-pass build was **not run** and the revised source page count,
  warnings, and compiled PDF are unknown.
- `scripts/gen_refs_new.py` requires missing `refwork/lines.txt` and
  `refwork/inventory_dec.csv`; its input data were not present in the archive.
  The catalogue generator is excluded from the harness because it overwrites
  the catalogue and does only keyword classification.

## Crossref spot-check of `refs_extra.bib`

Compared title, author list, journal, year, volume and pages with Crossref and
added the following matching DOI fields. This is a metadata check, not a
verification of scientific claims or full-text contents. DOI links point to the
Crossref records and are intentionally listed so the checks are auditable.

| Key | Crossref DOI |
|---|---|
| Ackerman1966 | [10.1103/PhysRevLett.16.789](https://api.crossref.org/works/10.1103/PhysRevLett.16.789) |
| Jackson1970 | [10.1103/PhysRevLett.25.26](https://api.crossref.org/works/10.1103/PhysRevLett.25.26) |
| Zener1937 | [10.1103/PhysRev.52.230](https://api.crossref.org/works/10.1103/PhysRev.52.230) |
| Lifshitz2000 | [10.1103/PhysRevB.61.5600](https://api.crossref.org/works/10.1103/PhysRevB.61.5600) |
| McNelly1970 | [10.1103/PhysRevLett.24.100](https://api.crossref.org/works/10.1103/PhysRevLett.24.100) |
| Huberman2019 | [10.1126/science.aav3548](https://api.crossref.org/works/10.1126/science.aav3548) |
| Brorson1987 | [10.1103/PhysRevLett.59.1962](https://api.crossref.org/works/10.1103/PhysRevLett.59.1962) |
| Thomsen1986 | [10.1103/PhysRevB.34.4129](https://api.crossref.org/works/10.1103/PhysRevB.34.4129) |
| Cahill2003 | [10.1063/1.1524305](https://api.crossref.org/works/10.1063/1.1524305) |
| Kaminski1990 | [10.1115/1.2910422](https://api.crossref.org/works/10.1115/1.2910422) |
| Pennes1948 | [10.1152/jappl.1948.1.2.93](https://api.crossref.org/works/10.1152/jappl.1948.1.2.93) |

Crossref's record for [Mitra1995](https://api.crossref.org/works/10.1115/1.2822615)
spells the third author's surname `Vedevarz`, whereas the manuscript has
`Vedavarz` and other citing sources use both spellings. This conflict is not
resolved by the present audit; the entry is left unchanged pending a check of
the original publication. The other 20 entries in `refs_extra.bib` were not
checked in this audit. Crossref searches can return later reprints, as with
Pennes, so publication year/volume/pages were checked before choosing the DOI.

## Remaining work

- Independently validate the Lamb determinant and root branch across the
  parameter range; examine every numerical claim and plot.
- Verify every field in the other 20 `refs_extra.bib` entries, and all
  `refs.bib` and `refs_new.bib` records and claims against primary publications.
  41 `refs_new.bib` author fields explicitly contain `and others`; none was
  completed in this audit. Records without that string are not thereby verified.
- Manually review catalogue relevance/classification and main-text discussion;
  keyword-based classification is insufficient. No entries were removed and
  no further-reading papers were newly discussed without full-text review.
- Select a journal and apply its current author instructions; edit the entire
  paper for consistency and technical accuracy. Build and inspect all pages,
  bibliography, figures, tables and warnings; confirm the final build is at
  least 100 pages. Replace the old PDF only with a verified new build.
