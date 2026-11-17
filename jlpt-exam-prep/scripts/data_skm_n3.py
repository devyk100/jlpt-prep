# -*- coding: utf-8 -*-
"""
Shin Kanzen Master N3 Bunpou - Complete Canonical Syllabus (Units 1 to 12 & Form Classifications A-J)
Fully annotated with lexical tokens, literal glosses, nuance notes, and 4-way quiz explanations.
"""
from data_genki1 import tok, make_sentence, make_quiz

def get_skm_n3_points():
    pts = [
        # Unit 1: 〜うちに
        {
            "id": "gp-skm3-uchini",
            "title": "〜うちに (While State Lasts / Before Opportunity Slips)",
            "meaning": "1) While a continuous situation persists, do something before it changes. 2) While doing X, a natural change Y occurred unnoticed.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 / V-ている / V-ない + うちに | い-adj + うちに | な-adj + な + うちに | Noun + の + うちに",
            "nuance": "URGENCY & TIME LIMIT: Clause B carries psychological pressure: if you don't act now during window A, it will become impossible later (冷めないうちに食べる - eat before it gets cold).",
            "keyTakeaway": "MUG-UP: V-ない + うちに = 'Before it becomes...' (暗くならないうちに = Before it gets dark).",
            "sentences": [
                make_sentence(
                    "s-skm3-1-1",
                    "スープが熱いうちに、どうぞ召し上がってください。",
                    "Please go ahead and enjoy the soup while it is still piping hot.",
                    "Soup hot-is while, please eat (respectful).",
                    [
                        tok("熱いうちに", "あついうちに", "atsui uchi ni", "while it is hot", "Grammar"),
                        tok("召し上がってください", "めしあがってください", "meshiagatte kudasai", "please eat (sonkeigo)", "Verb")
                    ],
                    "い-adjective connects directly to うちに."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-1",
                    "雨が（　　）うちに、急いで家に帰りましょう。",
                    "Let's hurry home before it starts raining.",
                    ["降らない", "降った", "降る", "降らなくて"],
                    0,
                    [
                        "Correct! 降らないうちに means 'before it rains / while it is not raining'.",
                        "Incorrect. 降ったうちに is ungrammatical (past cannot pair with うちに).",
                        "Incorrect. 降るうちに implies while it is actively raining.",
                        "Incorrect. 降らなくて cannot directly connect to うちに."
                    ],
                    "V-ない + うちに (Before...)",
                    "Taking action before a negative change occurs."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Time Limit", "Opportunity"]
        },

        # Unit 1: 〜ところだ (Phase of Action)
        {
            "id": "gp-skm3-tokoro-da",
            "title": "〜ところだ (Exact Phase of Action: Imminent, Ongoing, or Just Finished)",
            "meaning": "Pinpoints the exact temporal boundary of an action: 1) Just about to start (辞書形). 2) In the middle of doing (ている). 3) Just finished moments ago (た形).",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 + ところだ (About to) | V-ている + ところだ (Midst) | V-た + ところだ (Just finished)",
            "nuance": "CASE PARTICLE COMBINATIONS: ところへ (interrupted by an arrival), ところを (caught in the act with を), ところで (at the temporal junction).",
            "keyTakeaway": "MUG-UP: V-るところ (About to) -> V-ているところ (Right in middle) -> V-たところ (Just finished right now).",
            "sentences": [
                make_sentence(
                    "s-skm3-1-2",
                    "今から家を出るところですから、三十分後には着くと思います。",
                    "I am just about to leave the house right now, so I think I'll arrive in about 30 minutes.",
                    "Now house leave-about-to-am, 30-minutes-after arrive think.",
                    [
                        tok("出るところですから", "でるところですから", "deru tokoro desu kara", "just about to leave, so", "Grammar")
                    ],
                    "V-辞書形 + ところ marks imminent inception."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-2",
                    "ちょうど今、昼ご飯を食べ（　　）ところだから、お腹がいっぱいです。",
                    "I just finished eating lunch right now, so I am completely full.",
                    ["終わった", "終わる", "終わっている", "終われ"],
                    0,
                    [
                        "Correct! V-た + ところだ indicates an action that was completed moments ago.",
                        "Incorrect. 終わるところ implies about to finish, so one wouldn't be completely full yet.",
                        "Incorrect. 終わっているところ is awkward and redundant with ところ.",
                        "Incorrect. 終われ is the imperative form."
                    ],
                    "V-た + ところだ (Just completed)",
                    "Action concluded moments before the present utterance."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Aspect", "Temporal Phase"]
        },

        # Unit 1: 〜てからでないと
        {
            "id": "gp-skm3-te-kara-denaito",
            "title": "〜てからでないと / 〜てからでなければ (Not Until / Only After Doing X Can Y Happen)",
            "meaning": "Action Y cannot possibly take place unless condition X has been thoroughly fulfilled first ('Unless you do X first, Y cannot be done').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-て + からでないと / からでなければ + Negative / Impossible Predicate",
            "nuance": "MANDATORY NEGATIVE CONCEQUENCE: Clause B ALWAYS expresses an impossibility, refusal, or inability (できません, 決められません, 分かりません).",
            "keyTakeaway": "MUG-UP: V-て + からでないと + [Negative consequence] = 'Can't do Y until X is done!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-1-3",
                    "上司と相談してからでないと、この場でお返事はできません。",
                    "Unless I consult with my supervisor first, I cannot give you an answer on the spot.",
                    "Supervisor-with consult-after-only, this place-at reply cannot.",
                    [
                        tok("相談してからでないと", "そうだんしてからでないと", "soudan shite kara de nai to", "not until consulting", "Grammar"),
                        tok("お返事はできません", "おへんじはできません", "ohenji wa dekimasen", "cannot reply", "Grammar")
                    ],
                    "Strict prerequisite followed by polite business refusal."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-3",
                    "詳しい契約内容を（　　）からでないと、サインすることはできません。",
                    "Unless I read the detailed contract contents first, I cannot sign it.",
                    ["読んで", "読む", "読んだ", "読まない"],
                    0,
                    [
                        "Correct! 読む connects via te-form: 読んで + からでないと.",
                        "Incorrect. Dictionary form cannot connect to からでないと.",
                        "Incorrect. Past form cannot connect to からでないと.",
                        "Incorrect. Negative form cannot connect here."
                    ],
                    "V-て + からでないと prerequisite",
                    "Refusing signature until terms are thoroughly reviewed."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Prerequisite", "Time"]
        },

        # Unit 2: 〜とおりに / 〜どおりに
        {
            "id": "gp-skm3-toori-ni",
            "title": "〜とおりに / 〜どおりに (Just As / In Exact Accordance With)",
            "meaning": "Performing an action in exact, faithful accordance with instructions, thoughts, maps, or expectations ('Just as planned / As told').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "V-辞書形 / V-た + とおりに | Noun + の + とおりに | Noun + どおりに (Voiced sound without の!)",
            "nuance": "VOICING RULE (連濁): When attached directly to a noun without particle の, とおり voices into どおり: 計画どおり (as planned), 予想どおり (as predicted), 指示どおり (as instructed).",
            "keyTakeaway": "MUG-UP: Noun + の + とおりに OR Noun + どおりに (voiced!). V-る / V-た + とおりに.",
            "sentences": [
                make_sentence(
                    "s-skm3-2-3",
                    "レシピに書いてあるとおりに作ったら、とても美味しいケーキが焼き上がった。",
                    "When I made it just as written in the recipe, a delicious cake was baked.",
                    "Recipe-on written-is as-exact made-when, delicious cake baked-finished.",
                    [
                        tok("書いてあるとおりに", "かいてあるとおりに", "kaite aru toori ni", "just as it is written", "Grammar")
                    ],
                    "Following written recipe instructions to the letter."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-3",
                    "事態は我々の当初の計画（　　）に進展しており、何の問題もありません。",
                    "The situation is progressing exactly according to our original plan, and there are no problems whatsoever.",
                    ["どおり", "とおり", "ばかり", "ほど"],
                    0,
                    [
                        "Correct! Noun 計画 combines directly as 計画どおり (voiced without の).",
                        "Incorrect. とおり directly after noun requires の (計画のとおり).",
                        "Incorrect. ばかり means only / just.",
                        "Incorrect. ほど means extent or proportion."
                    ],
                    "Noun + どおり (Voiced without の)",
                    "Adhering faithfully to the initial operational plan."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Accordance", "Adherence"]
        },

        # Unit 2: 〜ついでに
        {
            "id": "gp-skm3-tsuide-ni",
            "title": "〜ついでに (While at It / Taking Advantage of the Opportunity)",
            "meaning": "While performing primary task A, seizing the opportunity to conveniently execute secondary task B ('While you're at the store, could you also buy...').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 / V-た + ついでに | Noun + の + ついでに",
            "nuance": "PRIMARY VS INCIDENTAL: Action A is the main planned errand. Action B is an incidental side errand piggybacking on A.",
            "keyTakeaway": "MUG-UP: V-る / V-た / Noun + の + ついでに = Convenient 2-for-1 side action!",
            "sentences": [
                make_sentence(
                    "s-skm3-2-4",
                    "郵便局へ切手を買いに行くついでに、コンビニで公共料金を支払ってきた。",
                    "While heading to the post office to buy stamps, I stopped by the convenience store and paid my utility bills.",
                    "Post-office stamps buy go while-at-it, convenience-store utility-bills paid.",
                    [
                        tok("行くついでに", "いくついでに", "iku tsuide ni", "while going (convenient opportunity)", "Grammar")
                    ],
                    "Taking advantage of an errand outing to pay bills."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-4",
                    "散歩の（　　）、ポストにこの手紙を投函してきてくれませんか。",
                    "While you're out taking a walk, would you mind dropping this letter into the mailbox for me?",
                    ["ついでに", "たびに", "うちに", "最中に"],
                    0,
                    [
                        "Correct! 散歩のついでに means conveniently posting the letter while already out on a walk.",
                        "Incorrect. たびに means every single time you walk.",
                        "Incorrect. うちに means before the walk ends or before an opportunity slips.",
                        "Incorrect. 最中に means right in the middle of walking."
                    ],
                    "Noun + の + ついでに (Incidental side-task)",
                    "Piggybacking a chore onto an existing outing."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Convenience", "Time"]
        },

        # Unit 2: 〜たびに
        {
            "id": "gp-skm3-tabini",
            "title": "〜たびに (Every Single Time / Whenever)",
            "meaning": "Whenever X happens, Y invariably occurs as a natural or habitual accompaniment ('Every time I see this photo, I remember...').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 + たびに | Noun + の + たびに",
            "nuance": "EMOTIONAL REPETITION: Used when the speaker notices a recurring pattern or emotional reflex.",
            "keyTakeaway": "MUG-UP: V-る / Noun + の + たびに = Invariable recurrence ('every single time without exception').",
            "sentences": [
                make_sentence(
                    "s-skm3-2-1",
                    "この曲を聴くたびに、楽しかった学生時代を思い出します。",
                    "Every time I listen to this song, I recall my happy student days.",
                    "This song hear every-time, enjoyable student-era recall.",
                    [
                        tok("聴くたびに", "きくたびに", "kiku tabi ni", "every time I listen", "Grammar")
                    ],
                    "Emotional trigger recurs whenever the song plays."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-1",
                    "父は出張の（　　）、家族にその土地の名物のお菓子を買ってきてくれる。",
                    "Every time my father goes on a business trip, he buys local specialty sweets for the family.",
                    ["たびに", "うちに", "ついでに", "最中に"],
                    0,
                    [
                        "Correct! 出張のたびに expresses habitual recurrence on every single business trip.",
                        "Incorrect. うちに means while or before opportunity slips.",
                        "Incorrect. ついでに means taking advantage of an errand to do another side task.",
                        "Incorrect. 最中に means right in the middle of a continuous event."
                    ],
                    "Noun + の + たびに",
                    "Recurrent occurrence on every instance of the noun."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Repetition", "Recurrence"]
        },

        # Unit 2: (〜ば)〜ほど
        {
            "id": "gp-skm3-ba-hodo",
            "title": "(〜ば)〜ほど (Proportional Correlation: The More... The More...)",
            "meaning": "As the degree of condition A increases, the degree of consequence B increases proportionally ('The more you practice, the better you get').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "V-ば + V-辞書形 + ほど | い-adj ければ + い-adj + ほど | な-adj なら + な-adj な + ほど | Noun + であればあるほど",
            "nuance": "ELLIPSIS ALLOWED: The first conditional part (〜ば) can be omitted in spoken Japanese.",
            "keyTakeaway": "MUG-UP: [ば-form] + [Dictionary form] + ほど = The more X, the more Y.",
            "sentences": [
                make_sentence(
                    "s-skm3-2-2",
                    "外国語は使えば使うほど、上手に話せるようになります。",
                    "The more you use a foreign language, the more fluently you become able to speak it.",
                    "Foreign-language use-if use-extent, skillfully speak able become.",
                    [
                        tok("使えば使うほど", "つかえばつかうほど", "tsukaeba tsukau hodo", "the more you use it", "Grammar")
                    ],
                    "Proportional growth between usage and fluency."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-2",
                    "荷物は（　　）ほど、旅行は身軽で快適になる。",
                    "The less luggage you have, the lighter and more comfortable your trip becomes.",
                    ["少なければ少ない", "少ないなら少ない", "少なくて少ない", "少ないと少ない"],
                    0,
                    [
                        "Correct! い-adjective proportional formula: 少なければ + 少ない + ほど.",
                        "Incorrect. なら does not combine in this standard correlative pair with い-adjectives.",
                        "Incorrect. て-form cannot establish this proportional formula.",
                        "Incorrect. と conditional does not match the ほど correlative construction."
                    ],
                    "い-adjective (〜ければ)〜ほど",
                    "Expressing proportional scale with an い-adjective."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Proportion", "Correlation"]
        },

        # Unit 3: 〜くらいなら
        {
            "id": "gp-skm3-kurai-nara",
            "title": "〜くらいなら (Rather Than Suffer X, I'd Prefer Extreme Y)",
            "meaning": "Considers condition X so unbearable that one would rather choose an extreme, drastic alternative Y instead ('If it comes down to doing X, I'd rather die/quit!').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "V-辞書形 + くらいなら / ぐらいなら + Preferable Alternative (〜ほうがいい, 〜ほうがましだ)",
            "nuance": "HYPERBOLIC RESENTMENT: Option A is painted as utterly intolerable. Option B represents a radical sacrifice that is still preferable to A.",
            "keyTakeaway": "MUG-UP: V-る + くらいなら = 'Rather than suffer X, I'd far prefer Y!'. Pairs with 〜ほうがましだ.",
            "sentences": [
                make_sentence(
                    "s-skm3-3-2",
                    "不正をしてまで合格するくらいなら、堂々と落ちて再挑戦するほうがましだ。",
                    "Rather than passing by resorting to dishonesty, I would far prefer to fail with dignity and try again.",
                    "Dishonesty doing-to-extent pass rather-than, proudly fail re-challenge side preferable-is.",
                    [
                        tok("合格するくらいなら", "ごうかくするくらいなら", "goukaku suru kurai nara", "rather than passing via deceit", "Grammar"),
                        tok("ほうがましだ", "ほうがましだ", "hou ga mashi da", "is far preferable", "Expression")
                    ],
                    "Ethical rejection of a dishonest shortcut."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-3-2",
                    "あんな嫌味な上司に頭を（　　）くらいなら、会社を辞めたほうがずっといい。",
                    "Rather than bow my head to such a sarcastic boss, I'd much rather quit the company.",
                    ["下げる", "下げた", "下げて", "下げない"],
                    0,
                    [
                        "Correct! V-辞書形 下げる connects directly to くらいなら.",
                        "Incorrect. Past 下げた cannot connect to くらいなら.",
                        "Incorrect. Te-form cannot connect to くらいなら.",
                        "Incorrect. Negative cannot connect here."
                    ],
                    "V-辞書形 + くらいなら (Rather than...)",
                    "Strong preference for quitting over humiliating subjugation."
                )
            ],
            "tags": ["N3", "SKM Unit 3", "Preference", "Hyperbole"]
        },

        # Unit 3: 〜に限る
        {
            "id": "gp-skm3-ni-kagiru",
            "title": "〜に限る (Nothing Beats... / The Best Method Is)",
            "meaning": "Subjective judgment that X is definitively the best, unsurpassed choice or remedy ('There's nothing quite like X').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun + に限る | V-辞書形 / V-ない + に限る",
            "nuance": "SPEAKER'S PERSONAL BIAS: This is not an objective scientific law; it is the speaker's firm conviction based on experience.",
            "keyTakeaway": "MUG-UP: X に限る = X is the absolute best way! Cannot be used for objective facts.",
            "sentences": [
                make_sentence(
                    "s-skm3-3-1",
                    "風邪をひいた時は、温かいものを食べて早く寝るに限る。",
                    "When you have caught a cold, nothing beats eating something warm and going to bed early.",
                    "Cold caught time, warm-thing eating early sleeping best-is.",
                    [
                        tok("寝るに限る", "ねるにかぎる", "neru ni kagiru", "going to bed is the absolute best", "Grammar")
                    ],
                    "Speaker's strong conviction regarding the best cold remedy."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-3-1",
                    "暑い夏の日の仕事終わりには、やっぱり冷えたビールに（　　）。",
                    "At the end of work on a hot summer day, there is really nothing quite like an ice-cold beer.",
                    ["限る", "過ぎる", "至る", "沿う"],
                    0,
                    [
                        "Correct! 〜に限る expresses that cold beer is the unsurpassed, ideal choice.",
                        "Incorrect. 過ぎる means to exceed or do excessively.",
                        "Incorrect. 至る means to arrive at a terminal stage.",
                        "Incorrect. 沿う means to conform to or follow along a line."
                    ],
                    "Noun + に限る (Nothing beats...)",
                    "Declaring an option as definitively best."
                )
            ],
            "tags": ["N3", "SKM Unit 3", "Best Choice", "Subjective"]
        },

        # Unit 4: 〜に対して
        {
            "id": "gp-skm3-ni-taishite",
            "title": "〜に対して (In Sharp Contrast To / Toward an Object)",
            "meaning": "1) Contrasts two entities displaying opposite traits ('Whereas A is..., B is...'). 2) Directs an attitude or action toward someone ('Rude toward customers').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Noun + に対して | Plain clause + のに対して (Noun/な-adj non-past affirmative: なのに対して)",
            "nuance": "TWO DIFFERENT FUNCTIONS: Contrast ('兄が活発なのに対して弟はおとなしい') vs Target of attitude ('客に対して敬語を使う').",
            "keyTakeaway": "MUG-UP: A のに対して B = A and B stand in polar opposition. Target: [Person] に対して = Toward [Person].",
            "sentences": [
                make_sentence(
                    "s-skm3-4-1",
                    "兄が社交的で外交的なのに対して、弟は家で読書をするのが好きな内向的な性格だ。",
                    "Whereas the older brother is sociable and outgoing, the younger brother has an introverted personality who prefers reading books at home.",
                    "Older-brother sociable being whereas, younger-brother home reading like introverted personality is.",
                    [
                        tok("外交的なのに対して", "がいこうてきなのに対して", "gaikouteki na no ni taishite", "whereas he is outgoing", "Grammar")
                    ],
                    "な-adjective takes な + のに対して for sharp contrast."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-4-1",
                    "前学期は成績が優秀だった（　　）に対して、今学期は少し怠けてしまった。",
                    "Whereas my grades were outstanding last semester, I slacked off a bit this semester.",
                    ["の", "こと", "もの", "わけ"],
                    0,
                    [
                        "Correct! Contrast clauses take [Plain sentence] + のに対して.",
                        "Incorrect. ことに対して is not the standard contrastive clause formula.",
                        "Incorrect. ものに対して is ungrammatical here.",
                        "Incorrect. わけに対して does not exist in standard grammar."
                    ],
                    "Clause + のに対して contrast",
                    "Contrasting past academic success with present decline."
                )
            ],
            "tags": ["N3", "SKM Unit 4", "Contrast", "Opposition"]
        },

        # Unit 4: 〜反面
        {
            "id": "gp-skm3-hanmen",
            "title": "〜反面 (On the Flip Side / But on the Other Hand)",
            "meaning": "Presents two opposing, contradictory aspects existing simultaneously within the very same entity, situation, or person ('Convenient, but on the flip side, expensive').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Plain form + 反面 (な-adj takes な/である, Noun takes である)",
            "nuance": "SAME COIN PARADOX: Unlike 対して which contrasts two different people, 反面 examines the two sides of a SINGLE coin (e.g., urban living is exciting, but on the flip side, noisy).",
            "keyTakeaway": "MUG-UP: Two opposing sides of the SAME subject. な-adj takes な + 反面 / である反面.",
            "sentences": [
                make_sentence(
                    "s-skm3-4-2",
                    "この薬は即効性があって効果が高い反面、眠気などの強い副作用が生じる恐れがある。",
                    "While this medication works rapidly and is highly effective, on the flip side there is a risk of severe side effects such as drowsiness.",
                    "This medicine rapid-action having effect high flip-side, drowsiness strong side-effects occur risk has.",
                    [
                        tok("効果が高い反面", "こうかがたかいはんめん", "kouka ga takai hanmen", "high efficacy, but on the flip side", "Grammar")
                    ],
                    "Balancing medical efficacy against adverse side effects."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-4-2",
                    "一人暮らしは自由気ままで快適な（　　）、病気の時は非常に心細い。",
                    "While living alone is free and comfortable, on the flip side, when you are sick you feel terribly lonely and helpless.",
                    ["反面", "ついでに", "とたんに", "かぎりに"],
                    0,
                    [
                        "Correct! 快適な反面 contrasts the liberating comfort against the vulnerable loneliness of living alone.",
                        "Incorrect. ついでに means taking advantage of an opportunity to do a side chore.",
                        "Incorrect. とたんに means the instant that an accident occurs.",
                        "Incorrect. かぎりに is ungrammatical here."
                    ],
                    "な-adj + な + 反面 two sides of same coin",
                    "Contrasting the freedom and vulnerability of living alone."
                )
            ],
            "tags": ["N3", "SKM Unit 4", "Flip Side", "Contrast"]
        },

        # Unit 4: 〜というより
        {
            "id": "gp-skm3-to-iu-yori",
            "title": "〜というより (Rather Than Calling It X, It's More Like Y)",
            "meaning": "Corrects or refines an initial description: 'Rather than saying X, it would be more accurate to describe it as Y'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Word/Clause A + というより (は) + Word/Clause B",
            "nuance": "PRECISION REFRAMING: Speaker feels label A is somewhat misleading or an understatement; label B captures the nuance far better.",
            "keyTakeaway": "MUG-UP: A というより B = 'Not so much A, but rather B!'. Connects directly to words or plain forms.",
            "sentences": [
                make_sentence(
                    "s-skm3-4-3",
                    "彼は親切というよりは、単に断るのが苦手なだけなのかもしれない。",
                    "Rather than being kind, it might be that he simply struggles with saying no.",
                    "He kind saying-than, simply refuse weak-at only might-be.",
                    [
                        tok("親切というよりは", "しんせつというよりは", "shinsetsu to iu yori wa", "rather than being kind", "Grammar")
                    ],
                    "Reframing someone's apparent kindness as inability to decline."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-4-3",
                    "昨日の試験は難しかったという（　　）、問題量が多すぎて時間が足りなかった。",
                    "Rather than saying yesterday's exam was difficult, the volume of questions was simply so vast that time ran out.",
                    ["より", "ほど", "ばかり", "とおり"],
                    0,
                    [
                        "Correct! というより reframes the cause from exam difficulty to excessive time pressure.",
                        "Incorrect. というほど means 'not to the extent that'.",
                        "Incorrect. というばかり is ungrammatical.",
                        "Incorrect. というとおり is ungrammatical."
                    ],
                    "〜というより reframing",
                    "Refining a statement to pinpoint the real issue."
                )
            ],
            "tags": ["N3", "SKM Unit 4", "Reframing", "Nuance"]
        },

        # Unit 5: 〜おかげで vs 〜せいで
        {
            "id": "gp-skm3-okage-sei",
            "title": "〜おかげで vs 〜せいで (Gratitude vs Blame / Causal Attributions)",
            "meaning": "おかげで (Thanks to X, a desirable outcome occurred). せいで (Due to X's fault, an undesirable consequence occurred).",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 5: 原因・理由 (Causes & Reasons)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + おかげで / せいで (な-adj takes な, Noun takes の)",
            "nuance": "IRONIC EXCEPTION: おかげで can sometimes be used sarcastically.",
            "keyTakeaway": "MUG-UP: おかげで = Good outcome (Gratitude). せいで = Bad outcome (Blame). Noun + の + おかげで / せいで.",
            "sentences": [
                make_sentence(
                    "s-skm3-5-1",
                    "先生が熱心に教えてくださったおかげで、無事に合格することができました。",
                    "Thanks to the teacher teaching me so passionately, I was able to pass safely.",
                    "Teacher passionately taught thanks-to, safely pass able-was.",
                    [
                        tok("教えてくださったおかげで", "おしえてくださったおかげで", "oshiete kudasatta okage de", "thanks to having taught me", "Grammar")
                    ],
                    "Gratitude for a favorable outcome resulting from teacher's help."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-5-1",
                    "昨夜の台風の（　　）、電車が大幅に遅れて会議に間に合わなかった。",
                    "Owing to last night's typhoon, the train was drastically delayed and I missed the meeting.",
                    ["せいで", "おかげで", "ために", "せっかく"],
                    0,
                    [
                        "Correct! Missing a meeting due to a typhoon is an undesirable outcome, requiring せいで.",
                        "Incorrect. おかげで is for positive outcomes (gratitude).",
                        "Incorrect. 台風のために is possible, but 台風のせいで is the canonical choice when assigning fault.",
                        "Incorrect. せっかく means 'with much trouble / precious opportunity'."
                    ],
                    "Noun + の + せいで (Blame)",
                    "Attributing a negative outcome to an external disruption."
                )
            ],
            "tags": ["N3", "SKM Unit 5", "Cause", "Gratitude", "Blame"]
        },

        # Unit 6: 〜さえ〜ば
        {
            "id": "gp-skm3-sae-ba",
            "title": "〜さえ〜ば (If Only / The Sole Necessary Condition)",
            "meaning": "If only this single minimal condition is satisfied, everything else will be fine or succeed ('All you need is...').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 6: 条件・仮定 (Conditions & Hypotheses)",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "Noun + さえ + V-ば / い-adj ければ / な-adj なら | V-stem + さえすれば",
            "nuance": "PARTICLE ABSORPTION: さえ replaces case particles が and を directly.",
            "keyTakeaway": "MUG-UP: [Noun] さえ [Verb-ば] = As long as / If only this one thing happens! Replaces が and を.",
            "sentences": [
                make_sentence(
                    "s-skm3-6-1",
                    "パスポートとクレジットカードさえあれば、何とかなりますよ。",
                    "As long as you have your passport and credit card, you'll manage somehow.",
                    "Passport and credit-card only have-if, somehow manage will.",
                    [
                        tok("さえあれば", "さえあれば", "sae areba", "if only you have", "Grammar")
                    ],
                    "Minimal requirement ensuring success."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-6-1",
                    "道が（　　）さえすれば、あと十分で空港に着くはずです。",
                    "As long as the roads are not congested, we should arrive at the airport in ten minutes.",
                    ["混み", "混む", "混んで", "混ま"],
                    0,
                    [
                        "Correct! Verb stem formula: V-stem + さえすれば (混む stem is 混み).",
                        "Incorrect. 混む is dictionary form; cannot precede さえすれば.",
                        "Incorrect. 混んで is te-form.",
                        "Incorrect. 混ま is negative stem."
                    ],
                    "V-stem + さえすれば",
                    "Minimal condition formula with verb stem."
                )
            ],
            "tags": ["N3", "SKM Unit 6", "Minimal Condition", "Conditionals"]
        },

        # Unit 8: 〜わけがない
        {
            "id": "gp-skm3-wake-ga-nai",
            "title": "〜わけがない / 〜はずがない (Emphatic Impossibility: Cannot Possibly Be)",
            "meaning": "The speaker emphatically denies the possibility of something based on objective logical grounds ('There is absolutely no reason why X could be true!').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + わけがない (な-adj takes な, Noun takes の)",
            "nuance": "LOGICAL CONVICTION: Asserts that based on known laws of logic and nature, it is unthinkable.",
            "keyTakeaway": "MUG-UP: わけがない = Mathematically / logically impossible! Noun + の / な-adj + な + わけがない.",
            "sentences": [
                make_sentence(
                    "s-skm3-8-1",
                    "こんなに難しい専門書を、一度読んだだけで理解できるわけがありません。",
                    "There is no way on earth anyone could comprehend such a difficult specialized book after reading it just once.",
                    "Such difficult specialist-book once read only understand able reason-none.",
                    [
                        tok("理解できるわけがありません", "りかいできるわけがありません", "rikai dekiru wake ga arimasen", "cannot possibly understand", "Grammar")
                    ],
                    "Logical impossibility asserted by speaker."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-8-1",
                    "あんなに真面目な山田さんが、会社のお金を盗む（　　）がない。",
                    "There is no way that such a diligent person like Yamada-san would steal company money.",
                    ["わけ", "こと", "もの", "つもり"],
                    0,
                    [
                        "Correct! 〜わけがない expresses strong logical conviction that the claim is impossible.",
                        "Incorrect. 盗むことがない means 'never steals' (habit/experience), lacking emphatic denial.",
                        "Incorrect. ものがない is ungrammatical here.",
                        "Incorrect. つもりがない means 'has no intention to steal', not logical impossibility."
                    ],
                    "〜わけがない logical impossibility",
                    "Denying an accusation based on character evidence."
                )
            ],
            "tags": ["N3", "SKM Unit 8", "Impossibility", "Certainty"]
        },

        # Unit 8: 〜わけではない
        {
            "id": "gp-skm3-wake-dewa-nai",
            "title": "〜わけではない (Partial Negation: It Does Not Mean That...)",
            "meaning": "Partially negates an assumption or extreme conclusion: 'It is not necessarily true that...' or 'It does not mean that...'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + わけではない (な-adj takes な, Noun takes の/である)",
            "nuance": "SOFTENING ABSOLUTES: Used to clarify that while something might seem true at first glance, the reality is nuanced.",
            "keyTakeaway": "MUG-UP: わけではない = Partial negation ('It is not the case that...'). Protects against misunderstandings.",
            "sentences": [
                make_sentence(
                    "s-skm3-8-2",
                    "日本料理が嫌いなわけではありませんが、納豆だけはどうしても苦手です。",
                    "It does not mean that I dislike Japanese cuisine, but natto is the one thing I just cannot handle.",
                    "Japanese-food hate reason-is-not but, natto only just weak-at.",
                    [
                        tok("嫌いなわけではありませんが", "きらいなわけではありませんが", "kirai na wake dewa arimasen ga", "it is not that I dislike it, but", "Grammar")
                    ],
                    "Partial denial of disliking Japanese food in general."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-8-2",
                    "生活に不満がある（　　）ではないが、もっと広い家に引っ越したい。",
                    "It is not that I am dissatisfied with my life, but I would like to move to a larger house.",
                    ["わけ", "はず", "もの", "こと"],
                    0,
                    [
                        "Correct! わけではない performs partial softening negation ('it is not that...').",
                        "Incorrect. はずではない is ungrammatical (must be はずがない).",
                        "Incorrect. ものではない indicates social disapproval, not partial negation.",
                        "Incorrect. ことではない does not form standard partial negation."
                    ],
                    "〜わけではない partial negation",
                    "Clarifying that life is not entirely unsatisfactory."
                )
            ],
            "tags": ["N3", "SKM Unit 8", "Partial Negation", "Nuance"]
        },

        # Unit 10: 〜べきだ
        {
            "id": "gp-skm3-bekida",
            "title": "〜べきだ / 〜べきではない (Moral Obligation & Social Duty: Ought to)",
            "meaning": "States a strong moral, ethical, or social duty: 'One ought to do X' (common sense / universal conscience). Negative: 'Must not do'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 10: 助言・義務 (Advice & Duty)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + べきだ (する irregular: すべきだ or するべきだ) | Negative: べきではない",
            "nuance": "NOT RULES OR LAWS: Laws and regulations use なければならない. べきだ reflects universal ethics and social propriety.",
            "keyTakeaway": "MUG-UP: する irregular has two accepted forms: すべきだ (formal) and するべきだ. Ethical obligation.",
            "sentences": [
                make_sentence(
                    "s-skm3-10-1",
                    "約束した時間は絶対に守るべきです。社会人の基本マナーですから。",
                    "You ought to strictly keep the promised time. It is basic etiquette for a working adult.",
                    "Promised time absolutely keep-ought. Working-adult's basic manner is because.",
                    [
                        tok("守るべきです", "まもるべきです", "mamoru beki desu", "ought to keep / protect", "Grammar")
                    ],
                    "Ethical societal obligation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-10-1",
                    "困っている人がいたら、進んで手を差し伸べる（　　）だ。",
                    "If someone is in distress, one ought to proactively extend a helping hand.",
                    ["べき", "はず", "わけ", "こと"],
                    0,
                    [
                        "Correct! 〜べきだ expresses ethical and moral duty toward someone in trouble.",
                        "Incorrect. はずだ expresses logical expectation, not moral duty.",
                        "Incorrect. わけだ expresses natural consequence or explanatory conclusion.",
                        "Incorrect. ことだ is personal practical advice, whereas べきだ is universal conscience."
                    ],
                    "〜べきだ moral duty",
                    "Moral duty to assist those in distress."
                )
            ],
            "tags": ["N3", "SKM Unit 10", "Obligation", "Ethics"]
        },

        # Form E: 〜わけにはいかない
        {
            "id": "gp-skm3-wake-niwa-ikanai",
            "title": "〜わけにはいかない vs 〜ないわけにはいかない (Psychological / Social Constraint)",
            "meaning": "〜わけにはいかない (Cannot do X due to moral, social, or emotional conscience). 〜ないわけにはいかない (Must do X because conscience/duty leaves no choice).",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 E: わけの用法 (Uses of Wake)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + わけにはいかない (Cannot do) | V-ない + わけにはいかない (Cannot NOT do = Must do)",
            "nuance": "CONSCIENCE CONSTRAINT: Physically one is capable of doing it, but social shame, duty, or conscience prevents it.",
            "keyTakeaway": "MUG-UP: わけにはいかない = Social/moral guilt prevents doing it. ないわけにはいかない = Obliged to do it!",
            "sentences": [
                make_sentence(
                    "s-skm3-e-1",
                    "明日は重要なプレゼンがあるので、熱があっても休むわけにはいきません。",
                    "I have an important presentation tomorrow, so even if I have a fever, I cannot afford to take the day off.",
                    "Tomorrow important presentation have because, fever have even take-off reason cannot-go.",
                    [
                        tok("休むわけにはいきません", "やすむわけにはいきません", "yasumu wake niwa ikimasen", "cannot afford to take off (conscience)", "Grammar")
                    ],
                    "Conscience and professional responsibility dictate attendance."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-e-1",
                    "親友の結婚式ですから、どんなに忙しくても出席（　　）わけにはいきません。",
                    "Since it is my best friend's wedding, no matter how busy I am, I cannot fail to attend.",
                    ["しない", "する", "して", "した"],
                    0,
                    [
                        "Correct! Double negative ないわけにはいかない expresses the imperative obligation to attend.",
                        "Incorrect. 出席するわけにはいかない would mean 'I cannot attend', contrary to best friend loyalty.",
                        "Incorrect. して cannot connect to わけにはいかない.",
                        "Incorrect. した is past tense and ungrammatical here."
                    ],
                    "V-ない + わけにはいかない (Must do)",
                    "Double negative expressing compelling moral duty."
                )
            ],
            "tags": ["N3", "SKM Form E", "Conscience", "Constraint"]
        },

        # Form J: 〜がち (Tendency to / Prone to Negatives)
        {
            "id": "gp-skm3-gachi",
            "title": "〜がち (Prone to Negative Habit / Tendency to Often...)",
            "meaning": "Has a strong recurring tendency or habit to end up in an undesirable state ('Prone to catching colds / Often forgets').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "V-stem (ます形 without ます) + がち | Noun + がち (Conjugates as な-adjective: 〜がちな, 〜がちだ)",
            "nuance": "NEGATIVE BIAS: Used almost exclusively for undesirable lapses, weaknesses, or human faults (遅刻しがち, 忘れがち, 遠慮しがち, 曇りがち). Cannot be used for positive habits.",
            "keyTakeaway": "MUG-UP: V-stem / Noun + がち = Tendency towards a NEGATIVE habit! Becomes a な-adjective (遅刻しがちな人).",
            "sentences": [
                make_sentence(
                    "s-skm3-j-1",
                    "一人暮らしを始めると、外食が増えて栄養のバランスが偏りがちになる。",
                    "When you start living alone, eating out increases and your nutritional balance tends to become skewed.",
                    "Alone-living start-when, eating-out increase nutrition balance skew-prone become.",
                    [
                        tok("偏りがちになる", "かたよりがちになる", "katayorigachi ni naru", "tends to become unbalanced", "Grammar")
                    ],
                    "Negative nutritional tendency when living alone."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-j-1",
                    "季節の変わり目は、体調を崩し（　　）ですから、健康管理に気をつけましょう。",
                    "During seasonal transitions, one is prone to falling ill, so let us take care of our health.",
                    ["がち", "気味", "っぽい", "だらけ"],
                    0,
                    [
                        "Correct! 体調を崩し (masu-stem of 崩す) + がち denotes frequent susceptibility to falling ill.",
                        "Incorrect. 気味 attaches to nouns or stems for a mild present symptom (風邪気味), but 崩しがち is the canonical verbal tendency.",
                        "Incorrect. っぽい indicates personality resemblance or prone to temper (怒りっぽい).",
                        "Incorrect. だらけ means covered in dirt/mistakes."
                    ],
                    "V-stem + がち negative tendency",
                    "Prone to health decline during seasonal shifts."
                )
            ],
            "tags": ["N3", "SKM Form J", "Tendency", "Negative Habit"]
        },

        # Form J: 〜気味 (Slight Feeling / Touch of...)
        {
            "id": "gp-skm3-gimi",
            "title": "〜気味 (Slight Touch of / Mild Sensation of)",
            "meaning": "Displays a slight, faint touch or physical symptom of an unfavorable state ('A touch of a cold / Slightly stressed').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "V-stem (ます形 without ます) + 気味 | Noun + 気味 (風邪気味, 疲れ気味, 寝不足気味, 太り気味)",
            "nuance": "GENTLE SYMPTOM: You haven't fully fallen sick yet, but you sense the early faint signs. Common pairings: 風邪気味 (touch of a cold), 緊張気味 (a bit nervous).",
            "keyTakeaway": "MUG-UP: Sensation of a slight touch: 風邪気味 (touch of cold), 太り気味 (gained a bit of weight).",
            "sentences": [
                make_sentence(
                    "s-skm3-j-2",
                    "最近少し風邪気味で喉が痛いので、今夜は早めに休むことにします。",
                    "Recently I've had a slight touch of a cold and my throat hurts, so I've decided to turn in early tonight.",
                    "Recently slightly cold-touch throat hurts because, tonight early rest decide.",
                    [
                        tok("風邪気味で", "かぜぎみで", "kaze gimi de", "with a touch of a cold", "Grammar")
                    ],
                    "Early onset of mild cold symptoms."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-j-2",
                    "連日の残業が続いて、社員全体が少し（　　）気味になっている。",
                    "Due to continuous daily overtime, the entire staff has become slightly overtired.",
                    ["疲れ", "疲れた", "疲れる", "疲れて"],
                    0,
                    [
                        "Correct! 疲れる masu-stem 疲れ + 気味 forms 疲れ気味 ('a touch overtired').",
                        "Incorrect. Past form cannot attach to 気味.",
                        "Incorrect. Dictionary form cannot attach to 気味.",
                        "Incorrect. Te-form cannot attach to 気味."
                    ],
                    "V-stem + 気味 mild sensation",
                    "Early fatigue from cumulative work pressure."
                )
            ],
            "tags": ["N3", "SKM Form J", "Symptom", "Subtle"]
        }
    ]
    return pts

if __name__ == '__main__':
    points = get_skm_n3_points()
    print(f"SKM N3 generated {len(points)} grammar points.")
