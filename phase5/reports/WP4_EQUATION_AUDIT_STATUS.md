# WP4 Equation Audit — Initial Inventory and Status

**Status:** in progress. The initial inventory and first targeted correction were committed as `85520cd` (CI run `40543260698`, output commit `bc2a867`). Fractional-definition assumptions and scoped checks were then added in content commit `8eff8ec` (CI run `40544982191`, output commit `1eaf8e3`), followed by the MDD normalization check in `11b8b8c` (CI run `40546060319`, output commit `77ec18a`). These are inventory and bounded checks, not completion of the equation audit.

## Scope and coverage

The audit covers every `equation` and `equation*` display group in Sections 4–10. The new `EQUATION_AUDIT.csv` has 77 rows: Section 4 = 17, Section 5 = 16, Section 6 = 8, Section 7 = 4, Section 8 = 7, Section 9 = 12, and Section 10 = 13. `check_equation_audit_inventory.py` verifies that each current display group has exactly one row with matching source line and label. It is a coverage check only and does not validate formulas.

Current dispositions after the first fractional-definition check:

| Status | Rows | Meaning at this checkpoint |
| --- | ---: | --- |
| `VERIFIED-SOURCE` | 1 | One equation has a targeted primary-source equation/page anchor. |
| `VERIFIED-SYMBOLIC` | 17 | Existing or new scripts check the displayed algebra within the row's stated scope; source transcription is not implied unless separately anchored. |
| `CONDITIONAL` | 55 | The equation is retained only under the assumptions and limits stated in its row; many still need an exact source anchor or equation-specific derivation. |
| `OPEN` | 4 | Equation-level verification remains unperformed; the rows identify the required next action. |

The status count is intentionally conservative. A `CONDITIONAL` or `OPEN` row is not a verified scientific claim. Each unverified display is linked to a section-specific Class C ledger row, and the row itself names the remaining source/derivation check.

## First corrections: Section 5 piezoelectric energy and stiffness

Section 5 previously called the correction in the displayed tensor relation a “short-circuit/open-circuit” correction. That conflated distinct electrical conditions. The manuscript now states the derivation from its displayed linear constitutive equations precisely: under quasistatic open circuit, `D=0` gives `C_open = C + e^T K^{-1}e`; under short circuit, `E=0` leaves `C_short = C`. The positive-semidefinite statement is conditional on positive-definite permittivity. The same script checks both substitutions and includes negative tests against the wrong sign and against conflating the two boundary conditions (OCL-500).

The displayed `1/2 D_i E_i` expression is now explicitly restricted to the electric-field energy contribution of an uncoupled linear dielectric (`D=K E`). The text states that it is not the total stored energy of the coupled piezoelectric system. The script verifies the dielectric identity and tests that the coupled displacement law leaves a strain-electric cross term (OCL-510).

## Reduction checks and negative tests

`verify_unified_reductions.py` now tests both positive substitutions and negative alternatives for the displayed relations: LS-to-Fourier; first-order DPL-to-LS/Fourier (including the explicit rejection of `tau_q=0` as the LS limit); TPL-to-DPL; the candidate MGT-to-LS-type and MGT-to-Fourier reductions; the GN-III/GN-II derivative-level relation; selected Caputo integer endpoints; and the displayed nonlocal local limit. A separate script checks the Caputo and Riemann–Liouville integral definitions against beta-integral monomial actions for orders with `n=1,2,3`, and uses the constant at `alpha=1/2` as a negative test showing their initial-data behavior differs (OCL-511). Negative tests retain the terms left behind when only one required parameter is removed, distinguish fractional order one-half from an ordinary derivative, and distinguish a finite-wavenumber nonlocal speed from its local value. These are symbolic checks of displayed equations, not source-transcription, admissibility, solution-convergence, stability, or family-wide equivalence proofs (OCL-470–OCL-473, OCL-509).

## External independent check inspected

Fetched the read-only audit branch `arena/0be2770f-le` at `6e095abcaa674ee5d92d2a8589446bd38ae61780`. Its tree contains a B22 report, but no B23/Brave report file. The B22 report lists no P0 findings and four P1 findings. A comparison with this branch shows the corresponding matters are already corrected or qualified here: the DPL-to-LS table uses `tau_T -> 0` with `tau_q=tau_0`; the Quintanilla DOI is set to the Crossref-matching candidate but remains `verified=NO` and the conflicting first-page reports remain recorded; the interface cross-term script derives the actual fields rather than asserting a tautology; and Eq. 9.10 explicitly defines its incident-flux denominator as the net same-plane incident flux. No new P0/P1 defect was identified in this check. The DOI conflict remains open and is not being treated as resolved.

