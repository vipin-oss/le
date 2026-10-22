# Separate quality gates — phase5 v1.1 source

## Engineering / build — NOT PASSED

- **Static structure checks:** passed for duplicate labels (0), unresolved reference labels (0), duplicate bibliography keys (0), missing citation keys (0), missing `\input`/`\include` files (0), missing bibliography files (0), and missing figure assets (0). Inventory: 37 TeX files (431 labels, 308 reference commands, 222 citation calls); malformed truncated ref fragments: 0; unescaped underscores in `\texttt` paths: 0; stray single Markdown-style backticks: 0.
- **Figure assets:** 18/18 PDFs generated from 18/18 parseable SVGs; vector drawing operators and extractable text confirmed. Contact-sheet overview reviewed. Individual final-size visual proof, caption match, scientific content, and license/source provenance remain open.
- **LaTeX compilation:** no strict successful build. Local TeX tools are absent; thirteen strict GitHub attempts failed (first three exit 12; last ten exit 1). The latest completed pdfLaTeX/BibTeX with zero fatal errors, unresolved refs/citations, missing files, or missing BibTeX keys, but the strict gate rejected 675 overfull boxes >1 pt. The largest sources were the comparison table and equation register. A split comparison table and constrained column widths are now in the working tree, unbuilt. The runner PDF was 148 pages but not uploaded; no local/inspectable PDF is available.
- **PDF inspection:** v1.0 baseline surveyed at overview scale only; the latest CI runner created a transient 148-page PDF, but the build gate failed before upload, so v1.1 page/text/box/font visual inspection is NOT RUN.
- **Strict warnings/cross-reference/BibTeX pass:** NOT PASSED. Static source scans are not a LaTeX or BibTeX build.

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

**Overall release decision:** do not call this a final scientific review, journal-ready submission, or completed audit. Treat this as a partially repaired v1.1 source workspace with explicit open gates.
