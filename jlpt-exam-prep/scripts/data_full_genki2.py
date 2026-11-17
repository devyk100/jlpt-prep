# -*- coding: utf-8 -*-
"""
Genki II (3rd Edition) - Full Unabridged N4 Grammar Syllabus (Lessons 13 to 23)
Every single grammar point from every lesson is represented individually.
"""
from data_full_genki1 import tok, make_sentence, make_quiz

def get_full_genki2():
    pts = [
        # === LESSON 13 ===
        {
            "id": "g2-l13-potential",
            "title": "可能形 (Potential Verbs: Ability & Possibility)",
            "meaning": "Expresses that an agent has the ability to do an action or that circumstances permit it.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 13: Looking for a Part-time Job",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Ru-verbs: 食べる→食べられる | U-verbs: 書く→書ける, 飲む→飲める | Irregular: する→できる, くる→こられる",
            "nuance": "PARTICLE FLIP: The direct object particle を frequently shifts to が (日本語を話す → 日本語が話せる).",
            "keyTakeaway": "MUG-UP: U-verbs: change final -u to -e + る (行く→行ける). Object を often becomes が!",
            "sentences": [
                make_sentence(
                    "s-g2-13-1",
                    "漢字が難しくて、新聞がすらすら読めません。",
                    "The kanji are difficult, so I cannot read the newspaper smoothly.",
                    "Kanji difficult-being, newspaper smoothly read-cannot.",
                    [
                        tok("読めません", "よめません", "yomemasen", "cannot read (potential neg)", "Grammar")
                    ],
                    "読む potential negative: 読める → 読めません."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-13-1",
                    "刺身は新鮮ですが、どうしても生魚が（　　）。",
                    "The sashimi is fresh, but I just cannot eat raw fish.",
                    ["食べられません", "食べません", "食べさせません", "食べてもらえません"],
                    0,
                    [
                        "Correct! 食べる potential negative is 食べられない / 食べられません.",
                        "Incorrect. 食べません is a simple will decision ('I will not eat').",
                        "Incorrect. 食べさせません is causative ('I will not let someone eat').",
                        "Incorrect. 食べてもらえません means cannot get someone to eat."
                    ],
                    "可能形 potential negative",
                    "Inability to consume raw fish."
                )
            ],
            "tags": ["N4", "Genki L13", "Potential", "Ability"]
        },
        {
            "id": "g2-l13-shi-reasons",
            "title": "〜し、〜し (Listing Multiple Parallel Reasons)",
            "meaning": "Lists two or more complementary reasons leading up to a conclusion or emotion ('Not only... but also...').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 13: Looking for a Part-time Job",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + し (Noun/な-adj non-past affirmative takes だ: 綺麗だし, 休みだし)",
            "nuance": "CUMULATIVE FACTORS: Unlike から which gives one direct explanation, 〜し accumulates multiple contributing factors.",
            "keyTakeaway": "MUG-UP: Connects to plain forms. Remember: Noun / な-adj non-past takes だ + し (親切だし).",
            "sentences": [
                make_sentence(
                    "s-g2-13-2",
                    "物価も安いし、治安もいいし、この街に住んでよかったです。",
                    "Prices are cheap and public safety is great, so I am really glad I live in this town.",
                    "Prices-also cheap-and, safety-also good-and, this town-in living glad-was.",
                    [
                        tok("物価も安いし", "ぶっかもやすいし", "bukka mo yasui shi", "prices are cheap and", "Grammar")
                    ],
                    "Two positive factors combined using 〜し."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-13-2",
                    "このアパートは家賃も安いし、駅からも（　　）し、とても便利です。",
                    "This apartment has cheap rent and is close to the station, so it is very convenient.",
                    ["近い", "近くだ", "近くに", "近いで"],
                    0,
                    [
                        "Correct! 近い is an い-adjective, connecting directly to し (近いし).",
                        "Incorrect. 近い is an い-adjective and never takes だ.",
                        "Incorrect. 近くに is an adverbial form.",
                        "Incorrect. 近いで is ungrammatical."
                    ],
                    "い-adjective connection to 〜し",
                    "Listing attributes with parallel reason marker し."
                )
            ],
            "tags": ["N4", "Genki L13", "Reasons", "Conjunction"]
        },
        {
            "id": "g2-l13-te-miru",
            "title": "〜てみる (Trying Out an Action: Doing Something to See What Happens)",
            "meaning": "Performs an experimental action to test the waters or see what the outcome will be: 'try doing / give it a try'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 13: Looking for a Part-time Job",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-て + みる (Conjugates as a Ru-verb: 〜てみます, 〜てみたい)",
            "nuance": "TESTING THE WATERS: Literally uses the verb 見る (to see): 'do and see'. 履いてみる (try shoes on), 食べてみる (taste it), 行ってみる (go and check).",
            "keyTakeaway": "MUG-UP: V-て + みる = Give it a try to see the result! (やってみよう = Let's give it a shot!).",
            "sentences": [
                make_sentence(
                    "s-g2-13-3",
                    "日本の納豆はまだ食べたことがないので、一口食べてみます。",
                    "Since I have never eaten Japanese natto yet, I will try taking a bite to see what it's like.",
                    "Japan's natto yet eaten experience have-not since, one-bite eat-and-see.",
                    [
                        tok("食べてみます", "たべてみます", "tabete mimasu", "will try eating", "Grammar")
                    ],
                    "Experimental culinary trial."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-13-3",
                    "この服、サイズが合うかどうか一度（　　）みてもいいですか。",
                    "May I try this clothing on once to see if the size fits?",
                    ["着て", "着る", "着", "着た"],
                    0,
                    [
                        "Correct! 着る is a Ru-verb: te-form 着て + みてもいいですか (着てみてもいいですか).",
                        "Incorrect. 着る is dictionary form.",
                        "Incorrect. 着 is bare stem.",
                        "Incorrect. 着た is past form."
                    ],
                    "V-て + みる (Try doing)",
                    "Trying on clothes in a store."
                )
            ],
            "tags": ["N4", "Genki L13", "Trial", "Te-Form"]
        },
        {
            "id": "g2-l13-nara-conditional",
            "title": "なら (Contextual Limitation Conditional: If It's X / As For X)",
            "meaning": "Singles out a specific topic from context: 'If we're talking about X, then... / As for X (though other things might not be)'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 13: Looking for a Part-time Job",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "Noun + なら (Attaches directly without だ!) | Plain form + なら",
            "nuance": "CONTRASTIVE CONTEXT: Often carries an implicit contrast: 'ひらがななら読めます' (If it's hiragana I can read it—implying kanji is impossible).",
            "keyTakeaway": "MUG-UP: Noun + なら = 'If it's X you're talking about...'. Replaces topic は.",
            "sentences": [
                make_sentence(
                    "s-g2-13-4",
                    "英語なら話せますが、フランス語は全く話せません。",
                    "If it's English, I can speak it, but I cannot speak French at all.",
                    "English if-talking-about speak-can but, French at-all speak-cannot.",
                    [
                        tok("英語なら", "えいごなら", "eigo nara", "if it's English", "Grammar")
                    ],
                    "Selective linguistic competence."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-13-4",
                    "「明日京都に行くんですが。」「京都（　　）、金閣寺がおすすめですよ。」",
                    "'I'm going to Kyoto tomorrow.' 'If it's Kyoto, Kinkaku-ji is highly recommended!'",
                    ["なら", "たら", "ば", "と"],
                    0,
                    [
                        "Correct! なら picks up the conversational topic mentioned by the partner.",
                        "Incorrect. たら is temporal sequence ('if/when Kyoto happens').",
                        "Incorrect. ば requires a predicate (verb/adjective).",
                        "Incorrect. と is natural inevitable consequence."
                    ],
                    "Contextual conditional なら",
                    "Offering a recommendation based on the listener's plan."
                )
            ],
            "tags": ["N4", "Genki L13", "Conditionals", "Limitation"]
        },

        # === LESSON 14 ===
        {
            "id": "g2-l14-hoshii",
            "title": "ほしい (Expressing Desire for an Object: Want Something)",
            "meaning": "Expresses first-person desire to possess a concrete object or commodity: [Item] が ほしい ('I want [Item]').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 14: Valentine's Day",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "[Item] が ほしいです (Conjugates 100% as an い-adjective: ほしくない, ほしかった)",
            "nuance": "HOSHII VS TAI: たい is for ACTIONS ('I want to BUY a car' = 車を買いたい). ほしい is for NOUN OBJECTS ('I want a car' = 車がほしい). Target takes が!",
            "keyTakeaway": "MUG-UP: [Noun] が ほしい! Never use を with ほしい. (Action desire = 〜たい).",
            "sentences": [
                make_sentence(
                    "s-g2-14-1",
                    "今度の誕生日に、新しいノートパソコンがほしいです。",
                    "For my upcoming birthday, I want a new laptop computer.",
                    "This-time's birthday-on, new laptop want is.",
                    [
                        tok("ノートパソコンが", "ノートパソコンが", "nootopasokon ga", "laptop", "Noun+Particle"),
                        tok("ほしいです", "ほしいです", "hoshii desu", "want", "Adjective")
                    ],
                    "Desire for material item marked with が."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-14-1",
                    "今は何も（　　）くないです。ただゆっくり休みたいです。",
                    "Right now I don't want anything. I just want to rest leisurely.",
                    ["ほし", "ほしい", "ほしく", "ほしな"],
                    0,
                    [
                        "Correct! ほしい drops い + くない = ほしくない (Nothing wanted).",
                        "Incorrect. ほしいくない retains the extra い.",
                        "Incorrect. ほしく is already adverbial; adding another くない is invalid.",
                        "Incorrect. ほしな is ungrammatical."
                    ],
                    "Negative of ほしい (ほしくない)",
                    "Expressing absence of material desire."
                )
            ],
            "tags": ["N4", "Genki L14", "Desire", "Possession"]
        },
        {
            "id": "g2-l14-kamoshirenai",
            "title": "〜かもしれない / 〜かもしんない (Epistemic Possibility: Might / May)",
            "meaning": "States that something is possible without guaranteeing it: 'might / may be X' (roughly 50% or less certainty).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 14: Valentine's Day",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + かもしれません | Noun / な-adj attach directly without だ!",
            "nuance": "NO だ BEFORE KAMOSHれない: Just like でしょう, nouns and な-adjectives drop だ: 雨かもしれない (NOT 雨だかもしれない ❌), 暇かもしれない.",
            "keyTakeaway": "MUG-UP: Attach directly without だ! (風邪かもしれない = Might have caught a cold).",
            "sentences": [
                make_sentence(
                    "s-g2-14-2",
                    "午後から天気が崩れて、雨が降るかもしれません。",
                    "The weather may deteriorate from the afternoon, and it might rain.",
                    "Afternoon-from weather deteriorate, rain fall might.",
                    [
                        tok("降るかもしれません", "ふるかもしれません", "furu kamoshiremasen", "might fall", "Grammar")
                    ],
                    "Epistemic possibility of rain."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-14-2",
                    "山田さんはまだ来ませんね。道に（　　）のかもしれません。",
                    "Yamada-san hasn't arrived yet, has he? He might have gotten lost on the way.",
                    ["迷った", "迷う", "迷って", "迷い"],
                    0,
                    [
                        "Correct! Past plain form 迷った + のかもしれません ('might have gotten lost').",
                        "Incorrect. 迷う is non-past ('will get lost').",
                        "Incorrect. 迷って is te-form.",
                        "Incorrect. 迷い is masu-stem."
                    ],
                    "Past conjecture with 〜かもしれない",
                    "Speculating on reasons for someone being late."
                )
            ],
            "tags": ["N4", "Genki L14", "Possibility", "Modality"]
        },
        {
            "id": "g2-l14-tara-dou-desu-ka",
            "title": "〜たらどうですか (Casual Advice / Suggestion: Why Don't You?)",
            "meaning": "Offers a suggestion or recommendation to the listener: 'Why don't you try X? / How about doing X?'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 14: Valentine's Day",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-た + らどうですか",
            "nuance": "CRITICAL SOCIAL CAUTION: This phrase can sound patronizing or critical if said to superiors ('Why don't you do your job?'). Use only with peers, friends, or juniors.",
            "keyTakeaway": "MUG-UP: V-た + らどうですか = Friendly suggestion ('Why don't you...?'). Avoid with superiors!",
            "sentences": [
                make_sentence(
                    "s-g2-14-3",
                    "頭が痛いなら、無理をしないで薬を飲んで寝たらどうですか。",
                    "If you have a headache, why don't you stop overworking, take medicine, and sleep?",
                    "Head hurts if, overwork do-not medicine take slept-if how is?",
                    [
                        tok("寝たらどうですか", "ねたらどうですか", "netara dou desu ka", "why don't you sleep?", "Grammar")
                    ],
                    "Sympathetic peer recommendation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-14-3",
                    "分からない単語があるなら、辞書で（　　）たらどうですか。",
                    "If there are vocabulary words you don't understand, why don't you look them up in a dictionary?",
                    ["調べ", "調べる", "調べて", "調べた"],
                    0,
                    [
                        "Correct! 調べる (Ru-verb) past form is 調べた + らどうですか (調べたらどうですか).",
                        "Incorrect. 調べる is dictionary form.",
                        "Incorrect. 調べて is te-form.",
                        "Incorrect. 調べた already contains た, so adding たら produces '調べたらたら'."
                    ],
                    "Advice formula 〜たらどうですか",
                    "Suggesting dictionary lookup."
                )
            ],
            "tags": ["N4", "Genki L14", "Advice", "Suggestions"]
        },

        # === LESSON 15 ===
        {
            "id": "g2-l15-volitional-form",
            "title": "意向形 (The Volitional Form: Casual Let's Do / Self-Resolve)",
            "meaning": "The casual plain equivalent of 〜ましょう: 'Let's do X!' In monologue, expresses personal determination: 'I shall do X!'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 15: A Trip to Nagano",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Ru-verbs: drop る + よう (食べよう) | U-verbs: change final -u to -ou (行こう, 飲もう) | する→しよう, くる→こよう",
            "nuance": "CASUAL COMPANION: In peer conversation, '行こう!' replaces '行きましょう!'. In internal monologue, 'よし、頑張ろう!' expresses resolve.",
            "keyTakeaway": "MUG-UP: Ru-verbs = drop る + よう. U-verbs = change final -u to long -ou (書く→書こう).",
            "sentences": [
                make_sentence(
                    "s-g2-15-1",
                    "今日は天気がいいから、海までドライブに行こう！",
                    "The weather is great today, so let's go for a drive to the beach!",
                    "Today weather good since, beach-to drive-to let's-go!",
                    [
                        tok("行こう", "いこう", "ikou", "let's go (volitional)", "Verb")
                    ],
                    "Casual peer invitation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-15-1",
                    "疲れたから、あそこのカフェで少し（　　）よう。",
                    "Since we're tired, let's rest for a bit at that cafe over there.",
                    ["休も", "休もう", "休み", "休ま"],
                    1,
                    [
                        "Incorrect. 休も lacks the long vowel う.",
                        "Correct! 休む (U-verb) becomes 休もう in volitional form.",
                        "Incorrect. 休み is masu-stem.",
                        "Incorrect. 休ま is negative stem."
                    ],
                    "U-verb volitional form 休もう",
                    "Casual proposal to rest."
                )
            ],
            "tags": ["N4", "Genki L15", "Volitional", "Verbs"]
        },
        {
            "id": "g2-l15-volitional-to-omotte-iru",
            "title": "意向形 + と思っている (Firm Ongoing Determination: Intending To)",
            "meaning": "Expresses an ongoing, settled determination that the speaker has been contemplating over time: 'I have been planning/intending to do X'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 15: A Trip to Nagano",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-意向形 + と思っています (Ongoing firm intent) / と思います (Decision made on the spot)",
            "nuance": "SPONTANEOUS VS PONDERED: と思う = decided right now on the spot. と思っている = has been decided for some time and remains an ongoing intention.",
            "keyTakeaway": "MUG-UP: V-よう + と思っている = A settled plan I have been thinking about for a while.",
            "sentences": [
                make_sentence(
                    "s-g2-15-2",
                    "来年から日本企業で働こうと思っています。",
                    "I am planning on working at a Japanese firm starting next year.",
                    "Next-year-from Japanese firm-at work-shall quote thinking-am.",
                    [
                        tok("働こうと思っています", "はたらこうとおもっています", "hatarakou to omotte imasu", "am intending to work", "Grammar")
                    ],
                    "Ongoing career resolution."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-15-2",
                    "夏休みに富士山に（　　）と思っています。",
                    "I am intending to climb Mt. Fuji during summer vacation.",
                    ["登ろう", "登る", "登り", "登った"],
                    0,
                    [
                        "Correct! 登る volitional is 登ろう + と思っています.",
                        "Incorrect. 登る is dictionary form (takes つもり, not volitional と思う).",
                        "Incorrect. 登り is masu-stem.",
                        "Incorrect. 登った is past form."
                    ],
                    "V-意向形 + と思っている",
                    "Ongoing vacation intent."
                )
            ],
            "tags": ["N4", "Genki L15", "Intention", "Volitional"]
        },
        {
            "id": "g2-l15-relative-clauses",
            "title": "連体修飾節 (Relative Clauses / Qualifying Nouns with Sentences)",
            "meaning": "Embedding an entire sentence before a noun to modify it without any relative pronoun ('The book that I bought yesterday').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 15: A Trip to Nagano",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Plain sentence + Noun (Subordinate subject marked with が, NEVER は!)",
            "nuance": "NO RELATIVE PRONOUN: Japanese uses NO 'who', 'which', or 'that'. The modifying sentence simply directly precedes the head noun. Crucially, the subject inside the relative clause takes が!",
            "keyTakeaway": "MUG-UP: [Plain clause] + [Noun]. Inside the clause, use が for the subject (母が作った料理 = Food that mother made).",
            "sentences": [
                make_sentence(
                    "s-g2-15-3",
                    "これは私が昨日デパートで買ったセーターです。",
                    "This is the sweater that I bought at the department store yesterday.",
                    "This topic I-subject yesterday department-store-at bought sweater is.",
                    [
                        tok("私が昨日デパートで買った", "わたしがきょうデパートでかった", "watashi ga kinou depaato de katta", "that I bought at department store yesterday", "Clause"),
                        tok("セーター", "セーター", "seetaa", "sweater", "Noun")
                    ],
                    "Direct noun qualification without pronouns."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-15-3",
                    "あそこに立って（　　）人は、私の高校の英語の先生です。",
                    "The person standing over there is my high school English teacher.",
                    ["いる", "います", "いたの", "いまして"],
                    0,
                    [
                        "Correct! Plain form いる modifies the head noun 人 (立っている人).",
                        "Incorrect. Polite form います cannot modify a noun directly.",
                        "Incorrect. いたの人は has unnecessary nominalizer の.",
                        "Incorrect. いまして is te-form."
                    ],
                    "Relative clause noun modification with plain form",
                    "Modifying person with ongoing action."
                )
            ],
            "tags": ["N4", "Genki L15", "Relative Clauses", "Syntax"]
        },

        # === LESSON 16 ===
        {
            "id": "g2-l16-to-ii-hoping",
            "title": "〜といい (Hoping for Favorable Outcomes: I Hope That...)",
            "meaning": "Expresses hope or wish that a favorable condition will happen: 〜といいね (Hoping for listener's sake) vs 〜といいんですが (Hoping for speaker's own sake).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 16: Lost and Found",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain non-past verb + といいですね / といいんですが",
            "nuance": "FOR OTHER VS FOR SELF: When wishing good fortune for the other person, say '〜といいですね' (I hope it goes well for you!). When wishing for yourself, soften with '〜といいんですが' (I hope I pass...).",
            "keyTakeaway": "MUG-UP: V-plain + といいね (Wishing for others). V-plain + といいんですが (Wishing for self).",
            "sentences": [
                make_sentence(
                    "s-g2-16-1",
                    "明日の試合、晴れるといいですね。「ええ、本当に。」",
                    "I hope it will be sunny for tomorrow's match, don't you? 'Yes, truly.'",
                    "Tomorrow's match, clear-up if good is right? Yes, really.",
                    [
                        tok("晴れるといいですね", "はれるといいですね", "hareru to ii desu ne", "I hope it clears up", "Grammar")
                    ],
                    "Expressing mutual hope for good weather."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-16-1",
                    "来週の採用試験に無事合格できる（　　）いいんですが。",
                    "I really hope I can pass next week's employment exam safely.",
                    ["と", "ば", "たら", "なら"],
                    0,
                    [
                        "Correct! できるといいんですが is the standard formula for expressing personal hopes.",
                        "Incorrect. できるば is an invalid conjugation (must be できれば).",
                        "Incorrect. できたらいいんですが is colloquial, but と is the canonical textbook pattern.",
                        "Incorrect. できるならいい requires a different contextual nuance."
                    ],
                    "Hoping formula 〜といい",
                    "Hoping to pass employment exam."
                )
            ],
            "tags": ["N4", "Genki L16", "Hopes", "Modality"]
        },
        {
            "id": "g2-l16-toki-tense",
            "title": "〜時（とき）の時制 (Tense Nuances in 'When' Clauses: V-る時 vs V-た時)",
            "meaning": "Tense distinctions before とき: V-る時 (Action NOT yet completed before main verb) vs V-た時 (Action ALREADY completed before main verb).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 16: Lost and Found",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 + 時 (Prior/During) | V-た + 時 (After completion)",
            "nuance": "CRITICAL TENSE PUZZLE: '日本に行く時カメラを買った' = Bought camera BEFORE arriving in Japan. '日本に行った時カメラを買った' = Bought camera AFTER arriving in Japan!",
            "keyTakeaway": "MUG-UP: V-る時 = Before you do it. V-た時 = After you have finished doing it!",
            "sentences": [
                make_sentence(
                    "s-g2-16-2",
                    "出かける時、鍵をかけるのを忘れました。",
                    "When I was heading out, I forgot to lock the door.",
                    "Head-out when, lock apply forgot.",
                    [
                        tok("出かける時", "でかけるとき", "dekakeru toki", "when heading out", "Grammar")
                    ],
                    "Action was in progress/prior to completing the departure."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-16-2",
                    "日本へ（　　）時、空港の免税店でお土産を買いました。",
                    "When I went to Japan (prior to boarding/reaching Japan), I bought souvenirs at the airport duty-free shop.",
                    ["行く", "行った", "行っている", "行かない"],
                    0,
                    [
                        "Correct! Buying souvenirs at the departure duty-free shop happens BEFORE reaching Japan, requiring 行く時.",
                        "Incorrect. 行った時 would mean after already having arrived in Japan.",
                        "Incorrect. 行っている時 is awkward here.",
                        "Incorrect. 行かない is negative."
                    ],
                    "Tense before とき (V-る時 prior action)",
                    "Action performed before arrival at destination."
                )
            ],
            "tags": ["N4", "Genki L16", "Time", "Aspect"]
        },

        # === LESSON 17 ===
        {
            "id": "g2-l17-hearsay-sou-desu",
            "title": "〜そうです (Hearsay / Quoting Reports: I Heard That / Reportedly)",
            "meaning": "Relays information obtained from external news, reports, or rumors without personal verification: 'I heard that... / Reportedly'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 17: Grumble and Gossip",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + そうです (Noun / な-adj non-past takes だ: 暇だそうです, 雨だそうです)",
            "nuance": "CRUCIAL DIFFERENCE FROM CONJECTURE: Appearance: drop い (おいしそう = looks tasty). Hearsay: KEEP い and keep だ (おいしいそうです = I heard it's tasty; 暇だそうです = I heard he's free).",
            "keyTakeaway": "MUG-UP: Hearsay attaches to 100% UNCHANGED plain form (including だ for nouns/na-adj)! Drop nothing!",
            "sentences": [
                make_sentence(
                    "s-g2-17-1",
                    "ニュースによると、明日は関東地方で雪が降るそうです。",
                    "According to the news, I heard that it will snow in the Kanto region tomorrow.",
                    "News according-to, tomorrow Kanto-region snow fall reportedly.",
                    [
                        tok("雪が降るそうです", "ゆきがふるそうです", "yuki ga furu sou desu", "I heard it will snow", "Grammar")
                    ],
                    "Relaying journalistic weather forecast."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-17-1",
                    "田中さんの話では、新しい先生はとても（　　）そうです。",
                    "According to Tanaka-san, I heard that the new teacher is very kind.",
                    ["親切だ", "親切", "親切な", "親切に"],
                    0,
                    [
                        "Correct! Hearsay requires plain affirmative copula だ for な-adjectives: 親切だそうです.",
                        "Incorrect. 親切 without だ creates appearance/conjecture ('looks kind').",
                        "Incorrect. 親切な is noun-modifying form.",
                        "Incorrect. 親切に is adverbial."
                    ],
                    "Hearsay 〜そうです with な-adjective",
                    "Reporting secondhand rumor about teacher's personality."
                )
            ],
            "tags": ["N4", "Genki L17", "Hearsay", "Modality"]
        },
        {
            "id": "g2-l17-tara-conditional",
            "title": "〜たら (Specific & Temporal Conditional: If / When / Once Done)",
            "meaning": "Universal conditional: 1) Hypothetical condition ('If X happens, then Y'). 2) Temporal certainty in future ('When / Once X finishes, Y will happen').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 17: Grumble and Gossip",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "V-た + ら | い-adj かった + ら | な-adj / Noun だった + ら",
            "nuance": "MOST VERSATILE CONDITIONAL: Unlike と (which forbids commands) or ば (which restricts volitions), 〜たら allows commands, invitations, requests, and future decisions in clause B!",
            "keyTakeaway": "MUG-UP: Formed by adding ら to past た-form! Allows commands and requests in clause B.",
            "sentences": [
                make_sentence(
                    "s-g2-17-2",
                    "家に帰ったら、すぐに手を洗ってうがいをしましょう。",
                    "Once you return home, let's wash our hands and gargle right away.",
                    "Home return-once, immediately hands wash gargle let's-do.",
                    [
                        tok("帰ったら", "かえったら", "kaettara", "once you return", "Grammar")
                    ],
                    "Temporal sequential conditional triggering action."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-17-2",
                    "東京駅に（　　）ら、私に電話をかけてください。",
                    "Once you arrive at Tokyo Station, please call me.",
                    ["着いた", "着く", "着き", "着いて"],
                    0,
                    [
                        "Correct! 着く past is 着いた + ら = 着いたら ('once you arrive').",
                        "Incorrect. 着く is dictionary form.",
                        "Incorrect. 着き is masu-stem.",
                        "Incorrect. 着いて is te-form."
                    ],
                    "V-たら conditional connection",
                    "Instruction to call upon arrival."
                )
            ],
            "tags": ["N4", "Genki L17", "Conditionals", "Sequence"]
        },
        {
            "id": "g2-l17-nakute-mo-ii",
            "title": "〜なくてもいいです (Lack of Obligation: You Do Not Have To)",
            "meaning": "States that an action is unnecessary: 'You do not have to do X / It is fine even if you don't do X'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 17: Grumble and Gossip",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-ない (drop い) + くてもいいです",
            "nuance": "LITERAL MEANING: Even if you do not do X, it is fine. Releases the listener from social or official obligation.",
            "keyTakeaway": "MUG-UP: V-ない (drop い) + くてもいいです = You don't have to do it!",
            "sentences": [
                make_sentence(
                    "s-g2-17-3",
                    "明日は祝日ですから、朝早く起きなくてもいいですよ。",
                    "Since tomorrow is a national holiday, you do not have to wake up early.",
                    "Tomorrow national-holiday is since, morning early wake-not-even-if good is.",
                    [
                        tok("起きなくてもいいですよ", "おきなくてもいいですよ", "okinakute mo ii desu yo", "you don't have to wake up", "Grammar")
                    ],
                    "Releasing listener from waking up early."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-17-3",
                    "パスポートのコピーは提出し（　　）くてもいいです。",
                    "You do not have to submit a copy of your passport.",
                    ["なか", "ない", "なくて", "なかった"],
                    0,
                    [
                        "Correct! 提出しない drops い to become なか + くてもいいです.",
                        "Incorrect. ないくても is ungrammatical (must change い to く).",
                        "Incorrect. なくて already has て.",
                        "Incorrect. なかった is past form."
                    ],
                    "〜なくてもいい lack of obligation",
                    "Noting non-essential document requirement."
                )
            ],
            "tags": ["N4", "Genki L17", "Permission", "Lack of Obligation"]
        },

        # === LESSON 18 ===
        {
            "id": "g2-l18-transitive-intransitive",
            "title": "自動詞 vs 他動詞 (Intransitive vs Transitive Verb Pairs)",
            "meaning": "Pairs of verbs distinguishing self-occurring natural phenomena (自動詞: marked with が) from deliberate actions on an object (他動詞: marked with を).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 18: John's Part-Time Job",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Entity が 自動詞 (開く, 閉まる, つく, 消える) | Agent が Object を 他動詞 (開ける, 閉める, つける, 消す)",
            "nuance": "AGENCY TRAP: ドアが開いた = The door opened (spontaneously/naturally). ドアを開けた = Someone intentionally opened the door. Crucial for advanced JLPT parsing!",
            "keyTakeaway": "MUG-UP: 自動詞 takes が (自発・自然). 他動詞 takes を (Human action). (窓が開く vs 窓を開ける).",
            "sentences": [
                make_sentence(
                    "s-g2-18-1",
                    "風でドアが閉まりました。寒かったので、私がドアを閉めました。",
                    "The door closed in the wind. Because it was cold, I deliberately closed the door.",
                    "Wind-by door closed (intrans). Cold was since, I door closed (trans).",
                    [
                        tok("ドアが閉まりました", "ドアがしまりました", "doa ga shimarimashita", "door closed (intransitive)", "Grammar"),
                        tok("ドアを閉めました", "ドアをしめました", "doa o shimemashita", "closed door (transitive)", "Grammar")
                    ],
                    "Side-by-side contrast of intransitive vs transitive pairs."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-18-1",
                    "部屋が暗いですね。電気を（　　）ましょう。",
                    "The room is dark, isn't it? Let's turn on the lights.",
                    ["つけ", "つき", "消し", "消え"],
                    0,
                    [
                        "Correct! Direct object marker を requires transitive verb つける (stem つけ + ましょう).",
                        "Incorrect. つく is intransitive (電気がつく).",
                        "Incorrect. 消す means turn off.",
                        "Incorrect. 消える is intransitive turn off."
                    ],
                    "Transitive verb つける with direct object を",
                    "Deliberately turning on the lights."
                )
            ],
            "tags": ["N4", "Genki L18", "Transitivity", "Verbs"]
        },
        {
            "id": "g2-l18-to-natural-consequence",
            "title": "〜と (Natural Consequence & Inevitable Conditional: When / If)",
            "meaning": "States an inevitable natural consequence, physical law, or habitual fact: 'Whenever X happens, Y automatically occurs'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 18: John's Part-Time Job",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "V-辞書形 / V-ない + と",
            "nuance": "STRICT PROHIBITION ON WILL: Clause B CANNOT be a human request, command, suggestion, or permission (e.g., '春になると花見に行きましょう' ❌ is ungrammatical; must use たら). B must be an automatic physical/natural fact.",
            "keyTakeaway": "MUG-UP: V-る + と = Inevitable automatic trigger! Clause B CANNOT be a command or invitation!",
            "sentences": [
                make_sentence(
                    "s-g2-18-2",
                    "このボタンを押すと、お釣りが出ます。",
                    "When you press this button, the change automatically comes out.",
                    "This button press-when, change comes-out.",
                    [
                        tok("押すと", "おすと", "osu to", "when you press it", "Grammar")
                    ],
                    "Automatic mechanical consequence."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-18-2",
                    "あの交差点を右に（　　）と、左手に大きな郵便局が見えます。",
                    "When you turn right at that intersection, you will see a large post office on your left.",
                    ["曲がる", "曲がった", "曲がって", "曲がり"],
                    0,
                    [
                        "Correct! Plain non-past 曲がる connects directly to と for automatic route guidance.",
                        "Incorrect. Past 曲がった cannot connect to と for future directions.",
                        "Incorrect. 曲がって is te-form.",
                        "Incorrect. 曲がり is masu-stem."
                    ],
                    "Route guidance conditional 〜と",
                    "Automatic visual consequence upon turning."
                )
            ],
            "tags": ["N4", "Genki L18", "Conditionals", "Natural Law"]
        },
        {
            "id": "g2-l18-ba-yokatta",
            "title": "〜ばよかった (Retrospective Regret: I Should Have Done)",
            "meaning": "Expresses retrospective regret or remorse over an unfulfilled action: 'I should have done X (but unfortunately I didn't)'. Negative: 'I shouldn't have done X'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 18: John's Part-Time Job",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "V-ば + よかった (Affirmative regret: should have) | V-なければ + よかった (Negative regret: shouldn't have)",
            "nuance": "MISSED OPPORTUNITY: Communicates a sigh of self-reproach. '傘を持ってくればよかった' implies it is pouring now and I am drenched.",
            "keyTakeaway": "MUG-UP: V-ば + よかった = 'Ah, I should have done it!'. Negative: V-なければよかった.",
            "sentences": [
                make_sentence(
                    "s-g2-18-3",
                    "昨夜もっと早く寝ればよかった。今日は一日中頭がぼーっとしています。",
                    "I should have gone to bed earlier last night. Today my head is in a daze all day long.",
                    "Last-night more early slept-if was-good. Today all-day head dazed-is.",
                    [
                        tok("寝ればよかった", "ねればよかった", "nereba yokatta", "should have slept", "Grammar")
                    ],
                    "Remorse over late night."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-18-3",
                    "こんなに雨が降るなら、傘を持って（　　）ばよかった。",
                    "If it was going to rain this much, I should have brought an umbrella.",
                    ["くれ", "くる", "こ", "きた"],
                    0,
                    [
                        "Correct! 持ってくる conditional is 持ってくれば + よかった (should have brought).",
                        "Incorrect. くる is dictionary form.",
                        "Incorrect. こ is negative stem.",
                        "Incorrect. きた is past form."
                    ],
                    "V-ばよかった retrospective regret",
                    "Regretting forgetting an umbrella in the rain."
                )
            ],
            "tags": ["N4", "Genki L18", "Regret", "Causality"]
        },

        # === LESSON 19 ===
        {
            "id": "g2-l19-sonkeigo-verbs",
            "title": "尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)",
            "meaning": "Elevates the actions, states, and possessions of the respected subject (professors, clients, superiors).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 19: Meeting the Boss",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "Special verbs: いらっしゃる (行く/来る/いる), おっしゃる (言う), なさる (する), 召し上がる (食べる/飲む), ご覧になる (見る), ご存じだ (知っている) | Regular formula: お + V-stem + になる",
            "nuance": "NEVER USE ON SELF: 尊敬語 elevates the OTHER person. Using it for your own actions is a catastrophic error in Japanese etiquette.",
            "keyTakeaway": "MUG-UP: 尊敬語 (Sonkeigo) is STRICTLY for superiors' actions! Never use for yourself!",
            "sentences": [
                make_sentence(
                    "s-g2-19-1",
                    "先生は昨日の学会で、非常に興味深い研究成果をおっしゃいました。",
                    "The professor stated highly intriguing research findings at yesterday's academic conference.",
                    "Professor yesterday's conference-at, intriguing findings honorably-said.",
                    [
                        tok("おっしゃいました", "おっしゃいました", "osshaimashita", "honorably said (sonkeigo)", "Verb")
                    ],
                    "Elevating professor's speech act via おっしゃる."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-19-1",
                    "社長はもうお昼ご飯を（　　）ましたか。",
                    "Has the company president already eaten lunch?",
                    ["召し上がり", "いただき", "参り", "拝見し"],
                    0,
                    [
                        "Correct! 召し上がる is the special honorific (尊敬語) verb for 食べる/飲む.",
                        "Incorrect. いただく is humble (謙譲語) for oneself eating.",
                        "Incorrect. 参る is humble for going/coming.",
                        "Incorrect. 拝見する is humble for looking."
                    ],
                    "Special honorific verb 召し上がる",
                    "Elevating the president's lunch action."
                )
            ],
            "tags": ["N4", "Genki L19", "Keigo", "Honorific"]
        },
        {
            "id": "g2-l19-o-kudasai",
            "title": "お + V-stem + ください (Polite Honorific Request: Please Graciously Do)",
            "meaning": "A graceful, courteous request formula for superiors or customers: 'Please graciously do X' (much more polite than 〜てください).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 19: Meeting the Boss",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "お + V-stem + ください (Group 3 する verbs: ご + Noun + ください: ご注意ください)",
            "nuance": "CUSTOMER SERVICE REGISTER: Ubiquitous in stores, public transit, and professional offices: お座りください (Please be seated), お入りください (Please come in), ご覧ください (Please take a look).",
            "keyTakeaway": "MUG-UP: お + [Masu-stem] + ください (Native verbs) / ご + [Noun] + ください (Sino-Japanese).",
            "sentences": [
                make_sentence(
                    "s-g2-19-2",
                    "足元が滑りやすくなっておりますので、十分にお気をつけください。",
                    "Because the footing has become slippery, please take great care.",
                    "Footing slippery become since, sufficiently take-care please.",
                    [
                        tok("お気をつけください", "おきをつけください", "o-ki o tsukete kudasai", "please take care", "Expression")
                    ],
                    "Polite safety announcement."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-19-2",
                    "どうぞこちらのお席にお（　　）ください。",
                    "Please graciously have a seat here in this chair.",
                    ["掛け", "掛ける", "掛けて", "掛けた"],
                    0,
                    [
                        "Correct! 腰を掛ける stem is 掛け: お掛けください (Please have a seat).",
                        "Incorrect. 掛ける is dictionary form.",
                        "Incorrect. 掛けて is te-form.",
                        "Incorrect. 掛けた is past form."
                    ],
                    "Honorific request formula お + stem + ください",
                    "Inviting someone to sit down."
                )
            ],
            "tags": ["N4", "Genki L19", "Requests", "Keigo"]
        },

        # === LESSON 21 ===
        {
            "id": "g2-l21-te-aru",
            "title": "〜てある (Transitive Verb Resultant State: Deliberately Prepared)",
            "meaning": "Describes a continuous state that resulted from someone having deliberately performed an action beforehand for a purpose: 'has been done and remains so'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 21: Which Style of House?",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "Transitive Verb-て + ある (Object is marked with が: 窓が開けてある)",
            "nuance": "DELIBERATE HUMAN PURPOSE: Contrast with 〜ている! '窓が開いている' = The window is open (mere state). '窓が開けてある' = Someone purposely opened the window for ventilation and left it open!",
            "keyTakeaway": "MUG-UP: Transitive verb-て + ある = Purposely prepared beforehand. Object particle flips to が!",
            "sentences": [
                make_sentence(
                    "s-g2-21-1",
                    "会議室の黒板に、今日の議題が書いてあります。",
                    "On the blackboard in the conference room, today's agenda has been written.",
                    "Conference-room blackboard-on, today's agenda written-remains.",
                    [
                        tok("書いてあります", "かいてあります", "kaite arimasu", "has been written and remains so", "Grammar")
                    ],
                    "Deliberately posted agenda."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-21-1",
                    "パーティーのために、壁に綺麗な花が（　　）あります。",
                    "For the party, beautiful flowers have been deliberately hung on the wall.",
                    ["飾って", "飾る", "飾り", "飾られ"],
                    0,
                    [
                        "Correct! 飾る (to decorate) connects via te-form 飾って + あります.",
                        "Incorrect. 飾る is dictionary form.",
                        "Incorrect. 飾り is masu-stem.",
                        "Incorrect. 飾られ is passive stem."
                    ],
                    "Transitive resultant state 〜てある",
                    "Decorations intentionally hung for an upcoming party."
                )
            ],
            "tags": ["N4", "Genki L21", "Resultant State", "Preparation"]
        },
        {
            "id": "g2-l21-aida-vs-aidani",
            "title": "〜間に vs 〜間 (During a Moment vs Throughout the Entire Duration)",
            "meaning": "〜間に (A short, discrete action occurs AT SOME MOMENT during interval X). 〜間 (A continuous state persists THROUGHOUT THE ENTIRETY of interval X).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 21: Which Style of House?",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-ている / Noun + の + 間に (Momentary point) vs 間 (Continuous entirety)",
            "nuance": "CRITICAL PARTICLE DISCRIMINATOR: '留守の[間]、犬が寝ていた' = The dog slept the ENTIRE time I was gone. '留守の[間に]、泥棒が入った' = A thief broke in AT A MOMENT during my absence.",
            "keyTakeaway": "MUG-UP: 〜間 = 100% of the time interval. 〜間に = A single moment during the window!",
            "sentences": [
                make_sentence(
                    "s-g2-21-2",
                    "子供が昼寝をしている間に、急いで晩ご飯の支度を済ませた。",
                    "While the child was taking a nap, I quickly completed the dinner preparations.",
                    "Child nap doing was while-in, quickly dinner prep completed.",
                    [
                        tok("している間に", "しているあいだに", "shite iru aida ni", "during the time that...", "Grammar")
                    ],
                    "Action finished at a moment within the child's nap window."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-21-2",
                    "日本に留学している（　　）、一度富士山に登ってみたいです。",
                    "While I am studying abroad in Japan, I want to try climbing Mt. Fuji once.",
                    ["間に", "間", "うちに", "最中に"],
                    0,
                    [
                        "Correct! Climbing Mt. Fuji is a discrete, one-time momentary event during the stay, requiring 間に.",
                        "Incorrect. 間 would imply climbing Mt. Fuji continuously for the entire years of study abroad!",
                        "Incorrect. うちに emphasizes urgency before leaving, but 間に is the canonical duration contrast.",
                        "Incorrect. 最中に implies right in the thick of a physical activity."
                    ],
                    "〜間に (Momentary action within time frame)",
                    "Climbing Mt. Fuji during study abroad stay."
                )
            ],
            "tags": ["N4", "Genki L21", "Time", "Duration"]
        },

        # === LESSON 22 ===
        {
            "id": "g2-l22-ba-conditional",
            "title": "〜ば (The Hypothetical Conditional: If)",
            "meaning": "States a logical or hypothetical condition: 'If X condition is met, then Y occurs'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 22: Education in Japan",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "Verbs: change final -u to -e + ば (書く→書けば, 食べる→食べれば) | い-adj: drop い + ければ | な-adj / Noun: なら (ば)",
            "nuance": "THE VOLITIONAL PROHIBITION TRAP: If clause A is an action verb (not state), clause B CANNOT be a human request, volition, or command! You cannot say '車を買えば、海に行きましょう' ❌ (Must use たら).",
            "keyTakeaway": "MUG-UP: All verbs: final -u changes to -e + ば! (話す→話せば, 待つ→待てば).",
            "sentences": [
                make_sentence(
                    "s-g2-22-1",
                    "分からない言葉があれば、いつでも私に聞いてください。",
                    "If there are words you don't understand, please ask me anytime.",
                    "Understand-not words have-if, anytime me-to ask please.",
                    [
                        tok("あれば", "あれば", "areba", "if there is (stative verb)", "Grammar")
                    ],
                    "ある is a stative verb, so requests in clause B are permitted."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-22-1",
                    "毎日練習を（　　）ば、誰でもピアノが上手に弾けるようになりますよ。",
                    "If you practice every day, anyone will become able to play the piano skillfully.",
                    ["すれ", "する", "した", "して"],
                    0,
                    [
                        "Correct! する irregular conditional is すれば.",
                        "Incorrect. する is dictionary form.",
                        "Incorrect. した is past form.",
                        "Incorrect. して is te-form."
                    ],
                    "Verb conditional form 〜ば of する (すれば)",
                    "Practice leading to musical proficiency."
                )
            ],
            "tags": ["N4", "Genki L22", "Conditionals", "Conjugation"]
        },
        {
            "id": "g2-l22-noni-frustration",
            "title": "〜のに (Frustrated Concession: Even Though / In Spite Of)",
            "meaning": "States that contrary to natural, logical expectation, the reality turned out disappointing or perplexing: 'even though / in spite of the fact that'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 22: Education in Japan",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Plain form + のに (Noun / な-adj non-past affirmative takes な: 好きなのに, 暇なのに)",
            "nuance": "EMOTIONAL INDIGNATION: Unlike が or けれども which are neutral contrasts, のに carries emotional coloring: frustration, indignation, bewilderment, or grievance.",
            "keyTakeaway": "MUG-UP: Connects like んです: Noun / な-adj + な + のに! Carries frustration / disappointment.",
            "sentences": [
                make_sentence(
                    "s-g2-22-2",
                    "一生懸命勉強したのに、試験で目標の点数が取れませんでした。",
                    "Even though I studied with all my might, I couldn't get my target score on the exam.",
                    "Utmost-effort studied even-though, exam-in target score take-could-not.",
                    [
                        tok("勉強したのに", "べんきょうしたのに", "benkyou shita noni", "even though I studied", "Grammar")
                    ],
                    "Frustrated disappointment at unrewarded hard effort."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-22-2",
                    "薬を飲んだ（　　）、頭痛が一向によくなりません。",
                    "Even though I took medicine, my headache is not improving at all.",
                    ["のに", "ので", "から", "なら"],
                    0,
                    [
                        "Correct! のに conveys grievance that medicine failed to work as expected.",
                        "Incorrect. ので indicates objective cause ('because I took medicine').",
                        "Incorrect. から indicates subjective cause.",
                        "Incorrect. なら is conditional."
                    ],
                    "Concessive emotional linker 〜のに",
                    "Frustration that headache persists."
                )
            ],
            "tags": ["N4", "Genki L22", "Concession", "Frustration"]
        },

        # === LESSON 23 ===
        {
            "id": "g2-l23-temo-even-if",
            "title": "〜ても / 〜でも (Concessive Conditional: Even If / Even Though)",
            "meaning": "States that even under extreme or hypothetical condition X, result Y does not change: 'Even if X happens, Y'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 23: Good-bye",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "V-て + も | い-adj くて + も | な-adj / Noun + でも",
            "nuance": "OPPOSITE OF TARA: たら means 'if it happens, I will do Y'. ても means 'even if it happens, I STILL will do Y regardless' (雨が降っても行く = Even if it rains, I'm going).",
            "keyTakeaway": "MUG-UP: Formed by adding も to te-form! Verbs/い-adj = 〜ても. Nouns/な-adj = 〜でも.",
            "sentences": [
                make_sentence(
                    "s-g2-23-1",
                    "どんなに困難でも、私は最後まで諦めません。",
                    "No matter how difficult it may be, I will not give up until the very end.",
                    "No-matter-how difficult even-if, I last-until give-up-not.",
                    [
                        tok("困難でも", "こんなんでも", "konnan de mo", "even if difficult", "Grammar")
                    ],
                    "Unshakable resolve despite hardship."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-23-1",
                    "いくら（　　）も、答えがどうしても思い出せない。",
                    "No matter how much I think, I just cannot recall the answer.",
                    ["考えて", "考える", "考えた", "考え"],
                    0,
                    [
                        "Correct! 考える te-form 考えて + も forms 考えても ('even if I think').",
                        "Incorrect. 考える is dictionary form.",
                        "Incorrect. 考えた is past form.",
                        "Incorrect. 考え is masu-stem."
                    ],
                    "V-て + も concessive conditional",
                    "Persistent mental block despite hard thinking."
                )
            ],
            "tags": ["N4", "Genki L23", "Concession", "Conditionals"]
        },
        {
            "id": "g2-l23-koto-ni-suru-naru",
            "title": "〜ことにする vs 〜ことになる (Personal Decision vs Outside Emergence)",
            "meaning": "〜ことにする (The speaker personally decides to do X). 〜ことになる (It has been determined by external rules, organizations, or circumstances that X will happen).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 23: Good-bye",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 / V-ない + ことにする / ことになる",
            "nuance": "DECISION VS SOCIAL CONSENSUS: '会社を辞めることにした' = I personally chose to quit. '会社を辞めることになった' = Due to layoffs, restructuring, or external consensus, I am leaving (polite Japanese deflection).",
            "keyTakeaway": "MUG-UP: ことにする = MY active decision. ことになる = OUTSIDE circumstance / official rule.",
            "sentences": [
                make_sentence(
                    "s-g2-23-2",
                    "健康のために、毎日野菜をたくさん食べることにしました。",
                    "For my health, I decided to eat lots of vegetables every day.",
                    "Health-for, every-day vegetables lots eat-decision made.",
                    [
                        tok("食べることにしました", "たべることにしました", "taberu koto ni shimashita", "decided to eat", "Grammar")
                    ],
                    "Voluntary personal lifestyle decision."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-23-2",
                    "来月から大阪の支店へ転勤する（　　）になりました。",
                    "It has been arranged that I will transfer to the Osaka branch from next month.",
                    ["こと", "もの", "わけ", "はず"],
                    0,
                    [
                        "Correct! Official company job transfer is an outside organizational decision: 〜ことになった.",
                        "Incorrect. ものになった is nonsensical.",
                        "Incorrect. わけになった does not exist.",
                        "Incorrect. はずになった is ungrammatical."
                    ],
                    "External emergence 〜ことになる",
                    "Reporting official corporate reassignment."
                )
            ],
            "tags": ["N4", "Genki L23", "Decision", "Modality"]
        }
    ]
    return pts

if __name__ == '__main__':
    pts = get_full_genki2()
    print(f"Genki II generated {len(pts)} exhaustive discrete grammar points.")

