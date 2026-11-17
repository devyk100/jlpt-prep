import re

with open('jlpt-exam-prep/src/data/mugUpTables.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find any string inside quotes in mugUpTables.ts
strings = re.findall(r"'([^']*)'", text)

print(f'Total strings in mugUpTables.ts: {len(strings)}')

# Check each string for parenthesized romaji or pronunciation
romaji_candidates = []
for s in strings:
    # Pattern where a kanji or kana word is followed by (romaji)
    # e.g., 買う (kau), 待つ (matsu), ぷん (pun), いい (ii), はたち (hatachi)
    # or where english pronunciation is in parentheses
    m = re.findall(r'[\u3040-\u30ff\u4e00-\u9faf]+\s*\([a-zA-Z\s/-]+\)', s)
    if m:
        romaji_candidates.append((s, m))

print(f'Strings with kanji/kana + (latin): {len(romaji_candidates)}')
for s, matches in romaji_candidates:
    print(f'String: {s}')
    print(f'   Matches: {matches}')
