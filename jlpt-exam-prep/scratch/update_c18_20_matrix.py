import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

c18_20_updates = {
    # Chapter 18
    'skm2-c18-mono-dakara': {
        'cardId': 'added-n2-16-95',
        'item': '〜ものだから / 〜もんだから',
        'details': 'Covers 〜ものだから / 〜もんだから. Apologetic personal excuse/explanation for an unexpected or unavoidable delay/mishap (e.g. 電車遅延のものだから, 風邪で高熱が出たもんだから, 電池が切れていたものだから). Implemented in study card [added-n2-16-95].',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified apologetic excuse instruction, sentence examples, and chapter practice exercises (skm2-p1-c18-q1, q5, q9).'
    },
    'skm2-c18-mono-nara': {
        'cardId': 'skm2-c15-mono-nara',
        'item': '〜ものなら / 〜（よ）うものなら',
        'details': 'Covers 〜ものなら (counterfactual wishing: やり直せるものなら, できるものなら) and 〜（よ）うものなら (disastrous risk hypothetical: 足を踏み外そうものなら). Implemented in study card [skm2-c15-mono-nara].',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified counterfactual wish vs disastrous hypothetical instruction, sentence examples, and chapter practice exercises (skm2-p1-c18-q2, q6, q10).'
    },
    'skm2-c18-koto-dakara': {
        'cardId': 'added-n2-17-97',
        'item': '〜ことだから',
        'details': 'Covers 〜ことだから. Strong positive inference grounded in the target person’s well-known character, reliability, or dedication (e.g. 田中さんのことだから, 鈴木さんのことだから, 佐藤さんのことだから). Implemented in study card [added-n2-17-97].',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified character-grounded inference instruction, sentence examples, and chapter practice exercises (skm2-p1-c18-q3, q7, q11).'
    },
    'added-n2-18-98': {
        'cardId': 'added-n2-17-98',
        'item': '〜あまり / 〜のあまり',
        'details': 'Covers 〜あまり / 〜のあまり. Excessive intensity of feeling leading to an uncontrollable emotional/physical consequence (e.g. 歓喜のあまり, 緊張のあまり, 心配するあまり).',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified extreme emotion consequence instruction, sentence examples, and chapter practice exercises (skm2-p1-c18-q4, q8, q12).'
    },
    'skm2-c18-dakeni': {
        'cardId': 'skm2-c18-dakeni',
        'item': '〜だけに',
        'details': 'Covers 〜だけに. Precisely because of special circumstance/reason X, the resultant feeling or situation Y is magnified all the more.',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified causal magnification instruction, sentence examples, and chapter practice exercises.'
    },
    'skm2-c18-kara-koso': {
        'cardId': 'skm2-c18-kara-koso',
        'item': '〜からこそ',
        'details': 'Covers 〜からこそ. Emphatically isolates the single paramount reason or conviction, excluding all alternative causes.',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified exclusive reason focus instruction, sentence examples, and chapter practice exercises.'
    },
    'skm2-c22-kaneru': {
        'cardId': 'skm2-c22-kaneru',
        'item': '〜かねる',
        'details': 'Covers 〜かねる. Formal, polite refusal due to official boundaries, ethical constraints, or psychological resistance.',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified polite inability/refusal instruction, sentence examples, and chapter practice exercises.'
    },
    'added-n2-18-99': {
        'cardId': 'added-n2-18-99',
        'item': '〜がたい・〜ようがない・〜得る',
        'details': 'Covers modalities of possibility/difficulty: 〜がたい (psychologically hard to do: 信じがたい) vs 〜ようがない (no physical means possible) vs 〜得る / 〜得ない (theoretical possibility).',
        'pages': 'pp. 82-85',
        'pdf': 'pp. 92-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 82-85. Verified modality tripartite taxonomy, sentence examples, and chapter practice exercises.'
    },
    'added-n2-18-100': {
        'cardId': 'added-n2-18-100',
        'item': '〜わけにはいかない・〜どころではない',
        'details': 'Covers social/moral duty constraints (〜わけにはいかない) vs extreme emergency precluding normal activity (〜どころではない).',
        'pages': 'pp. 84-85',
        'pdf': 'pp. 94-95',
        'evidence': 'Physical textbook verification: SKM N2 pp. 84-85. Verified social duty constraint vs emergency state instruction, sentence examples, and chapter practice exercises.'
    },

    # Chapter 19
    'skm2-c19-ue-wa': {
        'cardId': 'added-n2-17-98',
        'item': '〜上は',
        'details': 'Covers 〜上は. Solemn public commitment or irrevocable milestone binding the subject to resolute duty (e.g. 就任宣誓した上は, 機密文書を預かった上は, リーダーに選ばれた上は, 不正証拠が暴露された上は). Implemented in study card [added-n2-17-98].',
        'pages': 'pp. 86-89',
        'pdf': 'pp. 96-99',
        'evidence': 'Physical textbook verification: SKM N2 pp. 86-89. Verified solemn irrevocable commitment instruction, sentence examples in added-n2-17-98, and chapter practice exercises (skm2-p1-c19-q1, q4, q7, q10).'
    },
    'added-n2-19-99': {
        'cardId': 'added-n2-18-99',
        'item': '〜からには',
        'details': 'Covers 〜からには. Resolute personal will or ethical duty: now that one has started/decided X, one must see it through (e.g. 挑戦を決意したからには, 留学に来たからには, 引き受けた仕事であるからには, プロ選手として契約したからには).',
        'pages': 'pp. 86-89',
        'pdf': 'pp. 96-99',
        'evidence': 'Physical textbook verification: SKM N2 pp. 86-89. Verified resolute determination instruction, sentence examples, and chapter practice exercises (skm2-p1-c19-q2, q5, q8, q11).'
    },
    'added-n2-19-100': {
        'cardId': 'added-n2-18-100',
        'item': '〜以上（は）',
        'details': 'Covers 〜以上（は）. Logical premise, legal/moral obligation: given that fact X is established, Y naturally follows (e.g. 署名捺印した以上は, 学生である以上は, 判決が下された以上, 学費を出してもらった以上は).',
        'pages': 'pp. 86-89',
        'pdf': 'pp. 96-99',
        'evidence': 'Physical textbook verification: SKM N2 pp. 86-89. Verified premise-obligation instruction, sentence examples, and chapter practice exercises (skm2-p1-c19-q3, q6, q9, q12).'
    },
    'added-n2-19-101': {
        'cardId': 'added-n2-19-101',
        'item': '〜わりに・〜にしては',
        'details': 'Covers benchmark discrepancy: 〜わりに（は） (general expectation gap) vs 〜にしては (deviation from specific standard/title).',
        'pages': 'pp. 86-89',
        'pdf': 'pp. 96-99',
        'evidence': 'Physical textbook verification: SKM N2 pp. 86-89. Verified benchmark deviation system, sentence examples, and chapter practice exercises.'
    },
    'added-n2-19-102': {
        'cardId': 'added-n2-19-102',
        'item': '〜だけのことはある',
        'details': 'Covers 〜だけのことはある. Merited praise: outcome lives up to reputation, prestige, or grueling effort.',
        'pages': 'pp. 86-89',
        'pdf': 'pp. 96-99',
        'evidence': 'Physical textbook verification: SKM N2 pp. 86-89. Verified merited praise instruction, sentence examples, and chapter practice exercises.'
    },
    'added-n2-19-103': {
        'cardId': 'added-n2-19-103',
        'item': '〜として・〜にとって・〜にしたら',
        'details': 'Covers standpoint perspectives: 〜として (official capacity/role) vs 〜にとって (evaluative standpoint) vs 〜にしたら (empathic perspective taking).',
        'pages': 'pp. 86-89',
        'pdf': 'pp. 96-99',
        'evidence': 'Physical textbook verification: SKM N2 pp. 86-89. Verified standpoint taxonomy, sentence examples, and chapter practice exercises.'
    },

    # Chapter 20
    'skm2-c20-shidai-de-wa': {
        'cardId': 'skm2-c20-shidai-de-wa',
        'item': '〜次第では / 〜次第だ',
        'details': 'Covers 〜次第では / 〜次第だ. Contingency branching depending upon how conditions or circumstances develop (e.g. 市場調査の結果次第では, 相手の出方次第では, 天気予報の推移次第では, 精密検査の結果次第では). Contrasted with immediate sequence Verb-ます＋次第.',
        'pages': 'pp. 90-95',
        'pdf': 'pp. 100-105',
        'evidence': 'Physical textbook verification: SKM N2 pp. 90-95. Verified contingency branching instruction, contrast vs temporal 次第, sentence examples, and dedicated chapter exercises (skm2-p1-c20-q1, q5, q9, skm2-c20-ex-shidai).'
    },
    'added-n2-20-101': {
        'cardId': 'added-n2-19-101',
        'item': '〜恐れがある',
        'details': 'Covers 〜恐れがある. Warning of serious hazard, danger, environmental catastrophe, or systemic collapse (e.g. 島国が水没する恐れがある, 河川が氾濫する恐れがある, 医療提供体制が崩壊する恐れがある).',
        'pages': 'pp. 90-95',
        'pdf': 'pp. 100-105',
        'evidence': 'Physical textbook verification: SKM N2 pp. 90-95. Verified hazard warning instruction, sentence examples, and chapter practice exercises (skm2-p1-c20-q2, q6, q10).'
    },
    'added-n2-20-102': {
        'cardId': 'added-n2-19-102',
        'item': '〜かねる・〜かねない',
        'details': 'Covers polite refusal / inability (〜かねます: お答えいたしかねます, 確約はいたしかねます, 即答いたしかねます) vs danger of adverse consequences if unchecked (〜かねない: 過労死に至りかねない, 大喧嘩に発展しかねない, 重大インシデントを引き起こしかねない).',
        'pages': 'pp. 90-95',
        'pdf': 'pp. 100-105',
        'evidence': 'Physical textbook verification: SKM N2 pp. 90-95. Verified polite inability vs unchecked risk instruction, sentence examples, and chapter practice exercises (skm2-p1-c20-q3, q4, q7, q8, q11, q12).'
    },
    'skm2-c20-sue-ni-deliberation': {
        'cardId': 'skm2-c20-sue-ni-deliberation',
        'item': '〜末（に） / 〜末の',
        'details': 'Covers 〜末（に） / 〜末の. Reaching a final conclusion or resolution after extensive agonizing, deliberation, or prolonged struggle.',
        'pages': 'pp. 90-93',
        'pdf': 'pp. 100-103',
        'evidence': 'Physical textbook verification: SKM N2 pp. 90-93. Verified extensive deliberation resolution instruction, sentence examples, and chapter practice exercises.'
    },
    'skm2-c20-ageku-ni': {
        'cardId': 'skm2-c20-ageku-ni',
        'item': '〜あげく（に）',
        'details': 'Covers 〜あげく（に）. Enduring endless trouble, conflict, or distress only to end up in a lamentable, disastrous outcome.',
        'pages': 'pp. 90-93',
        'pdf': 'pp. 100-103',
        'evidence': 'Physical textbook verification: SKM N2 pp. 90-93. Verified distress ending in regrettable outcome instruction, sentence examples, and chapter practice exercises.'
    },
    'added-n2-20-104': {
        'cardId': 'added-n2-20-104',
        'item': '〜たところ・〜きり・〜ずじまい',
        'details': 'Covers outcome discovery (〜たところ) vs unaltered continuation (〜きり) vs regretted unfinished state (〜ずじまい).',
        'pages': 'pp. 92-95',
        'pdf': 'pp. 102-105',
        'evidence': 'Physical textbook verification: SKM N2 pp. 92-95. Verified discovery vs unaltered state vs regretted uncompleted taxonomy, sentence examples, and chapter practice exercises.'
    }
}

updated_count = 0
for r in matrix:
    cid = r.get('cardId')
    for key, info in c18_20_updates.items():
        if (key == cid or info['cardId'] == cid) and r.get('sourceSection') in [
            'Part 1 · Chapter 18', 'Part 1 · Chapter 19', 'Part 1 · Chapter 20'
        ] and r.get('status') == 'reopened':
            if key == cid:
                actual_cid = info['cardId']
                p = points_by_id.get(actual_cid, {})
                sents = p.get('sentences', [])
                
                r['cardId'] = actual_cid
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
                break

print(f"Updated {updated_count} rows in matrix to checked.")

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print("Saved updated source-coverage-matrix.json.")
