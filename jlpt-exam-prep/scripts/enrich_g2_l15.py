import json

# 1. Update chapterExercises.json for Lesson 15 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l15-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l15-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 15',
        'type': 'multiple-choice',
        'context': 'Spontaneous visual perception: Looking out of the hotel room window and noticing the ocean.',
        'question': 'ホテルの部屋の窓から、青い海が（　　）。',
        'translation': 'From the window of the hotel room, the blue ocean is visible.',
        'options': [
            '見えます',
            '見られます',
            '見ます',
            '見せます'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l15-relative-clauses',
        'grammarPointTitle': '連体修飾節 (Relative Clauses / Qualifying Nouns with Sentences)',
        'explanation': {
            'overall': 'Genki II Lesson 15 explicitly distinguishes 見える from 見られる: 見える means something is spontaneously visible to the eyes without effort (海が見えます). 見られる means the subject can actively choose to view or has circumstances permitting viewing (映画が見られます).',
            'options': [
                {
                    'text': '見えます',
                    'isCorrect': True,
                    'reason': 'Correct. Spontaneous visual perception: [Sight] が 見えます.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '見られます',
                    'isCorrect': False,
                    'reason': 'Incorrect. 見られます is the active potential form (can watch/view deliberately), inappropriate for passive visibility from a window.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '見ます',
                    'isCorrect': False,
                    'reason': 'Incorrect. Direct volitional action takes object marker を, not subject が with spontaneous scenery.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '見せます',
                    'isCorrect': False,
                    'reason': 'Incorrect. Causative/transitive "to show something to someone".',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which verb describes scenery that is spontaneously visible to your eyes without effort?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l15-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l15-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 15',
        'type': 'multiple-choice',
        'context': 'Contrasting personal intention vs objective prediction: Stating personal intention to work at a Japanese firm.',
        'question': '大学を卒業したら、日本の会社で（　　）と思っています。',
        'translation': 'Upon graduating from college, I intend to work for a Japanese company.',
        'options': [
            '働こう',
            '働く',
            '働いた',
            '働いて'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l15-volitional-to-omotte-iru',
        'grammarPointTitle': '意向形 + と思っている (Firm Ongoing Determination: Intending To)',
        'explanation': {
            'overall': 'Genki II Lesson 15 contrasts Volitional + と思っている with Present tense + と思っている: The volitional form (働こうと思っている) expresses personal intention or determination ("I intend to work"). The present tense (働くと思っている) expresses objective prediction ("I think someone will work").',
            'options': [
                {
                    'text': '働こう',
                    'isCorrect': True,
                    'reason': 'Correct. Volitional form + と思っている expresses personal intention/determination.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '働く',
                    'isCorrect': False,
                    'reason': 'Incorrect. Present dictionary form + と思っている expresses prediction, not determined intention.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '働いた',
                    'isCorrect': False,
                    'reason': 'Incorrect. Past short form + と思っている expresses belief about a past occurrence.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '働いて',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form cannot precede と思っている.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which verb form combines with と思っている to express personal determination / intention?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 15!')

# 2. Enrich base-reviewed.json for Lesson 15 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. g2-l15-volitional-form
c = card_map.get('g2-l15-volitional-form')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 15'
    c['nuance'] = (
        'The volitional form of a verb is the casual spoken equivalent of 〜ましょう ("Let\'s do / shall we?"). It is used to suggest a plan to a close friend or to express firm self-resolve. '
        'Conjugation rules: '
        '(1) Ru-verbs: drop final -ru and add -yoo (見る → 見よう, 食べる → 食べよう, 寝る → 寝よう). '
        '(2) U-verbs: drop final -u and add -oo (the final syllable shifts to the o-row of the hiragana chart + う): '
        '行く → 行こう, 泳ぐ → 泳ごう, 話す → 話そう, 待つ → 待とう, 飲む → 飲もう, 帰る → 帰ろう, 買う → 買おう. '
        '(3) Irregular verbs: 来る (くる) → こよう; する → しよう. '
        'Questions: Volitional + か asks for the listener\'s opinion or makes an offer: 手伝おうか (Shall I lend you a hand?); 今度いつ会おうか (When shall we meet again?).'
    )
    c['keyTakeaway'] = 'Ru-verbs: -yoo (食べよう). U-verbs: u -> o-row + う (行こう, 飲もう). くる→こよう, する→しよう. Casual "Let\'s do". Question + か: "Shall I / we?"'
    c['connection'] = 'Ru: V-stem + よう | U: V (u->o) + う | くる→こよう | する→しよう | 意向形 + か (offer/suggestion)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 15, Grammar 1, printed pp. 74-75 (PDF pp. 82-83).'

# 2. g2-l15-volitional-to-omotte-iru
c = card_map.get('g2-l15-volitional-to-omotte-iru')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 15'
    c['nuance'] = (
        'Volitional form + と思っている / と思う expresses personal resolutions and intentions ("I am intending / planning to do X"). '
        'ASPECTUAL DICHOTOMY: '
        '(1) 意向形 + と思っている: Firm ongoing determination that the speaker has entertained for some time and has already decided (毎日三時間日本語を勉強しようと思っています: I have decided to study 3 hours every day). '
        '(2) 意向形 + と思う: A decision made on the spot at the moment of speaking (旅行に行こうと思います: I will go on a trip - decision made right now). '
        'CRITICAL CONTRAST: Volitional form vs Present tense before と思う: '
        '日本の会社で働こうと思います = Intention ("I intend / resolve to work"). '
        '日本の会社で働くと思います = Prediction ("I think they/I will be working").'
    )
    c['keyTakeaway'] = '意向形 + と思っている = Ongoing firm resolution already decided. 意向形 + と思う = On-the-spot decision. Volitional = Intention; Present dictionary = Prediction.'
    c['connection'] = 'V-意向形 + と思っている (ongoing plan) | V-意向形 + と思う (on-the-spot decision)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 15, Grammar 1, printed p. 75 (PDF p. 83).'

# 3. added-g2-15-24 (~ておく)
c = card_map.get('added-g2-15-24')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 15'
    c['nuance'] = (
        'The te-form of a verb plus the auxiliary verb おく describes an action performed in advance, in preparation for a future event or convenience ("to do something in preparation / beforehand"). '
        'Formation: V-て + おく (e.g. ホテルを予約しておく: make hotel reservations in advance; 部屋を掃除しておく: clean room beforehand). '
        'Conjugation: おく conjugates as a regular U-verb (〜ておきます、〜ておいてください、〜ておいた). '
        'SPOKEN CONTRACTION: In casual spoken Japanese, 〜ておく frequently contracts to 〜とく (予約しとく: I will reserve in advance; 買っとく: I will buy beforehand; 読んどく: I will read in advance).'
    )
    c['keyTakeaway'] = 'V-て + おく (action performed in preparation for future). Conjugates as U-verb. Spoken casual contraction: 〜ておく → 〜とく (予約しとく, 買っとく).'
    c['connection'] = 'V-て形 + おく / おきます / おいて / おいた | Casual: V-て形 + とく'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 15, Grammar 2, printed p. 76 (PDF p. 84).'

# 4. g2-l15-relative-clauses
c = card_map.get('g2-l15-relative-clauses')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 15'
    c['nuance'] = (
        'Relative clauses (qualifying nouns with sentences) in Japanese precede the modified head noun directly without relative pronouns (who, which, that do not exist). '
        'Formation rules: '
        '(1) Qualifier verbs: The predicate inside the relative clause MUST be in short form (present or past, affirmative or negative: 昨日買った本, 彼女がくれた本, テーブルの上にある本, 日本で買えない本). '
        '(2) INTERNAL SUBJECT RULE: When the subject of the action appears inside the relative clause, it is marked by particle が, NEVER は! (彼女がくれた本; strictly prohibited: *彼女はくれた本). '
        '(3) Synthesis: The entire [Clause + Noun] unit functions as a single noun phrase and can take any case particle in the main clause (これは彼女がくれた本です; 父が村上春樹が書いた本をくれました).'
    )
    c['keyTakeaway'] = '[Sentence in short form] + Noun = Relative clause. No relative pronouns! INTERNAL SUBJECT RULE: Subject inside the qualifier clause takes が, NEVER は (彼女がくれた本).'
    c['connection'] = '[V-short form] + Noun | [Subject が V-short] + Noun'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 15, Grammar 3, printed pp. 76-77 (PDF pp. 84-85).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 4 Lesson 15 cards in base-reviewed.json!')

# 3. Add 4 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 15 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 15')]

l15_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 15',
        'exactPrintedPages': 'pp. 74-75',
        'exactPdfPages': 'pp. 82-83',
        'grammarItem': '意向形 (The Volitional Form: Casual Let\'s Do / Self-Resolve)',
        'instructionalDetails': 'Ru-verbs: -yoo (食べよう, 見よう); U-verbs: final u shifts to o-row + う (行こう, 泳ごう, 待とう, 飲もう); irregulars: くる→こよう, する→しよう; casual equivalent of 〜ましょう; question pattern with か (手伝おうか: Shall I lend a hand?).',
        'cardId': 'g2-l15-volitional-form',
        'exampleCount': 3,
        'exampleIds': ['g2-l15-volitional-form::s-g2-15-1', 'g2-l15-volitional-form::genki2-use-examples-25', 'g2-l15-volitional-form::genki2-use-examples-26'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 74-75 (PDF pp. 82-83, p82_printed74.png, p83_printed75.png). Verified volitional conjugation paradigms across verb classes and offer/opinion questions with か.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 15',
        'exactPrintedPages': 'p. 75',
        'exactPdfPages': 'p. 83',
        'grammarItem': '意向形 + と思っている / と思う (Firm Ongoing Determination: Intending To)',
        'instructionalDetails': '意向形 + と思っている for ongoing firm determination already decided; 意向形 + と思う for decision made on the spot; contrast with present dictionary form + と思う (which conveys objective prediction rather than determined intention).',
        'cardId': 'g2-l15-volitional-to-omotte-iru',
        'exampleCount': 3,
        'exampleIds': ['g2-l15-volitional-to-omotte-iru::s-g2-15-2', 'g2-l15-volitional-to-omotte-iru::genki2-use-examples-27', 'g2-l15-volitional-to-omotte-iru::genki2-use-examples-28'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 75 (PDF p. 83, p83_printed75.png). Verified aspectual dichotomy between ongoing resolution (と思っている) and spontaneous decision (と思う), plus prediction contrast.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 15',
        'exactPrintedPages': 'p. 76',
        'exactPdfPages': 'p. 84',
        'grammarItem': '〜ておく (Preparatory Action: Doing Something in Advance)',
        'instructionalDetails': 'V-て + おく describes actions performed in advance in preparation for a future event; U-verb inflection; spoken casual contraction 〜ておく → 〜とく (予約しとく, 買っとく).',
        'cardId': 'added-g2-15-24',
        'exampleCount': 6,
        'exampleIds': [
            'added-g2-15-24-example',
            'added-g2-15-24::genki2-use-examples-31',
            'added-g2-15-24::genki2-use-examples-32',
            'added-g2-15-24::merged-genki2-te-oku::s-g2-15-1',
            'added-g2-15-24::merged-genki2-te-oku::supp-use-examples-24',
            'added-g2-15-24::merged-genki2-te-oku::supp-use-examples-25'
        ],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 76 (PDF p. 84, p84_printed76.png). Verified preparatory aspect semantics, U-verb conjugation, and spoken casual contraction 〜とく.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 15',
        'exactPrintedPages': 'pp. 76-77',
        'exactPdfPages': 'pp. 84-85',
        'grammarItem': '連体修飾節 (Relative Clauses / Qualifying Nouns with Sentences)',
        'instructionalDetails': 'Qualifier sentence in short form directly precedes modified noun without relative pronouns; INTERNAL SUBJECT RULE: subject inside relative clause is marked by が, never は (彼女がくれた本; ban on *彼女はくれた本); expression notes: 見える vs 見られる (spontaneous visibility vs active capability), 聞こえる vs 聞ける, and ordinal suffix 〜目.',
        'cardId': 'g2-l15-relative-clauses',
        'exampleCount': 3,
        'exampleIds': ['g2-l15-relative-clauses::s-g2-15-3', 'g2-l15-relative-clauses::genki2-use-examples-29', 'g2-l15-relative-clauses::genki2-use-examples-30'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 76-77 (PDF pp. 84-85, p84_printed76.png, p85_printed77.png). Verified relative clause syntax, internal subject が rule, and expression notes for 見える/見られる.'
    }
]

matrix.extend(l15_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Successfully updated matrix! Total rows now: {len(matrix)}')
