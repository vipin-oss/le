# HANDOFF — read this first (state at 31 Oct 2026, 20:05 IST)

Repo: github.com/vipin-oss/le, branch `review-paper-v2`, folder `paper_v2/`. Latest commits: 7e9289d (benchmark registry), f0c8b94 (claim register). Never put Drive IDs, links or folder names of the source library in any file in this repo.

## 1. Aim
Finish the review "Waves in Thermoelastic and Multiphysics Continua" as a journal-ready, field-defining review of the whole field (not only the authors' papers), fully verified, nothing invented, following `BLUEPRINT_v3.1.md`. Target venue: Applied Mechanics Reviews or Physics Reports (final choice open).

## 2. Roles
- Claude (main session): edits the manuscript (LaTeX), runs scripts, builds the PDF, packages and pushes. Only Claude edits `main.tex` and `sections/*.tex`.
- Arena chats (other AIs): evidence work only — read sources, check claims, audit, report. They must NOT change manuscript structure or the .tex files, cannot compile LaTeX, and must put PDFs outside the repo.
- Every Arena output is verified by Claude before it is accepted; unverified output is not used.
- Arena rules: save CSV headers to a scratch file before context compaction (headers get lost); push to the assigned branch and show `git ls-remote` proof; a script check must print a line starting with `PASS` and exit 0; mark anything not read in a source as "SOURCE NOT AVAILABLE" or "from general knowledge, not verified"; no guessing of DOIs, pages or quotes.

## 3. Manuscript now
145 pages, 0 undefined references, 0 errors, 14 of 14 checks PASS (`scripts/run_checks.py`, log `scripts/checks_log.txt`, all printed numbers archived in `scripts/numbers_log.txt`). Build: pdflatex + bibtex on `main.tex` (working tree is outside the repo; the repo holds `main.pdf`, `overleaf_package.zip` = `paper_sources.zip` with all sources and scripts).

## 4. What has been done
1. Bibliography (238 keys): every entry checked at level R0–R3 (R1 = no DOI); metadata errors fixed. R0 (not read) keys: Cattaneo1948, Vernotte1958, Tzou1997, Achenbach1973, Nowacki1975, Duhamel1837, Chadwick1960, Carlson1972, Gulyaev1969.
2. Claim checks for sections 2–15: 224 claim checks merged into `claim_register.csv` (50 supported, 18 partly, 2 not, 154 source not available). Wording of flagged claims was changed in the manuscript; re-audit pending.
3. Notation audit (51 items): all high and most medium/low fixed (omega_*, i->ii, symbols for diffusivity/front speed/lengths, abbreviations, nomenclature table). Still open: A021 (alpha as Caputo order and GN-III coefficient), A022, A026, A036, A037, A039, A050, A051.
4. Numbers audit (133 rows): one real error fixed earlier; all "no script found" items now backed by `numbers_log.txt` or new script assertions. Not scripted by design: values read off figures (peak positions, percentage levels).
5. Citation audit (48 rows): uncited Bleustein/Gulyaev cited, author-order bug fixed, "et al." fixes. Key-year mismatches are harmless labels.
6. Referee read (43 rows): organising claim narrowed (Green–Lindsay and Guyer–Krumhansl lie outside the heat-flux template), duplicate nomenclature and keywords removed, DPL result stated as numerical.
7. New own-derivation content: layered waves chapter (Love, Stoneley, Scholte-type; `check_layered`), atlas geometry figures drawn from the sources' own problem statements, identifiability subsection (4 of 5 template parameters identifiable; synthetic test only; `check_identify`), effective-modulus/causality/Kramers–Kronig section (`check_modulus`; sum rule verified for the classical model only), Appendix H benchmark registry (14 code-verification benchmarks; no physical validation exists because no new experiment is reported).

## 5. What is still open (priority order)
A. Missing sources. 154 claims cannot be verified because the PDF was not available. `missing_sources_priority.csv` ranks the 141 cited sources by claims blocked. Highest: Chirita–D'Apice–Zampoli 2016; Povstenko 2004/2007/2009 and 2011 (Cattaneo); Prasad–Kumar 2020; Chen–Nunziato 1974; Chirita–Ciarletta–Tibullo 2017; Chandrasekharaiah 1996; Zener 1937; Eringen 1983; Mindlin–Tiersten 1962; Quintanilla 2002b/2003/2006/2008/2009; Fabrizio–Lazzari 2014; Rukolaine 2014; Cattaneo 1948; Vernotte 1958; Ackerman 1966; Jackson 1970; Joseph–Preziosi 1989/1990; Biot JASA 1956 I/II. The author supplies PDFs; Arena then re-runs claim checks on them.
B. Claim checks not yet done: sections after 15 (16–36 incl. atlas, benchmarks, guides, appendices) and batches 003, 004, 008 (their files are not in the repo).
C. Quintanilla 2003: the statement "tau_T >= tau_q/2 belongs to one Taylor truncation" is attributed to it but the PDF was never read; keep hedged until read.
D. Gurtin–Pipkin 1968 hereditary heat conduction is absent from the paper and is a missing landmark; needs a verified source (title, journal, DOI) before it can be cited. Also check other missing landmarks (Callaway/phonon BTE closure, Jeffreys-type laws).
E. Independent second implementation of the key dispersion/modulus/front results (another group's code or a different language) is not done; the registry says so.
F. Experimental evidence is thin (no new data). Literature search for measured thermal relaxation times, second-sound, TDTR/pump-probe, attenuation vs frequency in solids with DOIs and the quoted numbers (units, temperature, model used) would strengthen section 31; atlas of 14 problems is a "first instalment" and is not representative — needs a systematic sampling plan.
G. Chapters not written: Biot poroelastic waves (needs Biot JASA I/II PDFs), viscoelastic/fractional Kramers–Kronig beyond the classical case, experiments chapter, cross-model limit table.
H. Journal choice, cover letter, highlights and proposal cleanup (AMR/Physics Reports) — after A–D.
I. Housekeeping: `main_els.tex` (Elsevier format) untested; one Overfull hbox earlier near section 3 text; repo visibility unconfirmed and older Arena registers on `arena/*` branches may contain library IDs (clean before making the repo public).

## 6. Arena tasks to run now (copy each into a separate chat)
### Task 1 — claim checks for sections 16–36 (and batches 003/004/008 if you have them)
Read `paper_v2/main.pdf` (outside the repo copy) and `sections/*.tex` from the branch. For every sentence in sections 16–36 and appendices that cites a source for a technical statement, make one row: claim_id, manuscript_location (section + page), manuscript_statement (quote, max 25 words), cited_source (bib key), source_doi, found_in_library (yes/no), verdict (SUPPORTED / PARTLY SUPPORTED / NOT SUPPORTED / SOURCE NOT AVAILABLE), source_page_or_equation, source_wording_max25words, what_source_actually_states, verification_level (R0–R3), notes. Only mark SUPPORTED when you read the passage; otherwise SOURCE NOT AVAILABLE. Save to `paper_v2/arena_deliverables/P3_evidence_claims_B/claim_check_B_batch_NNN.csv` (headers first, 40 rows per batch), push, show `git ls-remote`.

### Task 2 — re-audit of the 20 flagged claims
For each PARTLY/NOT row in `claim_register.csv` find the current sentence in the latest `main.pdf`, and say whether it now matches what the source states. Output: claim_id, current_text, matches_source (yes/partly/no), suggested_wording (max 30 words, only what the source supports), page_or_equation. Do not edit the .tex files.

### Task 3 — missing landmark literature
Search the web (publisher/DOI pages only) for the landmark works not in the paper: Gurtin–Pipkin 1968 (hereditary heat conduction), phonon-BTE/Callaway closures, Jeffreys-type and Maxwell–Cattaneo-with-memory laws, Joseph–Preziosi 1989/1990, Chandrasekharaiah 1998 review, recent reviews of thermoelastic waves 2020–2026. For each: authors, title, journal, volume, pages, year, DOI (copy from the DOI page; if not found write "NOT FOUND"), one-line relevance, section where it belongs. Output `paper_v2/arena_deliverables/P2_landmarks/landmarks_2.csv`. Never infer a DOI.

### Task 4 — experimental data survey
List measured values of thermal relaxation times and second-sound/ballistic heat observations in solids (graphite, NaF, Bi, Si, Ge, GaAs, SiC, metals via pump–probe/TDTR), thermoelastic damping measurements in resonators, and attenuation vs frequency tests of Lord–Shulman/DPL fits. For each: DOI, material, temperature, method, the quoted number with units and page, model used to extract it, and whether the authors state the uncertainty or identifiability. Output `paper_v2/arena_deliverables/P3_experiments/experiments_1.csv`. Mark entries read only from an abstract as "abstract only".

### Task 5 — atlas expansion plan
Propose (do not write) a systematic sampling of 40 published problems in generalized thermoelastic/multiphysics wave propagation 2000–2026 stratified by wave family (bulk, Rayleigh, Lamb, interface, thermoelastic damping, piezo/magneto, porous), with DOI, model, geometry, what the paper validates against, and whether full text was read. Output `paper_v2/arena_deliverables/P3_atlas/atlas_plan.csv`.

### Task 6 — independent second implementation
Write a standalone Python (or Julia/Matlab) code that does not import anything from `scripts/models.py` and computes: (i) the coupled 1D dispersion roots K=k^2 for the template G(s) with the parameter sets in `scripts/models.py` docstring; (ii) the phase speed and Q^-1 of the elastic branch at 20 frequencies. Compare with `scripts/numbers_log.txt` and report max relative difference. Put the code in `paper_v2/arena_deliverables/P4_second_impl/` and a short report with the table of differences. Do not touch `scripts/`.

## 7. Files that matter
`BLUEPRINT_v3.1.md` (rules and required registers), `P1_DEFECT_REGISTER.md`, `claim_register.csv` + `claim_register_README.md`, `missing_sources_priority.csv`, `benchmark_registry.csv`, `refs_catalogue_check.csv`, `verification_register.csv`, `arena_deliverables/P1_audit/*` (notation, numbers, citation, referee reports), `scripts/` (inside `paper_sources.zip`).

## 8. Definition of done
Reference register and claim register complete (every critical technical claim at R3 or independently derived); every number in the text traceable to a script line; benchmark registry with an independent second implementation; experiments section backed by a surveyed table; atlas representative; journal chosen; PDF builds with 0 undefined references; no library IDs in the public repo.
