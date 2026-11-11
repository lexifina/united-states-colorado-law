"""Deterministic extraction of Colorado's official 2023 session-law PDFs."""
import sys, re, json, hashlib, html, datetime as dt, time
from pathlib import Path
from io import BytesIO
import pymupdf
from pypdf import PdfReader
from bs4 import BeautifulSoup
import collect_2023_depth as common

ROOT, JOB, EVIDENCE = common.ROOT, common.JOB, common.EVIDENCE
PART = 'zzzzz-q1575-session-laws-2023-depth.json'
norm = common.norm

def listing():
    rows={}
    for n in range(1,20):
        url=f'https://leg.colorado.gov/laws/session-laws?sess=2023a&page={n}'
        soup=BeautifulSoup(common.get(url),'html.parser')
        for tr in soup.select('tr[role="row"]'):
            cells={td.get('data-label'):td for td in tr.select('td[data-label]')}
            if 'Chapter #' not in cells: continue
            chapter=int(cells['Chapter #'].get_text(' ',strip=True))
            link=next(a['href'] for a in tr.select('a[href]') if '/download' in a['href'])
            rows[chapter]={'chapter':chapter,'bill':cells['Measure'].get_text(' ',strip=True).split()[0],
                'effective':cells['Effective Date'].get_text(' ',strip=True),
                'url':'https://leg.colorado.gov'+link,'listing_url':url}
        print('listing',n,len(rows),flush=True)
    assert len(rows)==474 and set(rows)==set(range(1,475))
    common.save('official-2023-listing.json',rows)
    return rows

def cleaned_independent(page):
    text=page.extract_text()
    assert text, 'page without text layer'
    # Printed page number, category and chapter form one running-header line.
    lines=text.splitlines()
    assert re.search(r'Ch\.\s*\d+',lines[0]), 'unrecognized running header'
    lines=lines[1:]
    text='\n'.join(lines)
    text=re.split(r'\){5}\s*Capital letters',text)[0]
    return re.sub(r'_{3,}','',text)

