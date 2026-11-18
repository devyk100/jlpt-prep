import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    eid = ex.get('id')
    exp_opts = ex.get('explanation', {}).get('options', [])
    for idx, opt in enumerate(exp_opts):
        r = opt.get('reason', '')
        if len(r.strip()) < 20:
            print(f"[{eid}] opt {idx} ({opt.get('text')}): {r} (len={len(r.strip())})")
