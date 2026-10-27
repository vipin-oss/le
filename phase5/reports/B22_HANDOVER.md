# B22 handover — fixed-branch implementation and audit

**Date:** 2026-10-27
**Working branch:** `arena/b5e608f8-le` (active)
**Read-only audit branch fetched:** `arena/0be2770f-le` at `6e095abcaa674ee5d92d2a8589446bd38ae61780`. It was not checked out, modified, or pushed to.
**Scope status:** B22 P1/P2 findings implemented and audited. Q3–Q5 and later work packages remain open; this handover does not call the manuscript submission-ready.

## Ledger integrity

The source snapshot immediately before B22 work was `e1452a8` (end of the prior Q2 package): **487 rows — A=30, B=128, C=314, V=15**. Counts were recomputed from the committed CSV at each checkpoint:

| Checkpoint | Rows | A | B | C | V | Change |
|---|---:|---:|---:|---:|---:|---|
| Before B22 (`e1452a8`) | 487 | 30 | 128 | 314 | 15 | Baseline |
| After F1 (`76014e0`) | 487 | 30 | 128 | 314 | 15 | No new row |
| After F2 (`2261161`) | 488 | 30 | 129 | 314 | 15 | OCL-488, unresolved DOI conflict, Class B |
| After F3 (`4a35a42`) | 488 | 30 | 129 | 314 | 15 | OCL-467 re-evaluated as Class V; no count change |
| After F4 (`817f6f6`) | 489 | 30 | 130 | 314 | 15 | OCL-489, conditional same-plane definition, Class B |
| After P2 bibliography disposition (`274873d`) | 490 | 30 | 130 | 315 | 15 | OCL-490, removed uncited entry, Class C |
| Current content (`d0301a6`) | 490 | 30 | 130 | 315 | 15 | MDD comparison wording only; no count change |

The ledger validator passes. All 19 Kumar-dependent rows (OCL-076 and OCL-278–OCL-295) remain B/C. No F1–F4 or P2 correction promoted an unsupported generalized theorem.

## P1 implementation

| Finding | Content commit | CI run | Disposition and independent audit |
|---|---|---|---|
| F1 — DPL → LS limit | `76014e0d3da3ae910539851c6d38cc260de15a09` | `40480957456` | The manuscript now uses `tau_T -> 0` with `tau_q = tau_0`; `tau_q -> 0` is not described as LS. The reduction verifier has a positive assertion for the correct limit and a negative assertion against the incorrect one. `git grep` found no remaining DPL→LS `tau_q -> 0` row. B22's independent reduction script passed 11/11 checks. |
| F2 — Quintanilla DOI/provenance | `2261161dedeb4d06a7ab777c1b84510abdfb817f` | `40481634107` | The bibliography candidate is Crossref-resolving `10.1080/713855996`; `verified=NO` is retained because two source-page reports conflict. The false assertion that the earlier first-page check confirmed that DOI was removed. `CROSSREF_FINAL.csv` records all 14 field comparisons for the two bibliography entries carrying first-page-confirmation notes; unavailable raw fields are `NOT-CHECKED`, not inferred. |
| F3 — OCL-467 cross term | `4a35a4237bca759a2917d9e711823b8d768cf07c` | `40482398909` | Replaced the tautological complex-number assertion with a two-wave field, stress/velocity-derived flux, the mixed phasor product before averaging, and its zero mean for the stated 1D, same-medium, lossless case. Substantive field checks are distinguished from definitional closures. OCL-467 remains Class V with evidence mode `SYMPY-HARMONIC-STRESS-VELOCITY-DERIVATION; SUBSTANTIVE 1D FIELD CHECK`. B22's independent derivation reproduces the result and identifies the former test as vacuous. |
| F4 — Eq. (105) incident flux | `817f6f62eea9100ee130a4c1dda8b5cdb8e4a129` | `40482993502` | `J_{inc,n}` is defined as net incident normal flux `P_{i,Sigma}>0` at the interface reference plane. `A_int=D_Sigma/P_{i,Sigma}` is limited to the same-plane normalization; it is not equated to remote-plane incident power under bulk attenuation. OCL-486 and the conditional B row OCL-489 reflect that scope. |

All four P1 CIs passed. Artifact commits: `02feeb4` (40480957456), `cba3f26` (40481634107), `57edc1d` (40482398909), and `2f47135` (40482993502).

## P2 implementation and verification

- **Comparative evidence cluster — `274873da57958c3c7cef649b57f5592e2dd334de`; CI `40483888640` (pass); artifact `cc95626`.** Added the unclassified `tau_theta = tau_q/2` case; marked both MDD limiting-case rows model-dependent; filled Dell’Oro–Pata volume 76, pages 641–655 using the saved B22 comparison while retaining `verified=NO` because the raw response is unavailable here; removed uncited `Abdalla2022` and recorded OCL-490. Reopened the DOI-matched Kumar et al. (2023) *Phys. Scr.* 98:115211 source: the 19-page article's printed p. 17 conclusion supports only the reported approximate-unity observation, not an identity or theorem; OCL-207 remains bounded Class A.
- **Equation register and scan cluster — `b07ab06e731cd67205c7cd3ba63e9399d6cdb7ef`; CI `40484672150` (failed before the manuscript build).** Added register entries for Eq. 10.13–10.16 and renamed the old generalized-flux placeholder to `EQ-10.GEN` to remove the ID collision. Updated the companion equation ledger and a structural verifier. The failure was a stale exact-string assertion after the reference-plane caveat was reworded, not a manuscript or build-gate failure.
- **One-line verifier correction — `15f04154c6abca5fa10addf19e8532e059c81e5f`; CI `40485088078` (pass); artifact `912a029`.** Broadened the verifier to check the underlying reference-plane phrase rather than exact editorial wording.
- **MDD comparison correction — `d0301a608a63f8002b754d9c03715eaa20b42cf0`; CI `40486388596` (pass); artifact `7c9c7ad`.** All ten substantive MDD cells in the current Part B cross-theory table are now explicitly “Model-dependent,” with a note that no governing MDD law is displayed with a source-anchored equation. The script checks each cell; OCL-483 remains B.

