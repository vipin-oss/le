"""make_figures.py — figures for the manuscript (matplotlib, data-driven; no generative-AI imagery).
Reads 09_Raw_Data/production, 09_Raw_Data/convergence, 10_Processed_Data/ANALYSIS_V2.json, 07_Tests/TEST_RESULTS.json.
Usage: python make_figures.py [fig1 fig2 ...]  (default: all that have data)
"""
import sys, os, json, ast
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyArrowPatch
import production_matrix as pm
import cg_pipeline as cp

PROD = os.path.join(ROOT, '09_Raw_Data', 'production'); CONV = os.path.join(ROOT, '09_Raw_Data', 'convergence')
FIG = os.path.join(ROOT, '11_Figures'); os.makedirs(FIG, exist_ok=True)
SHIPPED = '/home/user/work/handoff/PROJECT_CRYSTAL_GEOMETRY_01/data/PROD'
AN = json.load(open(os.path.join(ROOT, '10_Processed_Data', 'ANALYSIS_V2.json'))) if os.path.exists(os.path.join(ROOT, '10_Processed_Data', 'ANALYSIS_V2.json')) else {}
plt.rcParams.update({'font.size': 9, 'axes.grid': True, 'grid.alpha': 0.25, 'figure.dpi': 140, 'savefig.dpi': 200,
                     'axes.spines.top': False, 'axes.spines.right': False, 'legend.frameon': False})
COL = dict(circle='#1f77b4', ellipse='#d62728', iso='#7f7f7f', cv='#2ca02c', qs='#9467bd', shipped='#bbbbbb')

def load(tag, d=PROD):
    jp = os.path.join(d, tag + '.json')
    if not os.path.exists(jp): return None
    q = json.load(open(jp)); z = np.load(os.path.join(d, tag + '.npz'))
    q.update(t=z['t'], hoop=z['hoop'], wall=z['wall'], probe=z['probe']); return q

def save(fig, name):
    p = os.path.join(FIG, name); fig.savefig(p, bbox_inches='tight'); plt.close(fig); print('wrote', p)

# --------------------------------------------------------------------------------------------- Fig 1: setup
def fig1():
    fig, ax = plt.subplots(1, 3, figsize=(10.4, 3.2), gridspec_kw=dict(width_ratios=[1, 1, 1.2], wspace=0.28))
    for k, (title, chi) in enumerate((('(a) circular cavity', 1.0), ('(b) equal-area ellipse, $\\chi=2$', 2.0))):
        a_ = ax[k]; a_.set_aspect('equal'); a_.axis('off'); a_.set_xlim(-2.3, 2.5); a_.set_ylim(-2.6, 1.9)
        a_.add_patch(Ellipse((0, 0), 2 * np.sqrt(chi), 2 / np.sqrt(chi), angle=0, fc='#f4d6c8', ec='k', lw=1.4))
        a_.annotate('', xy=(2.05, 0), xytext=(-2.05, 0), arrowprops=dict(arrowstyle='->', color='0.35', lw=0.9))
        a_.annotate('', xy=(0, 1.55), xytext=(0, -1.55), arrowprops=dict(arrowstyle='->', color='0.35', lw=0.9))
        a_.text(1.55, -0.32, 'a', fontsize=8, color='0.35'); a_.text(0.1, 1.5, 'c', fontsize=8, color='0.35')
        ph = np.radians(35)
        a_.annotate('', xy=(1.75 * np.cos(ph), 1.75 * np.sin(ph)), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=COL['circle'], lw=1.4))
        a_.text(1.0, 1.55, 'rotated crystal\n$a$-axis ($\\phi$)', fontsize=7.5, color=COL['circle'], ha='left')
        a_.text(0, -2.25, 'wall: $\\theta=p(t)$, traction-free\nouter boundary $R=80a$: $\\theta=0,\\ u=0$', ha='center', va='center', fontsize=7.5)
        a_.set_title(title, fontsize=9)
    a3 = ax[2]; t = np.linspace(-1, 8, 400); a3.plot(t, np.exp(-((t - 2.5) / 1.2) ** 2), color='k')
    a3.set_xlabel('$t/t_{th}$'); a3.set_ylabel('wall temperature $p(t)$ (per K)'); a3.set_title('(c) wall pulse, quiescent initial state', fontsize=9)
    a3.axvline(6.0, color=COL['ellipse'], ls=':', lw=1); a3.text(6.1, 0.55, 'QoI window\n$t\\leq 6$', fontsize=7.5, color=COL['ellipse'])
    a3.text(5.3, 0.9, '$t_0=2.5,\\ t_w=1.2$', ha='center', fontsize=8)
    save(fig, 'fig1_setup.png')

