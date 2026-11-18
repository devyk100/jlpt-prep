import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)

by_book = {}
for p in sps:
    b = p.get('book', 'Unknown')
    by_book.setdefault(b, []).append(p)

for b, cards in by_book.items():
    print(f"\n==================== BOOK: {b} (Total: {len(cards)}) ====================")
    for c in cards:
        print(f"[{c['id']}] (Ch {c.get('chapter')}) {c['title']}")
