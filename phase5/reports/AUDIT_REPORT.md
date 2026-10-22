# Phase5 v1.1 audit report

**Audit status:** In progress; no release recommendation.<br>
**Scope examined:** source provenance, LaTeX path/static references, local conservation-law edits, selected thermoelastic equations and assertions, figure asset conversion/structure, repository baseline PDF overview, and the inherited literature inventory.<br>
**Scope not completed:** clean compile, manuscript-scale proofing, all-equation derivation, all-primary-source checking, claim-level citation review, table-by-table scientific transcription, benchmarks, journal requirements, and independent peer review.

## Executive disposition

A versioned copy was audited and partially repaired. The v1.0 source/PDF remain unchanged. Static structure checks report zero duplicate labels, unresolved cross-references, duplicate bibliography keys, missing inputs, citation keys, or figure PDFs. Eighteen SVGs were converted to vector PDFs without converter warnings; the results contain extractable text and vector drawing operators. These are engineering checks, not scientific validation. There is no successful v1.1 build or PDF: TeX tools are absent locally, and the first strict GitHub phase5 run (39728213927) failed in the combined build step with exit 12. Its detailed log artifact could not be downloaded through the signed endpoint, so the precise failure remains unknown.

The available baseline PDF is 161 pages, SHA-256 `b03dc426046a1473d3d6cf1088f9fc115c7103b4786c4eb2389ab968f640c636`, producer pdfTeX 1.40.25. It contains visible figures in the page-thumbnail survey, but shows poor appendix-table layout on multiple pages. It is not the separately described 170-page/pdfTeX 1.40.29 file, which was unavailable. Those two artifacts must not be conflated.

## Findings and disposition

| Severity | Finding | Evidence / action | Remaining gate |
|---|---|---|---|
| Critical | No phase5 compile or final PDF exists | Local TeX tools absent; scripts/strict workflow prepared but not run | Run a clean fail-fast build; preserve full log/artifacts; inspect final PDF |
| Critical | Reported 170-page artifact absent | Repository baseline is 161 pages, different producer/version metadata | Obtain/identify exact external artifact before attributing symptoms to it |
| High | Classical energy flux needed explicit sign and index convention | Derived from symmetric Cauchy stress and local momentum/internal-energy balances; corrected inconsistent free/dummy-index contractions; `J_i=q_i-sigma_ij v_j`; harmonic mechanical term uses minus sign and conjugated velocity | Sweep appendix, tables, equations, figures, and every interface normal; compile and independently review derivation |
| High | Legacy generalized energy-flux and admissibility claims exceed derivation evidence | Several formulas/assertions withheld or narrowed; no universal generalized flux asserted | Derive model-specific balances from primary constitutive systems/free energies, or leave claims clearly OPEN |
| High | Generalized-theory source claims lack primary full-text verification | GL, GN, MGT, DPL/TPL, MDD, fractional and multiphysics systems recorded with status and remaining checks | Access and compare cited primary texts equation-by-equation; citations alone are not verification |
| High | Literature metadata not claim-mapped | `literature-evidence-matrix.csv` carries 95 rows; each is `OPEN`/`UNVERIFIED`; DOI/retrieval fields are inherited only | Verify records; map each manuscript claim to evidence and source passage; check relevance/context |
| High | Appendix/table layout and technical assertions are unresolved | Thumbnail review shows baseline appendix table overflow/fragmentation; phase5 tables have not been compiled/proofed | Rework widths/landscape/splitting and inspect page-scale output |
| Medium | SVG source/licence history is undocumented | Register now discloses repository SVG provenance/licence unknown; PDFs render structurally | Establish authorship, rights, and accuracy for each figure |
| Medium | Local manuscript input paths needed portability repair | Tables and figures copied into phase5 package; static path/reference scan passes | Confirm wrappers, bibliography, `latexmk`, and CI use the same working directory |
| Medium | Fractional scalar equation had dimensionally fixed diffusivity for arbitrary derivative order | Replaced `a` with `a_alpha` and stated units `m^2 s^-alpha`; narrowed interpretation | Verify a model-specific constitutive embedding and initial-value problem |
| Medium | Spring-interface equation named stiffness but used a compliance multiplier and inconsistent limits | Recast as displacement jump equal to inverse stiffness times traction; stated stiffness units and eigenvalue limits | Verify the intended spring law, passivity, and source/model convention |
| Medium | Old appendix/register material may contradict revised sections | `equation-audit.csv` and scientific audit flag incomplete appendix sweep | Reconcile every occurrence and do not retain false legacy PASS/verified labels |
| Medium | Legacy CI green status is not a phase5 gate | Inherited workflow builds phase4 and suppressed failures with `|| true`; replacement is fail-fast | Execute strict workflow and inspect artifacts; do not cite old green run as v1.1 validation |

## Inventory outputs

- Latest static inventory: 37 TeX files; 430 labels; 293 reference commands; 56 bibliography keys; 222 citation calls; zero unresolved items in the scanned classes.
- Figures: 18/18 source SVGs parse; 18/18 requested PDF assets generated; converter reported zero warnings; each generated PDF has text and vector operators, with zero raster XObjects.
- Baseline PDF: 161 pages; seven thumbnail sheets cover pages 1–161. This overview is not text extraction or final-size proofing.
- Literature inventory: 95 records; 48 DOI cells populated, 47 blank; inherited full-text/open-access flags are not independently validated here.
- Audit register: `equation-audit.csv`; literature register: `literature-evidence-matrix.csv`; figure/licence register: `figure-audit.csv`.

## Release decision

**Do not release, submit, or call the manuscript validated.** Proceed with phases P0–P4 only as a source-audit work plan: (P0) exact source/artifact provenance; (P1) clean fail-fast compile and portable assets; (P2) source-backed scientific/equation checks; (P3) restructure, literature/citation and layout proof; (P4) independent engineering, scientific, and editorial gates. A journal source wrapper or source ZIP is not a compiled submission. A compiled PDF alone will not pass the scientific gate.
