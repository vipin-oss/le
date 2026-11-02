#!/usr/bin/env python3
"""Build REVIEW_SCOPE_BRIEF_2026-11-02.pdf — a short brief on the theories and the
materials covered by the review paper.

Every number printed here is copied from the paper's own section and table files
(paper_v2/overleaf_package.zip): tab:param and tab:final (§3, §16), tab:materials (§3),
tab:aniso (§8), tab:scenarios (§30), plus the gate counts in the paper README.
Nothing is added and nothing is re-derived.

    python3 make_brief_pdf.py
"""
import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "REVIEW_SCOPE_BRIEF_2026-11-02.pdf")

FDIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Body", os.path.join(FDIR, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("BodyB", os.path.join(FDIR, "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Head", os.path.join(FDIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("HeadB", os.path.join(FDIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Mono", os.path.join(FDIR, "DejaVuSansMono.ttf")))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="BodyB", italic="Body", boldItalic="BodyB")

INK = colors.HexColor("#1a1a1a")
ACC = colors.HexColor("#0b4f7a")
GREY = colors.HexColor("#555555")
RULE = colors.HexColor("#b8c4cc")
BAND = colors.HexColor("#eef3f7")

S = dict(
    title=ParagraphStyle("t", fontName="HeadB", fontSize=19, leading=23, textColor=INK, spaceAfter=2),
    sub=ParagraphStyle("s", fontName="Head", fontSize=11.5, leading=15, textColor=ACC, spaceAfter=8),
    meta=ParagraphStyle("m", fontName="Body", fontSize=8.4, leading=12, textColor=GREY),
    h1=ParagraphStyle("h1", fontName="HeadB", fontSize=12.6, leading=15, textColor=ACC,
                      spaceBefore=11, spaceAfter=4, keepWithNext=1),
    h2=ParagraphStyle("h2", fontName="HeadB", fontSize=9.8, leading=12, textColor=INK,
                      spaceBefore=8, spaceAfter=2, keepWithNext=1),
    p=ParagraphStyle("p", fontName="Body", fontSize=8.9, leading=12.9, textColor=INK,
                     alignment=TA_JUSTIFY, spaceAfter=4.5),
    small=ParagraphStyle("sm", fontName="Body", fontSize=7.7, leading=10.4, textColor=GREY,
                         alignment=TA_JUSTIFY, spaceAfter=3),
    bullet=ParagraphStyle("b", fontName="Body", fontSize=8.7, leading=12.4, textColor=INK,
                          leftIndent=9, bulletIndent=1, spaceAfter=2.4, alignment=TA_JUSTIFY),
    cap=ParagraphStyle("c", fontName="Head", fontSize=7.6, leading=9.6, textColor=GREY, spaceBefore=2),
    tbl=ParagraphStyle("tb", fontName="Body", fontSize=7.0, leading=8.9, textColor=INK),
    tblh=ParagraphStyle("th", fontName="HeadB", fontSize=7.0, leading=8.9, textColor=colors.white),
    mono=ParagraphStyle("mo", fontName="Mono", fontSize=7.6, leading=10.5, textColor=INK,
                        alignment=1, spaceBefore=3, spaceAfter=3),
)

FLOW = []


def h1(t):
    FLOW.append(Paragraph(t, S["h1"]))


def h2(t):
    FLOW.append(Paragraph(t, S["h2"]))


def p(t):
    FLOW.append(Paragraph(t, S["p"]))


def small(t):
    FLOW.append(Paragraph(t, S["small"]))


def bullets(items):
    for it in items:
        FLOW.append(Paragraph(it, S["bullet"], bulletText="\u2022"))


def table(rows, widths, caption, head=True, align=None, size=None, keep=True):
    data = []
    for i, r in enumerate(rows):
        if size:
            style = ParagraphStyle("tbc", parent=S["tblh" if (head and i == 0) else "tbl"],
                                   fontSize=size, leading=size * 1.28)
        else:
            style = S["tblh"] if (head and i == 0) else S["tbl"]
        data.append([c if isinstance(c, Paragraph) else Paragraph(str(c), style) for c in r])
    t = Table(data, colWidths=[w * cm for w in widths], repeatRows=1 if head else 0)
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3.2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3.2),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
    ]
    if head:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), ACC)]
        for i in range(2, len(data), 2):
            cmds.append(("BACKGROUND", (0, i), (-1, i), BAND))
    else:
        for i in range(1, len(data), 2):
            cmds.append(("BACKGROUND", (0, i), (-1, i), BAND))
    if align:
        for col, a in align.items():
            cmds.append(("ALIGN", (col, 0), (col, -1), a))
    t.setStyle(TableStyle(cmds))
    cap = Paragraph(caption, S["cap"])
    if keep:
        FLOW.append(KeepTogether([t, Spacer(1, 2), cap, Spacer(1, 5)]))
    else:
        FLOW.append(t)
        FLOW.append(Spacer(1, 2))
        FLOW.append(cap)
        FLOW.append(Spacer(1, 5))


