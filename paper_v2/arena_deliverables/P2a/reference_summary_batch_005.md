# P2-a batch 005 verification summary

## Scope and source handling

This batch covers only the 15 selected `refs_new.bib` records below. The read-only `paper_v2/paper_sources.zip!refs_new.bib` archive was used to extract original values and source line ranges. Each selected Google Drive PDF was opened and its first page was inspected for the title, byline, citation details, and DOI; the abstract was also inspected. Publisher pages/citation exports were opened where the PDF did not supply final citation metadata. Filenames and search results were not used as stand-alone evidence. No Crossref source or claim is used.

Original BibTeX values and observed values remain separate in the evidence CSV. Every observed field has an explicit `matches_original` value of `yes` or `no`. Full printed author lists are retained, including initials as printed; no `et al.` list is used as a full author list. Article identifiers are entered in the `pages` field and noted as article identifiers, not page ranges. An issue is shown as `-` only where no issue was printed or available in the opened citation source; none was inferred.

## Candidate census

`refs_new.bib` contains 141 entries. The candidate rule identified 79 author fields: 41 containing `and others` and 38 containing only one name. These are raw author-field candidates; a one-name field was not assumed to prove that the publication itself has one author. All 79 candidates have a DOI.

Already covered in batch 001 (15 keys):

`Pathania2022`, `Pathania2023`, `Dutta2024`, `Gupta2024b`, `Barak2023a`, `Gupta2023a`, `Gupta2023b`, `Gupta2024c`, `Das2024`, `Pathania2024`, `Gupta2023c`, `Guha2025`, `Das2025`, `Gupta2026`, `Gupta2025a`.

Remaining after batch 001 and before batch 005: 64 keys, grouped by raw author-field pattern.

- 38 one-name fields: `Ignaczak1985`, `Ignaczak1982`, `Bem1982`, `Sherief1993`, `Scott2007`, `McCarthy1972`, `Sherief1992`, `Sherief1993a`, `Ignaczak1981`, `Bem1983`, `Ezzat2004`, `Quintanilla2018`, `Hosseini2017`, `Quintanilla2002`, `Quintanilla2002a`, `Chandrasekharaiah1997`, `Ciarletta1999`, `Iesan1998`, `Youssef2011`, `Quintanilla1999`, `Quintanilla2002b`, `Rukolaine2014`, `Antaki2000`, `Quintanilla2008`, `Quintanilla2009`, `Abouelregal2019`, `Chirita2017`, `Youssef2010`, `Youssef2012`, `Shaw2019`, `Quintanilla2020`, `Biswas2020b`, `Chirita2012`, `Singh2020e`, `Biswas2020c`, `Abouelregal2011`, `Singh2013`, `Singh2015`.
- 26 `and others` fields: `Kumar2025a`, `Seema2024`, `Meghana2025`, `Meghana2026`, `Gupta2026a`, `Sur2026`, `Meghana2026a`, `Das2025a`, `Aldandani2026a`, `Meghana2025a`, `Guha2026`, `Vinyas2017`, `Yadav2022`, `Zhao2018`, `Chen2004`, `Raja2004`, `Szekeres2012`, `AboDahab2020`, `Zhang2021`, `Ma2020`, `Guo2018`, `Li2021`, `Mondal2020`, `Gao2007`, `Lim2015`, `Ke2014`.

## Batch 005 selection and remaining keys

Selected 15 DOI-bearing `and others` records in source order:

`Kumar2025a`, `Seema2024`, `Meghana2025`, `Meghana2026`, `Gupta2026a`, `Sur2026`, `Meghana2026a`, `Das2025a`, `Aldandani2026a`, `Meghana2025a`, `Guha2026`, `Vinyas2017`, `Yadav2022`, `Zhao2018`, `Chen2004`.

After batch 005, 49 candidates remain:

- 38 one-name fields: `Ignaczak1985`, `Ignaczak1982`, `Bem1982`, `Sherief1993`, `Scott2007`, `McCarthy1972`, `Sherief1992`, `Sherief1993a`, `Ignaczak1981`, `Bem1983`, `Ezzat2004`, `Quintanilla2018`, `Hosseini2017`, `Quintanilla2002`, `Quintanilla2002a`, `Chandrasekharaiah1997`, `Ciarletta1999`, `Iesan1998`, `Youssef2011`, `Quintanilla1999`, `Quintanilla2002b`, `Rukolaine2014`, `Antaki2000`, `Quintanilla2008`, `Quintanilla2009`, `Abouelregal2019`, `Chirita2017`, `Youssef2010`, `Youssef2012`, `Shaw2019`, `Quintanilla2020`, `Biswas2020b`, `Chirita2012`, `Singh2020e`, `Biswas2020c`, `Abouelregal2011`, `Singh2013`, `Singh2015`.
- 11 `and others` fields: `Raja2004`, `Szekeres2012`, `AboDahab2020`, `Zhang2021`, `Ma2020`, `Guo2018`, `Li2021`, `Mondal2020`, `Gao2007`, `Lim2015`, `Ke2014`.

