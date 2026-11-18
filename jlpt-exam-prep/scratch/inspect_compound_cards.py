import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

for cid in ['added-n2-14-92', 'added-n2-15-93', 'added-n2-19-101', 'added-n2-16-96', 'added-n2-17-98']:
    p = points_by_id.get(cid)
    if p:
        print(f"=== {cid}: {p.get('title')} ===")
        print(f"Explanation:\n{p.get('explanation')}\n")
        print("Sentences:")
        for s in p.get('sentences', []):
            print(f"  [{s.get('id')}]: {s.get('japanese')} / {s.get('english')}")
        print("-" * 50)
