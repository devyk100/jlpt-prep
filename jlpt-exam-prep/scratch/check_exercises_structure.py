import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

non_dict = 0
for i, ex in enumerate(exercises):
    opts = ex.get('options', [])
    for opt in opts:
        if not isinstance(opt, dict):
            non_dict += 1
            print(f"Ex {i} (id={ex.get('id')}) has non-dict option: {type(opt)} -> {opt}")
            if non_dict >= 10:
                break
    if non_dict >= 10:
        break

print(f"Total exercises: {len(exercises)}, non-dict options encountered: {non_dict}")
