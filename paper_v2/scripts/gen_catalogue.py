"""Generate the classified literature catalogue (appendix) from refs.bib.
Entries are classified by title keywords only; no content is summarised beyond the title."""
import re,os
root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
t=''.join(open(os.path.join(root,f)).read() for f in ['refs.bib','refs_extra.bib','refs_new.bib'])
ents=[]
for blk in re.split(r'(?m)^@',t)[1:]:
    m=re.match(r'(\w+)\{([^,]+),(.*)',blk,flags=re.S)
    if m and m.group(1).lower() not in ('comment','string'): ents.append((m.group(1),m.group(2),m.group(3)))
def f(b,k):
    m=re.search(r'(?i)\b'+k+r'\s*=\s*',b)
    if not m: return ''
    j=m.end(); o=b[j]
    if o=='{':
        dep=0
        for q in range(j,len(b)):
            dep+=(b[q]=='{')-(b[q]=='}')
            if dep==0: return re.sub(r'\s+',' ',b[j+1:q]).strip()
        return ''
    if o=='"':
        q=b.find('"',j+1); return re.sub(r'\s+',' ',b[j+1:q]).strip()
    m2=re.match(r'[^,}\n]*',b[j:]); return m2.group(0).strip()
rules=[
 ('Second sound, phonon transport and kinetic theory',['second sound','phonon','ballistic','kinetic','guyer','krumhansl','boltzmann','heat pulse','heat transport']),
 ('Dual-phase-lag, three-phase-lag and delay models',['lag','delay','tzou','dual','three-phase']),
 ('Green--Naghdi, Green--Lindsay and extended thermodynamics',['green','naghdi','without energy','extended thermodynamics','generalized','generalised','lord','thermodynamic']),
 ('Moore--Gibson--Thompson and third-order models',['moore','gibson','thompson','third order','third-order','mgt','jordan']),
 ('Fractional and memory-dependent models',['fractional','memory','derivative','caputo','mittag','fractal']),
 ('Nonlocal, gradient and size-dependent theories',['nonlocal','non-local','gradient','size','nano','micro','couple stress','eringen','lattice','atomistic']),
 ('Surface, interface and reflection problems',['rayleigh','surface','reflection','refraction','transmission','interface','half-space','half space','lamb','scatter','incidence','plane wave','plane-wave']),
 ('Piezoelectric, magnetic, porous, micropolar and diffusive coupling',['piezo','magneto','micropolar','void','porous','semiconductor','diffusion','electro','micropolar','dielectric','photo']),
 ('Mathematical analysis, numerics and inversion',['laplace','inversion','numerical','finite','existence','uniqueness','stability','well-posed','asymptotic','spectral','method']),
 ('Foundations, monographs and general thermoelasticity',['thermoelastic','thermoelasticity','elasticity','thermomechanic','continuum','theory']),
]
groups={r[0]:[] for r in rules}; groups['Other related work']=[]
for ty,key,b in ents:
    ti=f(b,'title'); low=ti.lower(); placed=False
    for name,kws in rules:
        if any(k in low for k in kws):
            groups[name].append((key,f(b,'year'),ti,f(b,'journal') or f(b,'booktitle') or f(b,'publisher'))); placed=True; break
    if not placed: groups['Other related work'].append((key,f(b,'year'),ti,f(b,'journal') or f(b,'booktitle') or f(b,'publisher')))
out=[r'\section{Classified catalogue of the cited literature}\label{app:catalogue}',
r'This appendix lists every work in the reference database, grouped by the subject of its title. Works that are not discussed in the main text are included as further reading for the corresponding topic. The grouping is automatic and by title keywords only; it is an aid to locating the literature and does not summarise the content of any paper. Within each group the entries are ordered by year. A work whose title touches several topics appears once, under the first matching group.']
n=0
for name,items in groups.items():
    if not items: continue
    items.sort(key=lambda x:(x[1],x[0]))
    out.append(r'\subsection{'+name+r'}')
    out.append(r'\begin{itemize}\itemsep0pt\small')
    for key,y,ti,jr in items:
        n+=1
        out.append(r'\item \citet{'+key+r'}: \emph{'+ti.replace('{','').replace('}','')+r'}'+(r'; '+jr.replace('{','').replace('}','') if jr else '')+r'.')
    out.append(r'\end{itemize}')
open(os.path.join(root,'sections','appD_catalogue.tex'),'w').write('\n'.join(out)+'\n')
print(n,{k:len(v) for k,v in groups.items()})
