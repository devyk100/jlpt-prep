import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c14_17_exs = [ex for ex in exercises if ex.get('bookId') == 'skm-n2' and ex.get('chapter') in [
    'Part 1 · Chapter 14', 'Part 1 · Chapter 15', 'Part 1 · Chapter 16', 'Part 1 · Chapter 17'
]]

print(f"Total exercises in Ch 14-17: {len(c14_17_exs)}")

generic_count = 0
for ex in c14_17_exs:
    eid = ex.get('id')
    chap = ex.get('chapter')
    opts = ex.get('explanation', {}).get('options', [])
    for opt in opts:
        r = opt.get('reason', '')
        if '文脈・文法関係' in r or '不適切です。' in r:
            generic_count += 1

print(f"Generic options count in Ch 14-17: {generic_count}")
