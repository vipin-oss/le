#!/usr/bin/env python3
"""V-B8a checks: TPL lag law against Roy Choudhuri 2007 as reported in FULLTEXT_FINDINGS_02 (F6).

Two independent checks, no network, no sympy:
  (A) dimensional bookkeeping of the printed second-order term in the manuscript
  (B) Taylor-truncation bookkeeping of the three-lag law, to see which coefficients
      a legitimate second-order truncation can produce, and whether tau_v/2 * d2/dt2(grad T)
      can arise at ANY order.

Units convention (SI exponents only):
    [t] = 1, [T] = K, [x] = m, [q] = W/m^2, [k] = W/(m K), [k*] = W/(m K) (same as k after
    v has units of K*s, i.e. v_dot = T with v having units K*s).
ASCII only.
"""

from fractions import Fraction

def dims():
    # exponent vectors over (s, m, K)
    return {
        't': (1, 0, 0),
        'x': (0, 1, 0),
        'T': (0, 0, 1),
    }

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def mul(a, n):
    return tuple(x * n for x in a)

def fmt(d):
    s, m, k = d
    parts = []
    if s: parts.append(f"s^{s}")
    if m: parts.append(f"m^{m}")
    if k: parts.append(f"K^{k}")
    return "*".join(parts) if parts else "1"

print("=== (A) dimensional bookkeeping of the second-order term ===")
# Target: a term added to T_,i inside the bracket of the flux law, so it must have units of T_,i.
grad_T = (0, -1, 1)                 # dT/dx
dt2_grad_T = add(grad_T, mul((1, 0, 0), -2))   # d2/dt2 of grad T
print("  [T_,i]            =", fmt(grad_T))
print("  [d2/dt2 T_,i]     =", fmt(dt2_grad_T))

for name, tau_power in (("tau_nu/2   (printed)", 1), ("tau_nu^2/2 (squared)", 2)):
    tau = mul((1, 0, 0), tau_power)
    got = add(tau, dt2_grad_T)
    ok = (got == grad_T)
    print(f"  {name:22s} coeff units {fmt(tau):6s} -> term units {fmt(got):10s} "
          f"{'OK' if ok else 'MISMATCH (term has extra s^%d)' % (got[0] - grad_T[0])}")

print()
print("=== (A2) same check in the frequency domain (legacy eq. ef:tpl:2) ===")
# Printed: q(1 - i w tq) = -k T_,i [ (1 - i w tT) - (w^2 tv/2)(1 - i w tv) ]
# The bracket must be dimensionless. With [w] = s^-1, [t] = s.
print("  coefficient (w^2 * tv / 2):     s^-2 * s^1 = s^-1   -> NOT dimensionless")
print("  coefficient (w^2 * tv^2 / 2):   s^-2 * s^2 = 1      -> dimensionless")
print("  coefficient (w * tq), (w * tT): s^-1 * s^1 = 1      -> dimensionless (as expected)")

print()
print("=== (B) Taylor truncation of the three-lag law, order by order ===")
# Law (Roy Choudhuri 2007 eq 3, as reported in F6 and confirmed in two OA papers):
#   q(t+tq) = -[ k grad T(t+tT) + k* grad v(t+tv) ],   v_dot = T
# Truncate the LHS and each RHS piece to order N and list the coefficients.
# We only track the ORDER of the derivative and the power of the lag, which is what decides
# whether a "tau_v/2 * d2/dt2" coefficient can appear.
print("  term structure of the RHS gradient pieces after Taylor expansion:")
for lag, power in (("tau_T (grad T side)", "tau_T^r / r!"), ("tau_v (grad v side)", "tau_v^r / r!")):
    print(f"    {lag:22s}: coefficient of d^r/dt^r is {power}")

print("  with v_dot = T, d^r/dt^r (grad v) = d^(r-1)/dt^(r-1) (grad T), so the grad-v piece")
print("  contributes to the grad-T axis with coefficient tau_v^r/r! at derivative order r-1:")
rows = [(r, Fraction(1, 1)) for r in range(0, 1)]
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
for r in range(0, 5):
    c = Fraction(1, factorial(r))
    print(f"    r={r}: coeff tau_v^{r}/{factorial(r)} on d^{max(r-1,0)}/dt^{max(r-1,0)}(grad T)")

print()
print("  smallest r that gives a second time derivative of grad T on the tau_v axis: r = 3")
print("  => coefficient tau_v^3/6 on d2/dt2(grad T); r = 2 gives tau_v^2/2 on d1/dt(grad T).")
print("  => NO truncation order produces (tau_v/2) * d2/dt2(grad T).")
print()
print("  second-order truncation of the WHOLE flux law (both lags to tau^2/2) gives, on the")
print("  grad-T axis:  (1 + tq D + tq^2/2 D^2) q = -k (1 + tT D + tT^2/2 D^2) grad T")
print("                                                     - k* (1 + tv D + tv^2/2 D^2) grad v")
print("  and after grad v = D^-1 grad T the last bracket becomes tv*(grad T) + tv^2/2 * D(grad T) + ...")
print("  i.e. the tau_v pieces land on grad T itself and on its FIRST derivative, not its second.")

print()
print("=== (C) comparison of the three documented forms of the law ===")
forms = [
    ("Roy Choudhuri 2007 eq (3), as in F6 and in Zhang/Sun/Yang 2020 eq (4) and eq (7)",
     "lagged form with k* grad v", "first order in tq, tT, tv", "no tau^2/2 anywhere"),
    ("Barak et al. 2023 JTS eq (2.5), as in F9",
     "sum form: first order tv, tT ; second order tq on the energy bracket",
     "second order in tq only", "(tq^2/2) D_s^2"),
    ("Abouelregal/Khalil/Mohammed/Nasr/Zakaria/Ahmed 2020 Sci Rep eqs (9)-(11)",
     "general sums tau^r/r! on the flux (m) and gradient (n) axes",
     "any order m, n, p", "tau^2/2 at r = 2, on the tau_q and tau_phi axes"),
]
for f in forms:
    print("  -", f[0])
    print("      structure:", f[1], "| orders:", f[2], "| second-order coefficient:", f[3])