def rule():
    FLOW.append(Spacer(1, 3))
    FLOW.append(Table([[""]], colWidths=[17 * cm], rowHeights=[1.2],
                      style=TableStyle([("LINEABOVE", (0, 0), (-1, -1), 0.8, ACC)])))
    FLOW.append(Spacer(1, 6))


# ---------------------------------------------------------------- front matter
FLOW.append(Paragraph("Waves in Thermoelastic and Multiphysics Continua", S["title"]))
FLOW.append(Paragraph("Scope brief: the theories and the materials the review covers", S["sub"]))
FLOW.append(Paragraph(
    "164 pages &nbsp;·&nbsp; 38 numbered sections &nbsp;·&nbsp; 90 numbered equations &nbsp;·&nbsp; "
    "25 tables &nbsp;·&nbsp; 40 figures &nbsp;·&nbsp; 337 references &nbsp;·&nbsp; "
    "compiled 2 November 2026", S["meta"]))
rule()

p("This brief says what the review contains, in two parts: which heat-conduction and continuum "
  "theories it treats, and which materials it puts numbers on. Every figure printed here is copied "
  "from the paper's own tables — the parameter table of §3, the materials table of §3, the "
  "comparative tables of §33, the anisotropy table of §14 and the regime table of §30 — so the brief "
  "adds no claim, no reference and no number of its own. Where the paper labels a value as a rounded "
  "handbook number for illustration, this brief says so too.")

h1("1. The organising idea: one template, not a list of theories")
p("The literature presents generalized thermoelasticity one theory at a time, and the labels hide "
  "what actually differs between two papers. The review starts instead from a single heat-flux "
  "function with two conductivities and three lags:")
FLOW.append(Paragraph("G(s) = [ k (1 + τ_T s) + k* (1 + τ_v s)/s ] / (1 + τ_q s),   s = −iω", S["mono"]))
p("Set the parameters and the familiar theories appear: Fourier (Biot) at k* = τ_q = τ_T = τ_v = 0, "
  "Cattaneo/Lord–Shulman at τ_q = τ_0, dual-phase-lag with τ_q and τ_T, three-phase-lag when k* is "
  "kept, the Moore–Gibson–Thompson flux form with its third order in time, and the Green–Naghdi "
  "types as the limits k → 0 (type II) and lags → 0 with k* ≠ 0 (type III). Two theories are "
  "deliberately left outside the template, because they change structure rather than a parameter: "
  "Green–Lindsay, which modifies the coupling with two relaxation times, and Guyer–Krumhansl, which "
  "comes from phonon kinetics and carries a length scale.")
p("Coupling the template to momentum balance gives one dispersion polynomial in K = k², checked "
  "symbolically. From that single polynomial the review reads phase speed, attenuation and "
  "thermoelastic damping for every member of the family, and then carries the same machinery into "
  "transient, surface, interface, size-effect and multiphysics problems. The exact delay, fractional "
  "powers and memory kernels are treated where they make the dispersion relation transcendental or "
  "multivalued; every quantitative figure in the paper is produced by an accompanying script.")

# ---------------------------------------------------------------- theories
h1("2. Heat-conduction theories covered")
p("The first block are the members of the template; the second block are the models that leave it and "
  "are handled on their own terms. The last column follows the review's own criterion for a rational "
  "heat law: sG(s) must tend to a finite non-zero limit as s → ∞.")
