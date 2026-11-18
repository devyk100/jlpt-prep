import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)

queries = [
    ('んです', 'g1'),
    ('ほうがいい', 'g1'),
    ('たらどう', 'g1'),
    ('そう', 'g2'),
    ('あげる', 'g2'),
    ('くれる', 'g2'),
    ('もらう', 'g2'),
    ('条件', 'g2'),
    ('ば', 'g2'),
    ('たら', 'g2'),
    ('なら', 'g2'),
    ('敬語', 'g2'),
    ('尊敬', 'g2'),
    ('謙譲', 'g2'),
    ('受身', 'g2'),
    ('使役', 'g2'),
    ('ことにする', 'g2'),
    ('ことになる', 'g2'),
    ('うちに', 'skm3'),
    ('間に', 'skm3'),
    ('反面', 'skm3'),
    ('一方で', 'skm3'),
    ('に対して', 'skm3'),
    ('わけ', 'skm3'),
    ('次第', 'skm2'),
    ('わりに', 'skm2'),
    ('にしては', 'skm2'),
    ('くせに', 'skm2'),
    ('反面', 'skm2'),
    ('ことから', 'skm2'),
    ('かねる', 'skm2'),
    ('がたい', 'skm2'),
    ('ようがない', 'skm2'),
    ('恐れがある', 'skm2'),
    ('かねない', 'skm2'),
    ('末に', 'skm2'),
    ('あげく', 'skm2'),
    ('ものだ', 'skm2'),
    ('べきだ', 'skm2'),
    ('ことだ', 'skm2'),
    ('わけではない', 'skm2'),
    ('わけがない', 'skm2')
]

for q, prefix in queries:
    matches = [sp for sp in sps if (q in sp['title'] or q in sp.get('meaning', '') or q in sp.get('connection', '')) and (prefix in sp['id'] or prefix in sp.get('book', '').lower() or prefix in sp.get('level', '').lower())]
    print(f"=== Query [{q}] in [{prefix}]: {len(matches)} match(es) ===")
    for m in matches:
        print(f"  ID: {m['id']} | Level: {m.get('level')} | Title: {m['title']}")
