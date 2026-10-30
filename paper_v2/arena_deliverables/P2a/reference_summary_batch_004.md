# P2-a Reference Metadata and Evidence Audit - Batch 004

## Scope and method
- Audited the specified 10 records in source order from `paper_v2/paper_sources.zip!refs_extra.bib`: Duhamel1837; Danilovskaya1950; Jou2010; Scruby1990; BornKarman1912; Brorson1987; Thomsen1986; Cahill2003; Bleustein1968; Gulyaev1969.
- External page access was tested first and succeeded at `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.16.789`. That page was only an access test and is not batch evidence.
- Searches by title and first author were used only to locate pages. Search snippets were not used as evidence; URLs in the evidence CSV were actually opened publisher, journal, or catalogue pages. No Drive candidate PDFs were searched or opened.
- The five batch-003 R0 records were retried with different source pages: Duhamel1837, Danilovskaya1950, Jou2010, Scruby1990, and BornKarman1912. Previously opened APS/AIP publisher observations for Brorson1987, Thomsen1986, Cahill2003, and Bleustein1968 were carried forward without repeating their searches; only in-scope records are included.
- `paper_sources.zip` was read-only. Original BibTeX title and DOI fields were extracted verbatim for `existing_title` and `existing_doi`; no BibTeX or source files were edited. Observed values are kept separately. Accented text is rendered in ASCII transliteration where needed.
- Evidence `source_type` values are restricted to `publisher_page` and `catalogue_page`. Metadata `matches_original` values are `yes` or `no`; abstract-inspection rows use `-` because an abstract is not a BibTeX metadata field. R2 is assigned only where a publisher abstract was read. No R3 is assigned.
- "Own group" means Vipin Gupta and co-authors; none of these ten cited works is treated as an own-group reference.

## Verification-level totals

| Level | Count | Records |
| --- | ---: | --- |
| R0 | 4 | Duhamel1837; Jou2010; Scruby1990; Gulyaev1969 |
| R1 | 0 | None |
| R1-noDOI | 2 | Danilovskaya1950; BornKarman1912 |
| R2 | 4 | Brorson1987; Thomsen1986; Cahill2003; Bleustein1968 |
| R3 | 0 | None |
| **Total** | **10** | **10** |

## Records remaining at R0
- **Duhamel1837:** an opened Springer publisher chapter's references print Duhamel JMC (1837), Tome 15, Cahier 25, pages 1-57. The official JEP history identifies cahiers 18-31 (1820-1847) as *Journal de l'Ecole royale polytechnique*, while the Springer citation uses *J de l'Ecole Polytechnique*; the BnF serial page also lists this historical title variant. Preserve the journal-title discrepancy and keep R0. The original 1837 issue page was not opened; the Google Books record was for Volume 22, Issues 38-39 (1861).
- **Jou2010:** Google Books lists David Jou, Georgy Lebon, and Jose Casas-Vazquez as book authors, while Springer book metadata lists David Jou and Georgy Lebon. Springer lists David Jou, Jose Casas-Vazquez, and Georgy Lebon for the target chapter, pages 199-231. Book-level and chapter-level lists are recorded separately; the book-level discrepancy is unresolved.
- **Scruby1990:** Google Books lists CRC Press and a title without a colon; WorldCat lists A. Hilger and a title with a colon; Routledge lists CRC Press but varies the title form within its page. ISBNs and extents are preserved, but the 1990 publisher/title observations are not silently selected.
- **Gulyaev1969:** the official JETP article page prints page 37, while the official volume-9 author index lists page 63. Neither is a *Radiotekhnika i Elektronika* article page, which remains unfound. Preserve the page disagreement; the printed author form is `Gulyaiev Yu. V.` (spelling check needed); keep R0.

## Field discrepancies retained
- **Danilovskaya1950:** the official PMM page prints the Russian title; the register stores an ASCII transliteration. The original BibTeX uses an English translation. The publisher page confirms the byline, year, volume 14, issue 3, pages 316-318, and no DOI; no abstract was read.
- **BornKarman1912:** the issue scan prints `No. 8`, `13. Jahrgang`, and 15 April 1912. The contents start the article at page 297; the page 309 scan was opened and the next article is listed at page 310. The full range 297-309 is supported by the issue scan; no endpoint is inferred from a first-page-only citation. No DOI is listed.
- **Brorson1987** and **Thomsen1986:** APS prints only starting pages 1962 and 4129, respectively. Original BibTeX ranges are preserved; no end page is inferred. Their abstracts were read, so both are R2.
- **Cahill2003** and **Bleustein1968:** the AIP pages print complete pages and DOI; both abstracts were read. AIP prints the Bleustein title in uppercase and the author's full name.
- Publisher DOI and issue fields absent from original BibTeX entries are retained as observed differences; no source BibTeX values were normalized.

## Deliverables and QA
- `paper_v2/arena_deliverables/P2a/reference_register_batch_004.csv` - 10 records.
- `paper_v2/arena_deliverables/P2a/reference_evidence_batch_004.csv` - 99 field-level observations.
- `paper_v2/arena_deliverables/P2a/reference_match_verify_batch_004.csv` - 10 comparisons.
- `paper_v2/arena_deliverables/P2a/reference_summary_batch_004.md` - this report.
- CSV headers were read from `/tmp/p2a_batch003_headers.txt` and match the exact batch-001 header rows.
- Only these four batch-004 deliverables were written. No manuscript, script, PDF, source archive, or `BLUEPRINT_v3.1.md` was changed. No LaTeX compilation was run. Batch 005 was not started.
- Base SHA: `340328c5fc46bc80067c4d7638f6fd73c7bd6257` on `origin/review-paper-v2`.
