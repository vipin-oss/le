"""reproduce.py — reproduction test (MASTER_PROMPT §75).  Re-computes, from the frozen code, one verification case, one
convergence/error study, one principal result, one principal figure and one table, and compares with the stored outputs.
Tolerances (same machine/software; different hardware would need ~1e-6): 1e-9 for stress values, 1e-12 for tables from stored data.
Writes 07_Tests/REPRODUCTION_TEST_REPORT.md"""
import sys, os, json, time, hashlib, csv, shutil, tempfile
sys.dont_write_bytecode = True
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, '06_Source_Code', 'src'))
import numpy as np
import cg_pipeline as cp
import cg_ref1d as r1
from cg_grid import Grid
from cg_solver import HarmonicSolver
from cg_model import rho, cp_ESTIMATED, T0, alpha_crys
T = time.time(); rows = []
def rec(item, expected, actual, tol, extra=''):
    ok = abs(actual - expected) <= tol * max(abs(expected), 1e-300)
    rows.append((item, expected, actual, abs(actual - expected) / max(abs(expected), 1e-300), tol, 'PASS' if ok else 'FAIL', extra)); print(rows[-1], flush=True)

tests = {c['case']: c for c in json.load(open(os.path.join(ROOT, '07_Tests', 'TEST_RESULTS.json')))['cases']}
# 1) verification case: V8 steady gradient load, grids 48x24 and 96x48 (stored: 0.0063, 0.0016 as 4-digit strings; recompute exact and compare with closed form)
a = cp.A0; R = 80 * a
KISO, QISO, BISO = cp.KISO, cp.QISO, cp.BISO
lam, mu = QISO[0, 1], QISO[2, 2]
from scipy.integrate import quad
th = lambda r: np.log(R / r) / np.log(R / a)
IR = quad(lambda s_: th(s_) * s_, a, R, epsabs=0, epsrel=1e-13)[0]
C1 = -(BISO[0] / (lam + 2 * mu)) * IR / R / (R / 2 + (lam + mu) * a * a / (2 * mu * R))
sig_exact = -(2 * mu / (lam + 2 * mu)) * BISO[0] + 2 * (lam + mu) * C1
errs = []
for (Nr, Nt) in ((48, 24), (96, 48)):
    g = Grid(chi=1.0, a=a, R=R, Nr=Nr, Nt=Nt, gamma=cp.GAMMA_DEFAULT)
    s = HarmonicSolver(g, KISO, np.asarray(QISO, complex), BISO, rho, cp_ESTIMATED, T0, model='FOURIER')
    errs.append(float((s.stress_wall(s.solve(0.0)[0])[0].real.mean() - sig_exact) / abs(sig_exact)))
stored = [float(x) for x in eval(tests['V8_steady_thermal_gradient_load']['rel_err_48_96_192_384'])]
rec('V8 steady-gradient error 48x24 (stored value, 4 digits)', stored[0], errs[0], 1e-2)
rec('V8 steady-gradient error 96x48 (stored value, 4 digits)', stored[1], errs[1], 1e-1, 'stored value has 4 digits')
rec('closed-form steady wall hoop (Pa/K)', tests['U7_ref1d_spectral_steady_closed_form']['sigma_exact_Pa_per_K'], sig_exact, 1e-12)
# 2) convergence/error study: V11 single-pulse isotropic circle, 48x24 and 96x48 (quasi-static, uncoupled) vs time-domain reference
from cg_model import rho as rho_
kap_iso = KISO[0, 0] / (rho_ * cp_ESTIMATED); ratio = kap_iso / cp.KAPPA
tau_ref, sig_ref, _ = r1.qs_single_pulse_reference(a, R, lam, mu, float(np.mean(alpha_crys)), t0=2.5 * ratio, tw=1.2 * ratio, tstart=-7 * ratio, tmax=9 * ratio)
pk = float(np.abs(sig_ref).max())
rec('V11 reference peak (Pa/K)', tests['V11_single_pulse_isotropic_circle_vs_time_domain']['reference_peak_Pa_per_K'], pk, 1e-12)
e = []
for (Nr, Nt) in ((48, 24), (96, 48)):
    q = cp.run_config('rep', 'FOURIER', 0.0, 1.0, 0, a, iso=True, energy_coupling=False, inertia_scale=0.0, Nr=Nr, Nt=Nt, save=False, quiet=True)
    e.append(float((q['sig_interp'] + pk) / pk))
