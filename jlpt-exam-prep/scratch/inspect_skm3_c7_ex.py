import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c7_ex = [e for e in exercises if e.get('bookId') == 'skm-n3' and e.get('chapter') == 'Part 1 · Chapter 7']
print(f"Total exercises in SKM N3 Chapter 7: {len(c7_ex)}")

for e in c7_ex:
    print(f"=== {e['id']} ===")
    print("Q:", e['question'])
    print("Trans:", e['translation'])
    for i, opt in enumerate(e['explanation']['options']):
        print(f"  Opt {i} [{opt['text']}] (isCorrect: {opt['isCorrect']}): {opt['reason']}")
    print()
