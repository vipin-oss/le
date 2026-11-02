# P11 — the eleven added PDFs (evidence only)

Goal: read the eleven papers that were added to the library and turn every "SOURCE NOT AVAILABLE"
in P9/P10 into an actual verdict, with equation numbers and printed page numbers. **Nothing in
this folder changes the manuscript.** No `.tex` file and no pipeline script was touched; no PDF is
stored in the repository; no folder identifier, sharing link or download link appears anywhere in
these files.

Result in one line: **11 of 11 found**, all text-extractable, all the right papers;
`refs_P8.csv` moved **10 rows to R3 and 1 to R2**; S1 **PARTLY SUPPORTED**, S2 **SUPPORTED**,
S3 **PARTLY SUPPORTED**.

## Files

- `report.md` — identity table for the eleven PDFs, what was read in each (equations with pages),
  the three sentence verdicts, and the six points where the review wording has to be careful.
- `evidence_P11.csv` — 42 rows: `key, sentence, claim_checked, quote, eq, page, equation_read,
  note`. Every `quote` is a verbatim substring of the cited page (≤ 15 words); rows marked
  `(normalized)` in `equation_read` are readings of equations whose glyphs are damaged in the text
  layer, not character-exact quotations. Rows with `NOT QUOTABLE - absence` record a counted
  absence (the count is in `note`), never an assumed one.
- `missing_P11.csv` — the outstanding list; it has no real rows, because nothing is outstanding.
- `check_p11.py` — the gate for this batch.

## What the gate checks

1. The four files exist.
2. Evidence covers exactly the eleven keys, ≥ 3 rows each, sentence tags in S1/S2/S3, quotes within
   15 words, an equation reference and a printed page (or the page-less `abstract` tag) on every
   quotable row, and a counted-absence note on every absence row.
3. `refs_P8.csv` still matches `refs_P8.bib` key-for-key, and the eleven rows really are at R2/R3
   with `pdf_status = READ` and a P11 note carrying a page number.
4. `missing_P11.csv` contradicts nothing and lists nothing.
5. The report states a verdict for S1, S2 and S3 from the allowed set.
6. No PDFs, no Drive identifiers or links, no URLs and no absolute sandbox paths in this folder.

## Reproduce

```
python3 paper_v2/arena_deliverables/P11_verification/check_p11.py
python3 paper_v2/arena_deliverables/P8_coverage/check_p8.py
python3 paper_v2/arena_deliverables/P9_verification/check_p9.py
python3 paper_v2/arena_deliverables/P10_verification/check_p10.py
python3 paper_v2/arena_deliverables/check_readme_paths.py --root .
```

Each prints `PASS` and exits 0.

## Known state (deliberate, not an oversight)

`refs_P8.csv` was updated directly, because this phase is evidence-only. The P8 builder
(`P8_coverage/build_p8.py`, its `PDF_STATUS` map) and the P8 data module
(`P8_coverage/refs_data.py`, the `ver`/`note` fields) still say `NOT FOUND` / `R0` for these
eleven keys. Anyone who re-runs the builder must update those two first, otherwise the builder
will rewrite the eleven rows back to their P9 values. `report.md` §6 repeats this warning.
