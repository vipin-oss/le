# Submission checklist - IJHMT (Elsevier), monoclinic cavity manuscript

Status symbols: [x] done and machine-checked, [ ] needs the authors, [!] cannot be closed in
this environment.

## Manuscript body
- [x] Title; no undefined abbreviations in it; subtitle kept (it carries the claims)
- [x] Abstract 249 words (limit 250), one paragraph, no citations, no undefined abbreviations
- [x] Highlights: 5 items, longest 78 characters (limit 85), `highlights.txt` identical to the block
- [x] Keywords: 6, semicolon-separated
- [x] 9 numbered sections, 41 subsections, 84 numbered equations, 8 figures, 11 tables
- [x] Numbered citation style: 55 references, ascending first-appearance order, no orphan,
      no dangling key; `elsarticle-num` in the LaTeX, so Markdown and .tex agree
- [x] Explicit limitations (§7.2) and a "verified, not validated" position stated in the
      highlights, abstract, §7 and §8
- [x] Back matter: Acknowledgements, Declarations, Appendix A (nomenclature), References
- [x] No banned hyperbole; no project-internal vocabulary in the printed text
- [ ] [AUTHOR INPUT REQUIRED] author names, affiliations, ORCID iDs, corresponding author
- [ ] [PUBLIC REPOSITORY/DOI TO BE INSERTED] in the Data availability statement
- [ ] CRediT statement, competing interest, funding: drafted skeletons to be completed

## Declarations
- [x] Elsevier-form AI declaration for the writing process, above the references
- [x] Research-process AI use disclosed in the numerical-methods section
- [x] Data availability points at the code freeze and the package inventory in §9
- [ ] [!] Authors to confirm the AI wording matches what actually happened

## Files to upload
- [x] `FINAL_REVISED_MANUSCRIPT.tex` (+ `manuscript_IJHMT.pdf`, 33 pages) - source and preview
- [x] `FINAL_REVISED_CALCULATIONS.tex` (+ `calculations_IJHMT.pdf`, 14 pages) - companion
- [x] `FINAL_REVISED_REFERENCES.bib` - 55 entries, keys identical to the printed list
- [x] `SUPPLEMENTARY_TABLES.xlsx` - 8 sheets, satisfies the "full table: supplementary
      material" promise in the Table 2 caption
- [x] `PDF_VERIFICATION.txt` - captured `tools/verify_pdf.py` output for both documents
- [x] `cover_letter.md` - refreshed draft (see below)
- [ ] [!] Figures: eight PNGs at the resolution the plotting scripts produced; IJHMT asks for
      300 dpi or better in individual files - regenerate as TIFF/EPS/PDF from
      `11_Figures/make_figures.py` if the editor's system asks
- [ ] [!] `pdflatex` compile of both `.tex` files with `elsarticle` - no TeX engine exists
      here, so both were checked statically only (`tools/audit_tex.py`,
      `tools/check_tex_commands.py`, `tools/check_crossrefs.py`, `tools/test_md_to_tex.py`)

## Provenance
- [x] Deposit manifest `06_Source_Code/CODE_FREEZE_submission_2026_10_03j.json` (27 files),
      every entry re-hashed against the code
- [x] History preserved byte-unchanged: `CODE_FREEZE_2026_10_02.json`, `CODE_FREEZE_submission_2026_10_03.json`, `..._03b` ... `..._03i`, `CODE_FREEZE_v2_gate.json`, `CODE_FREEZE_v2_blockF.json`
- [x] `tools/connection_audit.py` green except for the working-tree check (resolved by the
      commit that closes the phase)
- [x] Verification suite re-run: 28 cases, 27 PASS, 0 FAIL, 1 exploratory (INFO) - matches the
      sentence in §5
- [ ] [!] Author-side expert read of the formulation (Phase 1 recorded this as beyond an
      agent's competence); the P5-1 literature item (Cattaneo 1948 / Vernotte 1958 primary
      sourcing) stays open and is disclosed in the cover letter

## Cover letter (draft, `13_Manuscript/cover_letter.md`)
Complete except: date, editor name, corresponding author, suggested reviewers, repository DOI,
journal-choice confirmation (alternatives and the reasoning are in `JOURNAL_FIT.md`). It states
the verification scope, the limitations, the AI split and the Cattaneo/Vernotte citation
decision, and it claims no experimental validation.

## Not submitted (by design)
- Nothing merges to `main` and no pull request: the programme's work lives on the session
  branch `arena/01a10176-le`, committed per phase.
- No fabricated author, funding, DOI or reviewer content; no result was added or edited during
  Phases 6-8 - every change was wording, structure, provenance or tooling.
