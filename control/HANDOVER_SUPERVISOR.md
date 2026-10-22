# HANDOVER for a NEW supervisor chat (written 2026-10-22 18:3x IST, control head after this commit)

## 1. Who/what
- User = Vipin Gupta (vipin@gurugramuniversity.ac.in), HANDLER, writes Hinglish, tz Asia/Calcutta. He wants ONLY prompts from the supervisor; he pastes them to Arena/Brave and says "Arena done"/"Brave done" or pastes outputs. Reply in Hinglish, short, plain, no jargon dumps.
- Supervisor (you, Claude) = AUDITOR: write prompts, audit Arena/Brave pushes from git (compile, PDFs, ledgers, re-derivations), arbitrate, keep control/STATUS.md and BLUEPRINT.md current. You do NOT write the scholarly content. You are the only writer of branch claude/control.
- Arena = SCHOLAR/builder (pushes manuscript to branch arena/40393d9f-le, folder phase5/master; CI builds PDF). Brave AI = INDEPENDENT VERIFIER (pushes to arena/04fdf32e-le, folder verification/; has Drive access; sandbox cannot write claude/control).
- Mission: very long top-class review paper "Multiphysics Wave Mechanics in Generalized Continua: A Constructive Review of Theory, Energy Transport, and Interface Phenomena" (generalized thermoelasticity, piezothermoelasticity, nonlocal/gradient, memory-dependent and fractional heat conduction, interface energy partition). 10+ authors. Target journal PRIMARY Applied Mechanics Reviews (ASME); backups Archives of Computational Methods in Engineering, Physics Reports. Wants it the most reliable and most-cited reference. No hurry; perfection first.

## 2. Repo and branches (https://github.com/vipin-oss/le, PUBLIC)
- claude/control (control/ folder): README, BLUEPRINT (rounds R1-R6, gates, escalation), STATUS (current table), ARENA_NEXT, BRAVE_* briefs, FULLTEXT_FINDINGS_01..05 (supervisor-read primary-source facts), HANDOVER_SUPERVISOR (this file).
- arena/40393d9f-le: manuscript phase5/master (main.tex, sections sec01-17, appendices, references_local.bib, tables), phase5/reports (R2_STATUS etc.), phase5/build_outputs (CI-published PDF + contact sheets).
- arena/04fdf32e-le: verification/ (EQUATION_LEDGER 176, CLAIM_LEDGER 53, APPA_LEDGER 84, FULLTEXT_FACTS ~104, LITERATURE_BASE 499 records, REFERENCE_PLAN 193 rows, REFERENCE_GAPS 16, DRIVE_INVENTORY/PRIORITY/TIER3, PDF_REQUEST_LIST*, V-B*.md reports).
- Git tip: after `git fetch`, use explicit refspecs `+refs/heads/<b>:refs/remotes/origin/<b>`; stale tracking refs cause false "unpushed commit" stop-hook warnings; check with `git ls-remote origin claude/control`.
- Commit trailers on supervisor commits: "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" and "Claude-Session: <current session URL>".

