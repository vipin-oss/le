# P5 merge report — what the final paper is missing, and what I would do about it

Date: 2026-11-02. Branch: `arena/9b458c54-le`. Package: `paper_v2/arena_deliverables/P5_merge/`.

Nothing in the final paper, in `overleaf_package.zip`, or in `manuscript_v2/` was modified. This
directory is the whole output. Every artefact here is re-derivable from files in this repository, and
every checker prints `PASS` and exits 0.

---

## 1. The answer in one paragraph

The final paper is **not a superset** of the verified v1.2 manuscript, and it is not a subset either. It
is an independent descendant: richer in worked examples, figures, benchmarks and applied cases (145
pages, 56 labelled equations, 44 section files, 8 appendices), and *thinner in audit apparatus* — the
part of v1.2 that took the most work to earn. Measured section by section, 15 of 45 rows overlap heavily,
14 partly, and 16 have no counterpart on either side. Probed for the six things that make v1.2 auditable,
the final paper returns **zero hits** for all six. So the merge is not "port the missing pages"; it is
**eleven pages of missing apparatus plus twelve disagreements to settle**, of which two decide whether the
merged paper is internally consistent and one decides whether a citation is defensible.

Total new material if everything is pasted: **10.8 pages** (10.4 if the optional abstract replacement is
excluded), against a 145-page paper.

---

## 2. What the measurement says

| measurement | result |
|---|---|
| section map | 45 rows: **high 15 / partial 14 / none 16** |
| final paper | 56 labelled equations, 258 labels, 362 bibliography keys, 11 keywords, nomenclature present |
| v2 cited keys not in the final bibliography | **0** (all 144 already present) → no new references needed to paste any snippet |
| probe: verification register | 0 hits |
| probe: evidence protocol | 0 hits |
| probe: contributions table | 0 hits |
| probe: research-question / acceptance-test table | 0 hits |
| probe: five-axis taxonomy | 0 hits |
| probe: derivations of the balance laws as an appendix | 0 hits (the balances are asserted in one sentence; `appA` derives the dispersion polynomial instead) |
| v2 equation register | 61 audited rows over 136 printed equations: 11 equations carry a status, **125 do not** |

The 16 final-paper sections with no v2 counterpart are, in effect, the author's own new work:
`kinetic theory`, `exact delay`, `modulus/Debye`, `transients`, `thermal modes`, `Lamb`, `bar`,
`flexural TED`, `layered media`, `BGK`, `worked examples`, `atlas`, `reporting standards`,
`app:disp`, `app:catalogue`, `app:debye`. Nothing in this package proposes to touch them.

---

## 3. If only ten things could merge

Ranked by (value to the paper) ÷ (risk of breaking it). Page estimates are for the pasted text.

