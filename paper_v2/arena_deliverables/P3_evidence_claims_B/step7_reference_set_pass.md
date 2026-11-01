# Step 7 - the reference set the author supplied: what each file is, and what it settled

Written 2026-11-01. This pass had one job: take the nineteen PDFs the author supplied, identify every
one of them from its own first page, and use them to settle the claims that had been left at
`SOURCE NOT AVAILABLE`. Everything below was read on the printed page; nothing is inferred. The files
were read outside the repository and are not committed.

## 1. What the nineteen files are

Each row is what the file itself says on its first article page - title, journal, pagination, DOI where
one is printed. All nineteen carry a text layer, so the pages were read as text, not guessed from the
filename.

| file | the work it actually is | printed evidence |
|---|---|---|
| `10.1016@j.ijheatmasstransfer.2016.06.019.pdf` | Chirita, D'Apice and Zampoli, "The time differential three-phase-lag heat conduction model: Thermodynamic compatibility and continuous dependence", Int. J. Heat Mass Transfer (2016), 7 pp. | title and abstract, p. 1 |
| `10.1080@01495739.2017.1397494.pdf` | **Stan Chirita alone**, "High-order approximations of three-phase-lag heat conduction model: Some qualitative results", J. Thermal Stresses (2017), DOI 10.1080/01495739.2017.1397494 | cover citation, p. 1; abstract p. 2 |
| `zener1937.pdf` | Zener, "Internal Friction in Solids I. Theory of Internal Friction in Reeds", Phys. Rev. 52, 230 (1937), 6 pp. | volume/year line, p. 230 |
| `mindlin1962.pdf` | Mindlin and Tiersten, "Effects of Couple-stresses in Linear Elasticity", Arch. Rat. Mech. Anal. 11, from p. 415, 34 pp. | title page and contents, p. 415 |
| `eringen1983.pdf` | Eringen, "On differential equations of nonlocal elasticity and solutions of screw dislocation and surface waves", J. Appl. Phys. 54, 4703, DOI 10.1063/1.332803 | citation line, p. 4703 |
| `chandrasekharaiah1996.pdf` | Chandrasekharaiah, "A Uniqueness Theorem in the Theory of Thermoelasticity Without Energy Dissipation", J. Thermal Stresses 19:3, 267-272, DOI 10.1080/01495739608946173 | cover citation, p. 1 |
| `chen1974.pdf` | Chen and Nunziato, "Thermodynamic Restrictions on the Relaxation Functions of the Theory of Heat Conduction with Finite Wave Speeds", ZAMP 25 (1974), 8 pp. | title and author line, p. 1 |
| `povstenko2004.pdf` | Povstenko, "Fractional Heat Conduction Equation and Associated Thermal Stress", J. Thermal Stresses 28:1, 83-102, DOI 10.1080/014957390523741 | cover citation, p. 1 |
| `povstenko2007.pdf` | Povstenko, "Fundamental Solutions to Central Symmetric Problems for Fractional Heat Conduction Equation and Associated Thermal Stresses", 23 pp. | abstract, p. 2 |
| `povstenko2009.pdf` | Povstenko, "Thermoelasticity that uses Fractional Heat Conduction Equation", J. Mathematical Sciences 162(2), 2009 - a survey, paginated from p. 297 | journal header, p. 297 |
| `prasad2020.pdf` | Prasad and Kumar, "On the characterization and stability of plane waves under hyperbolic two-temperature generalized thermoelasticity", J. Thermal Stresses (2020), DOI 10.1080/01495739.2020.1806764 | cover citation, p. 1 |
| `moore1960.pdf` | Moore and Gibson, "Propagation of Weak Disturbances in a Gas Subject to Relaxation Effects" | title page, introduction p. 1 |
| `antaki2000.pdf` | Antaki, technical note in J. Thermophysics and Heat Transfer 14(2), 2000, from p. 277 - the DPL ignition time | running head, p. 277 |
| `quintanilla2002.pdf` | Quintanilla, "Exponential stability in the dual-phase-lag heat conduction theory", J. Non-Equilibrium Thermodynamics 27, 217-227 | p. 218 |
| `quintanilla2006.pdf` | Quintanilla and Racke, the note on stability in dual-phase-lag heat conduction | Section 1, p. 1 |
| `quintanilla2008.pdf` | **Quintanilla, "End effects in three-phase-lag heat conduction", Applicable Analysis: An International Journal 87:8, 943-955, DOI 10.1080/00036810802428938** | cover citation, p. 1 |
| `quintanilla2009.pdf` | Quintanilla, "A Well-Posed Problem for the Three-Dual-Phase-Lag Heat Conduction", J. Thermal Stresses 32:12, 1270-1278, DOI 10.1080/01495730903310599 | cover citation, p. 1 |
| `rukolaine2014.pdf` | Rukolaine, "Unphysical effects of the dual-phase-lag model of heat conduction" | Section 1, p. 2 |
| `marchand2012.pdf` | Marchand, McDevitt and Triggiani, abstract semigroup approach to the third-order MGT equation, DOI 10.1002/mma.1576 | description of results, p. 2 |

