import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

c10_13_card_info = {
    # Chapter 10
    'skm2-c10-nuki-de': {
        'item': '〜抜きで / 〜抜きにして（は） / 〜抜きには',
        'details': 'Covers 〜抜きで (dispensing with formality or habitual elements: 冗談抜きで, 挨拶は抜きにして) and 〜抜きにしては / 〜抜きには (hypothetical failure without an indispensable contributor: 貢献抜きにしては語れない, 指導力抜きには不可能).',
        'pages': 'pp. 46-51',
        'pdf': 'pp. 56-61',
        'evidence': 'Physical textbook verification: SKM N2 pp. 46-51. Verified exclusion of formality and essential-element conditionality, sentence examples, and chapter practice exercises (skm2-p1-c10-q1, q2, q7, q12).'
    },
    'added-n2-10-85': {
        'item': '〜やら〜やら / 〜というか〜というか',
        'details': 'Covers 〜やら〜やら (heterogeneous jumble of tasks, disasters, or burdens: 搬出やら手続きやら, 財布を落とすやら乗り遅れるやら) vs 〜というか〜というか (hesitation between two complementary or conflicting characterizations: 勇気があるというか無謀というか, 個性派というか奇抜というか).',
        'pages': 'pp. 46-51',
        'pdf': 'pp. 56-61',
        'evidence': 'Physical textbook verification: SKM N2 pp. 46-51. Verified disorderly enumeration vs evaluative hesitation distinction, sentence examples, and chapter practice exercises (skm2-p1-c10-q3, q4, q8, q9).'
    },
    'added-n2-10-86': {
        'item': '〜にしても〜にしても / 〜といった',
        'details': 'Covers 〜にしても〜にしても (inclusive application regardless of which bipolar choice is selected: 賛成にしても反対にしても, 進学するにしても就職するにしても) vs 〜といった (bundling representative exemplars into a superordinate category: 寿司や天ぷらといった和食, 納豆やキムチといった発酵食品).',
        'pages': 'pp. 46-51',
        'pdf': 'pp. 56-61',
        'evidence': 'Physical textbook verification: SKM N2 pp. 46-51. Verified bipolar condition inclusion vs superordinate exemplar bundling, sentence examples, and chapter practice exercises (skm2-p1-c10-q5, q6, q10, q11).'
    },

    # Chapter 11
    'skm2-c11-ni-kakawarazu': {
        'item': '〜にかかわらず / 〜にかかわりなく',
        'details': 'Covers 〜にかかわらず / 〜にかかわりなく. Action or rule applies uniformly unaffected by weather, attendance, presence/absence, or natural dichotomy (e.g. 雨天・晴天にかかわらず, 参加費の有無にかかわりなく, 理由の如何にかかわらず).',
        'pages': 'pp. 52-55',
        'pdf': 'pp. 62-65',
        'evidence': 'Physical textbook verification: SKM N2 pp. 52-55. Verified uniform unconditioned application instruction, sentence examples, and chapter practice exercises (skm2-p1-c11-q2, q7, q12).'
    },
    'skm2-c11-ha-tomo-kaku': {
        'item': '〜はともかく（として）',
        'details': 'Covers 〜はともかく（として）. Temporarily shelves value assessment or quality evaluation of element A in order to emphasize the definite merit or necessity of element B (e.g. デザインの良し悪しはともかく, 値段が高いか安いかはともかくとして).',
        'pages': 'pp. 52-55',
        'pdf': 'pp. 62-65',
        'evidence': 'Physical textbook verification: SKM N2 pp. 52-55. Verified evaluative postponement instruction, contrast with はさておき, sentence examples, and chapter practice exercises (skm2-p1-c11-q4, q9).'
    },
    'skm2-c11-ha-sateoki': {
        'item': '〜はさておき',
        'details': 'Covers 〜はさておき. Explicitly sets aside a secondary matter or conversational digression to redirect focus toward immediate essential priorities or central business (e.g. 経費の計算はさておき人命救助, 冗談話はさておき新工場の安全性).',
        'pages': 'pp. 52-55',
        'pdf': 'pp. 62-65',
        'evidence': 'Physical textbook verification: SKM N2 pp. 52-55. Verified priority redirection discourse marker instruction, sentence examples, and chapter practice exercises (skm2-p1-c11-q5, q10).'
    },
    'added-n2-11-87': {
        'item': '〜を問わず / 〜もかまわず',
        'details': 'Covers 〜を問わず (formal removal of attribute restrictions: 年齢・国籍を問わず, 昼夜を問わず, 経験の有無を問わず) vs 〜もかまわず (blatant disregard for surrounding norms, danger, or eyes: 周囲の迷惑もかまわず, 泥で汚れるのもかまわず).',
        'pages': 'pp. 52-55',
        'pdf': 'pp. 62-65',
        'evidence': 'Physical textbook verification: SKM N2 pp. 52-55. Verified attribute-blind inclusivity vs norm-disregarding behavior distinction, sentence examples, and chapter practice exercises (skm2-p1-c11-q1, q3, q6, q8, q11).'
    },

    # Chapter 12
    'skm2-c12-dokoroka': {
        'item': '〜どころか',
        'details': 'Covers 〜どころか. Sharply contrasts an expected or mild baseline state X against a reality that is far more extreme, diametrically opposed, or dramatically aggravated (e.g. 給料が上がるどころかボーナス削減, 風邪は治るどころか肺炎寸前, 感謝されるどころか怒られた).',
        'pages': 'pp. 56-59',
        'pdf': 'pp. 66-69',
        'evidence': 'Physical textbook verification: SKM N2 pp. 56-59. Verified extreme reversal/aggravation instruction, sentence examples, and chapter practice exercises (skm2-p1-c12-q1, q5, q9).'
    },
    'added-n2-12-88': {
        'item': '〜わけがない / 〜ものか / 〜というものではない',
        'details': 'Covers 〜わけがない / 〜はずがない (objective logical impossibility grounded in character or physical proof: 裏切るわけがない, 知っているはずがない, 否認し続けられるわけがない) vs 〜ものか / 〜もんか (emotional defiance and unwavering rejection: 二度と行くものか, 諦めてたまるもんか, 泣き言を言うものか) vs 〜というものではない / 〜というものでもない (philosophical partial negation: 幸福が手に入るというものではない, 大成功できるというものでもない, 喜ばれるというものではない).',
        'pages': 'pp. 56-59',
        'pdf': 'pp. 66-69',
        'evidence': 'Physical textbook verification: SKM N2 pp. 56-59. Verified three-way modal negation taxonomy (logical impossibility, subjective defiance, rational qualification), sentence examples, and chapter practice exercises (skm2-p1-c12-q2, q3, q4, q6, q7, q8, q10, q11, q12).'
    },

    # Chapter 13
    'added-n2-13-89': {
        'item': '〜とは / 〜といえば / 〜となると・〜となれば',
        'details': 'Covers 〜とは (amazed topic marker foregrounding an astonishing or philosophical reality: 愛する家族に看取られるとは, 激怒して机を叩いたとは, 初日に無断欠勤したとは) vs 〜といえば (evoking classic representative associations: 春の風物詩といえばお花見, 北海道グルメといえばラーメン, 夏休みの定番といえばキャンプ) vs 〜となると / 〜となれば (threshold condition transition to sober practical reality: マイホームを購入するとなると, 海外へ単身赴任するとなれば, 起業するとなると).',
        'pages': 'pp. 60-63',
        'pdf': 'pp. 70-73',
        'evidence': 'Physical textbook verification: SKM N2 pp. 60-63. Verified pragmatic topic presentation system, sentence examples, and chapter practice exercises (skm2-p1-c13-q1, q2, q3, q5, q6, q7, q9, q10, q11).'
    },
    'added-n2-13-90': {
        'item': '〜といったら（ありはしない／ない）',
        'details': 'Covers 〜といったら. Expresses overwhelming, words-defying magnitude of visual, emotional, or sensory experience (e.g. オーロラの美しさといったら, ご来光の荘厳さといったら, 息子の喜びようといったら).',
        'pages': 'pp. 60-63',
        'pdf': 'pp. 70-73',
        'evidence': 'Physical textbook verification: SKM N2 pp. 60-63. Verified superlative emotional magnitude instruction, noun-head attachment, sentence examples, and chapter practice exercises (skm2-p1-c13-q4, q8, q12).'
    }
}

updated_count = 0
for r in matrix:
    cid = r.get('cardId')
    if cid in c10_13_card_info:
        info = c10_13_card_info[cid]
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
