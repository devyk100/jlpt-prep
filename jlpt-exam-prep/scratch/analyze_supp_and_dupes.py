import json
from pathlib import Path

root = Path(r"c:\JLPT\jlpt-exam-prep")
pts = json.loads((root / "src/data/studyPoints.json").read_text(encoding="utf-8"))

textbook_cards = [p for p in pts if p.get("book")]
supp_cards = [p for p in pts if not p.get("book")]

print(f"Total cards: {len(pts)}")
print(f"Textbook cards: {len(textbook_cards)}")
print(f"Supplementary cards: {len(supp_cards)}")

print("\n--- ALL 70 SUPPLEMENTARY CARDS ---")
for s in supp_cards:
    print(f"ID: {s['id']:<30} | Level: {s.get('level'):<4} | Title: {s['title']}")

print("\n--- EXACT OR NEAR-EXACT DUPLICATES ---")
# Let's find overlaps where supplementary cards teach the exact same grammar point as textbook cards
dupes = []
for s in supp_cards:
    st = s['title'].lower()
    sid = s['id']
    for t in textbook_cards:
        tt = t['title'].lower()
        tid = t['id']
        
        # Check specific known duplicates
        # 1. Te form
        if 'te-form' in sid and ('te-form' in tid or 'て形' in tt):
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 2. X wa Y desu
        elif 'wa-desu' in sid and ('wa-desu' in tid or 'は' in tt and 'です' in tt):
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 3. Verb groups
        elif 'verb-groups' in sid and ('verb-conjugation' in tid or '動詞' in tt and '活用' in tt):
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 4. Ni kagiru / kagiri
        elif ('ni-kagiri' in sid or 'ni-kagiru' in sid) and ('ni-kagiri' in tid or 'ni-kagiru' in tid):
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 5. Ni kurabete
        elif 'kurabete' in sid and 'kurabete' in tid:
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 6. Tokoro datta vs tokoro da
        elif 'tokoro-datta' in sid and 'tokoro-da' in tid:
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 7. Garu
        elif 'garu' in sid and 'garu' in tid:
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 8. Kara koso
        elif 'kara-koso' in sid and 'kara-koso' in tid:
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 9. Ippou de
        elif 'ippou-de' in sid and 'ippou-de' in tid:
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))
        # 10. Kko nai
        elif 'kko-nai' in sid and 'kko-nai' in tid:
            dupes.append((sid, s['title'], tid, t['title'], t.get('book'), t.get('chapter')))

print(f"Found {len(dupes)} direct duplicate pairs:")
for sid, st, tid, tt, bk, ch in dupes:
    print(f"\n[DUPLICATE]")
    print(f"  Supplementary: {sid} -> {st}")
    print(f"  Textbook:      {tid} -> {tt} ({bk} {ch})")
