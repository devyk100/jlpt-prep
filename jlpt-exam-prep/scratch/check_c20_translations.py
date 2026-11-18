import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c20_exercises = [ex for ex in exercises if ex.get('chapter') == 'Part 1 · Chapter 20' or 'c20' in ex.get('id', '')]
print(f"Total C20 exercises: {len(c20_exercises)}")
for ex in c20_exercises:
    print(f"ID: {ex['id']}")
    print(f"  Q: {ex.get('question')}")
    print(f"  Ctx: {ex.get('context')}")
    print(f"  Tr: {ex.get('translation')}")
    print(f"  Key: {ex['options'][ex['correctIndex']]}")
    print('-'*40)
