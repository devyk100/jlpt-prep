import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)
with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)
cids = set(c['id'] for c in cards)

print(f"Total rows in matrix: {len(matrix)}")
broken = 0
for r in matrix:
    cid = r.get('cardId')
    exists = cid in cids
    if not exists:
        broken += 1
        print(f"  BROKEN LINK: {r.get('sourceBook')} | {r.get('sourceSection')} | {r.get('grammarItem')[:30]} -> {cid}")
    else:
        print(f"  OK: {r.get('sourceBook')} | {r.get('sourceSection')} -> {cid}")
print(f"Broken links: {broken} / {len(matrix)}")
