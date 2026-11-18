import json

with open('c:/JLPT/jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

skm3_cards = [c for c in cards if 'Shin Kanzen Master N3' in str(c.get('book', '')) or 'N3' in str(c.get('chapter', ''))]
print(f"Total N3 cards in base-reviewed.json: {len(skm3_cards)}")

chapters = {}
for c in skm3_cards:
    ch = c.get('chapter', 'Unknown')
    chapters[ch] = chapters.get(ch, 0) + 1

for ch, count in sorted(chapters.items()):
    print(f"{ch}: {count} cards")
