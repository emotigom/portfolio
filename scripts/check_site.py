#!/usr/bin/env python3
"""Offline, dependency-free checks for the static portfolio. No live-site claims."""
from __future__ import annotations
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: Counter[str] = Counter()
        self.ids: list[str] = []
        self.elements: list[tuple[str,dict[str,str | None]]] = []
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.lang: str | None = None
        self.doctype = False
    def handle_decl(self, decl: str) -> None:
        self.doctype = decl.lower() == 'doctype html'
    def handle_starttag(self, tag: str, attrs: list[tuple[str,str | None]]) -> None:
        attr = dict(attrs)
        self.tags[tag] += 1
        self.elements.append((tag,attr))
        if len(attrs) != len(attr): self.errors.append(f'Duplicate attribute on <{tag}>')
        if tag == 'html': self.lang = attr.get('lang')
        if attr.get('id'): self.ids.append(str(attr['id']))
        if tag not in VOID: self.stack.append(tag)
    def handle_startendtag(self, tag: str, attrs: list[tuple[str,str | None]]) -> None:
        self.handle_starttag(tag,attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_endtag(self, tag: str) -> None:
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f'Mismatched closing tag </{tag}>')
            return
        self.stack.pop()

def audit(root: Path) -> tuple[list[str],dict[str,int]]:
    errors: list[str] = []
    path=root/'index.html'
    if not path.is_file(): return ['index.html is missing'], {}
    parser=DocumentParser()
    try: parser.feed(path.read_text(encoding='utf-8'))
    except (OSError,UnicodeError) as exc: return [f'HTML read failed: {exc}'], {}
    errors.extend(parser.errors)
    if parser.stack: errors.append('Unclosed HTML elements: '+', '.join(parser.stack))
    if not parser.doctype: errors.append('HTML5 doctype is required')
    if parser.lang != 'ko': errors.append('HTML language must be ko')
    for tag in ('html','head','body','title','main','h1'):
        if parser.tags[tag] != 1: errors.append(f'Expected one {tag}, found {parser.tags[tag]}')
    for tag in ('header','nav','footer'):
        if not parser.tags[tag]: errors.append(f'Missing semantic {tag}')
    for id_,count in Counter(parser.ids).items():
        if count != 1: errors.append(f'Duplicate id: {id_}')
    ids=set(parser.ids)
    try:
        data=json.loads((root/'assets/evidence-map.json').read_text(encoding='utf-8'))
        evidence=data['evidence']
        if not isinstance(evidence,dict): raise ValueError('evidence must be an object')
    except (OSError,UnicodeError,ValueError,KeyError) as exc:
        evidence={};errors.append(f'Evidence map is invalid: {exc}')
    links=0; internals=0; source_links=0
    for tag,attr in parser.elements:
        if tag=='img' and 'alt' not in attr: errors.append('Image without alt')
        if tag=='button' and attr.get('type')!='button': errors.append('Button needs explicit type')
        for name in ('href','src'):
            if name not in attr: continue
            value=attr.get(name) or ''
            if not value: errors.append(f'Empty {name}');continue
            target=urlsplit(value)
            if target.scheme in ('javascript','data'): errors.append(f'Unsafe link scheme: {target.scheme}')
            if target.scheme or target.netloc: continue
            if tag=='a': links+=1
            if not target.path:
                if target.fragment and unquote(target.fragment) not in ids:
                    errors.append(f'Broken internal anchor: {value}')
                continue
            internals+=1
            local=(root/unquote(target.path)).resolve()
            if not local.is_relative_to(root.resolve()): errors.append(f'Path escapes site: {value}')
            elif not local.is_file(): errors.append(f'Missing local asset: {value}')
        if tag=='a':
            links+=int(bool(urlsplit(attr.get('href') or '').scheme))
            if attr.get('target')=='_blank' and not {'noopener','noreferrer'} <= set((attr.get('rel') or '').split()):
                errors.append(f'Unsafe new-tab relation: {attr.get("href")}')
        if attr.get('data-evidence'):
            key=str(attr['data-evidence']); source_links+=1
            if key not in evidence: errors.append(f'Unknown evidence key: {key}')
            elif attr.get('href') != evidence[key]['url']: errors.append(f'Evidence URL mismatch: {key}')
    for key,entry in evidence.items():
        url=entry.get('url','')
        if entry.get('level')=='contribution-history':
            if not re.fullmatch(r'https://github\.com/[^/]+/[^/]+/pull/\d+',url):
                errors.append(f'Invalid PR evidence: {key}')
        else:
            sha=entry.get('revision','')
            if not re.fullmatch('[0-9a-f]{40}',sha): errors.append(f'Unpinned evidence: {key}')
            expected=f'https://github.com/{entry.get("repository")}/blob/{sha}/{entry.get("path")}'
            if url!=expected: errors.append(f'Invalid pinned URL: {key}')
        if not entry.get('scope'): errors.append(f'Evidence scope is missing: {key}')
    pdf=root/'assets/Ahn_Sangkyoon_Resume_PythonBackend_Fullstack.pdf'
    if pdf.is_file() and not pdf.read_bytes().startswith(b'%PDF-'):
        errors.append('Resume asset is not a PDF')
    return errors,{'links':links,'local_asset_references':internals,'evidence_link_instances':source_links,'evidence_records':len(evidence),'unique_ids':len(ids)}

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--json',type=Path)
    args=ap.parse_args()
    errors,counts=audit(args.root)
    report={'result':'FAIL' if errors else 'PASS','mode':'offline static checks','counts':counts,'errors':errors}
    if args.json: args.json.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return int(bool(errors))
if __name__=='__main__': sys.exit(main())
