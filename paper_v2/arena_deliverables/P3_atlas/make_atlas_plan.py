#!/usr/bin/env python3
"""Build atlas_plan.csv (Task 5): a proposed stratified sample of 40 published
wave-propagation problems, drawn only from papers already present in
paper_v2/verification_register.csv (so every DOI is one the project has already
catalogued - no DOI is invented here).

Nothing is written into the atlas itself; this is a sampling plan.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, "..", "..", "verification_register.csv"))
OUT = os.path.join(HERE, "atlas_plan.csv")

# keyword -> wave family, first match wins
RULES = [
    ("TED / damping", r"damping|resonator|quality factor|thermoelastic damping"),
    ("shear / SH", r"\bSH\b|love wave|shear wave|torsional"),
    ("surface (Rayleigh)", r"rayleigh|surface wave|surface acoustic"),
    ("Lamb / plate", r"\blamb\b|plate|shell|beam|waveguide|nanoshell"),
    ("interface / layered", r"reflect|transmis|interface|layer|bilayer|bonded|trilayer|tri-layered|half-space|seabed|tunnel"),
    ("porous / voids", r"porous|poro|void"),
    ("multifield", r"piezo|magnet|flexo|photo|hygro|semiconductor|thermoelectric|quasicrystal|electro"),
    ("bulk", r"."),
]
QUOTA = {"bulk": 8, "surface (Rayleigh)": 6, "Lamb / plate": 4,
         "interface / layered": 7, "shear / SH": 3, "porous / voids": 5,
         "multifield": 5, "TED / damping": 2}
# what our second-implementation benchmark could check against a paper of this family
TEST = {
    "bulk": "two-branch dispersion vs the paper's secular equation; front speeds",
    "surface (Rayleigh)": "Rayleigh secular determinant / speed ratio vs the paper's closed form",
    "Lamb / plate": "Lamb A0/S0 dispersion vs the paper's plate determinant (elastic limit)",
    "interface / layered": "Snell/reflection coefficients and energy flux continuity",
    "shear / SH": "SH dispersion and cut-off frequencies",
    "porous / voids": "number of propagating branches and their high-frequency limits",
    "multifield": "coupled piezo/magneto branch speeds vs the paper's secular equation",
    "TED / damping": "Q^-1 peak position and height vs the paper's Debye-type expression",
}


def family(title):
    t = title.lower()
    for name, pat in RULES:
        if re.search(pat, t, re.I):
            return name
    return "bulk"


def geometry(title):
    t = title.lower()
    if "cylind" in t or "tunnel" in t:
        return "cylindrical"
    if "plate" in t or "shell" in t or "beam" in t:
        return "plate/shell"
    if "layer" in t or "bilayer" in t or "half-space" in t or "seabed" in t:
        return "layered half-space"
    if "sphere" in t:
        return "spherical"
    return "unstated in title"


def model(title):
    t = title.lower()
    tags = []
    for k, pat in [("MGT", r"moore-gibson-thompson|MGT"),
                   ("three-phase-lag", r"three-phase-lag|3P"),
                   ("dual-phase-lag", r"dual-phase-lag|DPL"),
                   ("Lord-Shulman", r"lord-shulman|LS\b"),
                   ("Green-Naghdi", r"green-naghdi|GN-"),
                   ("fractional", r"fractional"),
                   ("memory-dependent", r"memory"),
                   ("nonlocal", r"nonlocal"),
                   ("micropolar", r"micropolar"),
                   ("Klein-Gordon", r"klein-gordon"),
                   ("size-dependent", r"size-dependent|strain gradient|couple stress"),
                   ("two-temperature", r"two temperature|two-temperature")]:
        if re.search(pat, t, re.I):
            tags.append(k)
    return "+".join(tags) if tags else "classical/generalized coupled (title gives no lag model)"


def main():
    rows = list(csv.DictReader(open(REG, newline="")))
    cand = []
    for r in rows:
        year = (r.get("year") or "").strip()
        doi = (r.get("doi") or "").strip()
        title = (r.get("title") or "").strip()
        if not doi.startswith("10.") or not year.isdigit() or not title:
            continue
        if int(year) < 2000 or int(year) > 2026:
            continue
        if len(title) < 25:
            continue
        cand.append(dict(bibkey=r["bibkey"], doi=doi, title=title, year=year,
                         level=r.get("verification_level") or "",
                         family=family(title)))
    total = sum(QUOTA.values())
    picked, counts = [], {k: 0 for k in QUOTA}
    for c in cand:                       # register order is the deterministic order
        if counts[c["family"]] < QUOTA[c["family"]]:
            counts[c["family"]] += 1
            picked.append(c)
        if len(picked) == total:
            break
    # some strata are thinner than their quota in a 119-entry register: top up from
    # the remaining candidates in register order and say so in the README
    if len(picked) < total:
        taken = {c["bibkey"] + c["doi"] for c in picked}
        for c in cand:
            if c["bibkey"] + c["doi"] in taken:
                continue
            counts[c["family"]] += 1
            picked.append(c)
            if len(picked) == total:
                break
    if len(picked) < total:
        print("FAIL only %d candidates for a quota of %d" % (len(picked), total))
        return 1
    with open(OUT, "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["problem_id", "wave_family", "bibkey", "DOI", "title", "year",
                     "model_as_titled", "geometry_as_titled",
                     "validation_target_proposed", "evidence_basis",
                     "full_text_read", "in_current_atlas", "gap_note", "priority"])
        for i, c in enumerate(picked, 1):
            wr.writerow([
                "AT-%02d" % i, c["family"], c["bibkey"], c["doi"], c["title"], c["year"],
                model(c["title"]), geometry(c["title"]),
                TEST[c["family"]],
                "register metadata + title only (verification level %s)" % (c["level"] or "unstated"),
                "no",
                "no",
                "no experimental or damping-vs-frequency counterpart in the current atlas"
                if c["family"] != "TED / damping"
                else "needs a measured Q^-1 curve, not only a formula",
                "high" if c["family"] in ("bulk", "surface (Rayleigh)", "TED / damping") else "medium",
            ])
    print("wrote %s: %d rows, family counts %s" % (OUT, len(picked), counts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
