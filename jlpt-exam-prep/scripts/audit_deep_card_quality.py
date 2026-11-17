import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

with open("jlpt-exam-prep/src/data/bookSources.json", "r", encoding="utf-8") as f:
    books = json.load(f)

print("=== DETAILED CARD AUDIT ACROSS ALL 4 TEXTBOOKS ===")

# 1. Cards with low example counts (< 3)
low_examples = [p for p in points if len(p['sentences']) < 3]
print(f"\n1. Cards with fewer than 3 examples: {len(low_examples)}")
for p in low_examples[:10]:
    print(f"   [{p['id']}] {p['title']} ({p.get('book')} {p.get('chapter')}) -> {len(p['sentences'])} examples")

# 2. Cards with 0 quizzes
no_quiz = [p for p in points if len(p['quiz']) == 0]
print(f"\n2. Cards with ZERO quiz questions: {len(no_quiz)} / {len(points)}")
by_book_no_quiz = {}
for p in no_quiz:
    b = p.get('book', 'Comparison/Other')
    by_book_no_quiz[b] = by_book_no_quiz.get(b, 0) + 1
print(f"   Breakdown of 0-quiz cards by book: {by_book_no_quiz}")

# 3. Lumped / multi-pattern cards
lumped = []
for p in points:
    # check for multiple patterns in title
    title = p['title']
    if any(sep in title for sep in ['・', ' vs ', ' / ', '〜と〜', '〜ば〜']):
        lumped.append(p)
print(f"\n3. Potentially lumped multi-pattern cards: {len(lumped)}")
for p in lumped[:10]:
    print(f"   [{p['id']}] {p['title']} (sentences: {len(p['sentences'])})")

# 4. Check attachment rules (connection field) completeness
weak_connection = [p for p in points if len(p.get('connection', '')) < 15 or '待つ' in p.get('connection', '')]
print(f"\n4. Cards with very brief or missing connection rules: {len(weak_connection)}")
for p in weak_connection[:5]:
    print(f"   [{p['id']}] {p['title']}: '{p.get('connection')}'")

# 5. Check nuance field completeness
weak_nuance = [p for p in points if len(p.get('nuance', '')) < 30]
print(f"\n5. Cards with very brief or missing nuance/restrictions: {len(weak_nuance)}")
for p in weak_nuance[:5]:
    print(f"   [{p['id']}] {p['title']}: '{p.get('nuance')}'")
