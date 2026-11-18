import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for eid in ['skm3-c2-ex-7', 'skm3-c5-ex-8', 'g2-l15-ex-3']:
    for ex in exercises:
        if ex['id'] == eid:
            print(f"=== {eid} ===")
            print(json.dumps(ex, ensure_ascii=False, indent=2))
