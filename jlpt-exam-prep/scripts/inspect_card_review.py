import json

with open("jlpt-exam-prep/audit/card-review.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

print(f"Total cards in card-review: {len(cards)}")

statuses = {}
for c in cards:
    st = c.get('reviewStatus', 'unknown')
    statuses[st] = statuses.get(st, 0) + 1
print("Review statuses:", statuses)

missing_uses = [c for c in cards if c.get('missingUses') and len(c.get('missingUses')) > 0]
print(f"Cards with explicit missing uses: {len(missing_uses)}")
for c in missing_uses[:5]:
    print(f"  [{c['id']}] {c['title']}: {c['missingUses']}")

checked = [c for c in cards if c.get('reviewStatus') == 'checked']
print(f"Total checked cards: {len(checked)}")
for c in checked[:10]:
    print(f"  [{c['id']}] {c['title']} (missing: {c.get('missingUses')})")
