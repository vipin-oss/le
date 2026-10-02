"""run_convergence.py — Phase 9 (2026-10-01), revised plan.  Grid convergence (C1) is evaluated from the production data
(radial family R48/M/R192, angular family T48/M/T144; see analyze_v2.py); the mesh-direction / clustering study (C4) is
run_convergence_dirs.py.  This script runs
  C2  Bromwich-contour parameter independence (T, gamma)            [ellipse phi=90 deg, 96x48]
  C3  outer-radius (echo) sensitivity R = 80a vs 160a, a = 10 and 50 nm, peak stress and thermal-memory deviation D [circle, 96x48]
Outputs: 09_Raw_Data/convergence/*.json|npz, 10_Processed_Data/CONVERGENCE_RESULTS.json"""
import sys, os, json, time
sys.dont_write_bytecode = True
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, '06_Source_Code', 'src'))
import numpy as np
import cg_pipeline as cp
RAW = os.path.join(ROOT, '09_Raw_Data', 'convergence'); OUTJ = os.path.join(ROOT, '10_Processed_Data', 'CONVERGENCE_RESULTS.json')
os.makedirs(RAW, exist_ok=True)
CPU0 = time.process_time(); WALL0 = time.time(); RES = dict(label='Phase 9 C2/C3', date='2026-10-01', status='RUNNING')
def save():
    RES['cpu_seconds'] = time.process_time() - CPU0; RES['wall_seconds'] = time.time() - WALL0
    json.dump(RES, open(OUTJ, 'w'), indent=1, default=str)
def run(tag, model, tau_ps, chi, phi, a=cp.A0, **kw):
    jp = os.path.join(RAW, tag + '.json')
    if os.path.exists(jp):
        q = json.load(open(jp)); d = np.load(os.path.join(RAW, tag + '.npz')); q['_series'] = dict(t=d['t'], hoop=d['hoop'], wall=d['wall'], probe=d['probe']); return q
    return cp.run_config(tag, model, tau_ps, chi, phi, a, outdir=RAW, **kw)
def D_series(h_cv, h_f, t, tmax=6.0):
    n = int(np.searchsorted(t, tmax + 1e-9, side='right'))
    return float(np.abs(h_cv[:, :n] - h_f[:, :n]).max() / np.abs(h_f[:, :n]).max())
# ---------------- C2
base = run('C2_ell_phi090_T20_g0p9', 'FOURIER', 0.0, 2.0, 90, Nr=96, Nt=48)
C2 = {'T20_g0.9': dict(sig_interp=base['sig_interp'], n_solves=base['n_solves'])}
for (T, gam) in ((32.0, 0.6), (16.0, 1.1)):
    q = run(f'C2_ell_phi090_T{T:g}_g{gam:g}', 'FOURIER', 0.0, 2.0, 90, Nr=96, Nt=48, plan_kw=dict(T=T, gamma=gam))
    n = int(np.searchsorted(q['_series']['t'], 6.0 + 1e-9, side='right'))
    C2[f'T{T:g}_g{gam:g}'] = dict(sig_interp=q['sig_interp'], rel_diff_sig=float(abs(q['sig_interp'] - base['sig_interp']) / abs(base['sig_interp'])),
                                  series_max_rel_diff=float(np.abs(q['_series']['hoop'][:, :n] - base['_series']['hoop'][:, :n]).max() / np.abs(base['_series']['hoop'][:, :n]).max()),
                                  n_solves=q['n_solves'], wall_pulse_err=q['wall_pulse_err'])
    print('C2', T, gam, C2[f'T{T:g}_g{gam:g}'], flush=True)
RES['C2'] = C2; save()
# ---------------- C3
C3 = {}
for a_nm in (10, 50):
    a = a_nm * 1e-9; rows = {}
    for Rfac, Nr in ((80.0, 96), (160.0, 191)):
        qf = run(f'C3_a{a_nm}_R{int(Rfac)}_F', 'FOURIER', 0.0, 1.0, 0, a=a, Nr=Nr, Nt=48, Rfac=Rfac)
        qc = run(f'C3_a{a_nm}_R{int(Rfac)}_CV20', 'CV', 20.0, 1.0, 0, a=a, Nr=Nr, Nt=48, Rfac=Rfac)
        rows[f'R{int(Rfac)}a'] = dict(sig_F=qf['sig_interp'], sig_CV=qc['sig_interp'],
                                      D_t_le_6=D_series(qc['_series']['hoop'], qf['_series']['hoop'], qf['_series']['t']),
                                      D_t_le_12=D_series(qc['_series']['hoop'], qf['_series']['hoop'], qf['_series']['t'], tmax=12.0),
                                      echo_roundtrip_t_th=float(2 * (Rfac - 1) * qf['epsilon']), epsilon=qf['epsilon'], Lambda_CV=qc['Lambda'])
    r80, r160 = rows['R80a'], rows['R160a']
    rows['peak_change_R80_to_R160'] = float((abs(r160['sig_F']) - abs(r80['sig_F'])) / abs(r80['sig_F']))
    rows['D_change_R80_to_R160'] = float((r160['D_t_le_6'] - r80['D_t_le_6']) / r80['D_t_le_6'])
    C3[f'a{a_nm}nm'] = rows; print('C3', a_nm, rows, flush=True)
RES['C3'] = C3; RES['status'] = 'COMPLETE'; save()
print(f"CONVERGENCE C2/C3 DONE cpu {RES['cpu_seconds']:.0f}s wall {RES['wall_seconds']:.0f}s")
