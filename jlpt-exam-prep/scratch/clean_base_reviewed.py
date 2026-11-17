import json

with open('jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'r', encoding='utf-8') as f:
    tables = json.load(f)

for c in cards:
    if c.get('id') == 'genki1-te-form':
        c['nuance'] = 'CRITICAL EXCEPTION: 行く は「いいて」にならず、「行って」と促音便になります。'
        c['table'] = tables['teFormMatrix']
    elif c.get('id') == 'added-g1-6-8':
        c['table'] = tables['teFormMatrix']
    elif 'table' in c and c['table'].get('title') == 'The Te-Form (て形) Conjugation Matrix':
        c['table'] = tables['teFormMatrix']

with open('jlpt-exam-prep/content/base-reviewed.json', 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Updated base-reviewed.json successfully!')
