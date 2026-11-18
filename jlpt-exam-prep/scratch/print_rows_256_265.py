import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
for idx in [256, 257, 258, 259, 260, 261, 262, 263, 264, 265]:
    r = matrix[idx]
    print(f"--- Row {idx} ---")
    for k, v in r.items():
        print(f"  {k}: {v}")
