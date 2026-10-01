"""cg_pipeline.py — configuration -> complex-frequency transfer values -> single-pulse series -> QoIs.
Shared by production, convergence and test scripts (Phase 7+, 2026-10-01).  Uses the UNCHANGED frequency-domain
operator (cg_solver.HarmonicSolver, real Q: no hysteretic damping) at complex w = -i s/t_th (see cg_bromwich.py).
"""
import json, os, time
from pathlib import Path
import numpy as np
from cg_grid import Grid
from cg_model import (plane_strain_block, iso_control, K_ac, rotate_Q_beta, rotate2,
                      rho, cp_ESTIMATED, T0, derived, GPa, Cij_GPa, alpha_crys)
from cg_solver import HarmonicSolver
from cg_bromwich import BromwichPlan

A0 = 1e-8                       # 10 nm reference cavity radius
DV = derived()
KAPPA = DV['kappa']             # kbar/(rho cp), kbar = sqrt(det K_ac)
C_REF = DV['c_ref']
Q0, BETA0 = plane_strain_block()
KISO, QISO, BISO = iso_control()
T_QOI = 6.0                     # pre-registered QoI window end (t_th)
PULSE_T0, PULSE_TW = 2.5, 1.2   # pre-registered pulse (t_th)
PHIS = list(range(0, 180, 15))
PLAN_DEFAULT = dict(T=20.0, gamma=0.9)
GAMMA_DEFAULT = 5.0             # radial clustering of the mapped grid (handoff: 3.5; changed 2026-10-01, P9-D001: near-wall resolution controls the ellipse-tip stress)
T_STORE = np.arange(0.0, 12.0 + 1e-9, 0.05)       # stored time grid (t_th)
T_FINE = np.arange(0.0, T_QOI + 1e-9, 0.01)       # QoI search grid


def delta_feedback():
    """Thermoelastic coupling number  delta = T0 beta.beta / (rho cp Cbar)  (computed, not hard-coded)."""
    return float(DV['delta'])


# ---- material variants (ablations / parameter sensitivity; Phase 10-11, added 2026-10-01) -----------------------------
# Built with the independent 3-D rank-4 rotation route (verified equal to rotate_Q_beta to 1.6e-16 by test U1).
_VM = {0: (0, 0), 1: (1, 1), 2: (2, 2), 3: (1, 2), 4: (0, 2), 5: (0, 1)}
def _voigt_to_tensor(C6):
    T = np.zeros((3, 3, 3, 3))
    for I, (i, j) in _VM.items():
        for J, (k, l) in _VM.items():
            for (a_, b_) in {(i, j), (j, i)}:
                for (c_, d_) in {(k, l), (l, k)}:
                    T[a_, b_, c_, d_] = C6[I, J]
    return T
def _tensor_to_voigt(T):
    out = np.zeros((6, 6))
    for I, (i, j) in _VM.items():
        for J, (k, l) in _VM.items():
            out[I, J] = T[i, j, k, l]
    return out
def _C6_mono():
    C = Cij_GPa; C6 = np.zeros((6, 6))
    for (i, j, key) in [(0, 0, 'C11'), (1, 1, 'C22'), (2, 2, 'C33'), (3, 3, 'C44'), (4, 4, 'C55'), (5, 5, 'C66'), (0, 1, 'C12'),
                        (0, 2, 'C13'), (1, 2, 'C23'), (0, 4, 'C15'), (1, 4, 'C25'), (2, 4, 'C35'), (3, 5, 'C46')]:
        C6[i, j] = C6[j, i] = C[key] * GPa
    return C6
def _C6_iso():
    lam, mu = Cij_GPa['C12'] * GPa, Cij_GPa['C66'] * GPa          # same constants as iso_control()
    C6 = np.zeros((6, 6))
    for i in range(3):
        for j in range(3):
            C6[i, j] = lam
        C6[i, i] = lam + 2 * mu; C6[i + 3, i + 3] = mu
    return C6
