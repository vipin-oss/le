"""ms_derivation.py — expanded Sections 2 and 3 of the manuscript: the full derivation chain
(kinematics, balance laws, monoclinic plane-strain reduction, crystal rotation, conduction
kernels, boundary/initial conditions, non-dimensionalisation) and the analytical results
(collapse identity, local response of the circle, feedback bound).

Every displayed equation here is either a definition, an algebraic rearrangement of the
equations the solver actually discretises, or a closed-form result that is also used as a
verification reference.  No numerical result of the study is produced in this module: the
numbers that appear are model constants read from cg_model / cg_pipeline, i.e. the same
constants the production runs use.

Equation cross-references use the @@eq:key@@ placeholder; build_manuscript.py replaces them
with the number the equation gets in order of appearance.
"""
import os
import sys

sys.dont_write_bytecode = True


def _pp_root(_start):
    _p = os.path.abspath(_start)
    while True:
        if os.path.basename(_p) == 'PAPER_PROJECT':
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            break
        _p = _q
    return os.environ.get('PAPER_PROJECT_ROOT', '/home/user/PAPER_PROJECT')


ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, '06_Source_Code', 'src'))
import numpy as np                                            # noqa: E402
import cg_model as M                                          # noqa: E402
import cg_pipeline as cp                                      # noqa: E402

Q, BETA = M.plane_strain_block()
C = M.Cij_GPa
KAPPA = cp.KAPPA
C_REF = cp.C_REF
DELTA = cp.delta_feedback()
KBAR = float(np.sqrt(np.linalg.det(M.K_ac)))
QEIG = np.linalg.eigvalsh(Q)
KEIG = np.linalg.eigvalsh(M.K_ac)
BNORM = float(np.linalg.norm(BETA))
LAM = C['C12'] * 1e9
MU = C['C66'] * 1e9
M_LAME = LAM + 2 * MU
ALPHA_ISO = float(np.mean(M.alpha_crys))
GAMMA_T = (3 * LAM + 2 * MU) * ALPHA_ISO
G_T = GAMMA_T / M_LAME
R_OVER_A = 80.0


def E(tex, key=None):
    """a displayed equation; key enables @@eq:key@@ cross-references"""
    return ('eq', tex, '', key)


def GPa(x):
    return f'{x/1e9:.1f}'


def MPa(x):
    return f'{x/1e6:.4f}'


# ----------------------------------------------------------------------------- Section 2 additions
def sec2_kinematics():
    """2.2 Kinematics, balance laws and conduction kernels"""
    return [
        ('p', 'The formulation is written in the laboratory frame; the crystal frame is introduced in Section 2.4 and the '
              'two frames coincide at rotation \u03c6 = 0. With displacement u = (u_{1}, u_{3}) and temperature rise '
              '\u03b8 = T \u2212 T_{0}, the small-strain tensor in the plane has the three independent components'),
        E(r'\epsilon_{11}=\frac{\partial u_1}{\partial x_1},\qquad '
          r'\epsilon_{33}=\frac{\partial u_3}{\partial x_3},\qquad '
          r'\gamma_{13}=\frac{\partial u_1}{\partial x_3}+\frac{\partial u_3}{\partial x_1}', 'strain'),
        ('p', 'written in Voigt form \u03f5 = (\u03f5_{11}, \u03f5_{33}, \u03b3_{13}) with the engineering shear '
              '\u03b3_{13} = 2\u03f5_{13}, so that the stress\u2013strain contraction \u03c3:\u03f5 = \u03c3_{11}\u03f5_{11} '
              '+ \u03c3_{33}\u03f5_{33} + \u03c3_{13}\u03b3_{13} is the mechanical work per unit volume. The strain components '
              'satisfy the two-dimensional compatibility relation'),
        E(r'\frac{\partial^2\epsilon_{11}}{\partial x_3^2}+\frac{\partial^2\epsilon_{33}}{\partial x_1^2}'
          r'=\frac{\partial^2\gamma_{13}}{\partial x_1\partial x_3}', 'compat'),
        ('p', 'which is what allows the displacement form used below. Balance of linear momentum and the first law, in the '
              'absence of body heating and internal heat sources, give'),
        E(r'\frac{\partial\sigma_{11}}{\partial x_1}+\frac{\partial\sigma_{13}}{\partial x_3}=\rho\,\ddot u_1,\qquad '
          r'\frac{\partial\sigma_{13}}{\partial x_1}+\frac{\partial\sigma_{33}}{\partial x_3}=\rho\,\ddot u_3', 'momentum'),
        E(r'\rho c_p\,\dot\theta+T_0\,\boldsymbol{\beta}:\dot{\boldsymbol{\epsilon}}=-\nabla\cdot\mathbf{q}', 'energy'),
        ('p', 'where q is the heat-flux vector and the coupling term T_{0}\u03b2:\u03f5\u0307 is the rate at which mechanical '
              'work is converted into heat (the Thomson term of linear thermoelasticity [10]). With the Cattaneo\u2013Vernotte '
              'flux law with a single relaxation time \u03c4,'),
        E(r'\mathbf{q}+\tau\,\frac{\partial\mathbf{q}}{\partial t}=-\mathbf{K}\nabla\theta', 'cvflux'),
        ('p', 'eliminating q between the flux law and the energy balance gives the heat equation that is discretised in '
              'Section 4,')
        , E(r'\nabla\cdot\left(\mathbf{K}\nabla\theta\right)='
            r'\left(1+\tau\,\frac{\partial}{\partial t}\right)'
            r'\left(\rho c_p\,\dot\theta+T_0\,\boldsymbol{\beta}:\dot{\boldsymbol{\epsilon}}\right)', 'heateq'),
        ('p', 'of which Eq. (@@eq:governing@@) of Section 2.1 is the compact form. The Fourier model is recovered at \u03c4 = 0. '
              'For \u03c4 > 0 the law is hyperbolic: temperature disturbances propagate at the finite speed'),
        E(r'v_T=\sqrt{\frac{\bar\kappa}{\tau}},\qquad \bar\kappa=\frac{\sqrt{\det\mathbf{K}}}{\rho c_p}', 'vT'),
        ('p', f'For the parameters of @@tab:params@@, \u03ba\u0304 = {KAPPA*1e6:.3f}\u00d710^{{\u22126}} m\u00b2/s, so that '
              f'v_{{T}} = \u221a(\u03ba\u0304/\u03c4) = {np.sqrt(KAPPA/1e-12):.0f} m/s at \u03c4 = 1 ps and '
              f'{np.sqrt(KAPPA/20e-12):.0f} m/s at \u03c4 = 20 ps, against the longitudinal wave speed '
              f'c_{{ref}} = (C_{{33}}/\u03c1)^{{1/2}} = {C_REF:.0f} m/s. The second law is satisfied in the form'),
        E(r'-\frac{\mathbf{q}\cdot\nabla\theta}{T_0}\geq 0', 'entropy'),
        ('p', 'which the Cattaneo\u2013Vernotte law meets for every \u03c4 > 0 because it is a positive-real (passive) '
              'kernel [55], a restriction stated there for a memory kernel rather than for a single relaxation time; the '
              'two-relaxation-time kernel of Section 2.5 is positive-real for the same reason but is not derived '
              'from a free energy, which is why it is carried as an exploratory variant only. Theories with two relaxation '
              'times [24,25,26] and the reviews of hyperbolic and generalized conduction [14,23,27,28,31,32] locate the '
              'single-relaxation-time law used here within that literature.')
    ]