# --------------------------------------------------------------------------------------------- Fig 2: phi sweep
def fig2():
    T4 = AN.get('T4_H2', {})
    if 'extrapolated_6phi' not in T4: print('fig2: no data'); return
    phis = cp.PHIS
    fig, ax = plt.subplots(1, 2, figsize=(9.8, 3.6))
    a_ = ax[0]
    for g, ls, al, lab in (('R48', ':', 0.6, '48×96'), ('M', '-', 1.0, '96×96 (production)')):
        v = [abs(load(f'A_chi2_phi{p:03d}_{g}')['sig_interp']) / 1e6 for p in phis]
        a_.plot(phis, v, ls, color=COL['ellipse'], alpha=al, marker='o', ms=3, label=f'ellipse {lab}')
    p6 = pm.PHIS6
    a_.plot(p6, [abs(load(f'A_chi2_phi{p:03d}_R192')['sig_interp']) / 1e6 for p in p6], 's', color='#ff7f0e', ms=5, mfc='none', label='ellipse 192×96')
    a_.plot(p6, np.array(T4['extrapolated_6phi']['values']) / 1e6, 'k*', ms=8, label='ellipse, extrapolated')
    cir = AN.get('circle_peak', {}).get('radial_interp', {})
    if cir.get('f'):
        for f_, ls in zip(cir['f'], (':', '-', '--')): a_.axhline(f_ / 1e6, color=COL['circle'], ls=ls, lw=1.0)
        a_.text(3, cir['f'][1] / 1e6 + 0.012, 'circle (all $\\phi$; three radial grids)', color=COL['circle'], fontsize=8)
    a_.set_xlabel('crystal rotation $\\phi$ (deg)'); a_.set_ylabel('peak $|\\sigma_{\\theta\\theta}|$ on the wall (MPa/K)'); a_.legend(fontsize=7, ncol=1, loc='lower right', bbox_to_anchor=(1.0, 0.07))
    a_.set_title('(a) corrected response (single pulse, undamped)', fontsize=9)
    a_ = ax[1]
    sh = AN.get('shipped', {})
    if sh:
        a_.plot(phis, np.array(sh['ellipse']) / 1e6, 'o--', color=COL['shipped'], ms=3, label='earlier analysis, ellipse')
        a_.plot(phis, np.array(sh['circle']) / 1e6, 's--', color=COL['shipped'], ms=3, mfc='none', label='earlier analysis, circle')
    v = [abs(load(f'A_chi2_phi{p:03d}_M')['sig_interp']) / 1e6 for p in phis]; a_.plot(phis, v, 'o-', color=COL['ellipse'], ms=3, label='this work, ellipse (M)')
    pc_ = [0, 15, 45, 75, 105, 135]; vc = [abs(load(f'A_chi1_phi{p:03d}_M')['sig_interp']) / 1e6 for p in pc_]
    a_.plot(pc_, vc, 's-', color=COL['circle'], ms=3, label='this work, circle (M)')
    a_.set_xlabel('crystal rotation $\\phi$ (deg)'); a_.set_ylabel('peak $|\\sigma_{\\theta\\theta}|$ (MPa/K)'); a_.legend(fontsize=7, ncol=2, loc='upper center', bbox_to_anchor=(0.5, -0.17))
    a_.set_title('(b) effect of the corrections (periodic synthesis, rotation bug, coarse wall mesh)', fontsize=8.5)
    save(fig, 'fig2_phi_sweep.png')

