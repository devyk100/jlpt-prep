import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))

for review_letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    ch_name = f"Part 1 · Form review {review_letter.upper()}"
    qs = [q for q in exercises if q.get('chapter') == ch_name]
    print(f"=== {ch_name}: {len(qs)} questions ===")
    for q in qs:
        opts = q.get('explanation', {}).get('options', [])
        corrupted = [o['text'] for o in opts if '【不正解】正解です' in o.get('reason', '')]
        generics = [o['text'] for o in opts if '文脈・文法関係' in o.get('reason', '') or '不適切です' in o.get('reason', '')]
        print(f"[{q['id']}] Q: {q.get('question')[:40]}... Ans: {q.get('correctIndex')} ({q.get('options')[q.get('correctIndex')]})")
        if corrupted:
            print(f"    CORRUPTED: {corrupted}")
        if generics:
            print(f"    Generics in: {generics}")
