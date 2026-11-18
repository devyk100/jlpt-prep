"""
verify_content_integrity.py
===========================

Automated regression check ensuring that:
1. Authoritative content sources (content/base-reviewed.json) and compiled study data
   (src/data/studyPoints.json) remain in exact sync.
2. Calibrated, sensible rule-strength explanations for `くせに` and `〜たらどうですか`
   survive normal pipeline assembly without reverting to obsolete blanket prohibitions
   or manufactured quotations.
3. Concrete exercise repairs for `skm2-p1-c24-q11`, `skm2-p1-c24-q12`, and `skm3-c2-ex-7`
   in src/data/chapterExercises.json remain intact with exact option substitution and
   no silent stem or particle collisions.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

def run_regression_checks():
    print("=== RUNNING CONTENT INTEGRITY & PIPELINE REGRESSION CHECKS ===")
    
    # 1. Load files
    sp_path = ROOT / "src/data/studyPoints.json"
    br_path = ROOT / "content/base-reviewed.json"
    ce_path = ROOT / "src/data/chapterExercises.json"
    
    with open(sp_path, 'r', encoding='utf-8') as f:
        sp_cards = {c['id']: c for c in json.load(f)}
    with open(br_path, 'r', encoding='utf-8') as f:
        br_cards = {c['id']: c for c in json.load(f)}
    with open(ce_path, 'r', encoding='utf-8') as f:
        exercises = {e['id']: e for e in json.load(f)}
        
    print(f"Loaded {len(sp_cards)} studyPoints, {len(br_cards)} base-reviewed, {len(exercises)} exercises.")
    
    failures = []
    
    # 2. Check kuse-ni in both authoritative base and compiled data
    for source_name, cards in [('base-reviewed.json', br_cards), ('studyPoints.json', sp_cards)]:
        kuse = cards.get('skm2-c15-kuse-ni')
        if not kuse:
            failures.append(f"Card skm2-c15-kuse-ni missing in {source_name}")
            continue
            
        nuance = kuse.get('nuance', '')
        # Check against regressed prohibition
        if "must share the same subject" in nuance:
            failures.append(f"Regressed prohibition 'must share the same subject' found in {source_name} for skm2-c15-kuse-ni")
        if "*私は知っているくせに... is ungrammatical" in nuance:
            failures.append(f"Regressed prohibition '*私は知っているくせに... is ungrammatical' found in {source_name} for skm2-c15-kuse-ni")
        # Check against unverified Japanese quotations attributed to SKM
        if "前と後ろの主語は同じ人であることが多い" in nuance:
            failures.append(f"Unverified Japanese quotation found in {source_name} for skm2-c15-kuse-ni")
        # Ensure calibrated wording is present
        if "SPEAKER'S BLAME & USAGE TENDENCY" not in nuance:
            failures.append(f"Expected calibrated header 'SPEAKER'S BLAME & USAGE TENDENCY' missing in {source_name} for skm2-c15-kuse-ni")

    # 3. Check tara-dou-desu-ka in both authoritative base and compiled data
    for source_name, cards in [('base-reviewed.json', br_cards), ('studyPoints.json', sp_cards)]:
        tara = cards.get('g2-l14-tara-dou-desu-ka')
        if not tara:
            failures.append(f"Card g2-l14-tara-dou-desu-ka missing in {source_name}")
            continue
            
        nuance = tara.get('nuance', '')
        if "INVITATION BAN: NEVER use" in nuance:
            failures.append(f"Regressed prohibition 'INVITATION BAN: NEVER use' found in {source_name} for g2-l14-tara-dou-desu-ka")
        if "PRAGMATIC USE & INVITATION CONVENTION" not in nuance:
            failures.append(f"Expected calibrated header 'PRAGMATIC USE & INVITATION CONVENTION' missing in {source_name} for g2-l14-tara-dou-desu-ka")

    # 4. Check synchronization between base-reviewed and studyPoints
    for cid in sp_cards:
        if cid not in br_cards:
            failures.append(f"Card {cid} in studyPoints.json missing in base-reviewed.json")
            continue
        sp_c = sp_cards[cid]
        br_c = br_cards[cid]
        for fld in ['title', 'meaning', 'connection', 'nuance', 'keyTakeaway']:
            if sp_c.get(fld, '').strip() != br_c.get(fld, '').strip():
                failures.append(f"Field mismatch between base-reviewed and studyPoints for card {cid} field '{fld}'")

    # 5. Check concrete exercise repairs in chapterExercises.json
    # 5a. skm2-p1-c24-q11
    q11 = exercises.get('skm2-p1-c24-q11')
    if not q11:
        failures.append("Exercise skm2-p1-c24-q11 missing")
    else:
        if q11.get('question') != '専門家が手厚くサポートしてくれるのだから、一人で余計な心配を（　）。':
            failures.append(f"skm2-p1-c24-q11 question prompt unexpected: '{q11.get('question')}'")
        expected_opts = ['することはない', 'することだ', 'しようではないか', 'するまい']
        if q11.get('options') != expected_opts:
            failures.append(f"skm2-p1-c24-q11 options mismatch: {q11.get('options')}")
        if q11.get('correctIndex') != 0:
            failures.append(f"skm2-p1-c24-q11 correctIndex is {q11.get('correctIndex')} != 0")

    # 5b. skm2-p1-c24-q12
    q12 = exercises.get('skm2-p1-c24-q12')
    if not q12:
        failures.append("Exercise skm2-p1-c24-q12 missing")
    else:
        if q12.get('question') != '志望校合格の夢を果たすまで、いかなることがあろうとも受験勉強を（　）。':
            failures.append(f"skm2-p1-c24-q12 question prompt unexpected: '{q12.get('question')}'")
        expected_opts = ['投げ出すまい', '投げ出すことだ', '投げ出そうではないか', '投げ出すことはない']
        if q12.get('options') != expected_opts:
            failures.append(f"skm2-p1-c24-q12 options mismatch: {q12.get('options')}")

    # 5c. skm3-c2-ex-7
    ex7 = exercises.get('skm3-c2-ex-7')
    if not ex7:
        failures.append("Exercise skm3-c2-ex-7 missing")
    else:
        q_text = ex7.get('question', '')
        if '（　　）は' in q_text:
            failures.append(f"skm3-c2-ex-7 prompt contains '（　　）は' risking double particle collision: '{q_text}'")
        if ex7.get('options') != ['によっては', 'については', 'に対しては', 'にとっては']:
            failures.append(f"skm3-c2-ex-7 options mismatch: {ex7.get('options')}")

    if failures:
        print(f"\nFAILED: {len(failures)} integrity check(s) failed:")
        for fail in failures:
            print(f"  ❌ {fail}")
        return False
    else:
        print("\n✓ ALL CONTENT INTEGRITY & PIPELINE REGRESSION CHECKS PASSED CLEANLY!")
        return True

if __name__ == '__main__':
    ok = run_regression_checks()
    if not ok:
        sys.exit(1)
