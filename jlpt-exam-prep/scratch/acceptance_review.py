import json
import re

print("=== STARTING COMPREHENSIVE FINAL ACCEPTANCE REVIEW ===")

# Load data
with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    study_points = json.load(f)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'r', encoding='utf-8') as f:
    tables = json.load(f)

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

print(f"Loaded {len(study_points)} study points, {len(exercises)} exercises, {len(tables)} tables, {len(matrix)} matrix rows.")

# 1. GROUPED CONSTRUCTIONS REVIEW
print("\n--- 1. AUDITING GROUPED CONSTRUCTIONS ---")

# Let's map target grouped constructions and verify cards and exercises
target_groups = {
    "Genki I: L12 〜んです vs plain assertion": ["g1-l12-1"],
    "Genki I: L11 〜ほうがいい vs 〜たらどうですか": ["g1-l11-2"],
    "Genki II: L13 〜そうです (appearance) vs L17 〜そうです (hearsay)": ["g2-l13-2", "g2-l17-1"],
    "Genki II: L14 Benefactives あげる / くれる / もらう": ["g2-l14-2"],
    "Genki II: L18/L22 Conditionals (と, ば, たら, なら)": ["g2-l18-3", "g2-l22-3"],
    "Genki II: L19/L20 Keigo (尊敬語 vs 謙譲語)": ["g2-l19-1", "g2-l19-2", "g2-l20-1", "g2-l20-2"],
    "Genki II: L21-23 Voice (受身 vs 使役 vs 使役受身)": ["g2-l21-1", "g2-l22-1", "g2-l23-1"],
    "Genki II: L23 〜ことにする vs 〜ことになる": ["g2-l23-3"],
    "SKM N3: Ch 1 〜うちに (opportunity vs change) vs 〜間に": ["skm3-c1-1", "skm3-c1-2", "skm3-c1-3"],
    "SKM N3: Ch 8 〜反面 vs 〜一方で vs 〜に対して": ["skm3-c8-1", "skm3-c8-2", "skm3-c8-3"],
    "SKM N3: Ch 9/11 〜わけだ vs 〜わけがない vs 〜わけではない": ["skm3-c9-1", "skm3-c9-2", "skm3-c11-1"],
    "SKM N2: Ch 1 〜次第では (contingency) vs 〜次第 (immediacy)": ["added-n2-1-次第では", "skm2-c1-1"],
    "SKM N2: Ch 3 〜わりに vs 〜にしては": ["skm2-c3-1", "skm2-c3-2"],
    "SKM N2: Ch 5 〜くせに (reproach) vs 〜のに": ["added-n2-5-くせに"],
    "SKM N2: Ch 8 〜反面 (internal duality) vs 〜一方で": ["added-n2-8-反面", "skm2-c8-1"],
    "SKM N2: Ch 10 〜ことから (origin/evidence) vs 〜ところから": ["added-n2-10-ことから"],
    "SKM N2: Ch 12 〜かねる vs 〜がたい vs 〜ようがない": ["skm2-c12-1", "skm2-c12-2", "skm2-c12-3"],
    "SKM N2: Ch 14 〜恐れがある vs 〜かねない": ["skm2-c14-2", "skm2-c14-3"],
    "SKM N2: Ch 17 〜末に vs 〜あげく": ["skm2-c17-1", "skm2-c17-2"],
    "SKM N2: Ch 18 〜ものだ vs 〜というものだ vs 〜べきだ vs 〜ことだ": ["skm2-c18-1", "skm2-c18-2", "skm2-c18-3", "skm2-c18-4"],
    "SKM N2: Ch 20 〜わけではない vs 〜わけがない": ["added-n2-20-わけではない", "skm2-c20-2"],
}

card_by_id = {c['id']: c for c in study_points}
for grp_name, card_ids in target_groups.items():
    found = []
    missing = []
    for cid in card_ids:
        if cid in card_by_id:
            c = card_by_id[cid]
            found.append(f"{cid} ({c['title']})")
        else:
            missing.append(cid)
    status_str = f"FOUND {len(found)}/{len(card_ids)}"
    if missing:
        status_str += f" [MISSING: {missing}]"
    print(f"[{status_str}] {grp_name}: {', '.join(found)}")

# 2. AUDITING MASTER TABLES AND PREREQUISITE MAPPINGS
print("\n--- 2. AUDITING MASTER TABLES ---")
for tid, tbl in tables.items():
    title = tbl.get('title', 'No Title')
    headers = tbl.get('headers', [])
    rows = tbl.get('rows', [])
    print(f"Table [{tid}]: {title} ({len(headers)} columns, {len(rows)} rows)")
    # Check for empty cells or suspicious placeholders
    for r_idx, row in enumerate(rows):
        for c_idx, cell in enumerate(row):
            if not str(cell).strip():
                print(f"  WARNING: Table {tid} row {r_idx} col {c_idx} is empty!")

# 3. AUDITING STAR-MARK LINGUISTIC RECONSTRUCTION & INTEGRITY
print("\n--- 3. AUDITING STAR-ORDER LINGUISTIC RECONSTRUCTION ---")
star_exercises = [ex for ex in exercises if ex.get('type') == 'star' or '【★】' in ex.get('prompt', '') or '★' in ex.get('prompt', '') or ex.get('reconstructedSentence')]
print(f"Total star exercises: {len(star_exercises)}")

# 4. AUDITING PASSAGE & DISCOURSE GRAMMAR
print("\n--- 4. AUDITING PASSAGE & DISCOURSE GRAMMAR ---")
passage_exercises = [ex for ex in exercises if 'passage' in ex.get('id', '') or 'p3' in ex.get('id', '') or ex.get('passageContext')]
print(f"Total passage exercises: {len(passage_exercises)}")

# 5. AUDITING LINGUISTIC ANSWER UNIQUENESS & DISTRACTOR FEEDBACK
print("\n--- 5. AUDITING DISTRACTOR EXCLUSIVITY & REASONS ---")
suspicious_reasons = []
generic_patterns = [
    r'不適切',
    r'間違',
    r'文脈',
    r'文法'
]
single_word_or_short = []
for ex in exercises:
    eid = ex.get('id', 'unknown')
    opts = ex.get('options', [])
    for o_idx, opt in enumerate(opts):
        r = opt.get('reason', '')
        if len(r.strip()) < 15:
            single_word_or_short.append((eid, o_idx, opt.get('text', ''), r))

print(f"Exercises with short distractor reasons (< 15 chars): {len(single_word_or_short)}")
if single_word_or_short:
    for item in single_word_or_short[:10]:
        print(f"  {item[0]} opt {item[1]} ({item[2]}): {item[3]}")

print("\n=== ACCEPTANCE REVIEW AUDIT INITIAL RUN COMPLETE ===")
