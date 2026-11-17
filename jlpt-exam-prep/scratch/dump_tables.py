import sys
sys.path.append('jlpt-exam-prep')
import json

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'r', encoding='utf-8') as f:
    tables = json.load(f)

for tid, t in tables.items():
    print(f'================ {tid} ================')
    print('Title:', t.get('title'))
    print('Columns:', t.get('columns'))
    for r in t.get('rows', []):
        print(f"  Row label: {r.get('label')}")
        print(f"  Row cells: {r.get('cells')}")
        if r.get('note'):
            print(f"  Row note: {r.get('note')}")
