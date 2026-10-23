#!/usr/bin/env python3
"""Dynamically Crossref-check only the two R3e Section 8 sources in CI."""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

import crossref_enrich as cr

EXPECTED_DOIS = {
    "10.1145/321439.321446",
    "10.1145/361953.361969",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map-csv", type=Path, required=True)
    parser.add_argument("--findings-file", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--raw-dir", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--pause", type=float, default=1.0)
    args = parser.parse_args()

    mappings = read_csv(args.map_csv)
    dois = [row.get("doi", "").strip() for row in mappings]
    if len(mappings) != 2 or len(set(dois)) != 2 or set(dois) != EXPECTED_DOIS:
        raise ValueError(f"R3e must contain exactly the two authorized DOI rows; got {dois}")
    if any(row.get("include", "").strip().upper() != "YES" for row in mappings):
        raise ValueError("Both requested R3e sources must remain explicitly mapped")

    findings = args.findings_file.read_text(encoding="utf-8").lower()
    required_facts = (
        "10.1145/321439.321446", "eq 15", "trapezoidal rule", "t=2 t_max",
        "10.1145/361953.361969", "n even", "v_i", "rounding errors dominate",
    )
    absent = [fact for fact in required_facts if fact not in findings]
    if absent:
        raise ValueError("Pinned FULLTEXT_FINDINGS_09.md is missing required source facts: " + ", ".join(absent))

    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    request_log = args.report_dir / "CROSSREF_R3E_REQUEST_LOG.csv"
    responses: dict[str, tuple[int, dict | None]] = {}
    with request_log.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["DOI", "HTTP_status", "timestamp_utc", "metadata_json", "error"])
        for number, doi in enumerate(sorted(dois), 1):
            print(f"R3e Crossref {number}/2: {doi}", flush=True)
            responses[doi] = cr._fetch_r3a(doi, args.raw_dir, writer, args.pause)

    existing = cr.parse_bib(args.local_bib)
    by_key = {entry["key"]: entry for entry in existing}
    by_doi: dict[str, list[dict[str, str]]] = {}
    for entry in existing:
        doi = entry.get("doi", "").strip().lower()
        if doi:
            by_doi.setdefault(doi, []).append(entry)

    output: list[dict[str, str]] = []
    bib = ["% R3e entries: exact requested DOI rows only; Crossref VERIFIED and bibliography-ready only.", ""]
    bib_keys: set[str] = set()
    for mapping in mappings:
        doi = mapping["doi"].strip()
        key = mapping["citekey"].strip()
        status_http, message = responses[doi]
        title_values = (message or {}).get("title") or []
        cross_title = title_values[0] if title_values else ""
        venues = ((message or {}).get("container-title") or []) + ((message or {}).get("short-container-title") or [])
        cross_years = cr._crossref_years(message or {})
        overlap, substring = cr._title_overlap(mapping["title"], cross_title)
        exact_title = bool(cross_title) and cr._normal_metadata(mapping["title"]) == cr._normal_metadata(cross_title)
        title_ok = bool(cross_title) and (exact_title or substring or overlap >= .60)
        try:
            base_year = int(mapping["year"])
        except ValueError:
            base_year = 0
        year_delta = min((abs(base_year - int(year)) for year in cross_years if year.isdigit()), default=None)
        year_ok = year_delta is not None and year_delta <= 1
        year_exact = str(base_year) in cross_years
        venue_ok = cr._venue_matches(mapping["venue"], venues)
        doi_ok = (message or {}).get("DOI", "").strip().lower() == doi.lower()
        status = (
            "NOT-FOUND" if status_http == 404 else
            "VERIFIED" if status_http == 200 and doi_ok and title_ok and year_ok and venue_ok else
            "MISMATCH"
        )
        reasons = []
        if status_http == 404:
            reasons.append("Crossref returned HTTP 404")
        else:
            if status_http != 200:
                reasons.append(f"Crossref HTTP status {status_http}, expected 200")
            if not doi_ok:
                reasons.append("Crossref DOI differs from requested DOI")
            if not title_ok:
                reasons.append(f"title overlap={overlap:.2f} (<0.60)")
            elif not exact_title:
                reasons.append(f"title accepted under relaxed overlap/substring rule ({overlap:.2f})")
            if not year_ok:
                reasons.append(f"base year {base_year} not within one year of Crossref years {', '.join(sorted(cross_years))}")
            elif not year_exact:
                reasons.append(f"base year differs by {year_delta} year(s)")
            if not venue_ok:
                reasons.append("normalized venue does not match Crossref container title")

        resolved = ""
        bib_ready = "NO"
        scope = ""
        same_doi = by_doi.get(doi.lower(), [])
        target_key = same_doi[0]["key"] if same_doi else key
        if status == "VERIFIED":
            authors = cr.authors_from_message(message or {})
            conflict = target_key in by_key and by_key[target_key].get("doi", "").strip().lower() != doi.lower()
            if not authors:
                reasons.append("Crossref author metadata empty; no BibTeX citation emitted")
            elif conflict:
                reasons.append(f"BibTeX key {target_key} belongs to another DOI")
            else:
                resolved = target_key
                bib_ready = "YES"
                scope = "PRIMARY-SOURCE-CHECKED"
                if target_key not in bib_keys:
                    bib.append(cr._bib_from_crossref(target_key, doi, message or {}))
                    bib.append("")
                    bib_keys.add(target_key)

        output.append({
            "map_id": mapping.get("map_id", ""),
            "citekey": key,
            "resolved_citekey": resolved,
            "DOI": doi,
            "status": status,
            "HTTP_status": str(status_http),
            "claim_status": mapping.get("claim_status", ""),
            "title_match": "YES" if exact_title else "NO",
            "title_overlap": f"{overlap:.2f}",
            "title_acceptable": "YES" if title_ok else "NO",
            "year_match": "YES" if year_exact else "NO",
            "year_acceptable": "YES" if year_ok else "NO",
            "year_delta": "" if year_delta is None else str(year_delta),
            "venue_match": "YES" if venue_ok else "NO",
            "base_title": mapping.get("title", ""),
            "base_venue": mapping.get("venue", ""),
            "crossref_title": cross_title,
            "crossref_years": "; ".join(sorted(cross_years)),
            "crossref_venue": "; ".join(venues),
            "raw_json": str(args.raw_dir / (cr.safe_doi(doi) + ".json")),
            "citation_scope": scope,
            "bib_ready": bib_ready,
            "reason": "; ".join(reasons),
        })

    verify_path = args.report_dir / "CROSSREF_R3E_VERIFY.csv"
    with verify_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(output[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)
    (args.report_dir / "R3E_VERIFIED_REFERENCES.bib").write_text("\n".join(bib), encoding="utf-8")

    title_checks = [row for row in output if row["status"] == "MISMATCH" and row["title_acceptable"] == "NO"]
    human_lines = ["# R3e Crossref title human checks", "", "Rows failing the relaxed 0.60 shorter-title overlap threshold.", ""]
    human_lines += ([f"- {row['citekey']} ({row['DOI']}); overlap {row['title_overlap']}; base: {row['base_title']}; Crossref: {row['crossref_title']}" for row in title_checks] or ["None."])
    (args.report_dir / "CROSSREF_R3E_HUMAN_CHECK.md").write_text("\n".join(human_lines) + "\n", encoding="utf-8")

    counts = Counter(row["status"] for row in output)
    bib_ready = sum(row["bib_ready"] == "YES" for row in output)
    method = f"""# R3e Crossref verification method

Only the two DOI strings explicitly requested for Section 8 were queried: {', '.join(sorted(dois))}. The pinned read-only `FULLTEXT_FINDINGS_09.md` was checked for the equation/method anchors before Crossref requests. Crossref comparison requires a returned DOI match, exact/prefix/substring title or at least 0.60 shorter-title token overlap, a published/issued year within one year, and a normalized container-title match. HTTP 404 is NOT-FOUND. Network/decoding errors fail the job. Only VERIFIED records with Crossref author metadata and no BibTeX DOI conflict are emitted for bibliography merge.

The manuscript claims are limited to the source-checked Eq. (15) cosine-series/trapezoidal inversion and Stehfest's even-N weighted formula and rounding-error trade-off. No behavior inference beyond Stehfest's own statements is used, and no general method ranking is inferred. Rows={len(output)}; DOI requests={len(dois)}; VERIFIED={counts['VERIFIED']}; MISMATCH={counts['MISMATCH']}; NOT-FOUND={counts['NOT-FOUND']}; NO-DOI={counts['NO-DOI']}; bibliography-ready={bib_ready}; new BibTeX keys={len(bib_keys)}.
"""
    (args.report_dir / "CROSSREF_R3E_METHOD.md").write_text(method, encoding="utf-8")
    print(f"R3e rows={len(output)} requests={len(dois)} counts={dict(counts)} bib-ready={bib_ready}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
