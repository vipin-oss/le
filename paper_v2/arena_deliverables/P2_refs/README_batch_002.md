# P2 reference verification - batch 002

Scope: bibliographic metadata only. No paper was read for content; every value in this batch was
checked against a catalogue record fetched in this session. Nothing was written to any .bib file.

## 1. Input files

- `paper_v2/refs_extra.bib` - 34 entries.
- `paper_v2/refs_new.bib` - 141 entries.
- `refs.bib`: there is **no standalone `refs.bib` in the working tree and none in the tracked tree of
  `origin/review-paper-v2`**. The file exists inside `paper_v2/paper_sources.zip` and
  `paper_v2/overleaf_package.zip` on that branch; it was extracted from `paper_sources.zip` to /tmp
  (73,224 bytes, 150 entries) and used from there. The archives and the working tree were not touched.

Union of the three files: 325 unique keys. The 87 keys already at R1, R2 or R1-noDOI in
`paper_v2/verification_register.csv` were skipped, as were the 25 keys of batch 001. That leaves a
worklist of 227 entries; this batch takes worklist positions 26-85.

## 2. What this batch covers

60 entries, continuing in the same order after batch 001's last key (Askes2011):
Maranganti2006 through Tiwari2021. 466 field rows.

## 3. Level definitions used

- `R2` - the DOI printed in the bib entry was sent to Crossref and resolved to a record that carries
  the same work. Field-level disagreements are recorded row by row.
- `R1` - the bib entry carries no DOI; the entry was located through a catalogue query and matched on
  title, author, journal, volume and pages.
- `R0` - not verified: no catalogue record for the cited item was found, or the nearest record is a
  different edition or has an identity conflict. Nothing was inferred to fill the gap.

## 4. Counts in this batch

- Entries by level: R2 = 58, R1 = 0, R0 = 2.
- Field rows by match: yes = 440, partial = 17, no = 9.
- Unreachable: 0. Every catalogue request in this batch returned a response; no request failed.

Both R0 entries are pre-1990 books: Achenbach1973 and Nowacki1975. Their treatment is set out in
section 5.

## 5. Findings worth acting on

- `Barak2023IJP`: the bib prints issue 11; the Crossref record for DOIs 10.1007/s12648-022-02568-w
  gives volume 97, issue 8, pages 2369-2383. The issue number disagrees (`match = no`); the other
  seven fields agree. This is the only hard field disagreement in the batch.
- `MooreGibson1960`: the bib gives only author, title, journal, year and DOI. The catalogue record
  supplies volume 27 and issue 2, pages 117-127. Recorded as three `partial` rows, not filled in.
- Article numbers and missing page fields: Crossref returns no `page` field for `Maranganti2006`,
  `Maranganti2007`, `Barak2023`, `Abouelregal2023`, `Gupta2026HeatMap`, `Srivastava2026`, `Yu2024`,
  `Abouelregal2020`, `Abouelregal2020a` and `Das2026`, all of which carry an article number in the
  bib. Where the bib prints a locator it is marked `partial`, because the catalogue neither confirms
  nor contradicts it; where the bib carries none, no page row is written and the entry note says so.
- `Povstenko2016`: the bib DOI 10.1007/978-3-319-15335-3 is the e-book DOI. The record is the 2015
  Springer book (series Solid Mechanics and Its Applications), print ISBN 9783319153346, e-ISBN
  9783319153353 - the bib year 2015 and its print ISBN agree. Crossref returns no publisher field for
  this item, so the publisher row is `partial`; the 10.1007 prefix indicates Springer but that is not
  printed in the record.
- `Achenbach1973` (R0): an ISBN filter query for the bib ISBN 9780444858160 returns zero records. The
  only catalogue record with this title and year is an Elsevier edited-book,
  10.1016/c2013-0-04485-4, ISBN 9780720423679, which carries no author field and a different ISBN, so
  the cited printing is not confirmed. The DOI found by title search is reported in `source_value`
  only and was not added to the bib.
- `Nowacki1975` (R0): no record for a 1975 Pergamon edition; the ISBN query for 9780080175238 returns
  zero records and Crossref holds only chapters of the 1986 edition, printed under the author name
  Witold Nowacki. Neither the edition nor the bib's author initial can be checked from the catalogue.
- `Sharma2022`: the citekey names an author who is not on the paper. The record's authors are Sherief
  and Hussein, and all eight checked fields agree with the record; the mismatch is in the citekey, not
  in the metadata.
- Year-versus-issue timing: `Gupta2023IJNMF` (issued 2022-10-18, volume 33 issue 2), `Yang2021`
  (issued 2021-03-26, volume 34 issue 1), `Barak2023JTS` (issued 2023-10-11, volume 47 issue 2) and
  `Bachher2019` (issued 2018-04-02, volume 29 issue 4) each pair an early online date with a later
  volume or issue. In every case the bib year equals the year the record carries, and the record
  itself carries the same volume and issue the bib prints, so the fields are recorded as matches.
- `Quintanilla2003DPL` omits the issue number (record: issue 7) and `Barak2023` and
  `Abouelregal2023` omit the issue (both issue 1); all recorded as `partial`, not filled in.
- DOI case differences (for example `10.1108/HFF-06-2025-0411` versus `10.1108/hff-06-2025-0411`, and
  the three 10.1103 entries) are not errors; DOIs are case-insensitive. They are recorded as matches
  with a note.

## 6. Transliteration

Four values carry diacritics or typographic characters in the bib or in the catalogue. All are
rendered in ASCII in this CSV and flagged in the note column: Quintanilla (Ramon), Chirita
(comma-below s), Craciun and Yaylaci (dotless i), and the en dash in Kelvin-Voigt, Klein-Gordon,
Moore-Gibson-Thompson and Green-Lindsay.

## 7. Integrity checks

- Header byte-identical to the required header, read from a /tmp scratch file.
- 466 rows, 8 columns on every row, one field record per row, CRLF, CSV-quoted.
- ASCII only: 0 non-ASCII bytes and 0 control characters.
- No empty cell; `match` takes only the values yes, partial and no; `verification_level` only R2 and
  R0 in this batch.
- `paper_v2/arena_deliverables/P2_refs/` is the only directory written. No .tex, .bib, script, PDF,
  archive, `verification_register.csv` or `atlas_targets.csv` was modified.
