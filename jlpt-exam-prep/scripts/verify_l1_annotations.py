import json, re

with open('jlpt-exam-prep/src/data/annotations.json', 'r', encoding='utf-8') as f:
    ann = json.load(f)

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

pattern = re.compile(r'([一-龯々〆ヵヶぁ-んァ-ヶー]+)')

l1_cards = [p for p in sp if p.get('book') == 'Genki I' and p.get('chapter') == 'Lesson 1']

print("=== CHECKING L1 SENTENCES ===")
missing_sentence_spans = []
for c in l1_cards:
    print(f"\nCard: {c['id']}")
    for s in c.get('sentences', []):
        jp = s.get('japanese')
        spans = [span for span in pattern.split(jp) if span.strip() and pattern.match(span)]
        for span in spans:
            if span in ann:
                print(f"  [OK] {span} -> {len(ann[span])} tokens")
            else:
                print(f"  [MISSING] {span}")
                missing_sentence_spans.append(span)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

l1_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == 'Lesson 1']

print("\n=== CHECKING L1 EXERCISES ===")
missing_ex_spans = []
for e in l1_exs:
    print(f"\nExercise: {e['id']}")
    # check question
    q = e.get('question', '')
    spans = [span for span in pattern.split(q) if span.strip() and pattern.match(span)]
    for span in spans:
        if span in ann:
            print(f"  Q [OK] {span}")
        else:
            print(f"  Q [MISSING] {span}")
            missing_ex_spans.append(span)
    # check options
    for opt in e.get('options', []):
        spans = [span for span in pattern.split(opt) if span.strip() and pattern.match(span)]
        for span in spans:
            if span in ann:
                print(f"  Opt [OK] {span}")
            else:
                print(f"  Opt [MISSING] {span}")
                missing_ex_spans.append(span)

print(f"\nSummary:")
print(f"Missing sentence spans: {len(missing_sentence_spans)}")
print(f"Missing exercise spans: {len(missing_ex_spans)}")
