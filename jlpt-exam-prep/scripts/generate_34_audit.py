import json, subprocess

# Load git HEAD version of chapterExercises.json
res = subprocess.run(['git', 'show', 'HEAD:jlpt-exam-prep/src/data/chapterExercises.json'], capture_output=True, text=True, encoding='utf-8')
orig_exercises = {e['id']: e for e in json.loads(res.stdout)}

# Load current working tree version
with open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8') as f:
    curr_exercises = {e['id']: e for e in json.load(f)}

target_ids = [
    'skm3-p2-c1-q6', 'skm3-p2-c1-q10', 'skm3-p2-c2-q7', 'skm3-p2-c2-q8', 'skm3-p2-c2-q9', 'skm3-p2-c2-q12',
    'skm3-p2-c3-q1', 'skm3-p2-c3-q7', 'skm2-p2-c1-q2', 'skm2-p2-c1-q4', 'skm2-p2-c1-q6', 'skm2-p2-c1-q7',
    'skm2-p2-c1-q8', 'skm2-p2-c1-q9', 'skm2-p2-c1-q10', 'skm2-p2-c1-q12', 'skm2-p2-c2-q1', 'skm2-p2-c2-q2',
    'skm2-p2-c2-q4', 'skm2-p2-c2-q6', 'skm2-p2-c2-q7', 'skm2-p2-c2-q8', 'skm2-p2-c2-q9', 'skm2-p2-c2-q10',
    'skm2-p2-c2-q11', 'skm2-p2-c2-q12', 'skm2-p2-c3-q1', 'skm2-p2-c3-q2', 'skm2-p2-c3-q3', 'skm2-p2-c3-q4',
    'skm2-p2-c3-q6', 'skm2-p2-c3-q7', 'skm2-p2-c3-q8', 'skm2-p2-c3-q9'
]

records = []
for tid in target_ids:
    o = orig_exercises.get(tid, {})
    c = curr_exercises.get(tid, {})
    
    order = c.get('scrambleOrder', [])
    c_opts = c.get('options', [])
    o_opts = o.get('options', [])
    
    c_recon = c.get('reconstructedSentence', '')
    o_recon = o.get('reconstructedSentence', '')
    
    # Check what fragment received the comma
    comma_opt = [opt for opt in c_opts if '、' in opt]
    
    records.append({
        'id': tid,
        'chapter': c.get('chapter'),
        'question': c.get('question'),
        'orig_options': o_opts,
        'curr_options': c_opts,
        'scrambleOrder': order,
        'orig_reconstructedSentence': o_recon,
        'curr_reconstructedSentence': c_recon,
        'comma_attached_to': comma_opt,
        'explanation_overall': c.get('explanation', {}).get('overall', '')
    })

with open('jlpt-exam-prep/scripts/detailed_34_audit.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print(f'Saved detailed analysis of {len(records)} items to detailed_34_audit.json')
