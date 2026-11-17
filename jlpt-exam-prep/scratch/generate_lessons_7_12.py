import json

def get_exercises_l7_to_l12():
    exercises = []

    # ------------------ LESSON 7 ------------------
    exercises.extend([
        {
            "id": "g1-l7-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Phone call. Mom calls and asks what you are currently doing right now in your room.",
            "question": "今、部屋で日本語の教科書を（　　）。",
            "translation": "Right now, I am reading the Japanese textbook in my room.",
            "options": ["読んでいます", "読みます", "読んだ", "読みました"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-7-9",
            "grammarPointTitle": "〜ている：動作・結果",
            "explanation": {
                "overall": "〜ている attached to an activity verb denotes an ongoing progressive action happening at the current moment.",
                "options": [
                    {"text": "読んでいます", "isCorrect": True, "reason": "Correct. Ongoing progressive aspect: te-form + います.", "trapCategory": "formation"},
                    {"text": "読みます", "isCorrect": False, "reason": "Incorrect. Non-past expresses habitual action or future intent, not action occurring at '今'.", "trapCategory": "meaning"},
                    {"text": "読んだ", "isCorrect": False, "reason": "Incorrect. Casual past form.", "trapCategory": "formation"},
                    {"text": "読みました", "isCorrect": False, "reason": "Incorrect. Past tense indicates the reading has already finished.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which aspectual construction expresses an action in progress right now?"
        },
        {
            "id": "g1-l7-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Talking about family status. Ken got married three years ago and is currently in that marital state.",
            "question": "兄は三年前から（　　）。",
            "translation": "My older brother is married (has been married for three years).",
            "options": ["結婚しています", "結婚します", "結婚しました", "結婚ている"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-7-9",
            "grammarPointTitle": "〜ている：動作・結果",
            "explanation": {
                "overall": "結婚する is a change-of-state verb. In 〜ている, it describes the resulting persistent state ('is married'), not an ongoing ceremony.",
                "options": [
                    {"text": "結婚しています", "isCorrect": True, "reason": "Correct. Resultant state aspect: 結婚している ('is married').", "trapCategory": "meaning"},
                    {"text": "結婚します", "isCorrect": False, "reason": "Incorrect. Means he will get married in the future.", "trapCategory": "meaning"},
                    {"text": "結婚しました", "isCorrect": False, "reason": "Incorrect. While true in past tense, '〜から' with ongoing marital state requires 〜ています.", "trapCategory": "context"},
                    {"text": "結婚ている", "isCorrect": False, "reason": "Incorrect. Missing verb stem し before て.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you express the ongoing state of being married in Japanese?"
        },
        {
            "id": "g1-l7-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Asked if you know the teacher's phone number. You do not possess this information.",
            "question": "A:「先生の電話番号を知っていますか。」 B:「いいえ、（　　）。」",
            "translation": "A: 'Do you know the teacher's phone number?' B: 'No, I do not know it.'",
            "options": ["知りません", "知っていません", "知らないでした", "知りませんでした"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-7-9",
            "grammarPointTitle": "〜ている：動作・結果",
            "explanation": {
                "overall": "Famous Genki I grammatical rule: while knowing is '知っています', not knowing is strictly '知りません' (NOT *知っていません).",
                "options": [
                    {"text": "知りません", "isCorrect": True, "reason": "Correct. The negative of 知っています is 知りません.", "trapCategory": "formation"},
                    {"text": "知っていません", "isCorrect": False, "reason": "Incorrect. Famous learner trap: 知っていません is ungrammatical in standard Japanese.", "trapCategory": "formation"},
                    {"text": "知らないでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical hybrid formation.", "trapCategory": "formation"},
                    {"text": "知りませんでした", "isCorrect": False, "reason": "Incorrect. Past negative ('I did not know it [until you told me]'), but the speaker still does not know it.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the correct negative form corresponding to 知っています?"
        },
        {
            "id": "g1-l7-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Stating current residence. Where you reside permanently or long-term.",
            "question": "私は家族と東京に（　　）。",
            "translation": "I live in Tokyo with my family.",
            "options": ["住んでいます", "住みます", "住んであります", "住みでした"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-7-9",
            "grammarPointTitle": "〜ている：動作・結果",
            "explanation": {
                "overall": "住む expresses establishing residence; living somewhere continuously is expressed by the continuous state 住んでいます.",
                "options": [
                    {"text": "住んでいます", "isCorrect": True, "reason": "Correct. Ongoing state of residence: に住んでいます.", "trapCategory": "formation"},
                    {"text": "住みます", "isCorrect": False, "reason": "Incorrect. Implies future relocation ('I will move to Tokyo').", "trapCategory": "meaning"},
                    {"text": "住んであります", "isCorrect": False, "reason": "Incorrect. 〜てある is transitive preparation, not human residence.", "trapCategory": "formation"},
                    {"text": "住みでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which pattern expresses continuous residential state in a city?"
        },
        {
            "id": "g1-l7-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Describing Mary's physical appearance: she has long hair.",
            "question": "メアリーさんは髪（　　）長いです。",
            "translation": "Mary has long hair.",
            "options": ["が", "は", "を", "の"],
            "correctIndex": 0,
            "grammarPointId": "g1-l7-describing-people",
            "grammarPointTitle": "身体の描写 (Describing People's Physical Attributes: 目が大きいです)",
            "explanation": {
                "overall": "The Japanese pattern for describing personal attributes is: [Person] は [Body Part] が [Adjective] です.",
                "options": [
                    {"text": "が", "isCorrect": True, "reason": "Correct. Marks specific attribute: Person は Body part が Adjective です.", "trapCategory": "formation"},
                    {"text": "は", "isCorrect": False, "reason": "Incorrect. Double は creates contrast rather than standard attribute description.", "trapCategory": "context"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. 長い is an adjective, not an action verb taking a direct object.", "trapCategory": "formation"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. 'メアリーさんの髪長いです' lacks standard topic structure.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle marks the specific body feature in 'Person は [Feature] ___ [Adjective] です'?"
        },
        {
            "id": "g1-l7-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Describing Professor Tanaka who is wearing glasses right now.",
            "question": "田中先生は眼鏡を（　　）。",
            "translation": "Professor Tanaka is wearing glasses.",
            "options": ["かけています", "着ています", "履いています", "かぶっています"],
            "correctIndex": 0,
            "grammarPointId": "g1-l7-describing-people",
            "grammarPointTitle": "身体の描写 (Describing People's Physical Attributes: 目が大きいです)",
            "explanation": {
                "overall": "In Japanese, different clothing items take distinct verbs: glasses take かける -> かけています. (着る is for upper body, 履く for feet/legs, かぶる for hats).",
                "options": [
                    {"text": "かけています", "isCorrect": True, "reason": "Correct. Specific verb for wearing eyeglasses is 眼鏡をかける.", "trapCategory": "meaning"},
                    {"text": "着ています", "isCorrect": False, "reason": "Incorrect. 着る is for shirts/jackets over torso.", "trapCategory": "meaning"},
                    {"text": "履いています", "isCorrect": False, "reason": "Incorrect. 履く is for shoes, socks, pants.", "trapCategory": "meaning"},
                    {"text": "かぶっています", "isCorrect": False, "reason": "Incorrect. かぶる is for headgear/hats.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which specific Japanese verb is used for wearing glasses?"
        },
        {
            "id": "g1-l7-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Recommending a local ramen shop: the food is inexpensive AND delicious.",
            "question": "あの店のラーメンは（　　）、とても美味しいです。",
            "translation": "That shop's ramen is cheap and very delicious.",
            "options": ["安くて", "安いで", "安いて", "安くてで"],
            "correctIndex": 0,
            "grammarPointId": "g1-l7-adj-te-forms",
            "grammarPointTitle": "形容詞・名詞の「て形」 (Connecting Adjectives & Nouns: 〜くて / 〜で)",
            "explanation": {
                "overall": "To connect two い-adjectives, drop final い and append くて (安い -> 安くて).",
                "options": [
                    {"text": "安くて", "isCorrect": True, "reason": "Correct. い-adjective te-form rule: -i -> -kute.", "trapCategory": "formation"},
                    {"text": "安いで", "isCorrect": False, "reason": "Incorrect. で is the connector for な-adjectives and nouns, not い-adjectives.", "trapCategory": "formation"},
                    {"text": "安いて", "isCorrect": False, "reason": "Incorrect. Missing k in -kute.", "trapCategory": "formation"},
                    {"text": "安くてで", "isCorrect": False, "reason": "Incorrect. Redundant combination.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the te-form of an い-adjective used to connect it to another predicate?"
        },
        {
            "id": "g1-l7-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Describing the hotel's room: it is quiet AND clean.",
            "question": "部屋は（　　）、綺麗でした。",
            "translation": "The room was quiet and clean.",
            "options": ["静かで", "静かくて", "静かて", "静かなで"],
            "correctIndex": 0,
            "grammarPointId": "g1-l7-adj-te-forms",
            "grammarPointTitle": "形容詞・名詞の「て形」 (Connecting Adjectives & Nouns: 〜くて / 〜で)",
            "explanation": {
                "overall": "To connect な-adjectives or nouns, attach で (静か -> 静かで). Tense is expressed at the end of the sentence (綺麗でした).",
                "options": [
                    {"text": "静かで", "isCorrect": True, "reason": "Correct. な-adjective / noun te-form connector is で.", "trapCategory": "formation"},
                    {"text": "静かくて", "isCorrect": False, "reason": "Incorrect. 〜くて is only for い-adjectives; 静か is a な-adjective.", "trapCategory": "formation"},
                    {"text": "静かて", "isCorrect": False, "reason": "Incorrect. Missing voiced sound d.", "trapCategory": "formation"},
                    {"text": "静かなで", "isCorrect": False, "reason": "Incorrect. Do not retain な before connecting で.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the connector form for な-adjectives when linking clauses?"
        },
        {
            "id": "g1-l7-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Explaining the purpose of going to the library: to borrow books.",
            "question": "図書館へ本を（　　）に行きます。",
            "translation": "I am going to the library to borrow books.",
            "options": ["借り", "借りる", "借ります", "借りて"],
            "correctIndex": 0,
            "grammarPointId": "g1-l7-purpose-ni-iku",
            "grammarPointTitle": "V-stem + に行く / に来る (Purpose of Movement: Going to Do)",
            "explanation": {
                "overall": "The pattern for purpose of movement is: Destination へ Verb-stem + に行く / に来る (借りる -> 借り + に行く).",
                "options": [
                    {"text": "借り", "isCorrect": True, "reason": "Correct. Verb stem of 借りる is 借り: 借りにいきます.", "trapCategory": "formation"},
                    {"text": "借りる", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot directly precede purpose particle に.", "trapCategory": "formation"},
                    {"text": "借ります", "isCorrect": False, "reason": "Incorrect. Masu-ending must be dropped to leave the pure stem.", "trapCategory": "formation"},
                    {"text": "借りて", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede purpose に.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of the verb precedes the purpose particle に in 〜に行く?"
        },
        {
            "id": "g1-l7-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Specifying how many people are in your immediate family: four people.",
            "question": "私の家族は（　　）です。",
            "translation": "My family is four people.",
            "options": ["四人（よにん）", "四人（しにん）", "四人（よんひと）", "四人（よんにん）"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-7-10",
            "grammarPointTitle": "人数を数える",
            "explanation": {
                "overall": "The counter for people has irregular readings: 1=ひとり, 2=ふたり, and 4 is strictly よにん (NOT しにん, which sounds like 死人 'corpse').",
                "options": [
                    {"text": "四人（よにん）", "isCorrect": True, "reason": "Correct. Four people is pronounced よにん.", "trapCategory": "formation"},
                    {"text": "四人（しにん）", "isCorrect": False, "reason": "Incorrect. Taboo homophone error with 'dead person'.", "trapCategory": "formation"},
                    {"text": "四人（よんひと）", "isCorrect": False, "reason": "Incorrect. Irregular pseudo-reading.", "trapCategory": "formation"},
                    {"text": "四人（よんにん）", "isCorrect": False, "reason": "Incorrect. Overgeneralizing yon without truncation to yo-.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the correct pronunciation of four people (四人)?"
        },
        {
            "id": "g1-l7-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Describing someone who has gained weight and is currently plump/heavy.",
            "question": "私の猫はちょっと（　　）。",
            "translation": "My cat is a little fat / plump.",
            "options": ["太っています", "太ります", "太ったでした", "太るです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-7-9",
            "grammarPointTitle": "〜ている：動作・結果",
            "explanation": {
                "overall": "太る is a change-of-state verb ('to gain weight'). To describe someone as being fat/overweight, Japanese uses the resultant state 太っています.",
                "options": [
                    {"text": "太っています", "isCorrect": True, "reason": "Correct. Resultant state: 太っている ('is fat/heavy').", "trapCategory": "meaning"},
                    {"text": "太ります", "isCorrect": False, "reason": "Incorrect. Means 'will gain weight' in the future.", "trapCategory": "meaning"},
                    {"text": "太ったでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical double past copula.", "trapCategory": "formation"},
                    {"text": "太るです", "isCorrect": False, "reason": "Incorrect. Plain verb cannot attach です.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you say that someone is currently fat/overweight in Japanese?"
        },
        {
            "id": "g1-l7-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 7",
            "type": "multiple-choice",
            "context": "Negative adjective coordination: the hotel was not cheap, and was inconvenient.",
            "question": "そのホテルは（　　）、不便でした。",
            "translation": "That hotel was not cheap, and it was inconvenient.",
            "options": ["安くなくて", "安くないで", "安くなかったで", "安いくなくて"],
            "correctIndex": 0,
            "grammarPointId": "g1-l7-adj-te-forms",
            "grammarPointTitle": "形容詞・名詞の「て形」 (Connecting Adjectives & Nouns: 〜くて / 〜で)",
            "explanation": {
                "overall": "The negative of an い-adjective is 〜くない. Since ない itself functions as an い-adjective, its te-form is 〜くなくて (安くない -> 安くなくて).",
                "options": [
                    {"text": "安くなくて", "isCorrect": True, "reason": "Correct. Negative い-adjective te-form: -kunai -> -kunakute.", "trapCategory": "formation"},
                    {"text": "安くないで", "isCorrect": False, "reason": "Incorrect. 〜ないで is negative verb request ('without doing'), not adjective linker.", "trapCategory": "formation"},
                    {"text": "安くなかったで", "isCorrect": False, "reason": "Incorrect. Tense is marked at the final clause, not with past connector.", "trapCategory": "formation"},
                    {"text": "安いくなくて", "isCorrect": False, "reason": "Incorrect. Failing to drop stem final -i.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the te-form of the negative ending 〜くない?"
        }
    ])

    # ------------------ LESSON 8 ------------------
    exercises.extend([
        {
            "id": "g1-l8-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Art museum security guard politely reminding visitors not to take photographs.",
            "question": "ここで写真を撮ら（　　）ください。",
            "translation": "Please do not take photographs here.",
            "options": ["ないで", "なくて", "ない", "ず"],
            "correctIndex": 0,
            "grammarPointId": "g1-l8-nai-de-kudasai",
            "grammarPointTitle": "〜ないでください (Negative Request: Please Do Not)",
            "explanation": {
                "overall": "Negative requests use the formula: Verb short negative (nai-form) + でください -> 〜ないでください.",
                "options": [
                    {"text": "ないで", "isCorrect": True, "reason": "Correct. Negative request formula: 〜ないでください.", "trapCategory": "formation"},
                    {"text": "なくて", "isCorrect": False, "reason": "Incorrect. 〜なくて is the causal/coordinate te-form, not used for requests.", "trapCategory": "formation"},
                    {"text": "ない", "isCorrect": False, "reason": "Incorrect. Missing で before ください.", "trapCategory": "formation"},
                    {"text": "ず", "isCorrect": False, "reason": "Incorrect. Classical archaic negative prefix.", "trapCategory": "formation"}
                ]
            },
            "hint": "What ending attaches to the negative verb stem before ください to make a polite negative request?"
        },
        {
            "id": "g1-l8-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Casual conversation between close friends. Asking if the friend will go to the party tonight.",
            "question": "今晩のパーティー、（　　）？",
            "translation": "Are you going to tonight's party? (Casual short form)",
            "options": ["行く", "行きます", "行った", "行き"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-11",
            "grammarPointTitle": "普通形・と思う・と言う",
            "explanation": {
                "overall": "In informal casual speech with friends, questions use the dictionary short form with rising intonation, omitting か.",
                "options": [
                    {"text": "行く", "isCorrect": True, "reason": "Correct. Casual short form present affirmative with rising pitch.", "trapCategory": "context"},
                    {"text": "行きます", "isCorrect": False, "reason": "Incorrect. Polite form, not casual peer speech.", "trapCategory": "context"},
                    {"text": "行った", "isCorrect": False, "reason": "Incorrect. Past tense, but event is '今晩'.", "trapCategory": "meaning"},
                    {"text": "行き", "isCorrect": False, "reason": "Incorrect. Bare stem cannot terminate a casual sentence.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which form of 行く is used for casual present questions among friends?"
        },
        {
            "id": "g1-l8-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Conjugating U-verb 話す into short negative (nai-form): 'I will not speak'.",
            "question": "私はその秘密をだれにも（　　）。",
            "translation": "I will not speak of that secret to anyone.",
            "options": ["話さない", "話しない", "話さないです", "話すない"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-11",
            "grammarPointTitle": "普通形・と思う・と言う",
            "explanation": {
                "overall": "U-verbs ending in -su change -u vowel to -a vowel and add -nai: 話す -> 話さ + ない -> 話さない.",
                "options": [
                    {"text": "話さない", "isCorrect": True, "reason": "Correct. U-verb nai-form: su -> sa + nai.", "trapCategory": "formation"},
                    {"text": "話しない", "isCorrect": False, "reason": "Incorrect. Overgeneralizing する irregular stem.", "trapCategory": "formation"},
                    {"text": "話さないです", "isCorrect": False, "reason": "Incorrect. Formal hybrid, not pure short form.", "trapCategory": "formation"},
                    {"text": "話すない", "isCorrect": False, "reason": "Incorrect. Adding nai directly to dictionary form is ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the short negative (nai-form) of the U-verb 話す?"
        },
        {
            "id": "g1-l8-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Stating that you do not have money today. The verb is ある (inanimate existence).",
            "question": "今日、お金が全然（　　）。",
            "translation": "I don't have any money at all today.",
            "options": ["ない", "あらない", "ありませんでした", "なかった"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-11",
            "grammarPointTitle": "普通形・と思う・と言う",
            "explanation": {
                "overall": "The short negative form of ある is irregular: it becomes simply ない (there is no *あらない in Japanese).",
                "options": [
                    {"text": "ない", "isCorrect": True, "reason": "Correct. Famous irregular short negative: ある -> ない.", "trapCategory": "formation"},
                    {"text": "あらない", "isCorrect": False, "reason": "Incorrect. Overregularization trap; あらない does not exist.", "trapCategory": "formation"},
                    {"text": "ありませんでした", "isCorrect": False, "reason": "Incorrect. Polite past form.", "trapCategory": "meaning"},
                    {"text": "なかった", "isCorrect": False, "reason": "Incorrect. Past tense, but context specifies '今日'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the short negative form of the verb ある?"
        },
        {
            "id": "g1-l8-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Expressing your personal opinion about tomorrow's weather.",
            "question": "明日は雨が降る（　　）。",
            "translation": "I think it will rain tomorrow.",
            "options": ["と思います", "と言います", "と聞きます", "と話します"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-11",
            "grammarPointTitle": "普通形・と思う・と言う",
            "explanation": {
                "overall": "〜と思う takes a clause in short form and expresses the speaker's personal thought or speculation.",
                "options": [
                    {"text": "と思います", "isCorrect": True, "reason": "Correct. Expresses personal opinion: Short form + と思います.", "trapCategory": "context"},
                    {"text": "と言います", "isCorrect": False, "reason": "Incorrect. 言います means 'says', quoting someone else.", "trapCategory": "meaning"},
                    {"text": "と聞きます", "isCorrect": False, "reason": "Incorrect. 聞きます means 'hears'.", "trapCategory": "meaning"},
                    {"text": "と話します", "isCorrect": False, "reason": "Incorrect. 話します means 'speaks/tells'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which phrase expresses personal belief or opinion: 'I think that...'?"
        },
        {
            "id": "g1-l8-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Reporting what Ken said: Ken said he was busy yesterday.",
            "question": "けんさんはきのう忙しかった（　　）。",
            "translation": "Ken said that he was busy yesterday.",
            "options": ["と言っていました", "と思っていました", "と行きました", "と見ました"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-11",
            "grammarPointTitle": "普通形・と思う・と言う",
            "explanation": {
                "overall": "To report third-person speech or statements, Japanese uses: Short form + と言っていました (or と言いました).",
                "options": [
                    {"text": "と言っていました", "isCorrect": True, "reason": "Correct. Standard indirect quotation formula for reporting third-person speech.", "trapCategory": "context"},
                    {"text": "と思っていました", "isCorrect": False, "reason": "Incorrect. Reports inner thoughts, not what Ken verbally stated.", "trapCategory": "meaning"},
                    {"text": "と行きました", "isCorrect": False, "reason": "Incorrect. Meaningless combination.", "trapCategory": "formation"},
                    {"text": "と見ました", "isCorrect": False, "reason": "Incorrect. Meaningless combination.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which pattern is used to report what someone else said?"
        },
        {
            "id": "g1-l8-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Expressing your hobby: 'I like reading Japanese manga'.",
            "question": "私は日本の漫画を（　　）が好きです。",
            "translation": "I like reading Japanese manga.",
            "options": ["読むの", "読み", "読むことの", "読んで"],
            "correctIndex": 0,
            "grammarPointId": "g1-l8-nominalizer-no",
            "grammarPointTitle": "動詞の「の」名詞化 (Nominalizing Verbs with の: のが好き / 上手 / 下手)",
            "explanation": {
                "overall": "To make a verb into a noun phrase before が好き/嫌い/上手/下手, attach the nominalizer の to the dictionary short form (読む -> 読むの).",
                "options": [
                    {"text": "読むの", "isCorrect": True, "reason": "Correct. Verb nominalization formula: V-dict + の + が好きです.", "trapCategory": "formation"},
                    {"text": "読み", "isCorrect": False, "reason": "Incorrect. Masu-stem alone cannot function as the object of 好き.", "trapCategory": "formation"},
                    {"text": "読むことの", "isCorrect": False, "reason": "Incorrect. Redundant particle の.", "trapCategory": "formation"},
                    {"text": "読んで", "isCorrect": False, "reason": "Incorrect. Te-form cannot be nominalized with が好き.", "trapCategory": "formation"}
                ]
            },
            "hint": "What particle nominalizes a verb directly before が好きです?"
        },
        {
            "id": "g1-l8-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Stating that Takeshi is skillful at cooking.",
            "question": "たけしさんは料理を（　　）がとても上手です。",
            "translation": "Takeshi is very good at cooking meals.",
            "options": ["作るの", "作ります", "作った", "作って"],
            "correctIndex": 0,
            "grammarPointId": "g1-l8-nominalizer-no",
            "grammarPointTitle": "動詞の「の」名詞化 (Nominalizing Verbs with の: のが好き / 上手 / 下手)",
            "explanation": {
                "overall": "Skill evaluation (上手 / 下手) takes a nominalized verb phrase: V-dict + の が 上手です.",
                "options": [
                    {"text": "作るの", "isCorrect": True, "reason": "Correct. V-dict + の nominalization with が上手です.", "trapCategory": "formation"},
                    {"text": "作ります", "isCorrect": False, "reason": "Incorrect. Masu-form cannot attach が上手です.", "trapCategory": "formation"},
                    {"text": "作った", "isCorrect": False, "reason": "Incorrect. General skill is evaluated with non-past nominalization, not past ta-form.", "trapCategory": "meaning"},
                    {"text": "作って", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach が上手です.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you nominalize 作る before が上手です?"
        },
        {
            "id": "g1-l8-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Asking someone if they ate anything for lunch.",
            "question": "昼ご飯に（　　）食べましたか。",
            "translation": "Did you eat something for lunch?",
            "options": ["何か", "何を", "何も", "何"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-12",
            "grammarPointTitle": "が・何か・何も",
            "explanation": {
                "overall": "何か means 'something' in affirmative questions. Unlike 何を ('what did you eat?'), 何か asks whether you ate anything at all.",
                "options": [
                    {"text": "何か", "isCorrect": True, "reason": "Correct. Indefinite pronoun 'something' / 'anything' in yes-no questions.", "trapCategory": "meaning"},
                    {"text": "何を", "isCorrect": False, "reason": "Incorrect. 何を turns it into an open question ('What did you eat?'), not a general yes-no inquiry.", "trapCategory": "meaning"},
                    {"text": "何も", "isCorrect": False, "reason": "Incorrect. 何も requires a negative verb (何も食べませんでした).", "trapCategory": "formation"},
                    {"text": "何", "isCorrect": False, "reason": "Incorrect. Missing particle/marker.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which word means 'something' in a yes-no question?"
        },
        {
            "id": "g1-l8-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Responding to a food question: having had no appetite, you ate nothing at all.",
            "question": "お腹が痛かったから、（　　）食べませんでした。",
            "translation": "Because my stomach hurt, I did not eat anything.",
            "options": ["何も", "何か", "何が", "何を"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-12",
            "grammarPointTitle": "が・何か・何も",
            "explanation": {
                "overall": "Total negation requires: 何も + negative verb ('not eat anything / eat nothing').",
                "options": [
                    {"text": "何も", "isCorrect": True, "reason": "Correct. Total negation: 何も + negative verb.", "trapCategory": "formation"},
                    {"text": "何か", "isCorrect": False, "reason": "Incorrect. 何か is used in affirmative sentences ('ate something').", "trapCategory": "meaning"},
                    {"text": "何が", "isCorrect": False, "reason": "Incorrect. Interrogative subject, ungrammatical here.", "trapCategory": "formation"},
                    {"text": "何を", "isCorrect": False, "reason": "Incorrect. 何を requires question か, not negative statement.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which word combines with a negative verb to mean 'not anything / nothing'?"
        },
        {
            "id": "g1-l8-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Stating that you think tomorrow is a day off. Noun predicate before と思う.",
            "question": "明日は休み（　　）と思います。",
            "translation": "I think that tomorrow is a day off.",
            "options": ["だ", "です", "な", "の"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-11",
            "grammarPointTitle": "普通形・と思う・と言う",
            "explanation": {
                "overall": "Before quotative と, nouns and な-adjectives take the short copula だ (休みだ / 静かだ). Omitting だ or using polite です is ungrammatical.",
                "options": [
                    {"text": "だ", "isCorrect": True, "reason": "Correct. Short copula だ required for nouns and な-adjectives before と思う.", "trapCategory": "formation"},
                    {"text": "です", "isCorrect": False, "reason": "Incorrect. Quotative と clause must be in short form, not polite です.", "trapCategory": "formation"},
                    {"text": "な", "isCorrect": False, "reason": "Incorrect. な is pre-noun modifier, not copula before と.", "trapCategory": "formation"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. の cannot act as the copula before と.", "trapCategory": "formation"}
                ]
            },
            "hint": "What copula form must attach to a noun before と思います?"
        },
        {
            "id": "g1-l8-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 8",
            "type": "multiple-choice",
            "context": "Looking into the empty auditorium: nobody is there.",
            "question": "教室には（　　）いませんでした。",
            "translation": "There was no one in the classroom.",
            "options": ["だれも", "だれか", "だれが", "だれは"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-8-12",
            "grammarPointTitle": "が・何か・何も",
            "explanation": {
                "overall": "だれも + negative verb means 'no one / nobody'.",
                "options": [
                    {"text": "だれも", "isCorrect": True, "reason": "Correct. だれも + negative verb = 'no one'.", "trapCategory": "formation"},
                    {"text": "だれか", "isCorrect": False, "reason": "Incorrect. だれか means 'someone', used with affirmative predicates.", "trapCategory": "meaning"},
                    {"text": "だれが", "isCorrect": False, "reason": "Incorrect. Who was there (inquiry), not 'nobody'.", "trapCategory": "meaning"},
                    {"text": "だれは", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which word combines with a negative verb to mean 'no one'?"
        }
    ])

    # ------------------ LESSON 9 ------------------
    exercises.extend([
        {
            "id": "g1-l9-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Casual conversation. Asking a friend if they read yesterday's article.",
            "question": "きのうの記事、（　　）？",
            "translation": "Did you read yesterday's article? (Casual past affirmative)",
            "options": ["読んだ", "読みた", "読だ", "読まなかった"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "The short past affirmative (Ta-form) follows identical rules to the te-form: 読む -> 飲んで -> 読んだ.",
                "options": [
                    {"text": "読んだ", "isCorrect": True, "reason": "Correct. Ta-form of 読む is 読んだ.", "trapCategory": "formation"},
                    {"text": "読みた", "isCorrect": False, "reason": "Incorrect. Unassimilated stem error.", "trapCategory": "formation"},
                    {"text": "読だ", "isCorrect": False, "reason": "Incorrect. Missing nasal n.", "trapCategory": "formation"},
                    {"text": "読まなかった", "isCorrect": False, "reason": "Incorrect. Negative past form ('did not read').", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the short past form (ta-form) of 読む?"
        },
        {
            "id": "g1-l9-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Stating in short past negative that you did not go to school yesterday.",
            "question": "きのうは熱があったから、学校へ（　　）。",
            "translation": "Because I had a fever yesterday, I didn't go to school.",
            "options": ["行かなかった", "行かないでした", "行かなかったでした", "行きてなかった"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "Short past negative drops -i from nai-form and adds -katta: 行かない -> 行かなかった.",
                "options": [
                    {"text": "行かなかった", "isCorrect": True, "reason": "Correct. Short past negative: nai -> nakatta.", "trapCategory": "formation"},
                    {"text": "行かないでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical hybrid construction.", "trapCategory": "formation"},
                    {"text": "行かなかったでした", "isCorrect": False, "reason": "Incorrect. Redundant past markers.", "trapCategory": "formation"},
                    {"text": "行きてなかった", "isCorrect": False, "reason": "Incorrect. Ungrammatical stem.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the short past negative of 行く?"
        },
        {
            "id": "g1-l9-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Asking if homework has already been completed.",
            "question": "A:「（　　）宿題をしましたか。」 B:「はい、もうしました。」",
            "translation": "A: 'Have you already done the homework?' B: 'Yes, I have already done it.'",
            "options": ["もう", "まだ", "また", "もっと"],
            "correctIndex": 0,
            "grammarPointId": "g1-l9-mou-mada",
            "grammarPointTitle": "もう〜ました vs まだ〜ていません (Already Done vs Have Not Yet Done)",
            "explanation": {
                "overall": "もう + past verb means 'already done'.",
                "options": [
                    {"text": "もう", "isCorrect": True, "reason": "Correct. Expresses completion: もう + past verb.", "trapCategory": "formation"},
                    {"text": "まだ", "isCorrect": False, "reason": "Incorrect. まだ means 'still/not yet'.", "trapCategory": "meaning"},
                    {"text": "また", "isCorrect": False, "reason": "Incorrect. また means 'again'.", "trapCategory": "meaning"},
                    {"text": "もっと", "isCorrect": False, "reason": "Incorrect. もっと means 'more'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which word means 'already' when paired with a past verb?"
        },
        {
            "id": "g1-l9-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Asked if you have already eaten lunch. You have not eaten it yet.",
            "question": "A:「もう昼ご飯を食べましたか。」 B:「いいえ、（　　）。」",
            "translation": "A: 'Have you already eaten lunch?' B: 'No, I have not eaten yet.'",
            "options": ["まだ食べていません", "まだ食べませんでした", "もう食べません", "食べませんでした"],
            "correctIndex": 0,
            "grammarPointId": "g1-l9-mou-mada",
            "grammarPointTitle": "もう〜ました vs まだ〜ていません (Already Done vs Have Not Yet Done)",
            "explanation": {
                "overall": "To say 'have not yet done something', Japanese strictly requires まだ〜ていません. Using *まだ食べませんでした is a major error because past negative implies you never will/did not during the whole past period.",
                "options": [
                    {"text": "まだ食べていません", "isCorrect": True, "reason": "Correct. The formula for 'have not yet done' is まだ〜ていません.", "trapCategory": "formation"},
                    {"text": "まだ食べませんでした", "isCorrect": False, "reason": "Incorrect. Major learner mistake: まだ cannot be used with simple past negative for unfinished actions.", "trapCategory": "formation"},
                    {"text": "もう食べません", "isCorrect": False, "reason": "Incorrect. Means 'I will not eat anymore'.", "trapCategory": "meaning"},
                    {"text": "食べませんでした", "isCorrect": False, "reason": "Incorrect. Simple past negative implies you skipped lunch entirely.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the standard grammatical formula for 'have not yet done'?"
        },
        {
            "id": "g1-l9-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Talking about a book: 'The book that I bought yesterday was interesting'.",
            "question": "きのう（　　）本はとても面白かったです。",
            "translation": "The book that I bought yesterday was very interesting.",
            "options": ["買った", "買いました", "買うの", "買って"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "In Japanese relative clauses, verbs modify nouns in short form (short past 買った + 本). Polite forms (*買いました本) are not used.",
                "options": [
                    {"text": "買った", "isCorrect": True, "reason": "Correct. Short past form modifying noun directly: 買った本.", "trapCategory": "formation"},
                    {"text": "買いました", "isCorrect": False, "reason": "Incorrect. Polite forms cannot modify nouns in relative clauses.", "trapCategory": "formation"},
                    {"text": "買うの", "isCorrect": False, "reason": "Incorrect. Pre-noun relative clauses do not insert の.", "trapCategory": "formation"},
                    {"text": "買って", "isCorrect": False, "reason": "Incorrect. Te-form cannot directly modify a noun.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form modifies nouns in Japanese relative clauses?"
        },
        {
            "id": "g1-l9-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Describing delicious food: 'The cake that my mother made was delicious'.",
            "question": "母（　　）作ったケーキは美味しかったです。",
            "translation": "The cake that my mother made was delicious.",
            "options": ["が", "は", "を", "に"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "Within a relative clause, the subject is strictly marked by が (or の), NEVER the topic marker は.",
                "options": [
                    {"text": "が", "isCorrect": True, "reason": "Correct. Subject inside relative clauses takes が.", "trapCategory": "formation"},
                    {"text": "は", "isCorrect": False, "reason": "Incorrect. Subject inside embedded relative clauses cannot take topic marker は.", "trapCategory": "formation"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. Mother is the actor/maker, not direct object.", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. Mother is the subject of 作った, not destination.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the subject inside an embedded relative clause?"
        },
        {
            "id": "g1-l9-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Explaining that the person who lived next door was famous.",
            "question": "昔、隣に住んでいた人は（　　）人でした。",
            "translation": "The person who lived next door long ago was a famous person.",
            "options": ["有名な", "有名", "有名だった", "有名で"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "When modifying a noun directly, a な-adjective attaches な (有名 + な + 人).",
                "options": [
                    {"text": "有名な", "isCorrect": True, "reason": "Correct. Pre-noun modification requires な: 有名な人.", "trapCategory": "formation"},
                    {"text": "有名", "isCorrect": False, "reason": "Incorrect. Missing modifier connector な.", "trapCategory": "formation"},
                    {"text": "有名だった", "isCorrect": False, "reason": "Incorrect. While grammatically possible, standard pre-noun attribution uses 有名な人 unless emphasizing that the fame has completely ceased.", "trapCategory": "context"},
                    {"text": "有名で", "isCorrect": False, "reason": "Incorrect. で is clause connector, cannot directly modify following noun.", "trapCategory": "formation"}
                ]
            },
            "hint": "What connector attaches a な-adjective to the noun it modifies?"
        },
        {
            "id": "g1-l9-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Explaining why you arrived late to class: the train was delayed.",
            "question": "電車が遅れました（　　）、遅刻しました。",
            "translation": "Because the train was delayed, I was late.",
            "options": ["から", "けど", "が", "のに"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-kara-reason",
            "grammarPointTitle": "〜から (Stating Reasons / Because - Clause Linker)",
            "explanation": {
                "overall": "から provides the subjective reason or explanation clause: [Reason] から、[Result].",
                "options": [
                    {"text": "から", "isCorrect": True, "reason": "Correct. Explanatory conjunction 'because': [Reason] から.", "trapCategory": "formation"},
                    {"text": "けど", "isCorrect": False, "reason": "Incorrect. けど indicates contrast ('although').", "trapCategory": "meaning"},
                    {"text": "が", "isCorrect": False, "reason": "Incorrect. が indicates contrast.", "trapCategory": "meaning"},
                    {"text": "のに", "isCorrect": False, "reason": "Incorrect. のに indicates contradiction/disappointment.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the reason/cause clause?"
        },
        {
            "id": "g1-l9-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Casual conversation. Asking your friend if yesterday's concert was good.",
            "question": "きのうのコンサート、（　　）？",
            "translation": "Was yesterday's concert good? (Casual past affirmative)",
            "options": ["よかった", "いいだった", "いかった", "よくあった"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "The short past affirmative of the irregular adjective いい is よかった.",
                "options": [
                    {"text": "よかった", "isCorrect": True, "reason": "Correct. Irregular past of いい is よかった.", "trapCategory": "formation"},
                    {"text": "いいだった", "isCorrect": False, "reason": "Incorrect. い-adjectives never take だった.", "trapCategory": "formation"},
                    {"text": "いかった", "isCorrect": False, "reason": "Incorrect. Failing to shift base to yo-.", "trapCategory": "formation"},
                    {"text": "よくあった", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the short past form of the irregular adjective いい?"
        },
        {
            "id": "g1-l9-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Casual peer conversation. Saying that yesterday was not a day off.",
            "question": "きのうは休み（　　）。普通に出勤したよ。",
            "translation": "Yesterday wasn't a day off. I went to work as usual. (Casual short past negative)",
            "options": ["じゃなかった", "じゃないだった", "でなかった", "くないだった"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "The short past negative of a noun or な-adjective is じゃなかった (or ではなかった).",
                "options": [
                    {"text": "じゃなかった", "isCorrect": True, "reason": "Correct. Short past negative for nouns/な-adj is じゃなかった.", "trapCategory": "formation"},
                    {"text": "じゃないだった", "isCorrect": False, "reason": "Incorrect. Ungrammatical concatenation.", "trapCategory": "formation"},
                    {"text": "でなかった", "isCorrect": False, "reason": "Incorrect. Literary fragment, unnatural in casual speech.", "trapCategory": "formation"},
                    {"text": "くないだった", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the casual short past negative form of a noun predicate?"
        },
        {
            "id": "g1-l9-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Relative clause modifying a noun: 'The person who has long hair over there is Mary'.",
            "question": "あそこで髪が（　　）人はメアリーさんです。",
            "translation": "The person over there who has long hair is Mary.",
            "options": ["長い", "長いの", "長くて", "長な"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "い-adjectives directly modify nouns in plain dictionary form: 長い人 (or 髪が長い人).",
                "options": [
                    {"text": "長い", "isCorrect": True, "reason": "Correct. Direct adnominal modification: 長い + 人.", "trapCategory": "formation"},
                    {"text": "長いの", "isCorrect": False, "reason": "Incorrect. い-adjectives do not insert の before nouns.", "trapCategory": "formation"},
                    {"text": "長くて", "isCorrect": False, "reason": "Incorrect. Te-form cannot directly modify a noun head.", "trapCategory": "formation"},
                    {"text": "長な", "isCorrect": False, "reason": "Incorrect. い-adjectives never take な.", "trapCategory": "formation"}
                ]
            },
            "hint": "How does an い-adjective modify a noun in a relative clause?"
        },
        {
            "id": "g1-l9-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 9",
            "type": "multiple-choice",
            "context": "Relative clause with progressive action: 'The student who is reading a book over there'.",
            "question": "あそこで本を（　　）学生は誰ですか。",
            "translation": "Who is the student reading a book over there?",
            "options": ["読んでいる", "読んでいます", "読んだ", "読みます"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-9-13",
            "grammarPointTitle": "過去の普通形・名詞修飾",
            "explanation": {
                "overall": "To modify a noun with an ongoing action, use the short progressive form: 読んでいる + 学生. Polite forms (読んでいます) cannot modify nouns.",
                "options": [
                    {"text": "読んでいる", "isCorrect": True, "reason": "Correct. Short form progressive modifying noun directly.", "trapCategory": "formation"},
                    {"text": "読んでいます", "isCorrect": False, "reason": "Incorrect. Polite -masu forms cannot modify nouns.", "trapCategory": "formation"},
                    {"text": "読んだ", "isCorrect": False, "reason": "Incorrect. Past form implies reading has already finished, not ongoing action 'あそこで'.", "trapCategory": "meaning"},
                    {"text": "読みます", "isCorrect": False, "reason": "Incorrect. Polite form cannot modify noun.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of 〜ている modifies a noun directly in a relative clause?"
        }
    ])

    # ------------------ LESSON 10 ------------------
    exercises.extend([
        {
            "id": "g1-l10-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Comparing two modes of transportation: the bullet train is faster than the bus.",
            "question": "新幹線（　　）バス（　　）速いです。",
            "translation": "The bullet train is faster than the bus.",
            "options": ["のほうが・より", "より・のほうが", "と・と", "が・で"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-10-14",
            "grammarPointTitle": "比較・一番",
            "explanation": {
                "overall": "The comparative construction is: A のほうが B より [Adjective] です (A is more [Adj] than B).",
                "options": [
                    {"text": "のほうが・より", "isCorrect": True, "reason": "Correct. A のほうが B より [Adj] です.", "trapCategory": "formation"},
                    {"text": "より・のほうが", "isCorrect": False, "reason": "Incorrect. Reversing the markers would mean the bus is faster than the bullet train.", "trapCategory": "meaning"},
                    {"text": "と・と", "isCorrect": False, "reason": "Incorrect. と・と is used in comparative questions, not statement comparisons.", "trapCategory": "formation"},
                    {"text": "が・で", "isCorrect": False, "reason": "Incorrect. Ungrammatical comparative markers.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the standard comparative pattern: 'A is more [Adj] than B'?"
        },
        {
            "id": "g1-l10-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Asking a comparison question: which is colder, Russia or Canada?",
            "question": "ロシア（　　）カナダ（　　）どちらが寒いですか。",
            "translation": "Between Russia and Canada, which is colder?",
            "options": ["と・と", "より・より", "のほう・のほう", "や・や"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-10-14",
            "grammarPointTitle": "比較・一番",
            "explanation": {
                "overall": "The comparative question pattern comparing two options is: A と B と どちらが [Adjective] ですか.",
                "options": [
                    {"text": "と・と", "isCorrect": True, "reason": "Correct. Question pattern: A と B と どちらが [Adj] ですか.", "trapCategory": "formation"},
                    {"text": "より・より", "isCorrect": False, "reason": "Incorrect. より means 'than' in comparative statements.", "trapCategory": "formation"},
                    {"text": "のほう・のほう", "isCorrect": False, "reason": "Incorrect. のほう marks the chosen answer side.", "trapCategory": "formation"},
                    {"text": "や・や", "isCorrect": False, "reason": "Incorrect. や is non-exhaustive listing.", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do you frame a question comparing two specific alternatives?"
        },
        {
            "id": "g1-l10-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Stating a superlative: among all four seasons, spring is the most pleasant.",
            "question": "四季（　　）春が（　　）好きです。",
            "translation": "Among the four seasons, I like spring the best.",
            "options": ["の中で・一番", "より・もっと", "と・どちらが", "で・とても"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-10-14",
            "grammarPointTitle": "比較・一番",
            "explanation": {
                "overall": "The superlative construction among 3+ items is: [Category] の中で [Item] が一番 [Adjective] です.",
                "options": [
                    {"text": "の中で・一番", "isCorrect": True, "reason": "Correct. Superlative formula: Category の中で Item が一番 [Adj].", "trapCategory": "formation"},
                    {"text": "より・もっと", "isCorrect": False, "reason": "Incorrect. Comparative markers, not superlative.", "trapCategory": "meaning"},
                    {"text": "と・どちらが", "isCorrect": False, "reason": "Incorrect. どちら is restricted to 2 choices, but seasons are four.", "trapCategory": "formation"},
                    {"text": "で・とても", "isCorrect": False, "reason": "Incorrect. とても means 'very', not 'the most'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the grammatical pattern for superlatives: 'among [category], [item] is the most'?"
        },
        {
            "id": "g1-l10-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Stating personal intent: I plan to go to graduate school next year.",
            "question": "来年、大学院に（　　）つもりです。",
            "translation": "I intend / plan to go to graduate school next year.",
            "options": ["行く", "行きます", "行った", "行きて"],
            "correctIndex": 0,
            "grammarPointId": "g1-l10-tsumori",
            "grammarPointTitle": "〜つもりだ / つもりです (Stated Personal Intention: Plan To)",
            "explanation": {
                "overall": "〜つもりです attaches to the dictionary short form of a verb: V-dict + つもりです.",
                "options": [
                    {"text": "行く", "isCorrect": True, "reason": "Correct. Short form dictionary verb precedes つもりです.", "trapCategory": "formation"},
                    {"text": "行きます", "isCorrect": False, "reason": "Incorrect. Masu-form cannot precede つもりです.", "trapCategory": "formation"},
                    {"text": "行った", "isCorrect": False, "reason": "Incorrect. Past ta-form cannot precede future intention つもり.", "trapCategory": "meaning"},
                    {"text": "行きて", "isCorrect": False, "reason": "Incorrect. Ungrammatical te-form.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of the verb precedes つもりです to state a personal plan?"
        },
        {
            "id": "g1-l10-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Negative personal intention: I plan NOT to buy that expensive computer.",
            "question": "あの高いパソコンは（　　）つもりです。",
            "translation": "I plan not to buy that expensive computer.",
            "options": ["買わない", "買いますない", "買わなかった", "買いてない"],
            "correctIndex": 0,
            "grammarPointId": "g1-l10-tsumori",
            "grammarPointTitle": "〜つもりだ / つもりです (Stated Personal Intention: Plan To)",
            "explanation": {
                "overall": "Negative intention is expressed by: Verb nai-form + つもりです (買わないつもりです).",
                "options": [
                    {"text": "買わない", "isCorrect": True, "reason": "Correct. Nai-form precedes つもりです: 買わないつもりです.", "trapCategory": "formation"},
                    {"text": "買いますない", "isCorrect": False, "reason": "Incorrect. Ungrammatical hybrid.", "trapCategory": "formation"},
                    {"text": "買わなかった", "isCorrect": False, "reason": "Incorrect. Past tense contradicts future intent.", "trapCategory": "meaning"},
                    {"text": "買いてない", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which verb form attaches to つもりです to express an intention not to do something?"
        },
        {
            "id": "g1-l10-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Change of state with い-adjective: the weather became warm in spring.",
            "question": "春になって、（　　）なりました。",
            "translation": "Spring has arrived, and it has become warm.",
            "options": ["暖かく", "暖かいに", "暖かい", "暖か"],
            "correctIndex": 0,
            "grammarPointId": "g1-l10-adj-naru",
            "grammarPointTitle": "形容詞 + なる (Expressing Change of State: To Become)",
            "explanation": {
                "overall": "To express change of state with an い-adjective, drop final い and append く + なる (暖かい -> 暖かくなる / 暖かくなりました).",
                "options": [
                    {"text": "暖かく", "isCorrect": True, "reason": "Correct. い-adjective adverbial rule: -i -> -ku + なりました.", "trapCategory": "formation"},
                    {"text": "暖かいに", "isCorrect": False, "reason": "Incorrect. い-adjectives never take に with なる.", "trapCategory": "formation"},
                    {"text": "暖かい", "isCorrect": False, "reason": "Incorrect. Plain adjective cannot modify verb なりました directly.", "trapCategory": "formation"},
                    {"text": "暖か", "isCorrect": False, "reason": "Incorrect. Bare stem without -ku.", "trapCategory": "formation"}
                ]
            },
            "hint": "How does an い-adjective change before the verb なる (to become)?"
        },
        {
            "id": "g1-l10-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Change of state with な-adjective / noun: Ken practiced hard and became skillful at Japanese.",
            "question": "たくさん練習して、日本語が（　　）なりました。",
            "translation": "I practiced a lot and became good at Japanese.",
            "options": ["上手に", "上手く", "上手な", "上手"],
            "correctIndex": 0,
            "grammarPointId": "g1-l10-adj-naru",
            "grammarPointTitle": "形容詞 + なる (Expressing Change of State: To Become)",
            "explanation": {
                "overall": "For な-adjectives and nouns, change of state attaches に + なる (上手 -> 上手になる / 上手になりました).",
                "options": [
                    {"text": "上手に", "isCorrect": True, "reason": "Correct. な-adjective + に + なりました.", "trapCategory": "formation"},
                    {"text": "上手く", "isCorrect": False, "reason": "Incorrect. -ku is only for い-adjectives; 上手 is a な-adjective.", "trapCategory": "formation"},
                    {"text": "上手な", "isCorrect": False, "reason": "Incorrect. な is for modifying nouns, not verb なる.", "trapCategory": "formation"},
                    {"text": "上手", "isCorrect": False, "reason": "Incorrect. Missing particle に.", "trapCategory": "formation"}
                ]
            },
            "hint": "What particle connects a な-adjective to the verb なる?"
        },
        {
            "id": "g1-l10-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Pronoun substitute の: shopping for sweaters. Looking at a red one vs a black one.",
            "question": "赤いセーターを持っていますから、黒い（　　）を買いたいです。",
            "translation": "I have a red sweater, so I want to buy a black one.",
            "options": ["の", "こと", "もの", "セーターの"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-10-15",
            "grammarPointTitle": "名詞の代わりの「の」",
            "explanation": {
                "overall": "The particle の acts as an indefinite pronoun substitute ('one') to avoid repeating the noun already mentioned (セーター).",
                "options": [
                    {"text": "の", "isCorrect": True, "reason": "Correct. Indefinite pronoun substitute 'one': 黒いの = black one.", "trapCategory": "formation"},
                    {"text": "こと", "isCorrect": False, "reason": "Incorrect. こと refers to intangible matters/concepts, not a physical sweater.", "trapCategory": "meaning"},
                    {"text": "もの", "isCorrect": False, "reason": "Incorrect. While grammatically conceivable, standard conversational Genki I pronoun substitution uses の.", "trapCategory": "context"},
                    {"text": "セーターの", "isCorrect": False, "reason": "Incorrect. Redundant repetition with dangling particle.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which small particle replaces an already-mentioned noun to mean 'the [Adjective] one'?"
        },
        {
            "id": "g1-l10-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Commuting by walking: stating that you go to school on foot every day.",
            "question": "私は毎朝、学校へ（　　）行きます。",
            "translation": "I go to school on foot every morning.",
            "options": ["歩いて", "歩いてで", "歩きで", "歩くで"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-10-16",
            "grammarPointTitle": "どこか・どこにも・で",
            "explanation": {
                "overall": "Genki I Lesson 10 explicitly highlights this exception: while vehicles take で (電車で行く), walking uses the te-form adverb 歩いて行く without particle で.",
                "options": [
                    {"text": "歩いて", "isCorrect": True, "reason": "Correct. Exception rule: 歩いて行く (never *歩いてで行く).", "trapCategory": "formation"},
                    {"text": "歩いてで", "isCorrect": False, "reason": "Incorrect. Explicit textbook trap: do not add で after 歩いて.", "trapCategory": "formation"},
                    {"text": "歩きで", "isCorrect": False, "reason": "Incorrect. Less common noun form; standard textbook expression is 歩いて行きます.", "trapCategory": "formation"},
                    {"text": "歩くで", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Do you use particle で when saying you go somewhere on foot (歩いて)?"
        },
        {
            "id": "g1-l10-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Asking a friend if they went somewhere fun over the weekend.",
            "question": "週末、（　　）行きましたか。",
            "translation": "Did you go somewhere over the weekend?",
            "options": ["どこかへ", "どこにも", "どこへも", "どこが"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-10-16",
            "grammarPointTitle": "どこか・どこにも・で",
            "explanation": {
                "overall": "どこか ('somewhere') can take へ or drop it (どこかへ行きましたか). どこにも requires a negative verb.",
                "options": [
                    {"text": "どこかへ", "isCorrect": True, "reason": "Correct. Indefinite destination 'somewhere' in affirmative question.", "trapCategory": "meaning"},
                    {"text": "どこにも", "isCorrect": False, "reason": "Incorrect. どこにも requires a negative verb (どこにも行きませんでした).", "trapCategory": "formation"},
                    {"text": "どこへも", "isCorrect": False, "reason": "Incorrect. どこへも requires negative verb.", "trapCategory": "formation"},
                    {"text": "どこが", "isCorrect": False, "reason": "Incorrect. Interrogative subject, not destination.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which phrase means 'to somewhere' in an affirmative question?"
        },
        {
            "id": "g1-l10-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Responding that you stayed home all weekend and went nowhere.",
            "question": "雨が降っていましたから、（　　）行きませんでした。",
            "translation": "Because it was raining, I did not go anywhere.",
            "options": ["どこにも", "どこかに", "どこかへ", "どこでも"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-10-16",
            "grammarPointTitle": "どこか・どこにも・で",
            "explanation": {
                "overall": "Total negative destination: どこにも (or どこへも) + negative verb ('nowhere / not anywhere').",
                "options": [
                    {"text": "どこにも", "isCorrect": True, "reason": "Correct. Total negation for destination: どこにも + negative verb.", "trapCategory": "formation"},
                    {"text": "どこかに", "isCorrect": False, "reason": "Incorrect. どこか is used with affirmative predicates.", "trapCategory": "meaning"},
                    {"text": "どこかへ", "isCorrect": False, "reason": "Incorrect. Pairs with affirmative predicates.", "trapCategory": "meaning"},
                    {"text": "どこでも", "isCorrect": False, "reason": "Incorrect. どこでも means 'anywhere' (e.g. どこでもいい).", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which word combines with a negative verb to mean 'not anywhere / nowhere'?"
        },
        {
            "id": "g1-l10-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 10",
            "type": "multiple-choice",
            "context": "Change of state to a profession: Ken studied medicine and became a doctor.",
            "question": "けんさんは医者（　　）なりました。",
            "translation": "Ken became a doctor.",
            "options": ["に", "で", "を", "と"],
            "correctIndex": 0,
            "grammarPointId": "g1-l10-adj-naru",
            "grammarPointTitle": "形容詞 + なる (Expressing Change of State: To Become)",
            "explanation": {
                "overall": "When a noun becomes something (change of role/profession), it attaches に to なる: Noun + になる (医者になる).",
                "options": [
                    {"text": "に", "isCorrect": True, "reason": "Correct. Noun + に + なりました.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で does not mark the target state of なる.", "trapCategory": "meaning"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. なる is an intransitive verb, cannot take direct object を.", "trapCategory": "formation"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. となる is literary/formal, standard Genki I grammar uses になる.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle marks the resulting profession or status with the verb なる?"
        }
    ])

    # ------------------ LESSON 11 ------------------
    exercises.extend([
        {
            "id": "g1-l11-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Stating personal desire: I want to go to Kyoto this summer.",
            "question": "今年の夏、京都へ（　　）です。",
            "translation": "I want to go to Kyoto this summer.",
            "options": ["行きたい", "行きたがる", "行きてたい", "行くたい"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-tai-desire",
            "grammarPointTitle": "〜たい / 〜たくない (Expressing Desire to Do: Want to Do)",
            "explanation": {
                "overall": "Desiderative 〜たい attaches to the verb stem (drop -masu): 行く -> 行き -> 行きたいです.",
                "options": [
                    {"text": "行きたい", "isCorrect": True, "reason": "Correct. Verb stem + たいです.", "trapCategory": "formation"},
                    {"text": "行きたがる", "isCorrect": False, "reason": "Incorrect. 〜たがる is used for third-person desires, not first-person.", "trapCategory": "context"},
                    {"text": "行きてたい", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach たい.", "trapCategory": "formation"},
                    {"text": "行くたい", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach たい.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of the verb attaches to たいです to express desire?"
        },
        {
            "id": "g1-l11-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Negative personal desire: feeling nauseous, so you do not want to eat anything right now.",
            "question": "気分が悪いですから、何も（　　）。",
            "translation": "Because I feel sick, I don't want to eat anything.",
            "options": ["食べたくないです", "食べたいじゃないです", "食べたくないでした", "食べないたいです"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-tai-desire",
            "grammarPointTitle": "〜たい / 〜たくない (Expressing Desire to Do: Want to Do)",
            "explanation": {
                "overall": "〜たい conjugates exactly like an い-adjective: negative is 〜たくないです (or 〜たくありません).",
                "options": [
                    {"text": "食べたくないです", "isCorrect": True, "reason": "Correct. Negative desiderative: -tai -> -takunai desu.", "trapCategory": "formation"},
                    {"text": "食べたいじゃないです", "isCorrect": False, "reason": "Incorrect. 〜たい is an い-adjective type ending, cannot take じゃないです.", "trapCategory": "formation"},
                    {"text": "食べたくないでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical hybrid past.", "trapCategory": "formation"},
                    {"text": "食べないたいです", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "How does the desiderative ending 〜たい conjugate into negative?"
        },
        {
            "id": "g1-l11-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Describing past desire: when I was a child, I wanted to become a pianist.",
            "question": "子どもの時、ピアニストになり（　　）。",
            "translation": "When I was a child, I wanted to become a pianist.",
            "options": ["たかったです", "たいでした", "たいだった", "たかったでした"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-tai-desire",
            "grammarPointTitle": "〜たい / 〜たくない (Expressing Desire to Do: Want to Do)",
            "explanation": {
                "overall": "Past affirmative of 〜たい follows い-adjective rules: drop い and append かったです -> 〜たかったです.",
                "options": [
                    {"text": "たかったです", "isCorrect": True, "reason": "Correct. Past affirmative desiderative: -tai -> -takatta desu.", "trapCategory": "formation"},
                    {"text": "たいでした", "isCorrect": False, "reason": "Incorrect. でした cannot attach directly to -tai.", "trapCategory": "formation"},
                    {"text": "たいだった", "isCorrect": False, "reason": "Incorrect. だった cannot attach directly to -tai.", "trapCategory": "formation"},
                    {"text": "たかったでした", "isCorrect": False, "reason": "Incorrect. Redundant past markers.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the past affirmative form of the desiderative ending 〜たい?"
        },
        {
            "id": "g1-l11-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Thirsty after running: wanting to drink cold water.",
            "question": "喉が渇きました。冷たい水（　　）飲みたいです。",
            "translation": "I am thirsty. I want to drink cold water.",
            "options": ["が", "に", "で", "へ"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-tai-desire",
            "grammarPointTitle": "〜たい / 〜たくない (Expressing Desire to Do: Want to Do)",
            "explanation": {
                "overall": "In 〜たい sentences, the direct object particle を is frequently replaced by が, emphasizing the desired target.",
                "options": [
                    {"text": "が", "isCorrect": True, "reason": "Correct. Object of 〜たい can take が (or を).", "trapCategory": "formation"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に cannot mark the object of drinking.", "trapCategory": "meaning"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で does not mark target of desire.", "trapCategory": "meaning"},
                    {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ marks direction of movement.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle can replace を to mark the target of desire in 〜たい sentences?"
        },
        {
            "id": "g1-l11-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Describing a third person's desire: Mary wants to go to a hot spring.",
            "question": "メアリーさんは温泉に行き（　　）。",
            "translation": "Mary wants to go to a hot spring. (Describing third-person desire)",
            "options": ["たがっています", "たいです", "たいでした", "たがるでした"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-tai-desire",
            "grammarPointTitle": "〜たい / 〜たくない (Expressing Desire to Do: Want to Do)",
            "explanation": {
                "overall": "Genki I explicitly teaches that 〜たいです is reserved for the speaker's own internal feelings. For third persons, Japanese uses 〜たがっています (or 〜たいと言っています).",
                "options": [
                    {"text": "たがっています", "isCorrect": True, "reason": "Correct. Third-person desire construction: V-stem + たがっている.", "trapCategory": "context"},
                    {"text": "たいです", "isCorrect": False, "reason": "Incorrect. Direct 〜たいです cannot describe a third person's internal psychological state in standard Japanese.", "trapCategory": "context"},
                    {"text": "たいでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical formation.", "trapCategory": "formation"},
                    {"text": "たがるでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What construction is used to describe a third person's desire?"
        },
        {
            "id": "g1-l11-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Asking about past lifetime experience: have you ever climbed Mt. Fuji?",
            "question": "富士山に登っ（　　）ことがありますか。",
            "translation": "Have you ever climbed Mt. Fuji?",
            "options": ["た", "て", "る", "ます"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-koto-ga-aru",
            "grammarPointTitle": "〜ことがある (Past Experiential Aspect: Have Ever Done)",
            "explanation": {
                "overall": "The experiential pattern 'have done before' is: Verb ta-form + ことがある (登ったことがある).",
                "options": [
                    {"text": "た", "isCorrect": True, "reason": "Correct. Formula: Verb ta-form + ことがある.", "trapCategory": "formation"},
                    {"text": "て", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede ことがある.", "trapCategory": "formation"},
                    {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form with ことがある means 'it sometimes happens', not past experience.", "trapCategory": "meaning"},
                    {"text": "ます", "isCorrect": False, "reason": "Incorrect. Masu-form cannot precede ことがある.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form precedes ことがある to express past life experience?"
        },
        {
            "id": "g1-l11-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Stating that you have never once eaten horsemeat sashimi in your life.",
            "question": "一度も馬刺しを食べ（　　）。",
            "translation": "I have never once eaten horsemeat sashimi.",
            "options": ["たことがありません", "ませんでした", "ていません", "ないことがありました"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-koto-ga-aru",
            "grammarPointTitle": "〜ことがある (Past Experiential Aspect: Have Ever Done)",
            "explanation": {
                "overall": "To state that one has never had a specific lifetime experience, use: Verb ta-form + ことがありません (paired with 一度も).",
                "options": [
                    {"text": "たことがありません", "isCorrect": True, "reason": "Correct. Experiential negation: V-ta + ことがありません.", "trapCategory": "formation"},
                    {"text": "ませんでした", "isCorrect": False, "reason": "Incorrect. Simple past negative does not explicitly express lifetime experiential aspect.", "trapCategory": "meaning"},
                    {"text": "ていません", "isCorrect": False, "reason": "Incorrect. 〜ていません expresses unfinished recent actions, not lifetime absence of experience.", "trapCategory": "meaning"},
                    {"text": "ないことがありました", "isCorrect": False, "reason": "Incorrect. Means 'there were times when I didn't eat'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do you express that you have never once had a certain experience?"
        },
        {
            "id": "g1-l11-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Listing non-exhaustive weekend activities: doing things like cleaning and doing laundry.",
            "question": "休みの日は、掃除をし（　　）洗濯をし（　　）します。",
            "translation": "On my days off, I do things like cleaning and doing laundry.",
            "options": ["たり・たり", "て・て", "たら・たら", "と・と"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-11-17",
            "grammarPointTitle": "〜たり〜たりする・や",
            "explanation": {
                "overall": "Listing activities as illustrative examples among others uses: Verb-ta + り + Verb-ta + りする (〜たり〜たりする).",
                "options": [
                    {"text": "たり・たり", "isCorrect": True, "reason": "Correct. Illustrative action listing: 〜たり〜たりする.", "trapCategory": "formation"},
                    {"text": "て・て", "isCorrect": False, "reason": "Incorrect. 〜て〜て implies an exhaustive chronological sequence of events.", "trapCategory": "meaning"},
                    {"text": "たら・たら", "isCorrect": False, "reason": "Incorrect. 〜たら is conditional 'if/when'.", "trapCategory": "formation"},
                    {"text": "と・と", "isCorrect": False, "reason": "Incorrect. と connects nouns, not verbs.", "trapCategory": "formation"}
                ]
            },
            "hint": "What pattern lists activities as representative examples among others?"
        },
        {
            "id": "g1-l11-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Stating that yesterday you did things like watching movies and reading books. Tense placement.",
            "question": "きのうは映画を見たり本を読んだり（　　）。",
            "translation": "Yesterday I did things like watching movies and reading books.",
            "options": ["しました", "します", "していた", "するでした"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-11-17",
            "grammarPointTitle": "〜たり〜たりする・や",
            "explanation": {
                "overall": "In 〜たり〜たりする, the tense of the entire sentence is carried exclusively by the final auxiliary verb する (past = しました).",
                "options": [
                    {"text": "しました", "isCorrect": True, "reason": "Correct. Final verb carries sentence tense: きのう -> しました.", "trapCategory": "formation"},
                    {"text": "します", "isCorrect": False, "reason": "Incorrect. Present tense contradicts 'きのう'.", "trapCategory": "meaning"},
                    {"text": "していた", "isCorrect": False, "reason": "Incorrect. Casual progressive past, inconsistent with polite predicate.", "trapCategory": "context"},
                    {"text": "するでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Where and how is the sentence tense marked in the 〜たり〜たりする pattern?"
        },
        {
            "id": "g1-l11-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Non-exhaustive listing of items purchased: bought things like apples and bananas.",
            "question": "スーパーでりんご（　　）バナナなどを買いました。",
            "translation": "I bought things like apples and bananas at the supermarket.",
            "options": ["や", "と", "も", "で"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-11-17",
            "grammarPointTitle": "〜たり〜たりする・や",
            "explanation": {
                "overall": "The particle や connects nouns in a non-exhaustive list ('things like A and B, among others'). Frequently paired with など.",
                "options": [
                    {"text": "や", "isCorrect": True, "reason": "Correct. Non-exhaustive noun connector: A や B など.", "trapCategory": "formation"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. と lists nouns exhaustively and clashes with など.", "trapCategory": "meaning"},
                    {"text": "も", "isCorrect": False, "reason": "Incorrect. も means 'also', does not form non-exhaustive list.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で cannot coordinate nouns.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle lists nouns non-exhaustively ('things like A and B')?"
        },
        {
            "id": "g1-l11-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Stating that you went to Kyoto and visited temples, shrines, etc.",
            "question": "京都でお寺（　　）神社を見学しました。",
            "translation": "In Kyoto, I toured temples and shrines (and other sights).",
            "options": ["や", "と", "に", "を"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-11-17",
            "grammarPointTitle": "〜たり〜たりする・や",
            "explanation": {
                "overall": "や indicates that temples and shrines are representative examples of the many historical places visited.",
                "options": [
                    {"text": "や", "isCorrect": True, "reason": "Correct. Non-exhaustive listing particle.", "trapCategory": "formation"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. と would mean only temples and shrines were seen and nothing else.", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に cannot connect two nouns.", "trapCategory": "formation"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. を connects only the full object phrase to the verb.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle indicates an open, non-exhaustive list of items?"
        },
        {
            "id": "g1-l11-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 11",
            "type": "multiple-choice",
            "context": "Conjugating U-verb 泳ぐ into past experiential form: have ever swum in the ocean.",
            "question": "海で（　　）ことがありますか。",
            "translation": "Have you ever swum in the ocean?",
            "options": ["泳いだ", "泳ぎた", "泳いで", "泳ぐ"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-koto-ga-aru",
            "grammarPointTitle": "〜ことがある (Past Experiential Aspect: Have Ever Done)",
            "explanation": {
                "overall": "泳ぐ ends in ぐ, so its ta-form is voiced: 泳いだ -> 泳いだことがありますか.",
                "options": [
                    {"text": "泳いだ", "isCorrect": True, "reason": "Correct. Voiced ta-form of 泳ぐ is 泳いだ.", "trapCategory": "formation"},
                    {"text": "泳ぎた", "isCorrect": False, "reason": "Incorrect. Unassimilated stem error.", "trapCategory": "formation"},
                    {"text": "泳いで", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede ことがある.", "trapCategory": "formation"},
                    {"text": "泳ぐ", "isCorrect": False, "reason": "Incorrect. Dictionary form expresses habit, not past life experience.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the past ta-form of the verb 泳ぐ?"
        }
    ])

    # ------------------ LESSON 12 ------------------
    exercises.extend([
        {
            "id": "g1-l12-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Giving strong advice to a sick friend: 'You had better go to the hospital'.",
            "question": "早く病院へ（　　）ほうがいいですよ。",
            "translation": "You had better go to the hospital early.",
            "options": ["行った", "行く", "行きます", "行って"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-12-19",
            "grammarPointTitle": "〜ほうがいい",
            "explanation": {
                "overall": "Affirmative advice uses the past ta-form before ほうがいい: Verb ta-form + ほうがいいです (行ったほうがいい).",
                "options": [
                    {"text": "行った", "isCorrect": True, "reason": "Correct. Affirmative advice rule: Verb ta-form + ほうがいい.", "trapCategory": "formation"},
                    {"text": "行く", "isCorrect": False, "reason": "Incorrect. Using dictionary form sounds more like a general comparison than personal advice in Genki I grammar.", "trapCategory": "formation"},
                    {"text": "行きます", "isCorrect": False, "reason": "Incorrect. Masu-form cannot precede ほうがいい.", "trapCategory": "formation"},
                    {"text": "行って", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede ほうがいい.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form precedes ほうがいいです for affirmative advice?"
        },
        {
            "id": "g1-l12-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Giving negative advice: 'You had better not stay up late tonight'.",
            "question": "今晩は夜更かしを（　　）ほうがいいです。",
            "translation": "You had better not stay up late tonight.",
            "options": ["しない", "しなかった", "するない", "しなくて"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-12-19",
            "grammarPointTitle": "〜ほうがいい",
            "explanation": {
                "overall": "Negative advice uses the present negative nai-form before ほうがいい: Verb nai-form + ほうがいいです (しないほうがいい).",
                "options": [
                    {"text": "しない", "isCorrect": True, "reason": "Correct. Negative advice rule: Verb nai-form + ほうがいい.", "trapCategory": "formation"},
                    {"text": "しなかった", "isCorrect": False, "reason": "Incorrect. Overgeneralizing past ta-form to negative (*しなかったほうがいい) is a common error; negative advice takes present nai-form.", "trapCategory": "formation"},
                    {"text": "するない", "isCorrect": False, "reason": "Incorrect. Ungrammatical stem.", "trapCategory": "formation"},
                    {"text": "しなくて", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede ほうがいい.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form precedes ほうがいいです for negative advice?"
        },
        {
            "id": "g1-l12-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Explaining the background reason for missing class: 'The truth is, I have a fever'.",
            "question": "熱が（　　）んです。",
            "translation": "The thing is, I have a fever. (Explanatory mode)",
            "options": ["ある", "あります", "あった", "あり"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-12-18",
            "grammarPointTitle": "〜んです",
            "explanation": {
                "overall": "The explanatory 〜んです attaches to the short plain form of verbs: V-dict + んです (あるんです).",
                "options": [
                    {"text": "ある", "isCorrect": True, "reason": "Correct. Verb short form + んです.", "trapCategory": "formation"},
                    {"text": "あります", "isCorrect": False, "reason": "Incorrect. Polite masu-form cannot precede んです.", "trapCategory": "formation"},
                    {"text": "あった", "isCorrect": False, "reason": "Incorrect. Past tense implies the fever is already gone.", "trapCategory": "meaning"},
                    {"text": "あり", "isCorrect": False, "reason": "Incorrect. Bare stem cannot attach んです.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of the verb precedes the explanatory ending 〜んです?"
        },
        {
            "id": "g1-l12-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Explaining background condition with a な-adjective: 'Because I am free today'.",
            "question": "今日は（　　）んです。",
            "translation": "The thing is, I am free today.",
            "options": ["暇な", "暇だ", "暇", "暇の"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-12-18",
            "grammarPointTitle": "〜んです",
            "explanation": {
                "overall": "Before 〜んです, な-adjectives and nouns require な (NOT だ): 暇な + んです / 病気な + んです.",
                "options": [
                    {"text": "暇な", "isCorrect": True, "reason": "Correct. な-adjectives and nouns insert な before んです.", "trapCategory": "formation"},
                    {"text": "暇だ", "isCorrect": False, "reason": "Incorrect. Major learner trap: だ changes to な before んです (never *暇なんです with だ).", "trapCategory": "formation"},
                    {"text": "暇", "isCorrect": False, "reason": "Incorrect. Missing connector な.", "trapCategory": "formation"},
                    {"text": "暇の", "isCorrect": False, "reason": "Incorrect. の cannot replace な before んです.", "trapCategory": "formation"}
                ]
            },
            "hint": "What connector do な-adjectives take immediately before 〜んです?"
        },
        {
            "id": "g1-l12-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Noticing a friend dressed in a formal suit and inquiring about the reason.",
            "question": "どうしてスーツを着ている（　　）。",
            "translation": "Why is it that you are wearing a suit?",
            "options": ["んですか", "ますか", "のです", "んです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-12-18",
            "grammarPointTitle": "〜んです",
            "explanation": {
                "overall": "〜んですか is used when asking for an explanation based on an observed situation (seeing the suit).",
                "options": [
                    {"text": "んですか", "isCorrect": True, "reason": "Correct. Seeking explanation for an observed situation: 〜んですか.", "trapCategory": "context"},
                    {"text": "ますか", "isCorrect": False, "reason": "Incorrect. Simple factual inquiry lacks the curiosity/contextual inquiry nuance.", "trapCategory": "context"},
                    {"text": "のです", "isCorrect": False, "reason": "Incorrect. Statement form, missing question marker か.", "trapCategory": "formation"},
                    {"text": "んです", "isCorrect": False, "reason": "Incorrect. Missing question marker か.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which ending is used when asking someone to explain the reason behind what you observe?"
        },
        {
            "id": "g1-l12-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Stomachache after dinner: 'I ate too much food'.",
            "question": "晩ご飯を（　　）しまいました。",
            "translation": "I ended up eating too much for dinner.",
            "options": ["食べすぎて", "食べるすぎて", "食べたすぎて", "食べりすぎて"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-sugiru",
            "grammarPointTitle": "〜すぎる (Excessiveness: Too Much / Overdoing)",
            "explanation": {
                "overall": "〜すぎる attaches to the verb stem (drop -masu): 食べる -> 食べ + すぎる -> 食べすぎました / 食べすぎてしまいました.",
                "options": [
                    {"text": "食べすぎて", "isCorrect": True, "reason": "Correct. Verb stem + すぎて.", "trapCategory": "formation"},
                    {"text": "食べるすぎて", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach すぎる.", "trapCategory": "formation"},
                    {"text": "食べたすぎて", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach すぎる.", "trapCategory": "formation"},
                    {"text": "食べりすぎて", "isCorrect": False, "reason": "Incorrect. Ungrammatical stem.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form attaches to the excessiveness suffix 〜すぎる?"
        },
        {
            "id": "g1-l12-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Looking at a price tag on a coat: 'This is too expensive'.",
            "question": "このコートは（　　）ますね。",
            "translation": "This coat is too expensive, isn't it?",
            "options": ["高すぎ", "高いすぎ", "高くてすぎ", "高かったすぎ"],
            "correctIndex": 0,
            "grammarPointId": "g1-l11-sugiru",
            "grammarPointTitle": "〜すぎる (Excessiveness: Too Much / Overdoing)",
            "explanation": {
                "overall": "For い-adjectives, drop final い and attach すぎる: 高い -> 高 + すぎます -> 高すぎます.",
                "options": [
                    {"text": "高すぎ", "isCorrect": True, "reason": "Correct. い-adjective stem (drop -i) + すぎます.", "trapCategory": "formation"},
                    {"text": "高いすぎ", "isCorrect": False, "reason": "Incorrect. Failing to drop final い.", "trapCategory": "formation"},
                    {"text": "高くてすぎ", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach すぎる.", "trapCategory": "formation"},
                    {"text": "高かったすぎ", "isCorrect": False, "reason": "Incorrect. Past form cannot attach すぎる.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you attach 〜すぎる to an い-adjective like 高い?"
        },
        {
            "id": "g1-l12-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Stating strict obligation: I must take my medicine after meals.",
            "question": "毎食後、薬を飲ま（　　）。",
            "translation": "I must take medicine after every meal.",
            "options": ["なければいけません", "てもいいです", "てください", "たいです"],
            "correctIndex": 0,
            "grammarPointId": "g1-l12-nakereba-ikemasen",
            "grammarPointTitle": "〜なければいけません / なきゃいけません (Obligation: Must Do / Have to Do)",
            "explanation": {
                "overall": "The standard grammatical pattern for obligation ('must / have to') is: Verb nai-stem + なければいけません (飲む -> 飲ま -> 飲まなければいけません).",
                "options": [
                    {"text": "なければいけません", "isCorrect": True, "reason": "Correct. Obligation formula: -nakereba ikemasen.", "trapCategory": "formation"},
                    {"text": "てもいいです", "isCorrect": False, "reason": "Incorrect. Expresses permission ('you may'), not obligation.", "trapCategory": "meaning"},
                    {"text": "てください", "isCorrect": False, "reason": "Incorrect. Request directed at another person.", "trapCategory": "meaning"},
                    {"text": "たいです", "isCorrect": False, "reason": "Incorrect. Personal desire ('I want to take medicine').", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the standard polite grammatical ending for 'must do / have to do'?"
        },
        {
            "id": "g1-l12-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Casual conversation between friends about obligations: 'I have to return home soon'.",
            "question": "もうすぐ帰ら（　　）。",
            "translation": "I have to head home soon. (Casual spoken obligation)",
            "options": ["なきゃ", "なくて", "ないで", "なければ"],
            "correctIndex": 0,
            "grammarPointId": "g1-l12-nakereba-ikemasen",
            "grammarPointTitle": "〜なければいけません / なきゃいけません (Obligation: Must Do / Have to Do)",
            "explanation": {
                "overall": "In casual everyday speech, 〜なければいけません is frequently contracted to 〜なきゃ (or 〜なくちゃ).",
                "options": [
                    {"text": "なきゃ", "isCorrect": True, "reason": "Correct. Casual spoken contraction of obligation: 〜なきゃ.", "trapCategory": "context"},
                    {"text": "なくて", "isCorrect": False, "reason": "Incorrect. 〜なくて is causal te-form, does not express obligation by itself.", "trapCategory": "formation"},
                    {"text": "ないで", "isCorrect": False, "reason": "Incorrect. Negative request fragment ('without doing').", "trapCategory": "meaning"},
                    {"text": "なければ", "isCorrect": False, "reason": "Incorrect. Dangling conditional 'if I don't', incomplete without predicate.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the common casual contraction for 'I gotta / I must'?"
        },
        {
            "id": "g1-l12-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Giving an objective cause: 'Because it is raining heavily, I will take a taxi'.",
            "question": "雨がひどく降っている（　　）、タクシーで行きます。",
            "translation": "Because it is raining heavily, I will go by taxi.",
            "options": ["ので", "のに", "ても", "ながら"],
            "correctIndex": 0,
            "grammarPointId": "g1-l12-node-objective-reason",
            "grammarPointTitle": "〜ので (Reason / Background Circumstance)",
            "explanation": {
                "overall": "〜ので gives an objective, polite cause or circumstance explaining the speaker's action.",
                "options": [
                    {"text": "ので", "isCorrect": True, "reason": "Correct. Objective reason connective: Short form + ので.", "trapCategory": "formation"},
                    {"text": "のに", "isCorrect": False, "reason": "Incorrect. のに expresses disappointed contrast ('even though').", "trapCategory": "meaning"},
                    {"text": "ても", "isCorrect": False, "reason": "Incorrect. ても expresses concession ('even if').", "trapCategory": "meaning"},
                    {"text": "ながら", "isCorrect": False, "reason": "Incorrect. ながら expresses simultaneous action ('while doing').", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which connective particle provides an objective, polite explanation for an action?"
        },
        {
            "id": "g1-l12-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Forming 〜ので with a noun predicate: 'Because tomorrow is Sunday, the bank is closed'.",
            "question": "明日は日曜日（　　）ので、銀行は休みです。",
            "translation": "Because tomorrow is Sunday, the bank is closed.",
            "options": ["な", "だ", "の", "である"],
            "correctIndex": 0,
            "grammarPointId": "g1-l12-node-objective-reason",
            "grammarPointTitle": "〜ので (Reason / Background Circumstance)",
            "explanation": {
                "overall": "Before 〜ので, nouns and な-adjectives must attach な (日曜日 + な + ので). They cannot take だ.",
                "options": [
                    {"text": "な", "isCorrect": True, "reason": "Correct. Nouns and な-adjectives take な before ので (Noun + なので).", "trapCategory": "formation"},
                    {"text": "だ", "isCorrect": False, "reason": "Incorrect. Major grammar trap: *だので does not exist in standard Japanese.", "trapCategory": "formation"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. *のので is ungrammatical.", "trapCategory": "formation"},
                    {"text": "である", "isCorrect": False, "reason": "Incorrect. Formal written style, unnatural in standard Genki I discourse.", "trapCategory": "context"}
                ]
            },
            "hint": "What particle connects a noun to the reason connective ので?"
        },
        {
            "id": "g1-l12-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 12",
            "type": "multiple-choice",
            "context": "Looking at dark gray clouds: predicting that it will probably rain this afternoon.",
            "question": "午後は雨が降る（　　）。傘を持っていきましょう。",
            "translation": "It will probably rain this afternoon. Let's take an umbrella.",
            "options": ["でしょう", "でした", "です", "ます"],
            "correctIndex": 0,
            "grammarPointId": "g1-l12-deshou-darou",
            "grammarPointTitle": "〜でしょう / 〜だろう (Conjecture & Probability: Probably)",
            "explanation": {
                "overall": "〜でしょう (short form だろう) expresses probability or conjecture ('probably'). It attaches to verb short forms.",
                "options": [
                    {"text": "でしょう", "isCorrect": True, "reason": "Correct. Expresses probability/conjecture: V-short + でしょう.", "trapCategory": "meaning"},
                    {"text": "でした", "isCorrect": False, "reason": "Incorrect. Past copula, contradicts future prediction '午後'.", "trapCategory": "meaning"},
                    {"text": "です", "isCorrect": False, "reason": "Incorrect. Verb cannot attach です directly without nominalization.", "trapCategory": "formation"},
                    {"text": "ます", "isCorrect": False, "reason": "Incorrect. Plain verb cannot attach ます directly.", "trapCategory": "formation"}
                ]
            },
            "hint": "What ending expresses probability or polite conjecture ('probably')?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_exercises_l7_to_l12()
    print(f"Generated {len(ex_list)} exercises across Lessons 7 to 12.")
    
    with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)
    
    # Filter out any existing L7-L12
    kept = [x for x in existing if not any(f"Lesson {i}" == x['chapter'] for i in range(7, 13))]
    combined = kept + ex_list
    
    with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(combined)} exercises to c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json")
