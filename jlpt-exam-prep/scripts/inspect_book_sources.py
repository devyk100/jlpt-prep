import json

with open("jlpt-exam-prep/src/data/bookSources.json", "r", encoding="utf-8") as f:
    books = json.load(f)

for b in books:
    print(f"==================================================")
    print(f"Book: {b['name']} ({b['level']}) - Total sections: {len(b['sections'])}")
    total_ids = sum(len(s['grammarIds']) for s in b['sections'])
    print(f"Total grammar IDs mapped: {total_ids}")
    for s in b['sections']:
        print(f"  Section: {s['name']} -> {len(s['grammarIds'])} items: {s['grammarIds']}")
