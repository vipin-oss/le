#!/usr/bin/env python3
"""Validate the Task 5 benchmark layer (tolerances + per-problem map + results).

Checks, in order:
 1. bench_tolerances.csv: exactly the eight benchmark ids, unique, every one has a
    non-empty tolerance, a script and a reference type from the allowed set;
 2. bench_atlas_results.csv: same eight ids, all eight verdicts PASS, and each
    measured error within the tolerance recorded in bench_tolerances.csv;
 3. benchmark_map.csv: the same 40 problem ids as atlas_plan.csv, every referenced
    benchmark id exists, n_benchmarks equals the number of ids listed, and no row
    claims that the paper's own equation was read;
 4. coverage: every wave family in atlas_plan.csv appears in the map.

Prints one PASS line per group plus a final `PASS all checks (...)` and exits 0;
exits 1 with a FAIL line otherwise.  Standard library only.
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOL = os.path.join(HERE, "bench_tolerances.csv")
RES = os.path.join(HERE, "bench_atlas_results.csv")
MAP = os.path.join(HERE, "benchmark_map.csv")
PLAN = os.path.join(HERE, "atlas_plan.csv")
ALLOWED_REFTYPE = {"model structure (exact)", "closed form", "closed form (Zener)",
                   "closed form (exact)", "asymptotic law", "Lyapunov / Routh-Hurwitz"}
IDS = ["BK-%02d" % i for i in range(1, 9)]

errors = []


def fail(msg):
    errors.append(msg)


def load(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def nums(text):
    out = []
    for tok in text.replace(",", " ").replace("/", " ").split():
        try:
            out.append(float(tok))
        except ValueError:
            pass
    return out


def check_tolerances():
    rows = load(TOL)
    if [r["benchmark_id"] for r in rows] != IDS:
        fail("bench_tolerances.csv ids are %s, expected %s"
             % ([r["benchmark_id"] for r in rows], IDS))
    for r in rows:
        if not r["tolerance"].strip():
            fail("%s: empty tolerance" % r["benchmark_id"])
        if r["script"] != "bench_atlas.py":
            fail("%s: script is %r" % (r["benchmark_id"], r["script"]))
        if r["executable"] != "yes":
            fail("%s: not marked executable" % r["benchmark_id"])
        if r["reference_type"] not in ALLOWED_REFTYPE:
            fail("%s: reference type %r not in the allowed set"
                 % (r["benchmark_id"], r["reference_type"]))
        if not r["applies_to_families"].strip():
            fail("%s: no wave families listed" % r["benchmark_id"])
    print("PASS bench_tolerances.csv: %d benchmarks, tolerances and reference types ok"
          % len(rows))
    return {r["benchmark_id"]: r for r in rows}


def check_results(tol):
    rows = load(RES)
    if [r["benchmark_id"] for r in rows] != IDS:
        fail("bench_atlas_results.csv ids are %s, expected %s"
             % ([r["benchmark_id"] for r in rows], IDS))
    for r in rows:
        bid = r["benchmark_id"]
        if r["verdict"] != "PASS":
            fail("%s: verdict %s" % (bid, r["verdict"]))
        try:
            err = float(r["error"])
        except ValueError:
            fail("%s: error column is not a number (%r)" % (bid, r["error"]))
            continue
        t = nums(tol[bid]["tolerance"])
        limit = t[-1] if t else None
        if limit is None:
            fail("%s: tolerance has no numeric value" % bid)
        elif r["tolerance"].strip() == "exact":
            if err != 0.0:
                fail("%s: exact tolerance but error %r" % (bid, err))
        elif err > limit:
            fail("%s: error %.3e exceeds tolerance %.3e" % (bid, err, limit))
        if not math.isfinite(err):
            fail("%s: non-finite error" % bid)
    print("PASS bench_atlas_results.csv: %d runs, all within the recorded tolerance"
          % len(rows))
    return rows


def check_map(tol, res):
    m = load(MAP)
    plan = load(PLAN)
    plan_ids = [r["problem_id"] for r in plan]
    map_ids = [r["problem_id"] for r in m]
    if map_ids != plan_ids:
        fail("benchmark_map.csv ids differ from atlas_plan.csv ids")
    if len(set(map_ids)) != len(map_ids):
        fail("benchmark_map.csv has duplicate problem ids")
    for r in m:
        ids = [x for x in r["benchmark_ids"].split(";") if x]
        for bid in ids:
            if bid not in tol:
                fail("%s: unknown benchmark id %r" % (r["problem_id"], bid))
        if int(r["n_benchmarks"]) != len(ids):
            fail("%s: n_benchmarks=%s but %d ids listed"
                 % (r["problem_id"], r["n_benchmarks"], len(ids)))
        if r["paper_equation_read"] != "no" or r["paper_parameters_read"] != "no":
            fail("%s: claims a paper equation/parameter read that was not done"
                 % r["problem_id"])
        if not r["what_is_still_missing"].strip():
            fail("%s: empty 'what_is_still_missing'" % r["problem_id"])
        for bid in ids:
            fam = r["wave_family"]
            if fam not in tol[bid]["applies_to_families"].split("; "):
                fail("%s: %s is not listed as applying to family %r"
                     % (r["problem_id"], bid, fam))
    print("PASS benchmark_map.csv: %d problems, %d unique ids, every benchmark id resolves"
          % (len(m), len(set(map_ids))))
    return m, plan


def check_coverage(m, plan):
    fams = {r["wave_family"] for r in plan}
    seen = {r["wave_family"] for r in m}
    missing = fams - seen
    if missing:
        fail("wave families missing from the map: %s" % sorted(missing))
    used = set()
    for r in m:
        used.update(x for x in r["benchmark_ids"].split(";") if x)
    unused = [b for b in IDS if b not in used]
    if unused:
        fail("benchmarks not used by any problem: %s" % unused)
    print("PASS coverage: %d wave families, all 8 benchmarks used" % len(fams))


def main():
    tol = check_tolerances()
    res = check_results(tol)
    m, plan = check_map(tol, res)
    check_coverage(m, plan)
    if errors:
        for e in errors:
            print("FAIL " + e)
        print("FAIL %d check(s) failed" % len(errors))
        return 1
    print("PASS all checks (rows=%d, benchmarks=%d, families=%d)"
          % (len(m), len(IDS), len({r['wave_family'] for r in plan})))
    return 0


if __name__ == "__main__":
    sys.exit(main())
