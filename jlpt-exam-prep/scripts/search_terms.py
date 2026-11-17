import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

for target in ['まじき', 'べからず', '甲斐', 'をおいて', 'かいが']:
    matches = [p for p in points if target in p['title'] or target in p['meaning'] or target in p['connection'] or any(target in s['japanese'] for s in p['sentences'])]
    print(f"Target '{target}': {len(matches)} matches")
    for m in matches:
        print(f"  [{m['id']}] {m['title']} ({m.get('book')})")
