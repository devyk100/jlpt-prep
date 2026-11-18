import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
matrix = json.load(open(ROOT / "audit/source-coverage-matrix.json", encoding="utf-8"))
exercises = json.load(open(ROOT / "src/data/chapterExercises.json", encoding="utf-8"))
books = json.load(open(ROOT / "src/data/bookSources.json", encoding="utf-8"))
base_cards = json.load(open(ROOT / "content/base-reviewed.json", encoding="utf-8"))

print("=================================================================")
print("             DIGITAL CURRICULUM FINAL AUDIT REPORT               ")
print("=================================================================")
print(f"Total Base Cards in Knowledge Base: {len(base_cards)}")
print(f"Total Certified Source Coverage Matrix Rows: {len(matrix)}")
by_book_m = {}
for m in matrix:
    b = m.get("sourceBook", "Unknown")
    by_book_m[b] = by_book_m.get(b, 0) + 1
for b, c in sorted(by_book_m.items()):
    print(f"  * {b}: {c} certified rows")

print(f"\nTotal Authentic Chapter Exercises: {len(exercises)}")
by_book_e = {}
for e in exercises:
    b = e.get("bookId", "Unknown")
    by_book_e[b] = by_book_e.get(b, 0) + 1
for b, c in sorted(by_book_e.items()):
    print(f"  * {b}: {c} questions")

print("\nCurriculum Completeness by Book:")
for b in books:
    b_id = b["id"]
    n_secs = len(b["sections"])
    b_exs = by_book_e.get(b_id, 0)
    print(f"  * {b['name']} (Level {b['level']}, ID: {b_id}): {n_secs} sections, {b_exs} exercises (Avg {b_exs//n_secs if n_secs else 0}/sec)")

print("=================================================================")
