#!/usr/bin/env python3
"""Verify R3c Section 10 candidates in Actions; Section 4.11 has no eligible row."""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

import crossref_enrich as cr


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-csv", type=Path, required=True)
    parser.add_argument("--plan-csv", type=Path, required=True)
    parser.add_argument("--citation-map-csv", type=Path, required=True)
    parser.add_argument("--row-index-csv", type=Path, required=True)
    parser.add_argument("--r3c-map-csv", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--raw-dir", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--pause", type=float, default=1.0)
    args = parser.parse_args()

    base_rows = read_csv(args.base_csv)
    plan_rows = read_csv(args.plan_csv)
    supplied_map = read_csv(args.citation_map_csv)
    local_map = read_csv(args.r3c_map_csv)
    row_index = {row.get("id", ""): row for row in read_csv(args.row_index_csv)}
    base_by_id = {row.get("id", ""): row for row in base_rows}
    plan_scoped = [row for row in plan_rows if row.get("plan_section", "").strip() in {"s.10", "s.4.11"}]
    missing = sorted({row.get("lit_id", "") for row in plan_scoped} - set(base_by_id))
    if missing:
        raise ValueError("R3c plan ids missing from LITERATURE_BASE: " + ", ".join(missing))
    for plan in plan_scoped:
        indexed = row_index.get(plan.get("lit_id", ""))
        base_doi = base_by_id[plan["lit_id"]].get("DOI", "").strip().lower()
        index_doi = indexed.get("DOI", "").strip().lower() if indexed else ""
        if index_doi and index_doi != base_doi:
            raise ValueError(f"Historical DOI conflicts with LITERATURE_BASE for {plan['lit_id']}")

    full_plan_by_key = {row.get("citekey", "").strip(): row for row in plan_rows if row.get("citekey", "").strip()}
    included_keys = {row.get("citekey", "").strip() for row in local_map if row.get("include", "").upper() == "YES"}
    for mapping in local_map:
        if mapping.get("include", "").upper() != "YES":
            continue
        key = mapping.get("citekey", "").strip()
        planned = full_plan_by_key.get(key)
        if (not planned or planned.get("lit_id", "") != mapping.get("source_lit_id", "")
                or planned.get("technical_claim_eligible", "").strip().upper() != "YES"
                or mapping.get("plan_technical_eligible", "").strip().upper() != "YES"):
            raise ValueError(f"R3c include=YES mapping does not resolve to its technically eligible REFERENCE_PLAN row: {key}")
    map_by_key: dict[str, list[str]] = {}
    known_claim_ids = {claim for item in supplied_map for claim in re.findall(r"CL-\d+", item.get("claim_id", ""))}
    for mapping in local_map:
        for claim_id in re.findall(r"CL-\d+", mapping.get("frozen_map_claim_id", "")):
            if claim_id not in known_claim_ids:
                raise ValueError(f"R3c local map refers to unknown frozen CITATION_MAP claim: {claim_id}")
    for item in supplied_map:
        claim_id = item.get("claim_id", "")
        for key in re.split(r"[;,]\s*", item.get("proposed_citations", "")):
            if key.strip():
                map_by_key.setdefault(key.strip(), []).append(claim_id)
    eligible_source_keys = {row.get("citekey", "").strip() for row in plan_scoped
                            if row.get("technical_claim_eligible", "").strip().upper() == "YES"}
    supplied_keys = set(map_by_key)
    exact_matches = sorted(eligible_source_keys & supplied_keys)

    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    eligible_dois = sorted({base_by_id[row["lit_id"]].get("DOI", "").strip()
                            for row in plan_scoped
                            if row.get("technical_claim_eligible", "").strip().upper() == "YES"
                            and cr.DOI_RE.match(base_by_id[row["lit_id"]].get("DOI", "").strip())})
    request_log = args.report_dir / "CROSSREF_R3C_REQUEST_LOG.csv"
    responses: dict[str, tuple[int, dict | None]] = {}
    with request_log.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["DOI", "HTTP_status", "timestamp_utc", "metadata_json", "error"])
        for number, doi in enumerate(eligible_dois, 1):
            print(f"R3c Crossref {number}/{len(eligible_dois)}: {doi}", flush=True)
            responses[doi] = cr._fetch_r3a(doi, args.raw_dir, writer, args.pause)

    existing = cr.parse_bib(args.local_bib)
    by_doi: dict[str, list[dict[str, str]]] = {}
    by_key = {entry["key"]: entry for entry in existing}
    for entry in existing:
        if entry.get("doi", "").strip():
            by_doi.setdefault(entry["doi"].strip().lower(), []).append(entry)

    bib = ["% R3c entries: Crossref VERIFIED and REFERENCE_PLAN technical_claim_eligible=YES only.",
           "% Only entries with a local R3C_CITATION_MAP include=YES are emitted.", ""]
    bib_keys: set[str] = set()
    out: list[dict[str, str]] = []
    for plan in plan_scoped:
        lit_id = plan["lit_id"]
        base = base_by_id[lit_id]
        doi = base.get("DOI", "").strip()
        key = plan.get("citekey", "").strip()
        eligible = plan.get("technical_claim_eligible", "").strip().upper() == "YES"
        claims = "; ".join(sorted(set(map_by_key.get(key, []))))
        prior = "NOT_IN_INDEX"
        if lit_id in row_index:
            prior = "HISTORICAL_HTTP_" + row_index[lit_id].get("http_status", "UNKNOWN")

        resolved = ""
        scope = ""
        ready = "NO"
        reason = ""
        raw_path = ""
        if not eligible:
            status, http_status, message = "INELIGIBLE", 0, None
            reason = "technical_claim_eligible is not YES; no Crossref request or citation"
        elif not cr.DOI_RE.match(doi):
            status, http_status, message = "NO-DOI", 0, None
            reason = "no valid DOI recorded; no Crossref request"
        else:
            http_status, message = responses[doi]
            raw_path = str(args.raw_dir / (cr.safe_doi(doi) + ".json"))
            cross_titles = (message or {}).get("title") or []
            cross_title = cross_titles[0] if cross_titles else ""
            venues = ((message or {}).get("container-title") or []) + ((message or {}).get("short-container-title") or [])
            overlap, substring = cr._title_overlap(base.get("title", ""), cross_title)
            exact_title = bool(cross_title) and cr._normal_metadata(base.get("title", "")) == cr._normal_metadata(cross_title)
            title_ok = exact_title or substring or overlap >= .60
            years = cr._crossref_years(message or {})
            try:
                base_year = int(base.get("year", "").strip())
            except ValueError:
                base_year = 0
            delta = min((abs(base_year-int(year)) for year in years if year.isdigit()), default=None)
            year_exact = str(base_year) in years
            year_ok = delta is not None and delta <= 1
            venue_ok = cr._venue_matches(base.get("venue", ""), venues)
            doi_ok = (message or {}).get("DOI", "").strip().lower() == doi.lower()
            status = "NOT-FOUND" if http_status == 404 else ("VERIFIED" if http_status == 200 and doi_ok and title_ok and year_ok and venue_ok else "MISMATCH")
            reasons=[]
            if http_status != 404:
                if http_status != 200: reasons.append(f"Crossref HTTP status {http_status}, expected 200")
                if not doi_ok: reasons.append("Crossref DOI differs from requested DOI")
                if not title_ok: reasons.append(f"title overlap={overlap:.2f} (<0.60)")
                elif not exact_title: reasons.append(f"title accepted under relaxed overlap/substring rule ({overlap:.2f})")
                if not year_ok: reasons.append(f"base year {base_year} not within one year of Crossref years {', '.join(sorted(years))}")
                elif not year_exact: reasons.append(f"base year differs by {delta} year(s)")
                if not venue_ok: reasons.append("normalized venue does not match Crossref container title")
            else:
                reasons.append("Crossref returned HTTP 404")
            reason = "; ".join(reasons)
            if status == "VERIFIED" and key and cr.authors_from_message(message or {}):
                same_doi = by_doi.get(doi.lower(), [])
                target_key = same_doi[0]["key"] if same_doi else key
                conflict = target_key in by_key and by_key[target_key].get("doi", "").strip().lower() != doi.lower()
                if not conflict:
                    resolved = target_key
                    if key in included_keys:
                        ready = "YES"
                        scope = "technical"
                        if target_key not in bib_keys:
                            bib.append(cr._bib_from_crossref(target_key, doi, message or {}))
                            bib.append("")
                            bib_keys.add(target_key)
                    else:
                        reason = (reason + "; " if reason else "") + "verified eligible source has no R3C_CITATION_MAP include=YES mapping; metadata only"
                else:
                    reason = (reason + "; " if reason else "") + f"BibTeX key {target_key} belongs to another DOI"
            elif status == "VERIFIED" and eligible:
                reason = (reason + "; " if reason else "") + "Crossref author metadata empty; no BibTeX citation emitted"

        cross_titles = (message or {}).get("title") or []
        cross_title = cross_titles[0] if cross_titles else ""
        venues = ((message or {}).get("container-title") or []) + ((message or {}).get("short-container-title") or [])
        overlap, substring = cr._title_overlap(base.get("title", ""), cross_title)
        years = cr._crossref_years(message or {})
        try:
            audit_base_year = int(base.get("year", "").strip())
        except ValueError:
            audit_base_year = 0
        audit_year_delta = min((abs(audit_base_year-int(year)) for year in years if year.isdigit()), default=None)
        year_acceptable = audit_year_delta is not None and audit_year_delta <= 1
        out.append({"lit_id": lit_id, "citekey": key, "resolved_citekey": resolved, "section": plan.get("plan_section", ""),
                    "proposed_section": plan.get("proposed_section", ""), "DOI": doi, "status": status,
                    "title_match": "YES" if cross_title and cr._normal_metadata(base.get("title", "")) == cr._normal_metadata(cross_title) else "NO",
                    "title_overlap": f"{overlap:.2f}", "title_acceptable": "YES" if (cross_title and (cr._normal_metadata(base.get("title", "")) == cr._normal_metadata(cross_title) or substring or overlap >= .60)) else "NO",
                    "year_match": "YES" if base.get("year", "").strip() in years else "NO", "year_acceptable": "YES" if year_acceptable else "NO",
                    "year_delta": "" if audit_year_delta is None else str(audit_year_delta),
                    "venue_match": "YES" if eligible and cr.DOI_RE.match(doi) and cr._venue_matches(base.get("venue", ""), venues) else "NO",
                    "base_title": base.get("title", ""), "base_venue": base.get("venue", ""), "crossref_title": cross_title,
                    "crossref_year": cr.crossref_issued_year(message or {}), "crossref_years": "; ".join(sorted(years)),
                    "crossref_venue": "; ".join(venues), "technical_claim_eligible": "YES" if eligible else "NO",
                    "read_level": plan.get("read_level", ""), "prior_api_log": prior, "citation_map_claims": claims,
                    "raw_json": raw_path, "reason": reason, "citation_scope": scope, "bib_ready": ready})

    verify_path = args.report_dir / "CROSSREF_R3C_VERIFY.csv"
    fields = list(out[0]) if out else []
    with verify_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(out)
    (args.report_dir / "R3C_VERIFIED_REFERENCES.bib").write_text("\n".join(bib), encoding="utf-8")

    human = [row for row in out if row["status"] == "MISMATCH" and row["title_acceptable"] == "NO"]
    lines = ["# R3c Crossref title human checks", "", "Rows failing the relaxed 0.60 shorter-title overlap threshold.", ""]
    lines += ([f"- {r['lit_id']} `{r['citekey']}`; overlap {r['title_overlap']}; base: {r['base_title']}; Crossref: {r['crossref_title']}" for r in human] or ["None."])
    (args.report_dir / "CROSSREF_R3C_HUMAN_CHECK.md").write_text("\n".join(lines)+"\n", encoding="utf-8")

    counts = Counter(row["status"] for row in out)
    eligible_count = sum(row["technical_claim_eligible"] == "YES" for row in out)
    method = f"""# R3c Crossref verification method

Scope: REFERENCE_PLAN rows in s.10 and s.4.11. All and only `technical_claim_eligible=YES` rows were queried; ineligible s.4.11 metadata rows were retained as INELIGIBLE with no request. New R3c DOI data was fetched dynamically in Actions. Comparison uses the R3a relaxed rules: exact/prefix/substring or at least 0.60 shorter-title token overlap; published/issued year exact or within one year; normalized container title; returned DOI equal to requested DOI. A 404 is NOT-FOUND. Network errors fail the job. Raw files contain allowlisted bibliographic metadata only.

The frozen CITATION_MAP is parsed using its `proposed_citations` field. Exact key matches among the four eligible s.10 candidates: {len(exact_matches)}. Section-specific placements are documented in `R3C_CITATION_MAP.csv`; this local map connects the read-only plan's proposed-section/source notes to CL-013/014/015 topics and clearly labels non-matches. Kumar2017 is carried forward only from its R3b row (VERIFIED, technical eligible, bib-ready); it is not refetched. Barak2023JTS is excluded because there is no eligible REFERENCE_PLAN row, despite a pre-existing Crossref-verified local BibTeX record.

Only Crossref-VERIFIED, technically eligible, include=YES local-map sources with authors and no BibTeX key conflict enter `R3C_VERIFIED_REFERENCES.bib`. Rows: {len(out)}; eligible s.10 DOI requests: {len(eligible_dois)}; eligible rows: {eligible_count}; VERIFIED: {counts['VERIFIED']}; MISMATCH: {counts['MISMATCH']}; NOT-FOUND: {counts['NOT-FOUND']}; NO-DOI: {counts['NO-DOI']}; INELIGIBLE (not queried): {counts['INELIGIBLE']}; newly cited BibTeX keys: {len(bib_keys)}.
"""
    (args.report_dir / "CROSSREF_R3C_METHOD.md").write_text(method, encoding="utf-8")
    print(f"R3c rows={len(out)} requests={len(eligible_dois)} counts={dict(counts)} bib-ready-mapped={len(bib_keys)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
