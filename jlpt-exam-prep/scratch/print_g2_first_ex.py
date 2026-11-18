import json

exs = [e for e in json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8')) if e.get('bookId') == 'genki-2']
first_exs = {}
for e in exs:
    ch = e['chapter']
    if ch not in first_exs:
        first_exs[ch] = e

for ch in sorted(first_exs.keys(), key=lambda x: int(x.replace('Lesson ', ''))):
    fe = first_exs[ch]
    c_idx = fe['correctIndex']
    print(f"{ch}: id={fe['id']}, correctOpt='{fe['options'][c_idx]}', question='{fe['question']}'")
