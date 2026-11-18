import json

data = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
for idx in range(53, 105):
    r = data[idx]
    sec = r.get("sourceSection")
    item = r.get("grammarItem")
    mw = r.get("missingWork")
    st = r.get("status")
    print(f"Row {idx:3d} | {sec:12s} | {st:7s} | {item[:30]:30s} | {mw}")
