import mpmath as mp, numpy as np
mp.mp.dps=15
tests=[('smooth: $1/(s+1)^2$',lambda s:1/(s+1)**2,lambda t:t*mp.e**(-t),[0.5,2,5,10]),
       ('oscillatory: $1/\\sqrt{s^2+1}$',lambda s:1/mp.sqrt(s**2+1),lambda t:mp.besselj(0,t),[0.5,2,5,10]),
       ('step: $e^{-s}/s$',lambda s:mp.e**(-s)/s,lambda t:mp.mpf(1) if t>1 else mp.mpf(0),[0.5,0.95,1.05,2,5]),
       ('diffusive: $e^{-\\sqrt s}/s$',lambda s:mp.e**(-mp.sqrt(s))/s,lambda t:mp.erfc(1/(2*mp.sqrt(t))),[0.5,2,5,10])]
methods=['talbot','stehfest','dehoog','cohen']
rows=[]
for name,F,f,ts in tests:
    row=[name]
    for m in methods:
        errs=[]
        for t in ts:
            try:
                v=mp.invertlaplace(F,t,method=m); errs.append(abs(float(mp.re(v))-float(f(t))))
            except Exception as e:
                errs.append(float('nan'))
        row.append(np.nanmax(errs) if not all(np.isnan(errs)) else float('nan'))
    rows.append(row); print(row)
def fmt(x): 
    if np.isnan(x): return '--'
    return f'{x:.1e}'.replace('e-0','e$-$').replace('e-','e$-$').replace('e+0','e').replace('e+','e')
lines=[r'\begin{tabular}{@{}lrrrr@{}}\toprule',r'Test function & Talbot & Stehfest & de Hoog & Cohen\\\midrule']
for r in rows: lines.append(r[0]+' & '+' & '.join(fmt(x) for x in r[1:])+r'\\')
lines.append(r'\bottomrule\end{tabular}')
open('../tables/laplace_bench.tex','w').write('\n'.join(lines))
