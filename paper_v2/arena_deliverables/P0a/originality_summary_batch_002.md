# P0-a - Prior Literature Originality Matrix, Batch 002

## Scope and handling
- Searched Google Drive for `RP5` (`name contains 'RP5'`). The search returned one item: `RP_5.zip`, a ZIP file, not a folder (Drive file ID `1b1_C6s4xbp_1B1TZkIpbwx6HL4CCoH3K`; MIME type `application/x-zip-compressed`; modified `2026-10-30T12:49:02.101Z`). Its Drive size is 13,984,955 bytes. The local archive copy has the same SHA-256 checksum as Drive: `19a8ce8ef0854933daf8ecb678123a34c66358c9082e1ffd8e81e4ca16caa529`.
- The ZIP has exactly five file entries and no directory entries:

| Archive member | Uncompressed size |
|---|---:|
| `jcde%2Fqwaa082 (1).pdf` | 8,956,677 bytes |
| `1-s2.0-S1290072925006994-main.pdf` | 3,890,093 bytes |
| `j.apm.2016.01.010.pdf` | 1,284,045 bytes |
| `1-s2.0-S0735193320302505-main.pdf` | 2,070,736 bytes |
| `RevModPhys.61.41.pdf` | 1,899,497 bytes |

- The local archive checksum also matches the Drive MD5 checksum. The PDFs were extracted read-only to `/tmp/rp5_pdfs/`; neither the Drive archive nor batch 001 was changed.
- Target PDFs were matched by their printed first-page title and author information, with the printed DOI checked where present. Archive names are retained only for provenance. Four PDFs print the requested DOI on the first page. The Joseph and Preziosi PDF does not print a DOI on page 41; its matrix DOI is `-`, and this caveat is recorded in match verification.
- Only new `_batch_002` deliverables were created. No manuscript, bibliography, source PDF, or blueprint was edited. Batch 003 was not started.

## Matched records and reading coverage
- `P0A001` - Shakeriaski et al. (2021), `jcde%2Fqwaa082 (1).pdf`. First-page title, authors, journal, year, page range, and DOI match. Read the abstract (p. 15), the theory/model survey and selected cited applications/results (selected pages in pp. 16-27), and the conclusion (pp. 28-30); the whole review was not read end-to-end.
- `P0A002` - Azhdari et al. (2026), `1-s2.0-S1290072925006994-main.pdf`. First-page title, all seven authors, journal, year, article number, and DOI match. Visually checked the abstract page; read CV/SPL, DPL, and TPL descriptions, printed pp. 2-5, reviewed experiment material, pp. 13-17, and synthesis/conclusion, pp. 16-18. The review's summarized experiments are distinguished from new measurements by the review authors.
- `P0A003` - El-Karamany and Ezzat (2016), `j.apm.2016.01.010.pdf`. The accepted-manuscript cover prints the matching title, authors, and DOI; the title has minor spacing/capitalization differences. Read the abstract, constitutive/model sections, explicit thermodynamic restrictions, numerical application/results, and conclusions. The Lord-Shulman second-law caveat is retained rather than flattened into the general entropy-production discussion.
- `P0A004` - Zenkour and El-Mekawy (2020), `1-s2.0-S0735193320302505-main.pdf`. First-page title, authors, journal, year, article number, and DOI match. Visually checked the first page; read the lag-law derivation, special cases, photothermal beam example/results, theory comparisons, and conclusion. The authors' term validation example is not treated as experimental validation: the checked results are model-to-model plots, with no measured reference identified.
- `P0A006` - Joseph and Preziosi (1989), `RevModPhys.61.41.pdf`. The printed title, both authors, journal, year, volume, issue, and page 41 match. Read the abstract, Sections I-VII (printed pp. 41-51), the opening/overview of Section VIII on p. 51, and the Section IX conclusion on p. 70. The chronology on pp. 52-69 was not read exhaustively. The reviewed historical experiments are not presented as new experiments by these authors.

## Verification counts
| Level | Count | Meaning in this batch |
|---|---:|---|
| R0 | 0 | No matching target PDF was verified. |
| R1 | 0 | No metadata-only records. |
| R2 | 0 | No abstract-only records. |
| R3 | 5 | Full-text evidence was checked on cited pages; this does not mean each entire article was read end-to-end. |
| Total | 5 | The five requested target records. |

No target PDF is absent from the Drive ZIP. All five target records are R3; there are no R0 records in this batch.

## Unresolved items and cautions
- `P0A006`: DOI `10.1103/revmodphys.61.41` is not printed on page 41. The record is matched by the printed title, authors, journal, year, volume, issue, and page; the matrix DOI remains `-` rather than asserting first-page DOI verification.
- `P0A002`: the abstract and conclusion report a near-zero-to-32-second range, while Section 3 also cites values as high as 500-600 without repeating the unit in that sentence. Both statements are preserved; the discrepancy is not reconciled.
- `P0A006`: the chronology section, printed pp. 52-69, remains unread end-to-end. Some extracted text-layer glyphs are imperfect; only legible prose was used, and unclear equations/symbols were not reconstructed.
- `P0A003`: some equation glyphs in the accepted-manuscript text layer are poorly mapped. The matrix records only clearly legible verbal conditions and restrictions; unclear symbols were not reconstructed.
- Unconfirmed fields remain `-` in the matrix, including general thermodynamic restrictions and/or benchmarks where the checked paper did not establish them, and direct experimental evidence where no experiment was reported. The Zenkour beam comparison is explicitly distinguished from measured experimental validation.
- No manuscript novelty or originality claim is made.

## Evidence and output controls
- The three CSV headers exactly match the batch-001 headers copied to `/tmp/p0a_batch001_headers.txt` and read back before deliverable creation.
- Every non-`-` matrix field has a page-specific evidence row. The evidence CSV distinguishes printed journal pages from one-based PDF page indices; source excerpts are at most 25 words and interpretations are written in my own words.
- ASCII/control-character scan: passed for all three CSVs and this summary; no non-ASCII bytes or disallowed control characters were found.
- Output paths:
  - `paper_v2/arena_deliverables/P0a/originality_matrix_batch_002.csv`
  - `paper_v2/arena_deliverables/P0a/originality_evidence_batch_002.csv`
  - `paper_v2/arena_deliverables/P0a/originality_match_verify_batch_002.csv`
  - `paper_v2/arena_deliverables/P0a/originality_summary_batch_002.md`

## Repository provenance
- Branch: `arena/06654118-le`
- Base SHA: `fad98f923e76563e3fe4e8852d85cd68fc7c6fc5`
- The final commit SHA is reported in the completion message.
