import json

with open('c:/JLPT/jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

for r in matrix:
    if 'N3' in str(r.get('sourceBook', '')):
        print(r.get('cardId'), '|', r.get('sourceSection'), '|', r.get('grammarItem'), '|', r.get('status'))
