import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
exs = json.load(open(ROOT / "src/data/chapterExercises.json", encoding="utf-8"))

n3_chaps = {}
for e in exs:
    if e.get("bookId") == "skm-n3":
        ch = e.get("chapter", "unknown")
        q = e.get("question", "").strip()
        t = e.get("translation", "").strip()
        is_bad_trans = (not t or t == q)
        if ch not in n3_chaps:
            n3_chaps[ch] = {"total": 0, "bad_trans": 0}
        n3_chaps[ch]["total"] += 1
        if is_bad_trans:
            n3_chaps[ch]["bad_trans"] += 1

for ch, d in sorted(n3_chaps.items()):
    if d["bad_trans"] > 0:
        print(f"{ch}: {d['bad_trans']} / {d['total']} bad translations")
