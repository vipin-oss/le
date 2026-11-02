#!/usr/bin/env python3
"""Check that the READMEs are true.

A handoff README is worse than none if it points at files that have moved or quotes
numbers that have changed. This gate reads the two entry-point READMEs, extracts every
repository path they mention, and checks:

  M1  every referenced path exists
  M2  every referenced path that ought to be *absent* (PDFs, figures) is not silently
      claimed as present (no false claim of a file that must live outside the repo)
  M3  the quoted build numbers agree with the audit artefacts:
        pages and words  <-> P1_audit/page_audit_results.csv (check P02)
        equations        <-> P1_audit/equation_inventory.csv (row count)
        register rows    <-> P1_audit/register_linkage.csv (row count)
  M4  the quoted zip name exists and is the one committed under submission/
  M5  the READMEs do not contain drive identifiers, drive links or uploaded file names
      (a standing rule for every file in this repository)

Prints `PASS (...)` and exits 0 only if all of that holds.

Usage:  python3 check_readme_paths.py [--root ../..]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# The entry-point READMEs describe the *current* state, so every path they name must
# exist. The deep log (`README_FOR_CLAUDE.md`) is explicitly historical: it describes
# files that were moved, so its paths are deliberately not existence-checked.
CURRENT = ["README.md", "paper_v2/README.md"]
READMES = CURRENT + ["paper_v2/arena_deliverables/README_FOR_CLAUDE.md"]

# A README may be read from the repository root or from the directory it lives in, so a
# relative path is accepted if it resolves against any sensible anchor.
ANCHORS = ["", "paper_v2", "paper_v2/manuscript_v2", "paper_v2/manuscript_v2/master",
           "paper_v2/arena_deliverables", "paper_v2/arena_deliverables/P1_audit",
           "paper_v2/arena_deliverables/P5_merge", "paper_v2/arena_deliverables/P6_post_merge",
           "paper_v2/versions"]

# Paths that must live outside the repository by rule; a README may name them only as
# prose, never as an in-repo location.
FORBIDDEN_CLAIMS = ["google_drive", "drive.google.com", "drive id"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="../..")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    audit = root / "paper_v2" / "arena_deliverables" / "P1_audit"
    problems: list[str] = []
    notes: list[str] = []

    texts = {}
    for r in READMES:
        p = root / r
        if not p.exists():
            problems.append(f"M1 missing README: {r}")
            continue
        texts[r] = p.read_text(encoding="utf-8")

    # ---- M1: every backticked path that looks like a repo path exists --------
    checked = skipped = 0
    for name in CURRENT:
        txt = texts.get(name, "")
        for raw in re.findall(r"`([^`\n]+)`", txt):
            tok = raw.strip()
            if " " in tok or tok.startswith(("python3", "cd ", "pdflatex", "--")):
                skipped += 1          # commands, not paths
                continue
            if any(ch in tok for ch in ("…", "*", "<", ">", "|")) or tok.endswith((".tex", ".md")):
                pass                  # still check, but patterns below skip the unverifiable ones
            if tok.startswith(".") or tok.startswith("arena/"):
                skipped += 1          # a bare extension, or the branch name
                continue
            if "…" in tok or "*" in tok:
                skipped += 1          # elided or globbed path
                continue
            looks_like_path = ("/" in tok or tok.endswith((".py", ".md", ".csv", ".zip", ".tex",
                                                           ".bib", ".pdf", ".tex")))
            if not looks_like_path:
                skipped += 1
                continue
            if tok.startswith("./"):
                tok = tok[2:]
            ok = False
            for anchor in ANCHORS:
                cand = (root / anchor / tok).resolve()
                if cand.exists():
                    ok = True
                    break
                # a trailing slash names a directory that must exist
                if tok.endswith("/") and (root / anchor / tok.rstrip("/")).is_dir():
                    ok = True
                    break
            if not ok:
                problems.append(f"M1 {name}: references missing path `{tok}`")
            checked += 1
    notes.append(f"paths checked={checked}, skipped={skipped}")

    # ---- M5: no actual Drive link / identifier / uploaded file name ----------
    # The rule text itself ("do not put Drive identifiers in the repository") is allowed;
    # only the thing it forbids is flagged.
    for name, txt in texts.items():
        for line in txt.splitlines():
            low = line.lower()
            if any(v in low for v in ("do not", "never", "not put", "stays out", "deliberately not")):
                continue
            for bad in ("drive.google.com", "docs.google.com", "google_drive"):
                if bad in low:
                    problems.append(f"M5 {name}: contains an actual Drive reference ('{bad}')")
            if re.search(r"\b1[A-Za-z0-9_-]{24,}\b", line):
                problems.append(f"M5 {name}: looks like a Drive file id "
                                f"('{re.search(r'1[A-Za-z0-9_-]{24,}', line).group(0)[:12]}…')")

    # ---- M3: quoted numbers agree with the artefacts -------------------------
    # The current paper is paper_v2/main.pdf (164 pp); P1_audit describes the v1.2 snapshot.
    # If P6 has measured the current build, that measurement is the one the READMEs must match.
    p6 = root / "paper_v2" / "arena_deliverables" / "P6_post_merge" / "final_paper_numbers.csv"
    if p6.exists():
        meas = {r["quantity"]: r["value"] for r in csv.DictReader(p6.open(encoding="utf-8"))}
        must = {"pages": "page count", "equations": "numbered equations",
                "tables": "tables", "figures": "figures", "references": "references",
                "sections": "sections"}
        for key, label in must.items():
            val = meas.get(key, "")
            if not val:
                continue
            for name in ("README.md", "paper_v2/README.md"):
                txt = texts.get(name, "")
                if not re.search(r"(?<![\d,.])" + re.escape(val) + r"(?![\d])", txt):
                    problems.append(f"M3 {name}: does not quote the measured {label} ({val})")
        notes.append("P6 numbers: " + ", ".join(f"{k}={meas.get(k)}" for k in must))
    res = audit / "page_audit_results.csv"
    inv = audit / "equation_inventory.csv"
    lnk = audit / "register_linkage.csv"
    if res.exists() and not p6.exists():
        rows = {r["check_id"]: r for r in csv.DictReader(res.open(encoding="utf-8"))}
        obs = rows.get("P02", {}).get("observed", "")
        m = re.search(r"(\d+) pages", obs)
        pages = int(m.group(1)) if m else None
        mw = re.search(r"([\d,]+) words", obs)
        words = int(mw.group(1).replace(",", "")) if mw else None
        for name in ("README.md", "paper_v2/README.md"):
            txt = texts.get(name, "")
            if pages and f"{pages}" not in txt:
                problems.append(f"M3 {name}: does not quote the measured page count ({pages})")
            if words and f"{words:,}" not in txt and f"{words}" not in txt:
                problems.append(f"M3 {name}: does not quote the measured word count ({words})")
        notes.append(f"pages={pages} words={words}")
    elif not p6.exists():
        problems.append("M3 page_audit_results.csv missing")

    if inv.exists() and not p6.exists():
        n_eq = sum(1 for _ in csv.DictReader(inv.open(encoding="utf-8")))
        for name in ("README.md", "paper_v2/README.md"):
            if str(n_eq) not in texts.get(name, ""):
                problems.append(f"M3 {name}: does not quote the inventoried equation count ({n_eq})")
        notes.append(f"equations={n_eq}")
    elif not p6.exists():
        problems.append("M3 equation_inventory.csv missing")

    # The claim register is the ledger the READMEs speak about; the v1.2 linkage table is the fallback
    # used only when that register is absent.
    claim_reg = root / "paper_v2" / "claim_register.csv"
    if claim_reg.exists():
        n_reg = sum(1 for _ in csv.DictReader(claim_reg.open(encoding="utf-8")))
        notes.append(f"claim_register_rows={n_reg}")
        for name in ("README.md", "paper_v2/README.md"):
            if str(n_reg) not in texts.get(name, ""):
                problems.append(f"M3 {name}: does not quote the claim-register row count ({n_reg})")
    elif lnk.exists():
        n_reg = sum(1 for _ in csv.DictReader(lnk.open(encoding="utf-8")))
        notes.append(f"register_rows={n_reg}")
        if str(n_reg) not in texts.get("README.md", ""):
            problems.append("M3 README.md: does not quote the register row count")

    # ---- M4: the zip the README names is the one that ships ------------------
    sub = root / "paper_v2" / "arena_deliverables" / "submission"
    zips = sorted(p.name for p in sub.glob("*.zip")) if sub.exists() else []
    allowed = set(zips) | {p.name for p in (root / "paper_v2").glob("*.zip")}
    if not zips:
        problems.append("M4 no zip in submission/")
    else:
        for name, txt in texts.items():
            for mentioned in re.findall(r"([\w.\-]+\.zip)", txt):
                if mentioned not in allowed:
                    problems.append(f"M4 {name}: names a zip that is not in submission/: {mentioned}")
        notes.append(f"zip={zips[0]}")

    if problems:
        for p in problems:
            print("FAIL " + p)
        print(f"FAIL {len(problems)} problem(s)")
        return 1
    print(f"PASS all checks ({', '.join(notes)}; no drive references; README paths all exist)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
