"""Retrieve public metadata and a representative selection of user-linked papers.
Does not execute archive contents, submit manuscripts, or upload unpublished texts.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.parse import quote
import requests, json, re, hashlib, time

ROOT = Path('/home/user')
READING = ROOT/'RESEARCH_READING'
records = json.loads((READING/'PUBLISHED_PAPERS_INVENTORY.json').read_text())
HEADERS = {'User-Agent':'User-authorized research reading (metadata verification)', 'Accept':'application/json'}

def crossref_record(rec):
    doi = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', rec['publisher_or_doi_url'], flags=re.I).strip()
    out = {'paper_id':rec['paper_id'], 'doi_user_supplied':doi, 'checked_utc':datetime.now(timezone.utc).isoformat()}
    url = 'https://api.crossref.org/works/'+quote(doi, safe='/')
    try:
        r=requests.get(url,headers=HEADERS,timeout=(15,55))
        out['http_status']=r.status_code
        if r.ok:
            m=r.json()['message']
            out.update({'metadata_status':'METADATA_VERIFIED_CROSSREF', 'crossref_title':m.get('title',[]), 'crossref_journal':m.get('container-title',[]),'crossref_doi':m.get('DOI'), 'published':m.get('published'), 'published_online':m.get('published-online'), 'published_print':m.get('published-print'), 'volume':m.get('volume'), 'issue':m.get('issue'), 'page':m.get('page'), 'article_number':m.get('article-number'), 'url':m.get('URL'), 'resource':m.get('resource'), 'links':m.get('link',[]), 'abstract':m.get('abstract'), 'relation':m.get('relation'), 'update_to':m.get('update-to'), 'authors':m.get('author',[])})
        else:
            out['metadata_status']='REQUIRES_VERIFICATION'
    except Exception as e:
        out.update({'metadata_status':'REQUIRES_VERIFICATION','error':str(e)})
    return out

results=[]
with ThreadPoolExecutor(max_workers=5) as ex:
    futures={ex.submit(crossref_record,r):r for r in records}
    for f in as_completed(futures):
        out=f.result(); results.append(out)
        print('METADATA',out['paper_id'],out['metadata_status'],out.get('http_status'),flush=True)
results.sort(key=lambda x:int(x['paper_id']))
(READING/'CROSSREF_METADATA_VERIFICATION.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))

selected={'1','2','10','21','25','29','35','38','45','47'}
folder=ROOT/'RESEARCH_PROJECT_INPUT/LITERATURE/Accessible_Published_Fulltexts'
folder.mkdir(parents=True,exist_ok=True)

def download_selected(rec):
    out={'paper_id':rec['paper_id'],'title_user_supplied':rec['title'],'checked_utc':datetime.now(timezone.utc).isoformat(),'fulltext_status':'NOT_RETRIEVED'}
    url=rec['article_url']; match=re.search(r'/file/d/([^/]+)',url)
    if match:
        fid=match.group(1)
        urls=[f'https://drive.google.com/uc?export=download&id={fid}',f'https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t']
    elif rec['paper_id']=='2':
        urls=['https://www.nature.com/articles/s41598-023-44339-5.pdf']
    else: urls=[url]
    for attempt in urls:
        try:
            r=requests.get(attempt,headers={'User-Agent':'Mozilla/5.0'},timeout=(20,100))
            body=r.content
            if r.ok and body[:5]==b'%PDF-':
                if len(body)>20*1024*1024:
                    out.update({'fulltext_status':'NOT_RETRIEVED_SIZE_LIMIT','bytes':len(body)}); return out
                p=folder/f"P{int(rec['paper_id']):02d}.pdf"; p.write_bytes(body)
                out.update({'fulltext_status':'FULLTEXT_DOWNLOADED_NOT_YET_READ','source_url':attempt,'local_path':str(p.relative_to(ROOT)),'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest()})
                return out
            out['last_http_status']=r.status_code; out['last_content_type']=r.headers.get('content-type'); out['last_response_head']=body[:160].decode(errors='replace')
        except Exception as e: out['last_error']=str(e)
    return out

downloads=[]
with ThreadPoolExecutor(max_workers=3) as ex:
    futures={ex.submit(download_selected,r):r for r in records if r['paper_id'] in selected}
    for f in as_completed(futures):
        out=f.result(); downloads.append(out)
        print('FULLTEXT',out['paper_id'],out['fulltext_status'],out.get('bytes'),flush=True)
downloads.sort(key=lambda x:int(x['paper_id']))
(READING/'PUBLISHED_FULLTEXT_RETRIEVAL.json').write_text(json.dumps(downloads,ensure_ascii=False,indent=2))
