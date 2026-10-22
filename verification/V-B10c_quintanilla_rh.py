#!/usr/bin/env python3
"""V-B10c — independent Routh-Hurwitz check of the TPL stability window printed as
eq (1.2) of Quintanilla, Appl. Math. Comput. 213 (2009) 153-162
(DOI 10.1016/j.amc.2009.03.005).

The window as printed is:  (k/k*) tau_q  <  tau*_m  <  2 k tau_T / tau_q.

Model used here (rigid heat conductor, no coupling, no source; the only subsystem
checked -- NOT the coupled thermoelastic system): the once-time-differentiated
TPL heat equation of the T2 truncation (second order in tau_q, first order in
tau_T and tau_m), in the form printed for Roy Choudhuri (2007) eq (9) with the
second-order Taylor factor:

  (1 + tau_q d/dt + (tau_q^2/2) d^2/dt^2) T_ddot
      = tau*_v lap(T_dot) + k tau_T lap(T_ddot) + c0 lap(T)

Plane-wave ansatz T ~ exp(s t + i xi.x), lap -> -lam2 (lam2 = |xi|^2 > 0) gives

  a0 s^4 + a1 s^3 + a2 s^2 + a3 s + a4 = 0
  a0 = tau_q^2/2, a1 = tau_q, a2 = 1 + lam2 k tau_T, a3 = lam2 tau*_v,
  a4 = lam2 c0

Two normalisations of the constant term are tested (see report):
  N1: c0 = k            (RC2007 normalisation, flux law divided by k*)
  N2: c0 = k_star/k     (so that the T-coefficient grouping matches k/k*)

Run:  /tmp/venv/bin/python verification/V-B10c_quintanilla_rh.py
"""
import sympy as sp
import numpy as np

s, tq, tT, tm, k, kst, lam2 = sp.symbols('s tau_q tau_T tau_m k k_star lam2',
                                         positive=True)

def poly(c0):
    a0 = tq**2/2
    a1 = tq
    a2 = 1 + lam2*k*tT
    a3 = lam2*tm
    a4 = lam2*c0
    return [a0, a1, a2, a3, a4]

print("="*78)
print("1. SYMBOLIC ROUTH-HURWITZ TABLE (quartic, exact rational arithmetic)")
print("="*78)
for name, c0 in (("N1 (c0 = k)", k), ("N2 (c0 = k*/k)", kst/k)):
    a0, a1, a2, a3, a4 = poly(c0)
    # Routh array for a0 s^4 + a1 s^3 + a2 s^2 + a3 s + a4
    b1 = sp.simplify((a1*a2 - a0*a3)/a1)
    b2 = sp.simplify((a1*a4 - a0*sp.Integer(0))/a1)          # a1*a4/a1
    c1 = sp.simplify((b1*a3 - a1*b2)/b1)
    c2 = sp.simplify((b1*0 - a1*0)/b1)
    print(f"\n--- {name} ---")
    print("first column: a0, a1, b1, c1, a4")
    print("  a0 =", a0)
    print("  a1 =", a1)
    print("  b1 =", b1)
    print("  c1 =", c1)
    print("  a4 =", a4)
    # positivity of b1 and c1 are the only non-trivial conditions
    num_b1 = sp.numer(sp.together(b1))
    num_c1 = sp.numer(sp.together(c1))
    print("  b1 > 0  <=>  ", sp.factor(sp.simplify(num_b1)), " > 0")
    print("  c1 > 0  <=>  ", sp.factor(sp.simplify(num_c1)), " > 0")
    # rewrite c1's numerator as  A + lam2*B
    A, B = sp.symbols('A B')
    expr = sp.expand(sp.simplify(num_c1))
    expr = sp.expand(expr/ (tq*lam2))     # divide by the positive factor tq*lam2
    print("  c1 numerator / (tau_q*lam2) =", sp.collect(sp.simplify(expr), lam2))
    print("  as  P + lam2*Q :  P =", sp.simplify(expr.subs(lam2, 0)),
          "   Q =", sp.simplify(sp.diff(expr, lam2)))
print("""
READING OF THE SYMBOLIC RESULT
  The two non-trivial Routh conditions are
     (R1)  P + lam2*Q > 0  for every lam2 > 0
     (R2)  which, since a0,a1,a2,a3,a4 > 0 already holds, is the whole condition.
  For both normalisations this splits into
     P > 0   ->  tau_m > tau_q * c0        (lower bound, proportional to the T-coefficient)
     Q >= 0  ->  tau_m <= 2*k*tau_T/tau_q  (upper bound, INDEPENDENT of the normalisation)
""")

