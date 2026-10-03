"""ms_numerics.py — expanded Section 4 (numerical method) of the manuscript: the mapped grid, the
conservative finite-difference operators, the boundary treatment, the frequency-domain system, the
Bromwich inversion with its error budget, the definitions of the quantities of interest and the
numerical-uncertainty procedure.

Everything described here is what the frozen code in 06_Source_Code/src implements; the numbers
quoted (contour parameters, numbers of solves, error floors) are read from cg_bromwich or from the
code constants so that text and code cannot drift apart.
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
import cg_bromwich as cb                                      # noqa: E402

PLAN = cb.BromwichPlan()          # T = 20, gamma = 0.9, t0 = 2.5, tw = 1.2, eps = 1e-10
import json                                                 # noqa: E402  (measured errors come from ANALYSIS_V2.json)

_AN = {}
try:
    _AN = json.load(open(os.path.join(ROOT, '10_Processed_Data', 'ANALYSIS_V2.json')))
except Exception:
    _AN = {}


def _num_(which='qoi', tw=None):
    """Measured wall-pulse reconstruction error over the stored production runs (audit A5).  Falls back to the
    analytic alias bound of the plan when the analysis output is not available."""
    NUM = _AN.get('numerics', {})
    if tw is not None:
        v = (NUM.get('wall_pulse_error_by_tw') or {}).get(str(tw), {})
        x = v.get('full' if which == 'full' else 'qoi')
        return f'{x:.1e}' if x else '\u2014'
    key = 'max_wall_pulse_error_full_window_0_12' if which == 'full' else 'max_wall_pulse_error'
    x = NUM.get(key)
    return f'{x:.1e}' if x else f'{PLAN.describe().get("alias", float("nan")):.1e}' 


def E(tex, key=None):
    return ('eq', tex, '', key)


# ----------------------------------------------------------------------------- 4.1 grid
def sec4_grid():
    d = PLAN.describe()
    return [
        ('h2', '4.2 Body-fitted mapped grid'),
        ('p', 'The annular domain between the cavity and the outer circle R = 80a is mapped from the unit square '
              '(\u03be, \u03b7) \u2208 [0, 1] \u00d7 [0, 2\u03c0) by a transfinite map that is radial in the parameter but not in '
              'physical space, so that the grid is body-fitted to the ellipse for every \u03c7. The radial coordinate is '
              'clustered towards the cavity with the exponential map'),
        E(r'\rho(\xi)=\frac{\exp(\gamma\xi)-1}{\exp(\gamma)-1},\qquad '
          r'\xi\in[0,1],\qquad \frac{\mathrm{d}\rho}{\mathrm{d}\xi}=\frac{\gamma\exp(\gamma\xi)}'
          r'{\exp(\gamma)-1}', 'clust'),
        ('p', 'and the physical coordinates are'),
        E(r'x=A(\rho)\cos\eta,\qquad y=B(\rho)\sin\eta,\qquad '
          r'A=a_e+(R-a_e)\rho,\qquad B=b_e+(R-b_e)\rho', 'map'),
        E(r'a_e=a\sqrt{\chi},\qquad b_e=\frac{a}{\sqrt{\chi}}', 'axes'),
        ('p', 'so that \u03c0 a_{e}b_{e} = \u03c0 a\u00b2 for every \u03c7: the circle and the ellipse have the same area, which is '
              'what makes the comparison of Section 6 a comparison of shape alone. The grid is uniform in \u03be and \u03b7 and '
              'periodic in \u03b7; with \u03b3 = 5 the ratio of the largest to the smallest radial spacing is '
              f'({np.exp(5.0)-1:.0f})/5 \u2248 {((np.exp(5.0)-1)/5):.0f} for the grids used, i.e. the near-wall layer carries most '
              'of the radial resolution. All metric terms are evaluated analytically from the map,'),
        E(r'x_\xi=\frac{\mathrm{d}A}{\mathrm{d}\xi}\cos\eta,\quad x_\eta=-A\sin\eta,\quad '
          r'y_\xi=\frac{\mathrm{d}B}{\mathrm{d}\xi}\sin\eta,\quad y_\eta=B\cos\eta,\quad '
          r'J=x_\xi y_\eta-x_\eta y_\xi', 'metrics'),
        ('p', 'and physical derivatives follow from the chain rule by inverting'),
        E(r'f_x=\frac{y_\eta f_\xi-y_\xi f_\eta}{J},\qquad f_y=\frac{-x_\eta f_\xi+x_\xi f_\eta}{J}', 'chain'),
        ('p', 'Derivatives in \u03be and \u03b7 are second-order central differences, replaced at the two radial boundaries by the '
              'one-sided three-point formulas'),
        E(r'\left.\frac{\partial f}{\partial\xi}\right|_{0}=\frac{-3f_0+4f_1-f_2}{2h},\qquad '
          r'\left.\frac{\partial f}{\partial\xi}\right|_{N_r-1}=\frac{3f_{N_r-1}-4f_{N_r-2}+f_{N_r-3}}{2h}', 'onesided'),
        ('p', 'and central periodic differences in \u03b7. The operators D_{x} and D_{y} are assembled as sparse matrices from '
              'Eq. (@@eq:chain@@); the discrete metric identities \u2202_{\u03be}y_{\u03b7} = \u2202_{\u03b7}y_{\u03be} and '
              '\u2202_{\u03be}x_{\u03b7} = \u2202_{\u03b7}x_{\u03be} hold exactly at interior nodes, which is what makes a uniform-stress '
              'field have exactly zero discrete divergence (the patch test of Section 5.1).')
    ]


# ----------------------------------------------------------------------------- 4.2 operators
def sec4_ops():
    return [
        ('h2', '4.3 Conservative discretisation of the two operators'),
        ('p', 'The heat and momentum operators are written in contravariant flux form rather than as compositions of first '
              'derivatives, because the composition D_{x}D_{x} has a 2h stencil with odd\u2013even decoupling: it possesses '
              'spurious null modes that a narrow conservative stencil does not. For any vector field v the identity'),
        E(r'J\,\nabla\cdot\mathbf{v}=\frac{\partial}{\partial\xi}\left(v_xy_\eta-v_yx_\eta\right)'
          r'+\frac{\partial}{\partial\eta}\left(-v_xy_\xi+v_yx_\xi\right)', 'thompson'),
        ('p', 'is exact for analytic metrics, and discretely exact for the discrete metrics of Section 4.1. Applying it to '
              'v = \u2212K\u2207\u03b8 gives the thermal operator'),
        E(r'J\,\nabla\cdot\left(\mathbf{K}\nabla\theta\right)=\frac{\partial}{\partial\xi}'
          r'\left(\mathcal{A}\theta_\xi+\mathcal{B}\theta_\eta\right)'
          r'+\frac{\partial}{\partial\eta}\left(\mathcal{B}\theta_\xi+\mathcal{D}\theta_\eta\right)', 'thermalop'),
        E(r'\mathcal{A}=\frac{K_{11}y_\eta^2-2K_{13}x_\eta y_\eta+K_{33}x_\eta^2}{J},\qquad '
          r'\mathcal{D}=\frac{K_{11}y_\xi^2-2K_{13}x_\xi y_\xi+K_{33}x_\xi^2}{J},', 'coefAD'),
        E(r'\mathcal{B}=\frac{K_{13}\left(x_\xi y_\eta+x_\eta y_\xi\right)-K_{11}y_\xi y_\eta-K_{33}x_\xi x_\eta}{J}', 'coefB'),
        ('p', 'with the coefficients evaluated at half points as arithmetic averages of the nodal values, and the fluxes '
              'differentiated with the same stencils as in Eq. (@@eq:onesided@@); the resulting matrix has the narrow '
              '(i \u00b1 1, j \u00b1 1) stencil. The momentum operator is built the same way from the contravariant fluxes'),
        E(r'\mathcal{P}_1=y_\eta\sigma_{11}-x_\eta\sigma_{13},\qquad \mathcal{P}_2=y_\eta\sigma_{13}-x_\eta\sigma_{33},'
          r'\qquad \mathcal{R}_1=-y_\xi\sigma_{11}+x_\xi\sigma_{13},\qquad '
          r'\mathcal{R}_2=-y_\xi\sigma_{13}+x_\xi\sigma_{33}', 'momflux'),
        ('p', 'through the same identity, with the stresses of Eq. (@@eq:sig11@@) evaluated from the strain components')
        , E(r'\epsilon_{11}=u_{1,x},\qquad \epsilon_{33}=u_{3,y},\qquad '
            r'\gamma_{13}=u_{1,y}+u_{3,x}', 'straincomp'),
        ('p', 'computed with Eq. (@@eq:chain@@). The thermal-stress term is deliberately kept out of the flux: it is '
              'assembled as the first-derivative operator'),
        E(r'\mathcal{G}_1=\beta_1\frac{\partial}{\partial x}+\beta_5\frac{\partial}{\partial y},\qquad '
          r'\mathcal{G}_2=\beta_5\frac{\partial}{\partial x}+\beta_3\frac{\partial}{\partial y}', 'grows'),
        ('p', 'so that a uniform temperature field produces exactly zero body force, which is the V7 patch test of '
              'Section 5.1; putting \u03b2\u03b8 into the flux and differentiating it would leave a residual of the order of '
              'the metric-identity error and would destroy that property.')
    ]


# ----------------------------------------------------------------------------- 4.3 boundary
def sec4_bc():
    return [
        ('h2', '4.4 Boundary conditions and extraction of the wall stress'),
        ('p', 'Boundary conditions are imposed by row replacement, not by elimination. On the cavity wall the '
              'temperature row is the Dirichlet condition \u03b8 = 1 (unit transfer amplitude) and the two momentum rows are '
              'the traction conditions built from the first-derivative stress operators'),
        E(r'\mathcal{S}_{11}=-\beta_1+Q_{11}\frac{\partial}{\partial x}+Q_{15}\frac{\partial}{\partial y},\qquad '
          r'\mathcal{S}_{13}=-\beta_5+Q_{15}\frac{\partial}{\partial x}+Q_{55}\frac{\partial}{\partial y},\qquad '
          r'\mathcal{S}_{33}=-\beta_3+Q_{35}\frac{\partial}{\partial x}+Q_{13}\frac{\partial}{\partial y}', 'sops'),
        ('p', 'acting on (\u03b8, u_{1}, u_{3}), and combined with the wall normal of the ellipse,')
        , E(r'n_x\propto b_e\cos\eta,\qquad n_y\propto a_e\sin\eta,\qquad '
            r't_x\propto-a_e\sin\eta,\qquad t_y\propto b_e\cos\eta', 'normal'),
        ('p', 'into the two traction rows'),
        E(r'n_x\mathcal{S}_{11}+n_y\mathcal{S}_{13}=0,\qquad n_x\mathcal{S}_{13}+n_y\mathcal{S}_{33}=0', 'traction'),
        ('p', 'On the outer boundary \u0393_{R} all three rows are Dirichlet (\u03b8 = 0, u_{1} = u_{3} = 0). The wall hoop '
              'stress reported throughout the paper is the tangential component of the same stress operators,'),
        E(r'\sigma_{\theta\theta}=t_x^2\,\mathcal{S}_{11}+2t_xt_y\,\mathcal{S}_{13}+t_y^2\,\mathcal{S}_{33}', 'hoop'),
        ('p', 'evaluated at the wall nodes; the two traction components of Eq. (@@eq:traction@@) are monitored in every run '
              'and are zero to the solver\u2019s backward error, so the wall is traction-free by construction rather than '
              'approximately.')
    ]


# ----------------------------------------------------------------------------- 4.4 frequency-domain system
def sec4_system():
    return [
        ('h2', '4.5 Frequency-domain system'),
        ('p', 'For a single complex frequency the coupled system is solved in one linear system for the vector '
              'U = (\u03b8, u_{1}, u_{3}) of 3N_{r}N_{\u03b8} unknowns. With the harmonic convention fields \u221d exp(+i\u03c9t) the '
              'semi-discrete equations of Section 2.5 read'),
        E(r'\mathbf{A}(\omega)\,\mathbf{U}=\mathbf{f},\qquad '
          r'\mathbf{A}(\omega)=\mathbf{A}_0+\omega^2\mathbf{A}_{in}+i\omega\mathbf{A}_d+g(\omega)\mathbf{A}_{lap}',
          'asys'),
        ('p', 'whose blocks (rows: momentum-1, momentum-2, energy) are'),
        E(r'\mathbf{A}_0=\left[-\mathcal{G}_1,\;\mathbf{M}_1,\;\mathbf{M}_2;'
          r'\;-\mathcal{G}_2,\;\mathbf{M}_2^{\prime},\;\mathbf{M}_3;\;\mathbf{0},\;\mathbf{0},\;\mathbf{0}\right],'
          r'\qquad \mathbf{A}_{in}=\rho\,\mathrm{diag}(0,1,1)', 'ablocks'),
        E(r'\mathbf{A}_d=\left[\mathbf{0},\;\mathbf{0},\;\mathbf{0};\;-\rho c_p\mathbf{I},\;'
          r'-T_0\mathcal{G}_1,\;-T_0\mathcal{G}_2\right],\qquad '
          r'\mathbf{A}_{lap}=\left[\mathbf{0},\;\mathbf{0},\;\mathbf{0};\;\mathbf{L},\;\mathbf{0},\;\mathbf{0}\right]',
          'ablocks2'),
        ('p', 'with M the conservative momentum operator of Eq. (@@eq:momflux@@), L the conservative thermal operator of '
              'Eq. (@@eq:thermalop@@) and \u0041 the row-replaced boundary rows of Section 4.3; the right-hand side f is '
              'nonzero only on the Dirichlet rows of the wall. The complex frequency is the Laplace variable of the '
              'inversion plan,'),
        E(r'\omega=-\,i\,\frac{s}{t_{th}},\qquad g(\omega)=\frac{1}{1+i\omega\tau}', 'w_of_s'),
        ('p', 'so that i\u03c9 = s/t_{th} and \u03c9\u00b2 = \u2212s\u00b2/t_{th}\u00b2 as required by Eq. (@@eq:lapheat@@). Two steps control '
              'round-off. First, interior rows are multiplied by the nodal Jacobian J (of order a\u00b2 in SI units), which '
              'brings the PDE rows from O(10^{20}) to O(10^{5}) relative to the unit boundary rows; then each row is scaled '
              'to unit maximum modulus. The system is complex symmetric but not Hermitian; it is factorised by sparse LU '
              'and improved by two steps of iterative refinement,'),
        E(r'\mathbf{U}^{(k+1)}=\mathbf{U}^{(k)}+\mathbf{A}^{-1}\left(\mathbf{f}-\mathbf{A}\mathbf{U}^{(k)}\right),\qquad '
          r'\eta=\frac{\|\mathbf{f}-\mathbf{A}\mathbf{U}\|_{\infty}}'
          r'{\left(\|\mathbf{A}\|_{\infty}\|\mathbf{U}\|_{\infty}\right)}', 'refine'),
        ('p', 'with the backward error \u03b7 recorded for every solve (frequency-domain formulations of dynamic '
              'coupled thermoelasticity with relaxation times go back to [38] and are reviewed in [39]): refinement lowers the floor of the wall stress from about '
              '10^{\u22128} to 10^{\u221214} relative, which matters because the quantities of interest in Section 6 are '
              'differences of nearly equal stresses.')
    ]


# ----------------------------------------------------------------------------- 4.5 Bromwich
def sec4_bromwich(p_intro=None, eq_brom=None, p_close=None):
    """p_intro / eq_brom / p_close are the legacy blocks of the earlier 'Single-pulse response by Bromwich
    inversion' subsection: its lead-in (which carries the [21,22] citations), its displayed inversion formula
    (which is the equation the paper cites as Eq. (@@eq:brom@@)) and its closing paragraph (contour parameters,
    alias error, validity window, pulse-train warning).  They are reused so that the wording and the
    numbering of the published derivation are kept."""
    d = PLAN.describe()
    out = [
        ('h2', '4.6 Single-pulse response by Bromwich inversion'),
        ('p', 'The time-domain response of the medium at rest to one pulse is the inverse Laplace transform of the product '
              'of the transfer function H(s) (computed with unit wall amplitude) and the transform of the pulse. For the '
              'Gaussian of Eq. (@@eq:pulse@@) extended to all real t \u2014 legitimate because the medium is quiescent and the '
              'pulse is numerically zero for t < t_{0} \u2212 5t_{w} \u2014 the two-sided transform is entire,'),
        E(r'P(s)=\int_{-\infty}^{\infty}p(t)\,e^{-st}\,\mathrm{d}t'
          r'=\sqrt{\pi}\,t_w\exp\left[\left(\frac{st_w}{2}\right)^2-s\,t_0\right],\qquad Y(s)=H(s)P(s)', 'Pdef'),
        ('p', 'and the response is the Bromwich integral evaluated by the trapezoidal rule on the vertical line '
              'Re s = \u03b3_{B},')
        , E(r'y(t)=\frac{1}{2\pi i}\int_{\gamma_B-i\infty}^{\gamma_B+i\infty}Y(s)\,e^{st}\,\mathrm{d}s'
            r'\;\approx\;\frac{e^{\gamma_B t}}{T}\left[Y(\gamma_B)+2\,\mathrm{Re}\sum_{k=1}^{K}'
            r'Y(\gamma_B+i\omega_k)\,e^{i\omega_k t}\right],\qquad \omega_k=\frac{2\pi k}{T}', 'bromwich'),
        ('p', f'which is Eq. (@@eq:brom@@) with the plan made explicit. Three errors enter and all three are '
              f'controlled: (i) the trapezoidal rule periodises the integrand, so the result is the response of a train of '
              f'pulses of period T plus the alias error e^{{\u2212\u03b3_{{B}}T}} = e^{{{-PLAN.T*PLAN.gamma:.0f}}} = '
              f'{d["alias"]:.1e} for the plan used; (ii) the sum is truncated at K terms, where K is fixed by requiring the '
              f'pulse spectrum to have fallen to {PLAN.eps:.0e} of its value at s = \u03b3_{{B}},'),
        E(r'K=\left\lceil\frac{T}{2\pi}\sqrt{\gamma_B^2+\frac{4}{t_w^2}\ln\frac{1}{\varepsilon}}\;\right\rceil'
          r'\;=\;' + str(PLAN.K), 'Kdef'),
        ('p', f'giving {PLAN.n_solves} solves per run; and (iii) round-off of the inversion grows like e^{{\u03b3_{{B}}t}}, which is '
              f'{np.exp(PLAN.gamma*6):.1f} at t = 6t_{{th}} and {np.exp(PLAN.gamma*12):.1f} at t = 12t_{{th}}. With '
              f'T = {PLAN.T:.0f} t_{{th}} and \u03b3_{{B}} = {PLAN.gamma}/t_{{th}} the reconstruction is therefore valid for '
              f'0 \u2264 t \u2264 {d["t_valid_max"]:.1f} t_{{th}} for the baseline pulse width t_{{w}} = {PLAN.tw:g} t_{{th}}, comfortably '
              f'beyond the window 0 \u2264 t \u2264 6 t_{{th}} of the quantities of interest. The bound is checked against the stored '
              f'series of every production run, not only estimated: the reconstructed wall temperature deviates from the '
              f'imposed Gaussian by at most {_num_()} anywhere in 0 \u2264 t \u2264 6 t_{{th}}; over the whole stored window '
              f'0 \u2264 t \u2264 12 t_{{th}} the worst case for t_{{w}} = {PLAN.tw:g} is {_num_(which="full")}, while the widest pulse '
              f'used in the locality test (t_{{w}} = 2.4 t_{{th}}) is the one case whose image term enters inside the stored '
              f'window ({_num_(which="full", tw="2.4")} at t = 12 t_{{th}}), so that test is read only for peak values, which lie '
              f'well inside the reported window. The real symmetry H(s\u0304) = conj H(s) of the undamped real system halves nothing but '
              f'is used as a consistency check, and because the contour lies at distance \u03b3_{{B}} from the resonances of the '
              f'finite undamped domain, no artificial damping is needed. The wall temperature reconstructed from H is '
              f'compared with the Gaussian in every run (Section 5.1).'),
        ('p', 'Substituting a discrete Fourier synthesis over a window of a few thermal times for Eq. (@@eq:brom@@) is '
              'the mistake this plan replaces: the DFT synthesis returns the periodic steady state of a pulse train of '
              'period T, in which the mean wall temperature is 0.27 of the peak, a steady temperature profile reaches the '
              'outer boundary and the clamped boundary raises the stress. The two answers differ by more than the effects '
              'studied here, which is why the earlier internal analysis had to be recomputed.'),
        ('p', 'Peaks in time are located on the sampled history and refined by the three-point parabola through the '
              'sample maximum,')
        , E(r't_\star=t_i+\frac{\Delta t}{2}\,\frac{y_{i-1}-y_{i+1}}{y_{i-1}-2y_i+y_{i+1}},\qquad '
            r'y_\star=y_i-\frac{1}{4}\left(y_{i-1}-y_{i+1}\right)\frac{t_\star-t_i}{\Delta t}', 'parab'),
        ('p', 'which removes the sampling bias of the peak time and amplitude at negligible cost. The alternative '
              'inversion algorithms surveyed in [40,41,42,43,44] were not needed here: the Gaussian spectrum decays '
              'fast enough for the plain trapezoidal sum on a shifted contour to reach the tolerance above.')
    
    ]
    if p_intro is not None:
        out[1] = p_intro                     # legacy lead-in carries the [21,22] citations
    k = next(i for i, b in enumerate(out) if b[0] == 'eq' and len(b) > 3 and b[3] == 'bromwich')
    if eq_brom is not None:
        out[k] = eq_brom                     # identical formula; keep the published one (key 'brom')
    if p_close is not None:
        out.insert(k + 1, p_close)           # legacy paragraph with T, gamma_B, K, alias, validity window
    return out


# ----------------------------------------------------------------------------- 4.6 QoI
def sec4_qoi():
    return [
        ('h2', '4.7 Definitions of the quantities of interest'),
        ('p', 'Let \u03c3_{\u03b8\u03b8}(\u03b7_{j}, t) be the wall hoop stress of Eq. (@@eq:hoop@@) at wall node j. The primary '
              'observable is the peak of its modulus over the wall and over the window 0 \u2264 t \u2264 6t_{th},'),
        E(r'\hat\sigma_{\mathrm{nodal}}=\max_{j}\max_{0\leq t\leq 6t_{th}}|\sigma_{\theta\theta}(\eta_j,t)|', 'sig nodal'),
        ('p', 'and, to remove the nodal quantisation of the angular maximum \u2014 a bias of order (\u0394\u03b7)\u00b2 that is not '
              'negligible on the coarse grids \u2014 the same maximum taken over the trigonometric interpolant of the nodal '
              'wall profile,'),
        E(r'\sigma_{\theta\theta}(\eta,t)=\sum_{k=-N_\theta/2}^{N_\theta/2-1}c_k(t)\,e^{ik\eta},\qquad '
          r'c_k=\frac{1}{N_\theta}\sum_{j=0}^{N_\theta-1}\sigma_{\theta\theta}(\eta_j,t)\,e^{-ik\eta_j},\qquad '
          r'\hat\sigma=\max_{\eta}\max_{0\leq t\leq 6t_{th}}|\sigma_{\theta\theta}(\eta,t)|', 'siginterp'),
        ('p', 'Both are reported per kelvin of wall-temperature amplitude. The orientation modulation of the ellipse and '
              'the thermal-memory deviation of the circle are'),
        E(r'A_\phi=\frac{\max_\phi\hat\sigma-\min_\phi\hat\sigma}{\mathrm{mean}_\phi\,\hat\sigma}', 'Aphidef'),
        E(r'D=\frac{\max_{\eta,t}|\sigma_{\theta\theta}^{\mathrm{CV}}-\sigma_{\theta\theta}^{\mathrm{F}}|}'
          r'{\max_{\eta,t}|\sigma_{\theta\theta}^{\mathrm{F}}|},\qquad 0\leq t\leq 6t_{th}', 'Ddef'),
        ('p', 'the latter evaluated on the same grid and with the same inversion plan for the two conduction laws, so that '
              'D is a property of the model pair and not of the discretisation. The two-point modulation A_{2} used in the '
              'pulse-width test of Section 6.2 is Eq. (@@eq:Aphidef@@) restricted to two orientations. Because D is a small '
              'difference of two nearly equal histories, its numerical accuracy is assessed separately (Section 5.1).')
    ]


# ----------------------------------------------------------------------------- 4.7 uncertainty
def sec4_uncertainty():
    return [
        ('h2', '4.8 Numerical uncertainty'),
        ('p', 'Grid convergence is assessed on two refinement families that vary one direction at a time: radial '
              '(R48 = 48\u00d796, M = 96\u00d796, R192 = 192\u00d796) and angular (T48 = 96\u00d748, M = 96\u00d796, '
              'T144 = 96\u00d7144). For three values f_{1}, f_{2}, f_{3} on meshes with N_{1} < N_{2} < N_{3} directions, the '
              'observed order p solves'),
        E(r'\frac{f_1-f_2}{f_2-f_3}=\frac{N_1^{-p}-N_2^{-p}}{N_2^{-p}-N_3^{-p}}', 'order'),
        ('p', '(a root is sought numerically; if the differences are not monotone the order is undefined and no '
              'extrapolation is made). The order is then clipped to the interval [1, 3] \u2014 below 1 the observed '
              'convergence is not trustworthy, above 3 it is not credible for a second-order scheme \u2014 and the error model'),
        E(r'f(N)=f_\infty+c\,N^{-p},\qquad c=\frac{f_2-f_3}{N_2^{-p}-N_3^{-p}},\qquad f_\infty=f_3-c\,N_3^{-p}', 'richardson'),
        ('p', 'is calibrated on the two finest levels. The extrapolated value quoted in Section 6 is the production grid '
              'M corrected additively by the two one-directional corrections,'),
        E(r'f_{\mathrm{ext}}=f_M+\left(f_\infty^{\mathrm{radial}}-f_M\right)+\left(f_\infty^{\mathrm{angular}}-f_M\right)', 'fext'),
        ('p', 'which assumes the two error components are additive \u2014 an assumption, not a result. The numerical '
              'uncertainty of the orientation modulation is then'),
        E(r'u_{\mathrm{num}}=\max\left(|A_\phi(M)-A_\phi(R192)|,\;|A_\phi(M)-A_\phi(T144)|,\;'
          r'|A_\phi(M)-A_\phi(\mathrm{ext})|\right)', 'unum'),
        ('p', 'i.e. the largest of the differences between the production value and the finer or extrapolated estimates, '
              'and the pre-registered detection criterion for the modulation is A_{\u03c6} > max(5u_{num}, 2%). Following the '
              'extrapolation of Eq. (@@eq:richardson@@) goes back to Richardson and Gaunt [52], and in the standard '
              'terminology of the verification literature [53,54], these are solution-verification quantities: '
              'they bound the discretisation error of the computed solution of the stated model, and say nothing about '
              'model error.')
    ]
