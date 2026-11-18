import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex.get('bookId') == 'skm-n2' and ex.get('chapter') in ['Part 1 · Chapter 4', 'Part 1 · Chapter 5', 'Part 1 · Chapter 6']:
        eid = ex.get('id')
        print(f"=== {eid} ===")
        print(f"Chapter: {ex.get('chapter')}")
        print(f"Question: {ex.get('question')}")
        print(f"Translation: {ex.get('translation')}")
        print(f"Options: {ex.get('options')}")
        print(f"CorrectIndex: {ex.get('correctIndex')}")
        for idx, opt in enumerate(ex.get('explanation', {}).get('options', [])):
            print(f"  opt {idx} [{opt.get('text')}]: isCorrect={opt.get('isCorrect')}")
            print(f"    reason: {opt.get('reason')}")
