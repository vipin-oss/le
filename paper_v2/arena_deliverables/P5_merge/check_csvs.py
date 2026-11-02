#!/usr/bin/env python3
"""Validate the P5 CSV deliverables: required columns, unique ids, non-empty cells,
and that every location named in a row resolves to a real source file.

Final-paper locations are resolved against final_labels.csv (harvested from the final
sources); v2 locations against the working tree. Prints PASS, exit 0.
"""
import csv, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))

required = {
    "conflicts.csv": ["id", "topic", "severity", "final_location", "final_wording",
                      "v2_location", "v2_wording", "matches_source", "evidence",
                      "recommendation", "action_in_merge"],
    "from_v2_missing_in_final.csv": ["id", "priority", "item", "snippet_file", "v2_source",
                                     "status_in_v2", "why_absent_in_final", "absence_evidence",
                                     "placement", "new_labels", "est_pages", "note"],
    "section_map.csv": ["final_file", "v2_file", "overlap"],
}
final_files = {r["final_file"] for r in csv.DictReader(open(os.path.join(ROOT, "final_labels.csv"), encoding="utf-8"))}
# cells that are legitimately empty: section_map marks "no equivalent" rows with blanks
nullable = {
    "section_map.csv": {"v2_file", "v2_section_title", "shared_cite_keys", "cite_jaccard",
                        "v2_words", "note"},
}

errors, checked = [], 0

for name, cols in required.items():
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        errors.append(f"{name}: missing")
        continue
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    got = list(rows[0].keys()) if rows else []
    for c in cols:
        if c not in got:
            errors.append(f"{name}: column {c!r} missing")
    ids = [r.get("id") or r.get("final_file") for r in rows]
    if len(ids) != len(set(ids)):
        errors.append(f"{name}: duplicate ids")
    for r in rows:
        checked += 1
        for c in got:
            if not (r.get(c) or "").strip() and c not in nullable.get(name, set()):
                errors.append(f"{name}: empty cell {c!r} in row {r.get('id')}")
        # resolve final-paper file references
        for f in re.findall(r"(?:sections|tables|figs_tikz)/[A-Za-z0-9_.]+\.tex", r.get("final_location", "")):
            if f not in final_files:
                errors.append(f"{name}: {r.get('id')}: unknown final file {f}")
        # resolve v2 file references
        for f in re.findall(r"(?:sections|appendices|frontmatter)/[A-Za-z0-9_.]+\.tex", r.get("v2_location", "")):
            if not os.path.exists(os.path.join(REPO, "paper_v2", "manuscript_v2", "master", f)):
                errors.append(f"{name}: {r.get('id')}: unknown v2 file {f}")
        snip = r.get("snippet_file", "")
        if snip and not os.path.exists(os.path.join(ROOT, snip)):
            errors.append(f"{name}: {r.get('id')}: snippet missing {snip}")
print(f"rows checked: {checked}")
if errors:
    print(f"{len(errors)} problem(s):")
    for e in errors:
        print("  -", e)
    print("FAIL")
    sys.exit(1)
print("PASS")
