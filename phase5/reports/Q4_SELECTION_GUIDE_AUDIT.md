# Q4 conditional selection guide and evidence audit

**Date:** 2026-10-27  
**Status:** Implemented and rendered; final strict CI passed and the published PDF was visually reviewed.

## Scope

Section 1 was narrowed to describe the review's evidence-bounded scope rather than promise uniform constitutive, admissibility, computation, or interface results across all families. Section 16 now contains a conditional model-selection workflow, a table separating script-verified checks from primary-source checkpoints, a note distinguishing Appendix C benchmark specifications from validated numerical reference solutions, and a Q3-derived roadmap. No new bibliography item or new primary-source claim was introduced.

The guide is explicitly not a theory ranking. It requires actual equations, fields, geometry, initial/boundary data, interface conditions, and measured observables to be specified. Properties are recorded against the exact equations and assumptions, not attached to a family label.

## Evidence map retained in the guide

| Guide entry | Evidence and limitation |
|---|---|
| Local Cauchy/Fourier baseline | OCL-480 (Class V, local balance/flux derivation); no generalized thermoelastic flux claim. |
| Lord–Shulman | OCL-495 (Class A, page-image-checked source-specific law/system); OCL-011 remains Class C for the unresolved parameter/admissibility claim. |
| GN-II / GN-III | OCL-493/OCL-494 (Class A, source-bounded page-image findings); OCL-498 (Class V, selected zero-source equation map); OCL-491 remains B for GN-II mapping/energy, while OCL-492 remains B for GN-III energy/admissibility/interface work. |
| DPL / TPL | OCL-445 (Class A, source-bounded strict-inequality result for the stated one-dimensional problem); OCL-488 retains the DOI/source-page conflict and equality remains unclassified. OCL-169 supports only the cited first-order TPL formulation; OCL-123 remains open for higher-order variants. |
| Spatial, fractional, hereditary, and coupled fields | The guide asks for exact operator/kernel/closure and data. It preserves bounded source rows (including OCL-195, OCL-258, OCL-321) and open comparison/status rows (including OCL-402, OCL-403, OCL-483, OCL-485); no family-wide properties are inferred. |

## Benchmark evidence distinction

- **Script-verified calculations:** OCL-480 records the classical local flux derivation; OCL-466–468 record the selected one-dimensional welded-interface stress/velocity-flux calculation and distinguish the algebraic closure from an independent conservation theorem; OCL-470–473 record displayed-equation reductions and limits; OCL-498 checks the selected GN-III source-equation coefficient map. None proves solution convergence or family equivalence.
- **Primary-source checkpoints:** OCL-493–496 are bounded source-page findings, not code-validated numerical solutions or full well-posedness proofs.
- **Problem specifications:** Appendix C BM-1–BM-5 specify comparison problems/observables. They are not represented as validated numerical reference solutions unless a separate script-backed check is explicitly identified.

## Q3-derived roadmap

The Section 16 roadmap keeps open: the GN-I equation/source mapping; equation-to-manuscript reconciliation for selected GN-II/LS formulations and other variants; exact-model parameter admissibility and well-posedness; bulk and interface energy-flux derivations; and extensions of benchmarks only after equations, data, normalization, and observables are fixed. The GN-III p. 254–255 scope review and selected p. 261 coefficient map are now complete; its model-specific energy/flux questions remain open. These remaining items are work items, not completed results.

## Hostile review of the preceding docs-only source updates

Reviewed the documentation changes from `a477548` through `7814bf0` on the fixed branch, including `a477548`, `a3220c7`, `a072010`, and `7814bf0`; the CI-output publication commit `3499c26` was checked as a distinct generated artifact update.

- The GL, GN-I, GN-II, GN-III, and LS records retain source/page bounds and explicitly keep broader parameter, stability, existence, family-wide, and energy/interface claims open. GN-I remains unresolved; GN-II/GN-III/LS additions are narrowly anchored to the reviewed printed pages.
- The later GN-III equation/regime pages are image-reviewed. A follow-up image check of printed pp. 254–255 located the type-II-only no-dissipation footnote on p. 254 and the type-III scope summary on p. 255; no type-II result is transferred to type III.
- The DPL DOI/source-page disagreement remains visible under OCL-488; equality is still unclassified. The Kumar split verifier confirms all 19 dependent rows remain B/C.
- The earlier fixed-branch PDF at `6e8cf1e` was 119 pages; the read-only older `e56755f` report's 130-page manuscript is a different source version. The current post-Q4 fixed-branch PDF is 121 pages; the counts are not interchangeable.
- The private Drive link/ID scan of the preceding seven changed text files returned zero hits; `git diff --check` passed. No material unsupported class promotion or privacy leak was identified in that documentation review.

