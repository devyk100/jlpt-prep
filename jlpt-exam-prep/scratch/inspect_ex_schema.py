import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print("Exercise 0 keys:", list(exercises[0].keys()))
print("\nExercise 0 sample:")
print(json.dumps(exercises[0], ensure_ascii=False, indent=2))

for ex in exercises:
    if ex.get('book') == 'Shin Kanzen Master N2':
        print("\nSKM N2 Exercise sample:")
        print(json.dumps(ex, ensure_ascii=False, indent=2))
        break
