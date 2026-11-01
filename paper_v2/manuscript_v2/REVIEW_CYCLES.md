# Review cycles — author → reviewer → editor → author

The manuscript is revised in named cycles. Each cycle records what was looked at, what was found, what was
changed, and what was deliberately left alone. Nothing in a cycle edits a source silently: every change is in git.

**Where the text lives.**
- `paper_v2/versions/v1.1_source_snapshot/` — the sources exactly as they were received (branch
  `arena/36bc8cc8-le`, tip 2026-10-28). Never edited, kept as the record.
- `paper_v2/manuscript_v2/` — the working master, revised in cycles. Every cycle bumps the version in
  `CHANGELOG_v2.md`.

**What can be verified here, and what cannot.** There is no TeX engine in this environment (no `pdflatex`,
no CTAN access), so the PDF is built on Overleaf. Everything that can be checked statically *is* checked here:
cross-references, labels, citations against the bibliography, `\input` chains, figure files, duplicate labels,
figure/table counts, placeholders, front matter, declarations. Page-level claims (signs, dimensions, derivations)
are checked line by line against the printed equations and the appendix equation register, not by compiling.

---

## Cycle 1 — v1.2 (2026-11-01)

### Author pass (write)
- Wrote a new abstract: the old one was 123 words and said what the review *covers*; it did not say what the
  reader gets. The new one is 259 words, keeps every scoped statement of the old one verbatim (the energy-flux
  split, Lord–Shulman vs Green–Lindsay, the bounded nonlocal frequency, the absence of a propagating EM branch),
  and adds the constructive promise: assumptions → modes → closed-form benchmark or stated mode count, plus the
  five-axis taxonomy and the model-selection guide.
- Added **keywords** (11 terms) — the manuscript had none.
- Added a **Declarations** section: CRediT author contributions, funding, competing interests, data availability,
  and a plain statement of how generative tools were used. It is placed before the bibliography, where journals
  expect it. The data-availability statement points at the benchmark scripts and the appendix tables that print
  measured value, reference value and residual, because that is what actually makes the numbers checkable.
- Wrapped the abstract in `\begin{abstract}…\end{abstract}`; in v1.1 the abstract text was `\input` raw, with no
  environment, so it ran straight into the notation section without a heading.
- Replaced the hard-coded title-page date `22 October 2026` with `\today` and left a comment for the author's
  affiliation and correspondence address rather than inventing one.

### Reviewer pass (check)
- **Duplicate table sources (finding A2b).** Eight table sources existed twice, at `master/tables/source/` and
  `tables/source/`. Only the `master/` copies are reached by the `\input` chain. The duplicate has been removed
  from the working master and kept in the v1.1 snapshot.
- **Dangling citation (finding A3).** `Eringen1968b` was cited in `tables/source/T3_coupled_multiphysics.tex` and
  existed in no bibliography file. Checked: the citation is in the *stale duplicate* only — the live
  `master/tables/source/T3_coupled_multiphysics.tex` does not contain it. Removing the duplicate resolved it, and
  no bibliography entry was invented to paper over it.
- **Five appendices existed but were never compiled.** v1.1 `\input`-ed only `appB` and `appC`. `appA` (equation
  register), `appD` (figure-status table), `appE` (table index) and `appF` (reproducibility notes) sat in the tree
  unreachable. All six are now in the appendix chain, in order, each starting on a new page. `appD` matters in
  particular: it is where the manuscript declares which figures are provisional, and a declaration nobody compiles
  is not a declaration.
