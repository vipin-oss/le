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
check("the register still holds at least the 119 rows step 24 left", len(ver) >= 119, str(len(ver)))
check("the four levels step 24 fixed are unchanged (62 R2, 4 R3, 4 R1-noDOI, 7 R0)",
      lv.get("R2") == 62 and lv.get("R3") == 4 and lv.get("R1-noDOI") == 4 and lv.get("R0") == 7,
      "R2=%d R3=%d R1-noDOI=%d R0=%d" % (lv.get("R2", 0), lv.get("R3", 0),
                                         lv.get("R1-noDOI", 0), lv.get("R0", 0)))
check("every other row is R1", lv.get("R1", 0) == len(ver) - 62 - 4 - 4 - 7, str(lv.get("R1", 0)))
check("the levels add up to the row count", sum(lv.values()) == len(ver), str(sum(lv.values())))

keys = collections.Counter(r["bibkey"] for r in ver)
dups = sorted(k for k, v in keys.items() if v > 1)
check("the register still carries at least the 113 distinct bibkeys of step 24",
      len(keys) >= 113, str(len(keys)))
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

print("== the coverage extension ==")
ext = [r for r in ver if r["batch"] == "007-ext"]
check("the extension added 85 rows", len(ext) == 85, str(len(ext)))
check("every extension row is R1 with a DOI and a title",
      all(r["verification_level"] == "R1" and r["doi"].strip() and r["title"].strip() for r in ext))
check("every extension row says it is title-level verification only",
      all("Title-level verification only" in r["metadata_status"] for r in ext))
cov = rows(os.path.join(HERE, "COVERAGE_EXTENSION_2026-11-01.csv"))
check("the extension table has one row per added row", len(cov) == len(ext), str(len(cov)))
check("every added row was matched at 0.80 or better",
      all(float(r["title_match_score"]) >= 0.80 for r in cov),
      min(float(r["title_match_score"]) for r in cov).__str__())
check("two rows got the author-level check",
      sum(r["author_level_check"] == "yes" for r in cov) == 2)
check("Chen and Nunziato 1974 is now a located paper (ZAMP 25, 791-798)",
      any(r["bibkey"] == "LM1_ChenNunziato1974" and r["volume"] == "25"
          and r["pages"] == "791--798" for r in ver))
check("Coleman and Gurtin 1967 carries its own DOI (J. Chem. Phys. 47, 597-613)",
      any(r["bibkey"] == "LM1_ColemanGurtin1967" and r["doi"].lower() == "10.1063/1.1711937"
          and r["pages"] == "597--613" for r in ver))

print("== the nine catalogue R0 rows ==")
cat9 = rows(os.path.join(HERE, "CATALOGUE_R0_2026-11-01.csv"))
catv = collections.Counter(r["level"] for r in rows(os.path.join(PAPER, "refs_catalogue_check.csv")))
check("the catalogue still has 9 R0 rows", catv.get("R0") == 9, str(catv.get("R0")))
check("the notes cover all nine", len(cat9) == 9 and {r["key"] for r in cat9} ==
      {r["key"] for r in rows(os.path.join(PAPER, "refs_catalogue_check.csv")) if r["level"] == "R0"})
st = collections.Counter(r["status"] for r in cat9)
check("the status split is 5 print-only / 2 resolved / 1 reprint / 1 edition warning",
      st == {"PRINT_ONLY": 5, "RESOLVED": 2, "RESOLVED_AS_REPRINT": 1,
             "EDITION_MISMATCH_WARNING": 1}, str(dict(st)))
check("every resolved row prints the DOI or ISBN it found",
      all(r["doi_or_isbn_found"].strip().lower() != "none" for r in cat9
          if r["status"].startswith("RESOLVED") or r["status"] == "EDITION_MISMATCH_WARNING"))
check("every print-only row says none", all(r["doi_or_isbn_found"].strip().lower() == "none"
                                            for r in cat9 if r["status"] == "PRINT_ONLY"))
tz = [r for r in cat9 if r["key"] == "Tzou1997"][0]
check("the Tzou row warns that the record is the 2014 edition", "2014" in tz["evidence"] + tz["recommended_action"])
gy = [r for r in cat9 if r["key"] == "Gulyaev1969"][0]
check("the Gulyaev row says its bib DOI belongs to Coleman and Gurtin",
      "Coleman" in gy["recommended_action"] and "10.1063/1.1711937" in gy["recommended_action"])

print("== the note ==")
check("the note prints the level counts it can be checked against",
      "62 R2, 127 R1, 4 R3, 4 R1-noDOI, 7 R0" in txt)
check("the note prints the post-extension register size",
      "204 rows" in txt and "198 distinct bibkeys" in txt)
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
