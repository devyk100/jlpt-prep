import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

check_cids = [
    'skm2-c14-hanmen', 'skm2-c15-kuse-ni', 'skm2-c15-to-itte-mo', 'skm2-c15-to-shitara',
    'skm2-c16-kara-to-itte', 'skm2-c16-ni-shite-wa', 'skm2-c17-koto-kara', 'skm2-c17-wake-de-wa-nai',
    'added-n2-17-96', 'skm2-c18-mono-dakara', 'skm2-c18-mono-nara', 'skm2-c18-koto-dakara',
    'added-n2-18-98', 'skm2-c19-ue-wa', 'added-n2-19-99', 'added-n2-19-100',
    'skm2-c20-shidai-de-wa', 'added-n2-20-101', 'added-n2-20-102', 'added-n2-21-103'
]

found = {r['cardId']: r for r in rows if r['cardId'] in check_cids}
print(f"Found {len(found)} of {len(check_cids)} IDs in matrix:")
for cid in check_cids:
    r = found.get(cid)
    if not r:
        print(f"NOT FOUND in matrix: {cid}")
    else:
        print(f"[{cid}] status={r['status']} | book={r['sourceBook']} sec={r['sourceSection']}")
        print(f"   item: {r['grammarItem']}")
        print(f"   evidence: {r['evidence'][:120]}...")
