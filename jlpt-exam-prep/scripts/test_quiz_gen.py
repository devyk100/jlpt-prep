import json
import re

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

zero_quiz_points = [p for p in points if len(p.get('quiz', [])) == 0]
print(f"Total zero-quiz cards: {len(zero_quiz_points)}")

for p in zero_quiz_points[:5]:
    print(f"\n--- Card: [{p['id']}] {p['title']} ({p.get('book')}) ---")
    print(f"Meaning: {p['meaning']}")
    print(f"Connection: {p['connection']}")
    print(f"Sentences: {len(p['sentences'])}")
    for s in p['sentences']:
        print(f"  * {s['japanese']} -> {s['english']}")
