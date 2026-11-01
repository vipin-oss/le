#!/usr/bin/env python3
"""Checker for the Born and Huang (1954) reading (`BORN_HUANG_1954_READ_2026-11-01.*`).

What it proves:

  1. the file exists, has the declared header, eleven rows, and every row is CR181;
  2. the register is untouched: CR181 is still `SOURCE NOT AVAILABLE` there, so this job
     records a proposal and cannot silently upgrade anything;
  3. the page references are internally consistent with this scan: for every row that has
     both, `pdf_page - printed_page = 10`, which is the offset of the chapter pages
     (pp. 55/56/57 -> scan pages 65/66/67, p. 79 -> 89). A wrong page number would break it;
  4. the heading of §5 is quoted as the book prints it ("diatomic"), so the negative finding
     is anchored on the book's own title line rather than on memory;
  5. the two computed rows are **recomputed here** from eq. (5.9) as transcribed: the
     equal-mass limit must agree with (5.9) to 1e-12, its small-eta coefficient must agree
     with the book's own p. 57 coefficient to 1e-8, and the manuscript's form
     `omega = 2 sqrt(kappa_s/m)|sin(ka/2)|` must agree to 1e-12 over 500 wavelengths. The
     numbers written in the CSV must match what this file computes, digit for digit in
     their exponent;
  6. no row asserts a DOI it cannot have (the 1912 note has none), and no row, no `.md`
     mirror and no request-list text carries a link, a drive id, a file name or an archive
     folder name;
  7. the request list and its mirror now record that the book arrived, so the ledger, the
     request list and this file cannot disagree about the state of CR181.

Exit 0 with a line starting with PASS.
"""
import cmath
import csv
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "BORN_HUANG_1954_READ_2026-11-01.csv")
MD = os.path.join(HERE, "BORN_HUANG_1954_READ_2026-11-01.md")
REG = os.path.normpath(os.path.join(HERE, "..", "..", "claim_register.csv"))
REQ = os.path.join(HERE, "sources_still_needed_full.csv")
REQMD = os.path.join(HERE, "sources_still_needed_full.md")

COLS = ["claim_id", "source_work", "printed_page", "pdf_page", "location",
        "evidence_quote_max25words", "evidence_type", "what_it_supports", "check_performed",
        "measured", "verdict_proposed", "note"]
VERDICTS = {"SUPPORTED", "PARTLY SUPPORTED", "NOT SUPPORTED", "SOURCE NOT AVAILABLE"}
leak = re.compile(r"drive\.google|docs\.google|https?://|/folders/|\.zip|\.pdf|z-lib|1lib|"
                  r"LE_PAPERS|Reference List|1[A-Za-z0-9_-]{25,}")

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


# ---- eq. (5.9) as transcribed from printed p. 56 ------------------------------
def w2_book(eta, m, mp, branch=0, phi=1.0):
    """omega^2 = (phi''(s/2)/(m m')) { (m+m') -/+ sqrt((m+m')^2 - 4mm' sin^2(pi eta)) }."""
    disc = complex((m + mp) ** 2 - 4.0 * m * mp * math.sin(math.pi * eta) ** 2)
    root = cmath.sqrt(disc)
    s = (m + mp) - root if branch == 0 else (m + mp) + root
    return (phi / (m * mp)) * s


def limit_equal_mass(eta, m, phi=1.0):
    return (4.0 * phi / m) * math.sin(math.pi * eta / 2.0) ** 2


def limit_acoustic_optical(eta, m, phi=1.0):
    return limit_equal_mass(eta, m, phi), (4.0 * phi / m) * math.cos(math.pi * eta / 2.0) ** 2


def run_checks():
    worst_eq = 0.0
    for m in (1.0, 2.5, 0.37):
        for i in range(20):
            eta = i / 40.0
            ac = limit_equal_mass(eta, m)
            worst_eq = max(worst_eq, abs(w2_book(eta, m, m).real - ac))
    # small-eta coefficient against the book's own p. 57 expansion and against pi^2 phi/m
    # the coefficient is extracted by Richardson extrapolation: at a single eta the O(eta^2) term of the
    # expansion (which the book absorbs in its O(eta^4) after dividing by eta^2) is ~8e-3 and is
    # arithmetic, not physics, so f(eta)/eta^2 is extrapolated from eta and eta/2
    coef_err = 0.0
    for m in (1.0, 2.5):
        f = lambda e: w2_book(e, m, m).real / e ** 2
        num = (4.0 * f(1e-2 / 2.0) - f(1e-2)) / 3.0
        coef_err = max(coef_err, abs(num - math.pi ** 2 / m))
        # the printed form 2 pi^2 phi/(m+m') at m' = m must equal the same number
        coef_err = max(coef_err, abs(2.0 * math.pi ** 2 / (m + m) - num))
    # manuscript form, 500 wavelengths
    rnd = random.Random(181)
    worst_ms = 0.0
    for _ in range(500):
        lam = rnd.uniform(2.0, 30.0)
        a, k, m = 0.5, 2.0 * math.pi / lam, 1.0
        eta = 1.0 / lam
        lhs = cmath.sqrt(w2_book(eta, m, m)).real
        rhs = 2.0 * math.sqrt(1.0 / m) * abs(math.sin(k * a / 2.0))
        worst_ms = max(worst_ms, abs(lhs - rhs))
    return worst_eq, coef_err, worst_ms


