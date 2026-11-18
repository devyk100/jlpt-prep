import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex.get('id') == 'skm3-p2-c1-q7':
        print(json.dumps(ex, ensure_ascii=False, indent=2))