- **Two figures shipped but never included (finding A11).** `fig07-theory-map` and `fig18-taxonomy` are not
  included anywhere. Checked against `appD_figures.tex`: both are declared provisional there (F-07 "provisional
  taxonomy; links are not verified limits", F-18 "content check open"). They are therefore **not** wired into the
  text — an unverified taxonomy diagram in the taxonomy section would be exactly the overclaim this review warns
  against. Now that `appD` is compiled, the reader is told instead. The audit reports them as declared, not as
  missing.

### Editor pass (decide)
- Structure accepted as is: 17 numbered sections, 6 appendices, declarations, bibliography. The section order
  (scope → literature strategy → foundations → thermoelastic → multiphysics → transport → nonlocal → methods →
  interfaces → energy → advanced → comparative → applications → taxonomy → challenges → future → conclusions)
  is a defensible review arc and is not rearranged for the sake of rearranging it.
- Ruled that the review may not claim case-level results: the atlas has 40 executable invariants and **0**
  case-level results. Any sentence that reads as a result must be a benchmark result (which is checkable) or a
  statement about modes/limits (which is derivable).
- Ruled that the "134 pages" figure, repeated in the project gates, is retired: the builds are 126 pages (phase 5
  v1.1) and 161 (phase 4). Planning against 134 was planning against nothing.

### Author pass (fix)
- Applied everything above to `paper_v2/manuscript_v2/`.
- Re-ran `P1_audit/audit_sources.py` against the revised master: **A1, A2, A3, A4, A5, A6, A7, A9, A2b all PASS**;
  A11 flags the two declared-provisional figures; A8 (294 unreferenced labels) and A10 (22 titles in more than one
  bib file) remain informational.

**Open at the end of cycle 1:** the page-level pass (signs, dimensions, derivations of the 166 numbered
equations), notation consistency across sections, and the D3 question — which of the 45 scripts actually assert
anything.

---

## Cycle 2 — page level (2026-11-01)

The compiled v1.2 build was measured page by page against the sources it came from:
**140 pages, 63,503 words, 136 numbered equations, 16 figures, 53 tables, 107 cited works,
430 bookmarks, 0 unresolved references, 0 missing citations, 0 leaked control sequences.**
Result: `arena_deliverables/P1_audit/PAGE_LEVEL_AUDIT_2026-11-01.md`, 26 checks, 0 FAIL.

### Reviewer pass (read the artefact, not the plan)
- The document a reader receives is a **review paper**: front matter pp. 1–13, seventeen sections pp. 14–120,
  reference list pp. 121–126, six appendices pp. 127–140. No book apparatus; no chapter-level scaffolding.
- Every section in `main.tex` is bookmarked and its page increases in source order; no source file is
  orphaned from the build, and no bookmark points at a section the build does not contain.
- Two defects that a plan-level audit cannot see, because they only exist in the artefact:
  1. Appendix A used two status labels its own legend never defined.
  2. An un-`\input` file (371 lines, headings "Open audit item 1…10") sat inside the build tree and was
     being shipped in the zip as if it were part of the paper.

### Editor pass (decide)
- **Label vs legend:** legend extended by two definitions written from those rows' own source notes.
  The verdict column is the author's record and was **not** rewritten. Decided, not deferred.
- **Orphan file:** it is a working collection by its own description; it is not an appendix of this review and
  its "open audit item" voice would contradict the review's register discipline. Moved out of the build tree to
  `paper_v2/working_notes/`, pre-edit copy kept in `paper_v2/versions/v1.2_edits_2026-11-01/`. The two
  Appendix-A sentences that pointed at it were re-pointed.
- **The "166 numbered equations" figure used in planning is retired**, on the same grounds as the "134 pages"
  figure in cycle 1: the build prints **136** numbered equations. Planning against 166 was planning against a
  number nobody had counted.
- **Register coverage is stated, not hidden:** 29 register rows cover 29 canonical equations of 136 printed
  (21.3%); 6 of the 29 rows are DERIVED or PRIMARY-SOURCE-CHECKED. The manuscript already says no comprehensive
  equation audit has been done; this puts a measured number on the sentence. Expanding the register is the
  remaining P1 item and is recorded as open rather than manufactured.

### Author pass (fix)
- `appA_equation_register.tex`: legend + two re-pointed sentences. `references_local.bib`: Chester 1963 DOI
  verified against Crossref (Physical Review 131, 2013–2015 — author, title, journal, volume and pages all
  match) and recorded; Cattaneo 1948 and Vernotte 1958 state plainly that no DOI exists.
- `P1_audit/audit_pages.py` (26 checks) + `check_page_audit.py` gate + `section_pagemap.csv`. The source-audit
  gate now asserts that the **frozen v1.1 snapshot** is untouched and that every change to the working sources
  is declared in the version log — previously it forbade editing the working tree at all, which contradicted
  the standing rule that sources may be edited when the old file is kept.

### Rebuild verification (same cycle, later)
The author rebuilt (16:58:57 UTC) and the rebuild was audited rather than assumed: **26 checks, 21 PASS, 5 REPORT,
0 FAIL**, 140 pages, 63,584 words (+81 = the two legend definitions and the two no-DOI notes). Every fix was
confirmed string by string in the artefact — legend labels, the EQ-014 and EQ-029 rows, the re-pointed
Appendix-A sentence, `doi: 10.1103/physrev.131.2013` on Chester 1963, and the two "No DOI assigned" notes.
The source-drift check (P25) flipped from REPORT to PASS, so nothing in the tree is newer than the PDF.

### Register traceability (measured, not asserted)
Every numbered equation was inventoried in print order — **136 of them, all labelled**, agreeing exactly with the
numbering the PDF prints. The register turns out to carry **no `\eqref` or `\ref` at all**, so each of its 29 rows
was matched to the printed equation containing that row's own mathematics: 9 unique, 2 unique once Appendix-B
restatements are set aside, 4 with several candidate restatements, 14 with no mathematics to match (prose rows such
as "Mechanical power balance"). Net: **11 of 29 rows (38%) are mechanisable, 18 are not.**
Left for the author, deliberately: whether the register expands to 136 rows or stays curated, and which printed
equation each of the 18 remaining rows points at. A wrong pointer is worse than an absent one, and the verdict
column is the author's.

**Open at the end of cycle 2:** the register decisions above; overfull-box warnings, which exist only in the
compile log and cannot be recovered from the PDF.
