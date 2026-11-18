import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

g1_rows = [r for r in matrix if r["sourceBook"] == "Genki I (3rd Ed.)"]
print(f"Total Genki I rows: {len(g1_rows)}")
for r in g1_rows[:5]:
    print("---")
    print("Item:", r["grammarItem"])
    print("Pages:", r["exactPrintedPages"], "| PDF:", r["exactPdfPages"])
    print("Card:", r["cardId"])
    print("Example IDs:", r["exampleIds"])
    print("Evidence:", r["evidence"])