The twentieth source on the list, Tzou (1997), *Macro- to Microscale Heat Transfer: The Lagging
Behavior*, is **not** in the set. Its online preview shows no readable body page, so it stays unread
and unquoted.

## 2. The reversal that had to be made

Step 5 concluded that Quintanilla (2008), "End effects in three-phase-lag heat conduction", could not
be obtained, because the only file of that name in the library folder is the Quintanilla-Racke note on
stability. **That conclusion is withdrawn.** The supplied set contains the paper itself, and its first
page prints the citation line quoted above. Read on pp. 943-944 it studies the spatial evolution of
solutions in a semi-infinite cylinder, obtains a Phragmen-Lindelof alternative for null initial data, an
upper bound on the amplitude term in terms of the boundary data, and shows the decay is controlled by
the exponential of a second-degree polynomial in the distance from the finite end. End effects, exactly
as the manuscript says. **CR019 is SUPPORTED at R3.**

The old observation survives in a narrower form, and is worth keeping: the *library* copy of
`quintanilla2008.pdf` really is the Quintanilla-Racke note. Two different files carry the same name, and
the library one must still not be cited for the end-effects sentence.

## 3. Where the evidence now stands

Deliverable: `../P3_evidence_claims_C/claim_check_C_batch_007.csv`, 32 rows, CC-0032 to CC-0063.

* **SUPPORTED at R3 (15 rows):** CR004, CR005, CR008, CR019, CR021, CR022, CR025, CR041, CR042, CR057,
  CR058, CR084, CR155, CR185, CR190.
* **PARTLY SUPPORTED (15 rows):** CR007, CR024, CR035, CR040, CR063, CR064, CR065, CR115, CR116, CR129,
  CR130, CR138, CR140, CR141, CR183.
* **NOT SUPPORTED (2 rows):** CR134, CR200.

That makes the C series 63 rows in seven batches: SUPPORTED 35, PARTLY SUPPORTED 23, NOT SUPPORTED 3,
SOURCE NOT AVAILABLE 2 (CR044 Sherief, which was not in the set, and CR210).

Seven claim-check-B rows were carried by the same files and were upgraded with them: CB-0082, CB-0084,
CB-0089, CB-0242, CB-0253, CB-0282 to SUPPORTED at R3; CB-0112 to NOT SUPPORTED (see item 6).

And the list of sources still owed by the author is now **one row**: `pdfs_needed_from_author.csv` holds
Tzou1997 only.

## 4. Details that are verified but narrower than the manuscript's wording

* **CR140/CR141 (Zener 1937).** The paper does derive thermoelastic internal friction for a *vibrating
  reed*, from thermodynamics alone, with a single relaxation time `p'` for temperature equalisation
  across the reed, isothermal and adiabatic limits on either side, and a `Q^-1` maximum at `omega = p'`
  (p. 234). It does **not** treat a plane compressional wave, and the `h^2/(pi^2 alpha)` display (its
  Eq. (12)) is set as an image and did not survive extraction, so that formula and the relaxation
  strength are not quoted.
