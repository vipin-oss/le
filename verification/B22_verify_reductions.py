#!/usr/bin/env python3
"""B22 -- INDEPENDENT re-implementation of the Q1 reduction checks.

Written from the displayed equations only; not derived from
phase5/verification/verify_unified_reductions.py. Conventions:
heat-flux law written as a residual (everything on the left = 0).

  Fourier      : q + k*grad_T                                  = 0
  LS (1967)    : q + t0*dq + k*grad_T                          = 0
  DPL 1st ord. : q + tq*dq + k*(grad_T + tT*dgrad_T)           = 0
  TPL (Roy Ch) : DPL + kstar*(grad_a + tv*dgrad_a)             = 0   (a = alpha_GN)
  MGT          : q + tm*dq + k*grad_T + kstar*grad_a           = 0
  GN-III       : rho*ce*dTT + beta*dT_du_x? -> see below
"""
import sympy as sp

q, dq = sp.symbols('q dq')
gT, dgT = sp.symbols('gT dgT')          # grad T and its time derivative
gA, dgA = sp.symbols('gA dgA')          # grad alpha (GN 'nu') and time derivative
k, kstar = sp.symbols('k kstar', positive=True)
t0, tq, tT, tv, tm = sp.symbols('t0 tq tT tv tm')

FOURIER = q + k*gT
LS = q + t0*dq + k*gT
DPL = q + tq*dq + k*(gT + tT*dgT)
TPL = DPL + kstar*(gA + tv*dgA)
MGT = q + tm*dq + k*gT + kstar*gA

checks = []

def chk(name, expr, target):
    ok = sp.simplify(sp.expand(expr - target)) == 0
    checks.append((name, ok))
    print(('PASS' if ok else 'FAIL'), name)

chk('LS --(t0=0)--> Fourier', LS.subs(t0, 0), FOURIER)
chk('DPL --(tT=0, tq=t0)--> LS', DPL.subs({tT: 0, tq: t0}), LS)
chk('DPL --(tT=0, tq=0)--> Fourier', DPL.subs({tT: 0, tq: 0}), FOURIER)
chk('TPL --(kstar=0)--> DPL', TPL.subs(kstar, 0), DPL)
chk('MGT --(tm=0, kstar=0)--> Fourier', MGT.subs({tm: 0, kstar: 0}), FOURIER)
# the physically standard MGT chain that the Arena script does NOT test:
chk('MGT --(tm=0)--> GN-III flux (k and kstar retained)', MGT.subs(tm, 0), q + k*gT + kstar*gA)
chk('MGT --(kstar=0)--> LS-type flux with t0=tm', MGT.subs(kstar, 0), LS.subs(t0, tm))

# ---- GN-III / GN-II at the level of the heat equation --------------------
x, t = sp.symbols('x t')
T = sp.Function('T')(x, t)
al = sp.Function('alpha')(x, t)
u = sp.Function('u')(x, t)
rho_ce, beta, kap, kstar_g = sp.symbols('rho_ce beta kappa kstar_g', positive=True)

# GN-II: rho ce alphatt = kstar alpha_xx - beta u_xt     (T = alpha_t)
gn2 = sp.Eq(rho_ce*sp.diff(al, t, 2), kstar_g*sp.diff(al, x, 2) - beta*sp.diff(u, x, t))
# GN-III: rho ce Ttt = kstar Txx + kappa T_xxt - beta u_xtt
gn3 = sp.Eq(rho_ce*sp.diff(T, t, 2), kstar_g*sp.diff(T, x, 2) + kap*sp.diff(T, x, 2, t) - beta*sp.diff(u, x, t, 2))
lhs2 = sp.expand(gn2.lhs - gn2.rhs); lhs3 = sp.expand(gn3.lhs - gn3.rhs)
diff_form = sp.expand(lhs3.subs(kap, 0).subs(T, sp.diff(al, t)) - sp.diff(lhs2, t))
checks.append(('GN-III(kappa=0) = d/dt[GN-II] under T=alpha_t', sp.simplify(diff_form) == 0))
print(('PASS' if checks[-1][1] else 'FAIL'), checks[-1][0])
print("   note: differentiating GN-II loses one integration constant ->")
print("   equality of equations does NOT imply equality of solution sets without compatible initial data.")

# ---- Caputo on monomials -------------------------------------------------
tc = sp.symbols('tc', positive=True)
cap_ok = True
for n in range(1, 8):
    for a in (sp.Rational(1, 2), sp.Rational(1, 3), sp.Integer(1), sp.Integer(2)):
        if a >= n:
            continue
        caputo = sp.gamma(n + 1)/sp.gamma(n + 1 - a)*tc**(n - a)
        if a.is_Integer:
            truth = sp.diff(tc**n, tc, int(a))
            if sp.simplify(caputo - truth) != 0:
                cap_ok = False
checks.append(('Caputo D^alpha t^n monomial identity (alpha=1/2,1/3,1,2; n<8)', cap_ok))
print(('PASS' if cap_ok else 'FAIL'), checks[-1][0])
print("   scope: monomial test functions only; NOT a general operator identity,")
print("   and alpha in (0,1) is the only range where the closed form is normally quoted.")

# ---- nonlocal xi -> 0 ----------------------------------------------------
xi, kk, c0 = sp.symbols('xi kk c0', positive=True)
sig, sig_loc, lap = sp.symbols('sigma sigma_loc lap_sigma')
helm = sig - xi**2*lap - sig_loc
chk('nonlocal Helmholtz form --(xi=0)--> local', helm.subs(xi, 0), sig - sig_loc)
# Eringen nonlocal dispersion: c^2 = c0^2/(1+xi^2 k^2)
c2 = c0**2/(1 + xi**2*kk**2)
ok = sp.simplify(c2.subs(xi, 0) - c0**2) == 0
checks.append(('nonlocal dispersion --(xi=0)--> c^2 = c0^2', ok))
print(('PASS' if ok else 'FAIL'), checks[-1][0])
# small-xi expansion: c = c0 (1 - xi^2k^2/2 + ...) -> softening, no cutoff
ser = sp.series(sp.sqrt(c2), xi, 0, 3).removeO()
print("   small-xi expansion:", sp.simplify(ser))

npass = sum(1 for _, ok in checks if ok)
print(f"\nSUMMARY: {npass}/{len(checks)} independent checks pass")
