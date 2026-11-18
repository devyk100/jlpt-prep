import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

def dump_chapter(chap_name):
    print(f"\n==================== {chap_name} ====================")
    for ex in exercises:
        if ex.get('bookId') == 'skm-n2' and ex.get('chapter') == chap_name:
            eid = ex.get('id')
            q = ex.get('question')
            opts = ex.get('options')
            ci = ex.get('correctIndex')
            print(f"\nID: {eid}")
            print(f"Q: {q}")
            print(f"Options: {opts}, correctIndex: {ci}")
            for idx, opt in enumerate(ex.get('explanation', {}).get('options', [])):
                print(f"  [{idx}] {opt.get('text')}: isCorrect={opt.get('isCorrect')}")
                print(f"      reason: {opt.get('reason')}")

dump_chapter('Part 1 · Chapter 18')
dump_chapter('Part 1 · Chapter 19')
dump_chapter('Part 1 · Chapter 20')
