import json

def get_genki2_l17_to_l23():
    exercises = []

    # ==================== LESSON 17 ====================
    exercises.extend([
        {
            "id": "g2-l17-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Reporting weather forecast hearsay: 'I heard that it will snow tomorrow'.",
            "question": "天気予報によると、明日は雪が降る（　　）。",
            "translation": "According to the weather forecast, I heard it will snow tomorrow.",
            "options": ["そうです", "らしいです", "ようです", "はずです"],
            "correctIndex": 0,
            "grammarPointId": "g2-l17-hearsay-sou-desu",
            "grammarPointTitle": "〜そうです (Hearsay / Quoting Reports: I Heard That / Reportedly)",
            "explanation": {
                "overall": "Hearsay 〜そうです attaches to short plain forms (降る + そうです). Paired with source marker によると.",
                "options": [
                    {"text": "そうです", "isCorrect": True, "reason": "Correct. Hearsay reporting: Short form + そうです.", "trapCategory": "formation"},
                    {"text": "らしいです", "isCorrect": False, "reason": "Incorrect. らしい denotes typical quality or indirect inference.", "trapCategory": "meaning"},
                    {"text": "ようです", "isCorrect": False, "reason": "Incorrect. ようです denotes sensory inference.", "trapCategory": "meaning"},
                    {"text": "はずです", "isCorrect": False, "reason": "Incorrect. はずです denotes logical expectation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern is standard for reporting hearsay based on an external source like a forecast?"
        },
        {
            "id": "g2-l17-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Hearsay formation with な-adjectives: I heard the town is quiet.",
            "question": "あの町はとても静か（　　）そうです。",
            "translation": "I hear that that town is very quiet.",
            "options": ["だ", "な", "（接続語なし）", "で"],
            "correctIndex": 0,
            "grammarPointId": "g2-l17-hearsay-sou-desu",
            "grammarPointTitle": "〜そうです (Hearsay / Quoting Reports: I Heard That / Reportedly)",
            "explanation": {
                "overall": "Crucial distinction: Hearsay 〜そうです requires the short copula だ for な-adjectives and nouns (静かだそうです), whereas appearance drops it (静かそうです).",
                "options": [
                    {"text": "だ", "isCorrect": True, "reason": "Correct. Hearsay requires copula だ: 静かだそうです.", "trapCategory": "formation"},
                    {"text": "な", "isCorrect": False, "reason": "Incorrect. な is pre-noun modifier.", "trapCategory": "formation"},
                    {"text": "（接続語なし）", "isCorrect": False, "reason": "Incorrect. Dropping だ results in appearance ('looks quiet'), not hearsay ('I hear it is quiet').", "trapCategory": "meaning"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で is te-form.", "trapCategory": "formation"}
                ]
            },
            "hint": "Do な-adjectives keep or drop だ before hearsay 〜そうです?"
        },
        {
            "id": "g2-l17-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Temporal conditional 〜たら: 'When I arrive at the station, I will contact you'.",
            "question": "駅に着い（　　）、連絡します。",
            "translation": "When I arrive at the station, I will contact you.",
            "options": ["たら", "れば", "と", "なら"],
            "correctIndex": 0,
            "grammarPointId": "g2-l17-tara-conditional",
            "grammarPointTitle": "〜たら (Specific & Temporal Conditional: If / When / Once Done)",
            "explanation": {
                "overall": "〜たら expresses temporal condition ('once action 1 occurs, will do action 2'). Can freely be followed by requests, plans, or future promises.",
                "options": [
                    {"text": "たら", "isCorrect": True, "reason": "Correct. Temporal sequence: V-ta + ら (着いたら).", "trapCategory": "formation"},
                    {"text": "れば", "isCorrect": False, "reason": "Incorrect. 〜ば denotes general hypothetical, not specific future time point.", "trapCategory": "meaning"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. と cannot be followed by volitional promises or requests.", "trapCategory": "formation"},
                    {"text": "なら", "isCorrect": False, "reason": "Incorrect. なら denotes contextual limitation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which conditional particle indicates 'when / once done' for a specific future occurrence?"
        },
        {
            "id": "g2-l17-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Stating lack of obligation: 'You do not have to come tomorrow if you are busy'.",
            "question": "忙しかったら、明日来（　　）もいいですよ。",
            "translation": "If you are busy, you do not have to come tomorrow.",
            "options": ["なくて", "ないで", "ない", "ず"],
            "correctIndex": 0,
            "grammarPointId": "g2-l17-nakute-mo-ii",
            "grammarPointTitle": "〜なくてもいいです (Lack of Obligation: You Do Not Have To)",
            "explanation": {
                "overall": "The pattern for lack of obligation ('do not have to') is: Verb nai-stem + くてもいいです (来なくてもいいです).",
                "options": [
                    {"text": "なくて", "isCorrect": True, "reason": "Correct. Lack of obligation: 〜なくてもいいです.", "trapCategory": "formation"},
                    {"text": "ないで", "isCorrect": False, "reason": "Incorrect. 〜ないでもいい is colloquial non-standard in textbook grammar.", "trapCategory": "formation"},
                    {"text": "ない", "isCorrect": False, "reason": "Incorrect. Missing -kute te-form.", "trapCategory": "formation"},
                    {"text": "ず", "isCorrect": False, "reason": "Incorrect. Archaic.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the grammatical formula for 'you don't have to [do]'?"
        },
        {
            "id": "g2-l17-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Casual conversation. Passing along rumor or hearsay with 〜って.",
            "question": "けんさん、来月結婚する（　　）。",
            "translation": "I hear Ken is getting married next month! (Casual hearsay)",
            "options": ["って", "と", "し", "よ"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-17-28",
            "grammarPointTitle": "〜って・みたいです",
            "explanation": {
                "overall": "〜って is the casual spoken equivalent of そうだ / と言っていた for quoting hearsay.",
                "options": [
                    {"text": "って", "isCorrect": True, "reason": "Correct. Casual spoken hearsay: 〜って.", "trapCategory": "context"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. Quotative と cannot terminate a sentence without a verb in standard speech.", "trapCategory": "formation"},
                    {"text": "し", "isCorrect": False, "reason": "Incorrect. し lists reasons.", "trapCategory": "meaning"},
                    {"text": "よ", "isCorrect": False, "reason": "Incorrect. よ conveys new fact, lacking hearsay quotation nuance.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which casual ending is used by friends to pass along hearsay ('I heard that...')?"
        },
        {
            "id": "g2-l17-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Resemblance / similarity: Ken speaks Japanese like a native speaker.",
            "question": "けんさんは日本人の（　　）日本語を話します。",
            "translation": "Ken speaks Japanese like a native Japanese person.",
            "options": ["ように", "ような", "みたい", "そうに"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-17-28",
            "grammarPointTitle": "〜って・みたいです",
            "explanation": {
                "overall": "When modifying a verb adverbially with a simile, use: Noun + のように (日本人のように話します).",
                "options": [
                    {"text": "ように", "isCorrect": True, "reason": "Correct. Adverbial simile modifying verb: Noun + のように + Verb.", "trapCategory": "formation"},
                    {"text": "ような", "isCorrect": False, "reason": "Incorrect. ような modifies nouns, not verbs.", "trapCategory": "formation"},
                    {"text": "みたい", "isCorrect": False, "reason": "Incorrect. みたい requires に before verbs (みたいに話します).", "trapCategory": "formation"},
                    {"text": "そうに", "isCorrect": False, "reason": "Incorrect. そうに is manner from appearance.", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do you form an adverbial simile modifying a verb ('speaks like a...')?"
        },
        {
            "id": "g2-l17-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Chronological order with 〜前に: brushing teeth before going to sleep.",
            "question": "寝る（　　）、歯を磨きます。",
            "translation": "Before going to bed, I brush my teeth.",
            "options": ["前に", "たら", "てから", "間に"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-17-29",
            "grammarPointTitle": "〜前に・〜てから",
            "explanation": {
                "overall": "The pattern for 'before doing X' is: Verb dictionary form + 前に (寝る前に).",
                "options": [
                    {"text": "前に", "isCorrect": True, "reason": "Correct. Formula: V-dict + 前に (寝る前に).", "trapCategory": "formation"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. たら means 'after/when'.", "trapCategory": "meaning"},
                    {"text": "てから", "isCorrect": False, "reason": "Incorrect. てから means 'after doing', opposite chronological order.", "trapCategory": "meaning"},
                    {"text": "間に", "isCorrect": False, "reason": "Incorrect. 間に means 'while'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses 'before doing [action]'?"
        },
        {
            "id": "g2-l17-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Chronological order with 〜てから: doing an action after another is complete.",
            "question": "宿題を（　　）から、ゲームをしました。",
            "translation": "After doing my homework, I played video games.",
            "options": ["して", "した", "する", "しないで"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-17-29",
            "grammarPointTitle": "〜前に・〜てから",
            "explanation": {
                "overall": "The pattern for 'after doing X' is: Verb te-form + から (してから). (V-dict + から means 'because').",
                "options": [
                    {"text": "して", "isCorrect": True, "reason": "Correct. Formula for 'after doing': V-te + から (してから).", "trapCategory": "formation"},
                    {"text": "した", "isCorrect": False, "reason": "Incorrect. したから means 'because I did', not chronological 'after'.", "trapCategory": "meaning"},
                    {"text": "する", "isCorrect": False, "reason": "Incorrect. するから means 'because I will do'.", "trapCategory": "meaning"},
                    {"text": "しないで", "isCorrect": False, "reason": "Incorrect. Without doing.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What verb form attaches to から to mean 'after doing [action]'?"
        },
        {
            "id": "g2-l17-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Unexpected discovery in past tense with 〜たら: opened the window and discovered it was snowing.",
            "question": "朝、窓を開け（　　）、雪が降っていました。",
            "translation": "When I opened the window in the morning, (I discovered that) it was snowing.",
            "options": ["たら", "と", "ば", "なら"],
            "correctIndex": 0,
            "grammarPointId": "g2-l17-tara-conditional",
            "grammarPointTitle": "〜たら (Specific & Temporal Conditional: If / When / Once Done)",
            "explanation": {
                "overall": "〜たら paired with past main clause denotes accidental discovery ('when I did X, I found that Y had happened').",
                "options": [
                    {"text": "たら", "isCorrect": True, "reason": "Correct. Discovery conditional: V-ta + ら + past observation.", "trapCategory": "context"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. While と can also express discovery, standard Genki II conditional instruction focuses on 〜たら for personal sequential discoveries.", "trapCategory": "context"},
                    {"text": "ば", "isCorrect": False, "reason": "Incorrect. 〜ば cannot express past factual occurrences.", "trapCategory": "formation"},
                    {"text": "なら", "isCorrect": False, "reason": "Incorrect. なら is topical/contextual limitation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which conditional ending is used when doing an action leads to an unexpected discovery?"
        },
        {
            "id": "g2-l17-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 17",
            "type": "multiple-choice",
            "context": "Attaching hearsay 〜そうです to い-adjectives: I heard the exam was difficult.",
            "question": "昨日の試験は（　　）そうです。",
            "translation": "I heard that yesterday's exam was difficult.",
            "options": ["難しかった", "難しく", "難しいだった", "難しかっただ"],
            "correctIndex": 0,
            "grammarPointId": "g2-l17-hearsay-sou-desu",
            "grammarPointTitle": "〜そうです (Hearsay / Quoting Reports: I Heard That / Reportedly)",
            "explanation": {
                "overall": "Hearsay 〜そうです attaches to the plain short past form of い-adjectives directly (難しかった + そうです).",
                "options": [
                    {"text": "難しかった", "isCorrect": True, "reason": "Correct. Past short form of い-adjective: 難しかった + そうです.", "trapCategory": "formation"},
                    {"text": "難しく", "isCorrect": False, "reason": "Incorrect. Adverbial form.", "trapCategory": "formation"},
                    {"text": "難しいだった", "isCorrect": False, "reason": "Incorrect. い-adjectives never take だった.", "trapCategory": "formation"},
                    {"text": "難しかっただ", "isCorrect": False, "reason": "Incorrect. Redundant copula だ.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the past short form of 難しい that attaches to hearsay そうです?"
        }
    ])

    # ==================== LESSON 18 ====================
    exercises.extend([
        {
            "id": "g2-l18-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Intransitive verb describing natural state: the door is open right now.",
            "question": "風でドアが（　　）。",
            "translation": "The door is open from the wind.",
            "options": ["開いています", "開けています", "開きました", "開けました"],
            "correctIndex": 0,
            "grammarPointId": "g2-l18-transitive-intransitive",
            "grammarPointTitle": "自動詞 vs 他動詞 (Intransitive vs Transitive Verb Pairs)",
            "explanation": {
                "overall": "開く (あく) is intransitive, taking subject marker が to describe an open state (ドアが開いています). 開ける (あける) is transitive, taking object marker を.",
                "options": [
                    {"text": "開いています", "isCorrect": True, "reason": "Correct. Intransitive verb state: ドアが開いています.", "trapCategory": "formation"},
                    {"text": "開けています", "isCorrect": False, "reason": "Incorrect. Transitive 開ける requires someone actively opening something (ドアを開けている).", "trapCategory": "meaning"},
                    {"text": "開きました", "isCorrect": False, "reason": "Incorrect. Simple past punctually describes the moment it opened, not current state.", "trapCategory": "meaning"},
                    {"text": "開けました", "isCorrect": False, "reason": "Incorrect. Transitive past.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which verb of the pair 開く / 開ける is the intransitive verb describing the state of the door?"
        },
        {
            "id": "g2-l18-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Transitive verb action: Ken turned off the classroom lights.",
            "question": "けんさんは教室の電気（　　）消しました。",
            "translation": "Ken turned off the classroom lights.",
            "options": ["を", "が", "に", "で"],
            "correctIndex": 0,
            "grammarPointId": "g2-l18-transitive-intransitive",
            "grammarPointTitle": "自動詞 vs 他動詞 (Intransitive vs Transitive Verb Pairs)",
            "explanation": {
                "overall": "消す (けす) is the transitive verb meaning 'to turn off / extinguish', taking direct object を. (消える is intransitive: 電気が消える).",
                "options": [
                    {"text": "を", "isCorrect": True, "reason": "Correct. Direct object of transitive verb 消す takes を.", "trapCategory": "formation"},
                    {"text": "が", "isCorrect": False, "reason": "Incorrect. が is for intransitive pair (電気が消えました).", "trapCategory": "formation"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に does not mark direct object.", "trapCategory": "meaning"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で does not mark direct object.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the direct object of the transitive verb 消す?"
        },
        {
            "id": "g2-l18-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Natural consequence conditional 〜と: when spring comes, cherry blossoms bloom.",
            "question": "春になる（　　）、桜が咲きます。",
            "translation": "Whenever spring comes, cherry blossoms bloom.",
            "options": ["と", "たら", "ば", "なら"],
            "correctIndex": 0,
            "grammarPointId": "g2-l18-to-natural-consequence",
            "grammarPointTitle": "〜と (Natural Consequence & Inevitable Conditional: When / If)",
            "explanation": {
                "overall": "The conditional 〜と expresses inevitable natural consequences, physical laws, or routine mechanical results (Whenever A occurs, B naturally happens).",
                "options": [
                    {"text": "と", "isCorrect": True, "reason": "Correct. Natural consequence conditional: V-dict + と.", "trapCategory": "meaning"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. While possible, と is the textbook prototype for inevitable natural phenomena.", "trapCategory": "context"},
                    {"text": "ば", "isCorrect": False, "reason": "Incorrect. Less prototypical for seasonal inevitability.", "trapCategory": "context"},
                    {"text": "なら", "isCorrect": False, "reason": "Incorrect. Contextual limitation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which conditional particle denotes inevitable natural consequence ('whenever X, Y inevitably happens')?"
        },
        {
            "id": "g2-l18-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Grammatical restriction of 〜と: the second clause CANNOT contain a request or command.",
            "question": "交差点を右に曲がる（　　）、郵便局がありますよ。",
            "translation": "If you turn right at the intersection, there is a post office.",
            "options": ["と", "なら", "て", "のに"],
            "correctIndex": 0,
            "grammarPointId": "g2-l18-to-natural-consequence",
            "grammarPointTitle": "〜と (Natural Consequence & Inevitable Conditional: When / If)",
            "explanation": {
                "overall": "Giving street directions uses 〜と because following the direction automatically reveals the destination landmark (曲がると、あります).",
                "options": [
                    {"text": "と", "isCorrect": True, "reason": "Correct. Direction-giving pattern: V-dict + と + あります.", "trapCategory": "context"},
                    {"text": "なら", "isCorrect": False, "reason": "Incorrect. Contextual limitation is unnatural here.", "trapCategory": "meaning"},
                    {"text": "て", "isCorrect": False, "reason": "Incorrect. Missing conditional linker.", "trapCategory": "formation"},
                    {"text": "のに", "isCorrect": False, "reason": "Incorrect. のに indicates frustrated contradiction.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which conditional is standard for giving navigational street directions?"
        },
        {
            "id": "g2-l18-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Retrospective regret: failing an exam and wishing you had studied more.",
            "question": "もっと勉強すれ（　　）よかったです。",
            "translation": "I should have studied more.",
            "options": ["ば", "たら", "と", "なら"],
            "correctIndex": 0,
            "grammarPointId": "g2-l18-ba-yokatta",
            "grammarPointTitle": "〜ばよかった (Retrospective Regret: I Should Have Done)",
            "explanation": {
                "overall": "The formula for expressing regret over something you did not do is: Verb conditional ba-form + よかった (〜ばよかった).",
                "options": [
                    {"text": "ば", "isCorrect": True, "reason": "Correct. Regret formula: V-ba + よかった (すればよかった).", "trapCategory": "formation"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. Standard Genki II textbook pattern for retrospective regret is 〜ばよかった.", "trapCategory": "formation"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "なら", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What conditional form is used in the retrospective regret pattern 'I should have done...'?"
        },
        {
            "id": "g2-l18-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Negative regret: wishing you hadn't bought such an expensive watch.",
            "question": "あんな高い時計、買わ（　　）よかったです。",
            "translation": "I shouldn't have bought such an expensive watch.",
            "options": ["なければ", "ないで", "なくて", "ず"],
            "correctIndex": 0,
            "grammarPointId": "g2-l18-ba-yokatta",
            "grammarPointTitle": "〜ばよかった (Retrospective Regret: I Should Have Done)",
            "explanation": {
                "overall": "Negative regret ('I shouldn't have done') is: Verb nai-stem + なければよかった (買わなければよかった).",
                "options": [
                    {"text": "なければ", "isCorrect": True, "reason": "Correct. Negative regret formula: 〜なければよかった.", "trapCategory": "formation"},
                    {"text": "ないで", "isCorrect": False, "reason": "Incorrect. Cannot combine with よかった.", "trapCategory": "formation"},
                    {"text": "なくて", "isCorrect": False, "reason": "Incorrect. 〜なくてよかった means 'I am glad I didn't do it' (relief, not regret!).", "trapCategory": "meaning"},
                    {"text": "ず", "isCorrect": False, "reason": "Incorrect. Archaic.", "trapCategory": "formation"}
                ]
            },
            "hint": "Be careful: 〜なくてよかった is relief, but which pattern expresses REGRET ('I shouldn't have')?"
        },
        {
            "id": "g2-l18-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Accidental action with regret: dropped smartphone and broke the screen.",
            "question": "スマホを落として、画面を割っ（　　）ました。",
            "translation": "I dropped my smartphone and ended up breaking the screen.",
            "options": ["てしまい", "ておき", "てみ", "てあり"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-18-30",
            "grammarPointTitle": "〜てしまう",
            "explanation": {
                "overall": "〜てしまう denotes completing an action with a feeling of regret, mishap, or lack of control.",
                "options": [
                    {"text": "てしまい", "isCorrect": True, "reason": "Correct. Regretful mishap aspect: 〜てしまう / 〜てしまいました.", "trapCategory": "meaning"},
                    {"text": "ておき", "isCorrect": False, "reason": "Incorrect. Preparation in advance.", "trapCategory": "meaning"},
                    {"text": "てみ", "isCorrect": False, "reason": "Incorrect. Trial action.", "trapCategory": "meaning"},
                    {"text": "てあり", "isCorrect": False, "reason": "Incorrect. Deliberate preparation state.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which auxiliary verb expresses an unfortunate or accidental mishap with regret?"
        },
        {
            "id": "g2-l18-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Exhaustive completion: finished reading the entire thick novel in a single afternoon.",
            "question": "面白かったので、一日で全部読ん（　　）ました。",
            "translation": "Because it was interesting, I read the whole thing completely in one day.",
            "options": ["でしまい", "でおき", "でみ", "でい"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-18-30",
            "grammarPointTitle": "〜てしまう",
            "explanation": {
                "overall": "The second major use of 〜てしまう is exhaustive completion: carrying an action out to the very end.",
                "options": [
                    {"text": "でしまい", "isCorrect": True, "reason": "Correct. Exhaustive completion: 読んでしまいました.", "trapCategory": "meaning"},
                    {"text": "でおき", "isCorrect": False, "reason": "Incorrect. Action in advance.", "trapCategory": "meaning"},
                    {"text": "でみ", "isCorrect": False, "reason": "Incorrect. Trial action.", "trapCategory": "meaning"},
                    {"text": "でい", "isCorrect": False, "reason": "Incorrect. Progressive.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which auxiliary verb indicates completing an action thoroughly to the very end?"
        },
        {
            "id": "g2-l18-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Simultaneous actions: listening to music while walking.",
            "question": "音楽を（　　）ながら、散歩します。",
            "translation": "I take walks while listening to music.",
            "options": ["聞き", "聞く", "聞いて", "聞いた"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-18-31",
            "grammarPointTitle": "〜ながら",
            "explanation": {
                "overall": "The simultaneous action construction is: Verb-stem + ながら (聞く -> 聞き + ながら). The main action is the second verb (散歩する).",
                "options": [
                    {"text": "聞き", "isCorrect": True, "reason": "Correct. Verb stem + ながら: 聞きながら.", "trapCategory": "formation"},
                    {"text": "聞く", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach ながら directly.", "trapCategory": "formation"},
                    {"text": "聞いて", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach ながら.", "trapCategory": "formation"},
                    {"text": "聞いた", "isCorrect": False, "reason": "Incorrect. Past form cannot attach ながら.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of the verb attaches to ながら to express simultaneous action?"
        },
        {
            "id": "g2-l18-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 18",
            "type": "multiple-choice",
            "context": "Losing an item: wallet fell from pocket (intransitive event).",
            "question": "ポケットから財布が（　　）ました。",
            "translation": "My wallet fell / dropped from my pocket.",
            "options": ["落ち", "落とし", "落として", "落ちてい"],
            "correctIndex": 0,
            "grammarPointId": "g2-l18-transitive-intransitive",
            "grammarPointTitle": "自動詞 vs 他動詞 (Intransitive vs Transitive Verb Pairs)",
            "explanation": {
                "overall": "落ちる (おちる) is intransitive ('to fall / drop'), taking subject marker が. 落とす (おとす) is transitive ('to drop something', taking を).",
                "options": [
                    {"text": "落ち", "isCorrect": True, "reason": "Correct. Intransitive verb: 財布が落ちました.", "trapCategory": "formation"},
                    {"text": "落とし", "isCorrect": False, "reason": "Incorrect. Transitive 落とす requires subject to act on an object with を (財布を落としました).", "trapCategory": "formation"},
                    {"text": "落として", "isCorrect": False, "reason": "Incorrect. Incomplete te-form.", "trapCategory": "formation"},
                    {"text": "落ちてい", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which verb is the intransitive partner of 落とす that pairs with particle が?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_genki2_l17_to_l23()
    print(f"Generated {len(ex_list)} exercises across Genki II Lessons 17 and 18.")
