import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

merged_rows = [r for r in rows if 'merged' in r.get('evidence', '').lower() or 'merged' in r.get('cardId', '').lower()]
print(f'Total rows mentioning merged: {len(merged_rows)}')
for i, r in enumerate(merged_rows):
    print(f"{i+1}. [{r['sourceBook']}] {r['sourceSection']} | {r['grammarItem']} | cardId: {r['cardId']}")
    print(f"   Evidence: {r['evidence'][:100]}...")
