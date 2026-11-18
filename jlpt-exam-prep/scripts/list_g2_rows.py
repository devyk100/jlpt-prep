import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

g2_rows = [r for r in matrix if r["sourceBook"] == "Genki II (3rd Ed.)"]
print(f"Genki II rows: {len(g2_rows)}")
for r in g2_rows:
    print(f"{r['sourceSection']} | {r['cardId']} | {r['grammarItem']} | {r['exactPrintedPages']} (PDF {r['exactPdfPages']})")
