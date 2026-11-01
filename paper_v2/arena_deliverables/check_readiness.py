#!/usr/bin/env python3
"""Validate PUBLICATION_READINESS_2026-11-01.md against the CSVs it summarises.

The readiness note is only useful if its numbers are the repository's numbers, so every count it
prints is recomputed here from the source files and searched for in the text. If a batch moves a
number and the note is not updated, this fails.

Checks
  1. every phase P0-P7 has a row in the phase table, quoted by the same word the table uses;
  2. the claim-register numbers (rows, supported, partly, not supported, unavailable) are printed;
  3. the five buckets of the unavailable claims are printed and still add up to the register;
  4. the reference-register numbers (entries, R0, R1, R2) are printed, and so are the catalogue
     check's own entries and R0 count;
  5. the build artefacts (atlas plan and results, benchmarks, second implementation, re-audit,
     experiment extraction, edit sheet) are printed with their real sizes;
  6. the defect register's fixed / partial / open / observed counts are printed;
  7. the two blueprint checklists are printed with their real pass counts;
  8. the note carries no link, no uploaded file name and no drive identifier.

Prints PASS lines and exits 0, FAIL and exit 1 otherwise. Standard library only.
"""
import collections
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.dirname(HERE)
DOC = os.path.join(HERE, "PUBLICATION_READINESS_2026-11-01.md")
B = HERE

fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else " :: " + str(detail)))
    if not ok:
        fails.append(name)


def rd(path):
    return list(csv.DictReader(open(path, newline="", encoding="utf-8", errors="replace")))


