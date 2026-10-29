#!/usr/bin/env python3
"""Apply only Crossref-VERIFIED, technically eligible R3b citations before strict build."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import crossref_enrich as cr


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def bib_blocks(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    return {match.group(2).strip(): match.group(0)
            for match in re.finditer(r"(?ms)^@(\w+)\{([^,]+),\n.*?^\}", text)}


def merge_bib(local_path: Path, generated_path: Path) -> tuple[int, set[str]]:
    local_text = local_path.read_text(encoding="utf-8")
    local_entries = {entry["key"]: entry for entry in cr.parse_bib(local_path)}
    generated = bib_blocks(generated_path)
    added: set[str] = set()
    preserve = {"status", "theory_family", "equation_source_status", "claim_status", "note", "notes", "url", "issn", "isbn"}
    for key, block in generated.items():
        existing = local_entries.get(key, {})
        extras = [f"  {field} = {{{existing[field]}}}," for field in sorted(preserve) if existing.get(field)]
        extras.extend(("  verified = {YES},", "  source = {Crossref},", "  access_date = {2026-10-22},"))
        block = block.rstrip()
        block = block[:block.rfind("}")].rstrip() + "\n" + "\n".join(extras) + "\n}"
        pattern = re.compile(rf"(?ms)^@\w+\{{{re.escape(key)},\n.*?^\}}")
        if key in local_entries:
            local_text, count = pattern.subn(lambda _match, value=block: value, local_text, count=1)
            if count != 1:
                raise RuntimeError(f"Expected one existing BibTeX entry for {key}, found {count}")
        else:
            local_text = local_text.rstrip() + "\n\n" + block + "\n"
            added.add(key)
    local_path.write_text(local_text, encoding="utf-8")
    parsed = cr.parse_bib(local_path)
    counts = Counter(entry["key"] for entry in parsed)
    duplicates = [key for key, count in counts.items() if count > 1]
    if duplicates:
        raise RuntimeError("Duplicate BibTeX keys after R3b merge: " + ", ".join(duplicates))
    return len(generated), added


def remove_bad_citations(text: str, bad_keys: set[str]) -> str:
    if not bad_keys:
        return text
    cite_pattern = re.compile(r"\\cite(?:[tp])?\*?(?:\[[^]]*\])?\{([^}]+)\}")

    def clean(match: re.Match[str]) -> str:
        keys = [key.strip() for key in match.group(1).split(",") if key.strip()]
        keep = [key for key in keys if key not in bad_keys]
        if len(keep) == len(keys):
            return match.group(0)
        if not keep:
            return ""
        return "\\cite{" + ",".join(keep) + "}"

    return cite_pattern.sub(clean, text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-csv", type=Path, required=True)
    parser.add_argument("--map-csv", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--reports-dir", type=Path, required=True)
    parser.add_argument("--sections-dir", type=Path, required=True)
    parser.add_argument("--status-report", type=Path, required=True)
    args = parser.parse_args()

    verify_rows = read_csv(args.verify_csv)
    map_rows = read_csv(args.map_csv)
    verify_by_key = {row.get("citekey", ""): row for row in verify_rows if row.get("citekey")}
    all_tex = {path.name: path for path in args.sections_dir.glob("sec*.tex")}

    # Group the source-specific summaries by their mapped manuscript subsection.
    additions: dict[Path, dict[str, list[tuple[str, str, str]]]] = defaultdict(lambda: defaultdict(list))
    cited_keys: set[str] = set()
    unresolved_map: list[str] = []
    mapped_keys = {row.get("citekey", "").strip() for row in map_rows}
    bad_keys = {row["citekey"] for row in verify_rows
                if row.get("technical_claim_eligible") == "YES" and row.get("status") in {"MISMATCH", "NOT-FOUND"}}

    for mapping in map_rows:
        key = mapping.get("citekey", "").strip()
        row = verify_by_key.get(key)
        if not row or row.get("status") != "VERIFIED" or row.get("technical_claim_eligible") != "YES" or row.get("bib_ready") != "YES":
            unresolved_map.append(key)
            continue
        resolved = row.get("resolved_citekey", "").strip()
        if not resolved:
            unresolved_map.append(key)
            continue
        section_number = mapping.get("section", "").split(".")[-1]
        source = f"sec{int(section_number):02d}_" if section_number.isdigit() else ""
        target = next((path for name, path in all_tex.items() if name.startswith(source)), None)
        if target is None:
            raise RuntimeError(f"No manuscript source file for mapped section {mapping.get('section')}")
        anchor = mapping.get("anchor", "").strip()
        additions[target][anchor].append((mapping.get("claim_short", "").strip(), mapping.get("risk", "CONDITIONAL").strip(), resolved))
        cited_keys.add(resolved)

    # Remove only scoped eligible R3b citations that failed verification; other baseline citations are untouched.
    for target in set(all_tex.values()):
        if not target.name.startswith(tuple(f"sec{n:02d}_" for n in (*range(5, 10), *range(11, 14)))):
            continue
        text = target.read_text(encoding="utf-8")
        text = remove_bad_citations(text, bad_keys)
        text = re.sub(r"(?ms)^\\paragraph\{R3b source-specific evidence\.\}.*?(?=^\\subsection\{Open questions for Section )", "", text)
        for anchor, sentences in additions.get(target, {}).items():
            block = ["\\paragraph{R3b source-specific evidence.}"]
            for summary, label, citekey in sentences:
                label = label.upper().replace("_", "-")
                block.append(f"{summary} ({label}) \\cite{{{citekey}}}.")
            rendered = " ".join(block) + "\n\n"
            if "\\paragraph{R3b source-specific evidence.}" in text:
                text = re.sub(r"(?ms)^\\paragraph\{R3b source-specific evidence\.\}.*?(?=^\\subsection\{Open questions for Section )", "", text)
            if text.count(anchor) != 1:
                raise RuntimeError(f"Expected one insertion anchor in {target}: {anchor!r}; found {text.count(anchor)}")
            text = text.replace(anchor, rendered + anchor, 1)
        target.write_text(text, encoding="utf-8")

    local_bib = args.local_bib
    generated_bib = args.reports_dir / "R3B_VERIFIED_REFERENCES.bib"
    bib_count, new_bib_keys = merge_bib(local_bib, generated_bib)

    # Check every newly inserted citation has a BibTeX entry.
    local_keys = {entry["key"] for entry in cr.parse_bib(local_bib)}
    missing = sorted(cited_keys - local_keys)
    if missing:
        raise RuntimeError("R3b citations missing BibTeX entries: " + ", ".join(missing))

    r3a_rows = read_csv(args.reports_dir / "CROSSREF_VERIFY.csv")
    r3a_counts = Counter(row["status"] for row in r3a_rows)
    r3a_eligible = sum(row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES" for row in r3a_rows)
    r3a_reclassified = sum(row.get("reclassified_from") == "MISMATCH" for row in r3a_rows)
    r3a_background = sum(row.get("citation_scope") == "background-only" and row.get("bib_ready") == "YES" for row in r3a_rows)
    r3b_counts = Counter(row["status"] for row in verify_rows)
    r3b_eligible_verified = sum(row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES" for row in verify_rows)
    r3b_verified_unready = [row for row in verify_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") != "YES"]
    r3b_no_doi_eligible = [row for row in verify_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") == "NO-DOI"]
    r3b_mismatches = [row for row in verify_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") in {"MISMATCH", "NOT-FOUND"}]
    r3b_section_counts = Counter(row["section"] for row in verify_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES")
    r3a_section_counts = Counter(row["section"] for row in r3a_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES")
    all_counts = r3a_section_counts + r3b_section_counts
    eligible_sections = [f"{section.replace('s.', '')} ({count})" for section, count in sorted(all_counts.items()) if count >= 6]
    human_r3a = (args.reports_dir / "CROSSREF_HUMAN_CHECK.md").read_text(encoding="utf-8").strip()
    human_r3b = (args.reports_dir / "CROSSREF_R3B_HUMAN_CHECK.md").read_text(encoding="utf-8").strip()

    report = args.status_report.read_text(encoding="utf-8")
    start = report.find("## R3b verification and evidence")
    if start < 0:
        raise RuntimeError("R3_STATUS.md lacks the R3b insertion section")
    end = report.find("## Final strict build", start)
    if end < 0:
        raise RuntimeError("R3_STATUS.md lacks the final-build section")
    map_matches = sum(bool(row.get("citation_map_claims", "")) for row in verify_rows if row.get("technical_claim_eligible") == "YES")
    result_block = [
        "## R3b verification and evidence",
        "",
        f"- Scope: {len(verify_rows)} REFERENCE_PLAN rows from sections 5–9 and 11–13; {sum(row.get('status') not in {'INELIGIBLE', 'NO-DOI'} for row in verify_rows)} technically eligible DOI rows queried; {len({row['DOI'] for row in verify_rows if row.get('status') not in {'INELIGIBLE', 'NO-DOI'} and row.get('DOI')})} unique Crossref requests.",
        f"- R3b Crossref results: {r3b_counts['VERIFIED']} VERIFIED, {r3b_counts['MISMATCH']} MISMATCH, {r3b_counts['NOT-FOUND']} NOT-FOUND, {r3b_counts['NO-DOI']} NO-DOI; {r3b_counts['INELIGIBLE']} metadata-only rows INELIGIBLE and not queried.",
        f"- Technical-eligible R3b rows: {r3b_eligible_verified} VERIFIED and bibliography-ready; {len(r3b_verified_unready)} VERIFIED but not bibliography-ready; {len(r3b_no_doi_eligible)} NO-DOI; {sum(row.get('technical_claim_eligible') == 'YES' and row.get('status') == 'MISMATCH' for row in verify_rows)} MISMATCH; {sum(row.get('technical_claim_eligible') == 'YES' and row.get('status') == 'NOT-FOUND' for row in verify_rows)} NOT-FOUND.",
        f"- R3b mapped citations inserted: {len(cited_keys)} unique verified eligible keys; new BibTeX keys added in this build: {len(new_bib_keys)}. No metadata-only or unverified row is inserted as technical evidence.",
        f"- Sections meeting ≥6 evidence-ready sources across R3a/R3b: {', '.join(eligible_sections) if eligible_sections else 'none'}.",
        "- R3b human-check list: `CROSSREF_R3B_HUMAN_CHECK.md`.",
        "- R3a final counts after cached-response reclassification: " + f"{r3a_counts['VERIFIED']} VERIFIED / {r3a_counts['MISMATCH']} MISMATCH / {r3a_counts['NOT-FOUND']} NOT-FOUND; {r3a_reclassified} rows record `reclassified_from=MISMATCH`; {r3a_eligible} technical-eligible bibliography-ready keys; {r3a_background} background-only review key.",
        "- R3a title human-check list: `CROSSREF_HUMAN_CHECK.md`.",
        "- Frozen `CITATION_MAP.csv` exact-key matches in the R3b candidate set: " + str(map_matches) + ". Section-specific additions are mapped in `R3B_CITATION_MAP.csv` from the eligible plan rows and their documented source claims.",
        "- Remaining gaps: Section 10 is reserved for R3c; Section 11 GAP-09 remains open; R3b MISMATCH, NOT-FOUND, and NO-DOI rows remain uncited. R3b rows with a title overlap below 0.60 are in `CROSSREF_R3B_HUMAN_CHECK.md`.",
        "",
        "### R3b unresolved identifiers (not cited)",
        "",
    ]
    if r3b_mismatches or r3b_no_doi_eligible or r3b_verified_unready:
        for row in r3b_mismatches + r3b_no_doi_eligible + r3b_verified_unready:
            result_block.append(f"- {row['lit_id']} `{row['citekey']}` — {row['status']}: {row.get('reason','')}")
    else:
        result_block.append("None among mapped, technically eligible R3b rows.")
    result_block += ["", ""]
    report = report[:start] + "\n".join(result_block) + report[end:]
    args.status_report.write_text(report, encoding="utf-8")
    print(f"R3b applied {len(cited_keys)} citations; {len(new_bib_keys)} new BibTeX keys; R3a background-only keys={r3a_background}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