def parse(row,raw):
    doc=pymupdf.open(stream=raw,filetype='pdf')
    reader=PdfReader(BytesIO(raw))
    assert len(doc)==len(reader.pages)
    paragraphs=[]; source_paragraphs=[]; deleted=0; drawings_audit=[]
    image_count=sum(len(p.get_images(full=True)) for p in doc)
    assert image_count==0, f'normative image review required: {image_count} source image resources'
    for pn,page in enumerate(doc):
        drawings=page.get_drawings()
        thin=[]
        for drawing in drawings:
            r=drawing['rect']
            if r.height<=1.5 and r.width>1:
                thin.append(r)
            else:
                raise ValueError('non-text vector drawing requires normative-image review')
        touched=set()
        for block in page.get_text('rawdict')['blocks']:
            if block['type']!=0: continue
            rawlines=[''.join(ch['c'] for s in line['spans'] for ch in s['chars']) for line in block['lines']]
            plain=norm(' '.join(rawlines))
            if block['bbox'][3]<55 or 'Capital letters or bold & italic numbers indicate new material' in plain: continue
            if re.fullmatch(r'[_\s]+',plain): continue
            rendered_lines=[]
            plain_lines=[]
            for line in block['lines']:
                output=''; active=False
                for span in line['spans']:
                    for char in span['chars']:
                        ch=char['c']; r=pymupdf.Rect(char['bbox'])
                        hit=[i for i,d in enumerate(thin) if d.y0>=r.y0+1 and d.y1<r.y1-0.5 and d.x0<=r.x0+r.width/2<=d.x1]
                        strike=bool(hit)
                        touched.update(hit)
                        if strike!=active:
                            output+=('<del>' if strike else '</del>'); active=strike
                        output+=html.escape(ch)
                        if strike and not ch.isspace(): deleted+=1
                if active: output+='</del>'
                rendered_lines.append(output)
                plain_lines.append(''.join(ch['c'] for s in line['spans'] for ch in s['chars']))
            paragraph=norm(' '.join(rendered_lines))
            text=norm(' '.join(plain_lines))
            # Remove only the source's decorative separator, including when grouped with a heading.
            paragraph=re.sub(r'_{3,}','',paragraph).strip()
            text=re.sub(r'_{3,}','',text).strip()
            if paragraph:
                paragraphs.append(paragraph)
                source_paragraphs.append(text)
        assert len(touched)==len(thin), f'unmatched drawing on page {pn+1}'
        independent=cleaned_independent(reader.pages[pn])
        primary=' '.join(source_paragraphs) # page slice below is checked separately
        drawings_audit.append({'page':pn+1,'source_strike_rectangles':len(thin),'matched':len(touched)})
    plain=' '.join(source_paragraphs)
    independent=' '.join(cleaned_independent(p) for p in reader.pages)
    # All non-whitespace source characters, including punctuation and deleted wording, must agree.
    squeeze=lambda s:re.sub(r'\s+','',s)
    assert squeeze(plain)==squeeze(independent), 'independent pypdf source-character mismatch'
    assert '\ufffd' not in plain and '\x00' not in plain, 'undecodable PDF text'
    assert re.search(rf'CHAPTER\s+{row["chapter"]}\b',plain)
    bill=re.search(r'(HOUSE|SENATE) BILL (\d{2}-\d+)',plain)
    assert bill and ('HB' if bill[1]=='HOUSE' else 'SB')+bill[2]==row['bill'], 'chapter/bill mismatch'
    title=re.search(r'AN ACT\s+(.+?)\s+Be it enacted by the General Assembly',plain)
    assert title, 'missing full enacted title'
    approval=re.search(r'(Approved|Became Law):\s*([A-Z][a-z]+ \d{1,2}, \d{4})',plain)
    assert approval, 'missing source approval date'
    made=dt.datetime.strptime(approval[2],'%B %d, %Y').date().isoformat()
    listed=dt.datetime.strptime(row['effective'],'%m/%d/%Y').date().isoformat()
    tail=plain[plain.rfind('SECTION '):]
    clauses=re.findall(r'SECTION \d+\.\s+(?:Act subject to petition - effective date|Effective date(?: - [^.]+)?|Safety clause)\..*?(?=SECTION \d+\.|Approved:|Became Law:|$)',plain)
    combined=' '.join(clauses)
    decision_clause=combined.split('; except that, if a referendum petition is filed')[0]
    if 'except that' in decision_clause or len(clauses)>1:
        raise ValueError('multiple or staged commencement provisions')
    if 'day following the expiration of the ninety-day period after final adjournment' in combined:
        effective='2023-08-07'
    elif re.search(r'This act takes effect (?:on )?([A-Z][a-z]+ \d{1,2}, \d{4})',decision_clause):
        dates=re.findall(r'This act takes effect (?:on )?([A-Z][a-z]+ \d{1,2}, \d{4})',combined)
        assert len(set(dates))==1
        effective=dt.datetime.strptime(dates[0],'%B %d, %Y').date().isoformat()
    elif 'Safety clause.' in combined and 'This act takes effect' not in plain:
        effective=made
    else:
        raise ValueError('unresolved commencement clause')
    assert effective==listed, f'listing/commencement conflict: {listed} vs {effective}'
    assert effective>=made, 'commencement before source approval'
    n=row['chapter']; slug=f'session-2023-ch-{n:03d}'; law=f'co-2023-ch-{n:03d}'
    note='As enacted; entire act in one text unit. Source approval: '+approval[0]+': '+approval[2]+'. In-force basis: '+combined+' Official chapter listing: '+row['effective']+' ('+row['listing_url']+').'
    text='\n'.join(paragraphs)+'\n'
    assert squeeze(html.unescape(re.sub(r'<[^>]*>','',text)))==squeeze(independent)
    act={'slug':slug,'short':f'2023 ch. {n}','title':title[1],'url':row['url'],'first_law':law,'earlier_laws':[],
        'versions':[{'from':effective,'source_url':row['url'],'sha256':hashlib.sha256(raw).hexdigest(),
            'units':{'act-text':{'label':'Complete enacted act','kind':'section','text':text}},'credits':{},'note':note}]}
    lawrec={'label':f'2023 chapter {n} ({row["bill"]})','title':title[1],'kind':'law','enacted':made,'published':None,'url':row['url'],'note':note}
    audit={'chapter':n,'url':row['url'],'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'pages':len(doc),
        'independent_source_characters_match':True,'deleted_characters':deleted,'drawings':drawings_audit,
        'source_images':0,'referenced_images':0,'omitted_images':0,'effective':effective,'enacted':made,'listing_effective':listed}
    return act,law,lawrec,audit

