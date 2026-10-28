# Q5/WP5 figure-specific audit — Figure 11 workflow

**Status:** The targeted Figure 11/F12 correction and final-size check are complete. Q5/WP5 as a whole remains open for notation/abbreviation reconciliation, figure-source/licence provenance, completion of table review, and page-level final-size review of the newly corrected F06 artwork in the next rebuilt manuscript PDF.

## Finding and correction

A visual inspection of the previous final CI PDF (printed p. 58) found that Figure 11's lower arrows crossed the Step 9/10 boxes and the feedback label overlapped a connector. In the corrected figure, the Step 4-to-5 row wrap, Step 8-to-9 energy-comparison route, Step 9-to-10 validation route, and Step 10-to-8 feedback route are separated from box interiors. The feedback label now sits in the open channel. Step 3/4 are described as a selected characteristic system and model-specific secular relation; the generic `J_j=q_j-σ_ji v_i` display and `R+T+A_int=1` closure were removed. Steps 8–10 now direct the reader to derive a selected-model flux, use matched reference planes, and validate only against specified evidence. The caption identifies the graphic as a model-specific checklist rather than a universal energy-ratio law.

The three SVG mirrors (`phase5/figures/source`, `phase5/master/figures/source`, and `phase5/master/figures/rendered`) are identical. The two tracked source PDFs were regenerated from that SVG with the repository's pinned renderer. `verify_fig12_workflow.py` checks mirror identity, ten step labels, intended connector routes, that routes avoid box interiors, absence of the removed generic flux/closure, and its OCL-499 Class V ledger path. It does not validate scientific conclusions or source/licence provenance.

## Content CI and visual check

Content commit `dc6cf8a` passed CI `40512329757`; the strict PDF remains 121 pages. Output publication commit `b8f562b` was fast-forwarded and matched the remote branch. Final build gates: undefined references/citations 0; overfull boxes >1 pt 0; near-overfull boxes >0.5 pt 0; privacy tokens 0; internal paths 0; manuscript tags 0; 18 figure PDFs rendered/16 included; deletion-audit `NONE` rows 0. The new workflow-figure verifier passed in CI. Broad-token CI annotations for `Primary-source`, `unverified`, and `R3` were false positives under the strict manuscript-tag pattern; the strict tag count remained zero.

Printed p. 58 was visually reviewed in the published PDF: all ten boxes and connector directions are clear, no arrows cross box interiors, the feedback label is separate from the loop, and the caption is legible without clipping. `git diff --check`, the figure verifier, and ledger validation passed locally.

A subsequent WP3 verification commit `552ba67` changed only the citation-key/Crossref verifier and CI workflow, not manuscript source or bibliography. CI `40514426363` passed and published the 121-page PDF in output commit `9f3afae`. The ten A/V rows below were rechecked against this latest rendered text, and printed p. 58 was rendered and visually reviewed again; the F12 geometry and caption remain clear. Latest build metrics and reference-hygiene results are recorded in `WP3_REFERENCE_HYGIENE_AUDIT.md` and `build-status.md`.

## Ten A/V checks against the latest rendered text

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


## Updated figure-layout review (2026-10-28)

Nine targeted figure-layout corrections were included in content commit `9c69852` and LaTeX CI run `40704135288`. The regenerated 122-page manuscript PDF was visually reviewed at final page scale. The corrected artwork is clear at these PDF page anchors (printed page in parentheses): F03, p. 20 (19); F04, p. 22 (21); F05, p. 28 (27); F09, p. 42 (41); F08, p. 48 (47); F10, p. 52 (51); F11, p. 55 (54); F15, p. 76 (75); and F16, p. 84 (83). F12 also remains clear at PDF p. 60 (printed p. 59). At p. 42 the multiphysics arrows are behind the node fills and labels; at p. 84 the notes now align within both bottom panels.

The page-level review exposed a filename/caption mismatch in the earlier issue list: PDF Figure 5 on p. 26 (printed p. 25) is sourced from `fig06-classical-waves.svg`, not F05. Its bottom-row labels overlapped, and the motion annotations clipped at the panel edge. F06 has now been repaired in the standalone PDF and the bottom speed labels and wave annotations have been re-reviewed; its rebuilt manuscript page remains pending the next CI PDF. The local checkout has no TeX engine, so only CI can produce the next full manuscript build.

The standalone proofs were also rendered at 1.1× as an approximate inclusion-size check; they do not substitute for the page-level reviews above. Figure content remains schematic and is not thereby source-verified. Notation/abbreviation reconciliation, complete table review, and original SVG authorship/licence provenance remain open. The 18-file vector PDF build completed with zero SVG warnings; `git diff --check` passed.
