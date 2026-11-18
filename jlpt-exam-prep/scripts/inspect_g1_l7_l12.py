import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

for l_num in range(7, 13):
    ch_name = f"Lesson {l_num}"
    cards = [p for p in sp if p.get('book') == 'Genki I' and p.get('chapter') == ch_name]
    ch_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == ch_name]
    print(f"=== {ch_name} ({len(cards)} cards, {len(ch_exs)} exercises) ===")
    for c in cards:
        tbl = c.get('table', {}).get('title') if c.get('table') else 'None'
        print(f"  [{c['id']}] {c['title']} ({len(c.get('sentences', []))} sentences, table: {tbl})")
    print(f"  First exercise: [{ch_exs[0]['id']}] {ch_exs[0]['question']} | Ans: {ch_exs[0]['options'][ch_exs[0]['correctIndex']]}")
    print()
