import json

with open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

for c in cards:
    if c['id'].startswith(('added-n3-', 'added-n2-')):
        print(f"{c['id']} | {c['title']} | {c.get('book')} {c.get('chapter')}")
