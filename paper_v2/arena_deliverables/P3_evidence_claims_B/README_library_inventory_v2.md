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
