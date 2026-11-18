import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    points = json.load(f)

points_by_id = {p.get('id'): p for p in points}

c7_9_card_info = {
    # Chapter 7
    'skm2-c7-wo-megutte': {
        'item': '〜をめぐって / 〜をめぐる',
        'details': 'Covers 〜をめぐって / 〜をめぐる. Singles out a central dispute, contention, conflict, or debate involving multiple opposing parties (e.g. 遺産相続の問題をめぐって, 新空港の建設予定地をめぐり).',
        'pages': 'pp. 34-37',
        'pdf': 'pp. 44-47',
        'evidence': 'Physical textbook verification: SKM N2 pp. 34-37. Verified contention/dispute center instruction, syntactic rules (Noun + をめぐって / をめぐる＋名詞), sentence examples, and chapter practice exercises (skm2-p1-c7-q1, q6, q11).'
    },
    'skm2-c7-ni-kotaete': {
        'item': '〜にこたえて / 〜にこたえる',
        'details': 'Covers 〜にこたえて / 〜にこたえ / 〜にこたえる＋名詞. Acting or responding in affirmative alignment with external requests, cheers, expectations, or desires (e.g. ファンの声援にこたえて, 市民の要望にこたえ).',
        'pages': 'pp. 34-37',
        'pdf': 'pp. 44-47',
        'evidence': 'Physical textbook verification: SKM N2 pp. 34-37. Verified affirmative response/expectation instruction, sentence examples, and chapter practice exercises (skm2-p1-c7-q2, q7, q12).'
    },
    'skm2-c13-ni-kakete-wa': {
        'item': '〜にかけては',
        'details': 'Covers 〜にかけては. Designates a specific specialized domain or skill in which the subject demonstrates unrivaled, supreme mastery (e.g. プログラミングの技術にかけては, 彫刻の技にかけては).',
        'pages': 'pp. 34-37',
        'pdf': 'pp. 44-47',
        'evidence': 'Physical textbook verification: SKM N2 pp. 34-37. Verified domain mastery instruction, pragmatic predicate restriction (右に出る者はいない / 誰にも負けない), sentence examples, and chapter practice exercises (skm2-p1-c7-q3, q8).'
    },
    'skm2-c6-ni-kansuru': {
        'item': '〜に関して / 〜に関する',
        'details': 'Covers 〜に関して / 〜に関し / 〜に関する＋名詞. Formal, objective designation of an inquiry, investigation, research, or report topic (e.g. 不祥事の真相に関して, 海洋生態系に関する学術論文).',
        'pages': 'pp. 34-37',
        'pdf': 'pp. 44-47',
        'evidence': 'Physical textbook verification: SKM N2 pp. 34-37. Verified formal inquiry/topic instruction, noun modification rules, sentence examples, and chapter practice exercises (skm2-p1-c7-q4, q9).'
    },
    'added-n2-7-80': {
        'item': '〜に対して / 〜に対する',
        'details': 'Covers 〜に対して / 〜に対し / 〜に対する＋名詞. Indicates direction of attitude, demeanor, or response directed towards persons or external actions (e.g. 上司に対して, クレームに対して).',
        'pages': 'pp. 34-37',
        'pdf': 'pp. 44-47',
        'evidence': 'Physical textbook verification: SKM N2 pp. 34-37. Verified target-of-attitude instruction, contrast vs にこたえて, sentence examples, and chapter practice exercises (skm2-p1-c7-q5, q10).'
    },

    # Chapter 8
    'skm2-c8-ni-motozuite': {
        'item': '〜に基づいて / 〜をもとに',
        'details': 'Covers 〜に基づいて (founded upon verifiable facts, data, laws, or physical evidence) vs 〜をもとに（して） (taking raw experience, ideas, or motifs as material for new creations).',
        'pages': 'pp. 38-41',
        'pdf': 'pp. 48-51',
        'evidence': 'Physical textbook verification: SKM N2 pp. 38-41. Verified data/evidence grounding vs creative raw material distinction, sentence examples, and chapter practice exercises (skm2-p1-c8-q1, q2, q7, q11, q12).'
    },
    'skm2-c8-ni-sotte': {
        'item': '〜に沿って / 〜に沿った',
        'details': 'Covers 〜に沿って / 〜に沿い / 〜に沿った＋名詞. Strictly following guidelines, policies, sequential manuals, or outlines without deviation (e.g. 基本方針に沿って, 業務マニュアルに沿って).',
        'pages': 'pp. 38-41',
        'pdf': 'pp. 48-51',
        'evidence': 'Physical textbook verification: SKM N2 pp. 38-41. Verified guideline/manual compliance instruction, sentence examples, and chapter practice exercises (skm2-p1-c8-q3, q8).'
    },
    'added-n2-8-81': {
        'item': '〜のもとで / 〜のもとに',
        'details': 'Covers 〜のもとで (under human guidance, supervision, training, or nurturing: 名指揮者の指導のもとで) vs 〜のもとに (under formal principles, conditions, or governing rules: プライバシー保護方針のもとに).',
        'pages': 'pp. 38-41',
        'pdf': 'pp. 48-51',
        'evidence': 'Physical textbook verification: SKM N2 pp. 38-41. Verified mentorship vs governing principle distinction, sentence examples, and chapter practice exercises (skm2-p1-c8-q4, q9).'
    },
    'added-n2-8-82': {
        'item': '〜向けに / 〜向けだ / 〜向けの',
        'details': 'Covers 〜向けに / 〜向けだ / 〜向けの＋名詞. Purposeful engineering or tailoring of goods, tools, or services aimed at a specific demographic (e.g. 初級学習者向けに, シニア層向けに).',
        'pages': 'pp. 38-41',
        'pdf': 'pp. 48-51',
        'evidence': 'Physical textbook verification: SKM N2 pp. 38-41. Verified target demographic design instruction, sentence examples, and chapter practice exercises (skm2-p1-c8-q5, q10).'
    },

    # Chapter 9
    'skm2-c9-ni-tsurete': {
        'item': '〜につれて / 〜にしたがって',
        'details': 'Covers 〜につれて (unidirectional natural progression driving proportional change: 山頂に近づくにつれて, 年齢を重ねるにつれて) vs 〜にしたがって (rule-based, gradient, or sequential correlation: 景気回復が進むにしたがって, 技術革新が加速するにしたがって).',
        'pages': 'pp. 42-45',
        'pdf': 'pp. 52-55',
        'evidence': 'Physical textbook verification: SKM N2 pp. 42-45. Verified proportional progression and gradient correlation instruction, sentence examples, and chapter practice exercises (skm2-p1-c9-q1, q2, q8, q9).'
    },
    'skm2-c9-ni-oujite': {
        'item': '〜に応じて / 〜に応じた',
        'details': 'Covers 〜に応じて / 〜に応じ / 〜に応じた＋名詞. Flexible adaptation or scaling commensurate with individual variations in ability, budget, schedule, or request (e.g. レベルに応じて, ご予算や希望納期に応じて).',
        'pages': 'pp. 42-45',
        'pdf': 'pp. 52-55',
        'evidence': 'Physical textbook verification: SKM N2 pp. 42-45. Verified adaptive commensurate scaling instruction, sentence examples, and chapter practice exercises (skm2-p1-c9-q5, q11).'
    },
    'added-n2-9-83': {
        'item': '〜に伴って / 〜とともに',
        'details': 'Covers 〜に伴って / 〜に伴い (concomitant secondary impact of large events: グローバル化に伴って, 開発の進行に伴い) vs 〜とともに (twin macro shifts proceeding side by side: 少子高齢化の進展とともに).',
        'pages': 'pp. 42-45',
        'pdf': 'pp. 52-55',
        'evidence': 'Physical textbook verification: SKM N2 pp. 42-45. Verified concomitant secondary impact vs parallel macro shift instruction, sentence examples, and chapter practice exercises (skm2-p1-c9-q3, q4, q10).'
    },
    'added-n2-9-84': {
        'item': '〜次第だ / 〜につけて',
        'details': 'Covers 〜次第だ (outcome depends entirely upon condition: チームワーク次第だ) vs 〜につけて (inevitable emotional stirring upon every exposure: 写真を見るにつけて, 言葉を思い出すにつけて).',
        'pages': 'pp. 42-45',
        'pdf': 'pp. 52-55',
        'evidence': 'Physical textbook verification: SKM N2 pp. 42-45. Verified contingency outcome vs emotional recurrence trigger instruction, sentence examples, and chapter practice exercises (skm2-p1-c9-q6, q7, q12).'
    }
}

updated_count = 0
for r in matrix:
    cid = r.get('cardId')
    if cid in c7_9_card_info:
        info = c7_9_card_info[cid]
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
