import json
from collections import defaultdict

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print(f"Total exercises: {len(exercises)}")

patterns = [
    'のため不適切です。本問の文脈に挿入すると、文意や文法的呼応が成立しません。',
    '文脈・文法関係',
    'Incorrect. Ungrammatical.',
    '不適切です。',
    'Incorrect.'
]

pattern_matches = defaultdict(list)
short_distractor_reasons = []
corrupted_correct = []

by_book_chapter = defaultdict(lambda: defaultdict(int))

for ex in exercises:
    eid = ex.get('id')
    book = ex.get('bookId')
    chap = ex.get('chapter')
    exp = ex.get('explanation', {})
    opts = exp.get('options', [])
    for opt in opts:
        is_correct = opt.get('isCorrect', False)
        reason = opt.get('reason', '')
        text = opt.get('text', '')
        
        if is_correct and ('【不正解】' in reason or 'Incorrect' in reason or '不適切' in reason):
            corrupted_correct.append((eid, text, reason))
            
        for p in patterns:
            if p in reason:
                pattern_matches[p].append((eid, book, chap, text, reason))
                by_book_chapter[p][f"{book} - {chap}"] += 1
                
        if not is_correct and len(reason.strip()) < 20:
            short_distractor_reasons.append((eid, book, chap, text, reason))

print("\n--- PATTERN SUMMARY ---")
for p, matches in pattern_matches.items():
    print(f"Pattern '{p}': {len(matches)} occurrences")
    # Show breakdown by book-chapter
    for bc, cnt in sorted(by_book_chapter[p].items()):
        print(f"   {bc}: {cnt}")

print(f"\nCorrupted correct options: {len(corrupted_correct)}")
if corrupted_correct:
    for c in corrupted_correct[:5]:
        print("   ", c)

print(f"\nShort distractor reasons (< 20 chars): {len(short_distractor_reasons)}")
if short_distractor_reasons:
    for s in short_distractor_reasons[:10]:
        print("   ", s)
