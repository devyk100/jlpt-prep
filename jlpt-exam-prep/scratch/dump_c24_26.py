import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ch_name in ['Part 1 · Chapter 24', 'Part 1 · Chapter 25', 'Part 1 · Chapter 26']:
    print(f"\n==================== {ch_name} ====================")
    for ex in exercises:
        if ex.get('chapter') == ch_name:
            print(f"[{ex['id']}] Q: {ex['question']}")
            print(f"  Key: {ex['correctIndex']} ({ex['options'][ex['correctIndex']]})")
            print(f"  Overall: {ex['explanation']['overall'][:70]}...")
