import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

card_ids = [
    'skm2-c7-wo-megutte', 'skm2-c7-ni-kotaete', 'skm2-c13-ni-kakete-wa', 'skm2-c6-ni-kansuru', 'added-n2-7-80',
    'skm2-c8-ni-motozuite', 'skm2-c8-ni-sotte', 'added-n2-8-81', 'added-n2-8-82',
    'skm2-c9-ni-tsurete', 'skm2-c9-ni-oujite', 'added-n2-9-83', 'added-n2-9-84'
]

points_by_id = {p.get('id'): p for p in points}

for cid in card_ids:
    p = points_by_id.get(cid)
    if not p:
        print(f"MISSING CARD: {cid}")
    else:
        print(f"Card {cid}: {p.get('title')} ({p.get('chapter')})")
        print(f"  Sentences: {len(p.get('sentences', []))}")
        print(f"  Explanation: {p.get('explanation', '')[:60]}...")
