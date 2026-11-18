import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

for idx, r in enumerate(matrix):
    if 'くせに' in str(r):
        print(f"Matrix Row {idx}:")
        print(json.dumps(r, ensure_ascii=False, indent=2))
