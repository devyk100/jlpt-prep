import json

data = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
for idx in range(240, len(data)):
    r = data[idx]
    sec = r.get("sourceSection")
    item = r.get("grammarItem")
    cid = r.get("cardId")
    st = r.get("status")
    print(f"{idx}: {sec} | {item} | cardId: {cid} | status: {st}")
