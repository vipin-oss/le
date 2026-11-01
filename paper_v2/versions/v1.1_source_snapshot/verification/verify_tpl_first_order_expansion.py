#!/usr/bin/env python3
"""Verify the first-order Taylor expansion displayed after Sec. 4 Eq. 4.17."""
import sympy as sp

t, tau_q, tau_T, tau_v = sp.symbols("t tau_q tau_T tau_v", real=True)
k, k_star = sp.symbols("k k_star", real=True)
q = sp.Function("q")(t)
grad_T = sp.Function("grad_T")(t)
grad_v = sp.Function("grad_v")(t)

# Shifted three-lag constitutive relation with all terms on the left.
shifted = q.subs(t, t + tau_q) + k * grad_T.subs(t, t + tau_T) + k_star * grad_v.subs(t, t + tau_v)
truncated = (
    q + tau_q * sp.diff(q, t)
    + k * (grad_T + tau_T * sp.diff(grad_T, t))
    + k_star * (grad_v + tau_v * sp.diff(grad_v, t))
)
first_order_series = (
    sp.series(q.subs(t, t + tau_q), tau_q, 0, 2).removeO()
    + k * sp.series(grad_T.subs(t, t + tau_T), tau_T, 0, 2).removeO()
    + k_star * sp.series(grad_v.subs(t, t + tau_v), tau_v, 0, 2).removeO()
)
assert sp.simplify(first_order_series - truncated) == 0

# The full shifted relation is not identical to its first-order truncation for
# independent nonzero lags; omitted second-order terms remain.
second_order_remainder = sp.series(q.subs(t, t + tau_q), tau_q, 0, 3).removeO() - sp.series(q.subs(t, t + tau_q), tau_q, 0, 2).removeO()
assert sp.simplify(second_order_remainder) != 0
assert sp.simplify(truncated.subs(k_star, 0) - (q + tau_q * sp.diff(q,t) + k * (grad_T + tau_T * sp.diff(grad_T,t)))) == 0

print("PASS: shifted three-lag law expands to the displayed first-order residual")
print("PASS: the higher-order remainder is nonzero in general; no second-order coefficient is asserted")
print("Scope: Taylor truncation in independent lags; source-specific admissibility is separate")
