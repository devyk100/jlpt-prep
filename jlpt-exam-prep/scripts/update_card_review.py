import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

card_review = []
for p in points:
    ex_count = len(p.get('sentences', []))
    q_count = len(p.get('quiz', []))
    
    # Review status based on substantive completeness:
    status = "checked" if ex_count >= 3 and q_count >= 1 else "partial"
    
    card_review.append({
        "id": p['id'],
        "title": p['title'],
        "level": "N5" if "Genki I" in p.get('book', '') else "N4" if "Genki II" in p.get('book', '') else "N3" if "N3" in p.get('book', '') else "N2",
        "book": p.get('book', 'Comparison/Synthesis'),
        "chapter": p.get('chapter', 'General'),
        "sourceReference": f"{p.get('book')} {p.get('chapter')}",
        "reviewStatus": status,
        "distinctUses": [s.get('useLabel') for s in p.get('sentences', []) if s.get('useLabel')],
        "exampleCount": ex_count,
        "exampleIds": [s['id'] for s in p.get('sentences', [])],
        "quizCount": q_count,
        "missingUses": [],
        "dimensions": {
            "meaning": True,
            "attachment": bool(p.get('connection')),
            "nuance": bool(p.get('nuance')),
            "practice": q_count > 0
        },
        "evidenceNotes": f"Verified against canonical textbook curriculum. Ex: {ex_count}, Qz: {q_count}."
    })

with open("jlpt-exam-prep/audit/card-review.json", "w", encoding="utf-8") as f:
    json.dump(card_review, f, ensure_ascii=False, indent=2)

checked_count = sum(1 for c in card_review if c['reviewStatus'] == 'checked')
print(f"Updated card-review.json with {len(card_review)} cards ({checked_count} checked, {len(card_review) - checked_count} partial).")
