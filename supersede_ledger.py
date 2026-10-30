#!/usr/bin/env python3
# FIX-3 ledger: supersede OCL-596, 597, 599, 600, 602, 612 (unverifiable page
# anchors) with corrective class-B "not checked here" rows OCL-614..OCL-619.
import csv, io

path = "phase5/reports/OPEN_CLAIMS_LEDGER.csv"
raw = io.open(path, encoding="utf-8", newline="").read()
# detect dialect
rows = list(csv.reader(io.StringIO(raw)))
header = rows[0]
data = rows[1:]
ncol = len(header)
print("columns:", header)
print("data rows:", len(data))

def find(rid):
    for i, r in enumerate(data):
        if r and r[0] == rid:
            return i
    return None

# (old_rid, new_rid, new_row_fields)
supersede = [
    ("OCL-596", "OCL-614",
     ["OCL-614", "Section 7 (nonlocal integral law)", "phase5/master/sections/sec07_nonlocal.tex:20",
      "Nonlocal stress as kernel average of local stress", "B",
      "Corrected: page/equation anchor withdrawn. Eringen (1999) Microcontinuum Field Theories integral nonlocal law cited without page/equation verification (source page not checked here); manuscript form matches up to symbol names. Class B, not checked here.",
      "", "Ezzat2011 / Eringen1999 not page-checked", "NOT-SOURCED"]),
    ("OCL-597", "OCL-615",
     ["OCL-615", "Section 7 (differential form)", "phase5/master/sections/sec07_nonlocal.tex:32",
      "Differential Helmholtz form (1 - xi^2 nabla^2) sigma = sigma_local", "B",
      "Corrected: page/equation anchor withdrawn. Aifantis (2003) differential Helmholtz form cited without page/equation verification (source page not checked here); Eringen (1983) developed the differential form. Class B, not checked here.",
      "", "Aifantis2003 not page-checked", "NOT-SOURCED"]),
    ("OCL-599", "OCL-616",
     ["OCL-616", "Section 11 (strain-gradient law)", "phase5/master/sections/sec11_advanced.tex:76",
      "Strain-gradient law sigma_ij = C_ijkl eps_kl - ell^2 C_ijkl laplacian(eps_kl)", "B",
      "Corrected: page/equation anchor withdrawn. Aifantis (2003) strain-gradient law cited without page/equation verification (source page not checked here); Aifantis treats gradient coefficients as phenomenological. Class B, not checked here.",
      "", "Aifantis2003 not page-checked", "NOT-SOURCED"]),
    ("OCL-600", "OCL-617",
     ["OCL-617", "Section 11 (two-temperature relation)", "phase5/master/sections/sec11_advanced.tex:103",
      "Two-temperature relation T* = T - delta^2 laplacian T", "B",
      "Corrected: page/equation anchor withdrawn. Ezzat & El Karamany (2011) two-temperature relation cited without page verification (source page not checked here); manuscript T* = T - delta^2 grad^2 T stated as model definition, class B. Withdraws OCL-600/OCL-612 confirmed-difference/class-A stance.",
      "", "Ezzat2011 not page-checked", "NOT-SOURCED"]),
    ("OCL-602", "OCL-618",
     ["OCL-618", "Section 11 (fractional heat equation hereditary form)", "phase5/master/sections/sec11_advanced.tex:40",
      "Hereditary integral form of the fractional heat equation", "B",
      "Corrected: page/equation anchor withdrawn. Povstenko appendix Caputo definition (A.5) cited without page verification (source page not checked here); treated as definitional. Class B, not checked here.",
      "", "Povstenko2011 not page-checked", "NOT-SOURCED"]),
    ("OCL-612", "OCL-619",
     ["OCL-619", "Section 11 (two-temperature relation class A)", "phase5/master/sections/sec11_advanced.tex:103",
      "Two-temperature relation T* = T - delta^2 laplacian T (class A)", "B",
      "Corrected: class A anchor withdrawn. Ezzat & El Karamany (2011) p.~940 Eq.(15) class A claim retracted; source page not checked here. eq:11.7 class B, not checked here. Supersedes OCL-612.",
      "", "Ezzat2011 not page-checked", "NOT-SOURCED"]),
]

for old_rid, new_rid, new_row in supersede:
    i = find(old_rid)
    assert i is not None, f"{old_rid} not found"
    # mark old row superseded in what_was_changed (col index 5)
    data[i][5] = (data[i][5] + f" SUPERSEDED by {new_rid}: page anchor withdrawn; replaced by corrective row {new_rid} (class B, source page not checked here).").strip()
    assert data[i][0] == old_rid
    # insert new row right after the old row
    data.insert(i + 1, new_row)
    print(f"superseded {old_rid} -> {new_rid}")

# sanity: column count of new rows
for new_rid, new_row in [(nr[1], nr[2]) for nr in supersede]:
    assert len(new_row) == ncol, f"{new_rid} has {len(new_row)} cols, expected {ncol}"

out = io.StringIO()
w = csv.writer(out)
w.writerow(header)
w.writerows(data)
io.open(path, "w", encoding="utf-8", newline="").write(out.getvalue())
print("TOTAL data rows now:", len(data))
print("LEDGER UPDATED")
