import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c4_6_exs = [ex for ex in exercises if ex.get('bookId') == 'skm-n2' and ex.get('chapter') in ['Part 1 · Chapter 4', 'Part 1 · Chapter 5', 'Part 1 · Chapter 6']]

print(f"Total exercises in Ch 4-6: {len(c4_6_exs)}")

for ex in c4_6_exs:
    eid = ex.get('id')
    q = ex.get('question')
    ci = ex.get('correctIndex')
    opts = ex.get('explanation', {}).get('options', [])
    has_generic = False
    for opt in opts:
        r = opt.get('reason', '')
        if '文脈・文法関係' in r or '不適切です。' in r or (opt.get('isCorrect') and '【不正解】' in r):
            has_generic = True
            break
    if has_generic:
        print(f"\n--- {eid} ({ex.get('chapter')}) ---")
        print(f"Q: {q}")
        print(f"Correct: {opts[ci].get('text')}")
        for idx, opt in enumerate(opts):
            print(f"  [{idx}] {opt.get('text')} (isCorrect={opt.get('isCorrect')}): {opt.get('reason')}")
