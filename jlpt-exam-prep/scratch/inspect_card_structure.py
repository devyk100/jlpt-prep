import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

p = [x for x in points if x.get('id') == 'skm2-c4-wo-hajime'][0]
print(json.dumps(p, ensure_ascii=False, indent=2))
