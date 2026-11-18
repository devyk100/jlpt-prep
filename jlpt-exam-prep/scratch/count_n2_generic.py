import json
from collections import defaultdict

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

generic_by_chap = defaultdict(list)

for ex in exercises:
    if ex.get('bookId') != 'skm-n2':
        continue
    eid = ex.get('id')
    chap = ex.get('chapter')
    opts = ex.get('explanation', {}).get('options', [])
    for opt in opts:
        reason = opt.get('reason', '')
        if '文脈・文法関係' in reason or '不適切です。' in reason:
            # check if it is generic boilerplate
            if '文脈・文法関係' in reason or reason.strip() in ['不適切です。', '【不正解】不適切です。']:
                generic_by_chap[chap].append((eid, opt.get('text'), reason))

print("Generic reasons count by SKM N2 chapter:")
for chap, items in sorted(generic_by_chap.items()):
    print(f"  {chap}: {len(items)} generic options across {len(set(x[0] for x in items))} exercises")
