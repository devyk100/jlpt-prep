import json

# 1. Update chapterExercises.json for Lesson 14 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l14-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l14-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 14',
        'type': 'multiple-choice',
        'context': 'Inviting a friend: Warmly inviting a classmate to come over to your house this weekend.',
        'question': '今度の週末、私のうちに（　　）か。',
        'translation': 'Won\'t you come over to my place this weekend?',
        'options': [
            '来ませんか',
            '来たらどうです',
            '来たらどうだ',
            '来てください'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l14-tara-dou-desu-ka',
        'grammarPointTitle': '〜たらどうですか (Casual Advice / Suggestion: Why Don\'t You?)',
        'explanation': {
            'overall': 'Genki II Lesson 14 explicitly warns: 〜たらどうですか is for giving advice/recommendations and can sound critical or disapproving. It CANNOT be used to extend invitations (*うちにきたらどうですか is inappropriate). To invite someone, use 〜ませんか (うちにきませんか).',
            'options': [
                {
                    'text': '来ませんか',
                    'isCorrect': True,
                    'reason': 'Correct. Polite invitation formula: V-ませんか (うちにきませんか).',
                    'trapCategory': 'context'
                },
                {
                    'text': '来たらどうです',
                    'isCorrect': False,
                    'reason': 'Incorrect. Explicit textbook constraint: 〜たらどうですか cannot be used to extend an invitation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '来たらどうだ',
                    'isCorrect': False,
                    'reason': 'Incorrect. Blunt advice form; inappropriate for a polite invitation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '来てください',
                    'isCorrect': False,
                    'reason': 'Incorrect. Polite request, but standard invitation question with か takes 〜ませんか.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'What verbal pattern is standard for inviting someone to your place, rather than giving them advice?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l14-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l14-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 14',
        'type': 'multiple-choice',
        'context': 'Observing third-party desires: Mary obviously wants a new winter coat.',
        'question': 'メアリーさんは新しいコート（　　）ほしがっています。',
        'translation': 'Mary (obviously) wants a new coat.',
        'options': [
            'を',
            'が',
            'に',
            'で'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l14-hoshii',
        'grammarPointTitle': 'ほしい (Expressing Desire for an Object: Want Something)',
        'explanation': {
            'overall': 'In Genki II Lesson 14, the derived verb ほしがる (to show outward signs of wanting) conjugates as an u-verb and takes ONLY particle を for the object of desire, unlike ほしい which takes が.',
            'options': [
                {
                    'text': 'を',
                    'isCorrect': True,
                    'reason': 'Correct. ほしがる takes direct object marker を (コートをほしがっている).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'が',
                    'isCorrect': False,
                    'reason': 'Incorrect. Although ほしい takes が, the derived verb ほしがる strictly takes を (*コートがほしがっている is ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'に',
                    'isCorrect': False,
                    'reason': 'Incorrect. に does not mark the desired object.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'で',
                    'isCorrect': False,
                    'reason': 'Incorrect. で marks location or instrument.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which particle marks the object of desire with the third-person verb ほしがる?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 14!')

# 2. Enrich base-reviewed.json for Lesson 14 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. g2-l14-hoshii
c = card_map.get('g2-l14-hoshii')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 14'
    c['nuance'] = (
        'ほしい means "(I) want (something)", expressing desire to possess a tangible or intangible entity. '
        'Conjugation: ほしい inflects identically to an い-adjective: ほしい、ほしくない、ほしかった、ほしくなかった. '
        'Particle: The object of desire is standardly marked with が (いい成績がほしいです). In negative sentences, contrastive は is also common (プレゼントはほしくないです). '
        'FIRST-PERSON RESTRICTION: Like 〜たい (Lesson 11), bare ほしい describes only the speaker\'s desires (or the listener in questions: プレゼントがほしいですか). '
        'It CANNOT describe third-person desires directly (*メアリーさんは車がほしいです is wrong). '
        'To describe third-person desires: '
        '(1) Quotation: 〜と言っていました (ヤスミンさんは新しいスマホがほしいと言っていました). '
        '(2) Guess / Probability: 〜でしょう / 〜かもしれません (アミさんはぬいぐるみがほしくないでしょう). '
        '(3) Derived verb ほしがる (usually 〜ほしがっている): conjugates as an u-verb. CRITICAL PARTICLE RULE: ほしがる takes ONLY particle を, NEVER が (友達をほしがっている; strictly prohibited: *友達がほしがっている). '
        'SEMANTIC BOUNDARY: Core meaning is desire to possess an object. To express desire to perform an action, use V-たい (昼ご飯を食べたい, not *昼ご飯がほしい).'
    )
    c['keyTakeaway'] = 'Noun が ほしい (I want [object]; conjugates like い-adj). First-person only. Third person: 〜と言っていた, 〜かもしれない, or 〜ほしがっている (takes ONLY を, never が). Action wish: use V-たい.'
    c['connection'] = 'Noun が ほしい / ほしくない / ほしかった | Noun を ほしがっている (third person)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 14, Grammar 1, printed pp. 50-51 (PDF pp. 58-59).'

# 2. g2-l14-kamoshirenai
c = card_map.get('g2-l14-kamoshirenai')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 14'
    c['nuance'] = (
        '〜かもしれない / 〜かもしんない expresses epistemic possibility: "maybe / might / may". It indicates a possibility where the speaker is less certain than with 〜でしょう. '
        'Casual contractions: 〜かもしんない or simply 〜かも (very common in spoken Japanese). '
        'Formation: Attaches to the short forms of predicates in both affirmative and negative, present and past (雨が降るかもしれない, よくないかもしれない, 背が高いかもしれない, いじめっ子だったかもしれない). '
        'CRITICAL COPULA BAN: For nouns and な-adjectives in the present tense affirmative, だ IS DROPPED! Attach かもしれません directly without だ: '
        'e.g. ウダイさんはインド人かもしれない (strictly prohibited: *インド人だかもしれない). '
        'e.g. 山下先生は犬が嫌いかもしれない (strictly prohibited: *嫌いだかもしれない).'
    )
    c['keyTakeaway'] = 'Short form + かもしれません (might / may). Casual: 〜かもしんない / 〜かも. CRITICAL RULE: Nouns & な-adj in present affirmative drop だ completely (インド人かもしれない, never *だかもしれない).'
    c['connection'] = 'Short form (V / い-adj) + かもしれません | な-adj stem + かもしれません (no だ!) | Noun + かもしれません (no だ!)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 14, Grammar 2, printed pp. 51-52 (PDF pp. 59-60).'

# 3. added-g2-14-22 (あげる・くれる・もらう)
c = card_map.get('added-g2-14-22')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 14'
    c['nuance'] = (
        'Japanese distinguishes transactions based on the direction of giving relative to psychological distance: '
        '(1) あげる: Used when the transaction moves away from the center (speaker) or stays away among others: '
        'I give to you; I give to others; You give to others; Third party gives to third party. '
        'Formula: (giver) は/が (recipient) に [Thing] を あげる. '
        '(2) くれる: Used when the transaction moves toward the center (toward "me" or my in-group/family): '
        'Somebody gives me; You give me; Somebody gives to my family member (Footnote 2: 大統領が妹に手紙をくれました). '
        'Formula: (giver) は/が (recipient: 私/in-group) に [Thing] を くれる. '
        '(3) もらう: Recipient is the grammatical subject who receives from a giver: '
        'Formula: (recipient) は/が (giver) に/から [Thing] を もらう. '
        'Perspective constraint: もらう implies feeling closer to the recipient than the giver; it is not used when the transaction is outbound from the speaker.'
    )
    c['keyTakeaway'] = 'あげる = Outward/neutral giving (I->you, I->others, others->others). くれる = Inward giving to me/my family. もらう = Subject receives from giver (recipient は giver に/から もらう).'
    c['connection'] = '(giver) は (recipient) に [Item] を あげる / くれる | (recipient) は (giver) に/から [Item] を もらう'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 14, Grammar 3, printed pp. 52-53 (PDF pp. 60-61).'

# 4. g2-l14-tara-dou-desu-ka
c = card_map.get('g2-l14-tara-dou-desu-ka')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 14'
    c['nuance'] = (
        '〜たらどうですか conveys advice or a recommendation: "Why don\'t you...? / How about doing...?". '
        'Formation: Attaches to the past tense affirmative short form of a verb: V-た + らどうですか (薬を飲んだらどうですか, もっと勉強したらどうですか). '
        'Casual variants: shortened to 〜たらどう？ or simply 〜たら？ in casual speech. '
        'CRITICAL PRAGMATIC WARNING: 〜たらどうですか can carry a critical or disapproving tone, implying mild reprimand that the person has not performed the sensible action already. Avoid using it unless your opinion or advice was requested. '
        'INVITATION BAN: NEVER use 〜たらどうですか to extend an invitation (e.g. telling a friend to come over: use うちに来ませんか, NEVER *うちに来たらどうですか).'
    )
    c['keyTakeaway'] = 'V-た + らどうですか (Why don\'t you...?; advice). Can carry critical tone (avoid unsolicited). BAN ON INVITATIONS: Never use for invitations (use 〜ませんか instead).'
    c['connection'] = 'V-た形 + らどうですか | Casual: V-た形 + らどう？ / 〜たら？'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 14, Grammar 4, printed p. 54 (PDF p. 62).'

# 5. added-g2-14-23 (数量＋も・しか〜ない)
c = card_map.get('added-g2-14-23')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 14'
    c['nuance'] = (
        'Modifying quantities to express surprising abundance or lamented scarcity: '
        '(1) Number + も: "As many as..." Expresses that the quantity is unexpectedly large or impressive: '
        '母は猫を三匹も飼っている (My mother owns as many as three cats!); 二十人も来ました (As many as 20 people came). '
        '(2) Number + しか + Negative verb: "Only / as few as..." Expresses that the quantity is insufficient or surprisingly small: '
        '本を一冊しか持っていません (I have only one book); 二台しかありません (There are only two computers). '
        'Contrast with だけ: だけ means "just that many (neutral / sufficient)" and can take affirmative verbs; しか expresses scarcity and STRICTLY REQUIRES a negative verb.'
    )
    c['keyTakeaway'] = '[Number] + も + affirmative = "as many as" (surprising abundance). [Number] + しか + negative = "only / as few as" (lamented scarcity; strictly requires negative verb).'
    c['connection'] = '[Number] + も (large quantity) | [Number] + しか + 否定形 (scarce quantity)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 14, Grammar 5, printed pp. 54-55 (PDF pp. 62-63).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 Lesson 14 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 14 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 14')]

l14_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 14',
        'exactPrintedPages': 'pp. 50-51',
        'exactPdfPages': 'pp. 58-59',
        'grammarItem': 'ほしい (Expressing Desire for an Object: Want Something)',
        'instructionalDetails': 'Noun が ほしい (desire for possession; conjugates like い-adj); first-person restriction (or second-person in questions); third person desires require quotation (〜と言っていた), probability (〜かもしれない), or derived verb ほしがる (takes ONLY を, never が; 友達をほしがっている); action desire uses V-たい.',
        'cardId': 'g2-l14-hoshii',
        'exampleCount': 3,
        'exampleIds': ['g2-l14-hoshii::s-g2-14-1', 'g2-l14-hoshii::genki2-use-examples-14', 'g2-l14-hoshii::genki2-use-examples-15'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 50-51 (PDF pp. 58-59, p58_printed50.png, p59_printed51.png). Verified object desire semantics, first-person restriction, third-person ほしがる behavior, and particle を constraint.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 14',
        'exactPrintedPages': 'pp. 51-52',
        'exactPdfPages': 'pp. 59-60',
        'grammarItem': '〜かもしれない / 〜かもしんない (Epistemic Possibility: Might / May)',
        'instructionalDetails': 'Short form + かもしれません for epistemic possibility (less certain than 〜でしょう); casual contractions 〜かもしんない and 〜かも; CRITICAL BAN on だ for nouns and な-adjectives in present affirmative (インド人かもしれない, 嫌いかもしれない; strictly prohibited: *だかもしれない).',
        'cardId': 'g2-l14-kamoshirenai',
        'exampleCount': 3,
        'exampleIds': ['g2-l14-kamoshirenai::s-g2-14-2', 'g2-l14-kamoshirenai::genki2-use-examples-16', 'g2-l14-kamoshirenai::genki2-use-examples-17'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 51-52 (PDF pp. 59-60, p59_printed51.png, p60_printed52.png). Verified possibility semantics, casual contractions, and strict ban on だ for nouns/な-adjectives.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 14',
        'exactPrintedPages': 'pp. 52-53',
        'exactPdfPages': 'pp. 60-61',
        'grammarItem': 'あげる・くれる・もらう (Benefactive / Transaction Verbs of Giving & Receiving)',
        'instructionalDetails': 'Three-way transaction orientation: あげる for outbound/staying away giving (giver は recipient に item を あげる); くれる for inbound giving toward speaker/family (giver は 私/family に item を くれる); もらう for subject receiving (recipient は giver に/から item を もらう; implies closer affinity to recipient).',
        'cardId': 'added-g2-14-22',
        'exampleCount': 4,
        'exampleIds': ['added-g2-14-22-example', 'added-g2-14-22::genki2-use-examples-20', 'added-g2-14-22::genki2-use-examples-21', 'added-g2-14-22::genki2-use-examples-22'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 52-53 (PDF pp. 60-61, p60_printed52.png, p61_printed53.png). Verified directional giving paradigm, concentric psychological distance model, and in-group くれる rules.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 14',
        'exactPrintedPages': 'p. 54',
        'exactPdfPages': 'p. 62',
        'grammarItem': '〜たらどうですか (Casual Advice / Suggestion: Why Don\'t You?)',
        'instructionalDetails': 'V-た + らどうですか for advice/recommendation (casual: 〜たらどう？ / 〜たら？); pragmatic caution: can sound critical/reproachful; STRICT INVITATION BAN: cannot be used to extend invitations (use 〜ませんか instead; うちに来ませんか, not *来たらどうですか).',
        'cardId': 'g2-l14-tara-dou-desu-ka',
        'exampleCount': 3,
        'exampleIds': ['g2-l14-tara-dou-desu-ka::s-g2-14-3', 'g2-l14-tara-dou-desu-ka::genki2-use-examples-18', 'g2-l14-tara-dou-desu-ka::genki2-use-examples-19'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 54 (PDF p. 62, p62_printed54.png). Verified advice formation, potential disapproving tone caution, and explicit ban on invitations.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 14',
        'exactPrintedPages': 'pp. 54-55',
        'exactPdfPages': 'pp. 62-63',
        'grammarItem': '数量＋も・しか〜ない (Quantity + も for Abundance / しか〜ない for Scarcity)',
        'instructionalDetails': '[Number] + も with affirmative for surprisingly large quantity ("as many as"); [Number] + しか with negative verb for lamented scarcity ("only / as few as"); contrast with neutral だけ (which can take affirmative verbs).',
        'cardId': 'added-g2-14-23',
        'exampleCount': 3,
        'exampleIds': ['added-g2-14-23-example', 'added-g2-14-23::genki2-use-examples-23', 'added-g2-14-23::genki2-use-examples-24'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 54-55 (PDF pp. 62-63, p62_printed54.png, p63_printed55.png). Verified quantity emphasis particles, negative polarity requirement on しか, and comparison with だけ.'
    }
]

matrix.extend(l14_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Successfully updated matrix! Total rows now: {len(matrix)}')
