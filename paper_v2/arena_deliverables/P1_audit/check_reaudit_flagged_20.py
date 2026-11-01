#!/usr/bin/env python3
"""Validate reaudit_flagged_20.csv (Task 2). Prints PASS lines, exits 0 only if all checks pass."""
import csv, sys
COLS = ["claim_id","current_text","matches_source","suggested_wording","page_or_equation",
        "cited_source","manuscript_page","basis_for_judgement"]
EXPECTED = ["CR032","CR034","CR037","CR045","CR046","CR062","CR071","CR076","CR086","CR087",
            "CR088","CR091","CR099","CR100","CR104","CR105","CR118","CR135","CR143","CR206"]
fails=[]
def check(n,ok,d=""):
    print(("PASS " if ok else "FAIL ")+n+("" if ok else " :: "+d))
    if not ok: fails.append(n)
rows=list(csv.DictReader(open("reaudit_flagged_20.csv")))
check("header matches spec", list(rows[0].keys())==COLS, str(list(rows[0].keys())))
check("20 rows", len(rows)==20, str(len(rows)))
check("claim ids equal the flagged set of claim_register.csv",
      sorted(r["claim_id"] for r in rows)==sorted(EXPECTED))
check("matches_source in {yes,partly,no}", all(r["matches_source"] in {"yes","partly","no"} for r in rows))
bad=[r["claim_id"] for r in rows if len(r["suggested_wording"].split())>30]
check("suggested_wording <= 30 words", not bad, str(bad))
bad=[r["claim_id"] for r in rows if not r["page_or_equation"].strip() or not r["manuscript_page"].strip()]
check("every row has a source page/equation and a manuscript page", not bad, str(bad))
bad=[r["claim_id"] for r in rows if len(r["current_text"].split())<8]
check("current_text quoted for every row", not bad, str(bad))
if fails:
    print("FAIL %d check(s)"%len(fails)); sys.exit(1)
print("PASS all checks (rows=%d)"%len(rows)); sys.exit(0)
