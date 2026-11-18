import json

with open("jlpt-exam-prep/src/data/mugUpTables.json", encoding="utf-8") as f:
    tables = json.load(f)

print("Type of tables:", type(tables))
if isinstance(tables, dict):
    print("Keys in mugUpTables.json:", list(tables.keys())[:10])
elif isinstance(tables, list):
    print("Length of list:", len(tables))
    if len(tables) > 0:
        print("Type of first element:", type(tables[0]))
        print("First element:", tables[0])

with open("jlpt-exam-prep/audit/card-review.json", encoding="utf-8") as f:
    cards = json.load(f)

g2_cards = [c for c in cards if c.get("book") == "Genki II"]
print("G2 cards in card-review.json:", len(g2_cards))
for c in g2_cards[:10]:
    print(f"{c['id']}: status={c.get('reviewStatus')} | missingUses={c.get('missingUses')} | distinctUses={len(c.get('distinctUses', []))}")
