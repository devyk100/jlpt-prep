import json

def get_genki2_l19_to_l23():
    exercises = []

    # ==================== LESSON 19 ====================
    exercises.extend([
        {
            "id": "g2-l19-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Honorific verb for a professor: 'Professor Yamada has already gone home'.",
            "question": "山田先生はもう（　　）。",
            "translation": "Professor Yamada has already gone home. (Honorific)",
            "options": ["お帰りになりました", "参りました", "帰られました", "お帰りしました"],
            "correctIndex": 0,
            "grammarPointId": "g2-l19-sonkeigo-verbs",
            "grammarPointTitle": "尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)",
            "explanation": {
                "overall": "The regular honorific formula is: お + Verb stem + になる (お帰りになりました).",
                "options": [
                    {"text": "お帰りになりました", "isCorrect": True, "reason": "Correct. Regular honorific formula: お + V-stem + になりました.", "trapCategory": "formation"},
                    {"text": "参りました", "isCorrect": False, "reason": "Incorrect. 参る is humble (謙譲語), cannot be used for a superior.", "trapCategory": "context"},
                    {"text": "帰られました", "isCorrect": False, "reason": "Incorrect. While passive honorific exists, regular formula お〜になる is standard polite sonkeigo in Genki II.", "trapCategory": "context"},
                    {"text": "お帰りしました", "isCorrect": False, "reason": "Incorrect. お〜する is the humble formula, inappropriate for superior.", "trapCategory": "context"}
                ]
            },
            "hint": "What is the standard regular honorific formula: お + [stem] + ___?"
        },
        {
            "id": "g2-l19-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Special honorific verb for eating: 'What did the guest eat?'.",
            "question": "お客様は何を（　　）か。",
            "translation": "What did the customer eat? (Special honorific verb)",
            "options": ["召し上がりました", "いただきました", "食べました", "お食べになりました"],
            "correctIndex": 0,
            "grammarPointId": "g2-l19-sonkeigo-verbs",
            "grammarPointTitle": "尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)",
            "explanation": {
                "overall": "The special honorific verb for 食べる and 飲む is 召し上がる (召し上がりました).",
                "options": [
                    {"text": "召し上がりました", "isCorrect": True, "reason": "Correct. Special honorific verb for 食べる/飲む is 召し上がる.", "trapCategory": "meaning"},
                    {"text": "いただきました", "isCorrect": False, "reason": "Incorrect. いただく is the humble verb used for the speaker, not the customer.", "trapCategory": "context"},
                    {"text": "食べました", "isCorrect": False, "reason": "Incorrect. Neutral polite, lacks honorific respect.", "trapCategory": "context"},
                    {"text": "お食べになりました", "isCorrect": False, "reason": "Incorrect. When a special verb exists, it takes precedence over regular formula.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the special honorific (尊敬語) verb for 食べる and 飲む?"
        },
        {
            "id": "g2-l19-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Special honorific verb for speaking/saying: 'The president said this'.",
            "question": "社長がそう（　　）。",
            "translation": "The company president said so. (Special honorific verb)",
            "options": ["おっしゃいました", "申しました", "申し上げました", "言いました"],
            "correctIndex": 0,
            "grammarPointId": "g2-l19-sonkeigo-verbs",
            "grammarPointTitle": "尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)",
            "explanation": {
                "overall": "The special honorific verb for 言う is おっしゃる (おっしゃいました).",
                "options": [
                    {"text": "おっしゃいました", "isCorrect": True, "reason": "Correct. Special honorific verb for 言う is おっしゃる.", "trapCategory": "meaning"},
                    {"text": "申しました", "isCorrect": False, "reason": "Incorrect. 申す is humble (謙譲語).", "trapCategory": "context"},
                    {"text": "申し上げました", "isCorrect": False, "reason": "Incorrect. 申し上げる is humble.", "trapCategory": "context"},
                    {"text": "言いました", "isCorrect": False, "reason": "Incorrect. Neutral, lacks honorific elevation.", "trapCategory": "context"}
                ]
            },
            "hint": "What is the special honorific verb for 言う?"
        },
        {
            "id": "g2-l19-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Special honorific verb for seeing/watching: 'Did the teacher watch the news?'.",
            "question": "先生はそのニュースを（　　）か。",
            "translation": "Did the teacher watch that news? (Special honorific verb)",
            "options": ["ご覧になりました", "拝見しました", "見ました", "お見になりました"],
            "correctIndex": 0,
            "grammarPointId": "g2-l19-sonkeigo-verbs",
            "grammarPointTitle": "尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)",
            "explanation": {
                "overall": "The special honorific verb for 見る is ご覧になる (ご覧になりました).",
                "options": [
                    {"text": "ご覧になりました", "isCorrect": True, "reason": "Correct. Special honorific verb for 見る is ご覧になる.", "trapCategory": "meaning"},
                    {"text": "拝見しました", "isCorrect": False, "reason": "Incorrect. 拝見する is the humble verb used by the speaker.", "trapCategory": "context"},
                    {"text": "見ました", "isCorrect": False, "reason": "Incorrect. Neutral polite.", "trapCategory": "context"},
                    {"text": "お見になりました", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the special honorific verb for 見る?"
        },
        {
            "id": "g2-l19-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Polite honorific request to a guest: 'Please take a seat here'.",
            "question": "どうぞこちらにお（　　）ください。",
            "translation": "Please take a seat over here. (Honorific request)",
            "options": ["座り", "座る", "座って", "座りになり"],
            "correctIndex": 0,
            "grammarPointId": "g2-l19-o-kudasai",
            "grammarPointTitle": "お + V-stem + ください (Polite Honorific Request: Please Graciously Do)",
            "explanation": {
                "overall": "The formula for polite honorific requests is: お + Verb stem + ください (お座りください). More polite than 座ってください.",
                "options": [
                    {"text": "座り", "isCorrect": True, "reason": "Correct. Formula: お + V-stem + ください: お座りください.", "trapCategory": "formation"},
                    {"text": "座る", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot follow お.", "trapCategory": "formation"},
                    {"text": "座って", "isCorrect": False, "reason": "Incorrect. Te-form is used in 座ってください, without the prefix お.", "trapCategory": "formation"},
                    {"text": "座りになり", "isCorrect": False, "reason": "Incorrect. Redundant combination.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form attaches between お and ください in polite honorific requests?"
        },
        {
            "id": "g2-l19-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Thanking a teacher for writing a recommendation letter.",
            "question": "推薦状を書いて（　　）、ありがとうございました。",
            "translation": "Thank you very much for writing a letter of recommendation for me.",
            "options": ["くださって", "くれて", "あげて", "もらって"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-19-32",
            "grammarPointTitle": "〜てくれてありがとう・〜てよかった",
            "explanation": {
                "overall": "To thank a superior for a favor, use the honorific: 〜てくださってありがとうございました (くれ is for peers/inferiors).",
                "options": [
                    {"text": "くださって", "isCorrect": True, "reason": "Correct. Respectful thank-you to superior: 〜てくださってありがとうございました.", "trapCategory": "context"},
                    {"text": "くれて", "isCorrect": False, "reason": "Incorrect. 〜てくれてありがとう is informal, inappropriate for a teacher.", "trapCategory": "context"},
                    {"text": "あげて", "isCorrect": False, "reason": "Incorrect. Cannot thank someone with あげて.", "trapCategory": "meaning"},
                    {"text": "もらって", "isCorrect": False, "reason": "Incorrect. Non-standard in direct gratitude.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which benefactive form is used when thanking a teacher or superior for doing a favor?"
        },
        {
            "id": "g2-l19-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Expressing relief: 'I'm glad that it did not rain yesterday during our picnic'.",
            "question": "きのう雨が降ら（　　）よかったです。",
            "translation": "I'm glad that it didn't rain yesterday.",
            "options": ["なくて", "ないで", "なければ", "なかった"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-19-32",
            "grammarPointTitle": "〜てくれてありがとう・〜てよかった",
            "explanation": {
                "overall": "To express relief ('I'm glad that...'), use: Verb te-form + よかった. For negative: 〜なくてよかった.",
                "options": [
                    {"text": "なくて", "isCorrect": True, "reason": "Correct. Relief formula for negative: 〜なくてよかった.", "trapCategory": "meaning"},
                    {"text": "ないで", "isCorrect": False, "reason": "Incorrect. 〜ないで cannot combine with よかった.", "trapCategory": "formation"},
                    {"text": "なければ", "isCorrect": False, "reason": "Incorrect. 〜なければよかった expresses regret ('I wish it hadn't'), opposite of relief!", "trapCategory": "meaning"},
                    {"text": "なかった", "isCorrect": False, "reason": "Incorrect. Plain past cannot attach よかった directly.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which pattern expresses relief: 'I am glad that [it did not happen]'?"
        },
        {
            "id": "g2-l19-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Objective expectation based on schedule: 'The package is supposed to arrive today'.",
            "question": "荷物は今日届く（　　）です。",
            "translation": "The package is expected / supposed to arrive today.",
            "options": ["はず", "わけ", "つもり", "そう"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-19-33",
            "grammarPointTitle": "〜はずです",
            "explanation": {
                "overall": "〜はずです expresses an objective expectation based on reliable knowledge, schedules, or logical grounds ('supposed to / expected to').",
                "options": [
                    {"text": "はず", "isCorrect": True, "reason": "Correct. Objective expectation: V-dict + はずです.", "trapCategory": "meaning"},
                    {"text": "わけ", "isCorrect": False, "reason": "Incorrect. わけ denotes explanation of cause or circumstance.", "trapCategory": "meaning"},
                    {"text": "つもり", "isCorrect": False, "reason": "Incorrect. つもり expresses personal intent of humans, not inanimate package delivery.", "trapCategory": "meaning"},
                    {"text": "そう", "isCorrect": False, "reason": "Incorrect. Hearsay/appearance.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which noun expresses that something is scheduled or logically expected to happen ('supposed to')?"
        },
        {
            "id": "g2-l19-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Formation of 〜はずです with a な-adjective: 'He should be free today'.",
            "question": "田中さんは今日暇（　　）はずです。",
            "translation": "Mr. Tanaka should be free today.",
            "options": ["な", "だ", "の", "である"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-19-33",
            "grammarPointTitle": "〜はずです",
            "explanation": {
                "overall": "Since はず is a noun, な-adjectives attach な before はず (暇なはずです), and nouns attach の (学生のはずです).",
                "options": [
                    {"text": "な", "isCorrect": True, "reason": "Correct. な-adjectives take な before noun はず.", "trapCategory": "formation"},
                    {"text": "だ", "isCorrect": False, "reason": "Incorrect. だ cannot modify the noun はず.", "trapCategory": "formation"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. の is for nouns (学生のはず), not な-adjectives.", "trapCategory": "formation"},
                    {"text": "である", "isCorrect": False, "reason": "Incorrect. Formal written style.", "trapCategory": "context"}
                ]
            },
            "hint": "What connector do な-adjectives take before the noun はず?"
        },
        {
            "id": "g2-l19-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 19",
            "type": "multiple-choice",
            "context": "Special honorific verb for knowing: 'Does the teacher know that person?'.",
            "question": "先生はあの方をご（　　）ですか。",
            "translation": "Does the teacher know that person? (Honorific)",
            "options": ["存じ", "存じ上げ", "知り", "知られ"],
            "correctIndex": 0,
            "grammarPointId": "g2-l19-sonkeigo-verbs",
            "grammarPointTitle": "尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)",
            "explanation": {
                "overall": "The honorific equivalent of 知っている is ご存じだ (ご存じですか). The humble equivalent used for oneself is 存じている / 存じ上げております.",
                "options": [
                    {"text": "存じ", "isCorrect": True, "reason": "Correct. Honorific for 知っている is ご存じです / ご存じですか.", "trapCategory": "meaning"},
                    {"text": "存じ上げ", "isCorrect": False, "reason": "Incorrect. 存じ上げる is humble (used for speaker), not honorific.", "trapCategory": "context"},
                    {"text": "知り", "isCorrect": False, "reason": "Incorrect. Neutral polite.", "trapCategory": "context"},
                    {"text": "知られ", "isCorrect": False, "reason": "Incorrect. Passive/potential.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the honorific equivalent of 知っていますか?"
        }
    ])

    # ==================== LESSON 20 ====================
    exercises.extend([
        {
            "id": "g2-l20-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Humble verb for going/coming: 'I will go to your office tomorrow at 2:00'.",
            "question": "明日二時に先生の研究室へ（　　）。",
            "translation": "I will come to your office tomorrow at 2:00. (Humble speech to teacher)",
            "options": ["伺います", "いらっしゃいます", "参ります", "行きます"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-34",
            "grammarPointTitle": "丁重語・謙譲語",
            "explanation": {
                "overall": "伺う (うかがう) is the specific humble verb for visiting or going to a superior's place (参る is general courteous movement, but 伺う specifically lowers the speaker visiting a superior).",
                "options": [
                    {"text": "伺います", "isCorrect": True, "reason": "Correct. Specific humble verb for visiting a superior: 伺います.", "trapCategory": "context"},
                    {"text": "いらっしゃいます", "isCorrect": False, "reason": "Incorrect. いらっしゃる is honorific (尊敬語) for the superior's actions, never speaker's.", "trapCategory": "context"},
                    {"text": "参ります", "isCorrect": False, "reason": "Incorrect. While humble, 参る is general movement; visiting a superior's office standardly uses 伺います.", "trapCategory": "context"},
                    {"text": "行きます", "isCorrect": False, "reason": "Incorrect. Neutral polite, lacks humble deference to a professor.", "trapCategory": "context"}
                ]
            },
            "hint": "Which humble verb specifically means to visit a superior's place or home?"
        },
        {
            "id": "g2-l20-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Humble introduction: 'My name is Ken Tanaka'.",
            "question": "田中けんと（　　）。よろしくお願いいたします。",
            "translation": "My name is Ken Tanaka. (Humble self-introduction)",
            "options": ["申します", "おっしゃいます", "言います", "話します"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-34",
            "grammarPointTitle": "丁重語・謙譲語",
            "explanation": {
                "overall": "The humble verb for 言う when stating one's own name is 申す (申します).",
                "options": [
                    {"text": "申します", "isCorrect": True, "reason": "Correct. Humble self-introduction: 〜と申します.", "trapCategory": "context"},
                    {"text": "おっしゃいます", "isCorrect": False, "reason": "Incorrect. おっしゃる is honorific, cannot be applied to oneself.", "trapCategory": "context"},
                    {"text": "言います", "isCorrect": False, "reason": "Incorrect. Neutral, lacks formal modesty.", "trapCategory": "context"},
                    {"text": "話します", "isCorrect": False, "reason": "Incorrect. Does not fit name introduction formula.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the humble verb for stating your own name in Japanese?"
        },
        {
            "id": "g2-l20-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Regular humble formula: offering to carry the professor's heavy luggage.",
            "question": "先生、そのお荷物をお（　　）しましょうか。",
            "translation": "Teacher, shall I carry that bag for you? (Humble offer)",
            "options": ["持ち", "持たれ", "持つ", "持って"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-34",
            "grammarPointTitle": "丁重語・謙譲語",
            "explanation": {
                "overall": "The regular humble formula for offering a service is: お + Verb stem + する (お持ちしましょうか).",
                "options": [
                    {"text": "持ち", "isCorrect": True, "reason": "Correct. Formula: お + V-stem + する: お持ちします.", "trapCategory": "formation"},
                    {"text": "持たれ", "isCorrect": False, "reason": "Incorrect. Passive/honorific stem.", "trapCategory": "formation"},
                    {"text": "持つ", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot follow お.", "trapCategory": "formation"},
                    {"text": "持って", "isCorrect": False, "reason": "Incorrect. Te-form cannot follow お in humble formula.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the regular humble formula: お + [stem] + する?"
        },
        {
            "id": "g2-l20-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Doing action without doing another: 'I went to school without having breakfast'.",
            "question": "朝ご飯を（　　）学校へ行きました。",
            "translation": "I went to school without eating breakfast.",
            "options": ["食べないで", "食べなくて", "食べない", "食べず"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-35",
            "grammarPointTitle": "〜ないで",
            "explanation": {
                "overall": "Doing an action without performing another is expressed by: Verb nai-form + で (食べないで). (〜なくて expresses reason/cause, not 'without doing').",
                "options": [
                    {"text": "食べないで", "isCorrect": True, "reason": "Correct. 'Without doing': Verb nai-form + で.", "trapCategory": "formation"},
                    {"text": "食べなくて", "isCorrect": False, "reason": "Incorrect. 〜なくて expresses cause ('because I didn't eat...'), not accompaniment.", "trapCategory": "meaning"},
                    {"text": "食べない", "isCorrect": False, "reason": "Incorrect. Missing particle で.", "trapCategory": "formation"},
                    {"text": "食べず", "isCorrect": False, "reason": "Incorrect. Written classical form.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which pattern means 'without doing [action]': 〜ないで or 〜なくて?"
        },
        {
            "id": "g2-l20-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Embedded question with question word: 'Please tell me what time the meeting starts'.",
            "question": "会議が何時に始まる（　　）、教えてください。",
            "translation": "Please tell me what time the meeting starts.",
            "options": ["か", "かどうか", "のを", "こと"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-36",
            "grammarPointTitle": "文の中の疑問・という名前",
            "explanation": {
                "overall": "An embedded question containing an interrogative question word (何時, どこ, だれ) takes particle か: Short form + か (何時に始まるか).",
                "options": [
                    {"text": "か", "isCorrect": True, "reason": "Correct. Wh-question embedded clause ends with か.", "trapCategory": "formation"},
                    {"text": "かどうか", "isCorrect": False, "reason": "Incorrect. かどうか is strictly for yes/no questions without question words.", "trapCategory": "formation"},
                    {"text": "のを", "isCorrect": False, "reason": "Incorrect. Nominalizer, does not embed question.", "trapCategory": "formation"},
                    {"text": "こと", "isCorrect": False, "reason": "Incorrect. Cannot embed question clause.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle closes an embedded question that contains a question word like 何時?"
        },
        {
            "id": "g2-l20-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Embedded yes/no question: 'I don't know whether or not Ken is coming tomorrow'.",
            "question": "けんさんが明日来る（　　）、分かりません。",
            "translation": "I don't know whether or not Ken will come tomorrow.",
            "options": ["かどうか", "か", "のか", "こと"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-36",
            "grammarPointTitle": "文の中の疑問・という名前",
            "explanation": {
                "overall": "An embedded yes-no question (without an interrogative question word) takes かどうか ('whether or not'): 来るかどうか、分かりません.",
                "options": [
                    {"text": "かどうか", "isCorrect": True, "reason": "Correct. Yes/no embedded question formula: 〜かどうか.", "trapCategory": "formation"},
                    {"text": "か", "isCorrect": False, "reason": "Incorrect. While sometimes used in casual speech, standard textbook Japanese uses かどうか for yes/no clauses.", "trapCategory": "context"},
                    {"text": "のか", "isCorrect": False, "reason": "Incorrect. Casual explanatory question marker.", "trapCategory": "formation"},
                    {"text": "こと", "isCorrect": False, "reason": "Incorrect. Noun nominalizer.", "trapCategory": "formation"}
                ]
            },
            "hint": "What pattern expresses an embedded 'whether or not' clause?"
        },
        {
            "id": "g2-l20-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Citing a name or title: 'A famous novel called I Am a Cat'.",
            "question": "「吾輩は猫である」（　　）小説を読みました。",
            "translation": "I read a novel called 'I Am a Cat'.",
            "options": ["という", "といった", "というの", "というな"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-36",
            "grammarPointTitle": "文の中の疑問・という名前",
            "explanation": {
                "overall": "The pattern for introducing or defining a name/title is: [Name] + という + [Noun] (「吾輩は猫である」という小説).",
                "options": [
                    {"text": "という", "isCorrect": True, "reason": "Correct. Identifying pattern: [Name] という [Category noun].", "trapCategory": "formation"},
                    {"text": "といった", "isCorrect": False, "reason": "Incorrect. といった means 'things such as'.", "trapCategory": "meaning"},
                    {"text": "というの", "isCorrect": False, "reason": "Incorrect. Extra の.", "trapCategory": "formation"},
                    {"text": "というな", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What phrase connects a specific name or title to the general category noun ('called / named')?"
        },
        {
            "id": "g2-l20-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Ease of performing an action: this electronic dictionary is very easy to use.",
            "question": "この電子辞書はとても使い（　　）です。",
            "translation": "This electronic dictionary is very easy to use.",
            "options": ["やすい", "にくい", "やすくて", "そう"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-37",
            "grammarPointTitle": "〜やすい・〜にくい",
            "explanation": {
                "overall": "The pattern for 'easy to do' is: Verb stem + やすい (使う -> 使い + やすい -> 使いやすいです). Conjugates like an い-adjective.",
                "options": [
                    {"text": "やすい", "isCorrect": True, "reason": "Correct. 'Easy to do': V-stem + やすい.", "trapCategory": "meaning"},
                    {"text": "にくい", "isCorrect": False, "reason": "Incorrect. にくい means 'difficult/hard to do'.", "trapCategory": "meaning"},
                    {"text": "やすくて", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede です.", "trapCategory": "formation"},
                    {"text": "そう", "isCorrect": False, "reason": "Incorrect. Appearance.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What suffix attaches to a verb stem to mean 'easy to do'?"
        },
        {
            "id": "g2-l20-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Difficulty of performing an action: this bitter medicine is hard to swallow.",
            "question": "この苦い薬は飲み（　　）です。",
            "translation": "This bitter medicine is hard to take / swallow.",
            "options": ["にくい", "やすい", "にくくて", "づらい"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-37",
            "grammarPointTitle": "〜やすい・〜にくい",
            "explanation": {
                "overall": "The pattern for 'hard / difficult to do' is: Verb stem + にくい (飲む -> 飲み + にくい -> 飲みにくいです).",
                "options": [
                    {"text": "にくい", "isCorrect": True, "reason": "Correct. 'Hard to do': V-stem + にくい.", "trapCategory": "meaning"},
                    {"text": "やすい", "isCorrect": False, "reason": "Incorrect. やすい means 'easy to do'.", "trapCategory": "meaning"},
                    {"text": "にくくて", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede です.", "trapCategory": "formation"},
                    {"text": "づらい", "isCorrect": False, "reason": "Incorrect. づらい expresses physical pain/discomfort, but standard textbook pattern is にくい.", "trapCategory": "context"}
                ]
            },
            "hint": "What suffix attaches to a verb stem to mean 'hard / difficult to do'?"
        },
        {
            "id": "g2-l20-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 20",
            "type": "multiple-choice",
            "context": "Conjugating 〜やすい into past tense: 'It was easy to understand'.",
            "question": "昨日の説明はとても分かり（　　）。",
            "translation": "Yesterday's explanation was very easy to understand.",
            "options": ["やすかったです", "やすいでした", "やすかったでした", "やすいでした"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-20-37",
            "grammarPointTitle": "〜やすい・〜にくい",
            "explanation": {
                "overall": "〜やすい and 〜にくい conjugate as い-adjectives: past affirmative drops final い and adds かったです (分かりやすかったです).",
                "options": [
                    {"text": "やすかったです", "isCorrect": True, "reason": "Correct. Past form of 〜やすい is 〜やすかったです.", "trapCategory": "formation"},
                    {"text": "やすいでした", "isCorrect": False, "reason": "Incorrect. い-adjective endings cannot take でした directly.", "trapCategory": "formation"},
                    {"text": "やすかったでした", "isCorrect": False, "reason": "Incorrect. Redundant past copula.", "trapCategory": "formation"},
                    {"text": "やすいでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you conjugate 〜やすい into the past tense?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_genki2_l19_to_l23()
    print(f"Generated {len(ex_list)} exercises across Genki II Lessons 19 and 20.")
