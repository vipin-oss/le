#!/usr/bin/env python3
"""Crossref-verify only the mapped read sources for the R3f content batch."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

import crossref_enrich as cr

EXPECTED_KEYS = {
    "Chandrasekharaiah1984", "Nowacki1978", "Cowin1983", "Nunziato1979", "Iesan1986",
    "MarchandMcDevittTriggiani2012", "ChadwickSneddon1958", "Joseph1989", "Joseph1990",
    "HetnarskiIgnaczak1999", "Stroh1958", "Stroh1962", "IvanovSavova1991", "Povstenko2009",
    "Gorenflo1997", "GorenfloKilbasMainardiRogosin2014", "vanDerMerwe2021", "Chirita2016",
    "ChenGurtin1968", "GurtinWilliams1966", "WangLi2025IV", "Durbin1974", "HonigHirdes1984",
    "Luchko2010", "Cattaneo1948",
}
USER_AGENT = f"le-r3f-crossref/1.0 (mailto:{cr.MAILTO})"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def families(value: str) -> list[str]:
    return [cr._normal_metadata(item).replace(" ", "") for item in value.split(";") if item.strip()]


def norm_pages(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (value or "").lower().replace("–", "-").replace("−", "-"))


def normalized_words(value: str) -> set[str]:
    return set(cr._normal_metadata(value).split())


def venue_match(base: str, candidates: list[str]) -> tuple[bool, str, float]:
    base_words = normalized_words(base)
    best_name = ""
    best = 0.0
    for item in candidates:
        other = normalized_words(item)
        score = len(base_words & other) / max(1, min(len(base_words), len(other)))
        if score > best:
            best, best_name = score, item
    return best >= 0.60, best_name, best


def check_candidate(row: dict[str, str], message: dict) -> dict[str, str]:
    title_items = message.get("title") or []
    cross_title = str(title_items[0]) if title_items else ""
    author_families = [cr._normal_metadata(a.get("family") or a.get("name") or "").replace(" ", "")
                       for a in (message.get("author") or [])]
    expected_families = families(row.get("authors", ""))
    author_ok = bool(expected_families) and all(
        any(expected == actual or expected in actual or actual in expected
            for actual in author_families) for expected in expected_families
    )
    years = cr._crossref_years(message)
    base_year = row.get("year", "").strip()
    year_ok = base_year.isdigit() and any(y.isdigit() and abs(int(y) - int(base_year)) <= 1 for y in years)
    year_exact = base_year in years
    base_title = row.get("title", "").strip()
    if base_title:
        overlap, substring = cr._title_overlap(base_title, cross_title)
        title_ok = bool(cross_title) and (substring or overlap >= 0.80)
    else:
        overlap, title_ok = 0.0, bool(cross_title)
    venue_values = (message.get("container-title") or []) + (message.get("short-container-title") or [])
    venue_ok, cross_venue, venue_score = venue_match(row.get("venue", ""), [str(x) for x in venue_values])
    checks: dict[str, str] = {
        "author_match": "YES" if author_ok else "NO",
        "title_match": "YES" if title_ok else "NO",
        "title_overlap": f"{overlap:.2f}" if base_title else "NA",
        "year_match": "YES" if year_exact else ("NO" if not year_ok else "YEAR-DELTA-1"),
        "venue_match": "YES" if venue_ok else "NO",
        "venue_overlap": f"{venue_score:.2f}",
        "base_title": base_title,
        "crossref_title": cross_title,
        "base_year": base_year,
        "crossref_years": "; ".join(sorted(years)),
        "base_venue": row.get("venue", ""),
        "crossref_venue": "; ".join(str(x) for x in venue_values),
        "crossref_volume": str(message.get("volume", "")),
        "crossref_issue": str(message.get("issue", "")),
        "crossref_pages": str(message.get("page") or message.get("article-number") or ""),
    }
    for field, metadata_field in (("volume", "volume"), ("issue", "issue"), ("pages", "page")):
        expected = row.get(field, "").strip()
        actual = str(message.get(metadata_field) or (message.get("article-number") if field == "pages" else "") or "")
        if expected and actual:
            checks[field + "_match"] = "YES" if norm_pages(expected) == norm_pages(actual) else "NO"
        else:
            checks[field + "_match"] = "UNAVAILABLE" if expected else "NA"
    checks["accepted"] = "YES" if author_ok and year_ok and title_ok and venue_ok and all(
        checks[k] != "NO" for k in ("volume_match", "issue_match", "pages_match")
    ) else "NO"
    return checks


def fetch_json(url: str) -> tuple[int, dict | None, str]:
    last_error = ""
    for attempt in range(5):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return int(response.status), json.loads(response.read().decode("utf-8")), ""
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return 404, None, "HTTP 404"
            last_error = f"HTTP {exc.code}: {exc.reason}"
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 4:
                break
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt == 4:
                break
        time.sleep(min(30, 2 ** attempt * 2))
    raise RuntimeError(f"Crossref request failed after retries: {last_error}")


def retain_metadata(message: dict) -> dict:
    return cr._crossref_metadata(message)


def request_record(row: dict[str, str], raw_dir: Path, log_writer: csv.writer, pause: float):
    doi = row.get("doi", "").strip()
    query = row.get("query", "").strip()
    mode = "DOI" if doi else "BIBLIOGRAPHIC-SEARCH"
    if doi:
        url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    else:
        params = urllib.parse.urlencode({"query.bibliographic": query, "rows": "10"})
        url = "https://api.crossref.org/works?" + params
    status_http, payload, error = fetch_json(url)
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    messages: list[dict] = []
    if status_http == 200 and payload:
        if doi:
            message = payload.get("message") or {}
            if isinstance(message, dict):
                messages = [message]
        else:
            messages = [m for m in ((payload.get("message") or {}).get("items") or []) if isinstance(m, dict)]
    ranked = []
    for message in messages:
        metadata = retain_metadata(message)
        checks = check_candidate(row, metadata)
        ranked.append((checks["accepted"] == "YES", float(checks["venue_overlap"]),
                       float(checks["title_overlap"]) if checks["title_overlap"] != "NA" else 0.0,
                       metadata, checks))
    ranked.sort(key=lambda item: (item[0], item[1], item[2]), reverse=True)
    chosen = ranked[0] if ranked else None
    message = chosen[3] if chosen else None
    checks = chosen[4] if chosen else {}
    cross_doi = str((message or {}).get("DOI", "")).strip()
    target = raw_dir / ((cr.safe_doi(doi or cross_doi) if (doi or cross_doi) else re.sub(r"[^A-Za-z0-9_-]", "_", row["citekey"])) + ".json")
    raw_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({"map_id": row["map_id"], "mode": mode, "requested_doi": doi,
                                  "query": query, "http_status": status_http,
                                  "message": message}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if status_http == 404 or (not messages and status_http == 200):
        result = "NOT-FOUND"
    elif chosen and checks.get("accepted") == "YES" and not cross_doi:
        result = "NO-DOI"
        error = "Matching Crossref record has no DOI; do not emit BibTeX"
    elif chosen and checks.get("accepted") == "YES" and (not doi or cross_doi.lower() == doi.lower()):
        result = "VERIFIED"
    else:
        result = "MISMATCH"
    if status_http != 200 and status_http != 404:
        raise RuntimeError(f"Unexpected Crossref HTTP status {status_http} for {row['citekey']}")
    why = []
    if result == "NOT-FOUND":
        why.append("Crossref returned no matching record")
    elif result == "NO-DOI":
        why.append("matching Crossref record has no DOI; it is not bibliography-ready under this batch")
    elif result == "MISMATCH":
        if doi and cross_doi.lower() != doi.lower():
            why.append(f"returned DOI {cross_doi!r} differs from requested {doi!r}")
        for name, label in (("author_match", "author"), ("title_match", "title"), ("year_match", "year"),
                            ("venue_match", "venue"), ("volume_match", "volume"),
                            ("issue_match", "issue"), ("pages_match", "pages")):
            if checks.get(name) == "NO":
                why.append(f"{label} mismatch")
    elif chosen:
        for name in ("volume_match", "issue_match", "pages_match"):
            if checks.get(name) == "UNAVAILABLE":
                why.append(f"Crossref {name.removesuffix('_match')} unavailable; no conflicting value")
    log_writer.writerow([row["map_id"], row["citekey"], mode, doi, query, status_http,
                         cross_doi, result, timestamp, str(target), "; ".join(why)])
    if pause:
        time.sleep(pause)
    return result, status_http, message, checks, target, "; ".join(why)


def bib_entry(key: str, doi: str, message: dict) -> str:
    authors = cr.authors_from_message(message)
    titles = message.get("title") or []
    title = str(titles[0]) if titles else ""
    year = cr.crossref_issued_year(message)
    containers = message.get("container-title") or []
    container = str(containers[0]) if containers else ""
    kind = str(message.get("type", ""))
    if kind == "book-chapter":
        bibtype, container_field = "incollection", "booktitle"
    elif kind in {"book", "monograph", "edited-book"}:
        bibtype, container_field = "book", "publisher"
    else:
        bibtype, container_field = "article", "journal"
    fields = [("author", authors), ("title", title), ("year", year), ("doi", doi)]
    if container:
        fields.append((container_field, container))
    if bibtype == "book":
        publisher = str(message.get("publisher", ""))
        if publisher:
            fields.append(("publisher", publisher))
    for source, dest in (("volume", "volume"), ("issue", "number"), ("page", "pages"), ("article-number", "pages")):
        value = str(message.get(source, ""))
        if value and not any(dest == existing for existing, _ in fields):
            fields.append((dest, value))
    fields.extend([("verified", "YES"), ("source", "Crossref"), ("access_date", "2026-10-23"), ("status", "FOUNDATIONAL")])
    lines = [f"@{bibtype}{{{key},"]
    lines.extend(f"  {name} = {{{cr.bib_escape(value)}}}," for name, value in fields if value)
    lines.append("}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map-csv", type=Path, required=True)
    parser.add_argument("--findings-file", type=Path, required=True)
    parser.add_argument("--findings-04", type=Path, required=True)
    parser.add_argument("--findings-09", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--raw-dir", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--pause", type=float, default=1.0)
    args = parser.parse_args()

    mappings = read_csv(args.map_csv)
    if len(mappings) != len(EXPECTED_KEYS) or {row.get("citekey", "").strip() for row in mappings} != EXPECTED_KEYS:
        raise ValueError("R3f map must contain 24 Crossref candidates plus the Cattaneo NO-DOI status row")
    if len({row["map_id"] for row in mappings}) != len(mappings):
        raise ValueError("R3f map has duplicate map IDs")
    allowed_flags = {"YES", "NO-DOI"}
    if any(row.get("include", "").strip().upper() not in allowed_flags for row in mappings):
        raise ValueError("Every R3f row must be explicitly in scope")
    no_doi_rows = [row for row in mappings if row.get("include", "").strip().upper() == "NO-DOI"]
    if len(no_doi_rows) != 1 or no_doi_rows[0].get("citekey") != "Cattaneo1948" or no_doi_rows[0].get("doi", "").strip():
        raise ValueError("Only Cattaneo1948 may be recorded as NO-DOI, with no requested DOI")
    findings = args.findings_file.read_text(encoding="utf-8").lower()
    findings04 = args.findings_04.read_text(encoding="utf-8").lower()
    findings09 = args.findings_09.read_text(encoding="utf-8").lower()
    missing_anchors = [row["findings_anchor"] for row in mappings
                       if row["findings_anchor"].lower() not in findings]
    for required in ("maxwell 1867", "cattaneo 1948", "vernotte 1958", "c-t model", "f31", "f40", "f49"):
        if required not in findings:
            raise ValueError(f"Pinned R3f findings lack required anchor {required!r}")
    for document, text, required in (("FULLTEXT_FINDINGS_04", findings04, "f15 tzou 1995"),
                                     ("FULLTEXT_FINDINGS_09", findings09, "f28 dubner & abate")):
        if required not in text:
            raise ValueError(f"Pinned {document} lacks required comparison/context anchor {required!r}")
    if missing_anchors:
        raise ValueError("Pinned findings lack map anchors: " + ", ".join(sorted(set(missing_anchors))))

    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    request_path = args.report_dir / "CROSSREF_R3F_REQUEST_LOG.csv"
    responses = {}
    with request_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["map_id", "citekey", "query_mode", "requested_doi", "bibliographic_query",
                         "HTTP_status", "crossref_doi", "status", "timestamp_utc", "metadata_json", "reason"])
        for index, row in enumerate(mappings, 1):
            if row.get("include", "").strip().upper() == "NO-DOI":
                print("R3f status: Cattaneo1948 has NO-DOI; no request made", flush=True)
                responses[row["citekey"]] = ("NO-DOI", "NOT-REQUESTED", None, {}, Path(""),
                                               "NO-DOI retained; Crossref request omitted")
                continue
            print(f"R3f Crossref {index}/{len(mappings)}: {row['citekey']}", flush=True)
            responses[row["citekey"]] = request_record(row, args.raw_dir, writer, args.pause)

    existing = cr.parse_bib(args.local_bib)
    by_key = {entry["key"]: entry for entry in existing}
    output = []
    verified_bib = ["% R3f entries generated only from Crossref VERIFIED metadata.",
                    "% Bibliographic metadata only; supplied full-text findings remain the claim source.", ""]
    bib_keys = set()
    bib_generated = set()
    for row in mappings:
        status, http_status, message, checks, raw_path, reason = responses[row["citekey"]]
        cross_doi = str((message or {}).get("DOI", "")).strip()
        existing_entry = by_key.get(row["citekey"], {})
        existing_doi = existing_entry.get("doi", "").strip().lower()
        allowed_replace = row.get("replace_existing", "").strip().upper() == "YES"
        key_conflict = bool(existing_entry and existing_doi != cross_doi.lower() and not allowed_replace)
        author_string = cr.authors_from_message(message or {})
        title_items = (message or {}).get("title") or []
        title_string = str(title_items[0]) if title_items else ""
        year_string = cr.crossref_issued_year(message or {})
        bib_ready = status == "VERIFIED" and bool(author_string and title_string and year_string and cross_doi) and not key_conflict
        if status == "VERIFIED" and key_conflict:
            reason = (reason + "; " if reason else "") + f"BibTeX key {row['citekey']} already has DOI {existing_doi}; refusing overwrite"
        if bib_ready:
            if not existing_entry or allowed_replace:
                if row["citekey"] not in bib_generated:
                    verified_bib.append(bib_entry(row["citekey"], cross_doi, message or {}))
                    verified_bib.append("")
                    bib_generated.add(row["citekey"])
            bib_keys.add(row["citekey"])
        output.append({
            "map_id": row["map_id"], "citekey": row["citekey"],
            "resolved_citekey": row["citekey"] if bib_ready else "",
            "requested_doi": row.get("doi", ""), "DOI": cross_doi,
            "status": status, "HTTP_status": str(http_status),
            "author_match": checks.get("author_match", "NO"),
            "title_match": checks.get("title_match", "NO"),
            "title_overlap": checks.get("title_overlap", ""),
            "year_match": checks.get("year_match", "NO"),
            "venue_match": checks.get("venue_match", "NO"),
            "venue_overlap": checks.get("venue_overlap", ""),
            "volume_match": checks.get("volume_match", "NA"),
            "issue_match": checks.get("issue_match", "NA"),
            "pages_match": checks.get("pages_match", "NA"),
            "base_title": row.get("title", ""), "crossref_title": checks.get("crossref_title", ""),
            "base_year": row.get("year", ""), "crossref_years": checks.get("crossref_years", ""),
            "base_venue": row.get("venue", ""), "crossref_venue": checks.get("crossref_venue", ""),
            "sections": row.get("sections", ""), "primary_eligible": row.get("primary_eligible", "NO"),
            "claim_status": row.get("claim_status", ""), "raw_json": "" if status == "NO-DOI" else str(raw_path),
            "bib_ready": "YES" if bib_ready else "NO", "reason": reason,
        })

    fields = list(output[0])
    with (args.report_dir / "CROSSREF_R3F_VERIFY.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(output)
    (args.report_dir / "R3F_VERIFIED_REFERENCES.bib").write_text("\n".join(verified_bib), encoding="utf-8")
    counts = Counter(row["status"] for row in output)
    ready = sum(row["bib_ready"] == "YES" for row in output)
    mismatches = [row for row in output if row["status"] == "MISMATCH"]
    human = ["# R3f Crossref mismatch and title checks", "", "Rows with Crossref metadata that did not pass all mapped identity checks.", ""]
    human += [f"- `{r['citekey']}` DOI={r['DOI'] or 'not returned'}; {r['reason']}; base title={r['base_title'] or '(not supplied)'}; Crossref title={r['crossref_title']}" for r in mismatches] or ["None."]
    (args.report_dir / "CROSSREF_R3F_HUMAN_CHECK.md").write_text("\n".join(human) + "\n", encoding="utf-8")
    method = f"""# R3f Crossref verification method

