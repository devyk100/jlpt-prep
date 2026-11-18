import json

# 1. Update chapterExercises.json for Lesson 22 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l22-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l22-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 22',
        'type': 'multiple-choice',
        'context': 'Formal workplace request: Politely asking your manager for permission to take tomorrow off due to high fever.',
        'question': '熱があって体調が悪いため、明日仕事を（　　）いただけないでしょうか。',
        'translation': 'Because I have a fever and feel unwell, could you please allow me to take the day off tomorrow?',
        'options': [
            '休ませて',
            '休んで',
            '休まれて',
            '休ませられて'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-22-40',
        'grammarPointTitle': '使役・使役＋授受',
        'explanation': {
            'overall': 'To ask permission to do something humbly, combine the causative te-form with a request expression: V-させて + ください / いただけないでしょうか (休ませていただけないでしょうか: Could you please allow me to take off?). Simple 休んで asks the listener to take off, while 休まれて is passive.',
            'options': [
                {
                    'text': '休ませて',
                    'isCorrect': True,
                    'reason': 'Correct. Causative te-form 休ませて + いただけないでしょうか asks permission: "Could you please let me take off?".',
                    'trapCategory': 'formation'
                },
                {
                    'text': '休んで',
                    'isCorrect': False,
                    'reason': 'Incorrect. Simple 休んでいただけないでしょうか asks the boss to take time off, not the speaker.',
                    'trapCategory': 'register'
                },
                {
                    'text': '休まれて',
                    'isCorrect': False,
                    'reason': 'Incorrect. Passive 休まれて denotes receiving an action or suffering adversity, not asking permission.',
                    'trapCategory': 'voice'
                },
                {
                    'text': '休ませられて',
                    'isCorrect': False,
                    'reason': 'Incorrect. Causative-passive denotes being forced to rest against one\'s will.',
                    'trapCategory': 'voice'
                }
            ]
        },
        'hint': 'What verb form is used before いただけないでしょうか to politely ask permission for oneself: "please allow me to do"?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l22-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l22-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 22',
        'type': 'multiple-choice',
        'context': 'Study advice on memory retention: Warning that if you do not review vocabulary words every day, you will quickly forget them.',
        'question': '毎日新しい単語を復習（　　）、すぐに忘れてしまいますよ。',
        'translation': 'If you do not review new vocabulary every day, you will end up forgetting it right away.',
        'options': [
            'しなければ',
            'すれば',
            'しないなら',
            'しては'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l22-ba-conditional',
        'grammarPointTitle': '〜ば (The Hypothetical Conditional: If)',
        'explanation': {
            'overall': 'The negative conditional form of する using 〜ば is しなければ (derived by dropping -i from negative short form しない and adding -ければ).',
            'options': [
                {
                    'text': 'しなければ',
                    'isCorrect': True,
                    'reason': 'Correct. Negative conditional of する is しなければ ("if you do not do").',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'すれば',
                    'isCorrect': False,
                    'reason': 'Incorrect. すれば is affirmative ("if you do"), which contradicts the warning context.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'しないなら',
                    'isCorrect': False,
                    'reason': 'Incorrect. なら is a contextual topic conditional, less appropriate for general logical prerequisites.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': 'しては',
                    'isCorrect': False,
                    'reason': 'Incorrect. 〜ては expresses negative consequences of an action ("if you do..."), not the consequence of omission.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'How is the negative hypothetical conditional 〜ば formed from the verb する?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 22!')

# 2. Enrich base-reviewed.json for Lesson 22 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. added-g2-22-40 (使役・使役＋授受)
c = card_map.get('added-g2-22-40')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 22'
    c['nuance'] = (
        'Causative sentences (使役文 shieki-bun) describe who makes someone do something (coercion) or who lets someone do something (permission). '
        'CONJUGATION PARADIGM (p. 232): '
        '・Ru-verbs: drop final -ru, add -saseru (食べる → 食べさせる; 見る → 見させる). '
        '・U-verbs: drop final -u, add -aseru (行く → 行かせる; 待つ → 待たせる; 読む → 読ませる; 話す → 話させる). '
        '・Irregular verbs: くる → こさせる, する → させる. '
        'Causative verbs conjugate regularly as ru-verbs (食べさせた, 食べさせない, etc.). '
        'SENTENCE STRUCTURE & CASE MARKING: '
        '(1) Transitive verbs: [Director は] [Cast に] [Item を] V-causative. (To avoid double-wo, the cast is strictly marked with に: お母さんは子供に野菜を食べさせた: The mother made/let her child eat vegetables). '
        '(2) Intransitive verbs: [Director は] [Cast を / に] V-causative. (Cast takes を for coercive forced action: お父さんは子供を走らせた; Cast takes に for permissive action: お父さんは子供に行かせた). '
        'CAUSATIVE + BENEFACTIVE (pp. 233-234): '
        'Adding くれる / あげる unambiguously signals "let/allow": '
        '・[Director は] [Cast に] V-させてくれる (The director allows me to do). '
        '・Humble permission request: V-させてください / させていただけないでしょうか (Please allow me to do: 私に自己紹介をさせてください: Please let me introduce myself; 今日は早く帰らせてください: Please let me go home early today).'
    )
    c['keyTakeaway'] = 'Causative: Ru: -saseru, U: -aseru, くる→こさせる, する→させる. Dual meaning: make do (coercion) vs let do (permission). Transitive verbs: cast takes に (avoid double-wo). Permission request: V-させてください.'
    c['connection'] = 'Ru: -saseru | U: -aseru | [Director は] [Cast に] [Item を] V-causative | V-させてください'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 22, Grammar 1, printed pp. 232-234 (PDF pp. 240-242).'

# 2. added-g2-22-41 (~なさい)
c = card_map.get('added-g2-22-41')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 22'
    c['nuance'] = (
        'V(masu-stem) + なさい expresses a firm, authoritative command or directive ("do...!"). '
        'Formation: Attach なさい to the verb masu-stem (食べる → 食べなさい; 飲む → 飲みなさい; 勉強する → 勉強しなさい; 早く起きる → 早く起きなさい). '
        'SOCIOPRAGMATIC CONSTRAINTS (p. 234): '
        '・Implication: Speaking down from a position of authority. '
        '・Common usage domains: (1) Parents giving non-negotiable instructions to their children (野菜をちゃんと食べなさい: Eat your vegetables properly), (2) Teachers addressing school students, (3) Standard rubric instructions in written exam tests (次の文を読みなさい: Read the following sentence). '
        '・Strict prohibition: NEVER use toward equals, peers, or social superiors.'
    )
    c['keyTakeaway'] = 'V(masu-stem) + なさい: Firm, non-negotiable command ("do!"). Used by parents to children, teachers to students, or in written test instructions. Strictly prohibited toward superiors.'
    c['connection'] = 'V(masu-stem) + なさい'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 22, Grammar 2, printed p. 234 (PDF p. 242).'

# 3. g2-l22-ba-conditional (~ば)
c = card_map.get('g2-l22-ba-conditional')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 22'
    c['nuance'] = (
        'The conditional 〜ば establishes Clause A as a necessary prerequisite condition that naturally leads to consequence B ("If A, then B"). '
        'CONJUGATION PARADIGM (p. 235): '
        '・Affirmative verbs: Drop final -u, add -eba (食べる → 食べれば; 行く → 行けば; 待つ → 待てば; くる → くれば; する → すれば). '
        '・Negative verbs: Drop -i from ない, add -ければ (行かない → 行かなければ; 食べない → 食べなければ; しない → しなければ). '
        '・い-adjectives: Drop -i, add -ければ (高い → 高ければ; いい → よければ; 忙しくなければ). '
        '・な-adjectives & Nouns: Add なら / であれば (暇なら; 学生なら). '
        'SEMANTIC & PRAGMATIC CONSTRAINTS (p. 236): '
        '・Positive consequence implication: "A ば B" typically implies that fulfilling condition A ensures a good, desirable result ("If you do A, everything will be fine: この薬を飲めば大丈夫です; 先生に聞けばいいです"). '
        '・Advice pattern: Very commonly used in advice: V-ばいい (All you have to do is V). '
        '・Volition constraint: Like と, if clause A describes a volitional action, clause B generally cannot contain commands or requests (use 〜たら instead).'
    )
    c['keyTakeaway'] = 'Hypothetical conditional: Affirmative: V(u->eba). Negative: V-なければ. Adj: い->ければ, な->なら. Implies positive consequence ("If A, B will turn out well"). Advice: V-ばいい.'
    c['connection'] = 'V(u->eba) | V-なければ | い-adj(i->kereba) | な-adj/Noun + なら'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 22, Grammar 3, printed pp. 235-236 (PDF pp. 243-244).'

# 4. g2-l22-noni-frustration (~のに)
c = card_map.get('g2-l22-noni-frustration')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 22'
    c['nuance'] = (
        'Clause A + のに、Clause B connects two facts that hold true contrary to expectations: "Even though A, unexpectedly/frustratingly B" or "B, despite A". '
        'Unlike neutral けれども, 〜のに carries strong speaker emotion: disappointment, frustration, dissatisfaction, or surprise at an unfavorable outcome (徹夜で勉強したのに、試験が全然できませんでした: Even though I studied all night, I couldn\'t do well on the exam at all). '
        'FORMATION (Attached to Short Forms, pp. 236-237): '
        '・Verbs: Short form + のに (勉強したのに / 雨が降っているのに). '
        '・い-adjectives: Short form + のに (安いのに / 忙しいのに). '
        '・な-adjectives: な-adj + な + のに (静かなのに / 暇なのに; mandatory な!). '
        '・Nouns: Noun + な + のに (日曜日なのに / 学生なのに; mandatory な, identical to んだ/んです!). '
        'PRAGMATIC CONSTRAINTS: '
        'Clause B must describe an established fact; it CANNOT contain commands, invitations, or requests (*雨が降っているのに、傘を持っていきなさい is ungrammatical; must use けれども or が instead).'
    )
    c['keyTakeaway'] = '〜のに: Frustrated concession ("even though A, disappointingly B"). Formations: Verbs/い-adj short form + のに; な-adj + なのに; Noun + なのに (mandatory な!). Ban on commands/requests in B.'
    c['connection'] = 'Short form (+ な for な-adj/Noun) + のに、Clause B'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 22, Grammar 4, printed pp. 236-237 (PDF pp. 244-245).'

# 5. added-g2-22-42 (~のような・〜のように)
c = card_map.get('added-g2-22-42')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 22'
    c['nuance'] = (
        'Noun + のような and Noun + のように express resemblance, metaphor, or simile: "like / similar to / comparable to Noun" (pp. 237-238). '
        'FORMATION: '
        '(1) Adnominal (modifying a following Noun): '
        '・Noun A + のような + Noun B ("Noun B like Noun A") '
        '・メアリーさんは天使のような人です (Mary is a person like an angel). '
        '・トヨタのような大企業 (a large corporation like Toyota). '
        '(2) Adverbial (modifying a following Verb or Adjective): '
        '・Noun A + のように + Verb / Adjective ("verb or adj in the same way as Noun A") '
        '・魚のように上手に泳ぐ (swims skillfully like a fish). '
        '・孫悟空のように強い (strong like Goku). '
        '・雪のように白い (white like snow).'
    )
    c['keyTakeaway'] = 'Simile/Resemblance: Noun + のような + Noun (天使のような人 = angel-like person). Noun + のように + Verb/Adj (魚のように泳ぐ = swim like a fish; 雪のように白い = white like snow).'
    c['connection'] = 'Noun + のような + Noun | Noun + のように + Verb / Adjective'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 22, Grammar 5, printed pp. 237-238 (PDF pp. 245-246).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 Lesson 22 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 22 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 22')]

l22_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 22',
        'exactPrintedPages': 'pp. 232-234',
        'exactPdfPages': 'pp. 240-242',
        'grammarItem': '使役・使役＋授受 (Causative Sentences & Causative Benefactive)',
        'instructionalDetails': 'Ru: -saseru, U: -aseru, くる→こさせる, する→させる; dual meaning (make do vs let do); case marking: transitive cast strictly takes に to avoid double-wo; intransitive cast takes を (coercion) or に (permission); causative + くれる (let/allow); humble permission request V-させてください.',
        'cardId': 'added-g2-22-40',
        'exampleCount': 4,
        'exampleIds': ['added-g2-22-40-example', 'added-g2-22-40::genki2-use-examples-97', 'added-g2-22-40::genki2-use-examples-98', 'added-g2-22-40::genki2-use-examples-99'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 232-234 (PDF pp. 240-242, g2_p240_printed232.png to g2_p242_printed234.png). Verified causative conjugation paradigm, transitive double-wo avoidance rule, and causative + benefactive usage.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 22',
        'exactPrintedPages': 'p. 234',
        'exactPdfPages': 'p. 242',
        'grammarItem': '〜なさい (Firm Command / Directive)',
        'instructionalDetails': 'V(masu-stem) + なさい; authoritative non-negotiable instruction from parent to child, teacher to student, or written exam questions (読みなさい); strictly prohibited toward equals or superiors.',
        'cardId': 'added-g2-22-41',
        'exampleCount': 4,
        'exampleIds': ['added-g2-22-41-example', 'added-g2-22-41::genki2-use-examples-100', 'added-g2-22-41::genki2-use-examples-101', 'added-g2-22-41::genki2-use-examples-102'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 234 (PDF p. 242, g2_p242_printed234.png). Verified masu-stem connection, sociopragmatic hierarchy, and authoritative directive examples.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 22',
        'exactPrintedPages': 'pp. 235-236',
        'exactPdfPages': 'pp. 243-244',
        'grammarItem': '〜ば (The Hypothetical Conditional: If)',
        'instructionalDetails': 'Affirmative: drop -u, add -eba; negative: drop -i from ない, add -ければ; い-adj: drop -i, add -ければ; な-adj/Noun: + なら; prerequisite condition naturally leading to consequence; implies desirable outcome; advice formula V-ばいい; prohibition on requests/commands in B when A is volitional.',
        'cardId': 'g2-l22-ba-conditional',
        'exampleCount': 3,
        'exampleIds': ['g2-l22-ba-conditional::s-g2-22-1', 'g2-l22-ba-conditional::genki2-use-examples-103', 'g2-l22-ba-conditional::genki2-use-examples-104'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 235-236 (PDF pp. 243-244, g2_p243_printed235.png, g2_p244_printed236.png). Verified conditional conjugation rules, positive consequence nuance, and contrast with たら.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 22',
        'exactPrintedPages': 'pp. 236-237',
        'exactPdfPages': 'pp. 244-245',
        'grammarItem': '〜のに (Frustrated Concession: Even Though / In Spite Of)',
        'instructionalDetails': 'Connects two facts holding contrary to expectation with emotion of disappointment/frustration; short forms + のに; mandatory な insertion on な-adjectives and nouns (好きなのに, 日曜日なのに); prohibition against commands or requests in clause B.',
        'cardId': 'g2-l22-noni-frustration',
        'exampleCount': 3,
        'exampleIds': ['g2-l22-noni-frustration::s-g2-22-2', 'g2-l22-noni-frustration::genki2-use-examples-105', 'g2-l22-noni-frustration::genki2-use-examples-106'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 236-237 (PDF pp. 244-245, g2_p244_printed236.png, g2_p245_printed237.png). Verified emotional concession semantics, mandatory な insertion rule on nouns/な-adj, and clause B constraint.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 22',
        'exactPrintedPages': 'pp. 237-238',
        'exactPdfPages': 'pp. 245-246',
        'grammarItem': '〜のような・〜のように (Resemblance / Simile: Like / As If)',
        'instructionalDetails': 'Noun A + のような + Noun B (adnominal simile: 天使のような人); Noun A + のように + Verb/Adjective (adverbial simile: 魚のように泳ぐ, 悟空のように強い); denotes metaphorical or physical resemblance.',
        'cardId': 'added-g2-22-42',
        'exampleCount': 4,
        'exampleIds': ['added-g2-22-42-example', 'added-g2-22-42::genki2-use-examples-107', 'added-g2-22-42::genki2-use-examples-108', 'added-g2-22-42::genki2-use-examples-109'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 237-238 (PDF pp. 245-246, g2_p245_printed237.png, g2_p246_printed238.png). Verified noun modification with のような and verb/adjective modification with のように.'
    }
]

matrix.extend(l22_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified Lesson 22 in source coverage matrix! Total certified rows: {len(matrix)}')
