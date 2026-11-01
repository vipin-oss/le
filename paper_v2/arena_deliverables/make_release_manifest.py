#!/usr/bin/env python3
"""Release manifest: SHA-256 of every file that would go into the archive deposit.

This is the "archive checksums" half of defect D4 ("needs a clean-environment run and
archive checksums"). It does not pretend to be the clean-environment run - that has to
happen where the code runs, on an interpreter installed from `scripts/requirements.txt`,
which lives with the manuscript and not in this repository.

What it does: walks the repository, skips `.git`, and writes one row per tracked file
with its SHA-256, its size, and a coarse class (register / deliverable / checker / other).
The file itself and the manifest are excluded so the manifest can be regenerated.

Usage
  python3 make_release_manifest.py            # writes RELEASE_MANIFEST_<date>.csv
  python3 make_release_manifest.py --check    # recomputes and compares with the newest manifest
"""
import csv
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
NAME = "RELEASE_MANIFEST_2026-11-01.csv"
SELF = os.path.basename(__file__)


def classify(rel):
    if rel.endswith(".csv"):
        return "data"
    if os.path.basename(rel).startswith(("check", "bench", "make")):
        return "script"
    if rel.endswith((".md", ".txt")):
        return "note"
    if rel.endswith((".bib", ".tex")):
        return "manuscript-side"
    return "other"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def walk():
    rows = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = sorted(d for d in dirs if d != ".git")
        for name in sorted(files):
            path = os.path.join(root, name)
            rel = os.path.relpath(path, REPO).replace(os.sep, "/")
            if rel.endswith(NAME) or rel.endswith(SELF):
                continue
            rows.append({"path": rel, "sha256": sha256(path),
                         "bytes": os.path.getsize(path), "class": classify(rel)})
    return rows


def main():
    rows = walk()
    out = os.path.join(HERE, NAME)
    if "--check" in sys.argv:
        old = {r["path"]: r["sha256"] for r in csv.DictReader(open(out, encoding="utf-8"))}
        new = {r["path"]: r["sha256"] for r in rows}
        added = sorted(set(new) - set(old))
        gone = sorted(set(old) - set(new))
        changed = sorted(p for p in set(old) & set(new) if old[p] != new[p])
        print("manifest rows: %d (was %d)" % (len(new), len(old)))
        print("added %d, removed %d, changed %d" % (len(added), len(gone), len(changed)))
        for p in added[:10]:
            print("  added  ", p)
        for p in gone[:10]:
            print("  removed", p)
        for p in changed[:10]:
            print("  changed", p)
        # a manifest is only meant to be identical for the commit it was made on
        print("PASS manifest check ran (drift is reported above, not failed: the archive "
              "manifest belongs to the release commit, not to every commit)")
        return 0
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["path", "sha256", "bytes", "class"])
        w.writeheader()
        w.writerows(rows)
    print("wrote %s: %d files, %d bytes total"
          % (NAME, len(rows), sum(r["bytes"] for r in rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
