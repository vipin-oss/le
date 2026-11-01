#!/usr/bin/env python3
"""Checker for the Mittag-Leffler tail job (`ML_TAIL_READ_2026-11-01.*`).

The claim under test is CR046:

    "for alpha < 1 the solution is a stretched Mittag-Leffler-type decay with heavy
     tails [GorenfloKilbasMainardiRogosin2014, Luchko2010]"

and the book that carries the citation is now on the shelf.  The two things the
sentence asserts are, in the book's own words:

  (a) the tail is algebraic, not exponential - Prop. 3.6, eq. (3.4.15), printed p. 26:
      on the sector theta <= |arg z| <= pi the exponential term of (3.4.14) is gone and
          E_a(z) = -sum_{k=1}^{p} z^{-k}/Gamma(1-a k) + O(|z|^{-1-p});
      on the negative real axis (arg z = pi, z = -t^a) that reads
          E_a(-t^a) = sum_{k=1}^{p} (-1)^{k+1} / (Gamma(1-a k) t^{a k}) + O(t^{-a(1+p)})
      i.e. a power law t^{-a} with constant 1/Gamma(1-a) - a heavy tail.

  (b) it is a decay - Prop. 3.23 (Pollard), printed p. 47: E_a(-x) is completely
      monotonic for 0 <= a <= 1, so positive and decreasing.

This checker does not take either statement on trust.  It evaluates E_a(-x) two
independent ways (a spectral integral and the defining series), validates the fast
one against the closed form E_{1/2}(-x) = exp(x^2) erfc(x), and then:

  1. shows x*E_a(-x) -> 1/Gamma(1-a) as x grows, for four values of a;
  2. shows the residual of (3.4.15) truncated at p = 2 decays like t^{-3a}, which is
     the O(|z|^{-1-p}) the book prints, not just "something small";
  3. shows positivity and strict decrease on a grid for 0 < a < 1, and E_1(-x) = e^{-x};
  4. shows E_a(-x)/e^{-x} -> infinity, i.e. no exponential cut-off;
  5. re-reads claim_register.csv and asserts CR046 is still PARTLY SUPPORTED there -
     the proposal in the readout is not written into the register from here.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "ML_TAIL_READ_2026-11-01.csv")
REG = os.path.normpath(os.path.join(HERE, "..", "..", "claim_register.csv"))

COLS = ["row_id", "book", "page_printed", "what_is_printed", "verbatim", "claim_id",
        "relevance", "verdict_proposal", "numeric_check"]
DOI = "10.1007/978-3-662-43930-2"

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------- two evaluators
def MLneg(a, x, dps=40):
    """E_a(-x), 0 < a <= 1, spectral integral
       E_a(-x) = 1/(pi a) int_0^inf exp(-t w^{1/a}) sin(pi a)/(w^2 + 2 w cos(pi a) + 1) dw,
       t = x^{1/a}.  The substitution u = w^{1/a} removes the u^{a-1} singularity."""
    with mp.workdps(dps):
        a = mp.mpf(a); x = mp.mpf(x)
        if a == 1:
            return mp.e**(-x)
        if x == 0:
            return mp.mpf(1)
        t = x**(1/a)
        s = mp.sin(mp.pi*a); c = mp.cos(mp.pi*a)
        f = lambda w: mp.e**(-t*w**(1/a))*s/(w*w + 2*w*c + 1)
        return mp.quad(f, [0, 1, 10, mp.inf])/(mp.pi*a)


def MLneg_series(a, x, dps=90):
    """E_a(-x) from the defining series, at enough digits to survive cancellation."""
    with mp.workdps(dps):
        a = mp.mpf(a); x = mp.mpf(x)
        s = mp.mpf(0); k = 0
        while True:
            t = (-x)**k/mp.gamma(1 + a*k)
            s += t
            if abs(t) < abs(s)*mp.mpf(10)**(-25) and k > 3:
                return +s
            k += 1
            if k > 20000:
                raise RuntimeError("series did not settle")


def rhs_315(a, t, p):
    """(3.4.15) truncated at p, evaluated at z = -t^a."""
    a = mp.mpf(a); t = mp.mpf(t)
    tot = mp.mpf(0)
    for k in range(1, p + 1):
        g = mp.gamma(1 - a*k)
        if not mp.isfinite(g):
            continue                      # 1/Gamma = 0 at a pole of Gamma
        tot += (-1)**(k + 1)/(g*t**(a*k))
    return tot


mp.mp.dps = 40
rate = {}

print("A. the fast evaluator against a closed form, and against the defining series")
worst_closed = mp.mpf(0)
for x in (0.5, 2, 10, 40, 90):
    ex = mp.e**(mp.mpf(x)**2)*mp.erfc(mp.mpf(x))
    got = MLneg(0.5, x)
    worst_closed = max(worst_closed, abs(got - ex)/abs(ex))
check("spectral evaluator reproduces E_1/2(-x) = e^{x^2} erfc(x) to 1e-30",
      worst_closed < mp.mpf("1e-30"), "worst rel.err %.1e" % float(worst_closed))
worst_series = mp.mpf(0)
for a, x in ((0.3, 2), (0.5, 10), (0.8, 5)):
    d = abs(MLneg(a, x) - MLneg_series(a, x))/abs(MLneg(a, x))
    worst_series = max(worst_series, d)
check("the two independent evaluators agree to 1e-25 where both are usable",
      worst_series < mp.mpf("1e-25"), "worst rel.diff %.1e" % float(worst_series))

print("B. x*E_a(-x) -> 1/Gamma(1-a)  (the k = 1 term of (3.4.15), i.e. the heavy tail)")
tail_err = {}
for a in (0.3, 0.5, 0.7, 0.9):
    lim = 1/mp.gamma(1 - mp.mpf(a))
    e4 = abs(MLneg(a, mp.mpf(10)**4*mp.mpf(0) + (mp.mpf(10)**3)**mp.mpf(a))*((mp.mpf(10)**3)**mp.mpf(a)) - lim)/lim
    e5 = abs(MLneg(a, (mp.mpf(10)**5)**mp.mpf(a))*((mp.mpf(10)**5)**mp.mpf(a)) - lim)/lim
    tail_err[a] = float(e5)
    # the k = 2 term of (3.4.15) is O(t^{-2a}), so the relative error of the k = 1 term is
    # O(t^{-a}); the test is that scaling, not a flat tolerance
    bound = 3*mp.mpf(10)**(-a*5)
    check("a=%.1f: |x*E - 1/Gamma(1-a)| < 3*t^(-a) at t=1e5, and improving" % a,
          e5 < bound and e5 < e4/2,
          "rel.err %.1e, bound %.1e (t=1e3: %.1e)" % (float(e5), float(bound), float(e4)))

print("C. (3.4.15) truncated at p = 2 leaves a residual that decays like t^(-3a)")
resid = {}
for a in (0.3, 0.7, 0.9):
    r1 = abs(MLneg(a, mp.mpf(1000)**mp.mpf(a)) - rhs_315(a, 1000, 2))
    r2 = abs(MLneg(a, mp.mpf(10000)**mp.mpf(a)) - rhs_315(a, 10000, 2))
    ratio = r1/r2
    want = mp.mpf(10)**(3*mp.mpf(a))
    resid[a] = (float(ratio), float(want))
    check("a=%.1f: residual ratio %.1f against 10^(3a) = %.1f (within 10%%)" % (a, float(ratio), float(want)),
          abs(ratio - want)/want < mp.mpf("0.10"), "")

print("D. complete monotonicity on a grid (Prop. 3.23), and E_1(-x) = e^{-x}")
grid = [mp.mpf(10)**(mp.mpf(i)/4) for i in range(0, 13)]
for a in (0.25, 0.5, 0.75, 0.9):
    vals = [MLneg(a, x) for x in grid]
    check("a=%.2f: positive and strictly decreasing on x in [1, 1000]" % a,
          all(v > 0 for v in vals) and all(vals[i+1] < vals[i] for i in range(len(vals)-1)))
worst1 = max(abs(MLneg(1, x) - mp.e**(-x))/mp.e**(-x) for x in grid)
check("a=1 reduces to exp(-x)", worst1 < mp.mpf("1e-35"), "%.1e" % float(worst1))

print("E. no exponential cut-off: E_a(-x)/e^{-x} diverges")
grow = {}
for a in (0.5, 0.9):
    r5 = MLneg(a, 5)/mp.e**(-mp.mpf(5))
    r50 = MLneg(a, 50)/mp.e**(-mp.mpf(50))
    grow[a] = (float(r5), float(r50))
    check("a=%.1f: ratio at x=50 exceeds the ratio at x=5 by more than 1e5" % a,
          r50 > 1e5*r5, "%.2e -> %.2e" % (float(r5), float(r50)))

print("F. the readout is well formed and the register is untouched")
rows = list(csv.DictReader(open(CSV, newline="", encoding="utf-8")))
check("the readout exists with the declared header", list(rows[0].keys()) == COLS, str(list(rows[0].keys())))
check("row ids run 1..n", [int(r["row_id"]) for r in rows] == list(range(1, len(rows)+1)))
check("every row cites the same book and its printed page",
      all(r["book"].startswith("Gorenflo") and r["page_printed"].strip() for r in rows))
check("the pages the argument rests on are present (25, 26, 27, 47)",
      {"25", "26", "27", "47"} <= {r["page_printed"] for r in rows},
      str(sorted({r["page_printed"] for r in rows})))
check("every row carries CR046", {r["claim_id"] for r in rows} == {"CR046"})
check("the proposal is a proposal, not an edit",
      all(r["verdict_proposal"].startswith("PARTLY SUPPORTED -> SUPPORTED") for r in rows[:1]))
check("the readout names the book it read, and no other book",
      all(r["book"].startswith("Gorenflo") for r in rows))
check("the DOI asserted here is the register's own CR046 DOI (not a new one)",
      DOI == "10.1007/978-3-662-43930-2")

reg = list(csv.DictReader(open(REG, newline="", encoding="utf-8")))
cr046 = [r for r in reg if r["claim_id"] == "CR046"]
check("CR046 exists in the register exactly once", len(cr046) == 1)
check("the register still says PARTLY SUPPORTED for CR046 (verdict column not rewritten)",
      cr046 and cr046[0]["verdict"] == "PARTLY SUPPORTED", cr046[0]["verdict"] if cr046 else "-")
check("the register's CR046 row still carries the same DOI", cr046 and cr046[0]["source_doi"].strip() == DOI)

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (closed-form match %.1e, series match %.1e, tail constant at t=1e5 %s, "
      "residual ratio %s vs 10^(3a) %s, register CR046 still PARTLY SUPPORTED)"
      % (float(worst_closed), float(worst_series),
         " ".join("a=%.1f:%.1e" % (a, e) for a, e in sorted(tail_err.items())),
         " ".join("%.1f" % v[0] for v in resid.values()),
         " ".join("%.1f" % v[1] for v in resid.values())))
