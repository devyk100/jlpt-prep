import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    eid = ex.get('id')
    exp = ex.get('explanation', {})
    opts = exp.get('options', [])
    for idx, opt in enumerate(opts):
        if opt.get('isCorrect'):
            reason = opt.get('reason', '')
            if '【不正解】' in reason or 'Incorrect' in reason or '不適切' in reason:
                print(f"EID: {eid}, correctIndex in ex: {ex.get('correctIndex')}, optIndex: {idx}, text: {opt.get('text')}")
                print(f"   Reason: {reason}\n")
