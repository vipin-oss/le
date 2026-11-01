#!/usr/bin/env python3
"""Create explicitly labelled source-only phase5 handoff archives.

This script does not pretend the preserved v1.0 PDF is a v1.1 manuscript build.
It refuses to make a master source+PDF release archive unless a built PDF exists;
final visual/quality approval remains a separate human audit gate.
"""
from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import hashlib

ROOT = Path(__file__).resolve().parents[2]
PHASE5 = ROOT / "phase5"


def eligible(path: Path, *, include_baseline: bool, include_thumbnails: bool) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if "/node_modules/" in f"/{rel}/" or "/master/build/" in f"/{rel}/":
        return False
    if rel.startswith("phase5/exports/") and rel.endswith(".zip"):
        return False
    if not include_baseline and rel in {
        "phase5/master/v1.0-baseline.pdf",
        "phase5/master/v1.0-build-diagnostics.txt",
    }:
        return False
    if not include_thumbnails and rel.startswith("phase5/reports/v1.0-thumbnails/"):
        return False
    return path.is_file()


def write_archive(destination: Path, paths: list[Path]) -> str:
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(paths):
            zf.write(path, path.relative_to(ROOT).as_posix())
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    return digest


all_files = [p for p in PHASE5.rglob("*") if eligible(p, include_baseline=True, include_thumbnails=True)]
source_files = [p for p in PHASE5.rglob("*") if eligible(p, include_baseline=False, include_thumbnails=False)]

# Complete audit snapshot includes the preserved baseline for provenance, not as v1.1 output.
audit_zip = ROOT / "phase5-v1.1-source-audit.zip"
print(f"{audit_zip.name}: {len(all_files)} files; SHA-256 {write_archive(audit_zip, all_files)}")

# Master source archive: portable master and its assets, but deliberately no manuscript PDF.
master_prefixes = (
    "phase5/master/",
    "phase5/tables/source/",
    "phase5/figures/source/",
    "phase5/scripts/",
    "phase5/tools/",
    "phase5/reports/",
)
master_files = [p for p in source_files if p.relative_to(ROOT).as_posix().startswith(master_prefixes)]
master_files += [PHASE5 / "README.md", PHASE5 / "README_build.md", PHASE5 / "CHANGELOG.md", PHASE5 / "exports/README.md"]
master_files = [p for p in set(master_files) if p.is_file() and p.name not in {"v1.0-baseline.pdf", "v1.0-build-diagnostics.txt"}]
master_zip = ROOT / "phase5-v1.1-master-source-only.zip"
print(f"{master_zip.name}: {len(master_files)} files; SHA-256 {write_archive(master_zip, master_files)}")

# The generic journal and supplement wrappers share all non-baseline source/audit files.
journal_zip = ROOT / "phase5-v1.1-journal-source-supplement-only.zip"
print(f"{journal_zip.name}: {len(source_files)} files; SHA-256 {write_archive(journal_zip, source_files)}")

# Deliberately no complete master+PDF archive: no v1.1 manuscript PDF exists.
built_pdf = PHASE5 / "master" / "build" / "main.pdf"
if built_pdf.exists():
    print("A build PDF exists; inspect it and update this script to package only after all gates pass.")
else:
    print("NOT CREATED: complete master source+PDF ZIP; phase5/master/build/main.pdf is absent.")
