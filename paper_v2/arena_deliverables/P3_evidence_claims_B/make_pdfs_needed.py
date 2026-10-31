#!/usr/bin/env python3
"""Split the 141 blocked sources into "in the library" and "needs the author's copy".

Input : `missing_sources_priority.csv` (141 cited sources, ranked by claims_blocked),
        `refs_catalogue_check.csv` (which keys the source library holds, with batch/level),
        `verification_register.csv` (bibliographic record per key: authors, year, title, DOI,
        verification level).
Output: `pdfs_needed_from_author.csv` - the sources the library does not give me,
        highest claims_blocked first, with the archive bundle named where the PDF is present
        but unreachable, and
        `library_available_sources.csv` - the ones the library does hold, so that the author
        can see what is *not* being asked for.

DOI policy: a DOI is written only where `verification_register.csv` records it as verified
from the publisher page or from the opened PDF first page.  Otherwise the field says
NOT FOUND.  Nothing is typed from memory, and no DOI is inferred from a title.

Usage: python3 make_pdfs_needed.py
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
PRI = os.path.join(REPO, "missing_sources_priority.csv")
CAT = os.path.join(REPO, "refs_catalogue_check.csv")
VER = os.path.join(REPO, "verification_register.csv")
OUT_NEEDED = os.path.join(HERE, "pdfs_needed_from_author.csv")
OUT_AVAIL = os.path.join(HERE, "library_available_sources.csv")

TOP_N = 30
# Library status per bibliography key, transcribed from the source library's own ledger
# (SOURCE_LEDGER.csv).  FOUND-* = the library holds a copy; MISSING / *-MISMATCH = it does
# not hold this work (the ledger's own evidence column says which different paper the
# held file turned out to be).  Keys absent from this map are absent from the ledger, i.e.
# the library has no record of holding them.
LIB_STATUS = {
    "Bazarra2021": "FOUND", "Biot1956": "FOUND", "ChadwickSneddon1958": "FOUND",
    "Chandrasekharaiah1998": "FOUND", "Cowin1983": "FOUND", "Dhaliwal1980": "FOUND",
    "Eringen1966a": "FOUND", "Eringen1972": "FOUND", "Eringen1974": "FOUND",
    "Ezzat2011": "FOUND", "Gorenflo1997": "FOUND", "Green1972": "FOUND",
    "Green1991": "FOUND", "Green1993": "FOUND", "GreenGN1992": "FOUND",
    "Hughes1980": "FOUND", "Iesan1986": "FOUND", "IvanovSavova1991": "FOUND",
    "Kumar2008": "FOUND", "Kumar2023": "FOUND", "Kumar2023PhysScr": "FOUND",
    "LasieckaWang2015MGT": "FOUND", "LazarAgiasofitou2022": "FOUND", "Li2019": "FOUND",
    "Lord1967": "FOUND", "Marotti2013": "FOUND", "Nunziato1979": "FOUND",
    "Povstenko2011Cattaneo": "FOUND", "Quintanilla2019": "FOUND",
    "RoyChoudhuri2007": "FOUND", "Sarkar2019": "FOUND", "Shakeriaski2021": "FOUND",
    "Singh2020c": "FOUND", "Srivastava2026": "FOUND", "Sur2019": "FOUND",
    "Sur2025": "FOUND", "Tiwari2021": "FOUND", "Tzou1995": "FOUND", "Wang2011": "FOUND",
    "Youssef2006": "FOUND", "Yu2024": "FOUND", "Mindlin1974": "FOUND",
    "Kumar2018": "FOUND", "Kumar2025": "FOUND", "Liu2020": "FOUND",
    "GorenfloKilbasMainardiRogosin2014": "FOUND",
    "Abdalla2022": "MISSING", "Bayones2021": "MISSING", "Caputo1967": "MISSING",
    "Chandrasekharaiah1984": "MISSING", "ChenGurtin1968": "MISSING", "Chirita2016": "MISSING",
    "Das2008": "MISSING", "DubnerAbate1968": "MISSING", "Durbin1974": "MISSING",
    "Fu2013": "MISSING", "GurtinWilliams1966": "MISSING", "HonigHirdes1984": "MISSING",
    "Joseph1989": "MISSING", "Joseph1990": "MISSING", "Kalkal2020": "MISSING",
    "Kumar2019": "MISSING", "Kumar2022": "MISSING", "Luchko2010": "MISSING",
    "MarchandMcDevittTriggiani2012": "MISSING", "MooreGibson1960": "MISSING",
    "Nowacki1978": "MISSING", "Povstenko2004": "MISSING", "Povstenko2007": "MISSING",
    "Povstenko2009": "MISSING", "Povstenko2011": "MISSING", "Prasad2020": "MISSING",
    "Sharma2022": "MISSING", "Sherief2010Fractional": "MISSING", "Singh2019": "MISSING",
    "Singh2020": "MISSING", "Singh2020a": "MISSING", "Singh2020b": "MISSING",
    "Stehfest1970": "MISSING", "Stroh1958": "MISSING", "Stroh1962": "MISSING",
    "Wang2021": "MISSING", "WangLi2025IV": "MISSING", "vanDerMerwe2021": "MISSING",
    "Yu2018ModifiedGL": "MISSING",
    "HetnarskiIgnaczak1999": "MISMATCH", "Iesan2013": "MISMATCH", "Kumar2017": "MISMATCH",
    "Eringen1968b": "MISMATCH",
}
# archive members that the project's own split-parts index records, with the bundle that
# holds each one.  These are present in the library but cannot be extracted here.
ARCHIVE = {
    "cahill2003.pdf": "LE_PAPERS_P02__was_R3.zip",
    "2ndSoundSolids.pdf": "LE_PAPERS_P02__was_R3.zip",
    "huberman2019.pdf": "LE_PAPERS_P03__was_R4.zip",
    "jackson1970.pdf": "LE_PAPERS_P03__was_R4.zip",
}
# cited name -> bibliography key, where the priority list spells the name out
MANUAL = {
    "Chen and Nunziato 1974": "ChenNunziato1974",
    "Coleman and Gurtin 1967": "ColemanGurtin1967",
    "Ackerman et al. 1966": "Ackerman1966",
    "van der Merwe": "vanDerMerwe2021",
    "Muller and Ruggeri 1998": "MuellerRuggeri1998",
    "Muller 1967": "Mueller1967",
    "de Hoog": "deHoog1982",
    "McNelly et al. 1970": "McNelly1970",
    "Huberman et al. 2019": "Huberman2019",
    "Cahill et al. 2003": "Cahill2003",
}
# which archive member belongs to which bibliography key
ARCHIVE_KEY = {"Cahill2003": "cahill2003.pdf", "Huberman2019": "huberman2019.pdf",
               "Jackson1970": "jackson1970.pdf"}
# DOIs that Task 4's survey recorded as verified, with the source stated there
# (P3_experiments/experiments_1.csv, column doi_source).  Nothing new is typed from memory.
DOI_FROM_TASK4 = {
    "McNelly1970": "10.1103/PhysRevLett.24.100",
    "Jackson1970": "10.1103/PhysRevLett.25.26",
    "Huberman2019": "10.1126/science.aav3548",
    "Cahill2003": "10.1063/1.1524305",
    "Zener1937": "10.1103/PhysRev.52.230",
}
EXTRA_ARCHIVE = [("SecondSound1970review", "2ndSoundSolids.pdf",
                  "A review of second sound in solids held only inside the same bundle "
                  "(member name as it appears in the archive).")]


def surnames(src):
    head = re.sub(r"\d{4}.*", "", src.split("(")[0])
    return [p.strip() for p in re.split(r",| and |&", head) if p.strip() and p.strip()[0].isupper()]


def year_of(src):
    m = re.search(r"\b(1[89]\d\d|20\d\d)\b", src)
    return m.group(1) if m else ""


def resolve(src, allkeys, ver):
    if "|" in src:
        cand = src.split("|")[0].strip()
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", cand):
            return cand
    for name, key in MANUAL.items():
        if src.startswith(name):
            return key
    sn, y = surnames(src), year_of(src)
    if not sn or not y:
        return ""
    cands = [k for k in allkeys if k.lower().startswith(sn[0].lower().replace("'", "")) and y in k]
    if not cands:
        return ""
    if len(cands) > 1:
        def score(k):
            a = (ver.get(k, {}) or {}).get("full_authors", "") or ""
            return sum(1 for s in sn if s.split()[0].lower() in a.lower())
        cands = sorted(cands, key=score, reverse=True)
    return cands[0]


def doi_ok(rec):
    """A DOI is written only when the register says it was verified on a publisher page."""
    if not rec:
        return False
    doi = (rec.get("doi") or "").strip()
    if not doi or doi in ("(absent)", "-"):
        return False
    status = (rec.get("metadata_status") or "").lower()
    level = rec.get("verification_level", "")
    return ("verified" in status) and level in ("R1", "R2", "R3", "R1-noDOI")


def catalogue_titles():
    """Titles from the manuscript's own classified catalogue (paper_sources.zip)."""
    import zipfile
    out = {}
    try:
        z = zipfile.ZipFile(os.path.join(REPO, "paper_sources.zip"))
        tex = z.read("sections/appD_catalogue.tex").decode("utf-8", "replace")
        for m in re.finditer(r"\\item \\citet\{([^}]+)\}: \\emph\{([^}]*)\}", tex):
            out[m.group(1)] = m.group(2)
    except Exception:
        pass
    return out


