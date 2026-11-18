import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))

for ch_num in range(21, 27):
    ch_name = f"Part 1 · Chapter {ch_num}"
    qs = [q for q in exercises if q.get('chapter') == ch_name]
    print(f"=== {ch_name}: {len(qs)} questions ===")
    for q in qs:
        # Check alignment between question and translation
        print(f"[{q['id']}] Q: {q.get('question')}")
        print(f"       T: {q.get('translation')}")
        opts = q.get('explanation', {}).get('options', [])
        generics = [o['text'] for o in opts if '文脈・文法関係' in o.get('reason', '') or '不適切です' in o.get('reason', '') or '不自然です' in o.get('reason', '')]
        if generics:
            print(f"       Generics in: {generics}")
