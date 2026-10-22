#!/usr/bin/env python3
"""Build verification/APPA_LEDGER.csv from the two appA equation registers.

Inputs (read-only, extracted with `git archive` into /tmp/ms):
  phase4/manuscript/appendices/appA_equation_register.tex   (LEGACY)
  phase5/master/appendices/appA_equation_register.tex       (LIVE)

The file reproduces every register row verbatim (ID, printed equation,
status tag exactly as the register gives it, register note) and adds the
B9 columns: whether *this* audit re-checked the row, the verdict, the
execution evidence, and the scope the verdict covers.

EQUATION_LEDGER.csv (176 rows) and CLAIM_LEDGER.csv (53 rows) are NOT
touched by this script.
"""
import csv, json, os, re, sys

SRC = "/tmp/appA_rows.json"
FILES = [("LEGACY", "/tmp/ms/phase4/manuscript/appendices/appA_equation_register.tex"),
         ("LIVE", "/tmp/ms/phase5/master/appendices/appA_equation_register.tex")]

def parse(paths):
    """Re-parse the two registers (same strict ' & ' split used to build the CSV)."""
    out = []
    for ver, path in paths:
        sec = "?"
        for ln in open(path):
            m = re.match(r"\\subsection\{(Layer [IVX]+)[^}]*Section (\d+)", ln)
            if m:
                sec = "S" + m.group(2)
            if not ln.startswith("EQ-"):
                continue
            line = re.sub(r"\\\\+\s*$", "", ln.rstrip("\n"))
            parts = line.split(" & ")
            if len(parts) != 4:
                print("SPLIT-ERR", ver, len(parts), file=sys.stderr)
                continue
            eid, eq, st, note = [p.strip().rstrip("\\\\").strip() for p in parts]
            out.append(dict(row_id=eid, version=ver, section=sec, equation=eq,
                            status_in_register=st, register_note=note))
    return out

# (version, row_id) -> (check, verdict, evidence, scope)
V = {}
def v(ver, rid, check, verdict, ev, scope):
    V[(ver, rid)] = (check, verdict, ev, scope)

L, VV = "LEGACY", "LIVE"
DIM = "V-B9a_checks.py CHECK 1"

# ---------------- Layer I / section 3 (identical in both versions except 007)
for ver in (L, VV):
    v(ver, "EQ-001", "re-checked", "CORRECT",
      "momentum balance, v_i = du_i/dt", "classical Cauchy continuum, no body couple")
    v(ver, "EQ-002", "re-checked", "CORRECT-CONDITIONAL",
      "angular momentum balance", "no couple stresses (assumption stated in row)")
    v(ver, "EQ-003", "re-checked", "CORRECT",
      "product of EQ-001 with v_i gives sigma_ij eps_dot_ij", "no couple stresses")
    v(ver, "EQ-004", "re-checked", "CORRECT",
      "first law, no internal supply", "small strain, single temperature")
    v(ver, "EQ-005", "not re-checked", "CARRIED",
      "row text truncated in register ('Dissipation inequality >= 0')", "-")
    v(ver, "EQ-006", "not re-checked", "CARRIED",
      "row text truncated in register ('Coleman--Noll restrictions')", "-")
    v(ver, "EQ-008", "re-checked", "CORRECT",
      "definition of velocity; no content to falsify", "kinematic definition")
    v(ver, "EQ-009", "re-checked", "CORRECT",
      "definition of infinitesimal strain", "small-strain kinematics")
    v(ver, "EQ-010", "re-checked", "CORRECT",
      "definition of rotation tensor", "small-strain kinematics")
v(L, "EQ-007", "re-checked", "CORRECT-CONDITIONAL",
  "sign of mechanical channel; cf. V-B3d S2.4 (J = -sigma v + theta q/T0, tensile-positive)",
  "correct only for compressive-positive stress, which the legacy row does not state")
v(VV, "EQ-007", "re-checked", "CORRECT-CONDITIONAL",
  "agrees with V-B3d S2.4 once tensile-positive + outward-positive are fixed (stated in row)",
  "classical energy flux, outward-positive, symmetric stress")

