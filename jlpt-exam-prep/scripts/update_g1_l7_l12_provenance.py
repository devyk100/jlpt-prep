import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

updated_count = 0
for e in exs:
    if e.get('bookId') == 'genki-1' and e.get('chapter') in [f"Lesson {i}" for i in range(7, 13)]:
        e['provenance'] = 'original'
        ch = e.get('chapter')
        e['sourceEvidence'] = f"Original diagnostic exercise authored to test specified learning objectives of Genki I {ch}."
        updated_count += 1

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exs, f, ensure_ascii=False, indent=2)

print(f"Updated {updated_count} exercises in chapterExercises.json for Lessons 7-12 to honest 'original' provenance!")
