# Separate quality gates — phase5 v1.1 source

## Engineering / build — STRICT CI PASSED; VISUAL REVIEW OPEN

- **Static structure checks:** passed for duplicate labels (0), unresolved reference labels (0), duplicate bibliography keys (0), missing citation keys (0), missing `\input`/`\include` files (0), missing bibliography files (0), and missing figure assets (0). Inventory: 37 TeX files (431 labels, 308 reference commands, 222 citation calls); malformed truncated ref fragments: 0; unescaped underscores in `\texttt` paths: 0; stray single Markdown-style backticks: 0.
- **Figure assets:** 18/18 PDFs generated from 18/18 parseable SVGs; vector drawing operators and extractable text confirmed. Contact-sheet overview reviewed. Individual final-size visual proof, caption match, scientific content, and license/source provenance remain open.
- **LaTeX compilation:** strict CI run `39748215109` on commit `5df59c6d4d6d3eb0915d8fbc47fc2302cc330604` passed with no weakened thresholds. It generated a 146-page PDF; the required font check, strict build, contact-sheet rendering, and artifact uploads succeeded. The preceding detailed font report found all 77 resources embedded.
- **PDF inspection:** the 161-page v1.0 baseline was surveyed at overview scale. The final v1.1 PDF and contact sheets were generated and uploaded, but artifact download returns EOF here; final page/text/box/font visual inspection is NOT RUN.
- **Strict warnings/cross-reference/BibTeX pass:** strict CI PASSED. Detailed run `39745464117` found zero duplicate destinations, PDF-string token warnings, and `[h]` warnings; 416 underfull hboxes remain to review (latest count unavailable). Underfull warnings were not globally suppressed.

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

**Overall release decision:** the strict engineering build gate passed in run `39748215109`, but Part 1/R1 is not yet complete because final PDF/contact-sheet review, page-count reconciliation, and the remaining underfull-warning disposition are open. Do not begin Part 2 yet. Do not call this a final scientific review, journal-ready submission, or completed audit.
