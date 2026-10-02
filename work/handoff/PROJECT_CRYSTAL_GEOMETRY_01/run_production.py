"""run_production.py — Phase 9 confirmatory production matrix (frozen-plan derived).

DESIGN RECORD (deviations from frozen plan logged in CHANGELOG/DECISION_LOG):
- Outer radius R = 80a (frozen plan said 25a with a causal claim that does not hold:
  longitudinal round trip at 25a = 2.47 t_th, i.e. before the response peak of the
  frozen pulse (t0=2.5 t_th, tw=1.2 t_th).  R=80a gives round trip 8.1 t_th (long.)
  and 14.9 t_th (shear) -> analysis window t <= 6 t_th is causally clean.)
- Pulse: t0 = 2.5 t_th, tw = 1.2 t_th  (PROBLEM_DEFINITION.md frozen values).
- Hysteretic damping eta_d = 0.05 on Q in DYNAMIC runs (undamped finite-domain
  resonances make harmonic sampling grid-sensitive; see logs/verify_rerun_v3 +
  sensitivity runs at eta_d in {0.02, 0.1}).  Static checks (V6/V7) run undamped.
- QoI window: t <= 6 t_th (pre-reflection).
- Row-equilibrated conservative operator (src/cg_ops.py + src/cg_solver.py).

BLOCK A  phi x chi  (T1/T4, H1/H2):  chi in {1,2}, phi in {0..165} step 15, Fourier,
         a=10nm  -> 24 runs
BLOCK B  Lambda/size (T2, H3): circle phi=0: CV tau in {1,5,20}ps @a=10nm; CV tau=20ps
         @a in {5,20,50}nm; Fourier @a in {5,20,50}nm; MCV3 tau in {5,20}ps @a=10nm
         -> 11 runs  (Fourier a=10 tau=0 = run A[phi=0,chi=1] reused)
BLOCK C  feedback (T3, H4): circle phi=0 a=10nm CV tau=20ps, energy_coupling=False
         -> 1 run (coupled reference reused from B)
BLOCK D  iso control (ablation): circle + ellipse phi=0 Fourier a=10nm -> 2 runs
"""
import sys, os, json, time
from pathlib import Path as _P
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import numpy as np
from cg_grid import Grid
from cg_model import (plane_strain_block, iso_control, K_ac, rotate_Q_beta,
                      rho, cp_ESTIMATED, T0, derived, GPa)
from cg_solver import HarmonicSolver
from cg_transient import make_pulse, freq_grid, synthesize

DATA = os.path.join(os.path.dirname(__file__), 'data', 'PROD')
os.makedirs(DATA, exist_ok=True)
CPU0 = time.process_time()

ETA_D = 0.05
A0 = 1e-8                 # 10 nm reference
T_WIN = 8.0               # t_th units
NT_T = 128
W_CUT = 20.0
PULSE_T0, PULSE_TW = 2.5, 1.2
T_QOI = 6.0               # causal QoI window end (t_th units)
NR, NT = 96, 48
PHIS = list(range(0, 180, 15))

Q0, BETA0 = plane_strain_block()
DV = derived()
KISO, QISO, BISO = iso_control()

def rotate2(K, th):
    c, s = np.cos(th), np.sin(th)
    R = np.array([[c, -s], [s, c]])
    return R @ np.asarray(K)[:2, :2] @ R.T

def qoi_windowed(t, hoop):
    nt = int(np.searchsorted(t, T_QOI, side='right'))
    hw = hoop[:, :nt]
    idx = np.unravel_index(np.argmax(np.abs(hw)), hw.shape)
    modes = np.abs(np.fft.fft(hoop[:, idx[1]])) / hoop.shape[0]
    return dict(sig_max=float(hoop[idx[0], idx[1]]),
                sig_abs_max=float(np.abs(hw).max()),
                theta_star_deg=float(idx[0] * 360.0 / hoop.shape[0]),
                t_star=float(t[idx[1]]),
                ang_modes=[float(m) for m in modes[:9]])

