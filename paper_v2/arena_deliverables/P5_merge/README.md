# P5 — merge package for the final review paper

Everything here is additive. Nothing in the final paper, in `overleaf_package.zip`, or in
`manuscript_v2/` was modified; this directory is the only output of the merge.

| Step | Artefact | State |
|---|---|---|
| 1 | `section_map.csv` (45 rows), `build_section_map.py` | done |
| 2 | `from_v2_missing_in_final.csv` (11 rows), `snippets/` (11 files), `check_snippets.py` | done |
| 3 | `conflicts.csv` | next |
| 4 | front/back matter — delivered inside Step 2 as `snippets/FM01`, `M03`, `M06`, `M01`+`FM04` | done |
| 5 | `v2_verified_ledger.csv` | later |
| 6 | `REPORT.md` | last |

## How to check this package

```
cd paper_v2/arena_deliverables/P5_merge
python3 check_snippets.py      # prints PASS, exit 0
python3 build_register_coverage.py   # regenerates equation_coverage.csv + FM04, prints PASS
```

`check_snippets.py` verifies, for every snippet: brace balance and no leftover markers; every
`\cref`/`\eqref` target resolves to a label of the final paper (`final_labels.csv`, harvested from the
final sources: 216 labels) or to a label the snippet declares as new; every citation key exists in the
final bibliography (`final_bib_keys.txt`, 362 keys); no duplicate `\label`; no declared-new label that
already exists in the final paper; and a header naming the source and the intended placement.

## The snippets, in paste order

| Id | File | What it adds | New labels | Pages |
|---|---|---|---|---|
| 1 | `snippets/M05_exact_energy_flux.tex` | exact Eulerian total-energy flux, and the first-order reduction | `eq:exactflux`, `eq:exactflux-balance` | 0.6 |
| 2 | `snippets/M02_evidence_protocol.tex` | the six-rule evidence protocol | `sec:evidence_protocol` | 0.8 |
| 3 | `snippets/M06_contributions_table.tex` | contributions C1–C7 with delivery point and evidence | `tab:contributions` | 0.8 |
| 4 | `snippets/M01_equation_register.tex` | per-equation verification register | `sec:eqregister`, `tab:eqregister` | 1.2 |
| 5 | `snippets/M07_taxonomy.tex` | five-axis taxonomy + axis-weight dissimilarity | `sec:taxonomy`, `tab:taxonomy-axes`, `eq:taxdissim` | 1.0 |
| 6 | `snippets/M04_research_questions.tex` | R1–R10 with acceptance tests | `tab:research-questions`, `sec:research_questions` | 1.0 |
| 7 | `snippets/M08_balance_derivations.tex` | derivations of the balance laws used | `app:balance` + 4 equations | 1.4 |
| 8 | `snippets/M09_provenance_notes.tex` | page-level provenance of the attributions | `sec:provenance`, `tab:provenance` | 0.9 |
| 9 | `snippets/M03_declarations.tex` | declarations (CRediT, funding, competing, data, tools) | `sec:declarations` | 0.7 |
| 10 | `snippets/FM01_abstract_keywords.tex` | abstract (259 words) + 14 keywords — **replacement candidate only** | — | 0.4 |
| 11 | `snippets/FM04_equation_register_coverage.tex` | coverage inventory of the register (generated) | `sec:eqcoverage`, `tab:eqcoverage` | 2.5 |

Paste order is the priority order. Every file is a self-contained LaTeX fragment written in the final
paper's own conventions: `article` 12pt, natbib numbers, `\cref`/`\eqref`, `\bm`, `\bu`/`\bq`/`\bx`/`\bn`,
`\tr`, `\dd`, `\ii`, `\Real`, `tabularx` + `booktabs`, `longtable` for FM04.

## What is **not** missing — do not paste it

Nine v2 pieces were probed against the final sources and found already present in equivalent form; they
are deliberately absent from this package: the nomenclature table, the graphical abstract, the
dispersion-polynomial derivation (their `appA`), the characteristic-numbers appendix, the benchmark
registry, the reproducibility appendix, the literature catalogue, the glossary and the parameter register.
The abstract is present too — `FM01` is a replacement, not an addition.

## Two things that will bite on paste

1. **`\mathcal E` is taken.** In the final paper `\mathcal E` is the availability (quadratic) energy and
   `P_i` its flux. The exact total-energy flux therefore needs `\mathcal E_{\mathrm{tot}}`; M05 and M08 use
   that symbol, and M01/M05 both say why the two objects must not be merged into one.
2. **`\xi` is taken.** In the final paper `\xi` is the nonlocal length; the taxonomy snippet uses only
   axis labels and weights, no `\xi`. Nothing in the package introduces a new symbol that collides with a
   symbol of the final paper except `\mathcal E_{\mathrm{tot}}`, which is stated in the text.

## Conventions held throughout

No PDFs, no links, no identifiers of any kind beyond printed bibliographic data. Nothing is asserted that
was not verified in v1.2; every unverified item is labelled `UNVERIFIED` in the paper's own register
vocabulary rather than quietly upgraded. Where the final paper's reading of a source differs from v2's, the
difference is recorded in `conflicts.csv` (Step 3) instead of being edited into a snippet.
