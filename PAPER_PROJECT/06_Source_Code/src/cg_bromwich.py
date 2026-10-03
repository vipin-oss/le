"""cg_bromwich.py — single-pulse, zero-initial-condition time response from frequency-domain
transfer values, by Bromwich (complex-frequency) inversion.            [added 2026-10-01, Phase 7]

Why (see 05_Numerical_Method/NUMERICAL_METHOD_V2.md): the handoff's `cg_transient.synthesize`
(irfft of H(w_k)*FFT(pulse)) returns the PERIODIC STEADY STATE of a pulse TRAIN (period T), not the
response of a quiescent medium to ONE pulse.  Here the same linear frequency-domain operator is
evaluated on the vertical line Re(s) = gamma > 0 of the Laplace plane and inverted with the standard
trapezoidal Bromwich sum

    y(t) = exp(gamma t)/T * [ Y(gamma) + 2 Re sum_{k=1..K} Y(gamma + i w_k) exp(i w_k t) ],   w_k = 2 pi k / T,

Y(s) = H(s) P(s).  H(s) is the transfer function solved with unit wall amplitude by
`HarmonicSolver.solve(w)` at the COMPLEX frequency  w = -i s / t_th  (the solver's convention is exp(+i w t),
so i*w = s, w^2 = -s^2).  P(s) is the two-sided Laplace transform of the wall pulse

    p(t) = exp(-((t-t0)/tw)^2)  for all real t  (medium at rest as t -> -infinity):
    P(s) = sqrt(pi) tw exp((s tw/2)^2 - s t0)                          (entire function of s)

All times are dimensionless (units of t_th = a^2/kappa_bar).  Alias error of the periodised inverse is
~ exp(-gamma T) * |y(t+T)| (n>=1 images) and exp(+gamma T)*|y(t-T)| (n<=-1 images; negligible because the
Gaussian pre-history is ~0 for t < t0 - 5 tw); roundoff growth is exp(gamma t).  Defaults T=20, gamma=0.9:
exp(-18) = 1.5e-8; validity 0 <= t <= T - (t0 + 2.5*tw) = 14.5 for the baseline tw = 1.2 (11.5 for
tw = 2.4: the bound tracks the pulse width, so wide-pulse runs are read only inside the peak window).  K is chosen so that |P(s_K)|/|P(s_0)| < eps.
The real-system symmetry Y(conj(s)) = conj(Y(s)) (real K, Q, beta, rho, cp; NO hysteretic damping) is used.
"""
import numpy as np


class BromwichPlan:
    def __init__(self, T=20.0, gamma=0.9, t0=2.5, tw=1.2, eps=1e-10):
        self.T, self.gamma, self.t0, self.tw, self.eps = float(T), float(gamma), float(t0), float(tw), float(eps)
        wmax = np.sqrt(self.gamma ** 2 + 4.0 * np.log(1.0 / self.eps) / self.tw ** 2)
        self.K = int(np.ceil(wmax * self.T / (2.0 * np.pi)))
        self.k = np.arange(self.K + 1)
        self.omega = 2.0 * np.pi * self.k / self.T                 # dimensionless angular frequency (1/t_th)
        self.s = self.gamma + 1j * self.omega                      # dimensionless Laplace variable s*t_th
        self.P = np.sqrt(np.pi) * self.tw * np.exp((self.s * self.tw / 2.0) ** 2 - self.s * self.t0)
        self.weights = np.where(self.k == 0, 1.0, 2.0)

    @property
    def n_solves(self):
        return self.K + 1

    @property
    def t_valid_max(self):
        """Largest time for which the backward image e^{+gamma*T}*y(t-T) is negligible.  A Gaussian pulse
        has no compact support, so the bound follows from the pulse width rather than from causality:
        t <= T - (t0 + 2.5*tw), i.e. 2.5 widths of pre-history, where the image is exp(-6.25) ~ 2e-3 of
        the peak and e^{+gamma*T} * that is still far below the forward alias e^{-gamma*T}.  The previous
        hard-coded T - 5.5 was this expression for the baseline tw = 1.2 and was too generous for wider
        pulses (tw = 2.4 gives 11.5, not 14.5), which is the case used in the locality test.
        """
        return self.T - (self.t0 + 2.5 * self.tw)

    def w_phys(self, t_th):
        """Complex angular frequencies (rad/s) for HarmonicSolver.solve (exp(+i w t)): w = -i s / t_th."""
        return -1j * self.s / float(t_th)

    def synth(self, H, t):
        """H: complex array (K+1, ...) of unit-wall-amplitude transfer values at s_k.
        t: 1-D array of dimensionless times (0 <= t <= t_valid_max recommended).
        Returns real array (..., len(t))."""
        H = np.asarray(H)
        sh = (-1,) + (1,) * (H.ndim - 1)
        Y = H * (self.P * self.weights).reshape(sh)
        E = np.exp(1j * np.outer(self.omega, np.asarray(t, float)))      # (K+1, nt)
        y = np.tensordot(Y, E, axes=(0, 0))                              # (..., nt)
        return (np.exp(self.gamma * np.asarray(t, float)) / self.T * y).real

    def pulse(self, t):
        t = np.asarray(t, float)
        return np.exp(-(((t - self.t0) / self.tw) ** 2))

    def describe(self):
        return dict(T=self.T, gamma=self.gamma, K=self.K, n_solves=self.n_solves, eps=self.eps,
                    t0=self.t0, tw=self.tw, alias=float(np.exp(-self.gamma * self.T)),
                    t_valid_max=self.t_valid_max, growth_at_12=float(np.exp(self.gamma * 12.0)))


def parabolic_peak(t, y):
    """Refine the extremum of |y| near its sample maximum by a 3-point parabola. Returns (t*, y*)."""
    i = int(np.argmax(np.abs(y)))
    if i == 0 or i == len(y) - 1:
        return float(t[i]), float(y[i])
    y0, y1, y2 = y[i - 1], y[i], y[i + 1]
    den = (y0 - 2.0 * y1 + y2)
    if den == 0.0:
        return float(t[i]), float(y1)
    d = 0.5 * (y0 - y2) / den
    h = t[i + 1] - t[i]
    return float(t[i] + d * h), float(y1 - 0.25 * (y0 - y2) * d)
