import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

card_ids = [
    "skm2-c20-shidai-de-wa",
    "skm2-c15-kuse-ni",
    "skm2-c17-koto-kara",
    "skm2-c17-wake-de-wa-nai",
    "skm2-c14-hanmen"
]

target_cards = [p for p in points if p["id"] in card_ids]
for c in target_cards:
    print("=" * 70)
    print(f"ID: {c['id']}")
    print(f"Title: {c['title']}")
    print(f"Meaning: {c['meaning']}")
    print(f"Connection: {c.get('connection')}")
    print(f"Nuance: {c.get('nuance')}")
    print(f"Key Takeaway: {c.get('keyTakeaway')}")
    print("Sentences:")
    for s in c.get("sentences", []):
        print(f"  JA: {s.get('japanese')}")
        print(f"  EN: {s.get('english')}")
        print(f"  Breakdown: {s.get('literalBreakdown')}")
