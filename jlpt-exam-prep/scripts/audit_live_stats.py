import json

pts = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
bks = json.load(open('jlpt-exam-prep/src/data/bookSources.json', encoding='utf-8'))
ann = json.load(open('jlpt-exam-prep/src/data/annotations.json', encoding='utf-8'))

print("TOTAL CARDS:", len(pts))
print("TOTAL ANNOTATION SPANS:", len(ann))

book_stats = {}
for p in pts:
    b = p.get('book', 'Unknown')
    if b not in book_stats:
        book_stats[b] = {
            'count': 0,
            'sentences': 0,
            'quizzes': 0,
            'tables': 0,
            'zero_quiz': 0,
            'zero_sentences': 0,
            'levels': set()
        }
    book_stats[b]['count'] += 1
    s_cnt = len(p.get('sentences', []))
    q_cnt = len(p.get('quiz', []))
    book_stats[b]['sentences'] += s_cnt
    book_stats[b]['quizzes'] += q_cnt
    if 'table' in p and p['table']:
        book_stats[b]['tables'] += 1
    if q_cnt == 0:
        book_stats[b]['zero_quiz'] += 1
    if s_cnt == 0:
        book_stats[b]['zero_sentences'] += 1
    book_stats[b]['levels'].add(p.get('level', ''))

for b, st in sorted(book_stats.items()):
    print(f"\n=== {b} ===")
    print(f"  Cards: {st['count']}")
    print(f"  Sentences: {st['sentences']} (avg {st['sentences']/st['count']:.2f}/card)")
    print(f"  Quizzes: {st['quizzes']} (avg {st['quizzes']/st['count']:.2f}/card)")
    print(f"  In-lesson Tables: {st['tables']}")
    print(f"  Zero quiz cards: {st['zero_quiz']}")
    print(f"  Zero sentence cards: {st['zero_sentences']}")
    print(f"  Levels: {st['levels']}")

print("\n=== OVERALL TOTALS ===")
total_cards = len(pts)
total_s = sum(len(p.get('sentences', [])) for p in pts)
total_q = sum(len(p.get('quiz', [])) for p in pts)
total_t = sum(1 for p in pts if 'table' in p and p['table'])
print(f"Total Cards: {total_cards}")
print(f"Total Sentences: {total_s} (avg {total_s/total_cards:.2f}/card)")
print(f"Total Quizzes: {total_q} (avg {total_q/total_cards:.2f}/card)")
print(f"Total In-lesson Tables: {total_t}")