def sec2_constitutive():
    """2.3 Plane-strain reduction of the monoclinic law"""
    out = [
        ('h2', '2.3 Plane-strain reduction of the monoclinic law'),
        ('p', 'Monoclinic \u03b2-Ga\u2082O\u2083 has point group 2/m with the twofold axis along the crystallographic b '
              'direction. With the b axis taken as x_{2} and Voigt indices 1 = 11, 2 = 22, 3 = 33, 4 = 23, 5 = 13, 6 = 12, '
              'the stiffness has thirteen independent constants and the form of @@tab:stiff@@; the four constants C_{15}, C_{25}, '
              'C_{35} and C_{46} are the monoclinic couplings, and the thermal expansion is diagonal in the crystal frame, '
              '\u03b1 = (\u03b1_{a}, \u03b1_{b}, \u03b1_{c}, 0, 0, 0), so that'),
        E(r'\sigma_I=\sum_{J=1}^{6}C_{IJ}\left(\epsilon_J-\alpha_J\theta\right),\qquad '
          r'\beta_I=\sum_{J=1}^{6}C_{IJ}\alpha_J', 'sigfull'),
        ('p', 'with I = 1, \u2026, 6 (Voigt conventions and the Stroh and Lekhnitskii formalisms for such media are '
              'described in [45,46,47]). Plane strain in the a\u2013c plane imposes \u03f5_{22} = \u03f5_{23} = \u03f5_{12} = 0, '
              'so the six-dimensional law collapses onto the three in-plane components and'),
        E(r'\sigma_{11}=C_{11}\epsilon_{11}+C_{13}\epsilon_{33}+C_{15}\gamma_{13}-\beta_1\theta', 'sig11'),
        E(r'\sigma_{33}=C_{13}\epsilon_{11}+C_{33}\epsilon_{33}+C_{35}\gamma_{13}-\beta_3\theta', 'sig33'),
        E(r'\sigma_{13}=C_{15}\epsilon_{11}+C_{35}\epsilon_{33}+C_{55}\gamma_{13}-\beta_5\theta', 'sig13'),
        ('p', 'i.e. \u03c3 = Q\u03f5 \u2212 \u03b2\u03b8 with the 3\u00d73 block Q of @@tab:Qblock@@. The thermal-stress vector '
              '\u03b2 = \u03a3_{J} C_{IJ}\u03b1_{J} involves the b-axis expansion \u03b1_{b} through the constants C_{12}, '
              'C_{23}, C_{25} that couple the in-plane normal strains to \u03f5_{22}:'),
        E(r'\beta_1=C_{11}\alpha_a+C_{12}\alpha_b+C_{13}\alpha_c+C_{15}\alpha_5', 'beta1'),
        E(r'\beta_3=C_{13}\alpha_a+C_{23}\alpha_b+C_{33}\alpha_c+C_{35}\alpha_5', 'beta3'),
        E(r'\beta_5=C_{15}\alpha_a+C_{25}\alpha_b+C_{35}\alpha_c+C_{55}\alpha_5', 'beta5'),
        ('p', f'where \u03b1_{{5}} = 2\u03f5_{{13}}^{{th}} is the thermal shear, set to zero (a limitation of the available '
              f'data, Section 7.2). With the parameters of @@tab:params@@ this gives \u03b2 = ({MPa(BETA[0])}, {MPa(BETA[1])}, '
              f'{MPa(BETA[2])})\u00d710^{{6}} Pa/K and \u2016\u03b2\u2016 = {BNORM/1e6:.4f} MPa/K; the eigenvalues of Q are '
              f'{QEIG[0]/1e9:.2f}, {QEIG[1]/1e9:.2f} and {QEIG[2]/1e9:.2f} GPa, so the block is positive definite and the '
              f'elastic problem is elliptic. The out-of-plane stress does not enter the equilibrium equations but is '
              f'recovered afterwards from'),
        E(r'\sigma_{22}=C_{12}\epsilon_{11}+C_{23}\epsilon_{33}+C_{25}\gamma_{13}-\beta_2\theta,\qquad '
          r'\beta_2=C_{12}\alpha_a+C_{22}\alpha_b+C_{23}\alpha_c+C_{25}\alpha_5', 'sig22'),
        ('p', 'and does no work because \u03f5_{22} = 0 by construction. @@tab:Qblock@@ collects the numerical '
              'values of the reduced block and of the thermal-stress vector.'),
        ('table', ['Q_{11}', 'Q_{13}', 'Q_{15}', 'Q_{33}', 'Q_{35}', 'Q_{55}',
                   '\u03b2_{1}', '\u03b2_{3}', '\u03b2_{5}', '\u2016\u03b2\u2016'],
         [[f'{Q[0,0]/1e9:.1f}', f'{Q[0,1]/1e9:.1f}', f'{Q[0,2]/1e9:.2f}', f'{Q[1,1]/1e9:.1f}', f'{Q[1,2]/1e9:.2f}',
           f'{Q[2,2]/1e9:.1f}', f'{BETA[0]/1e6:.4f}', f'{BETA[1]/1e6:.4f}', f'{BETA[2]/1e6:.4f}', f'{BNORM/1e6:.4f}']],
         'Plane-strain stiffness block Q (GPa, Eq. (@@eq:sig11@@)) and thermal-stress vector \u03b2 (MPa/K, '
         'Eq. (@@eq:beta1@@)) in the crystal frame, computed from @@tab:params@@.',
         [0.62, 0.62, 0.62, 0.62, 0.62, 0.62, 0.66, 0.66, 0.66, 0.66], 'Qblock'),
        ('table', ['C_{11}', 'C_{22}', 'C_{33}', 'C_{44}', 'C_{55}', 'C_{66}', 'C_{12}', 'C_{13}', 'C_{23}',
                   'C_{15}', 'C_{25}', 'C_{35}', 'C_{46}'],
         [[GPa(C['C11'] * 1e9), GPa(C['C22'] * 1e9), GPa(C['C33'] * 1e9), GPa(C['C44'] * 1e9), GPa(C['C55'] * 1e9),
           GPa(C['C66'] * 1e9), GPa(C['C12'] * 1e9), GPa(C['C13'] * 1e9), GPa(C['C23'] * 1e9),
           f"{C['C15']:.2f}", f"{C['C25']:.2f}", f"{C['C35']:.2f}", f"{C['C46']:.2f}"]],
         'Independent stiffness constants of monoclinic \u03b2-Ga\u2082O\u2083 used in this study (GPa; '
         'literature values [15] transcribed and checked against the source).', [0.55] * 13, 'stiff'),
    ]
    # the stiffness table is cited first in the text: put it before the Q/beta table
    i = next(k for k, b in enumerate(out) if b[0] == 'table' and len(b) > 5 and b[5] == 'Qblock')
    j = next(k for k, b in enumerate(out) if b[0] == 'table' and len(b) > 5 and b[5] == 'stiff')
    out[i], out[j] = out[j], out[i]
    return out


