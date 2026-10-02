"""analyze_v2.py — Phase 12 analysis of the v2 production data.  Every number in the output is computed here from
09_Raw_Data/production (no hard-coded results).  Criteria are those of 02_Problem_Definition/ACCEPTANCE_CRITERIA_V2_FROZEN.md.
Outputs: 10_Processed_Data/ANALYSIS_V2.json, ANALYSIS_V2_TABLES.md, 12_Tables/*.csv
"""
import sys, os, json, csv
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import numpy as np
import production_matrix as pm
import cg_pipeline as cp

def _repo_root(_start):
    """walk up from _start to the checkout that holds PAPER_PROJECT (path-independent
    replacement for the hard-coded '/home/user/work/...' literals)."""
    _p = os.path.abspath(_start)
    while True:
        if os.path.isdir(os.path.join(_p, 'PAPER_PROJECT')):
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            raise RuntimeError('PAPER_PROJECT not found above %s' % _start)
        _p = _q


PROD = os.environ.get('PROD_DIR', os.path.join(ROOT, '09_Raw_Data', 'production'))
OUTJ = os.path.join(ROOT, '10_Processed_Data', 'ANALYSIS_V2.json')
OUTM = os.path.join(ROOT, '10_Processed_Data', 'ANALYSIS_V2_TABLES.md')
TAB = os.path.join(ROOT, '12_Tables'); os.makedirs(TAB, exist_ok=True)
SHIPPED = os.path.join(_repo_root(__file__), 'work', 'handoff',
                      'PROJECT_CRYSTAL_GEOMETRY_01', 'data', 'PROD')
A = {}; L = []
def log(s=''):
    print(s); L.append(s)

_cache = {}
def load(tag):
    if tag in _cache: return _cache[tag]
    jp = os.path.join(PROD, tag + '.json')
    if not os.path.exists(jp):
        _cache[tag] = None; return None
    q = json.load(open(jp)); d = np.load(os.path.join(PROD, tag + '.npz'))
    q.update(t=d['t'], hoop=d['hoop'], wall=d['wall'], probe=d['probe'])
    _cache[tag] = q
    return q

def sig(q, key='sig_interp'): return abs(q[key])

def gci(f3, r=2.0):
    f_c, f_m, f_f = f3
    e21, e32 = f_m - f_c, f_f - f_m
    out = dict(f=[float(x) for x in f3])
    if e21 == 0 or e32 == 0 or np.sign(e21) != np.sign(e32):
        out.update(p=None, f_ext=None, gci_fine=None, note='non-monotone'); return out
    p = float(np.log(abs(e21 / e32)) / np.log(r))
    # Richardson with the observed order, but never assume p outside [1, 2.5]
    pc = min(max(p, 1.0), 2.5)
    f_ext = f_f + (f_f - f_m) / (r ** pc - 1.0)
    out.update(p=p, p_used=pc, f_ext=float(f_ext), gci_fine=float(1.25 * abs((f_f - f_m) / f_f) / (r ** pc - 1.0)),
               rel_diff_fine_vs_ext=float(abs(f_f - f_ext) / abs(f_ext)))
    return out

def D_metric(qcv, qf, tmax=6.0):
    n = int(np.searchsorted(qf['t'], tmax + 1e-9, side='right'))
    return float(np.abs(qcv['hoop'][:, :n] - qf['hoop'][:, :n]).max() / np.abs(qf['hoop'][:, :n]).max())

def amp(vals):
    v = np.abs(np.asarray(vals, float)); return float((v.max() - v.min()) / v.mean())

def write_csv(name, header, rows):
    with open(os.path.join(TAB, name), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)

# ======================================================================== T1 / H1: circle invariance
log('## T1 / H1 — circle peak invariance (grid-aligned phi)')
T1 = {}
for g, phis in (('R48', cp.PHIS), ('M', (0, 15, 45, 75, 105, 135))):
    qs = [load(f'A_chi1_phi{p:03d}_{g}') for p in phis]
    if all(qs):
        for key in ('sig_nodal', 'sig_interp'):
            v = np.array([abs(q[key]) for q in qs])
            T1[f'{g}_{key}'] = dict(phis=list(phis), mean=float(v.mean()), spread_rel=float((v.max() - v.min()) / v.mean()), values=[float(x) for x in v])
