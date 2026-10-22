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
import html
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


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def _normal_metadata(value: str) -> str:
    import unicodedata
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]*>", " ", value)  # Crossref occasionally embeds inline markup in titles.
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.replace("&", " and ")
    value = re.sub(r"\\[A-Za-z]+\*?(?:\{([^{}]*)\})?", lambda m: m.group(1) or "", value)
    value = re.sub(r"[^a-zA-Z0-9]+", " ", value).lower().strip()
    return re.sub(r"\s+", " ", value)


def _normal_venue(value: str) -> str:
    # Remove editorial notes and trailing volume/issue/page locators, but retain
    # named editions such as "English Edition" and normalize only explicit abbreviations.
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]*>", " ", value)
    value = re.sub(r"\s+\((?=[^)]*(?:published online|online\s+\d|volume/pages))[^)]*\)", "", value, flags=re.I)
    value = re.sub(r"\s+\d{1,4}(?:\(\d+\))?\s*[,;:]\s*[\w./–-]+\s*$", "", value)
    abbreviations = {
        "int": "international", "j": "journal", "mech": "mechanics",
        "phys": "physics", "physical": "physics", "physics": "physics",
        "sci": "science", "science": "science", "sciences": "science",
        "transf": "transfer", "therm": "thermal", "proc": "proceedings",
        "natl": "national", "acad": "academy", "appl": "applied", "applied": "applied",
        "mater": "materials", "material": "materials", "materials": "materials",
        "eng": "engineering", "engl": "english", "english": "english", "ed": "edition",
        "math": "mathematics", "comp": "computational", "rev": "review",
        "adv": "adv", "advances": "adv", "advanced": "adv",
        "struct": "structures", "structures": "structures", "technol": "technology", "sect": "section",
        "univ": "university", "lett": "letters", "res": "research", "commun": "communications",
        "des": "design", "mach": "machines",
    }
    tokens = _normal_metadata(value).split()
    return " ".join(abbreviations.get(token, token) for token in tokens if token not in {"of", "the", "and"})


def _crossref_years(message: dict) -> set[str]:
    years: set[str] = set()
    for field in ("published-print", "published-online", "issued"):
        for parts in (message.get(field, {}) or {}).get("date-parts", []) or []:
            if parts:
                years.add(str(parts[0]))
    return years


def _crossref_metadata(message: dict) -> dict:
    # Keep bibliographic metadata only; omit abstracts, references, links, and other content.
    allowed = ("DOI", "type", "title", "author", "published-print", "published-online", "issued",
               "container-title", "short-container-title", "publisher", "volume", "issue", "page",
               "article-number", "ISSN", "ISBN")
    return {key: message[key] for key in allowed if key in message}


def _load_r3a_raw(doi: str, raw_dir: Path) -> tuple[int, dict | None]:
    target = raw_dir / (safe_doi(doi) + ".json")
    if not target.is_file():
        raise RuntimeError(f"Saved Crossref metadata is missing for {doi}: {target}")
    try:
        payload = json.loads(target.read_text(encoding="utf-8"))
        status = int(payload["http_status"])
        message = payload.get("message")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise RuntimeError(f"Saved Crossref metadata is invalid for {doi}: {target}: {exc}") from exc
    if status == 404:
        return status, None
    if status != 200 or not isinstance(message, dict):
        raise RuntimeError(f"Saved Crossref metadata has unexpected status/content for {doi}: {status}")
    return status, message


