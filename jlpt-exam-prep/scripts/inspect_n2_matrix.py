import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

n2_rows = [r for r in rows if r['sourceBook'] == 'Shin Kanzen Master N2']
print(f"Total N2 rows: {len(n2_rows)}")

sections = {}
for r in n2_rows:
    sec = r['sourceSection']
    if sec not in sections:
        sections[sec] = []
    sections[sec].append(r)

for sec, r_list in sections.items():
    print(f"=== {sec} ({len(r_list)} items) ===")
    for r in r_list:
        print(f"  [{r['cardId']}] {r['grammarItem']} (pages: {r['exactPrintedPages']} / {r['exactPdfPages']}) status={r['status']}")
        if r.get('missingWork'):
            print(f"    missingWork: {r['missingWork'][:60]}...")
