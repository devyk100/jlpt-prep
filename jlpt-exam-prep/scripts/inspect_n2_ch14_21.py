import json

with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

for p in sp:
    b = p.get("book", "")
    ch = p.get("chapter", "")
    cid = p.get("id", "")
    if "N2" in b or "n2" in cid:
        for cnum in range(14, 22):
            if f"Chapter {cnum}:" in ch or f"c{cnum}" in cid or f"-{cnum}-" in cid:
                print(f"[{cid}] {ch} -> {p.get('title')}")