def run_config(tag, model, tau_ps, chi, phi_deg, a, coupled=True,
               iso=False, eta_d=ETA_D, grid=None, energy_coupling=True):
    t_th = a * a / DV['kappa']
    tau = tau_ps * 1e-12
    phi = np.radians(phi_deg)
    K2 = rotate2(KISO if iso else K_ac, phi) if phi_deg else (KISO if iso else K_ac)
    Qm = rotate_Q_beta(QISO if iso else Q0, BISO if iso else BETA0, phi)[0] if phi_deg else (QISO if iso else Q0)
    bb = rotate_Q_beta(QISO if iso else Q0, BISO if iso else BETA0, phi)[1] if phi_deg else (BISO if iso else BETA0)
    if not coupled:
        bb = np.zeros(3)
    g = grid or Grid(chi=chi, a=a, R=80.0 * a, Nr=NR, Nt=NT)
    Quse = np.asarray(Qm, complex) * (1.0 + 1j * eta_d) if model != 'FOURIER' or True else Qm
    # damping on dynamic solves (all harmonic solves here are dynamic-range sampled)
    s = HarmonicSolver(g, K2, Quse, bb, rho, cp_ESTIMATED, T0, model=model, tau=tau,
                       energy_coupling=energy_coupling)
    t, thp, TH = make_pulse(T_WIN * t_th, NT_T, PULSE_T0 * t_th, PULSE_TW * t_th)
    wgrid = freq_grid(T_WIN * t_th, NT_T)
    nfreq = int(np.searchsorted(wgrid, W_CUT / t_th, side='right'))
    nfreq = min(nfreq, NT_T // 2 + 1)
    H_hoop = np.zeros((nfreq, g.Nt), dtype=complex)
    H_wall = np.zeros((nfreq, g.Nt), dtype=complex)
    backs = []
    t0w = time.time()
    for ik in range(nfreq):
        U, back = s.solve(wgrid[ik])
        hoop, _, _ = s.stress_wall(U)
        H_hoop[ik] = hoop
        H_wall[ik] = s.wall_theta(U)
        backs.append(float(back))
    hoop_t = np.zeros((g.Nt, NT_T)); wall_t = np.zeros((g.Nt, NT_T))
    for j in range(g.Nt):
        hoop_t[j] = synthesize(H_hoop[:, j], TH, NT_T)
        wall_t[j] = synthesize(H_wall[:, j], TH, NT_T)
    tnorm = t / t_th
    q = qoi_windowed(tnorm, hoop_t)
    q.update(tag=tag, model=model, tau_ps=tau_ps, chi=chi, phi=phi_deg,
             a_nm=a * 1e9, coupled=coupled, iso=iso, eta_d=eta_d,
             energy_coupling=energy_coupling, nfreq=nfreq,
             back_max=max(backs), wall_rel_max=float(np.abs(wall_t).max()),
             wall_max_dev_from_1=float(np.abs(wall_t - 1.0).max()),
             cpu_s=time.process_time() - CPU0, wall_s=time.time() - t0w,
             t_th_s=t_th)
    np.savez_compressed(os.path.join(DATA, tag + '.npz'),
                        t=tnorm, hoop=hoop_t, wall=wall_t, r=g.r)
    _P(os.path.join(DATA, tag + '.json')).write_text(json.dumps(q, indent=2, default=str))
    print(f"[{tag}] sig={q['sig_max']:.6e} th*={q['theta_star_deg']:.1f} t*={q['t_star']:.3f} "
          f"|wall|max={q['wall_rel_max']:.3f} back={q['back_max']:.1e} ({q['wall_s']:.0f}s)", flush=True)
    return q

def main():
    global RESULTS
    RESULTS = []
    def record(q):
        RESULTS.append(q)
        _P(os.path.join(DATA, 'PRODUCTION_SUMMARY.json')).write_text(
            json.dumps(dict(cpu_s=time.process_time() - CPU0, runs=RESULTS), indent=2, default=str))
    
    # ---------------- BLOCK A: phi x chi ----------------
    for chi in (1.0, 2.0):
        for phi in PHIS:
            tag = f'A_chi{int(chi)}_phi{phi:03d}'
            if os.path.exists(os.path.join(DATA, tag + '.json')):
                record(json.loads(_P(os.path.join(DATA, tag + '.json')).read_text()))
                print(f'[{tag}] cached', flush=True)
                continue
            record(run_config(tag, 'FOURIER', 0.0, chi, phi, A0))
    
    # ---------------- BLOCK B: Lambda / size sweep ----------------
    B_RUNS = [
        ('B_CV_tau1_a10',  'CV',   1.0, 1.0, 0, A0),
        ('B_CV_tau5_a10',  'CV',   5.0, 1.0, 0, A0),
        ('B_CV_tau20_a10', 'CV',  20.0, 1.0, 0, A0),
        ('B_CV_tau20_a5',  'CV',  20.0, 1.0, 0, A0 / 2),
        ('B_CV_tau20_a20', 'CV',  20.0, 1.0, 0, A0 * 2),
        ('B_CV_tau20_a50', 'CV',  20.0, 1.0, 0, A0 * 5),
        ('B_F_tau0_a5',    'FOURIER', 0.0, 1.0, 0, A0 / 2),
        ('B_F_tau0_a20',   'FOURIER', 0.0, 1.0, 0, A0 * 2),
        ('B_F_tau0_a50',   'FOURIER', 0.0, 1.0, 0, A0 * 5),
        ('B_MCV3_tau5_a10',  'MCV3',  5.0, 1.0, 0, A0),
        ('B_MCV3_tau20_a10', 'MCV3', 20.0, 1.0, 0, A0),
    ]
    for tag, model, tau_ps, chi, phi, a in B_RUNS:
        if os.path.exists(os.path.join(DATA, tag + '.json')):
            record(json.loads(_P(os.path.join(DATA, tag + '.json')).read_text()))
            print(f'[{tag}] cached', flush=True)
            continue
        record(run_config(tag, model, tau_ps, chi, phi, a))
    
    # ---------------- BLOCK C: feedback off ----------------
    tag = 'C_CV_tau20_coupling_off'
    if os.path.exists(os.path.join(DATA, tag + '.json')):
        record(json.loads(_P(os.path.join(DATA, tag + '.json')).read_text()))
    else:
        record(run_config(tag, 'CV', 20.0, 1.0, 0, A0, energy_coupling=False))
    
    # ---------------- BLOCK D: iso control ----------------
    for tag, chi in (('D_iso_circle', 1.0), ('D_iso_ellipse', 2.0)):
        if os.path.exists(os.path.join(DATA, tag + '.json')):
            record(json.loads(_P(os.path.join(DATA, tag + '.json')).read_text()))
        else:
            record(run_config(tag, 'FOURIER', 0.0, chi, 0, A0, iso=True))
    
    print('PRODUCTION DONE cpu', time.process_time() - CPU0, flush=True)

if __name__ == '__main__':
    main()
