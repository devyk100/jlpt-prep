import json

with open('c:/JLPT/jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

with open('c:/JLPT/jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

skm3_cards = [c for c in cards if 'Shin Kanzen Master N3' in str(c.get('book', ''))]
print(f"Total SKM N3 cards in base-reviewed: {len(skm3_cards)}")

skm3_matrix = [r for r in matrix if 'N3' in str(r.get('sourceBook', ''))]
print(f"Total SKM N3 rows in matrix: {len(skm3_matrix)}")

checked_matrix = [r for r in skm3_matrix if r.get('status') == 'checked']
print(f"Checked SKM N3 rows in matrix: {len(checked_matrix)}")

# Print sample SKM N3 card
if skm3_cards:
    c = skm3_cards[0]
    print("\nSample N3 card:")
    print("ID:", c.get('id'))
    print("Book:", c.get('book'))
    print("Chapter:", c.get('chapter'))
    print("Title:", c.get('title'))
    print("Nuance:", c.get('nuance')[:100] if c.get('nuance') else "None")
