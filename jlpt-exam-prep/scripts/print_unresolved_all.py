import json

with open("jlpt-exam-prep/scripts/unresolved_reasons.json", encoding="utf-8") as f:
    items = json.load(f)

print(f"Total: {len(items)}")
for i, it in enumerate(items, 1):
    print(f"\n# {i}. {it['id']} ({it['ch']})")
    print(f"# Q: {it['q']}")
    print(f"# Options: {it['options']}")
    print(f"# Bad options needing explanation: {[b[0] for b in it['bad_opts']]}")
