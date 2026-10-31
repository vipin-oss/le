# P2 reference verification - batch 005 (final batch)

Scope: bibliographic metadata only. No paper was read for content; every value in this batch was
checked against a catalogue record fetched in this session. Nothing was written to any .bib file.

This is the last batch on the worklist, so section 7 carries the closed totals for batches 001-005
and the full list of every entry that ended at R0.

## 1. Input files

- `paper_v2/refs_extra.bib` - 34 entries.
- `paper_v2/refs_new.bib` - 141 entries.
- `refs.bib`: there is **no standalone `refs.bib` in the working tree and none in the tracked tree of
  `origin/review-paper-v2`**. The file exists inside `paper_v2/paper_sources.zip` and
  `paper_v2/overleaf_package.zip` on that branch; it was extracted from `paper_sources.zip` to /tmp
  (73,224 bytes, 150 entries) and used from there. The archives and the working tree were not touched.

Union of the three files: 325 unique keys. The 87 keys already at R1, R2 or R1-noDOI in
`paper_v2/verification_register.csv` were skipped, as were the 190 keys covered by batches 001-004.
This batch takes the last 48 keys on the worklist, positions 191-238.

## 2. What this batch covers

48 entries, continuing in the same order after batch 004's last key (Yu2014): Ezzat2016a through
Gulyaev1969. 359 field rows.

- 31 entries print a DOI in the bib. Thirty of them were resolved with four batched Crossref
  `filter=doi:` requests; `Mueller1967` is treated separately in section 5 because its DOI belongs to
  a different work.
- 17 entries print no DOI. Six of them are journal articles and were located with Crossref
  bibliographic queries (Rayleigh1885, Ackerman1966, Jackson1970, Kaminski1990, Mitra1995,
  Pennes1948); six are books held by Open Library (Podlubny1999, Boley1960, Scruby1990, Auld1973,
  Cohen2007, IgnaczakOstoja2010) and one more book was checked on the publisher's page (Jou2010);
  the remaining four are the R0 entries in section 5.

Row-level sources: Crossref 298 rows, Open Library 46, Gallica/BnF 8, Springer book page 7.

## 3. Level definitions used

- `R2` - the DOI printed in the bib entry was sent to Crossref and resolved to a record that carries
  the same work. Field-level disagreements are recorded row by row.
- `R1` - the entry was verified against a catalogue record located without using a bib DOI: a Crossref
  bibliographic search, an Open Library record or a publisher page. A DOI found during that search is
  reported in `source_value` only and was not added to the bib. `Mueller1967` is R1 because its
  printed DOI is wrong, not because it lacks one.
- `R0` - not verified: no catalogue record for the cited item was found. The rows still record what
  the search did reach, so the reason for the R0 is visible on every row.

## 4. Counts in this batch

- Entries by level: R2 = 30, R1 = 14, R0 = 4.
- Field rows by match: yes = 256, partial = 75, no = 28.
- Unreachable: 0. Every catalogue request returned a response; no request failed.

## 5. Findings worth acting on

- `Mueller1967` (R1, the one identity conflict in this batch): the bib prints DOI
  10.1007/978-1-4612-2210-1, which resolves to a 1998 Springer book, *Rational Extended
  Thermodynamics* by Muller and Ruggeri, not to the cited article. The DOI row is therefore `no`.
  A Crossref bibliographic query located the actual article - Ingo Muller, "On the entropy
  inequality", Archive for Rational Mechanics and Analysis 26:118-141 - under DOI
  10.1007/BF00285677, and title, author, journal, year, volume and pages all agree. One further
  disagreement: the bib gives issue 1, the record gives issue 2 (`no`). The entry therefore ends at
  R1, not R2: it is verified against the right record, but the DOI in the bib must be replaced by
  10.1007/BF00285677 before submission. The bib also carries publisher, address, edition, booktitle
  and editor fields that do not belong to a journal article.
- Four R0 entries:
  - `Duhamel1837`: nothing in Crossref or Open Library; Gallica holds the *Journal de l'Ecole
    polytechnique* as a series (1795-1939) but no record of volume 15, cahier 25 or of the article.
  - `Chadwick1960`: Open Library holds the four-volume series *Progress in Solid Mechanics* (editors
    Sneddon and Hill, North-Holland, Amsterdam, 1960), which confirms the series title, publisher,
    place and start year, but not volume 1, the chapter title or pp. 263-328.
  - `Carlson1972`: the catalogue holds *Encyclopedia of Physics* VIa/3 and a Group 3 volume, not
    VIa/2, so the chapter "Linear thermoelasticity" could not be checked at all.
  - `Gulyaev1969`: no 1969 *JETP Letters* material in Crossref; the JETP archive at jetp.ras.ru uses
    the JETP volume numbering, in which volume 9 is 1959. The bib's own note already says "entered
    from memory; verify before submission".
- Eight entries (`Pathania2023`, `Gupta2024b`, `Barak2023a`, `Gupta2023a`, `Gupta2023b`,
  `Gupta2023c`, `Guha2025`, `Gupta2025a`) print the author field as "FirstAuthor and others" with the
  note "first author only". The author row is `partial` for each; the catalogue supplies the full
  author list. These same eight entries print no volume, issue or pages, so those three rows are
  `partial` as well - the values are in `source_value` but were not inserted into the bib.
- `Jou2010` (book, R1): the bib lists three authors; the 2010 fourth edition as catalogued lists two
  (David Jou, Georgy Lebon). The edition statement itself is confirmed (4th edition), publisher
  `Springer Netherlands` against the bib's `Springer` (`partial`), year 2010 confirmed.
