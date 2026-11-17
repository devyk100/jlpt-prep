# -*- coding: utf-8 -*-
"""
Genki II (3rd Edition) - Complete Canonical N4 Grammar Syllabus (Lessons 13 to 23)
Fully annotated with lexical tokens, literal glosses, nuance notes, and 4-way quiz explanations.
"""
from data_genki1 import tok, make_sentence, make_quiz

def get_genki2_points():
    pts = [
        # 1. Lesson 13: 可能形 (Potential Verbs)
        {
            "id": "gp-genki2-kanoukei",
            "title": "可能形 (Potential Verbs: Ability & Possibility)",
            "meaning": "Expresses that an agent has the capacity to perform an action or that external conditions permit it.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 13: Looking for a Part-time Job",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Ru-verbs: 食べる→食べられる | U-verbs: 書く→書ける, 飲む→飲める | Irregular: する→できる, くる→こられる",
            "nuance": "PARTICLE FLIP TRAP: When a transitive verb converts to potential form, the direct object particle を frequently shifts to が (日本語を話す → 日本語が話せる).",
            "keyTakeaway": "MUG-UP: U-verbs: change final -u to -e + る (行く→行ける). Object particle を usually flips to が!",
            "sentences": [
                make_sentence(
                    "s-g2-13-1",
                    "漢字が難しくて、新聞をすらすら読むことができません（読めません）。",
                    "The kanji are difficult, so I cannot read the newspaper smoothly.",
                    "Kanji difficult-being, newspaper smoothly read cannot.",
                    [
                        tok("漢字", "かんじ", "kanji", "kanji", "Noun"),
                        tok("新聞を", "しんぶんを", "shinbun o", "newspaper", "Noun+Particle"),
                        tok("読めません", "よめません", "yomemasen", "cannot read (potential neg)", "Grammar")
                    ],
                    "飲む/読む (U-verbs) conjugate to 飲める/読める."
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
                        "Incorrect. 食べません is a simple will decision ('I will not eat'), not ability.",
                        "Incorrect. 食べさせません is causative ('I will not let someone eat').",
                        "Incorrect. 食べてもらえません means cannot get someone to eat."
                    ],
                    "可能形 potential negative",
                    "Eating raw fish is impossible due to personal inability (食べられない)."
                )
            ],
            "tags": ["N4", "Genki L13", "Potential", "Ability"]
        },

        # 2. Lesson 13: 〜し (Listing Reasons)
        {
            "id": "gp-genki2-shi",
            "title": "〜し、〜し (Listing Multiple Parallel Reasons)",
            "meaning": "Lists two or more complementary reasons leading up to an overall conclusion or feeling ('Not only... but also...').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 13: Looking for a Part-time Job",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + し (Noun/な-adj non-past affirmative takes だ: 綺麗だし, 休みだし)",
            "nuance": "Unlike から, which offers a single direct explanation, 〜し accumulates multiple contributing factors, often implying 'and besides other things too'.",
            "keyTakeaway": "MUG-UP: Connects to plain forms. Remember: Noun / な-adj non-past takes だ + し (親切だし).",
            "sentences": [
                make_sentence(
                    "s-g2-13-2",
                    "物価も安いし、治安もいいし、この街に住んでよかったです。",
                    "Prices are cheap and public safety is great, so I am really glad I live in this town.",
                    "Prices-also cheap-and, safety-also good-and, this town-in living glad-was.",
                    [
                        tok("物価も安いし", "ぶっかもやすいし", "bukka mo yasui shi", "prices are cheap and", "Grammar"),
                        tok("治安もいいし", "ちあんもいいし", "chian mo ii shi", "safety is good and", "Grammar"),
                        tok("住んでよかったです", "すんでよかったです", "sunde yokatta desu", "glad I live here", "Grammar")
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

        # 3. Lesson 13: 〜そうです (Appearance / It looks like)
        {
            "id": "gp-genki2-sou-conjecture",
            "title": "〜そうです (Visual Conjecture: Looks Like / On the Verge Of)",
            "meaning": "Expresses an impression based on visual appearance: 'It looks [adj]' or an action looks imminent: 'It looks like it's about to [verb]'.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 13: Looking for a Part-time Job",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Verb-stem + そうだ | い-adj (drop い) + そうだ | な-adj stem + そうだ",
            "nuance": "IRREGULARITY ALERT: いい (good) becomes よさそう (NOT いそう ❌)! ない (negative) becomes なさそう (NOT なそう ❌)!",
            "keyTakeaway": "MUG-UP: Stem + そうだ. Drop final い! Exceptions: いい→よさそう, ない→なさそう.",
            "sentences": [
                make_sentence(
                    "s-g2-13-3",
                    "空が暗くなってきましたね。今にも雨が降りそうです。",
                    "The sky has grown dark, hasn't it? It looks like it is about to rain any second.",
                    "Sky dark become-came. Even-now rain fall-looks-like.",
                    [
                        tok("今にも", "いまにも", "ima ni mo", "at any moment", "Adverb"),
                        tok("雨が降りそうです", "あめがふりそうです", "ame ga furisou desu", "looks like it will rain", "Grammar")
                    ],
                    "降る (masu-stem 降り) + そうです indicates imminent precipitation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-13-3",
                    "このケーキは見た目も綺麗で、とても（　　）ですね。",
                    "This cake looks beautiful, and it looks very delicious, doesn't it?",
                    ["おいしそう", "おいしいそう", "おいしいだそう", "おいしくそう"],
                    0,
                    [
                        "Correct! おいしい drops its final い to connect to そう (おいしそう).",
                        "Incorrect. おいしいそう (retaining い) turns it into HEARSAY ('I heard it is delicious')!",
                        "Incorrect. おいしいだそう is ungrammatical.",
                        "Incorrect. おいしくそう is ungrammatical."
                    ],
                    "Visual conjecture 〜そうです with い-adjective",
                    "Dropping final い for appearance."
                )
            ],
            "tags": ["N4", "Genki L13", "Conjecture", "Appearance"]
        },

        # 4. Lesson 14: あげる / くれる / もらう (Giving & Receiving Objects)
        {
            "id": "gp-genki2-giving-receiving-items",
            "title": "あげる・くれる・もらう (Giving & Receiving Material Goods)",
            "meaning": "Defines social vector of transactions: あげる (Giver gives outward), くれる (Inward giver gives TO ME/my in-group), もらう (Receiver receives from someone).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 14: Valentine's Day",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "[Giver] が [Receiver] に [Item] を あげる / くれる | [Receiver] が [Giver] に/から [Item] を もらう",
            "nuance": "THE KURERU BOUNDARY: You can NEVER say '私が友達にくれた' ❌! くれる ALWAYS means someone gave to ME or my in-group (友達が私にくれた).",
            "keyTakeaway": "MUG-UP: くれる = Gives to ME. あげる = I give to others. もらう = I receive from someone.",
            "sentences": [
                make_sentence(
                    "s-g2-14-1",
                    "誕生日に母が新しい財布をくれました。私は大切に使っています。",
                    "My mother gave me a new wallet for my birthday. I am using it with great care.",
                    "Birthday-on mother new wallet gave-me. I carefully using-am.",
                    [
                        tok("母が", "ははが", "haha ga", "my mother", "Noun"),
                        tok("財布をくれました", "さいふをくれました", "saifu o kuremashita", "gave me a wallet", "Grammar")
                    ],
                    "Mother gave TO ME, so くれました is mandatory."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-14-1",
                    "去年のクリスマスに、兄が私に素敵な時計を（　　）。",
                    "Last Christmas, my older brother gave me a wonderful watch.",
                    ["くれました", "あげました", "もらいました", "やりました"],
                    0,
                    [
                        "Correct! The direction is from older brother to ME (私に), requiring くれました.",
                        "Incorrect. あげました implies I gave to someone else, or a third person gave outward.",
                        "Incorrect. もらいました requires the subject to be the receiver (私が兄にもらいました).",
                        "Incorrect. やりました is only for pets, plants, or juniors in crude register."
                    ],
                    "くれる for inbound giving to speaker",
                    "Subject gives to the speaker."
                )
            ],
            "tags": ["N4", "Genki L14", "Giving and Receiving", "Transactions"]
        },

        # 5. Lesson 15: 〜ておく (Preparatory Action in Advance)
        {
            "id": "gp-genki2-te-oku",
            "title": "〜ておく / 〜とく (Doing in Advance / Preparatory Action)",
            "meaning": "Performing an action in advance to prepare for future convenience or leaving a state as is for later.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 15: A Trip to Nagano",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-て + おく (Casual spoken contraction: 〜ておく → 〜とく / 〜でおく → 〜どく)",
            "nuance": "Forward-looking mindset: 'I'll buy tickets beforehand so we don't wait in line' (切符を買っておく). In casual speech, 買っておく becomes 買っとく.",
            "keyTakeaway": "MUG-UP: V-て + おく = Action done in advance for future convenience. Contracted: 〜とく.",
            "sentences": [
                make_sentence(
                    "s-g2-15-1",
                    "パーティーの前に、部屋を綺麗に掃除しておきます。",
                    "Before the party, I will clean up the room nicely in advance.",
                    "Party's before, room cleanly clean-up in-advance.",
                    [
                        tok("掃除しておきます", "そうじしておきます", "souji shite okimasu", "will clean in advance", "Grammar")
                    ],
                    "Preparatory action executed specifically for the upcoming party."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-15-1",
                    "明日から旅行なので、ホテルの予約を（　　）おきました。",
                    "Since I'm traveling from tomorrow, I made hotel reservations in advance.",
                    ["して", "する", "した", "し"],
                    0,
                    [
                        "Correct! する becomes して, forming しておきました ('reserved in advance').",
                        "Incorrect. Dictionary form cannot connect to おく.",
                        "Incorrect. Past form cannot connect to おく.",
                        "Incorrect. Masu-stem cannot connect to おく."
                    ],
                    "〜ておく te-form connection",
                    "Connecting to te-form for preparatory action."
                )
            ],
            "tags": ["N4", "Genki L15", "Advance Action", "Preparation"]
        },

        # 6. Lesson 16: 〜てあげる / 〜てくれる / 〜てもらう (Giving & Receiving Favors)
        {
            "id": "gp-genki2-te-favors",
            "title": "〜てあげる・〜てくれる・〜てもらう (Benefactive Transactions / Favors)",
            "meaning": "Indicates doing or receiving actions as psychological favors: 〜てあげる (do favor for other), 〜てくれる (someone does favor for me), 〜てもらう (get someone to do favor).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 16: Lost and Found",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "V-て + あげる / くれる / もらう",
            "nuance": "PATRONIZING TRAP: Saying '〜てあげましょうか' to superiors sounds condescending ('Shall I do you a favor?'). Use '〜ましょうか' or humble 'お〜いたしましょうか' instead.",
            "keyTakeaway": "MUG-UP: てくれる = They did it for ME. てもらう = I got them to do it. Caution: てあげる can sound patronizing!",
            "sentences": [
                make_sentence(
                    "s-g2-16-1",
                    "道に迷っていたら、親切な人が駅まで案内してくれました。",
                    "When I was lost, a kind person guided me all the way to the station.",
                    "Way lost-when, kind person station-to guided gave-me.",
                    [
                        tok("案内してくれました", "あんないしてくれました", "annai shite kuremashita", "kindly guided me", "Grammar")
                    ],
                    "Third party performed the favor for the benefit of the speaker."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-16-1",
                    "重い荷物を持っていたら、友達が（　　）くれました。",
                    "When I was carrying heavy luggage, my friend kindly carried it for me.",
                    ["持って", "持つ", "持ち", "持った"],
                    0,
                    [
                        "Correct! 持つ connects via te-form 持って + くれました.",
                        "Incorrect. Dictionary form cannot connect to くれる.",
                        "Incorrect. Masu-stem cannot connect to くれる.",
                        "Incorrect. Past form cannot connect to くれる."
                    ],
                    "〜てくれる benefactive favor",
                    "Forming the favor construction."
                )
            ],
            "tags": ["N4", "Genki L16", "Favors", "Benefactive"]
        },

        # 7. Lesson 18: 〜てしまう (Completion vs Regret)
        {
            "id": "gp-genki2-te-shimau",
            "title": "〜てしまう / 〜ちゃう (Irreversible Completion & Spoken Regret)",
            "meaning": "1) Completed entirely to the end. 2) Regrettable, irreversible mishap ('Oh no, I accidentally did it!'). Spoken: 〜ちゃう / 〜じゃう.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 18: John's Part-Time Job",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "V-て + しまう (Spoken: てしまう→ちゃう, でしまう→じゃう)",
            "nuance": "Emotional resonance: Saying '宿題を忘れました' is neutral. Saying '宿題を忘れてしまいました / 忘れちゃった' admits fault and expresses distress.",
            "keyTakeaway": "MUG-UP: V-て + しまう = 100% finished OR oops, I messed up! Spoken: 忘れてしまう → 忘れちゃう.",
            "sentences": [
                make_sentence(
                    "s-g2-18-1",
                    "大事な書類を電車の網棚に忘れてしまいました。",
                    "I accidentally left an important document behind on the train luggage rack.",
                    "Important document train's luggage-rack-on forgetting-ended-up.",
                    [
                        tok("忘れてしまいました", "わすれてしまいました", "wasurete shimaimashita", "ended up forgetting (regret)", "Grammar")
                    ],
                    "Expresses distressing, irreversible carelessness."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-18-1",
                    "お気に入りのコップを落として（　　）壊してしまいました。",
                    "I dropped my favorite glass and ended up breaking it.",
                    ["割って", "割る", "割れ", "割り"],
                    0,
                    [
                        "Correct! Te-form 割って connects into the sequence leading to regretful damage.",
                        "Incorrect. Dictionary form cannot link actions here.",
                        "Incorrect. Potential stem cannot link here.",
                        "Incorrect. Masu-stem is too literary for this sentence."
                    ],
                    "Sequence with regretful outcome",
                    "Connecting actions leading into 〜てしまう."
                )
            ],
            "tags": ["N4", "Genki L18", "Regret", "Completion"]
        },

        # 8. Lesson 18: 〜ながら (Simultaneous Concurrent Actions)
        {
            "id": "gp-genki2-nagara",
            "title": "〜ながら (Simultaneous Concurrent Actions by the Same Subject)",
            "meaning": "Two actions performed at the exact same time by the same person: Action 1 while doing Action 2 (Action 2 is the main verb).",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 18: John's Part-Time Job",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-stem (ます形 without ます) + ながら + Main Verb",
            "nuance": "SAME AGENT CONSTRAINT: Both actions MUST be performed by the exact same human agent! You cannot say '雨が降りながら私が走る' ❌. Furthermore, the second verb is the primary focus.",
            "keyTakeaway": "MUG-UP: V-stem + ながら. The main focus is ALWAYS on the second verb at the end!",
            "sentences": [
                make_sentence(
                    "s-g2-18-2",
                    "毎朝好きな音楽を聴きながら、公園をジョギングしています。",
                    "Every morning, while listening to my favorite music, I jog in the park.",
                    "Every-morning favorite music listening-while, park jogging-am.",
                    [
                        tok("聴きながら", "ききながら", "kikinagara", "while listening", "Grammar"),
                        tok("ジョギングしています", "ジョギングしています", "jogingu shite imasu", "am jogging (primary action)", "Verb")
                    ],
                    "聴く (stem 聴き) + ながら. Main action is jogging."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-18-2",
                    "テレビを（　　）ながらご飯を食べるのは、行儀がよくありません。",
                    "Eating meals while watching television is bad manners.",
                    ["見", "見て", "見る", "見な"],
                    0,
                    [
                        "Correct! 見る masu-stem is 見 (見ます), which connects to ながら (見ながら).",
                        "Incorrect. 見て is te-form, which cannot connect to ながら.",
                        "Incorrect. 見る is dictionary form, which cannot connect to ながら.",
                        "Incorrect. 見な is ungrammatical."
                    ],
                    "〜ながら masu-stem connection",
                    "Attaching the simultaneous marker to the verb stem."
                )
            ],
            "tags": ["N4", "Genki L18", "Simultaneous", "Time"]
        },

        # 9. Lesson 20: 謙譲語 (Humble Forms)
        {
            "id": "gp-genki2-kenjougo",
            "title": "謙譲語 (Humble Speech: Lowering One's In-Group Actions)",
            "meaning": "Lowers the actions of the speaker or speaker's in-group to show deep respect and courtesy toward the listener or receiver of the action.",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 20: Mary Goes Shopping",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "お + V-stem + する / いたす | Special verbs: 参る (行く/来る), 申す (言う), 拝見する (見る), 存じる (知る/思う)",
            "nuance": "SPEAKER ACTIONS ONLY: You can NEVER use kenjougo for your customer or boss! Saying '社長がお荷物をお持ちしました' ❌ is a catastrophic business faux pas. You lower YOURSELF.",
            "keyTakeaway": "MUG-UP: Kenjougo (謙譲語) is for ME and MY in-group to lower ourselves before superiors.",
            "sentences": [
                make_sentence(
                    "s-g2-20-1",
                    "明日、午後三時に御社へ伺います。",
                    "I will humbly visit your esteemed company tomorrow at 3 PM.",
                    "Tomorrow, 3-PM-at your-company humble-visit.",
                    [
                        tok("御社へ", "おんしゃへ", "onsha e", "to your esteemed company", "Noun+Particle"),
                        tok("伺います", "うかがいます", "ukagaimasu", "will humbly visit / ask (kenjougo)", "Verb")
                    ],
                    "伺う replaces 行く/訪問する to humble speaker's movement."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-20-1",
                    "重そうな荷物ですね。私が（　　）。",
                    "That looks like heavy luggage. Allow me to carry it for you.",
                    ["お持ちします", "お持ちになります", "持たれます", "お持ちください"],
                    0,
                    [
                        "Correct! お + stem 持ち + します is the humble formula for the speaker's offer.",
                        "Incorrect. お持ちになります is honorific (尊敬語) for the OTHER person's actions.",
                        "Incorrect. 持たれます is honorific passive.",
                        "Incorrect. お持ちください is an instruction telling the other person to carry it."
                    ],
                    "Humble formula お〜する",
                    "Selecting the correct humble pattern for speaker action."
                )
            ],
            "tags": ["N4", "Genki L20", "Keigo", "Humble"]
        },

        # 10. Lesson 21: 受身形 (Passive Voice)
        {
            "id": "gp-genki2-ukemi",
            "title": "受身形 (Passive Voice: Direct vs Suffering/Indirect Passive)",
            "meaning": "Action is received from another agent: Direct passive (I was praised) vs Suffering/Indirect passive (adversity inflicted on subject: 'I had my wallet stolen').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 21: Which Style of House?",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "Ru-verbs: drop る + られる | U-verbs: change final -u to -a + れる (書く→書かれる) | する→される, くる→こられる",
            "nuance": "THE SUFFERING PASSIVE (迷惑受身): Japanese uniquely uses intransitive verbs in passive to express suffering or inconvenience: 雨に降られた (I got rained on), 赤ちゃんに泣かれた (I was troubled by baby crying).",
            "keyTakeaway": "MUG-UP: U-verbs: a + れる. In passive, the person inflicting the action is marked with に!",
            "sentences": [
                make_sentence(
                    "s-g2-21-1",
                    "満員電車の中で、見知らぬ人に足を踏まれました。",
                    "On the crowded train, my foot was stepped on by a stranger.",
                    "Crowded-train inside, stranger-by foot stepped-was (adversity).",
                    [
                        tok("見知らぬ人に", "みしらぬひとに", "mishiranu hito ni", "by an unknown stranger", "Noun+Particle"),
                        tok("踏まれました", "ふまれました", "fumaremashita", "was stepped on (passive)", "Grammar")
                    ],
                    "踏む (U-verb) becomes 踏まれる. Expresses victim's pain."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-21-1",
                    "テストで満点を取って、先生に（　　）。",
                    "I got a perfect score on the test and was praised by my teacher.",
                    ["ほめられました", "ほめさせました", "ほめてあげました", "ほめさせられました"],
                    0,
                    [
                        "Correct! ほめる (Ru-verb) passive is ほめられる (ほめられました).",
                        "Incorrect. ほめさせました is causative ('made someone praise').",
                        "Incorrect. ほめてあげました means I praised the teacher.",
                        "Incorrect. ほめさせられました is causative-passive ('was forced to praise')."
                    ],
                    "Passive form ほめられる",
                    "Receiving praise from an external agent (先生に)."
                )
            ],
            "tags": ["N4", "Genki L21", "Passive", "Ukemi"]
        },

        # 11. Lesson 22: 使役形 (Causative Voice)
        {
            "id": "gp-genki2-shieki",
            "title": "使役形 (Causative Voice: Make or Let Someone Do)",
            "meaning": "Causing someone to perform an action: Coercive ('make someone do') or Permissive ('let/allow someone do').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 22: Education in Japan",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "Ru-verbs: drop る + させる | U-verbs: change final -u to -a + せる (書く→書かせる) | する→させる, くる→こさせる",
            "nuance": "PARTICLE OF THE DOER: If the main action is intransitive (run, go), the doer takes を (子供を走らせる). If the main verb has its own object with を (eat vegetables), the doer takes に (子供に野菜を食べさせる) to avoid double を!",
            "keyTakeaway": "MUG-UP: Ru-verbs = させる. U-verbs = a + せる. Doer marked with に when verb has an object.",
            "sentences": [
                make_sentence(
                    "s-g2-22-1",
                    "両親は私に好きな習い事をさせてくれました。",
                    "My parents kindly let me take the hobby lessons that I liked.",
                    "Parents topic me-to favorite lessons do-caused kindly-gave.",
                    [
                        tok("させてくれました", "させてくれました", "sasete kuremashita", "kindly let me do (permissive causative + favor)", "Grammar")
                    ],
                    "Causative + てくれる creates permissive gratitude ('let me do')."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-22-1",
                    "母は弟に部屋の片付けを（　　）。",
                    "My mother made my younger brother tidy up his room.",
                    ["させました", "されました", "させられました", "してもらいました"],
                    0,
                    [
                        "Correct! する causative is させる (させました), indicating making someone clean.",
                        "Incorrect. されました is passive ('mother was cleaned').",
                        "Incorrect. させられました is causative-passive ('mother was forced').",
                        "Incorrect. してもらいました expresses gratitude, whereas sentence describes parental direction."
                    ],
                    "Causative form of する (させる)",
                    "Directing another person to complete a chore."
                )
            ],
            "tags": ["N4", "Genki L22", "Causative", "Shieki"]
        },

        # 12. Lesson 23: 使役受身形 (Causative-Passive Voice)
        {
            "id": "gp-genki2-shieki-ukemi",
            "title": "使役受身形 (Causative-Passive: Made/Forced to Do Against One's Will)",
            "meaning": "Subject was pressured, forced, or reluctantly compelled to do an action against their will ('I was made to do...').",
            "level": "N4",
            "book": "Genki II",
            "chapter": "Lesson 23: Good-bye",
            "streamId": "stream-social",
            "streamName": "Social Hierarchy, Benefaction & Modesty",
            "connection": "Ru-verbs: させられる (食べさせられる) | U-verbs: される (待たされる, 飲まされる) [Except す: 話させられる] | する→させられる, くる→こさせられる",
            "nuance": "THE U-VERB SHORTCUT: For most U-verbs (except ending in す), the long -せられる contracts naturally to -される: 待つ → 待たせる → 待たされる (NOT 待たせられる).",
            "keyTakeaway": "MUG-UP: Causative-Passive = Was made to do it against my will! U-verbs shortcut: a + される (飲まされた).",
            "sentences": [
                make_sentence(
                    "s-g2-23-1",
                    "子供の頃、嫌いなピーマンを無理やり食べさせられました。",
                    "When I was a child, I was forced against my will to eat green peppers that I hated.",
                    "Child's time, hated bell-pepper forcibly eat-caused-was.",
                    [
                        tok("食べさせられました", "たべさせられました", "tabesaseraremashita", "was forced to eat (causative-passive)", "Grammar")
                    ],
                    "Reluctant compliance under parental compulsion."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g2-23-1",
                    "カラオケでみんなの前で歌を（　　）、とても恥ずかしかったです。",
                    "I was forced to sing a song in front of everyone at karaoke, and it was very embarrassing.",
                    ["歌わされた", "歌わせた", "歌われた", "歌ってくれた"],
                    0,
                    [
                        "Correct! 歌う (U-verb) contracts to 歌わされる / 歌わされた ('was made to sing').",
                        "Incorrect. 歌わせた is active causative ('I made someone else sing').",
                        "Incorrect. 歌われた is simple passive ('was sung').",
                        "Incorrect. 歌ってくれた means someone kindly sang for me."
                    ],
                    "Causative-passive U-verb contraction",
                    "Reluctantly singing under social pressure."
                )
            ],
            "tags": ["N4", "Genki L23", "Causative-Passive", "Voice"]
        }
    ]
    return pts

if __name__ == '__main__':
    points = get_genki2_points()
    print(f"Genki II generated {len(points)} grammar points.")

