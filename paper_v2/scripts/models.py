"""Heat-flux template and dispersion relations used for the figures.

Template (linear, isotropic, uniform reference temperature T0):
    q + tau_q q' = -k (grad T + tau_T grad T') - ks (grad v + tau_v grad v'),  v' = T.
Energy balance:  rho cv T' + beta T0 div u' = - div q.
Plane waves exp(i(k x - w t)); s = -i w.
"""
import numpy as np

# model parameter sets in the template: (k, ks, tau_q, tau_T, tau_v)
def model(name, tau=1.0):
    m = {
      'Fourier': dict(k=1.0, ks=0.0, tq=0.0, tT=0.0, tv=0.0),
      'LS':      dict(k=1.0, ks=0.0, tq=tau, tT=0.0, tv=0.0),
      'DPL':     dict(k=1.0, ks=0.0, tq=tau, tT=0.5*tau, tv=0.0),
      'GN-II':   dict(k=0.0, ks=1.0, tq=0.0, tT=0.0, tv=0.0),
      'GN-III':  dict(k=1.0, ks=1.0, tq=0.0, tT=0.0, tv=0.0),
      'MGT':     dict(k=1.0, ks=1.0, tq=tau, tT=0.0, tv=0.0),
    }
    return m[name]

def G(s, p):
    """q^ = -G(s) dT^/dx  (scalar thermal problem, no coupling)."""
    return (p['k']*(1+p['tT']*s) + p['ks']*(1+p['tv']*s)/s) / (1+p['tq']*s)

def k_thermal(w, p, rcv=1.0):
    """complex wavenumber (Im k >= 0) of the uncoupled thermal branch."""
    s = -1j*np.asarray(w, dtype=complex)
    k2 = -s*rcv/G(s, p)
    kk = np.sqrt(k2)
    kk = np.where(kk.imag < 0, -kk, kk)
    return kk

def coupled_k2(w, p, rho=1.0, rcv=1.0, c1=1.0, beta2T0=0.0):
    """Roots K=k^2 of the 1D coupled longitudinal dispersion polynomial
         (rho c1^2 K - rho w^2)(s rcv + G(s) K) + beta2T0 s K = 0,  s=-i w
       (symbolically checked against the field equations, see scripts/check_dispersion.py)."""
    s = -1j*complex(w)
    g = G(s, p)
    a = rho*c1**2*g
    b = rho*c1**2*s*rcv - rho*w**2*g + beta2T0*s
    c = -rho*w**2*s*rcv
    disc = np.sqrt(b*b - 4*a*c)
    return (-b + disc)/(2*a), (-b - disc)/(2*a)
