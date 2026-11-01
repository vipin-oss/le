#!/usr/bin/env python3
"""Check the 2026-11-01 P2 pass: the R0 rows of the verification register and the
four held sources. Run from inside this directory:

    cd paper_v2/arena_deliverables/P2_verification && python3 check_p2_pass.py

Exit 0 and a line starting with PASS only if every claim in
README_R0_AND_HELD_2026-11-01.md is still true of the data on disk.
"""
import collections
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.abspath(os.path.join(HERE, "..", ".."))
REG = os.path.join(PAPER, "verification_register.csv")
CLM = os.path.join(PAPER, "claim_register.csv")
RES = os.path.join(HERE, "R0_RESOLUTION_2026-11-01.csv")
HELD = os.path.join(HERE, "HELD_SOURCES_2026-11-01.csv")
NOTE = os.path.join(HERE, "README_R0_AND_HELD_2026-11-01.md")

fails = []


def check(label, ok, detail=""):
    if ok:
        print("  ok   %s%s" % (label, ("  [%s]" % detail) if detail else ""))
    else:
        print("  FAIL %s%s" % (label, ("  [%s]" % detail) if detail else ""))
        fails.append(label)


def rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


ver = rows(REG)
res = rows(RES)
held = rows(HELD)
clm = rows(CLM)
txt = open(NOTE, encoding="utf-8").read()

print("== the verification register ==")
lv = collections.Counter(r["verification_level"] for r in ver)
check("the register still holds 119 rows", len(ver) == 119, str(len(ver)))
check("the levels are 62 R2 / 42 R1 / 4 R3 / 4 R1-noDOI / 7 R0",
      lv == {"R2": 62, "R1": 42, "R3": 4, "R1-noDOI": 4, "R0": 7}, str(dict(lv)))
check("the levels add up to the row count", sum(lv.values()) == len(ver), str(sum(lv.values())))

keys = collections.Counter(r["bibkey"] for r in ver)
dups = sorted(k for k, v in keys.items() if v > 1)
check("119 rows carry 113 distinct bibkeys", len(keys) == 113, str(len(keys)))
check("exactly six bibkeys are duplicated",
      dups == ["Bleustein1968", "BornKarman1912", "Danilovskaya1950", "Duhamel1837",
               "Jou2010", "Scruby1990"], ", ".join(dups))
check("only Bleustein1968 has two different levels",
      sum(1 for k in dups if len({r["verification_level"] for r in ver if r["bibkey"] == k}) > 1) == 1)

r0 = sorted({r["bibkey"] for r in ver if r["verification_level"] == "R0"})
check("the five works still at R0 are the ones the note names",
      r0 == ["Auld1973", "Chadwick1960", "Duhamel1837", "Gulyaev1969", "Scruby1990"], ", ".join(r0))

stale = {"Jackson1970": "10.1080/01495739208946136",
         "Rayleigh1885": "10.15625/0866-7136/19728",
         "Mueller1967": "10.1007/s00419-026-03092-7",
         "IgnaczakOstoja2010": "10.1177/1081286519862007",
         "Kaminski1990": "10.1016/j.apm.2021.02.028",
         "Mitra1995": "10.1016/j.csite.2021.101211",
         "Pennes1948": "10.1007/s11043-023-09647-3"}
check("none of the seven wrong DOIs is still attached to the row it had been pasted into",
      not [k for k, d in stale.items()
           if any(r["bibkey"] == k and r["doi"].strip().lower() == d.lower() for r in ver)])
# two of the borrowed DOIs are real entries in their own right and must survive on their own rows
check("the two borrowed DOIs still sit on the rows they belong to (Li2021, Zhang2021)",
      any(r["bibkey"] == "Li2021" and r["doi"].strip().lower() == "10.1016/j.apm.2021.02.028" for r in ver)
      and any(r["bibkey"] == "Zhang2021" and r["doi"].strip().lower() == "10.1016/j.csite.2021.101211" for r in ver))

fixed = {"Jackson1970": "10.1103/physrevlett.25.26",
         "Rayleigh1885": "10.1112/plms/s1-17.1.4",
         "Mueller1967": "10.1007/bf00285677",
         "Kaminski1990": "10.1115/1.2910422",
         "Mitra1995": "10.1115/1.2822615",
         "Pennes1948": "10.1152/jappl.1948.1.2.93",
         "Ackerman1966": "10.1103/physrevlett.16.789",
         "Bleustein1968": "10.1063/1.1652495"}