table([
    ["Theory", "Position in the template", "Free parameters", "Finite thermal front"],
    ["Classical (Fourier, Biot)", "k* = 0, all lags zero", "—", "no"],
    ["Lord–Shulman (Cattaneo)", "τ_q = τ_0, k* = 0", "τ_0", "yes, c_T = √(k/ρcτ_0)"],
    ["Dual-phase-lag, first order in τ_q", "τ_q, τ_T kept", "τ_q, τ_T", "no (strictly diffusive)"],
    ["Dual-phase-lag, second order in τ_q", "same law, expanded to O(τ_q²)", "τ_q, τ_T",
     "depends; stable only if τ_T ≥ τ_q/2"],
    ["Three-phase-lag", "k, k*, τ_q, τ_T, τ_v", "four", "no (strictly diffusive)"],
    ["Moore–Gibson–Thompson (flux form)", "k, k*, τ_q", "2–3", "yes: c_* low, c_T high frequency"],
    ["Green–Naghdi II", "k = 0, k* > 0", "k*", "yes: c_* = √(k*/ρc), non-dispersive"],
    ["Green–Naghdi III", "k, k* kept, no lags", "k, k*", "no (strictly diffusive)"],
    ["Green–Lindsay", "outside: modifies the coupling", "τ_0, τ_1", "yes"],
    ["Exact delay (untruncated)", "outside: G = k·e^(−τ_q s)", "τ_q",
     "yes, exact front (G not rational)"],
    ["Caputo-fractional", "outside: order α in time", "α and a lag", "depends on α"],
    ["Memory-dependent derivative", "outside: kernel K(t − s)", "1–3", "variant-dependent"],
    ["Guyer–Krumhansl (kinetic)", "outside: phonon hydrodynamics", "l (mean free path), τ_R, τ_N", "yes (second sound)"],
], [4.3, 4.4, 2.5, 5.8], keep=False,
    caption="Table 1. Heat-conduction theories and their place in the review's template (paper §3, the "
    "parameter table; §33, the comparative table). Thresholds are the paper's: for a rational G, a finite front needs sG(s) → const ≠ 0 as s → ∞.")
p("Three results in this part carry the weight. First, the widely repeated dual-phase-lag stability "
  "condition τ_T ≥ τ_q/2 belongs to the second-order Taylor truncation, not to the first-order "
  "template, which is stable for every τ_T > 0; the review locates the condition and shows what it "
  "does and does not protect. Second, the reductions are checked symbolically and the review records "
  "which are regular and which are singular: dual-phase-lag to Lord–Shulman needs τ_T → 0 at fixed "
  "τ_q, not τ_q → 0, and fractional order α → 2 is the wave equation, not Fourier's law. Third, "
  "Taylor truncation of the delay is a modelling choice with a measurable error, so the truncated "
  "laws are compared against the exact delay G = k·e^(−τ_q s), with relative error ≈ (ωτ)²/4 at "
  "small ωτ.")

h2("2.1 Elastic and continuum enrichments (size effects)")
bullets([
    "Eringen nonlocal elasticity in both forms used in the literature — the stress smoothed by the "
    "nonlocal operator and the thermal stress left local, and the form where the coupling is "
    "smoothed too; the review shows that the two give different damping near the elastic cut-off.",
    "Strain-gradient elasticity, with the opposite sign of dispersion to nonlocal elasticity: a "
    "positive gradient coefficient stiffens the short waves, whereas the lattice softens.",
    "Couple-stress and micropolar continua, Klein–Gordon type enrichment, and Kelvin–Voigt "
    "viscoelasticity, each used in the recent thermoelastic literature.",
    "Nonlocality in the heat flux as well as in the stress, and the caveat that the nonlocal length "
    "ξ must be calibrated against a stated target (zone boundary or long wavelength), since the two "
    "calibrations do not agree.",
])

h2("2.2 Coupled fields")
p("Four added fields are developed to the point where they can be solved, not merely listed:")
bullets([
    "Piezoelectricity and thermopiezoelectricity: bulk stiffening, the exact renormalisation of the "
    "thermoelastic dispersion relation by the electric field, pyroelectric sign conventions, and "
    "Bleustein–Gulyaev shear-horizontal surface waves on a hexagonal (6mm) crystal with metallised "
    "and free electrical boundary conditions.",
    "Magneto-thermoelasticity: the magnetic field enters as a stiffness contribution at all "
    "frequencies.",
    "Thermoelastic diffusion and chemical coupling.",
    "Microstructure — micropolar, voids and porosity — and the two-temperature and "
    "semiconductor/photothermal variants treated in the taxonomy.",
])

