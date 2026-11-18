import json

with open("jlpt-exam-prep/scripts/detailed_34_audit.json", encoding="utf-8") as f:
    items = json.load(f)

print(f"Total inspected: {len(items)}")

# Categorize the 34 items by grammatical pattern
categories = {}
for it in items:
    comma_frag = it["comma_attached_to"][0] if it["comma_attached_to"] else "NONE"
    eid = it["id"]
    book = "SKM N3" if "skm3" in eid else "SKM N2"
    ch = it["chapter"]
    
    # Identify syntactic role of the comma
    if any(k in comma_frag for k in ["かどうか", "思って"]):
        cat = "Embedded Clause / Quotation Boundary"
    elif any(k in comma_frag for k in ["甲斐があって", "甲斐もなく"]):
        cat = "Adverbial Clause of Result (〜甲斐があって／なく)"
    elif any(k in comma_frag for k in ["以上"]):
        cat = "Conditional / Causal Clause (〜以上は)"
    elif any(k in comma_frag for k in ["て", "で"]):
        cat = "Te-form Conjunctive Clause Boundary"
    elif any(k in comma_frag for k in ["は", "が"]):
        cat = "Topical / Subject Clause Boundary"
    elif any(k in comma_frag for k in ["ために"]):
        cat = "Purpose Adverbial Clause (〜ために)"
    elif any(k in comma_frag for k in ["など"]):
        cat = "Exemplification / Object Focus (〜など)"
    else:
        cat = "Other Clause Boundary"
        
    categories.setdefault(cat, []).append(it)

print("\n=== BREAKDOWN OF THE 34 EXERCISES BY SYNTACTIC FUNCTION ===")
for cat, ex_list in categories.items():
    print(f"\n{cat} ({len(ex_list)} exercises):")
    for ex in ex_list:
        print(f"  - [{ex['id']}] {ex['question']}")
        print(f"    Scramble order: {ex['scrambleOrder']}")
        print(f"    Comma fragment: {ex['comma_attached_to']}")
        print(f"    Reconstructed: {ex['curr_reconstructedSentence']}")
