import json

def get_skm3_exercises():
    exercises = []

    # ==================== SKM N3 PART 1 CHAPTER 1 ====================
    exercises.extend([
        {
            "id": "skm3-c1-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Eating soup while it is still piping hot before it cools down.",
            "question": "スープが温かい（　　）召し上がってください。",
            "translation": "Please eat the soup while it is still warm.",
            "options": ["うちに", "間に", "際して", "ところで"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u1-uchini-while",
            "grammarPointTitle": "〜うちに (While State Lasts / Before Opportunity Slips)",
            "explanation": {
                "overall": "〜うちに means 'while the current favorable condition lasts / before the state changes'. Soup cools down continuously, so doing the action before the window closes requires うちに.",
                "options": [
                    {"text": "うちに", "isCorrect": True, "reason": "Correct. Favorable opportunity window: 温かいうちに.", "trapCategory": "meaning"},
                    {"text": "間に", "isCorrect": False, "reason": "Incorrect. 間に denotes an objective time frame (e.g. while person is away), lacking the 'before the condition changes' nuance.", "trapCategory": "context"},
                    {"text": "際して", "isCorrect": False, "reason": "Incorrect. 際して means 'on the special occasion of'.", "trapCategory": "meaning"},
                    {"text": "ところで", "isCorrect": False, "reason": "Incorrect. ところで means 'by the way' or 'even if'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern denotes acting while a temporary favorable state still exists?"
        },
        {
            "id": "skm3-c1-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Gradual unnoticed change: listening to the lecture, I naturally drifted off to sleep.",
            "question": "先生の講義を聞いている（　　）、いつの間にか眠ってしまった。",
            "translation": "While listening to the teacher's lecture, before I knew it I fell asleep.",
            "options": ["うちに", "間に", "ところで", "たびに"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u1-uchini-change",
            "grammarPointTitle": "〜うちに (Unnoticed Natural Evolution: While Doing X, Y Emerged)",
            "explanation": {
                "overall": "〜うちに paired with 'いつの間にか' denotes an unconscious, natural evolution or shift in state that emerged without the speaker intending it.",
                "options": [
                    {"text": "うちに", "isCorrect": True, "reason": "Correct. Natural unconscious transition: 聞いているうちにいつの間にか.", "trapCategory": "meaning"},
                    {"text": "間に", "isCorrect": False, "reason": "Incorrect. 間に marks objective time boundaries, whereas うちに emphasizes gradual spontaneous transition.", "trapCategory": "context"},
                    {"text": "ところで", "isCorrect": False, "reason": "Incorrect. Temporal phase or connective.", "trapCategory": "meaning"},
                    {"text": "たびに", "isCorrect": False, "reason": "Incorrect. たびに means 'every single time'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which expression pairs with いつの間にか to express a gradual, unconscious change?"
        },
        {
            "id": "skm3-c1-ex-3",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Strict prerequisite: cannot sign the contract without first consulting a lawyer.",
            "question": "弁護士に相談し（　　）、契約書にサインはできません。",
            "translation": "I cannot sign the contract without first consulting a lawyer / Not until I consult a lawyer can I sign.",
            "options": ["てからでないと", "てから", "た後で", "たところで"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u1-te-kara-denaito",
            "grammarPointTitle": "〜てからでないと / 〜てからでなければ (Not Until / Only After Prerequisite Is Done)",
            "explanation": {
                "overall": "〜てからでないと (or 〜てからでなければ) strictly governs a negative or impossible main clause: 'Unless action X is done first, Y cannot take place'.",
                "options": [
                    {"text": "てからでないと", "isCorrect": True, "reason": "Correct. Prerequisite conditional with negative conclusion: 〜てからでないと…できない.", "trapCategory": "formation"},
                    {"text": "てから", "isCorrect": False, "reason": "Incorrect. 〜てから does not carry the absolute prerequisite restriction requiring a negative clause.", "trapCategory": "meaning"},
                    {"text": "た後で", "isCorrect": False, "reason": "Incorrect. Neutral chronological sequence.", "trapCategory": "meaning"},
                    {"text": "たところで", "isCorrect": False, "reason": "Incorrect. たところで means 'even if [hypothetical minimal benefit]'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern means 'not until / unless X is done first, Y cannot happen'?"
        },
        {
            "id": "skm3-c1-ex-4",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Temporal phase: on the very verge of leaving the house right this second.",
            "question": "今から出かける（　　）だから、後で電話するね。",
            "translation": "I'm just about to head out right now, so I'll call you later.",
            "options": ["ところ", "ばかり", "最中", "とおり"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u1-tokoro-da-phases",
            "grammarPointTitle": "〜ところだ (Temporal Phase: Imminent, In the Midst, or Just Finished)",
            "explanation": {
                "overall": "Verb dictionary form + ところだ expresses the imminent starting point ('just on the very verge of doing X').",
                "options": [
                    {"text": "ところ", "isCorrect": True, "reason": "Correct. Imminent action phase: V-dict + ところだ.", "trapCategory": "formation"},
                    {"text": "ばかり", "isCorrect": False, "reason": "Incorrect. 〜たばかり expresses action completed just moments ago, opposite temporal phase.", "trapCategory": "meaning"},
                    {"text": "最中", "isCorrect": False, "reason": "Incorrect. 最中 denotes being right in the middle of a dynamic event.", "trapCategory": "meaning"},
                    {"text": "とおり", "isCorrect": False, "reason": "Incorrect. とおり means 'in accordance with'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What pattern expresses being 'just about to / on the verge of doing'?"
        },
        {
            "id": "skm3-c1-ex-5",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Temporal phase: just completed an action this second. Finished eating lunch.",
            "question": "たった今、昼ご飯を食べ終わっ（　　）です。",
            "translation": "I have just this second finished eating lunch.",
            "options": ["たところ", "る最中", "るばかり", "たはず"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u1-tokoro-da-phases",
            "grammarPointTitle": "〜ところだ (Temporal Phase: Imminent, In the Midst, or Just Finished)",
            "explanation": {
                "overall": "Verb ta-form + ところだ emphasizes the immediate moment of completion ('just finished this very second', paired with たった今).",
                "options": [
                    {"text": "たところ", "isCorrect": True, "reason": "Correct. Immediate completion phase: V-ta + ところだ.", "trapCategory": "formation"},
                    {"text": "る最中", "isCorrect": False, "reason": "Incorrect. In the middle of.", "trapCategory": "meaning"},
                    {"text": "るばかり", "isCorrect": False, "reason": "Incorrect. Tendency towards negative.", "trapCategory": "meaning"},
                    {"text": "たはず", "isCorrect": False, "reason": "Incorrect. Logical expectation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What verb form combines with ところだ to mean 'just this second finished'?"
        },
        {
            "id": "skm3-c1-ex-6",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Duration contrast: reading continuously the whole time during summer vacation.",
            "question": "夏休みの（　　）、ずっと実家に滞在していました。",
            "translation": "Throughout the summer vacation, I was staying at my parents' home the entire time.",
            "options": ["間", "間に", "うちに", "最中に"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u1-aida-vs-aidani",
            "grammarPointTitle": "〜間 vs 〜間に (Continuous Duration vs Momentary Action)",
            "explanation": {
                "overall": "When the action lasts continuously throughout the entire span (emphasized by ずっと), use 〜間 without に.",
                "options": [
                    {"text": "間", "isCorrect": True, "reason": "Correct. Continuous duration: Noun の間 (paired with ずっと).", "trapCategory": "meaning"},
                    {"text": "間に", "isCorrect": False, "reason": "Incorrect. 間に denotes a single moment, clashing with ずっと滞在していた.", "trapCategory": "meaning"},
                    {"text": "うちに", "isCorrect": False, "reason": "Incorrect. うちに denotes temporary opportunity window.", "trapCategory": "context"},
                    {"text": "最中に", "isCorrect": False, "reason": "Incorrect. Clashes with full vacation duration.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Do you use 間 or 間に when an action continues for the entire duration without interruption?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 2 ====================
    exercises.extend([
        {
            "id": "skm3-c2-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 2",
            "type": "multiple-choice",
            "context": "Assembling furniture in exact accordance with the illustrated manual.",
            "question": "説明書に書いてある（　　）組み立ててください。",
            "translation": "Please assemble it exactly as written in the instruction manual.",
            "options": ["とおりに", "ように", "ままに", "ほどに"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u2-toori-ni-accordance",
            "grammarPointTitle": "〜とおりに / 〜どおりに (Just As / In Exact Accordance With)",
            "explanation": {
                "overall": "〜とおりに denotes following a model, pattern, or instructions faithfully without deviation ('just as / in exact accordance with').",
                "options": [
                    {"text": "とおりに", "isCorrect": True, "reason": "Correct. Faithful replication: V-short + とおりに.", "trapCategory": "meaning"},
                    {"text": "ように", "isCorrect": False, "reason": "Incorrect. ように denotes objective goal ('so that') or general resemblance.", "trapCategory": "meaning"},
                    {"text": "ままに", "isCorrect": False, "reason": "Incorrect. まま denotes leaving an unchanged passive condition.", "trapCategory": "meaning"},
                    {"text": "ほどに", "isCorrect": False, "reason": "Incorrect. ほど denotes degree.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern denotes doing an action 'in exact accordance with' instructions?"
        },
        {
            "id": "skm3-c2-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 2",
            "type": "multiple-choice",
            "context": "Different reactions depending on the person: customs vary by country.",
            "question": "文化や習慣は国（　　）違います。",
            "translation": "Cultures and customs differ depending on the country.",
            "options": ["によって", "にとって", "に対して", "について"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u2-ni-yotte-variation",
            "grammarPointTitle": "〜によって / 〜によっては (Depending on / According to Differences)",
            "explanation": {
                "overall": "〜によって denotes diversity, variance, or dependency: 'depending on / according to differences in X, Y varies'.",
                "options": [
                    {"text": "によって", "isCorrect": True, "reason": "Correct. Variation/diversity: Noun + によって (違います/様々です).", "trapCategory": "meaning"},
                    {"text": "にとって", "isCorrect": False, "reason": "Incorrect. にとって means 'from the perspective of [evaluator]'.", "trapCategory": "meaning"},
                    {"text": "に対して", "isCorrect": False, "reason": "Incorrect. に対して means 'in contrast to' or 'towards'.", "trapCategory": "meaning"},
                    {"text": "について", "isCorrect": False, "reason": "Incorrect. について means 'about / regarding'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern pairs with 違う / 様々だ to mean 'depending on [differences in]'?"
        },
        {
            "id": "skm3-c2-ex-3",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 2",
            "type": "multiple-choice",
            "context": "Invariable recurrence: every single time I listen to this song, I recall high school days.",
            "question": "この歌を聞く（　　）、高校時代を思い出します。",
            "translation": "Every single time I listen to this song, I recall my high school days.",
            "options": ["たびに", "ついでに", "とおりに", "うちに"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u2-tabini-repetition",
            "grammarPointTitle": "〜たびに (Every Single Time / Invariable Recurrence)",
            "explanation": {
                "overall": "〜たびに means 'every single time X happens, Y invariably occurs without exception'.",
                "options": [
                    {"text": "たびに", "isCorrect": True, "reason": "Correct. Invariable repetition: V-dict + たびに.", "trapCategory": "meaning"},
                    {"text": "ついでに", "isCorrect": False, "reason": "Incorrect. ついでに means doing a side task while performing a main task.", "trapCategory": "meaning"},
                    {"text": "とおりに", "isCorrect": False, "reason": "Incorrect. In accordance with.", "trapCategory": "meaning"},
                    {"text": "うちに", "isCorrect": False, "reason": "Incorrect. While temporary condition lasts.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What pattern means 'every single time [action happens]'?"
        },
        {
            "id": "skm3-c2-ex-4",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 2",
            "type": "multiple-choice",
            "context": "Proportional correlation: the more you practice, the more skillful you become.",
            "question": "練習すれ（　　）上手になります。",
            "translation": "The more you practice, the more skillful you become.",
            "options": ["ば練習するほど", "ば練習するたびに", "ば練習するとおり", "ば練習するうちに"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u2-ba-hodo-proportion",
            "grammarPointTitle": "(〜ば)〜ほど (Proportional Correlation: The More... The More...)",
            "explanation": {
                "overall": "The proportional correlation pattern 'the more X, the more Y' is: [Verb-ba] + [Verb-dict] + ほど (練習すれば練習するほど).",
                "options": [
                    {"text": "ば練習するほど", "isCorrect": True, "reason": "Correct. Proportional correlation formula: 〜ば〜ほど.", "trapCategory": "formation"},
                    {"text": "ば練習するたびに", "isCorrect": False, "reason": "Incorrect. Ungrammatical mixture.", "trapCategory": "formation"},
                    {"text": "ば練習するとおり", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "ば練習するうちに", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the formula for 'the more [X], the more [Y]'?"
        },
        {
            "id": "skm3-c2-ex-5",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 2",
            "type": "multiple-choice",
            "context": "Taking advantage of a main trip to perform a convenient side errand: posting a letter while out on a walk.",
            "question": "散歩の（　　）、ポストに手紙を入れてきてくれませんか。",
            "translation": "While you are out on your walk, could you drop this letter in the postbox?",
            "options": ["ついでに", "たびに", "うちに", "とおりに"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u2-tsuide-ni-opportunity",
            "grammarPointTitle": "〜ついでに (While at It / Seizing Opportunity for a Side Task)",
            "explanation": {
                "overall": "〜ついでに means taking advantage of a primary journey or action to conveniently perform a secondary errand (散歩のついでに).",
                "options": [
                    {"text": "ついでに", "isCorrect": True, "reason": "Correct. Incidental secondary task: Noun のついでに / V-dict ついでに.", "trapCategory": "meaning"},
                    {"text": "たびに", "isCorrect": False, "reason": "Incorrect. Every single time.", "trapCategory": "meaning"},
                    {"text": "うちに", "isCorrect": False, "reason": "Incorrect. While condition lasts.", "trapCategory": "meaning"},
                    {"text": "とおりに", "isCorrect": False, "reason": "Incorrect. In accordance with.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern means 'while you are at it / taking advantage of the opportunity'?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_skm3_exercises()
    print(f"Generated {len(ex_list)} SKM N3 exercises.")