def run():
    common.record_process()
    rows=listing()
    published=set()
    for part in (ROOT/'corpus.d').glob('*.json'):
        if part.name==PART: continue
        published.update(a['slug'] for a in json.loads(part.read_text(encoding='utf8')).get('acts',[]))
    corpus=json.loads((ROOT/'corpus.json').read_text(encoding='utf8'))
    corpus.update(acts=[],laws={},sources=[],decisions=[],ai_use=[])
    audits=[];held=[]
    for n in range(251,475):
        row=rows[n]
        if f'session-2023-ch-{n:03d}' in published: continue
        try:
            raw=common.get(row['url'])
            assert raw.startswith(b'%PDF'), 'source is not a PDF'
            first=parse(row,raw);second=parse(row,raw)
            assert first==second,'non-deterministic parse'
            a,k,l,audit=first
            corpus['acts'].append(a);corpus['laws'][k]=l;audits.append(audit)
        except (common.fs.HostStopped,common.fs.RobotsDisallowed,common.fs.NotNow):
            raise
        except Exception as exc:
            held.append({'chapter':n,'url':row['url'],'bill':row['bill'],'reason':str(exc),'type':type(exc).__name__})
        common.save('chapter-audit.json',audits);common.save('chapters-held.json',held)
        print('chapter',n,'admitted',len(audits),'held',len(held),flush=True)
    corpus['sources']=[{'name':'Colorado General Assembly, OLLS 2023 regular-session chapter PDFs',
        'url':'https://leg.colorado.gov/laws/session-laws?sess=2023a','retrieved':'2026-11-11',
        'licence':'Edicts of government; enacted legislation is public domain.',
        'notes':'Official as-enacted chapter text, with deletion marks preserved; not consolidated later CRS text.'}]
    corpus['decisions']=[f'Chapters 251–474 of the official 2023 session listing: {len(audits)} admitted and {len(held)} held individually. Complete as-enacted acts are single-file text units; no consolidated CRS reconstruction. Every non-whitespace character matches an independent PDF reader. Deletions retain source geometric strikethrough. Source commencement clauses agree with listing dates; no retrieval-day dates.']
    corpus['ai_use']=['GPT-6 wrote deterministic extraction and validation code; no model-authored law text or OCR.']
    path=ROOT/'corpus.d'/PART
    assert not path.exists() and not path.with_suffix('.PUBLISH').exists()
    assert corpus['acts']
    path.write_text(json.dumps(corpus,ensure_ascii=False,sort_keys=True,indent=1)+'\n',encoding='utf8',newline='\n')
    common.save('range-summary.json',{'listed':474,'range':224,'added':len(audits),'held':len(held),'identical_parses':True,'part_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    common.save('host-rates.json',{h:common.fs.host_report(h) for h in ['leg.colorado.gov','archive.org']})

def reprocess_held():
    common.record_process()
    path=ROOT/'corpus.d'/PART
    assert path.exists() and not path.with_suffix('.PUBLISH').exists() and not path.with_suffix('.PUBLISH.pending').exists()
    corpus=json.loads(path.read_text(encoding='utf8'))
    audits=json.loads((EVIDENCE/'chapter-audit.json').read_text())
    previous=json.loads((EVIDENCE/'chapters-held.json').read_text())
    common.save('first-pass-holds.json',previous)
    rows=json.loads((EVIDENCE/'official-2023-listing.json').read_text())
    held=[]
    for h in previous:
        row=rows[str(h['chapter'])]
        try:
            raw=(EVIDENCE/hashlib.sha256(row['url'].encode()).hexdigest()).read_bytes()
            first=parse(row,raw);second=parse(row,raw)
            assert first==second
            a,k,l,audit=first
            corpus['acts'].append(a);corpus['laws'][k]=l;audits.append(audit)
        except Exception as exc:
            held.append({**h,'reason':str(exc),'type':type(exc).__name__})
        print('reprocess',row['chapter'],'admitted',len(audits),'held',len(held),flush=True)
    corpus['acts'].sort(key=lambda a:a['slug'])
    audits.sort(key=lambda a:a['chapter'])
    corpus['decisions']=[f'Chapters 251–474 of the official 2023 session listing: {len(audits)} admitted and {len(held)} held individually. Complete as-enacted acts are single-file text units; no consolidated CRS reconstruction. Every non-whitespace character matches an independent PDF reader. Deletions retain source geometric strikethrough. Source commencement clauses agree with listing dates; standard referendum conditions are retained verbatim; no retrieval-day dates.']
    path.write_text(json.dumps(corpus,ensure_ascii=False,sort_keys=True,indent=1)+'\n',encoding='utf8',newline='\n')
    common.save('chapter-audit.json',audits);common.save('chapters-held.json',held)
    common.save('range-summary.json',{'listed':474,'range':224,'added':len(audits),'held':len(held),'identical_parses':True,'part_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})

if __name__=='__main__':
    reprocess_held() if '--reprocess-held' in sys.argv else run()