def sec2_rotation():
    """2.4 Rotation of the crystal by phi"""
    c, s = np.cos(np.radians(30.0)), np.sin(np.radians(30.0))
    rows = []
    for phi in (0.0, 30.0, 45.0, 90.0):
        _, br = M.rotate_Q_beta(Q, BETA, np.radians(phi))
        rows.append([f'{phi:.0f}°', f'{br[0]/1e6:+.4f}', f'{br[1]/1e6:+.4f}', f'{br[2]/1e6:+.4f}',
                     f'{np.linalg.norm(br)/1e6:.4f}'])
    return [
        ('h2', '2.4 Rotation of the crystal'),
        ('p', 'Rotating the crystal about the b axis by \u03c6 (equivalently, rotating the loading frame by \u2212\u03c6) '
              'transforms the material tensors but not the cavity: the cavity geometry is fixed in the laboratory frame and '
              'the crystal is turned underneath it. With'),
        E(r'\mathbf{R}(\phi)=\begin{bmatrix}\cos\phi&-\sin\phi\\ \sin\phi&\cos\phi\end{bmatrix}', 'rotmat') if False else
        E(r'\mathbf{R}(\phi)=\left[\cos\phi,\,-\sin\phi;\;\sin\phi,\,\cos\phi\right]', 'rotmat'),
        ('p', 'acting on in-plane vectors as v_{lab} = R v_{crys}, the fourth-order stiffness, the conductivity and the '
              'in-plane expansion transform as'),
        E(r'C^{\prime}_{ijkl}=R_{ip}R_{jq}R_{kr}R_{ls}\,C_{pqrs},\qquad '
          r'\mathbf{K}^{\prime}=\mathbf{R}\mathbf{K}\mathbf{R}^{T},\qquad '
          r'\boldsymbol{\alpha}^{\prime}_{(2)}=\mathbf{R}\,\mathrm{diag}(\alpha_a,\alpha_c)\,\mathbf{R}^{T}', 'rottensors'),
        ('p', 'and the rotated plane-strain block Q\u2032 is read off from C\u2032 by the same assembly rules as in '
              'Eq. (@@eq:sig11@@),'),
        E(r"Q^{\prime}_{11}=C^{\prime}_{1111},\quad Q^{\prime}_{13}=C^{\prime}_{1133},\quad "
          r"Q^{\prime}_{15}=C^{\prime}_{1113},\quad Q^{\prime}_{33}=C^{\prime}_{3333},\quad "
          r"Q^{\prime}_{35}=C^{\prime}_{3313},\quad Q^{\prime}_{55}=C^{\prime}_{1313}", 'Qrot'),
        ('p', 'which is the operation verified in test U1 against an independent three-dimensional rank-four implementation '
              '(Section 5.1). The b-axis expansion is not touched by the rotation about b, but the constants that carry it '
              'into the plane are: the symmetric 2\u00d72 block S = [[C_{12}, C_{25}], [C_{25}, C_{23}]] transforms as '
              'S\u2032 = R S R^{T}, i.e. with c = cos \u03c6 and s = sin \u03c6,'),
        E(r"C^{\prime}_{12}=c^2C_{12}+s^2C_{23}-2cs\,C_{25}", 'bc12'),
        E(r"C^{\prime}_{23}=s^2C_{12}+c^2C_{23}+2sc\,C_{25}", 'bc23'),
        E(r"C^{\prime}_{25}=cs\left(C_{12}-C_{23}\right)+\left(c^2-s^2\right)C_{25}", 'bc25'),
        ('p', 'so that the thermal-stress vector in the laboratory frame is'),
        E(r"\boldsymbol{\beta}^{\prime}(\phi)=\mathbf{Q}^{\prime}(\phi)\,"
          r"\left(\alpha^{\prime}_{11},\,\alpha^{\prime}_{33},\,2\alpha^{\prime}_{13}\right)"
          r"+\alpha_b\left(C^{\prime}_{12},\,C^{\prime}_{23},\,C^{\prime}_{25}\right)", 'betarot'),
        ('p', f'the factor 2 in the third slot being the engineering-shear convention. Two consequences are worth noting. '
              f'First, the thermal shear \u03b2\u2032_{{5}} does not vanish after rotation even though \u03b1_{{5}} = 0 in the '
              f'crystal frame (@@tab:betaphi@@): the rotated in-plane expansion acquires the off-diagonal component '
              f'\u03b1\u2032_{{13}} = (c\u00b2 \u2212 s\u00b2)\u00b7 0 + cs(\u03b1_{{c}} \u2212 \u03b1_{{a}}) \u2260 0 whenever '
              f'\u03b1_{{a}} \u2260 \u03b1_{{c}}. Second, all three components of S\u2032 enter through the cross term '
              f'\u2212 2cs C_{{25}} = {(-2*c*s*C["C25"]):+.3f} GPa at \u03c6 = 30\u00b0, and an error in the sign of that term is '
              f'invisible at \u03c6 = 0 and \u03c6 = 90\u00b0 (where cs = 0) but not at intermediate angles: this is precisely the '
              f'defect carried by a superseded version of this analysis, which tests U1 and V3 now exclude (Section 5.1).'),
        ('table', ['\u03c6', '\u03b2\u2032_{1} (MPa/K)', '\u03b2\u2032_{3} (MPa/K)', '\u03b2\u2032_{5} (MPa/K)',
                   "\u2016\u03b2\u2032\u2016 (MPa/K)"], rows,
         'Thermal-stress vector in the laboratory frame at four crystal rotations (computed from @@tab:params@@ with '
         'Eq. (@@eq:betarot@@)).', [0.7, 1.3, 1.3, 1.3, 1.3], 'betaphi'),
    ]


