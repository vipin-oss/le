# Q5/WP5 figure-specific audit — Figure 11 workflow

**Status:** The targeted Figure 11/F12 correction and final-size check are complete. Q5/WP5 as a whole remains open for notation/abbreviation reconciliation, figure-source/licence provenance, and final-size review of the remaining figures and tables.

## Finding and correction

A visual inspection of the previous final CI PDF (printed p. 58) found that Figure 11's lower arrows crossed the Step 9/10 boxes and the feedback label overlapped a connector. In the corrected figure, the Step 4-to-5 row wrap, Step 8-to-9 energy-comparison route, Step 9-to-10 validation route, and Step 10-to-8 feedback route are separated from box interiors. The feedback label now sits in the open channel. Step 3/4 are described as a selected characteristic system and model-specific secular relation; the generic `J_j=q_j-σ_ji v_i` display and `R+T+A_int=1` closure were removed. Steps 8–10 now direct the reader to derive a selected-model flux, use matched reference planes, and validate only against specified evidence. The caption identifies the graphic as a model-specific checklist rather than a universal energy-ratio law.

The three SVG mirrors (`phase5/figures/source`, `phase5/master/figures/source`, and `phase5/master/figures/rendered`) are identical. The two tracked source PDFs were regenerated from that SVG with the repository's pinned renderer. `verify_fig12_workflow.py` checks mirror identity, ten step labels, intended connector routes, that routes avoid box interiors, absence of the removed generic flux/closure, and its OCL-499 Class V ledger path. It does not validate scientific conclusions or source/licence provenance.

## Content CI and visual check

Content commit `dc6cf8a` passed CI `40512329757`; the strict PDF remains 121 pages. Output publication commit `b8f562b` was fast-forwarded and matched the remote branch. Final build gates: undefined references/citations 0; overfull boxes >1 pt 0; near-overfull boxes >0.5 pt 0; privacy tokens 0; internal paths 0; manuscript tags 0; 18 figure PDFs rendered/16 included; deletion-audit `NONE` rows 0. The new workflow-figure verifier passed in CI. Broad-token CI annotations for `Primary-source`, `unverified`, and `R3` were false positives under the strict manuscript-tag pattern; the strict tag count remained zero.

Printed p. 58 was visually reviewed in the published PDF: all ten boxes and connector directions are clear, no arrows cross box interiors, the feedback label is separate from the loop, and the caption is legible without clipping. `git diff --check`, the figure verifier, and ledger validation passed locally.

## Ten A/V checks against the rendered text

| Ledger row | Rendered location | Check |
|---|---|---|
| OCL-164 (A) | Section 4.7, printed p. 33 | GK scope remains tied to the phonon Boltzmann treatment, not a ready-made continuum thermoelastic law. |
| OCL-165 (A) | Section 4.7, printed p. 33 | Rapid-normal-scattering condition, characteristic-length relation, and Ziman-averaged time are present. |
| OCL-166 (A) | Section 4.7, printed pp. 33–34 | Tzou's pure-phonon continuum reduction is not attributed to the 1966 paper. |
| OCL-167 (A) | Section 4.7, printed p. 34 | The DPL parameter map remains tied to Tzou's stated phonon approximation. |
| OCL-169 (A) | Section 4.8, printed p. 34 | First-order TPL expansion and lag ordering are visible; variants are not conflated. |
| OCL-445 (A) | Table 6, printed p. 37; guide, p. 102 | Strict inequalities and unclassified equality remain scoped to the cited 1D problem. |
| OCL-466 (V) | Section 10.5.2, printed p. 68 | The two-amplitude welded-interface system and determinant are present. |
| OCL-467 (V) | Section 16.2, printed p. 103 | The cross-term-before-averaging and zero-time-average summary is present; the derivation remains script-backed. |
| OCL-480 (V) | Section 10.2, printed p. 66 | The classical outward-positive flux convention is present within its stated scope. |
| OCL-499 (V) | Figure 11, printed p. 58 | The model-specific workflow, matched-plane ratios, specified-benchmark step, and bounded caption match the geometry-verified SVG. |

This is a ten-row spot check, not full validation of every figure, table, or scientific claim. OCL-499 is Class V for figure structure/layout only. `figure-audit.csv` records the F12 visual correction; original SVG authorship/licence provenance remains undocumented and open. The current ledger is 499 rows (A=34, B=132, C=315, V=18).
