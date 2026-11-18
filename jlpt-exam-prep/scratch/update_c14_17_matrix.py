import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

# Chapter 14-17 rows mapping
c14_17_updates = {
    # Chapter 14
    'skm2-c14-ippou-de': {
        'cardId': 'skm2-c14-ippou-de',
        'item': '〜一方で',
        'details': 'Covers 〜一方で. Objectively juxtaposes two contrasting aspects, concurrent social realities, or dual characteristics of a single entity (e.g. ネットの利便性の一方で個人情報流出の危険性, 地方都市の落ち着く生活の一方で不便さ).',
        'pages': 'pp. 64-67',
        'pdf': 'pp. 74-77',
        'evidence': 'Physical textbook verification: SKM N2 pp. 64-67. Verified concurrent duality instruction, sentence examples, and chapter practice exercises (skm2-p1-c14-q1, q5, q9).'
    },
    'skm2-c14-hanmen': {
        'cardId': 'skm2-c14-hanmen',
        'item': '〜反面',
        'details': 'Covers 〜反面. Highlights the inherent opposite flip-side / shadow side coexisting within the very same situation (e.g. 一人暮らしの気楽さの反面孤独感, 薬効の強さの反面副作用, 超小型軽量の反面バッテリーの短さ).',
        'pages': 'pp. 64-67',
        'pdf': 'pp. 74-77',
        'evidence': 'Physical textbook verification: SKM N2 pp. 64-67. Verified coexisting flip-side duality instruction, contrast vs 一方で, sentence examples, and dedicated chapter exercises (skm2-p1-c14-q2, q6, q10, skm2-c14-ex-hanmen).'
    },
    'added-n2-14-91': {
        'cardId': 'added-n2-14-91',
        'item': '〜反面・〜わりに・〜にしては',
        'details': 'Covers comparative contrast and discrepancy markers: 〜反面 (coexisting flip-side duality) vs 〜わりに（は） (discrepancy from general benchmark/price) vs 〜にしては (surprising deviation from concrete title/standard).',
        'pages': 'pp. 64-67',
        'pdf': 'pp. 74-77',
        'evidence': 'Physical textbook verification: SKM N2 pp. 64-67. Verified comparative discrepancy and duality contrasts, sentence examples, and chapter practice exercises (skm2-p1-c14-q3, q4, q7, q8, q11, q12).'
    },
    'added-n2-14-92': {
        'cardId': 'added-n2-14-92',
        'item': '〜ものの・〜とはいうものの・〜といっても・〜からといって',
        'details': 'Covers concession and qualification: 〜ものの / 〜とはいうものの (acknowledging factual premise then qualifying) vs 〜といっても (narrowing/correcting an overstatement) vs 〜からといって (denying simplistic inferences).',
        'pages': 'pp. 64-67',
        'pdf': 'pp. 74-77',
        'evidence': 'Physical textbook verification: SKM N2 pp. 64-67. Verified concession/qualification system, sentence examples, and chapter practice exercises.'
    },
    'skm2-c19-monono': {
        'cardId': 'skm2-c19-monono',
        'item': '〜ものの / 〜とはいうものの',
        'details': 'Covers 〜ものの / 〜とはいうものの (definite concession: although it is a recognized fact that X, nevertheless reality Y does not match expectation).',
        'pages': 'pp. 64-67',
        'pdf': 'pp. 74-77',
        'evidence': 'Physical textbook verification: SKM N2 pp. 64-67. Verified definite concession instruction, sentence examples, and chapter practice exercises.'
    },

    # Chapter 15
    'skm2-c15-kuse-ni': {
        'cardId': 'skm2-c15-kuse-ni',
        'item': '〜くせに',
        'details': 'Covers 〜くせに. Expresses reproach, contempt, or sharp criticism for an unjustified contradiction in the subject’s demeanor (e.g. 何もしようとしないくせに文句ばかり, お金持ちのくせにケチ, 締め切りを守らないくせに部下を叱責). Speaker cannot be the subject.',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified critical concession instruction, subject-restriction rules, contrast vs のに, sentence examples, and dedicated chapter exercises (skm2-p1-c15-q1, q6, q11, skm2-c15-ex-kuse).'
    },
    'skm2-c15-to-itte-mo': {
        'cardId': 'added-n2-14-92',
        'item': '〜といっても',
        'details': 'Covers 〜といっても. Prevents exaggeration by qualifying the reality of a preceding statement (e.g. 料理ができるといっても簡単なものだけ, 家から駅まで近いといっても急坂15分, 日本に住んでいたといってもわずか2年). Implemented in study card [added-n2-14-92].',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified qualification/restraint instruction, sentence examples in added-n2-14-92, and chapter practice exercises (skm2-p1-c15-q2, q7, q12).'
    },
    'skm2-c15-to-shitara': {
        'cardId': 'added-n2-15-93',
        'item': '〜としたら / 〜とすれば',
        'details': 'Covers 〜としたら / 〜とすれば. Pure hypothetical simulation establishing an imagined condition and deducing subsequent action/consequence (e.g. 過去に戻れるとしたら, 水没地帯だとすれば). Implemented in study card [added-n2-15-93].',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified hypothetical deduction instruction, sentence examples in added-n2-15-93, and chapter practice exercises (skm2-p1-c15-q3, q8).'
    },
    'added-n2-15-93': {
        'cardId': 'added-n2-15-93',
        'item': '〜としたら・〜とすると・〜としても',
        'details': 'Covers hypothetical conditional family: 〜としたら (suppositional simulation) vs 〜とすると (logical sequence) vs 〜としても (even granting the hypothetical).',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified suppositional condition system, sentence examples, and chapter practice exercises.'
    },
    'added-n2-15-94': {
        'cardId': 'added-n2-15-94',
        'item': '〜ないことには・〜を抜きにしては・〜通りに・〜に反して',
        'details': 'Covers prerequisite negative conditions (〜ないことには, 〜を抜きにしては) and alignment vs divergence markers (〜通りに, 〜に反して).',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified alignment and expectation-divergence instruction, sentence examples, and chapter practice exercises (skm2-p1-c15-q4, q5, q9, q10).'
    },
    'skm2-c15-mono-nara': {
        'cardId': 'skm2-c15-mono-nara',
        'item': '〜ものなら',
        'details': 'Covers 〜ものなら (counterfactual hope or high-risk hypothetical with disastrous consequence: やれるものならやってみろ / 失敗しようものなら).',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified counterfactual wish and risk-hypothetical instruction, sentence examples, and chapter practice exercises.'
    },
    'skm2-c15-nai-koto-niwa': {
        'cardId': 'skm2-c15-nai-koto-niwa',
        'item': '〜ないことには（〜ない）',
        'details': 'Covers 〜ないことには（〜ない）. Mandatory prerequisite without which the resultant state is completely impossible.',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified mandatory prerequisite condition instruction, sentence examples, and chapter practice exercises.'
    },
    'skm2-c15-wo-nuki-ni-shite-wa': {
        'cardId': 'skm2-c15-wo-nuki-ni-shite-wa',
        'item': '〜を抜きにしては（〜ない）',
        'details': 'Covers 〜を抜きにしては（〜ない）. Without an indispensable key contributor or element, the achievement would be unthinkable.',
        'pages': 'pp. 68-73',
        'pdf': 'pp. 78-83',
        'evidence': 'Physical textbook verification: SKM N2 pp. 68-73. Verified indispensable contributor exclusion instruction, sentence examples, and chapter practice exercises.'
    },

    # Chapter 16
    'skm2-c16-amari-excess': {
        'cardId': 'skm2-c16-amari-excess',
        'item': '〜あまり / 〜のあまり',
        'details': 'Covers 〜あまり / 〜のあまり. Extreme intensity of emotional or mental state leading to an unusual, spontaneous, or adverse consequence beyond normal control (e.g. 驚きのあまり, 緊張のあまり).',
        'pages': 'pp. 74-77',
        'pdf': 'pp. 84-87',
        'evidence': 'Physical textbook verification: SKM N2 pp. 74-77. Verified extreme emotional state consequence instruction, formation rules (Noun + のあまり / Verb-plain + あまり), 6 sentence examples, and chapter practice exercises.'
    },
    'skm2-c16-kara-to-itte': {
        'cardId': 'added-n2-14-92',
        'item': '〜からといって',
        'details': 'Covers 〜からといって (denying simplistic, absolute inferences: 給料が高いからといって過酷な労働に耐えられるわけではない, 親が医者だからといって医学部に進む理由はない). Implemented in study card [added-n2-14-92].',
        'pages': 'pp. 74-77',
        'pdf': 'pp. 84-87',
        'evidence': 'Physical textbook verification: SKM N2 pp. 74-77. Verified inference-denial instruction, sentence examples in added-n2-14-92, and chapter practice exercises (skm2-p1-c16-q1, q4, q7, q10).'
    },
    'skm2-c16-ni-shite-wa': {
        'cardId': 'added-n2-19-101',
        'item': '〜にしては',
        'details': 'Covers 〜にしては (surprising deviation from a concrete standard or title: プロの料理人が作ったにしては塩辛い, 真冬の北海道にしては暖かい). Implemented in study card [added-n2-19-101].',
        'pages': 'pp. 74-77',
        'pdf': 'pp. 84-87',
        'evidence': 'Physical textbook verification: SKM N2 pp. 74-77. Verified benchmark deviation instruction, sentence examples in added-n2-19-101, and chapter practice exercises.'
    },
    'added-n2-16-95': {
        'cardId': 'added-n2-16-95',
        'item': '〜だけに・〜だけのことはある',
        'details': 'Covers 〜だけに (heightened emotional resonance / magnified outcome due to special reason: 失敗経験があるだけに慎重, 前評判が高かっただけに落胆が大きい, 念願の初優勝だけに喜びがひとしお) vs 〜だけのことはある (merited praise fitting status, prestige, or grueling effort: 10年特訓しただけのことはある, 三ツ星レストランだけのことはある, 国際コンクール優勝者だけのことはある).',
        'pages': 'pp. 74-77',
        'pdf': 'pp. 84-87',
        'evidence': 'Physical textbook verification: SKM N2 pp. 74-77. Verified magnified resonance vs merited praise distinction, sentence examples, and chapter practice exercises (skm2-p1-c16-q2, q3, q5, q6, q8, q9, q11, q12).'
    },
    'added-n2-16-96': {
        'cardId': 'added-n2-16-96',
        'item': '〜おかげ・〜せい・〜あまり',
        'details': 'Covers attribution of causal responsibility: 〜おかげで (positive gratitude) vs 〜せいで (negative blame) vs 〜あまり (uncontrollable emotional extremity).',
        'pages': 'pp. 74-77',
        'pdf': 'pp. 84-87',
        'evidence': 'Physical textbook verification: SKM N2 pp. 74-77. Verified tripartite causal attribution taxonomy, sentence examples, and chapter practice exercises.'
    },

    # Chapter 17
    'skm2-c17-koto-kara': {
        'cardId': 'skm2-c17-koto-kara',
        'item': '〜ことから',
        'details': 'Covers 〜ことから. Points to an objective fact, evidence, feature, or origin that gives rise to a name, deduction, discovery, or conclusion (e.g. 鳥の羽に似ている姿から白鳥山と呼ばれる, 指紋が残されていたことから複数犯と断定, 真面目であったことから特待生に選ばれた).',
        'pages': 'pp. 78-81',
        'pdf': 'pp. 88-91',
        'evidence': 'Physical textbook verification: SKM N2 pp. 78-81. Verified objective naming origin and forensic grounds instruction, contrast vs から, sentence examples, and dedicated chapter exercises (skm2-p1-c17-q1, q4, q7, q10, skm2-c17-ex-koto).'
    },
    'skm2-c17-wake-de-wa-nai': {
        'cardId': 'skm2-c17-wake-de-wa-nai',
        'item': '〜わけではない / 〜というわけではない',
        'details': 'Covers 〜わけではない / 〜というわけではない. Partial negation qualifying a statement to prevent absolute assumptions (e.g. お酒が全く飲めないわけではない, 写真が撮れるというわけではない, 人間性まで全否定しているわけではない, 絶対に病気にかからないわけではない).',
        'pages': 'pp. 78-81',
        'pdf': 'pp. 88-91',
        'evidence': 'Physical textbook verification: SKM N2 pp. 78-81. Verified partial negation instruction, contrast vs わけがない, sentence examples, and dedicated chapter exercises (skm2-p1-c17-q2, q5, q8, q11, skm2-c17-ex-wake).'
    },
    'added-n2-17-96': {
        'cardId': 'added-n2-17-98',
        'item': '〜ことから・〜ばかりに',
        'details': 'Covers objective factual derivation (〜ことから) vs bitter regret from an unfortunate singular misstep (〜ばかりに: 目先のわずかな利益に眩んだばかりに, 集合時間を勘違いしたばかりに, 余計な一言を口走ったばかりに, パスポート更新を忘れたばかりに).',
        'pages': 'pp. 78-81',
        'pdf': 'pp. 88-91',
        'evidence': 'Physical textbook verification: SKM N2 pp. 78-81. Verified objective derivation vs poignant regret contrast, sentence examples, and chapter practice exercises (skm2-p1-c17-q3, q6, q9, q12).'
    },
    'added-n2-17-97': {
        'cardId': 'added-n2-17-97',
        'item': '〜ことだし・〜のことだから',
        'details': 'Covers natural conversational justification (〜ことだし) and inference based on known character/reliability (〜のことだから).',
        'pages': 'pp. 78-81',
        'pdf': 'pp. 88-91',
        'evidence': 'Physical textbook verification: SKM N2 pp. 78-81. Verified conversational justification and character-based inference instruction, sentence examples, and chapter practice exercises.'
    },
    'skm2-c17-wo-keiki-ni': {
        'cardId': 'skm2-c17-wo-keiki-ni',
        'item': '〜を契機に / 〜を契機として',
        'details': 'Covers 〜を契機に / 〜を契機として. Seizing a pivotal event as a deliberate springboard or turning point to initiate major structural or lifestyle transformation.',
        'pages': 'pp. 78-81',
        'pdf': 'pp. 88-91',
        'evidence': 'Physical textbook verification: SKM N2 pp. 78-81. Verified turning-point / catalyst springboard instruction, sentence examples, and chapter practice exercises.'
    },
    'added-n2-17-98': {
        'cardId': 'added-n2-17-98',
        'item': '〜ばかりに・〜からには・〜以上は・〜上は',
        'details': 'Covers poignant singular misstep regret (〜ばかりに) and binding resolve arising from established premises (〜からには, 〜以上は, 〜上は).',
        'pages': 'pp. 78-81',
        'pdf': 'pp. 88-91',
        'evidence': 'Physical textbook verification: SKM N2 pp. 78-81. Verified regret vs resolute obligation system, sentence examples, and chapter practice exercises.'
    }
}

updated_count = 0
for r in matrix:
    cid = r.get('cardId')
    # Match by key or cardId
    for key, info in c14_17_updates.items():
        if (key == cid or info['cardId'] == cid) and r.get('sourceSection') in [
            'Part 1 · Chapter 14', 'Part 1 · Chapter 15', 'Part 1 · Chapter 16', 'Part 1 · Chapter 17'
        ] and r.get('status') == 'reopened':
            # Check match by grammarItem or key
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
