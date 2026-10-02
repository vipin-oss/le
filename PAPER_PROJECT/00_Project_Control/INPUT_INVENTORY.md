# INPUT_INVENTORY — Phase 0 (2026-10-01)

Scope: what the user has supplied (MASTER_PROMPT §6, §17). Inspection was read-only. Status labels follow §8.
"USER-SUPPLIED / HANDOFF-RECORDED" = I did not independently verify it.

## 1. Package identity and integrity
| Item | Value |
|---|---|
| Package | `COMPLETE_WORK_HANDOFF_2026-09-30.zip` — an AI-agent work handoff dated 2026-09-30, from the user's public GitHub repo `vipin-oss/BFS-FEM-MATLAB`. The repo name does not match the active project: the project inside is a Python finite-difference (FDFD) study, not MATLAB/BFS-FEM. |
| Retrieved | 2026-10-01, HTTP 200, 6,875,698 B, SHA-256 `405923ba8599e5358a58b69cab6831e76fc81c7ad84b595aa43efaf51ae59a9a` |
| Location | `/home/user/work/handoff.zip`; extracted to `/home/user/work/handoff/` — 304 files, 9,410,034 B uncompressed. **Read-only baseline; never edit.** |
| Integrity | `MANIFEST_SHA256.json` (built 2026-09-30T16:59:08, 303 entries): **303/303 SHA-256 match**, re-verified 2026-10-01. The manifest does not hash itself. A stray `src/__pycache__/cg_model.cpython-313.pyc` created by my own earlier code execution was not in the zip and was deleted (see CHANGELOG). |
| Master prompt in package | `MASTER_PROMPT.md` v2.1; its SHA-256 equals the value in `PROJECT_CONTROL/MASTER_PROMPT_PROVENANCE.json` (`c18fd525…dac0`). The user's 2026-10-01 paste: 10 of 10 sampled sentences found verbatim in this file; no full byte-diff done. |

## 2. Composition
| Folder | Files | ≈KB | Content |
|---|---|---|---|
| (root) | 15 | — | control/state docs: START_HERE, CURRENT_PROJECT_STATE, DECISION_LOG (D001–D018), CHANGELOG, COMPUTE_STATUS, REPRODUCIBILITY_STATUS, VALIDATION_STATUS, REJECTED_IDEAS, 3 earlier `PROJECT_STATE_*_01` files, MASTER_PROMPT (+VERSION, DATE), MANIFEST |
| PROJECT_CRYSTAL_GEOMETRY_01 | 143 | ≈3,100 | **active project** (see §3) |
| PILOT_HUANG_2025_01 | 70 | 2,253 | source-case reproduction of Huang et al. 2025 (CV/MCV3 models): code, data, logs, `PILOT_REPORT_FINAL.html` — "PILOT — NOT FINAL VALIDATION" |
| BENCHMARK_SOURCE_REVIEW/ALIT_01 | 26 | 2,088 | review of 3 benchmark PDFs (B01–B03), rendered page checks, `SOURCE_RIGHTS.md`, readiness workbook, a recovery zip (235 kB) |
| RESEARCH_READING | 24 | 1,344 | corpus reading: inventories, extracts, Crossref check, 3 reading-state files, 7 unpublished-manuscript text extracts (810,649 B) |
| PRE_EXECUTION_REVIEW | 16 | 852 | journal/benchmark screening before execution, Klimm source check, a recovery zip (174 kB) |
| CODE_REVIEW/FEM4_PACKAGE | 6 | 76 | static inspection of the user's MATLAB FEM4 package (not executed) |
| HEAT_MODEL_EXPLORATION | 3 | 36 | heat-conduction model options, thermoelastic direction note |
| PROJECT_CONTROL | 1 | 4 | master-prompt provenance JSON |

By type: json 101, md 66, npz 52, py 28, csv 17, png 16, txt 10, xlsx 3, log 3, zip 2, svg 2, html 2, no extension 2. **PDF: 0** — no third-party PDFs are inside the package.

