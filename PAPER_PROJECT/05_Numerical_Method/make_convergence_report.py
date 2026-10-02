"""make_convergence_report.py — CONVERGENCE_REPORT.md and STABILITY_REPORT.md (Phase 9) from the analysis/convergence JSON files."""
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
def J(p):
    p = os.path.join(ROOT, p); return json.load(open(p)) if os.path.exists(p) else {}
AN = J('10_Processed_Data/ANALYSIS_V2.json'); CR = J('10_Processed_Data/CONVERGENCE_RESULTS.json'); CD = J('10_Processed_Data/CONVERGENCE_DIRS.json'); TR = {c['case']: c for c in J('07_Tests/TEST_RESULTS.json').get('cases', [])}
T4, circ = AN.get('T4_H2', {}), AN.get('circle_peak', {})
L = ['# CONVERGENCE_REPORT — Phase 9 (2026-10-01)', '',
     'Verification, not validation (§39). Grid families (γ = 5): radial R48/M/R192 = 48×96, 96×96, 192×96 and angular T48/M/T144 = 96×48, 96×96, 96×144. Production grid M. Richardson with the observed order bounded to [1, 3].', '',
     '## 1. Mesh-direction and clustering study (C4; ellipse φ = 30°, interpolated peak, MPa/K)', '', '| N_r × N_θ | γ = 3.5 | γ = 5 | γ = 6.5 |', '|---|---|---|---|']
def v(k): 
    x = CD.get(k, {}).get('sig_interp'); return f'{abs(x)/1e6:.4f}' if x else '—'
for nn in ('96x48', '192x48', '96x96', '96x144', '144x72', '192x96'):
    L.append(f"| {nn} | {v(nn + '_gam3.5')} | {v(nn + '_gam5')} | {v(nn + '_gam6.5')} |")
L += ['', 'Reading: at γ = 3.5, doubling N_r changes the peak by −8.7% and doubling N_θ by +3.0%; γ = 5 at 96×48 lowers it by 11.9%; γ = 6.5 differs from γ = 5 by 0.7%. The near-wall radial resolution controls the tip stress → γ = 5 (P9-D001). With γ = 3.5 the handoff-family triplets 48×24/96×48/192×96 have observed orders 0.8–1.35 (`09_Raw_Data/convergence_gamma3p5/`, not asymptotic).', '']
if T4.get('extrapolated_6phi'):
    e = T4['extrapolated_6phi']; b = e['budget']
    L += ['## 2. Production quantities (ellipse, 6 orientations, MPa/K)', '', '| φ | M | radial p | radial corr. | angular p | angular corr. | extrapolated |', '|---|---|---|---|---|---|---|']
    for ph in ('0', '30', '60', '90', '120', '150'):
        x = b.get(ph, {}); 
        L.append(f"| {ph} | {x.get('M', 0)/1e6:.4f} | {x.get('radial_p') if x.get('radial_p') is None else round(x['radial_p'], 2)} | {100*x.get('radial_corr_rel', 0):+.2f}% | {x.get('angular_p') if x.get('angular_p') is None else round(x['angular_p'], 2)} | {100*x.get('angular_corr_rel', 0):+.2f}% | {x.get('extrapolated', 0)/1e6:.4f} |")
    L += ['', f"Amplitude A_φ (six orientations): grid M {100*T4['M_6phi_interp']['amplitude']:.2f}%, R192 {100*T4['R192_6phi_interp']['amplitude']:.2f}%, T144 {100*T4['T144_6phi_interp']['amplitude']:.2f}%, extrapolated {100*e['amplitude']:.2f}%; twelve orientations on M {100*T4['amplitude_M_12phi']:.2f}%; **u_num = {100*T4['u_num']:.2f}%**; frozen threshold max(5 u_num, 2%) = {100*T4['threshold']:.2f}% → {T4['status']}.", '']
