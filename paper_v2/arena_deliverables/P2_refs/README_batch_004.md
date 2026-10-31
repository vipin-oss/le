# P2 reference verification - batch 004

Scope: bibliographic metadata only. No paper was read for content; every value in this batch was
checked against a catalogue record fetched in this session. Nothing was written to any .bib file.

This is the last batch of the reference worklist, so section 7 also carries the totals for the whole
worklist (batches 001-004).

## 1. Input files

- `paper_v2/refs_extra.bib` - 34 entries.
- `paper_v2/refs_new.bib` - 141 entries.
- `refs.bib`: there is **no standalone `refs.bib` in the working tree and none in the tracked tree of
  `origin/review-paper-v2`**. The file exists inside `paper_v2/paper_sources.zip` and
  `paper_v2/overleaf_package.zip` on that branch; it was extracted from `paper_sources.zip` to /tmp
  (73,224 bytes, 150 entries) and used from there. The archives and the working tree were not touched.

Union of the three files: 325 unique keys. The 87 keys already at R1, R2 or R1-noDOI in
`paper_v2/verification_register.csv` were skipped, as were the 145 keys covered by batches 001-003.
That leaves 238 keys on the worklist; this batch takes positions 146-190, i.e. the first 45 of the
remaining 93.

## 2. What this batch covers

45 entries, continuing in the same order after batch 003's last key (Gorenflo1997): Eringen1999
through Yu2014. 348 field rows. Every row is sourced from the Crossref REST API: 44 entries carry a
DOI in the bib and were resolved through ten batched `filter=doi:` requests; `Eringen2002` carries no
DOI and was located with a Crossref bibliographic query plus a lookup of the record it returned.

## 3. Level definitions used

- `R2` - the DOI printed in the bib entry was sent to Crossref and resolved to a record that carries
  the same work. Field-level disagreements are recorded row by row.
- `R1` - the bib entry carries no DOI; the entry was located in the catalogue and matched on title,
  author and publisher without the DOI being usable as the anchor.
- `R0` - not verified: no catalogue record for the cited item was found, or the nearest record is a
  different edition or has an identity conflict.

## 4. Counts in this batch

- Entries by level: R2 = 44, R1 = 1, R0 = 0.
- Field rows by match: yes = 307, partial = 39, no = 2.
- Unreachable: 0. Every catalogue request in this batch returned a response; no request failed.
- Source sites: Crossref API only, 348 of 348 rows.

## 5. Findings worth acting on

- `Eringen2002` (the single R1 entry): the bib carries no DOI. A Crossref bibliographic search
  returned the book under DOI 10.1007/b97697 (Springer New York), which matches the bib on title,
  author and publisher, but the record's print date is 2004 against the bib's 2002 (`no` on year) and
  its ISBN is 9780387952758 (ISBN-10 0-387-95275-6) against the bib's 0387952697 (`no` on ISBN). The
  record also lists Eringen in its editor field and has no author field, so authorship is `partial`.
  The DOI found is reported in `source_value` only and was not added to the bib.
- Issue numbers missing from the bib, supplied by the catalogue: 34 of the 42 article entries in this
  batch print no `number`, while the record carries one (Kumar2010 2, Suh1998 3, Ignaczak1980 3,
  Wang2001 4, Verma2001 15, Sinha2003 5-6, Ezzat2010 4, Anwar1994 2, Hamza2014 9, Sachan2022 4,
  Carini2019 1, Youssef2014 10, Lazzari2016 7, Chirita2010 3, Gupta2019 9, Xue2020 1, Xu2015 3,
  Quintanilla2006 7-8, Julius2017 3, Miranville2010 1, Quintanilla2008a 1-2, Satish2021 8,
  Tiwari2015 4, Sur2012 12, Yu2021 04, Tripathi2016 2, Sherief2018 7, Youssef2010a 10, Tiwari2014 2,
  Youssef2014a 8, Singh2020d 10, Sarkar2020 7, Ezzat2016 10, Sarkar2019a 11). All are `partial`, not
  filled in.
- Locators that Crossref does not return as a page: `Julius2017` (article-number 031301),
  `Singh2020d` (102103) and `Ezzat2016` (372). The bib prints no pages for these, and the record
  carries no page field, so the `pages` row is `partial` in all three cases.
- Article numbers that Crossref does return in its page field are recorded as `yes`: `Xu2015`
  (034401), `Yang2020` (119752), `Miranville2022` (108264), `Kumar2020` (118997) and `Yu2021`
  (2150082).
- Records that store the title in capitals: `Ignaczak1980`, `Anwar1994` and `Yu2021` (which also
  stores both author names in capitals). Recorded as matches with a note.
