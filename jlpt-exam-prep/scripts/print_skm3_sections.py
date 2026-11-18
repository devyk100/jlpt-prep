import json

with open('c:/JLPT/jlpt-exam-prep/src/data/bookSources.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

skm3 = next(b for b in books if b['id'] == 'skm-n3')
for s in skm3['sections']:
    print(s['id'], '|', s['name'], '|', len(s['grammarIds']), 'cards:', s['grammarIds'])
