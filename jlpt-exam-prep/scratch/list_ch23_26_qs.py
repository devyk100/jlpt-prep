import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))

for ch in [23, 24, 25, 26]:
    qs = [q for q in exercises if q.get('chapter') == f'Part 1 · Chapter {ch}']
    print(f"=== Chapter {ch}: {len(qs)} questions ===")
    for q in qs:
        print(f"[{q['id']}] Q: {q['question']}")
        print(f"  Options: {q['options']}, Ans: {q['correctIndex']}")
