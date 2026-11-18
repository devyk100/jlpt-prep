import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

truly_short = []
for ex in exercises:
    eid = ex.get('id')
    opts = ex.get('explanation', {}).get('options', [])
    for idx, opt in enumerate(opts):
        r = opt.get('reason', '').strip()
        # Exclude star exercise element descriptions like "1番目の要素。従属節の主語です。" if we want, or inspect them all
        if len(r) < 30:
            truly_short.append((eid, idx, opt.get('text'), r, len(r)))

print(f"Total options with reason length < 30 chars: {len(truly_short)}")
for item in truly_short:
    print(f"[{item[0]}] opt {item[1]} ({item[2]}): {item[3]} (len={item[4]})")
