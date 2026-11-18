import re, json

with open("jlpt-exam-prep/src/data/expandedPoints.ts", encoding="utf-8") as f:
    text = f.read()

added_n2 = re.findall(r'"id":\s*"(added-n2-[^"]+)"', text)
added_n3 = re.findall(r'"id":\s*"(added-n3-[^"]+)"', text)
print(f"added-n2 points in expandedPoints.ts: {len(added_n2)}")
print(f"added-n3 points in expandedPoints.ts: {len(added_n3)}")

with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

print(f"Total points in studyPoints.json: {len(sp)}")
n2_sp = [p for p in sp if p.get("book") == "Shin Kanzen Master N2" or "n2" in p.get("id", "")]
n3_sp = [p for p in sp if p.get("book") == "Shin Kanzen Master N3" or "n3" in p.get("id", "")]
print(f"N2 points in studyPoints.json: {len(n2_sp)}")
print(f"N3 points in studyPoints.json: {len(n3_sp)}")
