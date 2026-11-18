import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print(f"Total exercises: {len(exercises)}")

short_reasons = []
inconsistent_counts = []
key_mismatches = []
star_exercises = []
passage_exercises = []

for idx, ex in enumerate(exercises):
    eid = ex.get('id', f'idx-{idx}')
    opts = ex.get('options', [])
    c_idx = ex.get('correctIndex')
    exp = ex.get('explanation', {})
    
    # 1. Structure check
    if not isinstance(exp, dict):
        inconsistent_counts.append((eid, "explanation is not dict"))
        continue
    
    exp_opts = exp.get('options', [])
    if len(opts) != len(exp_opts):
        inconsistent_counts.append((eid, f"options length ({len(opts)}) != explanation options length ({len(exp_opts)})"))
        continue
    
    # 2. Key consistency check
    true_indices = [i for i, o in enumerate(exp_opts) if o.get('isCorrect') is True]
    if len(true_indices) != 1 or true_indices[0] != c_idx:
        key_mismatches.append((eid, f"correctIndex is {c_idx} but isCorrect:True is at {true_indices}"))
    
    # 3. Distractor explanation quality
    for o_idx, o in enumerate(exp_opts):
        reason = o.get('reason', '')
        if len(reason.strip()) < 20:
            short_reasons.append((eid, o_idx, o.get('text'), reason))
            
    # 4. Star exercises
    if ex.get('type') == 'star' or '【★】' in ex.get('question', '') or '★' in ex.get('question', '') or ex.get('reconstructedSentence'):
        star_exercises.append(ex)
        
    # 5. Passage exercises
    if 'p3' in eid or 'passage' in eid or ex.get('context'):
        passage_exercises.append(ex)

print(f"Inconsistent counts: {len(inconsistent_counts)}")
if inconsistent_counts:
    print("  First 5:", inconsistent_counts[:5])

print(f"Key mismatches (isCorrect vs correctIndex): {len(key_mismatches)}")
if key_mismatches:
    print("  First 5:", key_mismatches[:5])

print(f"Short distractor reasons (<20 chars): {len(short_reasons)}")
if short_reasons:
    print("  First 5:", short_reasons[:5])

print(f"Star exercises found: {len(star_exercises)}")
print(f"Passage/context exercises found: {len(passage_exercises)}")
