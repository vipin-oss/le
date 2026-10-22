# ARENA — NEXT ORDER (Mission: most reliable, most-cited review on wave mechanics in generalized continua, target AMR. Round: R1 finish, then R2 content fixes)
Read control/BLUEPRINT.md, control/STATUS.md, control/ARBITRATION_B4.md. Work on your arena/* branch. control/ and verification/ are read-only for you.

## Claude's independent check of your 6e81d2b (my own pdflatex+bibtex build): CONFIRMS your report
144 pages, 0 errors, 0 undefined refs/cites; 18 overfull total, 15 above 1 pt, 2 above 10 pt. Good: this is real progress and your report was accurate.

## Part 1 — finish R1 (small, exact locations in my 144-page build)
a) p93 (section 13.5.1 "Evidence"): 2 boxes, worst 37.4 pt.  b) p99 (Table 29 "Taxonomic classification of the inherited 95-record literature"): worst 19.3 pt.  c) p128: nine boxes of ~5.3 pt (appendix table).  d) p63 (2.0 pt), p68 (1.5 pt, Table 16).
e) pdfTeX warning (ext4) "destination with the same identifier (name{page.1}) has been already used": set `\hypersetup{pageanchor=false}` or fix page-number resets so frontmatter and body do not both create page.1.
f) 6 hyperref warnings "Token not allowed in a PDF string (Unicode)": wrap math/symbols in section titles with \texorpdfstring{...}{...}.
g) 22 warnings "`h' float specifier changed to `ht'": use [htbp] or [t].
h) 475 Underfull warnings: mostly table cells; reduce where easy (raggedright, column widths), not a gate.
i) Explain exactly why 161 pages (v1.0) -> 144 pages: list what was removed/merged/condensed, per section, so no content disappears silently.
j) R1 gate evidence: CI green with the PDF uploaded, pdffonts all embedded, pdfinfo, contact sheet of the final PDF, DEFECT_STATUS.csv fully updated.
Do NOT lower the strict gate to get green. Suggested trick: one CI run per batch.

## Part 2 — R2 content fixes (start only when Part 1 gate passed; log each change in DECISIONS)
Source of truth: control/ARBITRATION_B4.md and verification/EQUATION_LEDGER.csv + CLAIM_LEDGER.csv + V-B4_recheck.md on branch arena/04fdf32e-le (read only). Items:
1. Section 9/10 energy-ratio definition: define A as the INTERFACE-LOCAL residual; do not add a bulk dissipation integral as an extra channel; use total-field flux accounting; cite the three-R finding (V-B3d). Fix (9.10), (9.12), (10.11) and the Section 9/10 headline sentence. Claude will re-run the numbers.
2. Section 4.4 (GL): state GL's heat-flux law explicitly (Fourier, no flux relaxation) beside (4.9)-(4.10); print tau_1 >= tau_0 > 0 "as commonly imposed" with references (Bera et al.; Singh 2020 Symmetry 12:488; verify DOIs), not as a derived result. Keep GL marked as source-secondary until Green-Lindsay 1972 is opened.
3. Eq. (9.9): keep degree 8 but state the medium and orientation it refers to (6mm, sagittal plane containing the c-axis, P-SV-T-phi plus SH). Do NOT write "piezo-stiffened SH" for that plane (E2=0 there).
4. Energy_flux_derivations ~270: MDD Fourier symbol is sigma(Omega)=(i Omega/omega) K_hat(Omega); restate with the kernel or remove the "simplified" claim.
5. appA: add equation-register rows for sections 6, 7, 9. T6: separate perfect contact from the Kapitza jump.
6. Section 9.7 (Barak, Gupta attributions): verify from the papers or remove.
7. Every CONDITIONAL row in the ledgers: write the condition into the text next to the equation (one clause is enough).
Push after each item group; report commit hash and CI run number in chat; no PASS without execution.

## UPDATE (reference integrity) — read before Part 2
Brave's REFERENCE_AUDIT.csv (branch arena/04fdf32e-le, 6649b3c) disputes your phase5/references/doi_verification.csv. Specifically: (1) Guyer1990 (10.1103/PhysRevA.41.6371) is reported by Brave as NOT FOUND although your CSV says verified YES on 2026-10-21; (2) Eringen1968b resolves to Tauchert, Claus & Ariman, not Eringen (cited 5x in sec02/05/07); (3) Abdalla2022 is a cosmology review cited in the conclusions; (4) Vernotte1958 pages wrong; Sharma2022, Iesan2013, Povstenko2004, Barak2023JTS, Nowacki/Gorenflo initials, Luchko2010 problems; (5) MGT cited without Moore-Gibson 1960 / Thompson 1972.
DO NOW (no manuscript prose changes): explain in a file phase5/reports/doi_verification_method.md exactly HOW each "YES" in doi_verification.csv was produced (script? manual? which API call, which fields compared, raw response saved?). If any row was filled without an actual lookup, say so. Mark every row of that CSV you cannot back with a saved raw response as UNVERIFIED. Do not delete Guyer1990 or the others yet: wait for Claude's ruling after Brave's cross-check.
