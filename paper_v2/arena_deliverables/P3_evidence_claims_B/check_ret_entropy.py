#!/usr/bin/env python3
"""Checker for the RET entropy job (`RET_ENTROPY_READ_2026-11-01.*`).

CR127 says: "In extended irreversible thermodynamics ... the entropy depends also on the
heat flux q_i, which must enter the state space."  The book has now been read on printed
p. 24, where the claim is printed in words and in an equation - so the reading part is a
quotation, and this file does not try to dress it up as a numerical result.

What it does test is the *structure* of the printed entropy of eq. (3.29),

    s = (k/m) ln(T^(3/2)/rho) + varsigma - t_<ij>t_<ij>/(4 rho p^2 T) - q_i q_i/(5 p^2 T),

because that structure is what the claim leans on, and it is testable without fixing the
book's moment normalisation:

  1. the correction is QUADRATIC and NEGATIVE for every non-zero (t, q): entropy is
     maximal at equilibrium, which is what makes it an entropy at all;
  2. it is EVEN in q: reversing the heat flux must not change the entropy, and the
     printed formula has only q_i q_i in it;
  3. there is NO t-q CROSS TERM: the printed formula has none, and the Gaussian
     expectation of the bracket in (3.27) confirms that none can appear;
  4. the ratio of the q term to the t term is 4/5 for the printed coefficients - recorded
     as a *printed* number, not as a reproduced one, because a naive evaluation of (3.27)
     does not fix both coefficients without the book's normalisation of the moments. The
     readout says so; this checker asserts that the readout says so;
  5. claim_register.csv still has CR127 at SOURCE NOT AVAILABLE.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "RET_ENTROPY_READ_2026-11-01.csv")
MD = os.path.join(HERE, "RET_ENTROPY_READ_2026-11-01.md")
REG = os.path.normpath(os.path.join(HERE, "..", "..", "claim_register.csv"))

COLS = ["row_id", "book", "page_printed", "what_is_printed", "verbatim", "claim_id",
        "relevance", "verdict_proposal", "numeric_check"]
fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


# ------------------------------------------------------------------ the structure test
def entropy_correction(t, q, rho=mp.mpf("1.2"), p=mp.mpf("1.0"), T=mp.mpf("300"), m=mp.mpf("1"),
                       k=mp.mpf("1"), npts=24001):
    """-k/2 * int f_E delta^2 dc for the Grad bracket of (3.27), in the rest frame.

    `t` is taken diagonal and traceless (the only case needed here), so the printed
    delta_ij term is subtracted as the trace.

    The bracket is taken exactly as printed; nothing is fitted.  Only the *shape* of the
    result is used (sign, parity, absence of a cross term), never its absolute value.
    """
    t = mp.matrix(t); q = mp.matrix(q)
    c0 = mp.sqrt(k*T/m)

    def fE(x):
        return mp.e**(-x*x/2)

    def delta(c):
        cx, cy, cz = c[0], c[1], c[2]
        trq = sum(t[i] * ((m/(k*T))*c[i]*c[j]) for i in range(3) for j in range(3))
        trq -= sum(t[i] for i in range(3))
        s2 = cx*cx + cy*cy + cz*cz
        lq = sum(q[i]*c[i] for i in range(3))
        return -(1/(2*p))*trq - (m/(rho*k*T))*lq*(1 - (m/(5*k*T))*c0*c0*s2)

    # 3D Gaussian expectation by tensor-product Gauss-Hermite in units of c0
    xg, wg = [], []
    for i in range(-12, 13):
        xg.append(mp.mpf(i)/2)
        wg.append(mp.e**(-(mp.mpf(i)/2)**2/2))
    Z = sum(wg)
    tot = mp.mpf(0)
    for i in range(len(xg)):
        for j in range(len(xg)):
            for l in range(len(xg)):
                c = mp.matrix([xg[i]*c0, xg[j]*c0, xg[l]*c0])
                d = delta(c)
                tot += wg[i]*wg[j]*wg[l]*d*d
    tot /= Z**3
    return -(k/2)*(rho/m)*tot


mp.mp.dps = 30
zero3 = [mp.mpf(0)]*3
dev = [mp.mpf(1), mp.mpf(-1), mp.mpf(0)]          # a traceless diagonal stress
qn = [mp.mpf("0.3"), mp.mpf(0), mp.mpf(0)]        # a heat flux along x

base = entropy_correction(dev, zero3)
qq = entropy_correction(zero3, qn)
both = entropy_correction(dev, qn)
qm = entropy_correction(zero3, [-x for x in qn])

check("equilibrium has zero correction", abs(entropy_correction(zero3, zero3)) < mp.mpf("1e-40"))
check("the stress correction is negative", base < 0, "%.3e" % float(base))
check("the heat-flux correction is negative", qq < 0, "%.3e" % float(qq))
check("the correction is even in q: reversing the flux changes nothing",
      abs(qq - qm) <= abs(qq)*mp.mpf("1e-30"), "|diff| %.1e" % float(abs(qq-qm)))
check("no t-q cross term: the joint correction is the sum of the two",
      abs(both - (base + qq)) <= abs(base + qq)*mp.mpf("1e-25"),
      "|cross| %.1e" % float(abs(both - (base + qq))))

print("C-2. the printed coefficients say the q term is 4/5 of the t term; the readout must say this was not reproduced")
check("printed coefficient ratio is recorded as 4/5",
      abs(mp.mpf(1)/5/(mp.mpf(1)/4) - mp.mpf("0.8")) < mp.mpf("1e-30"))
md = open(MD, encoding="utf-8").read()
check("the readout states plainly that the coefficients are quoted, not reproduced",
      "not claimed as reproduced" in md and "normalisation" in md
      and "does **not** reproduce" in md)

print("D. the readout and the register")
rows = list(csv.DictReader(open(CSV, newline="", encoding="utf-8")))
check("header matches the declared schema", list(rows[0].keys()) == COLS)
check("row ids run 1..n", [int(r["row_id"]) for r in rows] == list(range(1, len(rows)+1)))
check("every row is the same book and the same printed page 24",
      {r["page_printed"] for r in rows} == {"24"}, str({r["page_printed"] for r in rows}))
check("every row carries CR127", {r["claim_id"] for r in rows} == {"CR127"})
check("the verbatim sentence that answers the claim is present",
      any("depends on t_<ij> and q_i" in r["verbatim"] for r in rows))
check("at least one row is a negative finding",
      any(r["what_is_printed"].startswith("NEGATIVE FINDING") for r in rows))

reg = list(csv.DictReader(open(REG, newline="", encoding="utf-8")))
cr = [r for r in reg if r["claim_id"] == "CR127"]
check("CR127 exists exactly once", len(cr) == 1)
check("the register still says SOURCE NOT AVAILABLE for CR127",
      cr and cr[0]["verdict"] == "SOURCE NOT AVAILABLE", cr[0]["verdict"] if cr else "-")

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (p.24 read; correction negative and even in q, cross term zero; "
      "coefficients quoted not reproduced; register CR127 still SOURCE NOT AVAILABLE)")
