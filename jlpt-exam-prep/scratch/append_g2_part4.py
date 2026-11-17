import json

def get_genki2_l21_to_l23():
    exercises = []

    # ==================== LESSON 21 ====================
    exercises.extend([
        {
            "id": "g2-l21-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Deliberate preparation state with transitive verb: schedule is written on the calendar.",
            "question": "カレンダーに来週の予定が（　　）。",
            "translation": "The schedule for next week is written on the calendar (deliberately prepared).",
            "options": ["書いてあります", "書いています", "書きました", "書かれます"],
            "correctIndex": 0,
            "grammarPointId": "g2-l21-te-aru",
            "grammarPointTitle": "〜てある (Transitive Verb Resultant State: Deliberately Prepared)",
            "explanation": {
                "overall": "〜てある attaches to transitive verbs to express a state that has been deliberately brought about by someone for a future purpose (予定が書いてあります).",
                "options": [
                    {"text": "書いてあります", "isCorrect": True, "reason": "Correct. Deliberate preparation state: Transitive V-te + あります.", "trapCategory": "formation"},
                    {"text": "書いています", "isCorrect": False, "reason": "Incorrect. 書いている is progressive action ('is writing'), which requires a human subject.", "trapCategory": "meaning"},
                    {"text": "書きました", "isCorrect": False, "reason": "Incorrect. Simple past punctually describes the past writing action.", "trapCategory": "meaning"},
                    {"text": "書かれます", "isCorrect": False, "reason": "Incorrect. Passive/honorific non-past.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which pattern combines a transitive verb with あります to show that an action was done in preparation?"
        },
        {
            "id": "g2-l21-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Contrast between 〜ている (natural intransitive state) and 〜てある (deliberate transitive state): the window has been deliberately kept open for ventilation.",
            "question": "空気を入れ替えるために、窓が（　　）。",
            "translation": "In order to air out the room, the window has been deliberately kept open.",
            "options": ["開けてあります", "開いています", "開けました", "開きました"],
            "correctIndex": 0,
            "grammarPointId": "g2-l21-te-aru",
            "grammarPointTitle": "〜てある (Transitive Verb Resultant State: Deliberately Prepared)",
            "explanation": {
                "overall": "Because an intentional human purpose is stated (空気を入れ替えるために), the deliberate transitive state pattern 開けてあります is required, rather than the neutral intransitive 開いています.",
                "options": [
                    {"text": "開けてあります", "isCorrect": True, "reason": "Correct. Deliberate transitive state: 開けてあります.", "trapCategory": "meaning"},
                    {"text": "開いています", "isCorrect": False, "reason": "Incorrect. 開いている is neutral spontaneous state without reference to human intent.", "trapCategory": "context"},
                    {"text": "開けました", "isCorrect": False, "reason": "Incorrect. Punctual past action.", "trapCategory": "meaning"},
                    {"text": "開きました", "isCorrect": False, "reason": "Incorrect. Intransitive past action.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which form emphasizes that the window was deliberately left open for a specific purpose?"
        },
        {
            "id": "g2-l21-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Action occurring at a single point inside a time window: a delivery arrived while I was sleeping.",
            "question": "私が寝ている（　　）、荷物が届きました。",
            "translation": "While I was asleep, a package arrived.",
            "options": ["間に", "間", "時で", "前に"],
            "correctIndex": 0,
            "grammarPointId": "g2-l21-aida-vs-aidani",
            "grammarPointTitle": "〜間に vs 〜間 (During a Moment vs Throughout the Entire Duration)",
            "explanation": {
                "overall": "〜間に marks a momentary or punctual event (荷物が届く) occurring at some point WITHIN a continuous temporal frame (寝ている).",
                "options": [
                    {"text": "間に", "isCorrect": True, "reason": "Correct. Punctual action within a time window: 〜間に.", "trapCategory": "meaning"},
                    {"text": "間", "isCorrect": False, "reason": "Incorrect. 〜間 without に requires the second action to continue throughout the ENTIRE duration.", "trapCategory": "meaning"},
                    {"text": "時で", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "前に", "isCorrect": False, "reason": "Incorrect. Before, not during.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Do you use 〜間 or 〜間に when an event happens at a single instant during a period?"
        },
        {
            "id": "g2-l21-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Continuous action lasting throughout the entire duration: read a book continuously the whole time while waiting for the train.",
            "question": "電車を待っている（　　）、ずっと本を読んでいました。",
            "translation": "While waiting for the train, I was reading a book the entire time.",
            "options": ["間", "間に", "時で", "ながらに"],
            "correctIndex": 0,
            "grammarPointId": "g2-l21-aida-vs-aidani",
            "grammarPointTitle": "〜間に vs 〜間 (During a Moment vs Throughout the Entire Duration)",
            "explanation": {
                "overall": "〜間 (without に) denotes that the activity in the main clause lasts continuously from beginning to end across the entire duration (emphasized by ずっと).",
                "options": [
                    {"text": "間", "isCorrect": True, "reason": "Correct. Continuous action throughout entire period: 〜間 (paired with ずっと).", "trapCategory": "meaning"},
                    {"text": "間に", "isCorrect": False, "reason": "Incorrect. 間に denotes a momentary action, clashing with continuous ずっと.", "trapCategory": "meaning"},
                    {"text": "時で", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "ながらに", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which one expresses that an activity occurred continuously throughout the ENTIRE duration?"
        },
        {
            "id": "g2-l21-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Direct passive voice: I was praised by the teacher. Ru-verb 褒める.",
            "question": "私は先生に（　　）。",
            "translation": "I was praised by my teacher.",
            "options": ["褒められました", "褒めました", "褒まられました", "褒めさせました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-21-38",
            "grammarPointTitle": "受身",
            "explanation": {
                "overall": "Ru-verb passive formation: drop -ru and add -rareru (褒める -> 褒められる / 褒められました).",
                "options": [
                    {"text": "褒められました", "isCorrect": True, "reason": "Correct. Ru-verb passive: drop -ru + られました.", "trapCategory": "formation"},
                    {"text": "褒めました", "isCorrect": False, "reason": "Incorrect. Active voice ('I praised the teacher').", "trapCategory": "meaning"},
                    {"text": "褒まられました", "isCorrect": False, "reason": "Incorrect. U-verb passive overgeneralization.", "trapCategory": "formation"},
                    {"text": "褒めさせました", "isCorrect": False, "reason": "Incorrect. Causative ('I made the teacher praise').", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the passive form of the Ru-verb 褒める?"
        },
        {
            "id": "g2-l21-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Direct passive voice: had my foot stepped on by someone on the crowded train. U-verb 踏む.",
            "question": "満員電車で、知らない人に足を（　　）。",
            "translation": "On the crowded train, my foot was stepped on by a stranger.",
            "options": ["踏まれました", "踏みました", "踏みられました", "踏まさせました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-21-38",
            "grammarPointTitle": "受身",
            "explanation": {
                "overall": "U-verb passive formation: change final -u to -a and add -reru (踏む -> 踏まれる / 踏まれました).",
                "options": [
                    {"text": "踏まれました", "isCorrect": True, "reason": "Correct. U-verb passive: mu -> ma + remashita.", "trapCategory": "formation"},
                    {"text": "踏みました", "isCorrect": False, "reason": "Incorrect. Active voice ('I stepped on someone's foot').", "trapCategory": "meaning"},
                    {"text": "踏みられました", "isCorrect": False, "reason": "Incorrect. Overgeneralizing Ru-verb passive.", "trapCategory": "formation"},
                    {"text": "踏まさせました", "isCorrect": False, "reason": "Incorrect. Causative-passive hybrid.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the passive form of the U-verb 踏む?"
        },
        {
            "id": "g2-l21-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Suffering / adversity passive: was rained on and got soaked.",
            "question": "傘を持っていなかったので、雨に（　　）濡れてしまいました。",
            "translation": "Because I didn't have an umbrella, I was rained on and got soaked.",
            "options": ["降られて", "降って", "降らせて", "降らされて"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-21-38",
            "grammarPointTitle": "受身",
            "explanation": {
                "overall": "The suffering passive (迷惑の受身) with intransitive verbs denotes being adversely affected by an event: 雨に降られる (降る -> 降られて).",
                "options": [
                    {"text": "降られて", "isCorrect": True, "reason": "Correct. Suffering passive: 雨に降られて.", "trapCategory": "meaning"},
                    {"text": "降って", "isCorrect": False, "reason": "Incorrect. Active te-form cannot pair with '雨に' to express personal suffering.", "trapCategory": "formation"},
                    {"text": "降らせて", "isCorrect": False, "reason": "Incorrect. Causative ('making rain fall').", "trapCategory": "meaning"},
                    {"text": "降らされて", "isCorrect": False, "reason": "Incorrect. Causative-passive.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the famous Japanese suffering passive expression for being rained on?"
        },
        {
            "id": "g2-l21-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Transforming state: making the room quiet.",
            "question": "赤ちゃんが寝ていますから、テレビの音を（　　）してください。",
            "translation": "The baby is sleeping, so please make the TV sound smaller / quiet.",
            "options": ["小さく", "小さいに", "小さくて", "小さい"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-21-39",
            "grammarPointTitle": "形容詞＋する・〜てほしい",
            "explanation": {
                "overall": "To make something [Adjective], drop final い and attach く + する: 小さい -> 小さく + してください.",
                "options": [
                    {"text": "小さく", "isCorrect": True, "reason": "Correct. い-adjective + する: -i -> -ku + してください.", "trapCategory": "formation"},
                    {"text": "小さいに", "isCorrect": False, "reason": "Incorrect. い-adjectives never take に with する.", "trapCategory": "formation"},
                    {"text": "小さくて", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede してください directly.", "trapCategory": "formation"},
                    {"text": "小さい", "isCorrect": False, "reason": "Incorrect. Plain adjective cannot modify verb してください.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you conjugate an い-adjective before してください to mean 'make it [Adjective]'?"
        },
        {
            "id": "g2-l21-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Making something [Na-adjective]: please make the room clean.",
            "question": "パーティーの前に、部屋を（　　）しましょう。",
            "translation": "Before the party, let's make the room clean.",
            "options": ["綺麗に", "綺麗く", "綺麗な", "綺麗で"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-21-39",
            "grammarPointTitle": "形容詞＋する・〜てほしい",
            "explanation": {
                "overall": "For な-adjectives and nouns, to make something [Adj/Noun], attach に + する (綺麗にしましょう).",
                "options": [
                    {"text": "綺麗に", "isCorrect": True, "reason": "Correct. な-adjective + に + する: 綺麗にしましょう.", "trapCategory": "formation"},
                    {"text": "綺麗く", "isCorrect": False, "reason": "Incorrect. -ku is for い-adjectives; 綺麗 is a な-adjective.", "trapCategory": "formation"},
                    {"text": "綺麗な", "isCorrect": False, "reason": "Incorrect. な modifies nouns, not verb する.", "trapCategory": "formation"},
                    {"text": "綺麗で", "isCorrect": False, "reason": "Incorrect. で is te-form.", "trapCategory": "formation"}
                ]
            },
            "hint": "What particle connects a な-adjective to the verb する to mean 'make it [Adjective]'?"
        },
        {
            "id": "g2-l21-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 21",
            "type": "multiple-choice",
            "context": "Wanting someone else to do an action: I want my roommate to clean up the shared room.",
            "question": "ルームメイトに部屋を掃除し（　　）です。",
            "translation": "I want my roommate to clean the room.",
            "options": ["てほしい", "たい", "たがって", "てあげたい"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-21-39",
            "grammarPointTitle": "形容詞＋する・〜てほしい",
            "explanation": {
                "overall": "To express wanting another person to perform an action, use: Person に Verb te-form + ほしい (掃除してほしいです). (〜たい is for wanting oneself to do it).",
                "options": [
                    {"text": "てほしい", "isCorrect": True, "reason": "Correct. Wanting someone else to act: Person に V-te + ほしい.", "trapCategory": "meaning"},
                    {"text": "たい", "isCorrect": False, "reason": "Incorrect. 〜たい means the speaker wants to do the cleaning personally.", "trapCategory": "meaning"},
                    {"text": "たがって", "isCorrect": False, "reason": "Incorrect. Third-person desire.", "trapCategory": "meaning"},
                    {"text": "てあげたい", "isCorrect": False, "reason": "Incorrect. Means speaker wants to do favor for roommate.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses wanting SOMEONE ELSE to do something: 〜てほしい or 〜たい?"
        }
    ])

    # ==================== LESSON 22 ====================
    exercises.extend([
        {
            "id": "g2-l22-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Hypothetical conditional 〜ば: if you press this button, water comes out.",
            "question": "このボタンを（　　）、水が出ます。",
            "translation": "If you press this button, water comes out. (Conditional ba)",
            "options": ["押せば", "押したら", "押すと", "押すなら"],
            "correctIndex": 0,
            "grammarPointId": "g2-l22-ba-conditional",
            "grammarPointTitle": "〜ば (The Hypothetical Conditional: If)",
            "explanation": {
                "overall": "U-verb conditional 〜ば formation: change final -u vowel to -e and add ば (押す -> 押せば).",
                "options": [
                    {"text": "押せば", "isCorrect": True, "reason": "Correct. U-verb conditional ba: su -> se + ba.", "trapCategory": "formation"},
                    {"text": "押したら", "isCorrect": False, "reason": "Incorrect. While grammatically valid, lesson tests formation of 〜ば conditional.", "trapCategory": "context"},
                    {"text": "押すと", "isCorrect": False, "reason": "Incorrect. Conditional と, not ba.", "trapCategory": "formation"},
                    {"text": "押すなら", "isCorrect": False, "reason": "Incorrect. Conditional なら.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the conditional ba-form of the U-verb 押す?"
        },
        {
            "id": "g2-l22-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Hypothetical conditional 〜ば: if you practice every day, you will become good. Ru-verb 練習する / 食べる.",
            "question": "毎日野菜を食べ（　　）、健康になりますよ。",
            "translation": "If you eat vegetables every day, you will become healthy.",
            "options": ["れば", "たら", "ば", "ると"],
            "correctIndex": 0,
            "grammarPointId": "g2-l22-ba-conditional",
            "grammarPointTitle": "〜ば (The Hypothetical Conditional: If)",
            "explanation": {
                "overall": "Ru-verb conditional 〜ば formation: drop -ru and add -reba (食べる -> 食べれば).",
                "options": [
                    {"text": "れば", "isCorrect": True, "reason": "Correct. Ru-verb conditional: drop -ru + れば.", "trapCategory": "formation"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. Conditional たら.", "trapCategory": "formation"},
                    {"text": "ば", "isCorrect": False, "reason": "Incorrect. Cannot drop re for Ru-verbs.", "trapCategory": "formation"},
                    {"text": "ると", "isCorrect": False, "reason": "Incorrect. Conditional と.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the conditional ba-form of the Ru-verb 食べる?"
        },
        {
            "id": "g2-l22-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Negative hypothetical conditional: if you don't hurry, you will be late.",
            "question": "急が（　　）、電車に間に合いませんよ。",
            "translation": "If you don't hurry, you won't make the train in time.",
            "options": ["なければ", "ないで", "なくて", "ず"],
            "correctIndex": 0,
            "grammarPointId": "g2-l22-ba-conditional",
            "grammarPointTitle": "〜ば (The Hypothetical Conditional: If)",
            "explanation": {
                "overall": "Negative conditional 〜ば: change -nai to -nakereba (急がない -> 急がなければ).",
                "options": [
                    {"text": "なければ", "isCorrect": True, "reason": "Correct. Negative conditional: -nai -> -nakereba.", "trapCategory": "formation"},
                    {"text": "ないで", "isCorrect": False, "reason": "Incorrect. 'Without doing', not conditional if.", "trapCategory": "meaning"},
                    {"text": "なくて", "isCorrect": False, "reason": "Incorrect. Causal te-form.", "trapCategory": "formation"},
                    {"text": "ず", "isCorrect": False, "reason": "Incorrect. Archaic.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the negative conditional form ('if you do not...')?"
        },
        {
            "id": "g2-l22-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Frustrated concession 〜のに: 'Even though I studied all night, the exam went poorly'.",
            "question": "徹夜で勉強した（　　）、試験が全然できませんでした。",
            "translation": "Even though I studied all night, I couldn't do well on the exam at all.",
            "options": ["のに", "ので", "から", "けど"],
            "correctIndex": 0,
            "grammarPointId": "g2-l22-noni-frustration",
            "grammarPointTitle": "〜のに (Frustrated Concession: Even Though / In Spite Of)",
            "explanation": {
                "overall": "〜のに expresses frustrated concession ('even though / in spite of'), carrying the speaker's emotional indignation or disappointment when the outcome contradicts expectations.",
                "options": [
                    {"text": "のに", "isCorrect": True, "reason": "Correct. Frustrated concession: Short form + のに.", "trapCategory": "meaning"},
                    {"text": "ので", "isCorrect": False, "reason": "Incorrect. ので expresses cause ('because').", "trapCategory": "meaning"},
                    {"text": "から", "isCorrect": False, "reason": "Incorrect. から expresses cause.", "trapCategory": "meaning"},
                    {"text": "けど", "isCorrect": False, "reason": "Incorrect. けど is neutral contrast ('although'), lacking the strong personal frustration of のに.", "trapCategory": "context"}
                ]
            },
            "hint": "Which connective particle conveys emotional frustration or indignation: 'even though / despite'?"
        },
        {
            "id": "g2-l22-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Attaching 〜のに to a noun predicate: 'Even though it is Sunday, I have to work'.",
            "question": "日曜日（　　）のに、仕事に行かなければなりません。",
            "translation": "Even though it is Sunday, I have to go to work.",
            "options": ["な", "だ", "の", "である"],
            "correctIndex": 0,
            "grammarPointId": "g2-l22-noni-frustration",
            "grammarPointTitle": "〜のに (Frustrated Concession: Even Though / In Spite Of)",
            "explanation": {
                "overall": "Crucial formation rule: Before 〜のに, nouns and な-adjectives take な (日曜日 + な + のに, NOT *日曜日だのに).",
                "options": [
                    {"text": "な", "isCorrect": True, "reason": "Correct. Nouns and な-adjectives insert な before のに.", "trapCategory": "formation"},
                    {"text": "だ", "isCorrect": False, "reason": "Incorrect. Major learner trap: だ changes to な before のに.", "trapCategory": "formation"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. *ののに is ungrammatical.", "trapCategory": "formation"},
                    {"text": "である", "isCorrect": False, "reason": "Incorrect. Written formal style.", "trapCategory": "context"}
                ]
            },
            "hint": "What connector do nouns and な-adjectives take immediately before のに?"
        },
        {
            "id": "g2-l22-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Causative voice for Ru-verbs: Mother made the child eat vegetables. 食べる.",
            "question": "お母さんは子どもに野菜を（　　）。",
            "translation": "The mother made her child eat vegetables.",
            "options": ["食べさせました", "食べられました", "食べました", "食べさせられました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-22-40",
            "grammarPointTitle": "使役・使役＋授受",
            "explanation": {
                "overall": "Ru-verb causative formation: drop -ru and add -saseru (食べる -> 食べさせる / 食べさせました).",
                "options": [
                    {"text": "食べさせました", "isCorrect": True, "reason": "Correct. Ru-verb causative: drop -ru + させました.", "trapCategory": "formation"},
                    {"text": "食べられました", "isCorrect": False, "reason": "Incorrect. Passive voice ('was eaten').", "trapCategory": "meaning"},
                    {"text": "食べました", "isCorrect": False, "reason": "Incorrect. Simple active voice.", "trapCategory": "meaning"},
                    {"text": "食べさせられました", "isCorrect": False, "reason": "Incorrect. Causative-passive ('was forced to eat').", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the causative form of the Ru-verb 食べる?"
        },
        {
            "id": "g2-l22-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Causative voice for U-verbs: Father made Ken go shopping. 行く.",
            "question": "お父さんはけんに買い物に（　　）。",
            "translation": "The father made Ken go shopping.",
            "options": ["行かせました", "行かれました", "行きました", "行かせられました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-22-40",
            "grammarPointTitle": "使役・使役＋授受",
            "explanation": {
                "overall": "U-verb causative formation: change final -u vowel to -a and add -seru (行く -> 行かせる / 行かせました).",
                "options": [
                    {"text": "行かせました", "isCorrect": True, "reason": "Correct. U-verb causative: ku -> ka + semashita.", "trapCategory": "formation"},
                    {"text": "行かれました", "isCorrect": False, "reason": "Incorrect. Passive/honorific.", "trapCategory": "formation"},
                    {"text": "行きました", "isCorrect": False, "reason": "Incorrect. Simple active.", "trapCategory": "meaning"},
                    {"text": "行かせられました", "isCorrect": False, "reason": "Incorrect. Causative-passive ('was forced to go').", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the causative form of the U-verb 行く?"
        },
        {
            "id": "g2-l22-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Causative request asking for permission: 'Please let me introduce myself'.",
            "question": "私に自己紹介を（　　）ください。",
            "translation": "Please let me introduce myself.",
            "options": ["させて", "して", "されさせて", "してあげて"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-22-40",
            "grammarPointTitle": "使役・使役＋授受",
            "explanation": {
                "overall": "The formula for asking permission to do something yourself is: Causative te-form + ください (〜させてください). する -> させてください.",
                "options": [
                    {"text": "させて", "isCorrect": True, "reason": "Correct. Causative request formula: 〜させてください.", "trapCategory": "formation"},
                    {"text": "して", "isCorrect": False, "reason": "Incorrect. してください requests the OTHER person to introduce themselves.", "trapCategory": "meaning"},
                    {"text": "されさせて", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "してあげて", "isCorrect": False, "reason": "Incorrect. Ungrammatical in this context.", "trapCategory": "formation"}
                ]
            },
            "hint": "What causative request pattern means 'please allow/let me do [action]'?"
        },
        {
            "id": "g2-l22-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Parent issuing a firm command to a child: 'Eat your vegetables properly!'.",
            "question": "野菜をちゃんと（　　）なさい。",
            "translation": "Eat your vegetables properly! (Command from parent to child)",
            "options": ["食べ", "食べる", "食べて", "食べた"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-22-41",
            "grammarPointTitle": "〜なさい",
            "explanation": {
                "overall": "The command suffix 〜なさい attaches directly to the verb stem (drop -masu): 食べる -> 食べ + なさい (食べなさい).",
                "options": [
                    {"text": "食べ", "isCorrect": True, "reason": "Correct. Verb stem + なさい: 食べなさい.", "trapCategory": "formation"},
                    {"text": "食べる", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach なさい.", "trapCategory": "formation"},
                    {"text": "食べて", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach なさい.", "trapCategory": "formation"},
                    {"text": "食べた", "isCorrect": False, "reason": "Incorrect. Past form cannot attach なさい.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of the verb attaches to the imperative command suffix 〜なさい?"
        },
        {
            "id": "g2-l22-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 22",
            "type": "multiple-choice",
            "context": "Simile modifying a noun: 'A person like an angel'.",
            "question": "メアリーさんは天使の（　　）人です。",
            "translation": "Mary is a person like an angel.",
            "options": ["ような", "ように", "みたい", "そう"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-22-42",
            "grammarPointTitle": "〜のような・〜のように",
            "explanation": {
                "overall": "To modify a following noun with a simile, use: Noun + のような + Noun (天使のような人). (のように modifies verbs).",
                "options": [
                    {"text": "ような", "isCorrect": True, "reason": "Correct. Pre-noun simile modifier: Noun + のような + Noun.", "trapCategory": "formation"},
                    {"text": "ように", "isCorrect": False, "reason": "Incorrect. ように modifies verbs adverbially, not nouns.", "trapCategory": "formation"},
                    {"text": "みたい", "isCorrect": False, "reason": "Incorrect. みたい requires な before nouns (天使みたいな人), without の.", "trapCategory": "formation"},
                    {"text": "そう", "isCorrect": False, "reason": "Incorrect. Appearance suffix.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Do you use 〜のような or 〜のように to modify a NOUN?"
        }
    ])

    # ==================== LESSON 23 ====================
    exercises.extend([
        {
            "id": "g2-l23-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Concessive conditional 〜ても: 'Even if it rains tomorrow, the baseball match will take place'.",
            "question": "明日雨が降っ（　　）、試合はあります。",
            "translation": "Even if it rains tomorrow, the match will be held.",
            "options": ["ても", "たら", "れば", "と"],
            "correctIndex": 0,
            "grammarPointId": "g2-l23-temo-even-if",
            "grammarPointTitle": "〜ても / 〜でも (Concessive Conditional: Even If / Even Though)",
            "explanation": {
                "overall": "〜ても expresses concessive conditional ('even if / even though'): Verb te-form + も (降っても).",
                "options": [
                    {"text": "ても", "isCorrect": True, "reason": "Correct. Concessive conditional: V-te + も (降っても).", "trapCategory": "meaning"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. たら means 'if it rains [it will be canceled]'.", "trapCategory": "meaning"},
                    {"text": "れば", "isCorrect": False, "reason": "Incorrect. Hypothetical if.", "trapCategory": "meaning"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. Inevitable natural consequence.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses 'even if [condition occurs]'?"
        },
        {
            "id": "g2-l23-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Concessive conditional with い-adjective: 'Even if it is expensive, I want to buy it'.",
            "question": "少し（　　）も、この辞書を買いたいです。",
            "translation": "Even if it is a little expensive, I want to buy this dictionary.",
            "options": ["高く", "高い", "高くて", "高かった"],
            "correctIndex": 0,
            "grammarPointId": "g2-l23-temo-even-if",
            "grammarPointTitle": "〜ても / 〜でも (Concessive Conditional: Even If / Even Though)",
            "explanation": {
                "overall": "For い-adjectives, the concessive conditional drops final い and adds くても (高い -> 高くても).",
                "options": [
                    {"text": "高く", "isCorrect": True, "reason": "Correct. い-adjective te-form + も: -i -> -ku + ても (高くても).", "trapCategory": "formation"},
                    {"text": "高い", "isCorrect": False, "reason": "Incorrect. Failing to conjugate into te-form.", "trapCategory": "formation"},
                    {"text": "高くて", "isCorrect": False, "reason": "Incorrect. Extra 'て' before も.", "trapCategory": "formation"},
                    {"text": "高かった", "isCorrect": False, "reason": "Incorrect. Past tense.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the concessive conditional form of an い-adjective: 'even if it is [expensive]'?"
        },
        {
            "id": "g2-l23-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Personal conscious decision: 'I have decided to exercise every morning'.",
            "question": "毎朝ジョギングする（　　）にしました。",
            "translation": "I have decided to go jogging every morning.",
            "options": ["こと", "よう", "はず", "わけ"],
            "correctIndex": 0,
            "grammarPointId": "g2-l23-koto-ni-suru-naru",
            "grammarPointTitle": "〜ことにする vs 〜ことになる (Personal Decision vs Outside Emergence)",
            "explanation": {
                "overall": "〜ことにする denotes an active, personal conscious decision made by the speaker (V-dict + ことにする / ことにしました).",
                "options": [
                    {"text": "こと", "isCorrect": True, "reason": "Correct. Personal decision formula: V-dict + ことにする.", "trapCategory": "formation"},
                    {"text": "よう", "isCorrect": False, "reason": "Incorrect. ようにする means making an ongoing conscious effort, but '事にしました' is the decision formula.", "trapCategory": "meaning"},
                    {"text": "はず", "isCorrect": False, "reason": "Incorrect. Expectation.", "trapCategory": "meaning"},
                    {"text": "わけ", "isCorrect": False, "reason": "Incorrect. Explanation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which noun forms the decision pattern: V-dict + ___ にする?"
        },
        {
            "id": "g2-l23-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Habitual personal discipline: 'I make it a rule not to drink coffee at night'.",
            "question": "夜はコーヒーを飲まない（　　）。",
            "translation": "I make it a rule not to drink coffee at night.",
            "options": ["ことにしています", "ことになりました", "ことにします", "ことになっています"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-23-44",
            "grammarPointTitle": "〜ことにしている",
            "explanation": {
                "overall": "〜ことにしている denotes a personal rule or habitual policy that the speaker has decided upon and maintains consistently.",
                "options": [
                    {"text": "ことにしています", "isCorrect": True, "reason": "Correct. Habitual personal rule: 〜ことにしている.", "trapCategory": "meaning"},
                    {"text": "ことになりました", "isCorrect": False, "reason": "Incorrect. External organizational decision.", "trapCategory": "meaning"},
                    {"text": "ことにします", "isCorrect": False, "reason": "Incorrect. Single future decision, not established habitual practice.", "trapCategory": "meaning"},
                    {"text": "ことになっています", "isCorrect": False, "reason": "Incorrect. Established social rule/external regulation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses a personal habitual rule that you make a practice of following?"
        },
        {
            "id": "g2-l23-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "External arrangement / organizational decision: 'It has been decided that I will transfer to the Osaka branch next month'.",
            "question": "来月から大阪支社へ転勤する（　　）。",
            "translation": "It has been decided that I will transfer to the Osaka branch next month.",
            "options": ["ことになりました", "ことにしました", "ことになっています", "ことにしています"],
            "correctIndex": 0,
            "grammarPointId": "g2-l23-koto-ni-suru-naru",
            "grammarPointTitle": "〜ことにする vs 〜ことになる (Personal Decision vs Outside Emergence)",
            "explanation": {
                "overall": "〜ことになる denotes a decision or arrangement made by external circumstances, organizational decree, or mutual agreement outside one's sole personal control.",
                "options": [
                    {"text": "ことになりました", "isCorrect": True, "reason": "Correct. External/organizational decision: 〜ことになる / 〜ことになりました.", "trapCategory": "meaning"},
                    {"text": "ことにしました", "isCorrect": False, "reason": "Incorrect. Personal decision implies the speaker transferred themselves at will.", "trapCategory": "meaning"},
                    {"text": "ことになっています", "isCorrect": False, "reason": "Incorrect. General existing rule, not recent arrangement.", "trapCategory": "context"},
                    {"text": "ことにしています", "isCorrect": False, "reason": "Incorrect. Personal habit.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern denotes that something has been decided by external circumstances or organization: 〜ことになる or 〜ことにする?"
        },
        {
            "id": "g2-l23-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Causative-passive voice: was forced / made to sing a song at karaoke. U-verb 歌う.",
            "question": "カラオケで、先輩に歌を（　　）。",
            "translation": "At karaoke, I was forced / made to sing a song by my senior.",
            "options": ["歌わされました", "歌わせました", "歌われました", "歌いました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-23-43",
            "grammarPointTitle": "使役受身",
            "explanation": {
                "overall": "Causative-passive (使役受身) denotes being coerced or pressured into an action against one's preference. U-verbs (except -su) contract: 歌う -> 歌わされる / 歌わされました.",
                "options": [
                    {"text": "歌わされました", "isCorrect": True, "reason": "Correct. Contracted causative-passive: 歌わされました.", "trapCategory": "formation"},
                    {"text": "歌わせました", "isCorrect": False, "reason": "Incorrect. Causative ('I made the senior sing').", "trapCategory": "meaning"},
                    {"text": "歌われました", "isCorrect": False, "reason": "Incorrect. Passive voice.", "trapCategory": "meaning"},
                    {"text": "歌いました", "isCorrect": False, "reason": "Incorrect. Active voice.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the causative-passive form ('was forced to sing') of 歌う?"
        },
        {
            "id": "g2-l23-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Causative-passive voice: Ru-verb. Was made to eat disliked food. 食べる.",
            "question": "子どもの時、嫌いなピーマンを（　　）。",
            "translation": "When I was a child, I was made to eat bell peppers that I disliked.",
            "options": ["食べさせられました", "食べさせました", "食べられました", "食べました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-23-43",
            "grammarPointTitle": "使役受身",
            "explanation": {
                "overall": "Ru-verb causative-passive formation: drop -ru and append -saserareru (食べる -> 食べさせられる / 食べさせられました).",
                "options": [
                    {"text": "食べさせられました", "isCorrect": True, "reason": "Correct. Ru-verb causative-passive: 食べさせられました.", "trapCategory": "formation"},
                    {"text": "食べさせました", "isCorrect": False, "reason": "Incorrect. Causative ('I made someone eat').", "trapCategory": "meaning"},
                    {"text": "食べられました", "isCorrect": False, "reason": "Incorrect. Passive/potential.", "trapCategory": "meaning"},
                    {"text": "食べました", "isCorrect": False, "reason": "Incorrect. Active voice.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the causative-passive form of the Ru-verb 食べる?"
        },
        {
            "id": "g2-l23-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Deadline limit: 'Please submit the report by Friday at the latest'.",
            "question": "金曜日（　　）レポートを提出してください。",
            "translation": "Please submit the report by Friday.",
            "options": ["までに", "まで", "に", "で"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-23-45",
            "grammarPointTitle": "〜まで・〜方",
            "explanation": {
                "overall": "〜までに indicates a deadline by which a punctual action must be completed (金曜日までに提出する). 〜まで indicates continuous action lasting up until that point.",
                "options": [
                    {"text": "までに", "isCorrect": True, "reason": "Correct. Deadline limit: 〜までに.", "trapCategory": "meaning"},
                    {"text": "まで", "isCorrect": False, "reason": "Incorrect. 〜まで implies submitting continuously without stopping until Friday.", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に specifies exact punctual day, lacking the deadline 'no later than' nuance.", "trapCategory": "meaning"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で denotes time duration limit, but day deadline takes までに.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle marks a strict deadline by which an action must be done: 〜まで or 〜までに?"
        },
        {
            "id": "g2-l23-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Continuous duration: 'I will be studying at the library until 5:00'.",
            "question": "夕方五時（　　）図書館で勉強します。",
            "translation": "I will study at the library until 5:00 in the evening.",
            "options": ["まで", "までに", "から", "に"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-23-45",
            "grammarPointTitle": "〜まで・〜方",
            "explanation": {
                "overall": "〜まで denotes the endpoint of a continuous, ongoing activity (勉強する continues continuously until 5:00).",
                "options": [
                    {"text": "まで", "isCorrect": True, "reason": "Correct. Duration endpoint: 〜まで (continues until).", "trapCategory": "meaning"},
                    {"text": "までに", "isCorrect": False, "reason": "Incorrect. までに is for punctual completion deadline, clashing with continuous 勉強する.", "trapCategory": "meaning"},
                    {"text": "から", "isCorrect": False, "reason": "Incorrect. から indicates starting point ('starting from 5:00').", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に indicates punctual moment ('at 5:00').", "trapCategory": "meaning"}
                ]
            },
            "hint": "Do you use 〜まで or 〜までに for an activity continuing until a specific hour?"
        },
        {
            "id": "g2-l23-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 23",
            "type": "multiple-choice",
            "context": "Manner / method of doing: 'Please teach me how to read this kanji'.",
            "question": "この漢字の（　　）方を教えてください。",
            "translation": "Please teach me how to read this kanji.",
            "options": ["読み", "読む", "読ま", "読ん"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-23-45",
            "grammarPointTitle": "〜まで・〜方",
            "explanation": {
                "overall": "The method/manner noun pattern is: Verb stem (drop -masu) + 方 (かた): 読む -> 読み -> 読み方. The object marker を changes to noun-linking の (この漢字の読み方).",
                "options": [
                    {"text": "読み", "isCorrect": True, "reason": "Correct. Verb stem + 方: 読み方.", "trapCategory": "formation"},
                    {"text": "読む", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach 方 directly.", "trapCategory": "formation"},
                    {"text": "読ま", "isCorrect": False, "reason": "Incorrect. Negative stem.", "trapCategory": "formation"},
                    {"text": "読ん", "isCorrect": False, "reason": "Incorrect. Te-stem.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form attaches to 方（かた） to mean 'how to [do]'?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_genki2_l21_to_l23()
    print(f"Generated {len(ex_list)} exercises across Genki II Lessons 21 to 23.")
