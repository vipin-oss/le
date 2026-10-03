# Phase 5 changelog — literature audit and introduction repositioning

Reference additions are made in the sources of truth (`01_Literature/REFERENCES_VERIFIED.json`, the `.bib` file,
and the prose inside the builders), never in a generated document. `verification/patch_phase5.py` holds the
edits and is idempotent.

## 1. Reference list (54 -> 55)

- `PAPER_PROJECT/01_Literature/REFERENCES_VERIFIED.json` — entry 55 appended:
  Gurtin, M.E., Pipkin, A.C. *A general theory of heat conduction with finite wave speeds*.
  Archive for Rational Mechanics and Analysis 31(2), 113–126 (1968). doi 10.1007/BF00281373,
  with the level stated as metadata-verified from Crossref on 2026-10-03 by this audit (not full text read).
- `PAPER_PROJECT/13_Manuscript/FINAL_REVISED_REFERENCES.bib` — the matching `@article{gurtin1968}` appended, so
  the `.tex` path carries the same entry.
- No entry was removed, edited or renumbered; the existing 54 keep their positions, so the numbers in the text
  did not move.

## 2. Prose

- `ms_derivation.py` (Section 2.2) — the passivity sentence now carries [55] and states the relation precisely:
  the restriction is one "stated there for a memory kernel rather than for a single relaxation time", and
  τ > 0 is its instance here. The two-relaxation-time kernel sentence that follows is unchanged.
- `ms_static.py` (Section 1.2) — the framework sentence gains "; the general theory of heat conduction with a
  memory kernel and finite wave speeds is due to Gurtin and Pipkin [55]", so the introduction attributes the
  theory to a primary source instead of leaving it with the reviews. The bounded-search sentence in 1.1 was
  left word for word intact — no priority claim introduced or strengthened.
- `build_calculations.py` (companion 2.1) — the "both kernels are positive-real (passive)" sentence now points
  to manuscript reference [55], so the two documents make the same claim with the same support.

## 3. What was audited and needed no change

- Richardson extrapolation: already cited to Richardson and Gaunt [52] in Section 5 (B19's suspicion checked and
  found not to hold). A verified second candidate (Ferziger & Peri ć, doi 10.1007/978-3-642-56026-2) was not
  added: it would duplicate an existing citation.
- Claim ↔ citation sweep (`lit_B_claims_matrix.py` → `claims_matrix.json`): 139 citation instances, all 55
  entries cited (0 orphans), and no strong-verb claim in Sections 1–3 resting on a metadata-only record.
- Cattaneo 1948 and Vernotte 1958: searched, could not be verified to a record with usable details; not added.
  The query log, the contradictory secondary evidence and the exact follow-up needed for the authors are in
  `SEARCH_NOTES.md` (ledger item P5-1, open by decision, not by oversight).

## 4. Regenerated deliverables and freeze

- Order followed the Phase 4 rule: builders → `make_code_freeze.py submission_2026_10_03d` → both documents →
  supplementary workbook → `.tex` (both) → `.pdf` (both) → mirrors → gates.
- New manifest `CODE_FREEZE_submission_2026_10_03d.json` (27 files). Added, not overwritten: 03c, 03b, 10_03,
  10_02 and the gate manifest are byte-unchanged, and the companion's supersession sentence names them.
- Rebuilt: `manuscript_IJHMT.md/.pdf/.docx`, `calculations_IJHMT.md/.pdf`, `MANUSCRIPT_STATS.json`,
  `highlights.txt`, `SUPPLEMENTARY_TABLES.xlsx`, `FINAL_REVISED_{MANUSCRIPT,CALCULATIONS}.tex/.pdf`.
- Structure after the change: 9 sections, 41 subsections, 84 equations, 8 figures, 11 tables, **55 references**;
  abstract 249/250 words, highlights [78, 70, 69, 74, 69], body ≈10 474 words; companion 11/37/29/9, ≈5268
  words.
- Gates after the final build, all green: `tools/audit_tex.py`, `tools/audit_tex.py -c` (companion),
  `tools/check_tex_commands.py`, `tools/check_crossrefs.py`, `tools/verify_pdf.py` on each of the four PDFs.
  The digest quoted by both documents for 03d equals the manifest on disk.
- `07_Tests/run_tests.py` was not re-run in this phase: no numerical code changed (only prose builders, the
  reference database and the `.bib`), so the Phase 4 record of 27 PASS / 0 FAIL / 1 exploratory still describes
  the code. The suite is re-run for the release record in Phase 8.

## 5. Deliberate non-changes

- No reference added without a verifiable record (hence P5-1 stays open for the authors).
- No renumbering of the existing list, no removal of any entry, no "novel/first/comprehensive" language added to
  the introduction, and the bounded-search sentence left exactly as verified in earlier phases.
- The 1948/1958 attribution remains in the body as naming, not as a citation, because citing a 2011 reprint as
  the 1948 original would misdate it.
