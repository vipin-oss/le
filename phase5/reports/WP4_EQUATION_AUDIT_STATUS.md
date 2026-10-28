# WP4 Equation Audit — Initial Inventory and Status

**Status:** in progress. The initial inventory and first targeted correction were committed as `85520cd` (CI run `40543260698`, output commit `bc2a867`). Fractional-definition assumptions and scoped checks were then added in content commit `8eff8ec` (CI run `40544982191`, output commit `1eaf8e3`), followed by the MDD normalization check in `11b8b8c` (CI run `40546060319`, output commit `77ec18a`). These are inventory and bounded checks, not completion of the equation audit.

## Scope and coverage

The audit covers every active `equation` and `equation*` display group in Sections 4–10. The current `EQUATION_AUDIT.csv` has 78 records: 77 active displays (Section 4 = 17, Section 5 = 16, Section 6 = 8, Section 7 = 4, Section 8 = 7, Section 9 = 12, Section 10 = 13) plus one historical `WITHHELD` record for removed Eq. 4.12. `check_equation_audit_inventory.py` verifies active display coverage and ensures a withheld label is absent from the source; it does not validate formulas.

WP4 checkpoint after the R4B source reconciliation and targeted equation closure:

| Status | Rows | Meaning at this checkpoint |
| --- | ---: | --- |
| `VERIFIED-SOURCE` | 3 | Includes Biot (1956), printed p. 242, Eqs. (3.3)--(3.4), and the scoped GN-II Eq. 4.11 source mapping. |
| `VERIFIED-SYMBOLIC` | 25 | Includes model-specific checks for Eq. 7.3, uncoupled elastic speeds, LS elimination and scalar thermal characteristic speed, first-order TPL Taylor truncation, fractional definitions on tested functions, 1D nonlocal dispersion, and the reduced flux convention. |
| `CONDITIONAL` | 49 | Displays are retained only under stated assumptions; continue reducing these only where page-level source evidence or reproducible derivations support promotion. |
| `OPEN` | 0 | No active displayed equation remains unclassified as OPEN. |
| `WITHHELD` | 1 | Historical Eq. 4.12 record; its formula is removed from active text and working appendix pending exact source verification. |

There are 77 active display groups plus one WITHHELD historical record. The inventory gate is coverage-only; status still does not establish a formula outside its row-specific evidence and scope.

## First corrections: Section 5 piezoelectric energy and stiffness

Section 5 previously called the correction in the displayed tensor relation a “short-circuit/open-circuit” correction. That conflated distinct electrical conditions. The manuscript now states the derivation from its displayed linear constitutive equations precisely: under quasistatic open circuit, `D=0` gives `C_open = C + e^T K^{-1}e`; under short circuit, `E=0` leaves `C_short = C`. The positive-semidefinite statement is conditional on positive-definite permittivity. The same script checks both substitutions and includes negative tests against the wrong sign and against conflating the two boundary conditions (OCL-500).

The displayed `1/2 D_i E_i` expression is now explicitly restricted to the electric-field energy contribution of an uncoupled linear dielectric (`D=K E`). The text states that it is not the total stored energy of the coupled piezoelectric system. The script verifies the dielectric identity and tests that the coupled displacement law leaves a strain-electric cross term (OCL-510).

## Reduction checks and negative tests

`verify_unified_reductions.py` now tests both positive substitutions and negative alternatives for the displayed relations: LS-to-Fourier; first-order DPL-to-LS/Fourier (including the explicit rejection of `tau_q=0` as the LS limit); TPL-to-DPL; the candidate MGT-to-LS-type and MGT-to-Fourier reductions; the GN-III/GN-II derivative-level relation; selected Caputo integer endpoints; and the displayed nonlocal local limit. A separate script checks the Caputo and Riemann–Liouville integral definitions against beta-integral monomial actions for orders with `n=1,2,3`, and uses the constant at `alpha=1/2` as a negative test showing their initial-data behavior differs (OCL-511). Negative tests retain the terms left behind when only one required parameter is removed, distinguish fractional order one-half from an ordinary derivative, and distinguish a finite-wavenumber nonlocal speed from its local value. These are symbolic checks of displayed equations, not source-transcription, admissibility, solution-convergence, stability, or family-wide equivalence proofs (OCL-470–OCL-473, OCL-509).

## External independent check inspected

