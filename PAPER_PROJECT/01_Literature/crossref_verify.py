"""crossref_verify.py — metadata verification of manuscript references via the Crossref REST API (2026-10-01).
Level reached: METADATA VERIFIED (title/authors/journal/volume/pages/year as returned by Crossref). Not full-text."""
import json, time, urllib.request, urllib.parse, sys
UA = {'User-Agent': 'PAPER_PROJECT-reference-check/1.0 (research workflow; contact via user)'}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode())
def fmt(m):
    au = '; '.join(f"{a.get('family','?')}, {a.get('given','?')}" for a in m.get('author', [])[:12])
    return dict(doi=m.get('DOI'), title=(m.get('title') or [''])[0], authors=au, n_authors=len(m.get('author', [])),
                journal=(m.get('container-title') or [''])[0], year=(m.get('issued', {}).get('date-parts') or [[None]])[0][0],
                volume=m.get('volume'), issue=m.get('issue'), pages=m.get('page') or m.get('article-number'), type=m.get('type'),
                publisher=m.get('publisher'))
dois = {
 'ref_chao_gao_2001': '10.1016/S0020-7683(00)00403-0',
 'ref_2015_dpl_hole': '10.1080/15397734.2015.1029589',
 'ref_karmakar_2016': '10.1134/S002189441604009X',
 'ref_jafari_2019': '10.1177/0021998318795279',
 'ref_adachi_2018': '10.1063/1.5047017',
 'ref_klimm_2023': '10.1002/crat.202200204',
 'ref_tzou_1995_JHT': '10.1115/1.2822329',
 'ref_lord_shulman_1967': '10.1016/0022-5096(67)90024-5',
 'ref_apex_mfp': '10.35848/1882-0786/ad0ba8',
 'ref_huang_2025': '10.1007/s10483-025-3280-7',
}
out = {}
for k, d in dois.items():
    try:
        out[k] = fmt(get('https://api.crossref.org/works/' + urllib.parse.quote(d))['message'])
        print('OK ', k, '|', out[k]['title'][:90], '|', out[k]['journal'], out[k]['year'], out[k]['volume'], out[k]['pages'], '|', out[k]['authors'][:80], flush=True)
    except Exception as e:
        out[k] = dict(error=str(e)); print('ERR', k, e, flush=True)
    time.sleep(1.0)
queries = {
 'ref_florence_goodier_1959': 'Florence Goodier Thermal stress at spherical cavities and circular holes in uniform heat flow Journal of Applied Mechanics 1959',
 'ref_florence_goodier_1960': 'Florence Goodier Thermal stresses due to disturbance of uniform heat flow by an insulated ovaloid hole Journal of Applied Mechanics 1960',
 'ref_expansion_2015': 'Thermal expansion coefficients of beta-Ga2O3 single crystals powder X-ray diffraction 2015',
 'ref_debye_2021': 'beta-Ga2O3 Debye temperature specific heat ACS Omega 2021',
 'ref_chandrasekharaiah_1998': 'Chandrasekharaiah Hyperbolic thermoelasticity: a review of recent literature Applied Mechanics Reviews 1998',
 'ref_durbin_1974': 'Durbin Numerical inversion of Laplace transforms: an efficient improvement to Dubner and Abate method Computer Journal 1974',
 'ref_crump_1976': 'Crump Numerical inversion of Laplace transforms using a Fourier series approximation Journal of the ACM 1976',
}
for k, q in queries.items():
    try:
        items = get('https://api.crossref.org/works?rows=3&query.bibliographic=' + urllib.parse.quote(q))['message']['items']
        out[k] = [fmt(m) for m in items]
        for m in out[k]:
            print('Q  ', k, '|', m['title'][:80], '|', m['journal'], m['year'], m['volume'], m['pages'], '|', m['authors'][:60], '|', m['doi'], flush=True)
    except Exception as e:
        out[k] = dict(error=str(e)); print('ERR', k, e, flush=True)
    time.sleep(1.0)
json.dump(out, open('CROSSREF_VERIFICATION_2026-10-01.json', 'w'), indent=1)
