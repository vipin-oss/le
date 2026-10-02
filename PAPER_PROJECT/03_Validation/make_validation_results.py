"""make_validation_results.py — VALIDATION_RESULTS.md (Phase 8) and VALIDATION_STATUS.md from the verification test results."""
import json, os
def _pp_root(_start):
    """walk up from _start to the PAPER_PROJECT directory (path-independent replacement
    for the hard-coded '/home/user/PAPER_PROJECT' that used to be here)."""
    _p = os.path.abspath(_start)
    while True:
        if os.path.basename(_p) == 'PAPER_PROJECT':
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            break
        _p = _q
    return os.environ.get('PAPER_PROJECT_ROOT', '/home/user/PAPER_PROJECT')
ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__)))
R = {c['case']: c for c in json.load(open(os.path.join(ROOT, '07_Tests', 'TEST_RESULTS.json')))['cases']}
def g(case, key, default='n/a'): return R.get(case, {}).get(key, default)
def st(case): return R.get(case, {}).get('status', 'NOT_RUN')
rows = [
 ('R1', 'steady log temperature profile (ω→0, β=0, isotropic circle, clamped R=80a)', 'closed form ln(R/r)/ln(R/a)', 'V6_steady_log_law', f"max |θ error| (48/96/192) = {g('V6_steady_log_law','max_abs_err_48_96_192')}"),
 ('R2', 'static uniform-θ annulus hoop stress (isotropic)', 'closed form (Lamé)', 'V7_static_uniform_theta_annulus', f"rel. error (48/96/192) = {g('V7_static_uniform_theta_annulus','rel_err_48_96_192')}"),
 ('R3', 'steady thermal-gradient load, wall hoop stress (isotropic, clamped R=80a)', 'closed form Lamé + log profile (−1,234,746 Pa/K)', 'V8_steady_thermal_gradient_load', f"rel. error (48/96/192/384) = {g('V8_steady_thermal_gradient_load','rel_err_48_96_192_384')}; order {g('V8_steady_thermal_gradient_load','observed_order_48_to_96')}"),
 ('R4', '1-D Chebyshev reference (steady) vs closed form', 'closed form', 'U7_ref1d_spectral_steady_closed_form', f"rel. error = {g('U7_ref1d_spectral_steady_closed_form','rel_err')}"),
 ('R5', 'Laplace-domain 1-D reference + Bromwich vs time-domain Crank–Nicolson heat solve + Lamé stress', 'independent time integration', 'U8_bromwich_vs_time_domain_Crank_Nicolson', f"rel. error = {g('U8_bromwich_vs_time_domain_Crank_Nicolson','rel_err')}"),
 ('R6', 'single-pulse isotropic circle (2-D mapped FD + Bromwich, inertia off, uncoupled) vs time-domain reference', 'independent time-domain 1-D solution', 'V11_single_pulse_isotropic_circle_vs_time_domain', f"peak error (48/96/192) = {g('V11_single_pulse_isotropic_circle_vs_time_domain','peak_rel_err_48_96_192')}; orders {g('V11_single_pulse_isotropic_circle_vs_time_domain','order_48_96')}, {g('V11_single_pulse_isotropic_circle_vs_time_domain','order_96_192')}"),
 ('R7', 'dynamic coupled problem (inertia + feedback ON), Fourier/CV/MCV3: pulse-weighted spectral error', 'independent 1-D Chebyshev spectral solution', 'V9a_weighted_spectral_error_vs_1D', f"{g('V9a_weighted_spectral_error_vs_1D','weighted_errs')}"),
 ('R8', 'dynamic coupled wall-hoop series and peak (t≤6)', 'independent 1-D spectral + same Bromwich plan', 'V9d_time_domain_peak_and_series_vs_1D', f"peak errors {g('V9d_time_domain_peak_and_series_vs_1D','peak_errs')}"),
 ('R9', 'thermal-memory deviation D accuracy (CV5, CV20 vs Fourier)', '1-D reference D', 'V9e_thermal_memory_deviation_D_accuracy', f"{g('V9e_thermal_memory_deviation_D_accuracy','detail')}"),
]
L = ['# VALIDATION_RESULTS — Phase 8 (2026-10-01)', '',
     '**Scope statement (MASTER_PROMPT §12–14, §38).** Everything below is *verification* (Track A): comparison of the code with exact or independent numerical solutions of the SAME mathematical model. No experiment, measured physical quantity or physical benchmark was compared. **Physical validation: APPLICABLE — EVIDENCE_UNAVAILABLE** (no transient cavity measurements for β-Ga₂O₃ are known; the user directive D012 accepts limiting-case and source-case verification, which is what is reported). Validated scope: none (no physical-validation claim is made).', '',
     'Source-case pilot (Huang et al. 2025 benchmark family; handoff `PILOT_HUANG_2025_01/`): **PILOT — NOT FINAL VALIDATION**, 175/177 digitised points within the envelope (handoff-recorded); NOT re-executed here (the private digitisation `reference_local/` is not in the package); its code is independent of the cavity solver, so it supports confidence in the operator family only.', '',
     '| ID | Quantity compared | Reference | Test | Result | Status |', '|---|---|---|---|---|---|']
for rid, q, ref, case, res in rows:
    L.append(f"| {rid} | {q} | {ref} | {case} | {str(res)[:330].replace('|','/')} | {st(case)} |")
L += ['', 'Numerical uncertainty note (§38): the 2-D comparisons are preliminary until the grid study of Phase 9 (`05_Numerical_Method/CONVERGENCE_REPORT.md`) has been applied; the isotropic-circle errors above are the grid errors of the production discretisation for that case.']
open(os.path.join(ROOT, '03_Validation', 'VALIDATION_RESULTS.md'), 'w').write('\n'.join(L) + '\n')
print('VALIDATION_RESULTS.md written')