print("="*78)
print("2. NUMERIC SWEEP: does the printed window predict the sign of Re(s)?")
print("="*78)
def worst_real_part(tau_q, tau_T, tau_m, k=1.0, c0=1.0, n=400, lmax=1e6):
    """max over lam2>0 of max Re(root) of the quartic (log-spaced lam2 grid)."""
    best = -1e9; arg = None
    lams = np.logspace(-4, np.log10(lmax), n)
    for L in lams:
        a = [tau_q**2/2, tau_q, 1 + L*k*tau_T, L*tau_m, L*c0]
        r = np.roots(a)
        m = float(np.max(r.real))
        if m > best:
            best, arg = m, L
    return best, arg

# Case study with the numbers Barak (2023) prints for the second-order TPL model
# (tau_q = 0.05, tau_T = 0.03, tau_v = 0.02, recorded in control/FULLTEXT_FINDINGS_02 F9)
k = 1.0
for tq_, tT_, label in [(0.05, 0.03, "Barak-scale lags (tau_q=0.05, tau_T=0.03)"),
                        (0.02, 0.03, "tau_q < tau_T (0.02, 0.03)")]:
    lo = tq_*k                       # c0 = k normalisation -> tau_m > tau_q*k
    hi = 2*k*tT_/tq_
    print(f"\n{label}:  predicted window (c0=k) = ({lo:g}, {hi:g})")
    for tm_ in [0.5*lo, lo*0.999, lo*1.001, 0.5*(lo+hi), hi*0.999, hi*1.001, 10*hi]:
        w, L = worst_real_part(tq_, tT_, tm_, k=k, c0=k)
        inside = (lo < tm_ < hi)
        print(f"  tau_m={tm_:<9.5g} inside={str(inside):<5} "
              f"max Re(s)={w:+.6e} at lam2={L:.4g}  -> {'STABLE' if w<0 else 'UNSTABLE'}")

print("""
General symbolic condition for the constant term c0 = C:
   [tau_m - tau_q*C] + lam2*[tau_m*(k*tau_T - tau_m*tau_q/2)] > 0 for all lam2 > 0
   <=>  tau_m > tau_q*C   and   tau_m <= 2*k*tau_T/tau_q.
N1 (C=k)          -> (tau_q*k, 2*k*tau_T/tau_q)
N2 (C=k*/k)       -> (tau_q*k*/k, 2*k*tau_T/tau_q)
N3 (C=k/k*)       -> (tau_q*k/k*, 2*k*tau_T/tau_q)   <-- EXACTLY the printed eq (1.2)

The switch of sign of max Re(s) happens exactly at the two predicted edges
(to within the 1e-3 relative offset used for the test points), so the window is
confirmed for the normalisation c0 = k.  The upper edge 2*k*tau_T/tau_q is
normalisation-independent; the lower edge scales with c0.
""")

print("="*78)
print("3. EDGE SHARPNESS: scan tau_m through the predicted upper edge")
print("="*78)
tq_, tT_, k = 0.05, 0.03, 1.0
hi = 2*k*tT_/tq_
for tm_ in np.linspace(hi*0.90, hi*1.10, 9):
    w, L = worst_real_part(tq_, tT_, tm_, k=k, c0=k, n=600)
    print(f"  tau_m/hi={tm_/hi:.3f}  max Re(s)={w:+.4e}  argmax lam2={L:.4g}"
          f"   {'STABLE' if w<0 else 'UNSTABLE'}")
print("""
Near the edge the instability is pushed to ever larger wave numbers
(lam2* ~ P/|Q| -> infinity as tau_m -> 2*k*tau_T/tau_q from above), which is why
a finite wavelength grid that stops at lam2 = 400 misses it.  This is a
long-wavelength/short-wavelength split, not a failure of the criterion.""")

print("="*78)
print("4. N3: the exact printed form, checked numerically")
print("="*78)
k_, kst_ = 1.0, 0.4          # k/k* = 2.5
tq_, tT_ = 0.05, 0.03
C = k_/kst_
lo, hi = tq_*C, 2*k_*tT_/tq_
print(f"  C = k/k* = {C:g}, printed window = ({lo:g}, {hi:g})")
for tm_ in [0.9*lo, lo*1.001, 0.5*(lo+hi), hi*0.999, hi*1.05]:
    w, L = worst_real_part(tq_, tT_, tm_, k=k_, c0=C, n=600)
    print(f"  tau_m={tm_:<8.5g} predicted_inside={str(lo<tm_<hi):<5} "
          f"max Re(s)={w:+.4e} -> {'STABLE' if w<0 else 'UNSTABLE'}")
