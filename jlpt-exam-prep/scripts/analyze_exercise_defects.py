import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
exercises = json.load(open(ROOT / "src/data/chapterExercises.json", encoding="utf-8"))

by_book_defects = {}

for e in exercises:
    b = e.get("bookId", "unknown")
    ch = e.get("chapter", "unknown")
    if b not in by_book_defects:
        by_book_defects[b] = {"total": 0, "placeholder_trans": 0, "generic_reasons": 0, "chapters": {}}
    
    by_book_defects[b]["total"] += 1
    if ch not in by_book_defects[b]["chapters"]:
        by_book_defects[b]["chapters"][ch] = {"total": 0, "placeholder_trans": 0, "generic_reasons": 0}
    by_book_defects[b]["chapters"][ch]["total"] += 1

    # Check translation
    q = e.get("question", "").strip()
    t = e.get("translation", "").strip()
    has_placeholder_trans = (not t or t == q or any(ord(c) > 0x3000 for c in t if c not in "・〜「」『』… （）()"))
    if has_placeholder_trans:
        by_book_defects[b]["placeholder_trans"] += 1
        by_book_defects[b]["chapters"][ch]["placeholder_trans"] += 1

    # Check generic distractor reasons
    expl = e.get("explanation", {})
    if isinstance(expl, dict):
        opts = expl.get("options", [])
        for opt in opts:
            r = opt.get("reason", "")
            if any(p in r for p in [
                "語用論的制約に反します", "文脈上の時間関係", "文体・語用論", "文脈上の意味論",
                "モダリティ・感情表現の制約に反します", "文の組み立て・構造的呼応に反します",
                "文脈上の文型体系・機能制約に反します", "文体・語用論・結束性において不適切です"
            ]):
                by_book_defects[b]["generic_reasons"] += 1
                by_book_defects[b]["chapters"][ch]["generic_reasons"] += 1

print("=== EXERCISE DEFECT AUDIT ===")
for b, data in by_book_defects.items():
    print(f"\nBook: {b} (Total: {data['total']})")
    print(f"  Placeholder Translations: {data['placeholder_trans']} / {data['total']}")
    print(f"  Generic Distractor Reasons: {data['generic_reasons']}")
