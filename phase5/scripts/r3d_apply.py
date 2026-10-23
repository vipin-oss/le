#!/usr/bin/env python3
"""Apply only R3d VERIFIED, eligible, claim-mapped evidence and report scope."""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from r3c_apply import merge_bib


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def insert_block(text: str, marker: str, content: str, anchor: str) -> str:
    begin = f"% R3D-BEGIN:{marker}"
    end = f"% R3D-END:{marker}"
    pattern = re.compile(rf"(?ms)^{re.escape(begin)}\n.*?^{re.escape(end)}\n?")
    text = pattern.sub("", text)
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one insertion anchor for {marker}, found {text.count(anchor)}")
    block = f"{begin}\n{content.rstrip()}\n{end}\n\n"
    return text.replace(anchor, block + anchor, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-csv", type=Path, required=True)
    parser.add_argument("--map-csv", type=Path, required=True)
    parser.add_argument("--plan-csv", type=Path, required=True)
    parser.add_argument("--readiness-csv", type=Path, required=True)
    parser.add_argument("--reports-dir", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--sections-dir", type=Path, required=True)
    parser.add_argument("--status-report", type=Path, required=True)
    args = parser.parse_args()

    verified_rows = read_csv(args.verify_csv)
    mappings = read_csv(args.map_csv)
    plan_rows = read_csv(args.plan_csv)
    readiness_rows = read_csv(args.readiness_csv)
    plan_by_key = {row.get("citekey", "").strip(): row for row in plan_rows if row.get("citekey", "").strip()}
    verify_by_key = {row.get("citekey", "").strip(): row for row in verified_rows if row.get("citekey", "").strip()}
    map_by_key = {row.get("citekey", "").strip(): row for row in mappings if row.get("citekey", "").strip()}

    selected: dict[str, dict[str, str]] = {}
    for mapping in mappings:
        key = mapping.get("citekey", "").strip()
        check = verify_by_key.get(key, {})
        plan = plan_by_key.get(key, {})
        if (mapping.get("include", "").upper() == "YES"
                and plan.get("technical_claim_eligible", "").upper() == "YES"
                and check.get("technical_claim_eligible", "").upper() == "YES"
                and check.get("status") == "VERIFIED"
                and check.get("bib_ready") == "YES"):
            selected[key] = {**mapping, **check}

    added_keys = merge_bib(args.local_bib, args.reports_dir / "R3D_VERIFIED_REFERENCES.bib")
    local_keys = {row["key"] for row in __import__("crossref_enrich").parse_bib(args.local_bib)}
    missing_bib = sorted({row.get("resolved_citekey", "") for row in selected.values()} - local_keys)
    missing_bib = [key for key in missing_bib if key]
    if missing_bib:
        raise RuntimeError("R3d citations lack verified BibTeX entries: " + ", ".join(missing_bib))

    # Section 4.9/4.10: keep thermoelastic and abstract acoustic MGT results separate.
    sec04 = args.sections_dir / "sec04_thermoelastic.tex"
    text04 = sec04.read_text(encoding="utf-8")
    legacy_lead = ("This form is retained as an unverified source lead: its primary-source convention, assumptions, and admissibility are not checked here, "
                   "and no eliminated third-order equation, dispersion law, or energy identity is asserted.")
    text04 = text04.replace(legacy_lead, "This constitutive variant is discussed below with its source-specific assumptions and stability scope.")
    qkey = selected.get("Quintanilla2019", {}).get("resolved_citekey")
    bkey = selected.get("Bazarra2021MGTradial", {}).get("resolved_citekey")
    lkey = selected.get("LasieckaWang2015MGT", {}).get("resolved_citekey")
    dkey = selected.get("DellOroLasieckaPata2016MGT", {}).get("resolved_citekey")
    if not qkey:
        text04 = text04.replace(r"\cite{MooreGibson1960,Quintanilla2019}", r"\cite{MooreGibson1960}")

    thermo_sentences = []
    if qkey:
        thermo_sentences.append(
            f"The displayed Eq.~\\eqref{{eq:4.18}} is the thermoelastic MGT variant with relaxation in the heat-flux law and no relaxation term in the stress. Quintanilla's Eqs.~(2.4), (2.5), and (3.5) give the source-specific coercivity condition "
            f"$K_{{ij}}=k_{{ij}}-\\tau k^*_{{ij}}$ positive definite, with the scalar condition $k-\\tau k^*>0$; "
            f"in one dimension, $k>k^*\\tau$ yields exponential stability, while $k<k^*\\tau$ gives instability "
            f"(PRIMARY-SOURCE-CHECKED) \\cite{{{qkey}}}. The source uses $\\alpha_{{,j}}$ in (2.1) but $\\theta_{{,j}}$ in (2.5) and (3.5), without reconciling that notation; the conclusion is kept model-specific."
        )
    if bkey:
        thermo_sentences.append(
            f"Bazarra et al. document a distinct radial thermoelastic MGT variant in which $\\tau$ also appears in the stress coupling, "
            f"$-\\beta(\\theta_{{,i}}+\\tau\\dot{{\\theta}}_{{,i}})$; their radial decay result assumes $\\bar k=k-\\tau k^*>0$ "
            f"(PRIMARY-SOURCE-CHECKED) \\cite{{{bkey}}}. Thus the relaxation placement in the stress law is variant-specific."
        )
    acoustic_sentences = []
    if lkey:
        acoustic_sentences.append(
            f"For the separate abstract acoustic MGT equation with memory, Lasiecka and Wang report exponential decay in the subcritical regime $\\alpha\\beta>\\gamma$ "
            f"(PRIMARY-SOURCE-CHECKED, ABSTRACT-LEVEL) \\cite{{{lkey}}}."
        )
    if dkey:
        acoustic_sentences.append(
            f"Dell'Oro, Lasiecka, and Pata state that at $\\alpha\\beta=\\gamma$ exponential stability holds if and only if $A$ is bounded; otherwise the energy tends to zero without an exponential rate "
            f"(PRIMARY-SOURCE-CHECKED, ABSTRACT-LEVEL) \\cite{{{dkey}}}."
        )
    mgt_lines = [r"\paragraph{Thermoelastic MGT evidence.}"]
    mgt_lines += thermo_sentences or ["The eligible primary-source records did not pass all Crossref/BibTeX checks in this run; no new MGT admissibility result is cited."]
    mgt_lines.append("\\paragraph{Acoustic MGT evidence.} Acoustic MGT-with-memory PDE decay uses its own acoustic parameter set and is separate from thermoelastic admissibility. The gas-dynamics parameter $\\gamma_{\\rm ac}=b-\\tau c^2$ is acoustic only; it is not the thermoelastic condition $k-\\tau k^*>0$.")
    mgt_lines += acoustic_sentences or ["No acoustic-MGT-with-memory result is stated here without a verified, mapped source."]
    mgt_lines.append("\\paragraph{MGT evidence scope.} Limited primary sources are available for the s.4.9--s.4.10 MGT subtopics; these model-specific results do not constitute a family-wide classification.")
    text04 = insert_block(text04, "MGT", "\n\n".join(mgt_lines), r"\subsection{Memory-dependent derivative")
    sec04.write_text(text04, encoding="utf-8")

    # Section 5: Mindlin's classical Fourier system is the reference limit, not a universal derivation.
    sec05 = args.sections_dir / "sec05_multiphysics.tex"
    text05 = sec05.read_text(encoding="utf-8")
    mindlin = selected.get("Mindlin1974Thermopiezo", {}).get("resolved_citekey")
    if mindlin:
        mindlin_text = (
            r"\paragraph{Classical thermopiezoelectric baseline.} Mindlin's linear plate theory gives momentum balance, "
            r"$D_{i,i}=0$, entropy balance $h_{i,i}=-\Theta_0\dot{\eta}$, and Fourier heat flux "
            r"$h_i=-K_{ij}\theta_{,j}$, together with linear constitutive equations from an electric Gibbs function "
            f"\\cite{{{mindlin}}}\\allowbreak{{}} (PRIMARY-SOURCE-CHECKED).\n\n"
            "Generalized piezothermoelastic models replace Fourier's law with a lagged or memory law. Mindlin's Fourier system is the classical limiting-case check: test each generalized model using its own parameters and equations rather than assuming the limit. "
            "Limited primary sources are available for this broader family."
        )
    else:
        mindlin_text = (r"\paragraph{Thermopiezoelectric evidence scope.} Limited primary sources are available for this section; "
                        "the classical Fourier thermopiezoelectric baseline is not augmented here because its candidate record did not pass the Crossref/BibTeX gates.")
    text05 = insert_block(text05, "MINDLIN", mindlin_text, r"\subsubsection{Modal content of a piezoelectric solid}")
    sec05.write_text(text05, encoding="utf-8")

    # Section 11: operator origin, checked fractional thermoelastic law, and the conceptual MDD/FD contrast.
    sec11 = args.sections_dir / "sec11_advanced.tex"
    text11 = sec11.read_text(encoding="utf-8")
    caputo = selected.get("Caputo1967", {}).get("resolved_citekey")
    if caputo:
        caputo_text = (
            r"\paragraph{Caputo operator and origin.} Caputo's 1967 work introduced the fractional derivative in viscoelastic stress--strain "
            r"models to represent nearly frequency-independent $Q$; the paper examined Earth's free modes and an aluminium rod and fitted an order "
            r"near $0.15$. It is an origin in viscoelasticity/geophysics, not in heat conduction. In Eq.~\eqref{eq:11.2}, the derivative remains inside "
            r"the integral for $0<\alpha<1$; the printed definition (5) is reconstructed from its proof-page integrand because the display is not legible "
            f"in the checked copy (PRIMARY-SOURCE-CHECKED) \\cite{{{caputo}}}."
        )
    else:
        caputo_text = r"\paragraph{Fractional-source scope.} The Caputo definition/origin record did not pass the Crossref/BibTeX gates in this run; no new source-specific statement is cited."
    text11 = insert_block(text11, "CAPUTO", caputo_text, r"\subsubsection{The fractional heat equation as a hereditary integral}")

    wang = selected.get("Wang2021", {}).get("resolved_citekey")
    if wang:
        wang_text = (
            r"\paragraph{MDD versus fractional modelling.} Wang and Li (2021, Part I) argue that the MDD formulation gives the memory duration and kernel "
            r"an explicit temporal interpretation, whereas the fractional-order description emphasizes local-change behavior; their illustration is a logistic-population "
            f"model, not a thermoelastic equation (PRIMARY-SOURCE-CHECKED) \\cite{{{wang}}}. This is an attributed modelling perspective, not a general theorem."
        )
    else:
        wang_text = ""
    if wang_text:
        text11 = insert_block(text11, "WANGLI", wang_text, r"\subsubsection{Fractional Cattaneo-type equations}")

    sherief = selected.get("Sherief2010Fractional", {}).get("resolved_citekey")
    if sherief:
        sherief_text = (
            r"\paragraph{Fractional thermoelasticity.} Sherief, El-Sayed, and Abd El-Latief's Eq.~(2.29) gives "
            r"$q_i+\tau_0\,{}^C D_t^\alpha q_i=-k_{ij}T_{,j}$ for $0<\alpha\leq1$. In their Eq.~(2.37), the same factor "
            r"$(1+\tau_0{}^C D_t^\alpha)$ acts on both the temperature-rate term and the strain-rate coupling term; it is not applied only to $\dot T$ "
            f"(PRIMARY-SOURCE-CHECKED) \\cite{{{sherief}}}. Their prefactor $\\tau_0$ is source-specific and is not silently converted to a fractional Taylor-lag coefficient."
        )
    else:
        sherief_text = r"\paragraph{Fractional-theory scope.} The candidate fractional thermoelastic equations did not pass the Crossref/BibTeX gates; no equation-level citation is inserted."

    convention = (
        r"\paragraph{Fractional coefficient convention.} For the review's generalized fractional Taylor-lag coefficient we use the Gamma-normalized form "
        r"$\tau^\alpha/\Gamma(1+\alpha)$; writing $\tau^\alpha/\alpha!$ means the same only when the generalized factorial is defined by "
        r"$\alpha!:=\Gamma(1+\alpha)$, not as an ordinary integer factorial. Sherief et al.'s Eqs.~(2.29)/(2.37) instead retain their source-specific "
        r"$\tau_0$ prefactor. Limited primary sources are available for these fractional thermoelastic and MDD-versus-fractional subtopics; these source-specific formulations are not an exhaustive classification."
    )
    sherief_text += "\n\n" + convention
    text11 = insert_block(text11, "SHERIEF", sherief_text, r"\subsection{Strain-gradient and couple-stress theories}")
    sec11.write_text(text11, encoding="utf-8")

    # Section 12: secondary coverage only; no equation/number/stability claims from the survey.
    sec12 = args.sections_dir / "sec12_comparative.tex"
    text12 = sec12.read_text(encoding="utf-8")
    survey = selected.get("Shakeriaski2021", {}).get("resolved_citekey")
    if survey:
        survey_text = (
            r"\paragraph{Survey scope.} Shakeriaski et al. catalogue which LS, GL, GN, dual-phase-lag, and multi-phase-lag models have been applied to which geometries "
            f"(SECONDARY-SOURCE) \\cite{{{survey}}}. This is a coverage map only: it does not support equations, numerical values, stability claims, or the secondary ordering the review repeats. "
            "Limited primary sources are available for this section's cross-family coverage statement; substantive claims remain assigned to the underlying sources."
        )
    else:
        survey_text = (r"\paragraph{Survey scope.} Limited primary sources are available for this section's cross-family coverage statement; "
                       "the survey candidate did not pass the Crossref/BibTeX gates and is not cited.")
    text12 = insert_block(text12, "SURVEY", survey_text, r"\subsection{Cross-theory comparison}")
    sec12.write_text(text12, encoding="utf-8")

    # Compute unique, VERIFIED, bibliography-ready, primary-source coverage by destination section.
    verified_sources: dict[str, set[str]] = defaultdict(set)
    source_role = {key: row.get("role", "") for key, row in plan_by_key.items()}
    source_role.update({row["citekey"]: row.get("claim_status", "") for row in mappings})
    reports_to_read = [
        (args.reports_dir / "CROSSREF_VERIFY.csv", "section"),
        (args.reports_dir / "CROSSREF_R3B_VERIFY.csv", "section"),
        (args.reports_dir / "CROSSREF_R3C_VERIFY.csv", "section"),
    ]
    records: list[dict[str, str]] = []
    for path, _ in reports_to_read:
        if path.exists():
            records.extend(read_csv(path))
    records.extend(verified_rows)
    r3c_map = {row.get("citekey", ""): row for row in read_csv(args.reports_dir / "R3C_CITATION_MAP.csv")}
    for row in records:
        key = row.get("citekey", "").strip()
        if (not key or row.get("status") != "VERIFIED" or row.get("technical_claim_eligible") != "YES"
                or row.get("bib_ready") != "YES"):
            continue
        role = source_role.get(key, "")
        if "SECONDARY" in role.upper():
            continue
        if row.get("destination_section"):
            destinations = [item.strip() for item in re.split(r"[;,]", row["destination_section"]) if item.strip()]
        elif key in r3c_map:
            destinations = [r3c_map[key].get("destination_section", row.get("section", "")).strip()]
        else:
            destinations = [row.get("section", "").strip()]
        for destination in destinations:
            if destination:
                verified_sources[destination].add(key)
    threshold_sections = [f"{section} ({len(keys)})" for section, keys in sorted(verified_sources.items()) if len(keys) >= 6]
    scoped_counts = {section: len(verified_sources.get(section, set())) for section in ("s.4.9", "s.4.10", "s.5", "s.10", "s.11", "s.12")}

    readiness = {row.get("section", ""): row for row in readiness_rows}
    readiness_summary = []
    for section in ("s.4.9", "s.4.10", "s.5", "s.11", "s.12"):
        row = readiness.get(section, {})
        full = row.get("eligible_full_or_primary", "n/a")
        partial = row.get("eligible_partial_abstract", "n/a")
        total = row.get("eligible_now", "n/a")
        label = "one secondary / zero primary" if section == "s.12" else f"{full} full/primary, {partial} partial of {total} eligible"
        readiness_summary.append(f"{section}: {label}")

    r3d_counts = Counter(row.get("status", "") for row in verified_rows)
    ready_count = sum(row.get("bib_ready") == "YES" for row in verified_rows)
    new_citations = sum(key in selected for key in map_by_key)
    unresolved = [row for row in verified_rows if row.get("status") in {"MISMATCH", "NOT-FOUND", "NO-DOI"}
                  or (row.get("status") == "VERIFIED" and row.get("bib_ready") != "YES")]
    unselected_verified = [row for row in verified_rows if row.get("status") == "VERIFIED" and row.get("bib_ready") == "YES" and row.get("citekey") not in selected]

    report = args.status_report.read_text(encoding="utf-8")
    begin = report.find("## R3d verification and manuscript updates")
    end = report.find("## Final strict build")
    if end < 0:
        raise RuntimeError("R3_STATUS.md must have the final-build heading")
    if begin < 0:
        begin = end
    elif begin >= end:
        raise RuntimeError("R3d status section must precede the final-build section")
    output = [
        "## R3d verification and manuscript updates", "",
        f"- Scope: nine newly eligible REFERENCE_PLAN rows across s.4.9, s.4.10, s.5, s.11, and s.12; Crossref requests were dynamic in CI only.",
        f"- R3d Crossref: {r3d_counts['VERIFIED']} VERIFIED, {r3d_counts['MISMATCH']} MISMATCH, {r3d_counts['NOT-FOUND']} NOT-FOUND, {r3d_counts['NO-DOI']} NO-DOI; mapped and bibliography-ready: {ready_count}; unique mapped citations used: {new_citations}; new BibTeX keys: {len(added_keys)}.",
        f"- Frozen CITATION_MAP exact-key matches among R3d candidates: {sum(row.get('frozen_map_exact_key_match') == 'YES' for row in verified_rows)}. Each placement is separately auditable in `R3D_CITATION_MAP.csv`.",
        f"- Frozen REFERENCE_READINESS snapshot: {'; '.join(readiness_summary)}.",
        f"- Unique VERIFIED primary-source coverage by touched section after R3d (plan role excludes secondary surveys): {', '.join(f'{s}={n}' for s,n in scoped_counts.items())}.",
        f"- Sections meeting the ≥6 VERIFIED primary-source bar across R3a/R3b/R3c/R3d: {', '.join(threshold_sections) if threshold_sections else 'none'}.",
        "- Section 4 separates thermoelastic MGT admissibility from acoustic MGT-with-memory decay; the acoustic gamma condition is not transferred to thermoelasticity. Section 5 cites Mindlin's Fourier thermopiezoelectric baseline and treats generalized Fourier limits as model-specific checks.",
        "- Section 11 attributes the fractional operator's origin to viscoelasticity/geophysics, cites Sherief's operator on both rate terms, names the Gamma-normalized review convention, and attributes the MDD/FD contrast to Wang and Li (2021, Part I). Section 12 uses LIT-0040 as SECONDARY coverage only.",
        "- 'Limited primary sources' is stated for the touched subsections with fewer than six primary sources; LIT-0040 is not counted as primary. GAP-09, GAP-12, and GAP-13 remain open; no gap is closed by metadata verification alone.",
        "- R3d title human-check list: `CROSSREF_R3D_HUMAN_CHECK.md`.",
        "- R3d unresolved identifiers (not cited):",
    ]
    if unresolved:
        output.extend(f"  - {row.get('lit_id')} `{row.get('citekey')}` — {row.get('status')}: {row.get('reason','')}" for row in unresolved)
    else:
        output.append("  - None.")
    if unselected_verified:
        output.append("- Crossref-VERIFIED but not inserted because they failed the bibliography/claim-map gate:")
        output.extend(f"  - {row.get('lit_id')} `{row.get('citekey')}` — {row.get('reason','')}" for row in unselected_verified)
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
    print(f"R3d selected {len(selected)} verified mapped rows; new BibTeX keys={len(added_keys)}; open rows={len(unresolved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