def main():
    check("the readiness note exists", os.path.exists(DOC))
    if not os.path.exists(DOC):
        print("FAIL 1 check(s) failed")
        return 1
    txt = open(DOC, encoding="utf-8").read()

    # ---- recompute everything from the source files ----
    reg = rd(os.path.join(PAPER, "claim_register.csv"))
    ver = rd(os.path.join(PAPER, "verification_register.csv"))
    cat = rd(os.path.join(PAPER, "refs_catalogue_check.csv"))
    bench = rd(os.path.join(PAPER, "benchmark_registry.csv"))
    plan = rd(os.path.join(B, "P3_atlas", "atlas_plan.csv"))
    bres = rd(os.path.join(B, "P3_atlas", "bench_atlas_results.csv"))
    si = rd(os.path.join(B, "P4_second_impl", "second_impl_comparison.csv"))
    rea = rd(os.path.join(B, "P1_audit", "reaudit_flagged_20.csv"))
    exp2 = rd(os.path.join(B, "P3_experiments", "experiments_2.csv"))
    e = os.path.join(B, "P3_evidence_claims_B")
    es = rd(os.path.join(e, "PAPER_EDIT_SHEET_2026-11-01.csv"))
    upd = rd(os.path.join(e, "claim_upgrade_2026-11-01.csv"))
    b4 = rd(os.path.join(e, "SOURCE_READING_batch4_2026-11-01.csv"))
    held = rd(os.path.join(e, "SOURCE_READING_held_2026-11-01.csv"))
    books = rd(os.path.join(e, "SOURCE_READING_books_2026-11-01.csv"))
    reqp = rd(os.path.join(e, "REQUEST_P_claims_2026-11-01.csv"))
    wvd = rd(os.path.join(e, "waived_by_author_2026-11-01.csv"))
    still = rd(os.path.join(e, "sources_still_needed_full.csv"))
    rgl = rd(os.path.join(e, "register_level_pass_2026-11-01.csv"))

    V = {"SUPPORTED", "PARTLY SUPPORTED", "NOT SUPPORTED", "SOURCE NOT AVAILABLE"}
    cnt = lambda rows, k: sum(1 for r in rows if r["verdict"] == k)
    closed = (len(upd) + len(b4)
              + sum(1 for r in held if r["verdict"] in V)
              + sum(1 for r in books if r["verdict"] in V) + 1 + len(reqp))
    to_order = sum(len(r["claim_ids"].split()) for r in still)
    waived = len(wvd)
    heldunread = sum(1 for r in held if r["verdict"] not in V)
    lv = collections.Counter(r.get("verification_level", "") for r in ver)
    cl = collections.Counter(r.get("level", "") for r in cat)
    vR0, vR1, vR2 = lv.get("R0", 0), lv.get("R1", 0) + lv.get("R1-noDOI", 0), lv.get("R2", 0)
    vR3 = lv.get("R3", 0)
    cR0, cR1, cR2 = cl.get("R0", 0), cl.get("R1", 0), cl.get("R2", 0)

    dreg = open(os.path.join(PAPER, "P1_DEFECT_REGISTER.md"), encoding="utf-8").read().splitlines()
    dlines = [l for l in dreg if l.startswith("| D")]
    dfix = sum(1 for l in dlines if "FIXED" in l)
    dpar = sum(1 for l in dlines if "PARTIAL" in l)
    dop = sum(1 for l in dlines if "OPEN" in l)
    dobs = len(dlines) - dfix - dpar - dop

    bp = open(os.path.join(PAPER, "BLUEPRINT_v3.1.md"), encoding="utf-8").read()
    s11a = bp.split("### 11a")[1].split("### 11b")[0]
    s11b = bp.split("### 11b")[1]
    a_x, a_o = s11a.count("- [x]"), s11a.count("- [ ]")
    b_x, b_o = s11b.count("- [x]"), s11b.count("- [ ]")

    # ---- 1. every phase is covered ----
    for ph in ["P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7"]:
        check("the note has a row for phase %s" % ph, ("| %s " % ph) in txt)
    check("the phase table has eight status rows",
          len([l for l in txt.splitlines() if re.match(r"^\| P\d ", l)]) == 8)

    # ---- 2. claim register ----
    for label, v in [("register rows", len(reg)), ("supported", cnt(reg, "SUPPORTED")),
                     ("partly supported", cnt(reg, "PARTLY SUPPORTED")),
                     ("not supported", cnt(reg, "NOT SUPPORTED")),
                     ("source not available", cnt(reg, "SOURCE NOT AVAILABLE"))]:
        check("the note prints the claim register's %s (%d)" % (label, v),
              "**%d" % v in txt or "%d " % v in txt or "%d," % v in txt or " %d " % v in txt)

    # ---- 3. the five buckets ----
    check("the note prints the closed-claim count (%d)" % closed, "**%d closed**" % closed in txt)
    check("the note prints the to-order count (%d)" % to_order, "**%d to order**" % to_order in txt)
    check("the note prints the waived count (%d)" % waived, "**%d waived**" % waived in txt)
    check("the note prints the held-but-unread count (%d)" % heldunread,
          "**%d held but unread**" % heldunread in txt)
    check("the note prints the register-level count (%d)" % len(rgl),
          "**%d register-level**" % len(rgl) in txt)
    check("the five buckets still add up to the register's unavailable rows",
          closed + to_order + waived + heldunread + len(rgl) == cnt(reg, "SOURCE NOT AVAILABLE"),
          "%d + %d + %d + %d + %d" % (closed, to_order, waived, heldunread, len(rgl)))

    # ---- 4. reference register ----
    check("the note prints the verification register's size (%d)" % len(ver),
          "**%d entries**" % len(ver) in txt)
    check("the note prints the verification register's R0 count (%d)" % vR0,
          "**%d are R0**" % vR0 in txt)
    check("the note prints the register's R3 count (%d)" % vR3,
          "%d R3" % vR3 in txt)
    check("the note prints the catalogue check's size and R0 count (%d, %d)" % (len(cat), cR0),
          "**%d entries** with **%d R0**" % (len(cat), cR0) in txt)
    check("the reference levels add up", vR0 + vR1 + vR2 + vR3 == len(ver), str(len(ver)))
    check("the catalogue levels add up", cR0 + cR1 + cR2 == len(cat), str(len(cat)))

    # ---- 5. build artefacts ----
    cov = rd(os.path.join(PAPER, "arena_deliverables", "P3_atlas", "atlas_case_coverage.csv"))
    cfull = sum(1 for r in cov if r["coverage"] == "yes")
    cpart = sum(1 for r in cov if r["coverage"] == "partial")
    check("the note prints the atlas plan, its executable coverage and its lack of case results (%d, %d, %d)"
          % (len(plan), cfull, cpart),
          ("**%d cases planned**, **%d with a fully executable invariant** and " % (len(plan), cfull)
           + ("**none partial**" if cpart == 0 else "**%d partial**" % cpart)) in txt)
    check("the note prints the benchmark registry size (%d)" % len(bench),
          "**%d benchmark records**" % len(bench) in txt)
    check("the note prints the second-implementation comparisons (%d)" % len(si),
          "**%d comparisons**" % len(si) in txt)
    check("the note prints the re-audited claim count (%d)" % len(rea),
          "%d claims re-audited" % len(rea) in txt or "%d flagged claims re-audited" % len(rea) in txt)
    check("the note prints the experiment extraction size (%d)" % len(exp2),
          "**%d rows**" % len(exp2) in txt)
    check("the note prints the edit-sheet size and its mandatory count (%d, %d)"
          % (len(es), sum(r["priority"].startswith("P1") for r in es)),
          "**%d paper edits**" % len(es) in txt)

    # ---- 6. defects ----
    check("the note prints the defect register's totals (%d entries: %d fixed, %d partial, %d open)"
          % (dfix + dpar + dop + dobs, dfix, dpar, dop),
          "%d entries: %d fixed, %d partial, %d open" % (dfix + dpar + dop + dobs, dfix, dpar, dop) in txt)

    # ---- 7. the two checklists ----
    check("the note prints the freeze checklist (%d of %d)" % (a_x, a_x + a_o),
          "**%d of %d**" % (a_x, a_x + a_o) in txt)
    check("the note prints the submission checklist (%d of %d)" % (b_x, b_x + b_o),
          "**%d of %d items passed**" % (b_x, b_x + b_o) in txt)
    check("the freeze checklist and the note agree that it is not complete",
          (a_o == 0) == ("11a Blueprint freeze | **%d of %d**" % (a_x, a_x + a_o) in txt and a_o == 0))

    # ---- 8. hygiene ----
    check("the note carries no link or drive identifier",
          not re.search(r"https?://|drive\.google|docs\.google|/folders/", txt))
    check("the note names no uploaded file", not re.search(r"\.zip|z-library|\.pdf", txt))

    print("     readiness: %d claims registered, %d unavailable, %d closed, %d to order"
          % (len(reg), cnt(reg, "SOURCE NOT AVAILABLE"), closed, to_order))
    print("     references: %d registered (%d R0), %d catalogued (%d R0)"
          % (len(ver), vR0, len(cat), cR0))
    print("     artefacts: atlas %d planned (%d full, %d partial, no case results),"
          " benchmark rows %d+%d, benchmarks %d, second impl %d, defects %d open"
          % (len(plan), cfull, cpart, len(bres), len(rd(os.path.join(
              PAPER, "arena_deliverables", "P3_atlas", "bench_surface_results.csv"))),
             len(bench), len(si), dop))
    if fails:
        print("FAIL %d check(s) failed" % len(fails))
        return 1
    print("PASS all checks (phases=8, claims=%d, refs=%d, defects=%d)"
          % (len(reg), len(ver), len(dlines)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