def sec2_kernels():
    """2.5 Conduction kernels in the Laplace domain"""
    return [
        ('h2', '2.5 Conduction kernels in the Laplace domain'),
        ('p', 'In the Laplace domain (variable s, Re s > 0) all three conduction models used here are the same diffusion '
              'operator with a scalar, frequency-dependent conductivity factor, so that the heat equation reads'),
        E(r'\nabla\cdot\left(\mathbf{K}\,g(s)\,\nabla\hat\theta\right)='
          r's\left(\rho c_p\,\hat\theta+T_0\,\boldsymbol{\beta}:\hat{\boldsymbol{\epsilon}}\right)', 'lapheat'),
        ('p', 'and the momentum equation is unchanged apart from the transform of the inertia term,'),
        E(r'\nabla\cdot\boldsymbol{\hat\sigma}=\rho s^2\mathbf{\hat u},\qquad '
          r'\boldsymbol{\hat\sigma}=\mathbf{Q}\hat{\boldsymbol{\epsilon}}-\boldsymbol{\beta}\hat\theta', 'lapmom'),
        ('p', 'with the kernel'),
        E(r'g(s)=1\quad\text{(Fourier)},\qquad g(s)=\frac{1}{1+s\tau}\quad\text{(Cattaneo--Vernotte)},\qquad '
          r'g(s)=\frac{1/2}{1+s\tau_a}+\frac{1/2}{1+s\tau_b}\quad\text{(two-relaxation-time, exploratory)}', 'kernels'),
        ('p', 'the last with \u03c4_{a} = \u03c4/2 and \u03c4_{b} = 2\u03c4, i.e. an effective relaxation time '
              '\u03c4_{eff} = \u00bd(\u03c4_{a} + \u03c4_{b}) = 1.25\u03c4. Both non-Fourier kernels are positive real, so '
              'the models are passive; the two-relaxation-time kernel is a sensitivity device for asking how much of the '
              'thermal-memory effect depends on the shape of the kernel, and it is labelled exploratory wherever it '
              'appears because it does not follow from a free-energy functional. In the Fourier limit s\u03c4 \u2192 0 all three '
              'kernels tend to one, and the small-s expansion'),
        E(r'g(s)=1-s\tau_{\mathrm{eff}}+O\left((s\tau)^2\right)', 'gexp'),
        ('p', 'shows that the leading effect of thermal memory is a frequency-dependent reduction of the effective '
              'conductivity; in the time domain the same statement is that the flux lags the gradient. The physical motivation '
              'for such laws comes from heat conduction at small scales [33,35,36,37], the two-relaxation-time form is '
              'the two-term version of the multi-phase-lag kernels [34], and general presentations of the theories are '
              'given in [27,29,30].')
    ]


