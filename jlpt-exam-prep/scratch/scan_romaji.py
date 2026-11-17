import re

with open('jlpt-exam-prep/src/data/mugUpTables.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# find any word in latin characters surrounded by parentheses
romaji_paren = re.findall(r'\([a-zA-Z\s/,\.\-–—\?\'\:\!]+\)', text)
print(f'Total parenthesized latin expressions: {len(romaji_paren)}')
for p in set(romaji_paren):
    # filter out purely grammatical labels like (Dictionary), (Passive), etc.
    # vs romaji pronunciation like (kau), (matsu), (pun), (ii), etc.
    print('  ', p)