h2("2.3 Wave problems worked out")
table([
    ["Problem", "What the review reports"],
    ["Bulk plane waves in the template family", "dispersion polynomial roots, phase speed and attenuation "
     "for each member, branches tracked by continuity"],
    ["Anisotropy (cubic crystals)", "coupling of quasi-longitudinal waves along [100] and [111]; for "
     "copper the coupling itself differs by 41 % between the two directions"],
    ["Reflection at a thermoelastic free surface", "amplitude and energy coefficients, elastic limit "
     "recovered to 10⁻¹⁰"],
    ["Thermoelastic Rayleigh waves", "speed shift ≈ 2×10⁻³ at low wavenumber for ε = 0.05, ν = 0.3; "
     "damping peak Q⁻¹ ≈ 2×10⁻³ at k c₁/ω_* ≈ 0.4; Lord–Shulman changes the damping by less than "
     "1 % at low k and up to ≈ 12 % at high k"],
    ["Thermoelastic Lamb waves in a plate", "6×6 determinant; elastic limit and the "
     "Lifshitz–Roukes flexural loss recovered with ratio 1.000 for small kh"],
    ["Clamped-bar modes", "modal loss of a bar against the exact Fourier solution"],
    ["Interfaces and energy partition", "when the mode-wise energy ratios sum to one and when they do "
     "not; net heat-flux continuity as the correct bookkeeping"],
    ["Layered media", "Love, Stoneley and Scholte-type waves; classical closed forms used as benchmarks"],
    ["Transients", "heat pulse in a half-space (Fourier versus Cattaneo, exact front) and thermal "
     "shock of a coupled half-space, with the boundary conditions satisfied to machine precision"],
    ["Thermal-wave resonance", "resonances of a finite rod and the Cattaneo mode transition at "
     "k_c = 1/(2√(χτ))"],
    ["Flexural thermoelastic damping", "Zener relaxation and the exact Lifshitz–Roukes result, with the "
     "plane-strain factor (1 + ν)/(1 − ν)"],
], [4.6, 12.4], keep=False,
    caption="Table 2. The wave and damping problems solved in the review (sections 13–26). The quoted values "
    "are the ones printed in those sections; all are computed from rounded handbook inputs.")

# ---------------------------------------------------------------- materials
h1("3. Materials covered")
p("Only five materials carry computed numbers, and the paper labels those numbers as handbook-type "
  "values at 300 K, to be replaced by data for the specimen at hand:")
table([
    ["Material", "c₁ (m/s)", "ε (coupling)", "f_* = ω_*/2π (Hz)", "α = k/ρc (m²/s)"],
    ["Aluminium", "6198", "0.027", "6.3 × 10¹⁰", "9.8 × 10⁻⁵"],
    ["Copper", "4540", "0.019", "2.8 × 10¹⁰", "1.2 × 10⁻⁴"],
    ["Silicon", "8854", "0.00056", "1.4 × 10¹¹", "9.2 × 10⁻⁵"],
    ["Steel (carbon)", "5778", "0.0097", "4.1 × 10¹¹", "1.3 × 10⁻⁵"],
    ["Fused silica", "5972", "7.2 × 10⁻⁶", "6.6 × 10¹²", "8.6 × 10⁻⁷"],
], [3.2, 2.2, 2.2, 3.6, 3.4],
    "Table 3. Thermoelastic coupling and characteristic frequency for the five materials used in the "
    "calculations (paper §3, materials table; rounded handbook-type values at 300 K).",
    align={1: "RIGHT", 2: "RIGHT", 3: "RIGHT", 4: "RIGHT"})

p("Copper, aluminium and silicon are then treated as cubic crystals, where the coupling is "
  "direction-dependent:")
table([
    ["Crystal", "ε along [100]", "speed shift [100]", "ε along [111]", "speed shift [111]", "ratio"],
    ["Cu", "0.0238", "1.18 %", "0.0169", "0.84 %", "1.41"],
    ["Al", "0.0325", "1.61 %", "0.0306", "1.52 %", "1.06"],
    ["Si", "6.5 × 10⁻⁴", "0.032 %", "5.3 × 10⁻⁴", "0.026 %", "1.23"],
], [2.0, 2.9, 3.0, 2.9, 3.0, 1.6],
    "Table 4. Direction dependence of thermoelastic coupling for quasi-longitudinal waves (paper §14; "
    "300 K, rounded handbook inputs).",
    align={1: "RIGHT", 2: "RIGHT", 3: "RIGHT", 4: "RIGHT", 5: "RIGHT"})

