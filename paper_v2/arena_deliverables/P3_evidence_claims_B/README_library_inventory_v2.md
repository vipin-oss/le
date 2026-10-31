# library_inventory_v2 — first-page inventory of the unzipped library folder

Source: the one folder of unzipped PDFs present in the project's Drive source library
(the archive `LE_PAPERS_P01`, fully extracted, 37 PDFs, 16 MB). The other two archives
(P02, 52 MB; P03, 62 MB) are **not** extracted, so their papers are still not readable.
PDFs were read in place; nothing was copied into or committed to this repository.

## Files

| file | contents |
|---|---|
| `library_inventory_v2.csv` | 37 rows, one per PDF: `file_name, first_page_title, first_page_doi, matched_bib_key` |
| `library_inventory_v2_findings.csv` | the 7 PDFs that match no key in `refs*.bib`, with a recommended action |
| `check_library_inventory_v2.py` | validator; prints `PASS ...` and exits 0 |

## Method (and its limits)

* **First page only** was read for every file, exactly as requested. Nothing was inferred
  from the file name and nothing was filled in from memory: if a DOI is not printed on
  page 1 it is left blank, and `first_page_title` records the title, authors and the
  journal line that page 1 actually shows.
* `matched_bib_key` is filled only when the *content* of page 1 clearly corresponds to a
  key in `refs*.bib` (title match, author match, and journal/volume agreement).
  * blank = no key in `refs*.bib` describes this paper (see the findings file);
  * `MISMATCH (...)` = the file name points at a bib key, but page 1 shows a **different
    work**, so the file must not be used as that citation.

## Result at a glance

* 37 PDFs = 20 real papers/books + **17 withdrawn placeholders**.
* 11 exact key matches: `Biot1956`, `Eringen1972`, `Eringen1974`, `GuyerKrumhansl1966`,
  `AbateWhitt2006`, `Dhaliwal1980`, `Quintanilla2003DPL`, `Rayleigh1885`, `Stoneley1924`,
  `Talbot1979`, `Yang2018`.
* 7 papers with no key in the bibliography (findings file).
* 19 mismatches: 2 misleading file names + 17 empty Achenbach placeholders.

### The two misleading file names

1. **`quintanilla2008.pdf` is not `Quintanilla2008`.** Page 1 is *"A note on stability in
   three-phase-lag heat conduction"* by Quintanilla and Racke (Elsevier, received
   20 March 2007, available online 30 July 2007) — i.e. the paper the bibliography keys as
   **`Quintanilla2008a`** (`10.1016/j.ijheatmasstransfer.2007.04.045`). The cited
   *"End effects in three-phase-lag heat conduction"* (`10.1080/00036810802428938`)
   is **still not held**, so `CR019` stays blocked while `CR020` becomes checkable.
2. **`tzou1995.pdf` is not `Tzou1995`.** Page 1 is *"Experimental support for the lagging
   behavior in heat propagation"* (J. Thermophysics and Heat Transfer **9**(4), 1995),
   whereas the key `Tzou1995` is the 1995 *International Journal of Heat and Mass Transfer*
   paper *"A unified field approach for heat conduction from macro- to micro-scales"*.

### Opaque file names decoded (name says nothing, content is clear)

`1.1722351.pdf` = Biot 1956 (J. Appl. Phys. **27**, 240); `RAGJAKI.pdf` = Guyer and
Krumhansl 1966 (Phys. Rev. **148**, 766); `qam%2F575828.pdf` = Dhaliwal and Sherief,
*Q. Appl. Math.* **38**(1), 1980; `0020-72252990050-x.pdf` = Eringen 1972 (nonlocal
elasticity); `0020-72252990033-0.pdf` = Eringen 1974 (nonlocal thermoelasticity).

### Withdrawn placeholders — never citable

All 17 `WITHDRAWN--*` / `CHAPTER-*-WITHDRAWN--*` files contain only the chapter heading and
the sentence *"This book has been withdrawn."* (58–80 kB each). They are the front matter
and chapters of Achenbach, *Wave Propagation in Elastic Solids* (1975). No text, no
equation and no page of Achenbach can be quoted from them, so `Achenbach1973` must stay
unverified unless a real copy is obtained.

## Consequence for `P3_evidence_claims_C`

Of the 141 priority rows in `missing_sources_priority.csv`, only three correspond to a file
in this folder:

| priority rank | key | blocked claim | status after this inventory |
|---|---|---|---|
| 14 | `Quintanilla2003DPL` | CR003 | **checkable** — file present and matching |
| 24 | `Quintanilla2008a` | CR020 | **checkable** — file present and matching |
| 23 | `Quintanilla2008` | CR019 | **still blocked** — the file of that name is the 2008a paper |

