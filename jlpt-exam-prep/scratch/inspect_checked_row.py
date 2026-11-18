import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

for r in matrix:
    if r.get('sourceBook') == 'Shin Kanzen Master N2' and r.get('sourceSection') in ['Part 1 · Chapter 1', 'Part 1 · Chapter 2']:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        break
