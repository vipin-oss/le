#!/usr/bin/env python3
"""Build post_merge_claims.csv — the audit of the text the P5 merge added to the final paper.

One row per technical claim of the eight new pieces (contributions table, evidence protocol,
exact energy flux, provenance notes, balance-law appendix, interface-flux wording, taxonomy,
research questions, equation register + coverage, declarations), plus the structural claims the
merge could have broken (numbering, table placement).

Verdict vocabulary, applied strictly:
  SUPPORTED            the paper does what the claim says, and the evidence is in the package
  PARTLY               present but overstated, mis-pointed, or resting on an artefact not re-run here
  NOT SUPPORTED        the paper contradicts the claim (a real defect)
  SOURCE NOT AVAILABLE the underlying primary text is not in this workspace, so the attribution
                       cannot be re-checked here; this is not a verdict on the claim

Page numbers are the printed page numbers of paper_v2/main.pdf (164 pp).
Prints PASS and exits 0.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "post_merge_claims.csv"
COLS = ["claim_id", "location", "statement", "source", "verdict", "page_or_equation", "note"]

# (location, statement, source/bib key, verdict, page_or_equation, note)
R = [
    # ---- §1.3 contributions table (Table 2, p.14) ------------------------------------
    ("§1.3 p.14", "C1: one heat-law template with stepwise reductions covers LS, GL, GN-II/III, DPL, TPL, MGT, MDD, fractional models.",
     "eq:template (14); Table 5", "SUPPORTED", "(14), Table 5, pp.22",
     "Template (14) exists; the families named are treated in §7, §8, §10 as stated."),
    ("§1.3 p.14", "C1 evidence: the reductions are checked by check_reductions.py.",
     "scripts/check_reductions.py", "SUPPORTED", "Table 5; scripts/checks_log.txt",
     "The package's check log records 14 PASS and 0 FAIL, including 'all 9 reductions hold'."),
    ("§1.3 p.14", "C2: availability functional, its flux, the dissipation identity, and the statement that it is not the total-energy flux.",
     "eq:energy (16), eq:P (17), eq:exactflux (18)", "SUPPORTED", "(16)-(18), pp.23-24",
     "All three equations are present and the distinction is stated in words."),
    ("§1.3 p.14", "C2 evidence: net-flux balance at welded interfaces, Section 22.",
     "sec:interfaces; eq (17)", "SUPPORTED", "p.66, item (ii)",
     "Section 22 states that the net flux of (17), not the sum of mode fluxes, is conserved."),
    ("§1.3 p.14", "C3: comparison tables in Section 33 and a decision guide.",
     "Table 14, Table 15", "SUPPORTED", "§33 p.93",
     "Table 15 is the comparative summary of heat-conduction models; Table 14 the three-group taxonomy."),
    ("§1.3 p.14", "C3 evidence: one worked example per family in Section 31.",
     "§31 Examples 1-4", "PARTLY", "pp.87-89",
     "Four examples exist (lag law, nanobeam damping, interface partition, pulse). DPL, TPL, MGT, GN-II/III, fractional, MDD, non local and piezoelectric families have none, so 'per family' overstates it."),
    ("§1.3 p.14", "C4: five-axis taxonomy with an explicit dissimilarity.",
     "eq:taxdissim (82); Table 18", "SUPPORTED", "(82), Table 18, pp.101-103",
     "Five axes defined, dissimilarity (82) displayed, Table 18 assigns admissible values."),
    ("§1.3 p.14", "C5: per-equation verification register with a finite status vocabulary.",
     "Appendix J; Table 24", "SUPPORTED", "Table 24, p.128",
     "Eight statuses defined on p.127; ten equations registered in Table 24."),
    ("§1.3 p.14", "C6: fourteen executable benchmarks with reference solutions and tolerances.",
     "Appendix I; scripts/benchmark_registry.csv", "SUPPORTED", "Table 23; B01-B14",
     "The registry file has exactly 14 rows, B01-B14, each with reference solution, tolerance and script."),
    ("§1.3 p.14", "C7: stated evidence protocol and reporting standards.",
     "§1.6; §35", "SUPPORTED", "pp.15, 100", "Six rules in §1.6; checklist in §35."),

    # ---- §1.6 evidence protocol (p.15) ----------------------------------------------
    ("§1.6 p.15", "Rule 1: derivation and attribution are separated, and the register records which is which.",
     "Appendix J", "SUPPORTED", "p.15; p.127", "The register's status column does distinguish derived from source-checked."),
    ("§1.6 p.15", "Rule 2: every registered equation carries a status from a fixed vocabulary.",
     "Table 24", "SUPPORTED", "p.15; p.127", "Eight defined statuses; all ten registered rows carry one."),
    ("§1.6 p.15", "Rule 3: a secondary source is never promoted to a primary one.",
     "§1.6 rule 3", "SUPPORTED", "p.15", "Stated, and the register carries UNVERIFIED rows where the primary text was not read."),
    ("§1.6 p.15", "Rule 4: printed DOIs are checked to a level recorded in the reference register (R0-R3).",
     "verification_register.csv", "PARTLY", "p.15",
     "No R0-R3 reference register exists in the paper; the register is repository data only. The sentence points at something the reader cannot consult."),
    ("§1.6 p.15", "Rule 5: recomputable numbers are given with specification, reference solution and tolerance.",
     "Appendix I", "SUPPORTED", "p.15; Table 23", "Each benchmark row carries all three."),
    ("§1.6 p.15", "Rule 6: errors are recorded without personal characterisation.",
     "§1.6 rule 6", "SUPPORTED", "p.15", "Editorial rule; the text keeps to it (differences are called differences)."),
    ("§1.6 p.15", "The protocol states its own limits: not every cited work was read page by page.",
     "§1.6 closing paragraph", "SUPPORTED", "p.15", "Stated explicitly."),

    # ---- §3.5 exact energy flux (pp.23-24) ------------------------------------------
    ("§3.5 p.23", "Total energy per unit volume is kinetic plus internal; adding the two balances gives identity (18).",
     "eq:exactflux (18)", "SUPPORTED", "(18)",
     "Algebra on (1)-(9): no approximation enters, and the derivation was re-done by hand for this audit."),
    ("§3.5 p.23", "With no body force and no heat supply the outward-positive flux is (19).",
     "eq:exactflux-balance (19)", "SUPPORTED", "(19)", "Follows directly from (18)."),
    ("§3.5 p.23", "The flux has three parts: conduction, stress power and advection of total energy.",
     "eq (19)", "SUPPORTED", "(19)", "Each term is named in the following sentence."),
    ("§3.5 p.24", "The two-term flux J is the first-order reduction, not an exact fixed-volume flux.",
     "eq (19)", "SUPPORTED", "p.24", "Correct: J omits the advection term and the kinetic-energy part of the flux."),
    ("§3.5 p.24", "P_i is the flux whose net balance across a welded interface is exact (Section 22).",
     "eq:P (17); §22", "SUPPORTED", "(17); p.66", "Consistent with the interface section's item (ii)."),
    ("§3.5 p.24", "Energy is conserved exactly only for GN-II.",
     "summary box, p.24", "PARTLY", "p.24",
     "Read against (19) the sentence looks contradictory: (19) is an exact conservation law for any continuum. It should say that a positive-definite functional exists exactly only for GN-II."),

    # ---- §7.5 provenance table (Table 7, p.37) --------------------------------------
    ("§7.5 p.37", "Biot heat equation checked against Biot (1956) printed p.242, Eqs. (3.3)-(3.4).",
     "Biot1956", "SOURCE NOT AVAILABLE", "Table 7; (9)",
     "The 1956 paper is not in this workspace, so the page and equation numbers could not be re-checked."),
    ("§7.5 p.37", "Green-Lindsay stress and entropy checked against the primary text.",
     "Green1972", "SOURCE NOT AVAILABLE", "Table 7; (37)",
     "Green and Lindsay (1972) is not in this workspace; the attribution could not be re-checked."),
    ("§7.5 p.37", "GN-II form checked against Green and Naghdi (1993), Eq. (3.16) integrated once.",
     "Green1993", "SOURCE NOT AVAILABLE", "Table 7; §7",
     "Primary text not in this workspace. The appropriate image-only scan is on the outstanding list."),
    ("§7.5 p.37", "TPL law checked against Roy Choudhuri (2007), Eqs. (3)-(4).",
     "RoyChoudhuri2007", "SOURCE NOT AVAILABLE", "Table 7; (44)", "Primary text not in this workspace."),
    ("§7.5 p.37", "The DPL ordering tau_T > tau_q/2 is a spectral stability result of Quintanilla (2003).",
     "Quintanilla2003DPL", "SOURCE NOT AVAILABLE", "Table 7; §8",
     "Primary text not in this workspace; the register and the table state the same reading consistently."),
    ("§7.5 p.37", "Zener (1937) is the reed paper behind the flexural damping attribution.",
     "Zener1937", "SUPPORTED", "Table 7; Appendix E entry [24]",
     "The catalogue entry gives the title 'Theory of internal friction in reeds', which matches the use."),
    ("§7.5 p.37", "The second stiffness value in the piezothermoelastic bar is not quoted from the literature.",
     "eq:piezo (75)", "SUPPORTED", "Table 7; Table 24",
     "The example states its own data and the register marks (75) UNVERIFIED: the two statements agree."),

    # ---- Appendix A balance laws (p.108) --------------------------------------------
    ("App A p.108", "The momentum balance follows from Cauchy's postulate, the divergence theorem and the transport theorem.",
     "eq:mom (1)", "SUPPORTED", "(1); p.108", "The derivation as printed is correct on the stated assumptions."),
    ("App A p.108", "The stress is symmetric because the moment-of-momentum balance is applied with no couple stresses.",
     "eq (1)", "SUPPORTED", "p.108", "Correct; the text also says where the conclusion fails (micropolar continua)."),
    ("App A p.108", "Contracting (A) with the velocity gives the mechanical power balance.",
     "eq (1)", "NOT SUPPORTED", "p.108; (83)",
     "The cross-reference prints '(A)': its label sits on an unnumbered heading and inherits the appendix letter. It must point to (1)."),
    ("App A p.108", "The internal-energy balance is the second line of (1).",
     "eq (1), eq (84)", "SUPPORTED", "p.108", "(1) is displayed as two lines, so the reference is to the right place."),
    ("App A p.108", "The power and internal-energy balances are numbered (83) and (84).",
     "eq (83), eq (84)", "SUPPORTED", "(83)-(84)", "Both numbers appear in the build and continue the global sequence."),

    # ---- §22 interface energy (p.66) ------------------------------------------------
    ("§22 p.66", "The net flux of (17) into the interface equals the net flux out of it.",
     "eq:P (17)", "SUPPORTED", "p.66, item (ii)", "This is the corrected wording: net flux, not per-mode fractions."),
    ("§22 p.66", "In a dissipative medium the sum of mode fractions need not equal one, while the net flux does (66).",
     "eq (66)", "SUPPORTED", "(66)", "Statement and equation agree; the cross terms are the stated reason."),
    ("§22 p.66", "The four-mode sum reaches 1.34 near 8 omega*, and the transmitted elastic fraction reaches 1.1.",
     "Figure 26(b,c); scripts", "PARTLY", "p.66; Figure 26",
     "Numbers come from a figure script that was not re-run in this environment (no numeric stack), so they are quoted, not re-derived."),
    ("§22 p.66", "A correct energy check must use the net flux or include the interference terms.",
     "§22", "SUPPORTED", "p.66", "Follows from (66) and is stated as guidance."),
    ("§22 p.66", "Published ratio sets [94-97, 99-104] should be read with this qualification in mind.",
     "refs 94-104", "SUPPORTED", "p.66", "All cited numbers exist in the 337-entry reference list."),

    # ---- §36 taxonomy (pp.101-103) --------------------------------------------------
    ("§36 p.102", "The heat-flux template is a special case of Axis 2.",
     "§3.4; §36", "SUPPORTED", "p.102", "Reconciliation sentence is present and consistent with §3.4."),
    ("§36 p.102", "Five axes: physical, mathematical, wave, coupling, validation.",
     "Table 18", "SUPPORTED", "Table 18, p.103", "All five are defined and tabulated."),
    ("§36 p.102", "Two studies are directly comparable only when their vectors agree in the first two coordinates.",
     "eq (82)", "SUPPORTED", "p.102", "Stated, and the consequence for comparisons is given."),
    ("§36 p.102", "The axis-weight dissimilarity is (82), with w_math >= w_phys > w_coup > w_wave > w_val.",
     "eq:taxdissim (82)", "SUPPORTED", "(82)", "Displayed exactly as described; the ordering is called a modelling decision."),
    ("§36 p.102", "No result in the review depends on the numerical values of the weights.",
     "eq (82)", "SUPPORTED", "(82)", "Checked: (82) is displayed and cited but no later result evaluates it."),
    ("§36 p.102", "The paper's two classification schemes (Table 14's three groups, five axes here) are reconciled.",
     "Table 14; §36", "PARTLY", "p.93; pp.101-103",
     "No sentence maps the three groups onto the five axes. A reader meets two schemes for the same job."),

    # ---- §37 research questions (Table 19, pp.105-106) ------------------------------
    ("§37 p.106", "Table 19 lists ten researchable questions, each with the evidence that would settle it.",
     "Table 19", "SUPPORTED", "Table 19", "R1-R10 present, each with a 'what would settle it' entry."),
    ("§37 p.106", "Each row's 'stated in' column points to the section where the gap is first stated.",
     "§3, §22, §24, §27, §32, §33, Appendix I", "SUPPORTED", "Table 19",
     "All targets exist: Sections 3, 22, 24, 27, 32, 33 and Appendix I."),

    # ---- Appendix J register + coverage --------------------------------------------
    ("App J p.127", "Eight statuses are defined, each with a one-line meaning.",
     "§J vocabulary", "SUPPORTED", "p.127", "DERIVED, CONDITIONAL, PRIMARY-SOURCE-CHECKED, SECONDARY-SOURCE, VERIFIED-SYMBOLIC, UNVERIFIED, OPEN, WITHHELD."),
    ("App J p.128", "Table 24 registers ten equations of this paper.",
     "Table 24", "SUPPORTED", "Table 24", "Ten rows, each with a status and a basis."),
    ("App J p.128", "The registered equation numbers (1), (9), (37), (44), (11), (41), (4), (5), (48), (75) are the printed numbers of those equations.",
     "body equations", "SUPPORTED", "Table 24",
     "Cross-checked against the source labels: momentum=1, Biot=9, GL=37, TPL=44, relaxation=11, DPL=41, Clausius-Duhem=4, Coleman-Noll=5, MDD=48, piezothermoelastic=75."),
    ("App J p.128", "The source register holds 61 entries: 30 CONDITIONAL, 17 UNVERIFIED, 5 DERIVED, 4 PRIMARY-SOURCE-CHECKED, 3 OPEN, 1 WITHHELD, 1 VERIFIED-SYMBOLIC.",
     "manuscript_v2 appendix A register", "SUPPORTED", "p.128",
     "Recounted from the source file: the seven counts match and sum to 61."),
    ("App J p.129", "Of 136 printed equations of the source manuscript, 11 carry a status and 125 do not.",
     "equation_inventory.csv", "SUPPORTED", "p.129", "Regenerated from the inventory and the register: 136 rows, 11 registered."),
    ("App J p.129", "Table 25 inventories every printed equation with its label and status.",
     "Table 25", "SUPPORTED", "pp.129-135", "136 rows, printed order, statuses as in the generator."),
    ("App J p.129", "The Eq. and Label columns of Table 25 refer to the source manuscript, not to this paper's equations.",
     "Table 25 caption", "PARTLY", "p.129",
     "The caption explains the section titles only, so '1 eq:3.1' can be misread as this paper's equation 1. The caption should say the numbers and labels are the source's."),
    ("App J p.128", "Register sources are cited in author-year form.",
     "Table 24 basis column", "PARTLY", "Table 24",
     "The paper cites numerically everywhere else; the rows say 'Biot (1956)' with no bracket number, so the link to the reference list is not clickable or traceable."),

    # ---- Declarations (p.135) ------------------------------------------------------
    ("Declarations p.135", "CRediT statement lists one author with twelve roles.",
     "§declarations", "SUPPORTED", "p.135", "Self-declaration; nothing in the repository can contradict it."),
    ("Declarations p.135", "No specific grant from any funding agency supported the work.",
     "§declarations", "SUPPORTED", "p.135", "Self-declaration."),
    ("Declarations p.135", "Data and code availability points to Appendices D, I and H.",
     "Appendices D, I, H", "SUPPORTED", "p.135", "All three appendices exist and contain what the sentence names."),
    ("Declarations p.135", "Generative tools were used for drafting, for the scripts, and for the checks; the author is responsible.",
     "§declarations", "PARTLY", "p.135",
     "Self-declaration that cannot be verified from the repository; the scripts and checks_log.txt it refers to do exist."),

    # ---- structural claims of the merge -------------------------------------------
    ("whole paper", "The paper has 38 numbered sections and ten appendices A-J.",
     "table of contents", "SUPPORTED", "pp.2-9", "Counted from the contents pages and the source section commands."),
    ("whole paper", "Tables 21, 22 and 23 print in their appendices.",
     "Tables 21-23", "NOT SUPPORTED", "pp.162-164",
     "All three float after the reference list, which ends on p.161. The appendix bodies name tables that a reader finds 25 pages later."),
    ("§1.6 p.15", "Rule 1's cross-reference to Appendix J resolves.",
     "Appendix J", "SUPPORTED", "p.15; p.127", "Appendix J exists and is titled as referenced."),
]


def main() -> int:
    rows = []
    for i, (loc, stmt, src, verdict, pe, note) in enumerate(R, 1):
        rows.append({"claim_id": f"PMC-{i:03d}", "location": loc, "statement": stmt,
                     "source": src, "verdict": verdict, "page_or_equation": pe, "note": note})
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    import collections
    c = collections.Counter(r["verdict"] for r in rows)
    print(f"rows {len(rows)}: " + ", ".join(f"{k} {v}" for k, v in c.most_common()))
    over = [r["claim_id"] for r in rows if len(r["statement"].split()) > 25]
    print("statements over 25 words:", over or "none")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
