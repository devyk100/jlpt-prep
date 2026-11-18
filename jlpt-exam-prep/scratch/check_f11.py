import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex.get('id') == 'skm2-p1-form-review-f-q11':
        print(json.dumps(ex, ensure_ascii=False, indent=2))
