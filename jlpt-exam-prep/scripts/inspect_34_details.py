import json, re

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    ex = json.load(f)

# Re-identify the 34 exercises
target_ids = [
    'skm3-p2-c1-q6', 'skm3-p2-c1-q10', 'skm3-p2-c2-q7', 'skm3-p2-c2-q8', 'skm3-p2-c2-q9', 'skm3-p2-c2-q12',
    'skm3-p2-c3-q1', 'skm3-p2-c3-q7', 'skm2-p2-c1-q2', 'skm2-p2-c1-q4', 'skm2-p2-c1-q6', 'skm2-p2-c1-q7',
    'skm2-p2-c1-q8', 'skm2-p2-c1-q9', 'skm2-p2-c1-q10', 'skm2-p2-c1-q12', 'skm2-p2-c2-q1', 'skm2-p2-c2-q2',
    'skm2-p2-c2-q4', 'skm2-p2-c2-q6', 'skm2-p2-c2-q7', 'skm2-p2-c2-q8', 'skm2-p2-c2-q9', 'skm2-p2-c2-q10',
    'skm2-p2-c2-q11', 'skm2-p2-c2-q12', 'skm2-p2-c3-q1', 'skm2-p2-c3-q2', 'skm2-p2-c3-q3', 'skm2-p2-c3-q4',
    'skm2-p2-c3-q6', 'skm2-p2-c3-q7', 'skm2-p2-c3-q8', 'skm2-p2-c3-q9'
]

print(f"Total target exercises: {len(target_ids)}")

report = []
for tid in target_ids:
    item = [e for e in ex if e.get("id") == tid][0]
    q = item["question"]
    opts = item["options"]
    order = item.get("scrambleOrder", [])
    recon = item.get("reconstructedSentence", "")
    m = re.search(r"＿＿\s*＿＿\s*★\s*＿＿", q)
    prefix = q[:m.start()].strip()
    suffix = q[m.end():].strip()
    ordered_fragments = [opts[p - 1] for p in order]
    assembled = prefix + "".join(ordered_fragments) + suffix
    
    report.append({
        "id": tid,
        "chapter": item.get("chapter"),
        "question": q,
        "options": opts,
        "scrambleOrder": order,
        "ordered_fragments": ordered_fragments,
        "assembled": assembled,
        "current_recon": recon,
        "explanation_overall": item.get("explanation", {}).get("overall", "")
    })

with open("jlpt-exam-prep/scripts/reconstruction_inspection_34.json", "w", encoding="utf-8") as out:
    json.dump(report, out, ensure_ascii=False, indent=2)

print("Saved detailed inspection to reconstruction_inspection_34.json")
