import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
for idx in [322, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333]:
    r = matrix[idx]
    print(f"--- Row {idx} ---")
    for k, v in r.items():
        print(f"  {k}: {v}")