| # | What | File | New labels | Pages | Why this rank | If omitted |
|---|---|---|---|---|---|---|
| 1 | **Exact Eulerian total-energy flux and its first-order reduction** | `M05` | `eq:exactflux`, `eq:exactflux-balance` | 0.6 | The paper already says its availability flux "differs from the total-energy flux" but never shows how. This is the cheapest fix with the largest conceptual payoff, and it is pure algebra. | A reader cannot see what the difference is; the sentence stays an assertion (conflict C01). |
| 2 | **Evidence protocol (six rules + limits)** | `M02` | `sec:evidence_protocol` | 0.8 | It tells the reader how to discount everything else. A 145-page review whose claims cannot be discounted is read as a list of assertions. | The paper's own register would have no stated rule to appeal to. |
| 3 | **Contributions table C1–C7** | `M06` | `tab:contributions` | 0.8 | Converts a 145-page structure into seven citable claims, each pointing at where it is delivered. | Reviewers ask "what is new?" and the answer stays implicit. |
| 4 | **Per-equation verification register** | `M01` | `sec:eqregister`, `tab:eqregister` | 1.2 | Ten equations of this paper acquire a status from a finite vocabulary. This is the single most unusual feature of v1.2 and the least likely to be reconstructed by anyone else. | No equation distinguishes derived from quoted. |
| 5 | **Five-axis taxonomy + axis-weight dissimilarity** | `M07` | `sec:taxonomy`, `tab:taxonomy-axes`, `eq:taxdissim` | 1.0 | It is the paper's one genuinely novel organising device: the template is a coordinate on Axis 2, not a rival scheme (see C06). | Hybrid models have no place to sit; comparability is left to the label. |
| 6 | **Researchable questions R1–R10 with acceptance tests** | `M04` | `tab:research-questions`, `sec:research_questions` | 1.0 | Turns the prose agenda in `sec:open` into ten rows a reader could actually start from. | The agenda stays a wish list. |
| 7 | **Derivations of the balance laws** | `M08` | `app:balance` + 4 equations | 1.4 | Supplies the algebra behind #1 and behind the symmetry of the stress, which the paper currently asserts in one sentence. | The flux discussion of #1 has no visible foundation. |
| 8 | **Page-level provenance table** | `M09` | `sec:provenance`, `tab:provenance` | 0.9 | Says which attributions were checked at the printed page, and what the check does not cover. | Checked and unchecked attributions look identical. |
| 9 | **Declarations** | `M03` | `sec:declarations` | 0.7 | Not scholarship — compliance. Most journals will not accept the submission without it. | Submission blocked at the portal, not at review. |
| 10 | **Coverage inventory: all 136 printed equations** | `FM04` | `sec:eqcoverage`, `tab:eqcoverage` | 2.0 | Without it the register of #4 looks complete when 125 of 136 equations are unregistered. Honesty as a table. | The register over-claims by omission. |

Optional eleventh, **not** in the ten because it replaces rather than adds: `FM01`, a 259-word abstract and
14 keywords re-scoped for the merged paper. The final paper already has an abstract (~250 words) and 11
keywords; paste it only if the merged scope is adopted, because it names the exact flux, the taxonomy and
the register.

**Deliberately not in the list**, because they are already there: nomenclature table, graphical abstract,
dispersion-polynomial derivation (`appA`), characteristic numbers, benchmark registry (14 rows),
reproducibility appendix, classified catalogue, glossary, parameter register. Nine v2 pieces, nine
existing final-paper pieces — pasting any of them would duplicate, and duplicating a table in a review is
worse than not having it.

---

## 4. The three conflicts that must be settled before any paste

Full detail, with both wordings and locations, in `conflicts.csv` (12 rows: 3 high, 3 medium, 6 low).

* **C01 — what "energy flux" means.** The final paper calls `q_i − σ_ij u̇_j` "the flux of the *total*
  internal energy". The exact flux of total energy carries a third term, `E_tot u̇_j`. The two-term object
  is the first-order reduction, which is exactly what the paper needs for interface partition — so the
  physics is fine and the wording is what must change. Recommended: paste `M05`, keep `P_i` where it is.
* **C04 — Mindlin–Tiersten (1962) in the piezo bar.** The key sits on the sentence introducing the
  quasi-electrostatic bar. That 1962 paper is couple-stress elasticity — the paper's own catalogue says so
  — and cannot support a piezothermoelastic formulation. Recommended: drop it from that sentence, keep
  `Mindlin1974Thermopiezo` and `Yang2018`. This is the one row where a citation should be removed.
* **C10 — `\mathcal E` is taken.** In the final paper `\mathcal E` is the positive-definite availability
  energy and `P_i` its flux. Any v2 text that reuses `\mathcal E` for the total energy would silently
  change the meaning of a printed equation. All snippets print the total energy as
  `\mathcal E_{\mathrm{tot}}` and say in words that the two are different objects.

The four established readings are honoured rather than argued with: Green–Lindsay stays **outside** the
flux template (C02 — and this is why `FM01` was rewritten), the DPL condition `τ_T ≥ τ_q/2` is presented
as the **Quintanilla (2003) spectral result for the second-order truncation** (C03), Zener (1937) is cited
as the **reed** paper (C07), and **no numeric constant is borrowed from the NaF second-sound paper**
(C08, a guard row). C05 corrects an attribution in my own register: the relaxation law is Cattaneo (1948)
and Vernotte (1958); Lord–Shulman (1967) is its application.

---

## 5. Honest limits of this report