c = circ.get('radial_interp')
if c: L += ['## 3. Circle', '', f"Radial family at φ = 0: {[round(x/1e6, 4) for x in c['f']]} MPa/K (R48, M, R192), observed order {c.get('p')}, extrapolated {c.get('f_ext')/1e6:.4f} MPa/K; error of M {100*c.get('rel_err_mid'):+.2f}%, of R192 {100*c.get('rel_err_fine'):+.2f}%.", '']
if CR.get('C2'):
    L += ['## 4. Bromwich-plan independence (C2; ellipse φ = 90°, 96×48)', '', '| plan | peak change | series change | solves |', '|---|---|---|---|']
    for k, x in CR['C2'].items():
        if 'rel_diff_sig' in x: L.append(f"| {k} | {x['rel_diff_sig']:.2e} | {x['series_max_rel_diff']:.2e} | {x['n_solves']} |")
    L.append('')
if CR.get('C3'):
    L += ['## 5. Outer-radius (echo) sensitivity (C3; circle, 96×48 and 191×48)', '', '| a (nm) | echo round trip at R = 80a (t_th) | peak change R80→R160 | D(R80) | D(R160) | D change |', '|---|---|---|---|---|---|']
    for k, x in CR['C3'].items():
        L.append(f"| {k} | {x['R80a']['echo_roundtrip_t_th']:.2f} | {100*x['peak_change_R80_to_R160']:+.2f}% | {x['R80a']['D_t_le_6']:.3e} | {x['R160a']['D_t_le_6']:.3e} | {100*x['D_change_R80_to_R160']:+.1f}% |")
    L.append('')
L += ['## 6. Verification-level convergence orders', '', f"V8 steady gradient load: order {TR.get('V8_steady_thermal_gradient_load', {}).get('observed_order_48_to_96')}; V11 single pulse: orders {TR.get('V11_single_pulse_isotropic_circle_vs_time_domain', {}).get('order_48_96')}, {TR.get('V11_single_pulse_isotropic_circle_vs_time_domain', {}).get('order_96_192')}; V9d dynamic coupled: min order {TR.get('V9d_time_domain_peak_and_series_vs_1D', {}).get('min_order_peak_48_96')}.", '']
open(os.path.join(ROOT, '05_Numerical_Method', 'CONVERGENCE_REPORT.md'), 'w').write('\n'.join(L) + '\n')
S = ['# STABILITY_REPORT — Phase 9 (2026-10-01)', '',
     f"- Solver backward error (relative, after 2 refinement steps): max over all production runs = {AN.get('numerics', {}).get('max_backward_error')}; wall-pulse reconstruction error: max = {AN.get('numerics', {}).get('max_wall_pulse_error')} (≤ 6.3e-9, inversion check in every run).",
     '- Inversion plan: alias e^{−γ_B T} = 1.5e-8; round-off growth e^{γ_B t} ≤ 5e4 up to t = 12 (negligible vs 1e-16 × condition); plan independence C2 above.',
     '- Resonance handling: the undamped finite domain has real-axis resonances; the contour Re s = γ_B = 0.9/t_th keeps the integrand smooth (frequency spacing 0.31 < 0.9). No damping device is used.',
     '- Conjugate symmetry H(s̄) = conj H(s): 1.7e-15 (V12). τ → 0 limit: 4e-7 (V5). Rotation covariance 6e-14 (V3).',
     '- Memory: 192×96 solves need ≈ 0.7–1.0 GB (one such job at a time in the 2 GB environment); the single out-of-memory event (verification run 2) was a scheduling error, not a numerical instability.',
     '- Condition number: not computed explicitly (the refinement experiment shows the forward-error floor 1e-8 → 1e-14, which bounds the effective conditioning).']
open(os.path.join(ROOT, '05_Numerical_Method', 'STABILITY_REPORT.md'), 'w').write('\n'.join(S) + '\n')
print('convergence + stability reports written')
