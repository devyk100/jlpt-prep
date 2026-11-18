import json
import re

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# Find characters immediately before the blank
stem_ended_prompts = []

standard_particles = {'は', 'が', 'を', 'に', 'で', 'へ', 'と', 'の', 'も', 'より', 'から', 'まで', 'か', 'や', 'よ', 'ね', '、', '。', ' ', '　', '」', '』', '？', '！'}

for ex in exercises:
    if ex.get('type') == 'star-mark' or '★' in ex.get('question', ''):
        continue
    q = ex.get('question', '')
    m = re.search(r'（[^）]*）|\([^)]*\)|＿＿+', q)
    if not m:
        continue
    char_before = q[m.start()-1] if m.start() > 0 else ''
    two_chars = q[m.start()-2:m.start()] if m.start() > 1 else char_before
    
    if char_before not in standard_particles:
        stem_ended_prompts.append((ex['id'], q, two_chars, ex['options'], ex['explanation']['options']))

print(f"Total exercises where prompt does not end in standard particle/punctuation: {len(stem_ended_prompts)}")
for item in stem_ended_prompts:
    print(f"\n[{item[0]}] {item[1]}")
    print(f"  Ending: '{item[2]}' | Options: {item[3]}")
    for idx, opt in enumerate(item[4]):
        print(f"    opt {idx} ({opt.get('text')}): {opt.get('reason')[:60]}...")
