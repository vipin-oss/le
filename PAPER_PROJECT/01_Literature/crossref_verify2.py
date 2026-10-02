"""crossref_verify2.py — second batch (2026-10-01): additional references found during the refreshed literature search."""
import json, time, urllib.request, urllib.parse
UA = {'User-Agent': 'PAPER_PROJECT-reference-check/1.0 (research workflow)'}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
        return json.loads(r.read().decode())
def fmt(m):
    au = '; '.join(f"{a.get('family','?')}, {a.get('given','?')}" for a in m.get('author', []))
    return dict(doi=m.get('DOI'), title=(m.get('title') or [''])[0], authors=au, journal=(m.get('container-title') or [''])[0],
                year=(m.get('issued', {}).get('date-parts') or [[None]])[0][0], volume=m.get('volume'), issue=m.get('issue'),
                pages=m.get('page') or m.get('article-number'))
out = {}
for k, d in {'orlandi_2015': '10.7567/APEX.8.111101', 'jts_bem_2026': '10.1080/01495739.2025.2566326', 'symmetry_2022': '10.3390/sym14112387'}.items():
    try:
        out[k] = fmt(get('https://api.crossref.org/works/' + urllib.parse.quote(d))['message']); print('OK ', k, out[k], flush=True)
    except Exception as e:
        out[k] = dict(error=str(e)); print('ERR', k, e, flush=True)
    time.sleep(1)
qs = {
 'dhaliwal_sherief_1980': 'Dhaliwal Sherief Generalized thermoelasticity for anisotropic media Quarterly of Applied Mathematics 1980',
 'cheng_2018_expansion': 'Cheng Hanke Galazka Trampert Thermal expansion of single-crystalline beta-Ga2O3 from RT to 1200 K synchrotron high resolution x-ray diffraction',
 'handwerg_2016': 'Handwerg Mitdank Galazka Fischer Temperature-dependent thermal conductivity and diffusivity of a Mg-doped insulating beta-Ga2O3 single crystal',
 'biot_1956': 'Biot Thermoelasticity and irreversible thermodynamics Journal of Applied Physics 1956',
 'bem_discs_2022': 'Boundary Element and Sensitivity Analysis of Anisotropic Thermoelastic Metal and Alloy Discs with Holes Materials 2022',
 'cattaneo_1958': 'Cattaneo Sur une forme de ldquo equation de la chaleur eliminant le paradoxe dune propagation instantanee 1958',
 'stroh_1958': 'Stroh Dislocations and cracks in anisotropic elasticity Philosophical Magazine 1958',
}
for k, q in qs.items():
    try:
        items = get('https://api.crossref.org/works?rows=2&query.bibliographic=' + urllib.parse.quote(q))['message']['items']
        out[k] = [fmt(m) for m in items]
        for m in out[k]:
            print('Q  ', k, '|', m['title'][:85], '|', m['journal'], m['year'], m['volume'], m['pages'], '|', m['authors'][:70], '|', m['doi'], flush=True)
    except Exception as e:
        out[k] = dict(error=str(e)); print('ERR', k, e, flush=True)
    time.sleep(1)
json.dump(out, open('CROSSREF_VERIFICATION_2_2026-10-01.json', 'w'), indent=1)
