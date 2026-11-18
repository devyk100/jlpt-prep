import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

n3_rows = [r for r in rows if r['sourceBook'] == 'Shin Kanzen Master N3']
print(f"Total N3 rows: {len(n3_rows)}")

# Group by sourceSection
sections = {}
for r in n3_rows:
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
