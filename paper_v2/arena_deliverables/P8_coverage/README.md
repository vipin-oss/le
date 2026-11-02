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

Verification: **72 × R0** (title/venue/volume/pages/DOI matched against a Crossref record on
2026-11-02). No abstract was read, no full text was read, **no equation number is verified**.
Nothing is quoted, no page range or DOI was written from memory, and no missing paper was
filled in from guesswork — see `coverage_gaps.md` for what is still unverified.

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
- `build_p8.py` — regenerates the `.bib` and `.csv` from the single data file; asserts key
  uniqueness and zero clash with the existing bibliography.
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
| R0 | title/venue/pages/DOI matched in Crossref only | 72 |
| R1 | abstract read | 0 |
| R2 | full text read | 0 |
| R3 | equations checked | 0 |

The next step is not more references but reading: `pdfs_needed_P8.csv` lists the 35 that matter,
five of which (Toupin 1962, Toupin 1964, Mindlin 1965, Hussein 2014, Hutson & White 1962) carry
the equation numbers that areas (a) and (c) need.
