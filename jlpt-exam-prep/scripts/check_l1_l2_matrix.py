import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

for r in rows:
    if r.get('sourceBook') == 'Genki I (3rd Ed.)' and r.get('sourceSection') in ['Lesson 1', 'Lesson 2']:
        print(f"[{r['sourceSection']}] {r['grammarItem']} | status: {r['status']}")
        print(f"   missingWork: {r.get('missingWork')}")
        print(f"   evidence: {r.get('evidence')[:100]}...")