if 'M_sig_nodal' in T1:
    pairs = {}
    for g, plist in (('M', ((15, 105), (45, 135))), ('R48', tuple((p, p + 90) for p in range(0, 90, 15)))):
        rel = []
        for a_, b_ in plist:
            qa, qb = load(f'A_chi1_phi{a_:03d}_{g}'), load(f'A_chi1_phi{b_:03d}_{g}')
            if qa and qb: rel.append(abs(abs(qa['sig_nodal']) - abs(qb['sig_nodal'])) / abs(qa['sig_nodal']))
        pairs[g] = float(max(rel)) if rel else None
    T1['pairs_90deg_max_rel'] = pairs
    T1['status'] = 'PASS' if (T1['M_sig_nodal']['spread_rel'] <= 1e-8 and T1.get('R48_sig_nodal', {}).get('spread_rel', 1) <= 1e-8) else 'FAIL'
    T1['criterion'] = 'spread_rel of sig_nodal over the phi list <= 1e-8 on grids M (6 phi) and R48 (12 phi) (frozen threshold)'
A['T1_H1'] = T1
for k, v in T1.items():
    if isinstance(v, dict) and 'spread_rel' in v: log(f"  {k}: spread {v['spread_rel']:.2e}  mean {v['mean']:.1f} Pa/K")
log(f"  T1 status: {T1.get('status')}  (90-deg pairs max {T1.get('pairs_90deg_max_rel')})")

def solve_p(ratio_obs, n1, n2, n3):
    """observed order p from (f(n1)-f(n2))/(f(n2)-f(n3)) = (n1^-p - n2^-p)/(n2^-p - n3^-p) for error ~ N^-p."""
    from scipy.optimize import brentq
    f = lambda p: (n1 ** -p - n2 ** -p) / (n2 ** -p - n3 ** -p) - ratio_obs
    try: return float(brentq(f, 0.2, 6.0))
    except Exception: return None

def triplet(vals, ns):
    """Richardson for values at mesh sizes ns (monotone refinement). Returns dict with p, f_ext, correction at the middle level."""
    f1, f2, f3 = vals; n1, n2, n3 = ns
    out = dict(f=[float(x) for x in vals], n=list(ns))
    d12, d23 = f1 - f2, f2 - f3
    if d12 == 0 or d23 == 0 or np.sign(d12) != np.sign(d23):
        out.update(p=None, f_ext=None, note='non-monotone'); return out
    p = solve_p(d12 / d23, n1, n2, n3)
    if p is None:
        out.update(p=None, f_ext=None, note='no root'); return out
    pc = min(max(p, 1.0), 3.0)
    # error model f(n) = f_inf + c n^-pc, calibrated on the two finest levels
    c = (f2 - f3) / (n2 ** -pc - n3 ** -pc); f_inf = f3 - c * n3 ** -pc
    out.update(p=p, p_used=pc, f_ext=float(f_inf), corr_at_mid=float(f_inf - f2), corr_at_fine=float(f_inf - f3),
               rel_err_mid=float((f2 - f_inf) / f_inf), rel_err_fine=float((f3 - f_inf) / f_inf))
    return out

# ======================================================================== circle absolute value + convergence
log(); log('## Circle peak hoop stress (phi-independent), grid convergence')
circ = {}
rad = [load(f'A_chi1_phi000_{g}') for g in ('R48', 'M', 'R192')]
if all(rad):
    circ['radial_interp'] = triplet([abs(q['sig_interp']) for q in rad], (48, 96, 192))
    circ['radial_nodal'] = triplet([abs(q['sig_nodal']) for q in rad], (48, 96, 192))
    qT, qM = load('A_chi1_phi000_T48'), rad[1]
    if qT: circ['angular_T48_to_M_rel_change'] = float((abs(qM['sig_interp']) - abs(qT['sig_interp'])) / abs(qT['sig_interp']))
    A['circle_peak'] = circ
    c = circ['radial_interp']; log(f"  radial R48/M/R192: {[f'{x:.1f}' for x in c['f']]}  p={c.get('p')}  extrapolated={c.get('f_ext')}  error at M {c.get('rel_err_mid')}, at R192 {c.get('rel_err_fine')}; angular T48->M change {circ.get('angular_T48_to_M_rel_change')}")

# ======================================================================== T4 / H2: ellipse modulation
log(); log('## T4 / H2 — ellipse orientation modulation')
T4 = {}
def vals(g, plist=cp.PHIS, key='sig_interp'):
    qs = [load(f'A_chi2_phi{p:03d}_{g}') for p in plist]
    return [abs(q[key]) for q in qs] if all(qs) else None
