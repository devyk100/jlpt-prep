import json, glob, os, re

pts = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
books = json.load(open('jlpt-exam-prep/src/data/bookSources.json', encoding='utf-8'))
pts_by_id = {p['id']: p for p in pts}

source_dir = 'jlpt-exam-prep/audit/source-text'

print("=== INSIDE-OUT AUDIT REPORT ===")

# Check Genki I
print("\n" + "=" * 60)
print("1. GENKI I AUDIT")
print("=" * 60)
g1_files = sorted(glob.glob(os.path.join(source_dir, 'g1-p*.txt')))
g1_cards = [p for p in pts if p.get('book') == 'Genki I']
print(f"Genki I Page files in repo: {len(g1_files)}")
print(f"Genki I Cards in app: {len(g1_cards)}")

# Check chapter by chapter in Genki I
for lesson_num in range(1, 13):
    lesson_str = f"Lesson {lesson_num}"
    cards_in_lesson = [p for p in g1_cards if p.get('chapter') == lesson_str]
    titles = [p['title'].split(' (')[0] for p in cards_in_lesson]
    print(f"\n  [Genki I {lesson_str}] ({len(cards_in_lesson)} cards):")
    for c in cards_in_lesson:
        has_table = bool(c.get('table'))
        s_cnt = len(c.get('sentences', []))
        q_cnt = len(c.get('quiz', []))
        print(f"    - {c['id']}: {c['title']} | {s_cnt} ex, {q_cnt} qz {'[TABLE]' if has_table else ''}")

# Check Genki II
print("\n" + "=" * 60)
print("2. GENKI II AUDIT")
print("=" * 60)
g2_files = sorted(glob.glob(os.path.join(source_dir, 'g2-p*.txt')))
g2_cards = [p for p in pts if p.get('book') == 'Genki II']
print(f"Genki II Page files in repo: {len(g2_files)}")
print(f"Genki II Cards in app: {len(g2_cards)}")

for lesson_num in range(13, 24):
    lesson_str = f"Lesson {lesson_num}"
    cards_in_lesson = [p for p in g2_cards if p.get('chapter') == lesson_str]
    print(f"\n  [Genki II {lesson_str}] ({len(cards_in_lesson)} cards):")
    for c in cards_in_lesson:
        has_table = bool(c.get('table'))
        s_cnt = len(c.get('sentences', []))
        q_cnt = len(c.get('quiz', []))
        print(f"    - {c['id']}: {c['title']} | {s_cnt} ex, {q_cnt} qz {'[TABLE]' if has_table else ''}")

# Check SKM N3
print("\n" + "=" * 60)
print("3. SHIN KANZEN MASTER N3 AUDIT")
print("=" * 60)
n3_cards = [p for p in pts if p.get('book') == 'Shin Kanzen Master N3']
print(f"SKM N3 Cards in app: {len(n3_cards)}")
n3_chapters = {}
for p in n3_cards:
    ch = p.get('chapter', 'Unknown')
    n3_chapters.setdefault(ch, []).append(p)
for ch, clist in sorted(n3_chapters.items()):
    print(f"  {ch} ({len(clist)} cards): {[c['id'] for c in clist]}")

# Check SKM N2
print("\n" + "=" * 60)
print("4. SHIN KANZEN MASTER N2 AUDIT")
print("=" * 60)
n2_cards = [p for p in pts if p.get('book') == 'Shin Kanzen Master N2']
print(f"SKM N2 Cards in app: {len(n2_cards)}")
n2_chapters = {}
for p in n2_cards:
    ch = p.get('chapter', 'Unknown')
    n2_chapters.setdefault(ch, []).append(p)
for ch, clist in sorted(n2_chapters.items()):
    print(f"  {ch} ({len(clist)} cards): {[c['id'] for c in clist]}")
