"""Scenario table: dimensionless groups for typical applications (rounded handbook inputs of table_materials.py, tau_q=1 ps)."""
import numpy as np
from worked_examples import props, T0   # prints the example numbers too; harmless
tau=1e-12
S=[('Ultrasonic testing','Aluminium',10e6,None),
   ('GHz acoustics','Aluminium',1e9,None),
   ('Picosecond ultrasonics','Aluminium',100e9,None),
   ('Silicon beam, $h=1\\,\\mu$m, at $f_Z$','Silicon',None,1e-6),
   ('Silicon film, $h=20$\\,nm, at $f_Z$','Silicon',None,20e-9),
   ('Copper film, $h=50$\\,nm, at $f_Z$','Copper',None,50e-9)]
rows=[]
for name,mat,f,h in S:
    p=props(mat)
    if f is None: f=np.pi*p['chi']/(2*h**2)
    w=2*np.pi*f; x=w/p['ws']; lt=w*tau; ld=np.sqrt(2*p['chi']/w); lam=p['c1']/f
    verdict='Fourier adequate' if lt<0.1 and x<0.1 else ('lag may matter; check kinetics' if lt<1.5 else 'continuum law questionable')
    rows.append((name,mat,f,x,lt,ld,lam,verdict))
def sci(v): 
    e=int(np.floor(np.log10(v))); return '$%.1f\\times10^{%d}$'%(v/10**e,e)
tex=['\\setlength{\\tabcolsep}{3pt}\\begin{tabular}{@{}p{3.0cm}lrrrrrp{2.3cm}@{}}\\toprule','Scenario & Material & $f$ (Hz) & $\\omega/\\omega_*$ & $\\omega\\tau_q$ & $\\delta_T$ (m) & $\\lambda$ (m) & Assessment\\\\\\midrule']
for n,m,f,x,lt,ld,lam,v in rows: tex.append('%s & %s & %s & %s & %s & %s & %s & %s\\\\'%(n,m,sci(f),sci(x),sci(lt),sci(ld),sci(lam),v))
tex.append('\\bottomrule\\end{tabular}')
open('../tables/scenarios.tex','w').write('\n'.join(tex))
for r in rows: print(r)
