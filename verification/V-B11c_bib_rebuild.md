# V-B11c — `literature_base.bib` rebuilt; B10 blank-author base restated as 308

**Order:** `control/BRAVE_B11.md` condition 3 @ `origin/claude/control` `a0ace86`. **Access date:** 2026-10-22.
**Files touched:** `verification/literature_base.bib` (regenerated), `verification/LITERATURE_BASE.csv`
(unchanged in this item — the two rows were added in B9d).

---

## 1. Task

Re-base the B10d blank-author count to **308** (not 290), and regenerate `literature_base.bib` after
adding `LIT-0429` (Abouelregal et al. 2020) and `LIT-0430` (Green & Naghdi 1992).

## 2. Method

`python3 make_bibtex.py` in `verification/`, unchanged. The script reads `LITERATURE_BASE.csv`, builds
stable keys `FamilyYearWord`, reports duplicate DOIs/keys and DOI-less rows, and writes
`literature_base.bib`. No hand editing of the `.bib`; the known author-string garbling of
`make_bibtex.py` is left as it is (the standing rule is not to "fix" it there).

## 3. Result

```
read 430 records from LITERATURE_BASE.csv
duplicate DOIs: 0
keys generated: 430 (unique: 430)
records without DOI: 0
records without authors: 308   (run with --enrich to fill from Crossref)
wrote /home/user/le/verification/literature_base.bib
```

* `.bib` entries: **430** (was 428 before B9d).
* The two new records are present:
  `@article{…, doi = {10.1038/s41598-020-70388-1}, …}` and
  `@article{Green1992Undamped, author = {Green and Naghdi}, journal = {J. Thermal Stresses 15(2), 253-264}, doi = {10.1080/01495739208946136}}`.
* **B10d base: 308 blank-author rows**, not 290. The B10 brief's figure is superseded by this measured
  count; the difference (18) is not explained by the two rows added in B9d (both have authors), so the
  earlier 290 must have been read off a different snapshot.

### Two artefacts of the generator, recorded and NOT fixed here

1. `Green1992Undamped` writes `author = {Green and Naghdi}` with family names only (the CSV stores
   "Green; Naghdi", and the generator does not split into `Given Family`). It will render as
   "Green and Naghdi" — acceptable but not full initials. The proper form is `A. E. Green and P. M. Naghdi`
   (Crossref), and I am **not** editing the `.bib` by hand (standing rule); the CSV's `authors` field
   should be upgraded instead, which is a data change outside this item.
2. The `journal` field for LIT-0430 carries the volume/pages inside the journal name
   (`J. Thermal Stresses 15(2), 253-264`) because that is what I put in the `venue` column. Consistent
   with how other rows store `venue`, but it means the `.bib` has no `volume`/`pages` fields for it.

## 4. Evidence / sources

* `python3 make_bibtex.py` output (quoted verbatim above), run 2026-10-22 in `verification/`.
* Crossref records for both new DOIs (read in B9d): `10.1038/s41598-020-70388-1` (32 citations),
  `10.1080/01495739208946136` (1555 citations).
* `V-B9d_literature_base.md` for the row contents.

## 5. Checks done

1. Entry count in the `.bib` (430) equals the CSV row count (430) and the key count (unique 430).
2. Both new DOIs grep out of the `.bib` at the expected positions.
3. Duplicate DOI count 0 and DOI-less count 0 — so the new rows did not collide with an existing record
   under a different ID.
4. Blank-author count measured, not assumed: 308 (this is the re-based figure B10d must use).
5. Regeneration was a single run of the repository's own script — no manual `.bib` edits.

## 6. Confidence

* Counts (430 / 308 / 0 duplicates): **HIGH** (script output, reproducible).
* That the two new records are correctly keyed and carry their DOIs: **HIGH**.
* That 308 is the right B10d base: **HIGH** as a measurement; the *reason* the brief said 290 is
  **UNKNOWN** and I did not investigate it.

## 7. NOT verified / open issues

* **No `--enrich` run**: the 308 blank-author rows are still blank. `--enrich` needs Crossref from inside
  the script, and this sandbox reaches `api.crossref.org` only through my page-fetch tool, not from
  `python`. B10d remains the place to fill authors from the papers themselves.
* The `.bib` is not checked against `CITATION_MAP.csv` or against the manuscript's `\cite` keys — that is
  a different item (B5d) and was not re-run.
* `volume`/`pages` are missing for LIT-0430 in the `.bib` (they live inside `venue`); not fixed here.
* No claim is made that the `.bib` compiles: no LaTeX toolchain in this sandbox, and compilation is not
  part of the item.
