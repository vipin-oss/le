# Page-Level Audit — compiled v1.2 against its LaTeX sources

**Date:** 2026-11-01 · **Scope:** P1, second half (page level) · **Status of table:** 26 checks, 21 PASS, 5 REPORT, 0 FAIL
**Build measured:** the author's rebuild, compiled 2026-11-01 16:58:57 UTC (the earlier 16:39 build was measured first; its findings are kept below in F1–F5 and were re-verified on the rebuild in F8)
**Method:** the compiled PDF is parsed with PyMuPDF and every check is a comparison against the `.tex`/`.bib` sources it was built from. No check is a judgement of prose quality; each is an assertion about what the document physically contains.

## 1. Document census

| Quantity | Measured |
|---|---|
| Pages | 140 |
| Words (extracted) | 63,584 |
| Body words, sections 1–17 (pp. 14–120) | 43,543 |
| Numbered equations printed | 136 (highest number = 136, no gaps) |
| Numbered figures printed | 16 (1–16, contiguous) |
| Numbered tables printed | 53 (1–53, contiguous) |
| Distinct works cited | 107 |
| Entries in `references_local.bib` | 144 (37 uncited reserve entries) |
| Printed references carrying a DOI | 104 (103 + Chester 1963) |
| Printed references as books with ISBN | 2 |
| Printed references with neither (pre-DOI, stated plainly in the entry) | 2 |
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
| F6 | Source drift: after F1/F2/F5 the sources were newer than the PDF that had been measured. | **Closed.** The author rebuilt; on the rebuild every source predates the PDF, so P25 flips to PASS. No file remains drifted. |
| F7 | Typography at the level measurable from a PDF: no unresolved references, no leaked control sequences, no missing fonts, no caption missing, no figure/table number gap, no margin overflow. | Nothing to fix. Overfull `\hbox` warnings are a compile-log property and are not recoverable from the PDF; they remain on the Overleaf log, not in this audit. |

## 4. What this audit does **not** establish

- It does not verify that any equation is correct in physics — that is the register's job (see F3), and its verdict column is the author's, not the auditor's.
- It cannot see `Overfull \hbox` warnings, missing-glyph warnings, or float-placement decisions; those exist only in the compile log.
- It does not re-verify DOIs that were verified earlier; it only checks that a printed reference matches a cited key.

## 5. Rebuild verification (F8)

The rebuild was checked string by string, not assumed. Each fix is present in the artefact a reader receives:

| Fix | What the rebuild prints |
|---|---|
| Legend (F1) | `VERIFIED-SYMBOLIC: A closed-form expression checked by symbolic evaluation in this revision for a stated limiting case (e.g. the uncoupled thermal branch); …` and `WITHHELD: No expression is asserted; …` |
| Register row EQ-014 | `EQ-014 c_T = √(k/(ρc_vτ_0)) VERIFIED-SYMBOLIC Uncoupled scalar thermal branch β = 0; …` |
| Re-pointed note (F2) | `EQ-029 … OPEN Withdrawn from the retained working collection; …`, and the closing Appendix-A sentence now reads `… in the retained working collection (which is deliberately not part of this manuscript) …` |
| Chester 1963 (F5) | `Marvin Chester. Second sound in solids. Physical Review, 131:2013–2015, 1963. doi: 10.1103/physrev.131.2013` |
| Pre-DOI works (F5) | `C. Cattaneo. Sulla conduzione del calore. … 3:83–101, 1948. No DOI assigned: published before DOIs were issued.` and the same note on Vernotte 1958 |

Extent and structure are unchanged by these edits: still 140 pages, 16 figures, 53 tables, 136 numbered equations, six appendices; word count moves from 63,503 to 63,584 (+81 words, i.e. exactly the two legend definitions and the two no-DOI notes).

## 6. Equation inventory and register traceability (F9)

