# Historical quality-gate report — phase5 v1.1 snapshot

> **Historical snapshot:** this report describes the earlier 146-page run `39753968114`. It is not the current build status. The current 130-page engineering PASS is run `40372932181`; see [`build-status.md`](build-status.md).

## Engineering / build — STRICT CI PASSED; CONTACT-SHEET OVERVIEW REVIEW COMPLETE

- **Static structure checks:** passed for duplicate labels (0), unresolved reference labels (0), duplicate bibliography keys (0), missing citation keys (0), missing `\input`/`\include` files (0), missing bibliography files (0), and missing figure assets (0). Inventory: 37 TeX files (431 labels, 308 reference commands, 222 citation calls); malformed truncated ref fragments: 0; unescaped underscores in `\texttt` paths: 0; stray single Markdown-style backticks: 0.
- **Figure assets:** 18/18 PDFs generated from 18/18 parseable SVGs; vector drawing operators and extractable text confirmed. Contact-sheet overview reviewed. Individual final-size visual proof, caption match, scientific content, and license/source provenance remain open.
- **LaTeX compilation:** strict CI run `39753968114` passed; it generated a 146-page PDF, passed the required font check and unchanged strict gate, and committed the PDF/contact sheets under `phase5/build_outputs/`. No threshold was weakened.
- **PDF inspection:** all four 100-dpi sheets (40 pages max per sheet) were reviewed at overview scale; no blank page, obvious clipping/overlap, missing figure, or scratch text was evident. All 18 figure captions occur in the final PDF. This is not full-page-at-100%-zoom proofreading or scientific correctness review.
- **Strict warnings/cross-reference/BibTeX pass:** strict CI PASSED. Detailed run `39745464117` found zero duplicate destinations, PDF-string token warnings, and `[h]` warnings; final run `39753968114` reports 416 underfull hboxes and 0 underfull vboxes. No global suppression was used; no visible damage attributable to the underfull warnings was apparent at contact-sheet scale.

## Scientific — NOT PASSED

- Classical local total-energy density and outward-positive flux: DERIVED in the source from displayed local balances and symbolically checked under stated assumptions.
- Corrected model descriptions/dispersion statements: limited edits made; selected results are conditional.
- Primary-source equation verification, generalized energy-flux derivations, nonlocal boundary power, piezothermoelectric flux, material-parameter benchmarks, and claim-level reference checks: OPEN or UNVERIFIED.
- No new benchmark values, numerical experiments, or scientific plots were generated.

## Editorial / submission readiness — NOT PASSED

- The abstract and several corrected sections were edited.
- A generic article wrapper and separate supplement wrapper exist, but no target journal was specified and no journal-specific style, scope, length, author, ethics, data, or citation requirements were checked.
- No page-level proofread, final-size figure legibility inspection, bibliography layout check, or final PDF proofreading was possible.
- The generalized energy appendix retains only explicitly labelled source leads/open items; it requires full scientific reconciliation before submission.

**Overall release decision:** Part 1/R1 engineering and requested output/reconciliation checks are complete, with 416 underfull hboxes recorded as nonfatal and no obvious damage at contact-sheet scale. Per the task instruction, Part 2 has not started. Do not call this a final scientific review, journal-ready submission, or completed scientific audit.
