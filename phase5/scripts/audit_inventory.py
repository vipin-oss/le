#!/usr/bin/env python3
"""Static source/path inventory for phase5; not a TeX compiler or science validator."""
from collections import Counter, defaultdict
import csv
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "master"
# The master folder is self-contained; phase-level table mirrors are excluded.
TEX = sorted(MASTER.rglob("*.tex"))
labels = defaultdict(list)
refs: list[tuple[Path, str]] = []
cites: list[str] = []
figs: set[str] = set()
inputs: list[tuple[Path, str]] = []
bibliographies: set[str] = set()

for path in TEX:
    text = path.read_text(encoding="utf-8")
    for label in re.findall(r"\\label\{([^}]+)\}", text):
        labels[label].append(path.relative_to(ROOT).as_posix())
    refs.extend((path, label) for label in re.findall(r"\\(?:eqref|ref|cref|Cref|autoref)\{([^}]+)\}", text))
    for group in re.findall(r"\\cite\w*\{([^}]+)\}", text):
        cites.extend(key.strip() for key in group.split(",") if key.strip())
    figs.update(re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", text))
    inputs.extend((path, name.strip()) for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", text))
    for group in re.findall(r"\\bibliography\{([^}]+)\}", text):
        bibliographies.update(name.strip() for name in group.split(",") if name.strip())

bib_texts = {path.stem: path.read_text(encoding="utf-8") for path in MASTER.glob("*.bib")}
bib_text = "\n".join(bib_texts.values())
bib_matches = re.findall(r"@\w+\s*\{\s*([^,]+),", bib_text)
bib_keys = set(bib_matches)
bib_duplicates = {key: n for key, n in Counter(bib_matches).items() if n > 1}
missing_refs = Counter(label for _, label in refs if label not in labels)
missing_cites = sorted(set(cites) - bib_keys)
duplicates = {key: paths for key, paths in labels.items() if len(paths) > 1}
missing_figures = sorted(name for name in figs if not (MASTER / "figures/source" / name).is_file())
missing_inputs: list[tuple[str, str]] = []
for including_file, name in inputs:
    target = name if Path(name).suffix else f"{name}.tex"
    if not (MASTER / target).is_file():
        missing_inputs.append((including_file.relative_to(ROOT).as_posix(), name))
missing_bibs = sorted(name for name in bibliographies if name not in bib_texts)

print(f"TeX source files scanned: {len(TEX)}")
print(f"Labels: {len(labels)}; references: {len(refs)}; bibliography keys: {len(bib_keys)}; citations: {len(cites)}")
print(f"Duplicate labels: {len(duplicates)}")
for label, paths in sorted(duplicates.items()):
    print(f"  DUPLICATE {label}: {', '.join(paths)}")
print(f"Missing reference labels: {len(missing_refs)}")
for label, count in sorted(missing_refs.items()):
    print(f"  MISSING {label}: {count} reference(s)")
print(f"Duplicate bibliography keys: {len(bib_duplicates)}")
for key, count in sorted(bib_duplicates.items()):
    print(f"  DUPLICATE BIBKEY {key}: {count}")
print(f"Missing citation keys: {len(missing_cites)}")
for key in missing_cites:
    print(f"  MISSING CITE {key}")
print(f"Missing input/include files: {len(missing_inputs)}")
for source, name in missing_inputs:
    print(f"  MISSING INPUT {name} (from {source})")
print(f"Missing bibliography files: {len(missing_bibs)}")
for name in missing_bibs:
    print(f"  MISSING BIB {name}.bib")
print(f"Unresolved figure assets (PDF renderings expected): {len(missing_figures)}")
for name in missing_figures:
    print(f"  MISSING FIGURE {name}")

inventory = ROOT.parent / "phase4/literature/expanded_literature_database.csv"
if inventory.exists():
    with inventory.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    print(f"Inherited literature inventory: {len(rows)} records")
    for field in ("doi", "open_access", "full_text_available"):
        counts = Counter((row.get(field) or "").strip() for row in rows)
        print(f"  {field}: {dict(counts)}")
print("NOTE: This static check does not compile TeX, inspect the manuscript PDF, verify references externally, or validate scientific claims.")

if duplicates or missing_refs or bib_duplicates or missing_cites or missing_inputs or missing_bibs or missing_figures:
    sys.exit(1)
