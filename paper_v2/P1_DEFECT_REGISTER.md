# P1 Defect Register (initial, scripts and build) - 2026-10-30

Scope done so far: ran all 12 check/bench/table scripts and all 23 figure scripts in a clean scratch copy; read their outputs; independently re-computed the Cattaneo benchmark with mpmath. Scope NOT done yet: page-by-page audit of the 134 pages (equations, signs, notation, assumptions), independent re-derivation of the central results, claim-level review.

| ID | Severity | Location | Finding | Status |
|---|---|---|---|---|
| D1 | Medium | scripts/bench_schemes.py (print line) | Printed "exact theta at x=1,3,4.9" used wrong array indices (2.16, 1.39, 0.84). Independent mpmath inversion confirms the manuscript values (1.7615, 0.5923, 0.0959 at t=5) are correct; only the script print was wrong. Front jump printed with wrong exponent (x=4.9 instead of t=5): now exp(-t/2tau)=0.0821 as in s14b | FIXED (script now prints the correct values) |
| D2 | High | main.tex l.41; s01_intro l.55; s05_hyperbolic l.60; s16_synthesis l.97 (also abstract, s17_open) | Overbroad wording "one coupled dispersion polynomial / share one dispersion polynomial". Not valid for exact delays, fractional powers, hereditary kernels, layered/periodic media (Blueprint Sec. 3) | OPEN (rewrite in P1) |
| D3 | High | scripts/check_*.py, bench_*.py (9 files) | No assertions or coded tolerances: every check prints numbers and a human reads them. A check can silently fail | OPEN (add asserts and a tolerance log) |
| D4 | Medium | scripts/ | No pinned environment before this register. Added scripts/requirements.txt (numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, matplotlib 3.11.2, sympy 1.14.0). Needs a clean-environment run and archive checksums | PARTIAL |
| D5 | High | refs_extra.bib (32), refs_new.bib (41 first-author-only), Bleustein1968, Gulyaev1969 | Records not verified (R0/incomplete) | OPEN (P2) |
| D6 | Medium | Appendix D | About 65 entries appear only in the catalogue, not in the text | OPEN (P2) |
| D7 | Medium | s16b_atlas | 17-row atlas about 15/17 own-group papers; to be replaced by the Blueprint atlas (13 fields) | OPEN (P5) |
| D8 | Low | main_els.tex | Never compiled (no elsarticle here); paused until journal is chosen | OPEN |
| D9 | Low | main.log | A TeX message line starting with "! \OML ... c[] +" appears in the log without stopping the build; cause not identified (a table cell near s13_multiphysics) | OPEN (investigate) |
| D10 | Info | scripts | All 12 check/bench/table scripts and all 23 figure scripts exit with code 0 in a clean scratch copy | Observed |

Next in P1: (a) add assertions with tolerances to the 9 check/bench scripts and write a machine-readable pass/fail log; (b) rewrite D2 wording; (c) page-by-page audit with an equation and notation list; (d) independent re-derivation of the central dispersion and reflection results with a second method.