h2("3.1 Materials discussed without computed numbers")
p("The evidence and applications sections name further materials, deliberately without new numbers, "
  "because the point there is what the experiment shows rather than a prediction:")
bullets([
    "Solid helium and sodium fluoride — the classical second-sound observations, in narrow "
    "temperature windows where momentum-conserving phonon collisions dominate.",
    "Graphite — second sound above 100 K, the one case where a hydrodynamic phonon window is claimed "
    "at high temperature; the review quotes the source's fitted speed at 85 K (≈ 3200 m/s against "
    "3650 m/s from ab initio) and records that no error bar is given.",
    "Hexagonal 6mm piezoelectric crystals — the Bleustein–Gulyaev surface wave, with electromechanical "
    "coupling K² = e₁₅²/(c₄₄ε).",
    "Layered and bonded pairs — substrate–film, electrode–crystal, welded metal–metal, treated through "
    "impedance ratios rather than named materials.",
    "Saturated and partially saturated porous solids, and biological tissue — the latter described "
    "through the Pennes bioheat baseline and the disputed reports of relaxation times of order seconds.",
    "Water-like media, used only to show that ω_* ≈ 10¹³ rad/s lies far above any frequency of "
    "interest for tissue.",
])

# ---------------------------------------------------------------- regimes
h1("4. Which theory for which material and frequency")
p("This is the practical answer the review gives, and it is decided by two dimensionless groups: "
  "ωτ_q, which measures how far the frequency is from the flux lag, and ω/ω_*, which measures how far "
  "it is from the heat-carrier relaxation. Six scenarios are evaluated with τ_q = 1 ps:")
table([
    ["Scenario", "Material", "f (Hz)", "ω/ω_*", "ωτ_q", "δ_T (m)", "λ (m)", "Assessment"],
    ["Ultrasonic testing", "Aluminium", "1.0 × 10⁷", "1.6 × 10⁻⁴", "6.3 × 10⁻⁵",
     "1.8 × 10⁻⁶", "6.2 × 10⁻⁴", "Fourier adequate"],
    ["GHz acoustics", "Aluminium", "1.0 × 10⁹", "1.6 × 10⁻²", "6.3 × 10⁻³",
     "1.8 × 10⁻⁷", "6.2 × 10⁻⁶", "Fourier adequate"],
    ["Picosecond ultrasonics", "Aluminium", "1.0 × 10¹¹", "1.6", "6.3 × 10⁻¹",
     "1.8 × 10⁻⁸", "6.2 × 10⁻⁸", "lag may matter; check kinetics"],
    ["Silicon beam, h = 1 μm, at f_Z", "Silicon", "1.4 × 10⁸", "1.1 × 10⁻³", "9.1 × 10⁻⁴",
     "4.5 × 10⁻⁷", "6.1 × 10⁻⁵", "Fourier adequate"],
    ["Silicon film, h = 20 nm, at f_Z", "Silicon", "3.6 × 10¹¹", "2.7", "2.3",
     "9.0 × 10⁻⁹", "2.5 × 10⁻⁸", "continuum law questionable"],
    ["Copper film, h = 50 nm, at f_Z", "Copper", "7.3 × 10¹⁰", "2.6", "4.6 × 10⁻¹",
     "2.3 × 10⁻⁸", "6.2 × 10⁻⁸", "lag may matter; check kinetics"],
], [3.35, 1.95, 1.8, 1.55, 1.5, 1.6, 1.6, 3.65], size=6.7, keep=False,
    caption="Table 5. Dimensionless groups for six representative scenarios at T₀ = 300 K and τ_q = 1 ps "
    "(paper §30, regime table; the table is generated by the paper's own script from the rounded handbook "
    "inputs). δ_T is the thermal penetration depth, λ the acoustic wavelength.",
    align={2: "RIGHT", 3: "RIGHT", 4: "RIGHT", 5: "RIGHT", 6: "RIGHT"})

h2("4.1 The decision rule as stated in the paper")
bullets([
    "Fourier is adequate when ωτ_q &lt; 0.1 and ω/ω_* &lt; 0.1; in that corner the classical coupled "
    "theory is the baseline for essentially every ultrasonic, above-micron device and geophysical "
    "application.",
    "A lag law may matter when ωτ_q &lt; 1.5, but then the kinetic validity of the continuum model "
    "has to be checked at the same time, because the same corner of the map is where carrier mean "
    "free paths rival the wavelength.",
    "Beyond that, the continuum heat law itself is questionable: at 20–50 nm films the first "
    "deviation from Fourier is size-related, not lag-related, and the Guyer–Krumhansl or nonlocal "
    "description is the appropriate next model because it carries a length scale.",
    "Electromechanical and magnetic couplings change stiffness at all frequencies, so they matter "
    "even where the heat law does not.",
])