# --------------------------------------------------------------------------------------------- Fig 3: wall profiles
def fig3():
    qs = [('circle, $\\phi=0$', 'A_chi1_phi000_R192', COL['circle'])] + [(f'ellipse, $\\phi={p}^\\circ$', f'A_chi2_phi{p:03d}_R192', c) for p, c in ((30, '#ff7f0e'), (90, '#2ca02c'), (150, COL['ellipse']))]
    if not all(load(t) for _, t, _ in qs): print('fig3: missing data'); return
    fig, ax = plt.subplots(1, 2, figsize=(9.8, 3.5))
    for lab, tag, c in qs:
        q = load(tag); k = int(np.argmin(np.abs(q['t'] - q['t_star'])))
        up = cp.angular_upsample(q['hoop'][:, k], 16, axis=0) / 1e6; etau = np.arange(up.size) * 360.0 / up.size
        ax[0].plot(etau, -up, color=c, label=lab)
    ax[0].set_xlabel('wall parameter angle $\\eta$ (deg)'); ax[0].set_ylabel('compressive hoop stress $-\\sigma_{\\theta\\theta}$ at peak time (MPa/K)')
    ax[0].legend(fontsize=7.5); ax[0].set_xlim(0, 360); ax[0].set_title('(a) wall distribution at the peak (192×96)', fontsize=9)
    q = load('A_chi2_phi150_R192'); k0 = int(np.argmin(np.abs(q['t'] - q['t_star']))); i0 = int(np.argmax(np.abs(q['hoop'][:, k0])))
    p_ = np.exp(-((q['t'] - 2.5) / 1.2) ** 2)
    ax[1].plot(q['t'], q['hoop'][i0] / 1e6, color=COL['ellipse'], label='$\\sigma_{\\theta\\theta}$ at the peak node (ellipse, $\\phi=150^\\circ$)')
    ax[1].plot(q['t'], -p_ * abs(q['hoop'][i0]).max() / 1e6, 'k--', lw=1, label='$-p(t)\\times$ peak (local response)')
    ax[1].set_xlim(0, 8); ax[1].set_xlabel('$t/t_{th}$'); ax[1].set_ylabel('MPa/K'); ax[1].legend(fontsize=7.2, loc='lower left')
    ax[1].set_title('(b) stress follows the wall temperature near the peak', fontsize=9)
    save(fig, 'fig3_wall_profiles.png')

# --------------------------------------------------------------------------------------------- Fig 4: verification
def fig4():
    tr = json.load(open(os.path.join(ROOT, '07_Tests', 'TEST_RESULTS.json'))); cs = {c['case']: c for c in tr['cases']}
    fig, ax = plt.subplots(1, 3, figsize=(11.4, 3.5), gridspec_kw=dict(wspace=0.42))
    a_ = ax[0]; sh = AN.get('shipped', {})
    c48 = [abs(load(f'A_chi1_phi{p:03d}_R48')['sig_nodal']) for p in cp.PHIS] if load('A_chi1_phi000_R48') else None
    if sh and c48:
        s = np.array(sh['circle']); a_.semilogy(cp.PHIS, np.abs(s / s.mean() - 1) + 1e-16, 'o--', color=COL['shipped'], label='earlier analysis (rotation bug)')
        c = np.array(c48); a_.semilogy(cp.PHIS, np.abs(c / c.mean() - 1) + 1e-16, 's-', color=COL['circle'], label='this work (48×96)')
        a_.axhline(1e-8, color='k', ls=':', lw=1); a_.text(5, 1.6e-8, 'frozen criterion $10^{-8}$', fontsize=7.5)
        a_.set_xlabel('$\\phi$ (deg)'); a_.set_ylabel('$|\\hat\\sigma(\\phi)/\\bar\\sigma-1|$ (circle)'); a_.legend(fontsize=7, loc='center', bbox_to_anchor=(0.55, 0.36)); a_.set_ylim(1e-17, 1e-1)
    a_.set_title('(a) rotation invariance of the circle', fontsize=8.5)
    a_ = ax[1]; h = np.array([1 / 24, 1 / 48, 1 / 96.])
    def parse(s): return [abs(float(x)) for x in ast.literal_eval(s)] if isinstance(s, str) else None
    if 'V8_steady_thermal_gradient_load' in cs: a_.loglog(h, parse(cs['V8_steady_thermal_gradient_load']['rel_err_48_96_192_384'])[:3], 'o-', label='V8 steady gradient load')
    if 'V11_single_pulse_isotropic_circle_vs_time_domain' in cs: a_.loglog(h, parse(cs['V11_single_pulse_isotropic_circle_vs_time_domain']['peak_rel_err_48_96_192']), 's-', label='V11 single pulse vs time-domain')
    if 'V9d_time_domain_peak_and_series_vs_1D' in cs:
        pe = ast.literal_eval(cs['V9d_time_domain_peak_and_series_vs_1D']['peak_errs'])['CV20']; a_.loglog(h, [abs(float(x)) for x in pe], '^-', label='V9d dynamic coupled, CV (τ=20 ps)')
    if 'V7_static_uniform_theta_annulus' in cs: a_.loglog(h, parse(cs['V7_static_uniform_theta_annulus']['rel_err_48_96_192']), 'v-', label='V7 uniform-θ annulus')
    a_.loglog(h, 0.6 * (h / h[0]) ** 2 * 0.02, 'k:', lw=1, label='slope 2'); a_.set_xlabel('mesh size $h\\propto1/N_\\theta$ (axisymmetric tests)'); a_.set_ylabel('relative error'); a_.legend(fontsize=6.6)
    a_.set_title('(b) verification vs exact/independent solutions', fontsize=8.5)
    a_ = ax[2]; t = np.arange(0, 12.01, 0.05); a_.plot(t, cp.BromwichPlan().pulse(t), 'k', lw=1.2, label='exact pulse'); q = load('A_chi1_phi000_M')
    if q: a_.plot(q['t'], q['wall'][0], 'r--', lw=1, label='wall θ from Bromwich inversion')
    a_.set_xlabel('$t/t_{th}$'); a_.set_ylabel('wall temperature (per K)'); a_.legend(fontsize=7.5)
    a_.set_title(f"(c) inversion check (max error {AN.get('numerics', {}).get('max_wall_pulse_error', float('nan')):.0e}, t<=6)", fontsize=8.5)
    save(fig, 'fig4_verification.png')