## 3. Active project — `PROJECT_CRYSTAL_GEOMETRY_01` (143 files)
- 22 top-level files: 19 documents (ASSUMPTIONS, JOURNAL_SCREENING, MANUSCRIPT_DRAFT, MATHEMATICAL_FORMULATION, NUMERICAL_METHOD_SELECTION, PARAMETER_TABLE, PHYSICAL_VALIDATION_PLAN, PRIOR_WORK_COMPARISON_R2, PROBLEM_DEFINITION, PROJECT_STATE_PHASE_08…13, SCIENTIFIC_ACCEPTANCE_PLAN, SEARCH_LOG, SELF_AUDIT_CHECKLIST, VERIFICATION_PLAN) + 3 scripts (`run_verify.py`, `run_production.py`, `analyze_production.py`).
- `src/` 5 (cg_model, cg_grid, cg_ops, cg_solver, cg_transient) · `data/` 101 (ANALYSIS.json, ANALYSIS_TABLE.md, NUMBERS_AUDIT.csv, SUPP_*.csv, VERIFY.json, CODE_FREEZE.json, ENVIRONMENT.json, `PROD/` per-run json/npz) · `figures/` 6 (fig1–fig5 + FIGURE_CAPTIONS.md) · `logs/` 4 · `SUBMISSION_PACKAGE/` 5 (manuscript_IJHMT, cover_letter, title_page, declarations, README).

## 4. Literature and corpus inventory (§6 categories)
| Category | Items | Status / verification level |
|---|---|---|
| User's published papers | `Vipin_Research_Papers_06-Aug_2026.xlsx` (workbook not in package; derived `PUBLISHED_PAPERS_INVENTORY.csv/.json`): 48 records — 2022:1, 2023:10, 2024:15, 2025:9, 2026:13. User-supplied indexing: SCI 43, WOS 3, Scopus 2. Affiliation column: "Gurugram University" 25, "Other" 23. | indexing / impact factor / affiliation USER-SUPPLIED — NOT VERIFIED. Crossref metadata check: 12 OK, 36 rate-limited (HTTP 429) → incomplete, not invalid |
| Published full texts read | 8 PDFs (Sr. 1, 2, 25, 29, 35, 38, 45, 47; 148 pp.), section-level first pass. Sr. 10 and 21: no PDF retrieved. | PDFs not in package (extracts in `PUBLISHED_READING_EXTRACTS.json`) |
| User's unpublished manuscripts | `FEM_Total.zip`: 8 PDFs, 265 pp. (`FEM_!_Paper` [sic], FEM_2…FEM_5, GK_heat, Quasi_crystal, paper_springer). Text extracts exist for 7 (`RESEARCH_READING/EXTRACTED_UNPUBLISHED/`, 810,649 B); none for `paper_springer.pdf`. | publication status as supplied; handoff D018 records the 7 as the user's own |
| User's existing code | `FEM4_final_package (2).zip`: 226 files, 113 MATLAB `.m` (89 in `program/MATLAB_COMPLETE_PROGRAM/`), 3 Python figure scripts; static inspection only (`CODE_REVIEW/FEM4_PACKAGE/`) | NOT_RUN (no MATLAB/Octave); package not in this workspace (URL + SHA-256 in `CODE_REVIEW/FEM4_PACKAGE/SOURCE_MANIFEST.json`) |
| Benchmark papers | B01 Huang et al. 2025, *Appl. Math. Mech. (Engl. Ed.)*, DOI 10.1007/s10483-025-3280-7 · B02 Bagri & Eslami 2007, *Int. J. Mech. Sci.*, DOI 10.1016/j.ijmecsci.2007.04.004 · B03 Gordeliy, Crouch & Mogilevskaya 2008, *Int. J. Heat Mass Transf.*, DOI 10.1016/j.ijheatmasstransfer.2007.10.021 | publisher PDFs came from the user's public repo; redistribution rights not established (`ALIT_01/SOURCE_RIGHTS.md`); not in package. B01 source case reproduced by the pilot → PILOT — NOT FINAL VALIDATION |
| Material-data sources | Adachi et al., *J. Appl. Phys.* 124, 085102 (2018), DOI 10.1063/1.5047017 (13 elastic constants) · Klimm et al., *Cryst. Res. Technol.* 58, 2200204 (2023), DOI 10.1002/crat.202200204 (conductivity tensor) · thermal expansion (manuscript ref [10]) and heat capacity (ref [11]) sources: unidentified placeholders | Adachi and Klimm: values in the code match the primary sources (my check 2026-10-01). Refs [10], [11]: UNVERIFIED |
| Closest prior work / competing approaches | `PRIOR_WORK_COMPARISON_R2.md`, 8 rows: Florence & Goodier 1959/60; Chao & Gao 2001 (elliptic boundaries, anisotropic); DPL fibre-reinforced medium with circular hole (2015); orthotropic cylindrical-cavity family; Karmakar–Sur–Kanoria 2016; thermo-electro-elastic Green's function with elliptic hole (1999); Jafari 2019; Huang-2025 + Bagri–Eslami + Gordeliy | verification level mostly abstract / metadata / snippet; equations only for row 8. Gap "HOLDS" = PROVISIONAL. My 2026-10-01 spot searches found nothing contradicting it (not systematic) |
| Manuscript references | 11 numbered refs in `manuscript_IJHMT.md` | ref [9] (Tzou 1995) complete; **10 of 11 carry placeholders** (titles/initials; `SUBMISSION_PACKAGE/README.md` TODO 1) |
| Duplicates | Sr. 36 and 41 are the same record (title + DOI 10.1080/15376494.2024.2440131) | handoff-recorded |