## Remaining work

1. Audit all 55 conditional rows against exact source pages/equations or equation-specific scripts; explicitly record sign conventions, coefficient maps, domains, constitutive assumptions, and boundary/data restrictions.
2. Resolve or conservatively hedge/remove the four open displays: Eq. 4.2, 4.11, 4.12, and 7.3.
3. Check all source-sensitive displayed equations for sign/index/notation conflicts, including thermal-flux signs, conductivity tensor versus scalar use, equations involving `kappa*` versus `kappa_ij`, interface-system mode counts, and the exact assumptions behind each matrix inverse or balance identity.
4. For each reduction claimed in the manuscript, retain a positive check and a negative test for the most plausible incorrect substitution; keep source transcription separate from symbolic validity.
5. After the Section 4–10 equation rows are resolved, re-run the inventory, ledger, build, privacy, and hostile-diff checks; then continue the ordered Q1, Q3, Q5, WP3 remainder, WP6, WP7, and WP8 work.

Current equation-audit ledger total is 512 rows: A=48, B=123, C=317, V=24. The inventory checker establishes row coverage only; it does not close the remaining equation work.

## Build and rendered self-audit checkpoint

Content commit `85520cd0d2c3d520782dede20e44ba6c6ae5744c` passed LaTeX Build CI run `40543260698`. The strict build reports 122 PDF pages, undefined references/citations 0, forbidden privacy-token/internal-path/manuscript-tag counts 0, rendered figure PDFs 18, figure includes 16, deletion-audit `NONE` rows 0, and near-overfull boxes (>0.5 pt) 0. The workflow-published output commit `bc2a8679521ee3c5a8e4a56624dbdc3b4a9cb9ec` was fast-forwarded on the fixed branch and matched `git ls-remote`.

The changed Section 5 equations and the revised reduction table were visually reviewed at final PDF size (PDF pages 43–44, 40, and 80; printed pages 42–43, 39, and 79). Ten V-ledger claims—OCL-480, OCL-498, OCL-470, OCL-465, OCL-466, OCL-467, OCL-468, OCL-484, OCL-500, and OCL-510—were spot-checked against rendered text. Ledger validation passed with 511 rows (A=48, B=123, C=317, V=23); the inventory checker and all relevant symbolic/source-map tests passed. These checks establish engineering/render consistency and bounded algebra only, not completion of the remaining source-by-source WP4 audit.

The subsequent content commit `8eff8ecad74f0eb99008e26b8db8cae77ff2be90` passed CI run `40544982191`; its workflow output commit `1eaf8e35158d54f936b7b858ebe3e1417fffc16f` was fast-forwarded and verified equal to `git ls-remote`. It reproduced 122 pages, undefined references/citations 0, forbidden privacy-token/internal-path/manuscript-tag counts 0, rendered figure PDFs 18, figure includes 16, deletion-audit `NONE` rows 0, and near-overfull boxes (>0.5 pt) 0. Final-size PDF page 50 (printed p. 49) was visually inspected: Eqs. (71)–(73), order/regularity qualifiers, and neighboring text were readable without clipping. The ten prior A/V spot-checks (OCL-480, 498, 470, 465–468, 484, 500, 510) were rechecked against rebuilt text; new OCL-511 was additionally matched to the displayed Caputo/Riemann–Liouville definitions on PDF p. 50. Ledger validation, the 77-row inventory, reduction tests, piezoelectric checks, and `git diff --check` passed.

The next content commit `11b8b8c94fdd64ba4dad19e86378b624efd4d100` passed CI run `40546060319`, with build-output commit `77ec18a77e19ffaf2706075483bf286303f6b697` fast-forwarded and verified at the remote head. It reproduced 122 pages; undefined references/citations 0; forbidden privacy-token, internal-path, and manuscript-tag counts 0; rendered figure PDFs 18; figure includes 16; deletion-audit `NONE` rows 0; near-overfull boxes (>0.5 pt) 0. Final-size PDF page 51 (printed p. 50) was visually reviewed; the new MDD limiting paragraph and equations were legible without clipping. Ten existing A/V rows and new OCL-512 were checked against the rebuilt text. The ledger has 512 rows (A=48, B=123, C=317, V=24); the equation inventory is 1 `VERIFIED-SOURCE`, 17 `VERIFIED-SYMBOLIC`, 55 `CONDITIONAL`, and 4 `OPEN`.
