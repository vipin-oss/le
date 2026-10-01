"""cg_transient.py — pulse spectrum + Fourier synthesis (shared by run scripts).
Units: SI; the run scripts define t_th etc.  Convention:
  transfer H(w) solved with wall amplitude 1 (exp(+i w t)); pulse sampled on the DFT grid;
  time series = irfft( H(k)*fft(pulse)[k] , N )  for k = 0..N/2.
Frequencies beyond w_cut are NOT solved: filled with 0 (pulse spectrum < 1e-11 there).
"""
import numpy as np

def make_pulse(T, Nt, t0, tw):
    t = np.arange(Nt) * (T / Nt)
    th = np.exp(-((t - t0) / tw) ** 2)
    TH = np.fft.fft(th)                      # length Nt
    return t, th, TH

def freq_grid(T, Nt):
    """DFT angular frequencies for irfft half-spectrum k=0..Nt//2."""
    dt = T / Nt
    k = np.arange(Nt // 2 + 1)
    w = 2 * np.pi * k / T
    return w

def synthesize(H_half, TH, Nt):
    F = np.zeros(Nt // 2 + 1, dtype=complex)
    n = min(len(H_half), Nt // 2 + 1)
    F[:n] = H_half[:n] * TH[:n]
    return np.fft.irfft(F, n=Nt)

def gaussian_spectrum(w, t0, tw):
    """Analytic FT of exp(-((t-t0)/tw)^2) (continuous), for truncation diagnostics."""
    return 0.5 * tw * np.sqrt(np.pi) * np.exp(-(w * tw / 2.0) ** 2) * np.exp(-1j * w * t0)
