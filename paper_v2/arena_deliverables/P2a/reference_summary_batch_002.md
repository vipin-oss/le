# P2-a Reference Metadata and Evidence Audit - Batch 002

## Scope and handling
- Read `refs_extra.bib` from `paper_v2/paper_sources.zip` in read-only mode. The archive contains 34 records; none has a DOI field.
- Selected 15 records in source order for which a Drive PDF candidate was opened. The candidates are not treated as the cited works unless the first-page identity matches. All 15 opened candidate first pages are inconsistent with their BibTeX entry; no primary PDF for a selected reference was confirmed.
- The register reports observed candidate-page metadata only. It does not replace or correct the original BibTeX values, which are preserved in the evidence CSV. Candidate DOIs belong to the unrelated candidate papers, not to the BibTeX references.
- Unknown or unprinted candidate fields are `-`. No author list is completed from filename or citation context; `et al.` is not used as a full author list. `possible wrong paper / wrong metadata` is recorded for every R0 candidate.
- Full-text search results that only cited a target reference were not treated as verified copies. The `no PDF in Drive` list below means no matching primary/reference PDF was verified in Drive after targeted name and full-text searches; it does not mean Drive contains no incidental citing papers.
- No publisher page was used. No Crossref access is claimed. Abstract text from an unrelated candidate was not used to raise a record above R0. No manuscript, `.tex`, `.bib`, script, PDF, or blueprint file was changed. No LaTeX compilation was run.

## Verification counts
| Level | Count | Meaning in this batch |
|---|---:|---|
| R0 | 15 | An opened Drive candidate did not match the reference title/DOI; the reference remains unverified. |
| R1 | 0 | No matching source PDF or publisher page verified complete metadata. |
| R2 | 0 | No matching source PDF with an inspected abstract. |
| R3 | 0 | Not assigned. |
| Total | 15 | Candidate-backed records selected from `refs_extra.bib`. |

No exact target PDF was confirmed for any of the 15 selected records. R0 is assigned because each candidate first-page identity fails, even where the unrelated PDF prints a DOI or complete citation metadata.

## Ambiguous or incomplete candidate observations
- `Chadwick1960`: the opened first page identifies a different paper; publication year, journal, volume, issue, page range, and DOI are not reliably printed in the extracted first-page text.
- `Ackerman1966`: the unrelated candidate prints page 355 only; no page-range endpoint or DOI is printed on page 1.
- `Boley1960`: the opened PDF starts with a contents/chapter page and does not print a bibliographic title or author line.
- `Pennes1948`: the unrelated candidate prints a DOI and title, but volume, issue, and pages are not printed on the inspected first page.
- `Cohen2007`: first-page extraction is OCR-garbled; candidate title, complete author list, year, journal, volume, pages, and DOI remain `-` rather than being reconstructed from the filename.
- `Podlubny1999`: the candidate is a different chapter; only its opening page number is visible, so no page-range endpoint is inferred.

All 15 rows retain R0; these incomplete fields do not turn a wrong-paper candidate into a verified source.

## Duplicate candidates
- No duplicate copy of a target reference was confirmed, and no Drive file was deleted.
- `B05-016__Megahid, Abouelregal, Sedighi - 2023 - Modified.pdf` was a shared unrelated full-text hit for `Pennes1948` and `Brorson1987`.
- `B02-018__P53_2026_AMM-Engl_Effect-Phason-Transport-Lord-Shulman-Surface-Waves-Hexagonal-Quasicrystal.pdf` was a shared unrelated full-text hit for `Bleustein1968` and `Gulyaev1969`.
- For `Podlubny1999`, `gorenflo1997.pdf` and `gorenflo2014.pdf` are distinct works, not duplicate copies. Other Rayleigh/Cohen search hits were also distinct nonmatching papers.

## No PDF in Drive
The following 19 references have no matching primary/reference PDF verified in Drive; citation-bearing or otherwise unrelated results were not counted as source PDFs:
- `Duhamel1837` - no PDF in Drive
- `Danilovskaya1950` - no PDF in Drive
- `Zener1937` - no PDF in Drive
- `Lifshitz2000` - no PDF in Drive
- `Lamb1917` - no PDF in Drive
- `Coleman1963` - no PDF in Drive
- `MuellerRuggeri1998` - no PDF in Drive
- `Jou2010` - no PDF in Drive
- `Talbot1979` - no PDF in Drive
- `AbateWhitt2006` - no PDF in Drive
- `Scruby1990` - no PDF in Drive
- `BornKarman1912` - no PDF in Drive
- `deHoog1982` - no PDF in Drive
- `McNelly1970` - no PDF in Drive
- `Huberman2019` - no PDF in Drive
- `Brorson1987` - no PDF in Drive
- `Thomsen1986` - no PDF in Drive
- `Cahill2003` - no PDF in Drive
- `Gulyaev1969` - no PDF in Drive

## Own-group check
The original BibTeX author fields for the 15 selected records do not list Vipin Gupta. The unrelated `Bleustein1968` candidate PDF does list Vipin Gupta and is explicitly flagged as own group in the register; this does not make it a match for the Bleustein reference. Candidate author status is marked unknown where the inspected first page has no reliable byline.

## Deliverables and stop point
- `reference_register_batch_002.csv`
- `reference_evidence_batch_002.csv`
- `reference_match_verify_batch_002.csv`
- `reference_summary_batch_002.md`

Batch 002 is complete. Stop before batch 003.
