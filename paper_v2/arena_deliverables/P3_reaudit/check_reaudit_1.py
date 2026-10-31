#!/usr/bin/env python3
"""Validate P3_reaudit/reaudit_1.csv (Task 2, re-run).

Checks
 1. exactly the 20 flagged rows of claim_register.csv (verdict PARTLY SUPPORTED or
    NOT SUPPORTED) are present, once each, in register order;
 2. the twelve-column schema is exact;
 3. every row states a page of main.pdf (1..145) and quotes the current page text;
 4. the verdict vocabulary is fixed and every row carries a basis for its judgement;
 5. a row may say `resolved` only if it also says the wording the earlier pass judged is
    still present - a resolved verdict on text that has changed would be unfounded;
 6. no URLs, Drive links or unknown long identifiers anywhere (bibliography keys are
    allowed, a Drive id is not).

Prints PASS lines and exits 0; prints FAIL and exits 1 otherwise.  Standard library only.
"""
import csv
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
CSV_PATH = os.path.join(HERE, "reaudit_1.csv")
REG = os.path.join(REPO, "claim_register.csv")
ZIP = os.path.join(REPO, "paper_sources.zip")

COLS = ["claim_id", "register_verdict", "cited_source", "manuscript_page", "located_in_pdf",
        "current_text_in_pdf", "earlier_quote_still_present", "six_gram_overlap",
        "reaudit_verdict", "basis_for_judgement", "suggested_wording", "notes"]
VERDICTS = {"resolved", "still partly supported", "wording changed - re-check", "not located"}
PRESENT = {"yes", "partly", "no", "not applicable"}
fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else " :: " + detail))
    if not ok:
        fails.append(name)


def main():
    rows = list(csv.DictReader(open(CSV_PATH, newline="")))
    hdr = list(rows[0].keys())
    check("header matches the declared schema", hdr == COLS, str(hdr))

    flagged = [r["claim_id"] for r in csv.DictReader(open(REG, newline=""))
               if r["verdict"] in ("PARTLY SUPPORTED", "NOT SUPPORTED")]
    ids = [r["claim_id"] for r in rows]
    check("exactly the 20 flagged claims, in register order", ids == flagged,
          "%d rows, %d flagged" % (len(ids), len(flagged)))
    check("no duplicate claim ids", len(set(ids)) == len(ids))

    bad = [r["claim_id"] for r in rows
           if not (r["manuscript_page"].isdigit() and 1 <= int(r["manuscript_page"]) <= 145)]
    check("every row states a main.pdf page in 1..145", not bad, str(bad[:5]))

    bad = [r["claim_id"] for r in rows if r["located_in_pdf"] == "yes" and not r["current_text_in_pdf"].strip()]
    check("every located row quotes the current page text", not bad, str(bad[:5]))

    check("verdict vocabulary is fixed", all(r["reaudit_verdict"] in VERDICTS for r in rows),
          str({r["reaudit_verdict"] for r in rows} - VERDICTS))
    check("earlier-quote vocabulary is fixed",
          all(r["earlier_quote_still_present"] in PRESENT for r in rows),
          str({r["earlier_quote_still_present"] for r in rows} - PRESENT))
    check("every row carries a basis for its judgement",
          all(r["basis_for_judgement"].strip() for r in rows))

    bad = [r["claim_id"] for r in rows if r["reaudit_verdict"] == "resolved"
           and r["earlier_quote_still_present"] != "yes"]
    check("a resolved row has the earlier wording still present", not bad, str(bad[:5]))

    keys = set()
    try:
        z = zipfile.ZipFile(ZIP)
        for n in z.namelist():
            if n.startswith("refs") and n.endswith(".bib"):
                keys |= set(re.findall(r"@\w+\{([^,]+),", z.read(n).decode("utf-8", "replace")))
    except Exception:
        pass
    leak = re.compile(r"(drive\.google|docs\.google|https?://|/folders/)")
    longtok = re.compile(r"\b[A-Za-z0-9]{28,}\b")
    bad = [r["claim_id"] for r in rows
           if leak.search(" ".join(r.values()))
           or any(t not in keys for t in longtok.findall(" ".join(r.values())))]
    check("no URLs, Drive links or unknown long ids", not bad, str(bad[:5]))

    counts = {}
    for r in rows:
        counts[r["reaudit_verdict"]] = counts.get(r["reaudit_verdict"], 0) + 1
    print("     verdict counts: " + ", ".join("%s=%d" % kv for kv in sorted(counts.items())))

    if fails:
        print("FAIL %d check(s) failed" % len(fails))
        return 1
    print("PASS all checks (rows=%d, resolved=%d)" % (len(rows), counts.get("resolved", 0)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
