import json, re

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    ex = json.load(f)

stars = [e for e in ex if e.get("type") == "star-mark"]
for s in stars:
    q = s["question"]
    order = s.get("scrambleOrder", [])
    opts = s.get("options", [])
    recon = s["reconstructedSentence"]
    m = re.search(r"＿＿\s*＿＿\s*★\s*＿＿", q)
    prefix = q[:m.start()].strip()
    suffix = q[m.end():].strip()
    assembled = prefix + "".join(opts[p - 1] for p in order) + suffix
    if assembled != recon:
        print(f"[{s['id']}] {assembled}")
