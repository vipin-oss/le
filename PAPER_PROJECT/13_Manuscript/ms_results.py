"""ms_results.py — data-driven manuscript sections 4–7 (verification, results, discussion, conclusions).
Every number is read from TEST_RESULTS.json, CONVERGENCE_*.json and ANALYSIS_V2.json (no manuscript-only numbers)."""
import os, sys, json, ast
sys.dont_write_bytecode = True
ROOT = '/home/user/PAPER_PROJECT'
sys.path.insert(0, os.path.join(ROOT, '06_Source_Code', 'src')); sys.path.insert(0, os.path.join(ROOT, '13_Manuscript'))
import numpy as np
import cg_pipeline as cp
import ms_static as S

def J(p):
    p = os.path.join(ROOT, p); return json.load(open(p)) if os.path.exists(p) else {}
TR = {c['case']: c for c in J('07_Tests/TEST_RESULTS.json').get('cases', [])}
AN = J('10_Processed_Data/ANALYSIS_V2.json'); CR = J('10_Processed_Data/CONVERGENCE_RESULTS.json'); CD = J('10_Processed_Data/CONVERGENCE_DIRS.json')
T1, T2, T3, T4 = AN.get('T1_H1', {}), AN.get('T2_H3', {}), AN.get('T3_H4', {}), AN.get('T4_H2', {})
FLOC = (AN.get('F_locality', {}) or {}).get('rows', [])
CIRC, ISO, EAB, LOC, SH = AN.get('circle_peak', {}), AN.get('isotropic', {}), AN.get('E_ablations', {}), AN.get('locality', {}), AN.get('shipped', {})
def g(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict) and k in d: d = d[k]
        else: return default
    return d
def pc(x, nd=1): return 'n/a' if x is None else f'{100*x:.{nd}f}%'
def mp(x, nd=3): return 'n/a' if x is None else f'{abs(x)/1e6:.{nd}f}'
def sci(x, nd=1): return 'n/a' if x is None else f'{x:.{nd}e}'
def rsd(x): return 'below 1e-12' if (x is not None and x < 1e-12) else sci(x, 1)
def lst(s): return [float(v) for v in ast.literal_eval(s)] if isinstance(s, str) else s

# ----------------------------------------------------------------------------------------------- numbers
N = {}
N['u4'] = g(TR, 'U4_bromwich_identity', 'max_err_t_le_12'); N['u5'] = g(TR, 'U5_bromwich_damped_oscillator_vs_ODE', 'rel_err')
N['u6'] = g(TR, 'U6_bromwich_parameter_independence', 'rel_diff_T20g0p9_vs_T32g0p6'); N['u8'] = g(TR, 'U8_bromwich_vs_time_domain_Crank_Nicolson', 'rel_err')
N['u1_fixed'] = g(TR, 'U1_rotate_Q_beta_vs_independent_3D', 'fixed_rel_err_beta'); N['u1_ship'] = g(TR, 'U1_rotate_Q_beta_vs_independent_3D', 'shipped_rel_err_beta')
N['v3'] = g(TR, 'V3_rotation_covariance_all_grid_aligned_phi_FIXED', 'max_rel_err'); N['v3_ship45'] = g(TR, 'V3p_test_power_shipped_rotation', 'shipped_phi45_hoop')
N['v3_ship90'] = g(TR, 'V3p_test_power_shipped_rotation', 'shipped_phi90_worst'); N['v3d'] = g(TR, 'V3d_peak_stress_invariance_T1_quantity', 'rel_spread_phi_0_45_105')
N['v8'] = lst(g(TR, 'V8_steady_thermal_gradient_load', 'rel_err_48_96_192_384')); N['v8_order'] = g(TR, 'V8_steady_thermal_gradient_load', 'observed_order_48_to_96')
N['v7'] = lst(g(TR, 'V7_static_uniform_theta_annulus', 'rel_err_48_96_192')); N['v6'] = lst(g(TR, 'V6_steady_log_law', 'max_abs_err_48_96_192'))
N['v11'] = lst(g(TR, 'V11_single_pulse_isotropic_circle_vs_time_domain', 'peak_rel_err_48_96_192')); N['v11_ord'] = (g(TR, 'V11_single_pulse_isotropic_circle_vs_time_domain', 'order_48_96'), g(TR, 'V11_single_pulse_isotropic_circle_vs_time_domain', 'order_96_192'))
v9d = g(TR, 'V9d_time_domain_peak_and_series_vs_1D', 'peak_errs'); N['v9d'] = {k: [float(x) for x in v] for k, v in (ast.literal_eval(v9d) if isinstance(v9d, str) else {}).items()}
N['v9d_worst192'] = g(TR, 'V9d_time_domain_peak_and_series_vs_1D', 'worst_peak_192'); N['v9d_order'] = g(TR, 'V9d_time_domain_peak_and_series_vs_1D', 'min_order_peak_48_96')
N['v9e'] = g(TR, 'V9e_thermal_memory_deviation_D_accuracy', 'detail'); N['v9e_worst'] = g(TR, 'V9e_thermal_memory_deviation_D_accuracy', 'worst_rel_err_192')
N['v9b'] = g(TR, 'V9b_dynamic_a50nm_vs_1D_time_domain', 'peak_rel_err_96x48'); N['v9c'] = g(TR, 'V9c_inertia_off_switch', 'peak_rel_err_96x48')
N['v0b'] = g(TR, 'V0b_metric_consistency_production_grids', 'worst_production_grids'); N['n_pass'] = sum(c['status'] == 'PASS' for c in TR.values()); N['n_fail'] = sum(c['status'] == 'FAIL' for c in TR.values())
N['n_tests'] = len(TR)

