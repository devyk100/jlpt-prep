import json

exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))
p3_qids = ['skm3-p3-c2-q10', 'skm3-p3-c4-q6', 'skm3-p3-c5-q11', 'skm3-p3-c10-q4', 'skm3-p3-c10-q5', 'skm3-p3-c10-q8', 'skm3-p3-c10-q11']

for qid in p3_qids:
    q = next(x for x in exercises if x['id'] == qid)
    print(f"=== {q['id']} ({q.get('chapter')}) ===")
    print(f"Q: {q.get('question')}")
    print(f"T: {q.get('translation')}")
    print(f"Opts: {q.get('options')}, Ans: {q.get('correctIndex')}")
    for opt in q.get('explanation', {}).get('options', []):
        print(f"  [{opt.get('isCorrect')}] {opt.get('text')}: {opt.get('reason')}")
    print()
