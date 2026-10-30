# P2-a batch 006 verification summary

## Scope and source handling

This batch covers the 11 remaining `and others` records and four selected one-name author-field records, for 15 total. Records are in `refs_new.bib` source order. The read-only `paper_v2/paper_sources.zip!refs_new.bib` archive supplied the original values and line ranges. The three CSV headers were copied verbatim from `/tmp/p2a_batch006_headers.txt`; no CSV columns were added, removed, or reordered.

Each matching Drive PDF was opened and its first page checked for title, byline, citation details, and DOI; the abstract block was inspected. Publisher pages/citation exports supplied final citation fields absent from PDF first pages and completed the selected no-PDF records. Search results and filenames were used only as leads. No Crossref access is claimed or used. Original BibTeX values and observed values remain separate; every observed field has `matches_original` set to `yes` or `no`. Full bylines are transcribed without `et al.`; article identifiers are stored in the `pages` field and called out as identifiers. Unprinted issues remain `-` and are not inferred.

## Selection

All 11 mandatory `and others` keys were included: `Raja2004`, `Szekeres2012`, `AboDahab2020`, `Zhang2021`, `Ma2020`, `Guo2018`, `Li2021`, `Mondal2020`, `Gao2007`, `Lim2015`, and `Ke2014`.

The four selected one-name keys are `Sherief1993`, `Quintanilla2018`, `Abouelregal2019`, and `Youssef2010`. A title/DOI-matching Drive PDF was confirmed for `Abouelregal2019`; no matching PDF was confirmed for the other three, so the publisher-page fallback was used. No batch 007 work was started. Thirty-four one-name candidates remain after this batch.

## Verification outcomes

| Level | Count | Meaning in this batch |
| --- | ---: | --- |
| R0 | 0 | No unresolved wrong-paper or incomplete-metadata records. |
| R1 | 1 | `Sherief1993`: complete publisher citation metadata, but no matching PDF and no accessible abstract on the opened Taylor & Francis page. |
| R2 | 14 | Complete DOI/citation metadata plus an inspected abstract, from a matching PDF or an opened publisher article page. |
| R3 | 0 | Not assigned. |
| **Total** | **15** | **15 selected records** |

Three selected records have no confirmed matching Drive PDF: `Sherief1993`, `Quintanilla2018`, and `Youssef2010`. For `Quintanilla2018`, the opened `quintanilla2019.pdf` has a different first-page title, Moore-Gibson-Thompson thermoelasticity, and DOI 10.1177/1081286519862007; it is not a match. For `Youssef2010`, representative DOI-hit files opened were a Turnitin similarity report and a different Biswas 2019 paper; neither was treated as the cited work. For `Sherief1993`, the targeted Drive DOI query returned no matching PDF. Their publisher metadata is retained separately from original BibTeX values.

## Citation-year and metadata differences

- `Ma2020`: the PDF says published online 1 Dec 2020, matching the original online-first year. The final Taylor & Francis citation is 2023, volume 51, issue 2, pages 682-705; the register uses 2023.
- `Mondal2020`: the exact first-page title is `Memory dependent derivative effect on generalized piezo-thermoelastic medium under three theories`; the exact first-page DOI is `10.1080/17455030.2020.1730480`. Both match the original BibTeX. The PDF says published online 27 Feb 2020; the final Taylor & Francis citation is 2021, volume 31, issue 6, pages 2150-2167; the register uses 2021.
- `Ke2014`: the exact first-page title is `Thermo-electro-mechanical vibration of size-dependent piezoelectric cylindrical nanoshells under various boundary conditions`; the exact first-page DOI is `10.1016/j.compstruct.2014.05.048`. Both match the original BibTeX. The PDF citation is Composite Structures 116 (2014), pages 626-636.
- `Abouelregal2019`: the PDF first page gives received/accepted dates in 2019 and the Springer article page gives online publication on 27 Nov 2019. The final Springer citation is 2020, volume 94, issue 12, pages 1949-1963; the register uses 2020.
- `Guo2018`: the PDF final citation is 2018, volume 41, issues 10-12, pages 1538-1557; the separate online date is 12 Feb 2019.
- Article identifiers are explicitly noted for `AboDahab2020` (103270), `Zhang2021` (101211), and `Youssef2010` (061301). `Gao2007` issue 22-23 is confirmed by ScienceDirect; `Quintanilla2018` issue 14 by Springer citation export; `Sherief1993` issue 2 by Taylor & Francis citation export.

## Name spelling and own-group check

Every printed author was compared with Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar, and Rachaita Dutta. All 15 own-group flags are `no`. No author spelling discrepancy remains unresolved. In the Abo-Dahab PDF extraction, the trailing `a` after Abo-Dahab is a superscript affiliation marker; it is not part of the surname. Sage publisher text confirms `D. Dwarakanathan` for Raja2004 where the PDF extraction inserts spaces. Names are ASCII as printed; no diacritics needed removal.

## Duplicate candidates

No Drive PDFs were changed or deleted. Byte-identical copies were noted by MD5, and all candidate copies remain untouched.

