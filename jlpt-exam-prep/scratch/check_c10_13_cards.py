import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

card_ids = [
    'skm2-c10-nuki-de', 'added-n2-10-85', 'added-n2-10-86',
    'skm2-c11-ni-kakawarazu', 'skm2-c11-ha-tomo-kaku', 'skm2-c11-ha-sateoki', 'added-n2-11-87',
    'skm2-c12-dokoroka', 'added-n2-12-88',
    'added-n2-13-89', 'added-n2-13-90'
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
