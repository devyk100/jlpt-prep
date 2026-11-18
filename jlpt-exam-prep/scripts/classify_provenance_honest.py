import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    exercises = json.load(f)

counts = {"source-derived": 0, "adapted": 0, "original": 0}

for ex in exercises:
    b = ex.get("bookId")
    ch = ex.get("chapter", "")

    if b in ["genki-1", "genki-2"]:
        # Genki I & II drills directly transcribed from textbook practice exercises
        ex["provenance"] = "source-derived"
    elif b == "skm-n3":
        if "Part 2" in ch:
            ex["provenance"] = "adapted"
            ex["sourceEvidence"] = f"Adapted for digital star-mark practice from Shin Kanzen Master N3 Bunpou, Part 2 ({ch.split(' · ')[-1]}), pp. 104–115"
        elif "Part 3" in ch:
            ex["provenance"] = "adapted"
            ex["sourceEvidence"] = f"Adapted for sentence-level discourse practice from Shin Kanzen Master N3 Bunpou, Part 3 ({ch.split(' · ')[-1]}), pp. 116–140"
        else:
            ex["provenance"] = "source-derived"
    elif b == "skm-n2":
        if "Part 2" in ch:
            ex["provenance"] = "adapted"
            ex["sourceEvidence"] = f"Adapted for digital star-mark practice from Shin Kanzen Master N2 Bunpou, Part 2 ({ch.split(' · ')[-1]}), pp. 140–153"
        elif "Part 3" in ch:
            ex["provenance"] = "adapted"
            ex["sourceEvidence"] = f"Adapted for sentence-level discourse practice from Shin Kanzen Master N2 Bunpou, Part 3 ({ch.split(' · ')[-1]}), pp. 154–199"
        else:
            ex["provenance"] = "source-derived"

    counts[ex["provenance"]] += 1

with open("jlpt-exam-prep/src/data/chapterExercises.json", "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Updated provenance classifications:")
print(counts)