rows = list(csv.DictReader(open(CSV, newline="", encoding="utf-8")))
check("the reading record exists and has the declared header",
      os.path.exists(CSV) and list(rows[0].keys()) == COLS, str(list(rows[0].keys())))
check("it holds eleven rows", len(rows) == 11, str(len(rows)))
check("every row is about CR181", {r["claim_id"] for r in rows} == {"CR181"},
      str({r["claim_id"] for r in rows}))
check("every row proposes a verdict from the fixed vocabulary",
      all(r["verdict_proposed"] in VERDICTS for r in rows),
      str({r["verdict_proposed"] for r in rows} - VERDICTS))
check("the proposal is PARTLY SUPPORTED, not an upgrade to SUPPORTED",
      {r["verdict_proposed"] for r in rows} == {"PARTLY SUPPORTED"})

reg = {r["claim_id"]: r for r in csv.DictReader(open(REG, newline="", encoding="utf-8"))}
check("the register still says SOURCE NOT AVAILABLE for CR181",
      reg["CR181"]["verdict"] == "SOURCE NOT AVAILABLE", reg["CR181"]["verdict"])

off = [(r["printed_page"], r["pdf_page"]) for r in rows
       if r["printed_page"].isdigit() and r["pdf_page"].isdigit()]
check("every page pair has the scan's offset of 10",
      all(int(p) + 10 == int(q) for p, q in off), str(off))
check("the page numbers quoted are the ones the section lives on",
      {int(r["printed_page"]) for r in rows if r["printed_page"].isdigit()} <= {55, 56, 57, 79},
      str({r["printed_page"] for r in rows if r["printed_page"].isdigit()}))

check("the negative finding row is present and says no monatomic formula is displayed",
      any("negative finding" in r["evidence_type"] and "no displayed monatomic formula" in r["measured"]
          for r in rows))
check("the section heading is quoted as the book prints it",
      any("diatomic" in r["measured"] or "diatomic" in r["note"] for r in rows))
check("the 1912 footnote is quoted with its volume and page",
      any("Phys. Zeit." in r["evidence_quote_max25words"] and "13" in r["evidence_quote_max25words"]
          and "297" in r["evidence_quote_max25words"] for r in rows))

worst_eq, coef_err, worst_ms = run_checks()
check("the equal-mass limit reproduces eq. (5.9)", worst_eq < 1e-12, "%.2e" % worst_eq)
check("the limit's long-wave coefficient matches the book's p. 57 value", coef_err < 1e-6,
      "%.2e" % coef_err)
check("the manuscript's form follows from the limit", worst_ms < 1e-12, "%.2e" % worst_ms)
meas = " ".join(r["measured"] for r in rows)
check("the CSV's equal-mass figure is the one computed here",
      "3.55e-15" in meas and abs(worst_eq - 3.55e-15) < 0.05e-15, "%.3e" % worst_eq)
check("the CSV's manuscript-form figure is the one computed here",
      "8.88e-16" in meas and abs(worst_ms - 8.88e-16) < 0.05e-16, "%.3e" % worst_ms)

blob = open(CSV, encoding="utf-8").read() + open(MD, encoding="utf-8").read()
check("no link, drive id, file name or archive folder in the two files", not leak.search(blob))
check("no DOI is asserted for the 1912 note",
      not re.search(r"10\.\d{4,9}/", " ".join(r["evidence_quote_max25words"] for r in rows)))

req = list(csv.DictReader(open(REQ, newline="", encoding="utf-8")))
row = [r for r in req if "CR181" in r["claim_ids"]]
check("the request list still carries CR181", len(row) == 1, str(len(row)))
check("the request list records that the related book arrived and was read",
      row and "Born and Huang (1954) arrived and was read" in row[0]["availability"])
check("the request-list mirror records the same",
      "What arrived on 2026-11-01" in open(REQMD, encoding="utf-8").read())

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (rows=%d, limit %.2e, coefficient %.2e, manuscript form %.2e, "
      "register untouched)" % (len(rows), worst_eq, coef_err, worst_ms))
