import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c20_exs = [ex for ex in exercises if ex.get('chapter') == 'Part 1 · Chapter 20' and ex['id'].startswith('skm2-p1-c20-q')]
for ex in c20_exs:
    print(f"=== {ex['id']} ===")
    print(f"Q:   {ex['question']}")
    print(f"Ctx: {ex.get('context')}")
    print(f"Tr:  {ex.get('translation')}")
    print(f"Opts: {ex['options']} (Key: {ex['correctIndex']}: {ex['options'][ex['correctIndex']]})")
    print(f"Exp overall: {ex['explanation']['overall']}")
    for opt in ex['explanation']['options']:
        print(f"  opt: {opt['text']} (isCorrect={opt['isCorrect']}) -> {opt['reason'][:60]}...")
