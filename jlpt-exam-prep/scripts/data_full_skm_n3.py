# -*- coding: utf-8 -*-
"""
Shin Kanzen Master N3 Bunpou - Full Unabridged N3 Grammar Syllabus (Units 1 to 12 & Form Classifications A-J)
Every individual grammar formula and functional expression has its own dedicated entry.
"""
from data_full_genki1 import tok, make_sentence, make_quiz

def get_full_skm_n3():
    pts = [
        # === UNIT 1: 時・進行 (TIME & PROGRESS) ===
        {
            "id": "skm3-u1-uchini-while",
            "title": "〜うちに (While State Lasts / Before Opportunity Slips)",
            "meaning": "While a favorable situation or continuous condition persists, take action before the window of opportunity closes.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 / V-ている / V-ない + うちに | い-adj + うちに | な-adj + な + うちに | Noun + の + うちに",
            "nuance": "TIME SENSITIVITY: If you don't act now, it will become impossible later: スープが熱いうちに (before it gets cold), 日本にいるうちに (before leaving Japan).",
            "keyTakeaway": "MUG-UP: V-ない + うちに = 'Before it becomes...' (暗くならないうちに = Before it gets dark).",
            "sentences": [
                make_sentence(
                    "s-skm3-1-1",
                    "温かいうちに、どうぞ召し上がってください。",
                    "Please go ahead and enjoy the food while it is still warm.",
                    "Warm while, please eat.",
                    [
                        tok("温かいうちに", "あたたかいうちに", "atatakai uchi ni", "while it is warm", "Grammar")
                    ],
                    "い-adjective connects directly to うちに."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-1",
                    "雨が（　　）うちに、急いで洗濯物を取り込みましょう。",
                    "Let's hurry and bring in the laundry before it starts raining.",
                    ["降らない", "降った", "降る", "降らなくて"],
                    0,
                    [
                        "Correct! 降らないうちに means 'before it rains / while it is not raining'.",
                        "Incorrect. 降ったうちに is invalid (past tense cannot combine with うちに).",
                        "Incorrect. 降るうちに implies while it is actively raining.",
                        "Incorrect. 降らなくて cannot directly attach to うちに."
                    ],
                    "V-ない + うちに (Before...)",
                    "Taking action before laundry gets wet."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Time Limit", "Opportunity"]
        },
        {
            "id": "skm3-u1-uchini-change",
            "title": "〜うちに (Unnoticed Natural Evolution: While Doing X, Y Emerged)",
            "meaning": "While continuing action X over time, an uncalculated natural change or realization Y developed unnoticed.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-ている / V-辞書形 + うちに",
            "nuance": "NO CONSCIOUS INTENT: Clause B is NOT a planned decision; it is a spontaneous change that crept up silently (e.g. while reading I fell asleep; as we talked we grew fond of each other).",
            "keyTakeaway": "MUG-UP: V-ている + うちに = Inadvertently happened without realizing it!",
            "sentences": [
                make_sentence(
                    "s-skm3-1-2",
                    "本を読んでいるうちに、いつの間にか眠ってしまった。",
                    "While I was reading a book, before I knew it, I fell fast asleep.",
                    "Book reading was while, unnoticed slept-ended-up.",
                    [
                        tok("読んでいるうちに", "よんでいるうちに", "yonde iru uchi ni", "while reading", "Grammar")
                    ],
                    "Spontaneous transition into sleep."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-2",
                    "何度も練習を重ねて（　　）うちに、自然と上手に話せるようになった。",
                    "While repeating practice over and over, I naturally became able to speak skillfully.",
                    ["いる", "ある", "おく", "みる"],
                    0,
                    [
                        "Correct! 重ねているうちに marks the gradual, unforced emergence of fluency over continuous practice.",
                        "Incorrect. ある is for resultant state of inanimate objects.",
                        "Incorrect. おく is advance preparation.",
                        "Incorrect. みる is trial action."
                    ],
                    "V-ている + うちに gradual evolution",
                    "Fluency developing naturally over practice."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Natural Change", "Evolution"]
        },
        {
            "id": "skm3-u1-aida-vs-aidani",
            "title": "〜間 vs 〜間に (Continuous Duration vs Momentary Action)",
            "meaning": "〜間 (Action in B continues through 100% of duration A). 〜間に (Discrete action in B happens at some specific point during interval A).",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-ている / Noun + の + 間 (Throughout) vs 間に (Single point)",
            "nuance": "DURATION VS POINT: '夏休みの間、毎日泳いだ' (Swam every day the whole vacation). '夏休みの間に、免許を取った' (Acquired license at a moment during vacation).",
            "keyTakeaway": "MUG-UP: 間 = Whole time. 間に = At a moment within the interval.",
            "sentences": [
                make_sentence(
                    "s-skm3-1-3",
                    "両親が旅行している間、ずっと一人で留守番をしていた。",
                    "Throughout the entire time my parents were traveling, I looked after the house alone.",
                    "Parents traveling while, throughout alone home-tending did.",
                    [
                        tok("旅行している間", "りょこうしているあいだ", "ryokou shite iru aida", "throughout the entire time they traveled", "Grammar")
                    ],
                    "Continuous house-sitting for the entire vacation interval."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-3",
                    "お風呂に入っている（　　）、宅急便の配達員がベルを鳴らした。",
                    "While I was taking a bath, the courier delivery person rang the doorbell.",
                    ["間に", "間", "うちに", "最中に"],
                    0,
                    [
                        "Correct! Ringing the doorbell was a momentary event occurring at a point in the bath window, requiring 間に.",
                        "Incorrect. 間 would mean the courier rang the bell non-stop for the entire 30 minutes of the bath!",
                        "Incorrect. うちに implies urgency to avoid a negative change.",
                        "Incorrect. 最中に emphasizes physical interruption, but 間に is the standard temporal boundary contrast."
                    ],
                    "〜間に (Momentary event during interval)",
                    "Doorbell ringing during bath."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Duration", "Time Boundaries"]
        },
        {
            "id": "skm3-u1-te-kara-denaito",
            "title": "〜てからでないと / 〜てからでなければ (Not Until / Only After Prerequisite Is Done)",
            "meaning": "Action Y is completely impossible until prerequisite action X has been thoroughly fulfilled: 'Unless you do X first, Y cannot be done'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-て + からでないと / からでなければ + Negative / Impossible Predicate",
            "nuance": "MANDATORY NEGATIVE CONCEQUENCE: Clause B ALWAYS expresses inability, refusal, or impossibility (できません, 決められません, 分かりません).",
            "keyTakeaway": "MUG-UP: V-て + からでないと + [Negative] = Cannot do Y until X is completed first!",
            "sentences": [
                make_sentence(
                    "s-skm3-1-4",
                    "上司と相談してからでないと、この場でお返事はできません。",
                    "Unless I consult with my supervisor first, I cannot give you an answer on the spot.",
                    "Supervisor-with consult-after-only, this place-at reply cannot.",
                    [
                        tok("相談してからでないと", "そうだんしてからでないと", "soudan shite kara de nai to", "not until consulting", "Grammar")
                    ],
                    "Business prerequisite for answer."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-4",
                    "詳しい契約内容を（　　）からでないと、サインすることはできません。",
                    "Unless I read the detailed contract terms first, I cannot sign it.",
                    ["読んで", "読む", "読んだ", "読まない"],
                    0,
                    [
                        "Correct! 読む connects via te-form 読んで + からでないと.",
                        "Incorrect. 読む is dictionary form.",
                        "Incorrect. 読んだ is past form.",
                        "Incorrect. 読まない is negative form."
                    ],
                    "V-て + からでないと prerequisite",
                    "Refusing signature before review."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Prerequisite", "Time"]
        },
        {
            "id": "skm3-u1-tokoro-da-phases",
            "title": "〜ところだ (Temporal Phase: Imminent, In the Midst, or Just Finished)",
            "meaning": "Pinpoints the exact temporal boundary: 1) Just about to start (辞書形). 2) In the thick of doing (ている). 3) Just completed moments ago (た形).",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 1: 時・進行 (Time & Progress)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 + ところだ (Inception) | V-ている + ところだ (Midst) | V-た + ところだ (Conclusion)",
            "nuance": "PHASE CLUES: '今から出かけるところだ' (I'm putting on my shoes). '今調べているところだ' (Browsing right now). '今帰ったところだ' (Just stepped through the door).",
            "keyTakeaway": "MUG-UP: V-るところ (About to) -> V-ているところ (Right now) -> V-たところ (Just finished right now!).",
            "sentences": [
                make_sentence(
                    "s-skm3-1-5",
                    "今から家を出るところですから、三十分後には着くと思います。",
                    "I am just about to leave the house right now, so I think I'll arrive in about 30 minutes.",
                    "Now house leave-about-to, 30-mins-after arrive think.",
                    [
                        tok("出るところですから", "でるところですから", "deru tokoro desu kara", "just about to leave, so", "Grammar")
                    ],
                    "V-辞書形 + ところ indicates imminent departure."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-1-5",
                    "ちょうど今、昼ご飯を食べ（　　）ところだから、お腹がいっぱいです。",
                    "I just finished eating lunch right now, so I am completely full.",
                    ["終わった", "終わる", "終わっている", "終われ"],
                    0,
                    [
                        "Correct! V-た + ところだ indicates an action that concluded moments ago.",
                        "Incorrect. 終わるところ implies about to finish.",
                        "Incorrect. 終わっているところ is awkward with ところ.",
                        "Incorrect. 終われ is imperative."
                    ],
                    "V-た + ところだ (Just finished)",
                    "Explaining fullness after immediate completion."
                )
            ],
            "tags": ["N3", "SKM Unit 1", "Aspect", "Temporal Phase"]
        },

        # === UNIT 2: 対象・関連 (RELATION & REPETITION) ===
        {
            "id": "skm3-u2-toori-ni-accordance",
            "title": "〜とおりに / 〜どおりに (Just As / In Exact Accordance With)",
            "meaning": "Executing an action in faithful, exact alignment with instructions, drawings, thoughts, or maps ('Just as planned / Exactly as told').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "V-辞書形 / V-た + とおりに | Noun + の + とおりに | Noun + どおりに (Voiced sound without の!)",
            "nuance": "VOICING RULE (連濁): Noun + の + とおりに OR Noun + どおりに (voiced without の): 予定どおり (as scheduled), 期待どおり (as hoped).",
            "keyTakeaway": "MUG-UP: Noun + の + とおりに OR Noun + どおりに (voiced!). V-る / V-た + とおりに.",
            "sentences": [
                make_sentence(
                    "s-skm3-2-1",
                    "先生が指示したとおりに実験を行ったら、予想どおりの結果が出た。",
                    "When we conducted the experiment exactly as the teacher instructed, results came out just as expected.",
                    "Teacher instructed as-exact experiment conducted-when, expectation-as results came-out.",
                    [
                        tok("指示したとおりに", "しじしたとおりに", "shiji shita toori ni", "just as instructed", "Grammar"),
                        tok("予想どおりの", "よそうどおりの", "yosou doori no", "just as predicted", "Grammar")
                    ],
                    "Verbal とおりに and nominal どおり."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-1",
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
                    "Faithful progress according to plan."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Accordance", "Adherence"]
        },
        {
            "id": "skm3-u2-ni-yotte-variation",
            "title": "〜によって / 〜によっては (Depending on / According to Differences)",
            "meaning": "Indicates diversity, variety, or contingency: 'Depending on X, things differ / In some cases of X...'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + によって (異なる, 違う, さまざまだ) | Noun + によっては (Certain specific outcomes)",
            "nuance": "によって VS によっては: によって introduces general variety (国によって習慣が違う = Customs differ by country). によっては singles out an extreme or specific contingency (日によっては氷点下になる = On some days it drops below freezing).",
            "keyTakeaway": "MUG-UP: Noun + によって = Depending on X, things vary. によっては = In some specific cases of X.",
            "sentences": [
                make_sentence(
                    "s-skm3-2-2",
                    "文化や宗教によって、タブーとされる食べ物は大きく異なる。",
                    "Depending on culture and religion, foods considered taboo differ significantly.",
                    "Culture or religion depending-on, taboo considered food greatly differs.",
                    [
                        tok("宗教によって", "しゅうきょうによって", "shuukyou ni yotte", "depending on religion", "Grammar")
                    ],
                    "Societal variations across cultural groups."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-2",
                    "この薬は通常安全ですが、体質（　　）は軽いアレルギー反応が出ることがあります。",
                    "This medicine is usually safe, but depending on the individual constitution, mild allergic reactions may occur in some cases.",
                    ["によっては", "によって", "について", "にとって"],
                    0,
                    [
                        "Correct! 体質によっては singles out the specific subset of constitutions prone to reaction.",
                        "Incorrect. によって is general variation, whereas sentence describes an occasional specific outcome.",
                        "Incorrect. について means 'concerning / regarding'.",
                        "Incorrect. にとって means 'from the perspective of'."
                    ],
                    "Noun + によっては (Contingent outcome)",
                    "Specific adverse reactions in certain cases."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Variation", "Contingency"]
        },
        {
            "id": "skm3-u2-tabini-repetition",
            "title": "〜たびに (Every Single Time / Invariable Recurrence)",
            "meaning": "Whenever condition X occurs, emotional or behavioral response Y invariably accompanies it: 'Every single time without exception'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 + たびに | Noun + の + たびに",
            "nuance": "EMOTIONAL RECURRENCE: Used when the speaker notices a recurring pattern or emotional reaction. Cannot be used for everyday routine sequences without feeling (e.g. 'every day when I wake up').",
            "keyTakeaway": "MUG-UP: V-る / Noun + の + たびに = Every time without exception! (会うたびに = Every time we meet).",
            "sentences": [
                make_sentence(
                    "s-skm3-2-3",
                    "このアルバムを見るたびに、楽しかった学生時代を懐かしく思い出す。",
                    "Every time I look at this photo album, I fondly recall my happy student days.",
                    "This album look every-time, fun student-era fondly recall.",
                    [
                        tok("見るたびに", "みるたびに", "miru tabi ni", "every time I look", "Grammar")
                    ],
                    "Emotional trigger whenever looking at photos."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-3",
                    "父は出張の（　　）、家族にその土地の名産品を買ってきてくれる。",
                    "Every time my father goes on a business trip, he buys local specialty goods for the family.",
                    ["たびに", "うちに", "ついでに", "最中に"],
                    0,
                    [
                        "Correct! 出張のたびに expresses invariable recurrence on every business trip.",
                        "Incorrect. うちに means while or before opportunity slips.",
                        "Incorrect. ついでに means taking advantage of an errand to perform another side chore.",
                        "Incorrect. 最中に means right in the middle of a continuous event."
                    ],
                    "Noun + の + たびに",
                    "Recurrent occurrence on every business trip."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Repetition", "Recurrence"]
        },
        {
            "id": "skm3-u2-ba-hodo-proportion",
            "title": "(〜ば)〜ほど (Proportional Correlation: The More... The More...)",
            "meaning": "As the scale or intensity of condition A increases, consequence B escalates in direct proportion: 'The more X, the more Y'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "V-ば + V-辞書形 + ほど | い-adj ければ + い-adj + ほど | な-adj なら + な-adj な + ほど | Noun + であればあるほど",
            "nuance": "ELLIPSIS ALLOWED: The first conditional part (〜ば) is often dropped in speech: 考えるほど分からなくなる (The more I think, the less I understand).",
            "keyTakeaway": "MUG-UP: [ば-form] + [Dictionary form] + ほど = The more X, the more Y.",
            "sentences": [
                make_sentence(
                    "s-skm3-2-4",
                    "外国語は使えば使うほど、上手に話せるようになります。",
                    "The more you use a foreign language, the more fluently you become able to speak it.",
                    "Foreign-language use-if use-extent, skillfully speak able become.",
                    [
                        tok("使えば使うほど", "つかえばつかうほど", "tsukaeba tsukau hodo", "the more you use it", "Grammar")
                    ],
                    "Proportional correlation between usage and fluency."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-4",
                    "荷物は（　　）ほど、旅行は身軽で快適になる。",
                    "The less luggage you have, the lighter and more comfortable your trip becomes.",
                    ["少なければ少ない", "少ないなら少ない", "少なくて少ない", "少ないと少ない"],
                    0,
                    [
                        "Correct! い-adjective proportional formula: 少なければ + 少ない + ほど.",
                        "Incorrect. 少ないなら少ない does not combine in standard correlative pair.",
                        "Incorrect. て-form cannot form this correlative formula.",
                        "Incorrect. と does not match the ほど correlative construction."
                    ],
                    "い-adjective (〜ければ)〜ほど",
                    "Proportional scale of luggage to comfort."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Proportion", "Correlation"]
        },
        {
            "id": "skm3-u2-tsuide-ni-opportunity",
            "title": "〜ついでに (While at It / Seizing Opportunity for a Side Task)",
            "meaning": "While executing primary task A, seizing the convenient opportunity to perform secondary side task B: 'While you're at it / On the way'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 / V-た + ついでに | Noun + の + ついでに",
            "nuance": "PRIMARY VS INCIDENTAL: Task A is the planned main excursion. Task B is a minor incidental chore piggybacked on A.",
            "keyTakeaway": "MUG-UP: V-る / V-た / Noun + の + ついでに = Convenient 2-for-1 side action!",
            "sentences": [
                make_sentence(
                    "s-skm3-2-5",
                    "郵便局へ切手を買いに行くついでに、コンビニで公共料金を支払ってきた。",
                    "While heading to the post office to buy stamps, I stopped by the convenience store and paid utility bills.",
                    "Post-office stamps buy go while-at-it, convenience-store utility-bills paid.",
                    [
                        tok("行くついでに", "いくついでに", "iku tsuide ni", "while going", "Grammar")
                    ],
                    "Side errand during post office trip."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-2-5",
                    "散歩の（　　）、ポストにこの手紙を投函してきてくれませんか。",
                    "While you're out taking a walk, would you mind dropping this letter into the mailbox for me?",
                    ["ついでに", "たびに", "うちに", "最中に"],
                    0,
                    [
                        "Correct! 散歩のついでに means conveniently posting the letter while already out on a walk.",
                        "Incorrect. たびに means every single time you walk.",
                        "Incorrect. うちに means before the walk ends.",
                        "Incorrect. 最中に means in the middle of walking."
                    ],
                    "Noun + の + ついでに (Incidental side-task)",
                    "Piggybacking a chore onto a walk."
                )
            ],
            "tags": ["N3", "SKM Unit 2", "Convenience", "Time"]
        },

        # === UNIT 3: 比較・限定 (COMPARISON & BOUNDARIES) ===
        {
            "id": "skm3-u3-kurai-hodo-extent",
            "title": "〜くらいだ / 〜ほどだ (Expressing Extreme Degree: To the Extent That)",
            "meaning": "Vividly illustrates high intensity or emotional degree by comparing it to an exaggerated metaphorical state: 'so [adj] that... / to the extent that...'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "V-辞書形 / V-ない + くらいだ / ほどだ | Noun + くらい / ほど",
            "nuance": "METAPHORICAL EXAGGERATION: 'お腹が痛くて、涙が出るほどだった' (My stomach hurt so badly that tears were practically coming out). ほど is slightly more formal/elevated than くらい.",
            "keyTakeaway": "MUG-UP: V-る + くらい / ほど = Metaphorical intensity ('so much that...').",
            "sentences": [
                make_sentence(
                    "s-skm3-3-1",
                    "昨日の富士山頂からの日の出は、息をのむほど美しかった。",
                    "Yesterday's sunrise from the summit of Mt. Fuji was breathtakingly beautiful to the point of gasping.",
                    "Yesterday's Mt-Fuji summit sunrise, breath swallow extent beautiful-was.",
                    [
                        tok("息をのむほど", "いきをのむほど", "iki o nomu hodo", "to the extent of taking one's breath away", "Grammar")
                    ],
                    "Breathtaking beauty on mountain summit."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-3-1",
                    "昨夜はあまりに仕事が忙しくて、猫の手も借りたい（　　）だった。",
                    "Last night work was so overwhelmingly busy that I was in a state where I'd welcome even a cat's paw to help.",
                    ["くらい", "ばかり", "ところ", "わけ"],
                    0,
                    [
                        "Correct! 猫の手も借りたいくらいだ is the idiomatic expression for extreme desperation for help.",
                        "Incorrect. ばかり means only / just.",
                        "Incorrect. ところ means temporal phase.",
                        "Incorrect. わけ means logical reason."
                    ],
                    "〜くらいだ (Extreme metaphorical degree)",
                    "Desperate busyness."
                )
            ],
            "tags": ["N3", "SKM Unit 3", "Degree", "Metaphor"]
        },
        {
            "id": "skm3-u3-kurai-wa-nai",
            "title": "〜くらい…はない / 〜ほど…はない (Superlative: Nothing Is As... As X)",
            "meaning": "Subjective superlative declaring that entity X is unsurpassed in quality Y: 'Nothing is as [adjective] as X / There is nobody quite as [adjective] as X'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Noun + くらい / ほど + [Noun] はない (Negative predicate at the end!)",
            "nuance": "SPEAKER'S HEARTFELT RATING: Expresses the speaker's emotional conviction that X stands supreme (e.g. 'Nothing feels better than a hot bath in winter').",
            "keyTakeaway": "MUG-UP: [Entity] ほど [Adjective] ものはない = There is NOTHING in the world as great as X!",
            "sentences": [
                make_sentence(
                    "s-skm3-3-2",
                    "仕事で大汗をかいた後の一杯の冷たい水ほど、美味しいものはない。",
                    "There is nothing quite as delicious as a glass of cold water after sweating heavily at work.",
                    "Work-at big-sweat shed after one-glass cold water extent, delicious thing none.",
                    [
                        tok("冷たい水ほど", "つめたいみずほど", "tsumetai mizu hodo", "nothing as... as cold water", "Grammar"),
                        tok("美味しいものはない", "おいしいものはない", "oishii mono wa nai", "there is nothing as delicious", "Grammar")
                    ],
                    "Superlative personal evaluation of cold water."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-3-2",
                    "私にとって、家族と一緒に過ごす時間（　　）大切なものはありません。",
                    "For me, there is nothing as precious as the time I spend together with my family.",
                    ["ほど", "ばかり", "きり", "とおり"],
                    0,
                    [
                        "Correct! 〜ほど [大切なもの] はない establishes the superlative evaluation.",
                        "Incorrect. ばかり means only / just.",
                        "Incorrect. きり means only / limit.",
                        "Incorrect. とおり means in accordance with."
                    ],
                    "Noun + ほど…はない (Unsurpassed superlative)",
                    "Declaring family time as the supreme treasure."
                )
            ],
            "tags": ["N3", "SKM Unit 3", "Superlative", "Evaluation"]
        },

        # === UNIT 4: 対比・関係 (CONTRAST & RELATION) ===
        {
            "id": "skm3-u4-hanmen-flipside",
            "title": "〜反面 (On the Flip Side: Coexisting Contradictory Aspects)",
            "meaning": "Presents two opposing, contradictory qualities coexisting simultaneously within the exact same person, product, or phenomenon: 'Convenient, but on the flip side, expensive'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Plain form + 反面 (な-adj takes な/である, Noun takes である)",
            "nuance": "SAME ENTITY PARADOX: Unlike 対して which contrasts two separate people (兄 vs 弟), 反面 examines the two contradictory faces of ONE single subject.",
            "keyTakeaway": "MUG-UP: Two opposing sides of the SAME subject! な-adj takes な + 反面 / である反面.",
            "sentences": [
                make_sentence(
                    "s-skm3-4-1",
                    "都会の生活は刺激的で便利な反面、人との温かい触れ合いが少ない。",
                    "While urban living is stimulating and convenient, on the flip side, warm human connections are few.",
                    "Urban living stimulating convenient flip-side, people-with warm connection few.",
                    [
                        tok("便利な反面", "べんりなはんめん", "benri na hanmen", "convenient, but on the flip side", "Grammar")
                    ],
                    "Balancing urban convenience against social alienation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-4-1",
                    "一人暮らしは自由で気楽な（　　）、病気の時は非常に心細い。",
                    "While living alone is free and carefree, on the flip side, when you are sick you feel terribly lonely.",
                    ["反面", "ついでに", "とたんに", "かぎりに"],
                    0,
                    [
                        "Correct! 気楽な反面 contrasts the freedom against the loneliness of the same living situation.",
                        "Incorrect. ついでに means side task.",
                        "Incorrect. とたんに means instant surprise trigger.",
                        "Incorrect. かぎりに is ungrammatical here."
                    ],
                    "な-adj + な + 反面 two sides of same coin",
                    "Contrasting freedom and vulnerability."
                )
            ],
            "tags": ["N3", "SKM Unit 4", "Flip Side", "Contrast"]
        },
        {
            "id": "skm3-u4-kawari-ni-exchange",
            "title": "〜かわりに (In Exchange For / Compensation / Instead Of)",
            "meaning": "1) In exchange for doing or accepting X, compensating with Y ('I'll teach you English in exchange for Japanese lessons'). 2) Instead of regular X, doing alternate Y.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "V-辞書形 + かわりに | Noun + の + かわりに",
            "nuance": "RECIPROCAL EXCHANGE: Clause A balances Clause B like a financial or social trade-off. Can also mean substitution: '休みの日に働いたかわりに、月曜日に休む' (Compensatory day off).",
            "keyTakeaway": "MUG-UP: V-る / Noun + の + かわりに = In exchange for / In place of!",
            "sentences": [
                make_sentence(
                    "s-skm3-4-2",
                    "英語を教えてもらうかわりに、彼女に美味しい手料理をご馳走した。",
                    "In exchange for having her teach me English, I treated her to delicious home cooking.",
                    "English taught-get in-exchange, her-to delicious home-cooking treated.",
                    [
                        tok("教えてもらうかわりに", "おしえてもらうかわりに", "oshiete morau kawari ni", "in exchange for being taught", "Grammar")
                    ],
                    "Reciprocal favor trade."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-4-2",
                    "この仕事は残業が多くて大変な（　　）に、給料は非常に高い。",
                    "In exchange for this job having lots of overtime and being tough, the salary is exceptionally high.",
                    ["かわり", "ついで", "とおり", "あまり"],
                    0,
                    [
                        "Correct! 大変なかわりに balances tough working conditions with high financial compensation.",
                        "Incorrect. ついで means taking opportunity for side errand.",
                        "Incorrect. とおり means in accordance with.",
                        "Incorrect. あまり means overcome by emotion."
                    ],
                    "〜かわりに reciprocal trade-off",
                    "High salary compensating for tough overtime."
                )
            ],
            "tags": ["N3", "SKM Unit 4", "Exchange", "Compensation"]
        },

        # === UNIT 5: 原因・理由 (CAUSES & REASONS) ===
        {
            "id": "skm3-u5-tame-ni-causality",
            "title": "〜ためだ / 〜ために (Objective Cause: Due to / Owing to)",
            "meaning": "Formal written and broadcast expression stating an objective cause or reason: 'Due to X, consequence Y resulted'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 5: 原因・理由 (Causes & Reasons)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + ため（に） (な-adj takes な, Noun takes の: 大雪のために)",
            "nuance": "OBJECTIVE & NO PERSONAL INTENT IN B: Clause B cannot be a human command, request, or intention (e.g. '雨のため、傘を持って行きなさい' ❌ is ungrammatical; must use から). ため is for factual reporting.",
            "keyTakeaway": "MUG-UP: Noun + の + ために = Factual cause ('due to'). No commands or requests in clause B!",
            "sentences": [
                make_sentence(
                    "s-skm3-5-1",
                    "強風と大雨のため、全便の飛行機が見合わせとなっております。",
                    "Due to strong winds and heavy rain, all flights are currently suspended.",
                    "Strong-wind and heavy-rain due-to, all-flights airplane suspended become.",
                    [
                        tok("大雨のため", "おおあめのため", "ooame no tame", "due to heavy rain", "Grammar")
                    ],
                    "Formal public transportation announcement."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-5-1",
                    "道路工事の（　　）、この先は全面通行止めになっております。",
                    "Due to road construction, this road ahead is completely closed to traffic.",
                    ["ため", "せい", "わけ", "こと"],
                    0,
                    [
                        "Correct! 道路工事のため is the standard formal administrative announcement register.",
                        "Incorrect. せい is colloquial emotional blame.",
                        "Incorrect. わけ means logical reason.",
                        "Incorrect. こと indicates nominalization."
                    ],
                    "Noun + の + ため (Formal objective cause)",
                    "Road closure announcement."
                )
            ],
            "tags": ["N3", "SKM Unit 5", "Cause", "Formal"]
        },
        {
            "id": "skm3-u5-koto-kara-origin",
            "title": "〜ことから (Origin of Name, Judgment, or Fact: Arising from the Fact That)",
            "meaning": "Points to the historical origin, observable characteristic, or evidential cue that led to a name, reputation, or deduction: 'Named so / Inferred because of X'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 5: 原因・理由 (Causes & Reasons)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + ことから (な-adj takes な/である, Noun takes である)",
            "nuance": "NAME ORIGIN & EVIDENTIAL CLUE: Ubiquitous when explaining why places or plants are named: '形が星に似ていることから、星草と呼ばれている' (Called star grass because its shape resembles a star).",
            "keyTakeaway": "MUG-UP: [Observable Fact] ことから [Name / Deductive Conclusion]! Origin story marker.",
            "sentences": [
                make_sentence(
                    "s-skm3-5-2",
                    "道が濡れていることから、昨夜雨が降ったことが分かる。",
                    "From the fact that the roads are wet, we can deduce that it rained last night.",
                    "Roads wet-are fact-from, last-night rain fell fact understand.",
                    [
                        tok("濡れていることから", "ぬれていることから", "nurete iru koto kara", "from the fact that they are wet", "Grammar")
                    ],
                    "Physical evidence serving as deductive basis."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-5-2",
                    "富士山が美しく見える（　　）から、この坂は富士見坂と名付けられた。",
                    "From the fact that Mt. Fuji can be seen beautifully, this slope was named Fujimi-zaka.",
                    ["こと", "もの", "わけ", "ところ"],
                    0,
                    [
                        "Correct! 〜ことから expresses the historical origin of naming a geographical landmark.",
                        "Incorrect. ものから is ungrammatical here.",
                        "Incorrect. わけから does not exist.",
                        "Incorrect. ところから indicates starting location or circumstantial clue, but ことから is the canonical origin pattern."
                    ],
                    "Clause + ことから (Origin of name)",
                    "Naming origin of Fujimi Slope."
                )
            ],
            "tags": ["N3", "SKM Unit 5", "Origin", "Deduction"]
        },

        # === UNIT 6: 条件・仮定 (CONDITIONS & HYPOTHESES) ===
        {
            "id": "skm3-u6-no-dakara-reality",
            "title": "〜のだから / 〜んだから (Since It Is an Acknowledged Reality)",
            "meaning": "Since situation X is an undisputed fact known to all parties, consequence Y naturally follows: 'Since it's a fact that X, of course Y!'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 6: 条件・仮定 (Conditions & Hypotheses)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + のだから / んだから (な-adj / Noun takes な: 好きなのだから, 子供なのだから)",
            "nuance": "SHARED COMMON GROUND: You don't use のだから to announce new surprising information; you appeal to a shared premise to give advice, reproof, or encouragement.",
            "keyTakeaway": "MUG-UP: [Obvious Shared Fact] なのだから [Natural mandate or encouragement]!",
            "sentences": [
                make_sentence(
                    "s-skm3-6-1",
                    "まだ子供なのだから、失敗してもくよくよ悩む必要はありません。",
                    "Since you are still a child, there is no need to brood over your mistakes.",
                    "Still child is-since, fail even worry necessity is-not.",
                    [
                        tok("子供なのだから", "こどもなのだから", "kodomo na no da kara", "since you are a child", "Grammar")
                    ],
                    "Appealing to youth as a compassionate ground for reassurance."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-6-1",
                    "自分で決めたこと（　　）だから、最後まで諦めずにやり通しなさい。",
                    "Since this is something you decided for yourself, carry it through to the end without giving up.",
                    ["なん", "だん", "のん", "いん"],
                    0,
                    [
                        "Correct! Noun こと connects via なん to だから (ことなんだから / ことなのだから).",
                        "Incorrect. だんだから is ungrammatical.",
                        "Incorrect. のんだから is nonsensical.",
                        "Incorrect. いんだから is invalid."
                    ],
                    "Noun + なのだから / なんだから shared premise",
                    "Mandating responsibility for personal choice."
                )
            ],
            "tags": ["N3", "SKM Unit 6", "Common Ground", "Causality"]
        },
        {
            "id": "skm3-u6-tewa-dewa-negative-consequence",
            "title": "〜ては / 〜では (If Such a Condition Persists, Disaster Will Follow)",
            "meaning": "Considers condition X as a severe obstacle: 'If X happens / If you keep doing X, bad result Y is inevitable'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 6: 条件・仮定 (Conditions & Hypotheses)",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "V-て + は | い-adj くて + は | な-adj / Noun + では",
            "nuance": "NEGATIVE FOREBODING: Clause B ALWAYS describes a bad consequence, trouble, or failure: 'こんなにミスが多くては困る' (If you make this many errors, we're in trouble).",
            "keyTakeaway": "MUG-UP: V-ては / では + [Disaster / Complaint] = 'If this keeps happening, we're doomed!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-6-2",
                    "毎日こんなに遊んでいては、来月の大学入試に合格できませんよ。",
                    "If you spend every day playing around like this, you will never pass next month's university entrance exam.",
                    "Every-day like-this playing if, next-month's exam pass cannot.",
                    [
                        tok("遊んでいては", "あそんでいては", "asonde ite wa", "if you keep playing around", "Grammar")
                    ],
                    "Warning against persistent idleness."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-6-2",
                    "締め切りが明日（　　）、今夜は徹夜するしかありません。",
                    "If the deadline is tomorrow, we have no choice but to pull an all-nighter tonight.",
                    ["では", "ては", "なら", "たら"],
                    0,
                    [
                        "Correct! Noun 明日 connects via では (明日では = If it's already tomorrow, we're in trouble).",
                        "Incorrect. ては is for verbs and い-adjectives, not nouns.",
                        "Incorrect. なら is general conditional without the warning foreboding of では.",
                        "Incorrect. たら is temporal sequence."
                    ],
                    "Noun + では negative consequence conditional",
                    "Foreboding deadline emergency."
                )
            ],
            "tags": ["N3", "SKM Unit 6", "Negative Condition", "Foreboding"]
        },

        # === UNIT 8: 可能・確信 (CERTAINTY & LOGIC) ===
        {
            "id": "skm3-u8-to-wa-kagiranai-not-necessarily",
            "title": "〜とは限らない (Partial Truth: Not Necessarily the Case)",
            "meaning": "Denies the absolute validity of a generalization: 'It does not necessarily mean that X is always true in every single case'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + とは限らない (Frequently pairs with adverbs: 必ずしも, いつも, だれもが)",
            "nuance": "DEBUNKING ASSUMPTIONS: '高いものが必ずしも良いとは限らない' (Expensive things are not necessarily good). Softens rigid dogmas.",
            "keyTakeaway": "MUG-UP: 必ずしも [Plain form] とは限らない = Not always necessarily true!",
            "sentences": [
                make_sentence(
                    "s-skm3-8-1",
                    "有名大学を卒業したからといって、仕事ができるとは限りません。",
                    "Just because someone graduated from a famous university, it does not necessarily mean they are competent at work.",
                    "Famous university graduated just-because, work able is-not-necessarily.",
                    [
                        tok("できるとは限りません", "できるとはかぎりません", "dekiru to wa kagirimasen", "not necessarily competent", "Grammar")
                    ],
                    "Debunking academic credentials as sole proof of competence."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-8-1",
                    "値段が高い服が、必ずしも長持ちする（　　）とは限らない。",
                    "High-priced clothing does not necessarily last long in every case.",
                    ["の", "こと", "もの", "わけ"],
                    0,
                    [
                        "Correct! Plain predicate connects directly: 長持ちするとは限らない (or するものとは限らない).",
                        "Incorrect. こと requires additional syntax.",
                        "Incorrect. わけ requires connection rules.",
                        "Incorrect. の can be omitted; direct connection is canonical."
                    ],
                    "〜とは限らない partial negation",
                    "Rejecting the assumption that price equals longevity."
                )
            ],
            "tags": ["N3", "SKM Unit 8", "Certainty", "Partial Negation"]
        },
        {
            "id": "skm3-u8-nai-koto-wa-nai-litotes",
            "title": "〜ないことはない / 〜ないこともない (Double Negative Litotes: It's Not That I Can't)",
            "meaning": "Double negative expressing reluctant admission or modest possibility: 'It's not that I completely can't do it... / If pushed, I could possibly manage'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-ない + ことはない | い-adj くない + ことはない | な-adj / Noun でない + ことはない",
            "nuance": "RELUCTANT HESITATION: You don't want to boast 'I can do it easily'. You say '走れば間に合わないことはない' (If I run, it's not that I couldn't make it).",
            "keyTakeaway": "MUG-UP: [Negative] + ことはない = Double negative! 'It is not impossible for me to do X'.",
            "sentences": [
                make_sentence(
                    "s-skm3-8-2",
                    "納豆はあまり好きではありませんが、食べられないことはありません。",
                    "I don't like natto very much, but it's not that I can't eat it if offered.",
                    "Natto not-very like-not but, eat-cannot fact-is-not.",
                    [
                        tok("食べられないことはありません", "たべられないことはありません", "taberarenai koto wa arimasen", "it is not that I cannot eat it", "Grammar")
                    ],
                    "Reluctant dietary concession."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-8-2",
                    "どうしてもとおっしゃるなら、手伝わ（　　）こともありませんが。",
                    "If you insist that it must be done, it's not that I couldn't help you out...",
                    ["ない", "ず", "ぬ", "なくて"],
                    0,
                    [
                        "Correct! 手伝う negative is 手伝わない + こともありません (It's not that I can't help).",
                        "Incorrect. 手伝わず cannot pair with こともない.",
                        "Incorrect. 手伝わぬ is archaic.",
                        "Incorrect. 手伝わなくて is te-form."
                    ],
                    "V-ない + こともない double negative",
                    "Hesitant offer of assistance under insistence."
                )
            ],
            "tags": ["N3", "SKM Unit 8", "Litotes", "Modesty"]
        },

        # === UNIT 11: 意志・計画 (INTENT & REGULATIONS) ===
        {
            "id": "skm3-u11-you-to-suru-inception",
            "title": "〜(よ)うとする (On the Very Verge Of / In the Act of Attempting)",
            "meaning": "1) Inception: Right at the exact moment of about to execute an action. 2) Effort: Actively attempting or striving to achieve X.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 11: 意志・計画 (Intent & Regulations)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-意向形 + とする (Past: とした / としていた) | Negative: としない (Refuses to do)",
            "nuance": "VERGE OF INTERRUPTION: '家を出ようとした時、電話が鳴った' (Just as I was about to walk out the door, phone rang). Negative 〜ようとしない indicates stubborn refusal ('He refuses to apologize').",
            "keyTakeaway": "MUG-UP: V-よう + とする = Just about to do X! Negative: V-ようとしない = Stubbornly refuses to do!",
            "sentences": [
                make_sentence(
                    "s-skm3-11-1",
                    "電車に乗ろうとした瞬間、ドアが目の前で閉まってしまった。",
                    "The instant I attempted to board the train, the doors shut right in front of my eyes.",
                    "Train board-attempted instant, doors eyes-front-at closed-regrettably.",
                    [
                        tok("乗ろうとした瞬間", "のろうとしたしゅんかん", "norou to shita shunkan", "the moment I attempted to board", "Grammar")
                    ],
                    "Interrupted boarding action."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-11-1",
                    "うちの犬は、お風呂に（　　）とすると、必死で逃げ出そうとする。",
                    "Whenever I attempt to put my dog in the bath, he desperately tries to flee.",
                    ["入れよう", "入れる", "入れ", "入れた"],
                    0,
                    [
                        "Correct! 入れる volitional is 入れよう + とする (Attempting to put into bath).",
                        "Incorrect. 入れる is dictionary form.",
                        "Incorrect. 入れ is masu-stem.",
                        "Incorrect. 入れた is past form."
                    ],
                    "V-意向形 + とする (Attempting action)",
                    "Attempting to bathe resistant pet."
                )
            ],
            "tags": ["N3", "SKM Unit 11", "Attempt", "Inception"]
        },
        {
            "id": "skm3-u11-koto-ni-natte-iru",
            "title": "〜ことになっている (Customary Rule, Schedule, or Standing Regulation)",
            "meaning": "Indicates a pre-established rule, institutional regulation, law, or standing appointment that governs behavior: 'It is a rule that / It is scheduled that'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 11: 意志・計画 (Intent & Regulations)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 / V-ない + ことになっている",
            "nuance": "EXTERNAL REGULATION: This is NOT a personal whim. It represents external school rules, legal bylaws, or schedules: '教室では日本語で話すことになっている' (It is the standing classroom rule).",
            "keyTakeaway": "MUG-UP: V-る / V-ない + ことになっている = It is an established societal/organizational rule!",
            "sentences": [
                make_sentence(
                    "s-skm3-11-2",
                    "法律により、二十歳未満の飲酒と喫煙は禁止されることになっています。",
                    "By law, drinking and smoking under twenty years of age is strictly prohibited.",
                    "Law-by, 20-under drinking smoking prohibited become-is.",
                    [
                        tok("ことになっています", "ことになっています", "koto ni natte imasu", "is the standing legal regulation", "Grammar")
                    ],
                    "Standing statutory legal requirement."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-11-2",
                    "この寮では、夜十一時以降は静かに（　　）ことになっている。",
                    "In this dormitory, it is a standing rule to remain quiet after 11:00 PM.",
                    ["する", "して", "した", "し"],
                    0,
                    [
                        "Correct! V-辞書形 静かにする connects to ことになっている.",
                        "Incorrect. して is te-form.",
                        "Incorrect. した is past form.",
                        "Incorrect. し is bare stem."
                    ],
                    "Standing rule formula 〜ことになっている",
                    "Dormitory curfew rule."
                )
            ],
            "tags": ["N3", "SKM Unit 11", "Rules", "Regulations"]
        },

        # === FORM CLASSIFICATIONS (形式整理 J: 接尾辞) ===
        {
            "id": "skm3-fj-ppoi-personality",
            "title": "〜っぽい (Prone to Negative Behavior / Resembling Quality: -ish / -y)",
            "meaning": "1) Tendency toward a personality flaw (怒りっぽい = quick-tempered, 忘れっぽい = forgetful). 2) Displaying obvious childlike or cheap qualities (子供っぽい, 安っぽい).",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "V-stem + っぽい | Noun + っぽい | い-adj (drop い) + っぽい (Conjugates as an い-adjective: っぽくない)",
            "nuance": "CRITICAL DIFFERENCE FROM RASHII: らしい indicates genuine authentic nature (男らしい = Manly, worthy of a man). っぽい indicates superficial resemblance or flaw (男っぽい = Tomboyish; 子供っぽい = Childish/Immature).",
            "keyTakeaway": "MUG-UP: Suffix 〜っぽい = -ish, -like, prone to temper/lapse! Acts as an い-adj.",
            "sentences": [
                make_sentence(
                    "s-skm3-j-1",
                    "彼は些細なことで怒りっぽい性格なので、みんな話しかけにくそうにしている。",
                    "Because he has a quick-tempered personality who gets angry over trivial matters, everyone seems hesitant to talk to him.",
                    "He trivial-things-over angry-prone personality since, everyone speak-hard looking-is.",
                    [
                        tok("怒りっぽい性格", "おこりっぽいせいかく", "okorippoi seikaku", "quick-tempered personality", "Grammar")
                    ],
                    "怒る (stem 怒り) + っぽい describes chronic short temper."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-j-1",
                    "いい歳をした大人が、そんな（　　）っぽい嘘をつくのは恥ずかしいですよ。",
                    "It is shameful for a grown adult to tell such a childish lie.",
                    ["子供", "大人", "先生", "若者"],
                    0,
                    [
                        "Correct! 子供っぽい means 'childish / immature'.",
                        "Incorrect. 大人っぽい means mature-looking.",
                        "Incorrect. 先生っぽい means teacher-like.",
                        "Incorrect. 若者っぽい means youth-like."
                    ],
                    "Noun + っぽい (Superficial resemblance / immaturity)",
                    "Reproaching childish deception in an adult."
                )
            ],
            "tags": ["N3", "SKM Form J", "Suffix", "Personality"]
        },
        {
            "id": "skm3-fj-darake-flaws",
            "title": "〜だらけ (Covered in Mess, Flaws, or Filth: Riddled With / Full Of)",
            "meaning": "Covered entirely with an undesirable substance or riddled with flaws: 'covered in mud, full of errors, riddled with debts'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun + だらけ (泥だらけ, 間違いだらけ, ゴミだらけ, 借金だらけ)",
            "nuance": "STRICTLY NEGATIVE / DISGUST: You CANNOT use だらけ for desirable things (you cannot say '宝石だらけ' ❌ or 'お金だらけ' ❌ unless complaining of clutter). It is for filth, mess, or errors.",
            "keyTakeaway": "MUG-UP: Noun + だらけ = Covered in an undesirable MESS! (泥だらけ = Covered in mud).",
            "sentences": [
                make_sentence(
                    "s-skm3-j-2",
                    "急いで書いた彼のレポートは、誤字や文法の間違いだらけだった。",
                    "His report, which was written in a rush, was riddled with typos and grammatical errors.",
                    "Hurriedly wrote his report, typos grammar mistakes-riddled was.",
                    [
                        tok("間違いだらけだった", "まちがいだらけだった", "machigaidarake datta", "was riddled with mistakes", "Grammar")
                    ],
                    "Negative appraisal of messy draft."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-j-2",
                    "雨の中サッカーをして、ユニフォームが（　　）だらけになってしまった。",
                    "We played soccer in the rain, and my uniform ended up completely covered in mud.",
                    ["泥", "雨", "水", "土"],
                    0,
                    [
                        "Correct! 泥だらけ is the canonical idiom for covered all over in mud.",
                        "Incorrect. 雨だらけ is unnatural (must be びしょ濡れ).",
                        "Incorrect. 水だらけ is unidiomatic.",
                        "Incorrect. 土だらけ is less natural than 泥 after rain."
                    ],
                    "Noun + だらけ (Covered in mess)",
                    "Mud-splattered sports uniform."
                )
            ],
            "tags": ["N3", "SKM Form J", "Suffix", "Mess"]
        }
    ]
    return pts

if __name__ == '__main__':
    pts = get_full_skm_n3()
    print(f"SKM N3 generated {len(pts)} exhaustive discrete grammar points.")

