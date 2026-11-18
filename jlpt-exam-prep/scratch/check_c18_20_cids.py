import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

target_cids = [
    'skm2-c18-mono-dakara', 'skm2-c18-mono-nara', 'skm2-c18-koto-dakara', 'added-n2-18-98',
    'skm2-c18-dakeni', 'skm2-c18-kara-koso', 'skm2-c22-kaneru', 'added-n2-18-99', 'added-n2-18-100',
    'skm2-c19-ue-wa', 'added-n2-19-99', 'added-n2-19-100', 'added-n2-19-101', 'added-n2-19-102', 'added-n2-19-103',
    'skm2-c20-shidai-de-wa', 'added-n2-20-101', 'added-n2-20-102', 'skm2-c20-sue-ni-deliberation', 'skm2-c20-ageku-ni', 'added-n2-20-104'
]

for cid in target_cids:
    p = points_by_id.get(cid)
    if p:
        print(f"EXISTS: {cid} -> {p.get('title')} (sentences: {len(p.get('sentences', []))})")
    else:
        print(f"NOT DIRECT: {cid}")
