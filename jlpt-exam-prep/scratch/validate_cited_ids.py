import json
import re

# Load live data
with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)
sp_ids = set(p['id'] for p in sps)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)
ex_ids = set(e['id'] for e in exs)

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'r', encoding='utf-8') as f:
    tbls = json.load(f)
tbl_ids = set(tbls.keys())

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Read the artifact file to extract all cited IDs
artifact_path = 'C:/Users/devyk/.gemini/antigravity/brain/c59f6230-4d3b-4733-9f33-83b85592d14f/AUDIT_PROGRESS_AND_ACTION_PLAN.md'
with open(artifact_path, 'r', encoding='utf-8') as f:
    art_text = f.read()

# Extract backticked terms that look like IDs
backticked = re.findall(r'`([^`]+)`', art_text)
print(f"Total backticked terms in artifact: {len(backticked)}")

cited_cards = []
cited_tables = []
cited_exercises = []
unmatched_id_candidates = []

for b in sorted(set(backticked)):
    if b in sp_ids:
        cited_cards.append(b)
    elif b in tbl_ids:
        cited_tables.append(b)
    elif b in ex_ids:
        cited_exercises.append(b)
    elif any(prefix in b for prefix in ['g1-', 'g2-', 'skm2-', 'skm3-', 'added-', 'Matrix', 'Spectrum']):
        unmatched_id_candidates.append(b)

print(f"\nCited Cards found in studyPoints ({len(cited_cards)}):")
for c in cited_cards:
    print(f"  [OK CARD] {c}")

print(f"\nCited Tables found in mugUpTables ({len(cited_tables)}):")
for t in cited_tables:
    print(f"  [OK TABLE] {t}")

print(f"\nCited Exercises found in chapterExercises ({len(cited_exercises)}):")
for e in cited_exercises:
    print(f"  [OK EX] {e}")

print(f"\nUnmatched ID candidates ({len(unmatched_id_candidates)}):")
for u in unmatched_id_candidates:
    print(f"  [UNMATCHED] {u}")