def _fetch_r3a(doi: str, raw_dir: Path, log_writer: csv.writer, pause: float) -> tuple[int, dict | None]:
    filename = safe_doi(doi) + ".json"
    target = raw_dir / filename
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    last_error = ""
    for attempt in range(5):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                http_status = int(response.status)
                payload = json.loads(response.read().decode("utf-8"))
            message = payload.get("message") or {}
            metadata = _crossref_metadata(message)
            target.write_text(json.dumps({"query_doi": doi, "http_status": http_status,
                                          "message": metadata}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            log_writer.writerow([doi, http_status, timestamp, str(target), ""])
            if pause:
                time.sleep(pause)
            return http_status, metadata
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                target.write_text(json.dumps({"query_doi": doi, "http_status": 404, "message": None}, indent=2) + "\n", encoding="utf-8")
                log_writer.writerow([doi, 404, timestamp, str(target), "not found"])
                if pause:
                    time.sleep(pause)
                return 404, None
            last_error = f"HTTP {exc.code}: {exc.reason}"
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 4:
                break
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt == 4:
                break
        time.sleep(min(30, 2 ** attempt * 2))
    log_writer.writerow([doi, "NO_RESPONSE", dt.datetime.now(dt.timezone.utc).isoformat(), str(target), last_error])
    raise RuntimeError(f"Crossref request failed for {doi}; no verification row will be emitted: {last_error}")


def _bib_from_crossref(key: str, doi: str, message: dict, preferred_year: str = "") -> str:
    authors = authors_from_message(message)
    title_values = message.get("title") or []
    title = title_values[0] if title_values else ""
    title = html.unescape(re.sub(r"<[^>]*>", " ", title))
    title = re.sub(r"\s+", " ", title).strip()
    year = preferred_year if preferred_year in _crossref_years(message) else issued_year(message)
    container_values = message.get("container-title") or message.get("short-container-title") or []
    container = container_values[0] if container_values else ""
    kind = "book" if message.get("type") in ("book", "monograph") else "article"
    fields = [("author", authors), ("title", title), ("year", year), ("doi", doi)]
    if container:
        fields.append(("journal" if kind == "article" else "publisher", container))
    for source, dest in (("volume", "volume"), ("issue", "number"), ("page", "pages"), ("article-number", "pages")):
        value = str(message.get(source, ""))
        if value and not any(existing == dest for existing, _ in fields):
            fields.append((dest, value))
    lines = [f"@{kind}{{{key},"]
    lines.extend(f"  {field} = {{{bib_escape(value)}}}," for field, value in fields if value)
    lines.append("}")
    return "\n".join(lines)


def run_r3a(args: argparse.Namespace) -> int:
    base_rows = _read_csv(args.base_csv)
    plan_rows = _read_csv(args.plan_csv)
    citation_rows = _read_csv(args.citation_map_csv)
    row_index = {row.get("id", ""): row for row in _read_csv(args.row_index_csv)}
    base_by_id = {row.get("id", ""): row for row in base_rows}
    if len(base_by_id) != len(base_rows):
        raise ValueError("LITERATURE_BASE contains duplicate ids")
    sections = {f"s.4.{number}" for number in range(1, 13)}
    scoped = [row for row in plan_rows if row.get("plan_section", "").strip() in sections]
    missing_ids = sorted({row.get("lit_id", "") for row in scoped} - set(base_by_id))
    if missing_ids:
        raise ValueError("REFERENCE_PLAN ids absent from LITERATURE_BASE: " + ", ".join(missing_ids))
    for row in scoped:
        indexed = row_index.get(row.get("lit_id", ""))
        if indexed and (indexed.get("DOI", "").strip().lower() != base_by_id[row["lit_id"]].get("DOI", "").strip().lower()):
            raise ValueError(f"LITERATURE_ROW_INDEX DOI conflicts with LITERATURE_BASE for {row['lit_id']}")

    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    dois = sorted({base_by_id[row["lit_id"]].get("DOI", "").strip() for row in scoped
                   if DOI_RE.match(base_by_id[row["lit_id"]].get("DOI", "").strip())})
    log_path = args.report_dir / "CROSSREF_REQUEST_LOG.csv"
    messages: dict[str, tuple[int, dict | None]] = {}
    if args.reuse_raw:
        for index, doi in enumerate(dois, 1):
            print(f"Reuse saved Crossref response {index}/{len(dois)}: {doi}", flush=True)
            messages[doi] = _load_r3a_raw(doi, args.raw_dir)
        if not log_path.is_file():
            raise RuntimeError(f"Request log is missing while reusing saved responses: {log_path}")
    else:
        with log_path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, lineterminator="\n")
            writer.writerow(["DOI", "HTTP_status", "timestamp_utc", "metadata_json", "error"])
            for index, doi in enumerate(dois, 1):
                print(f"Crossref {index}/{len(dois)}: {doi}", flush=True)
                messages[doi] = _fetch_r3a(doi, args.raw_dir, writer, args.pause)

    map_by_key: dict[str, list[str]] = {}
    for item in citation_rows:
        keys = re.split(r"[;,]\s*", item.get("proposed_citations", ""))
        for key in keys:
            if key.strip():
                map_by_key.setdefault(key.strip(), []).append(item.get("claim_id", ""))

    verify_path = args.report_dir / "CROSSREF_VERIFY.csv"
    verify_fields = ["lit_id", "citekey", "resolved_citekey", "section", "DOI", "status", "title_match", "year_match",
                     "venue_match", "crossref_title", "crossref_year", "crossref_years", "crossref_venue", "technical_claim_eligible",
                     "read_level", "prior_api_log", "citation_map_claims", "raw_json", "reason", "bib_ready"]
    verified_bib: list[str] = ["% R3a entries only: Crossref VERIFIED and REFERENCE_PLAN technical_claim_eligible=YES.",
                               "% Metadata-only/NO rows are deliberately excluded; authors/fields come from saved Crossref JSON.", ""]
    rows_out: list[dict[str, str]] = []
    existing_entries = parse_bib(args.local_bib)
    existing_by_key = {entry["key"]: entry for entry in existing_entries}
    existing_by_doi: dict[str, list[dict[str, str]]] = {}
    for entry in existing_entries:
        if entry.get("doi", "").strip():
            existing_by_doi.setdefault(entry["doi"].strip().lower(), []).append(entry)
    bib_written: set[str] = set()

    for plan in scoped:
        lit_id = plan.get("lit_id", "")
        base = base_by_id[lit_id]
        doi = base.get("DOI", "").strip()
        if not DOI_RE.match(doi):
            continue  # no-DOI printed sources are recorded separately in R3_STATUS.md
        http_status, message = messages[doi]
        title_values = (message or {}).get("title") or []
        cross_title = title_values[0] if title_values else ""
        cross_year = issued_year(message or {})
        cross_venues = ((message or {}).get("container-title") or []) + ((message or {}).get("short-container-title") or [])
        cross_venue = cross_venues[0] if cross_venues else ""
        title_match = "YES" if cross_title and _normal_metadata(base.get("title", "")).replace(" ", "") == _normal_metadata(cross_title).replace(" ", "") else "NO"
        matching_years = _crossref_years(message or {})
        year_match = "YES" if base.get("year", "").strip() in matching_years else "NO"
        base_venue = _normal_venue(base.get("venue", ""))
        venue_match = "YES" if base_venue and any(base_venue == _normal_venue(v) for v in cross_venues) else "NO"
        response_doi = (message or {}).get("DOI", "").strip().lower()
        doi_match = response_doi == doi.lower()
        status = "NOT-FOUND" if http_status == 404 else ("VERIFIED" if title_match == year_match == venue_match == "YES" and doi_match else "MISMATCH")
        reason_parts = []
        if not doi_match and http_status != 404:
            reason_parts.append("DOI field differs from requested DOI")
        for label, value in (("title", title_match), ("year", year_match), ("venue", venue_match)):
            if value != "YES":
                reason_parts.append(f"{label} does not match LITERATURE_BASE")
        if http_status == 404:
            reason_parts.append("Crossref returned HTTP 404")
        key = plan.get("citekey", "").strip()
        eligible = plan.get("technical_claim_eligible", "").strip().upper() == "YES"
        resolved_key = ""
        claims = "; ".join(sorted(set(map_by_key.get(key, []))))
        prior = "NOT_IN_INDEX"
        if lit_id in row_index:
            prior = "HISTORICAL_HTTP_" + row_index[lit_id].get("http_status", "UNKNOWN")
        bib_ready = "NO"
        if status == "VERIFIED" and eligible and key and authors_from_message(message or {}):
            existing_for_doi = existing_by_doi.get(doi.lower(), [])
            target_key = existing_for_doi[0]["key"] if existing_for_doi else key
            conflict = target_key in existing_by_key and existing_by_key[target_key].get("doi", "").strip().lower() != doi.lower()
            if not conflict:
                bib_ready = "YES"
                resolved_key = target_key
                claims = "; ".join(sorted(set(map_by_key.get(key, []) + map_by_key.get(target_key, []))))
                if target_key not in bib_written:
                    preferred_year = base.get("year", "").strip() if base.get("year", "").strip() in matching_years else ""
                    verified_bib.append(_bib_from_crossref(target_key, doi, message or {}, preferred_year))
                    verified_bib.append("")
                    bib_written.add(target_key)
            else:
                reason_parts.append(f"citekey {target_key} already belongs to a different DOI")
        elif status == "VERIFIED" and eligible and not authors_from_message(message or {}):
            reason_parts.append("Crossref author metadata is empty; do not emit a BibTeX entry")
        elif status == "VERIFIED" and eligible and not key:
            reason_parts.append("REFERENCE_PLAN has no citekey; do not emit a BibTeX entry")
        rows_out.append({"lit_id": lit_id, "citekey": key, "resolved_citekey": resolved_key, "section": plan.get("plan_section", ""), "DOI": doi,
                         "status": status, "title_match": title_match, "year_match": year_match,
                         "venue_match": venue_match, "crossref_title": cross_title, "crossref_year": cross_year,
                         "crossref_years": "; ".join(sorted(matching_years)),
                         "crossref_venue": "; ".join(cross_venues), "technical_claim_eligible": "YES" if eligible else "NO",
                         "read_level": plan.get("read_level", ""), "prior_api_log": prior,
                         "citation_map_claims": claims, "raw_json": str(args.raw_dir / (safe_doi(doi) + ".json")),
                         "reason": "; ".join(reason_parts), "bib_ready": bib_ready})

    with verify_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=verify_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows_out)
    (args.report_dir / "R3A_VERIFIED_REFERENCES.bib").write_text("\n".join(verified_bib), encoding="utf-8")
    method = f"""# R3a Crossref verification method

Scope: REFERENCE_PLAN rows whose `plan_section` is s.4.1–s.4.12. Each `lit_id` is joined to `LITERATURE_BASE.id`; the DOI is read only from the capitalized `DOI` column. `CITATION_MAP.csv` supplies claim-to-key associations, and `LITERATURE_ROW_INDEX.csv` is checked only for consistency/history (its old HTTP status never upgrades a row to VERIFIED).

For each unique DOI, the job requests `https://api.crossref.org/works/<URL-encoded DOI>` with `{USER_AGENT}`. `CROSSREF_REQUEST_LOG.csv` records DOI, HTTP status, UTC time, metadata-file path, and error. `crossref_raw/` contains an allowlisted Crossref metadata projection (DOI, type, title, authors, issued/published dates, venue, publisher, volume/issue/pages, ISSN/ISBN); abstracts, links, reference lists, and full-text material are excluded.

`CROSSREF_VERIFY.csv` compares DOI, normalized title, year, and venue against `LITERATURE_BASE`. HTML tags/entities are normalized in titles. Venue comparison removes explicit editorial notes and trailing volume/page locators, then expands a fixed set of journal abbreviations and common word variants. The base year may match a Crossref `published-print`, `published-online`, or `issued` year; deposit/creation dates are not treated as publication years, and all eligible Crossref publication years are retained in the audit CSV. No row-index HTTP code is treated as verification evidence. `VERIFIED` requires DOI, title, year, and venue all to match. A Crossref HTTP 404 is `NOT-FOUND`; a returned record with any disagreement is `MISMATCH`. Network/decoding failures fail the job instead of being relabelled as NOT-FOUND. `--reuse-raw` recomputes the comparison from the previously saved responses without making new network requests or changing the original request log.

`R3A_VERIFIED_REFERENCES.bib` includes only `VERIFIED` rows with `technical_claim_eligible=YES`, a nonempty Crossref author field, and no conflicting existing BibTeX key. New author and bibliographic fields are taken from the saved metadata JSON. Metadata-only/NONE rows are excluded.

Counts: {len(scoped)} plan rows in scope; {len(rows_out)} rows with a Crossref DOI; {len(dois)} unique DOI requests; {sum(row['status'] == 'VERIFIED' for row in rows_out)} VERIFIED; {sum(row['status'] == 'MISMATCH' for row in rows_out)} MISMATCH; {sum(row['status'] == 'NOT-FOUND' for row in rows_out)} NOT-FOUND; {len(bib_written)} bibliography-ready eligible keys. No DOI records are handled separately in R3_STATUS.md as printed-source leads, not fabricated DOI matches.
"""
    (args.report_dir / "CROSSREF_METHOD.md").write_text(method, encoding="utf-8")
    print(f"R3a Crossref rows={len(rows_out)}; unique DOI requests={len(dois)}; bib-ready entries={len(bib_written)}")
    print(f"Wrote {verify_path} and {args.report_dir / 'R3A_VERIFIED_REFERENCES.bib'}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-csv", type=Path, required=True)
    ap.add_argument("--local-bib", type=Path, required=True)
    ap.add_argument("--raw-dir", type=Path, required=True)
    ap.add_argument("--references-dir", type=Path, required=True)
    ap.add_argument("--plan-csv", type=Path)
    ap.add_argument("--citation-map-csv", type=Path)
    ap.add_argument("--row-index-csv", type=Path)
    ap.add_argument("--report-dir", type=Path)
    ap.add_argument("--pause", type=float, default=1.0)
    ap.add_argument("--reuse-raw", action="store_true", help="recompute R3a status from saved Crossref responses without querying Crossref")
    args = ap.parse_args()
    if args.plan_csv:
        required = (args.citation_map_csv, args.row_index_csv, args.report_dir)
        if any(value is None for value in required):
            ap.error("R3a mode requires --citation-map-csv, --row-index-csv, and --report-dir")
        return run_r3a(args)
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
