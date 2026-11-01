# Page-Level Audit — compiled v1.2 against its LaTeX sources

**Date:** 2026-11-01 · **Scope:** P1, second half (page level) · **Status of table:** 26 checks, 20 PASS, 6 REPORT, 0 FAIL
**Method:** the compiled PDF is parsed with PyMuPDF and every check is a comparison against the `.tex`/`.bib` sources it was built from. No check is a judgement of prose quality; each is an assertion about what the document physically contains.

## 1. Document census

| Quantity | Measured |
|---|---|
| Pages | 140 |
| Words (extracted) | 63,503 |
| Body words, sections 1–17 (pp. 14–120) | 43,543 |
| Numbered equations printed | 136 (highest number = 136, no gaps) |
| Numbered figures printed | 16 (1–16, contiguous) |
| Numbered tables printed | 53 (1–53, contiguous) |
| Distinct works cited | 107 |
| Entries in `references_local.bib` | 144 (37 uncited reserve entries) |
| Printed references carrying a DOI | 104 |
| Printed references as books with ISBN | 2 |
| Printed references with neither (pre-DOI, stated plainly) | 2 |
| PDF outline (hyperref bookmarks) | 430 |
| Abstract | 245 words |
| Keywords | 11 |
| Unresolved `??` references | 0 |
| Missing citations `[?]` | 0 |
| Leaked LaTeX tokens in extracted text | 0 |
| Fonts without an embedded file | 0 |
| Pages with right-margin overflow (40 pt proxy) | 0 |

Story in one line: the document is a **140-page review paper** — not a book — whose front matter, 17 sections (pp. 14–120), reference list (pp. 121–126) and six appendices (pp. 127–140) all rendered with every reference and citation resolved.

## 2. Structure map (from hyperref bookmarks, cross-checked against `main.tex` order)

| Section | First page | | Section | First page |
|---|---|---|---|---|
| 1 Review Scope and Purpose | 14 | | 10 Energy Transport and Dissipation | 68 |
| 2 Literature Landscape and Scholarly Context | 17 | | 11 Advanced Theoretical Developments | 73 |
| 3 Foundations of Continuum Wave Mechanics | 21 | | 12 Comparative Synthesis of Existing Research | 78 |
| 4 Classical and Generalized Thermoelastic Theories | 31 | | 13 Applications of Multiphysics Wave Mechanics | 87 |
| 5 Coupled Multiphysics Continua | 43 | | 14 An Original Multidimensional Taxonomy | 94 |
| 6 Generalized Transport and Memory Effects | 50 | | 15 Major Scientific Challenges | 100 |
| 7 Nonlocal and Scale-Dependent Models | 54 | | 16 Future Research Opportunities | 107 |
| 8 Mathematical Methods for Wave Propagation | 58 | | 17 Conclusions and Scientific Outlook | 116 |
| 9 Reflection, Transmission, Interface Phenomena | 61 | | References | 121 |
| | | | A–F Appendices | 127, 134, 136, 137, 139, 140 |

Order is monotonic and matches the `\input` sequence in `main.tex` exactly; no section is bookmarked but missing from the body, and no source is orphaned from the build (check P23/P26). Row-level data: `section_pagemap.csv`.

## 3. Findings and dispositions

| # | Finding | Disposition |
|---|---|---|
| F1 | The equation register used **two status labels its own legend did not define** (`VERIFIED-SYMBOLIC` on EQ-014, `WITHHELD` on EQ-017). 29 rows, 8 labels, 6 defined. | Legend extended with two definitions written strictly from those rows' own source-note columns. **No verdict was altered** (the standing rule is that verdict columns are not rewritten unilaterally). |
| F2 | `appendices/energy_flux_derivations.tex` (371 lines) was a **dead file**: never `\input` by `main.tex`, yet shipped inside the build tree. Its own header calls it "a retained, unverified working collection" and its headings are "Open audit item 1…10". | Moved to `paper_v2/working_notes/` as a retained working collection; the two Appendix-A cross-references that pointed at it were re-pointed. Nothing cites it, so no reference in the built PDF changed. |
| F3 | Equation-register coverage: **29 of 136 printed equations** (21.3%). Derived + primary-source-checked = 6 of 29 rows (20.7%). | Reported, not patched. The manuscript already states that no comprehensive equation audit has been completed; this quantifies the gap and is the main remaining item for P1. |
| F4 | 37 `.bib` entries are uncited by the manuscript. | Reported. They are a reserve list (none is cited by the retained working collection either); no entry removed, since deleting bibliography is not an editorial improvement. |
| F5 | Three cited works carried no DOI/ISBN: Cattaneo 1948, Vernotte 1958, Chester 1963. | Chester 1963 **verified against Crossref** (Physical Review 131, 2013–2015, author/title/journal/volume/pages all match) and its DOI recorded; Cattaneo and Vernotte are pre-DOI and now state that plainly in the entry. No DOI was guessed. |
| F6 | Source drift: after F1/F2/F5 the sources are newer than the PDF that was measured. | Recorded as P25 (REPORT). A rebuild is required before submission; the drift list is in `page_audit_results.csv`. |
| F7 | Typography at the level measurable from a PDF: no unresolved references, no leaked control sequences, no missing fonts, no caption missing, no figure/table number gap, no margin overflow. | Nothing to fix. Overfull `\hbox` warnings are a compile-log property and are not recoverable from the PDF; they remain on the Overleaf log, not in this audit. |

## 4. What this audit does **not** establish

- It does not verify that any equation is correct in physics — that is the register's job (see F3), and its verdict column is the author's, not the auditor's.
- It cannot see `Overfull \hbox` warnings, missing-glyph warnings, or float-placement decisions; those exist only in the compile log.
- It does not re-verify DOIs that were verified earlier; it only checks that a printed reference matches a cited key.

## 5. Files

| File | Contents |
|---|---|
| `audit_pages.py` | the audit itself (PDF ↔ sources, 26 checks) |
| `page_audit_results.csv` | one row per checked object: `check_id, object, expected, observed, verdict, note` |
| `PAGE_AUDIT_SUMMARY.md` | machine-written summary, regenerated on every run |
| `section_pagemap.csv` | section → first page, derived from bookmarks |
| `check_page_audit.py` | gate: prints `PASS (...)` and exits 0 only if the state above holds |

Reproduce:

```bash
python3 P1_audit/audit_pages.py --pdf /path/to/compiled.pdf --master ../manuscript_v2/master --out P1_audit
python3 P1_audit/check_page_audit.py
```
