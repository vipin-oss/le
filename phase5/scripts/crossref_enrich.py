#!/usr/bin/env python3
"""Fetch and audit Crossref metadata for the literature base and local BibTeX.

All bibliographic fields written to literature_base_enriched.bib are read from the
saved Crossref JSON response for that DOI. A DOI is never marked matched without
field-by-field comparison with the existing local record.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MAILTO = "vipin@gurugramuniversity.ac.in"
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.I)
MATCH_FIELDS = ("title_match", "first_author_match", "year_match", "pages_match")
USER_AGENT = f"le-crossref-enrichment/1.0 (mailto:{MAILTO})"


def norm(value: str) -> str:
    value = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^]]*\])?\{([^{}]*)\}", r"\1", value or "")
    value = re.sub(r"\\[a-zA-Z]+\*?", "", value)
    return re.sub(r"[^a-z0-9]", "", value.lower())


def safe_doi(doi: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", doi.strip())


def parse_bib(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: list[dict[str, str]] = []
    start_re = re.compile(r"@([A-Za-z]+)\s*\{\s*([^,]+),")
    for m in start_re.finditer(text):
        end = text.find("\n}", m.end())
        if end < 0:
            end = text.find("}", m.end())
        body = text[m.end():end if end >= 0 else len(text)]
        fields: dict[str, str] = {}
        for f in re.finditer(r"(?m)^\s*([A-Za-z][A-Za-z0-9_-]*)\s*=\s*\{(.*?)\}\s*,?\s*$", body, re.S):
            fields[f.group(1).lower()] = f.group(2).strip()
        entries.append({"key": m.group(2).strip(), "type": m.group(1).lower(), **fields})
    return entries


def issued_year(message: dict) -> str:
    for field in ("published-print", "published-online", "issued", "created"):
        parts = message.get(field, {}).get("date-parts", [])
        if parts and parts[0]:
            return str(parts[0][0])
    return ""


def authors_from_message(message: dict) -> str:
    names = []
    for a in message.get("author", []) or []:
        family = (a.get("family") or a.get("name") or "").strip()
        given = (a.get("given") or "").strip()
        if family:
            names.append(f"{family}, {given}".rstrip(", "))
    return " and ".join(names)


def bib_escape(value: str) -> str:
    return (value.replace("\\", r"\textbackslash{}")
                 .replace("&", r"\&").replace("%", r"\%")
                 .replace("_", r"\_").replace("#", r"\#"))


def first_author_family(authors: str) -> str:
    if not authors:
        return ""
    first = authors.split(" and ", 1)[0].strip()
    return first.split(",", 1)[0].strip()


def crossref_record(doi: str, raw_dir: Path, log_writer: csv.writer, pause: float) -> dict | None:
    filename = safe_doi(doi) + ".json"
    target = raw_dir / filename
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    status = ""
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    error = ""
    for attempt in range(5):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                status = str(response.status)
                body = response.read()
            target.write_bytes(body)
            log_writer.writerow([doi, status, timestamp, str(target), ""])
            if pause:
                time.sleep(pause)
            payload = json.loads(body.decode("utf-8"))
            return payload.get("message")
        except urllib.error.HTTPError as exc:
            status = str(exc.code)
            error = f"HTTPError: {exc.reason}"
            try:
                body = exc.read()
                if body:
                    target.write_bytes(body)
            except Exception:
                pass
            if exc.code in (429, 500, 502, 503, 504) and attempt < 4:
                time.sleep(min(60, 2 ** attempt * 5))
                continue
            break
        except Exception as exc:  # network, decoding, or JSON error is recorded, not guessed around
            error = f"{type(exc).__name__}: {exc}"
            if attempt < 4:
                time.sleep(min(60, 2 ** attempt * 5))
                continue
            break
    log_writer.writerow([doi, status or "NO_RESPONSE", timestamp, str(target), error])
    if pause:
        time.sleep(pause)
    return None


def make_enriched_bib(records: list[dict[str, str]], messages: dict[str, dict | None], out: Path) -> None:
    seen_keys: dict[str, int] = {}
    lines = ["% Generated from saved Crossref REST responses; fields are not inferred.", "% DOI-specific JSON is preserved under crossref_raw/.", "% Stable BibTeX keys use the literature-base record IDs.", ""]
    for row in records:
        doi = row["DOI"].strip()
        m = messages.get(doi)
        if not m:
            continue
        authors = authors_from_message(m)
        title_list = m.get("title") or []
        title = title_list[0] if title_list else ""
        year = issued_year(m)
        container = (m.get("container-title") or [""])[0]
        volume = str(m.get("volume", ""))
        issue = str(m.get("issue", ""))
        page = str(m.get("page") or m.get("article-number") or "")
        if not (title and authors and year):
            continue
        stable_id = (row.get("id") or "").strip()
        if stable_id:
            base_key = re.sub(r"[^A-Za-z0-9_:-]", "", stable_id)
        else:
            base_key = "DOI_" + re.sub(r"[^A-Za-z0-9]", "", doi)
        seen_keys[base_key] = seen_keys.get(base_key, 0) + 1
        key = base_key if seen_keys[base_key] == 1 else f"{base_key}_dup{seen_keys[base_key]}"
        kind = "book" if m.get("type") in ("book", "monograph") else "article"
        fields = [("author", authors), ("title", title), ("year", year), ("doi", doi)]
        if container:
            fields.append(("journal" if kind == "article" else "publisher", container))
        if volume:
            fields.append(("volume", volume))
        if issue:
            fields.append(("number", issue))
        if page:
            fields.append(("pages", page))
        lines.append(f"@{kind}{{{key},")
        lines.extend(f"  {k} = {{{bib_escape(v)}}}," for k, v in fields)
        lines.extend(["}", ""])
    out.write_text("\n".join(lines), encoding="utf-8")


def write_duplicate_doi_audit(base_rows: list[dict[str, str]], local_entries: list[dict[str, str]], out: Path) -> None:
    groups: dict[str, dict[str, list[str]]] = {}
    for row in base_rows:
        doi = (row.get("DOI") or "").strip()
        if DOI_RE.match(doi):
            groups.setdefault(doi, {"literature_ids": [], "local_bib_keys": []})["literature_ids"].append((row.get("id") or "").strip())
    for row in local_entries:
        doi = (row.get("doi") or "").strip()
        if DOI_RE.match(doi):
            groups.setdefault(doi, {"literature_ids": [], "local_bib_keys": []})["local_bib_keys"].append(row.get("key", ""))
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doi", "record_count", "literature_ids", "local_bib_keys", "fetch_count"], lineterminator="\n")
        writer.writeheader()
        for doi, group in sorted(groups.items()):
            count = len(group["literature_ids"]) + len(group["local_bib_keys"])
            if count > 1:
                writer.writerow({"doi": doi, "record_count": count,
                                 "literature_ids": ";".join(x for x in group["literature_ids"] if x),
                                 "local_bib_keys": ";".join(group["local_bib_keys"]), "fetch_count": 1})


def compare(local: dict[str, str], message: dict | None) -> dict[str, str]:
    if not message:
        return {k: "UNVERIFIED" for k in ("doi_status", "title_match", "first_author_match", "year_match", "pages_match")}
    titles = message.get("title") or []
    cross_title = titles[0] if titles else ""
    cross_auth = authors_from_message(message)
    local_auth = local.get("author", "")
    cross_first = first_author_family(cross_auth)
    local_first = first_author_family(local_auth)
    cross_pages = str(message.get("page") or message.get("article-number") or "")
    local_pages = local.get("pages", "").replace("--", "-")
    cross_pages_norm = cross_pages.replace("–", "-").replace("−", "-")
    year = issued_year(message)
    title_match = "YES" if norm(local.get("title", "")) == norm(cross_title) else "NO"
    author_match = "YES" if norm(local_first) and norm(local_first) == norm(cross_first) else "NO"
    year_match = "YES" if local.get("year", "").strip() == year else "NO"
    pages_match = "UNVERIFIED" if not local_pages or not cross_pages_norm else ("YES" if norm(local_pages) == norm(cross_pages_norm) else "NO")
    return {"doi_status": "RESOLVED", "title_match": title_match, "first_author_match": author_match,
            "year_match": year_match, "pages_match": pages_match}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-csv", type=Path, required=True)
    ap.add_argument("--local-bib", type=Path, required=True)
    ap.add_argument("--raw-dir", type=Path, required=True)
    ap.add_argument("--references-dir", type=Path, required=True)
    ap.add_argument("--pause", type=float, default=1.0)
    args = ap.parse_args()
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.references_dir.mkdir(parents=True, exist_ok=True)

    with args.base_csv.open(encoding="utf-8-sig", newline="") as f:
        base_rows = list(csv.DictReader(f))
    local_entries = parse_bib(args.local_bib)
    dois = sorted({r.get("DOI", "").strip() for r in base_rows if DOI_RE.match(r.get("DOI", "").strip())} |
                  {r.get("doi", "").strip() for r in local_entries if DOI_RE.match(r.get("doi", "").strip())})
    log_path = args.references_dir / "crossref_request_log.csv"
    messages: dict[str, dict | None] = {}
    with log_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["doi", "http_status", "timestamp_utc", "raw_json", "error"])
        for n, doi in enumerate(dois, 1):
            print(f"Crossref {n}/{len(dois)}: {doi}", flush=True)
            messages[doi] = crossref_record(doi, args.raw_dir, writer, args.pause)

    bib_path = args.references_dir / "literature_base_enriched.bib"
    make_enriched_bib(base_rows, messages, bib_path)
    write_duplicate_doi_audit(base_rows, local_entries, args.references_dir / "duplicate_doi_audit.csv")

    audit_path = args.references_dir / "local_bib_crossref_audit.csv"
    with audit_path.open("w", encoding="utf-8", newline="") as f:
        fields = ["key", "doi", "status", "title_match", "first_author_match", "year_match", "pages_match", "raw_json"]
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in local_entries:
            doi = row.get("doi", "").strip()
            has_doi = bool(DOI_RE.match(doi))
            result = compare(row, messages.get(doi)) if has_doi else {k: "UNVERIFIED" for k in ("doi_status", "title_match", "first_author_match", "year_match", "pages_match")}
            full_match = all(result[k] == "YES" for k in MATCH_FIELDS)
            mismatch = any(result[k] == "NO" for k in MATCH_FIELDS)
            audit_status = ("RESOLVED-MATCH" if full_match else
                            "RESOLVED-MISMATCH" if has_doi and messages.get(doi) and mismatch else
                            "RESOLVED-UNVERIFIED" if has_doi and messages.get(doi) else "UNVERIFIED")
            writer.writerow({"key": row["key"], "doi": doi, "status": audit_status,
                             "title_match": result["title_match"], "first_author_match": result["first_author_match"],
                             "year_match": result["year_match"], "pages_match": result["pages_match"],
                             "raw_json": str(args.raw_dir / (safe_doi(doi) + ".json")) if has_doi and (args.raw_dir / (safe_doi(doi) + ".json")).exists() else ""})

    # Update the historical audit table only where the saved response can be cited and compared.
    doi_csv = args.references_dir / "doi_verification.csv"
    if doi_csv.exists():
        with doi_csv.open(encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
            cols = list(rows[0].keys()) if rows else []
        if rows:
            for row in rows:
                doi = row.get("doi", "").strip()
                if not DOI_RE.match(doi):
                    row["doi_syntax_valid"] = "N/A"
                    row["verified"] = "UNVERIFIED"
                    row["crossref_match"] = "N/A"
                    row["crossref_title_match"] = "N/A"
                    row["verification_source"] = "No DOI/raw response; archival verification not attached"
                    continue
                row["doi_syntax_valid"] = "YES"
                raw = messages.get(doi)
                local = next((x for x in local_entries if x.get("key") == row.get("bib_key")), {})
                result = compare(local, raw)
                full_match = all(result[k] == "YES" for k in MATCH_FIELDS)
                mismatch = any(result[k] == "NO" for k in MATCH_FIELDS)
                row["crossref_match"] = "YES" if full_match else ("NO" if mismatch else "UNVERIFIED")
                row["crossref_title_match"] = result["title_match"]
                row["verified"] = "YES" if full_match else ("NO-MATCH" if raw and mismatch else "UNVERIFIED")
                row["verification_source"] = (f"Crossref REST raw JSON: crossref_raw/{safe_doi(doi)}.json; see field-by-field results in local_bib_crossref_audit.csv"
                                               if raw else "No saved Crossref response; recheck required")
                row["verified_date"] = dt.datetime.now(dt.timezone.utc).date().isoformat() if raw else ""
            with doi_csv.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
                writer.writeheader()
                writer.writerows(rows)

    report = args.references_dir / "doi_verification_method.md"
    n_ok = sum(1 for x in local_entries if x.get("doi", "").strip() and messages.get(x["doi"].strip()))
    report.write_text(f"""# DOI verification method and current evidence\n\n\
