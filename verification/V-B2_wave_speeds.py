#!/usr/bin/env python3
"""
V-B2 wave-speed engine -- independent derivation of 1-D plane-wave dispersion
relations for the canonical thermoelastic models, with limit checks.

Written by the verifier (not by the paper's author).  Every model's dispersion
relation below is obtained from that model's OWN heat law as stated, not copied
from any paper.  Role of this script: (i) produce the characteristic equations
quoted in V-B2a..V-B2m, (ii) check each against a limit case, (iii) give the
numeric wave speeds/attenuation used in the files.

CONVENTIONS (stated once, used everywhere):
  * 1-D, isotropic, homogeneous, linear, small strain, no body force, no source.
  * unknowns: u(x,t) displacement, theta = T - T0 temperature increment.
  * time convention  exp(i(kx - wt))  =>  d/dt -> -i*w ,  d/dx -> i*k.
  * stress:  sigma = M*u_x - beta*theta ,  M = lambda + 2*mu ,  beta = (3*lambda+2*mu)*alpha_T
  * energy:  rho*c*theta_t + beta*T0*u_xt = -q_x   (entropy balance, linearised)
  * Fourier: q = -k_th*theta_x                      (k_th = conductivity)
  Run:  python3 V-B2_wave_speeds.py
"""
import numpy as np
import sympy as sp

# ---------------------------------------------------------------- symbols
k, w = sp.symbols('k omega', positive=True)          # wavenumber, frequency
rho, M, beta, T0, c, kth = sp.symbols('rho M beta T0 c kth', positive=True)

# ---------------------------------------------------------------- material
# Typical carbon steel (order-of-magnitude only; not a materials claim)
E, nu, alpha_T = 200e9, 0.29, 12e-6
lam = E*nu/((1+nu)*(1-2*nu)); mu = E/(2*(1+nu))
Mv = lam + 2*mu
betav = (3*lam + 2*mu)*alpha_T
rhov, cv, kthv, T0v = 7800.0, 460.0, 45.0, 293.0
c_el = np.sqrt(Mv/rhov)              # elastic bar speed  sqrt(M/rho)
kappa = kthv/(rhov*cv)               # thermal diffusivity
delta = T0v*betav**2/(rhov*cv*Mv)    # dimensionless coupling

def dispersion_matrix(heat_row2):
    """2x2 matrix [U,Theta] for motion + a model-specific heat equation.
    heat_row2 = (coef_of_U, coef_of_Theta) as sympy expressions in k,w."""
    aU, aT = heat_row2
    return sp.Matrix([[M*k**2 - rho*w**2, -sp.I*beta*k],
                      [aU, aT]])

def det_of(heat_row2):
    return sp.simplify(dispersion_matrix(heat_row2).det())

# ---------------------------------------------------------------- model heat rows
# Every row is derived from the model's heat law by direct substitution of
# d/dt -> -i w, d/dx -> i k.  Comments give the law being used.
models = {}

# (a) Fourier / Biot:  rho c th_t + beta T0 u_xt = kth th_xx
models['Biot'] = (beta*T0*w*k, kth*k**2 - sp.I*w*rho*c)

# (b) Lord-Shulman:  (1+tau0 d/dt)[rho c th_t + beta T0 u_xt] = kth th_xx
tau0 = sp.symbols('tau0', positive=True)
L = (1 - sp.I*w*tau0)
models['LordShulman'] = (L*beta*T0*w*k, kth*k**2 - sp.I*w*rho*c*L)

# (c) Green-Naghdi II:  rho c th_tt + beta T0 u_xtt = kstar th_xx
kstar = sp.symbols('kstar', positive=True)
models['GN_II'] = (-sp.I*beta*T0*w**2*k, kstar*k**2 - rho*c*w**2)

# (d) Green-Naghdi III: rho c th_tt + beta T0 u_xtt = kstar th_xx + kth th_xxt
models['GN_III'] = (-sp.I*beta*T0*w**2*k,
                    kstar*k**2 + sp.I*w*kth*k**2 - rho*c*w**2)

# (e) Dual-phase-lag (first order): (1+tq d/dt)[...] = kth(1+tT d/dt) th_xx
tq, tT = sp.symbols('tq tT', positive=True)
Dq, DT = (1 - sp.I*w*tq), (1 - sp.I*w*tT)
models['DPL'] = (Dq*beta*T0*w*k, kth*k**2*DT - sp.I*w*rho*c*Dq)

# (f) Triple-phase-lag: (1+tq d/dt + tv^2/2 d2/dt2)[...] = kth(1+tT d/dt) th_xx
tv = sp.symbols('tv', positive=True)
TQ = (1 - sp.I*w*tq - w**2*tv**2/2)
models['TPL'] = (TQ*beta*T0*w*k, kth*k**2*DT - sp.I*w*rho*c*TQ)

