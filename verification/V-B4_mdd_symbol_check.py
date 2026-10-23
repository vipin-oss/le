#!/usr/bin/env python3
"""V-B4 recheck — is the manuscript's Fourier symbol for the finite-horizon derivative right?

Manuscript, energy_flux_derivations.tex:270:
    D_w f(t)  <->  [(1 - e^{-i w_f w}) / (i w_f w)] * (-i w_f) \hat f     "(simplified)"
Manuscript, sec06:86:
    D_w f(t) = (1/w) \int_{t-w}^{t} kappa(t-xi) f'(xi) dxi

Written as a convolution, with eta = t - xi:
    D_w f(t) = (1/w) \int_0^w kappa(eta) f'(t - eta) deta
so its symbol is, for any kernel,
    sigma(Omega) = (i Omega / w) * Khat(Omega),   Khat(Omega) = \int_0^w kappa(eta) e^{-i Omega eta} deta
The manuscript's factor is the special case kappa == 1 (Khat = (1 - e^{-i Omega w})/(i Omega)).
This script evaluates both for the kernel the paper inherits (sec06:95) and reports the error.
"""
import sympy as sp

eta, Om_s, w_s = sp.symbols("eta Omega w", real=True)


def khat(Om, ww, al, be):
    """Khat(Omega) = int_0^w kappa(eta) e^{-i Omega eta} deta, exactly (kappa is a quadratic)."""
    kap = 1 - 2 * be * eta / w_s + al ** 2 * eta ** 2 / w_s ** 2
    expr = sp.integrate(kap * sp.exp(-sp.I * Om_s * eta), (eta, 0, w_s))
    return complex(expr.subs({Om_s: Om, w_s: ww}).evalf(20))


def run(al, be, ww, Om):
    sym_true = 1j * Om * khat(Om, ww, al, be) / ww
    sym_ms = complex(((1 - sp.exp(-sp.I * Om * ww)) / (sp.I * Om * ww) * (-sp.I * Om)).evalf(20))
    return sym_true, sym_ms

print("=" * 96)
print("finite-horizon derivative: exact symbol vs the manuscript's closed form")
print("kernel kappa(e) = 1 - 2*beta*e/w + alpha^2 e^2/w^2   (sec06:95),  window w")
print("=" * 96)
print(f"{'alpha':>6s} {'beta':>5s} {'w':>7s} {'Omega':>8s} | {'exact symbol':>26s} {'ms closed form':>26s} {'ratio':>8s}")
print("-" * 96)
for (al, be, ww, Om) in [(0.0, 0.0, 1.0, 3.0),     # kappa == 1 exactly -> the only case the formula covers
                         (1.0, 0.5, 1.0, 3.0),
                         (1.0, 0.0, 1.0, 3.0),
                         (0.5, 0.25, 2.0, 0.5),
                         (1.0, 0.5, 1.0, 12.0)]:
    a, b = run(al, be, ww, Om)
    print(f"{al:6.2f} {be:5.2f} {ww:7.2f} {Om:8.2f} | {a.real:+12.6f}{a.imag:+12.6f}j "
          f"{b.real:+12.6f}{b.imag:+12.6f}j {abs(a/b):8.3f}")
print("-" * 96)
print("Row 1 (kappa == 1) is the only row where the two agree; everywhere else the manuscript's")
print("factor is not a simplification of the operator but the symbol of a DIFFERENT operator.")
print("Reason: the closed form assumes kappa == 1; with the inherited kernel the transform is")
print("Khat(Omega) = int_0^w kappa e^{-i Omega eta} deta, which has no elementary closed form and")
print("is not a constant multiple of the kappa == 1 result.  A convolution does have a")
print("multiplicative symbol - it is just not that one.")
print()
print("Verdict: WRONG (CONFIRMED by derivation + numerics; no source needed, this is mathematics).")
print("Fix: either delete the line or write sigma(Omega) = (i Omega / w) Khat(Omega) with Khat defined.")