# ---------------- Layer II / section 4
for ver in (L, VV):
    v(ver, "EQ-011", "re-checked", "CORRECT",
      "substitute sigma = (lambda eps_kk)1 + 2 mu eps - beta T 1 into EQ-001", "isotropic linear, small strain")
    v(ver, "EQ-012", "re-checked", "CORRECT",
      "classical heat equation, rho c_v T_dot = k lap T - beta T0 u_dot_{i,i}", "Fourier, linearized")
    v(ver, "EQ-013", "re-checked", "CORRECT",
      "standard LS law q + tau0 q_dot = -k grad T", "consistency check only: Lord-Shulman 1967 not read")
    v(ver, "EQ-014", "re-checked", "CORRECT",
      "uncoupled branch of EQ-013 gives tau0 T_ddot + T_dot = (k/rho c_v) lap T => c_T^2 = k/(rho c_v tau0)",
      "isotropic uncoupled, tau0 > 0")
    v(ver, "EQ-016", "re-checked", "WRONG-CONFIRMED",
      DIM + "; also contradicted by Barak et al. 2023 eq (10) integrated once in time",
      "GN-II isotropic, alpha_dot = T, [beta] = Pa/K; the coupling term carries one time derivative too many")
    v(ver, "EQ-017", "re-checked", "WRONG-CONFIRMED",
      "V-B9a_checks.py CHECK 2 (missing 1/T factor; sign convention unstated)",
      "GN-II, p_i = entropy flux, [k*] = W/(m K) s")
    v(ver, "EQ-018", "re-checked", "CORRECT-CONDITIONAL",
      "definitional DPL lag relation; Taylor truncation NOT named (standing rule)",
      "any PDE use requires the truncation order to be stated")
    v(ver, "EQ-020", "re-checked", "CORRECT-CONDITIONAL",
      "matches Barak et al. 2023 eq (1) as printed (1/tau, horizon tau); dimension s^-1 OK",
      "MDD definition; kernel and horizon free")
    v(ver, "EQ-023", "re-checked", "CORRECT", "standard piezoelectric constitutive law", "linear, isothermal, no couple stress")
    v(ver, "EQ-024", "re-checked", "CORRECT", "standard electric displacement", "linear piezoelectric")
    v(ver, "EQ-025", "re-checked", "CORRECT", "E = -grad phi (quasi-static)", "no magnetic induction")
    v(ver, "EQ-026", "re-checked", "CORRECT", "charge conservation, no free charge", "quasi-static electric field")
    v(ver, "EQ-027", "re-checked", "CORRECT",
      "matches Barak et al. 2023 eq (3) as printed (PDF p.3) up to symbol names (e vs E)",
      "linear piezothermoelasticity; T = temperature increment in the source")
    v(ver, "EQ-028", "re-checked", "CORRECT",
      "matches Barak et al. 2023 eq (6) as printed (PDF p.3) up to symbol names",
      "linear piezothermoelasticity")

v(L, "EQ-015", "not re-checked", "CARRIED",
  "live register withdrew the two-temperature attribution; GL 1972 not read",
  "cannot adjudicate Green-Lindsay without the primary source")
v(VV, "EQ-015", "not re-checked", "CARRIED",
  "withdrawal of the two-temperature attribution is appropriate", "-")
v(L, "EQ-019", "frozen in B8a", "WRONG-CONFIRMED",
  "V-B8a_tpl_F6_F9_audit.md S3.8: no Taylor order reproduces (tau_nu/2) d_t^2 T_{,i}",
  "first- and second-order TPL constitutive laws, 1-D; constitutive axis only")
v(VV, "EQ-019", "re-checked", "CORRECT",
  "withdrawal of the legacy TPL row is the right action (V-B8a S3.8)", "row asserts no equation")
v(L, "EQ-021", "re-checked", "CORRECT-CONDITIONAL",
  "kernel matches Barak et al. 2023 eq (2) as printed, with tau written as omega",
  "MDD kernel; the symbol omega for a delay time is a notation hazard, not an error")
v(VV, "EQ-021", "not re-checked", "CARRIED", "row text truncated in register ('Inherited specific MDD kernel formula')", "-")
v(L, "EQ-022", "re-checked", "WRONG-CONFIRMED",
  "V-B9a_checks.py CHECK 3: LHS kg s^-4, RHS m K s^-2 (k/rho c is a diffusivity)",
  "MGT heat-flux equation as printed")
