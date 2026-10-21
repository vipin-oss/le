#!/usr/bin/env python3
"""
PDF Ingestion Pipeline for Multiphysics Continuum Review

Prepares technical infrastructure for the forthcoming corpus of 100+ original
full-text scholarly papers. Designed to run BEFORE PDFs arrive, ready to
process them when placed in the incoming directory.

Design principles:
- Preserve original documents (never overwrite, never delete)
- Never commit copyrighted full-text PDFs to public repository
- Generate SHA-256 hashes for deduplication
- Extract text where available (not OCR - OCR is manual review path)
- Identify scanned PDFs requiring special handling
- Generate searchable study-level index
- Map studies to manuscript sections
- Log extraction failures and uncertain mathematical content

Usage:
    python pdf_ingestion_pipeline.py --scan          # Scan incoming directory
    python pdf_ingestion_pipeline.py --index         # Generate study index
    python pdf_ingestion_pipeline.py --dedup         # Detect duplicates
    python pdf_ingestion_pipeline.py --report        # Generate ingestion report
"""

import csv
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CONFIG = {
    "incoming_dir": "phase4/literature/incoming",
    "verified_dir": "phase4/literature/verified",
    "metadata_dir": "phase4/literature/metadata",
    "extraction_dir": "phase4/literature/extraction",
    "duplicates_dir": "phase4/literature/duplicates",
    "reports_dir": "phase4/literature/reports",
    "index_file": "phase4/literature/metadata/study_index.json",
    "hash_file": "phase4/literature/metadata/file_hashes.csv",
    "log_file": "phase4/literature/reports/ingestion_log.csv",
    "max_extract_pages": 50,  # Don't extract entire PDF by default
    "math_heuristic_patterns": [
        r"\\begin\{equation\}",
        r"\\frac\{",
        r"\\nabla",
        r"\\partial",
        r"\\sigma_",
        r"\\varepsilon_",
        r"\\rho\s",
    ],
}


# ---------------------------------------------------------------------------
# Directory setup
# ---------------------------------------------------------------------------

def ensure_dirs():
    """Create all required directories if they don't exist."""
    for key in ["incoming_dir", "verified_dir", "metadata_dir",
                "extraction_dir", "duplicates_dir", "reports_dir"]:
        Path(CONFIG[key]).mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# SHA-256 hashing
# ---------------------------------------------------------------------------

