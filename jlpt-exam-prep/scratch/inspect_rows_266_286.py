import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
for idx in range(266, 287):
    r = matrix[idx]
    print(f"Row {idx:3d} | {r.get('sourceSection')} | {r.get('grammarItem')} | {r.get('cardId')} | {r.get('status')}")
    print(f"   missingWork: {r.get('missingWork')}")
    print(f"   evidence   : {r.get('evidence')[:100]}...")