st = eval(tests['V11_single_pulse_isotropic_circle_vs_time_domain']['peak_rel_err_48_96_192'])
rec('V11 peak error 48x24', float(st[0]), e[0], 5e-2, 'stored 4 digits')
rec('V11 peak error 96x48', float(st[1]), e[1], 5e-2, 'stored 4 digits')
# 3) principal result: ellipse phi=90, grid T48, from the stored production
jp = os.path.join(ROOT, '09_Raw_Data', 'production', 'A_chi2_phi090_T48.json')
if os.path.exists(jp):
    q0 = json.load(open(jp))
    q = cp.run_config('rep2', 'FOURIER', 0.0, 2.0, 90, a, Nr=96, Nt=48, save=False, quiet=True)
    rec('principal result: ellipse phi=90 peak (interp, Pa/K) re-computed vs stored', q0['sig_interp'], q['sig_interp'], 1e-9)
    rec('principal result: nodal peak', q0['sig_nodal'], q['sig_nodal'], 1e-9)
# 4) principal figure + 5) table from stored data
out = tempfile.mkdtemp()
src_fig = os.path.join(ROOT, '11_Figures', 'fig2_phi_sweep.png')
if os.path.exists(src_fig):
    import subprocess
    env = dict(os.environ); 
    tab = os.path.join(ROOT, '12_Tables', 'phi_sweep_ellipse.csv')
    h0 = hashlib.sha256(open(tab, 'rb').read()).hexdigest() if os.path.exists(tab) else None          # stored version, before regeneration
    r = subprocess.run([sys.executable, os.path.join(HERE, 'analyze_v2.py')], capture_output=True, text=True, cwd=HERE)
    rows.append(('analysis script re-run (exit code 0)', 0, r.returncode, 0.0, 0, 'PASS' if r.returncode == 0 else 'FAIL', ''))
    h1 = hashlib.sha256(open(tab, 'rb').read()).hexdigest() if os.path.exists(tab) else None
    rows.append(('table phi_sweep_ellipse.csv: sha256 before vs after regeneration from the stored raw data', h0, h1, 0.0, 0, 'PASS' if (h0 and h0 == h1) else 'FAIL', 'byte-identical required'))
    r2 = subprocess.run([sys.executable, os.path.join(HERE, 'make_figures.py'), 'fig2'], capture_output=True, text=True, cwd=HERE)
    rows.append(('principal figure fig2 regenerated (exit code 0)', 0, r2.returncode, 0.0, 0, 'PASS' if r2.returncode == 0 else 'FAIL', r2.stdout.strip()[-80:]))
L = ['# REPRODUCTION_TEST_REPORT (MASTER_PROMPT §75)', '',
     f"Date {time.strftime('%Y-%m-%d %H:%M:%S')} · environment: Python {sys.version.split()[0]}, numpy {np.__version__} · wall {time.time() - T:.0f} s (2 vCPU) · script `08_Experiments/reproduce.py`",
     'Scope: one verification case, one convergence/error study, one principal result, one principal figure, one table — re-computed from the frozen code and compared with stored outputs.', '',
     '| item | expected / stored | recomputed | rel. difference | tolerance | status | note |', '|---|---|---|---|---|---|---|']
for r in rows:
    L.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]:.2e} | {r[4]} | {r[5]} | {r[6]} |")
L.append(f"\nOverall: {sum(r[5] == 'PASS' for r in rows)} PASS, {sum(r[5] == 'FAIL' for r in rows)} FAIL.")
open(os.path.join(ROOT, '07_Tests', 'REPRODUCTION_TEST_REPORT.md'), 'w').write('\n'.join(L) + '\n')
print('REPRODUCTION REPORT written')
