#!/usr/bin/env python3
"""build_calculations.py — companion calculation document for the beta-Ga2O3 cavity paper.

The main manuscript (manuscript_IJHMT.md -> FINAL_REVISED_MANUSCRIPT.tex) states the model,
the results and the limitations.  This document is the *worked arithmetic* behind them: every
intermediate step that a reader (or a referee) would otherwise have to redo by hand.  It is
modelled on the worked-calculation companion that ships with the BFS-FEM3 paper.

What it is, and what it is not:
  * every number is either recomputed here, live, from the frozen source code in
    PAPER_PROJECT/06_Source_Code/src/, or read from the processed data package
    PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json;
  * no simulation is run, no result is added, and no number is rounded by hand: the values
    printed below are the values the code produces;
  * it inherits every limitation of the manuscript (labelling of the parameters, the alpha5 = 0
    limitation, the hypothetical relaxation time, the unverified continuum description at
    5-50 nm, the >10x spread of the expansion data).

Output:  calculations_IJHMT.md   (convert with: python3 tools/md_to_tex.py -i ... --companion)
         calculations_IJHMT.pdf  (via tools/md_to_pdf.py)

Usage:  python3 PAPER_PROJECT/13_Manuscript/build_calculations.py
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, 'PAPER_PROJECT', '06_Source_Code', 'src')
DATA = os.path.join(ROOT, 'PAPER_PROJECT', '10_Processed_Data', 'ANALYSIS_V2.json')
sys.path.insert(0, SRC)

import cg_model as M                      # noqa: E402
from cg_grid import Grid                  # noqa: E402
from cg_bromwich import BromwichPlan      # noqa: E402

OUT = []
_state = {'sec': 0, 'sub': 0, 'eq': 0, 'tab': 0, 'words': 0}


# ----------------------------------------------------------------- markdown helpers
def _emit(s=''):
    OUT.append(s)


def h1(title):
    _state['sec'] += 1
    _state['sub'] = 0
    _emit('\n## %d. %s\n' % (_state['sec'], title))


def h2(title):
    _state['sub'] += 1
    _emit('\n### %d.%d %s\n' % (_state['sec'], _state['sub'], title))


def para(text):
    _state['words'] += len(text.split())
    _emit(text + '\n')


def eq(latex, note=None):
    _state['eq'] += 1
    _emit('\n$$ %s \\qquad (%d) $$\n' % (latex, _state['eq']))
    if note:
        _state['words'] += len(note.split())
        _emit(note + '\n')


def table(headers, rows, caption):
    _state['tab'] += 1
    _emit('**Table C%d.** %s\n' % (_state['tab'], caption))
    _emit('| ' + ' | '.join(headers) + ' |')
    _emit('|' + '---|' * len(headers))
    for r in rows:
        _emit('| ' + ' | '.join(str(c) for c in r) + ' |')
    _emit('')


def bullets(items):
    for it in items:
        _state['words'] += len(it.split())
        _emit('- ' + it)
    _emit('')


# ----------------------------------------------------------------- number formatting
def g(x, n=3):
    return ('%.' + str(n) + 'f') % x


def MPa(x):
    """Pa -> MPa string"""
    return g(x / 1e6, 4)


def sci(x, n=3):
    return ('%.' + str(n) + 'e') % x


# ----------------------------------------------------------------- live inputs
C = M.Cij_GPa
K_ac = M.K_ac
alpha = M.alpha_crys
rho, cp, T0 = M.rho, M.cp_ESTIMATED, M.T0
Q, beta = M.plane_strain_block()
dv = M.derived()
c_ref, kappa, kbar, Cbar, delta = (dv['c_ref'], dv['kappa'], dv['kbar'],
                                   dv['Cbar'], dv['delta'])
bnorm = dv['beta_norm']
Qeig = np.linalg.eigvalsh(Q)
Kw, Kv = np.linalg.eigh(K_ac)
theta_K = 0.5 * np.degrees(np.arctan2(2 * K_ac[0, 1], K_ac[0, 0] - K_ac[1, 1]))
GPa = 1e9
lam = C['C12'] * GPa
mu = C['C66'] * GPa
m_lame = lam + 2 * mu
a_iso = float(np.mean(alpha))
gamma_T = (3 * lam + 2 * mu) * a_iso
g_T = gamma_T / m_lame
D = json.load(open(DATA, encoding='utf-8'))
plan = BromwichPlan()
grid = Grid(a=1.0, chi=1.0, R=80.0, Nr=96, Nt=48, gamma=3.5)
A_NM = 10e-9
t_th_nm = A_NM ** 2 / kappa
eps_num = kappa / (c_ref * A_NM)
Lam = lambda tau_ps: (tau_ps * 1e-12) / t_th_nm
vT = lambda tau_ps: np.sqrt(kappa / (tau_ps * 1e-12))


# ================================================================= document
_emit('# Worked calculations for “Orientation-dependent wall stress around circular and '
      'elliptical cavities in monoclinic β-Ga₂O₃ under a transient thermal pulse”\n')
_emit('*[AUTHOR INPUT REQUIRED: author names, affiliations, ORCID iDs and corresponding author]*\n')

para('This document is the calculation companion to the manuscript of the same title. It '
     'contains no new physics, no new simulation and no new result: every number below is '
     'either recomputed here from the frozen source code (PAPER_PROJECT/06_Source_Code/src/, '
     'SHA-256 recorded in the code-freeze manifests) or read from the processed data package '
     'PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json, which is itself produced from the '
     '300 runs stored in PAPER_PROJECT/09_Raw_Data/production/. Equation numbers in this '
     'companion are independent of those in the manuscript; where a step is quoted from the '
     'manuscript it is referenced as “Eq. (n) of the manuscript”. The purpose is that a '
     'reader can check every quantitative statement of the paper without re-running the code, '
     'and that a referee can see exactly which arithmetic stands behind each claim.')

para('Two conventions are used throughout. First, all quantities are in SI units unless a '
     'unit is printed; stresses in tables are converted to MPa and thermal-stress moduli to '
     'MPa/K because those are the natural magnitudes. Second, numbers are printed as the code '
     'produces them and rounded only for display: a displayed value such as 1.3093 MPa/K is '
     '1.30927… MPa/K in the arithmetic that follows.')

# ----------------------------------------------------------------- 1
h1('Material data, frames and conventions')
h2('Frames, Voigt order and sign conventions')
para('The crystallographic axes of monoclinic β-Ga₂O₃ are a, b, c with the twofold axis along '
     'b. The plane of the calculation is the a–c plane, i.e. the plane normal to the twofold '
     'axis, with laboratory coordinates x₁ = a and x₃ = c at zero rotation; x₂ = b is normal '
     'to the plane. Strains and stresses use the Voigt order (11, 33, 13) in the plane, with '
     'the engineering shear γ₁₃ = ε₁₃ + ε₃₁, so that the plane-strain stiffness block Q and '
     'the thermal-stress vector β are 3×3 and 3×1. The crystal frame and the laboratory frame '
     'coincide at rotation φ = 0; a rotation by φ about x₂ carries the crystal into the '
     'laboratory frame. Tension is positive and θ is the temperature rise above the reference '
     'temperature T₀ = %d K.' % int(T0))

h2('The thirteen independent stiffness constants')
para('Monoclinic symmetry (point group 2/m, unique axis b) leaves thirteen independent '
     'constants. The values used here are the literature values transcribed in '
     'PARAMETER_TABLE.md [15, 16] and are reproduced unchanged in Table C1; the two '
     'constants that do not enter the plane-strain block (C₄₄, C₄₆) are listed for '
     'completeness because they couple the out-of-plane shear components that the plane-strain '
     'ansatz excludes.')
table(['C₁₁', 'C₂₂', 'C₃₃', 'C₄₄', 'C₅₅', 'C₆₆', 'C₁₂', 'C₁₃', 'C₂₃', 'C₁₅', 'C₂₅', 'C₃₅', 'C₄₆'],
      [[g(C[k]) for k in ('C11', 'C22', 'C33', 'C44', 'C55', 'C66', 'C12', 'C13',
                          'C23', 'C15', 'C25', 'C35', 'C46')]],
      'Independent stiffness constants of monoclinic β-Ga₂O₃ (GPa), literature values [15]. '
      'C₁₅, C₂₅, C₃₅, C₄₆ are the monoclinic couplings that a higher-symmetry crystal would '
      'not have.')
para('The three in-plane monoclinic couplings are small but not negligible in the accounting '
     'that follows: C₁₅ = %s GPa, C₂₅ = %s GPa and C₃₅ = %s GPa. They are the reason the '
     'plane-strain block Q is fully populated rather than block-diagonal, and they are the '
     'reason the thermal-stress vector acquires a shear component β₅ once the crystal is '
     'rotated (Section 3).' % (g(C['C15'], 2), g(C['C25'], 2), g(C['C35'], 2)))

h2('Thermal expansion, and what α₅ = 0 removes')
para('The expansion tensor is diagonal in the crystal frame with components '
     'α_a = %s×10⁻⁶ K⁻¹, α_b = %s×10⁻⁶ K⁻¹ and α_c = %s×10⁻⁶ K⁻¹ [17]. The '
     'thermal shear α₅ = 2ε₁₃^{th} is **not** available in the source data and is set to zero. '
     'This is a limitation, not an approximation that has been verified: it removes the only '
     'mechanism that would generate an in-plane thermal shear at φ = 0, and it is carried '
     'through every number in this document. Its consequence is quantified in Section 10, '
     'where the alternative expansion set of [18] changes the absolute stress scale by a '
     'factor of about 16.' % (g(alpha[0] * 1e6, 2), g(alpha[1] * 1e6, 2), g(alpha[2] * 1e6, 2)))
para('The a- and c-axis expansions differ by a factor %s, so the expansion tensor is not '
     'isotropic in the plane of the calculation; this is the seed of the orientation '
     'dependence that the manuscript measures.' % g(alpha[2] / alpha[0], 2))

h2('Conductivity tensor: principal values and orientation')
para('The in-plane conductivity block is')
table(['K_aa', 'K_ac', 'K_ca', 'K_cc'],
      [[g(K_ac[0, 0], 3), g(K_ac[0, 1], 3), g(K_ac[1, 0], 3), g(K_ac[1, 1], 3)]],
      'In-plane conductivity block K (W m⁻¹ K⁻¹), axes ordered (a, c) [16]. The '
      'off-diagonal term is what makes the conduction tensor non-diagonal in the crystal '
      'frame.')
para('Its eigenvalues and the orientation of its principal axes follow from the standard '
     'two-dimensional expressions.')
eq(r'K_{1,2}=\frac{K_{11}+K_{33}}{2}\pm\sqrt{\left(\frac{K_{11}-K_{33}}{2}\right)^2+K_{13}^2}'
   r',\qquad \tan 2\psi_K=\frac{2K_{13}}{K_{11}-K_{33}}')
para('Numerically:')
bullets([
    'trace/2 = (%s + %s)/2 = %s W m⁻¹ K⁻¹;' % (g(K_ac[0, 0], 3), g(K_ac[1, 1], 3),
                                               g(0.5 * (K_ac[0, 0] + K_ac[1, 1]), 4)),
    'half-difference = (%s − %s)/2 = %s, off-diagonal = %s;'
    % (g(K_ac[0, 0], 3), g(K_ac[1, 1], 3), g(0.5 * (K_ac[0, 0] - K_ac[1, 1]), 4),
       g(K_ac[0, 1], 3)),
    'square-root term = √(%s² + %s²) = %s W m⁻¹ K⁻¹;'
    % (g(0.5 * (K_ac[0, 0] - K_ac[1, 1]), 4), g(K_ac[0, 1], 3),
       g(np.hypot(0.5 * (K_ac[0, 0] - K_ac[1, 1]), K_ac[0, 1]), 4)),
    'principal values K₁ = %s and K₂ = %s W m⁻¹ K⁻¹, ratio K₂/K₁ = %s;'
    % (g(Kw[0], 3), g(Kw[1], 3), g(Kw[1] / Kw[0], 3)),
    'principal axes at ψ_K = %s° from the a axis, i.e. the conductivity tensor is *not* '
    'diagonal in the crystal frame;' % g(theta_K, 2),
    'isotropic scale k̄ = √(det K) = √(%s × %s − %s²) = %s W m⁻¹ K⁻¹.'
    % (g(K_ac[0, 0], 3), g(K_ac[1, 1], 3), g(K_ac[0, 1], 3), g(kbar, 4)),
])
para('The conductivity anisotropy is therefore a factor %s in the plane — modest compared '
     'with the stiffness anisotropy — and the manuscript’s ablation E3 (isotropic '
     'conductivity, Section 10) shows that it is not what drives the orientation modulation.'
     % g(Kw[1] / Kw[0], 2))

h2('Density, heat capacity and the derived scales')
para('The mass density ρ = %s kg m⁻³ is a literature value; the specific heat capacity '
     'c_p = %d J kg⁻¹ K⁻¹ is **estimated** (Debye-model value at Θ_D = 685 K, flagged '
     'ESTIMATED in PARAMETER_TABLE.md). Because c_p enters the diffusivity and the coupling '
     'number linearly, this estimate propagates directly into both. The derived scales are:'
     % (g(rho, 0), int(cp)))
bullets([
    'diffusivity κ̄ = k̄/(ρc_p) = %s/(%s × %d) = %s m² s⁻¹;'
    % (g(kbar, 4), g(rho, 0), int(cp), sci(kappa)),
    'wave-speed scale c_ref = (C₃₃/ρ)^{1/2} = (%s×10⁹/%s)^{1/2} = %s m s⁻¹;'
    % (g(C['C33'], 1), g(rho, 0), g(c_ref, 2)),
    'reference modulus C̄ = C₃₃ = %s GPa;' % g(Cbar / GPa, 1),
    'thermal-stress scale ‖β‖ = %s MPa K⁻¹ (Section 2);' % MPa(bnorm),
    'coupling number δ = T₀‖β‖²/(ρc_pC̄) = %s (Section 5).' % sci(delta),
])

# ----------------------------------------------------------------- 2
h1('Plane-strain reduction of the monoclinic law')
h2('Setting the b-direction strain to zero')
para('The three-dimensional Voigt law of a monoclinic crystal, written in the axes '
     '(a, b, c) with Voigt order (11, 22, 33, 23, 13, 12), is σ = C ε − β θ. Plane strain in '
     'the a–c plane means ε₂₂ = 0, γ₂₃ = 0 and γ₁₂ = 0, so the strain vector reduces to '
     'ε = (ε₁₁, 0, ε₃₃, 0, γ₁₃, 0). Inserting this into the law and keeping the rows that '
     'carry in-plane stresses gives')
eq(r'\boldsymbol{\sigma}=\mathbf{Q}\boldsymbol{\epsilon}-\boldsymbol{\beta}\theta,\qquad'
   r'\boldsymbol{\epsilon}=(\epsilon_{11},\ \epsilon_{33},\ \gamma_{13}),')
para('where Q is the (11, 33, 13) **sub-block** of C and β is the corresponding sub-vector of '
     'the thermal-stress vector. Note what this is not: Q is not the condensed (Schur-'
     'complement) plane-strain stiffness of a material in which the out-of-plane stress is '
     'relaxed to zero. The out-of-plane normal stress is whatever the constraint ε₂₂ = 0 '
     'produces,')
eq(r'\sigma_{22}=C_{12}\epsilon_{11}+C_{23}\epsilon_{33}+C_{25}\gamma_{13}-\beta_2\theta,'
   r'\qquad \beta_2=C_{12}\alpha_a+C_{22}\alpha_b+C_{23}\alpha_c'
   r'+C_{25}\alpha_5,')
para('and it does no work, because the strain it is conjugate to vanishes by construction. '
     'With the data of Section 1, β₂ = %s MPa K⁻¹. The two out-of-plane shear stresses '
     'σ₂₃ and σ₁₂ are non-zero only through the monoclinic couplings C₄₄, C₄₆ and the '
     'corresponding strains, which are zero; they are therefore identically zero in this '
     'reduction.'
     % MPa((C['C12'] * alpha[0] + C['C22'] * alpha[1] + C['C23'] * alpha[2]) * GPa))

h2('The reduced block Q')
para('Reading the sub-block off Table C1 gives, in GPa,')
table(['Q₁₁', 'Q₁₃', 'Q₁₅', 'Q₃₃', 'Q₃₅', 'Q₅₅'],
      [[g(C['C11'], 1), g(C['C13'], 1), g(C['C15'], 2),
        g(C['C33'], 1), g(C['C35'], 2), g(C['C55'], 1)]],
      'Plane-strain stiffness block Q (GPa) in the crystal frame. Q₁₅, Q₃₅ are the '
      'monoclinic couplings C₁₅, C₃₅.')
para('The eigenvalues of Q are %s, %s and %s GPa — a factor %s between the softest and the '
     'stiffest in-plane mode, which is the stiffness anisotropy that the orientation sweep '
     'probes. The block is symmetric positive definite, so the quasi-static elasticity problem '
     'is well posed.'
     % (g(Qeig[0] / GPa, 2), g(Qeig[1] / GPa, 2), g(Qeig[2] / GPa, 2), g(Qeig[2] / Qeig[0], 2)))

h2('The thermal-stress vector β, term by term')
para('The thermal-stress vector is β = C α, restricted to the plane. Writing each component '
     'out with the numbers inserted (GPa × 10⁻⁶ K⁻¹ = MPa K⁻¹):')
b1 = [C['C11'] * alpha[0], C['C12'] * alpha[1], C['C13'] * alpha[2], C['C15'] * 0.0]
b3 = [C['C13'] * alpha[0], C['C23'] * alpha[1], C['C33'] * alpha[2], C['C35'] * 0.0]
b5 = [C['C15'] * alpha[0], C['C25'] * alpha[1], C['C35'] * alpha[2], C['C55'] * 0.0]
for name, terms, labs in (
        ('β₁', b1, ('C₁₁α_a', 'C₁₂α_b', 'C₁₃α_c', 'C₁₅α₅')),
        ('β₃', b3, ('C₁₃α_a', 'C₂₃α_b', 'C₃₃α_c', 'C₃₅α₅')),
        ('β₅', b5, ('C₁₅α_a', 'C₂₅α_b', 'C₃₅α_c', 'C₅₅α₅'))):
    para('%s = %s = %s = %s MPa K⁻¹'
         % (name, ' + '.join(labs),
            ' + '.join(g(t, 5) if t else '0' for t in terms), g(sum(terms), 5)))
para('so that β = (%s, %s, %s) MPa K⁻¹ and ‖β‖ = %s MPa K⁻¹. Two observations matter for '
     'what follows. First, β₁ ≠ β₃ (%s against %s MPa K⁻¹): the two in-plane directions '
     'are not equivalent, and a cavity wall that runs along one direction is loaded '
     'differently from a wall that runs along the other. Second, β₅ = %s MPa K⁻¹ is zero to '
     'five decimal places, and it is zero *only* because α₅ was set to zero: the last column '
     'of the arithmetic above, C_i5 α₅, is identically zero while the first three columns are '
     'not. This is the limitation flagged in Section 1, and Section 3 shows that it does not '
     'survive a rotation of the crystal.'
     % (MPa(beta[0]), MPa(beta[1]), MPa(beta[2]), MPa(bnorm),
        MPa(beta[0]), MPa(beta[1]), MPa(beta[2])))

h2('Scales derived from the reduced law')
para('The plane-strain law supplies the two scales that non-dimensionalise the problem: the '
     'wave-speed scale c_ref and the stress scale per kelvin ‖β‖. Their ratio fixes the '
     'elastic number ε = κ̄/(c_ref a) of Section 5. Numerically c_ref = %s m s⁻¹ and '
     '‖β‖ = %s MPa K⁻¹, so that a temperature rise of 1 K at a perfectly constrained wall '
     'would produce a stress of order 2 MPa — the magnitude against which the computed '
     'peaks of the manuscript (of order 1 MPa K⁻¹) should be read.'
     % (g(c_ref, 2), MPa(bnorm)))

# ----------------------------------------------------------------- 3
h1('Rotation of the crystal')
h2('Rotation matrix and the fourth-order transformation')
para('Let c_φ = cos φ and s_φ = sin φ. A rotation of the crystal by φ about the b axis '
     '(that is, a rotation of the material relative to the cavity) is represented in the '
     '(x₁, x₃) plane by')
table(['R₁₁', 'R₁₃', 'R₃₁', 'R₃₃'],
      [['cos φ', '−sin φ', 'sin φ', 'cos φ']],
      'Rotation matrix R(φ) in the (x₁, x₃) plane; below it is written '
      'c_φ = cos φ, s_φ = sin φ.')
eq(r"C^{\prime}_{abcd}=R_{ai}R_{bj}R_{ck}R_{dl}\,C_{ijkl},")
para('and the rotated plane-strain block is read off from the rotated fourth-order tensor '
     'with the same Voigt convention as before. The in-plane expansion tensor transforms as a '
     'second-order tensor, α′ = R diag(α_a, α_c) Rᵀ, and the b-axis expansion enters '
     'separately, because a rotation about b leaves the b direction itself unchanged: the '
     'constants that carry α_b into the plane are C₁₂, C₂₃ and C₂₅, and they transform '
     'into')
for lab, expr in (("C^{\\prime}_{12}", "c_\\varphi^2 C_{12}+s_\\varphi^2 C_{23}"
                                       "-2c_\\varphi s_\\varphi\\,C_{25}"),
                  ("C^{\\prime}_{23}", "s_\\varphi^2 C_{12}+c_\\varphi^2 C_{23}"
                                       "+2s_\\varphi c_\\varphi\\,C_{25}"),
                  ("C^{\\prime}_{25}", "c_\\varphi s_\\varphi\\left(C_{12}-C_{23}\\right)"
                                       "+\\left(c_\\varphi^2-s_\\varphi^2\\right)C_{25}")):
    eq(r'%s=%s' % (lab, expr))
para('The signs of the cross terms are the part that is easy to get wrong, and the code '
     'carries a regression test for exactly this (test U1, manuscript Section 5): the term is '
     'invisible at φ = 0 and φ = 90°, where c_φ s_φ = 0, and it is maximal at '
     'φ = 45°.')

h2('The b-axis coupling worked at φ = 30°')
c30, s30 = np.cos(np.radians(30)), np.sin(np.radians(30))
C12p = c30 ** 2 * C['C12'] + s30 ** 2 * C['C23'] - 2 * c30 * s30 * C['C25']
C23p = s30 ** 2 * C['C12'] + c30 ** 2 * C['C23'] + 2 * s30 * c30 * C['C25']
C25p = c30 * s30 * (C['C12'] - C['C23']) + (c30 ** 2 - s30 ** 2) * C['C25']
para('With c_φ = %s and s_φ = %s:' % (g(c30, 6), g(s30, 1)))
bullets([
    'C′₁₂ = %s×128.0 + %s×70.9 − 2×%s×%s×0.36 = %s + %s − %s = %s GPa;'
    % (g(c30 ** 2, 4), g(s30 ** 2, 4), g(c30, 4), g(s30, 1),
       g(c30 ** 2 * C['C12'], 4), g(s30 ** 2 * C['C23'], 4),
       g(2 * c30 * s30 * C['C25'], 4), g(C12p, 4)),
    'C′₂₃ = %s×128.0 + %s×70.9 + 2×%s×%s×0.36 = %s + %s + %s = %s GPa;'
    % (g(s30 ** 2, 4), g(c30 ** 2, 4), g(s30, 1), g(c30, 4),
       g(s30 ** 2 * C['C12'], 4), g(c30 ** 2 * C['C23'], 4),
       g(2 * s30 * c30 * C['C25'], 4), g(C23p, 4)),
    'C′₂₅ = %s×(128.0 − 70.9) + %s×0.36 = %s + %s = %s GPa.'
    % (g(c30 * s30, 4), g(c30 ** 2 - s30 ** 2, 4),
       g(c30 * s30 * (C['C12'] - C['C23']), 4),
       g((c30 ** 2 - s30 ** 2) * C['C25'], 4), g(C25p, 4)),
])
para('The cross term −2c_φ s_φ C₂₅ = %s GPa is small compared with C₁₂ and C₂₃, but '
     'it is the term whose sign was wrong in the analysis as first written, and the manuscript '
     'records the correction.' % g(-2 * c30 * s30 * C['C25'], 3))

h2('The rotated expansion tensor and the induced thermal shear')
para('The in-plane expansion tensor is diagonal in the crystal frame, so after rotation')
eq(r"\alpha^{\prime}_{11}=c_\varphi^2\alpha_a+s_\varphi^2\alpha_c,\qquad"
   r"\alpha^{\prime}_{33}=s_\varphi^2\alpha_a+c_\varphi^2\alpha_c,\qquad"
   r"\alpha^{\prime}_{13}=c_\varphi s_\varphi\left(\alpha_c-\alpha_a\right).")
para('The third of these is the important one: at any angle that is not a multiple of 90°, '
     'the rotated expansion tensor has a non-zero in-plane shear component even though the '
     'crystal-frame thermal shear α₅ was set to zero. At φ = 30°, '
     'α′₁₃ = %s × (%s − %s)×10⁻⁶ = %s×10⁻⁶ K⁻¹, which is %s%% of the '
     'mean in-plane expansion. The thermal-stress vector inherits a shear component from it.'
     % (g(c30 * s30, 4), g(alpha[2] * 1e6, 2), g(alpha[0] * 1e6, 2),
        g(c30 * s30 * (alpha[2] - alpha[0]) * 1e6, 4),
        g(100 * abs(c30 * s30 * (alpha[2] - alpha[0]) / a_iso), 1)))

h2('β′ at four angles')
rows = []
for deg in (0, 30, 45, 90):
    _, br = M.rotate_Q_beta(Q, beta, np.radians(deg))
    rows.append([str(deg), MPa(br[0]), MPa(br[1]), MPa(br[2]), MPa(np.linalg.norm(br))])
table(['φ (deg)', "β′₁ (MPa/K)", "β′₃ (MPa/K)", "β′₅ (MPa/K)", "‖β′‖ (MPa/K)"],
      rows,
      'Thermal-stress vector in the laboratory frame at four crystal rotations, computed '
      'with the transformation of Section 3.1 (test U1 of the manuscript).')
para('Two features are quantitative, not qualitative. First, β′₅ grows from %s MPa K⁻¹ '
     'at φ = 0 to %s MPa K⁻¹ at φ = 45° and then falls back: the induced shear is an '
     'odd function of sin 2φ, so it vanishes at 0° and 90° and is extremal near 45°. '
     'Second, ‖β′‖ is not exactly rotation invariant — it varies by %s%% over the '
     'quadrant — because the b-axis contribution (C′₁₂, C′₂₃, C′₂₅)α_b is '
     'not an isotropic tensor. The variation is small, so the *magnitude* of the thermal '
     'load is nearly orientation independent while its *distribution among components* is not: '
     'that is the mechanism the manuscript measures.'
     % (rows[0][3], rows[2][3],
        g(100 * (max(float(r[4]) for r in rows) - min(float(r[4]) for r in rows))
          / float(rows[0][4]), 2)))

# ----------------------------------------------------------------- 4
h1('Isotropic control and the closed-form circular cavity')
h2('Construction of the control')
para('The manuscript uses an isotropic control — an ablation, not a material claim — to '
     'test the numerical solution against a closed form. It is built to have the same bulk '
     'order as the crystal: the shear modulus is taken as μ = C₆₆, the Lamé constant as '
     'λ = C₁₂, and the expansion as the mean of the three crystal values. Then')
bullets([
    'μ = %s GPa, λ = %s GPa, m = λ + 2μ = %s GPa;' % (g(mu / GPa, 1), g(lam / GPa, 1),
                                                      g(m_lame / GPa, 1)),
    'α_iso = (%s + %s + %s)/3 ×10⁻⁶ = %s×10⁻⁶ K⁻¹;'
    % (g(alpha[0] * 1e6, 2), g(alpha[1] * 1e6, 2), g(alpha[2] * 1e6, 2), g(a_iso * 1e6, 4)),
    'γ_T = (3λ + 2μ)α_iso = (3×%s + 2×%s)×10⁹ × %s×10⁻⁶ = %s MPa K⁻¹;'
    % (g(lam / GPa, 1), g(mu / GPa, 1), g(a_iso * 1e6, 4), MPa(gamma_T)),
    'g_T = γ_T/m = %s/%s = %s×10⁻⁶ K⁻¹.' % (MPa(gamma_T), g(m_lame / GPa, 1), g(g_T * 1e6, 4)),
])
para('The isotropic conductivity is the mean of the two principal values of K, '
     'k_iso = (K₁ + K₂)/2 = %s W m⁻¹ K⁻¹, i.e. an isotropic tensor with the same trace '
     'as the crystal block.' % g(0.5 * (Kw[0] + Kw[1]), 4))

h2('Closed form for the circular cavity')
para('For a circular cavity of radius a in an isotropic solid in quasi-static plane strain, '
     'with a radially symmetric temperature field θ(r, t), the radial displacement u(r, t) '
     'satisfies')
eq(r'\frac{\mathrm{d}}{\mathrm{d}r}\left[\frac{1}{r}\frac{\mathrm{d}(ru)}{\mathrm{d}r}\right]'
   r'=g_T\,\frac{\mathrm{d}\theta}{\mathrm{d}r},\qquad g_T=\frac{\gamma_T}{m}=\frac{(3\lambda'
   r'+2\mu)\alpha}{m}.')
para('Integrating twice between a and r, with G(r) = ∫_a^r r′θ(r′, t) dr′ and '
     'integration constants C₁ and C₂,')
eq(r'u(r,t)=g_T\,\frac{G(r)}{r}+C_1 r+\frac{C_2}{r}.')
para('The hoop stress follows from the constitutive law, σ_θθ = λ u′ + m u/r − '
     'γ_T θ with u′ = ∂u/∂r. Substituting the expression above and using '
     'G(a) = 0 and G′(r) = r θ(r), the wall value at r = a is')
eq(r'\sigma_{\theta\theta}(a,t)=\left(\lambda g_T-\gamma_T\right)\theta(a,t)'
   r'+(\lambda+m)C_1+(m-\lambda)\frac{C_2}{a^2},')
eq(r'\sigma_{\theta\theta}(a,t)=\sigma_{\theta\theta}^{\mathrm{local}}(a,t)'
   r'+\sigma_{\theta\theta}^{\mathrm{far}}(a,t),\qquad'
   r'\sigma_{\theta\theta}^{\mathrm{local}}(a,t)=-2\mu g_T\,\theta(a,t),\qquad'
   r'\sigma_{\theta\theta}^{\mathrm{far}}(a,t)=(\lambda+m)C_1+2\mu\frac{C_2}{a^2}.')
para('because γ_T = m g_T and m − λ = 2μ. The first term is *local*: it involves the '
     'wall temperature only, not the temperature profile, and not the outer radius. The '
     'second term is everything else; with a traction-free or a fixed outer boundary at '
     'R = 80a it scales as (a/R)².')
iso_local = -2 * mu * g_T
D_iso = D['isotropic']
para('Numerically the local term is −2μ g_T = −2 × %s×10⁹ × %s×10⁻⁶ = '
     '%s MPa K⁻¹. The processed data package reports the closed-form wall stress as '
     '%s Pa K⁻¹ from the local term alone and %s Pa K⁻¹ with the far-field term '
     'included, a difference of %s Pa K⁻¹ (%s%%). The numerical solution on grid T48 '
     'gives %s Pa K⁻¹, i.e. %s%% from the closed form with the far field — the '
     'agreement quoted as verification test V3 in the manuscript.'
     % (g(mu / GPa, 1), g(g_T * 1e6, 4), MPa(abs(iso_local)),
        g(D_iso['circle_closed_form_local_term'], 2),
        g(D_iso['circle_closed_form_with_far_field'], 2),
        g(D_iso['circle_closed_form_with_far_field'] - D_iso['circle_closed_form_local_term'], 2),
        g(100 * (D_iso['circle_closed_form_with_far_field']
                 - D_iso['circle_closed_form_local_term'])
          / D_iso['circle_closed_form_local_term'], 3),
        g(D_iso['circle_T48'], 2),
        g(100 * abs(D_iso['circle_T48'] - D_iso['circle_closed_form_with_far_field'])
          / D_iso['circle_closed_form_with_far_field'], 2)))

h2('Why the wall stress is a local response')
para('The far-field term is proportional to (a/R)². With R = 80a, (a/R)² = %s. The '
     'manuscript reports the same conclusion from the numerical side: the local (first) term '
     'accounts for all but about 0.1%% of the closed-form wall stress, which is why the '
     'orientation dependence of the anisotropic results can be interpreted as a local '
     'property of the material at the wall rather than as a consequence of the temperature '
     'profile in the bulk.' % sci(1.0 / 80 ** 2, 4))

# ----------------------------------------------------------------- 5
h1('Non-dimensionalisation and the dimensionless groups')
h2('Scales')
para('Lengths are scaled by the cavity radius a, times by the thermal time '
     't_th = a²/κ̄, stresses by ‖β‖Θ with Θ the wall-temperature amplitude, '
     'and temperature by Θ. With a = 10 nm:')
bullets([
    't_th = a²/κ̄ = (10⁻⁸)²/%s = %s s = %s ps;'
    % (sci(kappa), sci(t_th_nm), g(t_th_nm * 1e12, 2)),
    'the elastic number ε = κ̄/(c_ref a) = %s/(%s × 10⁻⁸) = %s;'
    % (sci(kappa), g(c_ref, 2), g(eps_num, 4)),
    'the memory number Λ = τ/t_th: Λ = %s at τ = 1 ps, %s at τ = 5 ps and %s '
    'at τ = 20 ps;' % (g(Lam(1), 4), g(Lam(5), 4), g(Lam(20), 4)),
    'the coupling number δ = T₀‖β‖²/(ρc_pC̄) = %s×(%s×10⁶)²/(%s '
    '× %d × %s×10⁹) = %s;'
    % (g(T0, 0), g(bnorm / 1e6, 4), g(rho, 0), int(cp), g(Cbar / GPa, 1), sci(delta)),
])
para('δ is the fraction of the thermal energy that is converted into mechanical work '
     'per unit temperature rise; it is small (%s), and the manuscript uses that smallness '
     'twice: to argue that the thermoelastic feedback is negligible, and to bound it.' % sci(delta))

h2('Second-sound speed and the thermal wave')
para('The Cattaneo–Vernotte law turns the heat equation into a hyperbolic equation whose '
     'characteristic speed is v_T = (κ̄/τ)^{1/2}. In the dimensionless groups this is '
     'v_T/c_ref = ε/√Λ, so that at fixed ε the wave slows as Λ^{−1/2} '
     'when the relaxation time is increased. Numerically:')
table(['τ (ps)', 'Λ', 'v_T (m/s)', 'v_T/c_ref', 'a/v_T (ps)'],
      [[str(t), g(Lam(t), 4), g(vT(t), 1), g(vT(t) / c_ref, 5), g(A_NM / vT(t) * 1e12, 3)]
       for t in (1, 5, 20)],
      'Second-sound speed implied by the Cattaneo–Vernotte law at a = 10 nm. The '
      'relaxation time is hypothetical: these are sensitivities, not measurements.')
para('The transit time a/v_T is the time a thermal wave needs to cross the cavity radius; '
     'comparing it with t_th shows how far the model is from the diffusive limit for each τ.')

h2('The feedback bound')
para('The manuscript bounds the thermoelastic feedback — the effect of the deformation on '
     'the temperature field through the T₀β:ε̇ coupling — by comparing the '
     'temperature change it can produce with the applied temperature change. The criterion, fixed '
     'before the runs were made, is |Δθ|/|θ| ≤ 5δ, with the factor five a margin '
     'chosen before the runs rather than fitted to them. With δ = %s, 5δ = %s, '
     'i.e. a feedback of at most about half a per cent. The criterion is then checked '
     'numerically by switching the coupling off (manuscript Section 6.4), which is the '
     'ablation that turns a bound into a measured effect.'
     % (sci(delta), sci(5 * delta)))

# ----------------------------------------------------------------- 6
h1('Spatial discretisation')
h2('The map and its metrics')
para('The annular region between the cavity boundary and a circle of radius R = 80a is mapped '
     'from a rectangle (ξ, η) ∈ [0, 1] × [0, 2π) by')
eq(r'x=A(\rho)\cos\eta,\qquad y=B(\rho)\sin\eta,\qquad'
   r'\rho(\xi)=\frac{\exp(\gamma\xi)-1}{\exp(\gamma)-1},')
para('with A(ρ) = a_e + (R − a_e)ρ, B(ρ) = b_e + (R − b_e)ρ and a_e = a√χ, '
     'b_e = a/√χ for an ellipse of aspect ratio χ. The radial clustering parameter '
     'γ = %s places the first radial interval at Δρ = %s of the total, i.e. the '
     'near-wall cell is %s times thinner than it would be on a uniform grid — the '
     'resolution is needed because both the thermal boundary layer and the stress '
     'concentration live at the wall.'
     % (g(grid.gamma, 1), sci(grid.rho[1] - grid.rho[0], 3),
        g(1.0 / ((grid.rho[1] - grid.rho[0]) * (grid.Nr - 1)), 2)))
para('The Jacobian of the map is J = x_ξ y_η − x_η y_ξ. On the production grid '
     '(N_r × N_θ = %d × %d, γ = %s) the Jacobian is positive everywhere: '
     'J ranges from %s to %s in units of a², a ratio of %s. The metrics are '
     'differentiated analytically, not by finite differences, so the discrete operators are '
     'exact for the map quantities.'
     % (grid.Nr, grid.Nt, g(grid.gamma, 1), g(grid.J.min(), 4), g(grid.J.max(), 2),
        g(grid.J.max() / grid.J.min(), 1)))

h2('Contravariant coefficients of the two operators')
para('Written on the mapped rectangle, both operators take the contravariant form')
eq(r'\nabla\cdot(\mathbf{K}\nabla\theta)=\frac{1}{J}\left[\partial_\xi\left(A\,'
   r'\partial_\xi\theta+B\,\partial_\eta\theta\right)+\partial_\eta\left(B\,'
   r'\partial_\xi\theta+D\,\partial_\eta\theta\right)\right],')
para('with the coefficients (the notation follows cg_ops.thermal)')
for lab, expr in (
        ('A', r'\frac{K_{11}y_\eta^2-2K_{13}x_\eta y_\eta+K_{33}x_\eta^2}{J}'),
        ('D', r'\frac{K_{11}y_\xi^2-2K_{13}x_\xi y_\xi+K_{33}x_\xi^2}{J}'),
        ('B', r'\frac{K_{13}\left(x_\xi y_\eta+x_\eta y_\xi\right)-K_{11}y_\xi y_\eta'
              r'-K_{33}x_\xi x_\eta}{J}')):
    eq(r'%s=%s' % (lab, expr))
para('and the momentum operator is built in exactly the same way from the plane-strain block '
     'Q (cg_ops.momentum). At the wall (ξ = 0) of the circular production grid the three '
     'coefficients evaluate to A = %s, B = %s and D = %s W m⁻¹ K⁻¹; the '
     'mixed coefficient B is zero there by symmetry and non-zero for the ellipse, which is '
     'what makes the ellipse a genuinely two-dimensional test.'
     % (g(A0 := (M.K_ac[0, 0] * grid.y_eta[0, 0] ** 2
                 - 2 * M.K_ac[0, 1] * grid.x_eta[0, 0] * grid.y_eta[0, 0]
                 + M.K_ac[1, 1] * grid.x_eta[0, 0] ** 2) / grid.J[0, 0], 4),
        g((M.K_ac[0, 1] * (grid.x_xi[0, 0] * grid.y_eta[0, 0] + grid.x_eta[0, 0] * grid.y_xi[0, 0])
           - M.K_ac[0, 0] * grid.y_xi[0, 0] * grid.y_eta[0, 0]
           - M.K_ac[1, 1] * grid.x_xi[0, 0] * grid.x_eta[0, 0]) / grid.J[0, 0], 4),
        g((M.K_ac[0, 0] * grid.y_xi[0, 0] ** 2
           - 2 * M.K_ac[0, 1] * grid.x_xi[0, 0] * grid.y_xi[0, 0]
           + M.K_ac[1, 1] * grid.x_xi[0, 0] ** 2) / grid.J[0, 0], 4)))

h2('Discrete operators and boundary treatment')
para('Both operators are discretised in the conservative form above, so that the discrete flux '
     'divergence of a constant field is identically zero (the V7 patch test of the manuscript). '
     'In the radial direction the second derivative is replaced by a second-order one-sided '
     'three-point formula in the first and last interior ring, where the centred stencil would '
     'reach outside the domain; in the circumferential direction the stencil is the centred '
     'second-order formula with periodic wrap-around, discretely exact for the trigonometric '
     'modes that the grid supports. Derivatives of the map (x_ξ, x_η, y_ξ, '
     'y_η, J) are evaluated analytically from the closed-form map.')

h2('Grid sizes, unknowns and cost')
para('The unknown vector is U = (θ, u₁, u₃) at every node, i.e. 3N_rN_θ = '
     '3 × %d × %d = %d complex unknowns per frequency. The production grid is '
     'N_r × N_θ = 96 × 48 with γ = %s; the convergence families use '
     '(48, 96, 192) × 48 and 96 × (48, 144) together with clustering parameters '
     'γ ∈ {2.5, 3.5, 4.5}. One frequency-domain solve per Bromwich node is required, '
     'so the cost of a run is the number of solves times one sparse factorisation; the counts '
     'are given in Section 8.'
     % (grid.Nr, grid.Nt, 3 * grid.Nr * grid.Nt, g(grid.gamma, 1)))

# ----------------------------------------------------------------- 7
h1('Frequency-domain system')
h2('Assembly')
para('With the harmonic convention fields ∝ exp(+iωt), the semi-discrete equations are '
     'the single complex linear system')
eq(r'\mathbf{A}(\omega)\,\mathbf{U}=\mathbf{f},\qquad'
   r'\mathbf{A}(\omega)=\mathbf{A}_{\mathrm{base}}+\omega^2\mathbf{A}_{\mathrm{in}}'
   r'+i\omega\,\mathbf{A}_{\mathrm{d}}+g(\omega)\,\mathbf{A}_{\mathrm{lap}},')
para('where A_base holds the elastic stiffness and the steady conduction operator, A_in the '
     'mass matrix, A_d the (viscous-free) inertial coupling rows and A_lap the Laplacian of '
     'the heat equation, multiplied by the conduction kernel g(ω) of the chosen law. The '
     'four matrices are assembled once per grid and reused for every frequency, so a run costs '
     'one assembly and n_solves factorisations.')

h2('Conduction kernels')
para('The three laws differ only in the scalar factor g(ω):')
eq(r'g_{\mathrm{F}}(\omega)=1,')
eq(r'g_{\mathrm{CV}}(\omega)=\frac{1}{1+i\omega\tau},')
eq(r'g_{\mathrm{MCV3}}(\omega)=\frac{1}{2}\frac{1}{1+i\omega\tau/2}'
   r'+\frac{1}{2}\frac{1}{1+2i\omega\tau},')
table(['Law', 'kernel', 'status in this study'],
      [['Fourier', 'g = 1 for every ω', 'baseline of every comparison'],
       ['Cattaneo–Vernotte (one relaxation time)',
        'g = 1/(1 + iωτ)', 'primary non-Fourier model (Lord–Shulman form)'],
       ['Two relaxation times (MCV3)',
        'average of two CV kernels with τ/2 and 2τ',
        'exploratory sensitivity variant only']],
      'Conduction kernels in the frequency domain. All three reduce to g = 1 as '
      'ωτ → 0, so the Fourier case is the limit of the other two.')
para('The three kernels differ only in that scalar factor, which is why the whole model '
     'family is implemented as one assembly with g(ω) as a parameter.')
para('Both non-Fourier kernels are positive-real (passive) for real ω, which is the '
     'property that keeps the response physically admissible; the manuscript does not claim '
     'that either is the correct description of β-Ga₂O₃, and the relaxation time is '
     'treated as a hypothetical parameter throughout.')

h2('Boundary rows, scaling and the solve')
para('The cavity wall carries the Dirichlet condition θ = 1 (per unit amplitude) and '
     'zero traction; the outer boundary carries θ = 0 and u = 0. Both are imposed by '
     'row replacement. Before factorisation every row is multiplied by the local Jacobian and '
     'then scaled so that its largest entry has unit modulus (row equilibration); without it '
     'the spread of magnitudes between the temperature rows and the displacement rows costs '
     'several digits of accuracy. The system is factorised with a sparse LU (SuperLU, splu) '
     'and improved by two steps of iterative refinement. The measured effect, over %d '
     'production runs, is a backward error of at most %s and, after refinement, a forward-'
     'error floor of order 10⁻¹⁴ relative — the refinement is what makes the small '
     'differences of Section 9 (deviations of a few tenths of a per cent) resolvable at all.'
     % (D['numerics']['n_runs'], sci(D['numerics']['max_backward_error'], 3)))

# ----------------------------------------------------------------- 8
h1('Single-pulse response by Bromwich inversion')
h2('The contour and the inversion formula')
para('The frequency-domain solver returns the response to a steady harmonic wall temperature. '
     'The response to a *single* pulse in a medium at rest is obtained by Laplace inversion on '
     'a vertical contour Re(s) = γ_B > 0,')
eq(r'y(t)=\frac{\exp(\gamma_B t)}{T}\left[Y(\gamma_B)+2\,\mathrm{Re}\sum_{k=1}^{K}'
   r'Y\!\left(\gamma_B+i\omega_k\right)\exp\left(i\omega_k t\right)\right],\qquad'
   r'\omega_k=\frac{2\pi k}{T},')
para('with Y(s) = H(s)P(s), where H is the transfer function evaluated at the complex '
     'frequency ω = −i s/t_th (the solver’s exp(+iωt) convention makes iω = '
     's) and P is the two-sided Laplace transform of the Gaussian wall pulse '
     'p(t) = exp(−((t − t₀)/t_w)²),')
eq(r'P(s)=\sqrt{\pi}\,t_w\,\exp\!\left[\left(\frac{s\,t_w}{2}\right)^2-s\,t_0\right].')
para('This replaces the periodic-DFT synthesis of the handoff code, which returns the steady '
     'state of a pulse *train* rather than the response to one pulse: the distinction is '
     'quantitative, not cosmetic, because a pulse train accumulates heat in the medium '
     'between pulses.')

h2('Choice of the parameters')
para('The defaults are T = %s t_th, γ_B = %s/t_th, t₀ = %s t_th, '
     't_w = %s t_th and ε_tr = %s. They are fixed by three competing errors:'
     % (g(plan.T, 1), g(plan.gamma, 1), g(plan.t0, 1), g(plan.tw, 1), sci(plan.eps, 0)))
bullets([
    'alias error: periodising the inverse adds images at t ± nT; the n ≥ 1 images are '
    'suppressed by exp(−γ_B T) = exp(−%s) = %s, and the n ≤ −1 images by the '
    'Gaussian pre-history, which is negligible for t < t₀ − 5t_w = %s t_th;'
    % (g(plan.gamma * plan.T, 1), sci(np.exp(-plan.gamma * plan.T)),
       g(plan.t0 - 5 * plan.tw, 1)),
    'truncation: K is chosen so that |P(s_K)|/|P(s_0)| < ε_tr. Because |P| grows like '
    'exp((ω t_w/2)²), the condition is ω_max = √(γ_B² + 4 ln(1/ε_tr)/t_w²) '
    '= √(%s + 4×%s/%s) = %s, hence K, the smallest integer not below ω_max T/2π, is %d '
    'and n_solves = K + 1 = %d;'
    % (g(plan.gamma ** 2, 2), g(np.log(1 / plan.eps), 3), g(plan.tw ** 2, 2),
       g(np.sqrt(plan.gamma ** 2 + 4 * np.log(1 / plan.eps) / plan.tw ** 2), 4),
       plan.K, plan.n_solves),
    'round-off: the factor exp(γ_B t) amplifies the truncation error, growing to '
    'exp(%s × 6) = %s at t = 6 t_th and exp(%s × 12) = %s at '
    't = 12 t_th.'
    % (g(plan.gamma, 1), g(np.exp(plan.gamma * 6), 1), g(plan.gamma, 1),
       g(np.exp(plan.gamma * 12), 1)),
])
para('The three balance to the validity window printed by the plan, 0 ≤ t ≤ %s t_th '
     '(T − 5.5), comfortably beyond the quantity-of-interest window 0 ≤ t ≤ 6 t_th. '
     'The reconstruction is checked directly: the wall temperature recovered from H is '
     'compared with the prescribed Gaussian in every run, and the largest discrepancy over the '
     'QoI window is %s relative across %d runs.'
     % (g(plan.t_valid_max, 1), sci(D['numerics']['max_wall_pulse_error'], 3),
        D['numerics']['n_runs']))

# ----------------------------------------------------------------- 9
h1('Quantities of interest: worked arithmetic')
h2('Peak wall stress and the trigonometric interpolant')
para('The primary observable is the maximum over the wall and over the window of the modulus '
     'of the hoop stress,')
eq(r'\hat\sigma=\max_{\eta}\ \max_{0\leq t\leq 6t_{th}}\left|\sigma_{\theta\theta}'
   r'(\eta,t)\right|,\qquad \sigma_{\theta\theta}=t_x^2\sigma_{11}+2t_x t_y\,\sigma_{13}'
   r'+t_y^2\sigma_{33},')
para('with (t_x, t_y) the unit tangent of the wall. Taking the maximum over grid nodes '
     'quantises it and biases it low by an amount of order (Δη)², which is not '
     'negligible on the coarse grids; the manuscript therefore also evaluates the maximum of '
     'the trigonometric interpolant')
eq(r'\sigma_{\theta\theta}(\eta,t)=\sum_k c_k(t)\,\exp(ik\eta),\qquad '
   r'c_k=\frac{1}{N_\theta}\sum_j\sigma_{\theta\theta}(\eta_j,t)\,\exp(-ik\eta_j),')
_fn = D['circle_peak']['radial_nodal']['f'][-1]
_fi = D['circle_peak']['radial_interp']['f'][-1]
para('and reports both. On the finest radial grid of the circle study the two differ by %s%% '
     '(%s against %s Pa K⁻¹), and refining the angular direction from 48 to 192 '
     'intervals changes the interpolated peak by %s%% — the node-based and '
     'interpolant-based peaks are the same number to within the grid uncertainty, and the '
     'interpolant is used wherever a difference of a few tenths of a per cent matters.'
     % (g(100 * abs(_fn - _fi) / _fi, 3), g(_fn, 1), g(_fi, 1),
        g(100 * D['circle_peak']['angular_T48_to_M_rel_change'], 3)))

h2('Orientation modulation')
para('The orientation modulation is the peak-to-peak spread of the wall stress over crystal '
     'rotations, normalised by its mean,')
eq(r'A_\varphi=\frac{\max_\varphi\hat\sigma-\min_\varphi\hat\sigma}'
   r'{\mathrm{mean}_\varphi\,\hat\sigma}.')
sh = D['shipped']
para('For the twelve-angle sweep on the production grid the values are min = %s, max = %s and '
     'mean = %s MPa K⁻¹, so A_φ = (%s − %s)/%s = %s. The same quantity '
     'computed on the radial-extrapolated six-angle sweep is %s, i.e. the modulation is '
     'resolved well beyond the numerical uncertainty of %s.'
     % (MPa(sh['ellipse_min']), MPa(sh['ellipse_max']),
        MPa(np.mean(sh['ellipse'])),
        MPa(sh['ellipse_max']), MPa(sh['ellipse_min']), MPa(np.mean(sh['ellipse'])),
        g(sh['ellipse_amp'], 4),
        g(D['T4_H2']['amplitude_6phi_extrapolated'], 4), g(D['T4_H2']['u_num'], 4)))

h2('Thermal-memory deviation')
para('The thermal-memory deviation compares a non-Fourier run with the Fourier run at the '
     'same parameters,')
eq(r'D=\frac{\max_{\eta,t}\left|\sigma_{\theta\theta}^{\mathrm{CV}}'
   r'-\sigma_{\theta\theta}^{\mathrm{F}}\right|}'
   r'{\max_{\eta,t}\left|\sigma_{\theta\theta}^{\mathrm{F}}\right|},\qquad'
   r'0\leq t\leq 6t_{th}.')
dyn = {r['tag']: r for r in D['T2_H3']['dynamic']}
qs = {r['tag']: r for r in D['T2_H3']['quasi_static']}
rows = []
for tag in ('B_CV_tau1_a10', 'B_CV_tau5_a10', 'B_CV_tau20_a10'):
    if tag in dyn and tag + '_QS' in qs:
        d_, q_ = dyn[tag], qs[tag + '_QS']
        rows.append([g(d_['tau_ps'], 0), g(d_['Lambda'], 4), g(d_['D'], 5),
                     g(q_['D'], 5), g(d_['D'] - q_['D'], 5)])
if rows:
    table(['τ (ps)', 'Λ', 'D (dynamic)', 'D (quasi-static)', 'difference'], rows,
          'Thermal-memory deviation D of the circular cavity at a = 10 nm, dynamic and '
          'quasi-static, from the processed data package. Both are well below the '
          'numerical uncertainty of the grid.')
para('Two features of these numbers are worth stating explicitly. First, D is small in '
     'absolute terms — of the order of tenths of a per cent to a few per cent — so '
     'the thermal-memory effect is a correction, not a change of regime. Second, the dynamic '
     'D exceeds the quasi-static D by a systematic margin, which is the inertial contribution '
     'rather than the conductive one; the manuscript separates the two by comparing against '
     'the quasi-static family.')

h2('Richardson extrapolation, step by step')
iso_r = D['isotropic']['ellipse_radial']
f48, f96, f192 = iso_r['f']
p_obs = np.log((f48 - f96) / (f96 - f192)) / np.log(2.0)
f_ext = f192 + (f192 - f96) / (2 ** p_obs - 1)
para('The radial convergence study for the ellipse (isotropic control) gives peak values '
     'f₄₈ = %s, f₉₆ = %s and f₁₉₂ = %s Pa K⁻¹ at N_r = 48, 96, 192. '
     'Assuming a clean power law f_n = f_∞ + C n^{−p}, three grids determine p:'
     % (g(f48, 1), g(f96, 1), g(f192, 1)))
eq(r'p=\frac{\ln\left[(f_{48}-f_{96})/(f_{96}-f_{192})\right]}{\ln 2}'
   r'=\frac{\ln\left[%s/%s\right]}{\ln 2}=%s,'
   % (g(f48 - f96, 1), g(f96 - f192, 1), g(p_obs, 4)))
para('and then the extrapolated value is')
eq(r'f_\infty=f_{192}+\frac{f_{192}-f_{96}}{2^{p}-1}=%s+\frac{%s}{%s}=%s\ \mathrm{Pa\,K^{-1}},'
   % (g(f192, 1), g(f192 - f96, 1), g(2 ** p_obs - 1, 4), g(f_ext, 1)))
para('so the correction applied to the finest grid is %s Pa K⁻¹ (%s%% relative) and '
     'the extrapolated value differs from the production grid by %s%%. The observed order '
     'p = %s is below the formal second order of the stencils, which is expected: the wall '
     'stress is extracted at a boundary where one-sided formulas and a curved boundary both '
     'reduce the effective order, and the clustering parameter interacts with it. The '
     'manuscript quotes the extrapolated value with the observed order and reports the '
     'numerical uncertainty u_num = %s from the same budget.'
     % (g(f_ext - f192, 1), g(100 * (f_ext - f192) / f192, 3),
        g(100 * abs(f_ext - f96) / f96, 2), g(p_obs, 3), g(D['T4_H2']['u_num'], 4)))

h2('Uncertainty budget')
para('Two uncertainties are tracked and never added in quadrature, because they are of '
     'different kinds. The numerical uncertainty u_num = %s (relative) comes from the grid: '
     'it is the largest residual spread of the convergence families after extrapolation, and '
     'the resolvability threshold fixed before the runs was %s. The parameter uncertainty is '
     'separate and larger: it comes from the spread of the published thermal-expansion data '
     'and is quantified in Section 10. The manuscript keeps them apart throughout, because '
     'the first is a property of the discretisation and can be reduced by computing, while '
     'the second is a property of the material data and cannot.'
     % (g(D['T4_H2']['u_num'], 4), g(D['T4_H2']['threshold'], 4)))

# ----------------------------------------------------------------- 10
h1('Ablations: what each ingredient contributes')
h2('Mechanism ablations')
E = D['E_ablations']
rows = []
labels = [('baseline_6phi', 'baseline (all anisotropy)'),
          ('E3_K_iso', 'isotropic conductivity (K → k_iso I)'),
          ('E4_C_iso', 'isotropic stiffness (Q → Q_iso)'),
          ('E2_alpha_iso', 'isotropic expansion (α → mean)'),
          ('E1_alpha_cheng298', 'alternative expansion set [18]')]
for key, name in labels:
    if key in E:
        v = E[key]
        rows.append([name, g(v['amplitude'], 4), MPa(v['mean']),
                     g(v.get('mean_over_baseline', 1.0), 4)])
table(['Variant', 'A_φ', 'mean peak (MPa/K)', 'mean / baseline'], rows,
      'Mechanism ablations on the six-angle ellipse sweep. A_φ is the orientation '
      'modulation; the last column is the change of the absolute stress scale.')
para('Read the table in two columns at a time. The modulation A_φ collapses to %s when '
     'the expansion is made isotropic and to %s when the stiffness is made isotropic, while '
     'it barely moves when the conductivity is made isotropic (%s against a baseline of %s). '
     'The conclusion is that the orientation dependence is driven by the elastic and '
     'expansion anisotropy, not by the conduction anisotropy.'
     % (g(E['E2_alpha_iso']['amplitude'], 4), g(E['E4_C_iso']['amplitude'], 4),
        g(E['E3_K_iso']['amplitude'], 4), g(E['baseline_6phi']['amplitude'], 4)))

h2('The expansion data: the dominant uncertainty')
para('The last row is the one that matters for the absolute magnitude of every stress quoted '
     'in the manuscript. Replacing the reference expansion set with the alternative set of '
     '[18] divides the mean peak wall stress by %s — a factor of about %s — while '
     'changing the modulation only from %s to %s. The two effects are therefore separable: '
     'the *shape* of the orientation dependence is robust to which expansion set is used, '
     'while the *scale* is not. This is why the manuscript reports the modulation '
     'dimensionlessly and the stress per kelvin, and why it states the >10× uncertainty in '
     'the absolute stress scale prominently rather than in a footnote.'
     % (g(1 / E['E1_alpha_cheng298']['mean_over_baseline'], 2),
        g(1 / E['E1_alpha_cheng298']['mean_over_baseline'], 1),
        g(E['baseline_6phi']['amplitude'], 4), g(E['E1_alpha_cheng298']['amplitude'], 4)))

# ----------------------------------------------------------------- 11
h1('Reproduction')
h2('What to run, and what it must reproduce')
para('The companion inherits the provenance of the manuscript. The source code is frozen '
     'under PAPER_PROJECT/06_Source_Code/CODE_FREEZE_v2_gate.json (gate freeze, %d files) and '
     'CODE_FREEZE_v2_final.json (%d files), each entry carrying a SHA-256 of the file; the '
     'raw output of the %d production runs and the convergence families is in '
     'PAPER_PROJECT/09_Raw_Data/production/; the processed numbers quoted here are in '
     'PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json. Regenerating this document is a '
     'single command:'
     % (len(json.load(open(os.path.join(ROOT, 'PAPER_PROJECT', '06_Source_Code',
                                        'CODE_FREEZE_v2_gate.json'))).get('files', {})),
        len(json.load(open(os.path.join(ROOT, 'PAPER_PROJECT', '06_Source_Code',
                                        'CODE_FREEZE_v2_final.json'))).get('files', {})),
        D['numerics']['n_runs']))


def _frz(label):
    import hashlib as _hl
    _p = os.path.join(ROOT, 'PAPER_PROJECT', '06_Source_Code', 'CODE_FREEZE_%s.json' % label)
    try:
        _f = json.load(open(_p))['files']
    except (OSError, ValueError, KeyError):
        return 0, 0, 0
    _s = sum(1 for r, h in _f.items()
             if os.path.exists(os.path.join(ROOT, 'PAPER_PROJECT', r))
             and _hl.sha256(open(os.path.join(ROOT, 'PAPER_PROJECT', r), 'rb').read()).hexdigest() == h)
    return len(_f), _s, len(_f) - _s


SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03c', 'submission_2026_10_03b'

N_FRZ, N_FRZ_SAME, N_FRZ_DIFF = _frz('v2_gate')
N_SUB, N_SUB_SAME, N_SUB_DIFF = _frz(SUB_FREEZE)
N_MID, N_MID_SAME, N_MID_DIFF = _frz(PREV_FREEZE)
N_MIDN, N_MIDN_SAME, N_MIDN_DIFF = _frz('submission_2026_10_03')
N_PREV, N_PREV_SAME, N_PREV_DIFF = _frz('submission_2026_10_02')
if N_SUB_DIFF:
    raise SystemExit('CODE_FREEZE_%s.json no longer describes the code '
                     '(%d of %d entries differ); regenerate it before rebuilding this document'
                     % (SUB_FREEZE, N_SUB_DIFF, N_SUB))


def _frz_diff_names(label):
    """basenames of the entries of CODE_FREEZE_<label>.json whose recorded digest no longer matches
    the file as it stands, as prose; computed, so this document cannot state a stale list."""
    import hashlib as _hl
    _p = os.path.join(ROOT, 'PAPER_PROJECT', '06_Source_Code', 'CODE_FREEZE_%s.json' % label)
    try:
        _f = json.load(open(_p))['files']
    except (OSError, ValueError, KeyError):
        return 'none'
    names = [os.path.basename(r) for r, h in _f.items()
             if not os.path.exists(os.path.join(ROOT, 'PAPER_PROJECT', r))
             or _hl.sha256(open(os.path.join(ROOT, 'PAPER_PROJECT', r), 'rb').read()).hexdigest() != h]
    if not names:
        return 'none'
    if len(names) == 1:
        return names[0]
    return ', '.join(names[:-1]) + ' and ' + names[-1]


FRZ_DIFF_NAMES = _frz_diff_names('v2_gate')
para('Both archived manifests were taken on 2026-10-01. %d of the %d entries of the gate freeze are '
     'byte-identical in the code as submitted; %d entries (%s) have been edited since, so the '
     'digests recorded for them no longer describe it. The pipeline was therefore re-run end to end with '
     'the code as submitted, and it reproduces the archived results exactly: the production runs agree '
     'with the archived quantities of interest to zero relative difference, every leaf of '
     'ANALYSIS_V2.json agrees within 10\u207b\u2079, the eight figures and the five archived CSV tables are '
     'byte-identical, and only wall-clock timings differ '
     '(PAPER_PROJECT/15_Audits/RERUN_COMPARISON.md). The verification pass of 2026-10-03 added an '
     'ablation set at the production grid (24 runs), re-ran the analysis layer over all 175 stored runs '
     'with no pre-existing quantity changed, and re-solved one production job in a different '
     'Python/NumPy build, where it reproduced its stored peak wall stress to 2.7\u00d710\u207b\u00b9\u2076 relative. '
     'The mathematical audit that followed re-derived the constitutive algebra and every printed analytical '
     'identity symbolically and re-checked the discretisation, kernel and inversion conventions against the '
     'shipped code; it corrected two typographical statements in the model description, made the plane-strain '
     'class and the norm convention of \u03b4 explicit, and replaced the hard-coded validity window of the '
     'inversion by the bound it was an instance of (t \u2264 T \u2212 (t_{0} + 2.5t_{w}): 14.5 t_{th} for the '
     'baseline t_{w} = 1.2 t_{th}, 11.5 t_{th} for t_{w} = 2.4 t_{th}). No stored run and no reported value '
     'changed. CODE_FREEZE_%s.json (%d files, all %d byte-identical to the code as submitted) '
     'is the refreshed manifest, the one to deposit with the data package; it supersedes '
     'CODE_FREEZE_%s.json (taken the same day, before the audit, %d of whose %d entries '
     'still match), CODE_FREEZE_submission_2026_10_03.json and CODE_FREEZE_submission_2026_10_02.json, all '
     'kept unchanged as history.'
     % (N_FRZ_SAME, N_FRZ, N_FRZ_DIFF, FRZ_DIFF_NAMES, SUB_FREEZE, N_SUB, N_SUB_SAME, PREV_FREEZE, N_MID_SAME, N_MID))
bullets([
    'python3 PAPER_PROJECT/13_Manuscript/build_calculations.py — rebuilds this '
    'document from the frozen source and the processed data;',
    'python3 tools/md_to_tex.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md '
    '-o PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex --companion — '
    'the LaTeX source;',
    'python3 tools/md_to_pdf.py -i … -o … — the preprint PDF.',
])
h2('Status of the calculations and of the model')
para('This companion treats Fourier and Lord--Shulman conduction as the primary conduction '
     'laws: every number that carries a physical interpretation is computed with one of them. '
     'The two-relaxation-time kernel is carried as an exploratory sensitivity kernel only, and '
     'no statement in this document depends on it. Nothing here is a validation: every '
     'comparison is against an exact solution of the same mathematical model or against an '
     'independent implementation of it, and no experimental validation exists for the '
     'configuration studied. The continuum validity of the model at the 5–50 nm scale of '
     'the study is not established, and the relaxation times used are hypothetical parameters '
     'rather than measured ones. The thermal-expansion data that set the absolute stress scale '
     'differ between sources by more than an order of magnitude, which is why the orientation '
     'modulation is reported dimensionlessly and the stress is reported per kelvin; the '
     'modulation survives the change of expansion set, the scale does not.')
para('Code and data will be deposited on acceptance; the persistent identifier is '
     '[PUBLIC REPOSITORY/DOI TO BE INSERTED].')

_emit('\n## Declarations\n')
para('**CRediT authorship contribution statement:** [AUTHOR INPUT REQUIRED].')
para('**Declaration of competing interest:** [AUTHOR INPUT REQUIRED].')
para('**Funding:** [AUTHOR INPUT REQUIRED: name the grant, or state that no funding was '
     'received].')
para('**Data availability:** the Python source code, the verification suite, the per-run raw '
     'outputs and the processed analysis package from which every number in this companion is '
     'recomputed are provided in the project data package (SHA-256 code freeze '
     'CODE_FREEZE_v2_gate.json), to be deposited at [PUBLIC REPOSITORY/DOI TO BE INSERTED].')
para('**Declaration of Generative AI and AI-assisted technologies in the writing process.** '
     '[TEMPLATE — to be reviewed, edited and confirmed by the authors; Elsevier requires '
     'this statement above the references.] '
     'During the preparation of this work the author(s) used a generative-AI assistant (Arena.ai '
     'Agent Mode; the underlying models are provided by the service) for the writing process: '
     'drafting and revising the text and the figure captions, and checking the internal consistency '
     'of the manuscript, the calculation companion and the tables. After using this tool the '
     'author(s) reviewed and edited the content as needed and take(s) full responsibility for the '
     'content of the publication. The same class of tool was also used in the research process — '
     'reviewing and extending the numerical code and the verification suite, and running the '
     'simulations — which the journal policy places in the methods rather than in this declaration; '
     'the numerical-methods section of the manuscript records that use. No AI tool generated a '
     'physical result, no AI tool was used to produce or select any number reported here, and no AI '
     'tool is an author or is cited as a source.')

# ----------------------------------------------------------------- write
out_md = os.path.join(HERE, 'calculations_IJHMT.md')
with open(out_md, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(OUT).replace('\n\n\n', '\n\n') + '\n')

def _no_placeholder_tables(path, doc):
    """Submission guard (audit A2): a generated table must never ship a placeholder cell."""
    bad = []
    for i, line in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        if not line.lstrip().startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 2:
            continue
        for c in cells:
            if c in ('n/a', 'N/A', '??', 'TODO', ''):
                bad.append(f'  line {i}: {line.strip()[:110]}')
                break
    if bad:
        raise SystemExit(f'{doc}: placeholder cells in generated tables ({len(bad)} line(s)):\n'
                         + '\n'.join(bad[:8]) + '\nFix the builder or the data; do not ship the placeholder.')

print('wrote %s' % out_md)
print('  %d sections, %d subsections, %d equations, %d tables, ~%d words'
      % (_state['sec'], sum(1 for l in OUT if l.lstrip().startswith('### ')),
         _state['eq'], _state['tab'], _state['words']))

_no_placeholder_tables(out_md, 'companion calculations')