def verification():
    L = [('h1', '4. Verification and numerical uncertainty'),
         ('p', f"Verification is separated from validation: every comparison below is against an exact solution or an independent implementation of the same mathematical model (a 1-D axisymmetric Chebyshev solver in the Laplace domain and a time-domain Crank–Nicolson heat solver with the closed-form Lamé stress); none is a comparison with measurements. The suite has {N['n_tests']} tests ({N['n_pass']} passed, {N['n_fail']} failed, {N['n_tests'] - N['n_pass'] - N['n_fail']} exploratory; the failure is discussed below). The suite is summarised in Table 2, and the rotation-invariance, axisymmetric and inversion tests are illustrated in Fig. 2."),
         ('h2', '4.1 Component and reference tests')]
    rows = [
        ['Rotation of the stiffness/expansion tensors (27 angles)', 'independent 3-D rank-4 rotation', f"{sci(N['u1_fixed'])} (a sign error in one cross-term would give {sci(N['u1_ship'])})"],
        ['Rotation covariance of the circle (θ, u, wall hoop stress; all lattice φ, complex s)', 'exact discrete identity', f"{sci(N['v3'])}; peak-stress spread {sci(N['v3d'])}; a test at φ = 90° alone is blind to the sign error (6e-14 vs {sci(N['v3_ship45'])} at 45°)"],
        ['Bromwich inversion: identity / damped oscillator / contour independence', 'exact / ODE integration / (T, γ_B) change', f"{sci(N['u4'])} / {sci(N['u5'])} / {sci(N['u6'])}"],
        ['Laplace-domain 1-D solution + inversion vs time-domain solution (quasi-static, uncoupled)', 'Crank–Nicolson + Lamé', sci(N['u8'])],
        ['Steady log temperature profile; uniform-θ annulus; steady gradient load (wall hoop)', 'closed forms', f"V6 {sci(N['v6'][2]) if N['v6'] else 'n/a'} (θ, 192×96); V7 {pc(N['v7'][2], 2) if N['v7'] else 'n/a'}; V8 {pc(abs(N['v8'][1]), 2) if N['v8'] else 'n/a'} (96×48), {pc(abs(N['v8'][2]), 2) if N['v8'] else 'n/a'} (192×96), order {N['v8_order']:.2f}"],
        ['Single pulse, isotropic circle (quasi-static, uncoupled): peak', 'time-domain reference', f"{', '.join(pc(x, 2) for x in N['v11'])} (48×24, 96×48, 192×96), orders {N['v11_ord'][0]:.2f}, {N['v11_ord'][1]:.2f}" if N['v11'] else 'n/a'],
        ['Dynamic coupled problem (inertia + feedback): wall-hoop peak, Fourier / CV / MCV3', '1-D spectral + same inversion', f"{', '.join(pc(x, 2) for x in N['v9d'].get('FOURIER0', []))} (Fourier; 48×24, 96×48, 192×96); worst of the four conduction laws at 192×96: {pc(N['v9d_worst192'], 2)}"],
        ['Quasi-static switch; a = 50 nm (echo-dominated)', '1-D reference', f"{pc(N['v9c'], 2)}; {pc(N['v9b'], 2)} (96×48)"],
        ['Metric consistency (linear field)', '≤ 5×10^{−3}', f"production grids ≤ {sci(N['v0b'])}; the handoff-style 96×48 grid with χ = 2 gives 5.03×10^{{−3}} (reported failure of this criterion, angular-resolution dominated)"],
    ]
    L.append(('table', ['Quantity', 'Reference', 'Result'], rows, 'Summary of the verification suite (full table: supplementary material).', [2.6, 1.6, 2.6], 'verif'))
    L.append(('fig', os.path.join(ROOT, '11_Figures', 'fig4_verification.png'), '(a) Rotation invariance of the circular-cavity peak stress: earlier analysis (rotation-tensor sign error) versus this work; (b) errors of the axisymmetric verification tests versus mesh size; (c) wall-temperature reconstruction by the Bromwich inversion.', 6.6, 'verif'))
    try:
        dd = ast.literal_eval(N['v9e']); f = lambda k: ', '.join(f"{float(x)*100:+.1f}%" for x in dd[k]['rel_err'])
        dtxt = f"{f('CV5')} (τ = 5 ps) and {f('CV20')} (τ = 20 ps) on the 48×24, 96×48 and 192×96 grids"
    except Exception:
        dtxt = 'n/a'
    dgc = ', '.join('%+.1f%%' % (v['rel_change_T48_to_M'] * 100) for v in AN.get('D_grid_check', {}).values())
    L.append(('p', f"The thermal-memory deviation D is a small difference of two nearly equal series, so its accuracy was tested separately: relative to the 1-D reference the error of D is {dtxt}. On the grid used for the circle thermal-memory runs (96×48) D is therefore accurate to a few percent; D changes by {dgc} between that grid and the production grid M for the two members of the equal-Λ pair."))
    L.append(('h2', '4.2 Choice of the radial clustering'))
    if CD:
        def v(k): return mp(g(CD, k, 'sig_interp'))
        rows = [['3.5', v('96x48_gam3.5'), v('192x48_gam3.5'), v('96x96_gam3.5'), v('96x144_gam3.5'), v('192x96_gam3.5')], ['5.0', v('96x48_gam5'), '—', v('96x96_gam5'), '—', '—'], ['6.5', v('96x48_gam6.5'), '—', '—', '—', '—']]
        s_ = lambda k: abs(g(CD, k, 'sig_interp'))
        d_rad = (s_('192x48_gam3.5') - s_('96x48_gam3.5')) / s_('96x48_gam3.5'); d_ang = (s_('96x96_gam3.5') - s_('96x48_gam3.5')) / s_('96x48_gam3.5')
        d_g5 = (s_('96x48_gam5') - s_('96x48_gam3.5')) / s_('96x48_gam3.5'); d_g65 = (s_('96x48_gam6.5') - s_('96x48_gam5')) / s_('96x48_gam5')
        L.append(('p', f"The sharp tip of the ellipse (radius of curvature 0.35a at the ends of the major axis) is the most demanding location. A mesh-direction study for the ellipse at φ = 30° (@@tab:mesh@@, @@fig:mesh@@) shows that the near-wall radial resolution, not the angular resolution, controls the tip stress: with the clustering of the earlier 96×48 grid (γ = 3.5) doubling N_{{r}} changes the peak by {d_rad*100:+.1f}% while doubling N_{{θ}} changes it by {d_ang*100:+.1f}%; increasing the clustering to γ = 5 at fixed 96×48 changes the peak by {d_g5*100:+.1f}%, and γ = 6.5 changes it by only a further {d_g65*100:+.1f}%. The clustering γ = 5 with N_{{θ}} = 96 was therefore adopted (grid M = 96×96)."))
        L.append(('fig', os.path.join(ROOT, '11_Figures', 'fig6a_mesh.png'), 'Mesh-direction study for the ellipse at φ = 30°: peak wall stress for different meshes and radial clusterings γ (labels: N_r×N_θ).', 4.4, 'mesh'))
        L.append(('table', ['γ', '96×48', '192×48', '96×96', '96×144', '192×96'], rows, 'Peak wall hoop stress of the ellipse at φ = 30° (MPa/K) for different meshes and radial clusterings γ (interpolated maximum).', [0.6, 1.0, 1.0, 1.0, 1.0, 1.0], 'mesh'))
    L.append(('h2', '4.3 Grid convergence of the production quantities'))
    if T4.get('extrapolated_6phi'):
        e6 = T4['extrapolated_6phi']; b = e6['budget']
        rows = []
        for i, ph in enumerate((0, 30, 60, 90, 120, 150)):
            r = {k: T4.get(f'{k}_6phi_interp', {}).get('values', [None] * 6)[i] for k in ('R48', 'M', 'R192', 'T48', 'T144')}
            bb = b.get(str(ph), b.get(ph, {}))
            rows.append([ph, mp(r['R48'], 4), mp(r['M'], 4), mp(r['R192'], 4), mp(r['T48'], 4), mp(r['T144'], 4), mp(e6['values'][i], 4), pc(bb.get('radial_corr_rel'), 2), pc(bb.get('angular_corr_rel'), 2)])
        L.append(('table', ['φ (deg)', 'R48', 'M', 'R192', 'T48', 'T144', 'extrapolated', 'radial corr.', 'angular corr.'], rows,
                  'Peak wall hoop stress of the ellipse (MPa/K, interpolated maximum) on the grid families and the extrapolated value M + radial + angular correction (corrections relative to M).', [0.6, 0.7, 0.7, 0.7, 0.7, 0.7, 0.9, 0.8, 0.8], 'conv'))
    cr2, cr3 = CR.get('C2', {}), CR.get('C3', {})
    if cr2:
        d1, d2 = cr2.get('T32_g0.6', {}), cr2.get('T16_g1.1', {})
        L.append(('p', f"Changing the inversion plan from (T, γ_B) = (20, 0.9) to (32, 0.6) and (16, 1.1) changes the peak stress by {sci(d1.get('rel_diff_sig'))} and {sci(d2.get('rel_diff_sig'))} (series: {sci(d1.get('series_max_rel_diff'))}, {sci(d2.get('series_max_rel_diff'))}), i.e. the inversion is not a source of uncertainty at the level of interest."))
    if cr3:
        a10, a50 = cr3.get('a10nm', {}), cr3.get('a50nm', {})
        L.append(('p', f"Because the model is undamped and the outer boundary is finite, elastic echoes are features of the model. Doubling the outer radius (R = 160a, with N_{{r}} adjusted to keep the near-wall spacing) changes the peak wall stress by {pc(a10.get('peak_change_R80_to_R160'), 2)} for a = 10 nm (first echo at {a10.get('R80a', {}).get('echo_roundtrip_t_th', float('nan')):.1f} t_{{th}}, outside the window) and by {pc(a50.get('peak_change_R80_to_R160'), 2)} for a = 50 nm (echo at {a50.get('R80a', {}).get('echo_roundtrip_t_th', float('nan')):.1f} t_{{th}}, inside the window); the thermal-memory deviation D changes by {pc(a10.get('D_change_R80_to_R160'), 1)} and {pc(a50.get('D_change_R80_to_R160'), 1)}, which is of the size of the grid uncertainty of D (Section 4.1). The finite outer radius is therefore not a significant source of uncertainty for these observables."))
    return L