bad = [k for k, d in fixed.items()
       if not any(r["bibkey"] == k and r["doi"].strip().lower() == d for r in ver)]
check("all eight replaced rows now carry the corrected DOI", not bad, ", ".join(bad))

check("Mueller1967 now names the ARMA paper, not a 2026 one",
      any(r["bibkey"] == "Mueller1967" and r["title"] == "On the entropy inequality"
          and r["volume"] == "26" and r["pages"] == "118-141" for r in ver))
check("every row above R0 has a title", all(r["title"].strip() for r in ver
                                            if r["verification_level"] != "R0"))
check("the four books/chapters read in this cycle are marked R3",
      {r["bibkey"] for r in ver if r["verification_level"] == "R3"}
      == {"Boley1960", "Podlubny1999", "Carlson1972", "IgnaczakOstoja2010"})

print("== the resolution table ==")
check("it has one row for each of the 32 original R0 rows", len(res) == 32, str(len(res)))
vv = collections.Counter(r["verdict"] for r in res)
check("the verdicts are 8 completed / 8 replaced / 4 to R3 / 2 aligned / 1 memory / 2 confirmed / 7 still R0",
      vv == {"METADATA_COMPLETED": 8, "METADATA_REPLACED": 8, "UPGRADED_TO_R3": 4,
             "LEVEL_ALIGNED": 2, "MEMORY_ENTRY_CONFIRMED": 1,
             "CONFIRMED_AS_CANDIDATE": 2, "STILL_R0": 7}, str(dict(vv)))
check("every row carries evidence", all(r["evidence"].strip() for r in res))
still = {r["bibkey"] for r in res if r["verdict"] == "STILL_R0"}
check("the rows left at R0 in the table are the rows left at R0 in the register", still == set(r0),
      ", ".join(sorted(still)))
check("the table's level column agrees with the register",
      all(any(v["bibkey"] == r["bibkey"] and v["verification_level"] == r["level_now"] for v in ver)
          for r in res))
check("the table never prints a DOIs it did not verify",
      all(r["doi_now"].strip() for r in res))

print("== the four held sources ==")
check("the held table has four rows", len(held) == 4, str(len(held)))
check("the four claims are CR127 / CR152 / CR166 / CR196",
      [r["claim_id"] for r in held] == ["CR127", "CR152", "CR166", "CR196"])
check("every held citation was verified against a record today",
      all(r["record_verified_2026_11_01"] == "yes" for r in held))
check("every held row prints the title the record printed",
      all(r["crossref_title_2026_11_01"].strip() for r in held))
check("no held source is claimed as read",
      all(r["content_read"] == "no" for r in held))
check("the held claims keep their verdict",
      all(r["claim_verdict_unchanged"] == "SOURCE NOT AVAILABLE" for r in held))
cver = {r["claim_id"]: r["verdict"] for r in clm}
check("the claim register still says SOURCE NOT AVAILABLE for all four",
      all(cver.get(c) == "SOURCE NOT AVAILABLE" for c in ("CR127", "CR152", "CR166", "CR196")),
      ", ".join("%s=%s" % (c, cver.get(c)) for c in ("CR127", "CR152", "CR166", "CR196")))
check("the held table records the searches that were run",
      all(r["library_search_strings_used"].strip() and r["library_result"].strip() for r in held))

print("== the note ==")
check("the note prints the level counts it can be checked against",
      "62 R2, 42 R1, 4 R3, 4 R1-noDOI, 7 R0" in txt)
check("the note prints the duplicate count",
      "113 distinct bibkeys" in txt and "six bibkeys" in txt.lower())
check("the note prints the eleven works that were replaced or completed", "METADATA_REPLACED" in txt)
check("the note states that P2's exit condition is not met", "not met" in txt)
check("the note carries no link and no drive identifier",
      not re.search(r"https?://|drive\.google|docs\.google|/folders/", txt))
check("the note names no uploaded file", not re.search(r"\.zip|z-library|\.pdf", txt))

print()
print("     register: %d rows, %d unique bibkeys, R0 %d"
      % (len(ver), len(keys), lv.get("R0", 0)))
print("     resolution: %d rows, %d still R0, %d promoted"
      % (len(res), vv.get("STILL_R0", 0), len(res) - vv.get("STILL_R0", 0)))
print("     held sources: %d rows, %d unread" % (len(held), sum(r["content_read"] == "no" for r in held)))
if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (register=%d rows, R0=%d, resolution=%d, held=%d)"
      % (len(ver), lv.get("R0", 0), len(res), len(held)))
