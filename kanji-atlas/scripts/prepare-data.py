import json
import sys
from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://raw.githubusercontent.com/evanclan/OpenJLPT/main/'
def download(pair):
    remote, local = pair
    (ROOT / local).write_bytes(urlopen(BASE + remote).read())
files = [(f'data/json/{kind}/n{level}.json', f'data/{kind}-n{level}.json')
         for kind in ['kanji', 'vocab'] for level in [5,4,3,2]]
files += [('NOTICE.md','data/NOTICE.md'), ('LICENSE','data/LICENSE'), ('data/json/meta.json','data/meta.json')]
if '--offline' not in sys.argv:
    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(download, files))
read = lambda name: json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
words = [w for n in [5,4,3,2] for w in read(f'vocab-n{n}.json')]
corrections = read('corrections.json')
words = [w | corrections.get(w['id'], {}) for w in words]
entries = []
supplements = read('book-supplements.json')
references = read('book-references.json')
for n in [5,4,3,2]:
    for k in read(f'kanji-n{n}.json') + [s for s in supplements if s['level']==f'N{n}']:
        matches = []
        for w in words:
            forms = [w['word']] + w.get('other_forms', [])
            form = next((f for f in forms if k['character'] in f), None)
            if form:
                matches.append(w | {'word':form})
        matches.sort(key=lambda w: (-int(w['level'][1]), len(w['word']), w['reading']))
        vocab = [{key:w[key] for key in ['id','word','reading','meanings','level']} for w in matches]
        entries.append({key:k[key] for key in ['character','level','strokes','freq','onyomi','kunyomi','meanings']} | {'words':vocab,'bookReferences':references.get(k['character'],[]),'levelBasis':k.get('levelBasis','Community JLPT estimate; textbook coverage may differ.')})
assert len({k['character'] for k in entries}) == len(entries)
assert all(k['meanings'] and k['level'] in ['N5','N4','N3','N2'] for k in entries)
assert all(w['reading'] and w['meanings'] and w['level'] != 'N1' for k in entries for w in k['words'])
(ROOT/'src'/'kanji.json').write_text(json.dumps(entries, ensure_ascii=False), encoding='utf-8')
report = {'total':len(entries), 'levels':{f'N{n}':sum(k['level']==f'N{n}' for k in entries) for n in [5,4,3,2]}, 'vocabularyEntries':len(words), 'fewerThanFourWords':[k['character'] for k in entries if len(k['words'])<4], 'noWords':[k['character'] for k in entries if not k['words']]}
(ROOT/'data'/'coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({key:value for key,value in report.items() if key!='fewerThanFourWords'},ensure_ascii=False))