No batch 006 work was started.

## Verification outcomes

- Opened and inspected first pages and abstracts for all 15 selected PDFs; the first-page title/byline/citation and DOI were used to identify each paper. All 15 had a matching PDF; no-PDF count: 0.
- Publisher sources supplemented final citation metadata for eight records: Kumar2025a, Meghana2026, Meghana2026a, Das2025a, Meghana2025a, Guha2026, Yadav2022, and Zhao2018. Sources used were Taylor & Francis citation exports, ScienceDirect article pages, the Nature article page, and the Springer article page, as listed in the evidence CSV.
- Verification levels: R2 = 15; R1 = 0; R0 = 0. DOI-bearing records all had abstract and citation metadata checked. Where an issue number was not shown, `-` is recorded rather than inferred.
- Original-year/online-year/final-citation differences are recorded rather than silently normalized: Seema2024 has a 2025 citation and a 10 Dec 2024 online publication date; Das2025a and Meghana2025a have 2025 online dates and 2026 final citation years; Yadav2022 has a 2022 online date and 2024 final citation year; Meghana2026a has an in-press PDF citing 2025 and a 2026 version-of-record citation; Guha2026 has a 2025 online date and 2026 final citation year.
- Two records require manual review: Meghana2026 (the BibTeX title is shorter/different from the title on the PDF and publisher page, although the DOI matches) and Meghana2026a (the PDF byline uses a c-cedilla in Yaylaci while the publisher contribution text does not; spelling check needed).
- Duplicate candidates: 3 records / 3 extra copies, all byte-identical by MD5; no Drive files were changed or deleted.
  - Kumar2025a: IDs `1zB4nJl6wZrAld9i8VXtQc6_0tvkvwtZM` and `1hbErIqUcp-VGX6L_THsI49Nn2LFnngEt`; MD5 `c6953b417f7066236d6b12ca372f0902`.
  - Das2025a: IDs `1Jds3ZONprw5_5OnVIv795x6A2tHpQQvr` and `13-y48vtkaaSl8CJZY49FRFIVD5nzkfHz`; MD5 `18baff6e121aa3e1a008289b38472d70`.
  - Guha2026: IDs `1ztj9FdnyVaZ3eMsJZ-eDsqkQY09yfRCC` and `1yTIdNTZi_UX1ZiDi021cxqzJXllgRqPF`; MD5 `0a70f4268f376979a502de65091877f9`.
- Own-group flag in register notes: yes for 11 records and no for 4, based on comparison with Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar, and Rachaita Dutta. Guha2026 is flagged yes only because the PDF pairs byline `V. Gupta` with the corresponding-author email whose local part is `vipin`; the initials are not expanded. Anand Kumar Yadav is not treated as Rajesh Kumar. No affiliation-only inference was used.
- ASCII author rendering: `Murat Yaylaci` is used for the PDF spelling with a diacritic in Meghana2026, Gupta2026a, Meghana2026a, and Aldandani2026a; the register/evidence notes say `diacritics removed`. The Meghana2026a spelling discrepancy is separately flagged for review.

## Deliverables and scope checks

Created only these four batch 005 files under `paper_v2/arena_deliverables/P2a/`:

- `reference_register_batch_005.csv` - 15 records.
- `reference_evidence_batch_005.csv` - 256 evidence rows (75 original BibTeX field rows, 120 PDF field rows, 61 publisher-page field rows).
- `reference_match_verify_batch_005.csv` - 15 records.
- `reference_summary_batch_005.md` - this summary.

The three CSV headers were copied verbatim from `/tmp/p2a_batch005_headers.txt` and validated byte-for-byte. All four deliverables passed an ASCII scan; CSV row counts and selected keys were validated. No source/manuscript files or earlier batch files were modified. The pre-batch HEAD/base SHA was `3fa5e5eb0a28f922b679dd3700af73eeb4503f20` on branch `arena/06654118-le`. No LaTeX compilation was attempted or claimed. The pre-existing `google_drive/` directory remains outside the batch deliverables and was not staged.