ALPHA_SETS = {
    'baseline_orlandi2015': (1.54e-6, 3.37e-6, 3.15e-6),         # PARAMETER_TABLE (secondary-quoted values of Orlandi et al. 2015)
    'cheng2018_298K_like': (0.10e-6, 0.20e-6, 0.20e-6),          # SENSITIVITY-ONLY: abstract-level statement (alpha_a ~0.10e-6 at 298 K, alpha_b,c ~ 2 alpha_a)
    'isotropic_mean': (float(np.mean((1.54e-6, 3.37e-6, 3.15e-6))),) * 3,
}
def material_variant(phi_deg, variant, coupled=True):
    """variant: dict(alpha=(a1,a2,a3) | key of ALPHA_SETS, C='mono'|'iso', K='aniso'|'iso')."""
    al = variant.get('alpha', 'baseline_orlandi2015')
    al = np.array(ALPHA_SETS[al] if isinstance(al, str) else al, float)
    C6 = _C6_iso() if variant.get('C', 'mono') == 'iso' else _C6_mono()
    phi = np.radians(phi_deg); c, s_ = np.cos(phi), np.sin(phi)
    R3 = np.array([[c, 0, -s_], [0, 1, 0], [s_, 0, c]])
    Tr = np.einsum('ai,bj,ck,dl,ijkl->abcd', R3, R3, R3, R3, _voigt_to_tensor(C6))
    A = R3 @ np.diag(al) @ R3.T
    al_v = np.array([A[0, 0], A[1, 1], A[2, 2], 0.0, 2 * A[0, 2], 0.0])
    C6r = _tensor_to_voigt(Tr)
    Q = C6r[np.ix_([0, 2, 4], [0, 2, 4])]; b = (C6r @ al_v)[[0, 2, 4]]
    K2 = KISO if variant.get('K', 'aniso') == 'iso' else rotate2(K_ac, phi)
    if not coupled:
        b = np.zeros(3)
    return K2, Q, b


def material(phi_deg, iso=False, coupled=True, variant=None):
    if variant:
        return material_variant(phi_deg, variant, coupled)
    phi = np.radians(phi_deg)
    if iso:
        K2, Q, b = KISO, QISO, BISO
        if phi_deg:
            K2 = rotate2(KISO, phi); Q, b = rotate_Q_beta(QISO, BISO, phi)
    else:
        K2 = rotate2(K_ac, phi) if phi_deg else K_ac
        Q, b = rotate_Q_beta(Q0, BETA0, phi) if phi_deg else (Q0, BETA0)
    if not coupled:
        b = np.zeros(3)
    return K2, Q, b


def build(chi, phi_deg, a, model, tau_ps, iso=False, coupled=True, energy_coupling=True,
          inertia_scale=1.0, Nr=96, Nt=48, Rfac=80.0, gamma_grid=GAMMA_DEFAULT, variant=None):
    K2, Q, b = material(phi_deg, iso, coupled, variant)
    g = Grid(chi=chi, a=a, R=Rfac * a, Nr=Nr, Nt=Nt, gamma=gamma_grid)
    s = HarmonicSolver(g, K2, np.asarray(Q, complex), b, rho, cp_ESTIMATED, T0, model=model,
                       tau=tau_ps * 1e-12, energy_coupling=energy_coupling, inertia_scale=inertia_scale)
    return g, s


def transfer_set(g, s, plan, t_th, probe_fracs=(1.5, 2.0, 3.0), a=None):
    """Solve the harmonic problem at the plan's complex frequencies. Returns dict of H arrays (K+1, ...)."""
    a = a if a is not None else g.a
    n = plan.n_solves
    probe_i = [int(np.argmin(np.abs(g.r - f * a))) for f in probe_fracs]
    H_hoop = np.zeros((n, g.Nt), complex)
    H_wall = np.zeros((n, g.Nt), complex)
    H_probe = np.zeros((n, len(probe_i)), complex)
    backs = np.zeros(n)
    wk = plan.w_phys(t_th)
    for ik in range(n):
        U, back = s.solve(wk[ik])
        hoop, _, _ = s.stress_wall(U)
        H_hoop[ik] = hoop
        H_wall[ik] = s.wall_theta(U)
        th = U[:s.n].reshape(g.Nr, g.Nt)
        H_probe[ik] = th[probe_i, 0]
        backs[ik] = back
    return dict(H_hoop=H_hoop, H_wall=H_wall, H_probe=H_probe, back=backs, probe_i=probe_i,
                probe_r_over_a=[float(g.r[i] / a) for i in probe_i])


def angular_upsample(f, factor=16, axis=0):
    """Spectral (trigonometric) interpolation of periodic samples (angle axis `axis`) onto factor*Nt points."""
    Nt = f.shape[axis]
    F = np.fft.rfft(f, axis=axis)
    M = Nt * factor
    return np.fft.irfft(F * factor, n=M, axis=axis)