## 3. Standing rules
- Every prompt for Arena/Brave starts with repo + branch preamble (read control/STATUS.md first) and ends with "push, give commit hash + status".
- Repo is PUBLIC: never commit publisher PDFs, full paper text, page images or long quotes. Facts, equation numbers, <15-word quotes, status tags only. Never write the handler's private Drive folder name (a "Personal (Private...)" folder) into the repo; do not open/list it. Drive paper enumeration only by parentId of the papers folders.
- Process: no PASS without execution evidence; claim tags DERIVED / PRIMARY-SOURCE-CHECKED / SECONDARY-SOURCE / CONDITIONAL / UNVERIFIED / OPEN / DISPUTED; "no WRONG verdict without grepping own earlier V-files and stating which sub-system was checked". Own-group (Barak/Gupta) papers: neutral wording, never accuse; unverified criticism withdrawn.
- CI discipline for Arena: one commit per batch, one CI run, 25-minute cap, strict overfull gate (>1pt fails) never loosened, no commits for underfull/formatting of reports. CI TeX install can be 9-28 min; suggest caching.
- Supervisor tool notes: Crossref/doi.org direct fetch often fails from supervisor sandbox (Brave's sandbox works); GitHub artifact blob download is blocked (so PDFs are committed by Arena to phase5/build_outputs); handler's laptop Downloads reachable via mcp__remote-devices (stage files, pdftotext, render pages with pdftoppm; scanned PDFs need page render); Google Drive via read_file_content (large -> jq the saved file).

## 4. Verified science so far (see FULLTEXT_FINDINGS_01..05 for pages/equations)
- GL 1972: Fourier flux, stress beta(T+tau1 Tdot), energy k lap T = rho c (Tdot + tau0 Tddot) + beta T0 e_kk,t (NO tau0 on coupling), tau1>=tau0>0. LS has tau0 on coupling. Manuscript now corrected (hybrid labelled).
- DPL (Tzou 1995, J. Heat Transfer 117:8-16): stable iff tau_T > tau_q/2 (Quintanilla 2002). TPL = Roy Choudhuri 2007 (J. Thermal Stresses 30:231-238), first-order Taylor with k* grad v; second-order tau_q^2/2 on whole operator is Barak/Gupta/Aldawody/Yang/Deswal extension (secondary, conditional); Huang 2025 prints tau^2 (convention not universal). Quintanilla 2009 TPL window verified by sympy Routh-Hurwitz.
- GN: type II = GN 1993 J. Elasticity 31:189-208 (no dissipation); type III = GN 1992 J. Thermal Stresses 15:253-264; all introduced in GN 1991 (scanned, unread). Type II alpha-form: rho c alpha_tt + beta T0 div u_t = k* lap alpha (coupling ONE derivative; temperature form has div u_tt).
- GK 1966 (Phys Rev 148:778): kinetic (Boltzmann) derivation, lap q + 2 grad div q, lambda^2 = c^2 tau_N tau_z/5 (tau_z Ziman-averaged R time). Continuum flux law appears in Tzou 1995 eq (15) (secondary); DPL mapping tau_T = 9 tau_N/5, tau_q = tau_R.
- Moore-Gibson 1960 = gas-dynamics third-order acoustic eq (MGT is analogue). MGT needs b - tau c^2 > 0.
- Energy partition: three R definitions (R_flux/R_ref/R_mode); A is interface-local residual; EQ-10.12 identity printed in Barak 2023 eq (6.14) and Kumar-Kansal 2017 eq (80), others only "approximately unity"; Barak table-sum claim withdrawn (UNVERIFIED). Thermal channel factor is T/T0 (legacy T0/T wrong).
- Isotropic piezoelectricity impossible; eq (9.9) degree 8 correct.
- Fabricated ref: Guyer1990. Off-topic: Abdalla2022. Tzou1997 = book (no DOI) vs 1995 paper.

## 5. State at handover
- R1 PASSED (146 pp). R2 PASSED (150 pp, run 39779835094; follow-ups 33a9347, CI 39781561017, 149 pp). R3 (citations) OPEN: Arena was just given the R3a prompt (use LITERATURE_BASE DOI column joined to REFERENCE_PLAN lit_id; CI Crossref verification step writing phase5/reports/CROSSREF_VERIFY.csv; add only VERIFIED refs for sections 4.1-4.12; commit R3_STATUS.md; stop for audit). Next: audit R3a, then R3b (sections 5-9, 11-13), R3c (section 10 energy partition and 4.11 fractional; gaps GAP-09/12/13).
- Brave idle: remaining open items GN 1993 identity (4.15) untranscribed, GN 1991 scanned (needs render/OCR), Thompson 1972 not found, Cattaneo/Vernotte no DOI.
- Supervisor-side open: analyse AMR reviews (Chandrasekharaiah 1986, 1998 in handler Downloads) for length/structure benchmark; Eringen 1983, Mindlin 1974, Quintanilla 2002 details; read other Barak/Gupta papers from Drive for sec 9.7 attributions; R4 (journal fit, 10+ authors, AMR proposal email, author contributions, AI-use declaration), R5 author expert pass, R6 mock referee. Handler sends AMR proposal himself.
- Bibliography gap: manuscript ~98 refs vs AMR median ~180; target 180-200.
- Known fabricated-risk: 308 of 499 base records had blank authors (Crossref enrichment in R3a).
- Overall progress estimate given to handler: ~40-45%.

## 6. First actions for the new chat
1) git clone/fetch vipin-oss/le, read control/STATUS.md, BLUEPRINT.md, ARENA_NEXT.md, FULLTEXT_FINDINGS_01..05, this file. 2) Ask handler: "Arena done / Brave done?" and audit whatever was pushed (compile, open PDF, check ledgers). 3) Keep giving ONLY prompts.
