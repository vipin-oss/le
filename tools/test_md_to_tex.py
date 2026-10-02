#!/usr/bin/env python3
"""test_md_to_tex.py — unit checks for the unicode -> LaTeX conversion in tools/md_to_tex.py.

No TeX engine is available here, so the conversion is pinned by expected-output tests: every
case below is a pattern that occurs in the manuscript and that a previous version got wrong.

Run:  python3 tools/test_md_to_tex.py     (exit 0 = all passed)
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('md_to_tex', os.path.join(HERE, 'md_to_tex.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

CASES = [
    # (input, expected output)
    ('x \u03b2-Ga\u2082O\u2083 y', 'x $\\beta$-Ga$_2$O$_3$ y'),
    ('t_w (t_th)', '$t_{w}$ ($t_{th}$)'),
    ('$t_{th}$ = 25.3 ps', '$t_{th}$ = 25.3 ps'),
    ('(T, $\\gamma$_B) = (20, 0.9)', '(T, $\\gamma_B$) = (20, 0.9)'),
    ('A_$\\varphi$', '$A_\\varphi$'),
    ('labels: $N_{r}\\times$N_$\\theta$', 'labels: $N_{r}\\times N_\\theta$'),
    ('$\\rhoc_{p}$', '$\\rhoc_{p}$'),
    ('3.959\u00d710^{\u22126} m\u00b2/s', '3.959$\\times 10^{-6}$ $m^{2}$/s'),
    ('\u03ba\u0304 = (det K)^{1/2}', '$\\bar{\\kappa}$ = (det $K)^{1/2}$'),
    ('\u03c3\u0302 = max', '$\\hat{\\sigma}$ = max'),
    ('H(s\u0304) = conj H(s)', 'H($\\bar{s}$) = conj H(s)'),
    ('a\u2013c plane', 'a--c plane'),
    ('0.7 \u00b5m', '0.7 $\\mu$m'),
    ('Lam\u00e9 constants', "Lam\\'e constants"),
    ('\u03c6 = 30\u00b0', '$\\varphi$ = 30$^{\\circ}$'),
    ('5\u201350 nm', '5--50 nm'),
    ('\u2264 6 t_th', '$\\leq$ 6 $t_{th}$'),
    ('MASTER_PROMPT', 'MASTER\\_PROMPT'),
    ('peak 0.854 MPa/K', 'peak 0.854 MPa/K'),
    ('the stress \u03c3_{\u03b8\u03b8}', 'the stress $\\sigma_{\\theta\\theta}$'),
    ('e^{\u2212\u03b3_{B}T}', '$e^{-\\gamma_{B}T}$'),
    ('\u03b5\u00b2 inertia', '$\\varepsilon^{2}$ inertia'),
    ('(\u201ccollapse\u201d)', "(``collapse'')"),
    ('F = \u222b r\u03b8 dr', 'F = $\\int$ r$\\theta$ dr'),
    ('\u03c6 = 0, 30, \u2026, 150\u00b0', '$\\varphi$ = 0, 30, $\\ldots$, 150$^{\\circ}$'),
    ('50\\% and 28.7\\%', '50\\% and 28.7\\%'),
]


def main():
    bad = 0
    for src, want in CASES:
        got = m.u2l(src)
        ok = (got == want)
        bad += (not ok)
        print('%-4s %-42s -> %s' % ('ok' if ok else 'FAIL', src.replace('\n', ' '), got))
        if not ok:
            print('     expected: %s' % want)
    print('RESULT:', 'ALL %d CONVERSION TESTS PASSED' % len(CASES) if not bad
          else '%d CONVERSION TEST(S) FAILED' % bad)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
