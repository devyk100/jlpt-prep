import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
sp_map = {sp['id']: sp for sp in json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))}

for idx in range(266, 287):
    r = matrix[idx]
    cid = r.get('cardId')
    sp = sp_map.get(cid)
    sents = len(sp.get('sentences', [])) if sp else 0
    print(f"Row {idx:3d} | {r.get('sourceSection'):22s} | cid: {str(cid):30s} | SP: {'FOUND' if sp else 'MISSING'} ({sents} s) | {r.get('grammarItem')}")

for idx in [334, 335]:
    r = matrix[idx]
    cid = r.get('cardId')
    sp = sp_map.get(cid)
    sents = len(sp.get('sentences', [])) if sp else 0
    print(f"Row {idx:3d} | {r.get('sourceSection'):22s} | cid: {str(cid):30s} | SP: {'FOUND' if sp else 'MISSING'} ({sents} s) | {r.get('grammarItem')}")