* **CR183 (Eringen 1983).** The abstract (p. 4703) states the reduction of the integro-partial
  differential equations to singular partial differential equations for admissible kernels - the step
  that produces the differential form. The exact rendering `(1 - xi^2 nabla^2) sigma_ij = C_ijkl eps_kl`
  was not legible in this file.
* **CR138 (Chandrasekharaiah 1996).** The paper formulates the initial-boundary-value problem in stress
  and entropy flux and proves uniqueness, but it does not present "energy identities" as its starting
  point; the phrase does not occur. CR155, the plain uniqueness-for-type-II claim, is fully supported.
* **CR024 (Moore-Gibson 1960).** The acoustics-with-relaxation setting is the paper's own; the name
  "Moore-Gibson-Thompson" and the third-order abstract form come from the later literature, not from
  this source.
* **CR035 (Prasad 2020).** One generalised conduction law is coupled to the two-temperature theory; the
  paper does not compare Lord-Shulman with Green-Naghdi, so "with LS or GN heat laws" is wider than the
  source.
* **CR063/CR064/CR065 (Povstenko).** The three papers establish the time-fractional heat-conduction
  variant and its thermal stresses. None treats a lag equation with fractional orders: "dual-phase-lag"
  does not occur anywhere in their text.

## 5. Two claims the sources do not carry - the author should look at these

1. **CR134** - "For DPL and TPL (first-order truncations) an energy functional exists but its
   construction is more involved (Quintanilla 2003; Chirita 2016)." Chirita, D'Apice and Zampoli (2016)
   construct no energy functional: the seven pages contain no occurrence of "functional" or "entropy".
   The claim may still be carried by Quintanilla 2003, which is verified elsewhere in this audit; it is
   not carried by the Chirita paper as cited.
   **Suggested fix:** drop Chirita2016 from this sentence, or cite where the functional is actually
   constructed.

2. **CR200** - "The one-dimensional piezoelectric bar in the quasi-electrostatic approximation follows
   Yang (2018) and Mindlin and Tiersten (1962)." Mindlin and Tiersten 1962 is couple-stress elasticity
   with no electric field: "piezoelectric" does not occur in any of its 34 pages. The same wrong
   attribution sits in B row **CB-0112**, which is now recorded as NOT SUPPORTED.
   **Suggested fix:** delete MindlinTiersten1962 from that sentence; Yang 2018 alone carries it.

## 6. A bibliographic mismatch the author must resolve

The register key **Chirita2017** is cited as "Chirita, Ciarletta and Tibullo (2017), Int. J. Heat Mass
Transfer". The file supplied under that key is **single-author**: Stan Chirita, "High-order
approximations of three-phase-lag heat conduction model: Some qualitative results", *Journal of Thermal
Stresses* 2017, DOI 10.1080/01495739.2017.1397494. The content is close (restrictions that make the
high-order approximations well posed, uniqueness, continuous dependence), which is why CR116 and CR130
are recorded as PARTLY SUPPORTED rather than closed; but the author list and the journal in the
bibliography do not match the file. Either the bibliography entry or the supplied file is the wrong one,
and only the author can say which 2017 Chirita paper is meant.

## 7. Housekeeping

* The nineteen files entered `library_available_sources.csv` (34 rows now) with their claim ids.
* `library_inventory_v3.csv` is unchanged: it inventories the library folder, and these files are not in
  it. They are accounted for here and in the available-sources list instead.
* No `.tex` file was touched. No PDF, zip or Drive identifier is stored in this repository.
* Checkers after the pass: `check_claim_check_C.py` PASS (7 batches, 63 rows), `check_claim_check_B.py`
  PASS (667 rows, 18 batches), `check_pdfs_needed.py` PASS (needed=1, library=34, findings=3),
  `check_library_inventory_v3.py` PASS (unchanged).
