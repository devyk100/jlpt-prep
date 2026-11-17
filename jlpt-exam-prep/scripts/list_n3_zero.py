import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

n3_zero = [p for p in points if p.get('book') == 'Shin Kanzen Master N3' and len(p.get('quiz', [])) == 0]
print(f"N3 zero-quiz cards: {len(n3_zero)}")
for p in n3_zero:
    print(f"  {p['id']}: {p['title']}")
