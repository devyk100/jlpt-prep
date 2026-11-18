import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

card_ids = [
    'skm2-c4-wo-hajime', 'skm2-c4-kara-shite', 'skm2-c4-ni-watatte', 'added-n2-4-75', 'added-n2-4-76',
    'skm2-c4-kagiri-dewa', 'added-n2-5-77', 'added-n2-5-78',
    'skm2-c5-nomi-narazu', 'skm2-c5-bakari-ka', 'added-n2-6-79'
]

points_by_id = {p.get('id'): p for p in points}

for cid in card_ids:
    p = points_by_id.get(cid)
    if not p:
        print(f"MISSING CARD: {cid}")
    else:
        print(f"Card {cid}: {p.get('title')} ({p.get('bookId')}, {p.get('chapter')})")
        print(f"  Examples: {len(p.get('examples', []))}")
        print(f"  Formation: {p.get('formation', '')[:60]}...")
