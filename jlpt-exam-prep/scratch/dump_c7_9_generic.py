import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c7_9_exs = [ex for ex in exercises if ex.get('bookId') == 'skm-n2' and ex.get('chapter') in ['Part 1 · Chapter 7', 'Part 1 · Chapter 8', 'Part 1 · Chapter 9']]

print(f"Total exercises in Ch 7-9: {len(c7_9_exs)}")

for ex in c7_9_exs:
    eid = ex.get('id')
    chap = ex.get('chapter')
    q = ex.get('question')
    ci = ex.get('correctIndex')
    opts = ex.get('explanation', {}).get('options', [])
    generic_opts = []
    for idx, opt in enumerate(opts):
        r = opt.get('reason', '')
        if '文脈・文法関係' in r or '不適切です。' in r or (opt.get('isCorrect') and '【不正解】' in r):
            generic_opts.append((idx, opt.get('text'), opt.get('isCorrect'), r))
    if generic_opts:
        print(f"\n=== {eid} ({chap}) ===")
        print(f"Q: {q}")
        print(f"Correct: [{ci}] {opts[ci].get('text')}")
        for idx, text, corr, r in generic_opts:
            print(f"  [{idx}] {text} (isCorrect={corr}): {r}")
