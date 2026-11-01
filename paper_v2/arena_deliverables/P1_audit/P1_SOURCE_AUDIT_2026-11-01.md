# P1 source audit - 42 .tex files, 438 labels, 107 citation keys, 144 bib entries

Audited tree: `/home/user/le/paper_v2/manuscript_v2`

Sources: `paper_v2/from_overleaf/phase5/` (landed 2026-11-01 from the branch that held them; figures read from outside the repository). Nothing here edits a `.tex`.

| check | what | status | n |
|---|---|---|---|
| A1 | every cross-reference resolves to a label | **PASS** | 0 |
| A2 | no label is defined twice | **PASS** | 0 |
| A3 | every citation key exists in the bundled .bib files | **PASS** | 0 |
| A4 | every included figure exists on disk | **PASS** | 0 |
| A5 | every \input file exists | **PASS** | 0 |
| A6 | no placeholder text in the sources | **PASS** | 0 |
| A7 | the counts in the main.tex header match the sources | **PASS** | 0 |
| A8 | labels defined but never referenced (informational) | **INFO** | 294 |
| A9 | every .bib entry has author, title and year | **PASS** | 0 |
| A11 | every figure file in the tree is included somewhere | **FAIL** | 2 |
| A2b | the same source file does not appear twice in the tree | **PASS** | 0 |
| A10 | the same title appears in more than one bundled .bib file (informational: the R3* files are per-batch and overlap by design) | **INFO** | 22 |

## Findings

### A11 - every figure file in the tree is included somewhere (2)

```
fig07-theory-map.pdf; fig18-taxonomy.pdf
```


## What this audit does not cover

- signs, dimensions and derivation steps of the 166 numbered equations (needs the page-by-page pass)
- notation consistency across sections
- the 45 scripts in `phase5/scripts/` (D3: which of them assert anything)