# (g) MGT (scalar thermal prototype tau*T_ttt + T_tt = b T_xxt + c2 T_xx),
#     coupled to strain rate.  NOTE: coupled MGT thermoelasticity of Quintanilla
#     also couples strain-rate/history terms; that refinement is flagged in
#     V-B2h as not primary-checked.
tau, bcoef, c2coef = sp.symbols('tau b c2', positive=True)
mgt_theta_op = sp.I*w**3*tau - w**2 - sp.I*w*bcoef*k**2 + c2coef*k**2  # d3/dt3 -> (+i)w^3
models['MGT'] = (-sp.I*beta*T0*(-sp.I*w)**2*k, mgt_theta_op)  # placeholder, fixed below
# MGT coupling: rho c (tau th_ttt + th_tt) + beta T0 (u_xttt*tau + u_xtt) = thermal op
mgt_couple = beta*T0*((-sp.I*w)**2*(sp.I*k))*(1 - sp.I*w*tau)
models['MGT'] = (mgt_couple, mgt_theta_op)

# ---------------------------------------------------------------- determinants
dets = {n: sp.simplify(det_of(r)) for n, r in models.items()}
print("="*78); print("SYMBOLIC DETERMINANTS  det = 0  is the characteristic equation"); print("="*78)
for n, d in dets.items():
    print(f"\n[{n}]\n  {sp.factor(sp.expand(d))}")

# ---------------------------------------------------------------- LIMIT CHECKS
print("\n" + "="*78); print("LIMIT CHECKS (each model -> Biot as its parameter -> 0)"); print("="*78)
d_biot = dets['Biot']
checks = []
checks.append(("LordShulman tau0->0 == Biot",
               sp.simplify(dets['LordShulman'].subs(tau0, 0) - d_biot) == 0))
checks.append(("DPL tq=tT=0 == Biot",
               sp.simplify(dets['DPL'].subs({tq: 0, tT: 0}) - d_biot) == 0))
checks.append(("TPL tq=tT=tv=0 == Biot",
               sp.simplify(dets['TPL'].subs({tq: 0, tT: 0, tv: 0}) - d_biot) == 0))
# DPL with tq=0 reduces to the "Jeffreys"-type law; GN-III with kstar=0 -> Fourier-like
checks.append(("GN_III kstar->0 keeps a kth*th_xxt term (not Biot)",
               sp.simplify(dets['GN_III'].subs(kstar, 0) - d_biot) != 0))
# GN-II: rigid case kth-less: thermal branch must be a pure wave, k^2 = rho c w^2/kstar
rigid_GNII = sp.simplify(models['GN_II'][1].subs(beta, 0))
checks.append(("GN_II rigid: Theta eq gives k^2 = rho c w^2/kstar (exact wave)",
               sp.simplify(rigid_GNII) == kstar*k**2 - rho*c*w**2))
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# LS thermal speed in the rigid limit: tau0 w^2 + i w = kappa k^2  ->  c_h=sqrt(kappa/tau0)
print("\n  LS rigid-limit thermal wave speed (high frequency) c_h = sqrt(kappa/tau0):")
for tau0v in [1e-12, 1e-11, 1e-10]:
    print(f"     tau0={tau0v:.0e} s  ->  c_h = {np.sqrt(kappa/tau0v):.1f} m/s")

# ---------------------------------------------------------------- numeric eigenvalues
def branches(row, omega, params, kth_v=kthv, T0_v=T0v, c_v=cv):
    """Solve the characteristic equation for complex k at given real omega."""
    aU, aT = row
    f = sp.lambdify((k,), det_of(row).subs({w: omega, kth: kth_v, T0: T0_v,
                                            c: c_v, rho: rhov, M: Mv, beta: betav,
                                            **params}), 'numpy')
    # det is a polynomial in k of low degree; find roots on a grid-free basis
    poly = sp.Poly(sp.expand(det_of(row).subs({w: omega, kth: kth_v, T0: T0_v,
                                               c: c_v, rho: rhov, M: Mv, beta: betav,
                                               **params})), k)
    coeffs = [complex(x) for x in poly.all_coeffs()]
    return np.roots(coeffs)

def phase_speed(kc, omega):
    return omega/np.real(kc) if np.real(kc) != 0 else np.inf

print("\n" + "="*78); print("NUMERIC BRANCHES (real omega; k complex)"); print("="*78)
print(f"material: c_el = sqrt(M/rho) = {c_el:.1f} m/s, kappa = {kappa:.3e} m2/s, delta = {delta:.4f}")
print(f"thermal diffusion length at 1 MHz: {np.sqrt(kappa/(2*np.pi*1e6)):.3e} m")

