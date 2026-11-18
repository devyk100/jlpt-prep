import json, re

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    ex = json.load(f)

stars = [e for e in ex if e.get("type") == "star-mark"]
print(f"Checking {len(stars)} star mark exercises")

for s in stars:
    q = s["question"]
    order = s.get("scrambleOrder", [])
    opts = s.get("options", [])
    corr = s.get("correctIndex")
    expl_opts = s.get("explanation", {}).get("options", [])
    
    # 1. Permutation
    assert sorted(order) == [1, 2, 3, 4], f"{s['id']} order not permutation: {order}"
    
    # 2. Slot structure with ★ in slot 3
    m = re.search(r"＿＿\s*＿＿\s*★\s*＿＿", q)
    assert m, f"{s['id']} slot pattern mismatch: {q}"
    
    # 3. Keyed option corresponds to star slot (slot 3, index 2)
    assert corr == order[2] - 1, f"{s['id']} corr {corr} != order[2]-1 {order[2]-1}"
    
    # 4. Explanation options alignment
    assert len(expl_opts) == 4, f"{s['id']} expl_opts len != 4"
    for i in range(4):
        assert expl_opts[i]["text"] == opts[i], f"{s['id']} opt {i} text mismatch: {expl_opts[i]['text']} vs {opts[i]}"
        if i == corr:
            assert expl_opts[i]["isCorrect"] is True, f"{s['id']} corr opt isCorrect not True"
        else:
            assert expl_opts[i]["isCorrect"] is False, f"{s['id']} wrong opt isCorrect not False"

print("Checks 1-4 passed for all 84 star mark exercises!")