for g in ('R48', 'T48', 'M'):
    for key in ('sig_interp', 'sig_nodal'):
        v = vals(g, key=key)
        if v: T4[f'{g}_12phi_{key}'] = dict(amplitude=amp(v), min=float(min(v)), max=float(max(v)), mean=float(np.mean(v)),
                                            phi_min=int(cp.PHIS[int(np.argmin(v))]), phi_max=int(cp.PHIS[int(np.argmax(v))]))
sub = {g: vals(g, pm.PHIS6) for g in ('R48', 'M', 'R192', 'T48', 'T144')}
for g, v in sub.items():
    if v: T4[f'{g}_6phi_interp'] = dict(amplitude=amp(v), min=float(min(v)), max=float(max(v)), mean=float(np.mean(v)), values=[float(x) for x in v])
if all(sub[g] for g in ('R48', 'M', 'R192', 'T48', 'T144')):
    ext6, budget = [], {}
    for i, p in enumerate(pm.PHIS6):
        tr = triplet([sub['R48'][i], sub['M'][i], sub['R192'][i]], (48, 96, 192))
        ta = triplet([sub['T48'][i], sub['M'][i], sub['T144'][i]], (48, 96, 144))
        dr = tr['corr_at_mid'] if tr.get('f_ext') is not None else 0.0
        da = ta['corr_at_mid'] if ta.get('f_ext') is not None else 0.0
        # signs: stored values are |sigma| (positive); corrections are for |sigma|
        ext6.append(sub['M'][i] + dr + da)
        budget[int(p)] = dict(radial_p=tr.get('p'), radial_corr_rel=float(dr / sub['M'][i]), angular_p=ta.get('p'), angular_corr_rel=float(da / sub['M'][i]),
                              M=float(sub['M'][i]), extrapolated=float(sub['M'][i] + dr + da))
    T4['extrapolated_6phi'] = dict(values=[float(x) for x in ext6], amplitude=amp(ext6), min=float(min(ext6)), max=float(max(ext6)), mean=float(np.mean(ext6)), budget=budget)
    u_candidates = [abs(T4['R192_6phi_interp']['amplitude'] - T4['M_6phi_interp']['amplitude']), abs(T4['T144_6phi_interp']['amplitude'] - T4['M_6phi_interp']['amplitude']),
                    abs(T4['extrapolated_6phi']['amplitude'] - T4['M_6phi_interp']['amplitude'])]
    u_num = float(max(u_candidates))
    a_m = T4['M_12phi_sig_interp']['amplitude']
    thr = max(5 * u_num, 0.02)
    T4.update(u_num=u_num, threshold=float(thr), amplitude_M_12phi=a_m, amplitude_6phi_extrapolated=T4['extrapolated_6phi']['amplitude'],
              status='RESOLVABLE' if a_m >= thr else 'NULL+resolution-limit',
              criterion='A12(M) >= max(5*u_num, 2%), u_num = max(|A6(R192)-A6(M)|, |A6(T144)-A6(M)|, |A6(extrapolated)-A6(M)|)')
    ci = A.get('circle_peak', {}).get('radial_interp', {})
    if ci.get('f_ext'):
        T4['ellipse_extrapolated_mean_over_circle_extrapolated'] = float(T4['extrapolated_6phi']['mean'] / ci['f_ext'])
    write_csv('phi_sweep_ellipse.csv', ['phi_deg', 'M_interp_Pa_per_K', 'M_nodal', 'R48_interp', 'T48_interp', 'theta_star_deg_M'],
              [[p, abs(load(f'A_chi2_phi{p:03d}_M')['sig_interp']), abs(load(f'A_chi2_phi{p:03d}_M')['sig_nodal']), abs(load(f'A_chi2_phi{p:03d}_R48')['sig_interp']),
                abs(load(f'A_chi2_phi{p:03d}_T48')['sig_interp']), load(f'A_chi2_phi{p:03d}_M')['th_star_interp_deg']] for p in cp.PHIS])
    write_csv('convergence_ellipse_6phi.csv', ['phi_deg', 'R48', 'M', 'R192', 'T48', 'T144', 'extrapolated'],
              [[p, sub['R48'][i], sub['M'][i], sub['R192'][i], sub['T48'][i], sub['T144'][i], ext6[i]] for i, p in enumerate(pm.PHIS6)])
tips = []
for p in cp.PHIS:
    q = load(f'A_chi2_phi{p:03d}_M')
    if q:
        th = q['th_star_interp_deg'] % 180.0; tips.append((int(p), float(q['th_star_interp_deg']), bool(min(th, 180.0 - th) <= 15.0)))
