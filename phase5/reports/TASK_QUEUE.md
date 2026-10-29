# Task queue — overnight writing session (R4B-NIGHT-WRITE)

Branch: `arena/e6146644-le` (branch of record; never push to arena/36bc8cc8-le or arena/b5e608f8-le). Started 2026-10-28 ~21:00 IST. End 06:00 IST.
Rule: writing items first; each content commit = one CI run; docs-only commits do not build.
If this session dies, resume from this file plus `AUTONOMY_LOG.md`.

Status key: `[ ]` open, `[~]` in progress, `[x]` done (commit id in brackets), `[!]` blocked (see BLOCKERS.md).

## W1 Unified framework (Q1)
- [x] W1.0 Verifier `verify_unified_reductions.py` runs (needs sympy; installed in /tmp venv, not in repo). Output: PASS for all reduction checks.
- [x] W1.1 (046b8a3) Add subsection "One template and stepwise reductions" to `sec12_comparative.tex` (before 12.4): template statement (definition), per-reduction steps, negative cases.
- [x] W1.2 (OCL-535..548) Add ledger V rows for every new W1.1 claim (resolved_by = verifier line ranges; evidence_mode = SYMPY-...).
- [x] W1.3 (01cda7c) Notation mapping table: template symbol ↔ family symbol (LS, DPL, TPL, MGT, GN, MDD, fractional, nonlocal).
- [x] W1.4 (CI 40716977248, 40717508285) Build + CI on the W1 content commit (batched with W2 if sections are small).
- [x] W1.5 (bd0de3c, b1055d8) Comparison table cells audit: every cell class A/V or explicitly "model-dependent" (Table in sec12, `tab:limiting_cases_revisited`). Ledger rows OCL-584..OCL-595 appended; cell-by-cell audit sentence added to sec12_comparative.tex.

## W2 Per-family statements (Q3)
- [x] W2.1 (eab7d15) LS / Fourier family: established / disputed / open, with citations and reason.
- [x] W2.2 (eab7d15) DPL / TPL family: same format; note TPL ordering condition (0 <= tau_v < tau_T < tau_q) is source-specific.
- [x] W2.3 (eab7d15) MGT family: same format; cite Quintanilla 2019 variant as distinct.
- [x] W2.4 (eab7d15) GN-I/II/III family: same format; GN-III kappa=0 reduction is derivative-level only.
- [x] W2.5 (eab7d15) Fractional / MDD family: same format; MDD reduction model-dependent.
- [x] W2.6 (eab7d15) Nonlocal family: same format.
- [x] W2.7 (eab7d15) Two-temperature family: Ezzat2011 UNREAD (library copy is a different paper) — hedge class B; Chen–Gurtin not in library (MISSING).
- [x] W2.8 (DECISIONS_FOR_AUTHOR attribution section) Attribution corrections list: Tzou1995 (J. Heat Transfer) vs Tzou1995a (JTHT); Hetnarski 1999 vs 2000; Chen–Gurtin vs Gurtin–Pipkin; Dell'Oro–Pata two-author vs three-author; Quintanilla 2003 DOI 10.1080/713855996.
- [x] W2.9 (CI 40717508285) Build + CI.

## W3 Verified derivations in the body
- [x] W3.1 List the ~40 VERIFIED displays from EQUATION_AUDIT.csv (status VERIFIED-*); for each, assumptions, steps, limits (text only where a script or source supports the step). Inserted into sec12 at label sec:12.verified_register; body text sanitized (no internal paths/OCL ids/forbidden tags in PDF).
- [x] W3.2 Worked example for Sec 10 interface partition: complete worked one-dimensional welded-interface system in sec10 (r=(Z1-Z2)/(Z1+Z2), t=2Z1/(Z1+Z2), R=|r|^2, T=(Z2/Z1)|t|^2, R+T=1, incident/reflected cross-term derived); hedged to lossless longitudinal case.
- [x] W3.3 Worked example for one unified reduction (from W1.1): Lord--Shulman-to-Fourier from Eq. eq:12.template, added to sec12 W1.1 subsection (commit b52681d).
- [x] W3.4 Build + CI. Green run 40805451622 on a58d60b (130 pages, 0 undefined, 0 forbidden).

