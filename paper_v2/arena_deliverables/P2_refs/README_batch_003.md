# P2 reference verification - batch 003

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
`paper_v2/verification_register.csv` were skipped, as were the 85 keys covered by batches 001 and
002. This batch takes worklist positions 86-145.

## 2. What this batch covers

60 entries, continuing in the same order after batch 002's last key (Tiwari2021): Lata2020 through
Gorenflo1997. 470 field rows.

## 3. Level definitions used

- `R2` - the DOI printed in the bib entry was sent to Crossref and resolved to a record that carries
  the same work. Field-level disagreements are recorded row by row.
- `R1` - the bib entry carries no DOI; the entry was located on a publisher page and matched on title,
  author, journal, volume, issue and pages.
- `R0` - not verified: no catalogue record for the cited item was found, or the nearest record is a
  different edition or has an identity conflict.

## 4. Counts in this batch

- Entries by level: R2 = 59, R1 = 1, R0 = 0.
- Field rows by match: yes = 457, partial = 11, no = 2.
- Unreachable: 0. Every catalogue request in this batch returned a response; no request failed.

## 5. Findings worth acting on

- `Kumar2017` (R1): the bib gives this journal without a DOI and the journal registers none. The
  article was located on the journal's own contents page for Applications and Applied Mathematics
  Vol. 12, Issue 2 (December 2017), item 19, pp. 924-945, and all seven printed fields agree, so the
  entry is verified at R1 from a publisher page rather than from Crossref.
- `GorenfloKilbasMainardiRogosin2014` (book): the bib puts the series name
  "Springer Monographs in Mathematics" in the publisher field. The record gives the publisher as
  Springer Berlin Heidelberg and lists that series separately, so the publisher row is `no`. The bib
  carries no ISBN; the record supplies print 9783662439296 and e-ISBN 9783662439302 (recorded as
  `partial`, not added to the bib).
- `HetnarskiIgnaczak1999`: the DOI resolves, but the record keeps both authors in one unparsed string
  with the second name truncated ("Richard B. Hetnarski, Jozef Ignacza"), so the author list is only
  partly confirmed (`partial`). The same record stores the title in capitals.
- `ChadwickSneddon1958`: the record prints the second author as "Snedon", one d short of the bib's
  "Sneddon". Author row recorded as `partial`; the discrepancy is in the registry, not proved to be
  the bib's error.
- `DellOroPata2016Viscoelasticity`: the bib writes the journal as "Applied Mathematics and
  Optimization"; the record prints "Applied Mathematics & Optimization". Same journal, recorded as
  `partial`.
- `Singh2020`: the bib locator is the article number 97. Crossref returns no page field for the item;
  its `article-number` field carries 97. Per the batch rule, an article number that Crossref does not
  return as a page is `partial`.
- Issue numbers missing from the bib, supplied by the catalogue: `MindlinTiersten1962` (issue 1),
  `DellOroPata2016Viscoelasticity` (issue 3) and `HetnarskiIgnaczak2000` (issue 1-2). All three are
  `partial`, not filled in.
- `Gorenflo1997` (book chapter): the record carries the short chapter title "Fractional Calculus", so
  the bib subtitle is not confirmed (`partial`); the CISM series volume 378 is not returned by the
  record (`partial`); the record gives the publisher as "Springer Vienna" against the bib's
  "Springer" (`partial`, same publisher). Author, pages, year and DOI agree.
- Items whose locator is an article number that Crossref does return in the page field are recorded
  as `yes`: `Li2018` (e00860), `Lazar2022` (103038), `Liu2020` (103955), `Gupta2025` (118997),
  `Gupta2024a` (025515), `vanDerMerwe2021` (125934) and `WangLi2025IV` (794).
- DOI case differences are not errors; DOIs are case-insensitive. The affected entries here are
  `Aldandani2026`, `Yadav2023`, `Kumar2022` (10.1108/HFF-...), `Kumar2025` (10.47974/JIOS-1608),
  `Fu2013` (10.4028/.../AMR.803.419), `MindlinTiersten1962` (10.1007/BF00253946),
  `Mindlin1974Thermopiezo` (10.1016/0020-7683(74)90047-X) and `HetnarskiIgnaczak2000`
  (10.1016/S0020-7683(99)00089-X). They are recorded as matches with a note.

## 6. Transliteration

Catalogue and bib diacritics are rendered in ASCII and flagged in the note column: Chirita and
D'Apice (comma-below t, curly apostrophe), Iesan (s-comma-below), Fernandez/Jose/Ramon, Yaylaci
(dotless i), and the "fur" of Zeitschrift fur angewandte Mathematik und Physik. En dashes in
Klein-Gordon and Moore-Gibson-Thompson are rendered with hyphens.

## 7. Integrity checks

- Header byte-identical to the required header, read from a /tmp scratch file.
- 470 rows, 8 columns on every row, one field record per row, CRLF, CSV-quoted.
- ASCII only: 0 non-ASCII bytes and 0 control characters.
- No empty cell; `match` takes only the values yes, partial and no; `verification_level` only R2 and
  R1 in this batch.
- `paper_v2/arena_deliverables/P2_refs/` is the only directory written. No .tex, .bib, script, PDF,
  archive, `verification_register.csv` or `atlas_targets.csv` was modified.
