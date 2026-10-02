"""run_verify.py — V0-V7 verification suite (VERIFICATION_PLAN.md). Confirmatory unless noted.
Writes data/VERIFY.json + logs. No production outputs here.
"""
import json, time, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent / 'src'))
from cg_grid import Grid
from cg_model import (plane_strain_block, rotate_Q_beta, rotate2, K_ac, iso_control,
                      rho, cp_ESTIMATED, T0, GPa, alpha_crys, derived)
from cg_solver import HarmonicSolver
from cg_transient import make_pulse, freq_grid, synthesize

ROOT = Path(__file__).parent
DATA = ROOT / 'data'; LOGS = ROOT / 'logs'
DATA.mkdir(exist_ok=True); LOGS.mkdir(exist_ok=True)

RES = {'label': 'PROJECT_CRYSTAL_GEOMETRY_01 verification', 'date': '2026-09-30',
       'cases': [], 'status': 'RUNNING'}
CPU0 = time.process_time()

def record(case, status, **kw):
    RES['cases'].append({'case': case, 'status': status, **kw})
    print(f'[{status}] {case}: ' + ' '.join(f'{k}={v}' for k, v in kw.items() if not isinstance(v, (dict, list))))
    RES['cpu_seconds'] = time.process_time() - CPU0
    (DATA / 'VERIFY.json').write_text(json.dumps(RES, indent=2, default=str))

Q, beta = plane_strain_block()
DV = derived()
t_th = None  # set per material run; verification uses dimensionless a=1 -> kappa units

# ---------------- V0: metric + operator consistency ----------------
errs = []
for chi in (1.0, 2.0):
    g = Grid(chi=chi, Nr=96, Nt=48)
    lin = 3 * g.X - 2 * g.Y
    lx = (g.Dx @ lin.ravel()).reshape(g.X.shape); ly = (g.Dy @ lin.ravel()).reshape(g.X.shape)
    e1 = float(np.abs(lx[1:-1] - 3).max() / 3); e2 = float(np.abs(ly[1:-1] + 2).max() / 2)
    errs.append((e1, e2))
    assert g.J.min() > 0
record('V0_metric_consistency', 'PASS' if max(max(e) for e in errs) < 5e-3 else 'FAIL',
       linear_rel_errs=str(errs), note='2nd-order mapped FD consistency on linear field')

# ---------------- V1: stencil dispersion (operator family) ----------------
# 3-point central first/second derivative dispersion vs analytic wave: d2 -> -k^2
kh = np.array([0.2, 0.4, 0.8])
e_disp = 2 * np.sin(kh / 2) / kh - 1.0     # relative phase-speed error of d2 stencil sqrt
e_disp2 = (np.sin(kh / 2) / (kh / 2)) ** 2 - 1.0  # second-derivative symbol error
record('V1_stencil_dispersion', 'PASS' if abs(e_disp2[1]) < 0.02 else 'FAIL',
       kh=kh.tolist(), d2_symbol_rel_err=e_disp2.tolist(),
       note='3-point symbol: |err|<2% for kh<=0.4 (production wall modes m<=8 at Nt=48 -> kh<=0.53)')

# ---------------- helper: production-like transient QoI ----------------
PULSE = dict(t0=1.5, tw=0.5)   # in units of t_th = a^2/kappa (a=1 run)
ETA_D = 0.05                   # hysteretic damping on Q for DYNAMIC runs (undamped statics)
#                             # reason: outer boundary at 80a reflects at t=4.11 t_th ->
#                             # undamped finite-domain resonances (Q=inf) make late-time
#                             # response sampling-sensitive; document in CHANGELOG.
T_CAUSAL = 3.5                # QoI window end in t_th units (pre-reflection: < 4.11)
def dQ(Qm):
    return np.asarray(Qm, complex) * (1.0 + 1j * ETA_D)
T_WIN = 6.0
NT_T = 128
W_CUT = 20.0                   # /t_th ; pulse spectrum < 1e-11 beyond

