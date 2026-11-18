import json

with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

with open("jlpt-exam-prep/content/base-reviewed.json", encoding="utf-8") as f:
    br = json.load(f)

br_ids = {c["id"] for c in br}
new_cards = []
for p in sp:
    if p["id"] not in br_ids:
        # Construct base-reviewed entry
        entry = {
            "id": p["id"],
            "title": p["title"],
            "level": p.get("level", "N2"),
            "book": p.get("book", "Shin Kanzen Master N2"),
            "chapter": p.get("chapter", ""),
            "meaning": p.get("meaning", ""),
            "connection": p.get("connection", ""),
            "nuance": p.get("nuance", ""),
            "keyTakeaway": p.get("keyTakeaway", ""),
            "sentences": [
                {
                    "id": f"{p['id']}::{s['id']}",
                    "japanese": s["japanese"],
                    "english": s["english"],
                    "literal": s.get("literal", ""),
                    "tokens": s.get("tokens", [])
                }
                for s in p.get("sentences", [])
            ],
            "examples": []
        }
        br.append(entry)
        new_cards.append(p["id"])

with open("jlpt-exam-prep/content/base-reviewed.json", "w", encoding="utf-8") as f:
    json.dump(br, f, ensure_ascii=False, indent=2)

print(f"Synced base-reviewed.json. Added {len(new_cards)} cards: {new_cards}")