## 5. Referenced but NOT present in this workspace
- Original PDFs and archives: `FEM_Total.zip` (14,684,600 B, SHA-256 `0df95422…b2`), `FEM4_final_package (2).zip` (2,282,857 B, SHA-256 `6d8c7311…aa91`), the user's workbook (20,650 B, SHA-256 `1e1689b1…3124`), the three benchmark PDFs, the Klimm PDF, the 8 sampled published PDFs. They lived under `/home/user/RESEARCH_PROJECT_INPUT/` in the earlier agent's workspace. User-repo items can be re-fetched (URLs in `RESEARCH_READING/SOURCE_MANIFEST.json`); publisher PDFs are not mine to redistribute.
- `PILOT_HUANG_2025_01/reference_local/` (private digitization of source figures, excluded from recovery) → the pilot's 175/177 source-figure comparison cannot be re-run from this package alone.
- `RECOVERY_CRYSTAL_GEOMETRY_01.zip` and `FULL_RECOVERY_2026-09-30.zip` (571 files, 39 MB), cited by `CURRENT_PROJECT_STATE.md`, D018 and the manuscript's Data-availability text: not in this package.
- `RESEARCH_PROFILE.md`: referenced as a root file by three handoff documents; absent.
- Named MASTER_PROMPT deliverables of Phases 0/0A/3/4/5/7/9/12 and `PACKAGE_PHASE_xx`: see `PROJECT_STATE_PHASE_00.md` §3.

## 6. Metadata cautions
1. Sr. 47: workbook DOI `10.1016/j.jppr.2026.116904` differs from the PDF/publisher DOI `10.1016/j.jppr.2026.02.007` (handoff-proposed correction; original workbook not edited).
2. Sr. 2: the "Link to Article" points to an indexing search page, not the article.
3. Fallback-journal naming is inconsistent: `SUBMISSION_PACKAGE/README.md` and D017 call "MDSM" *Mechanics of Advanced Materials and Structures*; `JOURNAL_SCREENING.md` identifies it as *Mechanics Based Design of Structures and Machines* (ISSN 1539-7734); manuscript ref [4] writes "Mech. Adv. Mater. Struct." for DOI 10.1080/15397734.2015.1029589, whose prefix matches ISSN 1539-7734. To be settled from publisher records at Phase 13 — UNVERIFIED.
4. FEM4 package `main_final.pdf` is not byte-identical to the supplied `FEM_4_Paper.pdf`; revision alignment uncertified (`CODE_OVERVIEW.md`).

## 7. Reliability of the inputs
The handoff documents were written by an AI agent. They contain stale or inconsistent values and one confirmed code defect (`PROJECT_STATE_PHASE_00.md` §6–7). Treat them as an input corpus, not as verified truth (§6).
