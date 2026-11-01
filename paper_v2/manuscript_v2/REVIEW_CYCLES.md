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
