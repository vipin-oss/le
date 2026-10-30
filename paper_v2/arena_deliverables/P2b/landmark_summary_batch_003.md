# Landmark literature register - batch 003

## Scope and status

This is a Topic 5-only batch on parameter identification and experimental evidence for non-Fourier, second-sound, and thermal-wave models. It contains ten R2-verified records: Dreyer and Struchtrup (1993), Mitra et al. (1995), Roetzel et al. (2003), Scott et al. (2009), Liu et al. (2016), Forghani and Hadjiconstantinou (2019), Huberman et al. (2019), Beardo et al. (2021), Ding et al. (2022), and Zenji et al. (2024). The selection combines a critical review, primary experiments (including a reported null result), and inverse/reconstruction studies. The `source_type` field labels each record. Batch 004 was not started.

## Verification counts

- Register rows: 10; Topic 5: 10.
- R2: 10; R1: 0; R1-noDOI: 0; R0 register rows: 0; R3 claims: 0.
- Abstracts inspected: 10. All `primary_contribution` statements are paraphrases limited to the abstract; no model prediction is reported as an experimental result. Numerical temperature, time, or frequency detail is used only where the abstract states it; otherwise the register uses `-`.
- Full text accessible in checked sources: 5 (Forghani and Hadjiconstantinou 2019, Huberman et al. 2019, Beardo et al. 2021, Ding et al. 2022, and Zenji et al. 2024). Other entries are based on opened publisher metadata and abstracts/previews; no full-text-only contribution claims were added.
- Independence: `independent_by_authors` 10; `own_group` 0; `unknown` 0. Every listed author, including coauthors, was compared by name with Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar, and Rachaita Dutta. No exact name match was found and no institutional inference was made. S. Kumar was not conflated with Rajesh Kumar; Sarit K. Das was not conflated with Soumik Das.

## Duplicate and BibTeX accounting

The read-only duplicate audit covered `refs.bib`, `refs_extra.bib`, and `refs_new.bib` in `paper_v2/paper_sources.zip`, plus `refs_landmark_batch_001.bib` and `refs_landmark_batch_002.bib`. Counts were 150, 34, 141, 7, and 9 entries, respectively. Both DOI and normalized-title matching were applied.

- Mitra et al. 1995 is a normalized-title duplicate of `refs_extra.bib::Mitra1995`; the existing record has no DOI. Huberman et al. 2019 is a normalized-title duplicate of `refs_extra.bib::Huberman2019`; the existing record has no DOI. Both papers remain in the register and evidence files but are omitted from the new BibTeX file.
- The other eight records have no DOI or normalized-title match in the five audited bibliographies.
- `refs_landmark_batch_003.bib` contains those eight verified nonduplicates, with eight unique `LM3_` keys and eight unique DOI values. No duplicate DOI is present.

## Source and citation-chain notes

Publisher or library pages were opened for every paper. Sources include Springer (Dreyer and Struchtrup), ASME (Mitra; Scott), ScienceDirect (Roetzel; Liu), MIT DSpace and the AIP-published PDF (Forghani and Hadjiconstantinou), Science and MIT DSpace (Huberman), Science Advances (Beardo), Nature Communications (Ding), and Communications Materials (Zenji). The respective abstracts and publication metadata were checked. Publisher PDFs/library versions verified full bylines for the accessible full-text papers.

The Scott 2009 ASME reference list cites a separate 1999 proceedings item with the same title; only the directly verified 2009 journal article is registered here. The Ding 2022 Nature Communications reference list cites Huberman et al. 2019; the Huberman article was independently verified through Science and MIT DSpace and is retained only in the register because it duplicates an existing bibliography title. Reference-list links support citation-chain context only; they do not substitute for direct verification of target records.

## Access tests and limits

Publisher and library pages exposed metadata and abstracts for all ten entries. The Springer, ASME, and ScienceDirect pages for the paywalled records expose abstracts or previews rather than full article text; no full-text-only assertions are made for those records. Full-text PDFs or accepted versions were accessible for the five papers listed above. Search results were treated as discovery leads only. No Crossref access is claimed.

This is a literature-register and source-verification batch only. No `main.tex` citation sentences, manuscript-novelty claims, or LaTeX compilation are included. No existing `.tex`, `.bib`, script, PDF, or Blueprint file was modified. Only the five requested batch_003 deliverables were created; the pre-existing untracked `google_drive/` directory was not staged.

## QA record

- The three CSV headers were copied from `/tmp/p2b_batch003_headers.txt` and used verbatim.
- CSV parsing: 10 register rows, 17 evidence rows, and 10 match/verify rows; every row matches the copied header field count.
- ASCII-only and disallowed-control-character scans: passed for all five batch_003 files.
- BibTeX sanity validation: 8 article entries, 8 unique `LM3_` keys, 8 unique DOI values, required author/title/journal/year/DOI fields present, balanced braces and quotes.
- Branch: `arena/06654118-le` (active and fixed). Pre-batch HEAD: `7bb32f9520e0b0469a9fa6b1f4c5ae06afcba83e`. Merge-base with `origin/main`: `fad98f923e76563e3fe4e8852d85cd68fc7c6fc5`.
