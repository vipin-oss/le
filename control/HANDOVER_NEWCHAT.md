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
