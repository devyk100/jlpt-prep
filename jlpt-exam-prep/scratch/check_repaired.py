import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for eid in ['skm2-p1-c20-q3', 'skm2-p1-c20-q4', 'skm2-p1-c24-q11', 'skm2-p1-c24-q12', 'skm2-p1-c25-q1', 'skm2-p1-c25-q2']:
    for ex in exercises:
        if ex['id'] == eid:
            print(f"=== {eid} ===")
            print(f"Q:   {ex['question']}")
            print(f"Ctx: {ex.get('context')}")
            print(f"Tr:  {ex.get('translation')}")
            print(f"Key: {ex['options'][ex['correctIndex']]}")
