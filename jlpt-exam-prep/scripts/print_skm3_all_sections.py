import json

with open('c:/JLPT/jlpt-exam-prep/src/data/bookSources.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

skm3 = next(b for b in books if b['id'] == 'skm-n3')
for i, s in enumerate(skm3['sections'], 1):
    print(f"{i}. {s['name']} -> {len(s['grammarIds'])} cards: {s['grammarIds']}")
