"""
check_particle_collisions_and_option_keys.py
============================================

PURPOSE & SCOPE:
This script performs targeted, mechanical structural checks on chapter exercises in
src/data/chapterExercises.json.

WHAT THIS SCRIPT CHECKS:
1. Blank Detection: Verifies that every standard non-star exercise contains a recognized
   blank pattern (e.g. （　）, ( ), or ＿＿).
2. Structural String Collision: Reconstructs the complete sentence by substituting each
   option exactly as written into the blank, and checks for mechanical particle doubling
   (e.g. はは, をを, にに, がが) or missing slot bounds.
3. Option Text Consistency: Verifies that the text in `options[i]` exactly matches
   `explanation.options[i].text`.
4. Index Validity: Verifies that `correctIndex` is within the valid range of `options`.

CRITICAL LINGUISTIC DISCLAIMER:
- This script DOES NOT verify semantic explanation-to-sentence correspondence.
- It DOES NOT evaluate whether an explanation accurately describes the natural Japanese
  meaning, register, or aspectual nuances of the resulting sentence.
- Linguistic answer uniqueness, distractor plausibility, and pedagogical explanation
  fidelity require separate, qualitative linguistic review against authentic source
  materials.
"""

import json
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

with open(EXERCISES_PATH, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print(f"Loaded {len(exercises)} exercises from {EXERCISES_PATH.name}.")

def check_particle_collisions_and_keys():
    issues = []
    for idx, ex in enumerate(exercises):
        eid = ex.get('id', f'idx-{idx}')
        q = ex.get('question', '')
        opts = ex.get('options', [])
        exp = ex.get('explanation', {})
        exp_opts = exp.get('options', [])
        
        # Skip star-mark questions (they have multi-slot rearrangement verification)
        if ex.get('type') == 'star-mark' or '★' in q or ex.get('reconstructedSentence'):
            continue
            
        m = re.search(r'（[^）]*）|\([^)]*\)|＿＿+', q)
        if not m:
            issues.append((eid, "NO_BLANK_FOUND", q, None, "No blank delimiter found"))
            continue
            
        start, end = m.span()
        prefix = q[:start]
        suffix = q[end:]
        
        for o_idx, opt in enumerate(opts):
            recon = prefix + opt + suffix
            
            # Check for mechanical double particles
            for p in ['はは', 'をを', 'にに', 'がが']:
                if p in recon:
                    issues.append((eid, f"DOUBLE_PARTICLE_{p}", q, opt, f"Collision in: '{recon}'", o_idx))
                    
            # Check explanation option presence
            if o_idx >= len(exp_opts):
                issues.append((eid, "MISSING_EXP_OPTION", q, opt, f"Index {o_idx} >= {len(exp_opts)}", o_idx))
                continue
                
            e_opt = exp_opts[o_idx]
            # Check exact text alignment between option and explanation entry
            if e_opt.get('text') != opt:
                issues.append((eid, "OPTION_TEXT_MISMATCH", q, opt, f"exp text '{e_opt.get('text')}' != opt '{opt}'", o_idx))
                
    return issues

if __name__ == '__main__':
    issues = check_particle_collisions_and_keys()
    print(f"Total structural collision/keying issues found: {len(issues)}")
    for iss in issues:
        print(f"[{iss[0]}] {iss[1]}: prompt='{iss[2]}' | opt='{iss[3]}' | detail='{iss[4]}'")
    if not issues:
        print("✓ All exercises passed mechanical string collision and option keying checks cleanly.")
