import json
import re

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

split_stems = []

for ex in exercises:
    if ex.get('type') == 'star-mark' or '★' in ex.get('question', ''):
        continue
    q = ex.get('question', '')
    eid = ex.get('id', '')
    
    # Find what precedes the blank
    m = re.search(r'([^\s、。！？]+)[（(]', q)
    if m:
        preceding = m.group(1)
        # Check if preceding looks like a truncated verb stem:
        # e.g., ending in single hiragana of stem or kanji
        opts = ex.get('options', [])
        exp_opts = ex.get('explanation', {}).get('options', [])
        
        # Check if options start with inflectional endings like 'る', 'す', 'た', 'て', 'ない'
        opt_starts = [o[0] for o in opts if len(o) > 0]
        if any(o.startswith(('る', 'れ', 'ら', 'せ', 'さ', 'す', 'そ', 'た', 'て', 'ち', 'っ', 'ば')) for o in opts):
            split_stems.append((eid, q, preceding, opts, exp_opts))

print(f"Total exercises where options start with inflectional endings: {len(split_stems)}")
for item in split_stems:
    print(f"\n[{item[0]}] Prompt: {item[1]}")
    print(f"  Preceding: {item[2]} | Options: {item[3]}")