## CI and rendered-text audit

Two content commits were each followed by their own successful strict build:

| Content commit | CI run | Result |
|---|---:|---|
| `63f83f1` — Q4 guide and scope edits | `40502884138` | Success, 121 pages. The first visual check found Table 38 had floated ahead of subsection 16.1. |
| `d1b7e2d` — keep selection tables with headings | `40503549729` | Success, 121 pages. Table placement was corrected using a fixed-position float; the final rendered layout was inspected. |

Final CI reported: undefined references/citations = 0; overfull boxes above 1 pt = 0; near-overfull boxes above 0.5 pt = 0; forbidden privacy tokens = 0; forbidden internal paths = 0; forbidden manuscript tags = 0. It rendered 18 figure PDFs for 16 master includes. The CI-published output commit is `20bb6bf`, synchronized with the fixed branch.

The final PDF text was extracted from the published artifact. Printed pp. 102–103 were visually checked: Table 38 now follows subsection 16.1, both tables are legible, and their content remains within the page. Ten A/V ledger rows were compared with the rendered text:

| Ledger row | Rendered location | Comparison |
|---|---|---|
| OCL-164 (A) | Section 4.7, printed p. 33 | GK phonon-flux structure is attributed to the phonon Boltzmann treatment, not a ready-made continuum thermoelastic law; the scope matches the ledger. |
| OCL-165 (A) | Section 4.7, printed p. 33 | The stated rapid-normal-scattering condition and characteristic-length expression are present with the Ziman-averaged time defined. |
| OCL-166 (A) | Section 4.7, printed p. 33 | Tzou's Eq. 15 continuum reduction is identified as the pure-phonon case and is not attributed to the 1966 source. |
| OCL-167 (A) | Section 4.7, printed p. 33 | Tzou's Eq. 17 parameter map is printed and restricted to the stated phonon approximation. |
| OCL-169 (A) | Section 4.8, printed p. 34 | The first-order three-lag expansion and ordering are stated; later variants are not generalized from it. |
| OCL-445 (A) | Section 4.7/Table 6, printed p. 37; selection guide, p. 102 | The selected one-dimensional strict inequalities and unclassified equality are both visible; no universal DPL criterion is asserted. |
| OCL-466 (V) | Section 10.5.2, printed p. 68 | Displacement/traction continuity yields the displayed two-amplitude 2×2 system and determinant. |
| OCL-467 (V) | Section 16.2, printed p. 103 | The rendered summary states the stress/velocity-flux partition and zero time-average of the harmonic cross-term. The full algebra remains in the verifier; the prose does not claim a general interface theorem. |
| OCL-468 (V) | Section 9.7, printed p. 64 | Total-field closure is called a definition-level bookkeeping identity, not independent validation; cross-term scope is limited. |
| OCL-480 (V) | Section 10.2, printed p. 66 | The classical local flux $J_i=q_i-\sigma_{ij}v_j$ and outward-positive convention appear under the stated classical balance assumptions. |

## Verification and ledger integrity

The following passed locally: `verify_q3_status_matrix.py`, `verify_q4_selection_guide.py`, `verify_unified_reductions.py`, `verify_interface_energy.py`, `verify_interface_mode_counts.py`, `verify_q1_notation.py`, `verify_kumar2017_reference_split.py`, `validate_claim_ledger.py`, and `git diff --check`.

The final ledger state is 497 rows: A=34, B=132, C=315, V=16. OCL-497 is Class V for structural coverage/provenance mapping only; its verifier does not re-review sources or validate numerical solutions. The final CI gates and ten-row rendered-text check are recorded above.

## Q3 GN-III scope-page follow-up after Q4 CI

A targeted image review of Green & Naghdi (1992), printed pp. 254–255, corrected the earlier page attribution: the type-II-only no-dissipation footnote is on p. 254; p. 255 summarizes the type-III development and its finite-speed coupled system. OCL-476 remains Class A only for this bounded source-scope finding; OCL-492 remains Class B for exact equation-to-manuscript mapping and model-specific energy/admissibility/interface flux. The primary PDF was removed after review. No bibliography entry or theory-wide property was changed.

