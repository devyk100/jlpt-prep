import json
from collections import Counter

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

n3_rows = [r for r in data if r.get('sourceBook') == 'Shin Kanzen Master N3']
print(f"Total N3 rows: {len(n3_rows)}")
by_sec = Counter(r['sourceSection'] for r in n3_rows)
for sec, cnt in sorted(by_sec.items()):
    print(f"  {sec}: {cnt} rows")
