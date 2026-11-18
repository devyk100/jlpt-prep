import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

skm3_rows = [r for r in matrix if r["sourceBook"] == "Shin Kanzen Master N3"]
skm2_rows = [r for r in matrix if r["sourceBook"] == "Shin Kanzen Master N2"]

print(f"SKM N3 rows: {len(skm3_rows)}")
print(f"SKM N2 rows: {len(skm2_rows)}")

# Print all sections in SKM N3
skm3_sections = {}
for r in skm3_rows:
    sec = r["sourceSection"]
    skm3_sections.setdefault(sec, []).append(r)

print(f"\nSKM N3 has {len(skm3_sections)} sections:")
for sec, rows in list(skm3_sections.items())[:10]:
    print(f"  Section: {sec} ({len(rows)} items)")
    for r in rows:
        print(f"    - Card: {r['cardId']} | Item: {r['grammarItem']} | p. {r['exactPrintedPages']}")
