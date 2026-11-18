import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp_list = json.load(f)
pts = {p['id']: p for p in sp_list}

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    ex_list = json.load(f)

# The 20 items to audit
items = [
    {
        "source_item": "〜反面",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 14",
        "orig_merge_claim": "skm2-c14-ippou-de",
        "actual_card_id": "skm2-c14-hanmen"
    },
    {
        "source_item": "〜くせに",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 15",
        "orig_merge_claim": "added-n2-14-91",
        "actual_card_id": "skm2-c15-kuse-ni"
    },
    {
        "source_item": "〜といっても",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 15",
        "orig_merge_claim": "added-n2-14-92",
        "actual_card_id": "added-n2-14-92"
    },
    {
        "source_item": "〜としたら",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 15",
        "orig_merge_claim": "added-n2-15-93",
        "actual_card_id": "added-n2-15-93"
    },
    {
        "source_item": "〜からといって",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 16",
        "orig_merge_claim": "added-n2-14-92",
        "actual_card_id": "added-n2-14-92"
    },
    {
        "source_item": "〜にしては",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 16",
        "orig_merge_claim": "added-n2-19-101",
        "actual_card_id": "added-n2-19-101"
    },
    {
        "source_item": "〜ことから",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 17",
        "orig_merge_claim": "added-n2-16-95",
        "actual_card_id": "skm2-c17-koto-kara"
    },
    {
        "source_item": "〜わけではない",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 17",
        "orig_merge_claim": "added-n2-17-98",
        "actual_card_id": "skm2-c17-wake-de-wa-nai"
    },
    {
        "source_item": "〜あまり (Duplicate row added-n2-17-96)",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 17",
        "orig_merge_claim": "added-n2-16-96",
        "actual_card_id": "added-n2-16-96"
    },
    {
        "source_item": "〜ものだから",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 18",
        "orig_merge_claim": "added-n2-16-95",
        "actual_card_id": "added-n2-16-95"
    },
    {
        "source_item": "〜ものなら",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 18",
        "orig_merge_claim": "skm2-c15-mono-nara",
        "actual_card_id": "skm2-c15-mono-nara"
    },
    {
        "source_item": "〜ことだから",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 18",
        "orig_merge_claim": "added-n2-17-97",
        "actual_card_id": "added-n2-17-97"
    },
    {
        "source_item": "〜からには・以上は (Duplicate row added-n2-18-98)",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 18",
        "orig_merge_claim": "added-n2-17-98",
        "actual_card_id": "added-n2-17-98"
    },
    {
        "source_item": "〜上は",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 19",
        "orig_merge_claim": "added-n2-17-98",
        "actual_card_id": "added-n2-17-98"
    },
    {
        "source_item": "〜がたい・〜ようがない・〜得る (Duplicate row added-n2-19-99)",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 19",
        "orig_merge_claim": "added-n2-18-99",
        "actual_card_id": "added-n2-18-99"
    },
    {
        "source_item": "〜わけにはいかない・〜どころではない (Duplicate row added-n2-19-100)",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 19",
        "orig_merge_claim": "added-n2-18-100",
        "actual_card_id": "added-n2-18-100"
    },
    {
        "source_item": "〜次第では",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 20",
        "orig_merge_claim": "skm2-c9-ni-oujite",
        "actual_card_id": "skm2-c20-shidai-de-wa"
    },
    {
        "source_item": "〜わりに・〜にしては (Duplicate row added-n2-20-101)",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 20",
        "orig_merge_claim": "added-n2-19-101",
        "actual_card_id": "added-n2-19-101"
    },
    {
        "source_item": "〜だけのことはある (Duplicate row added-n2-20-102)",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 20",
        "orig_merge_claim": "added-n2-19-102",
        "actual_card_id": "added-n2-19-102"
    },
    {
        "source_item": "〜として・〜にとって・〜にしたら (Duplicate row added-n2-21-103)",
        "book": "Shin Kanzen Master N2",
        "section": "Part 1 · Chapter 21",
        "orig_merge_claim": "added-n2-19-103",
        "actual_card_id": "added-n2-19-103"
    }
]

print(f"Auditing {len(items)} items:\n")
for it in items:
    cid = it["actual_card_id"]
    p = pts.get(cid)
    if not p:
        print(f"FAILED: Card {cid} not found!")
        continue
    
    # Check matching exercises
    exs = [e for e in ex_list if e.get('grammarPointId') == cid or cid in e.get('id', '')]
    
    print(f"=== {it['source_item']} ===")
    print(f"Section: {it['section']} | Claimed Destination: {it['orig_merge_claim']} -> Actual Card: {cid}")
    print(f"Title: {p['title']}")
    print(f"Meaning: {p['meaning']}")
    print(f"Connection: {p['connection']}")
    print(f"Nuance (first 100 chars): {p['nuance'][:100]}...")
    print(f"Example Sentences ({len(p.get('sentences', []))}):")
    for s in p.get('sentences', []):
        print(f"  - [{s['id']}] {s['japanese']} -> {s['english']}")
    print(f"Exercises ({len(exs)}):")
    for e in exs:
        print(f"  - [{e['id']}] {e['question']} (type: {e.get('type')})")
    print()
