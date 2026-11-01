#!/usr/bin/env python3
"""Validate claim_upgrade_2026-11-01.csv - the verdict each of the 40 blocked claims
should now carry, on the evidence read from the author-supplied sources.

Run from this directory:  python3 check_claim_upgrade.py
Everything checks out -> lines starting with PASS and exit code 0.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "claim_register.csv")
UP = os.path.join(HERE, "claim_upgrade_2026-11-01.csv")
READING = os.path.join(HERE, "source_reading_2026-11-01.csv")
SUPPLIED = os.path.join(HERE, "supplied_by_author_2026-11-01.csv")

COLS = ["claim_id", "cited_source", "register_verdict", "proposed_verdict", "evidence_page",
        "evidence_quote", "what_source_actually_states", "action_for_author", "verification_level"]
VERDICTS = {"SUPPORTED", "PARTLY SUPPORTED", "NOT SUPPORTED", "SOURCE NOT AVAILABLE"}
leak = re.compile(r"(drive\.google|docs\.google|https?://|/folders/)")

fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else " :: " + detail))
    if not ok:
        fails.append(name)


def words(s):
    return [w for w in s.split() if w != "[...]"]


with open(UP, newline="", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    check("header matches the declared schema", rdr.fieldnames == COLS, str(rdr.fieldnames))
    up = list(rdr)

check("one row per blocked claim (40)", len(up) == 40, str(len(up)))
ids = [r["claim_id"] for r in up]
check("no claim appears twice", len(set(ids)) == len(ids),
      str([i for i in ids if ids.count(i) > 1][:5]))

reg = {r["claim_id"]: r for r in csv.DictReader(open(REG, newline="", encoding="utf-8"))}
unknown = [i for i in ids if i not in reg]
check("every claim is a row of the register", not unknown, str(unknown[:5]))

with open(SUPPLIED, newline="", encoding="utf-8") as f:
    freed = {c.strip() for r in csv.DictReader(f) for c in r["claim_ids"].split() if c.strip()}
check("the rows cover exactly the claims the supplied sources free", set(ids) == freed,
      str(sorted(set(ids) ^ freed)[:5]))

wrong = [r["claim_id"] for r in up if r["register_verdict"] != "SOURCE NOT AVAILABLE"]
check("every row starts from the register's blocked verdict", not wrong, str(wrong[:5]))
drift = [r["claim_id"] for r in up if reg[r["claim_id"]]["verdict"] != r["register_verdict"]]
check("the register verdict quoted is the one on file", not drift, str(drift[:5]))
src = [r["claim_id"] for r in up if reg[r["claim_id"]]["cited_source"] != r["cited_source"]]
check("the cited source quoted is the one on file", not src, str(src[:5]))

badv = sorted({r["proposed_verdict"] for r in up} - VERDICTS)
check("every proposed verdict is from the register vocabulary", not badv, str(badv))

nopage = [r["claim_id"] for r in up if r["proposed_verdict"] != "SOURCE NOT AVAILABLE"
          and not re.match(r"^p\. ?\d", r["evidence_page"].strip())]
check("every answered claim carries the page the wording was read on", not nopage, str(nopage[:5]))
short = [r["claim_id"] for r in up if r["proposed_verdict"] != "SOURCE NOT AVAILABLE"
         and len(words(r["evidence_quote"])) < 4]
check("every answered claim carries a quote", not short, str(short[:5]))
longq = [r["claim_id"] for r in up if len(words(r["evidence_quote"])) > 25]
check("no quote is longer than 25 words", not longq, str(longq[:5]))
unread = [r["claim_id"] for r in up if r["proposed_verdict"] == "SOURCE NOT AVAILABLE"]
badun = [r["claim_id"] for r in up if r["proposed_verdict"] == "SOURCE NOT AVAILABLE"
         and (r["evidence_page"] != "-" or r["evidence_quote"] != "-")]
check("a claim still without a readable source quotes nothing", not badun, str(badun[:5]))
noact = [r["claim_id"] for r in up if len(r["action_for_author"].split()) < 4]
check("every row tells the author what to do with the sentence", not noact, str(noact[:5]))
badl = [r["claim_id"] for r in up if not re.match(r"^[VR][0-3] ", r["verification_level"])]
check("every row states its verification level", not badl, str(badl[:5]))
weak = [r["claim_id"] for r in up if r["proposed_verdict"] == "SUPPORTED"
        and not r["verification_level"].startswith("V2")]
check("no SUPPORTED row sits below V2", not weak, str(weak[:5]))

reading = {r["claim_id"]: r for r in csv.DictReader(open(READING, newline="", encoding="utf-8"))}
conf = [r["claim_id"] for r in up
        if (reading[r["claim_id"]]["verdict"] == "NOT READ")
        != (r["proposed_verdict"] == "SOURCE NOT AVAILABLE")]
check("the two files agree on which claim has no readable source", not conf, str(conf[:5]))
quote_drift = [r["claim_id"] for r in up
               if r["evidence_quote"] != "-" and r["evidence_quote"] != reading[r["claim_id"]]["evidence_quote"]]
check("the quote is the same in both files", not quote_drift, str(quote_drift[:5]))
page_drift = [r["claim_id"] for r in up
              if r["evidence_page"] != "-" and r["evidence_page"] != reading[r["claim_id"]]["evidence_page"]]
check("the page is the same in both files", not page_drift, str(page_drift[:5]))

blob = open(UP, encoding="utf-8").read()
check("no URLs or Drive links anywhere", not leak.search(blob))
named = [r["claim_id"] for r in up
         if re.search(r"Reference List|\bPaper \d+|\.zip|google_drive", " ".join(r.values()))]
check("the uploaded files are not named", not named, str(named[:5]))

per = {v: sum(1 for r in up if r["proposed_verdict"] == v) for v in sorted(VERDICTS)}
print("     proposed verdicts: " + ", ".join("%s=%d" % kv for kv in per.items()))
print("     blocked claims answered: %d of 40" % (40 - per["SOURCE NOT AVAILABLE"]))

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (upgrades=%d)" % len(up))
sys.exit(0)
