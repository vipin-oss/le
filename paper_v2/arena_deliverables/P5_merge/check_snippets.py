#!/usr/bin/env python3
"""Validate every paste-ready snippet against the final paper's own labels and bibliography.

Checks, per snippet:
  1. brace balance and no leftover template markers;
  2. every \\cref/\\eqref/\\ref target is either a label of the final paper (final_labels.csv,
     harvested from the final sources) or a label the snippet declares as NEW in its header;
  3. every \\citep/\\citet key exists in the final paper's bibliography (final_bib_keys.txt);
  4. no duplicate \\label inside the snippet set, and no NEW label that already exists in the
     final paper (that would silently overwrite an equation number);
  5. every snippet states its source and its suggested placement in the header comment.

Prints PASS and exits 0 when all checks hold; prints FAIL and exits 1 otherwise.
"""
import csv, glob, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SNIP = os.path.join(ROOT, "snippets")

final_labels = {r["label"] for r in csv.DictReader(open(os.path.join(ROOT, "final_labels.csv"), encoding="utf-8"))}
bib = {l.strip() for l in open(os.path.join(ROOT, "final_bib_keys.txt"), encoding="utf-8") if l.strip()}

REF = re.compile(r"\\(?:c|C)ref\{([^}]+)\}|\\(?:eq|auto|page|name)?ref\{([^}]+)\}")
CITE = re.compile(r"\\cite[a-zA-Z]*\{([^}]+)\}")
NEWLAB = re.compile(r"^\s*%\s*NEW LABELS?[^:]*:\s*(.+)$", re.M)
LAB = re.compile(r"\\label\{([^}]+)\}")

errors, all_new, all_lab, texts = [], {}, {}, {}
files = sorted(glob.glob(os.path.join(SNIP, "*.tex")))

# pass 1: collect labels declared NEW anywhere in the snippet set, so that snippets may cite
# each other's labels (the paste order is fixed by the plan, not by the file names).
declared_global = set()
for path in files:
    txt = open(path, encoding="utf-8").read()
    for m in NEWLAB.finditer(txt):
        for part in re.split(r"[;,]", m.group(1)):
            part = part.strip().rstrip(".")
            if part:
                declared_global.add(part)
for path in files:
    name = os.path.basename(path)
    txt = open(path, encoding="utf-8").read()
    # 1
    if txt.count("{") != txt.count("}"):
        errors.append(f"{name}: unbalanced braces {txt.count('{')}/{txt.count('}')}")
    for bad in ("<<<<<<<", "TODO", "XXX", "???", "\\todo"):
        if bad in txt:
            errors.append(f"{name}: leftover marker {bad!r}")
    # 5
    if "Source:" not in txt or "Suggested placement" not in txt:
        errors.append(f"{name}: header missing Source/placement")
    # declared new labels
    declared = set()
    for m in NEWLAB.finditer(txt):
        for part in re.split(r"[;,]", m.group(1)):
            part = part.strip().rstrip(".")
            if part:
                declared.add(part)
    for d in declared:
        if d in all_new:
            errors.append(f"{name}: label {d} also declared NEW in {all_new[d]}")
        all_new[d] = name
        if d in final_labels:
            errors.append(f"{name}: NEW label {d} already exists in the final paper")
    # 2
    for m in REF.finditer(txt):
        targets = [t.strip() for t in (m.group(1) or m.group(2)).split(",")]
        for t in targets:
            if t and t not in final_labels and t not in declared_global:
                errors.append(f"{name}: unresolved ref {{{t}}}")
    # 3
    for m in CITE.finditer(txt):
        for k in (x.strip() for x in m.group(1).split(",")):
            if k and k != "*" and k not in bib:
                errors.append(f"{name}: citation key not in final bibliography: {k}")
    # 4
    for lb in LAB.findall(txt):
        if lb in all_lab:
            errors.append(f"{name}: duplicate \\label {lb} (also {all_lab[lb]})")
        all_lab[lb] = name
        if lb not in declared_global:
            errors.append(f"{name}: \\label {lb} not declared in the NEW LABELS header")

print(f"snippets checked : {len(files)}")
print(f"new labels       : {len(all_new)}")
print(f"final labels     : {len(final_labels)}")
print(f"bib keys         : {len(bib)}")
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in errors:
        print("  -", e)
    print("\nFAIL")
    sys.exit(1)
print("\nPASS")
