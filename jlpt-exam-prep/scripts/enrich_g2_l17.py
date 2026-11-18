import json

# 1. Update chapterExercises.json for Lesson 17 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l17-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l17-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 17',
        'type': 'multiple-choice',
        'context': 'Drawing an impression from observation: That person looks hungry based on how they are acting.',
        'question': 'あの人はお腹が空いている（　　）。',
        'translation': 'It looks like that person is hungry.',
        'options': [
            'みたいです',
            'そうです',
            'らしいです',
            'ようです'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-17-28',
        'grammarPointTitle': '〜って・みたいです',
        'explanation': {
            'overall': 'In Genki II Lesson 17, 〜みたいです follows a short-form verb to express that something appears to be the case based on direct sensory impressions (お腹が空いているみたいです).',
            'options': [
                {
                    'text': 'みたいです',
                    'isCorrect': True,
                    'reason': 'Correct. Verb short form + みたいです: "It appears that / looks like...".',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'そうです',
                    'isCorrect': False,
                    'reason': 'Incorrect. Attaching そうです directly to the short form (空いているそうです) means hearsay ("I hear they are hungry"), not an observed appearance.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'らしいです',
                    'isCorrect': False,
                    'reason': 'Incorrect. らしい conveys hearsay/conjecture from external reports, not standard Genki II grammar here.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'ようです',
                    'isCorrect': False,
                    'reason': 'Incorrect. Formal literary counterpart introduced in later levels.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which casual colloquial expression attaches to verbs to mean "it appears that / looks like..." based on impression?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l17-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l17-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 17',
        'type': 'multiple-choice',
        'context': 'Temporal sequence before past action: Studying Japanese for one semester before coming to Japan.',
        'question': '日本へ（　　）前に、一学期日本語を勉強しました。',
        'translation': 'Before I came to Japan, I studied Japanese for one semester.',
        'options': [
            '来る',
            '来た',
            '来て',
            '来ない'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-17-29',
        'grammarPointTitle': '〜前に・〜てから',
        'explanation': {
            'overall': 'In Genki II Lesson 17, the verb preceding 前に is ALWAYS in the present short form (V-る前に), regardless of whether the overall sentence predicate is in the past tense or present tense (日本へ来る前に、勉強しました; NEVER *来た前に).',
            'options': [
                {
                    'text': '来る',
                    'isCorrect': True,
                    'reason': 'Correct. The verb before 前に is strictly in the present dictionary form (来る前に).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '来た',
                    'isCorrect': False,
                    'reason': 'Incorrect. Explicit textbook constraint: Never use past short form before 前に (*来た前に is strictly ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '来て',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form pairs with から (来てから = after coming), not 前に.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '来ない',
                    'isCorrect': False,
                    'reason': 'Incorrect. Negative form contradicts the positive meaning.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'What tense form must a verb take before 前に, even if the main sentence is in the past?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 17!')

# 2. Enrich base-reviewed.json for Lesson 17 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. g2-l17-hearsay-sou-desu
c = card_map.get('g2-l17-hearsay-sou-desu')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 17'
    c['nuance'] = (
        '〜そうです presents a hearsay report quoting information heard from others ("I heard that... / reportedly..."). '
        'CONTRAST WITH LESSON 13 〜そうです (Conjectural Appearance): '
        '(1) Lesson 13 appearance: attaches to bare adjective stems (おいしそう, 元気そう, いい→よさそう) and verb stems (降りそう). '
        '(2) Lesson 17 hearsay: attaches to COMPLETE SHORT FORM PREDICATES in affirmative/negative, present/past (話すそうです, 寒かったそうです). '
        'MANDATORY だ RULE: For な-adjectives and Nouns in present affirmative, mandatory だ MUST precede そうです (親切だそうです: I hear they are kind; 学生だそうです: I hear they are students! NEVER *親切そうです which means "looks kind"). '
        'INVARIANCE (Footnote 1): Hearsay そうです is robustly invariant; only 〜そうです and casual 〜そうだ are used (never *そうじゃありません or *そうでした). '
        'SOURCE MARKER: Preface with [Source] によると to specify the information source (天気予報によると: according to the weather forecast).'
    )
    c['keyTakeaway'] = 'Short form + そうです = Hearsay ("I heard that..."). Invariant ending. MANDATORY: な-adj & Nouns take だそうです (親切だそうです; never bare stem). Source: [Source] によると.'
    c['connection'] = 'Short form (V / い-adj) + そうです | な-adj + だそうです | Noun + だそうです | [Source] によると'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 17, Grammar 1, printed pp. 118-119 (PDF pp. 126-127).'

# 2. added-g2-17-28 (~って・みたいです)
c = card_map.get('added-g2-17-28')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 17'
    c['nuance'] = (
        'This grammar point covers informal quotation 〜って and resemblance/inference 〜みたいです: '
        '(1) 〜って: The informal conversational counterpart of quotation particle と and hearsay そうです ("they say / she said..."). '
        'Follows short forms directly (メアリーさんは今日忙しいって; 明日試験があるって). Also replaces と before speech verbs (〜って言っていました). '
        '(2) 〜みたいです: '
        '- Resemblance to Noun: Noun + みたいです ("looks/acts like [Noun]"; 私の父はカーネル・サンダースみたいです: My dad looks like Colonel Sanders). '
        '- Inference from Observation: Verb(short form) + みたいです ("appears to be the case / looks like"; 雨が降ったみたいです: It looks like it rained; 空いているみたいです: Looks like they are hungry). '
        'Inflects like a な-adjective (みたいだ、みたいです、みたいなNoun、みたいにVerb).'
    )
    c['keyTakeaway'] = '〜って = Casual quote/hearsay (busyって, 行くって言ってた). 〜みたいです = Resemblance to noun (Nounみたい) or inference from observation (V-shortみたいです: looks like it rained).'
    c['connection'] = 'Short form + って | Noun + みたいです | V-short form + みたいです'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 17, Grammar 2 & 4, printed pp. 119, 122-123 (PDF pp. 127, 130-131).'

# 3. g2-l17-tara-conditional
c = card_map.get('g2-l17-tara-conditional')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 17'
    c['nuance'] = (
        'A たら B refers to conditional dependence: Event B is realized if and when the condition in A is met. '
        'Formation: Initial た comes from the past short form of predicates: '
        'Verbs: V-た + ら (行ったら, 食べたら; negative: 行かなかったら). '
        'い-adjectives: い → かったら (寒かったら; negative: 寒くなかったら). '
        'な-adjectives & Nouns: stem + だったら (静かだったら, 学生だったら; negative: 静かじゃなかったら). '
        'SEMANTIC MODES: '
        '(1) Open condition & consequence: If A occurs, B follows (山下先生に会ったら聞きます). '
        '(2) Temporal certainty ("once / when"): When A is virtually certain, arranges sequence in time: "Once A is done, let\'s do B" (宿題が終わったら、遊びに行きましょう). '
        '(3) Counterfactual hypothetical: Unreal condition contrary to fact (私が猫だったら、一日中寝ているのに: If I were a cat, I\'d sleep all day). '
        'CHRONOLOGICAL RESTRICTION: In A たら B, B CANNOT occur before A! B takes place at the time A comes true or later. '
        'NATURAL DEPENDENCY (Footnote 6): A たら B describes natural cause-consequence; it CANNOT express "even if A, B" (for "even if", use 〜ても).'
    )
    c['keyTakeaway'] = 'Past short form + ら (V-たら, かったら, だったら). Means: "if" (open), "once / when" (temporal sequence), or "if ... were" (counterfactual). B cannot happen before A.'
    c['connection'] = 'V-た + ら | い-adj (drop い) + かったら | な-adj / Noun + だったら | Negative: 〜なかったら'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 17, Grammar 3, printed pp. 119-121 (PDF pp. 127-129).'

# 4. g2-l17-nakute-mo-ii
c = card_map.get('g2-l17-nakute-mo-ii')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 17'
    c['nuance'] = (
        '〜なくてもいいです describes lack of obligation: "you do not have to / you do not need to do X". '
        'Formation: Take negative short form V-ない, drop final い, and add くていいです (V-なくてもいいです). '
        'Examples: 靴を脱がなくてもいいです (You do not need to take off your shoes); プレゼントは高くなくてもいいです (The present does not need to be expensive). '
        'Casual variants: Omit です for casual speech (〜なくてもいい), or omit も for spoken casual (〜なくていい: 来なくていいよ: You don\'t need to come).'
    )
    c['keyTakeaway'] = 'V-ない (drop い) + くて + もいいです = "do not have to / need not do". Casual: 〜なくてもいい / 〜なくていい. Describes absence of obligation.'
    c['connection'] = 'V-ない (drop い) + くてもいいです / くてもいい / なくていい'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 17, Grammar 3, printed p. 121 (PDF p. 129).'

# 5. added-g2-17-29 (~前に・〜てから)
c = card_map.get('added-g2-17-29')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 17'
    c['nuance'] = (
        'Expressing chronological temporal sequence between two events: '
        '(1) V-る + 前に: "Before doing A, do B". '
        'CRITICAL TENSE INVARIANCE: The verb preceding 前に is ALWAYS in the present dictionary form (V-る), regardless of whether the overall main sentence is present or past! '
        '(日本へ来る前に、日本語を勉強しました: Before I came to Japan, I studied Japanese; NEVER *来た前に). '
        '(2) V-て + から: "After doing A, do B / and then B". '
        '(勉強してから、遊びに行きました: I studied and then went out; けんさんが来てから、食べましょう: Let\'s eat after Ken arrives). '
        'Footnote 10: V-てから can also mean "ever since A happened": 猫が死んでから、とても寂しいです (I\'ve been lonely ever since my cat died).'
    )
    c['keyTakeaway'] = 'V(short present) + 前に = Before doing A, B (verb before 前に is strictly present tense!). V-て + から = After doing A, B (or "ever since A").'
    c['connection'] = 'V-辞書形 + 前に (before doing) | V-て形 + から (after doing / ever since)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 17, Grammar 5, printed pp. 122-123 (PDF pp. 130-131).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 Lesson 17 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 17 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 17')]

l17_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 17',
        'exactPrintedPages': 'pp. 118-119',
        'exactPdfPages': 'pp. 126-127',
        'grammarItem': '〜そうです (Hearsay Report: I Heard That / Reportedly)',
        'instructionalDetails': 'Short form + そうです for hearsay reports; contrast with Lesson 13 appearance; MANDATORY だ insertion for な-adjectives and nouns in present affirmative (親切だそうです, 学生だそうです; ban on *親切そうです which means appearance); invariant ending (Footnote 1); information source specified with [Source] によると (天気予報によると).',
        'cardId': 'g2-l17-hearsay-sou-desu',
        'exampleCount': 3,
        'exampleIds': ['g2-l17-hearsay-sou-desu::s-g2-17-1', 'g2-l17-hearsay-sou-desu::genki2-use-examples-44', 'g2-l17-hearsay-sou-desu::genki2-use-examples-45'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 118-119 (PDF pp. 126-127, p126_printed118.png, p127_printed119.png). Verified hearsay semantics, comparison table with appearance, mandatory だ on な-adjectives/nouns, and によると.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 17',
        'exactPrintedPages': 'pp. 119, 122-123',
        'exactPdfPages': 'pp. 127, 130-131',
        'grammarItem': '〜って・みたいです (Casual Quotation & Resemblance/Inference)',
        'instructionalDetails': '〜って as casual quotation/hearsay particle following short forms (忙しいって, 食べたって言ってた); 〜みたいです for resemblance to noun (Nounみたい: Colonel Sandersみたい) and inference from sensory observation (V-shortみたいです: 空いているみたいです: looks hungry; 降ったみたい: looks like it rained); な-adjective inflection.',
        'cardId': 'added-g2-17-28',
        'exampleCount': 4,
        'exampleIds': ['added-g2-17-28-example', 'added-g2-17-28::genki2-use-examples-50', 'added-g2-17-28::genki2-use-examples-51', 'added-g2-17-28::genki2-use-examples-52'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 119, 122-123 (PDF pp. 127, 130-131, p127_printed119.png, p130_printed122.png, p131_printed123.png). Verified colloquial quotation 〜って and dual functions of みたいです.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 17',
        'exactPrintedPages': 'pp. 119-121',
        'exactPdfPages': 'pp. 127-129',
        'grammarItem': '〜たら (Specific & Temporal Conditional: If / When / Once Done)',
        'instructionalDetails': 'Past short form + ら (V-たら, かったら, だったら, なかったら); open condition, temporal sequence certainty ("once / when A is done, let\'s do B"), and contrary-to-fact counterfactuals (私が猫だったら); strict chronological rule: B cannot happen before A; natural dependency rule (Footnote 6: cannot mean "even if").',
        'cardId': 'g2-l17-tara-conditional',
        'exampleCount': 3,
        'exampleIds': ['g2-l17-tara-conditional::s-g2-17-2', 'g2-l17-tara-conditional::genki2-use-examples-46', 'g2-l17-tara-conditional::genki2-use-examples-47'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 119-121 (PDF pp. 127-129, p127_printed119.png, p128_printed120.png, p129_printed121.png). Verified conditional formation table, temporal certainty vs hypothetical modes, and chronological constraints.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 17',
        'exactPrintedPages': 'p. 121',
        'exactPdfPages': 'p. 129',
        'grammarItem': '〜なくてもいいです (Lack of Obligation: You Do Not Have To)',
        'instructionalDetails': 'V-ない (drop い) + くて + もいいです for lack of obligation ("do not have to / need not do"); casual variants 〜なくてもいい and 〜なくていい.',
        'cardId': 'g2-l17-nakute-mo-ii',
        'exampleCount': 3,
        'exampleIds': ['g2-l17-nakute-mo-ii::s-g2-17-3', 'g2-l17-nakute-mo-ii::genki2-use-examples-48', 'g2-l17-nakute-mo-ii::genki2-use-examples-49'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 121 (PDF p. 129, p129_printed121.png). Verified negative te-form attachment, permission of omission semantics, and casual spoken forms.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 17',
        'exactPrintedPages': 'pp. 122-123',
        'exactPdfPages': 'pp. 130-131',
        'grammarItem': '〜前に・〜てから (Temporal Sequence: Before Doing vs After Doing)',
        'instructionalDetails': 'V(short present) + 前に for "before doing A, do B" (verb before 前に is strictly present tense, even in past sentences); V-て + から for "after doing A, do B" (also "ever since A happened"); expression note on 〜よね (shared mutual knowledge).',
        'cardId': 'added-g2-17-29',
        'exampleCount': 3,
        'exampleIds': ['added-g2-17-29-example', 'added-g2-17-29::genki2-use-examples-53', 'added-g2-17-29::genki2-use-examples-54'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 122-123 (PDF pp. 130-131, p130_printed122.png, p131_printed123.png). Verified strict present tense before 前に, sequential V-てから, and Footnote 10 "ever since" nuance.'
    }
]

matrix.extend(l17_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Successfully updated matrix! Total rows now: {len(matrix)}')
