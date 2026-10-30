import csv

LEDGER = "/home/user/le/phase5/reports/OPEN_CLAIMS_LEDGER.csv"

# ---- 1. Read all rows ----
with open(LEDGER, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = [r for r in reader]

print("header:", header)
print("existing rows:", len(rows))

# Index by id
by_id = {r[0]: r for r in rows}

# ---- 2. Mark OCL-576, OCL-577, OCL-579 as superseded ----
supersede_map = {
    "OCL-576": "OCL-596",
    "OCL-577": "OCL-597",
    "OCL-579": "OCL-598",
}
for old_id, new_id in supersede_map.items():
    r = by_id[old_id]
    # what_was_changed is index 5
    r[5] = (r[5] or "").rstrip() + " [SUPERSEDED by " + new_id + "; corrected source anchor applied]"
    print("superseded:", old_id, "->", new_id)

# ---- 3. New rows (class A anchors and class B hedges) ----
# (id, section, tex_file:line, old_text_short, class, what_was_changed, needed_source, resolved_by, evidence_mode)
# NOTE: Class A rows must carry the source anchor in resolved_by (col index 7).
new_rows = [
    ("OCL-596", "Section 7 (nonlocal integral law)", "phase5/master/sections/sec07_nonlocal.tex:20",
     "Nonlocal stress as kernel average of local stress", "A",
     "Corrected anchor: Eringen (1999) Microcontinuum Field Theories prints the integral nonlocal law as Eq.~(4.2) on p.~430; manuscript matches up to symbol names. Replaces Eringen 1972 (3.2)-(3.3) p.427-428 anchor.", "Eringen1999 p.430 (4.2)", "", "PRIMARY-SOURCE"),
    ("OCL-597", "Section 7 (differential form)", "phase5/master/sections/sec07_nonlocal.tex:32",
     "Differential Helmholtz form (1 - xi^2 nabla^2) sigma = sigma_local", "A",
     "Corrected attribution: the differential Helmholtz form is printed in Aifantis (2003) Eq.~(2.1) with pair (2.2) on p.~263, not in the held Eringen nonlocal papers; with c1=0, c2=ell^2 it reduces to the strain-gradient law. Aifantis (1992) p.~1282 notes stress-gradient terms then unexplored.", "Aifantis2003 p.263 (2.1)-(2.2)", "", "PRIMARY-SOURCE"),
    ("OCL-598", "Section 11 (fractional Cattaneo)", "phase5/master/sections/sec11_advanced.tex:57",
     "Fractional Cattaneo flux law q_i + zeta CD^alpha q_i = -k T_,i", "A",
     "Retracted notation-mapping hedge: source (29) p.101 prints q + zeta D^alpha q = -k grad T restricted to 0<alpha<=1; the manuscript matches after the identity symbol map (zeta->zeta, alpha->alpha); no Gamma-normalization conversion asserted.", "Povstenko2011Cattaneo (29) p.101", "", "PRIMARY-SOURCE"),
    ("OCL-599", "Section 11 (strain-gradient law)", "phase5/master/sections/sec11_advanced.tex:75",
     "Strain-gradient law sigma_ij = C_ijkl eps_kl - ell^2 C_ijkl laplacian(eps_kl)", "A",
     "Anchored to Aifantis (2003) Eq.~(2.1) p.~263; Aifantis treats gradient coefficients as phenomenological, not derived.", "Aifantis2003 p.263 (2.1)", "", "PRIMARY-SOURCE"),
    ("OCL-600", "Section 11 (two-temperature relation)", "phase5/master/sections/sec11_advanced.tex:102",
     "Two-temperature relation T* = T - delta^2 laplacian T", "B",
     "Source exists: Ezzat & El Karamany (2011) p.~940 Eq.~(15) writes the conductive-thermodynamic temperature difference as a coefficient times the Laplacian of the CONDUCTIVE temperature with a plus sign; the manuscript uses the thermodynamic temperature with a minus sign; they agree only to first order. Confirmed difference; hedge both anchors.", "Ezzat2011 p.940 (15)", "", "PRIMARY-SOURCE"),
    ("OCL-601", "Section 11 (couple-stress balance)", "phase5/master/sections/sec11_advanced.tex:84",
     "Couple-stress/angular-momentum balance sigma_[ij] + mu_ij,j = 0", "B",
     "Source-unavailable: the held Mindlin (1965) copy is a second-gradient theory and does not print this couple-stress balance; retained as standard couple-stress/micropolar form (Mindlin & Tiersten 1962; Eringen micropolar), not page-verified here.", "", "SOURCE-UNAVAILABLE", "NOT-SOURCED"),
    ("OCL-602", "Section 11 (fractional heat equation hereditary form)", "phase5/master/sections/sec11_advanced.tex:40",
     "Hereditary integral form of the fractional heat equation", "B",
     "Anchored to Povstenko (A.1) with Caputo definition (A.5), p.~112; for orders up to two an extra initial-rate term appears, so the order range must be stated with the display. Kept hedged class B.", "Povstenko p.112 (A.1)+(A.5)", "", "PRIMARY-SOURCE"),
    ("OCL-603", "Section 5 (piezothermoelastic stress law)", "phase5/master/sections/sec05_multiphysics.tex:65",
     "Piezothermoelastic constitutive stress sigma_ij = c_ijkl eps_kl - e_kij E_k - beta_ij T", "A",
     "Page-checked anchor: Yang (2018) p.~211 Eq.~(7.25) prints the same stress structure and signs.", "Yang2018 p.211 (7.25)", "", "PRIMARY-SOURCE"),
    ("OCL-604", "Section 5 (electric displacement law)", "phase5/master/sections/sec05_multiphysics.tex:77",
     "Electric displacement D_i = kappa_ij E_j + e_ikl eps_kl + p_i T", "A",
     "Page-checked anchor: Yang (2018) p.~211 Eq.~(7.25) prints the same structure; symbol cautions: source uses epsilon for permittivity (manuscript kappa) and lambda_i for pyroelectric vector (manuscript p_i).", "Yang2018 p.211 (7.25)", "", "PRIMARY-SOURCE"),
    ("OCL-605", "Section 6 (LS/Cattaneo Laplace multiplier)", "phase5/master/sections/sec06_transport.tex:39",
     "LS/Cattaneo Laplace multiplier D_LS(s) = 1 + tau_0 s", "A",
     "Page-checked anchor: Ezzat (2011) p.~940 Eq.~(12) gives the Cattaneo law whose zero-initial-flux Laplace form is this multiplier; the source's full heat equation (13) carries an extra relaxation-weighted source term.", "Ezzat2011 p.940 (12)", "", "PRIMARY-SOURCE"),
    ("OCL-606", "Section 6 (MDD operator definition)", "phase5/master/sections/sec06_transport.tex:97",
     "MDD operator D_omega_M f(t) = (1/omega_M) integral K_MDD f'", "A",
     "Page-checked anchor: Wang & Li (2011) Def.~2.1 Eq.~(5) p.~1563 and Eq.~(7) p.~1564 give the finite-horizon operator and its unit-kernel limit.", "Wang2011 p.1563 Def.2.1(5) + p.1564 (7)", "", "PRIMARY-SOURCE"),
    ("OCL-607", "Section 9 (mechanical interface conditions)", "phase5/master/sections/sec09_interfaces.tex:46",
     "Mechanical interface conditions u_i^(1)=u_i^(2), sigma_i3^(1)=sigma_i3^(2) at x3=0", "A",
     "Page-checked anchor: Yang (2018) p.~38 Eq.~(1.225) prints continuity of displacement and traction vector; manuscript restricts to x3 tractions, correct only for flat interface x3=0 with no in-plane variation.", "Yang2018 p.38 (1.225)", "", "PRIMARY-SOURCE"),
    ("OCL-608", "Section 9 (electrical interface conditions)", "phase5/master/sections/sec09_interfaces.tex:68",
     "Electrical interface conditions phi^(1)=phi^(2), D_3^(1)=D_3^(2) at x3=0", "A",
     "Page-checked anchor: Yang (2018) p.~39 Eq.~(1.230) prints potential continuity plus normal-displacement jump equal to free surface charge; zero-charge case used here.", "Yang2018 p.39 (1.230)", "", "PRIMARY-SOURCE"),
    ("OCL-609", "Section 3 (internal energy balance)", "phase5/master/sections/sec03_foundations.tex:157",
     "Internal energy balance rho edot = sigma_ij edot_ij - q_i,i + rho r", "A",
     "Page-checked anchor: Ezzat (2011) p.~940 Eq.~(11) prints this energy balance (and its source-free case r=0), credited there to Biot, in the linearised isotropic case.", "Ezzat2011 p.940 (11)", "", "PRIMARY-SOURCE"),
    ("OCL-610", "Section 3 (source-free energy balance)", "phase5/master/sections/sec03_foundations.tex:164",
     "Source-free internal energy balance rho edot = sigma_ij edot_ij - q_i,i", "A",
     "Page-checked anchor: Ezzat (2011) p.~940 Eq.~(11) source-free case (r=0); tied to the source-free window since the heat-supply term is order one in applications.", "Ezzat2011 p.940 (11)", "", "PRIMARY-SOURCE"),
    ("OCL-611", "Section 3 (Helmholtz free energy)", "phase5/master/sections/sec03_foundations.tex:230",
     "Helmholtz free energy psi = ... quadratic elastic/coupling/temperature-squared terms", "A",
     "Page-checked anchor: Yang (2018) p.~210 Eq.~(7.24) prints the quadratic free energy with elastic term, thermoelastic coupling term with minus sign, and temperature-squared term tied to specific heat; manuscript drops the piezoelectric terms.", "Yang2018 p.210 (7.24)", "", "PRIMARY-SOURCE"),
]

fields = ["ledger_row_id","section","tex_file:line","old_text_short","class",
          "what_was_changed","needed_source","resolved_by","evidence_mode"]
max_id = max(r[0] for r in rows)
print("current max id:", max_id)

out_rows = []
for r in rows:
    out_rows.append(r)
for nr in new_rows:
    nr = list(nr)
    # Class A: source anchor belongs in resolved_by (index 7); needed_source stays empty.
    nr[6], nr[7] = nr[7], nr[6]
    out_rows.append(nr)

# ---- 4. Write back with consistent LF endings ----
with open(LEDGER, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(out_rows)

print("wrote", len(out_rows), "total rows (header +", len(out_rows)-1, "data)")
print("new rows appended:", len(new_rows))
