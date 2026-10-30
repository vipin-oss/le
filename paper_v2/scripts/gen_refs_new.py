"""Build refs_new.bib from (a) records fetched from Crossref (refwork/lines.txt: DOI|year|authors|title|journal|vol|pages)
and (b) the verified inventory of the author's own paper library (refwork/inventory_dec.csv; first author only)."""
import re,csv,os,unicodedata
root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
existing=open(os.path.join(root,'refs.bib')).read()+open(os.path.join(root,'refs_extra.bib')).read()
have=set(d.lower() for d in re.findall(r'doi\s*=\s*[{"]([^}"]+)',existing,flags=re.I))
havekeys=set(re.findall(r'@\w+\{([^,]+),',existing))
def ascii_(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
def tex(s):
    s=s.replace('&','\\&').replace('%','\\%').replace('#','\\#').replace('_','\\_')
    s=re.sub(r'<[^>]+>','',s)
    return s
def nt(s): return re.sub(r'[^a-z0-9]','',s.lower())
exist_titles=set(nt(x) for x in re.findall(r'title\s*=\s*[{"]+(.*?)[}"]+,',existing,flags=re.S|re.I))
BLACK=['bio-electrochemical','Experimental support for the lagging','anisotropic piezothermoelastic shell laminates']
used=set(havekeys); out=[]; seen=set(); seen_t=set(exist_titles)
def key(fam,year):
    base=re.sub(r'[^A-Za-z]','',ascii_(fam))+str(year); k=base; i=0
    while k in used: i+=1; k=base+chr(96+i)
    used.add(k); return k
n=0
for line in open(os.path.join(root,'refwork','lines.txt')):
    p=[x.strip() for x in line.rstrip('\n').split(' | ')]
    if len(p)<7: continue
    doi,year,au,ti,jr,vol,pg=p[:7]
    if doi.lower() in have or doi.lower() in seen or nt(ti) in seen_t: continue
    seen.add(doi.lower()); seen_t.add(nt(ti))
    authors=[a.strip() for a in au.split(';') if a.strip()]
    fam=authors[0].split(',')[0]
    bibau=' and '.join(tex(ascii_(a)) if ',' in a else tex(ascii_(a)) for a in authors)
    k=key(fam,year)
    e=[f'@article{{{k},',f'  author = {{{bibau}}},',f'  title = {{{{{tex(ti)}}}}},',f'  journal = {{{tex(jr)}}},',f'  year = {{{year}}},']
    if vol!='NA': e.append(f'  volume = {{{vol}}},')
    if pg!='NA': e.append(f'  pages = {{{pg.replace("-","--") if "--" not in pg else pg}}},')
    e.append(f'  doi = {{{doi}}},'); e.append('  note = {record fetched from Crossref},'); e.append('}')
    out.append('\n'.join(e)); n+=1
csv.field_size_limit(10**9)
m=0
for r in csv.DictReader(open(os.path.join(root,'refwork','inventory_dec.csv'))):
    d=r['doi'].strip().lower(); 
    if not (r['title'] and r['first_author'] and r['year'] and r['journal'] and d): continue
    if d in have or d in seen or nt(r['title']) in seen_t or any(b.lower() in r['title'].lower() for b in BLACK): continue
    seen_t.add(nt(r['title']))
    if not re.match(r'^10\.\d{4,}/',d): continue
    seen.add(d); fam=r['first_author'].split()[-1]
    k=key(fam,r['year'])
    out.append('\n'.join([f'@article{{{k},',f'  author = {{{tex(ascii_(r["first_author"]))} and others}},',f'  title = {{{{{tex(r["title"])}}}}},',f'  journal = {{{tex(r["journal"])}}},',f'  year = {{{r["year"]}}},',f'  doi = {{{r["doi"].strip()}}},','  note = {metadata from the page-1 check of the author library; first author only},','}'])); m+=1
open(os.path.join(root,'refs_new.bib'),'w').write('% Records added to reach a broad literature base; see gen_refs_new.py\n'+'\n\n'.join(out)+'\n')
print('crossref',n,'library',m,'total new',n+m)