# --------------------------------------------------------------------------------------------- Fig 5: D(Lambda)
def fig5():
    if 'T2_H3' not in AN: print('fig5: no data'); return
    T2 = AN['T2_H3']
    fig, ax = plt.subplots(1, 2, figsize=(9.8, 3.6)); a_ = ax[0]; mk = {5: 'v', 10: 'o', 20: 's', 50: 'D'}
    for r in T2['dynamic']:
        if r['model'] == 'CV': a_.loglog(r['Lambda'], r['D'], mk.get(int(r['a_nm']), 'o'), color=COL['cv'], ms=6)
    for r in T2['extended_dynamic']: a_.loglog(r['Lambda'], r['D'], mk.get(int(r['a_nm']), 'o'), color=COL['cv'], alpha=0.4, ms=5)
    for r in T2['quasi_static'] + T2['extended_QS']:
        if r['model'] == 'CV': a_.loglog(r['Lambda'], r['D'], 'x', color=COL['qs'], ms=7)
    a_.plot([], [], 'x', color=COL['qs'], label='quasi-static (inertia off)')
    for a_nm, m in mk.items(): a_.plot([], [], m, color=COL['cv'], label=f'dynamic, a={a_nm} nm')
    a_.set_xlabel('$\\Lambda=\\tau\\bar\\kappa/a^2$'); a_.set_ylabel('$D=\\max|\\sigma_{CV}-\\sigma_F|/\\max|\\sigma_F|$  ($t\\leq 6$)')
    a_.legend(fontsize=7, ncol=2); a_.set_title('(a) thermal-memory deviation of the wall hoop stress', fontsize=9)
    a_ = ax[1]; qf = load('A_chi1_phi000_T48'); qc = load('B_CV_tau20_a10')
    if qf and qc:
        t = qf['t']; n = t <= 8; i = int(np.argmax(np.abs(qf['hoop'][:, int(np.argmin(np.abs(t - 2.5)))])))
        a_.plot(t[n], qf['hoop'][i][n] / 1e6, color='k', label='Fourier'); a_.plot(t[n], qc['hoop'][i][n] / 1e6, color=COL['cv'], ls='--', label='CV, $\\tau=20$ ps ($\\Lambda=0.79$)')
        ax2 = a_.twinx(); ax2.plot(t[n], 100 * (qc['hoop'][i][n] - qf['hoop'][i][n]) / abs(qf['hoop'][i]).max(), color=COL['ellipse'], lw=1)
        ax2.set_ylabel('difference (% of peak)', color=COL['ellipse']); ax2.grid(False); ax2.spines['right'].set_visible(True)
        a_.set_xlabel('$t/t_{th}$'); a_.set_ylabel('wall hoop stress (MPa/K)'); a_.legend(fontsize=7.5, loc='lower right')
    a_.set_title('(b) Fourier vs CV at the peak node (circle, 10 nm)', fontsize=9)
    save(fig, 'fig5_memory.png')

