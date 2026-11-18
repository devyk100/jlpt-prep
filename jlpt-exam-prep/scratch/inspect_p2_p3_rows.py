import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
for idx in range(295, 316):
    r = matrix[idx]
    print(f"Row {idx:3d} | {r.get('sourceSection'):25s} | cid: {str(r.get('cardId')):25s} | status: {r.get('status')} | {r.get('grammarItem')}")
    print(f"   missingWork: {r.get('missingWork')}")
    print(f"   evidence   : {r.get('evidence')[:100]}...")