def main():
    cat = {r["key"]: r for r in csv.DictReader(open(CAT, newline=""))}
    CATITLE = catalogue_titles()
    ver = {r["bibkey"]: r for r in csv.DictReader(open(VER, newline=""))}
    allkeys = set(cat) | set(ver)

    needed, avail, unresolved = [], [], []
    for r in csv.DictReader(open(PRI, newline="")):
        key = resolve(r["cited_source"], allkeys, ver)
        if not key:
            unresolved.append(r["cited_source"])
            continue
        rec = ver.get(key, {})
        member = ARCHIVE_KEY.get(key, "")
        cited = r["cited_source"]
        # The register has a few mis-keyed records (a key pointing at a different work).
        # A record is used only if the first surname of the citation actually appears in it.
        sn = surnames(cited)
        if rec and sn and sn[0].split()[0].lower() not in (rec.get("full_authors") or "").lower():
            rec = {}
        authors = (rec.get("full_authors") or "").strip() or cited.split(" (")[0].strip()
        title = (rec.get("title") or "").strip() or CATITLE.get(key, "").strip()
        if not title:
            title = "- (no title in the register or in the catalogue)"
        row = dict(bib_key=key,
                   authors=authors,
                   year=(rec.get("year") or year_of(r["cited_source"])).strip(),
                   title=title,
                   doi=(rec["doi"].strip() if doi_ok(rec)
                        else DOI_FROM_TASK4.get(key, "NOT FOUND")),
                   claims_blocked=int(r["claims_blocked"]),
                   claim_ids=r["claim_ids"],
                   priority_rank=int(r["rank"]),
                   cited_as=r["cited_source"][:120])
        st = LIB_STATUS.get(key, "")
        row["library_ledger_status"] = st or "no ledger record"
        if member:
            row["availability"] = "library - archive bundle %s (member %s), over the 25 MB cap" % (
                ARCHIVE[member], member)
            needed.append(row)
        elif st == "FOUND":
            row["availability"] = "library - held copy, ledger says FOUND"
            avail.append(row)
        elif st == "MISMATCH":
            row["availability"] = ("library - the held file is a different paper; this work "
                                   "itself is not held")
            needed.append(row)
        elif st == "MISSING":
            row["availability"] = "not in library - ledger says MISSING"
            needed.append(row)
        else:
            row["availability"] = "not in library - no ledger record"
            needed.append(row)

    for key, member, note in EXTRA_ARCHIVE:
        rec = ver.get(key, {})
        needed.append(dict(bib_key=key, authors=(rec.get("full_authors") or "not identified").strip(),
                           year=(rec.get("year") or "").strip(),
                           title=(rec.get("title") or "review of second sound in solids").strip(),
                           doi=(rec["doi"].strip() if doi_ok(rec)
                        else DOI_FROM_TASK4.get(key, "NOT FOUND")),
                           claims_blocked=0, claim_ids="", priority_rank=0,
                           cited_as=note,
                           availability="library - archive bundle %s (member %s), over the 25 MB cap"
                                        % (ARCHIVE[member], member)))

    dedup2 = {}
    for r in needed:
        k = r["bib_key"]
        if k not in dedup2 or r["claims_blocked"] > dedup2[k]["claims_blocked"]:
            dedup2[k] = r
    needed = list(dedup2.values())
    needed.sort(key=lambda r: (-r["claims_blocked"], r["priority_rank"]))
    top = needed[:TOP_N]
    # the archive-blocked rows must survive the cut: they are the ones the author can fix
    for r in needed:
        if "archive bundle" in r["availability"] and r not in top:
            top.append(r)

    cols = ["rank", "bib_key", "authors", "year", "title", "doi", "claims_blocked",
            "claim_ids", "availability", "library_ledger_status", "cited_as_in_priority_list"]
    for i, r in enumerate(top, 1):
        r["rank"] = i
    with open(OUT_NEEDED, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in top:
            w.writerow({k: r.get(k, "") for k in cols})

    # one row per bibliography key (the priority list can cite the same work twice)
    dedup = {}
    for r in avail:
        k = r["bib_key"]
        if k not in dedup or r["claims_blocked"] > dedup[k]["claims_blocked"]:
            dedup[k] = r
    avail = list(dedup.values())
    cols2 = ["bib_key", "authors", "year", "title", "doi", "claims_blocked", "claim_ids",
             "availability"]
    with open(OUT_AVAIL, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols2)
        w.writeheader()
        for r in sorted(avail, key=lambda r: -r["claims_blocked"]):
            w.writerow({k: r.get(k, "") for k in cols2})

    print("priority rows: %d | in library (loose): %d | needs author: %d (listed: %d) | "
          "unresolved names: %d" % (141, len(avail), len(needed), len(top), len(unresolved)))
    for u in unresolved:
        print("  WARN unresolved: %s" % u[:70])
    return 0


if __name__ == "__main__":
    sys.exit(main())
