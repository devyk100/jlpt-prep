import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

for b in ["Genki II (3rd Ed.)", "Shin Kanzen Master N3", "Shin Kanzen Master N2"]:
    rows = [r for r in matrix if r["sourceBook"] == b]
    print(f"=== Sample reopened row from {b} ({len(rows)} rows) ===")
    r = rows[0]
    print("Item:", r["grammarItem"])
    print("Pages:", r["exactPrintedPages"], "| PDF:", r["exactPdfPages"])
    print("Card:", r["cardId"])
    print("Status:", r["status"])
    print("Evidence:", r["evidence"])
