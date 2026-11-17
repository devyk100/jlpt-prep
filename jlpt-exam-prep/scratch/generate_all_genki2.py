import json

def get_all_genki2_exercises():
    # Load L13 and L14 already created
    import generate_genki2_exercises as g2_part1
    exercises = g2_part1.get_genki2_exercises()

    # ==================== LESSON 15 ====================
    exercises.extend([
        {
            "id": "g2-l15-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Casual suggestion to a friend: 'Let's go together!'. U-verb 行く.",
            "question": "一緒に（　　）！",
            "translation": "Let's go together! (Casual volitional)",
            "options": ["行こう", "行きましょう", "行こうよ", "行った"],
            "correctIndex": 0,
            "grammarPointId": "g2-l15-volitional-form",
            "grammarPointTitle": "意向形 (The Volitional Form: Casual Let's Do / Self-Resolve)",
            "explanation": {
                "overall": "U-verb volitional form: change final -u to -o and append う (行く -> 行こう).",
                "options": [
                    {"text": "行こう", "isCorrect": True, "reason": "Correct. U-verb volitional: ku -> kou.", "trapCategory": "formation"},
                    {"text": "行きましょう", "isCorrect": False, "reason": "Incorrect. Polite volitional form, not casual short form.", "trapCategory": "context"},
                    {"text": "行こうよ", "isCorrect": False, "reason": "Incorrect. Extra particle よ alters the basic base form.", "trapCategory": "formation"},
                    {"text": "行った", "isCorrect": False, "reason": "Incorrect. Past tense.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the casual volitional form (意向形) of the U-verb 行く?"
        },
        {
            "id": "g2-l15-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Ru-verb volitional form: 食べる -> 'Let's eat lunch'.",
            "question": "昼ご飯を（　　）。",
            "translation": "Let's eat lunch. (Casual volitional)",
            "options": ["食べよう", "食べろう", "食べようか", "食べた"],
            "correctIndex": 0,
            "grammarPointId": "g2-l15-volitional-form",
            "grammarPointTitle": "意向形 (The Volitional Form: Casual Let's Do / Self-Resolve)",
            "explanation": {
                "overall": "Ru-verb volitional form: drop final -ru and append -you (食べる -> 食べよう).",
                "options": [
                    {"text": "食べよう", "isCorrect": True, "reason": "Correct. Ru-verb volitional: drop -ru and add -you.", "trapCategory": "formation"},
                    {"text": "食べろう", "isCorrect": False, "reason": "Incorrect. Overgeneralizing U-verb rule.", "trapCategory": "formation"},
                    {"text": "食べようか", "isCorrect": False, "reason": "Incorrect. Question form ('Shall we eat?').", "trapCategory": "meaning"},
                    {"text": "食べた", "isCorrect": False, "reason": "Incorrect. Past tense.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the volitional form of the Ru-verb 食べる?"
        },
        {
            "id": "g2-l15-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Irregular verb volitional: する and くる.",
            "question": "今晩、宿題を（　　）。",
            "translation": "Let's do our homework tonight. / I'll do homework tonight.",
            "options": ["しよう", "すよう", "そう", "しろう"],
            "correctIndex": 0,
            "grammarPointId": "g2-l15-volitional-form",
            "grammarPointTitle": "意向形 (The Volitional Form: Casual Let's Do / Self-Resolve)",
            "explanation": {
                "overall": "The volitional form of irregular verb する is しよう.",
                "options": [
                    {"text": "しよう", "isCorrect": True, "reason": "Correct. Irregular volitional of する is しよう.", "trapCategory": "formation"},
                    {"text": "すよう", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "そう", "isCorrect": False, "reason": "Incorrect. Ungrammatical stem.", "trapCategory": "formation"},
                    {"text": "しろう", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the volitional form of する?"
        },
        {
            "id": "g2-l15-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Firm ongoing intention: I have been thinking of studying abroad in Japan.",
            "question": "日本に留学し（　　）と思っています。",
            "translation": "I have been thinking of studying abroad in Japan.",
            "options": ["よう", "ます", "た", "る"],
            "correctIndex": 0,
            "grammarPointId": "g2-l15-volitional-to-omotte-iru",
            "grammarPointTitle": "意向形 + と思っている (Firm Ongoing Determination: Intending To)",
            "explanation": {
                "overall": "The pattern for an ongoing intention considered over time is: Volitional form + と思っている (留学しようと思っています).",
                "options": [
                    {"text": "よう", "isCorrect": True, "reason": "Correct. Volitional form + と思っています expresses ongoing resolve.", "trapCategory": "formation"},
                    {"text": "ます", "isCorrect": False, "reason": "Incorrect. Masu-form cannot precede と思っています.", "trapCategory": "formation"},
                    {"text": "た", "isCorrect": False, "reason": "Incorrect. Past ta-form with と思っています implies past belief, not future intent.", "trapCategory": "meaning"},
                    {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form expresses casual conjecture, not volitional intent.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which verb form attaches to と思っています to express firm ongoing intention?"
        },
        {
            "id": "g2-l15-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Spontaneous decision on the spot: 'I think I will buy a drink'.",
            "question": "喉が渇いたから、ジュースを買いに行（　　）と思います。",
            "translation": "I'm thirsty, so I think I'll go buy some juice. (Decision made just now)",
            "options": ["こう", "く", "きました", "かない"],
            "correctIndex": 0,
            "grammarPointId": "g2-l15-volitional-to-omotte-iru",
            "grammarPointTitle": "意向形 + と思っている (Firm Ongoing Determination: Intending To)",
            "explanation": {
                "overall": "Volitional + と思う (non-progressive) denotes a decision made on the spot at the moment of speaking.",
                "options": [
                    {"text": "こう", "isCorrect": True, "reason": "Correct. Volitional 行こう + と思います denotes decision made right now.", "trapCategory": "context"},
                    {"text": "く", "isCorrect": False, "reason": "Incorrect. 行くと思います means 'I think someone will go', not personal resolution.", "trapCategory": "meaning"},
                    {"text": "きました", "isCorrect": False, "reason": "Incorrect. Past tense.", "trapCategory": "meaning"},
                    {"text": "かない", "isCorrect": False, "reason": "Incorrect. Negative.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What form precedes と思います for an immediate personal decision?"
        },
        {
            "id": "g2-l15-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Doing an action in advance in preparation: booking a hotel ticket beforehand.",
            "question": "旅行の前に、ホテルを予約し（　　）ます。",
            "translation": "Before the trip, I will book a hotel in advance.",
            "options": ["ておき", "てみ", "てあり", "てい"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-15-24",
            "grammarPointTitle": "〜ておく",
            "explanation": {
                "overall": "〜ておく denotes performing an action in advance in preparation for a future event or purpose.",
                "options": [
                    {"text": "ておき", "isCorrect": True, "reason": "Correct. Action in advance: 〜ておく / 〜ておきます.", "trapCategory": "meaning"},
                    {"text": "てみ", "isCorrect": False, "reason": "Incorrect. 〜てみる means trying out an action.", "trapCategory": "meaning"},
                    {"text": "てあり", "isCorrect": False, "reason": "Incorrect. 〜てある describes resulting state, not subject preparation.", "trapCategory": "meaning"},
                    {"text": "てい", "isCorrect": False, "reason": "Incorrect. 〜ている is progressive/state.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which auxiliary verb expresses doing something in advance in preparation?"
        },
        {
            "id": "g2-l15-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Leaving a state as it is in preparation: leaving the window open.",
            "question": "暑いから、窓を開け（　　）ください。",
            "translation": "Because it's hot, please leave the window open.",
            "options": ["ておいて", "てみて", "てしまって", "ていって"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-15-24",
            "grammarPointTitle": "〜ておく",
            "explanation": {
                "overall": "〜ておく also denotes maintaining a resulting condition or state for future convenience: 開けておく -> 開けておいてください.",
                "options": [
                    {"text": "ておいて", "isCorrect": True, "reason": "Correct. Maintaining a prepared condition: 開けておいてください.", "trapCategory": "meaning"},
                    {"text": "てみて", "isCorrect": False, "reason": "Incorrect. Means 'try opening it to see'.", "trapCategory": "meaning"},
                    {"text": "てしまって", "isCorrect": False, "reason": "Incorrect. Regret or completion.", "trapCategory": "meaning"},
                    {"text": "ていって", "isCorrect": False, "reason": "Incorrect. Open and go away.", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do you say 'please leave it [open]' in preparation?"
        },
        {
            "id": "g2-l15-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Relative clause: 'The person whom Mary met yesterday'.",
            "question": "メアリーさんがきのう（　　）人は、高校の先生でした。",
            "translation": "The person whom Mary met yesterday was her high school teacher.",
            "options": ["会った", "会いました", "会うの", "会いて"],
            "correctIndex": 0,
            "grammarPointId": "g2-l15-relative-clauses",
            "grammarPointTitle": "連体修飾節 (Relative Clauses / Qualifying Nouns with Sentences)",
            "explanation": {
                "overall": "In Japanese relative clauses, verbs modify nouns in short form (past affirmative 会った + 人).",
                "options": [
                    {"text": "会った", "isCorrect": True, "reason": "Correct. Short past verb modifying noun directly.", "trapCategory": "formation"},
                    {"text": "会いました", "isCorrect": False, "reason": "Incorrect. Polite forms cannot modify nouns.", "trapCategory": "formation"},
                    {"text": "会うの", "isCorrect": False, "reason": "Incorrect. No particle の between relative clause and modified noun.", "trapCategory": "formation"},
                    {"text": "会いて", "isCorrect": False, "reason": "Incorrect. Ungrammatical te-form.", "trapCategory": "formation"}
                ]
            },
            "hint": "What form of the verb modifies a noun directly in relative clauses?"
        },
        {
            "id": "g2-l15-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Relative clause subject marker: Ken made this cake.",
            "question": "これ、けんさん（　　）作ったケーキ？",
            "translation": "Is this the cake that Ken made? (Casual question)",
            "options": ["が", "は", "を", "に"],
            "correctIndex": 0,
            "grammarPointId": "g2-l15-relative-clauses",
            "grammarPointTitle": "連体修飾節 (Relative Clauses / Qualifying Nouns with Sentences)",
            "explanation": {
                "overall": "The subject inside a relative clause must be marked by が (never topic は).",
                "options": [
                    {"text": "が", "isCorrect": True, "reason": "Correct. Embedded clause subject takes が.", "trapCategory": "formation"},
                    {"text": "は", "isCorrect": False, "reason": "Incorrect. Topic marker は cannot mark the subject inside a relative clause.", "trapCategory": "formation"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. Ken is the maker, not object.", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. Ken is not indirect object.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the subject inside an embedded qualifying clause?"
        },
        {
            "id": "g2-l15-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 15",
            "type": "multiple-choice",
            "context": "Conversational contraction of 〜ておく: とく.",
            "question": "チケットを買っ（　　）ね。",
            "translation": "I'll buy the tickets in advance, okay? (Casual spoken contraction of 〜ておく)",
            "options": ["とく", "ておく", "おき", "たき"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-15-24",
            "grammarPointTitle": "〜ておく",
            "explanation": {
                "overall": "In casual speech, 〜ておく contracts into 〜とく (買っておく -> 買っとく).",
                "options": [
                    {"text": "とく", "isCorrect": True, "reason": "Correct. Casual spoken contraction: 買っとく.", "trapCategory": "formation"},
                    {"text": "ておく", "isCorrect": False, "reason": "Incorrect. '買ってておく' is ungrammatical stuttering.", "trapCategory": "formation"},
                    {"text": "おき", "isCorrect": False, "reason": "Incorrect. Bare stem.", "trapCategory": "formation"},
                    {"text": "たき", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the common spoken contraction of 〜ておく?"
        }
    ])

    # ==================== LESSON 16 ====================
    exercises.extend([
        {
            "id": "g2-l16-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Wishing for a favorable outcome for yourself: hoping tomorrow's exam will be easy.",
            "question": "明日の試験が簡単だ（　　）んですが。",
            "translation": "I hope tomorrow's exam will be easy.",
            "options": ["といい", "たらいい", "ばいい", "とよかった"],
            "correctIndex": 0,
            "grammarPointId": "g2-l16-to-ii-hoping",
            "grammarPointTitle": "〜といい (Hoping for Favorable Outcomes: I Hope That...)",
            "explanation": {
                "overall": "〜といい (or 〜といいんですが) expresses the speaker's wish for a favorable outcome outside their direct control.",
                "options": [
                    {"text": "といい", "isCorrect": True, "reason": "Correct. Wishing pattern for speaker: 〜といいんですが.", "trapCategory": "context"},
                    {"text": "たらいい", "isCorrect": False, "reason": "Incorrect. 〜たらいい requires different clause connectives in Genki II standard lessons.", "trapCategory": "formation"},
                    {"text": "ばいい", "isCorrect": False, "reason": "Incorrect. 〜ばいい is advice/asking for instructions ('what should I do').", "trapCategory": "meaning"},
                    {"text": "とよかった", "isCorrect": False, "reason": "Incorrect. Past tense, but exam is tomorrow.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses hoping for a favorable outcome: 'I hope that...'?"
        },
        {
            "id": "g2-l16-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Wishing well for the listener: 'I hope you pass the JLPT!'.",
            "question": "JLPTに合格する（　　）ですね！",
            "translation": "I hope you pass the JLPT!",
            "options": ["といい", "たらいい", "ばいい", "ていい"],
            "correctIndex": 0,
            "grammarPointId": "g2-l16-to-ii-hoping",
            "grammarPointTitle": "〜といい (Hoping for Favorable Outcomes: I Hope That...)",
            "explanation": {
                "overall": "When wishing something good for the conversational partner, use: 〜といいですね.",
                "options": [
                    {"text": "といい", "isCorrect": True, "reason": "Correct. Wishing for listener: V-dict + といいですね.", "trapCategory": "context"},
                    {"text": "たらいい", "isCorrect": False, "reason": "Incorrect. Non-standard in this polite conversational formula.", "trapCategory": "formation"},
                    {"text": "ばいい", "isCorrect": False, "reason": "Incorrect. Advising, not wishing.", "trapCategory": "meaning"},
                    {"text": "ていい", "isCorrect": False, "reason": "Incorrect. Permission, not wishing.", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do you wish someone good luck: 'I hope [it goes well] for you'?"
        },
        {
            "id": "g2-l16-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Tense nuances in 〜時: locking the door BEFORE going out.",
            "question": "出かける（　　）、鍵をかけます。",
            "translation": "When I go out (before leaving), I lock the door.",
            "options": ["時", "た時", "て時", "時に"],
            "correctIndex": 0,
            "grammarPointId": "g2-l16-toki-tense",
            "grammarPointTitle": "〜時（とき）の時制 (Tense Nuances in 'When' Clauses: V-る時 vs V-た時)",
            "explanation": {
                "overall": "V-る時 indicates that the action of locking occurs BEFORE or at the start of leaving. If V-た時 were used, you would already be outside and couldn't lock from inside.",
                "options": [
                    {"text": "時", "isCorrect": True, "reason": "Correct. V-る時 indicates action prior to completion: 出かける時.", "trapCategory": "meaning"},
                    {"text": "た時", "isCorrect": False, "reason": "Incorrect. 出かけた時 would mean you already left the house before locking.", "trapCategory": "meaning"},
                    {"text": "て時", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach 時 directly.", "trapCategory": "formation"},
                    {"text": "時に", "isCorrect": False, "reason": "Incorrect. Ungrammatical concatenation.", "trapCategory": "formation"}
                ]
            },
            "hint": "Do you use dictionary form (る) or past form (た) for an action taken before departing?"
        },
        {
            "id": "g2-l16-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Tense nuances in 〜時: washing hands AFTER returning home.",
            "question": "家に帰っ（　　）時、手を洗いました。",
            "translation": "When I got home (after arriving), I washed my hands.",
            "options": ["た", "る", "て", "ます"],
            "correctIndex": 0,
            "grammarPointId": "g2-l16-toki-tense",
            "grammarPointTitle": "〜時（とき）の時制 (Tense Nuances in 'When' Clauses: V-る時 vs V-た時)",
            "explanation": {
                "overall": "V-た時 indicates that the first action is completed before the second action begins (after getting inside the house, washing hands).",
                "options": [
                    {"text": "た", "isCorrect": True, "reason": "Correct. V-た時 indicates subsequent action after arrival.", "trapCategory": "meaning"},
                    {"text": "る", "isCorrect": False, "reason": "Incorrect. 帰る時 would mean washing hands on the way home before arriving.", "trapCategory": "meaning"},
                    {"text": "て", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede 時 directly.", "trapCategory": "formation"},
                    {"text": "ます", "isCorrect": False, "reason": "Incorrect. Masu-form cannot precede 時.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which form indicates that the movement is completed before the second action?"
        },
        {
            "id": "g2-l16-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Doing a favor for someone: I lent my friend an umbrella.",
            "question": "私は友達に傘を貸し（　　）。",
            "translation": "I lent my friend an umbrella (did the favor of lending).",
            "options": ["てあげました", "てくれました", "てもらいました", "ていただきました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-16-25",
            "grammarPointTitle": "〜てあげる・てくれる・てもらう",
            "explanation": {
                "overall": "When the speaker performs a helpful action for someone else, the benefactive auxiliary is 〜てあげる (貸してあげました).",
                "options": [
                    {"text": "てあげました", "isCorrect": True, "reason": "Correct. Speaker does favor for other: 〜てあげる.", "trapCategory": "meaning"},
                    {"text": "てくれました", "isCorrect": False, "reason": "Incorrect. 〜てくれる means someone does favor for the speaker.", "trapCategory": "meaning"},
                    {"text": "てもらいました", "isCorrect": False, "reason": "Incorrect. 〜てもらう means receiving a favor.", "trapCategory": "meaning"},
                    {"text": "ていただきました", "isCorrect": False, "reason": "Incorrect. Humble receiving.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which benefactive auxiliary denotes doing a favor FOR someone else?"
        },
        {
            "id": "g2-l16-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Someone doing a favor for me: Ken helped me with homework.",
            "question": "けんさんは私に宿題を手伝っ（　　）。",
            "translation": "Ken helped me with my homework (did me the favor of helping).",
            "options": ["てくれました", "てあげました", "てもらいました", "てやりました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-16-25",
            "grammarPointTitle": "〜てあげる・てくれる・てもらう",
            "explanation": {
                "overall": "When another person does a favor for the speaker, the benefactive auxiliary is 〜てくれる (手伝ってくれました).",
                "options": [
                    {"text": "てくれました", "isCorrect": True, "reason": "Correct. Giver does favor for speaker: 〜てくれる.", "trapCategory": "meaning"},
                    {"text": "てあげました", "isCorrect": False, "reason": "Incorrect. Other person cannot 'あげる' to speaker.", "trapCategory": "meaning"},
                    {"text": "てもらいました", "isCorrect": False, "reason": "Incorrect. Requires receiver as topic (私はけんさんに手伝ってもらいました).", "trapCategory": "formation"},
                    {"text": "てやりました", "isCorrect": False, "reason": "Incorrect. Inappropriate downward favor.", "trapCategory": "context"}
                ]
            },
            "hint": "Which benefactive verb is used when someone does a favor FOR YOU?"
        },
        {
            "id": "g2-l16-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Receiving a favor: I had Mary teach me kanji.",
            "question": "私はメアリーさんに漢字を教え（　　）。",
            "translation": "I had Mary teach me kanji (received the favor of teaching).",
            "options": ["てもらいました", "てあげました", "てくれました", "てやりました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-16-25",
            "grammarPointTitle": "〜てあげる・てくれる・てもらう",
            "explanation": {
                "overall": "When the speaker receives a favor from someone (marked by に), use 〜てもらう (教えてもらいました).",
                "options": [
                    {"text": "てもらいました", "isCorrect": True, "reason": "Correct. Speaker receives favor from person に: 〜てもらう.", "trapCategory": "meaning"},
                    {"text": "てあげました", "isCorrect": False, "reason": "Incorrect. Means speaker taught Mary.", "trapCategory": "meaning"},
                    {"text": "てくれました", "isCorrect": False, "reason": "Incorrect. Requires Mary as topic/subject.", "trapCategory": "formation"},
                    {"text": "てやりました", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which pattern expresses having someone do something for you (receiving a favor)?"
        },
        {
            "id": "g2-l16-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Politely requesting assistance from a teacher: 'Could you please explain this?'.",
            "question": "先生、ここを説明し（　　）ませんか。",
            "translation": "Teacher, could you please explain this to me? (Very polite request)",
            "options": ["ていただけ", "てくれ", "てもらえ", "てあげ"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-16-26",
            "grammarPointTitle": "〜ていただけませんか",
            "explanation": {
                "overall": "〜ていただけませんか is the humble/polite formula for asking a superior or teacher for assistance.",
                "options": [
                    {"text": "ていただけ", "isCorrect": True, "reason": "Correct. Polite request to superior: 〜ていただけませんか.", "trapCategory": "context"},
                    {"text": "てくれ", "isCorrect": False, "reason": "Incorrect. 〜てくれませんか is casual, too informal for a teacher.", "trapCategory": "context"},
                    {"text": "てもらえ", "isCorrect": False, "reason": "Incorrect. Less formal than いただけませんか.", "trapCategory": "context"},
                    {"text": "てあげ", "isCorrect": False, "reason": "Incorrect. Cannot use あげる in a request for assistance.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which request formula is suitably polite for asking a teacher or superior for a favor?"
        },
        {
            "id": "g2-l16-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Apologizing for arriving late: 'I am sorry for being late'.",
            "question": "遅れ（　　）すみませんでした。",
            "translation": "I am sorry for being late.",
            "options": ["て", "た", "る", "ます"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-16-27",
            "grammarPointTitle": "〜てすみません・なくてすみません",
            "explanation": {
                "overall": "To apologize for doing something, attach the te-form to すみません: Verb te-form + すみません (遅れてすみません).",
                "options": [
                    {"text": "て", "isCorrect": True, "reason": "Correct. Apologizing formula: V-te + すみませんでした.", "trapCategory": "formation"},
                    {"text": "た", "isCorrect": False, "reason": "Incorrect. Past ta-form cannot attach すみません directly.", "trapCategory": "formation"},
                    {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach すみません directly.", "trapCategory": "formation"},
                    {"text": "ます", "isCorrect": False, "reason": "Incorrect. Masu-form cannot attach すみません.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form attaches to すみませんでした to state what you are apologizing for?"
        },
        {
            "id": "g2-l16-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 16",
            "type": "multiple-choice",
            "context": "Apologizing for failing to do something: 'I am sorry for not contacting you earlier'.",
            "question": "連絡し（　　）すみませんでした。",
            "translation": "I am sorry for not getting in touch with you.",
            "options": ["なくて", "ないで", "なかった", "ず"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-16-27",
            "grammarPointTitle": "〜てすみません・なくてすみません",
            "explanation": {
                "overall": "To apologize for NOT doing something, attach 〜なくて to すみません: Verb-nakute + すみません (連絡しなくてすみません).",
                "options": [
                    {"text": "なくて", "isCorrect": True, "reason": "Correct. Negative apology formula: 〜なくてすみません.", "trapCategory": "formation"},
                    {"text": "ないで", "isCorrect": False, "reason": "Incorrect. 〜ないで expresses doing an action without doing another, not reason for apology.", "trapCategory": "formation"},
                    {"text": "なかった", "isCorrect": False, "reason": "Incorrect. Plain past cannot attach すみません.", "trapCategory": "formation"},
                    {"text": "ず", "isCorrect": False, "reason": "Incorrect. Classical archaic negative.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you apologize for NOT doing something: 'I am sorry for not [doing]'?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_all_genki2_exercises()
    print(f"Generated {len(ex_list)} exercises across Genki II Lessons 13-16.")