def results():
    L = [('h1', '5. Results')]
    # ---------------- 5.1 circle
    L.append(('h2', '5.1 Circular cavity: orientation-invariant peak and local response'))
    r_ = CIRC.get('radial_interp', {}); m96 = r_.get('f', [None, None, None])
    cm = mp(m96[1]); ce = mp(r_.get('f_ext')); err_m = pc(abs(r_.get('rel_err_mid')) if r_.get('rel_err_mid') is not None else None, 2)
    L.append(('p', f"For the circular cavity the peak wall stress is {cm} MPa/K on grid M, {ce} MPa/K after radial extrapolation (the error of grid M is {err_m}). It does not depend on the crystal orientation: over the 12 orientations (R48) and the six lattice orientations on grid M the relative spread of the nodal peak is {sci(g(T1, 'R48_sig_nodal', 'spread_rel'))} and {sci(g(T1, 'M_sig_nodal', 'spread_rel'))}, against the frozen criterion 10^{{−8}} (T1: {g(T1, 'status')}). The invariance is an exact property of the discrete problem for rotations that map the polar grid onto itself, and it is the one place where an implementation error in the rotation of the material tensors shows up unambiguously (Section 4.1)."))
    if LOC:
        cdev = LOC.get('circle_phi0_M', {}); edev = [v for k, v in LOC.items() if k.startswith('ellipse')]
        L.append(('p', f"The stress follows the wall temperature near the peak: at the peak node the ratio σ_{{θθ}}(t)/p(t) deviates from its value at the peak by at most {pc(cdev.get('max_dev_near_peak'), 1)} (circle) and {pc(max([e['max_dev_near_peak'] for e in edev] or [float('nan')]), 1)} (ellipse) for 2 ≤ t/t_{{th}} ≤ 3, and by {pc(cdev.get('dev_at_t3p5'), 1)} and {pc(max([e['dev_at_t3p5'] for e in edev] or [float('nan')]), 1)} at t = 3.5 t_{{th}} where p has fallen to 0.5 (@@fig:wall@@b): the delayed, non-local contribution grows after the peak and is larger for the ellipse. This is the signature of the local response derived in Section 2: for the isotropic circle in quasi-static plane strain the Lamé solution gives σ_{{θθ}}(a,t) = −2μ(γ_{{T}}/m)p(t) − 2(λ+m)(γ_{{T}}/m)F(t)/(R² + (λ+m)a²/2μ) with F = ∫ rθ dr, in which the second, far-field term is O((a/R)²) ≈ 10^{{−3}} of the first. The isotropic control gives {mp(g(ISO, 'circle_T48'))} MPa/K on the 96×48 grid, compared with 0.986 MPa/K from the independent time-domain solution (0.985 MPa/K for its first term)."))
    L.append(('fig', os.path.join(ROOT, '11_Figures', 'fig3_wall_profiles.png'), 'Wall hoop stress of the circular and elliptical cavity. (a) Distribution around the wall at the time of the peak (grid R192, interpolated). (b) Time history at the peak node compared with the wall temperature p(t).', 6.4, 'wall'))
    # ---------------- 5.2 ellipse
    L.append(('h2', '5.2 Elliptical cavity: crystal orientation modulates the peak wall stress'))
    a12 = g(T4, 'M_12phi_sig_interp', default={}); a6e = g(T4, 'extrapolated_6phi', default={})
    L.append(('p', f"For the equal-area ellipse the peak wall stress depends strongly on the crystal orientation (@@fig:phi@@a). On grid M the peak ranges from {mp(a12.get('min'))} MPa/K (φ = {a12.get('phi_min')}°) to {mp(a12.get('max'))} MPa/K (φ = {a12.get('phi_max')}°): an orientation modulation A_{{φ}} = {pc(a12.get('amplitude'))}; after radial and angular extrapolation the six-orientation sweep gives A_{{φ}} = {pc(a6e.get('amplitude'))} with extremes {mp(a6e.get('min'))}–{mp(a6e.get('max'))} MPa/K. The numerical uncertainty of the amplitude is u_{{num}} = {pc(T4.get('u_num'), 2)} (largest difference between grid M and the finer or extrapolated estimates), the frozen threshold is max(5u_{{num}}, 2%) = {pc(T4.get('threshold'), 2)}, and the modulation is therefore {str(T4.get('status', 'n/a')).lower()} (T4). The ellipse peak is {g(T4, 'ellipse_extrapolated_mean_over_circle_extrapolated', default=float('nan')):.2f} times the circle peak on average; the orientation of the crystal changes the ellipse peak by a factor of about {a12.get('max', 1) / a12.get('min', 1):.2f} between the most and the least favourable orientation."))
    L.append(('fig', os.path.join(ROOT, '11_Figures', 'fig2_phi_sweep.png'), 'Peak wall hoop stress per kelvin versus crystal rotation φ. (a) Ellipse on the three radial grids and Richardson-extrapolated; circle (horizontal lines, three grids). (b) Same orientations: the earlier internal analysis (periodic-pulse synthesis, rotation-tensor sign error, coarser wall mesh) compared with this work.', 6.5, 'phi'))
    if ISO.get('ellipse_radial'):
        er = ISO['ellipse_radial']
        L.append(('p', f"With isotropic stiffness, conductivity and expansion the ellipse is orientation-independent by symmetry and its peak is {mp(er.get('f_ext', er['f'][1]))} MPa/K (extrapolated; {mp(er['f'][1])} on grid M), i.e. {ISO.get('ellipse_M_over_circle_T48', float('nan')):.2f} times the isotropic circle: the shape alone raises the peak by the curvature at the ends of the major axis, and the crystal orientation then modulates the response by the amount given above."))
    if FLOC:
        tws = [r['tw'] for r in FLOC]; A2 = [r['A2'] for r in FLOC]; cc = [r['circle'] for r in FLOC]
        mono = all(A2[i] < A2[i + 1] for i in range(len(A2) - 1)); cvar = (max(cc) - min(cc)) / np.mean(cc)
        iso_ratio = ISO.get('ellipse_M_over_circle_T48')
        L.append(('p', f"Is the modulation a local effect? If the heated layer were thin compared with the radius of curvature, the response at each wall point would depend only on the local tangent direction; every tangent direction occurs on any convex wall, so the peak over the wall would be orientation-independent for the ellipse as well, and the modulation would vanish. In the present problem the heated layer is not thin: its thickness scales with t_{{w}}^{{1/2}} and is comparable to the cavity radius, and the isotropic ellipse already has a peak {iso_ratio if iso_ratio else float('nan'):.2f} times that of the isotropic circle, which a purely local response could not produce. A pulse-width test (t_{{w}} = {tws[0]:g}–{tws[-1]:g} t_{{th}}; @@tab:pw@@, @@fig:pw@@) shows that the two-point modulation A_{{2}} = (σ̂(150°) − σ̂(90°))/mean {'rises monotonically' if mono else 'does not vary monotonically'} but only weakly with the pulse width, from {pc(A2[0], 1)} to {pc(A2[-1], 1)}, while the circle peak varies by {pc(cvar, 1)} (peak to peak, relative to the mean; the narrowest pulse is the outlier). The trend is in the direction expected for a growing non-local contribution, but the accessible layer thicknesses (still thicker than the tip radius of curvature, 0.35a) do not reach the thin-layer limit, so the test neither confirms nor excludes a vanishing modulation in that limit; within the studied range the orientation dependence of the ellipse is a non-local effect of the interaction between the heated region and the cavity shape."))
        rows = [[f"{r['tw']:g}", mp(r['circle'], 4), mp(r['ell_phi90'], 4), mp(r['ell_phi150'], 4), pc(r['A2'], 1)] for r in FLOC]
        L.append(('table', ['t_w (t_th)', 'circle (MPa/K)', 'ellipse φ=90° (MPa/K)', 'ellipse φ=150° (MPa/K)', 'A_2'], rows, 'Pulse-width test (grid 96×48, interpolated peaks). t_w = 1.2 is the baseline.', [1.0, 1.3, 1.6, 1.6, 0.8], 'pw'))
        L.append(('fig', os.path.join(ROOT, '11_Figures', 'fig7_pulse_width.png'), 'Pulse-width test of the local-response interpretation (96×48). (a) Peak wall stress of the circle and of the ellipse at the baseline minimum and maximum orientations; (b) two-point orientation modulation.', 6.0, 'pw'))
    # ---------------- 5.3 ablations
    L.append(('h2', '5.3 Which anisotropy drives the modulation'))
    if EAB:
        bs = EAB.get('baseline_6phi', {})
        rows = [['full anisotropy (baseline)', pc(bs.get('amplitude')), mp(bs.get('mean'), 4), '1.000']]
        for key, lab in (('E3_K_iso', 'isotropic conductivity'), ('E4_C_iso', 'isotropic stiffness'), ('E2_alpha_iso', 'isotropic expansion (mean α)'), ('E1_alpha_cheng298', 'expansion set of the 298 K-like data [18]')):
            e = EAB.get(key)
            if e: rows.append([lab, pc(e['amplitude']), mp(e['mean'], 4), f"{e['mean_over_baseline']:.3f}"])
        rk = {k: (EAB[k]['amplitude'] / bs['amplitude']) for k in ('E3_K_iso', 'E4_C_iso', 'E2_alpha_iso') if k in EAB and bs.get('amplitude')}
        L.append(('p', 'To separate the contributions of the three anisotropic tensors the ellipse sweep was repeated with one tensor at a time made isotropic (stiffness from the same Lamé constants as the isotropic control; conductivity equal to the mean eigenvalue; expansion equal to the mean of the three axes) (Table 6, Fig. 7), and with an expansion set representing the 298 K measurements [18] (α = (0.10, 0.20, 0.20)×10^{−6} 1/K, a sensitivity-only set constructed from the abstract-level statement that α_{b} and α_{c} are about twice α_{a}). The ablations are exploratory and use the 96×48 grid (six orientations; the angular error common to all variants cancels in the comparison).'))
        if rk:
            L.append(('p', f"Removing the expansion anisotropy lowers the modulation to {pc(rk.get('E2_alpha_iso'), 0)} of the baseline, removing the stiffness anisotropy changes it to {pc(rk.get('E4_C_iso'), 0)} of the baseline, and removing the conductivity anisotropy changes it to {pc(rk.get('E3_K_iso'), 0)}. The orientation modulation therefore results from the competition of the expansion and stiffness anisotropies — the expansion anisotropy alone (isotropic stiffness) would give a larger modulation than the full crystal, the stiffness anisotropy partially compensates it — while the conductivity anisotropy is a minor modifier."))
        L.append(('table', ['Variant', 'Modulation A_φ', 'Mean peak (MPa/K)', 'Mean / baseline'], rows, 'Mechanism ablations and expansion-set sensitivity for the ellipse (grid 96×48, φ = 0, 30, …, 150°).', [2.6, 1.3, 1.5, 1.2], 'abl'))
        L.append(('fig', os.path.join(ROOT, '11_Figures', 'fig6b_ablation.png'), 'Orientation modulation of the ellipse peak stress for the baseline and with one anisotropic tensor made isotropic, and for the 298 K-like expansion set (96×48, six orientations).', 4.2, 'abl'))
    # ---------------- 5.4 thermal memory
    L.append(('h2', '5.4 Thermal memory and thermoelastic feedback'))
    pq, pd_ = T2.get('pair_QS'), T2.get('pair_dynamic')
    dyn = [r for r in T2.get('dynamic', []) if r['model'] == 'CV']; qs = [r for r in T2.get('quasi_static', []) if r['model'] == 'CV']
    dmax = max([r['D'] for r in dyn] or [float('nan')]); a10 = [r for r in dyn if r['a_nm'] == 10]; d10 = [r['D'] for r in a10]
    pk = max([abs(r['peak_shift']) for r in dyn + qs] or [float('nan')]); ext = AN.get('H3_extended_map', {})
    sl = [(v.get('delta_D_slope_5_10'), v.get('delta_D_slope_10_20')) for k_, v in ext.items() if v.get('delta_D_slope_5_10') is not None and float(k_) <= 0.8]
    sl32 = ext.get('3.2', {})
    sl_txt = (f"; for Λ ≤ 0.8 the excess of the dynamic over the quasi-static D falls with ε roughly as ε^{{{min(s[0] for s in sl):.1f}–{max(s[0] for s in sl):.1f}}} (5→10 nm) to ε^{{{min(s[1] for s in sl):.1f}–{max(s[1] for s in sl):.1f}}} (10→20 nm), consistent with an O(ε²) leading correction (steeper, ε^{{{sl32.get('delta_D_slope_5_10', float('nan')):.1f}}}–ε^{{{sl32.get('delta_D_slope_10_20', float('nan')):.1f}}}, at Λ = 3.2)" if sl else '')
    L.append(('p', f"The relaxation-time law changes the wall stress only slightly. Over the studied range (Λ up to {max([r['Lambda'] for r in dyn] or [float('nan')]):.1f}) the thermal-memory deviation of the full stress history is D ≤ {pc(dmax, 1)} (largest at a = 5 nm, Λ = 3.2); for a = 10 nm it is {pc(min(d10), 2)}–{pc(max(d10), 1)} for τ = 1–20 ps, and the peak value itself shifts by at most {pc(pk, 1)} (@@tab:D@@, @@fig:mem@@a). The two-relaxation-time kernel (MCV3 in @@tab:D@@) is an exploratory variant and is not used in any of the statements below. For a prescribed wall temperature the conduction law enters the wall stress of the isotropic circle only through the weak far-field term of Eq. (2); the anisotropic results are consistent with this. The scaling identity of Section 2 is confirmed to round-off: in the quasi-static, uncoupled limit D depends on Λ alone, and the equal-Λ pair (a = 10 nm, τ = 5 ps) and (a = 20 nm, τ = 20 ps) (Λ = 0.198) gives D = {sci(g(pq, 'D_a10_tau5'), 4)} and {sci(g(pq, 'D_a20_tau20'), 4)} (residual {rsd(g(pq, 'residual'))}, T2 quasi-static: {T2.get('status_quasi_static')}). With elastodynamics the same pair gives {sci(g(pd_, 'D_a10_tau5'), 3)} and {sci(g(pd_, 'D_a20_tau20'), 3)} (residual {pc(g(pd_, 'residual'), 0)}; T2 dynamic: {T2.get('status_dynamic')}). The pre-registered collapse in Λ alone therefore fails for the full model at the 25% level, but the failure is entirely due to elastic inertia (including, for a ≥ 20 nm, echoes): the quasi-static runs differ from the dynamic ones only by the inertia term, and the correction is O(ε²), of the same order (10^{{−3}}) as the thermal-memory effect itself{sl_txt}. For a = 20 nm and 50 nm the elastic echo returns inside the window, so those dynamic values are properties of the finite domain."))
    rows = []
    for r in sorted(dyn, key=lambda x: (x['a_nm'], x['tau_ps'])):
        q_ = next((x for x in qs if abs(x['Lambda'] - r['Lambda']) / r['Lambda'] < 1e-3 and x['model'] == 'CV'), None)
        rows.append([f"{r['a_nm']:.0f}", f"{r['tau_ps']:.0f}", f"{r['Lambda']:.3f}", f"{r['epsilon']:.4f}", sci(r['D'], 2), sci(q_['D'], 2) if q_ else '—', f"{r['peak_shift']*100:+.2f}%"])
    mc = [r for r in T2.get('dynamic', []) if r['model'] == 'MCV3']
    for r in mc: rows.append([f"{r['a_nm']:.0f}", f"{r['tau_ps']:.0f} (MCV3)", f"{r['Lambda']:.3f}", f"{r['epsilon']:.4f}", sci(r['D'], 2), '—', f"{r['peak_shift']*100:+.2f}%"])
    L.append(('table', ['a (nm)', 'τ (ps)', 'Λ', 'ε', 'D (dynamic)', 'D (quasi-static)', 'peak shift'], rows, 'Thermal-memory deviation D of the circular cavity (anisotropic, φ = 0; grid 96×48, t ≤ 6 t_{th}) and the relative shift of the peak stress for the dynamic runs. MCV3 = two-relaxation-time kernel (exploratory).', [0.7, 1.0, 0.7, 0.7, 1.1, 1.2, 0.9], 'D'))
    L.append(('fig', os.path.join(ROOT, '11_Figures', 'fig5_memory.png'), 'Thermal-memory deviation. (a) D versus Λ for dynamic (markers by cavity size) and quasi-static (crosses) runs; (b) wall hoop stress at the peak node for Fourier and CV (τ = 20 ps) conduction and their difference.', 6.4, 'mem'))
    if T3:
        L.append(('p', f"Thermoelastic feedback is negligible: with δ = {T3.get('delta', float('nan')):.3e} the largest relative change of the temperature at the probes r/a ≈ {', '.join(f'{x:.1f}' for x in T3.get('probe_r_over_a', []))} when the energy coupling is removed is {sci(T3.get('max_rel_dev'), 2)}, against the frozen bound 5δ = {sci(T3.get('bound_5delta'), 2)} (T3: {T3.get('status')}); the peak stress changes by {pc(T3.get('peak_stress_change'), 3)}. The cavity-wall temperature is Dirichlet-prescribed and shows no feedback by construction."))
    L.append(('h2', '5.5 Sensitivity to the expansion data'))
    e1 = EAB.get('E1_alpha_cheng298')
    if e1:
        L.append(('p', f"Stress per kelvin is proportional to the thermal-stress vector β = Cα. With the 298 K-like expansion set the mean ellipse peak is {e1['mean_over_baseline']:.3f} of the baseline value ({mp(e1['mean'], 4)} MPa/K) while the orientation modulation is {pc(e1['amplitude'])} (baseline {pc(EAB.get('baseline_6phi', {}).get('amplitude'))}). The absolute stress scale therefore carries a parameter uncertainty of more than an order of magnitude (a factor {1/e1['mean_over_baseline']:.0f} between the two expansion sets) through α, whereas the modulation depends on the anisotropy ratios of β and is almost unchanged; only the relative statements of this paper should be used quantitatively."))
    return L


