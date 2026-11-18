import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
books = json.load(open(ROOT / "src/data/bookSources.json", encoding="utf-8"))
base_cards = {c["id"]: c for c in json.load(open(ROOT / "content/base-reviewed.json", encoding="utf-8"))}
matrix = {m.get("cardId"): m for m in json.load(open(ROOT / "audit/source-coverage-matrix.json", encoding="utf-8"))}
exercises = json.load(open(ROOT / "src/data/chapterExercises.json", encoding="utf-8"))

n2 = [b for b in books if b["id"] == "skm-n2"][0]
print(f"Total N2 sections in bookSources.json: {len(n2['sections'])}")

missing_cards = []
matrix_checked = 0
matrix_missing = 0
all_n2_gids = []

for s in n2['sections']:
    for gid in s['grammarIds']:
        all_n2_gids.append(gid)
        if gid not in base_cards:
            missing_cards.append((s['name'], gid))
        if gid in matrix:
            matrix_checked += 1
        else:
            matrix_missing += 1

print(f"Total grammar IDs referenced across 48 sections: {len(all_n2_gids)}")
print(f"Unique grammar IDs: {len(set(all_n2_gids))}")
print(f"Missing cards in base-reviewed: {len(missing_cards)}")
print(f"Cards present in source-coverage-matrix: {matrix_checked}")
print(f"Cards missing from source-coverage-matrix: {matrix_missing}")

# Check exercises for skm-n2
n2_exercises = [e for e in exercises if e.get("bookId") == "skm-n2"]
print(f"Total existing exercises for skm-n2: {len(n2_exercises)}")
if n2_exercises:
    by_chap = {}
    for e in n2_exercises:
        ch = e.get("chapter", "unknown")
        by_chap[ch] = by_chap.get(ch, 0) + 1
    print(f"Existing exercises by chapter ({len(by_chap)} chapters covered):")
    for ch, count in sorted(by_chap.items()):
        print(f"  {ch}: {count} questions")
