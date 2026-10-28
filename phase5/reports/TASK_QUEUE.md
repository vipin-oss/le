# Task queue — overnight writing session (R4B-NIGHT-WRITE)

Branch: `arena/36bc8cc8-le` (branch of record). Started 2026-10-28 ~21:00 IST. End 06:00 IST.
Rule: writing items first; each content commit = one CI run; docs-only commits do not build.
If this session dies, resume from this file plus `AUTONOMY_LOG.md`.

Status key: `[ ]` open, `[~]` in progress, `[x]` done (commit id in brackets), `[!]` blocked (see BLOCKERS.md).

## W1 Unified framework (Q1)
- [x] W1.0 Verifier `verify_unified_reductions.py` runs (needs sympy; installed in /tmp venv, not in repo). Output: PASS for all reduction checks.
- [x] W1.1 (046b8a3) Add subsection "One template and stepwise reductions" to `sec12_comparative.tex` (before 12.4): template statement (definition), per-reduction steps, negative cases.
- [x] W1.2 (OCL-535..548) Add ledger V rows for every new W1.1 claim (resolved_by = verifier line ranges; evidence_mode = SYMPY-...).
- [x] W1.3 (01cda7c) Notation mapping table: template symbol ↔ family symbol (LS, DPL, TPL, MGT, GN, MDD, fractional, nonlocal).
- [x] W1.4 (CI 40716977248, 40717508285) Build + CI on the W1 content commit (batched with W2 if sections are small).
- [ ] W1.5 Comparison table cells audit: every cell class A/V or explicitly "model-dependent" (Table in sec12, `tab:limiting_cases_revisited`).

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
- [ ] W3.1 List the ~40 VERIFIED displays from EQUATION_AUDIT.csv (status VERIFIED-*); for each, assumptions, steps, limits (text only where a script or source supports the step).
- [ ] W3.2 Worked example for Sec 10 interface partition (from verify_interface_energy.py / verify_interface_mode_counts.py).
- [ ] W3.3 Worked example for one unified reduction (from W1.1).
- [ ] W3.4 Build + CI.

## W4 Introduction, positioning, decision guide, roadmap
- [ ] W4.1 Introduction and scope (sec01): definitions and scope only, plus A rows for any literature claim.
- [ ] W4.2 Positioning vs existing reviews: only reviews present in the library or verified in the ledger.
- [ ] W4.3 Decision guide "which theory for which regime": conditions from verified criteria only.
- [ ] W4.4 Benchmark list: checked sources only.
- [ ] W4.5 Research roadmap built from the open items of W2.
- [ ] W4.6 Conclusions mapped to A/V rows.
- [ ] W4.7 Build + CI.

## W5 Notation, abbreviations, figures
- [~] W5.1 (notation rows added 01cda7c; full master table not re-audited) Notation table (single table, all symbols used in sec 4 and sec 12).
- [ ] W5.2 Abbreviation list (LS, GL, GN, DPL, TPL, MGT, MDD, CC, etc.).
- [ ] W5.3 Figure and table captions: state the assumptions in each caption.
- [ ] W5.4 Replace any overclaiming figure with a script-generated figure (dispersion or wave-speed or flux-channel plot), committed with its script.
- [ ] W5.5 Build + CI.

## W6 Close the open reviewer objections
- [ ] W6.1 Reviewer 1: "generalized model balances" (OPEN; primary-source derivations required) — check whether W3 closes it.
- [ ] W6.2 Reviewer 1: fractional theory coupled constitutive formulation (CONDITIONAL, still open).
- [ ] W6.3 Reviewer 1: nonlocal boundary work (OPEN; derive per kernel/domain/BC) — write scope limitation if not derivable.
- [ ] W6.4 Reviewer 1: tables/compile proof and scientific verification — full-size figure proof (Q5).
- [ ] W6.5 Reviewer 2: review method and corpus protocol (OPEN).
- [ ] W6.6 Reviewer 2: DOI and source validation (OPEN; use ledger rows).
- [ ] W6.7 Reviewer 2: figure rights and accuracy (OPEN; document source/licence unknown).
- [ ] W6.8 Reviewer 2: artifact mismatch 161 vs 170 pages (OPEN; provenance).
- [ ] W6.9 Build + CI.

## Gates and close-out
- [ ] G1 After each content commit: CI green, pages, undefined refs, forbidden/privacy scans, ledger validator PASS.
- [ ] G2 Hostile self-re-read of each diff; 10-row spot-check against rendered PDF text.
- [ ] G3 AUTONOMY_LOG heartbeat every 2 h; 10-line entry every 3 commits.
- [ ] G4 06:00 IST: last CI green; FINAL_HANDOVER.md and TASK_QUEUE.md updated; final report.
