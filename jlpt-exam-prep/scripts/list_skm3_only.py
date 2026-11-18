import json

with open('c:/JLPT/jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

skm3_only = [c for c in cards if c.get('book') == 'Shin Kanzen Master N3']
print(f"Total cards with book == 'Shin Kanzen Master N3': {len(skm3_only)}")

ch_map = {}
for c in skm3_only:
    ch = c.get('chapter', 'Unknown')
    ch_map.setdefault(ch, []).append(c)

for ch, clist in sorted(ch_map.items()):
    print(f"\n=== {ch} ({len(clist)} cards) ===")
    for c in clist:
        print(f"  {c['id']} | {c['title']}")
