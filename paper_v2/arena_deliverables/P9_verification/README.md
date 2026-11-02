# P9 — verification of the three "wider material classes" sentences

Evidence only. No `.tex` file and no pipeline script was touched; `refs_P8.csv` gained a
`pdf_status` column and one upgraded verification level.

## Result in one table

| Sentence | Verdict |
|---|---|
| **S1** strain-gradient / couple-stress change the operator, heat kernel `G(s)` unchanged | **PARTLY SUPPORTED** — operator change verified at R3 (Mindlin 1965, eqs. (1), (17), (19), (20a), pp. 418–422); "`G` unchanged" is an absence argument (that paper has no thermal field); the couple-stress clause has **no primary source** in the library |
| **S2** locally resonant arrays → frequency-dependent effective mass / modulus | **SUPPORTED** — Oh et al. 2016, eqs. (1), (4a), (10), pp. 3–5 (R3); but the four P8 sources named for it (Liu 2000, Sigalas 1992, Kushwaha 1993, Hussein 2014) are **not available** |
| **S3** heat-flux kernel still insertable in piezo-semiconductor models | **SUPPORTED** — Hobiny/Abbas/Marin 2022, eqs. (2), (3), (8), p. 3 (R3, semiconductor without piezoelectric term); Gupta et al. 2026, eq. (1.1), p. 3 (R2, full piezo-semiconductor) |

## Two things to read before using this

1. **No section called "Wider material classes" exists in the repository** (`grep -r "material
   classes"` and `grep -r "Wider"` return nothing across all text files). The three sentences
   were therefore checked **as given in the task**, not against repository text.
2. **Eleven of the twelve priority PDFs are not in the library** — only Mindlin 1965 was found.
   They are listed with DOIs in `missing_pdfs_P9.csv`; nothing about them was inferred.

## Files

- `verdicts_P9.md` — the full verdict with the equations, equation numbers and pages, the
  caveats, and what the text should do about each sentence.
- `evidence_P9.csv` — five sources read in P9: level, pages read, equations checked with pages,
  which sentence each bears on, and its limitation.
- `missing_pdfs_P9.csv` — eleven priority PDFs absent from the library, with DOIs.
- `check_p9.py` — gate; prints `PASS` and exits 0. It also cross-checks `../P8_coverage/refs_P8.csv`.

## Change to the P8 batch

`../P8_coverage/refs_P8.csv` now has a `pdf_status` column
(`READ` 1 / `NOT FOUND` 11 / `NOT CHECKED` 60) and `Mindlin1965` is **R3**; the other 71 stay
**R0**. `refs_P8.bib` is unchanged apart from the regenerated header. Reproduce with:

```
python3 paper_v2/arena_deliverables/P8_coverage/build_p8.py
python3 paper_v2/arena_deliverables/P8_coverage/check_p8.py
python3 paper_v2/arena_deliverables/P9_verification/check_p9.py
```

The data file `refs_data.py` now lives inside `P8_coverage/`, so the build no longer depends on a
path outside the repository.
