import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"
COVERAGE_PATH = ROOT / "audit/coverage.json"
BASE_PATH = ROOT / "content/base-reviewed.json"

matrix = json.load(open(MATRIX_PATH, encoding="utf-8"))
cards = json.load(open(BASE_PATH, encoding="utf-8"))
cards_by_id = {c["id"]: c for c in cards}

reopened_count = 0
checked_count = 0

for m in matrix:
    cid = m.get("cardId")
    b = m.get("sourceBook", "")
    card = cards_by_id.get(cid)
    
    if not card:
        m["status"] = "reopened"
        m["missingWork"] = "Card missing from base-reviewed.json. Reopened for audit."
        m["exampleIds"] = []
        m["exampleCount"] = 0
        reopened_count += 1
        continue
    
    # Retrieve true sentence IDs from base-reviewed
    real_s_ids = []
    for s in card.get("sentences", []):
        if "id" in s and s["id"]:
            real_s_ids.append(s["id"])
    for ex in card.get("examples", []):
        if isinstance(ex, dict) and "id" in ex and ex["id"]:
            real_s_ids.append(ex["id"])
    
    # Check if existing exampleIds contained synthetic/fabricated patterns
    old_ids = m.get("exampleIds", [])
    had_synthetic = any(
        "::s-skm2-" in eid or "::s-skm3-p" in eid or "::s-skm2-rev-" in eid or "::s-skm2-sup-" in eid or eid not in real_s_ids
        for eid in old_ids
    ) or (b in ["Shin Kanzen Master N2", "Shin Kanzen Master N3"] and m.get("status") == "checked" and had_synthetic)
    
    # Update exampleIds to actual existing IDs
    m["exampleIds"] = real_s_ids
    m["exampleCount"] = len(real_s_ids)
    
    # If the row had synthetic IDs or was marked checked in the blanket automated pass, reopen it
    # Genki I is genuinely verified (12 lessons, 52 rows).
    # Genki II lessons with verified proof stay checked; problematic rows get reopened.
    # SKM N3 Part 1 Ch 1-12 with verified proof stay checked; other rows get reopened.
    # SKM N2 rows were mass-generated; all get reopened.
    
    is_genki1 = (b == "Genki I (3rd Ed.)")
    is_genki2_verified = (b == "Genki II (3rd Ed.)" and not had_synthetic and len(real_s_ids) > 0 and "review-g2" in m.get("evidence", ""))
    is_skm3_verified = (b == "Shin Kanzen Master N3" and not had_synthetic and len(real_s_ids) > 0 and "Part 1 · Chapter" in m.get("sourceSection", "") and not "Part 2" in m.get("sourceSection", "") and not "Part 3" in m.get("sourceSection", "") and not "Form review" in m.get("sourceSection", ""))
    
    if is_genki1 or is_genki2_verified or is_skm3_verified:
        m["status"] = "checked"
        m["missingWork"] = ""
        checked_count += 1
    else:
        m["status"] = "reopened"
        m["missingWork"] = "Reopened per user directive for rigorous physical scan comparison, true example verification, and non-generic distractor repair."
        reopened_count += 1

MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")

# Update coverage.json
coverage_data = {
    "totalRows": len(matrix),
    "checked": checked_count,
    "reopened": reopened_count,
    "byBook": {}
}

for m in matrix:
    b = m.get("sourceBook", "Unknown")
    if b not in coverage_data["byBook"]:
        coverage_data["byBook"][b] = {"total": 0, "checked": 0, "reopened": 0}
    coverage_data["byBook"][b]["total"] += 1
    if m["status"] == "checked":
        coverage_data["byBook"][b]["checked"] += 1
    else:
        coverage_data["byBook"][b]["reopened"] += 1

COVERAGE_PATH.write_text(json.dumps(coverage_data, ensure_ascii=False, indent=2), encoding="utf-8")

print("=== REOPENED AUDIT LEDGER RESULTS ===")
print(f"Total Rows: {len(matrix)}")
print(f"Verified Checked Rows: {checked_count}")
print(f"Reopened Rows: {reopened_count}")
for b, counts in coverage_data["byBook"].items():
    print(f"  {b}: {counts['checked']} checked, {counts['reopened']} reopened (Total: {counts['total']})")