- `Raja2004`: IDs `167ChHNDHChn9ieBw-NLnzyWURb62A3Uo` and `1ltq2jR0bueqe7VEJ0LVsu1Q147wfSt6w`; MD5 `9e372bab12220703b6d2c6c6f4b008b1`.
- `Szekeres2012`: IDs `1OYLJT41qrkYOvvdAiH2X2D2CbkoqjEio` and `1B-OxH0uAxHRUxggQlxwR0pCmsok0P1Rg`; MD5 `7b119a88cb3310daf13a6247079641b7`.
- `AboDahab2020`: IDs `1DPpJyz715AwYhEjMbv6iTBwzrZ0_4z2z` and `1Bk2qPbV7JBMiZutV8GWharz-4q6j2C-P`; MD5 `d8626167bb10383bdd4356352e8af25e`.
- `Zhang2021`: IDs `1nRRtjEXMhpgI9cYrWxvuoLiWhgj2tEIw` and `1zSQFC3dqISikIzMSJTqc2G80h1a07vAC`; MD5 `258e8ceb9fe5de5f94ead1641a8fe60c`.
- `Ma2020`: IDs `1Rl3JmWNNgDFAcVANtfG8U_Qc6uht4Y5n` and `1sdbAXIEXHFkySGx7AUYzP7YNyRyqHz1E`; MD5 `258b548c490732d08fa750460f899975`.
- `Guo2018`: two first-page-matching PDF versions with different MD5s; each version has a byte-identical copy. Version 1 IDs `1oY6hKUlgeDbpYnxwqbP6shlL1gFsPRUT` and `1ilj62LIhj6PoheFHM8O2s5pxLtJ30r9D`, MD5 `e572f7e4d94ab42e9e9a5042fae44e01`. Version 2 IDs `1c9HDTsM0IXFVmw0e3aiz0b7kA075wgqX` and `1QrFs5CnAFa20BYB9DBdiwuGQsCINZG_r`, MD5 `645dae87ab523906a1c7e1c2704250f2`.
- `Li2021`: IDs `1a7eHpTwrKfs6V6qfBj2OXIN8mJ3E71RW` and `1j_SuJmobkGDgz6udXhZHjy1DavkeHbHF`; MD5 `347383b2896a359cb3f0c234e0126d79`.
- `Mondal2020`: three copies share MD5 `e0c8a014f94e5a813d6c9a7358f33396`: IDs `1jUPO4a3fIYl-DG1Q98Fo7ywQ3wHSu6mA`, `1o4E_3ekpesdmfrP-HaWUBrZmlNnedsbn`, and `1xB_moKC1URj4qQGIrKMAuHEwvh4JW2HO`.
- `Gao2007`: IDs `1hofDUMsVueGsidKIExzg0-ZOWh7dwH7U` and `1X-8F98zTHYHbLRou6czCwNB9DCmV5mcY`; MD5 `886774274c67222decc8b94086c9e3cc`.
- `Lim2015`: IDs `1nQsYKzgkmsw-XhJCtYDBGS6zJe_y-SoB` and `1bQvUJcbV9LQ6i07JUKVLZXXmDpe4wkIz`; MD5 `56e8bbde542a03ff0e223315ff71aa32`.
- `Ke2014`: IDs `1OT2KXmmBC0PphRdRbJmOAeFhGdCTbUeQ` and `1Gi1d30U-X_o450qUzRbUKFMRBieY-szn`; MD5 `8fd0dd4a7b6aab59bd89219d6c78f490`.

## Remaining candidates

The 34 remaining one-name author-field candidates are `Ignaczak1985`, `Ignaczak1982`, `Bem1982`, `Scott2007`, `McCarthy1972`, `Sherief1992`, `Sherief1993a`, `Ignaczak1981`, `Bem1983`, `Ezzat2004`, `Hosseini2017`, `Quintanilla2002`, `Quintanilla2002a`, `Chandrasekharaiah1997`, `Ciarletta1999`, `Iesan1998`, `Youssef2011`, `Quintanilla1999`, `Quintanilla2002b`, `Rukolaine2014`, `Antaki2000`, `Quintanilla2008`, `Quintanilla2009`, `Chirita2017`, `Youssef2012`, `Shaw2019`, `Quintanilla2020`, `Biswas2020b`, `Chirita2012`, `Singh2020e`, `Biswas2020c`, `Abouelregal2011`, `Singh2013`, and `Singh2015`. No batch 007 work was started.

## Deliverables and QA

Created only these four batch 006 files under `paper_v2/arena_deliverables/P2a/`:

- `reference_register_batch_006.csv` - 15 verified citation records.
- `reference_evidence_batch_006.csv` - 221 evidence rows (82 original BibTeX field rows, 97 Drive PDF observations, and 42 publisher-page observations), with explicit matches to original values.
- `reference_match_verify_batch_006.csv` - 15 title/DOI/byline/duplicate/verification checks.
- `reference_summary_batch_006.md` - this summary.

The three CSV headers were checked byte-for-byte against `/tmp/p2a_batch006_headers.txt`. All four deliverables are ASCII; CSV row/key counts were validated. No sources, manuscript files, or earlier batches were modified. The pre-batch base was `29eed883084d10862dabf4f76e4989aec46dca20` on the fixed branch `arena/06654118-le`. The pre-existing `google_drive/` directory remains unstaged. No LaTeX compilation was attempted or claimed.
