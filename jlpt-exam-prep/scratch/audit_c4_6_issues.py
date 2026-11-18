import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex.get('bookId') == 'skm-n2' and ex.get('chapter') in ['Part 1 · Chapter 4', 'Part 1 · Chapter 5', 'Part 1 · Chapter 6']:
        eid = ex.get('id')
        opts = ex.get('explanation', {}).get('options', [])
        # Check reasons
        issues = []
        for i, o in enumerate(opts):
            r = o.get('reason', '')
            t = o.get('text', '')
            c = o.get('isCorrect', False)
            if c and not r.startswith('【正解】'):
                issues.append(f"Opt {i} ({t}) is correct but reason: {r}")
            elif not c and not r.startswith('【不正解】'):
                issues.append(f"Opt {i} ({t}) is distractor but reason doesn't start with 【不正解】: {r}")
            if '文脈・文法関係' in r:
                issues.append(f"Opt {i} ({t}) has generic 文脈・文法関係: {r}")
            if r.strip() in ['【不正解】不適切です。', '不適切です。']:
                issues.append(f"Opt {i} ({t}) is bare 不適切です: {r}")
        if issues:
            print(f"=== {eid}: {ex.get('question')} ===")
            for iss in issues:
                print("  *", iss)
