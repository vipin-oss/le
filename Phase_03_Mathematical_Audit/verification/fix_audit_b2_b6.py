#!/usr/bin/env python3
"""Fixes the two checks whose reconstruction was left as pseudo-code in audit_phase3.py:
B2 (Re g on the axis) and B6 (the one-sided three-point stencil).  Both are now computed, not asserted."""
from pathlib import Path
import ast

P = Path('/home/user/le/Phase_03_Mathematical_Audit/verification/audit_phase3.py')
t = P.read_text()

# ------------------------------------------------------------------ B2
i0 = t.index("x = sp.symbols('x', nonnegative=True)")
i1 = t.index("rhot = (1 + 2 * x)")
B2 = (
    "x = sp.symbols('x', nonnegative=True)          # x = (omega tau)^2\n"
    "gcv = sp.simplify(sp.re(CV.subs(s_, sp.I * sp.sqrt(x) / tau_)))\n"
    "gmc = sp.simplify(sp.re(MCV3.subs(s_, sp.I * sp.sqrt(x) / tau_)))\n"
    "ok_cv = bool(sp.simplify(gcv - (1 + x) ** (-1)) == 0)\n"
    "ok_mc = bool(sp.simplify(gmc - (1 + sp.Rational(3, 2) * x) / (1 + 4 * x)) == 0)\n"
    "chk(\"B2\", \"Re g on the axis is strictly positive for both kernels (companion 2.1)\",\n"
    "    ok_cv and ok_mc,\n"
    "    \"CV: Re g = 1/(1+x); MCV3: Re g = %s, both > 0 for x >= 0, so neither kernel puts energy on the wrong \"\n"
    "    \"side of the axis at leading order\" % sp.simplify(gmc))\n"
)
t = t[:i0] + B2 + t[i1:]

# ------------------------------------------------------------------ B6
i0 = t.index("xs = sp.symbols")
i1 = t.index("# ---------------------------------------------------------------- C.")
B6 = (
    "u_, h_ = sp.Symbol('u'), sp.Symbol('h', positive=True)\n"
    "c0, c1, c2 = sp.symbols('c0 c1 c2')\n"
    "sol = sp.solve([sp.Eq(c0 + c1 + c2, 0), sp.Eq(c1 * h_ + c2 * 2 * h_, 1),\n"
    "                sp.Eq(c1 * h_ ** 2 + c2 * (2 * h_) ** 2, 0)], [c0, c1, c2], dict=True)[0]\n"
    "exact_lin = sp.simplify((sol[c1] * h_ + sol[c2] * 2 * h_) / h_ - 1)\n"
    "exact_qua = sp.simplify((sol[c1] * h_ ** 2 + sol[c2] * (2 * h_) ** 2) / h_ - 0)\n"
    "err_cub = sp.simplify((sol[c1] * h_ ** 3 + sol[c2] * (2 * h_) ** 3) / h_ - 0)\n"
    "chk(\"B6\", \"the one-sided three-point metric derivative at chi = 0 and eta = 0 (Eqs. (49)-(50))\",\n"
    "    sp.simplify(sol[c0] + sp.Rational(3, 2)) == 0 and exact_lin == 0 and exact_qua == 0\n"
    "    and sp.simplify(err_cub + 2 * h_ ** 2) == 0,\n"
    "    \"the weights (%s, %s, %s)/h are the unique second-order one-sided set: exact on 1, u and u^2, and on u^3 \"\n"
    "    \"the error is -2 h^2 (magnitude) = (h^2/3) f-prime-prime-prime with f-prime-prime-prime = 6, i.e. the boundary rows of \"\n"
    "    \"the metric operator are O(h^2), not O(1)\"\n"
    "    % (sol[c0], sol[c1], sol[c2]))\n\n"
)
t = t[:i0] + B6 + t[i1:]
ast.parse(t)
P.write_text(t)
print("B2 and B6 now computed; file parses")