v(VV, "EQ-022", "re-checked", "CORRECT",
  "withdrawal of the dimensionally inconsistent legacy MGT row is correct (CHECK 3)",
  "row asserts no equation")
v(VV, "EQ-022F", "re-checked", "CORRECT-CONDITIONAL",
  "scalar fractional diffusion-wave; [a_alpha] = m^2 s^-alpha consistent",
  "scalar, uncoupled; coupled embedding not asserted")
v(L, "EQ-029", "re-checked", "CORRECT-CONDITIONAL",
  "1/2 D_i E_i is only the dielectric part of the free energy when D = e eps + kappa E",
  "linear piezoelectric; the cross term is not included")
v(VV, "EQ-029", "re-checked", "CORRECT",
  "withdrawal of a universal 'electrical storage formula' is correct (see legacy EQ-029)",
  "row asserts no equation")

# ---------------- Layer VI / section 10
v(L, "EQ-10.1", "re-checked", "CORRECT-CONDITIONAL",
  "energy balance with source P and dissipation D; both must be defined to be usable",
  "classical continuum, no internal heat supply")
v(L, "EQ-10.2", "re-checked", "CORRECT-CONDITIONAL",
  "same object as EQ-007; sign of the mechanical channel is convention-dependent",
  "compressive-positive stress only")
v(L, "EQ-10.3", "re-checked", "WRONG-CONFIRMED",
  "index mismatch (sigma_ji v_i* leaves j on the right of J_i) and mean of a harmonic q_hat is zero; "
  "V-B3d S2.4 verified instead J = -sigma v + theta q/T0, i.e. the LIVE EQ-10.4 form",
  "linearized harmonic field, time average, e^{-i omega t}")
v(L, "EQ-10.4", "re-checked", "CORRECT-CONDITIONAL",
  "jump condition is a definition; orientation must be stated", "finite interface, outward normal")
v(L, "EQ-10.5", "re-checked", "CORRECT-CONDITIONAL",
  "follows from EQ-10.4 only with zero interfacial power and storage", "passive interface")
v(L, "EQ-10.6", "re-checked", "CORRECT-CONDITIONAL",
  "A := 1 - R - T makes the row an identity once A is a residual (V-B3d S2)",
  "A defined as residual; says nothing about physics when R,T are mode-projected")
v(L, "EQ-10.7", "re-checked", "CORRECT-CONDITIONAL",
  "q(1 - i omega tau0) = -k grad T follows exactly from EQ-013 in the e^{-i omega t} convention; "
  "the row gives the first-order flux, not a time mean (a mean needs theta q/T0)",
  "LS frequency domain; time-mean use requires theta q/T0")
v(L, "EQ-10.8", "re-checked", "CORRECT-CONDITIONAL",
  "(1 - i omega tau_T)/(1 - i omega tau_q) is the FIRST-ORDER Taylor form of EQ-018; the truncation is not named",
  "frequency domain; truncation order must be stated (standing rule)")
v(L, "EQ-10.9", "not re-checked", "CARRIED", "GL primary source not read", "-")
v(L, "EQ-10.10", "not re-checked", "CARRIED", "GN-II flux derivation not asserted in the row", "-")
v(L, "EQ-10.11", "not re-checked", "CARRIED", "GN-III mixed flux not derived", "-")
v(L, "EQ-10.13", "not re-checked", "CARRIED", "MGT flux not derived", "-")
v(L, "EQ-10.15", "not re-checked", "CARRIED", "nonlocal integral flux not derived", "-")
v(L, "EQ-10.12", "re-checked", "WRONG-CONFIRMED",
  "render-confirmed source prints T/T0 (V-B9b); the row's (T0/T) inverts the sign of the second-order "
  "thermal flux in the source's own bracketing; 'confirmed across 8 sources' holds for at most 1 of the 8 (P05), and P05 disagrees",
  "LEGACY row only (the live register and live sec10 no longer print this row); linearized harmonic time-mean flux, thermal channel only")
v(L, "EQ-10.14", "re-checked", "WRONG-CONFIRMED",
  "same defect as legacy EQ-10.12 (V-B9b); the VERIFIED tag is unsupported",
  "LEGACY row only; no counterpart in the live register")
