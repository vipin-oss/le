# Separate quality gates — version 1.1 source

## Engineering / build — NOT PASSED

- **Static structure checks:** passed for duplicate labels (0), unresolved reference labels (0), duplicate bibliography keys (0), missing citation keys (0), missing `\\input`/`\\include` files (0), missing bibliography files (0), and missing figure assets (0), using `scripts/audit_inventory.py` on 37 TeX files (430 labels, 293 reference commands, 222 citation calls).
- **Figure assets:** 18/18 PDFs generated from 18/18 parseable SVGs; vector drawing operators and extractable text confirmed. Contact-sheet overview reviewed. Individual final-size visual proof, caption match, scientific content, and license/source provenance remain open.
- **LaTeX compilation:** NOT RUN; `pdflatex`, `latexmk`, and `tectonic` are unavailable. The strict build scripts/workflow are prepared but untested.
- **PDF inspection:** v1.0 baseline surveyed at overview scale only; no v1.1 PDF exists, so v1.1 page/text/box/font checks are NOT RUN.
- **Strict warnings/cross-reference/BibTeX pass:** NOT RUN. A static source scan is not a LaTeX or BibTeX build.

## Scientific — NOT PASSED

- Classical local total-energy density and outward-positive flux: DERIVED in the source from displayed local balances.
- Corrected model descriptions/dispersion statements: limited algebraic edits made; selected results are conditional.
- Primary-source equation verification, generalized energy-flux derivations, nonlocal boundary power, piezothermoelectric flux, material-parameter benchmarks, and claim-level reference checks: OPEN or UNVERIFIED.
- No new benchmark values, numerical experiments, or scientific plots were generated.

## Editorial / submission readiness — NOT PASSED

- The abstract and several corrected sections were edited.
- A generic article wrapper and separate supplement wrapper exist, but no target journal was specified and no journal-specific style, scope, length, author, ethics, data, or citation requirements were checked.
- No page-level proofread, figure legibility inspection, bibliography layout check, or final PDF proofreading was possible.
- The legacy energy-flux derivation appendix still contains unverified working formulas under a prominent warning; it requires full editorial and scientific reconciliation before submission.

**Overall release decision:** do not call this a final scientific review, journal-ready submission, or completed audit. Treat this as a partially repaired v1.1 source workspace with explicit open gates.