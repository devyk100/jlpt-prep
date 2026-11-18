import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ch_name in ['Part 1 · Chapter 6', 'Part 1 · Chapter 10', 'Part 1 · Form review A', 'Part 3 · Chapter 1']:
    exs = [e for e in exercises if e.get('bookId') == 'skm-n3' and e.get('chapter') == ch_name]
    if exs:
        e = exs[0]
        print(f"=== {e['id']} ({ch_name}) ===")
        for opt in e['explanation']['options']:
            print(f"  Opt [{opt['text']}]: {opt['reason']}")
