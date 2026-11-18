import json

# 1. Update chapterExercises.json for SKM N3 Chapter 1 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# Add Q7 through Q12 for SKM N3 Part 1 · Chapter 1
new_questions = [
    {
        'id': 'skm3-c1-ex-7',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 1',
        'type': 'multiple-choice',
        'context': 'Seizing opportunity before weather turns bad: Urging a friend to head home before the impending rain begins.',
        'question': '空が暗くなってきましたね。雨が（　　）うちに早く帰りましょう。',
        'translation': 'The sky has gotten dark. Let\'s hurry home before it starts raining.',
        'options': [
            '降らない',
            '降る',
            '降った',
            '降っている'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u1-uchini-while',
        'grammarPointTitle': '〜うちに (While State Lasts / Before Opportunity Slips)',
        'explanation': {
            'overall': 'When combined with a negative verb, V-ない + うちに means "before something happens / while X has not yet occurred" (雨が降らないうちに: before it rains).',
            'options': [
                {
                    'text': '降らない',
                    'isCorrect': True,
                    'reason': 'Correct. V-ない + うちに means "before it happens" (before it rains).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '降る',
                    'isCorrect': False,
                    'reason': 'Incorrect. 降るうちに would mean "while it is actively raining", which contradicts the urge to beat the rain.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '降った',
                    'isCorrect': False,
                    'reason': 'Incorrect. Past tense 降った does not connect with うちに for prospective actions.',
                    'trapCategory': 'tense'
                },
                {
                    'text': '降っている',
                    'isCorrect': False,
                    'reason': 'Incorrect. Continuous 降っている implies rain is already underway.',
                    'trapCategory': 'aspect'
                }
            ]
        },
        'hint': 'Which verb form attaches to うちに to mean "before [action/event] occurs"?'
    },
    {
        'id': 'skm3-c1-ex-8',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 1',
        'type': 'multiple-choice',
        'context': 'Momentary interruption during a continuous activity: Realizing someone called while you were taking a shower.',
        'question': 'シャワーを浴びている（　　）、誰かから電話がかかってきたようだ。',
        'translation': 'It seems someone called while I was taking a shower.',
        'options': [
            '間に',
            '間',
            'うちに',
            'ところで'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u1-aida-vs-aidani',
        'grammarPointTitle': '〜間 vs 〜間に (Continuous Duration vs Momentary Action)',
        'explanation': {
            'overall': 'When a momentary action or event occurs inside the duration of an ongoing background state, 〜間に is used. In contrast, 〜間 describes a continuous action extending through the whole duration.',
            'options': [
                {
                    'text': '間に',
                    'isCorrect': True,
                    'reason': 'Correct. The phone ringing is a momentary action occurring inside the shower duration, requiring 間に.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': '間',
                    'isCorrect': False,
                    'reason': 'Incorrect. 間 requires the event in clause B to last continuously for the entire duration of the shower.',
                    'trapCategory': 'aspect'
                },
                {
                    'text': 'うちに',
                    'isCorrect': False,
                    'reason': 'Incorrect. うちに focuses on temporal opportunity or gradual internal evolution, less natural for external objective phone calls.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': 'ところで',
                    'isCorrect': False,
                    'reason': 'Incorrect. ところで as a conditional means "even if", which does not fit.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which particle after 間 marks a momentary event occurring in the middle of a continuous timeframe?'
    },
    {
        'id': 'skm3-c1-ex-9',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 1',
        'type': 'multiple-choice',
        'context': 'Evaluating commercial software: Stating that you cannot determine its real utility until you test it yourself.',
        'question': '実際に使ってみてから（　　）、本当に役に立つかどうか判断できません。',
        'translation': 'Until I actually try using it, I cannot judge whether it is truly useful.',
        'options': [
            'でないと',
            'だから',
            'なら',
            'でも'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u1-te-kara-denaito',
        'grammarPointTitle': '〜てからでないと / 〜てからでなければ (Not Until / Only After Prerequisite Is Done)',
        'explanation': {
            'overall': 'V-てからでないと (or てからでなければ) expresses "not until / unless X is done first". The following clause strictly expresses impossibility, inability, or a negative state (判断できません: cannot judge).',
            'options': [
                {
                    'text': 'でないと',
                    'isCorrect': True,
                    'reason': 'Correct. V-てからでないと completes the prerequisite pattern "unless... cannot...".',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'だから',
                    'isCorrect': False,
                    'reason': 'Incorrect. からでないと is the formula, not だから.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'なら',
                    'isCorrect': False,
                    'reason': 'Incorrect. てからなら implies affirmative possibility, but the sentence concludes negatively.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': 'でも',
                    'isCorrect': False,
                    'reason': 'Incorrect. てからでも means "even after", which does not match the prerequisite dependency.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'What follows てから to express "unless prerequisite X is completed, Y cannot happen"?'
    },
    {
        'id': 'skm3-c1-ex-10',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 1',
        'type': 'multiple-choice',
        'context': 'Caught in the act: Getting discovered by your mother right while secretly eating snacks before dinner.',
        'question': '晩ご飯の前にこっそりケーキを食べている（　　）を、母に見つかってしまった。',
        'translation': 'Right in the middle of secretly eating cake before dinner, I was caught red-handed by my mother.',
        'options': [
            'ところ',
            'ばかり',
            'とおり',
            'ついで'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u1-tokoro-da-phases',
        'grammarPointTitle': '〜ところだ (Temporal Phase: Imminent, In the Midst, or Just Finished)',
        'explanation': {
            'overall': 'V-ている + ところ + を + 見つかる / 見る describes being caught or seen right in the middle of an ongoing action.',
            'options': [
                {
                    'text': 'ところ',
                    'isCorrect': True,
                    'reason': 'Correct. V-ているところを expresses being caught in the exact ongoing physical phase of an act.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'ばかり',
                    'isCorrect': False,
                    'reason': 'Incorrect. ばかりを is ungrammatical in this aspectual sense.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'とおり',
                    'isCorrect': False,
                    'reason': 'Incorrect. とおり means "in accordance with", which does not fit.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'ついで',
                    'isCorrect': False,
                    'reason': 'Incorrect. ついで means "taking opportunity for a side task", which does not fit.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which noun marks the temporal ongoing phase in the pattern "...ている [　] を見つかる"?'
    },
    {
        'id': 'skm3-c1-ex-11',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 1',
        'type': 'multiple-choice',
        'context': 'Unconscious gradual development: Naturally becoming fluent in Japanese as a result of living in Japan for a couple of years.',
        'question': '日本で何年も生活している（　　）、いつの間にか日本語が上手に話せるようになった。',
        'translation': 'While living in Japan for years, without even realizing it, I became able to speak Japanese skillfully.',
        'options': [
            'うちに',
            'あいだ',
            'まえに',
            'あとで'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u1-uchini-change',
        'grammarPointTitle': '〜うちに (Unnoticed Natural Evolution: While Doing X, Y Emerged)',
        'explanation': {
            'overall': 'V-ている + うちに expresses an unnoticed, non-volitional evolution or change that naturally emerges over time during an ongoing process.',
            'options': [
                {
                    'text': 'うちに',
                    'isCorrect': True,
                    'reason': 'Correct. うちに expresses natural gradual transformation without deliberate planning.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': 'あいだ',
                    'isCorrect': False,
                    'reason': 'Incorrect. あいだ merely states an objective chronological container, lacking the subtle internal evolution nuance.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': 'まえに',
                    'isCorrect': False,
                    'reason': 'Incorrect. まえに requires present short forms and means "before", contrary to chronology.',
                    'trapCategory': 'tense'
                },
                {
                    'text': 'あとで',
                    'isCorrect': False,
                    'reason': 'Incorrect. あとで requires past た-form and indicates a separate subsequent event.',
                    'trapCategory': 'tense'
                }
            ]
        },
        'hint': 'Which expression indicates that an unforced, gradual change occurred during a continuous process?'
    },
    {
        'id': 'skm3-c1-ex-12',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 1',
        'type': 'multiple-choice',
        'context': 'Imminent commencement: Announcing on the phone that the company meeting is just about to start in a few seconds.',
        'question': 'あ、田中さん。ちょうど今から定例会議が（　　）ところです。',
        'translation': 'Ah, Tanaka-san. The regular meeting is just about to start right now.',
        'options': [
            '始まる',
            '始まった',
            '始まっている',
            '始まりそう'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u1-tokoro-da-phases',
        'grammarPointTitle': '〜ところだ (Temporal Phase: Imminent, In the Midst, or Just Finished)',
        'explanation': {
            'overall': 'When combined with the dictionary form of a verb, V(dictionary) + ところだ describes an action that is imminent and just about to take place within seconds.',
            'options': [
                {
                    'text': '始まる',
                    'isCorrect': True,
                    'reason': 'Correct. Dictionary form + ところだ indicates imminent commencement ("just about to start").',
                    'trapCategory': 'tense'
                },
                {
                    'text': '始まった',
                    'isCorrect': False,
                    'reason': 'Incorrect. 始まったところだ would mean the meeting "just finished starting / just started a second ago".',
                    'trapCategory': 'aspect'
                },
                {
                    'text': '始まっている',
                    'isCorrect': False,
                    'reason': 'Incorrect. 始まっているところ indicates an action already in progress, incompatible with 今から ("starting from now").',
                    'trapCategory': 'aspect'
                },
                {
                    'text': '始まりそう',
                    'isCorrect': False,
                    'reason': 'Incorrect. 始まりそう + ところ is redundant and grammatically invalid.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which verb form attaches to ところだ to indicate an action that is just about to begin in a moment?'
    }
]

existing_ids = {e['id'] for e in exercises}
for q in new_questions:
    if q['id'] not in existing_ids:
        exercises.append(q)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for SKM N3 Chapter 1!')

# 2. Enrich base-reviewed.json for Chapter 1 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. skm3-u1-uchini-while
c = card_map.get('skm3-u1-uchini-while')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 1'
    c['nuance'] = (
        '〜うちに expresses seizing a transient window of opportunity before the current state or condition changes: "do something while condition ~ lasts / before opportunity slips away". '
        'FORMATION (Printed p. 16): '
        '・Noun + の + うちに (若いうちに: while young; 独身のうちに: while single). '
        '・Verb (Dictionary form / ている / ない) + うちに (温かいうちに: while still warm; 明るいうちに: while still light; 忘れないうちに: before I forget; 雨が降らないうちに: before it rains). '
        '・い-adjectives: 〜いうちに. '
        '・な-adjectives: 〜なうちに (元気なうちに: while still in good health). '
        'PRAGMATIC CONSTRAINTS (p. 16): '
        'Clause A represents a state or situation. Clause B is strictly an intentional, volitional action performed by the speaker to take advantage of the circumstance (日本にいるうちに一度富士山に登ってみたい: While in Japan, I want to try climbing Mt. Fuji).'
    )
    c['keyTakeaway'] = '〜うちに: Seizing a temporary window of opportunity ("do X while state holds / before state changes"). Clause B is strictly volitional (want to do / do!). Formation: Noun+の / な-adj+な / い-adj / V(dict/te-iru/nai) + うちに.'
    c['connection'] = 'Noun + の / な-adj + な / い-adj / Verb (辞書形/ている/ない) + うちに、[Volitional Action]'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 1, Section 1-1, printed p. 16 (PDF p. 39).'

# 2. skm3-u1-uchini-change
c = card_map.get('skm3-u1-uchini-change')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 1'
    c['nuance'] = (
        '〜うちに (Natural Evolution) expresses that while a continuous process or action ~ is happening, a change ... also emerges naturally without the deliberate intention of the speaker: "while doing..., gradually / before I realized it, change occurred". '
        'FORMATION (Printed p. 16): '
        '・Verb (Dictionary form / ている / ない) + うちに '
        '・音楽を聞いているうちに眠ってしまった (While listening to music, I fell asleep without realizing). '
        '・何回も練習するうちに、上手に弾けるようになった (While practicing repeatedly, I naturally became able to play well). '
        '・最初は嫌いだったが、付き合っているうちに好きになった (At first I disliked him, but while spending time together, I came to like him). '
        'STRICT VOLITION BAN (p. 16): '
        'Clause B CANNOT express speaker volition, requests, or commands (*見ているうちに、買いましょう is completely ungrammatical). It must describe an unconscious, emergent natural transformation or state change.'
    )
    c['keyTakeaway'] = '〜うちに (Evolution): While a continuous process ~ unfolds, an unforced change ... emerges without speaker volition ("before realizing it / gradually"). Clause B CANNOT be volitional (never requests/commands).'
    c['connection'] = 'Verb (辞書形 / ている形 / ない形) + うちに、[Non-Volitional Change]'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 1, Section 1-2, printed p. 16 (PDF p. 39).'

# 3. skm3-u1-aida-vs-aidani
c = card_map.get('skm3-u1-aida-vs-aidani')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 1'
    c['nuance'] = (
        'Shin Kanzen Master N3 rigorously systematizes the aspectual dichotomy between 〜間 and 〜間に: '
        'FORMATION (Printed pp. 16-17): '
        '・Noun + の / Verb (辞書形 / ている / ない) + 間 vs 間に. '
        '(1) 〜間 (Continuous Co-occurrence, p. 16): '
        '・"While ~ (continuous state), ... is going on continuously throughout the same duration." '
        '・Both ~ and ... describe sustained, ongoing states or actions that span the entire duration together (留守の間、友だちが犬の世話をしてくれた: While I was away, my friend took care of my dog the entire time; お母さんが昼寝をしている間、子どもたちは静かにテレビを見ていた). '
        '(2) 〜間に (Momentary Interruption, p. 17): '
        '・"While ~ (continuous state), ... happens as a momentary action or event." '
        '・~ describes a continuous state, but ... describes an instantaneous action or punctual event that begins and concludes within the timeframe (留守の間に泥棒が入った: A burglar broke in while I was away; シャワーを浴びている間に電話が鳴った: The phone rang while taking a shower).'
    )
    c['keyTakeaway'] = '〜間 = both clauses describe continuous actions spanning the whole timeframe together. 〜間に = momentary action or punctual event occurs inside the ongoing duration of clause A.'
    c['connection'] = '[Noun の / Verb (辞書形/ている/ない)] + 間 (continuous B) | 間に (momentary B)'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 1, Section 2-1 & 2-2, printed pp. 16-17 (PDF pp. 39-40).'

# 4. skm3-u1-te-kara-denaito
c = card_map.get('skm3-u1-te-kara-denaito')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 1'
    c['nuance'] = (
        '〜てからでないと / 〜てからでなければ expresses an indispensable prerequisite: "until/unless ~ happens or is completed, ... cannot happen or cannot be done either". '
        'FORMATION (Printed p. 17): '
        '・Verb て-form + からでないと / からでなければ. '
        '・手続きをしてからでないと、この部屋には入れません (You cannot enter this room until procedures are completed). '
        '・親と相談してからでなければ、留学するかどうか決められません (I cannot decide whether to study abroad until I talk with my parents). '
        '・実際に使ってみてからでないと、本当に役に立つか判断できません (Until actually trying it, one cannot judge whether it is helpful). '
        'STRICT NEGATIVE/INABILITY CONSTRAINT (p. 17): '
        'The following clause ... is strictly restricted to negative statements, expressing impossibility, inability (〜わけにはいかない, 〜できない), or an unfavorable state.'
    )
    c['keyTakeaway'] = 'V-てからでないと / でなければ: "not until / unless prerequisite ~ is done". Clause B is STRICTLY NEGATIVE (cannot do, impossible, prohibited: 入れません, 決められません).'
    c['connection'] = 'V-てからでないと / V-てからでなければ、[Negative / Impossibility Predicate]'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 1, Section 3, printed p. 17 (PDF p. 40).'

# 5. skm3-u1-tokoro-da-phases
c = card_map.get('skm3-u1-tokoro-da-phases')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 1'
    c['nuance'] = (
        '〜ところだ pinpoints the precise temporal phase of an action (imminent, concurrent, or freshly completed). '
        'FORMATION & THREE TEMPORAL PHASES (Printed p. 17): '
        '(1) Verb (辞書形) + ところだ: Just before ~ happens / on the very verge of doing: '
        '・ロケットは今まさに飛び立つところです (The rocket is on the very verge of blasting off). '
        '・今から出かけるところです (I am just about to head out right now). '
        '(2) Verb (ている形) + ところだ: Right in the midst of ~ happening: '
        '・今、原因を調べているところです (We are currently in the midst of investigating the cause). '
        '・電話しているところです (I am in the middle of a phone call). '
        '(3) Verb (た形) + ところだ: Just this very second finished ~ happening: '
        '・たった今、昼ご飯を食べ終わったところです (I have just this moment finished lunch). '
        'MID-SENTENCE PARTICLE ALTERNATION: '
        'Depending on the following verb, particles attach: '
        '・〜ところへ (at the moment when someone arrives: ケーキを食べているところへ母が帰ってきた). '
        '・〜ところを (caught in the midst of an action: 泥棒が逃げようとするところを逮捕された). '
        '・〜ところで (at the juncture where something interrupts: 相談しているところで電話が入った).'
    )
    c['keyTakeaway'] = '〜ところだ: (1) V-辞書形+ところだ = just about to start; (2) V-ている+ところだ = right in the midst; (3) V-た+ところだ = just finished this moment. Particles: ところへ, ところを, ところで.'
    c['connection'] = 'Verb (辞書形 / ている形 / た形) + ところだ (Sentence-final) | ところへ / ところを / ところで'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 1, Section 4, printed p. 17 (PDF p. 40).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 SKM N3 Chapter 1 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing SKM N3 Chapter 1 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Shin Kanzen Master N3' and r.get('sourceSection') == 'Part 1 · Chapter 1')]

skm3_c1_entries = [
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 1',
        'exactPrintedPages': 'p. 16',
        'exactPdfPages': 'p. 39',
        'grammarItem': '〜うちに (While State Lasts / Before Opportunity Slips)',
        'instructionalDetails': 'Seizing transient window of opportunity before condition changes; Clause A is state; Clause B is strictly intentional volitional action (登りたい, 買おう); connections: Noun+の, な-adj+な, い-adj, V(dict/te-iru/nai) + うちに; negative V-ないうちに means "before X happens".',
        'cardId': 'skm3-u1-uchini-while',
        'exampleCount': 4,
        'exampleIds': ['skm3-u1-uchini-while::s-skm3-1-1', 'skm3-u1-uchini-while::n3-use-examples-1', 'skm3-u1-uchini-while::n3-use-examples-2', 'skm3-u1-uchini-while::n3-use-examples-3'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 16 (PDF p. 39, skm3_pdf_39.png). Verified Section 1-1 rules, volitional clause B requirement, and negative V-ないうちに usage.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 1',
        'exactPrintedPages': 'p. 16',
        'exactPdfPages': 'p. 39',
        'grammarItem': '〜うちに (Unnoticed Natural Evolution: Non-Volitional Change)',
        'instructionalDetails': 'Change occurs naturally without speaker volition while continuous process unfolds ("before realizing it, became..."); Clause B strictly non-volitional (ban on requests/commands: *見ているうちに買いましょう is ungrammatical); connections: V(dict/te-iru/nai) + うちに.',
        'cardId': 'skm3-u1-uchini-change',
        'exampleCount': 4,
        'exampleIds': ['skm3-u1-uchini-change::s-skm3-1-2', 'skm3-u1-uchini-change::n3-use-examples-4', 'skm3-u1-uchini-change::n3-use-examples-5', 'skm3-u1-uchini-change::n3-use-examples-6'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 16 (PDF p. 39, skm3_pdf_39.png). Verified Section 1-2 rules, non-volitional clause B restriction, and gradual natural evolution examples.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 1',
        'exactPrintedPages': 'pp. 16-17',
        'exactPdfPages': 'pp. 39-40',
        'grammarItem': '〜間 vs 〜間に (Continuous Duration vs Momentary Action)',
        'instructionalDetails': '〜間 indicates that both situations hold continuously throughout the same duration; 〜間に indicates that a momentary action/event takes place inside the ongoing duration of Clause A; connections: Noun+の / V(dict/te-iru/nai) + 間/間に.',
        'cardId': 'skm3-u1-aida-vs-aidani',
        'exampleCount': 4,
        'exampleIds': ['skm3-u1-aida-vs-aidani::s-skm3-1-3', 'skm3-u1-aida-vs-aidani::n3-use-examples-7', 'skm3-u1-aida-vs-aidani::n3-use-examples-8', 'skm3-u1-aida-vs-aidani::n3-use-examples-9'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 16-17 (PDF pp. 39-40, skm3_pdf_39.png, skm3_pdf_40.png). Verified Section 2-1 and 2-2 aspectual distinction between sustained duration (間) and momentary interruption (間に).'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 1',
        'exactPrintedPages': 'p. 17',
        'exactPdfPages': 'p. 40',
        'grammarItem': '〜てからでないと / 〜てからでなければ (Not Until / Prerequisite)',
        'instructionalDetails': 'V-てからでないと / でなければ establishes necessary prerequisite; Clause B strictly restricted to negative statements of impossibility, inability, or prohibition (入れません, 決められません, 判断できない).',
        'cardId': 'skm3-u1-te-kara-denaito',
        'exampleCount': 4,
        'exampleIds': ['skm3-u1-te-kara-denaito::s-skm3-1-4', 'skm3-u1-te-kara-denaito::n3-use-examples-10', 'skm3-u1-te-kara-denaito::n3-use-examples-11', 'skm3-u1-te-kara-denaito::n3-use-examples-12'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 17 (PDF p. 40, skm3_pdf_40.png). Verified Section 3 formation, mandatory negative clause B constraint, and prerequisite logic.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 1',
        'exactPrintedPages': 'p. 17',
        'exactPdfPages': 'p. 40',
        'grammarItem': '〜ところだ (Temporal Phase: Imminent, In the Midst, Just Finished)',
        'instructionalDetails': 'Three distinct temporal phases: (1) V-辞書形+ところだ (just about to start); (2) V-ている+ところだ (right in the midst of); (3) V-た+ところだ (just this moment finished); mid-sentence case marking variations: ところへ, ところを, ところで.',
        'cardId': 'skm3-u1-tokoro-da-phases',
        'exampleCount': 4,
        'exampleIds': ['skm3-u1-tokoro-da-phases::s-skm3-1-5', 'skm3-u1-tokoro-da-phases::n3-use-examples-13', 'skm3-u1-tokoro-da-phases::n3-use-examples-14', 'skm3-u1-tokoro-da-phases::n3-use-examples-15'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 17 (PDF p. 40, skm3_pdf_40.png). Verified Section 4 tripartite aspectual conjugation and mid-sentence particle attachments (ところへ/を/で).'
    }
]

matrix.extend(skm3_c1_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified SKM N3 Chapter 1 in source coverage matrix! Total certified rows: {len(matrix)}')
