# Claim checks, sections 16–36 — set B (Task 1)

Arena task: `HANDOFF_FOR_ARENA.md`, section 6, **Task 1** (claim checks for sections 16–36; batches 003/004/008 were not supplied, so nothing from them is used here).
Branch: `arena/9b458c54-le` (based on `review-paper-v2`). Date: 31 Oct 2026.
`main.tex` and every file under `sections/` are unchanged — this is evidence work only.

## 1. What was done

Every sentence in sections 16–36 of `main.tex` that cites a source for a technical statement was extracted and turned into one row per (statement, cited source). Result: **283 rows**, **116 sentences**, **184 distinct sources**, in **8 batches** of 31–36 rows.

| verdict | rows |
|---|---|
| SUPPORTED | 4 |
| PARTLY SUPPORTED | 1 |
| NOT SUPPORTED | 0 |
| SOURCE NOT AVAILABLE | 278 |
| **total** | **283** |

| found_in_library | rows |
|---|---|
| yes | 234 |
| no | 13 |
| not confirmed | 36 |

Rows per section: 16 (11), 18 (25), 22 (25), 23 (11), 24 (38), 25 (57), 26 (4), 27 (11), 28 (2), 29 (26), 30 (2), 32 (12), 33 (29), 34 (28), 36 (2).

## 2. Files

| file | content |
|---|---|
| `claim_check_B_batch_001.csv` … `claim_check_B_batch_008.csv` | the rows, in manuscript order, 31–36 rows each |
| `claim_check_B_index.csv` | per-batch row count, claim-id range, section range, verdict and library counts |
| `check_claim_check_B.py` | validator: schema, ids, allowed values, word limits, no URLs/ids, verdict/level consistency. Prints `PASS` lines, exit 0 |

The columns are exactly those asked for in Task 1:
`claim_id, manuscript_location, manuscript_statement, cited_source, source_doi, found_in_library, verdict, source_page_or_equation, source_wording_max25words, what_source_actually_states, verification_level, notes`.
`claim_id` values are `CB-0001` … `CB-0283`; they are new and do not collide with the `CRnnn` ids of `claim_register.csv`. The `_B_` in the file name marks set B (sections 16–36); it is independent of the earlier `claim_check_batch_NNN.csv` files, which covered sections 2–15.

## 3. Scope decisions

