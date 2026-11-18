import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

issues = []
for ex in exercises:
    if ex.get('bookId') == 'skm-n2' and ex.get('chapter') in ['Part 1 · Chapter 7', 'Part 1 · Chapter 8', 'Part 1 · Chapter 9']:
        eid = ex.get('id')
        opts = ex.get('explanation', {}).get('options', [])
        for i, o in enumerate(opts):
            r = o.get('reason', '')
            t = o.get('text', '')
            c = o.get('isCorrect', False)
            if '文脈・文法関係' in r or '不適切です。' in r:
                # check if generic
                if '文脈・文法関係' in r or r.strip() in ['不適切です。', '【不正解】不適切です。']:
                    issues.append(f"{eid} opt {i} ({t}): generic -> {r}")
            if c and not r.startswith('【正解】'):
                issues.append(f"{eid} opt {i} ({t}): correct without 【正解】 -> {r}")
            if not c and not r.startswith('【不正解】'):
                issues.append(f"{eid} opt {i} ({t}): distractor without 【不正解】 -> {r}")

print(f"Total issues in Ch 7-9: {len(issues)}")
for iss in issues:
    print(" ", iss)
