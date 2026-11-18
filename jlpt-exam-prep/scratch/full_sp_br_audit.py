import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp_list = json.load(f)

with open('jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    br_list = json.load(f)

sp_dict = {p['id']: p for p in sp_list}
br_dict = {p['id']: p for p in br_list}

fields = ['title', 'meaning', 'connection', 'nuance', 'keyTakeaway']

for cid, sp in sp_dict.items():
    if cid not in br_dict:
        print(f"Card {cid} exists in studyPoints but missing in base-reviewed!")
        continue
    br = br_dict[cid]
    for field in fields:
        if sp.get(field, '').strip() != br.get(field, '').strip():
            print(f"DIFF [{cid}] {field}:")
            print(f"   SP: {sp.get(field)}")
            print(f"   BR: {br.get(field)}")

for cid in br_dict:
    if cid not in sp_dict:
        print(f"Card {cid} in base-reviewed but not in studyPoints!")