def sec2_bc():
    """2.6 Boundary and initial conditions"""
    return [
        ('h2', '2.6 Boundary and initial conditions'),
        ('p', 'The cavity wall \u0393_{c} is traction-free and held at a prescribed temperature; the outer boundary '
              '\u0393_{R} at R = 80a is clamped and cold:'),
        E(r'\boldsymbol{\sigma}\mathbf{n}=\mathbf{0}\;\text{and}\;\theta=p(t)\;\text{on}\;\Gamma_c,\qquad '
          r'\mathbf{u}=\mathbf{0}\;\text{and}\;\theta=0\;\text{on}\;\Gamma_R', 'bcs'),
        ('p', 'with the outward normal n of the cavity wall (pointing into the solid). The wall temperature is the Gaussian '
              'pulse'),
        E(r'p(t)=\exp\left[-\left(\frac{t-t_0}{t_w}\right)^2\right],\qquad t_0=2.5\,t_{th},\quad t_w=1.2\,t_{th}', 'pulse'),
        ('p', 'and the medium is quiescent before it: u = \u03b8 = 0 and \u2202u/\u2202t = 0 for t < 0. The response computed in '
              'Section 6 is therefore the response to a single pulse, not the periodic steady state of a pulse '
              'train; the distinction is quantitative, not cosmetic (Section 4.6). Because the wall temperature is a '
              'Dirichlet condition, the wall itself shows no thermoelastic feedback by construction, and the finite domain '
              'with a clamped outer boundary supports elastic echoes: the first return of the longitudinal wave to the '
              'wall occurs at'),
        E(r't_{\mathrm{echo}}=2\left(\frac{R}{a}-1\right)\frac{a}{c_{ref}}'
          r'=2\left(\frac{R}{a}-1\right)\epsilon\,t_{th}', 'echo'),
        ('p', f'which is {2*(R_OVER_A-1)*KAPPA/(C_REF*10e-9):.2f} t_{{th}} at a = 10 nm and '
              f'{2*(R_OVER_A-1)*KAPPA/(C_REF*50e-9):.2f} t_{{th}} at a = 50 nm; the quantity-of-interest window '
              f'0 \u2264 t \u2264 6 t_{{th}} is echo-free for a \u2264 10 nm only (Section 7.2).')
    ]


def sec2_dimensionless():
    """2.7 — equations behind the dimensionless groups (text and @@tab:params@@ come from ms_static)"""
    return [
        E(r't_{th}=\frac{a^2}{\bar\kappa},\qquad \bar\kappa=\frac{\sqrt{\det\mathbf{K}}}{\rho c_p}', 'tth'),
        E(r'\Lambda=\frac{\tau}{t_{th}}=\frac{\tau\bar\kappa}{a^2},\qquad '
          r'\epsilon=\frac{\bar\kappa}{c_{ref}a},\qquad \delta=\frac{T_0\,\Vert\boldsymbol{\beta}\Vert^{2}}'
          r'{\rho c_p\bar C}', 'groups'),
        ('p', f'with c_{{ref}} = (C_{{33}}/\u03c1)^{{1/2}} = {C_REF:.0f} m/s and C\u0304 = C_{{33}} = {C["C33"]:.1f} GPa. '
              f'The three groups have direct physical readings: \u039b compares the relaxation time with the time heat '
              f'takes to diffuse across the cavity, \u03b5 compares the thermal diffusion speed \u03ba\u0304/a with the '
              f'elastic wave speed (it is the Mach number of diffusion), and \u03b4 measures the heat released by the '
              f'mechanical deformation against the heat stored by the temperature rise, i.e. the strength of the '
              f'thermoelastic feedback. Numerically \u03ba\u0304 = {KAPPA*1e6:.3f}\u00d710^{{\u22126}} m\u00b2/s, '
              f'\u03b4 = {DELTA*1e3:.3f}\u00d710^{{\u22123}} and, at the reference size a = 10 nm, '
              f'\u03b5 = {KAPPA/(C_REF*10e-9):.4f}. The conductivity tensor has eigenvalues {KEIG[0]:.2f} and '
              f'{KEIG[1]:.2f} W/(m K) with the off-diagonal component {M.K_ac[0,1]:.3f} W/(m K), so the conduction is '
              f'anisotropic by a factor {KEIG[1]/KEIG[0]:.2f} and its principal axes are not aligned with the '
              f'crystallographic a and c axes.'),
        E(r'v_T=\frac{\bar\kappa}{a\sqrt{\Lambda}}=\frac{\epsilon\,c_{ref}}{\sqrt{\Lambda}}', 'vTdim'),
        ('p', 'which expresses the second-sound speed of Eq. (@@eq:vT@@) in the dimensionless groups: at fixed \u03b5 the '
              'thermal wave slows as \u039b^{\u22121/2} when the relaxation time is increased.')
    ]


