# Q4 conditional selection guide and evidence audit

**Date:** 2026-10-27  
**Status:** Drafted and locally validated; a content build is pending the Q4 commit and its single required CI run.

## Scope

Section 1 was narrowed to describe the review's evidence-bounded scope rather than promise uniform constitutive, admissibility, computation, or interface results across all families. Section 16 now contains a conditional model-selection workflow, a table separating script-verified checks from primary-source checkpoints, a note distinguishing Appendix C benchmark specifications from validated numerical reference solutions, and a Q3-derived roadmap. No new bibliography item or new primary-source claim was introduced.

The guide is explicitly not a theory ranking. It requires the actual equations, fields, geometry, initial/boundary data, interface conditions, and measured observables to be specified. It does not infer finite propagation speed, stability, thermodynamic admissibility, well-posedness, energy flux, or mode counts from a family label.

## Evidence map retained in the guide

| Guide entry | Evidence and limitation |
|---|---|
| Local Cauchy/Fourier baseline | OCL-480 (Class V, local balance/flux derivation); no generalized thermoelastic flux claim. |
| Lord–Shulman | OCL-495 (Class A, page-image-checked source-specific law/system); OCL-011 remains Class C for the unresolved parameter/admissibility claim. |
| GN-II / GN-III | OCL-493/OCL-494 (Class A, source-bounded page-image findings); OCL-491/OCL-492 remain Class B for equation-to-manuscript and energy/interface work. |
| DPL / TPL | OCL-445 (Class A, source-bounded strict-inequality result for the stated one-dimensional problem); OCL-488 retains the DOI/source-page conflict and equality remains unclassified. OCL-169 supports only the cited first-order TPL formulation; OCL-123 remains open for higher-order variants. |
| Spatial, fractional, hereditary, and coupled fields | The guide asks for exact operator/kernel/closure and data. It preserves bounded source rows (including OCL-195, OCL-258, OCL-321) and open comparison/status rows (including OCL-402, OCL-403, OCL-483, OCL-485); no family-wide properties are inferred. |

## Benchmark evidence distinction

- **Script-verified calculations:** OCL-480 records the classical local flux derivation; OCL-466–468 record the selected one-dimensional welded-interface stress/velocity-flux calculation and distinguish the algebraic closure from an independent conservation theorem; OCL-470–473 record displayed-equation reductions and limits, not solution convergence or family equivalence.
- **Primary-source checkpoints:** OCL-493–496 are bounded source-page findings, not code-validated numerical solutions or full well-posedness proofs.
- **Problem specifications:** Appendix C BM-1–BM-5 specify comparison problems/observables. They are not represented as validated numerical reference solutions unless a separate script-backed check is explicitly identified.

## Q3-derived roadmap

The Section 16 roadmap keeps open: the GN-I equation/source mapping; an image check of GN-III printed p. 255, whose type-II/type-III distinction remains text-extraction-only; equation-to-manuscript reconciliation for selected GN-II/GN-III/LS formulations; exact-model parameter admissibility and well-posedness; bulk and interface energy flux derivations; and extensions of benchmarks only after equations, data, normalization, and observables are fixed. These are work items, not completed results.

## Hostile review of the preceding docs-only source updates

Reviewed the documentation changes from `a477548` through `7814bf0` on the fixed branch, including `a477548`, `a3220c7`, `a072010`, and `7814bf0`; the CI-output publication commit `3499c26` was checked as a distinct generated artifact update.

- The GL, GN-I, GN-II, GN-III, and LS records retain source/page bounds and explicitly keep broader parameter, stability, existence, family-wide, and energy/interface claims open. GN-I remains unresolved; GN-II/GN-III/LS additions are narrowly anchored to the reviewed printed pages.
- GN-III's p. 255 distinction remains text-extraction-only; the later equation/regime pages are described as image-reviewed. No type-II result is transferred to type III.
- The DPL DOI/source-page disagreement remains visible under OCL-488; equality is still unclassified. The Kumar split verifier still confirms all 19 dependent rows remain B/C.
- The generated manuscript PDF and build README correspond to successful CI `40499379538` for content commit `6e8cf1e`; the later report-only updates did not replace that build. Keep the read-only older `e56755f` report's 130-page manuscript distinct from the fixed-branch PDF's 119-page artifact.
- The separate private Drive link/ID scan of seven changed text files returned zero hits; `git diff --check` passed. No material unsupported class promotion or privacy leak was identified in this review.

## Local checks for the Q4 change

The following passed locally before commit:

- `verify_q3_status_matrix.py`
- `verify_q4_selection_guide.py`
- `verify_unified_reductions.py`
- `verify_interface_energy.py`
- `verify_interface_mode_counts.py`
- `verify_q1_notation.py`
- `verify_kumar2017_reference_split.py`
- `validate_claim_ledger.py`
- `git diff --check`

Ledger state is 497 rows: A=34, B=132, C=315, V=16. The new OCL-497 is Class V for structural coverage/provenance mapping only; its verifier does not re-review sources or validate numerical solutions. The local environment lacks TeX build tools, so rendered-page, strict-box, undefined-reference, and rendered-text privacy gates remain pending CI.