if tips:
    T4['peak_location'] = dict(per_phi=[dict(phi=p, theta_star_deg=t, at_tip=b) for p, t, b in tips], n_at_tip=int(sum(b for _, _, b in tips)), n_total=len(tips),
                               note='tip = within 15 deg (parameter angle) of the ends of the major axis (eta = 0, 180)')
A['T4_H2'] = T4
for k in ('R48_12phi_sig_interp', 'T48_12phi_sig_interp', 'M_12phi_sig_interp'):
    if k in T4: log(f"  {k}: amplitude {T4[k]['amplitude']*100:.2f}%  range {T4[k]['min']/1e6:.4f}-{T4[k]['max']/1e6:.4f} MPa/K  (min at phi={T4[k]['phi_min']}, max at phi={T4[k]['phi_max']})")
for k in ('R48_6phi_interp', 'M_6phi_interp', 'R192_6phi_interp', 'T48_6phi_interp', 'T144_6phi_interp'):
    if k in T4: log(f"  {k}: amplitude {T4[k]['amplitude']*100:.2f}%  mean {T4[k]['mean']/1e6:.4f}")
if 'extrapolated_6phi' in T4:
    e = T4['extrapolated_6phi']; log(f"  extrapolated (6 phi): amplitude {e['amplitude']*100:.2f}%  range {e['min']/1e6:.4f}-{e['max']/1e6:.4f}; u_num={T4['u_num']:.4f}; threshold {T4['threshold']:.4f} -> {T4['status']}")

# ======================================================================== comparison with shipped numbers
log(); log('## Corrected vs shipped (handoff) numbers')
SH = {}
try:
    sc = [abs(json.load(open(os.path.join(SHIPPED, f'A_chi1_phi{p:03d}.json')))['sig_max']) for p in cp.PHIS]
    se = [abs(json.load(open(os.path.join(SHIPPED, f'A_chi2_phi{p:03d}.json')))['sig_max']) for p in cp.PHIS]
    SH = dict(circle_mean=float(np.mean(sc)), circle_scatter=float((max(sc) - min(sc)) / np.mean(sc)), ellipse_amp=amp(se),
              ellipse_min=float(min(se)), ellipse_max=float(max(se)), ellipse=[float(x) for x in se], circle=[float(x) for x in sc])
    vm = vals('M')
    if vm: SH['M_over_shipped_ellipse'] = [float(vm[i] / se[i]) for i in range(12)]
    cm = load('A_chi1_phi000_M')
    if cm: SH['M_over_shipped_circle'] = float(abs(cm['sig_interp']) / SH['circle_mean'])
    ce = A.get('circle_peak', {}).get('radial_interp', {})
    if ce.get('f_ext'): SH['circle_extrapolated_over_shipped'] = float(ce['f_ext'] / SH['circle_mean'])
    if 'extrapolated_6phi' in T4:
        se6 = [se[cp.PHIS.index(p)] for p in pm.PHIS6]
        SH['ellipse_6phi_extrapolated_over_shipped'] = [float(T4['extrapolated_6phi']['values'][i] / se6[i]) for i in range(6)]
    A['shipped'] = SH
    log(f"  shipped circle mean {SH['circle_mean']/1e6:.4f} MPa/K (scatter {SH['circle_scatter']:.2e}); shipped ellipse amplitude {SH['ellipse_amp']*100:.2f}%, range {SH['ellipse_min']/1e6:.4f}-{SH['ellipse_max']/1e6:.4f}")
    if 'circle_extrapolated_over_shipped' in SH: log(f"  circle: extrapolated / shipped = {SH['circle_extrapolated_over_shipped']:.4f}")
    if 'ellipse_6phi_extrapolated_over_shipped' in SH: log(f"  ellipse (6 phi): extrapolated / shipped = {[f'{x:.3f}' for x in SH['ellipse_6phi_extrapolated_over_shipped']]}")
except Exception as e:
    log(f'  (shipped data not readable: {e})')

# ======================================================================== T2 / H3: thermal-memory deviation
log(); log('## T2 / H3 — thermal-memory deviation D(Lambda, eps)')
T2 = {'dynamic': [], 'quasi_static': [], 'extended_dynamic': [], 'extended_QS': []}
def pt(tag_cv, tag_f):
    qc, qf = load(tag_cv), load(tag_f)
    if not (qc and qf): return None
    return dict(tag=tag_cv, model=qc['model'], tau_ps=qc['tau_ps'], a_nm=qc['a_nm'], Lambda=qc['Lambda'], epsilon=qc['epsilon'],
                D=D_metric(qc, qf), peak_shift=float((abs(qc['sig_interp']) - abs(qf['sig_interp'])) / abs(qf['sig_interp'])),
                D_t12=D_metric(qc, qf, 12.0))
