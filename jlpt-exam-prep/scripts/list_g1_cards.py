import json

with open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

for c in cards:
    if c.get('book') == 'Genki I':
        print(f"{c['chapter']} | {c['id']} | {c['title']}")