Fetched the read-only audit branch `arena/0be2770f-le` at `6e095abcaa674ee5d92d2a8589446bd38ae61780`. Its tree contains a B22 report, but no B23/Brave report file. The B22 report lists no P0 findings and four P1 findings. A comparison with this branch shows the corresponding matters are already corrected or qualified here: the DPL-to-LS table uses `tau_T -> 0` with `tau_q=tau_0`; the Quintanilla DOI is set to the Crossref-matching candidate but remains `verified=NO` and the conflicting first-page reports remain recorded; the interface cross-term script derives the actual fields rather than asserting a tautology; and Eq. 9.10 explicitly defines its incident-flux denominator as the net same-plane incident flux. No new P0/P1 defect was identified in this check. The DOI conflict remains open and is not being treated as resolved.

## Remaining work

1. Audit the 49 remaining conditional rows against exact source pages/equations or equation-specific scripts; explicitly record sign conventions, coefficient maps, domains, constitutive assumptions, and boundary/data restrictions.
2. Keep Eq. 4.11 source-verified only for the source-free GN-II alpha form with zero integration function; keep the exact entropy-flux component formula withheld (OCL-515–OCL-516). Eq. 7.3 is verified only for the declared positive quadratic gradient energy (OCL-514).
3. Check all source-sensitive displayed equations for sign/index/notation conflicts, including thermal-flux signs, conductivity tensor versus scalar use, equations involving `kappa*` versus `kappa_ij`, interface-system mode counts, and the exact assumptions behind each matrix inverse or balance identity.
4. For each reduction claimed in the manuscript, retain a positive check and a negative test for the most plausible incorrect substitution; keep source transcription separate from symbolic validity.
5. After reducing the remaining conditional rows, re-run the inventory, ledger, build, privacy, and hostile-diff checks; then continue the ordered Q1, Q3, Q5, WP3 remainder, WP6, WP7, and WP8 work.

Current equation-audit claim ledger total is 520 rows: A=56, B=119, C=316, V=29. The inventory checker establishes row coverage only; it does not close the remaining equation work.

## Build and rendered self-audit checkpoint

Content commit `85520cd0d2c3d520782dede20e44ba6c6ae5744c` passed LaTeX Build CI run `40543260698`. The strict build reports 122 PDF pages, undefined references/citations 0, forbidden privacy-token/internal-path/manuscript-tag counts 0, rendered figure PDFs 18, figure includes 16, deletion-audit `NONE` rows 0, and near-overfull boxes (>0.5 pt) 0. The workflow-published output commit `bc2a8679521ee3c5a8e4a56624dbdc3b4a9cb9ec` was fast-forwarded on the fixed branch and matched `git ls-remote`.

The changed Section 5 equations and the revised reduction table were visually reviewed at final PDF size (PDF pages 43–44, 40, and 80; printed pages 42–43, 39, and 79). Ten V-ledger claims—OCL-480, OCL-498, OCL-470, OCL-465, OCL-466, OCL-467, OCL-468, OCL-484, OCL-500, and OCL-510—were spot-checked against rendered text. Ledger validation passed with 511 rows (A=48, B=123, C=317, V=23); the inventory checker and all relevant symbolic/source-map tests passed. These checks establish engineering/render consistency and bounded algebra only, not completion of the remaining source-by-source WP4 audit.

The subsequent content commit `8eff8ecad74f0eb99008e26b8db8cae77ff2be90` passed CI run `40544982191`; its workflow output commit `1eaf8e35158d54f936b7b858ebe3e1417fffc16f` was fast-forwarded and verified equal to `git ls-remote`. It reproduced 122 pages, undefined references/citations 0, forbidden privacy-token/internal-path/manuscript-tag counts 0, rendered figure PDFs 18, figure includes 16, deletion-audit `NONE` rows 0, and near-overfull boxes (>0.5 pt) 0. Final-size PDF page 50 (printed p. 49) was visually inspected: Eqs. (71)–(73), order/regularity qualifiers, and neighboring text were readable without clipping. The ten prior A/V spot-checks (OCL-480, 498, 470, 465–468, 484, 500, 510) were rechecked against rebuilt text; new OCL-511 was additionally matched to the displayed Caputo/Riemann–Liouville definitions on PDF p. 50. Ledger validation, the 77-row inventory, reduction tests, piezoelectric checks, and `git diff --check` passed.