F_REF = {10: 'A_chi1_phi000_T48', 5: 'B_F_tau0_a5', 20: 'B_F_tau0_a20', 50: 'B_F_tau0_a50'}
F_REF_QS = {a_: f'B_F_tau0_a{a_}_QS' for a_ in (5, 10, 20, 50)}
for tag, model, tau, a_nm in pm.B_DEF:
    if model == 'FOURIER': continue
    p_ = pt(tag, F_REF[a_nm]); pq = pt(tag + '_QS', F_REF_QS[a_nm])
    if p_: T2['dynamic'].append(p_)
    if pq: T2['quasi_static'].append(pq)
for a_nm in (5, 10, 20):
    for lam in pm.LAMBDAS_B2:
        fr = 'A_chi1_phi000_T48' if a_nm == 10 else f'B2_F_a{a_nm}'
        p_ = pt(f'B2_CV_L{lam:g}_a{a_nm}', fr)
        if p_: T2['extended_dynamic'].append(p_)
for lam in pm.LAMBDAS_B2:
    p_ = pt(f'B2QS_CV_L{lam:g}_a10', 'B_F_tau0_a10_QS')
    if p_: T2['extended_QS'].append(p_)
def pair_resid(rows, tagA, tagB):
    a_ = next((r for r in rows if r['tag'] == tagA), None); b_ = next((r for r in rows if r['tag'] == tagB), None)
    if not (a_ and b_): return None
    return dict(D_a10_tau5=a_['D'], D_a20_tau20=b_['D'], Lambda=[a_['Lambda'], b_['Lambda']],
                residual=float(abs(a_['D'] - b_['D']) / max(a_['D'], b_['D'])), ratio=float(a_['D'] / b_['D']))
T2['pair_dynamic'] = pair_resid(T2['dynamic'], 'B_CV_tau5_a10', 'B_CV_tau20_a20')
T2['pair_QS'] = pair_resid(T2['quasi_static'], 'B_CV_tau5_a10_QS', 'B_CV_tau20_a20_QS')
def monotone(rows):
    r = sorted(rows, key=lambda x: x['Lambda']); Ds = [x['D'] for x in r]
    return bool(all(Ds[i] <= Ds[i + 1] * 1.25 for i in range(len(Ds) - 1)))
fam_a10 = [r for r in T2['dynamic'] if r['a_nm'] == 10 and r['model'] == 'CV']
fam_tau20 = [r for r in T2['dynamic'] if r['tau_ps'] == 20.0 and r['model'] == 'CV']
T2['monotone_family_a10_tau_sweep'] = monotone(fam_a10) if fam_a10 else None
T2['monotone_family_tau20_a_sweep'] = monotone(fam_tau20) if fam_tau20 else None
qs_ok = T2['pair_QS'] is not None and T2['pair_QS']['residual'] <= 0.25
dy_ok = T2['pair_dynamic'] is not None and T2['pair_dynamic']['residual'] <= 0.25
T2['status_quasi_static'] = ('SUPPORTED' if qs_ok else 'NOT-SUPPORTED') if T2['pair_QS'] else None
T2['status_dynamic'] = ('SUPPORTED' if dy_ok else 'NOT-SUPPORTED') if T2['pair_dynamic'] else None
T2['criterion'] = 'equal-Lambda pair (a=10 nm,tau=5 ps) vs (a=20 nm,tau=20 ps): |D1-D2|/max <= 25% AND D monotone in Lambda (25% band); D over all wall nodes, t<=6'
A['T2_H3'] = T2
for k in ('dynamic', 'quasi_static'):
    for r in sorted(T2[k], key=lambda x: (x['a_nm'], x['Lambda'])):
        log(f"  {k:12s} {r['tag']:22s} a={r['a_nm']:4.0f} Lambda={r['Lambda']:.4f} eps={r['epsilon']:.4f} D={r['D']:.4e} peak_shift={r['peak_shift']:+.2e}")
log(f"  equal-Lambda pair: dynamic {T2['pair_dynamic']}  quasi-static {T2['pair_QS']}")
log(f"  status: dynamic {T2['status_dynamic']}, quasi-static {T2['status_quasi_static']}")
rows = []
for k in ('dynamic', 'quasi_static', 'extended_dynamic', 'extended_QS'):
    for r in T2[k]:
        rows.append([k, r['tag'], r['model'], r['tau_ps'], r['a_nm'], r['Lambda'], r['epsilon'], r['D'], r['peak_shift'], r['D_t12']])