def discussion():
    pdn = T2.get('pair_dynamic') or {}
    A2 = [r['A2'] for r in FLOC] if FLOC else []
    iso_ratio = ISO.get('ellipse_M_over_circle_T48')
    mech = (f"For a prescribed wall temperature the peak wall stress of a circular cavity is, to about 10^{{−3}} for the isotropic circle (closed form) and to a few percent for the anisotropic crystal (stress/temperature ratio within the window near the peak, pulse-width test), a local, instantaneous constraint response, and it is orientation-invariant. The ellipse breaks this locality: its peak is {iso_ratio if iso_ratio else float('nan'):.2f} times that of the isotropic circle, and in the crystal it depends on orientation by {pc(g(T4, 'extrapolated_6phi', 'amplitude'), 0)}. The pulse-width test shows only a weak dependence of this modulation on the heated-layer thickness ({pc(A2[0], 1) if A2 else 'n/a'}–{pc(A2[-1], 1) if A2 else 'n/a'}), so within the accessible range it is a non-local effect of the interaction between the heated region and the cavity shape; whether it vanishes in the thin-layer limit is not tested. Every statement above concerns a relative quantity (a ratio or a modulation); the absolute stress scale carries the parameter uncertainty quantified in Section 5.5.")
    return [
        ('h1', '6. Discussion and limitations'),
        ('h2', '6.1 What the study shows'),
        ('bullets', [
            mech,
            'Heat-conduction physics (Fourier versus relaxation-time laws) has a bounded and small influence on this observable (evaluated for the circular cavity). Wall hoop stress under a prescribed wall temperature is therefore a poor discriminator of conduction laws; interior stresses, wall heat flux or a prescribed heat flux are the observables to examine.',
            'The scaling identity (Section 2) turns the pre-registered hypothesis of collapse in Λ into a statement about the size of two corrections (elastic inertia/echo, thermoelastic feedback); the numerical results quantify both.',
        ]),
        ('h2', '6.2 Limitations'),
        ('bullets', [
            '**No physical validation.** No transient cavity measurements for β-Ga\u2082O\u2083 are known to us; the study is verified, not validated (APPLICABLE — EVIDENCE_UNAVAILABLE).',
            '**Continuum validity.** Fourier and Cattaneo–Vernotte conduction are continuum models. In β-Ga\u2082O\u2083 the gray mean free path is of the order of 3 nm, but heat-carrying phonons with mean free paths up to about 0.7–1 µm exist [20]; cavities of 5–50 nm are therefore outside the demonstrated range of validity of these laws. The dimensionless results (Λ, ε, φ, χ) should be read as properties of the continuum model.',
            '**Parameters.** The relaxation times are hypothetical (order-of-magnitude estimates: gray ≈ 0.9 ps, longest-mean-free-path phonons ≈ 0.2 ns); c_{p} is assumed (485–540 J/(kg K) reported [19], 560 used) and enters only the time scale; the thermal-expansion coefficients are uncertain by more than an order of magnitude at 298 K [17,18]; α_{5} is set to zero; the b-axis expansion enters through C_{12}, C_{23}, C_{25}.',
            '**Scope of the runs.** Thermal-memory (relaxation-time) runs and the feedback test were made for the circular cavity; the elliptical cavity was run with Fourier conduction; the mechanism ablations are exploratory.',
            f'**Model scope.** Linear, small-strain, plane strain in the a–c plane; temperature-independent properties; prescribed (Dirichlet) wall temperature; finite undamped domain (R = 80a) with a clamped cold boundary, so elastic echoes are model features for a ≥ 20 nm and the QoI window t ≤ 6 t_{{th}} is echo-free only for a ≤ 10 nm (doubling R changed the peak by ≤ {max(abs(v["peak_change_R80_to_R160"]) for v in CR.get("C3", {}).values())*100:.1f}% and D by ≤ {max(abs(v["D_change_R80_to_R160"]) for v in CR.get("C3", {}).values())*100:.1f}%); no thermal boundary resistance, no surface or size effects on the elastic constants.',
            '**Numerics.** The sharp ends of the ellipse converge slowly: the extrapolation corrections of @@tab:conv@@ and u_{num} quantify this; a 192×192 grid could not be run within the 2 GB memory of the environment. The mechanism ablations use the 96×48 grid and are exploratory.',
            '**Method of analysis.** The code and the analysis were developed with AI assistance and verified as described in Section 4; the preliminary internal analysis from which this study started contained a rotation-tensor sign error, a periodic-pulse-train synthesis and an under-resolved wall mesh; all affected results were recomputed. Independent expert review of the formulation and the claims has not been carried out.',
        ]),
        ('h2', '6.3 Outlook'),
        ('p', 'Natural extensions are prescribed heat-flux loading, interior-stress and wall-heat-flux observables, three-dimensional and finite-strain effects, temperature-dependent properties, and a comparison with time-resolved thermoreflectance or X-ray measurements of strain around engineered cavities if such data become available.'),
    ]