Generated: {dt.datetime.now(dt.timezone.utc).isoformat()}\n\n\
The manually-triggered Crossref job requested `https://api.crossref.org/works/<URL-encoded DOI>` with User-Agent `{USER_AGENT}`. The exact response body for each successful DOI is preserved at `phase5/references/crossref_raw/<sanitized DOI>.json`; `crossref_request_log.csv` records DOI, HTTP status, UTC timestamp, raw-file path, and errors. No Crossref field is reconstructed or inferred.\n\n\
The local bibliography audit compares title, first-author family name, issued year, and page/article-number fields; each comparison is reported in `local_bib_crossref_audit.csv`. A row is marked matched only where all four comparisons are YES. Missing page data remain UNVERIFIED rather than being treated as a match; any field disagreement is reported as a mismatch. Crossref is fetched once per unique DOI; duplicate records are enumerated in `duplicate_doi_audit.csv`. Enriched BibTeX keys use stable literature-base IDs. The literature-base BibTeX is generated from the saved raw Crossref fields only. Records without a DOI or without a successful raw response remain UNVERIFIED.\n\n\
Current run: {len(dois)} unique DOI requests across {len(base_rows)} literature-base records and {len(local_entries)} local BibTeX entries; {n_ok} local-bibliography DOIs have saved responses.\n\n\
Before this workflow's first successful run, the repository contained no per-DOI raw Crossref JSON, request log, or reproducible verification script. Therefore the prior `YES` values in the previous CSV could not be independently reconstructed from repository evidence; they have been superseded by the comparisons and raw responses generated here.\n""", encoding="utf-8")
    print(f"Wrote {bib_path}, {audit_path}, {log_path}, and {report}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