## W4 Introduction, positioning, decision guide, roadmap
- [~] W4.1 Introduction and scope (sec01): definitions and scope only, plus A rows for any literature claim. Drafted in sec01.
- [~] W4.2 Positioning vs existing reviews: only reviews present in the library or verified in the ledger. Drafted in sec02 ("Existing reviews and the contribution of this article", nonlocal/fractional/hyperbolic/generalized reviews cited from library).
- [~] W4.3 Decision guide "which theory for which regime": conditions from verified criteria only. Drafted in sec12 (sec:12.6 three questions + sec:12.5 comparability conditions).
- [~] W4.4 Benchmark list: checked sources only. Framework present in sec16 ("Reproducible numerical benchmarks", BM-1 scattering matrix, approaches, obstacles).
- [~] W4.5 Research roadmap built from the open items of W2. Present in sec16 ("Research roadmap from the Q3 evidence gaps", "Sequencing the programme", future-directions summary table).
- [~] W4.6 Conclusions mapped to A/V rows. Drafted in sec17.
- [x] W4.7 Build + CI. Green run 40805451622 on a58d60b.

## W5 Notation, abbreviations, figures
- [x] W5.1 (notation rows added 01cda7c; full master table not re-audited) Notation table (single table, all symbols used in sec 4 and sec 12).
- [x] W5.2 Abbreviation list (LS, GL, GN, DPL, TPL, MGT, MDD, CC, etc.) — phase5/master/frontmatter/acronyms.tex included at main.tex:112, complete.
- [x] W5.3 Figure and table captions: state the assumptions in each caption. Captions across sec01-sec12 state assumptions/limitations (e.g. fig01 arrows conceptual; fig07 dispersion curves correspond only to stated 1-D laws; fig11 no universal flux correction asserted; fig14 flux under stated outward-positive convention).
- [x] W5.4 Script-generated dispersion figure committed with its script: phase5/tools/plot_dispersion.py (stdlib-only PDF generator) + phase5/master/figures/source/fig_dispersion.pdf, referenced in sec07 as fig:dispersion.
- [ ] W5.5 Build + CI.

## W6 Close the open reviewer objections (dispositions documented in DECISIONS_FOR_AUTHOR.md and WP6_MOCK_REFEREE_REGISTER.csv)
- [~] W6.1 Reviewer 1: "generalized model balances" (primary-source derivations required). W3.1/W3.3 provide verified derivations; reduced flux J_i kept as explicitly qualified first-order wave-flux convention (DECISIONS_FOR_AUTHOR "Exact versus reduced energy flux"). WP6-01 ALREADY-ADDRESSED.
- [~] W6.2 Reviewer 1: fractional theory coupled constitutive formulation (CONDITIONAL). Sec 11.1 states fractional models are scalar endpoints, not coupled constitutive derivations; WP6-04 ALREADY-ADDRESSED.
- [~] W6.3 Reviewer 1: nonlocal boundary work (OPEN; derive per kernel/domain/BC). Scope limitation stated in sec07.4/7.5 ("no universal correction", boundary conditions kernel-specific); WP6-06 PARTLY-ADDRESSED, remains OPEN for full derivation.
- [~] W6.4 Reviewer 1: tables/compile proof and scientific verification — full-size figure proof (Q5). Compile + gates green; B5 (print-size table review) remains open in BLOCKERS.md; WP6-05 OPEN.
- [~] W6.5 Reviewer 2: review method and corpus protocol (OPEN). Corpus protocol documented; WP6-07 PARTLY-FIXED, WP6-08 LIMITATION (blank DOIs).
- [~] W6.6 Reviewer 2: DOI and source validation (use ledger rows). SOURCE_LEDGER empty fields filled (LazarAgiasofitou2022, Mindlin1974 tier); OCL-591 MGT DOI-conflict withdrawn (OCL-613); DOI resolution distinguished from page access (DECISIONS_FOR_AUTHOR); WP6-08 LIMITATION.
- [~] W6.7 Reviewer 2: figure rights and accuracy (OPEN; document source/licence unknown). WP6-11 DECISION (figures original vector graphics; rights not documented).
- [~] W6.8 Reviewer 2: artifact mismatch 161 vs 170 pages (OPEN; provenance). WP6-12 LIMITATION.
- [x] W6.9 Build + CI. Green run 40805451622 on a58d60b.