# ----------------------------------------------------------------------------- Section 3: analytical results
def sec3(p_scaling=None, p_local_intro=None, p_local_close=None):
    """p_scaling / p_local_intro / p_local_close are the three legacy paragraphs of the earlier
    'Two analytical results' subsection, reused here (wording unchanged)."""
    out = [
        ('h1', '3. Analytical results'),
        ('p', 'Three analytical results are used to interpret the computations: a non-dimensionalisation that fixes which '
              'dimensionless groups the answer can depend on, a closed-form local-response solution for the circular '
              'cavity in an isotropic solid, and an order-of-magnitude bound on the thermoelastic feedback. None of them '
              'is a substitute for the computations; they say what the computations must show if the interpretation is '
              'right, and they provide two of the reference solutions of Section 5.'),
        ('h2', '3.1 Non-dimensionalisation'),
        ('p', 'Let \u0398 be the amplitude of the wall pulse and choose the expansion scale '
              '\u03b1_{0} = \u2016\u03b2\u2016/C\u0304, so that the natural stress scale is '
              'C\u0304\u03b1_{0}\u0398 = \u2016\u03b2\u2016\u0398. With'),
        E(r'\mathbf{x}=a\hat{\mathbf{x}},\qquad t=\frac{a^2}{\bar\kappa}\hat t,\qquad '
          r'\theta=\Theta\hat\theta,\qquad \mathbf{u}=a\alpha_0\Theta\,\hat{\mathbf{u}},\qquad '
          r'\boldsymbol{\sigma}=\|\boldsymbol{\beta}\|\Theta\,\hat{\boldsymbol{\sigma}}', 'scaling'),
        ('p', 'the strain is \u03f5 = \u03b1_{0}\u0398\u03f5\u0302 with \u03f5\u0302 = \u00bd(\u2207\u0302u\u0302 + '
              '\u2207\u0302u\u0302^{T}), the constitutive law keeps its form,')
        , E(r'\hat{\boldsymbol{\sigma}}=\hat{\mathbf{Q}}\hat{\boldsymbol{\epsilon}}-\hat{\mathbf{b}}\hat\theta,\qquad '
            r'\hat{\mathbf{Q}}=\frac{\mathbf{Q}}{\bar C},\qquad \hat{\mathbf{b}}=\frac{\boldsymbol{\beta}}'
            r'{\|\boldsymbol{\beta}\|}', 'constitutivehat'),
        ('p', 'and the two field equations become, using \u03ba\u0304 = \u221a(det K)/(\u03c1c_{p}) and '
              'c_{ref}\u00b2 = C\u0304/\u03c1,'),
        E(r'\hat\nabla\cdot\hat{\boldsymbol{\sigma}}=\epsilon^2\,\ddot{\hat{\mathbf{u}}}', 'mhat'),
        E(r'\hat\nabla\cdot\left(\hat{\mathbf{K}}\,g\,\hat\nabla\hat\theta\right)='
          r'\left(1+\Lambda\frac{\partial}{\partial\hat t}\right)'
          r'\left(\frac{\partial\hat\theta}{\partial\hat t}+\delta\,\hat{\mathbf{b}}:\dot{\hat{\boldsymbol{\epsilon}}}\right)',
          'ehat'),
        ('p', 'with \u039b, \u03b5 and \u03b4 the groups of Eq. (@@eq:groups@@) and K\u0302 = K/\u221a(det K). The dimensionless '
              'problem therefore depends on the cavity size a only through \u03b5, and the stress per unit wall-temperature '
              'amplitude is'),
        E(r'\frac{\boldsymbol{\sigma}}{\Theta}=\|\boldsymbol{\beta}\|\,\hat{\boldsymbol{\sigma}}'
          r'\left(\hat{\mathbf{x}};\,\phi,\chi,\frac{R}{a},\Lambda,\epsilon,\delta,t_0,t_w\right)', 'sigscale'),
        ('p', f'so that \u2016\u03b2\u2016 = {BNORM/1e6:.4f} MPa/K is the only material quantity that sets the absolute stress '
              f'scale; every other material parameter enters through the dimensionless groups, the orientation \u03c6 and the '
              f'shape \u03c7. This is the sense in which the results below are relative statements: the dimensionless response '
              f'\u03c3\u0302 is what the computations determine, and the dimensional stress per kelvin is Eq. (@@eq:sigscale@@) '
              f'multiplied by \u2016\u03b2\u2016, whose uncertainty is discussed in Section 6.5.'),
        ('h2', '3.2 The collapse identity and its two corrections'),
        ('p', 'Setting \u03b5 = 0 (quasi-static elasticity) and \u03b4 = 0 (no thermoelastic feedback) removes a from the '
              'problem entirely: the dimensionless temperature depends on \u039b, the geometry and the pulse parameters '
              'alone, and the stress is a linear functional of the temperature. Consequently the thermal-memory deviation '
              'D of Eq. (@@eq:Ddef@@), which is a ratio of two stress histories computed with the same geometry and pulse, '
              'depends on \u039b alone in that limit,'),
        E(r'D=D\left(\Lambda;\,\phi,\chi,\frac{R}{a},t_0,t_w\right)\qquad (\epsilon=0,\;\delta=0)', 'collapse'),
        ('p', 'a statement we call the collapse identity. For the full model the identity can fail only through the two '
              'terms that were dropped, and the failure is expected to be small because both \u03b5 and \u03b4 are small:'),
        E(r'D=D_{\mathrm{collapse}}(\Lambda)+c_1(\Lambda)\,\epsilon^{2}+c_2(\Lambda)\,\delta+O(\epsilon^4,\delta^2)',
          'collapsecorr'),
        ('p', 'the inertia correction entering as \u03b5\u00b2 because \u03b5 appears squared in Eq. (@@eq:mhat@@). Two runs with '
              'the same \u03b1 = \u03c4\u03ba\u0304/a\u00b2 but different a test Eq. (@@eq:collapse@@) directly: their D values '
              'must agree to within the corrections of Eq. (@@eq:collapsecorr@@). The pair used below is (a = 10 nm, '
              '\u03c4 = 5 ps) and (a = 20 nm, \u03c4 = 20 ps), which have the same \u039b = 0.198.'),
        ('h2', '3.3 Local response of the circular cavity in an isotropic solid'),
        ('p', 'For an isotropic solid in quasi-static plane strain the circular cavity can be solved in closed form, and '
              'the solution shows why the wall stress is insensitive to the conduction law. With radial displacement u(r, t), '
              'Lam\u00e9 constants \u03bb, \u03bc, m = \u03bb + 2\u03bc and \u03b3_{T} = (3\u03bb + 2\u03bc)\u03b1, the '
              'strains are \u03f5_{rr} = u\u2032 and \u03f5_{\u03b8\u03b8} = u/r, the stresses are'),
        E(r'\sigma_{rr}=m\,u^{\prime}+\lambda\frac{u}{r}-\gamma_T\theta,\qquad '
          r'\sigma_{\theta\theta}=m\frac{u}{r}+\lambda\,u^{\prime}-\gamma_T\theta', 'isotress'),
        ('p', 'and radial equilibrium d\u03c3_{rr}/dr + (\u03c3_{rr} \u2212 \u03c3_{\u03b8\u03b8})/r = 0 becomes'),
        E(r'm\left(u^{\prime\prime}+\frac{u^{\prime}}{r}-\frac{u}{r^2}\right)=\gamma_T\,\theta^{\prime},\qquad '
          r'\text{i.e.}\qquad m\frac{\mathrm{d}}{\mathrm{d}r}\left[\frac{1}{r}\frac{\mathrm{d}(ru)}{\mathrm{d}r}\right]'
          r'=\gamma_T\,\theta^{\prime}', 'radial'),
        ('p', 'Integrating once, with g_{T} = \u03b3_{T}/m and G(r) = \u222b_{a}^{r} r\u2032\u03b8(r\u2032, t) dr\u2032,'),
        E(r'\frac{1}{r}\frac{\mathrm{d}(ru)}{\mathrm{d}r}=g_T\,\theta+\frac{C_1}{m}'
          r'\quad\Longrightarrow\quad u(r)=\frac{g_T}{r}G(r)+\frac{C_1}{2m}\frac{r^2-a^2}{r}+\frac{C_2}{r}', 'usol'),
        ('p', 'where C_{1} and C_{2} are functions of time alone. Substituting Eq. (@@eq:usol@@) into the first of '
              'Eq. (@@eq:isotress@@) gives'),
        E(r'\sigma_{rr}=\frac{m+\lambda}{2m}C_1+\frac{m-\lambda}{r^2}'
          r'\left[-\left(g_T G+C_2\right)+\frac{C_1a^2}{2m}\right]', 'srr'),
        ('p', 'and the two boundary conditions \u03c3_{rr}(a) = 0 (traction-free wall, where G(a) = 0) and u(R) = 0 '
              '(clamped outer boundary) fix the constants:'),
        E(r'C_2=\frac{C_1a^2}{m-\lambda},\qquad '
          r'C_1=-\,g_T\,F(t)\left[\frac{R^2-a^2}{2m}+\frac{a^2}{m-\lambda}\right]^{-1},\qquad '
          r'F(t)=\int_a^R r\,\theta(r,t)\,\mathrm{d}r', 'constants'),
        ('p', 'Finally, substituting Eqs. (@@eq:usol@@) and (@@eq:constants@@) into the second of Eq. (@@eq:isotress@@) and '
              'using m \u2212 \u03bb = 2\u03bc and m \u2212 \u03bc = \u03bb + \u03bc gives the wall hoop stress'),
        E(r'\sigma_{\theta\theta}(a,t)=-\,2\mu\,g_T\,p(t)\;-\;'
          r'\frac{2(\lambda+m)\,g_T\,F(t)}{R^{2}+(\lambda+m)\,a^{2}/(2\mu)}', 'local'),
        ('p', 'which is the closed form used as the isotropic reference in Sections 5 and 6. The first term is local and instantaneous: it is the stress '
              'produced by constraining the thermal strain of the material at the wall, and it does not depend on the '
              'temperature field away from the wall at all, hence not on the conduction law. The conduction law enters only '
              'through F(t), and the ratio of the second term to the first is'),
        E(r'\frac{\lambda+m}{\mu}\,\frac{F(t)}{p(t)\,R^{2}}\;\lesssim\;'
          r'\frac{\lambda+m}{\mu}\,\frac{\delta_{th}}{a}\left(\frac{a}{R}\right)^{2}', 'ratio'),
        ('p', f'where \u03b4_{{th}} is the thickness of the heated layer; for \u03b4_{{th}} of order a, R = 80a and the Lam\u00e9 '
              f'constants of the isotropic control (\u03bb = {C["C12"]:.0f} GPa, \u03bc = {C["C66"]:.0f} GPa) the prefactor '
              f'(\u03bb+m)/\u03bc = {(LAM+M_LAME)/MU:.2f} and (a/R)\u00b2 = 1.6\u00d710^{{\u22124}}, so the far-field term is below '
              f'10^{{\u22123}} of the local term \u2014 the wall stress is a local response to 0.1%. For the same constants '
              f'\u03b3_{{T}} = {GAMMA_T/1e6:.4f} MPa/K, g_{{T}} = {G_T:.3e} 1/K and'),
        E(r'-\,2\mu\,g_T=-\,0.985\;\mathrm{MPa/K}', 'localnum'),
        ('p', 'the number used as the isotropic reference in Sections 5 and 6. The same expression shows what to expect for '
              'the anisotropic crystal. There the closed form is not available, because the tangential stiffness at a point '
              'of the wall depends on the direction of the tangent, so the wall hoop stress is not a single scalar multiple '
              'of p(t); but Eqs. (@@eq:sigscale@@) and (@@eq:local@@) together say that the wall stress is \u2016\u03b2\u2016 '
              'times a dimensionless factor of order unity that depends on the stiffness anisotropy and on the angle. That '
              'is the form in which the elliptical-cavity results are reported in Section 6.'),
        ('h2', '3.4 Bound on the thermoelastic feedback'),
        ('p', 'The coupling term of Eq. (@@eq:energy@@) is the only nonlinearity-free but still two-way link between the '
              'fields: the temperature drives the stress and the strain rate feeds back into the heat equation. Its size '
              'relative to the storage term \u03c1c_{p}\u03b8\u0307 is, from Eq. (@@eq:ehat@@), of order \u03b4 times the ratio of '
              'the strain rate to the temperature rate in dimensionless units, i.e. of order \u03b4 when the two evolve on '
              'the same time scale. This motivates the criterion used in Section 6.4: the feedback is negligible if '
              'the relative change of the temperature field when the coupling term is removed satisfies'),
        E(r'\frac{|\Delta\theta|}{|\theta|}\;\leq\;5\delta', 'feedback'),
        ('p', f'with the factor five a margin chosen before the runs, not fitted to them. For the parameters of @@tab:params@@, '
              f'\u03b4 = {DELTA:.3e} and 5\u03b4 = {5*DELTA:.3e}. A bound of this kind is an order-of-magnitude statement, not a '
              f'theorem: it is used to decide whether the coupling has to be resolved, and the decision is then checked '
              f'numerically by switching the coupling off (Section 6.4).'),
        ('h2', '3.5 What these results do and do not establish'),
        ('p', 'Equation (@@eq:sigscale@@) is exact within the model and fixes the parameter dependence of every number '
              'reported below; Eq. (@@eq:collapse@@) is exact in the \u03b5 = \u03b4 = 0 limit and is used as the null '
              'hypothesis for the thermal-memory runs; Eq. (@@eq:local@@) is exact for the isotropic circle and is used both '
              'as a reference solution and as the interpretation of the wall-stress peak. None of the three is a '
              'prediction about \u03b2-Ga\u2082O\u2083: Eq. (@@eq:local@@) is derived for an isotropic solid, '
              'Eq. (@@eq:collapse@@) for the quasi-static uncoupled limit, and Eq. (@@eq:feedback@@) is an order-of-magnitude '
              'criterion. Their role is to make the numerical experiment interpretable, and to say in advance which '
              'outcome would be surprising.')
    ]

    # ---- splice the legacy paragraphs into the new subsections
    def _after(heading):
        return next(k for k, b in enumerate(out) if b[0] == 'h2' and b[1] == heading) + 1
    if p_scaling is not None:
        out.insert(_after('3.2 The collapse identity and its two corrections'), p_scaling)
    if p_local_intro is not None:
        out.insert(_after('3.3 Local response of the circular cavity in an isotropic solid'), p_local_intro)
    if p_local_close is not None:
        out.insert(_after('3.4 Bound on the thermoelastic feedback') - (1 if p_local_intro is not None else 0), p_local_close)
    return out
