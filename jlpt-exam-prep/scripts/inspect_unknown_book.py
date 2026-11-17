import json

pts = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
unknowns = [p for p in pts if not p.get('book')]
print("Unknown count:", len(unknowns))
for u in unknowns[:15]:
    print(u['id'], u['title'], u.get('level'), u.get('chapter'), u.get('tags'))
