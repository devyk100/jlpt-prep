import json
import re

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)

with open('C:/Users/devyk/.gemini/antigravity/brain/c59f6230-4d3b-4733-9f33-83b85592d14f/AUDIT_PROGRESS_AND_ACTION_PLAN.md', 'r', encoding='utf-8') as f:
    art_text = f.read()

print("=== SCANNING FOR OVERLY ABSOLUTE CLAIMS IN STUDY POINTS ===")
absolute_terms = [r'\bBAN\b', r'\bNEVER\b', r'strictly forbidden', r'strictly ungrammatical', r'impossible in Japanese', r'cannot be used under any circumstances']

sp_findings = []
for sp in sps:
    text_to_check = f"{sp.get('nuance', '')} {sp.get('keyTakeaway', '')}"
    for term in absolute_terms:
        m = re.search(term, text_to_check, re.IGNORECASE)
        if m:
            sp_findings.append((sp['id'], sp['title'], m.group(0), text_to_check))
            break

print(f"Study points with absolute terms: {len(sp_findings)}")
for f in sp_findings:
    print(f"[{f[0]}] Term: '{f[2]}' | Title: {f[1]}")
    # print small context
    idx = f[3].lower().find(f[2].lower())
    start = max(0, idx - 40)
    end = min(len(f[3]), idx + 60)
    print(f"  Context: ...{f[3][start:end]}...")

print("\n=== SCANNING FOR OVERLY ABSOLUTE CLAIMS IN ARTIFACT ===")
art_findings = []
for line_no, line in enumerate(art_text.splitlines(), 1):
    for term in absolute_terms + [r'strictly prohibited', r'strictly ungrammatical', r'strictly forbidding', r'strictly enforced']:
        m = re.search(term, line, re.IGNORECASE)
        if m:
            art_findings.append((line_no, m.group(0), line))

print(f"Artifact lines with absolute terms: {len(art_findings)}")
for a in art_findings:
    print(f"  Line {a[0]} ('{a[1]}'): {a[2]}")
