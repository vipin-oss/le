# Language pass 4 — applying the audit findings

Baseline: `review-paper-v2` at `d9967c2f` (the author's nine punctuation fixes and the
rewritten abstract are preserved unchanged; `main.tex`'s abstract was not touched).
Work branch: `arena/d518b957-le`.

## What was done

| Step | Result |
|---|---|
| Sync to `d9967c2f` | `main.tex` + 53 section files copied; token check `0/54` files differ; commit `e9a08b0` |
| Introduction rewritten | list-like short paragraphs, the three-item problem list and the four-item contribution list turned into flowing prose; "This review covers the following ground." and the separate aim sentence merged; enumerate/itemize removed (7 items → prose), no content, citation or number lost |
| Audit fixes applied | 162 of 209 rows changed the flagged sentence (see table below); the actionable subset was the 179-row list, the remaining 30 rows were added from the stored full report and were mostly HIGH, so they were fixed too |
| Cross-references | 76 `Section~\ref` / `Table~\ref` / `Appendix~\ref` normalised to `\cref` |
| Self-reference | 6 remaining "this paper" / "this work" / "the paper" (where it means this review) → "this review"; the ones that refer to a cited source were left alone |
| Changelog | 257 new sentence-level rows appended to `language_changelog.csv`; the 378 existing rows are preserved (635 rows total) |

## Audit rows fixed, by type

Counted against the full 209-row `language_audit_report.csv`.

| Type | Fixed / total |
|---|---|
| LONG/DENSE | 76 / 88 |
| PRONOUN | 32 / 43 |
| TONE | 21 / 25 |
| FLOW | 8 / 12 |
| REPETITION | 6 / 8 |
| GRAMMAR/SPELLING | 6 / 10 |
| TERMS | 2 / 7 |
| STYLE | 2 / 5 |
| PASSIVE/NOMINALIZATION | 9 / 11 |
| **All** | **162 / 209** |

By severity: 24 of 28 HIGH rows changed, 140 of 157 MED, 3 of 24 LOW (LOW was out of
scope; the three changed ones were fixed incidentally while editing the same sentence).
The HIGH rows not changed are the two abstract rows in `main.tex` (out of scope by
instruction), `s01_intro:14` (see below), and `s06_lags:15`, where the flagged sentence
was already well formed and the missing information was added as a following sentence.

## Rows deliberately not changed

*Out of scope by instruction*

- `main.tex:45` (REPETITION and TONE) — abstract, not to be touched.
- 21 LOW rows (PRONOUN/STYLE/FLOW/REPETITION on single words such as "That", "Three
  limits follow directly", TikZ coordinates).

*Already correct, or fixed with different wording*

- `s04_classical:45`, `s04_classical:65`, `s17_open:28`, `s17_open:94` (already in the
  target form; no edit needed), `s02_history:65`, `s03_foundations:91`, `s03d_admiss:2`,
  `s06_lags:15`, `s07_memory:3`, `s08_waves3d:14`, `s15e:14`, `s16_synthesis:66` —
  handled with hand-written splits that keep every citation, number and qualifier
  (the audit's own wording in these rows dropped a `\citep`, a number or a bold
  run-in head, so it was not used verbatim).
- `s02_history:5`, `s04_classical:37`, `s01b_scope:120`, `s14_methods:28` — STYLE rows
  whose suggested fix was a fragment or would have started a sentence with `\eqref`
  or duplicated an `\item`; the cross-reference normalisation covers what they asked.

## Uncertain — left unchanged

| Row | Why |
|---|---|
| `s01_intro:14` TERMS (HIGH) | The row points into the `fig:refyears` caption; the suggested fix would have replaced the figure block. The caption text ("cited in this review") is already correct. |
| `s10b_lamb:17` PRONOUN | "This computation does not isolate that cause"; the proposed replacement names specific mechanisms (thermal vs geometric) that the section does not state, so the naming would be an inference. |
| `s15e_identify:2` TERMS | The suggested fix truncates the sentence at the point where equation `eq:Ginvert` is displayed; applying it would delete the equation. |
| `s18_declarations:22` TERMS | The fix drops the qualifier "and which were not", which weakens the statement about unchecked attributions. |
| `s14b_schemes:3` TONE | The proposed change is "hides" → "conceals", a synonym swap with no gain. |
| `s15c_experiments:6` (LOW, two rows) | LOW, and one of them would drop the five numeric temperature values from the sentence. |
| `s10_surface:12`, `s14_methods:12`, `s11b_layered:17,19` (MED) | The suggested wording changes the citation itself (a key replaced by another, a page locator `p.~120` rewritten as `pp.~124--126`, a review citation dropped). Citations are not edited in this pass. |
| `s14_methods:20` (HIGH, FLOW) | Fixed, but not with the suggested wording: the suggested text repeated the "first issue" sentence that the paragraph already contains. |
| `s12_size:58` (MED, Hosseini) | Fixed by hand: the suggested wording kept the passive frame ("was presented in \citep{...}") and the author name from the bibliography was used instead. |

## Verification

- Token-multiset check against `d9967c2f` (`paper_v2/tools/verify_tokens.py`): all math,
  citation keys, numbers and `\ref` targets preserved. Five files show intentional
  additions: the exact delay law `q(t+\tau_q)=-k\,\theta_{,x}(t)` (`s06b_delay`), the
  new `\cref` targets in `s08b_aniso` and `s12b_wider`, the branch-count sentence in
  `s08_waves3d`, and `G(s)` in `s13_multiphysics`.
- Brace balance and `\begin`/`\end` pairing: balanced in all 54 files; the `\item` count
  falls only in `s01_intro.tex`, where the list was converted to prose.
- All 425 cited keys resolve against the bibliography files; no `\label`/`\ref` target
  is undefined (checked by scanning labels against `\ref`/`\cref`/`\eqref`).
- No comma splices introduced (audited by scanning for `, The`, `, It`, `, This`).
- No LaTeX engine is available in this environment, so there is no compile check; the
  structural checks above stand in for it.
