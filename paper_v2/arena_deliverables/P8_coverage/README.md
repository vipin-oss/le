# P8 — coverage extension (evidence only)

Goal: widen the field coverage of the review so that research groups working outside the
GLS/LS/MGT tradition are represented. **Nothing in this folder changes the manuscript.** No
`.tex` file and no pipeline script was touched; this is a bibliography plus a plan.

| Area | Topic | Refs |
|---|---|---|
| a | strain-gradient / couple-stress / dipolar / gradient thermoelasticity | 18 |
| b | phononic crystals, elastic and thermal metamaterials, TED in them | 18 |
| c | piezoelectric and piezo-semiconductor waves, carriers, flexoelectricity, quasicrystals | 18 |
| d | graded, porous, magneto-electro-elastic, laminated, nanostructured, biological media | 18 |
| | **total** | **72** |

Verification: **60 × R0, 1 × R2, 11 × R3** (detail below). The R0 entries are
title/venue/volume/pages/DOI matched against a Crossref record on 2026-11-02: no abstract and no
full text were read for them, and no equation number is claimed. The 11 R3 entries are the
papers whose library PDFs were read in P11 (`../P11_verification/report.md`), and the single R2
entry is Green–Rivlin 1964, whose text was read but whose tensor equations survive the text layer
only in fragments. Nothing is quoted, no page range or DOI was written from memory, and no
missing paper was filled in from guesswork — see `coverage_gaps.md`.

## Files

- `refs_P8.bib` — the 72 entries, grouped by area, keys unique and disjoint from the paper's
  existing 362 keys.
- `refs_P8.csv` — one row per reference: area, authors, year, title, venue, volume, pages, DOI,
  verification level, **target section**, **inside/outside the template**, and a one-sentence
  "what it actually shows".
- `outlines_P8.md` — one page per area: which equations to state, how the addition attaches to
  the kernel `G(s)` and the effective modulus `m(s)`, inside/outside marking, one honest
  limitation each.
- `coverage_gaps.md` — measured mention counts in the current text, what is still missing, and
  the citation trap to avoid.
- `pdfs_needed_P8.csv` — 35 PDFs that must be obtained before any `R0` claim becomes `R2`/`R3`
  (title, venue, DOI, why it is needed).
- `refs_data.py` — the single data file (moved inside this folder in P9 so the build no longer
  depends on a path outside the repository).
- `existing_keys.txt` — the paper's 362 existing bib keys, used for the clash check.
- `build_p8.py` — regenerates the `.bib` and `.csv` from `refs_data.py`; asserts key uniqueness
  and zero clash with the existing bibliography, and prints the pdf_status split.
- `check_p8.py` — gate: parses both files, checks counts per area, fields, section ids,
  inside/outside flags, DOI agreement between bib and csv, no PDFs, no Drive ids or links.

## Reproduce

```
python3 paper_v2/arena_deliverables/P8_coverage/build_p8.py
python3 paper_v2/arena_deliverables/P8_coverage/check_p8.py
```

`check_p8.py` prints `PASS` and exits 0.

## Counts by verification level

| Level | Meaning | Count |
|---|---|---|
| R0 | title/venue/pages/DOI matched in Crossref only | 60 |
| R1 | abstract read | 0 |
| R2 | full text read | 1 (GreenRivlin1964: eqs. (8.3) p. 124, (10.1)-(10.10) p. 129, (15.9)-(15.10) p. 138) |
| R3 | equations checked | 11 (Mindlin1965 from P9; Toupin1962, Toupin1964, Mindlin1964, Hutson1962, White1962, Liu2000, Hussein2014, Sigalas1992, Kushwaha1993, Zubko2013 from P11) |

A second column, `pdf_status`, records which entries were opened: `READ` 12, `NOT FOUND` 0,
`NOT CHECKED` 60. The eleven papers that were still missing in P9 and P10 arrived and were read in
P11; the equations and printed pages for each are in the `notes` column and in
`../P11_verification/evidence_P11.csv`.

The next step is not more references but reading: `pdfs_needed_P8.csv` lists the 35 that matter,
and the five that carried the equation numbers areas (a) and (c) needed (Toupin 1962, Toupin 1964,
Mindlin 1965, Hussein 2014, Hutson & White 1962) have now all been read.

**If you rebuild from `build_p8.py`:** its `PDF_STATUS` map and the `ver`/`note` fields of
`refs_data.py` still hold the P9 values for those eleven keys, because P11 was evidence-only and
edited `refs_P8.csv` directly. Update those two first, or the rebuild will undo the P11 upgrade.
