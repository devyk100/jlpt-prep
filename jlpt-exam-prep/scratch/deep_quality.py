"""Deeper content quality checks for honest assessment."""
import json

ROOT = r"C:\JLPT\jlpt-exam-prep"
sp = json.load(open(f"{ROOT}/src/data/studyPoints.json", "r", encoding="utf-8"))
ex = json.load(open(f"{ROOT}/src/data/chapterExercises.json", "r", encoding="utf-8"))

# 1. Check exercise answer uniqueness - does only one option really work?
# Sample a few and manually verify logic
print("=== SAMPLE ANSWER UNIQUENESS CHECK ===")
# Specifically check some tricky N2 exercises
tricky_ids = [
    "skm2-p1-c24-q11",  # the repaired one  
    "skm2-p1-c24-q12",  # the repaired one
    "skm3-c2-ex-7",     # the repaired double-particle
    "skm2-p1-c10-q7",   # random N2
]
ex_map = {e["id"]: e for e in ex}
for eid in tricky_ids:
    e = ex_map.get(eid)
    if not e:
        print(f"  {eid}: NOT FOUND")
        continue
    q = e["question"]
    opts = e["options"]
    ci = e["correctIndex"]
    print(f"\n  {eid}")
    print(f"  Q: {q}")
    for i, opt in enumerate(opts):
        marker = "✓" if i == ci else "✗"
        # Reconstruct
        import re
        m = re.search(r"（[^）]*）", q)
        if m:
            reconstructed = q[:m.start()] + opt + q[m.end():]
            print(f"  [{marker}] {opt} → {reconstructed[:80]}")
        else:
            print(f"  [{marker}] {opt}")

# 2. Check for any exercises where translation is suspiciously similar to question
print("\n\n=== TRANSLATION VS QUESTION ALIGNMENT CHECK ===")
# In Genki exercises, check if the translation matches the context
g1_ex = [e for e in ex if e["bookId"] == "genki-1"]
missing_context = sum(1 for e in g1_ex if not e.get("context", "").strip())
missing_trans = sum(1 for e in g1_ex if not e.get("translation", "").strip())
print(f"Genki I exercises without context: {missing_context}/{len(g1_ex)}")
print(f"Genki I exercises without translation: {missing_trans}/{len(g1_ex)}")

# 3. Check card-to-exercise linkage
print("\n\n=== CARD-TO-EXERCISE COVERAGE ===")
# Which cards have exercises?
card_ids = set(c["id"] for c in sp)
exercised_cards = set(e.get("grammarPointId", "") for e in ex)
exercised_cards.discard("")

covered = card_ids & exercised_cards
uncovered = card_ids - exercised_cards
print(f"Cards with at least 1 exercise: {len(covered)}/{len(card_ids)}")
print(f"Cards without any exercise: {len(uncovered)}")
if uncovered:
    # Group by book
    uncov_by_book = {}
    for c in sp:
        if c["id"] in uncovered:
            b = c.get("book", "?")
            uncov_by_book.setdefault(b, []).append(c["id"])
    for b, ids in sorted(uncov_by_book.items()):
        print(f"  {b}: {len(ids)} uncovered cards")
        for eid in ids[:3]:
            print(f"    {eid}")
        if len(ids) > 3:
            print(f"    ... and {len(ids)-3} more")

# 4. How many chapters have < 6 exercises?
print("\n\n=== CHAPTER EXERCISE COUNTS ===")
from collections import Counter
chap_counts = Counter((e["bookId"], e["chapter"]) for e in ex)
thin_chapters = [(k, v) for k, v in chap_counts.items() if v < 6]
print(f"Chapters with <6 exercises: {len(thin_chapters)}")
for (bid, ch), n in sorted(thin_chapters):
    print(f"  {bid} / {ch}: {n}")

# 5. Check for duplicate questions
q_texts = Counter(e["question"] for e in ex)
dupes = [(q, n) for q, n in q_texts.items() if n > 1]
print(f"\n=== DUPLICATE QUESTIONS: {len(dupes)} ===")
for q, n in dupes[:5]:
    print(f"  ({n}x) {q[:80]}")
