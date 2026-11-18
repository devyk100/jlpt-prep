import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))

for ch_num in range(23, 27):
    ch_name = f"Part 1 · Chapter {ch_num}"
    qs = [q for q in exercises if q.get('chapter') == ch_name]
    print(f"==================== {ch_name} ({len(qs)} qs) ====================")
    for q in qs:
        print(f"--- {q['id']} ---")
        print(f"Q: {q.get('question')}")
        print(f"C: {q.get('context')}")
        print(f"T: {q.get('translation')}")
        print(f"Opts: {q.get('options')}")
        print(f"Ans : {q.get('correctIndex')} -> {q.get('options')[q.get('correctIndex')]}")
        for opt in q.get('explanation', {}).get('options', []):
            print(f"  [{opt.get('isCorrect')}] {opt.get('text')}: {opt.get('reason')}")