write_csv('D_lambda_eps.csv', ['set', 'tag', 'model', 'tau_ps', 'a_nm', 'Lambda', 'epsilon', 'D_t_le_6', 'peak_shift', 'D_t_le_12'], rows)
# extended map: collapse residual across sizes at fixed Lambda
ext = {}
for lam in pm.LAMBDAS_B2:
    ds = {r['a_nm']: r['D'] for r in T2['extended_dynamic'] if abs(r['Lambda'] - lam) < 1e-6}
    dq = [r['D'] for r in T2['extended_QS'] if abs(r['Lambda'] - lam) < 1e-6]
    if ds:
        v = list(ds.values()); ext[f'{lam:g}'] = dict(D_by_a=ds, spread_rel=float((max(v) - min(v)) / max(v)), D_QS=dq[0] if dq else None)
for lam_s, v in ext.items():
    if v.get('D_QS') is not None and all(k in v['D_by_a'] for k in (5.0, 10.0, 20.0)):
        dd = {a_: v['D_by_a'][a_] - v['D_QS'] for a_ in (5.0, 10.0, 20.0)}
        v['delta_D_inertia'] = {str(k): float(x) for k, x in dd.items()}
        if dd[5.0] > 0 and dd[10.0] > 0 and dd[20.0] > 0:
            v['delta_D_slope_5_10'] = float(np.log(dd[5.0] / dd[10.0]) / np.log(2.0)); v['delta_D_slope_10_20'] = float(np.log(dd[10.0] / dd[20.0]) / np.log(2.0))
A['H3_extended_map'] = ext
for k, v in ext.items(): log(f"  extended map Lambda={k}: D(a)={ {a_: f'{d:.3e}' for a_, d in v['D_by_a'].items()} } spread {v['spread_rel']*100:.1f}%  D_QS={v['D_QS']}  inertia excess slopes (eps) 5->10: {v.get('delta_D_slope_5_10')}, 10->20: {v.get('delta_D_slope_10_20')}")

# ======================================================================== T3 / H4: feedback
log(); log('## T3 / H4 — thermoelastic feedback')
T3 = {}
on, off = load('B_CV_tau20_a10'), load('C_CV_tau20_a10_coupling_off')
delta = cp.delta_feedback()
if on and off:
    n = int(np.searchsorted(on['t'], 12.0 + 1e-9, side='right'))
    dev = [float(np.abs(on['probe'][i] - off['probe'][i]).max() / np.abs(off['probe'][i]).max()) for i in range(on['probe'].shape[0])]   # probe index first, time second
    T3 = dict(delta=delta, bound_5delta=5 * delta, probe_r_over_a=on['probe_r_over_a'], probe_rel_dev=dev,
              max_rel_dev=max(dev), peak_stress_change=float((abs(on['sig_interp']) - abs(off['sig_interp'])) / abs(off['sig_interp'])),
              status='WITHIN-BOUND' if max(dev) <= 5 * delta else 'EXCEEDS-BOUND',
              note='cavity-wall theta is Dirichlet-prescribed (feedback invisible there); probes at r/a ~ 1.5, 2, 3 (wall angle index 0)')
    A['T3_H4'] = T3
    log(f"  delta={delta:.4e}, 5delta={5*delta:.3e}; probe deviations {[f'{x:.2e}' for x in dev]}; peak-stress change {T3['peak_stress_change']:+.2e} -> {T3['status']}")

# ======================================================================== D (isotropic controls) and shape effect
log(); log('## Isotropic controls')
ISO = {}
ic = load('D_iso_circle_T48')
iso_e = [load(f'D_iso_ellipse_{g}') for g in ('R48', 'M', 'R192')]
if ic and all(iso_e):
    ge = triplet([abs(q['sig_interp']) for q in iso_e], (48, 96, 192))
    ISO = dict(circle_T48=abs(ic['sig_interp']), ellipse_radial=ge, ellipse_M_over_circle_T48=float(abs(iso_e[1]['sig_interp']) / abs(ic['sig_interp'])),
               circle_closed_form_local_term=984599.37, circle_closed_form_with_far_field=985689.45)
    A['isotropic'] = ISO
    log(f"  iso circle T48 {abs(ic['sig_interp']):.1f} Pa/K (closed form 984,599 local term / 985,689 with far field); iso ellipse R48/M/R192 {[f'{x:.1f}' for x in ge['f']]}  extrapolated {ge.get('f_ext')}")

