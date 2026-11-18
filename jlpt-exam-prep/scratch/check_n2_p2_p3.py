import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    if ex.get('bookId') == 'skm-n2' and ('Part 2' in ex.get('chapter', '') or 'Part 3' in ex.get('chapter', '')):
        opts = ex.get('explanation', {}).get('options', [])
        for opt in opts:
            reason = opt.get('reason', '')
            if '文脈・文法関係' in reason or '不適切です。' in reason:
                print(ex.get('id'), ex.get('chapter'), opt.get('text'), reason)
