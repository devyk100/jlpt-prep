import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = {p['id']: p for p in json.load(f)}

pt = points.get('added-n2-c-118')
print(f"Title: {pt['title']}")
print(f"Meaning: {pt['meaning']}")
print(f"Nuance: {pt['nuance']}")
print(f"Sentences count: {len(pt['sentences'])}")
for s in pt['sentences']:
    print(f"  [{s.get('useLabel')}] {s['japanese']}")