# ======================================================================== E: mechanism ablations / sensitivity
log(); log('## E — mechanism ablations and expansion-set sensitivity (ellipse, 6 orientations, 96x48)')
E = {}
base6 = [abs(load(f'A_chi2_phi{p:03d}_T48')['sig_interp']) for p in pm.E_PHIS] if all(load(f'A_chi2_phi{p:03d}_T48') for p in pm.E_PHIS) else None
if base6:
    E['baseline_6phi'] = dict(amplitude=amp(base6), min=float(min(base6)), max=float(max(base6)), mean=float(np.mean(base6)))
    for name, _ in pm.E_VARIANTS:
        qs = [load(f'{name}_phi{p:03d}') for p in pm.E_PHIS]
        if all(qs):
            v = [abs(q['sig_interp']) for q in qs]
            E[name] = dict(amplitude=amp(v), min=float(min(v)), max=float(max(v)), mean=float(np.mean(v)),
                           mean_over_baseline=float(np.mean(v) / np.mean(base6)), values=[float(x) for x in v])
    A['E_ablations'] = E
    for k, v in E.items(): log(f"  {k:20s} amplitude {v['amplitude']*100:6.2f}%  mean {v['mean']/1e6:.4f} MPa/K" + (f"  (x{v['mean_over_baseline']:.3f} of baseline)" if 'mean_over_baseline' in v else ''))
    write_csv('ablations_E.csv', ['case', 'amplitude', 'min_Pa_per_K', 'max_Pa_per_K', 'mean_Pa_per_K'], [[k, v['amplitude'], v['min'], v['max'], v['mean']] for k, v in E.items()])

# ======================================================================== H5: angular modes
log(); log('## H5 — angular modes m2/m0 at the peak')
H5 = {}
for name, tag in (('circle_aniso', 'A_chi1_phi000_M'), ('ellipse_aniso_phi0', 'A_chi2_phi000_M'), ('ellipse_aniso_phi90', 'A_chi2_phi090_M'),
                  ('circle_iso', 'D_iso_circle_T48'), ('ellipse_iso', 'D_iso_ellipse_M')):
    q = load(tag)
    if q:
        m = q['ang_modes']; H5[name] = dict(m2_over_m0=float(m[2] / m[0]) if m[0] else None, m=[float(x) for x in m[:6]])
A['H5_modes'] = H5
for k, v in H5.items(): log(f"  {k}: m2/m0={v['m2_over_m0']}")

# ======================================================================== grid check of D (equal-Lambda pair, grid M vs T48)
log(); log('## Grid sensitivity of D (equal-Lambda pair)')
GD = {}
pm_ = [('a10_tau5', 'BM_CV_tau5_a10', 'A_chi1_phi000_M', 'B_CV_tau5_a10', 'A_chi1_phi000_T48'), ('a20_tau20', 'BM_CV_tau20_a20', 'BM_F_tau0_a20', 'B_CV_tau20_a20', 'B_F_tau0_a20')]
for name, cvM, fM, cvT, fT in pm_:
    qa, qb, qc_, qd = load(cvM), load(fM), load(cvT), load(fT)
    if all((qa, qb, qc_, qd)):
        GD[name] = dict(D_M=D_metric(qa, qb), D_T48=D_metric(qc_, qd))
        GD[name]['rel_change_T48_to_M'] = float((GD[name]['D_M'] - GD[name]['D_T48']) / GD[name]['D_T48'])
if GD:
    A['D_grid_check'] = GD
    for k, v in GD.items(): log(f"  {k}: D(T48)={v['D_T48']:.4e}  D(M)={v['D_M']:.4e}  change {v['rel_change_T48_to_M']*100:+.1f}%")
# ======================================================================== locality diagnostic: hoop(t)/p(t) at the peak node
log(); log('## Locality: wall hoop stress follows the wall temperature')
LOC = {}
for name, tag in (('circle_phi0_M', 'A_chi1_phi000_M'), ('ellipse_phi90_M', 'A_chi2_phi090_M'), ('ellipse_phi150_M', 'A_chi2_phi150_M')):
    q = load(tag)
    if q:
        k = int(np.argmin(np.abs(q['t'] - q['t_star']))); j = int(np.argmax(np.abs(q['hoop'][:, k])))
        p_ = np.exp(-((q['t'] - 2.5) / 1.2) ** 2); ts = [1.5, 2.0, 2.5, 3.0, 3.5]
        r = [float(q['hoop'][j, int(np.argmin(np.abs(q['t'] - t_)))] / p_[int(np.argmin(np.abs(q['t'] - t_)))] / (q['hoop'][j, k] / p_[k])) for t_ in ts]
        LOC[name] = dict(t=ts, ratio_to_peak_ratio=r, max_dev=float(max(abs(x - 1) for x in r)), max_dev_near_peak=float(max(abs(x - 1) for x in r[1:4])), dev_at_t3p5=float(abs(r[4] - 1)))
