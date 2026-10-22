#!/usr/bin/env python3
"""V-B9a checks: dimensional audit of appA register rows + the thermal-channel
factor algebra + the sum rule of the primary source's own printed tables.

stdlib only (no sympy in this sandbox -- stated in V-B9a/V-B9b).
Run:  python3 V-B9a_checks.py
All numbers printed below are the ones cited in V-B9a_appa_ledger.md,
V-B9b_thermal_factor.md and V-B9c_eint_identity.md.
"""
from fractions import Fraction as F

# ---------------------------------------------------------------- dimensions
# base exponents (kg, m, s, K, C) -- C = coulomb, kept so the piezoelectric
# rows can be handled in the same table.
def d(kg=0, m=0, s=0, K=0, C=0):
    return (F(kg), F(m), F(s), F(K), F(C))

def mul(*xs):
    out = [F(0)] * 5
    for x in xs:
        out = [a + b for a, b in zip(out, x)]
    return tuple(out)

def show(x):
    names = "kg m s K C".split()
    return " ".join("%s^%s" % (n, e) for n, e in zip(names, x) if e != 0) or "1"

KG, M, S, KEL, COU = 1, 1, 1, 1, 1
rho   = d(KG, -3)                 # kg/m^3
c     = d(0, 2, -2, -1)           # J/(kg K) = m^2/(s^2 K)
rhow  = mul(rho, c)               # J/(m^3 K)
kF    = d(KG, 1, -3, -1)          # Fourier  W/(m K)
kS    = d(KG, 1, -4, -1)          # GN-II    W/(m K) * s   (q = -k* grad alpha)
beta  = d(KG, -1, -2, -1)         # Pa/K
T0    = d(0, 0, 0, 1)             # K
u     = d(0, 1, 0)                # m
alpha = d(0, 0, 1, 1)             # K s   (alpha_dot = T)
q     = d(KG, 0, -3)              # W/m^2
Wm3   = d(KG, -1, -3)             # W/m^3

print("=" * 70)
print("CHECK 1  EQ-016 (GN-II in the thermal-displacement variable alpha)")
print("=" * 70)
print("printed: k*grad^2(alpha) = rho*c_e*alpha_ddot + beta*T0*u_ddot_{i,i}")
lhs_kS  = mul(kS, mul(d(0, -2), alpha))     # grad^2 alpha
lhs_kF  = mul(kF, mul(d(0, -2), alpha))
term_a  = mul(rhow, mul(alpha, d(0, 0, -2)))          # rho c alpha_ddot
term_u2 = mul(beta, T0, u, d(0, -1, -2))              # beta T0 u_ddot_{,i}
term_u1 = mul(beta, T0, u, d(0, -1, -1))              # beta T0 u_dot _{,i}
for nm, x in [("k* grad^2 a  (k* = GN-II const)", lhs_kS),
              ("k  grad^2 a  (k  = Fourier const)", lhs_kF),
              ("rho c_e alpha_ddot", term_a),
              ("beta T0 u_ddot_{i,i} (as printed)", term_u2),
              ("beta T0 u_dot _{i,i}  (correct)", term_u1),
              ("target W/m^3", Wm3)]:
    print("  %-38s %s" % (nm, show(x)))
print("  --> as printed the coupling term is off by one power of time in BOTH")
print("      readings of k; the corrected GN-II form is rho c alpha_ddot +")
print("      beta T0 u_dot_{i,i} = k* grad^2 alpha  (integrate the T-form once).")

print()
print("=" * 70)
print("CHECK 2  EQ-017 (candidate GN-II entropy flux p_i = k_ij alpha_{,j})")
print("=" * 70)
entropy_flux = d(KG, 0, -3, -1)                     # W/(m^2 K)
p_kS = mul(kS, mul(d(0, -1), alpha))
p_kF = mul(kF, mul(d(0, -1), alpha))
print("  p_i (k = k*)      %s" % show(p_kS))
print("  p_i (k = Fourier) %s" % show(p_kF))
print("  entropy flux      %s" % show(entropy_flux))
print("  --> with k* the row is short by exactly one factor 1/K (i.e. 1/T);")
print("      with the Fourier k it is not an entropy flux at all.")

print()
print("=" * 70)
print("CHECK 3  EQ-022 legacy MGT heat equation")
print("=" * 70)
lhs1 = mul(d(0, 0, 1), q, d(0, 0, -2))     # tau q_ddot
lhs2 = mul(q, d(0, 0, -1))                 # q_dot
def inv(x):
    return tuple(-e for e in x)
