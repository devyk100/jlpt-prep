import json

# 1. Update chapterExercises.json for Lesson 16 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l16-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l16-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 16',
        'type': 'multiple-choice',
        'context': 'Buying tea while abroad: You bought oolong tea in China after you had already arrived there.',
        'question': '中国に（　　）時、おいしい烏龍茶を買いました。',
        'translation': 'When I went to China (after arriving there), I bought delicious oolong tea.',
        'options': [
            '行った',
            '行く',
            '行っている',
            '行かない'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l16-toki-tense',
        'grammarPointTitle': '〜時（とき）の時制 (Tense Nuances in \'When\' Clauses: V-る時 vs V-た時)',
        'explanation': {
            'overall': 'In Genki II Lesson 16, relative tense in 時 clauses is governed by event completion: If action A has already occurred/finished at the time of main action B, Clause A takes the past short form (中国に行った時、お茶を買いました: arrived in China first, then bought tea).',
            'options': [
                {
                    'text': '行った',
                    'isCorrect': True,
                    'reason': 'Correct. Past short form: Action A (arriving in China) completed before B (buying tea).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '行く',
                    'isCorrect': False,
                    'reason': 'Incorrect. Present short form (行く時) means buying tea BEFORE leaving for China.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '行っている',
                    'isCorrect': False,
                    'reason': 'Incorrect. Explicit textbook constraint: 行っている describes prior arrival resultant state, not during-trip ongoing action.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '行かない',
                    'isCorrect': False,
                    'reason': 'Incorrect. Negative form contradicts the positive premise of buying tea in China.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Did the speaker arrive in China before or after buying the tea?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l16-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l16-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 16',
        'type': 'multiple-choice',
        'context': 'Doing a favor without a person case slot: Doing grocery shopping for your roommate Yui who was sick.',
        'question': '私は風邪を引いたゆい（　　）買い物に行ってあげました。',
        'translation': 'I went shopping for Yui, who had caught a cold.',
        'options': [
            'のために',
            'に',
            'を',
            'で'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-16-25',
        'grammarPointTitle': '〜てあげる・てくれる・てもらう',
        'explanation': {
            'overall': 'Genki II Lesson 16 (Footnote 1) explicitly specifies: When you want to add the idea of doing somebody a favor with a verb that does not have a syntactic slot for a person (such as 買い物に行く: to go shopping), use [Person] のために: ゆいのために買い物に行ってあげました.',
            'options': [
                {
                    'text': 'のために',
                    'isCorrect': True,
                    'reason': 'Correct. When main verb lacks a beneficiary person slot, use [Person] のために.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'に',
                    'isCorrect': False,
                    'reason': 'Incorrect. 買い物に行く does not take a person with particle に (*ゆいに買い物に行く is ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'を',
                    'isCorrect': False,
                    'reason': 'Incorrect. を marks direct objects, not the beneficiary of an intransitive motion verb.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'で',
                    'isCorrect': False,
                    'reason': 'Incorrect. で marks location or instrument.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'What phrase expresses "for the sake of [Person]" when the verb lacks a personal particle slot?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 16!')

# 2. Enrich base-reviewed.json for Lesson 16 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. added-g2-16-25 (~てあげる・てくれる・てもらう)
c = card_map.get('added-g2-16-25')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 16'
    c['nuance'] = (
        'Helping verbs あげる, くれる, and もらう following the te-form of a verb describe the giving and receiving of services and favors: '
        '(1) V-てあげる: Doing something as a favor for someone else. The beneficiary keeps whatever particle the main verb calls for (妹にお金を貸してあげた, 妹を駅に連れて行ってあげた). '
        'FOOTNOTE 1 RULE: If the main verb has no slot for a person (e.g. 買い物に行く, 掃除する), use [Person] のために (ゆいのために買い物に行ってあげました). '
        '(2) V-てくれる: Someone performs a favor for the speaker (or the speaker\'s in-group/family). Beneficiary is usually the speaker (友だちが宿題を手伝ってくれた; 親戚がりんごを送ってくれた). '
        '(3) V-てもらう: The beneficiary subject receives, arranges for, or persuades someone to do a favor: (beneficiary) は (benefactor) に [V-て] もらう (友だちに宿題を手伝ってもらいました). '
        'Can also simply acknowledge goodwill (知らない人に漢字を読んでもらいました).'
    )
    c['keyTakeaway'] = 'V-てあげる = do favor for others (use のために if verb lacks person slot). V-てくれる = someone does favor for me/my family. V-てもらう = subject receives favor from benefactor (に).'
    c['connection'] = 'V-て + あげる / くれる / もらう | [Person] のために V-てあげる'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 16, Grammar 1, printed pp. 96-98 (PDF pp. 104-106).'

# 2. added-g2-16-26 (~ていただけませんか)
c = card_map.get('added-g2-16-26')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 16'
    c['nuance'] = (
        'Three distinct politeness tiers for asking favors in Japanese: '
        '(1) V-ていただけませんか: Most polite and deferential. Derived from potential いただける (humble receiving). Standard and appropriate when making a request of professors, supervisors, superiors, or strangers (手伝っていただけませんか: Would you kindly lend me a hand?). '
        '(2) V-てくれませんか: Polite standard. Roughly equivalent to 〜てください. Standard in host-family or casual-polite interactions (待ってくれませんか). '
        '(3) V-てくれない？ / V-て: Casual. Appropriate with close peers and family (取ってくれない？ / 取って).'
    )
    c['keyTakeaway'] = 'Politeness hierarchy: V-ていただけませんか (most polite, for superiors/strangers) > V-てくれませんか (host family, peers in polite mode) > V-てくれない？ / V-て (casual peers).'
    c['connection'] = 'V-て + いただけませんか (superiors) | V-て + くれませんか (polite) | V-て + くれない？ (casual)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 16, Grammar 2, printed pp. 98-99 (PDF pp. 106-107).'

# 3. g2-l16-to-ii-hoping
c = card_map.get('g2-l16-to-ii-hoping')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 16'
    c['nuance'] = (
        '〜といい expresses hope for a favorable outcome: "I hope that [favorable event happens]". '
        'Formation: Attaches to the present tense short form of a predicate (affirmative or negative). '
        'SPEAKER VS LISTENER PRAGMATICS: '
        '(1) Hoping for oneself: Use 〜といいんですが or 〜といいんだけど (with explanatory/softening んですが) to politely express hope for oneself without sounding presumptuous (試験がやさしいといいんですが: I hope the exam will be easy). '
        '(2) Wishing for someone else: Use 〜といいですね or 〜といいね (friendly wish for the listener: いい仕事が見つかるといいですね: I hope you find a good job!).'
    )
    c['keyTakeaway'] = 'V(short present) + といい. Wishing for oneself: 〜といいんですが (softened). Wishing for listener: 〜といいですね (friendly encouragement).'
    c['connection'] = 'Short present + といいんですが (self) | Short present + といいですね (listener)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 16, Grammar 3, printed pp. 99-100 (PDF pp. 107-108).'

# 4. g2-l16-toki-tense
c = card_map.get('g2-l16-toki-tense')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 16'
    c['nuance'] = (
        'Relative tense in 時 (when) temporal clauses depends strictly on the chronological completion of Event A relative to Event B: '
        '(1) Clause A (present short) + 時、Clause B: Event B occurs BEFORE or DURING Event A (出かける時、鍵をかけました: Locked door BEFORE going out; 寝る時、電気を消します: Turn off light BEFORE going to sleep). '
        '(2) Clause A (past short) + 時、Clause B: Event A has ALREADY OCCURRED / is completed before Event B takes place (中国に行った時、お茶を買いました: Bought tea AFTER arriving in China; 疲れた時、お風呂に入ります: Take bath AFTER getting tired). '
        '(3) Ongoing background: If B occurs in the middle of ongoing action A, use V-ている時 (テレビを見ている時、電話がかかってきました). '
        '(4) Adjectives & Nouns: い-adj + 時 (寒い時); な-adj + な時 (元気な時 - keep な!); Noun + の時 (病気の時 - takes の!).'
    )
    c['keyTakeaway'] = 'Event order controls tense: V-る時 = B occurs BEFORE/during A (出かける時鍵をかける). V-た時 = A ALREADY HAPPENED before B (中国に行った時お茶を買う). な-adj takes な時, Nouns take の時.'
    c['connection'] = 'V-る時 (B happens before A) | V-た時 (A completed before B) | な-adj + な時 | Noun + の時'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 16, Grammar 4, printed pp. 100-102 (PDF pp. 108-110).'

# 5. added-g2-16-27 (~てすみません・なくてすみません)
c = card_map.get('added-g2-16-27')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 16'
    c['nuance'] = (
        'Apologizing for actions performed or neglected: '
        '(1) Apologizing for doing something: V-て + すみませんでした (汚い言葉を使って、すみませんでした: I am sorry for using bad language; 約束を忘れて、ごめん: Sorry I forgot our promise). '
        '(2) Apologizing for failing to do something: V-なくて + すみませんでした (take negative short form V-ない, drop final い, and add くて: 宿題を持ってこなくて、すみませんでした: Sorry for not bringing homework; 早く言わなくて、ごめん: Sorry for not telling you earlier). '
        'FOOTNOTE 8 TENSE NUANCE: すみませんでした (past) implies making a clean break from the mistake (e.g. after class: 遅刻してすみませんでした); すみません (present) is used when the problem is still ongoing (e.g. as you arrive at the classroom door: 遅刻してすみません).'
    )
    c['keyTakeaway'] = 'Apologizing for doing: V-て + すみませんでした. Apologizing for NOT doing: V-なくて + すみませんでした. Past すみませんでした = clean break; Present すみません = ongoing problem.'
    c['connection'] = 'V-て + すみませんでした / ごめん | V-なくて + すみませんでした / ごめん'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 16, Grammar 5, printed pp. 102-103 (PDF pp. 110-111).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 Lesson 16 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 16 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 16')]

l16_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 16',
        'exactPrintedPages': 'pp. 96-98',
        'exactPdfPages': 'pp. 104-106',
        'grammarItem': '〜てあげる・てくれる・てもらう (Benefactive Actions / Favors)',
        'instructionalDetails': 'V-てあげる for favors done for others (retains verb particle slot, or uses [Person] のために if no slot exists); V-てくれる for favors done for the speaker/in-group; V-てもらう for receiving/persuading favors (beneficiary は benefactor に V-てもらう); acknowledging goodwill.',
        'cardId': 'added-g2-16-25',
        'exampleCount': 4,
        'exampleIds': ['added-g2-16-25-example', 'added-g2-16-25::genki2-use-examples-37', 'added-g2-16-25::genki2-use-examples-38', 'added-g2-16-25::genki2-use-examples-39'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 96-98 (PDF pp. 104-106, p104_printed96.png, p105_printed97.png, p106_printed98.png). Verified benefactive action orientations, Footnote 1 のために rule, and grammatical case markings.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 16',
        'exactPrintedPages': 'pp. 98-99',
        'exactPdfPages': 'pp. 106-107',
        'grammarItem': '〜ていただけませんか (Polite Request Hierarchy)',
        'instructionalDetails': 'Politeness tiers for requests: V-ていただけませんか (most deferential, for professors, bosses, and strangers; derived from いただく) > V-てくれませんか (polite standard, roughly equal to 〜てください) > V-てくれない？ / V-て (casual peer request).',
        'cardId': 'added-g2-16-26',
        'exampleCount': 2,
        'exampleIds': ['added-g2-16-26-example', 'added-g2-16-26::genki2-use-examples-41'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 98-99 (PDF pp. 106-107, p106_printed98.png, p107_printed99.png). Verified three-tier politeness hierarchy, derivation from いただく, and social context applications.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 16',
        'exactPrintedPages': 'pp. 99-100',
        'exactPdfPages': 'pp. 107-108',
        'grammarItem': '〜といい (Hoping for Favorable Outcomes: I Hope That...)',
        'instructionalDetails': 'Present short form + といい; pragmatic differentiation: wishing for oneself takes 〜といいんですが (softened expectation); wishing for listener takes 〜といいですね (encouragement / friendly support).',
        'cardId': 'g2-l16-to-ii-hoping',
        'exampleCount': 3,
        'exampleIds': ['g2-l16-to-ii-hoping::s-g2-16-1', 'g2-l16-to-ii-hoping::genki2-use-examples-33', 'g2-l16-to-ii-hoping::genki2-use-examples-34'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 99-100 (PDF pp. 107-108, p107_printed99.png, p108_printed100.png). Verified present short form connection and speaker (〜といいんですが) vs listener (〜といいですね) pragmatics.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 16',
        'exactPrintedPages': 'pp. 100-102',
        'exactPdfPages': 'pp. 108-110',
        'grammarItem': '〜時（とき）の時制 (Tense Nuances in \'When\' Clauses: V-る時 vs V-た時)',
        'instructionalDetails': 'Relative completion controls tense: V-る時 when B occurs before/during A (出かける時鍵をかける); V-た時 when A is already completed before B occurs (中国に行った時お茶を買う); ongoing background with V-ている時; な-adj + な時; Noun + の時.',
        'cardId': 'g2-l16-toki-tense',
        'exampleCount': 3,
        'exampleIds': ['g2-l16-toki-tense::s-g2-16-2', 'g2-l16-toki-tense::genki2-use-examples-35', 'g2-l16-toki-tense::genki2-use-examples-36'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 100-102 (PDF pp. 108-110, p108_printed100.png, p109_printed101.png, p110_printed102.png). Verified relative tense mechanics, chronological diagrams, and adjectival/nominal connections.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 16',
        'exactPrintedPages': 'pp. 102-103',
        'exactPdfPages': 'pp. 110-111',
        'grammarItem': '〜てすみませんでした / 〜なくてすみませんでした (Apologies)',
        'instructionalDetails': 'V-て + すみませんでした for apologizing for actions taken; V-なくて + すみませんでした for apologizing for omissions/failures (drop い from ない and add くて); Footnote 8: past すみませんでした for clean break, present すみません for ongoing situation.',
        'cardId': 'added-g2-16-27',
        'exampleCount': 3,
        'exampleIds': ['added-g2-16-27-example', 'added-g2-16-27::genki2-use-examples-42', 'added-g2-16-27::genki2-use-examples-43'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 102-103 (PDF pp. 110-111, p110_printed102.png, p111_printed103.png). Verified affirmative and negative apology paradigms and Footnote 8 tense nuances.'
    }
]

matrix.extend(l16_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Successfully updated matrix! Total rows now: {len(matrix)}')
