import json, re

with open('jlpt-exam-prep/src/data/annotations.json', 'r', encoding='utf-8') as f:
    ann = json.load(f)

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

pattern = re.compile(r'([一-龯々〆ヵヶぁ-んァ-ヶー]+)')

for l_num in range(7, 13):
    ch_name = f"Lesson {l_num}"
    cards = [p for p in sp if p.get('book') == 'Genki I' and p.get('chapter') == ch_name]
    l_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == ch_name]
    
    missing_spans = []
    for c in cards:
        for s in c.get('sentences', []):
            jp = s.get('japanese')
            spans = [span for span in pattern.split(jp) if span.strip() and pattern.match(span)]
            for span in spans:
                if span not in ann:
                    missing_spans.append(span)
    
    for e in l_exs:
        q = e.get('question', '')
        spans = [span for span in pattern.split(q) if span.strip() and pattern.match(span)]
        for span in spans:
            if span not in ann:
                missing_spans.append(span)
        for opt in e.get('options', []):
            spans = [span for span in pattern.split(opt) if span.strip() and pattern.match(span)]
            for span in spans:
                if span not in ann:
                    missing_spans.append(span)
    
    print(f"{ch_name}: {len(cards)} cards, {len(l_exs)} exercises. Missing annotation spans: {len(missing_spans)}")
    if missing_spans:
        print("  Sample missing:", missing_spans[:5])
