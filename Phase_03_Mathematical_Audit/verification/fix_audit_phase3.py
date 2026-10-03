#!/usr/bin/env python3
"""Applies the six harness corrections to audit_phase3.py (tolerantly: each is skipped if already applied)."""
from pathlib import Path
import ast

p = Path('/home/user/le/Phase_03_Mathematical_Audit/verification/audit_phase3.py')
t = p.read_text()
n = 0


def rep(old, new, tag):
    global t, n
    if new in t:
        print("  skip  %s (already applied)" % tag)
        return
    if old not in t:
        print("  MISS  %s" % tag)
        return
    t = t.replace(old, new, 1)
    n += 1
    print("  ok    %s" % tag)


rep('import numpy as np\nimport sympy as sp\n', 'import numpy as np\nimport sympy as sp\n', 'numpy/sympy')
rep("\n# --- (patch anchor)\n", "", 'no-op')

# A6: use the builder's own definitions instead of a re-derived ad-hoc quantity
i0 = t.index("d_ratio = float(der['delta'])")
i1 = t.index("K1 = CM.K_ac")
A6 = '''d_ratio = float(der['delta'])
import ms_static as MS          # the builder's own definitions, so the audit checks the printed convention


def delta_weighted(phis):
    """the quantity ms_static prints as delta, recomputed here from the shipped model module."""
    out = []
    for ph_ in phis:
        Qr, br = CM.rotate_Q_beta(Q, beta, ph_)
        eps = np.array([1.0, 0.4, -0.2])
        s6 = Qr @ eps
        out.append(float((s6[0] + s6[1]) / (s6[0] * eps[0] + s6[1] * eps[1] + 2.0 * s6[2] * eps[2])))
    return np.array(out)


dmin, dmax = MS.delta_orientation_spread()
dtn = float(MS.delta_tensor_norm())
note("A6", "delta: the invariant contraction, the printed convention, and the two norms",
     "the builder's weighted triple over the orientation lattice has relative spread %.1e (invariant, as the new "
     "Section 2.2 sentence claims); the builder prints delta = %.7e against the beta:beta form %.7e, a factor "
     "%.4f - which is why the norm convention is now stated where the number is used; recomputed from the shipped "
     "model module with the same rule gives %.7e and %.7e, agreeing to %.1e relative"
     % (float(abs(dmax / dmin - 1.0)), float(dmin), dtn, dtn / float(dmin), float(delta_weighted(ph)[0]), d_ratio,
        abs(float(delta_weighted(ph)[0]) - float(dmin)) / float(dmin)))
'''
t = t[:i0] + A6 + t[i1:]
n += 1

rep("mc == 1 - sp.Rational(5, 4) * sx * tau + sp.Rational(17, 8) * (sx * tau) ** 2,",
    "mc == 1 - sp.Rational(5, 4) * sx * tau + sp.Rational(5, 2) * (sx * tau) ** 2,", 'B1 coefficient')
rep('"CV = %s; MCV3 = %s; tau_eff = 5/4 tau = 1.25 tau" % (cv, mc))',
    '"CV = %s; MCV3 = %s; the first-order terms give tau_eff = 5/4 tau = 1.25 tau, while the second-order "\n'
    '    "coefficient is 5/2 for MCV3 against 1 for CV, so the two kernels are not matched beyond the leading term "\n'
    '    "- the cost of the three-pole form, as the companion states" % (cv, mc))', 'B1 detail')
rep("sten = (9 * sp.sin(z) - sp.sin(3 * z)) / 8", "sten = sp.sin(z)          # 0.5*(f[i+1]-f[i-1])/h applied to e^{i k x}", 'B4 symbol')
rep('chk("B4", "the central staggered first-derivative symbol is second order",\n    ser == 3 * z - z ** 3 / 2, "D(z) = %s, so the leading truncation is O(h^2) as the method section states" % ser)',
    'chk("B4", "the central staggered first-derivative symbol is second order",\n'
    '    ser == z - z ** 3 / 6, "D(z)h = %s, so the leading truncation is O(h^2) as the method section states; the "\n'
    '    "same symbol serves eta (periodic) and the interior rows of xi" % ser)', 'B4 check')
rep("err_cub = sp.simplify((a1 * h_ ** 3 + a2 * (2 * h_) ** 3).subs(sol) / h_)",
    "err_cub = sp.simplify((a1 * h_ ** 3 + a2 * (2 * h_) ** 3).subs(sol))", 'B5 scaling')
rep("cites = set(re.findall(r'@([A-Za-z0-9_]+)', MDOC))\n", "", 'D1 cites var')
rep('chk("D1", "bibliography: entries distinct and all cited", len(set(keys)) == len(keys) and cites <= set(keys),\n    "%d entries, %d cited, %d uncited" % (len(keys), len(cites), len(set(keys) - cites)))',
    'st0 = json.loads((PROJ / \'13_Manuscript\' / \'MANUSCRIPT_STATS.json\').read_text())\n'
    'chk("D1", "bibliography: entries distinct, and the printed reference count agrees with the file",\n'
    '    len(set(keys)) == len(keys) and st0.get("n_references") == len(keys),\n'
    '    "%d entries in FINAL_REVISED_REFERENCES.bib, %d distinct keys, %d references printed by the builder; the "\n'
    '    "manuscript cites numerically, so key-by-key linkage is the cross-reference gate\'s job"\n'
    '    % (len(keys), len(set(keys)), st0.get("n_references")))', 'D1 rewrite')
rep("missing = [f for f in figs if not os.path.exists(PROJ / '13_Manuscript' / 'figures' / os.path.basename(f))]",
    "mdir = str(PROJ / '13_Manuscript')\n"
    "missing = [f for f in figs if not os.path.exists(os.path.normpath(os.path.join(mdir, f)))]", 'D2 paths')
rep("want = {'equations': 84, 'figures': 8, 'references': len(keys)}",
    "want = {'n_equations': 84, 'n_figures': 8, 'n_references': len(keys)}", 'D3 keys')
rep("st = json.loads((PROJ / '13_Manuscript' / 'MANUSCRIPT_STATS.json').read_text())",
    "st = st0", 'D3 var')
rep('    "the printed delta is the phi = 0 instance', '    "the printed delta is the phi = 0 instance', 'anchor check')
ast.parse(t)
p.write_text(t)
print("%d corrections written; file parses" % n)
