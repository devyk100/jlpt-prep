import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    exercises = json.load(f)

skm2_p2 = [e for e in exercises if e["id"].startswith("skm2-p2")]
print(f"Total skm2-p2 exercises in database: {len(skm2_p2)}")

for e in skm2_p2:
    print(f"{e['id']}: {e['question']}")
    print(f"   opts: {e['options']}")
    print(f"   recon: {e.get('reconstructedSentence')}")
