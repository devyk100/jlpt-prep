import json, os

with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    study_points = json.load(f)

# The 20 items and the specific grammar terms they represent
TARGETS = [
    ("skm2-c14-hanmen", "反面", "Ch 14"),
    ("skm2-c15-kuse-ni", "くせに", "Ch 15"),
    ("skm2-c15-to-itte-mo", "といっても", "Ch 15"),
    ("skm2-c15-to-shitara", "としたら", "Ch 15"),
    ("skm2-c16-kara-to-itte", "からといって", "Ch 16"),
    ("skm2-c16-ni-shite-wa", "にしては", "Ch 16"),
    ("skm2-c17-koto-kara", "ことから", "Ch 17"),
    ("skm2-c17-wake-de-wa-nai", "わけではない", "Ch 17"),
    ("added-n2-17-96", "おかげ", "Ch 17"),
    ("skm2-c18-mono-dakara", "ものだから", "Ch 18"),
    ("skm2-c18-mono-nara", "ものなら", "Ch 18"),
    ("skm2-c18-koto-dakara", "ことだから", "Ch 18"),
    ("added-n2-18-98", "ばかりに", "Ch 18"),
    ("skm2-c19-ue-wa", "上は", "Ch 19"),
    ("added-n2-19-99", "がたい", "Ch 19"),
    ("added-n2-19-100", "わけにはいかない", "Ch 19"),
    ("skm2-c20-shidai-de-wa", "次第では", "Ch 20"),
    ("added-n2-20-101", "わりに", "Ch 20"),
    ("added-n2-20-102", "だけのことはある", "Ch 20"),
    ("added-n2-21-103", "にしたら", "Ch 21"),
]

print("=== CHECKING ALL 20 TARGETS AGAINST LIVE studyPoints.json ===")

for cid, term, ch in TARGETS:
    # 1. Direct card match
    direct = [p for p in study_points if p.get("id") == cid]
    
    # 2. Cards whose title or meaning or connection or sentences contain the term
    matching_cards = []
    for p in study_points:
        p_id = p.get("id", "")
        title = p.get("title", "")
        conn = p.get("connection", "")
        nuance = p.get("nuance", "")
        meaning = p.get("meaning", "")
        sentences = [s.get("japanese", "") for s in p.get("sentences", [])]
        
        # Check if term appears in title, connection, or sentences
        if term in title or term in conn or any(term in s for s in sentences):
            matching_cards.append({
                "id": p_id,
                "title": title,
                "book": p.get("book", ""),
                "in_title": term in title,
                "in_conn": term in conn,
                "in_sentences": any(term in s for s in sentences)
            })
            
    print(f"\nTarget: [{cid}] '{term}' ({ch}):")
    print(f"  Direct card ID match: {len(direct)} ({direct[0]['title'] if direct else 'NONE'})")
    print(f"  Substantive matches in studyPoints: {len(matching_cards)}")
    for mc in matching_cards:
        print(f"    -> [{mc['id']}] ({mc['book']}) {mc['title']} | in_title={mc['in_title']}, in_conn={mc['in_conn']}, in_sentences={mc['in_sentences']}")
