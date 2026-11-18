import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp_list = json.load(f)

with open('jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    br_list = json.load(f)

sp_dict = {p['id']: p for p in sp_list}
br_dict = {p['id']: p for p in br_list}

print(f"Total cards in studyPoints.json: {len(sp_list)}")
print(f"Total cards in base-reviewed.json: {len(br_list)}")

diffs = []
fields_to_check = ['title', 'meaning', 'connection', 'nuance', 'keyTakeaway']

for cid, sp in sp_dict.items():
    if cid not in br_dict:
        diffs.append((cid, 'MISSING_IN_BASE_REVIEWED', None, None))
        continue
    br = br_dict[cid]
    for field in fields_to_check:
        sp_val = sp.get(field, '').strip()
        br_val = br.get(field, '').strip()
        if sp_val != br_val:
            diffs.append((cid, field, sp_val, br_val))

print(f"\nTotal field differences between studyPoints.json and base-reviewed.json: {len(diffs)}")
for d in diffs:
    print(f"Card [{d[0]}] Field '{d[1]}':")
    if d[1] != 'MISSING_IN_BASE_REVIEWED':
        print(f"  studyPoints:   {d[2][:100]}...")
        print(f"  base-reviewed: {d[3][:100]}...")
