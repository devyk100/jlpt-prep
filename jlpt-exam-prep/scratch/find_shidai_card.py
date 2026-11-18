import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)

for sp in sps:
    if 'shidai' in sp['id'] or '次第' in sp['title'] or ('c1' in sp['id'] and 'skm2' in sp['id']):
        print(f"ID: {sp['id']} | Title: {sp['title']}")
