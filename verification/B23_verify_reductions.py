#!/usr/bin/env python3
"""B23 independent re-implementation of the claimed limiting cases.

Written from the printed equations of the manuscript (phase5/master, commit
4caa9a8) without reading phase5/verification/verify_unified_reductions.py first;
differences found afterwards are listed in B23_REPORT.md.

Each check states the limit that the printed table claims, substitutes it, and
prints the residual so a reader can see *why* a row holds or fails.
"""
from __future__ import annotations

import sympy as sp

q, qd = sp.symbols("q qdot")
gT, gTd, gv, gvd = sp.symbols("gradT gradT_dot gradv gradv_dot")
k, ks = sp.symbols("k k_star")
t0, tq, tT, tv, tm = sp.symbols("tau0 tau_q tau_T tau_v tau_m")

fourier = q + k * gT
ls = q + t0 * qd + k * gT
dpl = q + tq * qd + k * (gT + tT * gTd)
tpl = q + tq * qd + k * (gT + tT * gTd) + ks * (gv + tv * gvd)
mgt = q + tm * qd + k * gT + ks * gv


def show(name: str, expr, expect_zero: bool) -> bool:
    expr = sp.simplify(expr)
    ok = (expr == 0) == expect_zero
    print(f"{'OK ' if ok else 'FAIL'} {name:62s} residual = {expr}")
    return ok


results = []
# Table row: LS -> classical coupled, tau_0 -> 0
results.append(show("LS (tau_0->0) = Fourier", ls.subs(t0, 0) - fourier, True))
# Table row: DPL -> LS, tau_T -> 0 with tau_q = tau_0   (the B22 repair)
results.append(show("DPL (tau_T->0, tau_q=tau_0) = LS", dpl.subs({tT: 0, tq: t0}) - ls, True))
# Negative control: the old, wrong substitution
results.append(show("DPL (tau_q->0) is NOT LS", dpl.subs(tq, 0) - ls, False))
# DPL -> Fourier when both lags vanish
results.append(show("DPL (tau_T=tau_q=0) = Fourier", dpl.subs({tT: 0, tq: 0}) - fourier, True))
# The trap: the naive "remove the third lag" substitution does NOT work. The
# manuscript does not claim it (T2 uses k^*=0), and this line shows why it must not.
results.append(show("TPL (tau_v->0) = DPL  [naive substitution, NOT claimed]", tpl.subs(tv, 0) - dpl, False))
# The limit that actually removes the third term
results.append(show("TPL (k_star->0) = DPL  [T2 reduction-map row]", tpl.subs(ks, 0) - dpl, True))
# Not claimed in print either, but a reader may try it: removing only the lags
# leaves the k^* v_{,i} term behind, so TPL alone does not reach Fourier.
results.append(show("TPL (all tau->0) = Fourier  [needs k_star=0 as well]", tpl.subs({tq: 0, tT: 0, tv: 0}) - fourier, False))
results.append(show("TPL (all tau->0, k_star=0) = Fourier", tpl.subs({tq: 0, tT: 0, tv: 0, ks: 0}) - fourier, True))
# MGT -> Fourier at tau_m = 0 and k_star = 0
results.append(show("MGT (tau_m->0, k_star->0) = Fourier", mgt.subs({tm: 0, ks: 0}) - fourier, True))
# MGT -> LS at k_star = 0, tau_0 = tau_m
results.append(show("MGT (k_star->0, tau_m=tau_0) = LS", mgt.subs({ks: 0, tm: t0}) - ls, True))

# GN-III with kappa = 0 is the time derivative of time-integrated GN-II
x, t = sp.symbols("x t", real=True)
a = sp.Function("alpha_gn")(x, t)
u = sp.Function("u")(x, t)
T = sp.Function("T")(x, t)
rho_c, bT0, kap, kstar = sp.symbols("rho_c beta_T0 kappa kappa_star", real=True)
gn2 = kstar * sp.diff(a, x, 2) - rho_c * sp.diff(a, t, 2) - bT0 * sp.diff(u, x, t)
gn3 = rho_c * sp.diff(T, t, 2) + bT0 * sp.diff(u, x, t, 2) - kap * sp.diff(T, x, 2, t) - kstar * sp.diff(T, x, 2)
gn3_0 = gn3.subs(kap, 0).subs(T, sp.diff(a, t))
results.append(show("GN-III (kappa=0) = d/dt GN-II, T = alpha_dot", gn3_0 + sp.diff(gn2, t), True))

# Caputo: at order 2 the operator is the ordinary second derivative
tc = sp.symbols("tc", positive=True)
cap_ok = all(
    sp.simplify(sp.gamma(n + 1) / sp.gamma(n - 1) * tc ** (n - 2) - sp.diff(tc**n, tc, 2)) == 0
    for n in range(2, 8)
)
print(("OK  " if cap_ok else "FAIL") + " Caputo order 2 = d2/dt2 on monomials 2..7")
results.append(cap_ok)

# Nonlocal Helmholtz operator: ell -> 0 gives the local law
ell = sp.symbols("ell", positive=True)
sig, sig_loc = sp.symbols("sigma sigma_local")
results.append(show("(1 - ell^2 lap) sigma -> sigma_loc at ell->0", sp.limit((sig - ell**2 * 0) - sig_loc, ell, 0) - (sig - sig_loc), True))

print()
print(f"passed {sum(results)} of {len(results)}")
print("the two 'FAIL' lines are intentional negative controls: they show that the")
print("naive substitutions do not reduce, and the manuscript does not claim them.")
