import json

with open("jlpt-exam-prep/scripts/detailed_34_audit.json", encoding="utf-8") as f:
    items = json.load(f)

for it in items:
    diff_recon = it["orig_reconstructedSentence"] != it["curr_reconstructedSentence"]
    print(f"{it['id']}: diff={diff_recon} | comma_opt={it['comma_attached_to']}")
    if diff_recon:
        print(f"   HEAD recon: {it['orig_reconstructedSentence']}")
        print(f"   CURR recon: {it['curr_reconstructedSentence']}")