# ---------------------------------------------------------------- map
h1("5. Map of the paper")
table([
    ["Part", "Sections", "Content"],
    ["Foundations", "§1–§5", "introduction; historical development; balance laws, thermodynamics, "
     "the template and its admissibility tests; kinetic origin of the hyperbolic laws"],
    ["Heat laws", "§6–§12", "classical coupled theory; Lord–Shulman, Green–Lindsay, Green–Naghdi; "
     "dual-, three-phase-lag and MGT; fidelity of the Taylor truncations; fractional and "
     "memory-dependent models; causality and Kramers–Kronig relations"],
    ["Waves", "§13–§18", "three-dimensional propagation; cubic anisotropy; free-surface reflection; "
     "transients and thermal shock; thermal-wave resonance; Rayleigh waves"],
    ["Structure and size", "§19–§26", "Lamb waves and bar modes; flexural damping (Zener and "
     "Lifshitz–Roukes); interfaces and energy partition; layered Love/Stoneley/Scholte waves; "
     "nonlocal and gradient size effects; piezoelectric, magnetic, diffusive and microstructural "
     "couplings; Bleustein–Gulyaev waves"],
    ["Practice", "§27–§32", "solution methods and verification; a finite-difference benchmark for "
     "hyperbolic heat conduction; applications from laser ultrasonics to resonators and tissue; "
     "regime table; worked examples; what the experiments actually identify"],
    ["Synthesis and apparatus", "§33–§38, Appendices A–H", "comparative synthesis, decision guide, "
     "pitfalls checklist; taxonomy of the field; atlas of problems from other groups; reporting "
     "standards; open problems; balance-law and dispersion derivations; glossaries; per-equation and "
     "benchmark registers; the classified reference catalogue"],
], [3.2, 2.6, 11.2],
    "Table 6. Structure of the review, using the paper's own section numbers.")

# ---------------------------------------------------------------- limits
h1("6. What the brief and the paper do not claim")
bullets([
    "No new experiment is reported. Every result is analytical or numerical, and the review says so "
    "where the evidence is thin.",
    "The material numbers are rounded handbook-type inputs for illustration, at 300 K, not "
    "measurements of a named specimen.",
    "Code verification is not physical validation: the benchmarks test that an implementation "
    "reproduces an exact or independently computed reference to a stated tolerance, and the paper "
    "states explicitly what a pass does not establish.",
    "Of the works cited, 103 are recorded as SOURCE NOT AVAILABLE in the paper's claim register: "
    "nothing is described from them, and no claim rests on them.",
    "The atlas of problems is a first instalment limited to papers read in full text, not a "
    "representative sample of the field.",
])

h1("Provenance of the numbers in this brief")
table([
    ["Content here", "Taken from"],
    ["Template, parameter assignments, finite-front criterion", "§3, §33 (comparative table), §8"],
    ["Materials table, coupling and characteristic frequency", "§3"],
    ["Cubic anisotropy of coupling", "§14"],
    ["Six scenarios and their assessment", "§30, §33.5 (decision guide)"],
    ["Rayleigh and Lamb numbers quoted in Table 2", "§18, §19"],
    ["Page, section, equation, table, figure and reference counts", "the paper's build and gate log"],
], [8.6, 8.4],
    "Every item is a file in the review package; none is from memory.")


# ---------------------------------------------------------------- document
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Head", 6.8)
    canvas.setFillColor(GREY)
    canvas.drawString(2 * cm, 1.15 * cm,
                      "Scope brief — Waves in Thermoelastic and Multiphysics Continua")
    canvas.drawRightString(A4[0] - 2 * cm, 1.15 * cm, "page %d" % doc.page)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(2 * cm, 1.45 * cm, A4[0] - 2 * cm, 1.45 * cm)
    canvas.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=1.7 * cm, bottomMargin=1.9 * cm,
                      title="Scope brief: theories and materials in the review",
                      author="Vipin Gupta", subject="Review paper scope")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=footer)])
doc.build(FLOW)
print("wrote %s (%.0f kB)" % (OUT, os.path.getsize(OUT) / 1024.0))
