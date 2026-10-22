# Separate quality gates — phase5 v1.1 source

## Engineering / build — NOT PASSED

- **Static structure checks:** passed for duplicate labels (0), unresolved reference labels (0), duplicate bibliography keys (0), missing citation keys (0), missing `\input`/`\include` files (0), missing bibliography files (0), and missing figure assets (0). Inventory: 37 TeX files (430 labels, 297 reference commands, 222 citation calls); malformed truncated ref fragments: 0; unescaped underscores in `\texttt` paths: 0; stray single Markdown-style backticks: 0.
- **Figure assets:** 18/18 PDFs generated from 18/18 parseable SVGs; vector drawing operators and extractable text confirmed. Contact-sheet overview reviewed. Individual final-size visual proof, caption match, scientific content, and license/source provenance remain open.
- **LaTeX compilation:** no successful build. Local TeX tools are absent; ten strict GitHub attempts failed (`39728213927`, `39728597464`, `39728900152` exit 12; `39729338751`, `39729569948`, `39729834892`, `39730189442`, `39730441139`, `39730774923`, `39731041813` exit 1). After the ref and path repairs, the latest run reached `energy_flux_derivations.tex` and failed on Markdown-style backticks around a candidate term. The source now uses `\texttt` and a static guard rejects stray single backticks; this change has not been rerun. The pre-fatal log also showed >1 pt overfull boxes in Appendices D/E; line-break edits were made but remain unverified. No v1.1 PDF was produced.
- **PDF inspection:** v1.0 baseline surveyed at overview scale only; no v1.1 PDF exists, so v1.1 page/text/box/font checks are NOT RUN.
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
