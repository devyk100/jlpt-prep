import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

n2_remaining = [p for p in points if p.get('book') == 'Shin Kanzen Master N2' and len(p.get('quiz', [])) == 0]
print(f"Remaining N2 cards without quiz: {len(n2_remaining)}")
for p in n2_remaining:
    print(f"  {p['id']}: {p['title']}")
