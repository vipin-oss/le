# B23 remediation report

**Audit source:** read-only B23 artifacts from audit commit `9ffab514b6b3ae8b652150dba8dd851dcb747536`, which examined manuscript commit `4caa9a89d68b058aca6a340704242b08b5498a2a`.

**Remediation:** content commit `a9348cb1c337788765722905beda5009699e1dc5` on `arena/b5e608f8-le`. CI run [40553021209](https://github.com/vipin-oss/le/actions/runs/40553021209) passed. The workflow published output in commit `537c6d5327a7b9354a1e4a086464550502bdbaff`; the local branch was fast-forwarded and matched `git ls-remote`. No audit-branch push or external submission occurred.

## Findings and disposition

| Finding | Status | Disposition |
|---|---|---|
| P1-1 — exact classical Eulerian energy balance omitted advection; prior check was tautological | **FIXED** | Sections 3 and 10, abstract, appendix/register, tables, and decisions now distinguish exact $F_i=q_i-\sigma_{ij}v_j+\mathcal{E}v_i$ from the explicitly first-order reduced $J_i=q_i-\sigma_{ij}v_j$. `verify_classical_flux.py` derives material and Eulerian residuals from independent field balances, tests the omitted-flux residual, gives a nonzero counterexample, and checks dimensions. The reduced flux is not claimed as an exact or general second-order mean flux. |
| P1-2 — expected fresh-evidence roster and source accessibility | **SCOPE CLARIFIED; PARTIAL DISAGREEMENT** | The exact ledger query `evidence_mode` containing `2026-10-27` returns **4** rows: OCL-195/207/404/405, not an approximately 20-row roster. No separate 20-row list is present in the active repository; none was reconstructed or invented. The source-unavailability verdict is contradicted for Mindlin (printed pp. 625–626), Biot (pp. 241–242), and Barak (p. 3), which were reopened and checked; Kumar (2023) was reopened at p. 1, while p. 17 remains supported by the existing same-date page-read record. Ledger entries now state the page ranges and the precise access limits. |
| F1 — Table 23 DPL-to-LS limit | **LANDED** | The qualified substitution $\tau_T\to0$ with $\tau_q=\tau_0$ remains; the incorrect $\tau_q\to0$ limit is not asserted. |
| F2 — Quintanilla DOI conflict | **LANDED; DISAGREEMENT PRESERVED** | DOI conflict remains `verified=NO` / unresolved in the saved record; no conflicting source identity was promoted. |
| F3 — interface cross term | **LANDED** | The displayed 1-D incident/reflected mixed phasor product is derived and its zero mean flux is limited to the lossless longitudinal example. The unsupported coupled-system numerical example and process-reference prose were removed. |
| F4 — incident/reference-plane power definitions | **LANDED** | $P_i,P_r,P_t$ are defined as signed modal-flux contributions at stated planes with $+x$ orientation; any remaining incident–reflected cross term must be included. The remote residual is separated from the local interface residual. |
| F5 — Appendix A equation register | **LANDED** | Energy entries now distinguish the exact Eulerian flux from the reduced first-order flux and record the Section 10 displays. |
| F6 — internal artifact references in print | **LANDED** | Work-package labels, “saved audit” wording, and unpointed verification-script references were removed from manuscript text. The workflow now counts these patterns and internal paths as separate forbidden categories. |
| P2-1 — `\\&amp;` in bibliography | **FIXED** | All eight malformed journal strings were corrected to `\\&`; structural reference-hygiene check passes. |
| P2-2 — TPL first-order residual absent | **FIXED** | The first-order Taylor residual is printed after Eq. 4.17; Table T2 points to it. Its first-order scope and negative substitution check are recorded, and the equation inventory includes the unnumbered display. |
| P2-3 — internal artifact wording | **FIXED** | Removed from manuscript; strict PDF internal-artifact count is 0. |
| P2-4 — remote-plane powers not reconstructible | **FIXED** | Modal flux integrals, signs, normal direction, reference-plane requirement, and cross-term caveat are explicit. |
| P2-5 — bibliography locator/title metadata | **FIXED / QUALIFIED** | Das2026 and Maranganti2006 no longer print uncorroborated page fields; their article-number notes say the Crossref locator is unverified and both entries remain `verified={NO}`. Eringen1966a remains `ARBITRATED` with `source={ARBITRATED/OCR}`. Exact-field search for `verified={NO}` together with `source={ARBITRATED}` returned no entries. |
| P2-6 — stale missing-source wording | **FIXED / NARROWED** | Six records now distinguish DOI resolution, source-index search scope, pages actually reviewed, and what remains unestablished. DOI resolution is not represented as full-text or claim verification. |
| P2-7 — four fresh rows allegedly not independently reopenable | **DISAGREEMENT, LEDGER UPDATED** | The four source pages listed for Mindlin, Biot, and Barak were reopened; Kumar identity/model family was checked at p. 1, with the p. 17 finding explicitly carried from the earlier same-date page-read record. See P1-2 and the four ledger entries. |

### Other retained disagreements and constraints

- Quintanilla’s positive conductivity-gradient signs remain distinct from the manuscript candidate’s minus signs; no sign mapping is asserted. Bazarra’s $\bar\kappa=\kappa-\tau\kappa^*>0$ condition remains separate from Quintanilla’s one-dimensional inequality.
- The Kumar/Kumar–Kansal identity split remains enforced; the 19 dependent claims remain B/C. The Indian J. Phys. companion is not attached to `Gupta2023Energy`.
- OCL-259 remains described as an operator derivation, not a “nonlocal balance law.” Green–Lindsay p. 5 is not used to establish an unrestricted Fourier-only law. HFF’s abstract energy-conservation rationale remains distinct from its interaction-energy ratio.

## Verification and self-audit

- **Local workflow-equivalent checks:** all 15 configured Python verification/ledger scripts passed after the inventory update. The inventory gate covers locations and row completeness only; it does not validate equations or sources.
- **CI:** run `40553021209` succeeded; build, PDF extraction, manuscript scan, and artifact publication all completed.
- **Rendered-PDF metrics:** 122 pages; undefined references/citations **0**; near-overfull boxes (>0.5 pt) **0**; rendered figure PDFs **18**, with **16** includes in the master; deletion-audit `NONE` rows **0**.
- **Forbidden scan counts:** strict manuscript tags **0**; privacy tokens **0**; new internal-artifact patterns (`V-B…`, “saved audit”, “verification script”) **0**; internal paths (`phase5/`, `phase4/`, `.csv`) **0**. The broad legacy substring scan emitted five diagnostic false positives (case-insensitive prose/math fragments only); none matched the strict forbidden-tag pattern and the gate passed.
- **Rendered-text A/V spot-check (10 rows):** OCL-174/175 (Quintanilla gradient signs, bounds, and stability scope, printed p. 34); OCL-195 (Mindlin baseline, pp. 625–626 source anchor, manuscript p. 43); OCL-207 (bounded Kumar numerical observation, p. 45); OCL-404/405 (narrowed Biot and Barak table features, p. 45); OCL-465/466/467 (control-volume split, 2×2 welded-interface solve, and mixed-term result, pp. 68–69); OCL-480 (exact Eulerian flux and reduced convention, pp. 26 and 67). Text was extracted from the published 122-page PDF; these are text-level checks, not a claim of visual review of every page.
- **Ledger:** 512 rows before and after this remediation; A/B/C/V = **48/123/317/24** before and **48/123/317/24** after. The older audit snapshot had 499 rows (48/123/310/18); it is not the current baseline.
- **Repository hygiene:** `git diff --check` passed; ledger and audit CSVs parsed as rectangular CSVs; all 78 Section 4–10 display groups have one inventory row. `stash@{0}` was not modified.

## B23 completion

All actionable P2 findings are fixed or explicitly narrowed; P1-1 is fixed, and P1-2 is resolved by reporting the exact four-row filter and documenting the source-access disagreement rather than manufacturing a larger roster. The remaining evidence limits are stated above and in the ledger. B23 remediation is complete; WP4 may resume from the remaining conditional/open equation-audit rows.