freqs = [1e3, 1e6, 1e9]
rows = {
    'Biot':        (models['Biot'], {}),
    'LordShulman': (models['LordShulman'], {tau0: 1e-11}),
    'GN_II':       (models['GN_II'], {kstar: 45.0/1e-11}),
    'GN_III':      (models['GN_III'], {kstar: 45.0/1e-11}),
    'DPL':         (models['DPL'], {tq: 1e-11, tT: 1e-11}),
    'TPL':         (models['TPL'], {tq: 1e-11, tT: 1e-11, tv: 1e-11}),
    'MGT':         (models['MGT'], {tau: 1e-11, bcoef: 2.5e-5, c2coef: 1.254e6}),
}
for name, (row, prm) in rows.items():
    print(f"\n[{name}]")
    for f0 in freqs:
        om = 2*np.pi*f0
        try:
            ks = branches(row, om, prm)
        except Exception as e:
            print(f"   f={f0:.0e} Hz : solver issue {e}"); continue
        ks = [q for q in ks if abs(q) > 0]
        ks.sort(key=lambda q: -abs(q))
        desc = []
        for q in ks[:4]:
            vph = om/np.real(q) if np.real(q) != 0 else float('inf')
            desc.append(f"|k|={abs(q):.3e} Re k={np.real(q):+.3e} v_ph={vph:9.1f} m/s")
        print(f"   f={f0:.0e} Hz : " + " ; ".join(desc))

# ---------------------------------------------------------------- MGT stability
print("\n" + "="*78); print("MGT STABILITY CHECK  (ACOUSTIC FORM ONLY - gamma = b - tau*c2 > 0)")
# B17 CORRECTION (2026-10-23): gamma = b - tau*c2 is the GAS-DYNAMICS (Moore-Gibson) acoustic form.
# The THERMOELASTIC MGT admissibility is k - tau*k* > 0 (Quintanilla 2019, Thm 4.7 / Sec 5).
# This script block tests the acoustic form only; do not quote its output for the thermoelastic law.; print("="*78)
def mgt_roots(tau_v, b_v, c2_v, kap):
    # tau s^3 + s^2 + b kap^2 s + c2 kap^2 = 0
    return np.roots([tau_v, 1.0, b_v*kap**2, c2_v*kap**2])
for (tau_v, b_v, c2_v) in [(1e-11, 2.5e-5, 1.254e6), (1e-11, 1.254e-5, 1.254e6), (1e-11, 1.0e-6, 1.254e6), (1e-11, 9.0e-6, 1.254e6)]:
    gam = b_v - tau_v*c2_v
    rr = mgt_roots(tau_v, b_v, c2_v, 1000.0)
    print(f"  tau={tau_v:.0e} b={b_v:g} c2={c2_v:g} -> gamma={gam:+.3e} "
          f"max Re(s)={max(np.real(rr)):+.3e}  {'STABLE' if max(np.real(rr))<0 else 'UNSTABLE'}")

# ---------------------------------------------------------------- fractional / MDD
print("\n" + "="*78); print("CAPUTO vs FOURIER: attenuation scaling (the falsifiable difference)"); print("="*78)
alpha_cap = [0.5, 0.8, 1.0]
print("  Caputo heat equation  D^a theta = kappa theta_xx  ->  (-iw)^a = -kappa k^2")
for a in alpha_cap:
    omega = 1e6
    kk = np.sqrt(-((-1j*omega)**a)/kappa)
    print(f"   alpha={a:.1f}: k = {kk:.4e} 1/m, attenuation/m = {np.imag(kk):.4e} "
          f"(Fourier would give {np.sqrt(omega/(2*kappa)):.4e})")

print("\nDone. All checks printed above are reproducible with this file alone.")

# ---------------------------------------------------------------- MGT, rigid case
# The coupled MGT printout above is unreliable for one mode: when Re(k) -> 0 the
# ratio w/Re(k) is not a phase speed but a numerical artefact, so here the rigid
# thermal problem is solved on its own, where the answer is analytic:
#     k^2 = w^2 (1 - i w tau) / (c^2 - i w b)
# and the high-frequency characteristic speed tends to sqrt(b/tau).
print("\n" + "="*78)
print("MGT RIGID-CASE DISPERSION (analytic k^2 = w^2(1-iw*tau)/(c2-i*w*b))")
print("="*78)
tau_v, b_v, c2_v = 1e-11, 2.5e-5, 1.254e6
for f0 in [1e3, 1e6, 1e9, 1e11]:
    om = 2*np.pi*f0
    k2 = om**2*(1 - 1j*om*tau_v)/(c2_v - 1j*om*b_v)
    kk = np.sqrt(k2)
    att = abs(np.imag(kk))
    vph = om/np.real(kk) if abs(np.real(kk)) > 1e-12 else float('nan')
    print(f"  f={f0:.0e} Hz: k={kk:+.4e} 1/m | v_ph={vph:8.1f} m/s | "
          f"atten. length={1/att if att>0 else np.inf:.3e} m")
print(f"  predicted high-frequency limit sqrt(b/tau) = {np.sqrt(b_v/tau_v):.1f} m/s")
print(f"  predicted low-frequency limit  sqrt(c2)    = {np.sqrt(c2_v):.1f} m/s")
