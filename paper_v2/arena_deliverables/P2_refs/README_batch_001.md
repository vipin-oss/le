# P2 reference verification - batch 001

Scope: bibliographic metadata only. No paper was read for content; every value in this batch was
checked against a catalogue record fetched in this session.

## 1. Input files and the refs.bib question

- `paper_v2/refs_extra.bib` - 34 entries.
- `paper_v2/refs_new.bib` - 141 entries.
- `refs.bib`: there is **no standalone `refs.bib` in the working tree and none in the tracked tree of
  `origin/review-paper-v2`**. The file exists inside both `paper_v2/paper_sources.zip` and
  `paper_v2/overleaf_package.zip` in that branch; it was extracted from `paper_sources.zip` to /tmp
  (73,224 bytes, 150 entries) and used from there. Nothing was written back into the archive or the
  working tree.

Union of the three files: 325 unique keys. The register `paper_v2/verification_register.csv` already
holds 87 keys at R1, R2 or R1-noDOI; those were skipped as instructed. 227 entries remain to verify.

## 2. What this batch covers

25 entries, the first 25 in file order after `refs.bib` (keys Biot1956 through Askes2011).
193 field rows. Batches 002 onward cover the remaining 202 entries, at most 25 per batch.

## 3. Level definitions used

- `R2` - the DOI printed in the bib entry was sent to Crossref and resolved to a record that carries
  the same work. Field-level disagreements are recorded row by row.
- `R1` - the bib entry carries no DOI; the entry was located through a Crossref bibliographic query and
  matched on title, author, journal, volume and pages.
- `R0` - not verified: no catalogue record for the cited item was found, or the nearest record is a
  different edition or a republication page. Nothing was inferred to fill the gap.

## 4. Counts in this batch

- Entries by level: R2 = 21, R1 = 1, R0 = 3.
- Field rows by match: yes = 147, partial = 29, no = 17.
- Unreachable: 0. Every catalogue request in this batch returned a response; no request failed.

The three R0 entries are Tzou1997 (book; only the 2014 Wiley edition is in Crossref, which is not the
cited 1997 CRC Press edition), Cattaneo1948 (the 1948 Atti paper is not in Crossref; the only hit is a
2011 reprint page) and Vernotte1958 (no matching record).

## 5. Recurring issues worth acting on

- `GreenGN1992` and `Chester1963` omit the issue number in the bib; the catalogue supplies it
  (issue 2 and issue 5 respectively).
- `Chester1963` carries no DOI; the catalogue supplies 10.1103/physrev.131.2013. Not added to the bib
  in this task, because the bib files are out of scope here.
- `Eringen1966a` resolves through its DOI, but the Crossref record is thin: no title, first page only
  and a single author initial. The entry is probably correct, but the catalogue cannot confirm the
  title or the page range; flagged for a publisher-page check.
- `Iesan2004` volume 118 is a series volume; the Crossref book record does not return it.
- DOI case differences (for example `10.1007/BF00045689` versus `10.1007/bf00045689`) are not errors;
  DOIs are case-insensitive. They are recorded as matches with a note.

## 6. Integrity checks

- Header byte-identical to the required header, read from a /tmp scratch file.
- 193 rows, 8 columns on every row, one record per row, CRLF, CSV-quoted.
- ASCII only: 0 non-ASCII bytes and 0 control characters.
- `match` takes only the values yes, partial and no; `verification_level` only R0, R1 and R2.
- No diacritic appears in the output; the catalogue form of the Iesan surname was transliterated.
