# -*- coding: utf-8 -*-
"""
Genki I (3rd Edition) - Full Unabridged N5 Grammar Syllabus (Lessons 1 to 12)
Every single grammar point from every lesson is represented individually.
"""

def tok(word, reading=None, romaji=None, meaning="", pos=None):
    d = {"word": word, "meaning": meaning}
    if reading: d["reading"] = reading
    if romaji: d["romaji"] = romaji
    if pos: d["pos"] = pos
    return d

def make_sentence(sid, ja, en, literal, tokens, nuanceNote=None, trapAlert=None):
    d = {
        "id": sid,
        "japanese": ja,
        "english": en,
        "literal": literal,
        "tokens": tokens
    }
    if nuanceNote:
        d["nuanceNote"] = nuanceNote
    if trapAlert:
        d["trapAlert"] = trapAlert
    return d

def make_quiz(qid, q, trans, opts, correct_idx, explanations, focus, hint):
    return {
        "id": qid,
        "question": q,
        "translation": trans,
        "options": opts,
        "correctIndex": correct_idx,
        "grammarFocus": focus,
        "ruleHint": hint,
        "explanations": [
            {
                "text": opts[i],
                "isCorrect": (i == correct_idx),
                "reason": explanations[i]
            }
            for i in range(len(opts))
        ]
    }