The pinned read-only `FULLTEXT_FINDINGS_04.md`, `_09.md`, and `_10.md` were checked before queries; the Tzou 1995 heat-law and C--T thermoelastic attributions remain distinct, and the existing Dubner--Abate context is retained. Exactly the 24 mapped R3f works were queried: rows with a DOI used Crossref's exact DOI endpoint; rows without a supplied DOI used a bibliographic query constrained by the mapped author, publication year, venue, volume/issue/pages where available. A record is VERIFIED only when Crossref author families, title when supplied, year (within one year), venue, and every available mapped volume/issue/page field agree; exact-DOI rows must also return that exact DOI. Search results without a qualifying record are NOT-FOUND when Crossref returns none and MISMATCH when records exist but fail the identity checks. Network failures fail the job. Raw files contain bibliographic metadata only; no abstracts, references, or full text are stored. Only VERIFIED rows with usable Crossref authors/title/year/DOI and no key conflict are bibliography-ready. Existing stale Luchko/Gorenflo book entries are replaced only through their explicit map flags and only with VERIFIED records.

Rows={len(output)}; Crossref requests={sum(r.get('HTTP_status') != 'NOT-REQUESTED' for r in output)}; DOI-specific requests={sum(bool(r.get('requested_doi')) for r in output)}; bibliographic searches={sum(not bool(r.get('requested_doi')) and r.get('status') != 'NO-DOI' for r in output)}; NO-DOI rows={counts['NO-DOI']}; VERIFIED={counts['VERIFIED']}; MISMATCH={counts['MISMATCH']}; NOT-FOUND={counts['NOT-FOUND']}; bibliography-ready={ready}; new BibTeX records={len(bib_generated)}.
"""
    (args.report_dir / "CROSSREF_R3F_METHOD.md").write_text(method, encoding="utf-8")
    print(f"R3f rows={len(output)} counts={dict(counts)} bibliography-ready={ready} new-records={len(bib_generated)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
