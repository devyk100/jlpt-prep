import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
for idx, r in enumerate(matrix):
    sec = r.get('sourceSection', '')
    if 'Form review' in sec:
        print(f"Row {idx:3d} | {sec:25s} | cid: {str(r.get('cardId')):25s} | status: {r.get('status')} | {r.get('grammarItem')}")
        print(f"   missingWork: {r.get('missingWork')}")
        print(f"   evidence   : {r.get('evidence')[:100]}...")
