#!/usr/bin/env python3
"""Fetch and compare Crossref metadata for R3b plan sections (5–9, 11–13)."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import time
from pathlib import Path

import crossref_enrich as cr

R3B_SECTIONS = {f"s.{number}" for number in (*range(5, 10), *range(11, 14))}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def verify_one(plan: dict[str, str], base: dict[str, str], http_status: int,
               message: dict | None, raw_path: str, row_index: dict[str, dict[str, str]],
               citation_map: dict[str, list[str]], bib_by_doi: dict[str, list[dict[str, str]]],
               bib_by_key: dict[str, dict[str, str]], verified_bib: list[str],
               bib_written: set[str]) -> dict[str, str]:
    lit_id = plan.get("lit_id", "")
    key = plan.get("citekey", "").strip()
    doi = base.get("DOI", "").strip()
    eligible = plan.get("technical_claim_eligible", "").strip().upper() == "YES"
    if not eligible:
        return {"lit_id": lit_id, "citekey": key, "resolved_citekey": "", "section": plan.get("plan_section", ""),
                "DOI": doi, "status": "INELIGIBLE", "title_match": "NO", "title_overlap": "", "title_acceptable": "NO",
                "year_match": "NO", "year_acceptable": "NO", "year_delta": "", "venue_match": "NO", "base_title": base.get("title", ""),
                "base_venue": base.get("venue", ""), "crossref_title": "", "crossref_year": "", "crossref_years": "",
                "crossref_venue": "", "technical_claim_eligible": "NO", "read_level": plan.get("read_level", ""),
                "prior_api_log": "NOT_QUERIED_INELIGIBLE", "citation_map_claims": "; ".join(sorted(set(citation_map.get(key, [])))),
                "raw_json": "", "reclassified_from": "", "reason": "technical_claim_eligible is not YES; no Crossref request or technical citation",
                "citation_scope": "", "bib_ready": "NO"}
    if http_status == 0:
        return {"lit_id": lit_id, "citekey": key, "resolved_citekey": "", "section": plan.get("plan_section", ""),
                "DOI": "", "status": "NO-DOI", "title_match": "NO", "title_overlap": "0.00", "title_acceptable": "NO",
                "year_match": "NO", "year_acceptable": "NO", "year_delta": "", "venue_match": "NO", "base_title": base.get("title", ""),
                "base_venue": base.get("venue", ""), "crossref_title": "", "crossref_year": "", "crossref_years": "",
                "crossref_venue": "", "technical_claim_eligible": "YES" if eligible else "NO", "read_level": plan.get("read_level", ""),
                "prior_api_log": "NO_DOI", "citation_map_claims": "; ".join(sorted(set(citation_map.get(key, [])))),
                "raw_json": "", "reclassified_from": "", "reason": "no DOI recorded; not Crossref-verifiable; keep uncited under this phase",
                "citation_scope": "", "bib_ready": "NO"}

    cross_title_values = (message or {}).get("title") or []
    cross_title = cross_title_values[0] if cross_title_values else ""
    cross_venues = ((message or {}).get("container-title") or []) + ((message or {}).get("short-container-title") or [])
    base_title = base.get("title", "")
    exact_title = bool(cross_title) and cr._normal_metadata(base_title) == cr._normal_metadata(cross_title)
    overlap, substring = cr._title_overlap(base_title, cross_title)
    title_acceptable = exact_title or substring or overlap >= 0.60
    matching_years = cr._crossref_years(message or {})
    try:
        base_year = int(base.get("year", "").strip())
    except ValueError:
        base_year = 0
    year_delta = min((abs(base_year - int(year)) for year in matching_years if year.isdigit()), default=None)
    exact_year = str(base_year) in matching_years
    year_acceptable = year_delta is not None and year_delta <= 1
    venue_acceptable = cr._venue_matches(base.get("venue", ""), cross_venues)
    doi_match = (message or {}).get("DOI", "").strip().lower() == doi.lower()
    status = "NOT-FOUND" if http_status == 404 else (
        "VERIFIED" if doi_match and title_acceptable and year_acceptable and venue_acceptable else "MISMATCH")
    reason: list[str] = []
    if http_status == 404:
        reason.append("Crossref returned HTTP 404")
    else:
        if not doi_match:
            reason.append("Crossref DOI field differs from requested DOI")
        if not exact_title:
            if title_acceptable:
                why = "prefix/substring" if substring else "shorter-title token coverage"
                reason.append(f"title accepted under relaxed rule: overlap={overlap:.2f}; {why}")
            else:
                reason.append(f"title overlap={overlap:.2f} (<0.60); needs human check")
        if not exact_year:
            if year_acceptable:
                reason.append(f"base year differs by {year_delta} year(s) from Crossref published/issued years {', '.join(sorted(matching_years))}")
            else:
                reason.append(f"base year {base_year} differs by >1 year from Crossref published/issued years {', '.join(sorted(matching_years))}")
        if not venue_acceptable:
            reason.append("normalized venue does not match Crossref container-title/short-container-title")
    prior = "NOT_IN_INDEX"
    if lit_id in row_index:
        prior = "HISTORICAL_HTTP_" + row_index[lit_id].get("http_status", "UNKNOWN")
    claims = "; ".join(sorted(set(citation_map.get(key, []))))
    resolved_key = ""
    bib_ready = "NO"
    citation_scope = ""
    if status == "VERIFIED" and eligible and key and cr.authors_from_message(message or {}):
        existing_for_doi = bib_by_doi.get(doi.lower(), [])
        target_key = existing_for_doi[0]["key"] if existing_for_doi else key
        conflict = target_key in bib_by_key and bib_by_key[target_key].get("doi", "").strip().lower() != doi.lower()
        if not conflict:
            resolved_key = target_key
            bib_ready = "YES"
            citation_scope = "technical"
            if target_key not in bib_written:
                verified_bib.append(cr._bib_from_crossref(target_key, doi, message or {}))
                verified_bib.append("")
                bib_written.add(target_key)
        else:
            reason.append(f"citekey {target_key} already belongs to a different DOI")
    elif status == "VERIFIED" and eligible and not cr.authors_from_message(message or {}):
        reason.append("Crossref author metadata is empty; do not emit BibTeX")
    elif status == "VERIFIED" and eligible and not key:
        reason.append("REFERENCE_PLAN has no citekey; do not emit BibTeX")
    return {"lit_id": lit_id, "citekey": key, "resolved_citekey": resolved_key,
            "section": plan.get("plan_section", ""), "DOI": doi, "status": status,
            "title_match": "YES" if exact_title else "NO", "title_overlap": f"{overlap:.2f}",
            "title_acceptable": "YES" if title_acceptable else "NO", "year_match": "YES" if exact_year else "NO",
            "year_acceptable": "YES" if year_acceptable else "NO", "year_delta": "" if year_delta is None else str(year_delta),
            "venue_match": "YES" if venue_acceptable else "NO", "base_title": base_title, "base_venue": base.get("venue", ""),
            "crossref_title": cross_title, "crossref_year": cr.crossref_issued_year(message or {}),
            "crossref_years": "; ".join(sorted(matching_years)), "crossref_venue": "; ".join(cross_venues),
            "technical_claim_eligible": "YES" if eligible else "NO", "read_level": plan.get("read_level", ""),
            "prior_api_log": prior, "citation_map_claims": claims, "raw_json": raw_path, "reclassified_from": "",
            "reason": "; ".join(reason), "citation_scope": citation_scope, "bib_ready": bib_ready}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-csv", type=Path, required=True)
    parser.add_argument("--plan-csv", type=Path, required=True)
    parser.add_argument("--citation-map-csv", type=Path, required=True)
    parser.add_argument("--row-index-csv", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--raw-dir", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--pause", type=float, default=1.0)
    args = parser.parse_args()

    base_rows = read_csv(args.base_csv)
    plan_rows = read_csv(args.plan_csv)
    citation_rows = read_csv(args.citation_map_csv)
    row_index = {row.get("id", ""): row for row in read_csv(args.row_index_csv)}
    base_by_id = {row.get("id", ""): row for row in base_rows}
    if len(base_by_id) != len(base_rows):
        raise ValueError("LITERATURE_BASE contains duplicate ids")
    scoped = [row for row in plan_rows if row.get("plan_section", "").strip() in R3B_SECTIONS]
    missing = sorted({row.get("lit_id", "") for row in scoped} - set(base_by_id))
    if missing:
        raise ValueError("R3b REFERENCE_PLAN ids missing from LITERATURE_BASE: " + ", ".join(missing))
    for row in scoped:
        indexed = row_index.get(row.get("lit_id", ""))
        if indexed and indexed.get("DOI", "").strip().lower() != base_by_id[row["lit_id"]].get("DOI", "").strip().lower():
            raise ValueError(f"Historical DOI conflicts with LITERATURE_BASE for {row['lit_id']}")

    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    doi_by_row = {row["lit_id"]: base_by_id[row["lit_id"]].get("DOI", "").strip() for row in scoped}
    eligible_ids = {row["lit_id"] for row in scoped if row.get("technical_claim_eligible", "").strip().upper() == "YES"}
    dois = sorted({doi_by_row[lit_id] for lit_id in eligible_ids if cr.DOI_RE.match(doi_by_row[lit_id])})
    log_path = args.report_dir / "CROSSREF_R3B_REQUEST_LOG.csv"
    messages: dict[str, tuple[int, dict | None]] = {}
    with log_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["DOI", "HTTP_status", "timestamp_utc", "metadata_json", "error"])
        for index, doi in enumerate(dois, 1):
            print(f"R3b Crossref {index}/{len(dois)}: {doi}", flush=True)
            messages[doi] = cr._fetch_r3a(doi, args.raw_dir, writer, args.pause)

    citation_map: dict[str, list[str]] = {}
    for row in citation_rows:
        for key in re.split(r"[;,]\s*", row.get("proposed_citations", "")):
            if key.strip():
                citation_map.setdefault(key.strip(), []).append(row.get("claim_id", ""))
    existing_entries = cr.parse_bib(args.local_bib)
    bib_by_key = {entry["key"]: entry for entry in existing_entries}
    bib_by_doi: dict[str, list[dict[str, str]]] = {}
    for entry in existing_entries:
        if entry.get("doi", "").strip():
            bib_by_doi.setdefault(entry["doi"].strip().lower(), []).append(entry)

    bib_lines = ["% R3b entries: Crossref VERIFIED and REFERENCE_PLAN technical_claim_eligible=YES only.",
                 "% Bibliographic fields come from the saved Crossref metadata response.", ""]
    bib_written: set[str] = set()
    rows_out: list[dict[str, str]] = []
    for plan in scoped:
        lit_id = plan["lit_id"]
        base = base_by_id[lit_id]
        doi = doi_by_row[lit_id]
        if lit_id not in eligible_ids:
            rows_out.append(verify_one(plan, base, 0, None, "", row_index, citation_map,
                                       bib_by_doi, bib_by_key, bib_lines, bib_written))
            continue
        if not cr.DOI_RE.match(doi):
            rows_out.append(verify_one(plan, base, 0, None, "", row_index, citation_map,
                                       bib_by_doi, bib_by_key, bib_lines, bib_written))
            continue
        http_status, message = messages[doi]
        raw_path = str(args.raw_dir / (cr.safe_doi(doi) + ".json"))
        rows_out.append(verify_one(plan, base, http_status, message, raw_path, row_index, citation_map,
                                   bib_by_doi, bib_by_key, bib_lines, bib_written))

    fields = list(rows_out[0]) if rows_out else []
    verify_path = args.report_dir / "CROSSREF_R3B_VERIFY.csv"
    with verify_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows_out)
    bib_path = args.report_dir / "R3B_VERIFIED_REFERENCES.bib"
    bib_path.write_text("\n".join(bib_lines), encoding="utf-8")

    human = [row for row in rows_out if row["status"] == "MISMATCH" and row["title_match"] == "NO" and row["title_acceptable"] == "NO"]
    human_lines = ["# R3b Crossref title human checks", "", "Only DOI-returned title pairs below the relaxed 0.60 threshold are listed.", ""]
    if human:
        human_lines.extend(f"- {row['lit_id']} `{row['citekey']}` — overlap {row['title_overlap']}; base: {row['base_title']}; Crossref: {row['crossref_title']}; {row['reason']}" for row in human)
    else:
        human_lines.append("None.")
    (args.report_dir / "CROSSREF_R3B_HUMAN_CHECK.md").write_text("\n".join(human_lines) + "\n", encoding="utf-8")

    status_counts = {status: sum(row["status"] == status for row in rows_out) for status in ("VERIFIED", "MISMATCH", "NOT-FOUND", "NO-DOI", "INELIGIBLE")}
    eligible_count = sum(row["technical_claim_eligible"] == "YES" for row in rows_out)
    method_doi_rows = sum(row["status"] != "INELIGIBLE" and row["status"] != "NO-DOI" for row in rows_out)
    method = f"""# R3b Crossref verification method

