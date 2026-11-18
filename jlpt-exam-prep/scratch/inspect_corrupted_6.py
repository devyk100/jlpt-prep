import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

targets = ['skm2-p1-c4-q10', 'skm2-p1-c4-q11', 'skm2-p1-c5-q5', 'skm2-p1-c5-q6', 'skm2-p1-c5-q9', 'skm2-p1-c5-q10']

for ex in exercises:
    if ex.get('id') in targets:
        print(f"ID: {ex.get('id')}")
        print(f"Question: {ex.get('question')}")
        print(f"Options: {ex.get('options')}")
        print(f"CorrectIndex: {ex.get('correctIndex')}")
        print("Explanation Options:")
        for opt in ex.get('explanation', {}).get('options', []):
            print(f"  text: {opt.get('text')}, isCorrect: {opt.get('isCorrect')}, reason: {opt.get('reason')}")
        print("-" * 50)