def compute_sha256(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# PDF text extraction
# ---------------------------------------------------------------------------

def extract_pdf_text(filepath: Path, max_pages: int = 50) -> dict:
    """
    Extract text from a PDF. Returns dict with:
      - text: extracted text (first max_pages pages)
      - page_count: total pages
      - extracted_pages: number of pages extracted
      - is_scanned: bool, True if little/no text extracted
      - extraction_method: 'pypdf2' | 'pdfplumber' | 'none'
      - errors: list of error messages
    """
    result = {
        "text": "",
        "page_count": 0,
        "extracted_pages": 0,
        "is_scanned": False,
        "extraction_method": "none",
        "errors": [],
    }

    if not HAS_PYPDF2 and not HAS_PDFPLUMBER:
        result["errors"].append("No PDF extraction library available (PyPDF2 or pdfplumber)")
        return result

    try:
        if HAS_PDFPLUMBER:
            import pdfplumber
            with pdfplumber.open(filepath) as pdf:
                result["page_count"] = len(pdf.pages)
                texts = []
                for i, page in enumerate(pdf.pages[:max_pages]):
                    try:
                        t = page.extract_text() or ""
                        texts.append(t)
                    except Exception as e:
                        result["errors"].append(f"Page {i+1}: {e}")
                result["text"] = "\n".join(texts)
                result["extracted_pages"] = min(max_pages, result["page_count"])
                result["extraction_method"] = "pdfplumber"
        elif HAS_PYPDF2:
            import PyPDF2
            with open(filepath, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                result["page_count"] = len(reader.pages)
                texts = []
                for i in range(min(max_pages, len(reader.pages))):
                    try:
                        t = reader.pages[i].extract_text() or ""
                        texts.append(t)
                    except Exception as e:
                        result["errors"].append(f"Page {i+1}: {e}")
                result["text"] = "\n".join(texts)
                result["extracted_pages"] = min(max_pages, result["page_count"])
                result["extraction_method"] = "pypdf2"
    except Exception as e:
        result["errors"].append(str(e))

    # Heuristic: scanned if very little text extracted
    if len(result["text"].strip()) < 100:
        result["is_scanned"] = True

    return result


# ---------------------------------------------------------------------------
# Metadata extraction from text
# ---------------------------------------------------------------------------

def extract_doi_from_text(text: str) -> Optional[str]:
    """Try to find a DOI in extracted text."""
    patterns = [
        r"10\.\d{4,}/[-._;()/:A-Za-z0-9]+",
        r"doi:\s*10\.\d{4,}/[-._;()/:A-Za-z0-9]+",
        r"https?://doi\.org/10\.\d{4,}/[-._;()/:A-Za-z0-9]+",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            doi = m.group(0)
            # Clean up URL prefixes
            doi = re.sub(r"https?://doi\.org/", "", doi)
            doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
            return doi.strip()
    return None


def extract_title_from_text(text: str) -> Optional[str]:
    """Try to extract title from first page text (heuristic)."""
    lines = text.strip().split("\n")[:20]
    for line in lines:
        line = line.strip()
        if len(line) > 30 and len(line) < 200:
            # Skip common non-title lines
            skip = ["abstract", "introduction", "keywords", "acknowledgment",
                    "references", "university", "journal", "vol.", "no.",
                    "copyright", "published"]
            if not any(s in line.lower() for s in skip):
                return line
    return None


def detect_math_content(text: str) -> dict:
    """Detect mathematical content in extracted text."""
    result = {
        "has_equations": False,
        "equation_count": 0,
        "math_patterns_found": [],
    }
    for pat in CONFIG["math_heuristic_patterns"]:
        matches = re.findall(pat, text)
        if matches:
            result["has_equations"] = True
            result["equation_count"] += len(matches)
            result["math_patterns_found"].append(pat)
    return result


# ---------------------------------------------------------------------------
# Study record
# ---------------------------------------------------------------------------

def create_study_record(filepath: Path, file_hash: str,
                        extraction: dict) -> dict:
    """Create a study record dictionary."""
    text = extraction["text"]
    doi = extract_doi_from_text(text)
    title = extract_title_from_text(text)
    math = detect_math_content(text)

    # Section mapping heuristic (based on keywords)
    section_hint = map_to_section(text)

    return {
        "filename": filepath.name,
        "filepath": str(filepath),
        "sha256": file_hash,
        "date_added": datetime.now().isoformat(),
        "page_count": extraction["page_count"],
        "extracted_pages": extraction["extracted_pages"],
        "extraction_method": extraction["extraction_method"],
        "is_scanned": extraction["is_scanned"],
        "doi": doi or "not_found",
        "title": title or "not_extracted",
        "has_equations": math["has_equations"],
        "equation_count": math["equation_count"],
        "extraction_errors": extraction["errors"],
        "section_hint": section_hint,
        "verification_status": "pending",
        "notes": "",
    }


def map_to_section(text: str) -> str:
    """Heuristic mapping of extracted text to manuscript section."""
    text_lower = text.lower()
    section_keywords = {
        "sec03_foundations": ["continuum mechanics", "balance law", "cauchy",
                              "strain", "stress", "navier"],
        "sec04_thermoelastic": ["lord-shulman", "green-lindsay",
                                 "green-naghdi", "phase-lag", "thermoelastic"],
        "sec05_multiphysics": ["piezoelectric", "porous", "micropolar",
                                "semiconductor", "magneto"],
        "sec06_transport": ["memory-dependent", "fractional", "hereditary",
                            "relaxation", "kernel"],
        "sec07_nonlocal": ["nonlocal", "strain-gradient", "scale-dependent",
                           "eringen"],
        "sec09_interfaces": ["reflection", "transmission", "interface",
                             "scattering", "interface conditions"],
        "sec10_energy": ["energy flux", "dissipation", "energy balance",
                         "conservation"],
    }
    scores = {}
    for section, keywords in section_keywords.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[section] = score
    if scores:
        return max(scores, key=scores.get)
    return "unclassified"


# ---------------------------------------------------------------------------
# Pipeline operations
# ---------------------------------------------------------------------------

def scan_incoming():
    """Scan incoming directory for PDFs and create records."""
    ensure_dirs()
    incoming = Path(CONFIG["incoming_dir"])
    if not incoming.exists():
        print(f"Incoming directory {incoming} does not exist.")
        return []

    records = []
    hash_file = Path(CONFIG["hash_file"])
    existing_hashes = set()
    if hash_file.exists():
        with open(hash_file, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_hashes.add(row["sha256"])

    for pdf_path in sorted(incoming.glob("*.pdf")):
        file_hash = compute_sha256(pdf_path)

        # Duplicate check by hash
        if file_hash in existing_hashes:
            print(f"DUPLICATE (by hash): {pdf_path.name}")
            # Move to duplicates directory
            dest = Path(CONFIG["duplicates_dir"]) / pdf_path.name
            if not dest.exists():
                pdf_path.rename(dest)
            continue

        extraction = extract_pdf_text(pdf_path)
        record = create_study_record(pdf_path, file_hash, extraction)
        records.append(record)

        # Save extracted text
        extraction_path = Path(CONFIG["extraction_dir"]) / f"{pdf_path.stem}.txt"
        with open(extraction_path, "w") as f:
            f.write(extraction["text"])

        print(f"Processed: {pdf_path.name} "
              f"(pages={extraction['page_count']}, "
              f"scanned={extraction['is_scanned']}, "
              f"DOI={record['doi']})")

    return records


def save_index(records):
    """Save study index to JSON and CSV."""
    ensure_dirs()
    index_path = Path(CONFIG["index_file"])

    # Load existing index if present
    existing = []
    if index_path.exists():
        with open(index_path) as f:
            existing = json.load(f)

    all_records = existing + records
    with open(index_path, "w") as f:
        json.dump(all_records, f, indent=2)

    # Also save as CSV for spreadsheet viewing
    csv_path = Path(CONFIG["metadata_dir"]) / "study_index.csv"
    if all_records:
        fieldnames = all_records[0].keys()
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_records)

    # Save hashes
    hash_path = Path(CONFIG["hash_file"])
    with open(hash_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sha256", "filename", "date_added"])
        for r in all_records:
            writer.writerow([r["sha256"], r["filename"], r["date_added"]])

    print(f"Index saved: {len(all_records)} total records")


def generate_report():
    """Generate ingestion report."""
    ensure_dirs()
    index_path = Path(CONFIG["index_file"])
    if not index_path.exists():
        print("No study index found. Run --scan first.")
        return

    with open(index_path) as f:
        records = json.load(f)

    total = len(records)
    scanned = sum(1 for r in records if r["is_scanned"])
    has_doi = sum(1 for r in records if r["doi"] != "not_found")
    has_equations = sum(1 for r in records if r["has_equations"])
    unclassified = sum(1 for r in records if r["section_hint"] == "unclassified")
    errors = sum(1 for r in records if r["extraction_errors"])

    report_lines = [
        "# PDF Ingestion Report",
        f"Generated: {datetime.now().isoformat()}",
        "",
        f"Total studies: {total}",
        f"Studies with DOI: {has_doi} ({has_doi/total*100:.1f}%)",
        f"Scanned PDFs (need OCR): {scanned} ({scanned/total*100:.1f}%)",
        f"Studies with equations: {has_equations} ({has_equations/total*100:.1f}%)",
        f"Unclassified sections: {unclassified}",
        f"Extraction errors: {errors}",
        "",
        "## By section hint:",
    ]

    section_counts = {}
    for r in records:
        s = r["section_hint"]
        section_counts[s] = section_counts.get(s, 0) + 1
    for section, count in sorted(section_counts.items()):
        report_lines.append(f"  {section}: {count}")

    report_lines.extend([
        "",
        "## Files needing manual review:",
    ])
    for r in records:
        if r["is_scanned"] or r["extraction_errors"] or r["doi"] == "not_found":
            report_lines.append(
                f"  - {r['filename']}: "
                f"scanned={r['is_scanned']}, "
                f"DOI={r['doi']}, "
                f"errors={len(r['extraction_errors'])}"
            )

    report_path = Path(CONFIG["reports_dir"]) / "ingestion_report.md"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))

    print(f"Report saved: {report_path}")
    print(f"Total: {total}, Scanned: {scanned}, With DOI: {has_doi}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="PDF Ingestion Pipeline for Multiphysics Continuum Review"
    )
    parser.add_argument("--scan", action="store_true",
                        help="Scan incoming directory for PDFs")
    parser.add_argument("--index", action="store_true",
                        help="Generate study index from records")
    parser.add_argument("--dedup", action="store_true",
                        help="Detect duplicates (done during scan)")
    parser.add_argument("--report", action="store_true",
                        help="Generate ingestion report")
    parser.add_argument("--all", action="store_true",
                        help="Run scan, index, and report")

    args = parser.parse_args()

    if args.all or args.scan:
        records = scan_incoming()
        if args.all or args.index:
            save_index(records)
    elif args.index:
        save_index([])
    if args.all or args.report:
        generate_report()

    if not any([args.scan, args.index, args.dedup, args.report, args.all]):
        parser.print_help()


if __name__ == "__main__":
    main()