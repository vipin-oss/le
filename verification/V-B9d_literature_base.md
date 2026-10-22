# V-B9d — `LITERATURE_BASE`: Abouelregal 2020 and Green–Naghdi 1992 added with `read_level`

**Order:** `control/BRAVE_B9.md` item 3 @ `origin/claude/control` `79999f7`. **Access date:** 2026-10-22.
**File changed:** `verification/LITERATURE_BASE.csv` only (428 → 430 rows). No `.bib` regeneration in
this item (see §7).

---

## 1. Task

Add **Abouelregal 2020 (Sci Rep)** and **Green–Naghdi 1992** to `LITERATURE_BASE` **with `read_level`**,
because both were missing while being load-bearing: the first is the only higher-order (`τʳ/r!`)
three-phase-lag model I have actually read, the second is the paper normally credited with Green–Naghdi
type II and had no row at all (flagged in `V-B7a` / `V-B8a`).

## 2. Method

1. Read the existing header and row schema (`id,authors,year,title,venue,DOI,type,sub_area,citations,
   read_level,proposed_section,why`) and copied the style of neighbouring rows exactly.
2. Verified **both** records against Crossref **this session** before writing them; nothing was entered
   from memory or from a secondary citation alone.
3. Assigned `id`s as the next two free integers (`LIT-0429`, `LIT-0430`) and re-read the file to confirm
   uniqueness and the new counts.
4. `read_level` assigned per the standing rule: `FULL` only for text I have actually read; Crossref
   metadata is **not** reading.

## 3. Result

| field | LIT-0429 | LIT-0430 |
|---|---|---|
| authors | Abouelregal; Khalil; Mohammed; Nasr; Zakaria; Ahmed | Green; Naghdi |
| year | 2020 | 1992 |
| title | A generalized heat conduction model of higher-order time derivatives and three-phase-lags for non-simple thermoelastic materials | On undamped heat waves in an elastic solid |
| venue | Scientific Reports (vol. 10) | J. Thermal Stresses **15**(2), 253–264 |
| DOI | `10.1038/s41598-020-70388-1` | `10.1080/01495739208946136` |
| citations | 32 (Crossref, 2026-10-22) | 1555 (Crossref, 2026-10-22) |
| `read_level` | **FULL** — gold OA; eqs (7)–(11) read earlier the same day; not re-opened in B9 | **metadata only** — Crossref record read 2026-10-22; paper not opened |
| sub_area | DPL / TPL | GN |
| proposed_section | s.4.8 | s.4.5–4.6 |

Base counts after the edit: **430 rows**, 430 distinct DOIs, **7** rows at `FULL`, **308** rows with a
blank `authors` field.

Two corrections to my own prior notes, recorded because both had been used in earlier verdicts:

* Green–Naghdi 1992 is **J. Thermal Stresses 15(2), 253–264**, not "J. Elasticity 31:189–208" as my
  earlier session note said. Crossref `container-title` = "Journal of Thermal Stresses", `volume` 15,
  `issue` 2, `page` 253-264, `issued` 1992-04. The earlier note was wrong; the base now carries the
  confirmed record.
* The blank-author count is **308**, not the 290 quoted in the B10 brief. B10d's "290 blank authors"
  target should be re-based to 308 or the difference explained before the Drive pass starts.

## 4. Evidence / sources

* `https://api.crossref.org/works/10.1038/s41598-020-70388-1` — Crossref JSON read 2026-10-22:
  title, six authors in order, vol. 10, `is-referenced-by-count` 32, CC-BY licence, published
  2020-08-12. Abstract (quoted here only in substance): higher-order three-phase lags with two
  temperatures, Chen–Gurtin as a special case. **Access level: metadata + abstract; the full text was
  read earlier the same day** (gold OA publisher pages, eqs (7)–(11)).
* `https://api.crossref.org/works/10.1080/01495739208946136` — Crossref JSON read 2026-10-22:
  "ON UNDAMPED HEAT WAVES IN AN ELASTIC SOLID", A. E. Green & P. M. Naghdi, J. Thermal Stresses 15(2)
  253–264, `is-referenced-by-count` 1555. **Access level: metadata only; the paper was not opened.**
* `verification/LITERATURE_BASE.csv` before/after (428 → 430 rows); the file is committed as data, no
  PDF, no text, no page image.

## 5. Checks done

1. Both DOIs resolved at Crossref and the returned title/author/venue/volume/pages were copied
   field-by-field; no field was filled from memory.
2. IDs `LIT-0429`/`LIT-0430` are unique in the file (the loader reports 430 rows, 430 distinct DOIs, no
   duplicate ID).
3. `read_level` distinguished honestly between the two: one `FULL` (read), one `metadata only` (not
   read). A Crossref record is *not* reading — that distinction is the whole point of the field.
4. Re-read the written file with `csv.DictReader` to confirm the schema survived (12 columns, quoting
   around the comma-bearing `why` field intact).
5. Counted `FULL` (7) and blank-author (308) rows after the edit so the numbers I quote are measured,
   not assumed.

## 6. Confidence

* Bibliographic fields of both rows: **HIGH** (publisher-deposited Crossref records).
* Green–Naghdi year/venue/pages: **HIGH**; my earlier "J. Elasticity 31" note is **retracted** here.
* That Abouelregal et al. is a *legitimate* primary for a higher-order `τʳ/r!` TPL family: **HIGH** —
  read directly (eqs (7)–(11)), and it is the only such primary in the base.
* That no other row duplicates these two: **HIGH** for DOIs (430 distinct), **MEDIUM** for title
  variants — a paper indexed under a different DOI elsewhere would not be caught by a DOI check.

## 7. NOT verified / open issues

* **Green–Naghdi 1992 was not read.** It is `metadata only`; no claim about its equations, its type-II
  vs type-III content, or its free-energy assumptions is made anywhere on the strength of this row. The
  type-II/type-III attribution remains contradictory across secondary sources (`V-B8a` §3.5) and this
  addition does **not** resolve it.
* `literature_base.bib` was **not** regenerated. `make_bibtex.py` is known to garble author strings and
  is outside this item; the two new rows will appear in the `.bib` only when that script is next run.
  Flagged rather than silently left inconsistent.
* The blank-author problem is **308 rows**, not 290; nothing in this item reduced it. That is B10d's job
  and needs the re-base noted in §3.
* I did not check whether either paper is already present in `literature_base.bib` under a different
  key, nor whether `CITATION_MAP.csv` should gain entries for them — both are downstream of this item
  and untouched.
* The Abouelregal row's `why` field says its third lag is a *temperature* lag in a two-temperature model
  rather than the manuscript's `τ_ν`. That reading comes from the abstract plus my earlier full-text
  read, not from a re-read today; treat it as `FULL`-grade but not re-confirmed in B9.
