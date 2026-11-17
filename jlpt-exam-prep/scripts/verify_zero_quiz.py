import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

zero = [p for p in points if len(p.get('quiz', [])) == 0]
print(f"Total cards: {len(points)}")
print(f"Total zero-quiz cards remaining: {len(zero)}")
if zero:
    for z in zero:
        print(f"  {z['id']}: {z['title']}")
