import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))
ch21_qs = [q for q in exercises if q.get('chapter') == 'Part 1 · Chapter 21']

for q in ch21_qs:
    print(f"=== {q['id']} ===")
    print(f"Question: {q.get('question')}")
    print(f"Context: {q.get('context')}")
    print(f"Translation: {q.get('translation')}")
    print(f"Options: {q.get('options')}")
    print(f"CorrectIndex: {q.get('correctIndex')}")
    exp = q.get('explanation', {})
    print(f"Overall: {exp.get('overall')}")
    for opt in exp.get('options', []):
        print(f"  [{opt.get('isCorrect')}] {opt.get('text')}: {opt.get('reason')}")
    print()
