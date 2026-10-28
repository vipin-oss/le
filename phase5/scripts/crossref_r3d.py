#!/usr/bin/env python3
"""Dynamically verify the newly eligible R3d citations in GitHub Actions."""
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
    parser.add_argument("--readiness-csv", type=Path, required=True)
    parser.add_argument("--citation-map-csv", type=Path, required=True)
    parser.add_argument("--row-index-csv", type=Path, required=True)
    parser.add_argument("--r3d-map-csv", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--raw-dir", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--pause", type=float, default=1.0)
    args = parser.parse_args()

    base_rows = read_csv(args.base_csv)
    plan_rows = read_csv(args.plan_csv)
    readiness_rows = read_csv(args.readiness_csv)
    supplied_map = read_csv(args.citation_map_csv)
    local_map = read_csv(args.r3d_map_csv)
    row_index = {row.get("id", ""): row for row in read_csv(args.row_index_csv)}
    base_by_id = {row.get("id", ""): row for row in base_rows}
    plan_by_id = {row.get("lit_id", ""): row for row in plan_rows}

    ids = [row.get("source_lit_id", "").strip() for row in local_map]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError("R3D citation map must contain unique source_lit_id values")
    missing_base = sorted(set(ids) - set(base_by_id))
    missing_plan = sorted(set(ids) - set(plan_by_id))
    if missing_base or missing_plan:
        raise ValueError(f"R3D map rows absent from inputs: LITERATURE_BASE={missing_base}; REFERENCE_PLAN={missing_plan}")

    map_by_key: dict[str, list[str]] = {}
    for item in supplied_map:
        for key in re.split(r"[;,]\s*", item.get("proposed_citations", "")):
            if key.strip():
                map_by_key.setdefault(key.strip(), []).append(item.get("claim_id", ""))
    known_claim_ids = {claim for row in supplied_map for claim in re.findall(r"CL-\d+", row.get("claim_id", ""))}
    for mapping in local_map:
        lit_id = mapping["source_lit_id"].strip()
        plan = plan_by_id[lit_id]
        key = mapping["citekey"].strip()
        if (plan.get("citekey", "").strip() != key
                or plan.get("technical_claim_eligible", "").strip().upper() != "YES"
                or mapping.get("plan_technical_eligible", "").strip().upper() != "YES"
                or mapping.get("include", "").strip().upper() != "YES"):
            raise ValueError(f"R3D include=YES map does not match a technically eligible plan row: {lit_id}/{key}")
        expected_exact = "YES" if key in map_by_key else "NO"
        if mapping.get("frozen_map_exact_key_match", "").strip().upper() != expected_exact:
            raise ValueError(f"R3D map's exact CITATION_MAP-match flag is stale for {key}: expected {expected_exact}")
        for claim_id in re.findall(r"CL-\d+", mapping.get("frozen_map_claim_id", "")):
            if claim_id not in known_claim_ids:
                raise ValueError(f"R3D map refers to an unknown frozen CITATION_MAP claim: {claim_id}")
        indexed = row_index.get(lit_id)
        plan_doi = base_by_id[lit_id].get("DOI", "").strip().lower()
        index_doi = indexed.get("DOI", "").strip().lower() if indexed else ""
        if index_doi and index_doi != plan_doi:
            raise ValueError(f"Historical DOI conflicts with LITERATURE_BASE for {lit_id}")

    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    eligible_dois = sorted({base_by_id[lit_id].get("DOI", "").strip() for lit_id in ids
                            if cr.DOI_RE.match(base_by_id[lit_id].get("DOI", "").strip())})
    request_log = args.report_dir / "CROSSREF_R3D_REQUEST_LOG.csv"
    responses: dict[str, tuple[int, dict | None]] = {}
    with request_log.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["DOI", "HTTP_status", "timestamp_utc", "metadata_json", "error"])
        for number, doi in enumerate(eligible_dois, 1):
            print(f"R3d Crossref {number}/{len(eligible_dois)}: {doi}", flush=True)
            responses[doi] = cr._fetch_r3a(doi, args.raw_dir, writer, args.pause)

    existing = cr.parse_bib(args.local_bib)
    by_key = {entry["key"]: entry for entry in existing}
    by_doi: dict[str, list[dict[str, str]]] = {}
    for entry in existing:
        doi = entry.get("doi", "").strip().lower()
        if doi:
            by_doi.setdefault(doi, []).append(entry)

    bib = ["% R3d entries: Crossref VERIFIED, technically eligible REFERENCE_PLAN rows, and mapped claims only.",
           "% Entries are emitted for include=YES rows in R3D_CITATION_MAP.csv.", ""]
    bib_keys: set[str] = set()
    out: list[dict[str, str]] = []
    for mapping in local_map:
        lit_id = mapping["source_lit_id"].strip()
        plan = plan_by_id[lit_id]
        base = base_by_id[lit_id]
        key = mapping["citekey"].strip()
        doi = base.get("DOI", "").strip()
        claims = "; ".join(sorted(set(map_by_key.get(key, []))))
        indexed = row_index.get(lit_id, {})
        prior_index = "NOT_IN_INDEX" if not indexed else "HISTORICAL_HTTP_" + indexed.get("http_status", "UNKNOWN")
        resolved = ""
        raw_path = ""
        reason = ""
        ready = "NO"
        scope = ""
        cross_title = ""
        venues: list[str] = []
        years: set[str] = set()
        overlap = 0.0
        substring = False
        exact_title = False
        if plan.get("technical_claim_eligible", "").strip().upper() != "YES":
            status, http_status, message = "INELIGIBLE", 0, None
            reason = "technical_claim_eligible is not YES; no Crossref request or citation"
        elif not cr.DOI_RE.match(doi):
            status, http_status, message = "NO-DOI", 0, None
            reason = "no valid DOI recorded; no Crossref request"
        else:
            http_status, message = responses[doi]
            raw_path = str(args.raw_dir / (cr.safe_doi(doi) + ".json"))
            title_values = (message or {}).get("title") or []
            cross_title = title_values[0] if title_values else ""
            venues = ((message or {}).get("container-title") or []) + ((message or {}).get("short-container-title") or [])
            overlap, substring = cr._title_overlap(base.get("title", ""), cross_title)
            exact_title = bool(cross_title) and cr._normal_metadata(base.get("title", "")) == cr._normal_metadata(cross_title)
            title_ok = exact_title or substring or overlap >= .60
            years = cr._crossref_years(message or {})
            try:
                base_year = int(base.get("year", "").strip())
            except ValueError:
                base_year = 0
            year_delta = min((abs(base_year - int(year)) for year in years if year.isdigit()), default=None)
            year_exact = str(base_year) in years
            year_ok = year_delta is not None and year_delta <= 1
            venue_ok = cr._venue_matches(base.get("venue", ""), venues)
            doi_ok = (message or {}).get("DOI", "").strip().lower() == doi.lower()
            status = ("NOT-FOUND" if http_status == 404 else
                      "VERIFIED" if http_status == 200 and doi_ok and title_ok and year_ok and venue_ok else "MISMATCH")
            reasons = []
            if http_status == 404:
                reasons.append("Crossref returned HTTP 404")
            else:
                if http_status != 200: reasons.append(f"Crossref HTTP status {http_status}, expected 200")
                if not doi_ok: reasons.append("Crossref DOI differs from requested DOI")
                if not title_ok: reasons.append(f"title overlap={overlap:.2f} (<0.60)")
                elif not exact_title: reasons.append(f"title accepted under relaxed overlap/substring rule ({overlap:.2f})")
                if not year_ok: reasons.append(f"base year {base_year} not within one year of Crossref years {', '.join(sorted(years))}")
                elif not year_exact: reasons.append(f"base year differs by {year_delta} year(s)")
                if not venue_ok: reasons.append("normalized venue does not match Crossref container title")
            reason = "; ".join(reasons)
            if status == "VERIFIED" and cr.authors_from_message(message or {}):
                same_doi = by_doi.get(doi.lower(), [])
                target_key = same_doi[0]["key"] if same_doi else key
                conflict = target_key in by_key and by_key[target_key].get("doi", "").strip().lower() != doi.lower()
                if conflict:
                    reason = (reason + "; " if reason else "") + f"BibTeX key {target_key} belongs to another DOI"
                else:
                    resolved = target_key
                    ready = "YES"
                    scope = "secondary" if mapping.get("claim_status", "").startswith("SECONDARY") else "technical"
                    if target_key not in bib_keys:
                        bib.append(cr._bib_from_crossref(target_key, doi, message or {}))
                        bib.append("")
                        bib_keys.add(target_key)
            elif status == "VERIFIED":
                reason = (reason + "; " if reason else "") + "Crossref author metadata empty; no BibTeX citation emitted"

        title_values = (message or {}).get("title") or []
        cross_title = title_values[0] if title_values else ""
        cross_years = cr._crossref_years(message or {})
        try:
            audit_year = int(base.get("year", "").strip())
        except ValueError:
            audit_year = 0
        year_delta_audit = min((abs(audit_year - int(year)) for year in cross_years if year.isdigit()), default=None)
        exact_map_match = key in map_by_key
        out.append({
            "map_id": mapping.get("map_id", ""), "lit_id": lit_id, "citekey": key,
            "resolved_citekey": resolved, "destination_section": mapping.get("destination_section", ""),
            "plan_section": plan.get("plan_section", ""), "proposed_section": plan.get("proposed_section", ""),
            "DOI": doi, "status": status, "technical_claim_eligible": "YES",
            "claim_status": mapping.get("claim_status", ""), "title_match": "YES" if exact_title else "NO",
            "title_overlap": f"{overlap:.2f}",
            "title_acceptable": "YES" if cross_title and (exact_title or substring or overlap >= .60) else "NO",
            "year_match": "YES" if base.get("year", "").strip() in cross_years else "NO",
            "year_acceptable": "YES" if year_delta_audit is not None and year_delta_audit <= 1 else "NO",
            "year_delta": "" if year_delta_audit is None else str(year_delta_audit),
            "venue_match": "YES" if cr.DOI_RE.match(doi) and cr._venue_matches(base.get("venue", ""), venues) else "NO",
            "base_title": base.get("title", ""), "base_venue": base.get("venue", ""),
            "crossref_title": cross_title, "crossref_years": "; ".join(sorted(cross_years)),
            "crossref_venue": "; ".join(venues), "read_level": plan.get("read_level", ""),
            "evidence_grade": plan.get("evidence_grade", ""), "prior_api_log": prior_index,
            "citation_map_claims": claims, "r3d_map_id": mapping.get("map_id", ""),
            "frozen_map_claim_id": mapping.get("frozen_map_claim_id", ""),
            "frozen_map_exact_key_match": "YES" if exact_map_match else "NO",
            "raw_json": raw_path, "reason": reason, "citation_scope": scope, "bib_ready": ready,
        })

    verify_path = args.report_dir / "CROSSREF_R3D_VERIFY.csv"
    with verify_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(out[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(out)
    (args.report_dir / "R3D_VERIFIED_REFERENCES.bib").write_text("\n".join(bib), encoding="utf-8")

    human = [row for row in out if row["status"] == "MISMATCH" and row["title_acceptable"] == "NO"]
    human_lines = ["# R3d Crossref title human checks", "", "Rows failing the relaxed 0.60 shorter-title overlap threshold.", ""]
    human_lines += ([f"- {row['lit_id']} `{row['citekey']}`; overlap {row['title_overlap']}; base: {row['base_title']}; Crossref: {row['crossref_title']}" for row in human] or ["None."])
    (args.report_dir / "CROSSREF_R3D_HUMAN_CHECK.md").write_text("\n".join(human_lines) + "\n", encoding="utf-8")

    counts = Counter(row["status"] for row in out)
    exact_matches = sum(row["frozen_map_exact_key_match"] == "YES" for row in out)
    ready_count = sum(row["bib_ready"] == "YES" for row in out)
    readiness_by_section = {row.get("section", ""): row for row in readiness_rows}
    readiness_summary = "; ".join(
        f"{section}: {readiness_by_section.get(section, {}).get('eligible_full_or_primary', 'n/a')} full/primary of {readiness_by_section.get(section, {}).get('eligible_now', 'n/a')} eligible"
        for section in ("s.4.9", "s.4.10", "s.5", "s.11", "s.12")
    )
    method = f"""# R3d Crossref verification method

The nine rows in `R3D_CITATION_MAP.csv` were re-checked dynamically in Actions because the frozen REFERENCE_PLAN marks them `technical_claim_eligible=YES`. No new R3d Crossref data is fetched outside CI. Comparison uses the saved R3a rules: returned DOI must match; title exact/prefix/substring or at least 0.60 shorter-title token overlap; Crossref published/issued year exact or within one year; normalized container title must match. HTTP 404 is NOT-FOUND. Network errors fail the job. Only VERIFIED rows with Crossref author data and no BibTeX DOI conflict enter `R3D_VERIFIED_REFERENCES.bib`.

The supplied `CITATION_MAP.csv` has {exact_matches} exact citekey matches among these nine candidates. Claim-level additions and non-exact mappings are explicit in `R3D_CITATION_MAP.csv`; the frozen plan/read-level notes control which content each source may support. In particular, LIT-0040 / Shakeriaski2021 is a SECONDARY survey for theory-to-geometry coverage only, not equations, numbers, or stability. Acoustic abstract-MGT findings are kept separate from thermoelastic MGT admissibility. R3 readiness baseline by section: {readiness_summary}.

Rows: {len(out)}; DOI requests: {len(eligible_dois)}; VERIFIED: {counts['VERIFIED']}; MISMATCH: {counts['MISMATCH']}; NOT-FOUND: {counts['NOT-FOUND']}; NO-DOI: {counts['NO-DOI']}; bibliography-ready mapped rows: {ready_count}; new BibTeX entries to merge: {len(bib_keys)}.
"""
    (args.report_dir / "CROSSREF_R3D_METHOD.md").write_text(method, encoding="utf-8")
    print(f"R3d rows={len(out)} requests={len(eligible_dois)} counts={dict(counts)} bib-ready={ready_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
