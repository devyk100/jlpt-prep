import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))
ch_map = {}
for q in exercises:
    ch = q.get('chapter', '')
    if any(k in ch for k in ['21', '22', '23', '24', '25', '26']):
        ch_map.setdefault(ch, []).append(q)

for ch, qs in sorted(ch_map.items()):
    print(f"Chapter: {ch:25s} | Questions: {len(qs)}")
    generic_count = 0
    for q in qs:
        opts = q.get('explanation', {}).get('options', [])
        for opt in opts:
            r = opt.get('reason', '')
            if '文脈・文法関係' in r or '不適切です' in r or '不自然です' in r or '文脈に合いません' in r:
                generic_count += 1
    print(f"   Generic distractor reasons in {ch}: {generic_count}")