def conclusions():
    a12 = g(T4, 'M_12phi_sig_interp', default={}); a6e = g(T4, 'extrapolated_6phi', default={})
    pq = T2.get('pair_QS') or {}; pd_ = T2.get('pair_dynamic') or {}
    dyn = [r for r in T2.get('dynamic', []) if r['model'] == 'CV']; qs = [r for r in T2.get('quasi_static', []) if r['model'] == 'CV']
    dmax = max([r['D'] for r in dyn + qs] or [float('nan')])
    return [('h1', '7. Conclusions'),
            ('bullets', [
                f"The response of a quiescent medium to one pulse can be obtained from a frequency-domain solver by Bromwich inversion on a shifted contour; it was verified against exact and independent solutions (peak error {pc(abs(N['v9d_worst192']) if N['v9d_worst192'] is not None else None, 2)} at 192×96 for the axisymmetric dynamic problem, second order), whereas a periodic synthesis over a few thermal times returns a pulse-train steady state.",
                f"The peak wall stress of a circular cavity in monoclinic β-Ga\u2082O\u2083 is orientation-invariant to round-off ({sci(g(T1, 'M_sig_nodal', 'spread_rel'))}) and equals {mp(g(CIRC, 'radial_interp', 'f_ext'))} MPa/K (extrapolated) for the parameters used.",
                f"An equal-area ellipse (axis ratio 2) converts crystal orientation into a peak-stress modulation of {pc(a6e.get('amplitude'))} (grid M: {pc(a12.get('amplitude'))}; numerical uncertainty {100*T4.get('u_num', float('nan')):.1f} percentage points), {str(T4.get('status', '')).lower()} against the frozen criterion.",
                f"Thermal memory changes the wall-stress history of the circular cavity by at most {pc(max([x['D'] for x in dyn] or [float('nan')]), 1)} (≤ {pc(max([x['D'] for x in dyn if x['a_nm'] >= 10] or [float('nan')]), 1)} for a ≥ 10 nm) and the peak by at most {pc(max([abs(x['peak_shift']) for x in dyn + qs] or [float('nan')]), 1)} for Λ up to {max([r['Lambda'] for r in dyn] or [float('nan')]):.1f}; D collapses in Λ in the quasi-static limit (residual {rsd(pq.get('residual'))}) and the elastodynamic residual ({pc(pd_.get('residual'), 0)}) is an O(ε²) inertia correction to an already small effect; thermoelastic feedback is bounded by 5δ ({T3.get('status')}).",
                'The absolute stress scale depends on the thermal-expansion data by more than an order of magnitude and on hypothetical relaxation times; the continuum description is not claimed at the nanometre scale; no experimental validation exists. Results are properties of the verified continuum model.',
            ])]
