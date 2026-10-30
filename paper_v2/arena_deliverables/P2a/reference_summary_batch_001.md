# P2-a Reference Metadata and Evidence Audit - Batch 001

## Scope and handling
- Audited the first 15 entries in `refs_new.bib` whose author fields are truncated (`and others`), in source order, using `paper_v2/paper_sources.zip` read-only.
- Drive searches were used as locators. A matching primary PDF was opened for every record; title and DOI identity were checked against its first page, and the full author list and printed metadata were transcribed from that page.
- Original BibTeX author, title, journal, year, and DOI values are recorded separately in the evidence CSV. The register contains observed PDF values; unknown or unprinted values are `-`. Differences are retained and described rather than silently corrected.
- Pre-existing BibTeX note text about prior author-library page checks was not used as evidence. No publisher page was opened, no Crossref source was accessed, and no Crossref access is claimed.
- Abstract blocks were inspected on the opened first pages. R2 is assigned only where the first-page citation metadata was complete; a visible abstract did not raise incomplete records above R0.
- No manuscript, `.tex`, `.bib`, script, PDF, or blueprint file was edited. No LaTeX compilation was run.

## Verification counts
| Level | Count | Meaning in this batch |
|---|---:|---|
| R0 | 8 | Matching PDFs were opened, but first-page publication metadata needed for a complete citation was missing or ambiguous. |
| R1 | 0 | No records at R1; every complete-metadata record also had its abstract inspected and is R2. |
| R2 | 7 | DOI and citation metadata verified on the opened PDF first page, with the abstract inspected. |
| R3 | 0 | Not assigned. |
| Total | 15 | All selected first-15 truncated-author records. |

All 15 selected records have a title- and DOI-matching PDF in Drive; none is marked `no PDF in Drive`. The eight R0 records are Pathania2023, Gupta2024b, Barak2023a, Gupta2023a, Gupta2023b, Gupta2023c, Guha2025, and Gupta2025a. Their first pages omit or do not unambiguously state one or more of volume, issue, pages, or publication year; these fields remain `-` rather than being inferred. The seven R2 records are Pathania2022, Dutta2024, Gupta2024c, Das2024, Pathania2024, Das2025, and Gupta2026.

For Dutta2024, Gupta2024c, Das2024, Pathania2024, Das2025, and Gupta2026, the first-page citation presents an article identifier rather than a page range; that printed identifier is placed in `pages` and clarified in the notes. Issue numbers not printed on page 1 are `-`.

## Duplicate candidates
Five records have duplicate candidate files flagged, with 11 additional Drive files in total: Gupta2024b (one byte-identical copy), Barak2023a (one byte-identical copy), Gupta2023b (five byte-identical copies and one compressed variant), Pathania2024 (two byte-identical copies), and Gupta2023c (one byte-identical copy). Duplicate candidates were not deleted. Equal MD5 values are noted as byte-identity evidence; the compressed Gupta2023b variant was opened and its first-page title and DOI matched. Other related-title search results were not treated as duplicate papers.

Vipin Gupta appears in the first-page author list for all 15 records; the register notes flag these as the author's own group. Author lists are transcribed from opened first pages and never use `et al.` as a full list. Output is ASCII-only; non-ASCII dash glyphs in a few titles are represented by ASCII hyphens and noted. No diacritic removal was needed based on the extracted first-page text.

## Deliverables
- `reference_register_batch_001.csv`
- `reference_evidence_batch_001.csv`
- `reference_match_verify_batch_001.csv`
- `reference_summary_batch_001.md`

Batch 002 remains deferred pending author review.