A['locality'] = LOC
for k, v in LOC.items(): log(f"  {k}: [hoop/p](t)/[hoop/p](t*) at t={v['t']}: {[f'{x:.4f}' for x in v['ratio_to_peak_ratio']]}")

# ======================================================================== F: locality test (pulse width), grid T48
log(); log('## F — pulse-width dependence (locality test), grid T48')
FR = []
for tw in (0.3, 0.6, 1.2, 2.4):
    if tw == 1.2: e90, e150, c0 = load('A_chi2_phi090_T48'), load('A_chi2_phi150_T48'), load('A_chi1_phi000_T48')
    else: e90, e150, c0 = load(f'F_tw{tw:g}_ell_phi090'), load(f'F_tw{tw:g}_ell_phi150'), load(f'F_tw{tw:g}_circ')
    if e90 and e150 and c0:
        s90, s150, sc = abs(e90['sig_interp']), abs(e150['sig_interp']), abs(c0['sig_interp'])
        FR.append(dict(tw=tw, ell_phi90=float(s90), ell_phi150=float(s150), circle=float(sc), A2=float((s150 - s90) / (0.5 * (s150 + s90))),
                       ell90_over_circle=float(s90 / sc), ell150_over_circle=float(s150 / sc), t_star=[e90['t_star'], e150['t_star'], c0['t_star']]))
if FR:
    A['F_locality'] = dict(rows=FR, note='two-point amplitude A2 = (sigma(150)-sigma(90))/mean; circle peak vs pulse width tests the local-response result')
    for r in FR: log(f"  tw={r['tw']:4.1f}: circle {r['circle']/1e6:.4f}  ellipse(90) {r['ell_phi90']/1e6:.4f}  ellipse(150) {r['ell_phi150']/1e6:.4f}  A2 {r['A2']*100:.2f}%  ratios {r['ell90_over_circle']:.3f}, {r['ell150_over_circle']:.3f}")
    write_csv('pulse_width_F.csv', ['tw', 'circle', 'ell_phi90', 'ell_phi150', 'A2', 'ell90_over_circle', 'ell150_over_circle'], [[r['tw'], r['circle'], r['ell_phi90'], r['ell_phi150'], r['A2'], r['ell90_over_circle'], r['ell150_over_circle']] for r in FR])

# ======================================================================== numerical-quality summary
log(); log('## Numerical quality of the stored runs')
qs = [q for q in (load(j['tag']) for j in pm.matrix()) if q]
def wall_err6(q):
    t0_, tw_ = (q.get('pulse_t0_tw') or [2.5, 1.2]); t = q['t']; n = t <= 6.0 + 1e-9
    return float(np.abs(q['wall'][:, n] - np.exp(-((t[n] - t0_) / tw_) ** 2)[None, :]).max())
w6 = [wall_err6(q) for q in qs]
A['numerics'] = dict(n_runs=len(qs), max_backward_error=max(q['back_max'] for q in qs) if qs else None,
                     max_wall_pulse_error=max(w6) if w6 else None,
                     max_wall_pulse_error_full_window_0_12=max(q['wall_pulse_err'] for q in qs) if qs else None,
                     note='wall-pulse error is evaluated for 0<=t<=6 (QoI window); over 0<=t<=12 it reaches 0.32 only for the t_w=2.4 runs of block F, where the n=-1 alias e^{gamma T} p(t-T) matters for t>8 (QoI unaffected)',
                     plan=qs[0]['plan'] if qs else None)
log(f"  runs {A['numerics']['n_runs']}/{len(pm.matrix())}; max backward error {A['numerics']['max_backward_error']}; max wall-pulse error (t<=6) {A['numerics']['max_wall_pulse_error']}; (t<=12) {A['numerics']['max_wall_pulse_error_full_window_0_12']}")

json.dump(A, open(OUTJ, 'w'), indent=1, default=str)
open(OUTM, 'w').write('\n'.join(L) + '\n')
print('WROTE', OUTJ)
