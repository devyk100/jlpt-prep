import json
import re

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print(f"Loaded {len(exercises)} exercises.")

anomalies = []

for idx, ex in enumerate(exercises):
    eid = ex.get('id', f'idx-{idx}')
    q = ex.get('question', '')
    opts = ex.get('options', [])
    exp_opts = ex.get('explanation', {}).get('options', [])
    c_idx = ex.get('correctIndex', 0)
    
    # Skip star questions as they have separate multi-slot scramble verification
    if ex.get('type') == 'star-mark' or '★' in q or ex.get('reconstructedSentence'):
        continue
        
    # Find blank
    # Match standard Japanese parentheses or underscores
    blank_match = re.search(r'（[^）]*）|\([^)]*\)|＿＿+', q)
    if not blank_match:
        anomalies.append((eid, "NO_BLANK", q, None, None, None))
        continue
        
    start, end = blank_match.span()
    prefix = q[:start]
    suffix = q[end:]
    
    for o_idx, opt_text in enumerate(opts):
        # Reconstruct sentence exactly as written
        reconstructed = prefix + opt_text + suffix
        
        # Check for obvious morphological collision:
        # 1. Double particles: をを, にに, でで, はは, がが, のの
        if re.search(r'([をにではが])\1', reconstructed):
            # except valid phrases like のの or はは if any
            m_dup = re.search(r'([をにではが])\1', reconstructed)
            anomalies.append((eid, f"DOUBLE_PARTICLE ({m_dup.group(0)})", q, opt_text, reconstructed, o_idx))
            
        # 2. Collision with punctuation: 。。 or 、、
        if '。。' in reconstructed or '、、' in reconstructed:
            anomalies.append((eid, "DOUBLE_PUNCTUATION", q, opt_text, reconstructed, o_idx))
            
        # 3. Truncated stem collisions like 'すよう' or 'るる' or 'るまい' after hiragana
        if re.search(r'[ぁ-ん]るる|[ぁ-ん]すよう', reconstructed):
            anomalies.append((eid, "MALFORMED_COLLISION", q, opt_text, reconstructed, o_idx))
            
        # 4. Check if explanation option text matches opt_text
        if o_idx < len(exp_opts):
            e_opt = exp_opts[o_idx]
            if e_opt.get('text') != opt_text:
                anomalies.append((eid, "EXP_TEXT_MISMATCH", q, opt_text, f"exp text: {e_opt.get('text')}", o_idx))

print(f"Total reconstruction anomalies detected: {len(anomalies)}")
for a in anomalies[:30]:
    print(f"\n[{a[0]}] Type: {a[1]}")
    print(f"  Prompt: {a[2]}")
    print(f"  Option [{a[5]}]: '{a[3]}'")
    print(f"  Reconstructed/Detail: '{a[4]}'")
