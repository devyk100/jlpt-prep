import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

for p in points:
    if 'connect actions' in p['meaning'].lower() or 'connect actions' in p['title'].lower():
        print(f"[{p['id']}] title: {p['title']}, meaning: {p['meaning']}")
