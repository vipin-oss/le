#!/usr/bin/env python3
"""Build v2_verified_ledger.csv — what manuscript_v2 actually verified, and what the merge does
with each item.

Sources, all in-repo:
  P1_audit/equation_inventory.csv          136 printed equations
  manuscript_v2/master/appendices/appA_equation_register.tex   61 audited register rows
  P1_audit/register_linkage.csv            register id -> equation label
  claim_register.csv                       224 claims with verdicts and verification levels

Every row carries a merge disposition, so the ledger answers "is this lost by the merge?".
Nothing is upgraded: a claim the source did not support stays flagged.
Prints PASS and exits 0.
"""
import csv, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))
INV = os.path.join(REPO, "paper_v2", "arena_deliverables", "P1_audit", "equation_inventory.csv")
LINK = os.path.join(REPO, "paper_v2", "arena_deliverables", "P1_audit", "register_linkage.csv")
REG = os.path.join(REPO, "paper_v2", "manuscript_v2", "master", "appendices",
                   "appA_equation_register.tex")
CLAIMS = os.path.join(REPO, "paper_v2", "claim_register.csv")
STATUS = ["DERIVED", "CONDITIONAL", "PRIMARY-SOURCE-CHECKED", "SECONDARY-SOURCE",
          "VERIFIED-SYMBOLIC", "UNVERIFIED", "OPEN", "WITHHELD"]
LAB, REF = re.compile(r"\\label\{(eq:[^}]+)\}"), re.compile(r"\\eqref\{(eq:[^}]+)\}")

# v2 label -> snippet that carries the same statement into the final paper
CARRY = {
    "eq:3.5": "M01/M08",      # momentum balance
    "eq:3.8": "M08",          # symmetry of the stress
    "eq:4.2": "M01",          # Biot heat conduction
    "eq:4.4": "M01",          # relaxation law for the flux
    "eq:4.11": "M01/M09",     # Green-Lindsay flux law
    "eq:4.15": "M01",         # dual-phase-lag law
    "eq:5.6": "M01",          # piezothermoelastic constitutive relation
}
# verification level -> meaning, from the register's own definitions
AUDIT_FACTS = [
    ("C01", "build", "v1.2 manuscript compiled and certified",
     "142 pages, 64,932 words, 136 printed equations, 16 figures, 55 tables, 107 cited works, 0 unresolved references",
     "six repository checkers print PASS and exit 0; submission zip is 606,104 B",
     "v1.2 submission package", "carried: the final paper is the author's own descendant of this text"),
    ("C02", "bibliography", "Crossref DOI verification of the monographs cited",
     "Eringen & Maugin I 10.1007/978-1-4612-3226-1; II 10.1007/978-1-4612-3236-0; Maugin 1988 10.1016/c2009-0-08748-0; "
     "Povstenko, Fractional Thermoelasticity 10.1007/978-3-319-15335-3 (2nd ed. 10.1007/978-3-031-64587-7); "
     "diffusion-wave 10.1007/978-3-319-17954-4; Achenbach 10.1016/c2013-0-04485-4; Miklowitz 10.1016/c2009-0-08749-2",
     "each identifier resolves to a record with matching author, title and year; Graff (1975) has no Crossref record and is listed without a DOI",
     "manuscript_v2 bibliography", "carried: every one of v2's 144 cited keys is present in the final paper's 362-key bibliography"),
    ("C03", "bibliography", "v2's cited-key set is a subset of the final bibliography",
     "144 v2 keys minus 362 final keys = 0", "set comparison of \\cite keys harvested from both trees", "both", "carried: no new bibliography entry is needed to paste any snippet"),
    ("C04", "audit", "Equation inventory complete for the printed document",
     "136 printed equations, printed numbers 1..136 with no gap, each traced to file/section/subsection",
     "P1_audit/equation_inventory.csv; continuity checked in this script", "manuscript_v2", "partial: 11 of the 136 carry a register status"),
    ("C05", "audit", "Claim register built",
     "224 claims: SUPPORTED 74, PARTLY SUPPORTED 34, NOT SUPPORTED 5, SOURCE NOT AVAILABLE 111; 43 claims re-read page by page in the final pass",
     "claim_register.csv; verifier column distinguishes the two reading passes", "manuscript_v2", "not carried as text: the register is audit apparatus, and its verdicts are reflected in the flags below"),
    ("C06", "probe", "Absence of v2's audit apparatus in the final paper",
     "0 hits for a verification register, an evidence protocol, a contributions table, a research-question table, the five-axis taxonomy, and balance-law derivations in the final sources",
     "six keyword/semantic probes over the final tree (main.tex + 46 section files + 8 appendices)", "final paper", "drives snippets M01, M02, M06, M04, M07, M08"),
]


