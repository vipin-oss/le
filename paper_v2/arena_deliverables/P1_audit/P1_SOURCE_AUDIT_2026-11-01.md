# P1 source audit - 49 .tex files, 438 labels, 108 citation keys, 144 bib entries

Sources: `paper_v2/from_overleaf/phase5/` (landed 2026-11-01 from the branch that held them; figures read from outside the repository). Nothing here edits a `.tex`.

| check | what | status | n |
|---|---|---|---|
| A1 | every cross-reference resolves to a label | **PASS** | 0 |
| A2 | no label is defined twice | **PASS** | 0 |
| A3 | every citation key exists in the bundled .bib files | **FAIL** | 1 |
| A4 | every included figure exists on disk | **PASS** | 0 |
| A5 | every \input file exists | **PASS** | 0 |
| A6 | no placeholder text in the sources | **PASS** | 0 |
| A7 | the counts in the main.tex header match the sources | **PASS** | 0 |
| A8 | labels defined but never referenced (informational) | **INFO** | 294 |
| A9 | every .bib entry has author, title and year | **PASS** | 0 |
| A11 | every figure file in the tree is included somewhere | **FAIL** | 2 |
| A2b | the same source file does not appear twice in the tree | **FAIL** | 8 |
| A10 | the same title appears in more than one bundled .bib file (informational: the R3* files are per-batch and overlap by design) | **INFO** | 22 |

## Findings

### A3 - every citation key exists in the bundled .bib files (1)

```
Eringen1968b (tables/source/T3_coupled_multiphysics.tex)
```

### A11 - every figure file in the tree is included somewhere (2)

```
fig07-theory-map.pdf; fig18-taxonomy.pdf
```

### A2b - the same source file does not appear twice in the tree (8)

```
tab:T1-historical in master/tables/source/T1_historical_development.tex and tables/source/T1_historical_development.tex; tab:T2-generalized in master/tables/source/T2_generalized_thermoelastic.tex and tables/source/T2_generalized_thermoelastic.tex; tab:T3-multiphysics in master/tables/source/T3_coupled_multiphysics.tex and tables/source/T3_coupled_multiphysics.tex; tab:T4-waves in master/tables/source/T4_wave_types.tex and tables/source/T4_wave_types.tex; tab:T5-techniques in master/tables/source/T5_solution_techniques.tex and tables/source/T5_solution_techniques.tex; tab:T6-interfaces in master/tables/source/T6_interface_configurations.tex and tables/source/T6_interface_configurations.tex; tab:energy_transport in master/tables/source/T7_energy_transport.tex and tables/source/T7_energy_transport.tex; tab:T8-applications in master/tables/source/T8_applications_validation.tex and tables/source/T8_applications_validation.tex
```


## What this audit does not cover

- signs, dimensions and derivation steps of the 166 numbered equations (needs the page-by-page pass)
- notation consistency across sections
- the 45 scripts in `phase5/scripts/` (D3: which of them assert anything)
