# HANDOVER FOR NEW SUPERVISOR CHAT (written 2026-10-26; read this FIRST, then STATUS.md, then HANDOVER_SUPERVISOR.md)

## Project
Review paper "Multiphysics Wave Mechanics in Generalized Continua" (generalized thermoelasticity, piezothermoelasticity, nonlocal/gradient elasticity, memory/fractional heat conduction, interface energy partition). Target ~150 pp. Journals: Physics Reports (proposal <=1000 words, invitation), ACME second, AMR via proposal to Editor. Page limits are third-party facts; check official guides.
User = Vipin Gupta (Hinglish, IST), HANDLER: pastes my prompts into Arena/Brave and pastes their outputs back.

## Roles
- ME = SUPERVISOR/AUDITOR: only prompts + audits (compile, PDFs, re-derivations), arbitration, control/ files. I do NOT write manuscript content. I record primary-source reads in control/FULLTEXT_FINDINGS_NN.md (next = 11).
- ARENA = builder, branch arena/b5e608f8-le (phase5/ manuscript, CI). BRAVE = independent verifier, branch arena/04fdf32e-le (verification/).
- Repo github.com/vipin-oss/le (PUBLIC). No copyrighted PDFs/text in repo. Never open/name the user's private Drive folder.
- Rule: one content commit = one CI run; strict gate (overfull >1 pt, 0 undefined refs); apply scripts only inside CI.

## State (as of 2026-10-24 repo; re-fetch to confirm)
- R3g: infra fix [R3G-INFRA] (TeX install hardened) -> run 40063975977 PASS; [R3G-REPORT] metrics run 40064319885 PASS. Later Arena commits (R3 audit reconciliation, Povstenko B21) all CI-green, latest head 26dffda (run 40078613093). Current PDF ~162 pp, 0 '??'.
- Brave B20/B21 verdict: "R3 not passed". Open: Guyer-Krumhansl .766/.778 DOI-title split in bib; Povstenko 2011 is .511931 (Eq.29 prints zeta; Gamma(1+alpha) prefactor claim OPEN); Povstenko2016 ISBN wrong (book is 10.1007/978-3-319-15335-3); s.12 = 3/6 sources (GAP-22: Chester 1963, Guyer-Krumhansl 1966, Chandrasekharaiah 1998); process language visible (39 PRIMARY-SOURCE-CHECKED, 162-row inventory) -> scrub in R4. Readiness: 8/20 sections clear the six-source bar; s.4.1, 4.9, 4.10, 13 below; GAP-09/12/13 open.
- Overall ~60-65%.

## New input waiting
User uploaded Papers_final_list.zip (56 files, 144 MB; names like majumdar1993, abate2006, dafermos1968, zhang2003, jou2010, liu1972, coleman1963/64, rayleigh1885, puri1972, nayfeh1971, yang2018, romano2017, lim2015, aifantis1992/2003, mindlin1965/68, maxwell1867, mitra1995, chen2021, jackson1970, fabrizio2014, povstenko2011/2015, cahill2003, crump1976, weideman2007, lamb1917, stoneley1924, ezzat2011, huberman2019, talbot1979, compte1997, eringen1972, chandrasekharaiah1988/1998, deresiewicz1957, achenbach1968, sinha1996/97, tzou1995, hetnarski2000, gurtin1968, quintanilla2003/2008, 2ndSoundSolids, RAGJAKI, Dell'Oro-Pata 10.1007/s00245-016-9365-1, books). Books still missing; user will send later. NEW CHAT: ask user to re-attach the zip (not stored in repo). Tracker: Papers_FINAL_list.xlsx (65 items, tiers 1-4) — user has it.

## Next steps (priority)
1. Read zip (Tier 1 MUST first: Chester/G-K/Chandrasekharaiah1998 for s.12, Povstenko2011, Dell'Oro-Pata, Mainardi) -> write FULLTEXT_FINDINGS_11.md (facts with page/eq anchors; mark supervisor inference). Cheap method: pdftotext to scratchpad, grep targeted passages; don't read whole books.
2. Give Brave prompt to ingest F-numbers + update readiness/GAPs; then Arena R3h prompt (source-specific edits, fix bib items above).
3. Audit Arena pushes (CI green, PDF pages, undefined refs, near-overfull, ledger).
4. R4: process-language scrub, journal-fit memo, Physics Reports <=1000-word proposal + AMR title/abstract/timeline (only if user says yes), author contributions/AI-use declaration. R5 author expert pass. R6 mock referee.
5. Open user decision: rewrite git history to remove private Drive folder name from old commits.

## Style
Reply in Hinglish, short. Give prompts in code blocks for Arena/Brave. Keep token use low: no recaps, targeted greps, no full-PDF dumps.

## UPDATE 2026-10-26 13:30 IST (supersedes "State" above where different)
- Arena head db7db34 = [R3-LOCAL-RECOVERY]: 23 docs/CSV files under recovery/ + R3_DEEP_CLAIM_TRACEABILITY_RECOVERY_CHECKPOINT; no PDFs; private refs redacted. Audited OK. Its CI run 40285030356 FAILED at "Install TeX" (20-min timeout, infra flake; docs-only commit so PDF unchanged). Valid PDF = 26dffda build, 162 pp, 0 undefined. Do NOT rerun.
- LOST/unlocated work from 24-25 Oct (96-claim traceability matrix, defect register 18 open [1 P0], D4/D5 decision packet, 43-test R3F/audit scripts): NOT on GitHub or Drive; Arena's 25 Oct session saw an empty checkout. A 155 MB archive le-working-state.tar.gz (pre-GAP-12, 2026-10-24) exists on user's/old-Arena machine. User decided: DROP it, move on with what exists.
- Zips seen: le-arena-b5e608f8-le.zip and le-arena-04fdf32e-le.zip = identical to GitHub snapshots (26dffda / 77769ef). LE_R3_Recovery_Reference_Pack = 4 text notes only.
- CURRENT STEP: Arena was given the R4a CLEAN-UP prompt (classify the 164 process-language rows A/B/C, remove ALL-CAPS tags/GAP/LIT/R3 ids from rendered text without hiding unverified claims; write phase5/reports/OPEN_CLAIMS_LEDGER.csv; Povstenko .511931 Eq.(29) uses zeta, no tau^a/Gamma(1+a) attribution; Sec 12 unsupported claims hedged/removed; GK .766 vs .778 distinct; pages <=162; add paths-ignore for recovery/**, R3_*.md, verification/** to workflow; commit "[R4A-CLEANUP] ..."). Awaiting handler to paste Arena's report. AUDIT it: forbidden-token grep on PDF text = 0, ledger class-C rows, Povstenko fix, CI pass, pages <=162, undefined 0, no Drive refs/PDFs added.
- THEN: read Papers_final_list.zip (user must re-attach) -> FULLTEXT_FINDINGS_11 -> Brave ingest -> Arena R4b to turn OPEN_CLAIMS_LEDGER class B/C rows into source-backed text. Then page compaction to ~150, journal memo/proposal.
- Token policy: user wants Supervisor (me) tokens low; Arena tokens unlimited => put heavy work (greps, big reads, drafts, checks) in Arena/Brave prompts; I only audit compactly.
