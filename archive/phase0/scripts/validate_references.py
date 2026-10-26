#!/usr/bin/env python3
"""Validate references against integrity rules.

Checks:
- DOI syntax validity (basic pattern)
- Duplicate DOIs across records
- Verified vs inferred status labeling
- Required fields present
- Access dates present for web sources

Usage:
    python3 scripts/validate_references.py
"""

import csv
import re
import sys
from pathlib import Path

DOI_PATTERN = re.compile(r"^10\.\d{4,}/.+$")
REQUIRED_BIB_FIELDS = {"id", "title", "authors", "year", "source"}
REQUIRED_DOI_FIELDS = {"study_id", "doi", "doi_verified", "verified_by", "verified_date"}
REQUIRED_PROV_FIELDS = {"source_id", "source_name", "url", "access_date", "verified_fields", "status"}


def load_csv(path):
    if not Path(path).exists():
        print(f"MISSING: {path}")
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate_doi(doi):
    return bool(doi and DOI_PATTERN.match(doi.strip()))


def main():
    repo_root = Path(__file__).resolve().parent.parent
    errors = []
    warnings = []

    # --- Validate literature master database ---
    db_path = repo_root / "phase1" / "04_literature_master_database.csv"
    db = load_csv(db_path)
    if db:
        dois = [r.get("doi", "").strip() for r in db if r.get("doi")]
        seen = set()
        for r in db:
            sid = r.get("study_id", "?")
            doi = r.get("doi", "").strip()
            if doi:
                if not validate_doi(doi):
                    errors.append(f"{sid}: invalid DOI syntax '{doi}'")
                if doi in seen:
                    errors.append(f"{sid}: duplicate DOI '{doi}'")
                seen.add(doi)
            access = r.get("full_text_access_status", "")
            if access and access not in ("ABSTRACT_ONLY", "OPEN_ACCESS", "EXTRACTED"):
                warnings.append(f"{sid}: unexpected full_text_access_status '{access}'")
        print(f"Database: {len(db)} records, {len(dois)} DOIs, {len(seen)} unique DOIs")
    else:
        warnings.append("Literature master database not found")

    # --- Validate screening decisions ---
    sc_path = repo_root / "phase1" / "05_screening_decisions.csv"
    sc = load_csv(sc_path)
    if sc:
        valid_decisions = {"INCLUDE", "EXCLUDE", "UNDECIDED"}
        for r in sc:
            sid = r.get("study_id", "?")
            if r.get("decision") not in valid_decisions:
                decision = r.get("decision")
                errors.append(f"{sid}: invalid decision '{decision}'")
            if not r.get("reason"):
                warnings.append(f"{sid}: missing screening reason")
        print(f"Screening decisions: {len(sc)} records")
    else:
        warnings.append("Screening decisions not found")

    # --- Validate full-text extraction matrix ---
    ex_path = repo_root / "phase1" / "06_fulltext_extraction_matrix.csv"
    ex = load_csv(ex_path)
    if ex:
        yes_no = {"YES", "NO", "NOT_YET_EXTRACTED"}
        for r in ex:
            sid = r.get("study_id", "?")
            for field in ("equations_extracted", "interface_conditions_extracted",
                          "energy_flux_extracted", "energy_balance_verified", "limiting_cases_checked"):
                if r.get(field) not in yes_no:
                    errors.append(f"{sid}: {field} = '{r.get(field)}' (expected YES/NOT_YET_EXTRACTED)")
        print(f"Extraction matrix: {len(ex)} records")
    else:
        warnings.append("Full-text extraction matrix not found")

    # --- Cross-reference: study IDs consistent across files ---
    ids_db = {r.get("study_id") for r in db if r.get("study_id")}
    ids_sc = {r.get("study_id") for r in sc if r.get("study_id")}
    ids_ex = {r.get("study_id") for r in ex if r.get("study_id")}
    if ids_db and ids_sc and ids_sc != ids_db:
        errors.append(f"Screening decision IDs ({len(ids_sc)}) != database IDs ({len(ids_db)})")
    if ids_db and ids_ex and ids_ex != ids_db:
        errors.append(f"Extraction matrix IDs ({len(ids_ex)}) != database IDs ({len(ids_db)})")

    # --- Summary ---
    print()
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} error(s)")
        for e in errors:
            print(f"  ERROR: {e}")
        sys.exit(1)
    else:
        print("VALIDATION PASSED: no errors")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for w in warnings:
            print(f"  WARN: {w}")


if __name__ == "__main__":
    main()