- `Mitra1995`: the third author's surname is `Vedavarz` in the bib and `Vedevarz` in the record
  (`partial`). Same pattern as `ChadwickSneddon1958` in batch 003 - the discrepancy is in the
  registry, not proved to be the bib's error.
- `Pennes1948`: the record's title string ends with a stray HTML italic close tag. The title row is
  `yes` with the artifact noted, because the wording agrees and the noise is in the registry.
- Locators that Crossref does not return as a page: `Tiwari2022` (article-number 190) and `Singh2023`
  (article-number 105). The bib prints no pages for either and the record has no page field, so both
  `pages` rows are `partial`.
- Issue numbers missing from the bib while the record supplies them: 33 rows, `partial` in every
  case. They cover Abouelregal2021 through Conti2019 among the DOI entries, plus Ackerman1966,
  Jackson1970, Rayleigh1885, Kaminski1990, Mitra1995 and Pennes1948 among the no-DOI articles.
- DOIs found for entries that print none (reported in `source_value`, never added to the bib):
  Rayleigh1885 10.1112/plms/s1-17.1.4, Ackerman1966 10.1103/physrevlett.16.789, Jackson1970
  10.1103/physrevlett.25.26, Kaminski1990 10.1115/1.2910422, Mitra1995 10.1115/1.2822615, Pennes1948
  10.1152/jappl.1948.1.2.93, Jou2010 10.1007/978-90-481-3074-0.
- ISBNs found for the six books that print none: Podlubny1999 9780125588409, Boley1960 0471086797,
  Scruby1990 0750300507, Auld1973 0471037001 (Wiley 1973 edition), Cohen2007 9780387282619,
  IgnaczakOstoja2010 9780199541645. All `partial`, none written into the bib.

## 6. Transliteration

Catalogue and bib diacritics are rendered in ASCII and flagged in the note column: the LaTeX accents
in the bib (`M{\"u}ller`, `m{\'e}moire`, `ph{\`e}nom{\`e}nes`), the Romanian t-comma-below in
`Chirita2024` and the curly apostrophe in D'Apice, and the en dashes in the Moore-Gibson-Thompson and
Maxwell-Cattaneo titles. No character outside printable ASCII appears in the CSV.

## 7. Closed totals for the worklist, batches 001-005

Worklist: 238 keys (325 unique bib keys minus the 87 already at R1, R2 or R1-noDOI in the register).
All 238 are now accounted for.

| Batch | Entries | Field rows | R2 | R1 | R0 | yes | partial | no |
|-------|---------|-----------|----|----|----|-----|---------|----|
| 001   | 25      | 193       | 21 | 1  | 3  | 147 | 29      | 17 |
| 002   | 60      | 466       | 58 | 0  | 2  | 440 | 17      | 9  |
| 003   | 60      | 470       | 59 | 1  | 0  | 457 | 11      | 2  |
| 004   | 45      | 348       | 44 | 1  | 0  | 307 | 39      | 2  |
| 005   | 48      | 359       | 30 | 14 | 4  | 256 | 75      | 28 |
| Total | 238     | 1836      | 212| 17 | 9  | 1607| 171     | 58 |

- Keys verified in some way (R2 or R1): 229 of 238 (96.2%).
- At R2, the bib DOI itself resolved to the cited work: 212.
- At R1, verified against a catalogue record without a usable bib DOI: 17.
- At R0, no record found: 9.
- Unreachable across all five batches: 0.

**Every entry that ended at R0 (9):**

| Key | What it is | Why R0 |
|-----|------------|--------|
| Cattaneo1948 | journal article, 1948 | only a 2011 republication page exists in Crossref |
| Vernotte1958 | journal article, 1958 | query returned unrelated records only; the Comptes Rendus vol. 246 citation is not verifiable from Crossref |
| Tzou1997 | book | only the 2014 Wiley edition is catalogued, which is a different edition |
| Achenbach1973 | book | no record carries the bib ISBN; the only title match is an Elsevier edited-book record with no author field |
| Nowacki1975 | book | only the 1986 Pergamon edition was reached |
| Duhamel1837 | journal article, 1837 | no article-level record; Gallica has the journal series only |
| Chadwick1960 | book chapter | series record only; volume 1, chapter title and pages unconfirmed |
| Carlson1972 | book chapter | no record for Encyclopedia of Physics VIa/2 |
| Gulyaev1969 | journal article, 1969 | no 1969 JETP Letters record; bib itself flags it as entered from memory |

**Every entry that ended at R1 (17):** Chester1963 (001), Kumar2017 (003), Eringen2002 (004),
Mueller1967, Jou2010, Podlubny1999, Boley1960, Scruby1990, Auld1973, Cohen2007, IgnaczakOstoja2010,
Rayleigh1885, Ackerman1966, Jackson1970, Kaminski1990, Mitra1995, Pennes1948 (005).

## 8. Integrity checks

- Header byte-identical to the required 8-column header and to the first line of
  `verified_refs_batch_004.csv`; the header was read from a /tmp scratch file.
- 359 rows, 8 columns on every row, one field record per row, CRLF, CSV-quoted, 82,197 bytes,
  360 CRLF-terminated lines.
- ASCII only: 0 non-ASCII bytes and 0 control characters.
- No empty cell; `match` takes only the values yes, partial and no; `verification_level` only R2, R1
  and R0; every one of the 48 keys appears, in worklist order.
- `paper_v2/arena_deliverables/P2_refs/` is the only directory written. No .tex, .bib, script, PDF,
  archive, `verification_register.csv` or `atlas_targets.csv` was modified.
- No bib field was changed anywhere. Where the catalogue disagreed with the bib, the catalogue value
  is in `source_value` and the bib is untouched.
