import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))

for let in ['b', 'c', 'd', 'e', 'f', 'g']:
    qs = [q for q in exercises if q.get('id', '').startswith(f"skm2-p1-form-review-{let}")]
    print(f"=== Form Review {let.upper()}: {len(qs)} questions ===")
    for q in qs:
        print(f"[{q['id']}] Q: {q['question']}")
        print(f"   Opts: {q['options']}, Ans: {q['correctIndex']}")
