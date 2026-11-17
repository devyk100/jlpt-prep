import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

zero_quiz = [p for p in points if len(p.get('quiz', [])) == 0]

print(f"Total zero-quiz cards: {len(zero_quiz)}")

by_book = {}
for p in zero_quiz:
    b = p.get('book', 'Comparison/Synthesis')
    by_book.setdefault(b, []).append(p)

for b, pts in by_book.items():
    print(f"\n=== {b} ({len(pts)} cards with 0 quizzes) ===")
    for p in pts:
        print(f"  [{p['id']}] {p['title']} ({p.get('chapter')})")
