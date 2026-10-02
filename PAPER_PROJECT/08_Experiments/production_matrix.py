"""production_matrix.py — single source of truth for the Phase 11 production matrix (v2, 2026-10-01; grid family revised
after Phase 9 / P9-D001: radial clustering gamma = 5).  Imported by run_production_v2.py and analyze_v2.py.
Frozen by 02_Problem_Definition/ACCEPTANCE_CRITERIA_V2_FROZEN.md before any production run.
Blocks: A orientation x shape (pre-registered); B thermal memory / size (pre-registered, dynamic undamped);
BQS quasi-static ablation of B; BM grid check of the equal-Lambda pair; B2/B2QS extended (Lambda, eps) map (EXPLORATORY);
C feedback (pre-registered); D isotropic control; E mechanism ablations / parameter sensitivity (EXPLORATORY, specified before running).
Grids (Nr x Nt, gamma = 5): R48 = 48x96, T48 = 96x48, M = 96x96 (production), R192 = 192x96, T144 = 96x144.
Radial family R48/M/R192 (Nt = 96) and angular family T48/M/T144 (Nr = 96) give separate Richardson estimates."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), '06_Source_Code', 'src'))
import cg_pipeline as cp

A0 = cp.A0
GRIDS = {'R48': (48, 96), 'T48': (96, 48), 'M': (96, 96), 'R192': (192, 96), 'T144': (96, 144)}
COST = {'R48': 'light', 'T48': 'light', 'M': 'medium', 'R192': 'heavy', 'T144': 'heavy'}
PHIS = cp.PHIS
PHIS6 = (0, 30, 60, 90, 120, 150)
LAMBDAS_B2 = (0.05, 0.2, 0.8, 3.2)
E_VARIANTS = [('E1_alpha_cheng298', dict(alpha='cheng2018_298K_like')), ('E2_alpha_iso', dict(alpha='isotropic_mean')),
              ('E3_K_iso', dict(K='iso')), ('E4_C_iso', dict(C='iso'))]
E_PHIS = PHIS6
B_DEF = [('B_CV_tau1_a10', 'CV', 1.0, 10), ('B_CV_tau5_a10', 'CV', 5.0, 10), ('B_CV_tau20_a10', 'CV', 20.0, 10),
         ('B_CV_tau20_a5', 'CV', 20.0, 5), ('B_CV_tau20_a20', 'CV', 20.0, 20), ('B_CV_tau20_a50', 'CV', 20.0, 50),
         ('B_F_tau0_a5', 'FOURIER', 0.0, 5), ('B_F_tau0_a20', 'FOURIER', 0.0, 20), ('B_F_tau0_a50', 'FOURIER', 0.0, 50),
         ('B_MCV3_tau5_a10', 'MCV3', 5.0, 10), ('B_MCV3_tau20_a10', 'MCV3', 20.0, 10)]
F_TW = (0.3, 0.6, 2.4)
BM_DEF = [('BM_CV_tau5_a10', 'CV', 5.0, 10), ('BM_CV_tau20_a20', 'CV', 20.0, 20), ('BM_F_tau0_a20', 'FOURIER', 0.0, 20)]


def tau_for_lambda(lam, a):
    return lam * a * a / cp.KAPPA * 1e12          # ps


def matrix():
    J = []
    def add(tag, block, model, tau_ps, chi, phi, a=A0, g='T48', **kw):
        Nr, Nt = GRIDS[g]
        J.append(dict(tag=tag, block=block, model=model, tau_ps=float(tau_ps), chi=float(chi), phi=float(phi), a=float(a),
                      Nr=Nr, Nt=Nt, grid=g, cost=COST[g], **kw))
    # ---- A -----------------------------------------------------------------------------------------------------
    for phi in PHIS:
        add(f'A_chi2_phi{phi:03d}_M', 'A', 'FOURIER', 0.0, 2, phi, g='M')
        add(f'A_chi2_phi{phi:03d}_R48', 'A', 'FOURIER', 0.0, 2, phi, g='R48')
        add(f'A_chi2_phi{phi:03d}_T48', 'A', 'FOURIER', 0.0, 2, phi, g='T48')
        add(f'A_chi1_phi{phi:03d}_R48', 'A', 'FOURIER', 0.0, 1, phi, g='R48')
    for phi in PHIS6:
        add(f'A_chi2_phi{phi:03d}_R192', 'A', 'FOURIER', 0.0, 2, phi, g='R192')
    for phi in PHIS6:
        add(f'A_chi2_phi{phi:03d}_T144', 'A', 'FOURIER', 0.0, 2, phi, g='T144')
    for phi in (0, 15, 45, 75, 105, 135):
        add(f'A_chi1_phi{phi:03d}_M', 'A', 'FOURIER', 0.0, 1, phi, g='M')
    add('A_chi1_phi000_T48', 'A', 'FOURIER', 0.0, 1, 0, g='T48')
    add('A_chi1_phi000_R192', 'A', 'FOURIER', 0.0, 1, 0, g='R192')
    # ---- B (dynamic) and BQS (quasi-static ablation), grid T48 ------------------------------------------------------
    for tag, model, tau, a_nm in B_DEF:
        add(tag, 'B', model, tau, 1, 0, a=a_nm * 1e-9)
    for tag, model, tau, a_nm in B_DEF + [('B_F_tau0_a10', 'FOURIER', 0.0, 10)]:
        add(tag + '_QS', 'BQS', model, tau, 1, 0, a=a_nm * 1e-9, inertia_scale=0.0)
    for tag, model, tau, a_nm in BM_DEF:
        add(tag, 'BM', model, tau, 1, 0, a=a_nm * 1e-9, g='M')
    # ---- B2 / B2QS extended map (exploratory), grid T48 --------------------------------------------------------------
    for a_nm in (5, 10, 20):
        for lam in LAMBDAS_B2:
            add(f'B2_CV_L{lam:g}_a{a_nm}', 'B2', 'CV', tau_for_lambda(lam, a_nm * 1e-9), 1, 0, a=a_nm * 1e-9)
    add('B2_F_a5', 'B2', 'FOURIER', 0.0, 1, 0, a=5e-9)
    add('B2_F_a20', 'B2', 'FOURIER', 0.0, 1, 0, a=20e-9)
    for lam in LAMBDAS_B2:
        add(f'B2QS_CV_L{lam:g}_a10', 'B2QS', 'CV', tau_for_lambda(lam, A0), 1, 0, inertia_scale=0.0)
    # ---- C ----------------------------------------------------------------------------------------------------------
    add('C_CV_tau20_a10_coupling_off', 'C', 'CV', 20.0, 1, 0, energy_coupling=False)
    # ---- D ----------------------------------------------------------------------------------------------------------
    add('D_iso_circle_T48', 'D', 'FOURIER', 0.0, 1, 0, iso=True)
    for g in ('R48', 'M', 'R192'):
        add(f'D_iso_ellipse_{g}', 'D', 'FOURIER', 0.0, 2, 0, g=g, iso=True)
    # ---- E ----------------------------------------------------------------------------------------------------------
    for name, var in E_VARIANTS:
        for phi in E_PHIS:
            add(f'{name}_phi{phi:03d}', 'E', 'FOURIER', 0.0, 2, phi, g='T48', variant=var)
    # ---- F (exploratory; added after the gate, before any F result existed): locality test = pulse-width dependence, grid T48 -----------------
    for tw in F_TW:
        add(f'F_tw{tw:g}_circ', 'F', 'FOURIER', 0.0, 1, 0, g='T48', pulse=(2.5, tw))
        for phi in (90, 150):
            add(f'F_tw{tw:g}_ell_phi{phi:03d}', 'F', 'FOURIER', 0.0, 2, phi, g='T48', pulse=(2.5, tw))
    return J


if __name__ == '__main__':
    import collections
    J = matrix()
    print(len(J), 'jobs;', dict(collections.Counter(j['block'] for j in J)))
    print('by cost class:', dict(collections.Counter(j['cost'] for j in J)))
    est = {'light': 10.0, 'medium': 55.0, 'heavy': 135.0}
    print('estimated CPU minutes:', round(sum(est[j['cost']] for j in J) / 60, 1))