- **A "claim"** is a sentence, table cell or figure caption that attributes a technical statement to a cited source. Pure bibliographic listing is not a claim.
- **Appendix D (`appD_catalogue.tex`, 323 `\cite` commands)** is the classified catalogue: one line per reference. It is a bibliography, not a set of technical claims, so it yields no rows. It is flagged here rather than claim-checked; if the author wants it audited, it belongs to the reference register, not the claim register.
- **Appendices A, B, C, E, F, G, H contain no source-citing technical sentences** (checked by scanning the sources), so they contribute nothing.
- **Sections 17, 19, 20, 21, 31 and 35** contain no citation-bearing technical sentences either (their material is the author's own derivation or reporting standards). Their absence from the rows is therefore expected, not an omission.
- Figure captions of the form "Geometry after [X]" are included but are marked as attributions in `notes` where the claim is only the attribution.

## 4. Value glossary

- `verdict` — the four values fixed by the task. `SUPPORTED` is used **only** where the passage was actually read in this chat. Everything not read is `SOURCE NOT AVAILABLE`, which is the project convention for "not verified", **not** a finding against the claim.
- `verification_level` — R0 (nothing read), R1 (bibliographic record), R2 (abstract/first page read), R3 (relevant full-text passage read). 271 rows are R0 and 12 are R2.
- `found_in_library` — three values, deliberately:
  - `yes` — the source key is in the library source catalogue (`refs_catalogue_check.csv`, which records the library batch and level) or its index entry was read in this chat;
  - `no` — `verification_register.csv` records that no matching library PDF was found;
  - `not confirmed` — no evidence either way could be reached in this chat (36 rows, mostly the `refs_atlas.bib` classics: Agarwal1978, AbdAlla2001, Sharma2014, Collet2006, Love1911, Scholte1947, Stoneley1924, Barnett1985, Zhang2018a/b).
  A `not confirmed` is not a `no`. No library file name, folder name or Drive id is recorded anywhere in these files.

## 5. What was read in this chat (12 rows, R2)

Abstract-level checks, all of the author's group's interface/atlas papers:

| claim | source | verdict |
|---|---|---|
| CB-0275 | Barak2023JTS (J. Thermal Stresses) | SUPPORTED |
| CB-0276 | Barak2023MMMS (MMMS 19(3) 464) | SUPPORTED |
| CB-0277 | Gupta2023Energy (HFF) | SUPPORTED |
| CB-0280 | Kumar2025 (JIOS) | SUPPORTED |
| CB-0274 | Barak2023IJP (Indian J. Phys.) | PARTLY SUPPORTED — the topic is supported, "vital role" is the reviewer's wording |
| CB-0269 | Das2026 | SOURCE NOT AVAILABLE — abstract read, the quoted smoothing/weakening result is not in it |
| CB-0270 | Gupta2023 | SOURCE NOT AVAILABLE — abstract read, result beyond it |
| CB-0271 | Gupta2024 | SOURCE NOT AVAILABLE — abstract read, the frequency trend is not in it |
| CB-0272 | Gupta2024a | SOURCE NOT AVAILABLE — abstract read, the "highest energy" result is not in it |
| CB-0273 | Gupta2026HeatMap | SOURCE NOT AVAILABLE — abstract read, the TPL-peak comparison is not in it |
| CB-0278 | Kumar2024 | SOURCE NOT AVAILABLE — abstract read, the ERP/ERS relation is not in it |
| CB-0281 | Sur2025 | SOURCE NOT AVAILABLE — abstract read, the MGT-vs-GN-III comparison is not in it |

The last seven are *not* findings against the claims: the atlas entries report results-section statements and only the abstract was opened. They need the results pages.

## 6. How the other 271 rows were produced, and what they are worth

Mechanical, from repository data only:

- statement: the sentence (or table row / caption) as written, LaTeX resolved, mathematics replaced by `[math]`, truncated at 25 words with `[...]`;
- location: section, subsection, source file and **PDF page**;
- `cited_source` and `source_doi`: from `refs.bib`, `refs_extra.bib`, `refs_new.bib`, `refs_atlas.bib` in `paper_sources.zip`. No DOI is typed from memory; where the entry has none the field says `(absent)` (16 sources);
- `source_page_or_equation`: the page or equation the manuscript itself points to, when its `\citep[...]` carries one (5 rows: CB-0062 to CB-0066); in the 12 R2 rows the field also records where the abstract was read. These five pointers are the cheapest rows to verify.

These rows are an **audit list**, not a verification. They contain no verdict about the science.

## 7. Observations for the author (no `.tex` was edited)

1. `sections/s13_multiphysics.tex` cites **Ezzat2011 twice in one sentence**, and **Cowin1983 and Iesan1986 twice each in another sentence**. Duplicate `\cite` keys in one command print once, so this is cosmetic, but it usually means the sentence was merged.
2. `sections/s11b_layered.tex` repeats Rayleigh1885 three times and Stoneley1924 twice inside one table; that is legitimate (one row per table line), noted only so it is not read as a defect.
3. Several sentences carry exact page/equation pointers (`eq. (40), p. 162`, `eq. (23), p. 418`, `eq. (2.11), p. 156`, `pp. 422–423`, `p. 120`). Those five pointers are the strongest claim-level evidence in the manuscript, and they are still R0 here because the sources were not opened.
4. PDF page numbers equal the printed page numbers (footer checked, e.g. p. 50). Page numbers in `manuscript_location` are therefore the numbers a reader will see.
5. `[math]` in a statement stands for a formula; the original is in the `.tex`. Greek letters in table cells are transliterated to ASCII (β → b, ρ → r).

## 8. Suggested next verification targets

Highest value per row, in this order:

| claim | source | what to open |
|---|---|---|
| CB-0062 | Love1911 | eq. (40), p. 162 |
| CB-0064 | Stoneley1924 | eq. (23), p. 418; existence discussion pp. 422–423 |
| CB-0066 | Barnett1985 | eq. (2.11), p. 156 |
| CB-0068–CB-0070 | Rayleigh1885 | speeds 0.9554 / 0.9194 / 0.8741 (table) |
| CB-0071–CB-0072 | Stoneley1924 | 0.99287 and the "no real root" case |
| CB-0213, CB-0214, CB-0216, CB-0217 | Chester1963, GuyerKrumhansl1966, McNelly1970, Jackson1970 | the second-sound predictions and the NaF measurements |
| CB-0218 | Huberman2019 | second sound in graphite above 100 K |
| CB-0221 | Cahill2003 | TDTR method statement |
| CB-0187 | Lifshitz2000 | beam/plate thermoelastic damping |
| CB-0199, CB-0224 | Pennes1948 | bioheat equation |
| CB-0095 | Eringen1974 | nonlocal thermoelasticity |
| CB-0112 | MindlinTiersten1962 | piezoelectric stiffening |
| CB-0001 | Talbot1979 | numerical inversion |

## 9. Limits — what this deliverable does not claim

- It does not claim that any of the 278 unread claims is right or wrong.
- It does not claim completeness of the library: `not confirmed` rows may well be in the library.
- `manuscript_statement` is a mechanical extract; check the wording against `main.pdf` before quoting it anywhere.
- Section numbering follows the compiled `main.pdf` (Section 16 = "Transient problems", Section 34 = "Atlas of problems", Section 36 = "Open problems"), not the file names.

## 10. Reproduce

```
cd paper_v2/arena_deliverables/P3_evidence_claims_B
python3 check_claim_check_B.py     # prints PASS lines, exits 0
```

## 11. Merging into `claim_register.csv`

Add the 283 rows with `origin = claim_check_B_batch_NNN.csv`, keep `CB-nnnn` as `claim_id`, map `verdict` unchanged, `status` = `open: source not read` for `SOURCE NOT AVAILABLE`, `supported by source at stated level` for `SUPPORTED`, `partly: wording is the reviewer's` for `PARTLY SUPPORTED`. The 12 R2 rows already have their quoted source wording in `source_wording_max25words`.
