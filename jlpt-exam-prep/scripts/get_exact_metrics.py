import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

with open("jlpt-exam-prep/src/data/bookSources.json", "r", encoding="utf-8") as f:
    books = json.load(f)

print("=== EXACT METRICS PER BOOK ===")
for b in books:
    b_id = b['id']
    b_name = b['name']
    b_pts = [p for p in points if p.get('book') == b_name]
    
    sentences = sum(len(p.get('sentences', [])) for p in b_pts)
    quizzes = sum(len(p.get('quiz', [])) for p in b_pts)
    with_table = sum(1 for p in b_pts if 'table' in p)
    zero_quiz = sum(1 for p in b_pts if len(p.get('quiz', [])) == 0)
    low_ex = sum(1 for p in b_pts if len(p.get('sentences', [])) < 3)
    
    print(f"\n{b_name} ({b['level']}):")
    print(f"  Sections: {len(b['sections'])}")
    print(f"  Cards: {len(b_pts)}")
    print(f"  Total Sentences: {sentences} (avg {sentences/len(b_pts):.1f} per card)")
    print(f"  Total Quizzes: {quizzes} (avg {quizzes/len(b_pts):.1f} per card)")
    print(f"  Cards with ZERO quizzes: {zero_quiz} ({zero_quiz/len(b_pts)*100:.1f}%)")
    print(f"  Cards with <3 examples: {low_ex}")
    print(f"  Cards with embedded tables: {with_table}")

supp_pts = [p for p in points if not p.get('book') or p.get('book') not in [b['name'] for b in books]]
print(f"\nSupplementary / Comparative Cards (Cross-book):")
print(f"  Cards: {len(supp_pts)}")
print(f"  Total Sentences: {sum(len(p.get('sentences', [])) for p in supp_pts)}")
print(f"  Total Quizzes: {sum(len(p.get('quiz', [])) for p in supp_pts)}")
