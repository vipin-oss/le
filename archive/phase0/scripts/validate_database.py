#!/usr/bin/env python3
"""Validate literature database consistency and completeness.

Checks:
- All required fields present and non-empty
- Study ID format valid (FW-### or RG-###)
- Decision/extraction status consistency
- Cross-file referential integrity
- Verified vs inferred labeling present

Usage:
    python3 scripts/validate_database.py
"""

import csv
import re
import sys
from pathlib import Path

REQUIRED_DB_FIELDS = [
    "study_id", "doi", "title", "authors", "year", "journal",
    "full_text_access_status", "verification_status", "screening_decision",
    "screening_reason",
]
STUDY_ID_PATTERN = re.compile(r"^(FW|RG)-\d{3}$")
VALID_ACCESS = {"ABSTRACT_ONLY", "OPEN_ACCESS", "EXTRACTED"}
VALID_VERIFICATION = {"VERIFIED", "PARTIAL", "UNVERIFIED"}
VALID_DECISIONS = {"INCLUDE", "EXCLUDE", "UNDECIDED"}


def load_csv(path):
    if not Path(path).exists():
        print(f"MISSING: {path}")
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    repo_root = Path(__file__).resolve().parent.parent
    errors = []
    warnings = []

    db_path = repo_root / "phase1" / "04_literature_master_database.csv"
    db = load_csv(db_path)
    if not db:
        print("Literature master database not found — cannot validate")
        sys.exit(1)

    for r in db:
        sid = r.get("study_id", "?")
        # Required fields
        for field in REQUIRED_DB_FIELDS:
            if not r.get(field):
                errors.append(f"{sid}: missing required field '{field}'")
        # Study ID format
        if sid and sid != "?" and not STUDY_ID_PATTERN.match(sid):
            errors.append(f"{sid}: invalid study ID format")
        # Access status
        access = r.get("full_text_access_status", "")
        if access and access not in VALID_ACCESS:
            errors.append(f"{sid}: invalid full_text_access_status '{access}'")
        # Verification status
        verif = r.get("verification_status", "")
        if verif and verif not in VALID_VERIFICATION:
            errors.append(f"{sid}: invalid verification_status '{verif}'")
        # Screening decision
        dec = r.get("screening_decision", "")
        if dec and dec not in VALID_DECISIONS:
            errors.append(f"{sid}: invalid screening_decision '{dec}'")

    # Consistency: screened records match database records
    sc_path = repo_root / "phase1" / "05_screening_decisions.csv"
    sc = load_csv(sc_path)
    ids_db = {r.get("study_id") for r in db if r.get("study_id")}
    ids_sc = {r.get("study_id") for r in sc if r.get("study_id")}
    if ids_sc and ids_sc != ids_db:
        only_in_sc = ids_sc - ids_db
        only_in_db = ids_db - ids_sc
        if only_in_sc:
            errors.append(f"Screening has IDs not in database: {sorted(only_in_sc)}")
        if only_in_db:
            errors.append(f"Database has IDs not in screening: {sorted(only_in_db)}")

    # Consistency: extraction matrix matches database records
    ex_path = repo_root / "phase1" / "06_fulltext_extraction_matrix.csv"
    ex = load_csv(ex_path)
    ids_ex = {r.get("study_id") for r in ex if r.get("study_id")}
    if ids_ex and ids_ex != ids_db:
        only_in_ex = ids_ex - ids_db
        only_in_db2 = ids_db - ids_ex
        if only_in_ex:
            errors.append(f"Extraction has IDs not in database: {sorted(only_in_ex)}")
        if only_in_db2:
            errors.append(f"Database has IDs not in extraction: {sorted(only_in_db2)}")

    # Extraction matrix field validation
    for r in ex:
        sid = r.get("study_id", "?")
        for field in ("equations_extracted", "interface_conditions_extracted",
                      "energy_flux_extracted", "energy_balance_verified", "limiting_cases_checked"):
            val = r.get(field, "")
            if val and val not in ("YES", "NO", "NOT_YET_EXTRACTED"):
                errors.append(f"{sid}: {field} = '{val}' (expected YES/NO/NOT_YET_EXTRACTED)")

    # Excluded records should have exclusion reasons
    for r in sc:
        sid = r.get("study_id", "?")
        if r.get("decision") == "EXCLUDE" and not r.get("reason"):
            errors.append(f"{sid}: EXCLUDE decision without reason")

    # --- Summary ---
    print(f"Database: {len(db)} records")
    cats = {}
    for r in db:
        cats[r.get("screening_decision", "?")] = cats.get(r.get("screening_decision", "?"), 0) + 1
    print(f"  By screening decision: {cats}")
    statuses = {}
    for r in db:
        statuses[r.get("full_text_access_status", "?")] = statuses.get(r.get("full_text_access_status", "?"), 0) + 1
    print(f"  By full-text access status: {statuses}")
    verifs = {}
    for r in db:
        verifs[r.get("verification_status", "?")] = verifs.get(r.get("verification_status", "?"), 0) + 1
    print(f"  By verification status: {verifs}")

    if errors:
        print(f"\nVALIDATION FAILED: {len(errors)} error(s)")
        for e in errors:
            print(f"  ERROR: {e}")
        sys.exit(1)
    print("VALIDATION PASSED: no errors")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for w in warnings:
            print(f"  WARN: {w}")


if __name__ == "__main__":
    main()
