import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

skm2_rows = [r for r in matrix if r["sourceBook"] == "Shin Kanzen Master N2"]

by_section = {}
for r in skm2_rows:
    by_section.setdefault(r["sourceSection"], []).append(r)

print(f"Total SKM N2 rows: {len(skm2_rows)} across {len(by_section)} sections")
for sec, rows in list(by_section.items())[:15]:
    print(f"{sec} ({len(rows)} rows):")
    for r in rows:
        print(f"  [{r['cardId']}] {r['grammarItem']} (pages: {r['exactPrintedPages']} / PDF {r['exactPdfPages']})")
