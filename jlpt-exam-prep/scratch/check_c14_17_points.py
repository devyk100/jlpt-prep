import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

target_cids = [
    'skm2-c14-ippou-de', 'skm2-c14-hanmen', 'added-n2-14-91', 'added-n2-14-92', 'skm2-c19-monono',
    'skm2-c15-kuse-ni', 'skm2-c15-to-itte-mo', 'skm2-c15-to-shitara', 'added-n2-15-93', 'added-n2-15-94',
    'skm2-c15-mono-nara', 'skm2-c15-nai-koto-niwa', 'skm2-c15-wo-nuki-ni-shite-wa',
    'skm2-c16-amari-excess', 'skm2-c16-kara-to-itte', 'skm2-c16-ni-shite-wa', 'added-n2-16-95', 'added-n2-16-96',
    'skm2-c17-koto-kara', 'skm2-c17-wake-de-wa-nai', 'added-n2-17-96', 'added-n2-17-97', 'skm2-c17-wo-keiki-ni', 'added-n2-17-98'
]

missing_cards = []
present_cards = []

for cid in target_cids:
    if cid in points_by_id:
        p = points_by_id[cid]
        present_cards.append((cid, p.get('title'), len(p.get('sentences', []))))
    else:
        missing_cards.append(cid)

print(f"Present cards: {len(present_cards)}")
for c in present_cards:
    print(f"  {c[0]}: {c[1]} (sentences: {c[2]})")

print(f"\nMissing cards: {len(missing_cards)}")
for m in missing_cards:
    print("  ", m)