# --------------------------------------------------------------------------------------------- Fig 6: mesh study (a) + ablations (b)
def fig6():
    E = AN.get('E_ablations'); cdir = os.path.join(ROOT, '10_Processed_Data', 'CONVERGENCE_DIRS.json')
    if os.path.exists(cdir):
        fig, a_ = plt.subplots(1, 1, figsize=(5.0, 3.5))
        C = json.load(open(cdir)); order = [('96x48_gam3.5', 3.5, 'o'), ('192x48_gam3.5', 3.5, 's'), ('96x96_gam3.5', 3.5, '^'), ('96x144_gam3.5', 3.5, 'v'), ('192x96_gam3.5', 3.5, 'D'),
                                           ('96x48_gam5', 5.0, 'o'), ('96x96_gam5', 5.0, '^'), ('144x72_gam5', 5.0, 'P'), ('96x48_gam6.5', 6.5, 'o')]
        cols = {3.5: '#d62728', 5.0: '#1f77b4', 6.5: '#2ca02c'}
        for k, gm, m in order:
            off = {'144x72_gam5': 0.006, '96x48_gam5': -0.005, '96x144_gam3.5': 0.004, '96x96_gam3.5': -0.004}.get(k, 0.0)
            if k in C: a_.plot(gm, abs(C[k]['sig_interp']) / 1e6, m, color=cols[gm], ms=6); a_.text(gm + 0.08, abs(C[k]['sig_interp']) / 1e6 + off, k.split('_')[0], fontsize=6.5, va='center')
        a_.set_xlabel('radial clustering $\\gamma$'); a_.set_ylabel('peak $|\\sigma_{\\theta\\theta}|$ (MPa/K), ellipse $\\phi=30^\\circ$'); a_.set_xlim(3.2, 7.4)
        a_.set_title('near-wall clustering controls the tip stress', fontsize=9)
        save(fig, 'fig6a_mesh.png')
    if E:
        fig, a_ = plt.subplots(1, 1, figsize=(5.0, 3.5))
        names = [('baseline_6phi', 'full\nanisotropy'), ('E3_K_iso', 'isotropic\nconductivity'), ('E4_C_iso', 'isotropic\nstiffness'), ('E2_alpha_iso', 'isotropic\nexpansion'), ('E1_alpha_cheng298', 'expansion set\n(298 K-like)')]
        vals = [E[k]['amplitude'] * 100 for k, _ in names if k in E]; labs = [l for k, l in names if k in E]
        a_.bar(range(len(vals)), vals, color=['k', '#8c564b', '#e377c2', '#17becf', '#bcbd22'][:len(vals)])
        a_.set_xticks(range(len(vals))); a_.set_xticklabels(labs, fontsize=7.5); a_.set_ylabel('orientation modulation of the ellipse peak (%)')
        for i, v in enumerate(vals): a_.text(i, v + 0.5, f'{v:.1f}', ha='center', fontsize=8)
        a_.set_title('which anisotropy drives the modulation (96×48)', fontsize=9)
        save(fig, 'fig6b_ablation.png')

# --------------------------------------------------------------------------------------------- Fig 7: pulse-width (locality) test
def fig7():
    F = AN.get('F_locality', {}).get('rows')
    if not F: print('fig7: no data'); return
    fig, ax = plt.subplots(1, 2, figsize=(9.2, 3.3)); tw = [r['tw'] for r in F]
    ax[0].semilogx(tw, [r['circle'] / 1e6 for r in F], 's-', color=COL['circle'], label='circle (all $\\phi$)')
    ax[0].semilogx(tw, [r['ell_phi90'] / 1e6 for r in F], 'o-', color='#2ca02c', label='ellipse $\\phi=90^\\circ$ (baseline minimum)')
    ax[0].semilogx(tw, [r['ell_phi150'] / 1e6 for r in F], 'o-', color=COL['ellipse'], label='ellipse $\\phi=150^\\circ$ (baseline maximum)')
    ax[0].set_xlabel('pulse width $t_w/t_{th}$'); ax[0].set_ylabel('peak wall stress (MPa/K, 96×48)'); ax[0].legend(fontsize=7.2); ax[0].set_title('(a) peak stress versus pulse width', fontsize=9)
    for a_ in ax: a_.set_xticks(tw); a_.set_xticklabels([f'{x:g}' for x in tw]); a_.minorticks_off()
    ax[1].semilogx(tw, [100 * r['A2'] for r in F], 'o-', color='k'); ax[1].set_xlabel('pulse width $t_w/t_{th}$'); ax[1].set_ylabel('two-point orientation modulation $A_2$ (%)')
    ax[1].set_title('(b) modulation vs thermal-layer thickness', fontsize=9); ax[1].set_ylim(bottom=0)
    save(fig, 'fig7_pulse_width.png')

if __name__ == '__main__':
    which = sys.argv[1:] or ['fig1', 'fig2', 'fig3', 'fig4', 'fig5', 'fig6', 'fig7']
    for w in which:
        try:
            globals()[w]()
        except Exception as e:
            print(f'{w}: FAILED {type(e).__name__}: {e}')
