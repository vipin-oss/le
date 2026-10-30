"""Coupling constants for representative solids (rounded handbook-type values at ~300 K; the reader should substitute
values for the specimen at hand).  Outputs ../tables/materials.tex"""
import numpy as np
T0=300.0
# name: rho [kg/m3], cp [J/kg/K] (used as c), k [W/m/K], alpha_T [1/K], E [GPa], nu
M={'Aluminium':(2700,900,237,23e-6,70,0.33),
   'Copper':(8960,385,400,17e-6,120,0.34),
   'Silicon':(2330,700,150,2.6e-6,160,0.22),
   'Steel (carbon)':(7850,490,50,12e-6,200,0.29),
   'Fused silica':(2200,740,1.4,0.5e-6,73,0.17)}
rows=[]
for n,(rho,c,k,al,E,nu) in M.items():
    E*=1e9; lam=E*nu/((1+nu)*(1-2*nu)); mu=E/(2*(1+nu)); L=lam+2*mu
    c1=np.sqrt(L/rho); beta=(3*lam+2*mu)*al
    eps=beta**2*T0/(rho**2*c*c1**2)
    wstar=rho*c*c1**2/k; fstar=wstar/2/np.pi
    alpha=k/(rho*c)
    rows.append((n,c1,eps,fstar,alpha))
    print(n,f'c1={c1:.0f} eps={eps:.4f} f*={fstar:.3e} Hz  alpha={alpha:.2e}')
tex=[r'\begin{tabular}{@{}lrrrr@{}}\toprule',r'Material & $c_1$ (m/s) & $\varepsilon$ & $f_*=\omega_*/2\pi$ (Hz) & $\alpha=k/\rho c$ (m$^2$/s)\\\midrule']
for n,c1,eps,f,al in rows:
    tex.append(f'{n} & {c1:.0f} & {eps:.2g} & ${f/10**int(np.floor(np.log10(f))):.1f}\\times10^{{{int(np.floor(np.log10(f)))}}}$ & ${al/10**int(np.floor(np.log10(al))):.1f}\\times10^{{{int(np.floor(np.log10(al)))}}}$\\\\')
tex+= [r'\bottomrule\end{tabular}']
open('../tables/materials.tex','w').write('\n'.join(tex))
