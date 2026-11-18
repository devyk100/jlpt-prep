import json
import re

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print(f"Total exercises to inspect: {len(exercises)}")

def check_all_reconstructions():
    issues = []
    for idx, ex in enumerate(exercises):
        eid = ex.get('id', f'idx-{idx}')
        q = ex.get('question', '')
        opts = ex.get('options', [])
        exp = ex.get('explanation', {})
        exp_opts = exp.get('options', [])
        
        # Check star marks separately
        if ex.get('type') == 'star-mark' or '★' in q:
            continue
            
        m = re.search(r'（[^）]*）|\([^)]*\)|＿＿+', q)
        if not m:
            issues.append((eid, "NO_BLANK_FOUND", q, None, None))
            continue
            
        start, end = m.span()
        prefix = q[:start]
        suffix = q[end:]
        
        for o_idx, opt in enumerate(opts):
            recon = prefix + opt + suffix
            
            # 1. Double particles
            for p in ['はは', 'をを', 'にに', 'がが']:
                if p in recon:
                    issues.append((eid, f"DOUBLE_PARTICLE_{p}", q, opt, recon, o_idx))
                    
            # 2. Check if explanation option exists
            if o_idx >= len(exp_opts):
                issues.append((eid, "MISSING_EXP_OPTION", q, opt, f"Index {o_idx} >= {len(exp_opts)}", o_idx))
                continue
                
            e_opt = exp_opts[o_idx]
            # Check text match
            if e_opt.get('text') != opt:
                issues.append((eid, "OPTION_TEXT_MISMATCH", q, opt, f"exp text '{e_opt.get('text')}' != opt '{opt}'", o_idx))
                
            # Check if explanation reason silently talks about a completely different verb or structure
            reason = e_opt.get('reason', '')
            
    return issues

issues = check_all_reconstructions()
print(f"Total issues found: {len(issues)}")
for iss in issues:
    print(f"[{iss[0]}] {iss[1]}: prompt='{iss[2]}' | opt='{iss[3]}' | detail='{iss[4]}'")