Scope: REFERENCE_PLAN plan_section s.5–s.9 and s.11–s.13 (Section 10 is reserved for R3c). Each plan `lit_id` joins to `LITERATURE_BASE.id`; only `technical_claim_eligible=YES` rows are queried, using the capitalized `DOI` field. Ineligible rows remain in the audit as `INELIGIBLE` and generate no request. The frozen CITATION_MAP is consulted for exact claim-to-key matches. New manuscript placements use the local `R3B_CITATION_MAP.csv`, which maps these eligible plan keys to section-specific source claims; metadata-only rows are never used as technical evidence.

The comparison uses the same relaxed R3a criteria: title is acceptable when exact, a prefix/substring, or shared-token coverage of at least 0.60 of the shorter title; the base year may match a published-print/online/issued year or differ by at most one year; the normalized venue must match Crossref container-title/short-container-title; requested DOI must equal returned DOI. Crossref title overlap under 0.60 is MISMATCH and listed in `CROSSREF_R3B_HUMAN_CHECK.md`. A 404 is NOT-FOUND; no DOI is NO-DOI. Network/decoding errors fail the job.

Only VERIFIED `technical_claim_eligible=YES` rows with Crossref authors and no BibTeX-key/DOI conflict enter `R3B_VERIFIED_REFERENCES.bib` and the conditional citation map. BibTeX year uses Crossref `issued` year (published-print/online fallback).

Rows: {len(rows_out)}; eligible DOI rows queried: {method_doi_rows}; unique DOI requests: {len(dois)}; eligible rows: {eligible_count}; VERIFIED: {status_counts['VERIFIED']}; MISMATCH: {status_counts['MISMATCH']}; NOT-FOUND: {status_counts['NOT-FOUND']}; NO-DOI: {status_counts['NO-DOI']}; INELIGIBLE (not queried): {status_counts['INELIGIBLE']}; bibliography-ready eligible keys: {len(bib_written)}.
"""
    (args.report_dir / "CROSSREF_R3B_METHOD.md").write_text(method, encoding="utf-8")
    print(f"R3b rows={len(rows_out)}; requests={len(dois)}; results={status_counts}; bib-ready={len(bib_written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
