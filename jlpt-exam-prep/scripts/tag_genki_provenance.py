import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

G1_PAGES = {
    "Lesson 1": "pp. 38–57",
    "Lesson 2": "pp. 58–83",
    "Lesson 3": "pp. 84–103",
    "Lesson 4": "pp. 104–127",
    "Lesson 5": "pp. 128–147",
    "Lesson 6": "pp. 148–167",
    "Lesson 7": "pp. 168–187",
    "Lesson 8": "pp. 188–209",
    "Lesson 9": "pp. 210–231",
    "Lesson 10": "pp. 232–255",
    "Lesson 11": "pp. 256–277",
    "Lesson 12": "pp. 278–303"
}

G2_PAGES = {
    "Lesson 13": "pp. 26–47",
    "Lesson 14": "pp. 48–69",
    "Lesson 15": "pp. 70–93",
    "Lesson 16": "pp. 94–117",
    "Lesson 17": "pp. 118–141",
    "Lesson 18": "pp. 142–165",
    "Lesson 19": "pp. 166–187",
    "Lesson 20": "pp. 188–209",
    "Lesson 21": "pp. 210–231",
    "Lesson 22": "pp. 232–253",
    "Lesson 23": "pp. 254–277"
}

tagged_g1 = 0
tagged_g2 = 0

for e in exercises:
    b = e.get("bookId")
    ch = e.get("chapter")
    if b == "genki-1" and ch in G1_PAGES:
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = f"Genki I (3rd Ed.), {ch} Grammar & Practice Drills, {G1_PAGES[ch]}"
        tagged_g1 += 1
    elif b == "genki-2" and ch in G2_PAGES:
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = f"Genki II (3rd Ed.), {ch} Grammar & Practice Drills, {G2_PAGES[ch]}"
        tagged_g2 += 1

print(f"Tagged {tagged_g1} Genki I exercises.")
print(f"Tagged {tagged_g2} Genki II exercises.")

with open(EXERCISES_PATH, "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved updated chapterExercises.json successfully.")