1. **The snippets have not been compiled.** They are validated structurally (brace balance, every `\cref`
   and `\eqref` resolving against the paper's 216 labels or a declared new label, every citation key
   present in the 362-key bibliography, no duplicate or clashing label), but this environment has no TeX
   engine that can build the paper's preamble. Expect a round of cosmetic fixes on first paste, in
   particular table widths.
2. **The register covers 11 of 136 printed equations.** That is the source register's coverage, not a
   defect introduced here — and `FM04` exists so the paper says so out loud.
3. **224 claims in the source register: 74 SUPPORTED, 34 PARTLY SUPPORTED, 5 NOT SUPPORTED, 111 SOURCE
   NOT AVAILABLE.** 150 rows are flagged in `v2_verified_ledger.csv` as "do not state as-is" or "restate
   with the qualification found". The merge carries *text*, not claim provenance; nothing here launders
   those verdicts into a stronger statement.
4. **The paper is not submission-ready for reasons this merge cannot fix**: expert reviews (P6) and the
   journal package (P7) in `PUBLICATION_READINESS_2026-11-01.md` are both at "not started", and the
   Elsevier variant has never compiled. The eleven pages here improve the paper; they do not clear those
   two gates.
5. **Ten equations of the final paper got a register row; forty-six did not.** Where a status could not be
   earned for the *same statement* in v2, the row was left out rather than guessed — that is why the table
   has ten rows and not fifty-six.

---

## 6. How to apply, in order

1. Paste `M05` after `eq:P` in `sections/s03_foundations.tex`; add the `\mathcal E_{\mathrm{tot}}`
   sentence. *(Fixes C01 and C10.)*
2. Paste `M08` as the new appendix before `app:disp`; add `\input` and the TOC line. *(Supports M05.)*
3. Paste `M02` at the end of `sections/s01_intro.tex`.
4. Paste `M06` in `sections/s01_intro.tex` before the outline.
5. Paste `M01` as a new appendix after `appH_registry`, then `FM04` after it. *(Long table; both can live
   in the appendix.)*
6. Paste `M07` as a new section between `s16_synthesis` and `s17_open`.
7. Paste `M04` at the end of `s17_open`.
8. Paste `M09` at the end of `s05_hyperbolic` (or beside `M01` in the audit appendix).
9. Paste `M03` before the bibliography.
10. Optionally replace the abstract with `FM01`, keeping the graphical abstract.
11. Apply C04 to `s13_multiphysics.tex` — one key removed, nothing else touched.
12. Compile, then re-run the checkers in this package against the *final* label set if any label was
    renamed during the paste.

---

## 7. Files in this package

| file | what it is |
|---|---|
| `section_map.csv` | 45 rows mapping every final-paper section to v2 (or to "no equivalent"), with measured citation overlap |
| `from_v2_missing_in_final.csv` | the 11 items, prioritised, each with the evidence that it is absent and where to put it |
| `conflicts.csv` | 12 disagreements: both wordings, locations, which one the source supports, recommendation, what was done here |
| `v2_verified_ledger.csv` | 366 rows: 136 equations + 224 claims + 7 audit facts, each with a merge disposition |
| `equation_coverage.csv` | the 136 printed equations with register status and id |
| `snippets/*.tex` | 11 paste-ready fragments in the paper's own macros and naming |
| `final_labels.csv`, `final_bib_keys.txt` | the paper's 216 labels and 362 keys, harvested so the checkers can run without the paper |
| `build_section_map.py`, `build_register_coverage.py`, `build_verified_ledger.py` | regenerate the three generated artefacts |
| `check_snippets.py`, `check_csvs.py` | the two gates; both print `PASS`, exit 0 |
| `README.md` | the short version, with the paste order and the two symbol traps |

Checks, from this directory:

```
python3 check_snippets.py    # 11 snippets, 21 new labels, 216 final labels, 362 bib keys -> PASS
python3 check_csvs.py        # 5 CSVs, 570 rows, every location resolves -> PASS
python3 build_register_coverage.py   # 136 printed equations, 11 registered -> PASS
python3 build_verified_ledger.py     # 366 ledger rows -> PASS
```
