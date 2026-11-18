import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

g2_rows = [r for r in rows if r['sourceBook'] == 'Genki II (3rd Ed.)']
print(f"Genki II rows count: {len(g2_rows)}")
missing_work_count = sum(1 for r in g2_rows if r.get('missingWork'))
print(f"Rows with missingWork: {missing_work_count}")
for r in g2_rows[:5]:
    print(f"[{r['sourceSection']}] {r['grammarItem']} (status: {r['status']})")
    print(f"   missingWork: {r.get('missingWork')}")
    print(f"   evidence: {r.get('evidence')[:100]}...")
