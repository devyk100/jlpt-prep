import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

l1_cards = [p for p in sp if p.get('book') == 'Genki I' and p.get('chapter') == 'Lesson 1']

for c in l1_cards:
    print("=" * 60)
    print(f"ID: {c['id']}")
    print(f"Title: {c['title']}")
    print(f"Meaning: {c['meaning']}")
    print(f"Connection: {c.get('connection')}")
    print(f"Nuance: {c.get('nuance')}")
    print(f"Key Takeaway: {c.get('keyTakeaway')}")
    print(f"Table: {c.get('table', {}).get('title') if c.get('table') else 'None'}")
    print(f"Sentences ({len(c.get('sentences', []))}):")
    for s in c.get('sentences', []):
        print(f"  - [{s.get('id')}] {s.get('japanese')}")
        print(f"    EN: {s.get('english')}")
        print(f"    Lit: {s.get('literal')}")
        print(f"    Tokens count: {len(s.get('tokens', []))}")
    print(f"Quiz ({len(c.get('quiz', []))}):")
    for q in c.get('quiz', []):
        print(f"  - [{q.get('id')}] Q: {q.get('question')} | Ans: {q.get('options')[q.get('correctIndex')]}")