## Gates and close-out
- [ ] G1 After each content commit: CI green, pages, undefined refs, forbidden/privacy scans, ledger validator PASS.
- [ ] G2 Hostile self-re-read of each diff; 10-row spot-check against rendered PDF text.
- [ ] G3 AUTONOMY_LOG heartbeat every 2 h; 10-line entry every 3 commits.
- [ ] G4 06:00 IST: last CI green; FINAL_HANDOVER.md and TASK_QUEUE.md updated; final report.

## Status at close of this session (2026-10-29, past the 06:00 IST close-out)
- Done: W1.0–W1.5; W2.1–W2.9; W3.1 verified equation register (40 items, sanitized); W3.2 sec10 interface-partition worked example; W3.3 unified-reduction worked example; W3.4 CI green run 40805451622; EQ_ANCHORS amendment (eq:11.7 class A to ZAMP p.940 Eq.(15); eq:7.2 Aifantis 2003 p.263; eq:7.1 kernel normalised to unity; Eringen 1999 p.430 (4.2)); P0-1/P0-2/P1-1/P1-2 corrections; equation-difference hedges OCL-571..OCL-583; all 8 watch-fix items applied (incl. OCL-591 MGT DOI withdrawn via OCL-613, SOURCE_LEDGER empty rows filled, GN-III 1992 class B + MISSING_SOURCES, DPL cell names J. Heat Transfer 117:8-16).
- Partly done: W4.1/4.2/4.3/4.4/4.5/4.6 (drafted in sec01/sec02/sec12/sec16/sec17); W5.1 notation rows (partial); W5.2–W5.4 not started (W5.4 needs script figure + TeX, deferred); W6.01–W6.08 dispositions documented (register + DECISIONS_FOR_AUTHOR); W6.09 CI green.
- Not done: W5.2–W5.4 (abbreviation list, caption assumptions, script-generated figure); full W6 manuscript responses (dispositions recorded, not re-written into body); B2/B5/B6/B8 blockers.
- Blocked: B2 (Drive partial re-copy), B4 (CI logs not downloadable), B5 (print-size table review), B6 (6 missing sources), B8 (journal policies unread).
- Ledger: 613 rows (validator PASS after OCL-612/OCL-613). EQUATION_AUDIT.csv inventory PASS (137 active + 2 WITHHELD). references_local.bib: 147 entries.
- HEAD == remote == 397a57b. Last green content CI: run 40805451622 on a58d60b (130 pages, 0 undefined refs, 0 forbidden).
- Blocked: none — EQ_ANCHORS and SOURCE_LEDGER_PUBLIC part1-4 located on Drive and downloaded; sanitized SOURCE_LEDGER re-copy committed (e3c531a). Manual CI dispatch still refused (403); a content push is the only trigger.
- CI: last content run 40728656087 on b1055d8 success (126 pages, 0 undefined refs, 0 forbidden). Bot output commit pulled; local HEAD == remote HEAD == e3c531a.

## This session (continued 2026-10-28, branch arena/e6146644-le)
- Corrections committed: P0-1 Ezzat2011 held (batch B07 p.1), hedged class B; P0-2 both Tzou 1995 papers held; P1-1 Quintanilla DOI-conflict statement removed from Sec 12 text (bib keeps verified=NO per hygiene gate); P1-2 tau_m re-anchored from Eq. 4.18 to Eq. 12 template.
- Equation hedges with ledger rows OCL-571..OCL-583: eq:4.13, eq:4.21, eq:4.22, eq:3.22, eq:3.15, eq:7.1, eq:7.2, eq:11.2, eq:11.4.
- Ledger validator PASS (583 rows: A=67, B=133, C=333, V=50). EQUATION_AUDIT.csv line anchors fixed; inventory verifier PASS.
- W1.5 cell-by-cell audit done (bd0de3c, b1055d8; ledger rows OCL-584..OCL-595).
- Sanitized SOURCE_LEDGER re-copy committed (e3c531a): public SOURCE_LEDGER_PUBLIC part1-4 merged, local-only curated keys preserved, Iesan2013 duplicate dropped; 118 rows, notes_part column added.
- CI green on head: run 40728656087 (126 pages, 0 undefined refs, 0 forbidden); bot output pulled; local HEAD == remote HEAD == e3c531a.
- Next: W3.2 sec10 interface partition; W4.2/W4.4/W4.5; W5.2–W5.4; W6 open objections; then FINAL_HANDOVER.md/TASK_QUEUE.md/final report at 06:00 IST.