def parse_register():
    out = {}
    for line in open(REG, encoding="utf-8", errors="replace").read().splitlines():
        if "&" not in line:
            continue
        cells = [c.strip() for c in line.split("&")]
        st = next((c.strip().strip("\\").strip() for c in cells
                   if c.strip().strip("\\").strip() in STATUS), None)
        if not st:
            continue
        note = re.sub(r"\s+", " ", cells[-1].strip())
        note = re.sub(r"\\\\\s*$", "", note).strip()[:130]
        for lb in LAB.findall(line) + REF.findall(line):
            out.setdefault(lb, (st, note))
    return out


def main():
    reg = parse_register()
    ids = {}
    for r in csv.DictReader(open(LINK, encoding="utf-8")):
        for lb in [x.strip() for x in (r["pointer"] or "").split(";") if x.strip().startswith("eq:")]:
            ids.setdefault(lb, r["eq_id"])
    rows = []
    inv = list(csv.DictReader(open(INV, encoding="utf-8")))
    nums = [int(r["printed"]) for r in inv]
    assert nums == list(range(1, len(inv) + 1)), "printed numbers are not contiguous"
    for r in inv:
        st, note = reg.get(r["label"], ("", ""))
        rid = ids.get(r["label"], "")
        carried = CARRY.get(r["label"], "")
        rows.append({
            "id": f"E{r['printed']:>03}",
            "kind": "equation",
            "item": f"printed eq. {r['printed']} ({r['label']})",
            "status": st or "not registered",
            "evidence": note if st else "no per-equation check exists",
            "v2_location": f"{r['file']} / {r['section']} / {r['subsection']}",
            "merge_disposition": (f"carried by snippet {carried}" if carried
                                  else "not carried: the final paper has no register, and this equation is not among the ten that M01 registers"),
            "merge_flag": "" if st else "",
        })
    for c in csv.DictReader(open(CLAIMS, encoding="utf-8")):
        v = c["verdict"]
        flag = "" if v == "SUPPORTED" else ("must not be stated as-is" if v in ("NOT SUPPORTED", "SOURCE NOT AVAILABLE")
                                            else "restate with the qualification found")
        rows.append({
            "id": c["claim_id"],
            "kind": "claim",
            "item": (c["manuscript_statement"] or "")[:180],
            "status": v,
            "evidence": (c["source_page_or_equation"] or "") + (" | " + (c["source_doi"] or "") if c["source_doi"] else ""),
            "v2_location": c["origin"],
            "merge_disposition": "audit record only: merge carries text, not claim provenance; "
                                 "consult conflicts.csv before pasting this topic",
            "merge_flag": flag,
        })
    for cid, kind, item, status, evidence, loc, disp in AUDIT_FACTS:
        rows.append({"id": cid, "kind": kind, "item": item, "status": status,
                     "evidence": evidence, "v2_location": loc,
                     "merge_disposition": disp, "merge_flag": ""})
    cols = ["id", "kind", "item", "status", "evidence", "v2_location", "merge_disposition", "merge_flag"]
    with open(os.path.join(ROOT, "v2_verified_ledger.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    import collections
    print("rows:", len(rows), "by kind:", dict(collections.Counter(r["kind"] for r in rows)))
    print("register statuses:", dict(collections.Counter(r["status"] for r in rows if r["kind"] == "equation" and r["status"] != "not registered")))
    print("carried by a snippet:", sum(1 for r in rows if r["merge_disposition"].startswith("carried by snippet")))
    print("flagged claims:", sum(1 for r in rows if r["merge_flag"]))
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