def qoi_from_series(t, hoop, t_qoi=T_QOI):
    """hoop: (Nt_angles, nt). Returns pre-registered nodal QoI and the angularly-interpolated QoI."""
    nt = int(np.searchsorted(t, t_qoi + 1e-12, side='right'))
    hw = hoop[:, :nt]
    j, k = np.unravel_index(np.argmax(np.abs(hw)), hw.shape)
    up = angular_upsample(hw, 16, axis=0)              # (16*Nt, nt)
    ju, ku = np.unravel_index(np.argmax(np.abs(up)), up.shape)
    modes = np.abs(np.fft.fft(hoop[:, k])) / hoop.shape[0]
    return dict(sig_nodal=float(hw[j, k]), th_star_nodal_deg=float(j * 360.0 / hoop.shape[0]),
                t_star=float(t[k]),
                sig_interp=float(up[ju, ku]), th_star_interp_deg=float(ju * 360.0 / up.shape[0]),
                t_star_interp=float(t[ku]),
                sig_abs_max=float(np.abs(hw).max()),
                ang_modes=[float(m) for m in modes[:9]],
                profile_at_peak=[float(v) for v in hoop[:, k]])


def run_config(tag, model, tau_ps, chi, phi_deg, a, outdir=None, plan_kw=None, iso=False, coupled=True,
               energy_coupling=True, inertia_scale=1.0, Nr=96, Nt=48, Rfac=80.0, save=True, quiet=False, variant=None,
               gamma_grid=GAMMA_DEFAULT, pulse=None):
    t_wall0 = time.time()
    t0_p, tw_p = pulse if pulse else (PULSE_T0, PULSE_TW)       # `pulse` added 2026-10-01 for block F (default: pre-registered pulse)
    plan = BromwichPlan(t0=t0_p, tw=tw_p, **(plan_kw or PLAN_DEFAULT))
    t_th = a * a / KAPPA
    g, s = build(chi, phi_deg, a, model, tau_ps, iso, coupled, energy_coupling, inertia_scale, Nr, Nt, Rfac, gamma_grid=gamma_grid, variant=variant)
    tr = transfer_set(g, s, plan, t_th, a=a)
    hoop_f = plan.synth(tr['H_hoop'], T_FINE)
    wall_f = plan.synth(tr['H_wall'], T_FINE)
    q = qoi_from_series(T_FINE, hoop_f)
    hoop_s = plan.synth(tr['H_hoop'], T_STORE)
    wall_s = plan.synth(tr['H_wall'], T_STORE)
    probe_s = plan.synth(tr['H_probe'], T_STORE)
    wall_err = float(np.abs(wall_s - plan.pulse(T_STORE)[None, :]).max())
    Lam = tau_ps * 1e-12 * KAPPA / a ** 2
    eps = KAPPA / (C_REF * a)
    q.update(tag=tag, model=model, tau_ps=tau_ps, chi=chi, phi=phi_deg, a_nm=a * 1e9, iso=iso, coupled=coupled,
             energy_coupling=energy_coupling, inertia_scale=inertia_scale, Nr=Nr, Nt=Nt, Rfac=Rfac, gamma_grid=gamma_grid, variant=variant,
             pulse_t0_tw=[t0_p, tw_p], Lambda=Lam, epsilon=eps, t_th_s=t_th, plan=plan.describe(), n_solves=plan.n_solves,
             back_max=float(tr['back'].max()), wall_pulse_err=wall_err,
             probe_r_over_a=tr['probe_r_over_a'], wall_s=time.time() - t_wall0)
    if save and outdir is not None:
        outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(outdir / f'{tag}.npz', t=T_STORE, hoop=hoop_s, wall=wall_s, probe=probe_s,
                            H_hoop=tr['H_hoop'], H_wall=tr['H_wall'], H_probe=tr['H_probe'],
                            s=plan.s, r=g.r)
        (outdir / f'{tag}.json').write_text(json.dumps(q, indent=1, default=str))
    if not quiet:
        print(f"[{tag}] sig_nodal={q['sig_nodal']:.6e} sig_interp={q['sig_interp']:.6e} t*={q['t_star']:.3f} "
              f"th*={q['th_star_interp_deg']:.1f} wall_err={wall_err:.1e} back={q['back_max']:.1e} ({q['wall_s']:.0f}s)",
              flush=True)
    q['_series'] = dict(t=T_STORE, hoop=hoop_s, wall=wall_s, probe=probe_s)
    q['_H'] = tr
    return q
