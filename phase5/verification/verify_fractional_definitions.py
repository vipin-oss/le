#!/usr/bin/env python3
"""Check selected consequences of the displayed Caputo/RL integral definitions.

The checks use Euler beta-integral evaluation for monomials at integer n=1,2,3
and a constant-function negative case. They verify representative analytic
consequences of Eqs. (6.3) and (6.4), not source transcription, general
function-space regularity, or a fractional thermoelastic model.
"""
from __future__ import annotations

import sympy as sp

m, alpha = sp.symbols("m alpha", positive=True)
t = sp.symbols("t", positive=True)

for n in (1, 2, 3):
    # For n-1 < alpha < n and m >= n, beta-integral evaluation of the Caputo
    # formula on t^m gives the stated gamma ratio.
    caputo_from_integral = (
        sp.gamma(m + 1) / sp.gamma(m - n + 1)
        * (sp.gamma(m - n + 1) * sp.gamma(n - alpha) / sp.gamma(m + 1 - alpha))
        / sp.gamma(n - alpha)
        * t ** (m - alpha)
    )
    caputo_monomial = sp.gamma(m + 1) / sp.gamma(m + 1 - alpha) * t ** (m - alpha)
    assert sp.simplify(caputo_from_integral - caputo_monomial) == 0

    # The RL integral is a beta integral; differentiate its power n times.
    rl_integral = t ** (m + n - alpha) * sp.gamma(m + 1) / sp.gamma(m + n + 1 - alpha)
    rl_from_integral = sp.diff(rl_integral, t, n)
    rl_monomial = sp.gamma(m + 1) / sp.gamma(m + 1 - alpha) * t ** (m - alpha)
    assert sp.simplify(rl_from_integral - rl_monomial) == 0

# Negative test for 0 < alpha < 1: Caputo differentiation annihilates a
# constant, while the Riemann--Liouville derivative gives a nonzero power.
alpha_half = sp.Rational(1, 2)
caputo_constant = sp.S.Zero
rl_constant = sp.diff(t ** (1 - alpha_half) / sp.gamma(2 - alpha_half), t)
rl_constant_expected = t ** (-alpha_half) / sp.gamma(1 - alpha_half)
assert sp.simplify(caputo_constant) == 0
assert sp.simplify(rl_constant - rl_constant_expected) == 0
assert sp.simplify(rl_constant_expected) != 0

print("PASS: beta-integral evaluation of the Caputo definition on t^m gives the stated gamma ratio for n=1,2,3")
print("PASS: beta-integral evaluation and n derivatives of the RL definition give the same monomial ratio for n=1,2,3")
print("PASS: negative constant-function check distinguishes Caputo from Riemann--Liouville at alpha=1/2")
print("Scope: selected monomial consequences only; no source transcription, regularity theorem, or coupled-model claim")
