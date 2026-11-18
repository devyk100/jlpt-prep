import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))
ch22_qs = [q for q in exercises if q.get('chapter') == 'Part 1 · Chapter 22']

for i, q in enumerate(ch22_qs):
    print(f"Index {i}: {q['id']}")
    print(f"  Japanese: {q['question']}")
    print(f"  Context : {q['context']}")
    print(f"  Transl  : {q['translation']}")
    print(f"  Options : {q['options']}")
    print(f"  Correct : {q['correctIndex']} -> {q['options'][q['correctIndex']]}")
    for j, opt in enumerate(q['explanation']['options']):
        print(f"    Opt {j} ({opt['text']}): {opt['reason']}")
    print()
