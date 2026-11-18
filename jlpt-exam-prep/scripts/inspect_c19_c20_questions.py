import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

print("=== Chapter 19 Exercises ===")
for e in exs:
    if 'c19' in e['id']:
        print(f"[{e['id']}] Q: {e['question']} | Correct: {e['options'][e['correctIndex']]}")

print("\n=== Chapter 20 Exercises ===")
for e in exs:
    if 'c20' in e['id']:
        print(f"[{e['id']}] Q: {e['question']} | Correct: {e['options'][e['correctIndex']]}")
