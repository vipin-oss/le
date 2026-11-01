#!/usr/bin/env python3
"""Check selected normalization consequences of the displayed MDD operator.

The checks treat the finite-window expression as a schematic operator and use
generic polynomial test functions through degree five with constant kernels.
They do not verify source transcription, a material kernel, admissibility, or a
general short-horizon theorem.
"""
from __future__ import annotations

import sympy as sp


t, omega, tau = sp.symbols("t omega tau", positive=True)
coefficients = sp.symbols("a0:6")
f = sum(coefficients[k] * t**k for k in range(6))
f_tau = sum(coefficients[k] * tau**k for k in range(6))
window_integral = sp.integrate(sp.diff(f_tau, tau), (tau, t - omega, t))

# For a generic polynomial of degree at most five and K_MDD = 1, the normalized
# finite-window average tends to the ordinary derivative as omega -> 0+.
unit_kernel_operator = window_integral / omega
assert sp.simplify(sp.limit(unit_kernel_operator, omega, 0, dir="+") - sp.diff(f, t)) == 0

# A constant kernel K_MDD = 2 scales the limit, showing that the normalization
# depends on kernel values and is not fixed by the horizon factor alone.
doubled_kernel_operator = 2 * window_integral / omega
assert sp.simplify(sp.limit(doubled_kernel_operator, omega, 0, dir="+") - 2 * sp.diff(f, t)) == 0
assert sp.simplify(2 * sp.diff(f, t) - sp.diff(f, t)) != 0

# Omitting the displayed 1/omega factor changes the short-window limit to zero.
unnormalized_integral = window_integral
assert sp.simplify(sp.limit(unnormalized_integral, omega, 0, dir="+")) == 0

print("PASS: for a generic polynomial through degree five and K_MDD=1, the normalized window tends to f'(t)")
print("PASS: constant K_MDD=2 doubles that limit, so kernel normalization matters")
print("PASS: omitting 1/omega makes the same window integral tend to zero")
print("Scope: polynomial/constant-kernel normalization checks only; no source transcription or general kernel theorem")
