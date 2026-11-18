import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex['id'] in ['skm2-p1-c25-q1', 'skm2-p1-c25-q2']:
        print(json.dumps(ex, ensure_ascii=False, indent=2))
