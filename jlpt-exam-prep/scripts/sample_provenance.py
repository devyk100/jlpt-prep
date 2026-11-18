import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    exercises = json.load(f)

for e in exercises[::100]:
    print(f"{e['id']} ({e.get('bookId')} - {e.get('chapter')}): prov={e.get('provenance')} | evid={e.get('sourceEvidence')}")
