#!/usr/bin/env python3
"""Step 1 of the P5 merge: map every section of the final paper to manuscript_v2.

Inputs (read-only, nothing is modified):
  --final   directory holding the extracted final paper (main.tex + sections/)
  --mine    manuscript_v2/master

Output: section_map.csv
  final_file, final_section_title, final_label   — from the final paper (labels live on the
                                                   \\input lines in its main.tex)
  v2_file, v2_section_title                      — the matching manuscript_v2 section, or
                                                   "no equivalent"
  overlap                                        — high / partial / none (topic judgement,
                                                   stated per row in the MAP table below)
  shared_cite_keys, cite_jaccard                 — the *measured* evidence for that judgement:
                                                   how many bibliography keys the two sections
                                                   actually share, and their Jaccard overlap
  final_words, v2_words                          — size on each side

The overlap column is a judgement, so the measurement that supports it is printed beside it:
a "high" row with 0 shared keys would be a mistake, and the CSV shows that immediately.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

# final file -> (manuscript_v2 file or None, overlap)
# None means the final paper has material with no counterpart in the review manuscript.
MAP: dict[str, tuple[str | None, str]] = {
    "s01_intro":               ("sec01_scope", "partial"),
    "s02_history":             ("sec02_literature", "high"),
    "s03_foundations":         ("sec03_foundations", "high"),
    "s03c_prelim":             ("sec08_mathematical_methods", "partial"),
    "s03d_admiss":             ("sec04_thermoelastic", "partial"),
    "s03b_kinetic":            (None, "none"),
    "s04_classical":           ("sec04_thermoelastic", "high"),
    "s05_hyperbolic":          ("sec04_thermoelastic", "high"),
    "s06_lags":                ("sec04_thermoelastic", "high"),
    "s06b_delay":              (None, "none"),
    "s07_memory":              ("sec06_transport", "high"),
    "s07b_fraccoupled":        ("sec06_transport", "partial"),
    "s07c_modulus":            (None, "none"),
    "s08_waves3d":             ("sec08_mathematical_methods", "partial"),
    "s08b_aniso":              ("sec12_comparative", "partial"),
    "s08c_reflection":         ("sec09_interfaces", "partial"),
    "s09_transient":           (None, "none"),
    "s09b_thermalmodes":       (None, "none"),
    "s10_surface":             ("sec09_interfaces", "partial"),
    "s10b_lamb":               (None, "none"),
    "s10c_bar":                (None, "none"),
    "s04b_flexted":            (None, "none"),
    "s11_interfaces":          ("sec09_interfaces", "high"),
    "s11b_layered":            (None, "none"),
    "s12_size":                ("sec07_nonlocal", "high"),
    "s13_multiphysics":        ("sec05_multiphysics", "high"),
    "s13b_bg":                 (None, "none"),
    "s14_methods":             ("sec08_mathematical_methods", "high"),
    "s14b_schemes":            ("sec08_mathematical_methods", "partial"),
    "s15_applications":        ("sec13_applications", "high"),
    "s15d_scenarios":          ("sec13_applications", "partial"),
    "s15b_examples":           (None, "none"),
    "s15c_experiments":        ("sec13_applications", "partial"),
    "s16_synthesis":           ("sec12_comparative", "high"),
    "s16b_atlas":              (None, "none"),
    "s17b_reporting":          (None, "none"),
    "s17_open":                ("sec15_challenges", "high"),
    "appA":                    (None, "none"),
    "appB":                    ("sec12_comparative", "partial"),
    "appC":                    ("appF_reproducibility", "high"),
    "appD_catalogue":          (None, "none"),
    "appE_glossary":           ("notation", "partial"),
    "appF_debye":              (None, "none"),
    "appG_params":             ("appD_figures", "partial"),
    "appH_registry":           ("appC_benchmarks", "high"),
}


def cite_keys(src: str) -> set[str]:
    out: set[str] = set()
    for m in re.finditer(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}", src):
        out |= {k.strip() for k in m.group(1).split(",") if k.strip()}
    return out


def with_ext(rel: str) -> str:
    """The path as LaTeX resolves it: keep the directory, add .tex if absent."""
    return rel if rel.endswith(".tex") else rel + ".tex"


def base(rel: str) -> str:
    """The bare file name, used for display and as the mapping key."""
    return Path(with_ext(rel)).name


def main() -> int:
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    repo = here.parent.parent.parent
    ap.add_argument("--final", default="/home/user/work/p5final",
                    help="directory holding the extracted final paper (read-only)")
    ap.add_argument("--mine", default=str(repo / "paper_v2" / "manuscript_v2" / "master"))
    ap.add_argument("--out", default=str(here / "section_map.csv"))
    a = ap.parse_args()

    final, mine = Path(a.final), Path(a.mine)
    for p_, what in ((final, "final paper"), (mine, "manuscript_v2/master")):
        if not p_.exists():
            raise SystemExit(f"cannot find {what} at {p_}; pass --final/--mine")
    fmain = (final / "main.tex").read_text(encoding="utf-8", errors="replace")

    theirs = []
    for m in re.finditer(r"\\input\{([^}]+)\}(?:\\label\{([^}]+)\})?", fmain):
        p = final / with_ext(m.group(1))
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8", errors="replace")
        titles = re.findall(r"^\s*\\section\*?\{([^}]*)\}", s, re.M)
        theirs.append({"file": base(m.group(1)),
                       "title": titles[0] if titles else "(section named only on its \\input line)",
                       "label": m.group(2) or "(none)",
                       "keys": cite_keys(s), "words": len(s.split())})

    mine_sections: dict[str, dict] = {}
    mmain = (mine / "main.tex").read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r"\\input\{([^}]+)\}", mmain):
        p = mine / with_ext(m.group(1))
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8", errors="replace")
        titles = re.findall(r"^\s*\\section\*?\{([^}]*)\}", s, re.M)
        mine_sections[Path(base(m.group(1))).stem] = {
            "title": titles[0] if titles else "(front matter)",
            "keys": cite_keys(s), "words": len(s.split())}

    rows = []
    for e in theirs:
        v2, overlap = MAP.get(Path(e["file"]).stem, (None, "none"))
        shared = jac = ""
        v2_title = "no equivalent"
        v2_words = ""
        if v2 and v2 in mine_sections:
            inter = e["keys"] & mine_sections[v2]["keys"]
            union = e["keys"] | mine_sections[v2]["keys"]
            shared = len(inter)
            jac = round(len(inter) / len(union), 3) if union else 0.0
            v2_title = mine_sections[v2]["title"]
            v2_words = mine_sections[v2]["words"]
        note = ""
        if overlap == "none":
            note = "no counterpart topic in manuscript_v2"
        elif shared == 0:
            note = "the final side carries no citations here, so overlap is judged on content"
        elif isinstance(shared, int) and shared < 3:
            note = "small bibliography overlap; see the section text before trusting the pair"
        rows.append({"final_file": e["file"], "final_section_title": e["title"],
                     "final_label": e["label"],
                     "v2_file": (v2 + ".tex") if v2 else "no equivalent",
                     "v2_section_title": v2_title, "overlap": overlap,
                     "shared_cite_keys": shared, "cite_jaccard": jac,
                     "final_words": e["words"], "v2_words": v2_words, "note": note})

    out = Path(a.out)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    tally: dict[str, int] = {}
    for r in rows:
        tally[r["overlap"]] = tally.get(r["overlap"], 0) + 1
    print(f"wrote {out}: {len(rows)} rows — " + ", ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    zero_high = [r["final_file"] for r in rows if r["overlap"] == "high" and r["shared_cite_keys"] == 0]
    if zero_high:
        print("WARNING: 'high' rows with no shared bib keys:", zero_high)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
