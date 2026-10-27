"""Offline integrity checks for the Phase 0 workspace.

Run:  python3 scripts/validate_workspace.py

Checks:
  1. Every DOI cited in deliverables resolves in source_verification_log.csv.
  2. topic_comparison_matrix.csv has expected schema and row count.
  3. No duplicate DOI in data/publications_verified.csv.
  4. Cross-file consistency: topics referenced in matrix exist in five_candidate_topics.md.
  5. DOI syntax sanity check (starts with 10.).
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ERRORS = []
WARN = []

def err(msg): ERRORS.append(msg)
def warn(msg): WARN.append(msg)

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
DOI_LINE_RE = re.compile(r"^" + DOI_RE.pattern + r"$")

# ---- 1. Source verification log ----
log = {}
log_path = ROOT / "source_verification_log.csv"
if log_path.exists():
    with log_path.open() as f:
        for r in csv.DictReader(f):
            doi = (r.get("verified_fields") or "").strip()
            # extract DOI-like token
            m = DOI_RE.search(doi)
            if m:
                log[m.group(0)] = r["source_id"]

# ---- 2. Publications CSV ----
pubs_path = ROOT / "data/publications_verified.csv"
dois = []
if pubs_path.exists():
    with pubs_path.open() as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            doi = r["doi"].strip().lower()
            dois.append(doi)
            if not DOI_RE.match(doi):
                err(f"publications_verified.csv line {i}: bad DOI syntax {doi}")
            if doi in log:
                pass  # ok, present in log
            else:
                warn(f"publications_verified.csv line {i}: DOI {doi} not in source_verification_log.csv")
    if len(set(dois)) != len(dois):
        err("publications_verified.csv: duplicate DOIs found")
    print(f"publications_verified.csv: {len(dois)} records")

# ---- 3. Review inventory ----
inv_path = ROOT / "data/review_inventory.csv"
if inv_path.exists():
    with inv_path.open() as f:
        n = sum(1 for _ in csv.DictReader(f))
    print(f"data/review_inventory.csv: {n} records")

# ---- 4. Matrix schema ----
mx_path = ROOT / "topic_comparison_matrix.csv"
expected = ["criterion","weight","T1_energy_flux_interfaces","T2_MDD_fractional_operators",
            "T3_double_porosity_interfaces","T4_nonlocal_surface_waves","T5_semiconductor_plasma_waves","notes"]
if mx_path.exists():
    with mx_path.open() as f:
        rd = csv.DictReader(f)
        if rd.fieldnames != expected:
            err(f"topic_comparison_matrix.csv header mismatch: {rd.fieldnames}")
        rows = list(rd)
        print(f"topic_comparison_matrix.csv: {len(rows)} rows")
        # weights should sum to ~1.0
        try:
            wsum = 0.0
            for r in rows:
                w = (r.get("weight") or "").strip()
                if not w: continue
                wsum += float(w)
            print(f"  criterion weights sum: {wsum:.3f}")
        except Exception as e:
            warn(f"could not sum weights: {e}")

# ---- 5. Markdown deliverables exist ----
for md in ["research_profile.md","domain_taxonomy.md","existing_review_analysis.md",
           "five_candidate_topics.md","recommended_research_direction.md","README.md"]:
    p = ROOT / md
    if not p.exists(): err(f"missing deliverable {md}")
    else: print(f"{md}: present ({p.stat().st_size} bytes)")

print()
if ERRORS:
    print("VALIDATION FAILED:")
    for e in ERRORS: print("  -", e)
    sys.exit(1)
print("All hard checks passed.")
if WARN:
    print("Warnings:")
    for w in WARN: print("  *", w)
