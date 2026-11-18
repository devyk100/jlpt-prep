import json
import re

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)
card_ids = set(c['id'] for c in cards)

with open('jlpt-exam-prep/scripts/assemble-content.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'card_table_map = \{(.*?)\}', text, re.DOTALL)
entries = re.findall(r"'([^']+)':\s*'([^']+)'", m.group(1))

print(f'Total mapped entries: {len(entries)}')
for cid, tkey in entries:
    exists = cid in card_ids
    if not exists:
        print(f'  MISSING CARD: {cid} -> {tkey}')
    else:
        card = next(c for c in cards if c['id'] == cid)
        print(f'  OK: {cid} ("{card["title"][:30]}") -> {tkey}')
