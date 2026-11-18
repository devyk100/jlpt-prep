import json

with open("jlpt-exam-prep/scripts/reconstruction_inspection_34.json", encoding="utf-8") as f:
    items = json.load(f)

# Previous reconstructed sentences from our git history / earlier state:
# In each item, the comma was present in the original reconstructed sentence.
for item in items:
    q = item["question"]
    opts = item["options"]
    order = item["scrambleOrder"]
    frags = item["ordered_fragments"]
    assembled = item["assembled"]
    expl = item["explanation_overall"]
    
    # Let's locate where the comma naturally occurs in expl or previous recon
    # E.g. in expl, look for quotes or structure
    print(f"\n[{item['id']}] ({item['chapter']})")
    print(f"  Prompt:   {q}")
    print(f"  Frags in order: 1: {frags[0]} | 2: {frags[1]} | 3(★): {frags[2]} | 4: {frags[3]}")
    print(f"  Assembled: {assembled}")
    print(f"  Expl excerpt: {expl[:120]}...")
