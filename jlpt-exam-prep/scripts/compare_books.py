import json

with open(r"c:\JLPT\jlpt-exam-prep\src\data\bookSources.json", "r", encoding="utf-8") as f:
    books = json.load(f)

with open(r"c:\JLPT\jlpt-exam-prep\src\data\studyPoints.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

card_ids = set(c["id"] for c in cards)

for b in books:
    print(f"\n==========================================")
    print(f"BOOK: {b['name']} ({b['id']}) - Level {b['level']}")
    sections = b.get("sections", [])
    print(f"Total Sections: {len(sections)}")
    total_gids = sum(len(s.get("grammarIds", [])) for s in sections)
    print(f"Total Grammar Card References: {total_gids}")
    
    missing = []
    for s in sections:
        for gid in s.get("grammarIds", []):
            if gid not in card_ids:
                missing.append((s["name"], gid))
    if missing:
        print(f"  WARNING: {len(missing)} missing card IDs: {missing[:5]}")
    else:
        print(f"  All {total_gids} card IDs exist in studyPoints.json!")

    for s in sections:
        gids = s.get("grammarIds", [])
        print(f"  {s['name']}: {len(gids)} points -> {gids}")