The next content commit `11b8b8c94fdd64ba4dad19e86378b624efd4d100` passed CI run `40546060319`, with build-output commit `77ec18a77e19ffaf2706075483bf286303f6b697` fast-forwarded and verified at the remote head. It reproduced 122 pages; undefined references/citations 0; forbidden privacy-token, internal-path, and manuscript-tag counts 0; rendered figure PDFs 18; figure includes 16; deletion-audit `NONE` rows 0; near-overfull boxes (>0.5 pt) 0. Final-size PDF page 51 (printed p. 50) was visually reviewed; the new MDD limiting paragraph and equations were legible without clipping. Ten existing A/V rows and new OCL-512 were checked against the rebuilt text. The ledger has 512 rows (A=48, B=123, C=317, V=24); the equation inventory is 1 `VERIFIED-SOURCE`, 17 `VERIFIED-SYMBOLIC`, 55 `CONDITIONAL`, and 4 `OPEN`.

## Section 4.2 source and linearization check

`verify_classical_thermoelastic.py` derives the source-free heat equation from the displayed linear entropy relation and local heat balance. With Fourier flux, constant coefficients, and first-order perturbations about $T_0$, the nonlinear remainder is quadratic; the two negative controls keep the heat-diffusion and thermoelastic strain-rate terms visible. The source anchor is Biot (1956), printed p. 242, Eqs. (3.3)--(3.4), recorded in OCL-513. The equation is now `VERIFIED-SOURCE` only within this linear isotropic Fourier scope; no nonlinear or generalized-theory extension is implied.

Content commit `4bfe01705ed4e6672509d0b83942d4cbeac9e6eb` passed CI `40554464253`; output commit `298ab6304a601b53d64062518ef244d7483219bf` was fast-forwarded. The build had 122 pages, zero undefined references/citations, zero forbidden privacy/internal-artifact/internal-path/manuscript tags, zero near-overfull boxes above 0.5 pt, and zero deletion-audit `NONE` rows. Ten A/V entries OCL-174/175/195/207/404/405/465/466/467/513 were checked against normalized extracted PDF text. At that checkpoint the ledger was 513 rows (A=49, B=123, C=317, V=24); the 78-display audit had 2 source-verified, 16 symbolic, 57 conditional, and 3 open rows. This checkpoint supersedes that status: 77 active displays are covered, Eq. 4.11 and Eq. 7.3 are verified within scope, Eq. 4.12 is withheld, and no active display remains OPEN.


## Additional equation-specific reductions (2026-10-28)

Eight active displays were promoted from `CONDITIONAL` to `VERIFIED-SYMBOLIC`, reducing the remaining conditional set from 57 to 49 without changing the active-display inventory. New reproducible checks derive: (1) the uncoupled elastic reference speeds from Eq. 4.1 at beta=0, with a negative control showing thermal coupling remains when beta is nonzero; (2) the LS heat equation by applying the time-relaxation operator to the local thermal balance and eliminating div(q) with Eq. 4.4; (3) the scalar LS characteristic speed only for the uncoupled beta=0 branch; (4) the first-order Taylor residual from the three shifted TPL terms while retaining a nonzero higher-order remainder; and (5) the one-dimensional Helmholtz-bar dispersion relation from the displayed operator. The Caputo/Riemann--Liouville definition checks are scoped to the tested beta-integral monomial actions, and Eq. 10.3 remains only the reduced first-order small-amplitude flux convention. These four new V-ledger records are OCL-517--OCL-520; scripts are `verify_isotropic_elastic_speeds.py`, `verify_ls_heat_equation.py`, `verify_tpl_first_order_expansion.py`, and `verify_nonlocal_dispersion.py`.

Eq. 4.17 remains `CONDITIONAL`: APPA EQ-019 and OCL-169 record inconsistent source equation-number ranges and no reconciled printed-page locator. The recorded full-text finding is not treated as page-level verification until that discrepancy is resolved. Eq. 4.12 remains WITHHELD. Current inventory status is 77 active displays plus one withheld historical record: 3 `VERIFIED-SOURCE`, 25 `VERIFIED-SYMBOLIC`, 49 `CONDITIONAL`, 0 `OPEN`, and 1 `WITHHELD`. The ledger has 520 rows (A=56, B=119, C=316, V=29).

Local TeX executables are unavailable in this workspace; these edits have not yet had a TeX build or CI run. The symbolic scripts and CSV/inventory checks are the available verification evidence for this checkpoint.