No other blocked claim in `claim_register.csv` cites a paper that this folder now supplies,
so the C batches can carry at most these rows until the P02/P03 archives are extracted
(they are 52 MB and 62 MB, above the 25 MB per-file read limit).

---

# Part 2 — the second, much larger unzip (79 files read)

The same folder was later filled with many more PDFs. Every file added in that wave was
read the same way (first page only) and recorded in
`library_inventory_v2_part2.csv` (79 rows), with `library_inventory_v2_part2_findings.csv`
for the 26 files that match no key. The library was still growing while this pass ran —
a ZIP (`ScienceDirect_articles_23Oct2026_17-34-39.438.zip`) also appeared and is not a
paper, so it is not in the CSV.

Result: **51 matches, 26 without a key, 2 mismatches.**

## The four Task-4 papers and the landmark are now here

| file | page 1 shows | key |
|---|---|---|
| `cahill2003.pdf` | *Nanoscale thermal transport*, Cahill et al., J. Appl. Phys. **93**, 793 (2003), DOI `10.1063/1.1524305` | `Cahill2003` |
| `huberman2019.pdf` | *Observation of second sound in graphite at temperatures above 100 K*, Science, **first release 14 March 2019** (the page says page numbers are not final) | `Huberman2019` |
| `jackson1970.pdf` | *Second sound in NaF*, Jackson, Walker & McNelly, PRL **25**(1), 6 July 1970 — the scan also carries the end of the previous article of that issue on the same page | `Jackson1970` |
| `gurtin1968.pdf` | *A General Theory of Heat Conduction with Finite Wave Speeds*, Gurtin & Pipkin | `GurtinPipkin1968` |
| `2ndSoundSolids.pdf` | *Second Sound in Solids*, Marvin Chester, Phys. Rev. **131**, 2013 (1963) — the scan opens with the tail of the preceding article on anomalous surface reflection of X-rays, and Chester's paper starts further down the same page | `Chester1963` (corrected 2026-10-31) |

## Two new traps

1. **`2ndSoundSolids.pdf` is the wrong *item*, but not an unreadable file.** CORRECTED
   2026-10-31: a first-lines-only pass had stopped inside the tail of the preceding
   article (an X-ray surface-reflection paper that ends on the same printed page), so the
   file was recorded as that article. Reading the whole first page shows that the file's
   own paper starts on it: **Marvin Chester, *Second Sound in Solids*, Physical Review 131,
   2013-2015 (1963)**, with its abstract ("a critical frequency ... above which heat
   transport proceeds by wave propagation rather than by diffusion") and, on p. 2014, the
   modified Fourier equation with a relaxation time and the Maxwell / Cattaneo / Vernotte
   references. So the file *is* a second-sound source and it settles CR098 — but it is a
   theory paper, not the review of second sound that this item was filed as, and that
   review is still missing.
2. **`ezzat2011.pdf` is not `Ezzat2011`.** The file is *Theory of fractional order in
   generalized thermoelectric MHD* (Applied Mathematical Modelling), whereas the key
   `Ezzat2011` is *Fractional order heat conduction law in magneto-thermoelasticity
   involving two temperatures*, ZAMP **62**(5) 937-952 (`10.1007/s00033-011-0126-3`).
   Any earlier verdict resting on "the library Ezzat 2011" should be re-checked against
   the ZAMP paper.

## Files that could not be read, and files with no key

* **Not readable:** `eringen1966.pdf` (no text layer), `maxwell1867.pdf` (JSTOR cover
  sheet only), `10.1007@978-1-4612-2210-1.pdf` (30.2 MB, over the cap),
  `povstenko2015.pdf` (reader error on every attempt), and `chen2021.pdf` /
  `bf01597243.pdf`, whose page 1 does not print their own title.
* **26 papers have no bib key** (see the findings file): Chen-Gurtin-Williams, El-Karamany
  and Ezzat 2016, Zenkour and El-Mekawy, Azhdari et al., Eringen and Edelen, Eringen 1972
  (nonlocal polar), Mindlin 1965 and 1968, Puri 1972, Nayfeh and Nemat-Nasser 1971,
  Deresiewicz 1957, Liu 1972, Coleman 1964, Chandrasekharaiah 1988, Achenbach 1968,
  Crump 1976, Compte 1997, Atangana and Baleanu, Quintanilla and Racke 2003, and the five
  unreadable/unidentified files above.

Validator: `python3 check_library_inventory_v2_part2.py`
→ `PASS all checks (rows=79, match=51, blank=26, mismatch=2, findings=26)`.
