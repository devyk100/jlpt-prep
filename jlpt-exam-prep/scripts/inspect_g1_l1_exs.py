import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

for ex in exs:
    if ex.get('bookId') == 'genki-1' and ex.get('chapter') == 'Lesson 1':
        print(f"ID: {ex['id']}")
        print(f"  Question: {ex['question']}")
        print(f"  Context: {ex.get('context')}")
        print(f"  Translation: {ex['translation']}")
        print(f"  Options: {ex['options']}")
        print(f"  Correct: {ex['options'][ex['correctIndex']]}")
        print('---')
