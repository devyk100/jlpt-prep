import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

skm3_rows = [r for r in matrix if r["sourceBook"] == "Shin Kanzen Master N3"]

by_section = {}
for r in skm3_rows:
    by_section.setdefault(r["sourceSection"], []).append(r)

print(f"Total SKM N3 rows: {len(skm3_rows)} across {len(by_section)} sections")
for sec, rows in by_section.items():
    print(f"{sec} ({len(rows)} rows):")
    for r in rows:
        print(f"  [{r['cardId']}] {r['grammarItem']} (pages: {r['exactPrintedPages']} / PDF {r['exactPdfPages']})")