The B22 report called the table with MDD cells “Table 23.” In the current rendered PDF, **Table 23 is Part A and has no MDD column; Table 24 is Part B and contains the MDD column**. The edits target the actual MDD-bearing table, Table 24. The Section 12 limiting-case table separately retains the two model-dependent MDD reductions. The register is maintained in `appA_equation_register.tex` and `APPA_LEDGER.csv`; Appendix A is not included in the current master PDF, consistent with the earlier cleanup. Thus the register entries are repository audit records, not claims that a printed register appeared in this build.

The p. 65 internal report path was removed from the Section 9 text. The p. 70 verification-script path had already been replaced during F3 with a generic description. The strict rendered-text gate was extended additively to reject `phase5/`, `phase4/`, `.csv`, privacy tokens, and the existing manuscript tags; no prior pattern was relaxed.

## Final CI gates and rendered audit

Latest B22 content CI: **`40486388596`**, content `d0301a6`, artifact `7c9c7ad`; the local head was pulled and matched `origin/arena/b5e608f8-le`. Build audit: **119 pages; undefined references/citations 0; overfull boxes >1 pt 0; near-overfull boxes >0.5 pt 0; forbidden manuscript tags 0; privacy tokens 0; internal-path tokens (`phase5/`, `phase4/`, `.csv`) 0; rendered figure PDFs 18; master figure includes 16; deletion-audit `NONE` rows 0.** The stricter path/privacy/tag checks also passed in CI `40485088078`.

Final-size visual review checked printed pp. 65 and 70 for path leakage/legibility, and printed p. 76 for the MDD column. No internal path or clipping was visible; the MDD entries wrap but remain legible. A 10-row A/V rendered-text spot check matched the ledger claims to the current PDF:

| Ledger row | PDF page(s) | Rendered-text check |
|---|---:|---|
| OCL-207 (A) | 46 | Approximate energy-ratio sum is reported as a numerical observation, not an exact identity. |
| OCL-445 (A) | 76 | Strict stability/instability inequalities are followed by an explicit unclassified equality case. |
| OCL-465 (V) | 68 | Control-volume split and the remote-plane residual's included losses appear. |
| OCL-466 (V) | 69 | 2×2 system, determinant `-(Z1+Z2)`, and positive-impedance uniqueness appear. |
| OCL-467 (V) | 69 | Incident/reflected mixed product is shown before averaging; the scoped zero mean-flux conclusion appears. |
| OCL-468 (V) | 65 | Total-field closure is identified as a definition-level bookkeeping identity, not independent validation. |
| OCL-478 (V) | 53 | Displayed nonlocal dispersion/group-velocity algebra is present. |
| OCL-474 (A) | 37 | GL claims remain abstract-level and are labelled as such. |
| OCL-475 (A) | 37 | GN-II abstract-level nondissipation/finite-speed scope is shown as type-II-specific. |
| OCL-476 (A) | 38 | GN-III scope is separated from the type-II nondissipation result. |

This is a rendered-text spot check, not a full scientific or typographic proof. The hostile diff review found only the scoped changes listed above in the content commits; the untracked Q3 matrix and verifier were preserved.

## Evidence disagreements and unresolved items

1. **Quintanilla DOI remains unresolved.** The earlier R4B page report gives `10.1080/01495730390203518`; the B22 held-cover report gives `10.1080/713855996`. Saved Crossref responses return a matching record only for the latter. The source copy could not be reopened to reconcile the two reports, so both are retained in OCL-488, the bibliography remains `verified=NO`, and no `CONTRADICTION-FIXED` label is claimed.
2. **Kumar p. 17 concern was a source-identity disagreement.** B22's held PDF was a different 13-page PNASI article. The exact DOI-matched *Phys. Scr.* article is 19 pages and its p. 17 supports the bounded approximate-unity wording. Why the wrong PDF was associated with the anchor is not independently established.
3. **Dell’Oro–Pata Crossref raw response is unavailable.** The paper's own first page supports authors, title, DOI, and year; volume/pages 76:641–655 are recorded as B22-reported only, and `verified=NO` remains.
4. **B22 source availability limit.** In its 26-row Class A sample, 7 were NOT-CHECKABLE because the source was not held; the report also audited all 9 Class V rows. This does not establish that the sources are absent. B22's 20-key DOI spot check was 20/20 for title/first-author/volume/pages. Its earlier `.511931`/`.511929` suspicion was explicitly retracted: both Povstenko entries were already correct and were not changed.
5. **Table numbering differs from B22's target snapshot.** The current PDF numbering was checked directly; the MDD-bearing table is Table 24 Part B, not current Table 23 Part A. This is a numbering/snapshot mismatch, not a source-evidence conflict.

## Continuation boundary

B22 P1/P2 work is complete at the stated evidence limits. Continue with Q3, then Q4/Q5 and WP3–WP8 in the existing work-package order. Keep source-dependent gaps and the seven NOT-CHECKABLE sampled A rows visible; do not infer that successful CI proves scientific validity.
