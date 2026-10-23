#!/usr/bin/env python3
"""Apply R3f claims and bibliography changes only after Crossref gates pass."""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import crossref_enrich as cr


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def insert_block(text: str, marker: str, content: str, anchor: str) -> str:
    begin, end = f"% R3F-BEGIN:{marker}", f"% R3F-END:{marker}"
    text = re.sub(rf"(?ms)^{re.escape(begin)}\n.*?^{re.escape(end)}\n?", "", text)
    if not content.strip():
        return text
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one R3f anchor for {marker}; found {text.count(anchor)}")
    return text.replace(anchor, f"{begin}\n{content.rstrip()}\n{end}\n\n{anchor}", 1)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} replacement target, found {count}")
    return text.replace(old, new, 1)


def remove_bib_entry(text: str, key: str) -> str:
    pat = re.compile(rf"(?ms)^@[A-Za-z]+\s*\{{\s*{re.escape(key)}\s*,.*?^\}}\s*\n?")
    updated, count = pat.subn("", text)
    if count > 1:
        raise RuntimeError(f"Duplicate BibTeX entries for {key}")
    return updated


def merge_verified_bib(local_bib: Path, generated_bib: Path, mappings: list[dict[str, str]], rows: list[dict[str, str]]) -> int:
    text = local_bib.read_text(encoding="utf-8")
    by_key = {row["citekey"]: row for row in rows}
    map_by_key = {row["citekey"]: row for row in mappings}
    # Luchko/Gorenflo are specifically inaccurate legacy entries; other replacements
    # occur only after their mapped record passes Crossref.
    replace_keys = {"Luchko2010", "Gorenflo1997"}
    replace_keys.update(key for key, mapping in map_by_key.items()
                        if mapping.get("replace_existing", "").strip().upper() == "YES"
                        and by_key.get(key, {}).get("status") == "VERIFIED"
                        and by_key.get(key, {}).get("bib_ready") == "YES")
    for key in sorted(replace_keys):
        text = remove_bib_entry(text, key)
    generated = cr.parse_bib(generated_bib)
    blocks = re.findall(r"(?ms)^@[A-Za-z]+\s*\{[^,]+,.*?^\}", generated_bib.read_text(encoding="utf-8"))
    generated_by_key = {entry["key"]: block for entry, block in zip(generated, blocks)}
    added = 0
    existing_keys = {entry["key"] for entry in cr.parse_bib(local_bib)}
    for key, row in by_key.items():
        if row.get("status") != "VERIFIED" or row.get("bib_ready") != "YES":
            continue
        if key in generated_by_key and (key not in existing_keys or key in replace_keys):
            text = text.rstrip() + "\n\n" + generated_by_key[key].rstrip() + "\n"
            added += 1
    local_bib.write_text(text.rstrip() + "\n", encoding="utf-8")
    return added


