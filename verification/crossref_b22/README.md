# B22 Crossref raw responses

Saved during the BRAVE B22 verification pass (2026-10-27). Query host:
`api.crossref.org`. Only key payload fields are reproduced where the full
payload exceeded the working buffer; each file records exactly what was read.

| file | DOI | result |
| --- | --- | --- |
| `10.1080_01495739.2010.511931.json` | 10.1080/01495739.2010.511931 | Povstenko, *Fractional Cattaneo-Type Equations and Generalized Thermoelasticity*, J. Thermal Stresses **34**(2):97-114 (2011). **Distinct from** the `.511929` Dirichlet-problem article (34(1):51-67). The manuscript bib carries both correctly. |
| `10.1080_713855996.json` | 10.1080/713855996 | Quintanilla, *A Condition on the Delay Parameters in the One-Dimensional Dual-Phase-Lag Thermoelastic Theory*, J. Thermal Stresses **26**(7):713-721 (2003). This is the DOI printed on the cover page of the held source PDF (`pdfs/quintanilla2003.pdf`). |
| `10.1080_01495730390203518.json` | 10.1080/01495730390203518 | **No Crossref record returned** for this DOI (both a direct lookup and a `filter=doi:` query). It is the DOI currently carried by bib key `Quintanilla2003DPL`. |

The 20-entry random bib sample was checked in one batched request; the
per-entry comparison is recorded in `../B22_BIB_SPOTCHECK.csv` (all 20 matched
title/first-author/volume/pages).
