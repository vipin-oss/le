# P2-a Reference Metadata and Evidence Audit - Batch 003

## Scope and method
- Audited the next 15 unattempted records in source order from `paper_v2/paper_sources.zip!refs_extra.bib`: Duhamel1837 through Huberman2019.
- External page access test succeeded on the APS publisher page `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.16.789` before the audit. That page was only the access test and is not batch evidence.
- For each record, searches by title and first author were used only to locate a publisher, journal, or catalogue page. Pages listed in the evidence CSV were actually opened. Search snippets, Wikipedia, memory, and incidental Drive citation hits were not used as evidence. No Drive full-text candidate PDFs were searched or opened.
- `paper_sources.zip` was read-only. Original BibTeX values were left unchanged; observed values are kept in the register/evidence files and compared field by field. The original raw titles and DOI fields are in `existing_title` and `existing_doi`; the archive remains the authoritative source for all original fields.
- Values are transcribed as printed, with ASCII transliteration for diacritics where necessary. For source pages that print only the starting page, no end page is inferred. `matches_original` is strictly `yes` or `no` in the evidence CSV.
- Evidence `source_type` values are restricted to `publisher_page` and `catalogue_page` (both are in the allowed set). No Crossref access is claimed or used. R2 is assigned only where the abstract was read. No R3 is assigned.

## Verification-level totals

| Level | Count | Records |
| --- | ---: | --- |
| R0 | 5 | Duhamel1837; Danilovskaya1950; Jou2010; Scruby1990; BornKarman1912 |
| R1 | 3 | Coleman1963; MuellerRuggeri1998; Talbot1979 |
| R1-noDOI | 0 | None |
| R2 | 7 | Zener1937; Lifshitz2000; Lamb1917; AbateWhitt2006; deHoog1982; McNelly1970; Huberman2019 |
| R3 | 0 | None |
| **Total** | **15** | **15** |

R1-noDOI is zero because the pre-1990 records without DOI did not have an opened publisher/journal article page with the full required volume and pages. The AbeBooks listing for Born-Karman omits volume 13; the Duhamel and Danilovskaya pages are not article-level records.

## Records that could not be verified (R0)
- **Duhamel1837:** BnF opened a catalogue record for the serial, not the 1837 article; it prints no article byline or article citation and lists a historical title variant for cahiers 18-31. The Google Books page opened was Volume 22, Issues 38-39 (1861), not the target. The Mathdoc page returned not found, and the linked Gallica route did not fetch. Search-result locators were not used as evidence.
- **Danilovskaya1950:** the opened official Science Journals page confirms the journal title/ISSN, but not this article. Its opened issue archive lists 2019-2023 only; no article-level 1950 page or full byline was opened.
- **Jou2010:** Springer book bibliographic information lists David Jou and Georgy Lebon, while chapter contents list David Jou, Jose Casas-Vazquez, and Georgy Lebon. The original BibTeX lists three book authors. Both printed lists are preserved; authorship remains ambiguous, so R0 despite the ISBN/DOI and edition data.
- **Scruby1990:** WorldCat prints A. Hilger for the 1990 book; Routledge prints CRC Press for the 1990 first-edition hardback. The Routledge heading omits the colon used by WorldCat and by the description on the same publisher page. Both publisher/title observations and ISBN/page-count details are preserved; no value is silently selected.
- **BornKarman1912:** the opened AbeBooks seller catalogue lists the abbreviated authors, journal, 1912 date, and article pages 297-309, but not volume 13. WorldCat redirected to sign-in and HathiTrust blocked access. The record is partial and is not promoted to R1-noDOI.

## Field discrepancies retained
- APS pages for Zener1937, Lifshitz2000, and McNelly1970 print only the first page (230, 5600, and 100 respectively). Original BibTeX page ranges remain unchanged; their evidence rows mark the page-range comparison `no`, and no endpoint was inferred.
- Coleman1963 has a December issue date but no numeric issue number on the opened Springer page. The register leaves `issue` as `-` and the evidence records the date separately.
- Book ISBNs, editions, publishers, and extents are recorded in the evidence CSV and register notes because the batch-001 register header has no dedicated ISBN or publisher column.

## Deliverables and QA
- `paper_v2/arena_deliverables/P2a/reference_register_batch_003.csv` - 15 records.
- `paper_v2/arena_deliverables/P2a/reference_evidence_batch_003.csv` - 129 field-level observations.
- `paper_v2/arena_deliverables/P2a/reference_match_verify_batch_003.csv` - 15 comparisons.
- `paper_v2/arena_deliverables/P2a/reference_summary_batch_003.md` - this report.
- CSV header rows were loaded from the saved batch-001 header file at `/tmp/p2a_batch003_headers.txt`; output headers match those exact rows.
- A byte-level scan of all four files found zero non-ASCII bytes and zero disallowed control characters.
- Only the four requested batch-003 files were created. No manuscript, scripts, source files, PDFs, or `BLUEPRINT_v3.1.md` were changed. No LaTeX compilation was run.
- Batch 004 was not started; Brorson1987, Thomsen1986, Cahill2003, and Gulyaev1969 remain untouched.
- Base SHA recorded for this audit: `340328c5fc46bc80067c4d7638f6fd73c7bd6257` on `origin/review-paper-v2`.
