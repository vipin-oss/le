# FULLTEXT_FINDINGS_09 — Laplace inversion sources (supervisor read, handler-supplied PDFs)
Status: PRIMARY-SOURCE-CHECKED (text extracted and read; no PDF/text committed).

## F28 Dubner & Abate (1968)
- Identity: H. Dubner, J. Abate, "Numerical Inversion of Laplace Transforms by Relating Them to the Finite Fourier Cosine Transform", J. ACM 15(1), Jan 1968, pp. 115-123 (printed in PDF). DOI 10.1145/321439.321446 (file name matches; Crossref check still owed to Arena).
- Method: f real, f(t)=0 for t<0; h(t)=e^{-at}f(t); Re F(s)=int e^{-at}f(t)cos(wt)dt (eq 3). Reflection of h on (nT,(n+1)T) gives even 2T-periodic g_n; summing over n gives Fourier cosine series (eq 9-10) with A(w_k)=Re F(a+ik pi/T).
- Working formula (eq 15): f(t) ~ (e^{at}/T)[ Re F(a)/2 + sum_{k>=1} Re F(a + i k pi/T) cos(k pi t/T) ], valid on 0<t<T/2. It is a trapezoidal rule on the cosine inversion integral (eq 4).
- Error (eq 14): sum_{n>=1} e^{-2aTn}[f(2nT+t)+e^{2at}f(2nT-t)]. If |f|<=C: error < C e^{-aT+at} cosh(at)/sinh(aT) (eq 16), i.e. O(C e^{-aT}); aT=10 gives ~C*1e-5. If |f|<=C t^m: error ~ C(1.5T)^m e^{-aT} (eq 17). Choose T=2 t_max. Series truncation error ~ size of last retained term.
- Tests: f=(t/2)sin t (aT=15,N=1000 and aT=10,N=100), damped sine, unit step U(t-25).
- Caveat for manuscript: Re F only, f real; oscillatory/step-like f degrade; the 1968 error bounds assume no singularities to the right of the origin (translation allowed).

## F29 Stehfest (1970)
- Identity: H. Stehfest, "Algorithm 368: Numerical inversion of Laplace transforms [D5]", Commun. ACM 13(1), Jan 1970, pp. 47-49 (printed; the PDF also carries pp. 50-54 of other items). DOI 10.1145/361953.361969 (file name matches; Crossref check owed).
- Method: Gaver expectation R_n=int F(t) f_n(a,t)dt with f_n(a,t)=a (2n)!/(n!(n-1)!) (1-e^{-at})^n e^{-nat}; linear combination of R_n (Salzer-type) with K=N/2, a=ln2/T.
- Working formula: F_a = (ln 2/T) sum_{i=1}^{N} V_i P(i ln2 / T), N EVEN, V_i = (-1)^{N/2+i} sum_{k=floor((i+1)/2)}^{min(i,N/2)} k^{N/2}(2k)! / [(N/2-k)! k! (k-1)! (i-k)! (2k-i)!].
- Behaviour: V_i depend on N only (compute once); only real values of P(s) on the real axis are needed; accuracy rises with N until rounding errors dominate (V_i grow; inversion is unbounded), optimum N rises with machine digits. Gaver extrapolation needs N a power of 2 and is less accurate for the same N.
- Table I shows failures: oscillatory/sine-type and sqrt tests lose accuracy at larger T (e.g. P=1/s^... vs sin test errors grow), plus discontinuous cases.
- Caveat for manuscript: poor for oscillatory or discontinuous f (typical of wave problems and thermal-shock fronts); use higher precision arithmetic for large N. Use for smooth diffusive-type thermal responses; for wave fronts prefer Dubner-Abate/Durbin-type Fourier methods.

## Readiness
Section 8 gains two primary sources (now 3 with Brave's prior one). Still need Honig-Hirdes 1984 or Durbin 1974 if Brave can obtain them; do not claim "comparison of methods" beyond these papers.
