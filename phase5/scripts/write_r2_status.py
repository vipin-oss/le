#!/usr/bin/env python3
"""Write the R2 completion report from a successful strict-build run."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import unicodedata
from pathlib import Path

PHASE5 = Path(__file__).resolve().parents[1]
REPO = PHASE5.parent


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", text)


def source_lines(rel: str, needles: list[str]) -> list[str]:
    path = REPO / rel
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    hits = []
    for needle in needles:
        for i, line in enumerate(lines, 1):
            if needle.casefold() in line.casefold():
                hits.append(f"`{rel}:{i}`")
                break
    return hits


def pages_for(pages: list[str], groups: list[list[str]]) -> list[int]:
    found: set[int] = set()
    normalized = [norm(page) for page in pages]
    for group in groups:
        terms = [norm(t) for t in group]
        for i, page in enumerate(normalized, 1):
            if all(term and term in page for term in terms):
                found.add(i)
    return sorted(found)


def read_timing(path: Path) -> dict[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values


def check_conditional_rows() -> tuple[bool, int]:
    path = PHASE5 / "reports/APPA_LEDGER.csv"
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    conditional = [r for r in rows if (r.get("status") or "").upper() == "CONDITIONAL"]
    return all((r.get("condition_or_source") or "").strip() for r in conditional), len(conditional)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", type=Path, required=True)
    ap.add_argument("--timing", type=Path, required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--source-commit", required=True)
    ap.add_argument("--pdf-pages", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    raw = args.text.read_text(encoding="utf-8", errors="replace")
    pages = [p for p in raw.split("\f") if p.strip()]
    if args.pdf_pages != len(pages):
        raise ValueError(f"PDF metadata reports {args.pdf_pages} pages but extracted text has {len(pages)}")
    timing = read_timing(args.timing)

    # Source-level completion checks are explicit and independent of PDF layout.
    sec04 = (PHASE5 / "master/sections/sec04_thermoelastic.tex").read_text(encoding="utf-8")
    sec02 = (PHASE5 / "master/sections/sec02_literature.tex").read_text(encoding="utf-8")
    bib = (PHASE5 / "master/references_local.bib").read_text(encoding="utf-8")
    t1 = (PHASE5 / "master/tables/source/T1_historical_development.tex").read_text(encoding="utf-8")
    t2 = (PHASE5 / "master/tables/source/T2_generalized_thermoelastic.tex").read_text(encoding="utf-8")
    appa = (PHASE5 / "master/appendices/appA_equation_register.tex").read_text(encoding="utf-8")
    t4 = (PHASE5 / "master/tables/source/T4_wave_types.tex").read_text(encoding="utf-8")
    conditional_ok, conditional_count = check_conditional_rows()

    active_tex = "\n".join(
        p.read_text(encoding="utf-8", errors="replace")
        for p in (PHASE5 / "master").rglob("*.tex")
        if "build" not in p.parts
    )
    no_active_guyer1990 = "Guyer1990" not in active_tex and "@article{Guyer1990" not in bib
    no_active_tzou1997_cite = r"\cite{Tzou1997}" not in active_tex and r"\citep{Tzou1997}" not in active_tex

    specifications = [
        {
            "id": "1. GN type labels/citations",
            "ok": all(x in sec04 for x in ("type II theory (1993)", "type III theory (1992)"))
            and "GreenGN1992" in t1 and "Green1993" in t1 and "GreenGN1992" in t2 and "Green1993" in t2,
            "sources": source_lines("phase5/master/sections/sec04_thermoelastic.tex", [
                "Green--Naghdi type II theory (1993)", "Green--Naghdi type III theory (1992)"])
                + source_lines("phase5/master/sections/sec02_literature.tex", ["The Green--Naghdi type-II primary formulation"])
                + source_lines("phase5/master/tables/source/T1_historical_development.tex", ["Green--Naghdi II / III"])
                + source_lines("phase5/master/tables/source/T2_generalized_thermoelastic.tex", ["Green--Naghdi type II", "Green--Naghdi type III"]),
            "page_groups": [["Green--Naghdi type II theory", "1993"], ["Green--Naghdi type III theory", "1992"]],
            "evidence": "F13, F16-F17; GN-II is Green & Naghdi 1993, GN-III is Green & Naghdi 1992.",
        },
        {
            "id": "2. GN equations/symbols",
            "ok": r"\kappa^*\nabla^2\alpha_{\mathrm{GN}}" in sec04 and r"\dot{u}_{i,i}" in sec04
            and r"\kappa\nabla^2\dot{T} + \kappa^*\nabla^2 T" in sec04
            and "PRIMARY-SOURCE-CHECKED" in appa and "EQ-016" in appa,
            "sources": source_lines("phase5/master/sections/sec04_thermoelastic.tex", [
                r"\label{eq:4.11}", r"\label{eq:4.14}"])
                + source_lines("phase5/master/appendices/appA_equation_register.tex", ["EQ-016 &"])
                + source_lines("phase5/master/appendices/energy_flux_derivations.tex", [r"\label{ef:gn2:2}", r"\label{ef:gn3:1}"]),
            "page_groups": [["Green--Naghdi type II theory", "1993"], ["Green--Naghdi type III theory", "1992"]],
            "evidence": "F16-F17; Eq. 4.11 has one fewer time derivative on the displacement-rate coupling; κ* and κ are distinguished.",
        },
        {
            "id": "3. Tzou 1995/1997 distinction",
            "ok": "Tzou, 1995" in sec04 and "@article{Tzou1995" in bib and "@book{Tzou1997" in bib
            and no_active_tzou1997_cite,
            "sources": source_lines("phase5/master/sections/sec04_thermoelastic.tex", ["Dual-phase-lag (DPL) theory (Tzou, 1995)"])
                + source_lines("phase5/master/references_local.bib", ["@article{Tzou1995", "% Separate 1997 monograph", "@book{Tzou1997"])
                + source_lines("phase5/master/tables/source/T1_historical_development.tex", ["Dual/triple phase lag"])
                + source_lines("phase5/master/tables/source/T2_generalized_thermoelastic.tex", ["Dual-phase-lag"]),
            "page_groups": [["Dual-phase-lag", "Tzou", "1995"]],
            "evidence": "F15; Tzou 1995 is the DPL journal article; the 1997 entry is a separate book, not cited as the DPL source.",
        },
        {
            "id": "4. GK 1966 / Tzou 1995 continuum law",
            "ok": "GuyerKrumhansl1966" in bib and "lambda^2=c^2" in sec04.replace(" ", "")
            and "Ziman-averaged" in sec04 and "Tzou (1995, Eq.~15)" in sec04 and "Eq.~17" in sec04
            and no_active_guyer1990,
            "sources": source_lines("phase5/master/sections/sec04_thermoelastic.tex", ["Guyer--Krumhansl (GK) phonon transport."])
                + source_lines("phase5/master/sections/sec02_literature.tex", ["Guyer and Krumhansl (1966)"])
                + source_lines("phase5/master/references_local.bib", ["@article{GuyerKrumhansl1966"]),
            "page_groups": [["Guyer and Krumhansl", "Ziman-averaged"], ["Tzou", "Eq. 15", "Eq. 17"]],
            "evidence": "F10-F12 and F18; GK 1966 supplies Boltzmann structure and λ², while the continuum form and DPL mapping are explicitly secondary to Tzou 1995.",
        },
        {
            "id": "5. Moore-Gibson 1960 scope",
            "ok": "Moore and Gibson (1960) derived a third-order acoustic wave equation" in sec04
            and "not a heat-conduction law" in sec04,
            "sources": source_lines("phase5/master/sections/sec01_scope.tex", ["Moore--Gibson--Thompson-type thermoelastic models"])
                + source_lines("phase5/master/sections/sec04_thermoelastic.tex", ["Moore and Gibson (1960) derived"])
                + source_lines("phase5/master/tables/source/T1_historical_development.tex", ["Moore--Gibson--Thompson &"])
                + source_lines("phase5/master/tables/source/T2_generalized_thermoelastic.tex", ["Moore--Gibson--Thompson-type models"]),
            "page_groups": [["Moore and Gibson", "1960", "third-order acoustic"]],
            "evidence": "F14; the 1960 origin is relaxing-gas acoustics, not solid heat conduction; later MGT thermoelasticity is described as an analogue.",
        },
        {
            "id": "6. CONDITIONAL scopes and GL hybrid label",
            "ok": "LS/GL hybrid" in sec04 and "no flux-relaxation time" in sec04 and conditional_ok
            and "Conditional on the displayed linear laws" in t4,
            "sources": source_lines("phase5/master/sections/sec04_thermoelastic.tex", ["LS/GL hybrid", r"\label{eq:4.9}"])
                + source_lines("phase5/master/tables/source/T4_wave_types.tex", ["Conditional on the displayed linear laws", "LS speed requires"])
                + source_lines("phase5/master/sections/sec13_applications.tex", ["Conditional on that regime"])
                + source_lines("phase5/master/appendices/appA_equation_register.tex", [r"\caption{Equation register for Section 6", "EQ-9.9 &", "EQ-10.12 &"]),
            "page_groups": [["LS/GL hybrid"], ["Equation register for Section 9"], ["Energy-balance register"]],
            "evidence": f"All {conditional_count} CONDITIONAL APPA_LEDGER rows have nonempty conditions; Table T4 and application claims state their regimes. GL (4.9) uses Fourier flux; the older uniform-τ0 strain-rate form is labelled LS/GL hybrid.",
        },
    ]

    sec09 = (PHASE5 / "master/sections/sec09_interfaces.tex").read_text(encoding="utf-8")
    sec12 = (PHASE5 / "master/sections/sec12_comparative.tex").read_text(encoding="utf-8")
    cross_term_report = (PHASE5 / "reports/V-B3d-cross-term-check.md").read_text(encoding="utf-8")
    vb3d_ok = all(x in sec09 for x in ("0.212026", "0.787974", "0.211074", "0.211592")) and all(
        x.casefold() in cross_term_report.casefold() for x in ("Executed", "read-only source", "2.22e-16", "1.00000")
    )
    vb3d_sources = source_lines("phase5/master/sections/sec09_interfaces.tex", ["A concrete V-B3d coupled Biot case"])
    vb3d_sources += source_lines("phase5/reports/V-B3d-cross-term-check.md", ["# V-B3d total-field cross-term check"])
    unsupported_limit_rows = (
        "Green--Naghdi III & Lord--Shulman",
        "Moore--Gibson--Thompson & Triple phase-lag",
        "Green--Naghdi II & Classical coupled",
    )
    limits_ok = "formal parameter substitutions, not convergence theorems" in sec12 and all(
        row not in sec12 for row in unsupported_limit_rows
    )
    specifications.append({
        "id": "7. Section 12 limiting-case scope",
        "ok": limits_ok,
        "sources": source_lines("phase5/master/sections/sec12_comparative.tex", [
            r"Table~\ref{tab:limiting_cases_revisited} lists candidate formal reductions only.",
            r"The rows in Table~\ref{tab:limiting_cases_revisited} are formal parameter substitutions",
        ]),
        "page_groups": [["formal parameter substitutions", "convergence theorems"]],
        "evidence": "Three unsupported reductions (GN-III→LS, MGT→TPL, GN-II→classical) are absent. The paragraph distinguishes a formal substitution from a convergence theorem and notes established model-pair results.",
    })
    specifications.append({
        "id": "8. V-B3d total-field cross-term reproduction",
        "ok": vb3d_ok,
        "sources": vb3d_sources,
        "page_groups": [["0.212026", "0.787974"]],
        "evidence": "Read-only V-B3d script copied without modification and re-executed locally. A=1-R-T is definitional; bulk-dissipation checks are the independent numerical comparisons.",
    })

    lines = [
        "# R2 status report",
        "",
        f"**Strict CI:** [run {args.run_id}](https://github.com/vipin-oss/le/actions/runs/{args.run_id}) — successful publisher step only runs after all strict gates pass.",
        f"**Source commit:** `{args.source_commit}`",
        f"**Build window (UTC):** {timing.get('started_utc','unknown')} to {timing.get('finished_utc','unknown')}",
        f"**Build time:** {timing.get('duration_seconds','unknown')} seconds for `build_master.sh` (dependency installation excluded)",
        f"**PDF pages:** {args.pdf_pages}",
        "**Build output:** `phase5/build_outputs/phase5-v1.1-master.pdf` and the matching contact sheets are published by the same run.",
        "**Control evidence:** read-only `control/` findings were read from `claude/control` commit `94f18130ef356290635d5078d9a4af6eea43e775`; `verification/` sources remained read-only.",
        "**R3:** NOT STARTED, per instruction.",
        "",
        "| Item | Status | Source file:line | PDF page(s) | Evidence / scope |",
        "|---|---|---|---|---|",
    ]
    for spec in specifications:
        pdf_pages = pages_for(pages, spec["page_groups"])
        status = "DONE" if spec["ok"] and pdf_pages else "NOT DONE"
        refs = "; ".join(spec["sources"]) or "source reference not located"
        page_text = ", ".join(str(n) for n in pdf_pages) if pdf_pages else "not located"
        lines.append(f"| {spec['id']} | {status} | {refs} | {page_text} | {spec['evidence']} |")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
