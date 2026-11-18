import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c25_exercises = [ex for ex in exercises if ex.get('chapter') == 'Part 1 · Chapter 25']
print(f"Total C25 exercises: {len(c25_exercises)}")
for ex in c25_exercises:
    print(f"ID: {ex['id']}")
    print(f"  Q: {ex['question']}")
    print(f"  Ctx: {ex.get('context')}")
    print(f"  Tr: {ex.get('translation')}")
    print(f"  Key: {ex['options'][ex['correctIndex']]}")
    print('-'*40)
