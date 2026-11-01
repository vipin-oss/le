#!/usr/bin/env python3
"""Checks BK-15: the multifield invariant now exists, it passes, and the atlas says so.

Recomputes every number in bench_multifield_results.csv from scratch (the file is never
trusted as evidence), then checks that the six multifield atlas cases - AT-04, AT-05, AT-06,
AT-09, AT-13, AT-40 - have coverage = yes with an invariant that names the source, and that
coverage has moved to 40 full / 0 partial / 0 none while the case-level result count stays 0.
"""
import csv
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
fails = []


def check(what, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + what + (" [%s]" % detail if detail and not ok else ""))
    if not ok:
        fails.append(what)


def rows(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))


res = {r["invariant"]: r for r in rows(os.path.join(HERE, "bench_multifield_results.csv"))}
cov = rows(os.path.join(HERE, "atlas_case_coverage.csv"))
src = open(os.path.join(HERE, "bench_multifield.py"), encoding="utf-8").read()

check("the result file carries invariants I1..I6",
      sorted(res) == ["I1", "I2", "I3", "I4", "I5", "I6"], str(sorted(res)))
check("every invariant passes", all(r["verdict"] == "PASS" for r in res.values()),
      str([k for k, r in res.items() if r["verdict"] != "PASS"]))
check("the source names the printed equations (5.11.4)-(5.11.6) and the pages",
      "(5.11.4)" in src and "(5.11.5)" in src and "(5.11.6)" in src and "pp. 165-166" in src)
check("the source quotes the book and the section",
      "Eringen" in src and "Maugin" in src and "5.11" in src)

# ---- independent recomputation --------------------------------------------------------
VOIGT = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
C = np.array([[2.71e11, 0.91e11, 0.83e11, 0, 0, 0],
              [0.91e11, 2.71e11, 0.83e11, 0, 0, 0],
              [0.83e11, 0.83e11, 2.12e11, 0, 0, 0],
              [0, 0, 0, 0.55e11, 0, 0],
              [0, 0, 0, 0, 0.55e11, 0],
              [0, 0, 0, 0, 0, 0.90e11]], dtype=float)
e = np.zeros((3, 6)); e[0, 4] = 0.05; e[1, 3] = 0.05
q = np.zeros((3, 6)); q[0, 4] = 0.30; q[1, 3] = 0.30
chi = np.diag([1.2e-8, 1.2e-8, 1.4e-8])
mu = np.diag([3.0e-4, 3.0e-4, 3.6e-4])
lam = np.array([[0, 0, 1e-6], [0, 0, 0], [1e-6, 0, 0]], dtype=float)

W = np.zeros((12, 12))
W[:6, :6] = C
W[:6, 6:9] = -e.T; W[6:9, :6] = -e
W[:6, 9:] = -q.T;  W[9:, :6] = -q
W[6:9, 6:9] = chi; W[9:, 9:] = mu
W[6:9, 9:] = lam;  W[9:, 6:9] = lam.T
check("I1 recomputed: the Hessian is symmetric to the last bit",
      float(np.max(np.abs(W - W.T))) < 1e-3, "%.3e" % float(np.max(np.abs(W - W.T))))
d = np.sqrt(np.diag(W))
Wn = (W/d[:, None])/d[None, :]
check("I2 recomputed: the scaled Hessian is positive definite",
      float(np.linalg.eigvalsh(0.5*(Wn + Wn.T)).min()) > 0,
      "%.6e" % float(np.linalg.eigvalsh(0.5*(Wn + Wn.T)).min()))

K = np.hstack([e.T, q.T])
D = np.block([[chi, lam], [lam.T, mu]])
Cs = C + K @ np.linalg.solve(D, K.T)
dC = Cs - C
check("I3 recomputed: C* - C is PSD and genuinely non-zero",
      float(np.linalg.eigvalsh(0.5*(dC + dC.T)).min()) > -1e-3 and dC.max() > 1e4,
      "%.3e / %.3e" % (float(np.linalg.eigvalsh(0.5*(dC + dC.T)).min()), float(dC.max())))


def tens(M6):
    T = np.zeros((3, 3, 3, 3))
    for a, (i, j) in enumerate(VOIGT):
        for b, (k, l) in enumerate(VOIGT):
            for ii, jj in {(i, j), (j, i)}:
                for kk, ll in {(k, l), (l, k)}:
                    T[ii, jj, kk, ll] = M6[a, b]
    return T


rng = np.random.default_rng(15)
worst = 1e9
for _ in range(48):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    lb = np.linalg.eigvalsh(0.5*(np.einsum("ijkl,j,l->ik", tens(C), n, n) +
                                np.einsum("ijkl,j,l->ki", tens(C), n, n)))
    lc = np.linalg.eigvalsh(0.5*(np.einsum("ijkl,j,l->ik", tens(Cs), n, n) +
                                np.einsum("ijkl,j,l->ki", tens(Cs), n, n)))
    worst = min(worst, float(np.min(lc - lb)))
check("I4 recomputed: coupled branches are never below the bare ones", worst > -1e-3,
      "%.6e" % worst)

e15 = np.zeros((3, 6)); e15[0, 4] = 0.05
C5 = C + np.hstack([e15.T, np.zeros((6, 3))]) @ np.linalg.solve(
    np.block([[chi, np.zeros((3, 3))], [np.zeros((3, 3)), mu]]),
    np.vstack([e15, np.zeros((3, 6))]))
closed = C[4, 4] + 0.05**2/1.2e-8
check("I5 recomputed: the piezo closed form C44 + e15^2/chi11 is reproduced",
      abs(C5[4, 4] - closed)/closed < 1e-12, "%.3e" % (abs(C5[4, 4] - closed)/closed))

# ---- the atlas rows -------------------------------------------------------------------
six = {"AT-04", "AT-05", "AT-06", "AT-09", "AT-13", "AT-40"}
by = {r["problem_id"]: r for r in cov}
check("the six multifield cases are present", six <= set(by), str(sorted(six - set(by))))
check("all six now carry coverage = yes", all(by[c]["coverage"] == "yes" for c in six),
      str([c for c in six if by[c]["coverage"] != "yes"]))
check("all six name BK-15 as the invariant they gained",
      all("BK-15" in by[c]["missing_invariant"] for c in six),
      str([c for c in six if "BK-15" not in by[c]["missing_invariant"]]))
check("no row still reads 'no coupled-field invariant exists'",
      not any("no coupled-field invariant exists" in r["missing_invariant"] for r in cov))
check("the six remain without a case-level result, and say why",
      all(by[c]["case_level_result"] == "no" and by[c]["why_no_case_result"].strip()
          for c in six))
check("the six are multifield", all(by[c]["wave_family"] == "multifield" for c in six))
cnt = {}
for r in cov:
    cnt[r["coverage"]] = cnt.get(r["coverage"], 0) + 1
check("coverage split is 40 full / 0 partial / 0 none",
      cnt.get("yes", 0) == 40 and cnt.get("partial", 0) == 0 and cnt.get("no", 0) == 0,
      str(cnt))
check("the case-level result count is still zero",
      not any(r["case_level_result"] == "yes" for r in cov))

print()
if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (BK-15: 6 invariants recomputed, atlas 40/0/0)")
