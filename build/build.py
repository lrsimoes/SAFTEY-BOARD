"""Rebuild index.html from build/template.html and data/*.json.
Run: python3 build/build.py   (from the repo root)"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
d = {
    'staff': json.loads((root / 'data/staff.json').read_text()),
    'attention': json.loads((root / 'data/attention.json').read_text()),
    'scan': json.loads((root / 'data/scan.json').read_text())[0],
}
html = (root / 'build/template.html').read_text().replace('__DATA__', json.dumps(d, ensure_ascii=False))
(root / 'index.html').write_text(html)
print('index.html rebuilt:', len(d['staff']), 'people,', len(d['attention']), 'attention items')
