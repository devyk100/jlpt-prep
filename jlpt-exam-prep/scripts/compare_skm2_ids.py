import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

sp_ids = {p["id"]: p for p in sp}
skm2_matrix_rows = [r for r in matrix if r["sourceBook"] == "Shin Kanzen Master N2"]

missing_in_sp = []
present_in_sp = []
for r in skm2_matrix_rows:
    cid = r["cardId"]
    if cid in sp_ids:
        present_in_sp.append(r)
    else:
        missing_in_sp.append(r)

print(f"Total SKM N2 matrix rows: {len(skm2_matrix_rows)}")
print(f"Present in studyPoints: {len(present_in_sp)}")
print(f"Missing in studyPoints: {len(missing_in_sp)}")
for r in missing_in_sp[:10]:
    print("  Missing cardId:", r["cardId"], "| Item:", r["grammarItem"], "| Sec:", r["sourceSection"])
