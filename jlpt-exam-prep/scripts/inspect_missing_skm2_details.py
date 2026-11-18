import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

sp_ids = {p["id"]: p for p in sp}
skm2_matrix_rows = [r for r in matrix if r["sourceBook"] == "Shin Kanzen Master N2"]

print("=== 20 SKM N2 MATRIX ROWS MISSING IN studyPoints.json ===")
for r in skm2_matrix_rows:
    cid = r["cardId"]
    if cid not in sp_ids:
        print(f"[{cid}] Section: {r['sourceSection']} | Pages: {r['exactPrintedPages']} | Item: {r['grammarItem']}")