- Ampersands: `Sinha2003` ("Computers \& Mathematics with Applications") and `Miranville2010`
  ("Applied Mathematics \& Optimization") print the LaTeX-escaped ampersand in the bib and the
  character itself in the record; the same journal, so `yes` with a note (not the 003-style
  "and"/"&" spelling difference).
- DOI case: `Aifantis2003` prints `10.1016/S0167-6636(02)00278-8`, the record returns the same DOI in
  lower case. DOIs are case-insensitive, so `yes` with a note.
- Author forms recorded as `yes` with a note because only the name order or the initials differ:
  every `refs_new.bib` entry prints surnames first with initials, while Crossref prints given names
  first. Three specific cases: `Satish2021` (the record spells the third author's middle name in full,
  K. Brahma Raju), `Singh2020d` (the record keeps the parentheses in Pal (Sarkar)) and `Sherief2018`
  (the record prints the initials without full stops).
- Three books were checked as books, not as journal articles: `Eringen1999` (ISBN 9781461268154,
  year 1999, DOI resolves), `Yang2018` (ISBN 9783030031367, year 2018, DOI resolves) and
  `Eringen2002` (see above).

## 6. Transliteration

Catalogue and bib diacritics are rendered in ASCII and flagged in the note column: Chirita (Romanian
t-comma-below) in `Chirita2010`; the typographic apostrophe in Eringen's in `Xue2020`; the en dashes
in Green-Naghdi in `Youssef2014` and `Lazzari2016`, and those in the Moore-Gibson-Thompson titles,
rendered with hyphens. No character outside printable ASCII appears in the CSV.

## 7. Whole worklist status after batch 004

Worklist: 238 keys (325 unique bib keys minus the 87 already at R1, R2 or R1-noDOI in the register).

| Batch | Entries | Field rows | R2 | R1 | R0 | yes | partial | no |
|-------|---------|-----------|----|----|----|-----|---------|----|
| 001   | 25      | 193       | 21 | 1  | 3  | 147 | 29      | 17 |
| 002   | 60      | 466       | 58 | 0  | 2  | 440 | 17      | 9  |
| 003   | 60      | 470       | 59 | 1  | 0  | 457 | 11      | 2  |
| 004   | 45      | 348       | 44 | 1  | 0  | 307 | 39      | 2  |
| Total | 190     | 1477      | 182| 3  | 5  | 1351| 96      | 30 |

- Entries verified: 190 of 238 (79.8%), at R2 = 182, R1 = 3 and R0 = 5.
- Unreachable across all four batches: 0.
- Entries still unverified: **48** (worklist positions 191-238). They are listed here so the gap is
  explicit and no count is implied that was not done:

  Ezzat2016a, Abouelregal2021, Sarkar2020a, Tiwari2022, Ezzat2016b, Ezzat2015, Sarkar2021, Li2020,
  Singh2021, Kumar2020a, Singh2023, Florea2021, Conti2019, Singh2022, Srivastava2023, Das2023,
  Jangid2020, Chirita2024, Kumar2008a, Kumar2024b, Vashishth2016, Deswal2019, Pathania2023,
  Gupta2024b, Barak2023a, Gupta2023a, Gupta2023b, Gupta2023c, Guha2025, Gupta2025a, Duhamel1837,
  Chadwick1960, Ackerman1966, Jackson1970, Rayleigh1885, Mueller1967, Jou2010, Podlubny1999, Boley1960,
  Carlson1972, IgnaczakOstoja2010, Kaminski1990, Mitra1995, Pennes1948, Scruby1990, Auld1973,
  Cohen2007, Gulyaev1969.

  Of these 48, 31 print a DOI in the bib and are therefore candidates for R2; the other 17 print none
  (books and pre-1990 classics), and several of those are expected to end at R0. One of the 31,
  Mueller1967, prints the DOI of a Springer book while citing an article in Archive for Rational
  Mechanics and Analysis, so its identity will need care.

## 8. Integrity checks

- Header byte-identical to the required 8-column header and to the first line of
  `verified_refs_batch_003.csv`; the header was read from a /tmp scratch file.
- 348 rows, 8 columns on every row, one field record per row, CRLF, CSV-quoted, 64,938 bytes,
  349 CRLF-terminated lines.
- ASCII only: 0 non-ASCII bytes and 0 control characters.
- No empty cell; `match` takes only the values yes, partial and no; `verification_level` only R2 and
  R1 in this batch.
- `paper_v2/arena_deliverables/P2_refs/` is the only directory written. No .tex, .bib, script, PDF,
  archive, `verification_register.csv` or `atlas_targets.csv` was modified.
