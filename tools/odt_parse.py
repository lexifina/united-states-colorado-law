"""Read one CRS title (or the Colorado Constitution) from an OLLS release ODT into sections, statute text only.

OLLS marks each part of a section with a small marker paragraph: "Statute text", "History" (the source note) and
"Annotations" (editor's notes, cross references, case annotations). Only the paragraphs after "Statute text" and
before the next marker or heading are kept.
"""
from __future__ import annotations

import re
import zipfile
import xml.etree.ElementTree as ET

NS = {'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
      'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
      'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0'}
T = '{%s}' % NS['text']
MARKERS = {'Statute text', 'History', 'Annotations'}
SEC = re.compile(r'^(\d{1,2}(?:\.\d)?)-(\d{1,3}(?:\.\d{1,2})?)-(\d{1,4}(?:\.\d{1,2})?)\.\s+(.*)$')


def _text(el) -> str:
    out = []

    def walk(e):
        tag = e.tag
        if tag == T + 's':
            out.append(' ' * int(e.get(T + 'c', '1')))
        elif tag in (T + 'tab', T + 'line-break'):
            out.append(' ')
        elif tag == T + 'note':
            return  # footnote bodies are not statute text
        else:
            if e.text:
                out.append(e.text)
            for ch in e:
                walk(ch)
                if ch.tail:
                    out.append(ch.tail)
                continue
            return
        if e.tail is not None:
            pass
    if el.text:
        out.append(el.text)
    for ch in el:
        walk(ch)
        if ch.tail:
            out.append(ch.tail)
    return ''.join(out)


def normalise(s: str) -> str:
    s = s.replace(' ', ' ').replace(' ', ' ').replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"').replace('–', '-').replace('­', '')
    return re.sub(r'\s+', ' ', s).strip()


def paragraphs(path) -> list[str]:
    root = ET.fromstring(zipfile.ZipFile(path).read('content.xml'))
    body = root.find('office:body/office:text', NS)
    return [normalise(_text(p)) for p in body.iter() if p.tag in (T + 'p', T + 'h')]


def sections(path) -> tuple[list[dict], dict]:
    """[{'num','heading','paras'}] in document order, plus counts. A section is a heading paragraph ("3-1-101. ...")
    followed by a "Statute text" marker."""
    ps = paragraphs(path)
    out, stats = [], {'paragraphs': len(ps), 'repealed': 0, 'no_text': 0}
    i = 0
    while i < len(ps):
        m = SEC.match(ps[i])
        if not m:
            i += 1
            continue
        # A heading is followed (after blanks) by a marker paragraph; table-of-contents lines are not.
        j = i + 1
        while j < len(ps) and not ps[j]:
            j += 1
        if j >= len(ps) or ps[j] not in MARKERS:
            i += 1
            continue
        num = f'{m.group(1)}-{m.group(2)}-{m.group(3)}'
        sec = {'num': num, 'heading': m.group(4), 'paras': []}
        k = j
        if ps[j] == 'Statute text':
            k = j + 1
            while k < len(ps) and ps[k] not in MARKERS and not (SEC.match(ps[k]) and _next_marker(ps, k)):
                if ps[k]:
                    sec['paras'].append(ps[k])
                k += 1
        if sec['paras']:
            out.append(sec)
        elif re.search(r'\(Repealed\)|Repealed\.?$', sec['heading']):
            stats['repealed'] += 1
        else:
            stats['no_text'] += 1
        i = max(k, i + 1)
    return out, stats


def _next_marker(ps, i):
    j = i + 1
    while j < len(ps) and not ps[j]:
        j += 1
    return j < len(ps) and ps[j] in MARKERS
