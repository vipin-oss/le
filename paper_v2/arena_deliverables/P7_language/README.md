# P7 — language pass: journal-style rewrite of the review

Every section of the review was rewritten into the prose a referee expects from *Applied Mechanics
Reviews* / *Journal of Thermal Stresses* / *Physics Reports*, one file at a time. The technical content
was held fixed. This folder holds the rewritten sections, the gate that proves the content is fixed,
the style report, and a script that assembles a drop-in replacement package.

**The originals in `paper_v2/overleaf_package.zip` were not touched.** They remain the authority the
gate reads from.

## Contents

| file | what it is |
|---|---|
| `s01_intro.tex` … `s18_declarations.tex`, `appA.tex` … `appH_registry.tex` | the 50 rewritten sections, same filenames as in `sections/` of the package |
| `abstract.tex` | Highlights box, graphical abstract, abstract and keywords, lifted out of `main.tex` and rewritten |
| `abstract_original.tex` | the same block exactly as it stood in `main.tex`, kept as the gate's reference |
| `check_invariants.py` | the gate: compares each rewrite to its original and prints `PASS` or `FAIL` |
| `FAILED_INVARIANTS.csv` | verdict and reason for every file, regenerated on each gate run |
| `STYLE_REPORT.md` | counts, the banned-pattern audit, and one before/after example per file |
| `gen_style_report.py` | regenerates `STYLE_REPORT.md` from the files on disk |
| `assemble_package.py` | builds `paper_v2/rewritten_package.zip`, the package with the new prose |

## The contract

`check_invariants.py` passes a file only when all six of these are **identical** to the original:

1. the content of every `equation`, `align`, `gather`, `multline`, `eqnarray`, `flalign`, `alignat`,
   `displaymath`, `\[…\]` and `$$…$$` environment;
2. the multiset of `\label`, `\eqref`, `\cref`, `\Cref`, `\ref` (and `\autoref`, `\pageref`, `\nameref`);
3. the multiset of `\cite*` keys;
4. the multiset of numbers (decimal and scientific);
5. the sequence of `\begin{…}` / `\end{…}` environments;
6. the multiset of `\path{…}` and `\texttt{…}` arguments.

Comments are stripped before counting, so a comment cannot smuggle a number past the gate. A file that
fails keeps its original text in the final paper and is recorded with its reason in
`FAILED_INVARIANTS.csv`; nothing that fails is shipped as a rewrite.

## Running it

```sh
cd paper_v2/arena_deliverables/P7_language
python3 check_invariants.py                 # all 51 files
python3 check_invariants.py --file s14_methods.tex --verbose
python3 gen_style_report.py                 # rebuild STYLE_REPORT.md
python3 assemble_package.py --check         # report what assembly would change, write nothing
python3 assemble_package.py                 # write paper_v2/rewritten_package.zip
```

## Result of the last gate run

```
checked 51 rewritten file(s): 51 PASS, 0 FAIL
PASS
```

`FAILED_INVARIANTS.csv` therefore contains 51 `PASS` rows and no failure. 241 paragraphs were edited;
paragraphs that were already in journal style were left as they stood.

Banned-pattern audit over the whole corpus (before → after): `This section` 10 → 0, `not only` 2 → 0,
`landscape` 1 → 0, `It is worth noting` 0 → 0, `Moreover`/`Furthermore`/`Additionally` 0 → 0, plus the
rest of the list in `STYLE_REPORT.md`. One `pivotal` survives on purpose: it sits in the "Reported
result" column of the atlas table, where the entry paraphrases the source's own claim, and rewriting it
would misreport the source.

## What the pass did and did not do

- Rewritten: sentence openings that announced the section ("This section …"), connective padding,
  nominalisations, stacked three-item lists in running text, closing sentences that only summarise the
  paragraph again, and hedging where the claim is in fact established.
- Kept: every equation, symbol, number, unit, citation, cross-reference, table, figure, footnote and
  script path; the `summarybox` arguments; and every hedge that the claim register marks PARTLY
  SUPPORTED or SOURCE NOT AVAILABLE.
- Not done: no LaTeX was compiled. There is no TeX engine in this sandbox and no way to obtain one
  (see `../TEX_ENGINE_STATUS_2026-11-01.md`). `assemble_package.py` performs only structural checks —
  every `\input` resolves, every environment sequence is unchanged, every section file is byte-identical
  to its twin here — so a build on Overleaf is the remaining step.
- Not fixed, deliberately: the two defects the post-merge audit found in the text itself — the `\cref`
  in Table 2 C4/P6 that prints "(A)" instead of equation (1), and Tables 21–23 floating after the
  reference list. Both are recorded in `../P6_post_merge/STATUS.md`. Repairing them changes what the
  paper says, which is outside a language pass.

## Assembling the rewritten paper

`assemble_package.py` writes `paper_v2/rewritten_package.zip`: all 168 entries of
`overleaf_package.zip` in their original order, with the 50 `sections/*.tex` replaced by the files here
and the Highlights/abstract block of `main.tex` replaced by `abstract.tex`. Nothing else changes — the
bibliography, tables, figures and scripts are byte-identical — so the zip can be uploaded to Overleaf in
place of the original package.