`build_equation_inventory.py` reads the sources in `\input` order and lists **every** numbered equation, then
cross-checks the list against the numbering actually printed.

| Measured | Value |
|---|---|
| Numbered equations in the sources | 136 — all `equation` environments, **all labelled**, none unnumbered |
| Highest number printed in the PDF | 136; distinct numbers printed 136 |
| Agreement | exact (`equation_inventory.csv`, `printed,label,section,subsection,file`) |

The register, however, had **no pointer at all** to any printed equation: no `\eqref`, no `\ref` in any of its
29 rows. So each row was matched to the printed equation(s) whose content actually contains that row's own
mathematics (`register_linkage.csv`):

| Linkage | Rows | Meaning |
|---|---|---|
| unique | 9 | the row's math appears in exactly one printed equation |
| unique-in-main-text | 2 | appears in one main-text equation plus an Appendix-B restatement; the main-text instance is the canonical one |
| multiple | 4 | appears in several printed equations (e.g. EQ-004 in eq:3.13, eq:3.14, eq:4.21 and two Appendix-B restatements) — choosing is the author's call |
| none (14) | 14 | the row is a prose description ("Mechanical power balance", "Coleman–Noll restrictions"), so there is nothing mechanical to match |

**11 of 29 rows (38%) can therefore be tied to a printed equation with no judgement at all; 18 cannot.**
That is the traceability gap, stated as a number instead of an impression. Deliberately **not** patched in this
cycle: adding 11 pointers while 18 rows stay unlinked would leave a half-linked table, and pointing a register
row at the wrong equation is worse than pointing at none.

## 7. Cycle-3 editorial additions and how the audit treats them

Three additions were made in the same day's citation-oriented pass (no new scientific claim; see
`REVIEW_CYCLES.md` cycle 3): Table `tab:contributions` in §1 (C1–C7 with delivery locations), a rewritten §2.7
evidence protocol (`sec:evidence_protocol`), and Table `tab:research-questions` in §16 (R1–R10 with what would
settle each). Eleven `\eqref` pointers were added to register rows whose mathematics occurs in exactly one printed
equation.

Because the sources are now newer than the last build, the audit reports these as **pending rebuild** rather than
missing: P06 says `1 not in this PDF (1 pending rebuild, 0 unexplained)` and P12 says
`70 present, 2 pending rebuild, 0 unexplained`. The difference matters — a title that is absent because nobody
rebuilt is not a defect in the document, and a title that is absent because a source is orphaned is. Making that
distinction exposed a real bug in this audit's own caption check (it compared one character of a caption instead
of the caption, and passed silently); it is fixed, and the check now counts 72 captions.

## 8. Files

| File | Contents |
|---|---|
| `audit_pages.py` | the audit itself (PDF ↔ sources, 26 checks) |
| `page_audit_results.csv` | one row per checked object: `check_id, object, expected, observed, verdict, note` |
| `PAGE_AUDIT_SUMMARY.md` | machine-written summary, regenerated on every run |
| `section_pagemap.csv` | section → first page, derived from bookmarks |
| `check_page_audit.py` | gate: prints `PASS (...)` and exits 0 only if the state above holds |
| `check_refs.py` | static gate for what a compiler would catch first (labels, refs, cites, braces, environments, float labels, input targets) |
| `build_equation_inventory.py` | builds the 136-row inventory and the 29-row register linkage |
| `equation_inventory.csv` | every printed equation: number, label, section, subsection, file |
| `register_linkage.csv` | every register row: status, candidate printed equations, linkage class |

Reproduce:

```bash
python3 P1_audit/audit_pages.py --pdf /path/to/compiled.pdf --master ../manuscript_v2/master --out P1_audit
python3 P1_audit/build_equation_inventory.py --master ../manuscript_v2/master --pdf /path/to/compiled.pdf
python3 P1_audit/check_page_audit.py      # now also fails if the inventory is incomplete or disagrees with the PDF
```