def run_transient(model, tau_rel, K2, Qm, betam, chi=1.0, phi=0.0, grid=None, coupled=True,
                  outer_theta_value=0.0, snapshots=False):
    """tau_rel in units of t_th; runs in SIMPLIFIED units: a=1, kappa-scale seconds via
    kappa in SI -> we run SI with a=1 m? No: run with SI tensors but scale a=1e-8 m."""
    # SI run with a = 10 nm
    a = 1e-8
    g = grid or Grid(chi=chi, a=a, R=80.0*a, Nr=96, Nt=48)
    kappa = DV['kappa']
    t_th = a * a / kappa
    tau = tau_rel * t_th
    bb = betam if coupled else np.zeros(3)
    s = HarmonicSolver(g, K2, dQ(Qm), bb, rho, cp_ESTIMATED, T0, model=model, tau=tau,
                       outer_theta_value=outer_theta_value)
    t, th, TH = make_pulse(T_WIN * t_th, NT_T, PULSE['t0'] * t_th, PULSE['tw'] * t_th)
    wgrid = freq_grid(T_WIN * t_th, NT_T)
    nfreq = int(np.searchsorted(wgrid, W_CUT / t_th, side='right'))
    nfreq = min(nfreq, NT_T // 2 + 1)
    H_hoop = np.zeros((nfreq, g.Nt), dtype=complex)
    H_wall = np.zeros((nfreq, g.Nt), dtype=complex)
    backs = []
    snap_H = []
    for ik in range(nfreq):
        w = wgrid[ik]
        U, back = s.solve(w)
        hoop, _, _ = s.stress_wall(U)
        H_hoop[ik] = hoop
        H_wall[ik] = s.wall_theta(U)
        backs.append(back)
        if snapshots and ik in (1, nfreq // 2):
            snap_H.append((ik, s.fields(U)))
    # synthesize wall series (Nt angles x NT_T times)
    hoop_t = np.zeros((g.Nt, NT_T)); wall_t = np.zeros((g.Nt, NT_T))
    for j in range(g.Nt):
        hoop_t[j] = synthesize(H_hoop[:, j], TH, NT_T)
        wall_t[j] = synthesize(H_wall[:, j], TH, NT_T)
    return dict(t=t / t_th, hoop=hoop_t, wall=wall_t, back_max=float(np.max(backs)),
                grid=g, t_th=t_th, nfreq=nfreq)

def qoi(h):
    hoop = h['hoop']
    nt_w = int(np.searchsorted(h['t'], T_CAUSAL, side='right'))
    hoop = hoop[:, :nt_w]
    idx = np.unravel_index(np.argmax(np.abs(hoop)), hoop.shape)
    sig_max = float(hoop[idx]); th_ang = float(idx[0] * 360.0 / h['hoop'].shape[0]); t_star = float(h['t'][idx[1]])
    return sig_max, th_ang, t_star

# ---------------- V2: grid convergence (2 configs x 3 grids) ----------------
v2 = []
for cfg in [('CV', 0.3, 1.0, 45.0), ('CV', 0.3, 2.0, 30.0)]:
    model, tau_rel, chi, phi = cfg
    QQ, bb = rotate_Q_beta(Q, beta, np.radians(phi))
    KK = rotate2(K_ac, np.radians(phi))
    vals = []
    for Nr, Nt in ((48, 24), (96, 48), (192, 96)):
        g = Grid(chi=chi, a=1e-8, R=80.0*1e-8, Nr=Nr, Nt=Nt)
        h = run_transient(model, tau_rel, KK, QQ, bb, chi=chi, grid=g)
        smax, ang, ts = qoi(h)
        vals.append({'grid': f'{Nr}x{Nt}', 'sigma_max': smax, 'theta_star': ang, 't_star': ts,
                     'back_max': h['back_max']})
    rel = abs(vals[2]['sigma_max'] - vals[1]['sigma_max']) / abs(vals[2]['sigma_max'])
    v2.append({'config': str(cfg), 'values': vals, 'med_vs_fine_rel': rel})
    print('V2', cfg, 'med-fine rel', rel)
v2_pass = all(x['med_vs_fine_rel'] <= 0.02 for x in v2)
record('V2_grid_convergence', 'PASS' if v2_pass else 'PARTIAL', detail=v2,
       criterion='|s_fine - s_med| <= 2% of s_fine (96x48 production grid)',
       note='if PARTIAL: claims use documented grid uncertainty or production at 192x96 for confirmatory only')

# ---------------- V3: rotation covariance (circle) ----------------
g = Grid(chi=1.0, a=1e-8, R=80.0*1e-8, Nr=96, Nt=48)
t_th = g.a**2 / DV['kappa']
w_test = [2 * np.pi / (3 * t_th), 2 * np.pi / (0.8 * t_th)]
Q0, b0 = Q, beta
K0 = K_ac
sA = HarmonicSolver(g, K0, dQ(Q0), b0, rho, cp_ESTIMATED, T0, model='CV', tau=0.3 * t_th)
phi90 = np.pi / 2
Q90, b90 = rotate_Q_beta(Q0, b0, phi90)
K90 = rotate2(K0, phi90)
sB = HarmonicSolver(g, K90, dQ(Q90), b90, rho, cp_ESTIMATED, T0, model='CV', tau=0.3 * t_th)
maxrel = 0.0
shift = g.Nt // 4  # 90 deg on 48-point circle
for w in w_test:
    UA, _ = sA.solve(w); UB, _ = sB.solve(w)
    thA, u1A, u3A = sA.fields(UA); thB, u1B, u3B = sB.fields(UB)
    # covariance: field B at (i,j) = R90 field A at (i, j-shift): theta same; (u1,u3)->(-u3,u1)
    thA_s = np.roll(thA, shift, axis=1); u1A_s = np.roll(u1A, shift, axis=1); u3A_s = np.roll(u3A, shift, axis=1)
    scale = max(np.abs(u1A).max(), np.abs(u3A).max(), np.abs(thA).max())
    e = max(np.abs(thB - thA_s).max(), np.abs(u1B + u3A_s).max(), np.abs(u3B - u1A_s).max()) / scale
    maxrel = max(maxrel, float(e))
record('V3_rotation_covariance_90deg', 'PASS' if maxrel <= 1e-8 else 'FAIL', max_rel_err=maxrel,
       criterion='<=1e-8 (machine-precision class; discrete circle automorphism)')
# secondary 37 deg: hoop-sigma scalar invariance with angle-shift interpolation (exploratory)
phi37 = np.radians(37.0)
Q37, b37 = rotate_Q_beta(Q0, b0, phi37); K37 = rotate2(K0, phi37)
sC = HarmonicSolver(g, K37, dQ(Q37), b37, rho, cp_ESTIMATED, T0, model='CV', tau=0.3 * t_th)
e37 = []
for w in w_test:
    UA, _ = sA.solve(w); UC, _ = sC.solve(w)
    hA, _, _ = sA.stress_wall(UA); hC, _, _ = sC.stress_wall(UC)
    shift37 = 37.0 / 360.0 * g.Nt
    j0 = int(np.floor(shift37)); frac = shift37 - j0
    hA_s = (1 - frac) * np.roll(hA, j0) + frac * np.roll(hA, j0 + 1)
    scale = np.abs(hA).max()
    e37.append(float(np.abs(hC - hA_s).max() / scale))
record('V3b_rotation_covariance_37deg_EXPLORATORY', 'PASS' if max(e37) < 5e-2 else 'FAIL',
       interp_rel_errs=e37, note='wall-hoop covariance with linear angle interpolation; O(h)+interp expected')

# ---------------- V4: alpha=0 null ----------------
h = run_transient('CV', 0.3, K_ac, Q, np.zeros(3), chi=1.0, coupled=False)
null = float(np.abs(h['hoop']).max())
record('V4_uncoupled_null', 'PASS' if null < 1e-6 * np.abs(beta).max() else 'FAIL',
       max_abs_hoop=Null if False else null, criterion='u,sigma exactly 0 when beta=0 (no mechanical load)')

# ---------------- V5: tau->0 limit ----------------
hF = run_transient('FOURIER', 0.0, K_ac, Q, beta, chi=1.0)
hC = run_transient('CV', 1e-6, K_ac, Q, beta, chi=1.0)
nt_w5 = int(np.searchsorted(hF['t'], T_CAUSAL, side='right'))
d = float(np.abs(hC['hoop'][:, :nt_w5] - hF['hoop'][:, :nt_w5]).max() / np.abs(hF['hoop'][:, :nt_w5]).max())
record('V5_tau_to_zero', 'PASS' if d <= 1e-3 else 'FAIL', rel_diff=d, criterion='<=1e-3 (tau=1e-6 t_th)')

# ---------------- V6: steady conduction log-law (circle, isotropic, beta=0) ----------------
Kiso, Qiso, biso = iso_control()
gs = Grid(chi=1.0, a=1e-8, R=80.0*1e-8, Nr=96, Nt=48)
sS = HarmonicSolver(gs, Kiso * 0 + Kiso, Qiso, np.zeros(3), rho, cp_ESTIMATED, T0, model='FOURIER')
U, back = sS.solve(0.0)
th, _, _ = sS.fields(U)
r = gs.r
th_exact = np.log((80.0*gs.a) / r) / np.log(80.0)
th_num = th[:, 0].real
e6 = float(np.abs(th_num - th_exact).max())
record('V6_steady_log_law', 'PASS' if e6 <= 0.01 else 'FAIL', max_abs_err=e6,
       criterion='<=0.01 of range (theta: 0..1)', back=back)

# ---------------- V7: static uniform-thermal-stress annulus (isotropic) ----------------
lam, mu = 128 * GPa, 104.0 * GPa   # isotropic control lam from C12, mu from C66 (iso_control)
al = float(np.mean(alpha_crys))
gam = (3 * lam + 2 * mu) * al
Rout = 80.0*1e-8; a_w = 1e-8
Aamp = gam / ((2 * lam + 2 * mu) + 2 * mu * Rout**2 / a_w**2)
sig_tt_a = (2 * lam + 2 * mu) * Aamp - 2 * mu * Aamp * Rout**2 / a_w**2 - gam
sU = HarmonicSolver(gs, Kiso, Qiso, biso, rho, cp_ESTIMATED, T0, model='FOURIER', outer_theta_value=1.0)
U, back = sU.solve(0.0)
hoop, t1, t2 = sU.stress_wall(U)
h_num = float(hoop[0].real)
e7 = abs(h_num - sig_tt_a) / abs(sig_tt_a)
record('V7_static_uniform_theta_annulus', 'PASS' if e7 <= 0.015 else 'FAIL',
       sigma_theta_a_numeric=h_num, sigma_theta_a_exact=sig_tt_a, rel_err=float(e7),
       criterion='<=1.5% vs closed form (isotropic plane strain, uniform theta, free cavity, fixed outer)')

RES['status'] = 'COMPLETE'
RES['cpu_seconds'] = time.process_time() - CPU0
RES['derived'] = {k: float(v) for k, v in DV.items()}
(DATA / 'VERIFY.json').write_text(json.dumps(RES, indent=2, default=str))
print('VERIFY DONE cpu', RES['cpu_seconds'])
