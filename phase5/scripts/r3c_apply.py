#!/usr/bin/env python3
"""Apply mapped, verified R3c Section 10 citations and document Section 4.11 gaps."""
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


def bib_blocks(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    return {match.group(2).strip(): match.group(0)
            for match in re.finditer(r"(?ms)^@(\w+)\{([^,]+),\n.*?^\}", text)}


def merge_bib(local_path: Path, generated_path: Path) -> set[str]:
    local_text = local_path.read_text(encoding="utf-8")
    entries = {entry["key"]: entry for entry in cr.parse_bib(local_path)}
    added: set[str] = set()
    preserve = {"status", "theory_family", "claim_status", "equation_source_status", "note", "notes", "url", "issn", "isbn"}
    for key, block in bib_blocks(generated_path).items():
        old = entries.get(key, {})
        if old and old.get("doi", "").strip().lower() != re.search(r"(?mi)^\s*doi\s*=\s*\{([^}]*)\}", block).group(1).strip().lower():
            raise RuntimeError(f"BibTeX key/DOI conflict for {key}")
        extra = [f"  {field} = {{{old[field]}}}," for field in sorted(preserve) if old.get(field)]
        extra += ["  verified = {YES},", "  source = {Crossref},", "  access_date = {2026-10-23},"]
        block = block.rstrip()
        block = block[:block.rfind("}")].rstrip() + "\n" + "\n".join(extra) + "\n}"
        pattern = re.compile(rf"(?ms)^@\w+\{{{re.escape(key)},\n.*?^\}}")
        if key in entries:
            local_text, n = pattern.subn(lambda _m, v=block: v, local_text, count=1)
            if n != 1:
                raise RuntimeError(f"Expected one local BibTeX entry for {key}, found {n}")
        else:
            local_text = local_text.rstrip() + "\n\n" + block + "\n"
            added.add(key)
    local_path.write_text(local_text, encoding="utf-8")
    parsed = cr.parse_bib(local_path)
    counts = Counter(row["key"] for row in parsed)
    duplicate = sorted(key for key, count in counts.items() if count > 1)
    if duplicate:
        raise RuntimeError("Duplicate BibTeX keys after R3c merge: " + ", ".join(duplicate))
    return added


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-csv", type=Path, required=True)
    parser.add_argument("--prior-r3b-verify", type=Path, required=True)
    parser.add_argument("--map-csv", type=Path, required=True)
    parser.add_argument("--reports-dir", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--sections-dir", type=Path, required=True)
    parser.add_argument("--status-report", type=Path, required=True)
    args = parser.parse_args()

    r3c_rows = read_csv(args.verify_csv)
    r3b_rows = read_csv(args.prior_r3b_verify)
    mappings = read_csv(args.map_csv)
    map_by_key = {row.get("citekey", "").strip(): row for row in mappings if row.get("citekey", "").strip()}
    current_by_key = {row.get("citekey", "").strip(): row for row in r3c_rows if row.get("citekey", "").strip()}
    prior_by_key = {row.get("citekey", "").strip(): row for row in r3b_rows if row.get("citekey", "").strip()}

    # Carry-forward Kumar2017 only if the R3b Crossref check still meets all gates.
    selected: dict[str, dict[str, str]] = {}
    for mapping in mappings:
        if mapping.get("include", "").upper() != "YES":
            continue
        key = mapping.get("citekey", "").strip()
        verification = (prior_by_key.get(key) if mapping.get("verification_basis", "").startswith("carry forward")
                        else current_by_key.get(key))
        if verification and verification.get("status") == "VERIFIED" and verification.get("technical_claim_eligible") == "YES" and verification.get("bib_ready") == "YES":
            resolved = verification.get("resolved_citekey", "").strip() or key
            selected[key] = {**mapping, "resolved_citekey": resolved, "status": "VERIFIED"}

    sec10 = args.sections_dir / "sec10_energy.tex"
    text10 = sec10.read_text(encoding="utf-8")
    text10 = re.sub(r"(?ms)^\\paragraph\{R3c source-specific energy-partition evidence\.\}.*?(?=^This identity is conditional on the theory-specific flux)", "", text10)
    sentences = ["Primary-source evidence for the exact lossless reduction is limited; GAP-09 remains open."]
    if "Kumar2017" in selected:
        k = selected["Kumar2017"]["resolved_citekey"]
        sentences.append(f"Kumar and Kansal report a model-specific interface energy-ratio balance with an explicit interaction term in Eq. (80); it supports retaining cross terms above, not a universal identity (CONDITIONAL) \\cite{{{k}}}.")
    if "Kumar2024" in selected:
        k = selected["Kumar2024"]["resolved_citekey"]
        sentences.append(f"The eligible own-group source defines ratios from average energy flux per incident-wave type, specifying normalization rather than closure (PRIMARY-SOURCE-CHECKED) \\cite{{{k}}}. Its definitions are not treated as a closure proof; any numerical near-unity result is described only as approximate for its stated model.")
    if "Kumar2024a" in selected:
        k = selected["Kumar2024a"]["resolved_citekey"]
        sentences.append(f"A related study describes its eight-model sum as close to unity for specified imperfect-interface cases; this is approximate, model-specific evidence, not an identity (CONDITIONAL) \\cite{{{k}}}.")
    if "De2020" in selected:
        k = selected["De2020"]["resolved_citekey"]
        sentences.append(f"A separate reflection model prints an inequality when surface-wave, interaction, and thermal channels are omitted; that conclusion is model-specific and conditional (CONDITIONAL) \\cite{{{k}}}.")
    block10 = "\\paragraph{R3c source-specific energy-partition evidence.} " + " ".join(sentences) + "\n\n"
    anchor10 = "This identity is conditional on the theory-specific flux"
    if text10.count(anchor10) != 1:
        raise RuntimeError(f"Expected one Section 10 insertion anchor; found {text10.count(anchor10)}")
    text10 = text10.replace(anchor10, block10 + anchor10, 1)
    sec10_map_keys = {item["resolved_citekey"] for item in selected.values()}

    sec04 = args.sections_dir / "sec04_thermoelastic.tex"
    text04 = sec04.read_text(encoding="utf-8")
    text04 = re.sub(r"(?ms)^\\paragraph\{R3c fractional-source scope\.\}.*?(?=^\\subsection\{Comparative summary\})", "", text04)
    fractional_scope = ("\\paragraph{R3c fractional-source scope.} Primary-source coverage is limited: the sole s.4.11 plan row is metadata-only and not technically eligible. "
                       "GAP-12 and GAP-13 remain open; no model-specific admissibility claim is inferred from that record.\n\n")
    anchor04 = "\\subsection{Comparative summary}"
    if text04.count(anchor04) != 1:
        raise RuntimeError(f"Expected one Section 4 comparative-summary anchor; found {text04.count(anchor04)}")
    text04 = text04.replace(anchor04, fractional_scope + anchor04, 1)
    sec10.write_text(text10, encoding="utf-8")
    sec04.write_text(text04, encoding="utf-8")

    local_bib = args.local_bib
    added_keys = merge_bib(local_bib, args.reports_dir / "R3C_VERIFIED_REFERENCES.bib")
    local_keys = {row["key"] for row in cr.parse_bib(local_bib)}
    missing = sorted(sec10_map_keys - local_keys)
    if missing:
        raise RuntimeError("R3c citations lack BibTeX entries: " + ", ".join(missing))

    r3a_rows = read_csv(args.reports_dir / "CROSSREF_VERIFY.csv")
    s10_rows = [row for row in r3c_rows if row.get("section") == "s.10"]
    s411_rows = [row for row in r3c_rows if row.get("section") == "s.4.11"]
    s10_eligible_rows = [row for row in s10_rows if row.get("technical_claim_eligible") == "YES"]
    s411_eligible_rows = [row for row in s411_rows if row.get("technical_claim_eligible") == "YES"]
    s10_counts = Counter(row["status"] for row in s10_eligible_rows)
    map_included_verified = {key for key in selected if selected[key]["status"] == "VERIFIED"}
    r3a_section = Counter(row["section"] for row in r3a_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES")
    r3b_section = Counter(row["section"] for row in r3b_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES")
    r3c_section = Counter(row["section"] for row in r3c_rows if row.get("technical_claim_eligible") == "YES" and row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES" and row.get("citekey") in map_by_key and map_by_key[row.get("citekey", "")].get("include", "").upper() == "YES")
    section_counts = r3a_section + r3b_section + r3c_section
    over_six = [f"{sec.replace('s.', '')} ({n})" for sec, n in sorted(section_counts.items()) if n >= 6]
    exact_matches = sum(row.get("technical_claim_eligible") == "YES" and bool(row.get("citation_map_claims", "").strip()) for row in r3c_rows)
    r3c_verified_ready = sum(row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES" for row in s10_eligible_rows)
    r3c_ineligible = sum(row.get("status") == "INELIGIBLE" for row in r3c_rows)
    r3c_unresolved = [row for row in s10_eligible_rows if row.get("status") in {"MISMATCH", "NOT-FOUND", "NO-DOI"}]
    r3c_no_map = [row for row in s10_eligible_rows if row.get("status") == "VERIFIED" and row.get("citekey") not in map_included_verified]
    kumar_used = "Kumar2017" in selected
    newly_requested_citations = sum(not map_by_key[key].get("verification_basis", "").startswith("carry forward") for key in map_included_verified)

    report = args.status_report.read_text(encoding="utf-8")
    begin = report.find("## R3c verification and evidence")
    end = report.find("## Final strict build")
    if end < 0:
        raise RuntimeError("R3_STATUS.md must have the final-build heading")
    if begin < 0:
        begin = end
    elif begin >= end:
        raise RuntimeError("R3c status section must precede the final-build section")
    output = [
        "## R3c verification and evidence", "",
        f"- Scope: REFERENCE_PLAN s.10 and s.4.11; Section 10 has {len(s10_eligible_rows)} technical-eligible rows and {sum(row.get('status') == 'INELIGIBLE' for row in s10_rows)} ineligible plan rows not queried; Section 4.11 has {len(s411_rows)} plan row(s), {len(s411_eligible_rows)} eligible; {r3c_ineligible} total rows across both sections are INELIGIBLE and unqueried.",
        f"- R3c new Crossref results for s.10 eligible rows: {s10_counts['VERIFIED']} VERIFIED, {s10_counts['MISMATCH']} MISMATCH, {s10_counts['NOT-FOUND']} NOT-FOUND, {s10_counts['NO-DOI']} NO-DOI.",
        f"- Verified and bibliography-ready s.10 eligible rows: {r3c_verified_ready}; new-request citations inserted: {newly_requested_citations}; verified carry-forward s.10 citations reused from R3b: {len(map_included_verified) - newly_requested_citations}; new BibTeX keys added: {len(added_keys)}.",
        f"- Kumar2017 is carried forward from R3b only because its plan row is technically eligible, proposed_section includes s.10.5, and R3b marked it VERIFIED/bibliography-ready: {'used' if kumar_used else 'not used'}.",
        "- Barak 2023 Eq. (6.14) is not cited: its local BibTeX record has no technically eligible REFERENCE_PLAN row. No new citation is created from that record.",
        f"- Frozen CITATION_MAP exact-key matches among R3c s.10 eligible sources: {exact_matches}. Claim IDs CL-013/014/015 are used as topic anchors in `R3C_CITATION_MAP.csv`; that file states the local plan-note rationale and does not imply supplied-map key matches.",
        f"- Sections meeting ≥6 evidence-ready sources across R3a/R3b/R3c: {', '.join(over_six) if over_six else 'none'}.",
        "- Limited primary sources are available for s.10 energy partition and s.4.11 fractional thermoelasticity. Section 10 Eq. (10.12) remains conditional/model-specific; own-group numeric observations are not presented as exact identities. Section 4.11 receives no technical citation because its only plan row is metadata-only.",
        "- GAP-09, GAP-12, and GAP-13 remain open. Section 10 identity conditions, Section 4.11 fractional-source/admissibility questions, and all R3b unresolved rows are not closed by metadata verification alone.",
        "- R3c title human-check list: `CROSSREF_R3C_HUMAN_CHECK.md`.",
        "- R3c unresolved eligible rows (not cited):",
    ]
    if r3c_unresolved:
        output.extend(f"  - {r['lit_id']} `{r['citekey']}` — {r['status']}: {r.get('reason','')}" for r in r3c_unresolved)
    else:
        output.append(f"  - None among the {len(s10_eligible_rows)} eligible s.10 DOI rows.")
    if r3c_no_map:
        output.append("- R3c technically eligible but not cited because no claim mapping was authorized by the local map:")
        output.extend(f"  - {r['lit_id']} `{r['citekey']}` — Crossref {r['status']}; {r.get('reason','')}" for r in r3c_no_map)
    output += ["", ""]
    report = report[:begin] + "\n".join(output) + report[end:]
    final_start = report.find("## Final strict build")
    final_block = report[final_start:]
    for label, marker in (("Content/source commit", "__R3_SOURCE_COMMIT__"),
                          ("Strict CI run ID", "__R3_CI_RUN_ID__"),
                          ("Strict build-step time", "__R3_BUILD_SECONDS__"),
                          ("PDF pages", "__R3_PDF_PAGES__"),
                          ("Undefined references/citations", "__R3_UNRESOLVED_REFS__")):
        final_block, count = re.subn(rf"(?m)^- {re.escape(label)}:.*$", f"- {label}: `{marker}`", final_block, count=1)
        if count != 1:
            raise RuntimeError(f"R3_STATUS.md final-build field missing: {label}")
    report = report[:final_start] + final_block
    args.status_report.write_text(report, encoding="utf-8")
    print(f"R3c applied {len(sec10_map_keys)} verified citations to Section 10; new BibTeX keys={len(added_keys)}; exact frozen-map matches={exact_matches}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