def selected_rows(mappings: list[dict[str, str]], checks: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    check_by_key = {r.get("citekey", "").strip(): r for r in checks}
    selected = {}
    for mapping in mappings:
        key = mapping["citekey"].strip()
        result = check_by_key.get(key, {})
        if (mapping.get("include", "").strip().upper() == "YES"
                and result.get("status") == "VERIFIED"
                and result.get("bib_ready") == "YES"
                and result.get("resolved_citekey") == key):
            selected[key] = {**mapping, **result}
    return selected


def section_count(selected: dict[str, dict[str, str]], section: str) -> int:
    return sum(1 for row in selected.values()
               if row.get("primary_eligible", "").strip().upper() == "YES"
               and section in {part.strip() for part in row.get("sections", "").split(";")})


def section_read_count(selected: dict[str, dict[str, str]], section: str) -> int:
    return sum(1 for row in selected.values()
               if section in {part.strip() for part in row.get("sections", "").split(";")})


def add_to_section(path: Path, marker: str, content: str, anchor: str) -> None:
    text = path.read_text(encoding="utf-8")
    path.write_text(insert_block(text, marker, content, anchor), encoding="utf-8")


def strip_citation_key(text: str, key: str) -> str:
    pattern = re.compile(r"\\cite(?:\[[^]]*\])?\{([^{}]*)\}")
    def rewrite(match: re.Match[str]) -> str:
        keys = [item.strip() for item in match.group(1).split(",") if item.strip()]
        kept = [item for item in keys if item != key]
        return match.group(0) if len(kept) == len(keys) else (r"\cite{" + ",".join(kept) + "}" if kept else "")
    return pattern.sub(rewrite, text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-csv", type=Path, required=True)
    parser.add_argument("--map-csv", type=Path, required=True)
    parser.add_argument("--reports-dir", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--sections-dir", type=Path, required=True)
    parser.add_argument("--status-report", type=Path, required=True)
    args = parser.parse_args()

    mappings = read_csv(args.map_csv)
    checks = read_csv(args.verify_csv)
    if len(mappings) != 25 or len(checks) != 25:
        raise RuntimeError("R3f apply requires 24 queried works plus the Cattaneo NO-DOI status row")
    selected = selected_rows(mappings, checks)
    checks_by_key = {row["citekey"]: row for row in checks}
    added_keys = merge_verified_bib(args.local_bib, args.reports_dir / "R3F_VERIFIED_REFERENCES.bib", mappings, checks)
    bib_keys = {entry["key"] for entry in cr.parse_bib(args.local_bib)}
    if {key for key in selected if key not in bib_keys}:
        raise RuntimeError("A verified/bibliography-ready R3f citation has no local BibTeX entry")

    # New statements are generated source-by-source; a failed Crossref gate contributes no citation.
    s5 = []
    if "Chandrasekharaiah1984" in selected:
        s5.append(r"Chandrasekharaiah's temperature-rate-dependent thermopiezoelectric model retains a Fourier-form heat flux, $q_i=-\theta_0(b_i\dot{\theta}+k_{ij}\theta_{,j})$, with additional material constants; setting $a=s=b_i=0$ returns Mindlin's theory, while suppressing piezoelectric effects recovers Green--Lindsay (PRIMARY-SOURCE-CHECKED) \cite{Chandrasekharaiah1984}.")
    if "Nowacki1978" in selected:
        s5.append(r"Nowacki's classical Fourier thermopiezoelectric theory establishes uniqueness from the energy balance and states generalized Hamilton and reciprocity theorems (PRIMARY-SOURCE-CHECKED) \cite{Nowacki1978}.")
    void_parts = []
    if "Nunziato1979" in selected:
        void_parts.append(r"the nonlinear parent theory treats solid-like porous materials with non-conducting heat and associates volume-fraction change with internal dissipation \cite{Nunziato1979}")
    if "Cowin1983" in selected:
        void_parts.append(r"the linear elastic theory makes void fraction an independent kinematic field and reports dispersed, attenuated longitudinal waves \cite{Cowin1983}")
    if "Iesan1986" in selected:
        void_parts.append(r"the linear thermoelastic-void theory establishes uniqueness, reciprocity, and variational results \cite{Iesan1986}")
    if void_parts:
        s5.append("The voids ingredient remains distinct from piezoelectric coupling: " + "; ".join(void_parts) + " (PRIMARY-SOURCE-CHECKED).")
    count_s5 = 4 + section_read_count(selected, "s.5")
    add_to_section(args.sections_dir / "sec05_multiphysics.tex", "READ-SOURCES", "\n\n".join(s5),
                   r"\subsubsection{Modal content of a piezoelectric solid}")
    sec5_path = args.sections_dir / "sec05_multiphysics.tex"
    sec5_text = sec5_path.read_text(encoding="utf-8")
    if count_s5 >= 6:
        s5_scope_note = (f"Section 5 now has {count_s5} eligible read sources; primary sources remain limited for the fully coupled piezo-thermal-void interaction, and results for separate constitutive ingredients are not merged into a new coupled law.")
    else:
        s5_scope_note = "Limited primary sources remain for the broader family and for the fully coupled piezo-thermal-void interaction; results for separate constitutive ingredients are not merged into a new coupled law."
    sec5_text = sec5_text.replace("Limited primary sources are available for this broader family.", s5_scope_note)
    sec5_path.write_text(sec5_text, encoding="utf-8")

    # Section 2 historical paragraph: distinguish the source's retrospective from unread originals.
    sec2_path = args.sections_dir / "sec02_literature.tex"
    sec2 = sec2_path.read_text(encoding="utf-8")
    old_history = ("In 1948, in the proceedings of the Italian academy, Cattaneo \\cite{Cattaneo1948} showed that the paradox disappears if heat flux is allowed a relaxation time; in 1958 Vernotte \\cite{Vernotte1958} reached the same conclusion independently in the French academy proceedings. The two papers are, in structural terms, the same result arrived at from the same constraint by two separate routes, and they established the argument that the history of the field would follow: a physical inconsistency is identified, a constitutive modification is proposed that removes it, and the modified model is then shown to require further modification because something else has been lost.")
    if "Joseph1989" in selected:
        new_history = ("Joseph and Preziosi's retrospective notes that Maxwell's 1867 heat-conduction equation contained a time-derivative term that Maxwell said could be neglected; it traces the first finite-speed heat-flux law to Cattaneo (1948) and describes Vernotte (1958a) as writing Cattaneo's law as the simplest generalisation (SECONDARY-SOURCE) \\cite{Joseph1989}. The Cattaneo bibliographic venue follows Povstenko (2009), Ref.~[12], and is explicitly retained as NO-DOI; the primary 1948 text was not checked here (BIBLIOGRAPHIC-SOURCE) \\cite{Povstenko2009}.")
    else:
        new_history = "The historical account of the 1867--1958 finite-speed heat-law developments is omitted in this update because its mapped Crossref source did not pass verification."
    sec2 = replace_once(sec2, old_history, new_history, "Section 2 history")
    old_proceedings = r"The founding hyperbolic-conduction results appeared in the Italian and French academy proceedings \cite{Cattaneo1948,Vernotte1958},"
    new_proceedings = (r"The founding hyperbolic-conduction history is summarized in Joseph and Preziosi's retrospective (SECONDARY-SOURCE) \cite{Joseph1989},"
                       if "Joseph1989" in selected else "The founding hyperbolic-conduction history is treated as source-conditional,")
    sec2 = replace_once(sec2, old_proceedings, new_proceedings, "Section 2 proceedings history")
    # Luchko is retained only for the checked Fourier-method claim; Gorenflo only where verified.
    sec2 = strip_citation_key(sec2, "Luchko2010")
    if "Gorenflo1997" not in selected:
        sec2 = strip_citation_key(sec2, "Gorenflo1997")
    sec2_path.write_text(sec2, encoding="utf-8")

    # Section 4: keep 1995 heat-law and 1998 thermoelastic C-T attributions distinct.
    dpl_parts = []
    if "HetnarskiIgnaczak1999" in selected:
        dpl_parts.append(r"Hetnarski and Ignaczak's 1999 survey calls the thermoelastic dual-phase-lag formulation the C--T model and attributes it to Chandrasekharaiah and Tzou (1998); this is distinct from Tzou's 1995 heat-conduction lag law (SECONDARY-SOURCE; the claim is dated to 1999) \cite{HetnarskiIgnaczak1999,Tzou1995}.")
        dpl_parts.append(r"The same survey states that, as of 1999, none of its five models had been confirmed by a combined thermoelastic experiment except in the rigid-conductor limit; this is a dated literature statement, not a claim about later experiments (SECONDARY-SOURCE) \cite{HetnarskiIgnaczak1999}.")
    add_to_section(args.sections_dir / "sec04_thermoelastic.tex", "CT-ATTRIBUTION", "\n\n".join(dpl_parts),
                   r"\begin{equation}" + "\n" + r"q_i(t + \tau_q)")
    acoustic = []
    if "MarchandMcDevittTriggiani2012" in selected:
        acoustic.append(r"Marchand, McDevitt, and Triggiani analyze an acoustic Jordan--MGT equation and report an exponential-decay result for that acoustic system; this source is not thermoelastic MGT evidence (PRIMARY-SOURCE-CHECKED; ACOUSTIC) \cite{MarchandMcDevittTriggiani2012}.")
    add_to_section(args.sections_dir / "sec04_thermoelastic.tex", "ACOUSTIC-MGT", "\n\n".join(acoustic),
                   r"\paragraph{MGT evidence scope.}")

    # Section 8 source-specific inversion and wave-formalism statements.
    s8 = []
    if "Durbin1974" in selected:
        s8.append(r"Durbin's averaged cosine-and-sine procedure improves on the earlier Dubner--Abate cosine method: its error bound is independent of $t$ over $0<t<2T$, and for $|f|\leq C$ is $C/(e^{2aT}-1)$ (PRIMARY-SOURCE-CHECKED) \cite{Durbin1974,DubnerAbate1968}.")
    if "HonigHirdes1984" in selected:
        s8.append(r"Honig and Hirdes combine Durbin's discretization correction with acceleration of a non-alternating series and parameter selection; in one reported example, Durbin required about 60 times as many transform evaluations and 30 times the CPU time as LAPIN for comparable accuracy, a result specific to that example (PRIMARY-SOURCE-CHECKED) \cite{HonigHirdes1984}.")
    if "Stroh1958" in selected or "Stroh1962" in selected:
        keys = [f"Stroh{year}" for year in ("1958", "1962") if f"Stroh{year}" in selected]
        refs = ",".join(keys)
        if len(keys) == 2:
            s8.append(rf"Stroh's 1958 anisotropic-elasticity treatment and 1962 steady-motion analysis are purely elastic; neither supplies a thermoelastic Stroh formulation (PRIMARY-SOURCE-CHECKED) \cite{{{refs}}}.")
        elif keys:
            s8.append(rf"The checked Stroh {keys[0][-4:]} paper treats purely elastic anisotropy and supplies no thermoelastic formulation (PRIMARY-SOURCE-CHECKED) \cite{{{refs}}}.")
    if "ChadwickSneddon1958" in selected:
        s8.append(r"In classical Fourier thermoelastic plane waves, Chadwick and Sneddon report no thermal modification of S waves, while the coupled P and thermal modes are dispersed and attenuated; no numerical attenuation constants are reproduced here (PRIMARY-SOURCE-CHECKED) \cite{ChadwickSneddon1958}.")
    section_count_s8 = 3 + section_read_count(selected, "s.8")
    inversion_count = 3 + sum(1 for key in ("Durbin1974", "HonigHirdes1984") if key in selected)
    # Remove Luchko from the Laplace/Mittag-Leffler claim regardless of its Crossref outcome.
    sec8_path = args.sections_dir / "sec08_mathematical_methods.tex"
    sec8_text = sec8_path.read_text(encoding="utf-8")
    sec8_text = sec8_text.replace(r"\cite{Gorenflo1997,Luchko2010}",
                                  r"\cite{Gorenflo1997}" if "Gorenflo1997" in selected else "")
    for key in ("Luchko2010", "Gorenflo1997"):
        if key not in selected:
            sec8_text = strip_citation_key(sec8_text, key)
    if "Luchko2010" in selected:
        fourier_anchor = "become the only available check on a numerical scheme."
        fourier_remark = (" For the specific time-fractional diffusion initial-boundary-value problem with a Caputo--Dzherbashyan derivative of order $0<\\alpha\\leq1$ and the stated divergence-form operator, Luchko proves existence by a Fourier method, alongside a maximum principle, uniqueness, and continuous dependence (PRIMARY-SOURCE-CHECKED) \\cite{Luchko2010}.")
        sec8_text = replace_once(sec8_text, fourier_anchor, fourier_anchor + fourier_remark, "Luchko Fourier-method remark")
    old_scope = "Limited primary sources are available for numerical Laplace inversion in this section."
    if section_count_s8 >= 6:
        new_scope = f"Section~8 now has {section_count_s8} eligible read sources overall, including {inversion_count} numerical-inversion sources."
        if old_scope in sec8_text:
            sec8_text = replace_once(sec8_text, old_scope, new_scope, "Section 8 evidence scope")
    sec8_text = insert_block(sec8_text, "READ-SOURCES", "\n\n".join(s8),
                             r"\subsection{Green's functions and fundamental solutions}")
    sec8_path.write_text(sec8_text, encoding="utf-8")

    # Section 10: distinguish classical surface-wave flux from interface energy partition.
    s10 = []
    if "IvanovSavova1991" in selected:
        s10.append(r"For the classical isotropic Rayleigh-type surface-wave problem, Ivanov and Savova find that the kinetic-plus-internal energy-flux vector is not parallel to the surface; its direction varies with depth, and its magnitude decays with depth and exponentially along the line of intersection of constant-phase planes (PRIMARY-SOURCE-CHECKED) \cite{IvanovSavova1991}.")
    joseph_keys = [key for key in ("Joseph1989", "Joseph1990") if key in selected]
    if joseph_keys:
        s10.append(rf"Joseph and Preziosi's historical review and addendum trace heat-wave ideas from kinetic theory to continuum models (SECONDARY-SOURCE); this chronology is not evidence for a modal energy-partition identity \cite{{{','.join(joseph_keys)}}}.")
    add_to_section(args.sections_dir / "sec10_energy.tex", "READ-SOURCES", "\n\n".join(s10),
                   r"\subsection{Interface energy balance}")
    count_s10 = 3 + section_read_count(selected, "s.10")
    sec10_path = args.sections_dir / "sec10_energy.tex"
    sec10_text = sec10_path.read_text(encoding="utf-8")
    old_scope_10 = "Limited primary sources are available for the exact lossless reduction; GAP-09 remains open."
    if count_s10 >= 6 and old_scope_10 in sec10_text:
        new_scope_10 = (f"Section 10 now has {count_s10} eligible read sources overall; evidence for the exact lossless reduction remains limited and model-specific; GAP-09 remains open.")
        sec10_text = replace_once(sec10_text, old_scope_10, new_scope_10, "Section 10 evidence scope")
        sec10_path.write_text(sec10_text, encoding="utf-8")

    # Section 11: fractional source facts and a visibly conditional 2011 attribution.
    s11 = []
    if "Povstenko2009" in selected:
        s11.append(r"Povstenko's 2009 account gives a power-law kernel leading to a Caputo time-fractional heat equation, with the Fourier case at $\alpha=1$ and the wave-equation case at $\alpha=2$ (SECONDARY-SOURCE) \cite{Povstenko2009}.")
        s11.append(r"That 2009 source does not print the fractional-Cattaneo flux law displayed below; its attribution to Povstenko (2011) remains CONDITIONAL pending equation-level checking of the 2011 paper (SECONDARY-SOURCE for the 2009 distinction) \cite{Povstenko2009,Povstenko2011}.")
    if "Gorenflo1997" in selected:
        s11.append(r"Gorenflo and Mainardi write $E_{\alpha}(z)=\sum_{n=0}^{\infty}z^n/\Gamma(\alpha n+1)$; equivalently, the generalized factorial in this series is $(\alpha n)!:=\Gamma(\alpha n+1)$ (REFERENCE-SOURCE) \cite{Gorenflo1997}.")
    if "GorenfloKilbasMainardiRogosin2014" in selected:
        s11.append(r"The 2014 Gorenflo--Kilbas--Mainardi--Rogosin monograph is used here as a reference for Mittag--Leffler definitions only; no specific theorem is attributed to it (REFERENCE-SOURCE) \cite{GorenfloKilbasMainardiRogosin2014}.")
    count_s11 = 5 + section_read_count(selected, "s.11")
    add_to_section(args.sections_dir / "sec11_advanced.tex", "READ-SOURCES", "\n\n".join(s11),
                   r"\subsubsection{Fractional models with internal structure}")
    sec11_path = args.sections_dir / "sec11_advanced.tex"
    sec11 = sec11_path.read_text(encoding="utf-8")
    old_attribution = r"Povstenko \cite{Povstenko2011} introduced a fractional Cattaneo-type constitutive law."
    new_attribution = (r"The attribution of the fractional Cattaneo-type constitutive law to Povstenko (2011) remains CONDITIONAL: the equation-level statement has not been checked against that paper. "
                       r"The displayed law is retained as a conditional review parameterization, not as a source-verified equation (CONDITIONAL) \cite{Povstenko2011}.")
    if old_attribution in sec11:
        sec11 = replace_once(sec11, old_attribution, new_attribution, "fractional-Cattaneo attribution")
    elif "fractional Cattaneo-type constitutive law to Povstenko (2011) remains CONDITIONAL" not in sec11:
        raise RuntimeError("The expected Section 11 fractional-Cattaneo attribution was not found")
    old_scope_11 = "Limited primary sources are available for these fractional thermoelastic and MDD-versus-fractional subtopics; these source-specific formulations are not an exhaustive classification."
    if count_s11 >= 6:
        new_scope_11 = (f"Section~11 now has {count_s11} eligible read sources; the MDD-versus-fractional subtopic remains source-specific and is not an exhaustive classification.")
        if old_scope_11 in sec11:
            sec11 = replace_once(sec11, old_scope_11, new_scope_11, "Section 11 evidence scope")
    if "Gorenflo1997" not in selected:
        sec11 = strip_citation_key(sec11, "Gorenflo1997")
    sec11_path.write_text(sec11, encoding="utf-8")

    # Section 12: keep each model's scope explicit; only five new eligible primaries here.
    s12 = []
    if "vanDerMerwe2021" in selected:
        s12.append(r"Van der Merwe, van Rensburg, and Sieberhagen compare DPL, Cattaneo--Vernotte, and Fourier heat-pulse models by modal analysis; their modal partial sums converge in an energy norm, and their reported over/underdamped pattern is specific to the stated one-dimensional model (PRIMARY-SOURCE-CHECKED) \cite{vanDerMerwe2021}.")
    if "Chirita2016" in selected:
        s12.append(r"Chirita, D'Apice, and Zampoli recast a time-differential three-phase-lag model through fading memory and report thermodynamic restrictions and continuous-dependence results; the delay-time inequalities are not reproduced because they were not extracted from the checked source (PRIMARY-SOURCE-CHECKED) \cite{Chirita2016}.")
    if "ChenGurtin1968" in selected:
        s12.append(r"Chen and Gurtin's two-temperature theory for non-simple materials includes the linear relation $\theta=\phi-a\nabla^2\phi$ and states $a\geq0$ when $k>0$ (PRIMARY-SOURCE-CHECKED) \cite{ChenGurtin1968}.")
    if "GurtinWilliams1966" in selected:
        s12.append(r"Gurtin and Williams analyze the second-law admissibility of two temperatures; for a broad class that includes most materials with memory, the dual-temperature construction is inadmissible and reduces to Clausius--Duhem (PRIMARY-SOURCE-CHECKED) \cite{GurtinWilliams1966}.")
    if "WangLi2025IV" in selected:
        s12.append(r"Wang and Li's 2025 (IV) paper compares conventional, spatial-FD, and space-dependent-derivative models for unsteady heat diffusion; it is a diffusion-modelling paper, not a thermoelastic study (PRIMARY-SOURCE-CHECKED) \cite{WangLi2025IV}.")
    add_to_section(args.sections_dir / "sec12_comparative.tex", "READ-SOURCES", "\n\n".join(s12),
                   r"\subsection{Cross-theory comparison}")

    # Publish auditable per-section source counts and unresolved Crossref outcomes.
    source_count_rows = []
    new_counts = {}
    for section in ("s.2", "s.4", "s.4.9", "s.4.10", "s.5", "s.8", "s.10", "s.11", "s.12"):
        selected_keys = [key for key, row in selected.items()
                         if section in {part.strip() for part in row.get("sections", "").split(";")}]
        primary_count = sum(1 for key in selected_keys if selected[key].get("primary_eligible", "").upper() == "YES")
        new_counts[section] = primary_count
        previous = {"s.4.9": 4, "s.4.10": 3, "s.5": 4, "s.8": 3, "s.10": 3, "s.11": 5, "s.12": 0}.get(section)
        read_count = len(selected_keys)
        final = "not previously reported" if previous is None else str(previous + read_count)
        source_count_rows.append({"section": section, "R3F_verified_read_sources": read_count,
                                  "R3F_verified_primary_sources": primary_count,
                                  "previous_reported_source_count": "" if previous is None else str(previous),
                                  "updated_eligible_read_source_count": final})
    count_path = args.reports_dir / "R3F_SECTION_COUNTS.csv"
    with count_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(source_count_rows[0]), lineterminator="\n")
        writer.writeheader(); writer.writerows(source_count_rows)

    counts = Counter(row.get("status", "") for row in checks)
    ready_count = sum(row.get("bib_ready") == "YES" for row in checks)
    unresolved = [row for row in checks if row.get("status") in {"MISMATCH", "NOT-FOUND"}
                  or (row.get("status") == "VERIFIED" and row.get("bib_ready") != "YES")]
    section_report = args.status_report.read_text(encoding="utf-8")
    heading = "## R3f verification and manuscript update"
    end = section_report.find("## Final strict build")
    if end < 0:
        raise RuntimeError("R3_STATUS.md is missing its final strict-build section")
    old_start = section_report.find(heading)
    if old_start >= 0:
        section_report = section_report[:old_start] + section_report[end:]
        end = section_report.find("## Final strict build")
    known_counts = [row for row in source_count_rows if row["updated_eligible_read_source_count"].isdigit()]
    above_six = [f"{row['section']}={row['updated_eligible_read_source_count']}" for row in known_counts
                 if int(row["updated_eligible_read_source_count"]) >= 6]
    below_six = [f"{row['section']}={row['updated_eligible_read_source_count']}" for row in known_counts
                 if int(row["updated_eligible_read_source_count"]) < 6]
    threshold_line = ("- Sections at/above six eligible read sources: " + (", ".join(above_six) or "none") +
                      ". Sections below six: " + (", ".join(below_six) or "none") +
                      ". Scope notes were changed only for threshold-crossing sections; Section 4's MGT count excludes the acoustic Marchand source.")
    new_section = [heading, "",
        "- Scope: 24 mapped DOI works were queried; Cattaneo (1948) is separately recorded as NO-DOI and was not requested.",
        f"- R3f Crossref: {len(checks)} status rows; {counts['VERIFIED']} VERIFIED, {counts['MISMATCH']} MISMATCH, {counts['NOT-FOUND']} NOT-FOUND, {counts['NO-DOI']} NO-DOI; 24 requests; bibliography-ready: {ready_count}; citations selected only from VERIFIED/bibliography-ready rows; new BibTeX entries: {added_keys}.",
        "- Cattaneo1948 venue corrected to Atti Sem. Mat. Fis. Univ. Modena 3:83--101 (1948), retained as `verified = {NO_DOI}`; Joseph--Preziosi (1989) prints a different page value, noted in the BibTeX verification note.",
        "- Per-section checked-source counts (R3f read sources pass both the findings and Crossref gates; eligible-primary counts are shown separately):"]
    for row in source_count_rows:
        new_section.append(f"  - {row['section']}: {row['R3F_verified_read_sources']} verified/read source(s), {row['R3F_verified_primary_sources']} eligible primary; updated cumulative eligible-read count {row['updated_eligible_read_source_count']}.")
    new_section += [
        threshold_line,
        "- Durbin's interval/error statement and Honig--Hirdes performance comparison are source-specific; Stroh is identified as purely elastic; no unsupported general ranking or thermoelastic attribution is added.",
        "- The 1999 five-model experimental statement is explicitly dated. The C--T DPL thermoelastic attribution is kept distinct from Tzou's 1995 heat-law paper. The fractional-Cattaneo attribution to Povstenko (2011) remains CONDITIONAL.",
        "- R3f unresolved Crossref rows (not newly cited or added):"]
    if unresolved:
        new_section.extend(f"  - `{row['citekey']}` — {row['status']}: {row.get('reason', '')}" for row in unresolved)
    else:
        new_section.append("  - None.")
    new_section += ["", ""]
    section_report = section_report[:end] + "\n".join(new_section) + section_report[end:]
    args.status_report.write_text(section_report, encoding="utf-8")
    print(f"R3f selected {len(selected)} verified/bibliography-ready sources; new BibTeX={added_keys}; unresolved={len(unresolved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
