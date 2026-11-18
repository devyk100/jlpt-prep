import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex['id'] in ['skm2-p1-c24-q11', 'skm2-p1-c24-q12', 'skm2-p1-c25-q1', 'skm2-p1-c25-q2']:
        print(f"=== {ex['id']} ===")
        print(f"Q: {ex['question']}")
        print(f"Opts: {ex['options']}")
        print(f"Key: {ex['correctIndex']} ({ex['options'][ex['correctIndex']]})")
        print(f"Exp: {json.dumps(ex['explanation'], ensure_ascii=False, indent=2)}")