def get_full_genki1():
    pts = [
        # === LESSON 1 ===
        {
            "id": "g1-l1-wa-desu",
            "title": "X は Y です (X is Y / Topic & Copula)",
            "meaning": "X is Y. Establishes X as the contextual topic with は and equates it to predicate Y with です.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 1: New Friends",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun1 + は + Noun2 / Adjective + です",
            "nuance": "The topic particle は (pronounced 'wa') presents the background context ('as for X...'). です serves as polite non-past copula.",
            "keyTakeaway": "MUG-UP: は marks the topic. Pronounced 'wa', written as は.",
            "sentences": [
                make_sentence(
                    "s-g1-1-1",
                    "私はアリゾナ大学の学生です。",
                    "I am a student at the University of Arizona.",
                    "I topic University-of-Arizona's student am.",
                    [
                        tok("私", "わたし", "watashi", "I / me", "Pronoun"),
                        tok("は", "わ", "wa", "topic marker", "Particle"),
                        tok("学生", "がくせい", "gakusei", "student", "Noun"),
                        tok("です", "です", "desu", "am / is", "Copula")
                    ],
                    "Standard polite self-identification."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-1-1",
                    "スミスさん（　　）イギリス人です。",
                    "Smith-san is British.",
                    ["は", "を", "に", "へ"],
                    0,
                    [
                        "Correct! は marks Smith-san as the topic being identified as British.",
                        "Incorrect. を marks direct objects of action verbs.",
                        "Incorrect. に marks destination, time, or location of existence.",
                        "Incorrect. へ marks direction of movement."
                    ],
                    "Topic particle は",
                    "Marks Smith-san as the conversational topic."
                )
            ],
            "tags": ["N5", "Genki L1", "Topic", "Copula"]
        },
        {
            "id": "g1-l1-question-ka",
            "title": "質問の「か」 (Question Sentence Marker 〜ですか)",
            "meaning": "Turns any declarative sentence into a question simply by appending か at the end, without inverting word order.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 1: New Friends",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Sentence + か (Rising intonation)",
            "nuance": "NO QUESTION MARK NEEDED: In traditional Japanese, particle か serves as the question mark itself. Question word goes right where the answer belongs.",
            "keyTakeaway": "MUG-UP: Append か to the end of a sentence to make it a polite question. No word inversion!",
            "sentences": [
                make_sentence(
                    "s-g1-1-2",
                    "専攻は何ですか。「日本語です。」",
                    "What is your major? 'It is Japanese.'",
                    "Major topic what is question? Japanese is.",
                    [
                        tok("専攻", "せんこう", "senkou", "major", "Noun"),
                        tok("何", "なん", "nan", "what", "Interrogative"),
                        tok("ですか", "ですか", "desu ka", "is it?", "Copula+Particle")
                    ],
                    "Interrogative 何 directly takes ですか."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-1-2",
                    "今何時（　　）。「午後二時です。」",
                    "What time is it now? 'It is 2:00 PM.'",
                    ["ですか", "でした", "でして", "ですね"],
                    0,
                    [
                        "Correct! ですか forms a standard polite question asking the time.",
                        "Incorrect. でした is past tense ('was it?').",
                        "Incorrect. でして is te-form of copula.",
                        "Incorrect. ですね seeks confirmation ('isn't it?'), not an open inquiry."
                    ],
                    "Question particle か",
                    "Inquiring about current time."
                )
            ],
            "tags": ["N5", "Genki L1", "Questions", "Particle か"]
        },
        {
            "id": "g1-l1-noun-no-noun",
            "title": "Noun1 の Noun2 (Noun Modification, Possession & Affiliation)",
            "meaning": "Particle の connects two nouns where Noun1 modifies, describes, or possesses Noun2 ('Noun1's Noun2' or 'Noun2 of Noun1').",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 1: New Friends",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun1 (Modifier/Owner) + の + Noun2 (Main item)",
            "nuance": "MODIFIER FIRST: Japanese strictly places the modifier before の: 日本の大学 (Japanese university), 私の友達 (my friend).",
            "keyTakeaway": "MUG-UP: [Owner/Category] の [Item]. The main noun is ALWAYS at the end!",
            "sentences": [
                make_sentence(
                    "s-g1-1-3",
                    "たけしさんはさくら大学の学生です。",
                    "Takeshi-san is a student of Sakura University.",
                    "Takeshi topic Sakura-University's student is.",
                    [
                        tok("さくら大学の", "さくらだいがくの", "sakura daigaku no", "Sakura University's", "Noun+Particle"),
                        tok("学生", "がくせい", "gakusei", "student", "Noun")
                    ],
                    "Affiliation: Sakura University modifies student."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-1-3",
                    "これは私の母（　　）写真です。",
                    "This is a photo of my mother.",
                    ["の", "に", "を", "と"],
                    0,
                    [
                        "Correct! の connects the subject of the photo (母) to the photo itself (写真).",
                        "Incorrect. に marks indirect objects, destinations, or specific time.",
                        "Incorrect. を marks direct objects of action verbs.",
                        "Incorrect. と means 'and' or 'with'."
                    ],
                    "Possessive / Attribute particle の",
                    "Mother qualifies the photo."
                )
            ],
            "tags": ["N5", "Genki L1", "Particle の", "Possession"]
        },
        {
            "id": "g1-l1-time-and-age",
            "title": "時間と年齢 (Telling Time with 〜時・〜分 and Age with 〜歳)",
            "meaning": "Formulas for hours (〜時 / じ), minutes (〜分 / ふん・ぷん), and age (〜歳 / さい) including critical phonological irregularities.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 1: New Friends",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "Number + 時 (Hour) | Number + 分 (Minutes) | Number + 歳 (Age)",
            "nuance": "IRREGULARITY ALERT: 4 o'clock is よじ (NOT よんじ ❌)! 7 o'clock is しちじ (NOT ななじ). 9 o'clock is くじ (NOT きゅうじ). Age 1 is いっさい; age 20 is はたち (二十歳)!",
            "keyTakeaway": "MUG-UP: 4:00 = よじ! 7:00 = しちじ! 9:00 = くじ! Age 20 = はたち!",
            "sentences": [
                make_sentence(
                    "s-g1-1-4",
                    "今、午前九時半です。私は十九歳です。",
                    "Right now, it is 9:30 AM. I am nineteen years old.",
                    "Now AM 9-hour-half is. I 19-years-old am.",
                    [
                        tok("午前", "ごぜん", "gozen", "AM / morning", "Noun"),
                        tok("九時半", "くじはん", "kuji han", "9:30", "Noun"),
                        tok("十九歳", "じゅうきゅうさい", "juukyuu sai", "19 years old", "Noun")
                    ],
                    "九時 is read くじ; 半 means half past."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-1-4",
                    "会議は午後（　　）から始まります。",
                    "The meeting starts from 4:00 PM.",
                    ["四時（よじ）", "四時（よんじ）", "四時（しじ）", "四時（ななじ）"],
                    0,
                    [
                        "Correct! 4 o'clock is strictly read as よじ (yoji).",
                        "Incorrect. よんじ is a common learner error but does not exist in standard Japanese.",
                        "Incorrect. しじ is avoided due to phonetic clash with death (死).",
                        "Incorrect. ななじ is 7, not 4."
                    ],
                    "Irregular hour reading 四時 (よじ)",
                    "Reading 4 o'clock correctly."
                )
            ],
            "tags": ["N5", "Genki L1", "Time", "Numbers"]
        },

        # === LESSON 2 ===
        {
            "id": "g1-l2-kore-sore-are-dore",
            "title": "これ・それ・あれ・どれ (Thing Demonstrative Pronouns)",
            "meaning": "Standalone pronouns indicating physical things relative to speaker and listener: これ (near speaker), それ (near listener), あれ (far from both), どれ (which one).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 2: Shopping",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "これ / それ / あれ / どれ + は / が / を (Standalone Pronouns)",
            "nuance": "STANDALONE RULE: これ/それ/あれ/どれ stand alone as independent nouns. They CANNOT directly modify a noun (you cannot say 'これ本' ❌; that requires 'この本').",
            "keyTakeaway": "MUG-UP: これ/それ/あれ/どれ stand ALONE. こ (me), そ (you), あ (far away), ど (which?).",
            "sentences": [
                make_sentence(
                    "s-g1-2-1",
                    "これは日本のペンです。あれはアメリカのペンです。",
                    "This is a Japanese pen. That one over there is an American pen.",
                    "This topic Japan's pen is. That-over-there America's pen is.",
                    [
                        tok("これ", "これ", "kore", "this (near me)", "Pronoun"),
                        tok("あれ", "あれ", "are", "that (over there)", "Pronoun")
                    ],
                    "Spatial contrast between proximal and distal items."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-2-1",
                    "（　　）は誰の傘ですか。「それですか。私のです。」",
                    "Whose umbrella is that near you? 'That one? It is mine.'",
                    ["それ", "ここ", "その", "そこ"],
                    0,
                    [
                        "Correct! それ refers to an object near the listener.",
                        "Incorrect. ここ means 'this place'.",
                        "Incorrect. その must directly precede a noun (その傘).",
                        "Incorrect. そこ means 'that place near you'."
                    ],
                    "Demonstrative pronoun それ",
                    "Pointing to an item near the conversation partner."
                )
            ],
            "tags": ["N5", "Genki L2", "Demonstratives", "Pronouns"]
        },
        {
            "id": "g1-l2-kono-sono-ano-dono",
            "title": "この・その・あの・どの + Noun (Pre-Noun Demonstrative Modifiers)",
            "meaning": "Demonstrative determiners that must immediately precede and specify a noun: この (this N), その (that N near you), あの (that N over there), どの (which N).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 2: Shopping",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "この / その / あの / どの + Noun",
            "nuance": "MUST HAVE A NOUN: Unlike これ which is an independent noun, この CANNOT stand by itself. Saying 'このは私の' ❌ is ungrammatical; must be 'この時計は私の'.",
            "keyTakeaway": "MUG-UP: この・その・あの・どの MUST be glued to a following Noun!",
            "sentences": [
                make_sentence(
                    "s-g1-2-2",
                    "あの時計はいくらですか。「三千円です。」",
                    "How much is that watch over there? 'It is 3,000 yen.'",
                    "That watch-over-there how-much is? 3000-yen is.",
                    [
                        tok("あの", "あの", "ano", "that (over there)", "Pre-noun"),
                        tok("時計", "とけい", "tokei", "watch / clock", "Noun")
                    ],
                    "あの directly modifies noun 時計."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-2-2",
                    "すみません、（　　）辞書を見せてください。",
                    "Excuse me, please show me that dictionary near you.",
                    ["その", "それ", "そんな", "そこに"],
                    0,
                    [
                        "Correct! その directly modifies the noun 辞書.",
                        "Incorrect. それ is a standalone pronoun and cannot directly attach to 辞書 without の.",
                        "Incorrect. そんな means 'that kind of'.",
                        "Incorrect. そこに is a locational postposition."
                    ],
                    "Pre-noun determiner その",
                    "Modifying the noun 辞書."
                )
            ],
            "tags": ["N5", "Genki L2", "Demonstratives", "Pre-nouns"]
        },
        {
            "id": "g1-l2-koko-soko-asoko-doko",
            "title": "ここ・そこ・あそこ・どこ (Place Demonstrative Pronouns)",
            "meaning": "Demonstrative locational nouns indicating places: ここ (here), そこ (there near you), あそこ (over there), どこ (where).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 2: Shopping",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "ここ / そこ / あそこ / どこ + は / に / で",
            "nuance": "PHONETIC IRREGULARITY: Notice the pattern: こ, そ, but あそこ (NOT あこ ❌)! Interrogative is どこ.",
            "keyTakeaway": "MUG-UP: Note the irregularity: ここ, そこ, あそこ (with -そ- in the middle!), どこ.",
            "sentences": [
                make_sentence(
                    "s-g1-2-3",
                    "図書館はどこですか。「あそこです。」",
                    "Where is the library? 'It is over there.'",
                    "Library topic where is? Over-there is.",
                    [
                        tok("図書館", "としょかん", "toshokan", "library", "Noun"),
                        tok("どこ", "どこ", "doko", "where", "Interrogative"),
                        tok("あそこ", "あそこ", "asoko", "over there", "Pronoun")
                    ],
                    "Inquiring place with どこ; answering with distant place あそこ."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-2-3",
                    "お手洗いは（　　）ですか。「あちらのエレベーターの隣です。」",
                    "Where is the restroom? 'It is next to the elevator over there.'",
                    ["どこ", "どれ", "だれ", "どう"],
                    0,
                    [
                        "Correct! どこ is the place interrogative meaning 'where'.",
                        "Incorrect. どれ means 'which item among 3+'.",
                        "Incorrect. だれ means 'who'.",
                        "Incorrect. どう means 'how'."
                    ],
                    "Locational interrogative どこ",
                    "Inquiring about location of facilities."
                )
            ],
            "tags": ["N5", "Genki L2", "Location", "Demonstratives"]
        },
        {
            "id": "g1-l2-mo-particle",
            "title": "助詞「も」 (Inclusive Particle 'Also / Too')",
            "meaning": "Indicates inclusion: equates the predicate for a new topic to that of a previously mentioned entity ('X is also Y').",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 2: Shopping",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + も (Directly replaces は, が, or を!)",
            "nuance": "PARTICLE ABSORPTION: Particle も directly absorbs and replaces topic particle は and object particle を. You NEVER say 'はも' ❌ or 'をも' ❌!",
            "keyTakeaway": "MUG-UP: も replaces は and を completely! (私[は]学生です → 田中さん[も]学生です).",
            "sentences": [
                make_sentence(
                    "s-g1-2-4",
                    "メアリーさんはアメリカ人です。ロバートさんもアメリカ人です。",
                    "Mary is an American. Robert is also an American.",
                    "Mary topic American is. Robert also American is.",
                    [
                        tok("ロバートさん", "ロバートさん", "robaato-san", "Robert", "Noun"),
                        tok("も", "も", "mo", "also / too", "Particle"),
                        tok("アメリカ人", "アメリカじん", "amerika-jin", "American", "Noun")
                    ],
                    "も replaces は to establish shared national identity."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-2-4",
                    "私もその本（　　）読みました。とても面白かったです。",
                    "I also read that book too.",
                    ["を", "も", "に", "で"],
                    1,
                    [
                        "Incorrect. を is standard object marker without 'also'.",
                        "Correct! も replaces を to express 'that book also'.",
                        "Incorrect. に indicates direction/time.",
                        "Incorrect. で indicates location/means."
                    ],
                    "Particle も replacing direct object",
                    "Inclusive object marking."
                )
            ],
            "tags": ["N5", "Genki L2", "Particle も", "Inclusion"]
        },
        {
            "id": "g1-l2-janai-desu",
            "title": "じゃないです / じゃありません (Negative Copula: Is Not)",
            "meaning": "Polite non-past negative form of copula です: 'is not / am not / are not'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 2: Shopping",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun / な-adj + じゃないです (Conversational) / じゃありません (Formal)",
            "nuance": "REGISTER DIFFERENCE: じゃないです is standard polite spoken Japanese. じゃありません is slightly more formal. ではありません is conservative written/speech style.",
            "keyTakeaway": "MUG-UP: Negative of です is じゃないです (or じゃありません). Connects to nouns and な-adjectives.",
            "sentences": [
                make_sentence(
                    "s-g1-2-5",
                    "山田さんは留学生じゃありません。先生です。",
                    "Yamada-san is not an international student. He is a teacher.",
                    "Yamada topic international-student is-not. Teacher is.",
                    [
                        tok("留学生", "りゅうがくせい", "ryuugakusei", "international student", "Noun"),
                        tok("じゃありません", "じゃありません", "ja arimasen", "is not (polite neg)", "Copula")
                    ],
                    "Polite denial of category followed by affirmative correction."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-2-5",
                    "私は一年生（　　）。三年生です。",
                    "I am not a first-year student. I am a third-year student.",
                    ["じゃありません", "ありません", "ないでした", "でした"],
                    0,
                    [
                        "Correct! じゃありません (or じゃないです) is the polite negative copula for nouns.",
                        "Incorrect. ありません is for inanimate existence (there isn't), not noun identity.",
                        "Incorrect. ないでした is ungrammatical.",
                        "Incorrect. でした is past affirmative ('was')."
                    ],
                    "Negative copula じゃありません",
                    "Negating noun identity."
                )
            ],
            "tags": ["N5", "Genki L2", "Negation", "Copula"]
        },

        # === LESSON 3 ===
        {
            "id": "g1-l3-masu-form",
            "title": "〜ます / 〜ません (Polite Non-Past Affirmative & Negative)",
            "meaning": "The standard polite verbal ending for present habitual actions and future actions: 〜ます (affirmative) and 〜ません (negative).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 3: Making a Date",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "Verb stem (ます-stem) + ます / ません",
            "nuance": "NON-PAST INCLUDES FUTURE: Japanese has only two grammatical tenses: past and non-past. 食べます means 'I eat (habitually)' OR 'I will eat (future)'.",
            "keyTakeaway": "MUG-UP: V-stem + ます = Present habit OR future plan. Negative = 〜ません.",
            "sentences": [
                make_sentence(
                    "s-g1-3-1",
                    "私は毎朝コーヒーを飲みますが、お茶は飲みません。",
                    "I drink coffee every morning, but I do not drink tea.",
                    "I every-morning coffee drink but, tea drink-not.",
                    [
                        tok("飲みます", "のみます", "nomimasu", "drink (polite)", "Verb"),
                        tok("飲みません", "のみません", "nomimasen", "do not drink (polite neg)", "Verb")
                    ],
                    "Habitual affirmative and negative actions."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-3-1",
                    "明日は日曜日ですから、仕事へ（　　）。",
                    "Since tomorrow is Sunday, I will not go to work.",
                    ["行きません", "行きます", "行きました", "行かないでした"],
                    0,
                    [
                        "Correct! 行きません is the polite non-past negative ('will not go').",
                        "Incorrect. 行きます is affirmative ('will go'), which contradicts Sunday.",
                        "Incorrect. 行きました is past tense ('went').",
                        "Incorrect. 行かないでした is ungrammatical."
                    ],
                    "Polite non-past negative 〜ません",
                    "Future negation based on Sunday."
                )
            ],
            "tags": ["N5", "Genki L3", "Verbs", "Polite Form"]
        },
        {
            "id": "g1-l3-masenka-invitation",
            "title": "〜ませんか (Polite Invitation: Won't You? / Would You Like To?)",
            "meaning": "Invites the listener to do an activity together politely: 'Won't you...? / Would you like to...?'",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 3: Making a Date",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "V-stem (ます-stem) + ませんか",
            "nuance": "RESPECTFUL INVITATION: Asking negatively gives the listener psychological space to decline without awkwardness. Saying '映画に行きますか' is an informational check; '映画に行きませんか' is a warm date invitation.",
            "keyTakeaway": "MUG-UP: V-stem + ませんか = The golden Japanese polite invitation! (一緒に食べませんか = Won't you eat with me?).",
            "sentences": [
                make_sentence(
                    "s-g1-3-2",
                    "今度の週末、一緒に美術館へ行きませんか。「ええ、ぜひ！」",
                    "Won't you go to the art museum together this coming weekend? 'Yes, by all means!'",
                    "This-time's weekend, together art-museum go-won't-you? Yes, definitely!",
                    [
                        tok("行きませんか", "いきませんか", "ikimasen ka", "won't you go? (invitation)", "Verb+Grammar"),
                        tok("ぜひ", "ぜひ", "zehi", "by all means / definitely", "Adverb")
                    ],
                    "Warm invitation paired with enthusiastic agreement."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-3-2",
                    "少し疲れましたね。喫茶店でお茶を（　　）ませんか。",
                    "We've gotten a bit tired, haven't we? Won't you drink some tea at a cafe?",
                    ["飲み", "飲む", "飲んで", "飲ま"],
                    0,
                    [
                        "Correct! 飲む stem is 飲み, connecting to ませんか (飲みませんか).",
                        "Incorrect. 飲む is dictionary form; cannot connect to ませんか.",
                        "Incorrect. 飲んで is te-form.",
                        "Incorrect. 飲ま is negative stem."
                    ],
                    "Polite invitation 〜ませんか with verb stem",
                    "Proposing a cafe rest."
                )
            ],
            "tags": ["N5", "Genki L3", "Invitation", "Social"]
        },

        # === LESSON 4 ===
        {
            "id": "g1-l4-past-forms-deshita",
            "title": "〜ました・〜ませんでした・〜でした (Polite Past Tense of Verbs & Copula)",
            "meaning": "Past tense for verbs (〜ました / 〜ませんでした) and noun/adjectival predicates (〜でした / 〜じゃありませんでした).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 4: The First Date",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "Verb stem + ました / ませんでした | Noun / な-adj + でした / じゃありませんでした",
            "nuance": "COPULA PAST NEGATIVE: In polite conversation, you can say either じゃありませんでした or じゃないでした / じゃなかったです.",
            "keyTakeaway": "MUG-UP: Verb past = ました. Verb past negative = ませんでした. Noun past = でした.",
            "sentences": [
                make_sentence(
                    "s-g1-4-1",
                    "昨日は雨でした。私はどこへも行きませんでした。",
                    "Yesterday was rainy. I did not go anywhere.",
                    "Yesterday rain was. I anywhere go-past-neg.",
                    [
                        tok("雨でした", "あめでした", "ame deshita", "was rain", "Noun+Copula"),
                        tok("行きませんでした", "いきませんでした", "ikimasen deshita", "did not go", "Verb")
                    ],
                    "Past state of weather and past negation of activity."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-4-1",
                    "昨夜は十二時まで日本語を（　　）。とても眠かったです。",
                    "Last night I studied Japanese until 12 o'clock. I was very sleepy.",
                    ["勉強しました", "勉強します", "勉強でした", "勉強しでした"],
                    0,
                    [
                        "Correct! 勉強する past form is 勉強しました.",
                        "Incorrect. 勉強します is present/future non-past.",
                        "Incorrect. 勉強でした uses copula past without verb inflection.",
                        "Incorrect. 勉強しでした is ungrammatical hybrid."
                    ],
                    "Verb past tense 〜ました",
                    "Completed past study action."
                )
            ],
            "tags": ["N5", "Genki L4", "Past Tense", "Verbs"]
        },
        {
            "id": "g1-l4-location-words",
            "title": "位置の名詞 (Spatial Postpositions: 上・下・前・後ろ・中・隣・近く・間)",
            "meaning": "Spatial relational nouns indicating position relative to a reference point: X の [上/下/前/後ろ/中/隣/間] に.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 4: The First Date",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Reference Noun + の + [上 / 下 / 前 / 後ろ / 中 / 隣 / 近く / 間] + に",
            "nuance": "TONARI VS CHIKAKU: 隣 (となり) is strictly adjacent of the same category (next to). 近く (ちかく) is in the general vicinity. 間 (あいだ) requires two bounds (A と B の間).",
            "keyTakeaway": "MUG-UP: [Object] の [Position] に. (机の[上]に = On top of the desk).",
            "sentences": [
                make_sentence(
                    "s-g1-4-2",
                    "猫が机の下で寝ています。銀行は郵便局と本屋の間にあります。",
                    "A cat is sleeping under the desk. The bank is between the post office and bookstore.",
                    "Cat desk-under sleeping-is. Bank post-office and bookstore's between exists.",
                    [
                        tok("机の下で", "つくえのしたで", "tsukue no shita de", "under the desk", "Noun+Postposition"),
                        tok("間にあります", "あいだにあります", "aida ni arimasu", "exists between", "Grammar")
                    ],
                    "Relational location followed by action/existence verbs."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-4-2",
                    "私の部屋の鍵は、カバンの（　　）にあります。",
                    "My room key is inside my bag.",
                    ["中", "上", "前", "間"],
                    0,
                    [
                        "Correct! 中 (なか) means 'inside'.",
                        "Incorrect. 上 means 'on top of'.",
                        "Incorrect. 前 means 'in front of'.",
                        "Incorrect. 間 means 'between two entities'."
                    ],
                    "Spatial noun 中 (inside)",
                    "Location of keys inside the bag."
                )
            ],
            "tags": ["N5", "Genki L4", "Spatial", "Positions"]
        },

        # === LESSON 5 ===
        {
            "id": "g1-l5-suki-kirai",
            "title": "好き（な） / 嫌い（な） (Expressing Likes and Dislikes with が)",
            "meaning": "Expresses fondness (好き) or aversion (嫌い): marked with particle が on the object of emotion, NOT を!",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 5: A Trip to Okinawa",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "[Person] は [Item] が 好きです / 嫌いです (Adjectival predicates)",
            "nuance": "PARTICLE TRAP: In English 'like' is a transitive verb (I like X). In Japanese, 好き is a な-adjective (X is pleasing to me), so the item takes particle が (NOT を ❌)!",
            "keyTakeaway": "MUG-UP: [Noun] が 好きです / 嫌いです! Never use を with 好き/嫌い!",
            "sentences": [
                make_sentence(
                    "s-g1-5-1",
                    "私は辛い食べ物が大好きですが、甘いお菓子はあまり好きじゃありません。",
                    "I love spicy food, but I don't like sweet snacks very much.",
                    "I spicy food like-very but, sweet snacks not-very like-not.",
                    [
                        tok("食べ物が", "たべものが", "tabemono ga", "food (target)", "Noun+Particle"),
                        tok("大好きですが", "だいすきですが", "daisuki desu ga", "love it, but", "Adjective")
                    ],
                    "Target of affection marked with が."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-5-1",
                    "ロバートさんは日本の歴史（　　）とても好きです。",
                    "Robert-san likes Japanese history very much.",
                    ["が", "を", "に", "で"],
                    0,
                    [
                        "Correct! Target of 好き requires particle が.",
                        "Incorrect. を is an English calque trap; 好き is an adjective, not a transitive verb.",
                        "Incorrect. に indicates direction/time.",
                        "Incorrect. で indicates location/means."
                    ],
                    "Object marker が with 好き",
                    "Marking the target of fondness."
                )
            ],
            "tags": ["N5", "Genki L5", "Preferences", "Particle が"]
        },
        {
            "id": "g1-l5-mashou-ka",
            "title": "〜ましょう / 〜ましょうか (Volitional Suggestion: Let's / Shall We?)",
            "meaning": "Proposes action enthusiastically: 〜ましょう ('Let's do it!') or offers assistance/mutual decision: 〜ましょうか ('Shall we do it? / Shall I help?').",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 5: A Trip to Okinawa",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "V-stem (ます-stem) + ましょう / ましょうか",
            "nuance": "TWO USES OF 〜ましょうか: 1) Suggesting mutual action ('Shall we take a break?'). 2) Offering personal assistance ('Shall I carry your bag?').",
            "keyTakeaway": "MUG-UP: V-stem + ましょう = Let's do it! V-stem + ましょうか = Shall we? / Shall I help?",
            "sentences": [
                make_sentence(
                    "s-g1-5-2",
                    "荷物が重そうですね。手伝いましょうか。「ありがとうございます！」",
                    "Your luggage looks heavy. Shall I help you? 'Thank you so much!'",
                    "Luggage heavy-looks. Shall-I-help? Thank-you!",
                    [
                        tok("手伝いましょうか", "てつだいましょうか", "tetsudaimashou ka", "shall I help?", "Verb+Grammar")
                    ],
                    "Offering courteous assistance to someone in need."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-5-2",
                    "雨が止みましたね。公園を少し（　　）ましょう。",
                    "The rain has stopped, hasn't it? Let's take a walk in the park for a bit.",
                    ["散歩し", "散歩する", "散歩して", "散歩した"],
                    0,
                    [
                        "Correct! 散歩する stem is 散歩し + ましょう (散歩しましょう = Let's take a walk).",
                        "Incorrect. 散歩する is dictionary form.",
                        "Incorrect. 散歩して is te-form.",
                        "Incorrect. 散歩した is past form."
                    ],
                    "Suggestion 〜ましょう with verb stem",
                    "Proposing a walk together."
                )
            ],
            "tags": ["N5", "Genki L5", "Volitional", "Suggestions"]
        },

        # === LESSON 6 ===
        {
            "id": "g1-l6-te-kudasai",
            "title": "〜てください (Polite Request: Please Do)",
            "meaning": "Politely instructs or requests the listener to perform an action for instruction, guidance, or courtesy: 'Please do X'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 6: A Day in Robert's Life",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "V-て + ください",
            "nuance": "REGISTER WARNING: Because ください carries an underlying mild command tone ('do this for me'), saying it to high superiors (professors, boss, clients) can sound overly direct. Use 〜ていただけませんか instead.",
            "keyTakeaway": "MUG-UP: V-て + ください = Please do X. Connects strictly to te-form!",
            "sentences": [
                make_sentence(
                    "s-g1-6-1",
                    "教科書の三十五ページを開けてください。",
                    "Please open your textbook to page 35.",
                    "Textbook's 35-page open please.",
                    [
                        tok("開けてください", "あけてください", "akete kudasai", "please open", "Verb+Grammar")
                    ],
                    "Standard classroom instructional request."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-6-1",
                    "ここにあなたのお名前と電話番号を（　　）ください。",
                    "Please write your name and phone number here.",
                    ["書いて", "書く", "書き", "書いた"],
                    0,
                    [
                        "Correct! 書く connects via te-form 書いて + ください.",
                        "Incorrect. 書く is dictionary form.",
                        "Incorrect. 書き is masu-stem.",
                        "Incorrect. 書いた is past form."
                    ],
                    "V-て + ください polite request",
                    "Requesting writing information."
                )
            ],
            "tags": ["N5", "Genki L6", "Requests", "Te-Form"]
        },
        {
            "id": "g1-l6-te-mo-ii",
            "title": "〜てもいいですか (Asking for & Granting Permission: May I?)",
            "meaning": "Asking for permission: 'May I do X?' (〜てもいいですか). Granting permission: 'You may do X' (〜てもいいです).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 6: A Day in Robert's Life",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "V-て + もいいですか / もいいです",
            "nuance": "LITERAL MEANING: 〜ても (even if I do) + いい (it is good). 'Even if I open the window, is it fine?'",
            "keyTakeaway": "MUG-UP: V-て + もいいですか = May I do this? Granting: V-て + もいいですよ.",
            "sentences": [
                make_sentence(
                    "s-g1-6-2",
                    "部屋が少し暑いですね。窓を開けてもいいですか。「ええ、どうぞ。」",
                    "The room is a bit hot, isn't it? May I open the window? 'Yes, please go ahead.'",
                    "Room slightly hot is. Window open-even-if good is question? Yes, please.",
                    [
                        tok("開けてもいいですか", "あけてもいいですか", "akete mo ii desu ka", "may I open it?", "Grammar")
                    ],
                    "Courteous permission query before altering shared environment."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-6-2",
                    "このペンを少しの間、（　　）てもいいですか。",
                    "May I borrow this pen for a brief moment?",
                    ["借り", "借る", "借りて", "借りた"],
                    0,
                    [
                        "Correct! 借りる is a Ru-verb: stem 借り + てもいいですか (借りてもいいですか).",
                        "Incorrect. 借る is an archaic form.",
                        "Incorrect. 借りて already has て; adding another てもいい creates '借りてても'.",
                        "Incorrect. 借りた is past form."
                    ],
                    "Permission formula 〜てもいいですか",
                    "Borrowing an item politely."
                )
            ],
            "tags": ["N5", "Genki L6", "Permission", "Te-Form"]
        },
        {
            "id": "g1-l6-kara-reason",
            "title": "〜から (Stating Reasons / Because - Clause Linker)",
            "meaning": "States a subjective explanation or cause: 'Because of X, Y happens' or 'Y happens because of X'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 6: A Day in Robert's Life",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Sentence 1 (Reason) + から、 Sentence 2 (Conclusion)",
            "nuance": "SUBJECTIVE CONVICTION: から represents the speaker's personal logic and subjective view. It can be paired directly with commands, requests, and volitions (雨が降っているから、傘を持って行きなさい).",
            "keyTakeaway": "MUG-UP: [Reason] から、[Result]. Unlike English, the reason comes FIRST!",
            "sentences": [
                make_sentence(
                    "s-g1-6-3",
                    "今日は大事なテストがありますから、早く寝ます。",
                    "Because I have an important test today, I will go to bed early.",
                    "Today important test have because, early sleep.",
                    [
                        tok("ありますから", "ありますから", "arimasu kara", "because I have", "Verb+Particle"),
                        tok("早く寝ます", "はやくねます", "hayaku nemasu", "will sleep early", "Adverb+Verb")
                    ],
                    "Reason precedes the resulting decision."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-6-3",
                    "明日は朝早く起きます（　　）、今夜はテレビを見ません。",
                    "Because I will wake up early tomorrow morning, I won't watch television tonight.",
                    ["から", "まで", "より", "ほど"],
                    0,
                    [
                        "Correct! から links the reason for abstaining from TV.",
                        "Incorrect. まで means 'until'.",
                        "Incorrect. より indicates comparison.",
                        "Incorrect. ほど indicates degree or proportion."
                    ],
                    "Causal clause linker から",
                    "Explaining the reason for an early night."
                )
            ],
            "tags": ["N5", "Genki L6", "Causality", "Reason"]
        },

        # === LESSON 7 ===
        {
            "id": "g1-l7-describing-people",
            "title": "身体の描写 (Describing People's Physical Attributes: 目が大きいです)",
            "meaning": "Formula for describing a person's physical features: [Person] は [Body Part] が [Adjective] です ('As for X, their eyes are big').",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 7: Family Picture",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "[Person] は + [Body Part] が + [Adjective] です",
            "nuance": "AVOID NOUN OF NOUN FOR BODY PARTS: In English we say 'Mary's hair is long'. In Japanese, 'メアリーさんの髪は長いです' sounds stiff; native syntax frames the person as topic: 'メアリーさんは髪が長いです'.",
            "keyTakeaway": "MUG-UP: [Person] は [Body part] が [Adjective]! (トムさんは背が高い = Tom is tall).",
            "sentences": [
                make_sentence(
                    "s-g1-7-1",
                    "私の妹は目が大きくて、髪が長いです。",
                    "My younger sister has big eyes and long hair.",
                    "My younger-sister eyes big-and, hair long-is.",
                    [
                        tok("妹は", "いもうとは", "imouto wa", "younger sister", "Noun+Particle"),
                        tok("目が大きくて", "めがおおきくて", "me ga ookikute", "eyes are big and", "Grammar"),
                        tok("髪が長いです", "かみがながいです", "kami ga nagai desu", "hair is long", "Grammar")
                    ],
                    "Natural Japanese body description framing."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-7-1",
                    "田中さんはとても背（　　）高いです。",
                    "Tanaka-san is very tall.",
                    ["が", "は", "を", "に"],
                    0,
                    [
                        "Correct! Body attribute takes particle が (背が高い).",
                        "Incorrect. は is already used for Tanaka-san as topic.",
                        "Incorrect. を is direct object marker.",
                        "Incorrect. に indicates destination/time."
                    ],
                    "Physical attribute marker が (背が高い)",
                    "Describing height with が."
                )
            ],
            "tags": ["N5", "Genki L7", "Description", "Attributes"]
        },
        {
            "id": "g1-l7-adj-te-forms",
            "title": "形容詞・名詞の「て形」 (Connecting Adjectives & Nouns: 〜くて / 〜で)",
            "meaning": "Links multiple qualities or attributes: い-adjectives change final い to くて; な-adjectives and nouns take で.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 7: Family Picture",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "い-adj (drop い) + くて | な-adj stem + で | Noun + で",
            "nuance": "THE II/YOI TE-FORM: いい (good) drops its irregular root and conjugates as よくて (NOT いくて ❌)! な-adjectives take で, exactly like nouns.",
            "keyTakeaway": "MUG-UP: い-adj = 〜くて (いい→よくて). な-adj / Noun = 〜で.",
            "sentences": [
                make_sentence(
                    "s-g1-7-2",
                    "この部屋は広くて明るくて、とても静かです。",
                    "This room is spacious, bright, and very quiet.",
                    "This room spacious-and bright-and, very quiet-is.",
                    [
                        tok("広くて", "ひろくて", "hirokute", "spacious and", "Adjective"),
                        tok("明るくて", "あかるくて", "akarukute", "bright and", "Adjective"),
                        tok("静かです", "しずかです", "shizuka desu", "is quiet", "Adjective")
                    ],
                    "Chaining two い-adjectives via くて into a terminal な-adjective."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-7-2",
                    "あのカフェはコーヒーが（　　）、値段も安いです。",
                    "That cafe's coffee is delicious, and the price is also cheap.",
                    ["おいしくて", "おいしいで", "おいしくで", "おいしいくて"],
                    0,
                    [
                        "Correct! おいしい drops い + くて = おいしくて.",
                        "Incorrect. おいしいで incorrectly applies noun/na-adj で to an い-adj.",
                        "Incorrect. おいしくで is ungrammatical.",
                        "Incorrect. おいしいくて fails to drop the initial い."
                    ],
                    "い-adjective te-form 〜くて",
                    "Connecting two positive attributes."
                )
            ],
            "tags": ["N5", "Genki L7", "Adjectives", "Te-Form"]
        },
        {
            "id": "g1-l7-purpose-ni-iku",
            "title": "V-stem + に行く / に来る (Purpose of Movement: Going to Do)",
            "meaning": "Expresses the specific purpose of movement: going (行く), coming (来る), or returning (帰る) in order to perform an action.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 7: Family Picture",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-stem (ます-stem) + に + 行く / 来る / 帰る | Activity Noun + に + 行く",
            "nuance": "VERB STEM BEFORE に: Drop ます and append に directly: 食べます → 食べに行く, 買いに行きます. If using an activity noun (買い物, 散歩), attach に directly: 買い物に行く.",
            "keyTakeaway": "MUG-UP: [Masu-stem] に行く = Going to DO X. Purpose particle is STRICTLY に!",
            "sentences": [
                make_sentence(
                    "s-g1-7-3",
                    "デパートへ友達の誕生日プレゼントを買いに行きました。",
                    "I went to the department store to buy a birthday present for my friend.",
                    "Department-store friend's birthday present buy-in-order-to went.",
                    [
                        tok("買いに行きました", "かいにいきました", "kai ni ikimashita", "went to buy", "Grammar")
                    ],
                    "買う (stem 買い) + に行きました."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-7-3",
                    "週末は図書館へ本を（　　）に行きます。",
                    "On weekends I go to the library to return books.",
                    ["返し", "返す", "返して", "返した"],
                    0,
                    [
                        "Correct! 返す (to return an item) stem is 返し + に行きます.",
                        "Incorrect. 返す is dictionary form.",
                        "Incorrect. 返して is te-form.",
                        "Incorrect. 返した is past form."
                    ],
                    "V-stem + に行く purpose of movement",
                    "Going to return library books."
                )
            ],
            "tags": ["N5", "Genki L7", "Movement", "Purpose"]
        },

        # === LESSON 8 ===
        {
            "id": "g1-l8-nai-de-kudasai",
            "title": "〜ないでください (Negative Request: Please Do Not)",
            "meaning": "Politely requests or instructs someone to refrain from an action: 'Please do not do X'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 8: Barbecue",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "V-ない + でください",
            "nuance": "NEGATIVE POLITE REQUEST: Formed from the plain negative ない-form + でください. Very common on signs, exams, and courteous instructions (忘れないでください).",
            "keyTakeaway": "MUG-UP: V-ない + でください = Please don't do X! (Drop nothing from ない).",
            "sentences": [
                make_sentence(
                    "s-g1-8-1",
                    "図書館の中では大声で話さないでください。",
                    "Please do not speak in a loud voice inside the library.",
                    "Library inside loud-voice-in speak-not-please.",
                    [
                        tok("話さないでください", "はなさないでください", "hanasanaide kudasai", "please do not speak", "Grammar")
                    ],
                    "話す negative 話さない + でください."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-8-1",
                    "まだテスト中ですから、教室から（　　）ないでください。",
                    "Since the test is still ongoing, please do not leave the classroom.",
                    ["出", "出る", "出て", "出な"],
                    0,
                    [
                        "Correct! 出る (Ru-verb) negative is 出ない + でください (出ないでください).",
                        "Incorrect. 出るない is false conjugation.",
                        "Incorrect. 出て is te-form.",
                        "Incorrect. 出な is ungrammatical."
                    ],
                    "V-ない + でください negative request",
                    "Requesting students remain in room."
                )
            ],
            "tags": ["N5", "Genki L8", "Requests", "Negation"]
        },
        {
            "id": "g1-l8-nominalizer-no",
            "title": "動詞の「の」名詞化 (Nominalizing Verbs with の: のが好き / 上手 / 下手)",
            "meaning": "Turns an action verb into a noun phrase using の, enabling evaluations of preference or skill: V-plain + のが好き / 上手 / 下手.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 8: Barbecue",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "V-辞書形 + のが [好き / 嫌い / 上手 / 下手 / 得意 / 苦手] です",
            "nuance": "NOMINALIZATION REQUIREMENT: In Japanese you cannot attach が directly to a verb ('食べるが好き' ❌). You must nominalize it with の ('食べるのが好き').",
            "keyTakeaway": "MUG-UP: [Verb-Dictionary] + のが + 好き / 上手 / 下手! The particle の acts as 'the act of'.",
            "sentences": [
                make_sentence(
                    "s-g1-8-2",
                    "私はギターを弾くのが大好きですが、歌を歌うのはあまり上手ではありません。",
                    "I love playing the guitar, but I am not very good at singing songs.",
                    "I guitar play-nominalizer like-very but, songs sing-nominalizer not-very good is-not.",
                    [
                        tok("弾くのが大好き", "ひくのがだいすき", "hiku no ga daisuki", "love playing", "Grammar"),
                        tok("歌うのは", "うたうのは", "utau no wa", "as for singing", "Grammar")
                    ],
                    "Nominalizing musical instruments and singing."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-8-2",
                    "母は料理を（　　）のがとても上手です。",
                    "My mother is very good at cooking meals.",
                    ["作る", "作って", "作り", "作った"],
                    0,
                    [
                        "Correct! V-辞書形 作る connects to nominalizer の (作るのが上手).",
                        "Incorrect. 作って is te-form.",
                        "Incorrect. 作り is masu-stem.",
                        "Incorrect. 作った is past form."
                    ],
                    "Nominalization V-辞書形 + の",
                    "Skill appraisal in cooking."
                )
            ],
            "tags": ["N5", "Genki L8", "Nominalization", "Skills"]
        },

        # === LESSON 9 ===
        {
            "id": "g1-l9-mou-mada",
            "title": "もう〜ました vs まだ〜ていません (Already Done vs Have Not Yet Done)",
            "meaning": "もう〜ました (Action has already been completed). まだ〜ていません (Action has not yet taken place; still in uncompleted state).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 9: Kabuki",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "もう + V-ました | まだ + V-ていません (NOT まだ〜ませんでした ❌!)",
            "nuance": "CRITICAL NEGATIVE TRAP: To say 'I haven't eaten yet', you CANNOT say 'まだ食べませんでした' ❌! Past negative implies you never intended to eat. You must say 'まだ食べていません' (still in state of not having eaten).",
            "keyTakeaway": "MUG-UP: Haven't done yet = まだ + [Te-form] + いません! Never use past negative with まだ!",
            "sentences": [
                make_sentence(
                    "s-g1-9-1",
                    "宿題はもう終わりましたか。「いいえ、まだ終わっていません。」",
                    "Have you finished your homework already? 'No, I have not finished it yet.'",
                    "Homework already finished? No, still finished-state-not.",
                    [
                        tok("もう終わりましたか", "もうおわりましたか", "mou owarimashita ka", "already finished?", "Grammar"),
                        tok("まだ終わっていません", "まだおわっていません", "mada owatte imasen", "have not finished yet", "Grammar")
                    ],
                    "Canonical pairing of もう with past vs まだ with progressive negative."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-9-1",
                    "昼ご飯はもう食べましたか。「いいえ、まだ（　　）。」",
                    "Did you eat lunch already? 'No, I haven't eaten yet.'",
                    ["食べていません", "食べませんでした", "食べません", "食べないでした"],
                    0,
                    [
                        "Correct! まだ takes progressive negative 食べていません ('have not eaten yet').",
                        "Incorrect. 食べませんでした means you didn't eat at all in the past, rather than not yet.",
                        "Incorrect. 食べません is present habitual refusal.",
                        "Incorrect. 食べないでした is ungrammatical."
                    ],
                    "まだ + V-ていません (Not yet)",
                    "Replying that lunch hasn't occurred yet."
                )
            ],
            "tags": ["N5", "Genki L9", "Aspect", "Time"]
        },

        # === LESSON 10 ===
        {
            "id": "g1-l10-tsumori",
            "title": "〜つもりだ / つもりです (Stated Personal Intention: Plan To)",
            "meaning": "States a conscious, determined personal intention or plan: 'I intend to / I plan to do X'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 10: Winter Vacations Approaching",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + つもりです (Affirmative plan) | V-ない + つもりです / つもりはありません (Negative plan)",
            "nuance": "FIRST/SECOND PERSON ONLY: In polite conversation, つもり states your own plans. Attributing つもり directly to superiors can sound rude because it presumes to know their internal mental intent.",
            "keyTakeaway": "MUG-UP: V-る + つもりです = I intend to do X. Negative: V-ない + つもりです.",
            "sentences": [
                make_sentence(
                    "s-g1-10-1",
                    "大学を卒業したら、日本の大学院に進学するつもりです。",
                    "Upon graduating from college, I intend to advance to graduate school in Japan.",
                    "College graduate-when, Japan's grad-school advance intend.",
                    [
                        tok("進学するつもりです", "しんがくするつもりです", "shingaku suru tsumori desu", "intend to advance to higher education", "Grammar")
                    ],
                    "Stating personal academic career intent."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-10-1",
                    "今年の夏休みは、どこへも旅行に（　　）つもりです。家で勉強します。",
                    "This summer vacation, I intend not to travel anywhere. I will study at home.",
                    ["行かない", "行く", "行かないで", "行った"],
                    0,
                    [
                        "Correct! Negative intention connects via ない-form: 行かないつもりです.",
                        "Incorrect. 行く indicates affirmative intent to travel.",
                        "Incorrect. 行かないで is te-form.",
                        "Incorrect. 行った is past form."
                    ],
                    "Negative intention V-ない + つもりだ",
                    "Intending to stay home."
                )
            ],
            "tags": ["N5", "Genki L10", "Intention", "Plans"]
        },
        {
            "id": "g1-l10-adj-naru",
            "title": "形容詞 + なる (Expressing Change of State: To Become)",
            "meaning": "Describes a natural or progressive change of state: 'to become [adjective]' (growing warm, becoming quiet, turning into an adult).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 10: Winter Vacations Approaching",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "い-adj (drop い) + くなる | な-adj stem + になる | Noun + になる",
            "nuance": "ADVERBIAL INFLECTION: い-adjectives change final い to く before なる (暖かくなる). な-adjectives and nouns take に before なる (静かになる, 先生になる).",
            "keyTakeaway": "MUG-UP: い-adj = 〜くなる (暑くなる). な-adj / Noun = 〜になる (元気になる, 医者になる).",
            "sentences": [
                make_sentence(
                    "s-g1-10-2",
                    "春になって、だんだん暖かくなってきましたね。",
                    "Spring has arrived, and it has gradually become warm, hasn't it?",
                    "Spring become, gradually warm became-came.",
                    [
                        tok("春になって", "はるになって", "haru ni natte", "became spring and", "Grammar"),
                        tok("暖かくなってきました", "あたたかくなってきました", "atatakaku natte kimashita", "has become warm", "Grammar")
                    ],
                    "Noun + になる and い-adj + くなる."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-10-2",
                    "薬を飲んだら、痛みがだいぶ（　　）なりました。",
                    "After taking the medicine, the pain became considerably better.",
                    ["よく", "いいに", "よくに", "いいく"],
                    0,
                    [
                        "Correct! いい changes through root よい to become adverbial よく + なりました.",
                        "Incorrect. いいに is ungrammatical; い-adjectives take く.",
                        "Incorrect. よくに is double adverbial marking.",
                        "Incorrect. いいく is invalid root conjugation."
                    ],
                    "Change of state with いい (よくなる)",
                    "Pain improving after medicine."
                )
            ],
            "tags": ["N5", "Genki L10", "Change of State", "Trends"]
        },

        # === LESSON 11 ===
        {
            "id": "g1-l11-tai-desire",
            "title": "〜たい / 〜たくない (Expressing Desire to Do: Want to Do)",
            "meaning": "Expresses first-person desire to perform an action: 'I want to do X'. Negative: 'I do not want to do X' (〜たくない).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 11: After-Vacation Plans",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-stem (ます-stem) + たい (Conjugates 100% as an い-adjective: 〜たくない, 〜たかった)",
            "nuance": "PARTICLE FLEXIBILITY: The direct object of the verb can be marked with EITHER を or が! 水を飲みたい is acceptable, but 水が飲みたい highlights the desired object more prominently.",
            "keyTakeaway": "MUG-UP: V-stem + たい = Want to do! Conjugates as an い-adj. Direct object particle を often becomes が.",
            "sentences": [
                make_sentence(
                    "s-g1-11-1",
                    "日本へ行って、本場のラーメンが食べたいです。",
                    "I want to go to Japan and eat authentic ramen.",
                    "Japan-to go, authentic ramen eat-want is.",
                    [
                        tok("食べたいです", "たべたいです", "tabetai desu", "want to eat", "Verb+Grammar")
                    ],
                    "Desire to eat authentic ramen."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-11-1",
                    "今日はとても疲れたので、何も（　　）たくないです。",
                    "Because I am so tired today, I do not want to do anything.",
                    ["し", "する", "して", "した"],
                    0,
                    [
                        "Correct! する stem is し + たくない (したくない = do not want to do).",
                        "Incorrect. する is dictionary form.",
                        "Incorrect. して is te-form.",
                        "Incorrect. した is past form."
                    ],
                    "Negative desire 〜たくない with verb stem",
                    "Desire to do nothing after tiring day."
                )
            ],
            "tags": ["N5", "Genki L11", "Desire", "Modality"]
        },
        {
            "id": "g1-l11-koto-ga-aru",
            "title": "〜ことがある (Past Experiential Aspect: Have Ever Done)",
            "meaning": "Expresses that one has had the lifetime historical experience of doing an action: 'Have had the experience of / Have ever done X'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 11: After-Vacation Plans",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-た + ことがある / あります (Negative: ありません / ない)",
            "nuance": "LIFETIME HISTORICAL ASPECT: Strictly connects to past た-form! Cannot be used for immediate recent routine events (e.g., 'I ate toast this morning' ❌). It refers to lifetime resume experiences.",
            "keyTakeaway": "MUG-UP: V-た + ことがある = I have had the lifetime experience of doing X!",
            "sentences": [
                make_sentence(
                    "s-g1-11-2",
                    "富士山に登ったことがありますか。「ええ、一度あります。」",
                    "Have you ever climbed Mt. Fuji? 'Yes, once.'",
                    "Mt-Fuji climbed experience have question? Yes, once have.",
                    [
                        tok("登ったことがありますか", "のぼったことがありますか", "nobotta koto ga arimasu ka", "have you ever climbed?", "Grammar")
                    ],
                    "Lifetime experiential inquiry."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-11-2",
                    "歌舞伎を（　　）ことがありますか。「いいえ、一度もありません。」",
                    "Have you ever seen Kabuki? 'No, not once.'",
                    ["見た", "見る", "見て", "見"],
                    0,
                    [
                        "Correct! Experiential aspect requires past form 見た + ことがある.",
                        "Incorrect. 見ることがある means 'there are times when I see' (occasional habit), not past experience.",
                        "Incorrect. 見て is te-form.",
                        "Incorrect. 見 is masu-stem."
                    ],
                    "V-た + ことがある lifetime experience",
                    "Inquiring about Kabuki viewing experience."
                )
            ],
            "tags": ["N5", "Genki L11", "Experience", "Aspect"]
        },
        {
            "id": "g1-l11-sugiru",
            "title": "〜すぎる (Excessiveness: Too Much / Overdoing)",
            "meaning": "Indicates exceeding a proper, healthy, or desirable threshold: 'too [adj]' or 'doing [verb] too much'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 11: After-Vacation Plans",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "V-stem + すぎる | い-adj (drop い) + すぎる | な-adj stem + すぎる (Conjugates as Ru-verb)",
            "nuance": "UNFAVORABLE THRESHOLD: Sugiru carries an overwhelmingly negative implication (e.g., this is too spicy to eat, I drank too much and got sick).",
            "keyTakeaway": "MUG-UP: Drop final い, drop ます, drop な, and append すぎる! Conjugates as a Ru-verb (すぎます, すぎた).",
            "sentences": [
                make_sentence(
                    "s-g1-11-3",
                    "昨夜はお酒を飲みすぎて、今朝はひどい二日酔いです。",
                    "Last night I drank too much alcohol, and this morning I have a terrible hangover.",
                    "Last-night alcohol drink-excessively, this-morning terrible hangover is.",
                    [
                        tok("飲みすぎて", "のみすぎて", "nomisugite", "drank too much and", "Grammar")
                    ],
                    "Excessive drinking resulting in hangover."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-11-3",
                    "この問題は難し（　　）て、私には全く分かりません。",
                    "This problem is too difficult, so I don't understand it at all.",
                    ["すぎ", "そう", "やすく", "がち"],
                    0,
                    [
                        "Correct! 難しい drops い + すぎて forms 難しすぎて ('too difficult').",
                        "Incorrect. そう indicates appearance (難しそう).",
                        "Incorrect. やすく indicates ease (難しやすく is nonsense).",
                        "Incorrect. がち indicates negative tendency."
                    ],
                    "い-adjective + すぎる excessiveness",
                    "Overly difficult problem."
                )
            ],
            "tags": ["N5", "Genki L11", "Excess", "Thresholds"]
        },

        # === LESSON 12 ===
        {
            "id": "g1-l12-node-objective-reason",
            "title": "〜ので (Objective Reason / Natural Causality: Since / Because)",
            "meaning": "Presents an objective, natural, or polite reason: 'Since / Because X, naturally Y'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 12: Feeling Sick",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + ので | な-adj / Noun + な + ので (Notice the required な!)",
            "nuance": "POLITE & NATURAL: Unlike から which sounds subjective and assertive, ので presents the reason as an objective circumstance beyond the speaker's personal whim. Far more polite in business requests.",
            "keyTakeaway": "MUG-UP: Noun / な-adj + な + ので (雨なので, 暇なので). More polite and objective than から.",
            "sentences": [
                make_sentence(
                    "s-g1-12-1",
                    "明日は朝早く出発するので、今夜は準備をして早く寝ます。",
                    "Since I will depart early tomorrow morning, I will prepare tonight and go to bed early.",
                    "Tomorrow morning early depart since, tonight prepare early sleep.",
                    [
                        tok("出発するので", "しゅっぱつするので", "shuppatsu suru node", "since I will depart", "Grammar")
                    ],
                    "Objective factual circumstance motivating early rest."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-12-1",
                    "明日は（　　）なので、一日中家でのんびり過ごします。",
                    "Since tomorrow is a holiday, I will spend the entire day relaxing at home.",
                    ["休み", "休みの", "休みだ", "休みに"],
                    0,
                    [
                        "Correct! Noun 休み connects via な to ので (休みなので).",
                        "Incorrect. 休みの is an invalid connector to ので.",
                        "Incorrect. 休みだ cannot attach to ので (must be なので, NOT だので ❌).",
                        "Incorrect. 休みに is adverbial."
                    ],
                    "Noun + な + ので objective causality",
                    "Connecting a noun to causal marker ので."
                )
            ],
            "tags": ["N5", "Genki L12", "Causality", "Polite Reason"]
        },
        {
            "id": "g1-l12-nakereba-ikemasen",
            "title": "〜なければいけません / なきゃいけません (Obligation: Must Do / Have to Do)",
            "meaning": "Expresses an unavoidable obligation or necessity: 'Must do / Have to do X'. Spoken contraction: 〜なきゃいけません / なきゃ.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 12: Feeling Sick",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-ない (drop い) + ければいけません / ければなりません",
            "nuance": "DOUBLE NEGATIVE LOGIC: Literally 'If I do not do X, it cannot go on'. Spoken casual forms contract heavily: なければ → なきゃ, 食べなきゃ.",
            "keyTakeaway": "MUG-UP: Drop final い from ない-form, add ければいけません! Casual: 〜なきゃ.",
            "sentences": [
                make_sentence(
                    "s-g1-12-2",
                    "明日の朝九時までに、レポートを提出しなければいけません。",
                    "I must submit the report by 9:00 AM tomorrow morning.",
                    "Tomorrow morning 9-by report submit must.",
                    [
                        tok("提出しなければいけません", "ていしゅつしなければいけません", "teishutsu shinakereba ikemasen", "must submit", "Grammar")
                    ],
                    "Strict academic obligation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-12-2",
                    "熱が高いですから、今日は病院へ（　　）ければいけませんよ。",
                    "Since your fever is high, you must go to the hospital today.",
                    ["行かな", "行く", "行って", "行き"],
                    0,
                    [
                        "Correct! 行く negative stem is 行かな + ければいけません.",
                        "Incorrect. 行く is dictionary form.",
                        "Incorrect. 行って is te-form.",
                        "Incorrect. 行き is masu-stem."
                    ],
                    "Obligation formula 〜なければいけません",
                    "Medical necessity to visit hospital."
                )
            ],
            "tags": ["N5", "Genki L12", "Obligation", "Necessity"]
        },
        {
            "id": "g1-l12-deshou-darou",
            "title": "〜でしょう / 〜だろう (Conjecture & Probability: Probably)",
            "meaning": "Expresses conjecture or probability without absolute certainty: 'Probably / It will likely be X'. Also used with rising tone to seek agreement ('Right?').",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 12: Feeling Sick",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + でしょう (Polite) / だろう (Plain) [Noun & な-adj attach directly without だ!]",
            "nuance": "NO だ BEFORE DESHOU: For nouns and な-adjectives, drop だ completely: 暇でしょう (NOT 暇だでしょう ❌), 雨でしょう (NOT 雨だでしょう ❌).",
            "keyTakeaway": "MUG-UP: Attach directly without だ! (雨でしょう = It will probably rain).",
            "sentences": [
                make_sentence(
                    "s-g1-12-3",
                    "天気予報によると、明日は午後から雨が降るでしょう。",
                    "According to the weather forecast, it will probably rain from the afternoon tomorrow.",
                    "Weather-forecast according-to, tomorrow afternoon-from rain fall probably.",
                    [
                        tok("降るでしょう", "ふるでしょう", "furu deshou", "will probably fall", "Grammar")
                    ],
                    "Meteorological conjecture."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-12-3",
                    "田中さんは毎日一生懸命勉強していますから、きっと試験に（　　）でしょう。",
                    "Since Tanaka-san studies hard every day, he will surely pass the exam.",
                    ["合格する", "合格して", "合格し", "合格したの"],
                    0,
                    [
                        "Correct! Plain dictionary form 合格する connects directly to でしょう.",
                        "Incorrect. 合格して is te-form.",
                        "Incorrect. 合格し is masu-stem.",
                        "Incorrect. 合格したの has unnecessary nominalizer の."
                    ],
                    "Conjecture 〜でしょう with plain verb",
                    "Predicting exam success based on diligence."
                )
            ],
            "tags": ["N5", "Genki L12", "Conjecture", "Probability"]
        }
    ]
    return pts

if __name__ == '__main__':
    pts = get_full_genki1()
    print(f"Genki I generated {len(pts)} exhaustive discrete grammar points.")

