import json

with open('c:/JLPT/jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

c1_cards = [c for c in cards if c.get('chapter') == 'Part 1 · Chapter 1']
print(f"Cards in Part 1 · Chapter 1: {len(c1_cards)}")
for c in c1_cards:
    print(c.get('id'), '|', c.get('title'), '|', c.get('pattern'))
    print("  Nuance:", c.get('nuance')[:120] if c.get('nuance') else "None")
    print("  SourceRef:", c.get('sourceReference'))