rhs  = mul(kF, inv(rhow), mul(d(0, -1), mul(d(0, 0, -1), T0)))
print("  tau q_ddot        %s" % show(lhs1))
print("  q_dot             %s" % show(lhs2))
print("  k/(rho c)  [diffusivity]                 %s" % show(mul(kF, inv(rhow))))
print("  grad(T_dot + tau T_ddot)                 %s" % show(mul(d(0, -1), mul(d(0, 0, -1), T0))))
print("  RHS (k/rho c) grad(T_dot + tau T_ddot)   %s" % show(rhs))
print("  --> LHS and RHS are not even in the same base dimensions: the printed")
print("      legacy MGT row is dimensionally inconsistent (the live register")
print("      withdrew it for exactly this reason).")

print()
print("=" * 70)
print("CHECK 4  thermal-channel factor: which of T0/T, T/T0 is the right one?")
print("=" * 70)
# J_th = <theta q>/T0 is the verified second-order mean (V-B3d eq. 2.4 check).
# Write the printed thermal channel as  c * (K grad T) = -c q   with
# K grad T = -q, and T = T0 + theta.  Keep first order in eps = theta/T0.
# Mean over a period: <q> = 0, so the mean of c*q is  <q1 * c1 eps>/... with
# c = c0 + c1 eps -> <c q> = c1 <eps q> = c1 <theta q>/T0.
# Bracket conventions: Barak eq (45) is P = -Re[...]; manuscript sec10:114 same.
Jbar = F(1)   # units of <theta q>/T0
for name, c0, c1, bracket in [
        ("(T0/T) = 1/(1+eps)",  F(1), F(-1), "-Re[...]  (source and manuscript)"),
        ("(T/T0) = 1+eps",      F(1), F(1),  "-Re[...]  (source and manuscript)")]:
    # term in bracket is c*K grad T = -c*q ; P = -Re[bracket]
    # mean of P = -< -c q > = +<c q> = c1*<theta q>/T0
    sign = +1 if c1 > 0 else -1
    print("  %-22s bracket %-38s  mean J_th = %+d * <theta q>/T0  -> %s"
          % (name, bracket, sign,
             "CORRECT" if sign == 1 else "SIGN-INVERTED"))
print("  (T = absolute temperature assumed above. If T denotes the increment")
print("   theta, then T0/T = T0/theta is singular as theta->0: unusable.)")
print("  CONCLUSION: in the source's own convention T/T0 is right and T0/T")
print("  would invert the sign of the second-order thermal flux.")

print()
print("=" * 70)
print("CHECK 5  the primary source's own sum rule, from its printed tables")
print("=" * 70)
# Barak et al. 2023 (Sci Rep 13), incident P wave, n=p=l=1 column as tabulated
# beneath Figs 2-9 of the publisher PDF.  ('-' = not printed / zero.)
tbl = {
    0:  dict(ERP=0.12, ERT=0.00, ERS=0.00, ES1=0.0,      ES2=0.0,    ES3=0.0,  ES4=0.0,  Eint=0.00),
    30: dict(ERP=0.00, ERT=0.00, ERS=0.082, ES1=7e-6,    ES2=0.0065, ES3=1.58, ES4=0.07, Eint=-0.85),
    70: dict(ERP=0.29, ERT=0.01, ERS=0.110, ES1=9e-5,    ES2=0.031,  ES3=2.23, ES4=0.52, Eint=-2.07),
}
print("  eq (58) of the source asserts sum(ES_s) + E_int + ERP + ERT + ERS = 1")
for ang in (0, 30, 70):
    r = tbl[ang]
    s = sum(r.values())
    print("    theta0=%2d deg : sum of the NINE printed numbers = %+.3f   (E_int = %+.2f)"
          % (ang, s, r["Eint"]))
print("  !! WITHDRAWN AS EVIDENCE 2026-10-22 (BRAVE_B11 cond.1): these numbers come from ONE")
print("  !! rendering (PDF conversion). The HTML article page and the per-figure pages carry")
print("  !! images only, so no second rendering agrees -> status UNVERIFIED, paper tag CONDITIONAL.")
print("  --> as read: E_int is printed, non-zero and O(1): the cross terms are NOT dropped.")
print("      [if the numbers hold] they miss 1 by 0.1 to 0.9; but see the withdrawal above.")

print()
print("=" * 70)
print("CHECK 6  why 'R+T=1' is a tautology in the total-flux convention")
print("=" * 70)
# A = 1 - R - T is a definition once R,T come from the total field; then
# |R+T+A-1| = 0 identically. Demonstrate: pick any R.
for R in (0.3, 0.5):
    A = 1 - R - (1 - R)
    print("    R=%.1f  T=%.1f  ->  A = 1-R-T = %.1f  (identically 0: no information)" % (R, 1 - R, A))
print("  The informative check is the independent dissipation integral (V-B3d 3.4).")
