import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

sp_ids = {p["id"]: p for p in sp}
skm3_matrix_rows = [r for r in matrix if r["sourceBook"] == "Shin Kanzen Master N3"]

missing_in_sp = [r for r in skm3_matrix_rows if r["cardId"] not in sp_ids]
print(f"SKM N3 total rows: {len(skm3_matrix_rows)} | Missing in studyPoints: {len(missing_in_sp)}")