Content commit `32dd431` passed CI `40505226590` and produced 121 pages; output publication commit `ecae40c` was fast-forwarded and matched the remote branch. Final gates: undefined references/citations 0; overfull boxes >1 pt 0; near-overfull boxes >0.5 pt 0; privacy tokens 0; internal paths 0; manuscript tags 0; 18 figure PDFs rendered/16 included. Printed p. 103 was visually rechecked with the revised roadmap and benchmark table; both are legible with no overflow.

The same ten A/V rows were rechecked against the final 121-page rendered text: OCL-164–OCL-167 at printed p. 33; OCL-169 at p. 34; OCL-445 at pp. 37 and 102; OCL-466 at p. 68; OCL-467 at p. 103 (summary; derivation remains script-backed); OCL-468 at p. 64; and OCL-480 at p. 66. All remain within their ledger scope. The Q3 image review closes the p. 254–255 source-scope gap only; GN-I mapping, GN-II/LS equation-to-manuscript reconciliation, parameter admissibility, and energy/flux work remain open. Ledger classes at that checkpoint were A=34, B=132, C=315, V=16.

## GN-III displayed-equation map follow-up after CI

Content commit `c98d7ad` passed CI `40510553492`; the strict PDF remains 121 pages. Artifact publication commit `77afb5c` was fast-forwarded and matched the remote head. Gates: undefined references/citations 0; overfull boxes >1 pt 0; near-overfull boxes >0.5 pt 0; privacy tokens 0; internal paths 0; manuscript tags 0; 18 figure PDFs rendered/16 included; deletion-audit `NONE` rows 0. The new symbolic map check ran green. Hostile diff review found only the scoped GN-III Section 4/T2 wording, Q3 roadmap, verification script/workflow, ledger/matrix and audit/work-package records; no bibliography change, private identifier, or model-wide theorem was added. `git diff --check` and the local ledger/matrix/Q4 verification suite passed.

Printed p. 33 was visually checked: the source assumptions, coefficient map and Eq. (4.14) are legible, with no clipping. Printed p. 103 was rechecked: the updated Q3 roadmap and Table 39 fit on the page. Ten A/V claims were compared with rendered text:

| Ledger row | Rendered location | Comparison |
|---|---|---|
| OCL-164 (A) | Section 4.7, printed p. 33 | GK phonon-flux scope is attributed to the phonon Boltzmann treatment, not a ready-made continuum thermoelastic law. |
| OCL-165 (A) | Section 4.7, printed p. 33 | Rapid-normal-scattering condition and characteristic-length expression are present. |
| OCL-166 (A) | Section 4.7, printed pp. 33–34 | The pure-phonon continuum reduction remains attributed to Tzou, not the 1966 paper. |
| OCL-167 (A) | Section 4.7, printed p. 34 | The DPL parameter map is printed with its phonon-approximation scope. |
| OCL-169 (A) | Section 4.8, printed p. 34 | The first-order three-lag expansion and ordering are stated without generalizing later variants. |
| OCL-445 (A) | Table 6, printed p. 37; selection guide, p. 102 | Strict inequalities and unclassified equality remain visible for the specified one-dimensional problem. |
| OCL-466 (V) | Section 10.5.2, printed p. 68 | The two-amplitude system and determinant are present. |
| OCL-467 (V) | Section 16.2, printed p. 103 | The rendered summary records the cross-term/time-average scope; the calculation remains script-backed. |
| OCL-480 (V) | Section 10.2, printed p. 66 | The classical local flux and outward-positive convention remain within their stated assumptions. |
| OCL-498 (V) | Section 4.6, printed p. 33 | The zero-source Eq. (3.19)–(3.20) to Eq. (4.1)/(4.14) coefficient/variable map is visible; symbolic scope is limited to substitution. |

The ledger now validates at 498 rows: A=34, B=132, C=315, V=17. OCL-494 remains Class A for bounded source findings; OCL-498 is Class V for the algebraic map only; OCL-492 remains Class B for the energy/admissibility/interface-flux gaps. A separate Q5 visual check of Figure 11 (source F12) on printed p. 58 confirmed the previously flagged lower arrows cross through the Step 9/10 boxes and the feedback label overlaps a connector; this remains an open visual defect for WP5/Q5, not a passed figure review.
