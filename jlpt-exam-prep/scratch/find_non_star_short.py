import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex.get('type') == 'star' or '【★】' in ex.get('question', '') or '★' in ex.get('question', '') or ex.get('reconstructedSentence'):
        continue
    eid = ex.get('id')
    opts = ex.get('explanation', {}).get('options', [])
    for idx, opt in enumerate(opts):
        r = opt.get('reason', '').strip()
        if len(r) < 22:
            print(f"[{eid}] opt {idx} ({opt.get('text')}): {r} (len={len(r)})")
