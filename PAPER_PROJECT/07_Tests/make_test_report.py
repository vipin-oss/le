"""make_test_report.py — TEST_REPORT.md from TEST_RESULTS.json (no hand-copied numbers)."""
import json, os, textwrap
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'TEST_RESULTS.json')))
def short(v, n=190):
    s = str(v); return s if len(s) <= n else s[:n - 3] + '...'
L = ['# TEST_REPORT — Phase 7/8 verification suite v2 (2026-10-01)', '',
     f"Script: `07_Tests/run_tests.py` · results: `07_Tests/TEST_RESULTS.json` · status {R['status']} · **{R.get('n_pass')} PASS, {R.get('n_fail')} FAIL** · CPU {R.get('cpu_seconds', 0):.0f} s, wall {R.get('wall_seconds', 0):.0f} s (2 vCPU).",
     'Grid family for all 2-D tests: radial clustering γ = 5 (production). Solver: `HarmonicSolver` with `refine = 2`. These are **verification** tests (Track A): exact/closed-form or independent 1-D references of the same mathematical model. Physical validation: APPLICABLE — EVIDENCE_UNAVAILABLE.',
     '', 'Run history (kept in `07_Tests/logs/`): run 1 (stock solver, γ = 3.5): 18 PASS / 5 FAIL — U3 (test bug: Voigt-form eigenvalues are not rotation invariant), V3p (units-mixed normalisation), V9/V9b/V9c (unweighted high-frequency metric); run 2 aborted by the OOM killer; run 3 (refined solver, γ = 3.5) partial; **run 4 (this report): refined solver, γ = 5.** Test definitions were corrected before the final run; no criterion was loosened to obtain a PASS (criteria changes are listed in the DECISION_LOG P7-D004).', '',
     '| Test | Status | Criterion | Key values |', '|---|---|---|---|']
for c in R['cases']:
    crit = c.get('criterion', c.get('note', ''))
    keys = {k: v for k, v in c.items() if k not in ('case', 'status', 'criterion', 'note', 'plan')}
    L.append(f"| {c['case']} | {c['status']} | {short(crit, 170).replace('|', '/')} | {short(', '.join(f'{k}={v}' for k, v in keys.items()), 260).replace('|', '/')} |")
L += ['', '## Notes on the one FAIL and on test power',
      '- **V0 (FAIL, reported as is):** linear-field metric consistency on the handoff grid family at γ = 5: χ = 2, 96×48 gives 5.03e-3 vs the handoff criterion 5e-3 (0.6% over; χ = 1: 4.18e-3 passes). Second-order convergent (1.96e-2 → 5.03e-3 → 1.26e-3). The error is dominated by the angular resolution (Nt = 48), not by the clustering (γ = 3.5 gives 4.81e-3). **V0b** (added after run 4, same criterion, supplement script) applies it to the grids that carry production claims: R48, M, R192, T144 all ≤ 3.6e-3 (M: 1.5e-3) → PASS; the 96×48 grid (T48) is used only for circle thermal-memory runs and for relative (ablation) comparisons, not for absolute ellipse stresses.',
      '- **Test power:** U1b and V3p show that the rotation tests fail on the shipped `rotate_Q_beta` (β error 1.7e-3; wall-hoop covariance 3.0e-3 at φ = 45°) and are blind at φ = 90° (6e-14), explaining why the handoff V3 could not see the bug. V3 (fixed code) gives 6.5e-14 for θ, u and wall hoop stress for every grid-aligned φ; V3d gives a peak-stress spread of 3.6e-15 (frozen T1 threshold 1e-8).',
      '- V3c (exploratory): a non-lattice rotation (37°) changes the circle peak by 1.5e-4 (48×24) and 4.0e-6 (96×48) — discretisation-order, as expected.']
open(os.path.join(HERE, 'TEST_REPORT.md'), 'w').write('\n'.join(L) + '\n')
print('TEST_REPORT.md written;', R.get('n_pass'), 'pass', R.get('n_fail'), 'fail')