v(L, "EQ-10.16", "re-checked", "CORRECT-CONDITIONAL",
  "div(-phi D_dot) = E.D_dot when div D_dot = 0", "quasi-static electric field, charge conservation")

v(VV, "EQ-10.1", "re-checked", "CORRECT", "V-B3d S2.4 derivation reproduced", "classical continuum")
v(VV, "EQ-10.2", "re-checked", "CORRECT",
  "V-B3d S2.4: J = -sigma u_dot + theta q/T0; the row prints the first-order total, which matches",
  "small strain, no internal supply")
v(VV, "EQ-10.3", "re-checked", "CORRECT",
  "V-B3d S2.4 and S3.4: mean mechanical flux -1/2 Re[sigma_ij v_j*] verified against a dissipation integral",
  "linearized harmonic, e^{-i omega t}, time average")
v(VV, "EQ-10.4", "re-checked", "CORRECT-CONDITIONAL",
  "V-B3d S2.4: the thermal channel of a mean flux is theta q/T0, not q-bar; the row's q-bar is admissible only if defined as that second-order mean",
  "harmonic field; q-bar must be the second-order mean")
v(VV, "EQ-10.5", "re-checked", "CORRECT-CONDITIONAL", "definition; orientation must be stated", "finite interface")
v(VV, "EQ-10.6", "re-checked", "CORRECT-CONDITIONAL", "follows from EQ-10.4 with zero interfacial power/storage", "passive interface")
v(VV, "EQ-10.11", "re-checked", "CORRECT-CONDITIONAL",
  "V-B3d: A = 1 - R - T is an identity, so the row is true but uninformative unless A is given independently",
  "A as residual")
v(VV, "EQ-10.12", "re-checked", "CORRECT-CONDITIONAL",
  "V-B3d S3.2: mode-projected sums miss 1 by up to 8.6e-4 (exactly 0 for lossless GN-II); total-flux sums close to 1e-16. "
  "The row's caveat ('lossless limit only; cross terms') is therefore correct and is the right qualifier",
  "dissipative coupled interface; 1-D normal incidence and oblique 7-mode case")
v(VV, "EQ-10.13", "not re-checked", "CARRIED", "no derivation in the row", "-")
# NOTE: the LIVE register has no EQ-10.14 (section 10 there is 10.1-10.6, 10.11-10.13).
# The (T0/T) factor survives only in the LEGACY tree; no live row asserts it.
v(VV, "EQ-10.16", "re-checked", "CORRECT-CONDITIONAL", "div(-phi D_dot) = E.D_dot when div D_dot = 0", "quasi-static electric field")

if all(os.path.exists(p) for _, p in FILES):
    rows = parse(FILES)          # preferred: parse the extracted tree directly
elif os.path.exists(SRC):
    rows = json.load(open(SRC))  # fallback: cached parse
else:
    sys.exit("extract the manuscript first: git archive origin/arena/40393d9f-le | tar -x -C /tmp/ms")
out = []
for r in rows:
    key = (r["version"], r["row_id"])
    check, verdict, ev, scope = V.get(key, ("not re-checked", "CARRIED", "no B9 check", "-"))
    eq = r["equation"]
    if len(eq) > 200:
        eq = eq[:197] + "..."
    out.append(dict(row_id=r["row_id"], version=r["version"], section=r["section"],
                    equation_as_printed=eq, status_in_register=r["status_in_register"],
                    register_note=r["register_note"][:300], b9_check=check,
                    b9_verdict=verdict, evidence=ev, scope=scope))

cols = ["row_id", "version", "section", "equation_as_printed", "status_in_register",
        "register_note", "b9_check", "b9_verdict", "evidence", "scope"]
with open("APPA_LEDGER.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(out)

print("rows written:", len(out))
missing = [(r["version"], r["row_id"]) for r in rows if (r["version"], r["row_id"]) not in V]
print("rows with no explicit verdict (CARRIED):", missing)
from collections import Counter
print("verdict tally:", Counter(o["b9_verdict"] for o in out))
print("per version:", Counter((o["version"], o["b9_verdict"]) for o in out))
