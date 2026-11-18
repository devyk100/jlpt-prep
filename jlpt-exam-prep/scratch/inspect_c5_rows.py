import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

c5_rows = [r for r in data if r.get('sourceBook') == 'Shin Kanzen Master N3' and r.get('sourceSection') == 'Part 1 · Chapter 5']
for r in c5_rows:
    print(json.dumps(r, indent=2, ensure_ascii=False))
