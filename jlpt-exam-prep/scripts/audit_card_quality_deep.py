import json

pts = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
print(f"Total cards evaluated: {len(pts)}")

short_meaning = []
short_connection = []
missing_nuance = []
cards_with_few_sentences = []
cards_without_notes = []

for p in pts:
    pid = p['id']
    m = p.get('meaning', '')
    c = p.get('connection', '')
    n = p.get('nuance', '')
    s = p.get('sentences', [])
    q = p.get('quiz', [])
    
    if len(m) < 20:
        short_meaning.append((pid, m))
    if len(c) < 5:
        short_connection.append((pid, c))
    if not n and not p.get('keyTakeaway'):
        missing_nuance.append(pid)
    if len(s) < 2:
        cards_with_few_sentences.append((pid, len(s)))
    
    has_any_note = any(bool(sent.get('nuanceNote')) for sent in s)
    if not has_any_note:
        cards_without_notes.append(pid)

print("\n--- FORENSIC DEEP SCAN RESULTS ---")
print(f"Cards with short meaning (<20 chars): {len(short_meaning)}")
for item in short_meaning[:5]:
    print(" ", item)

print(f"Cards with short/empty connection (<5 chars): {len(short_connection)}")
for item in short_connection[:5]:
    print(" ", item)

print(f"Cards missing both nuance and keyTakeaway: {len(missing_nuance)}")
for item in missing_nuance[:5]:
    print(" ", item)

print(f"Cards with fewer than 2 sentences: {len(cards_with_few_sentences)}")
for item in cards_with_few_sentences[:5]:
    print(" ", item)

print(f"Cards where sentences have zero nuanceNotes: {len(cards_without_notes)}")
print("Sample cards without sentence nuanceNotes:", cards_without_notes[:5])

# Distribution of sentence counts
s_counts = [len(p.get('sentences', [])) for p in pts]
print(f"\nSentence counts distribution:")
print(f"  Min: {min(s_counts)}, Max: {max(s_counts)}, Avg: {sum(s_counts)/len(s_counts):.2f}")
print(f"  Cards with 2 sentences: {s_counts.count(2)}")
print(f"  Cards with 3 sentences: {s_counts.count(3)}")
print(f"  Cards with 4 sentences: {s_counts.count(4)}")
print(f"  Cards with 5+ sentences: {sum(1 for c in s_counts if c >= 5)}")
