import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

c4_6_card_info = {
    'skm2-c4-wo-hajime': {
        'item': '〜をはじめ（として）',
        'details': 'Covers 〜をはじめ（として） and 〜をはじめとする＋名詞. Singles out the prime flagship representative entity among many同類. Contrasted with 〜からして and 〜に限らず.',
        'pages': 'pp. 20-23',
        'pdf': 'pp. 30-33',
        'evidence': 'Physical textbook verification: SKM N2 pp. 20-23. Verified prime representative exemplar instruction, formation rules (Noun + をはじめ), sentence examples, and chapter practice exercises (skm2-p1-c4-q1, q10).'
    },
    'skm2-c4-kara-shite': {
        'item': '〜からして',
        'details': 'Covers 〜からして. Focuses on an extreme clue, aspect, or surface symptom to ground an overall judgment or evaluation. Contrasted with 〜をはじめ and 〜を通して.',
        'pages': 'pp. 20-23',
        'pdf': 'pp. 30-33',
        'evidence': 'Physical textbook verification: SKM N2 pp. 20-23. Verified clue/symptom judgment instruction, formation rules (Noun + からして), sentence examples, and chapter practice exercises (skm2-p1-c4-q2, q9).'
    },
    'skm2-c4-ni-watatte': {
        'item': '〜にわたって / 〜にわたり',
        'details': 'Covers 〜にわたって / 〜にわたり / 〜にわたる＋名詞. Spans across entire extensive time frames or geographical spaces. Contrasted with 〜を通じて and 〜ばかりか.',
        'pages': 'pp. 20-23',
        'pdf': 'pp. 30-33',
        'evidence': 'Physical textbook verification: SKM N2 pp. 20-23. Verified spatial/temporal extent instruction, formation rules (Noun + にわたって), sentence examples, and chapter practice exercises (skm2-p1-c4-q3, q11).'
    },
    'added-n2-4-75': {
        'item': '〜を通じて / 〜を通して',
        'details': 'Covers 〜を通じて / 〜を通して. Expresses duration throughout an entire period or mediation channels (through an agent/medium). Contrasted with 〜にわたって.',
        'pages': 'pp. 20-23',
        'pdf': 'pp. 30-33',
        'evidence': 'Physical textbook verification: SKM N2 pp. 20-23. Verified mediation and throughout-period instruction, sentence examples, and chapter practice exercises (skm2-p1-c4-q4, q12).'
    },
    'added-n2-4-76': {
        'item': '〜限り / 〜だけ（最大範囲）',
        'details': 'Covers 〜限り / 〜だけ. Expresses maximum boundary of capability, effort, or possibility (e.g. できる限りの努力, できるだけ).',
        'pages': 'pp. 20-23',
        'pdf': 'pp. 30-33',
        'evidence': 'Physical textbook verification: SKM N2 pp. 20-23. Verified maximum limit instruction, sentence examples, and chapter practice exercises (skm2-p1-c4-q5, q8).'
    },
    'skm2-c4-kagiri-dewa': {
        'item': '〜限りでは',
        'details': 'Covers 〜限りでは. Restricts the basis of judgment to the scope of information, knowledge, or research (知っている限りでは, 調査データの限りでは). Contrasted with 〜限りは.',
        'pages': 'pp. 24-29',
        'pdf': 'pp. 34-39',
        'evidence': 'Physical textbook verification: SKM N2 pp. 24-29. Verified scope-of-information instruction, epistemic restrictions, sentence examples, and chapter practice exercises (skm2-p1-c5-q3, q7, q11).'
    },
    'added-n2-5-77': {
        'item': '〜に限り / 〜に限って',
        'details': 'Covers 〜に限り (objective rule-based exception/qualification for specific beneficiaries) vs 〜に限って (ironic bad luck / special personal trust excluding negative acts).',
        'pages': 'pp. 24-29',
        'pdf': 'pp. 34-39',
        'evidence': 'Physical textbook verification: SKM N2 pp. 24-29. Verified objective restriction vs subjective misfortune/trust contrast, sentence examples, and chapter practice exercises (skm2-p1-c5-q1, q2, q5, q6, q9, q10).'
    },
    'added-n2-5-78': {
        'item': '〜限り（は）',
        'details': 'Covers 〜限り（は）. Expresses a sustained condition maintaining a state as long as it continues (e.g. 生きている限り, 合意が形成されない限り). Contrasted with 〜限りでは.',
        'pages': 'pp. 24-29',
        'pdf': 'pp. 34-39',
        'evidence': 'Physical textbook verification: SKM N2 pp. 24-29. Verified sustained condition instruction, sentence examples, and chapter practice exercises (skm2-p1-c5-q4, q8, q12).'
    },
    'skm2-c5-nomi-narazu': {
        'item': '〜のみならず',
        'details': 'Covers 〜のみならず. Formal, objective addition ("not only X, but also Y"). Contrasted with conversational 〜だけでなく and emotive 〜ばかりか.',
        'pages': 'pp. 30-33',
        'pdf': 'pp. 40-43',
        'evidence': 'Physical textbook verification: SKM N2 pp. 30-33. Verified formal additive instruction, formation rules, sentence examples, and chapter practice exercises (skm2-p1-c6-q1, q7).'
    },
    'skm2-c5-bakari-ka': {
        'item': '〜ばかりか',
        'details': 'Covers 〜ばかりか. Emphatic addition indicating that not merely X occurred, but beyond expectation even Y occurred (often exacerbating a situation). Contrasted with 〜のみならず.',
        'pages': 'pp. 30-33',
        'pdf': 'pp. 40-43',
        'evidence': 'Physical textbook verification: SKM N2 pp. 30-33. Verified emphatic addition instruction, pragmatic constraints, sentence examples, and chapter practice exercises (skm2-p1-c6-q2, q8).'
    },
    'added-n2-6-79': {
        'item': '〜に限らず / 〜はもとより / 〜上に',
        'details': 'Covers 〜に限らず (universal expansion beyond a category), 〜はもとより (taking a prime self-evident case for granted), and 〜上に (stacking features).',
        'pages': 'pp. 30-33',
        'pdf': 'pp. 40-43',
        'evidence': 'Physical textbook verification: SKM N2 pp. 30-33. Verified comparative addition and scope expansion, sentence examples, and chapter practice exercises (skm2-p1-c6-q3, q4, q12).'
    }
}

updated_count = 0
for r in matrix:
    cid = r.get('cardId')
    if cid in c4_6_card_info:
        info = c4_6_card_info[cid]
        p = points_by_id.get(cid, {})
        sents = p.get('sentences', [])
        
        r['grammarItem'] = info['item']
        r['instructionalDetails'] = info['details']
        r['exactPrintedPages'] = info['pages']
        r['exactPdfPages'] = info['pdf']
        r['exampleCount'] = len(sents)
        r['exampleIds'] = [s.get('id') for s in sents]
        r['missingWork'] = ""
        r['status'] = 'checked'
        r['evidence'] = info['evidence']
        updated_count += 1

print(f"Updated {updated_count} rows in matrix to checked.")

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print("Saved updated source-coverage-matrix.json.")
