import json

def get_exercises_l2_to_l6():
    exercises = []

    # ------------------ LESSON 2 ------------------
    exercises.extend([
        {
            "id": "g1-l2-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Speaker holds a small black umbrella in their own hand while asking the listener.",
            "question": "A:「（　　）は誰の傘ですか。」 B:「それはメアリーさんのです。」",
            "translation": "A: 'Whose umbrella is this (near me)?' B: 'That is Mary's.'",
            "options": ["これ", "それ", "あれ", "どれ"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-kore-sore-are-dore",
            "grammarPointTitle": "これ・それ・あれ・どれ (Thing Demonstrative Pronouns)",
            "explanation": {
                "overall": "これ refers to an object located close to the speaker. The responder appropriately shifts the perspective to それ ('that near you').",
                "options": [
                    {"text": "これ", "isCorrect": True, "reason": "Correct. Refers to an object in the speaker's own hand or physical zone.", "trapCategory": "context"},
                    {"text": "それ", "isCorrect": False, "reason": "Incorrect. それ refers to an object close to the listener, not in the speaker's own hand.", "trapCategory": "meaning"},
                    {"text": "あれ", "isCorrect": False, "reason": "Incorrect. あれ refers to an object distant from both speaker and listener.", "trapCategory": "meaning"},
                    {"text": "どれ", "isCorrect": False, "reason": "Incorrect. どれ is the question word 'which one' and cannot take a known demonstrative reference in this slot.", "trapCategory": "formation"}
                ]
            },
            "hint": "Select the pronoun for an item immediately held by the speaker."
        },
        {
            "id": "g1-l2-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Speaker points to a dictionary sitting right on the listener's desk.",
            "question": "（　　）辞書はスミスさんのですか。",
            "translation": "Is that dictionary (near you) Mr. Smith's?",
            "options": ["その", "この", "あの", "どの"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-kono-sono-ano-dono",
            "grammarPointTitle": "この・その・あの・どの + Noun (Pre-Noun Demonstrative Modifiers)",
            "explanation": {
                "overall": "その modifies a noun located in the listener's immediate sphere. Unlike それ, その directly precedes a noun.",
                "options": [
                    {"text": "その", "isCorrect": True, "reason": "Correct. Pre-noun adnominal modifier pointing to an object close to the listener.", "trapCategory": "context"},
                    {"text": "この", "isCorrect": False, "reason": "Incorrect. この points to an object close to the speaker.", "trapCategory": "meaning"},
                    {"text": "あの", "isCorrect": False, "reason": "Incorrect. あの points to an object distant from both participants.", "trapCategory": "meaning"},
                    {"text": "どの", "isCorrect": False, "reason": "Incorrect. どの is interrogative ('which dictionary?'), but this sentence asks if it is Mr. Smith's.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which demonstrative adnominal refers to items near the conversational partner?"
        },
        {
            "id": "g1-l2-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Both speaker and listener look across the street at a tall white building in the distance.",
            "question": "（　　）は大学の図書館です。",
            "translation": "That over there (distant from both of us) is the university library.",
            "options": ["あれ", "これ", "それ", "ここ"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-kore-sore-are-dore",
            "grammarPointTitle": "これ・それ・あれ・どれ (Thing Demonstrative Pronouns)",
            "explanation": {
                "overall": "あれ refers to a thing or landmark positioned far from both the speaker and the listener.",
                "options": [
                    {"text": "あれ", "isCorrect": True, "reason": "Correct. Used for a referent physically distant from both speaker and listener.", "trapCategory": "context"},
                    {"text": "これ", "isCorrect": False, "reason": "Incorrect. これ indicates proximity to speaker.", "trapCategory": "meaning"},
                    {"text": "それ", "isCorrect": False, "reason": "Incorrect. それ indicates proximity to listener.", "trapCategory": "meaning"},
                    {"text": "ここ", "isCorrect": False, "reason": "Incorrect. ここ means 'this place right here', not a distant landmark across the street.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Identify the pronoun for an item distant from both people."
        },
        {
            "id": "g1-l2-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Three coats are hung on the wall. You are asking which one belongs to Mary.",
            "question": "メアリーさんのコートは（　　）ですか。",
            "translation": "Which one is Mary's coat?",
            "options": ["どれ", "どの", "だれ", "何"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-kore-sore-are-dore",
            "grammarPointTitle": "これ・それ・あれ・どれ (Thing Demonstrative Pronouns)",
            "explanation": {
                "overall": "どれ is the question pronoun meaning 'which one' among three or more items. It stands alone as a noun predicate before ですか.",
                "options": [
                    {"text": "どれ", "isCorrect": True, "reason": "Correct. Independent interrogative pronoun 'which one'.", "trapCategory": "formation"},
                    {"text": "どの", "isCorrect": False, "reason": "Incorrect. どの cannot stand alone before ですか; it must precede a noun (e.g. どのコート).", "trapCategory": "formation"},
                    {"text": "だれ", "isCorrect": False, "reason": "Incorrect. だれ asks 'who', but the coat is an object.", "trapCategory": "meaning"},
                    {"text": "何", "isCorrect": False, "reason": "Incorrect. 何 asks 'what' in general, not 'which one' among a specific group.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which question word stands alone to ask 'which one' among three or more choices?"
        },
        {
            "id": "g1-l2-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Visitor enters a department store and asks the receptionist for the post office counter.",
            "question": "A:「すみません、郵便局は（　　）ですか。」 B:「あそこです。」",
            "translation": "A: 'Excuse me, where is the post office?' B: 'It is over there.'",
            "options": ["どこ", "どれ", "だれ", "どう"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-koko-soko-asoko-doko",
            "grammarPointTitle": "ここ・そこ・あそこ・どこ (Place Demonstrative Pronouns)",
            "explanation": {
                "overall": "どこ asks for location ('where'). The receptionist responds with the spatial place pronoun あそこ ('over there').",
                "options": [
                    {"text": "どこ", "isCorrect": True, "reason": "Correct. Question word for place/location.", "trapCategory": "context"},
                    {"text": "どれ", "isCorrect": False, "reason": "Incorrect. どれ asks 'which thing', not where a place is.", "trapCategory": "meaning"},
                    {"text": "だれ", "isCorrect": False, "reason": "Incorrect. だれ asks 'who'.", "trapCategory": "meaning"},
                    {"text": "どう", "isCorrect": False, "reason": "Incorrect. どう asks 'how' or 'in what manner'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Identify the interrogative pronoun specifically used to inquire about location."
        },
        {
            "id": "g1-l2-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "You find an umbrella left behind in the classroom and ask around to locate the owner.",
            "question": "これは（　　）傘ですか。",
            "translation": "Whose umbrella is this?",
            "options": ["だれの", "だれ", "どれの", "何の"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-2-1",
            "grammarPointTitle": "だれの・ね・よ",
            "explanation": {
                "overall": "だれの (who + genitive particle の) means 'whose' when modifying a following noun.",
                "options": [
                    {"text": "だれの", "isCorrect": True, "reason": "Correct. だれ (who) + の creates the possessive modifier 'whose'.", "trapCategory": "formation"},
                    {"text": "だれ", "isCorrect": False, "reason": "Incorrect. だれ cannot directly modify the noun 傘 without the particle の.", "trapCategory": "formation"},
                    {"text": "どれの", "isCorrect": False, "reason": "Incorrect. どれ asks 'which thing', not who owns the umbrella.", "trapCategory": "meaning"},
                    {"text": "何の", "isCorrect": False, "reason": "Incorrect. 何の傘 asks what type of umbrella it is, not whose it is.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Form the interrogative modifier for possession: 'whose + noun'."
        },
        {
            "id": "g1-l2-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Takeshi has just introduced himself as a second-year student. Mary then states her own status.",
            "question": "たけしさんは二年生です。メアリーさん（　　）二年生です。",
            "translation": "Takeshi is a sophomore. Mary is also a sophomore.",
            "options": ["も", "は", "が", "の"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-mo-particle",
            "grammarPointTitle": "助詞「も」 (Inclusive Particle 'Also / Too')",
            "explanation": {
                "overall": "Particle も replaces は to indicate that the same predicate ('is a sophomore') holds true for the second person ('Mary too').",
                "options": [
                    {"text": "も", "isCorrect": True, "reason": "Correct. Replaces topic marker は to indicate inclusion ('also/too').", "trapCategory": "context"},
                    {"text": "は", "isCorrect": False, "reason": "Incorrect. While grammatically possible in isolation, は fails to express the intended inclusive relationship established by the preceding sentence.", "trapCategory": "context"},
                    {"text": "が", "isCorrect": False, "reason": "Incorrect. が creates exhaustive focus or subject contrast, which contradicts the inclusive context.", "trapCategory": "meaning"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. の makes Mary a possessive modifier, leaving the sentence without a grammatical subject/topic.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle replaces は to indicate that another person shares the exact same trait?"
        },
        {
            "id": "g1-l2-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Casual everyday conversation between classmates. Asked if you are a first-year student.",
            "question": "A:「一年生ですか。」 B:「いいえ、一年生（　　）。三年生です。」",
            "translation": "A: 'Are you a first-year student?' B: 'No, I am not a first-year. I am a third-year.'",
            "options": ["じゃないです", "です", "でした", "くないです"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-janai-desu",
            "grammarPointTitle": "じゃないです / じゃありません (Negative Copula: Is Not)",
            "explanation": {
                "overall": "じゃないです is the standard conversational negative form of です for noun predicates.",
                "options": [
                    {"text": "じゃないです", "isCorrect": True, "reason": "Correct. Standard polite spoken negation for noun predicates.", "trapCategory": "formation"},
                    {"text": "です", "isCorrect": False, "reason": "Incorrect. です is affirmative, contradicting 'いいえ'.", "trapCategory": "meaning"},
                    {"text": "でした", "isCorrect": False, "reason": "Incorrect. でした is past tense affirmative ('was').", "trapCategory": "meaning"},
                    {"text": "くないです", "isCorrect": False, "reason": "Incorrect. 〜くないです is the negative ending for い-adjectives, never attached to nouns.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the polite spoken negative form of the copula です for nouns?"
        },
        {
            "id": "g1-l2-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Formal polite speech in a business or academic interview setting.",
            "question": "山田先生は英語の先生（　　）。日本語の先生です。",
            "translation": "Prof. Yamada is not an English teacher. He is a Japanese teacher.",
            "options": ["じゃありません", "ありません", "ないです", "じゃあります"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-janai-desu",
            "grammarPointTitle": "じゃないです / じゃありません (Negative Copula: Is Not)",
            "explanation": {
                "overall": "じゃありません (or ではございません in formal registers) is the formal polite negative copula corresponding to です.",
                "options": [
                    {"text": "じゃありません", "isCorrect": True, "reason": "Correct. Formal polite negative copula for noun predicates.", "trapCategory": "formation"},
                    {"text": "ありません", "isCorrect": False, "reason": "Incorrect. ありません is the negative of the verb あります (inanimate existence), not the copula.", "trapCategory": "formation"},
                    {"text": "ないです", "isCorrect": False, "reason": "Incorrect. ないです requires the particle じゃ before it when negating a noun predicate.", "trapCategory": "formation"},
                    {"text": "じゃあります", "isCorrect": False, "reason": "Incorrect. Ungrammatical pseudo-construction.", "trapCategory": "formation"}
                ]
            },
            "hint": "Select the formal counterpart to じゃないです for negating noun predicates."
        },
        {
            "id": "g1-l2-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Two friends step outside into bright sunshine and warm breeze together.",
            "question": "今日はいい天気です（　　）。",
            "translation": "It is lovely weather today, isn't it?",
            "options": ["ね", "よ", "か", "わ"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-2-1",
            "grammarPointTitle": "だれの・ね・よ",
            "explanation": {
                "overall": "Sentence-ending particle ね requests agreement from the listener on a shared observation ('isn't it?').",
                "options": [
                    {"text": "ね", "isCorrect": True, "reason": "Correct. Requests mutual agreement or confirmation on shared facts.", "trapCategory": "context"},
                    {"text": "よ", "isCorrect": False, "reason": "Incorrect. よ conveys new information the listener is presumed not to know, inappropriate when both are looking at the sky.", "trapCategory": "meaning"},
                    {"text": "か", "isCorrect": False, "reason": "Incorrect. か turns the sentence into an inquiry ('Is it good weather?'), which is unnatural when standing outdoors together.", "trapCategory": "context"},
                    {"text": "わ", "isCorrect": False, "reason": "Incorrect. わ is an emphatic marker, not a consensus-seeking particle.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which sentence-ending particle seeks the listener's agreement on an obvious shared reality?"
        },
        {
            "id": "g1-l2-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "A customer is walking away leaving their jacket behind. The clerk calls out to inform them.",
            "question": "すみません、そのジャケットは田中さんのです（　　）！",
            "translation": "Excuse me, that jacket is yours, Mr. Tanaka (I am telling you)! / Don't forget it!",
            "options": ["よ", "ね", "か", "の"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-2-1",
            "grammarPointTitle": "だれの・ね・よ",
            "explanation": {
                "overall": "Sentence-ending particle よ provides authoritative or new information to a listener who does not yet realize it.",
                "options": [
                    {"text": "よ", "isCorrect": True, "reason": "Correct. Imparts information the speaker believes the listener does not know or has overlooked.", "trapCategory": "context"},
                    {"text": "ね", "isCorrect": False, "reason": "Incorrect. ね assumes the listener already knows and agrees, which defeats the purpose of an alert.", "trapCategory": "meaning"},
                    {"text": "か", "isCorrect": False, "reason": "Incorrect. か turns it into a question, but the clerk is informing Mr. Tanaka.", "trapCategory": "meaning"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. の alone here functions as a casual question/explanation marker.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle is used to give authoritative new information or an alert?"
        },
        {
            "id": "g1-l2-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 2",
            "type": "multiple-choice",
            "context": "Speaker points directly to a particular book on the counter before buying it.",
            "question": "（　　）本をください。",
            "translation": "Please give me this book.",
            "options": ["この", "これ", "ここ", "こんな"],
            "correctIndex": 0,
            "grammarPointId": "g1-l2-kono-sono-ano-dono",
            "grammarPointTitle": "この・その・あの・どの + Noun (Pre-Noun Demonstrative Modifiers)",
            "explanation": {
                "overall": "この must directly precede a noun (この本). これ is an independent pronoun and cannot modify a noun directly (*これ本).",
                "options": [
                    {"text": "この", "isCorrect": True, "reason": "Correct. Pre-noun adnominal modifier required before a noun.", "trapCategory": "formation"},
                    {"text": "これ", "isCorrect": False, "reason": "Incorrect. これ is a pronoun; 'これ本' is ungrammatical (would require これの本 or just これ).", "trapCategory": "formation"},
                    {"text": "ここ", "isCorrect": False, "reason": "Incorrect. ここ means 'this place', not 'this book'.", "trapCategory": "meaning"},
                    {"text": "こんな", "isCorrect": False, "reason": "Incorrect. こんな means 'this kind of', altering the demonstrative meaning.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which demonstrative word must be followed directly by a noun?"
        }
    ])

    # ------------------ LESSON 3 ------------------
    exercises.extend([
        {
            "id": "g1-l3-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Talking about daily breakfast habits. The verb is 食べる (Ru-verb).",
            "question": "私は毎朝七時にパンを（　　）。",
            "translation": "I eat bread every morning at 7:00.",
            "options": ["食べます", "食べります", "飲みます", "食べません"],
            "correctIndex": 0,
            "grammarPointId": "g1-l3-masu-form",
            "grammarPointTitle": "〜ます / 〜ません (Polite Non-Past Affirmative & Negative)",
            "explanation": {
                "overall": "食べる is a Ru-verb (stem ends in -e). Conjugation rule: drop -ru and add -masu -> 食べます.",
                "options": [
                    {"text": "食べます", "isCorrect": True, "reason": "Correct. Ru-verb: drop -ru and append -masu.", "trapCategory": "formation"},
                    {"text": "食べります", "isCorrect": False, "reason": "Incorrect. 食べる is not an U-verb; -ri-masu is an overgeneralization error.", "trapCategory": "formation"},
                    {"text": "飲みます", "isCorrect": False, "reason": "Incorrect. 飲む means to drink, not eat bread.", "trapCategory": "meaning"},
                    {"text": "食べません", "isCorrect": False, "reason": "Incorrect. Negative ('do not eat'), contradicting the habitual affirmative statement.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Conjugate the Ru-verb 食べる into polite non-past affirmative."
        },
        {
            "id": "g1-l3-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating that you drink green tea every day. The verb is 飲む (U-verb).",
            "question": "私は毎日お茶を（　　）。",
            "translation": "I drink green tea every day.",
            "options": ["飲みます", "飲ます", "飲みます", "飲めません"],
            "correctIndex": 0,
            "grammarPointId": "g1-l3-masu-form",
            "grammarPointTitle": "〜ます / 〜ません (Polite Non-Past Affirmative & Negative)",
            "explanation": {
                "overall": "飲む is an U-verb ending in -mu. Conjugation rule: change final -u vowel to -i vowel (-mi) and add -masu -> 飲みます.",
                "options": [
                    {"text": "飲みます", "isCorrect": True, "reason": "Correct. U-verb mu -> mi + masu.", "trapCategory": "formation"},
                    {"text": "飲ます", "isCorrect": False, "reason": "Incorrect. Causative stem error.", "trapCategory": "formation"},
                    {"text": "飲めません", "isCorrect": False, "reason": "Incorrect. Potential negative form ('cannot drink').", "trapCategory": "formation"},
                    {"text": "飲んだ", "isCorrect": False, "reason": "Incorrect. Casual past form.", "trapCategory": "formation"}
                ]
            },
            "hint": "Conjugate the U-verb 飲む into polite non-past affirmative."
        },
        {
            "id": "g1-l3-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating that you do Japanese homework in the evening. The verb is する (irregular).",
            "question": "今晩、日本語の宿題を（　　）。",
            "translation": "I will do my Japanese homework this evening.",
            "options": ["します", "すます", "されます", "しませんでした"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-2",
            "grammarPointTitle": "動詞の活用・語順・助詞",
            "explanation": {
                "overall": "Genki I identifies する as one of the two irregular verbs. Its polite non-past affirmative stem is し -> します.",
                "options": [
                    {"text": "します", "isCorrect": True, "reason": "Correct. する irreg stem is shi -> します.", "trapCategory": "formation"},
                    {"text": "すます", "isCorrect": False, "reason": "Incorrect. する does not conjugate regularly like an U-verb.", "trapCategory": "formation"},
                    {"text": "されます", "isCorrect": False, "reason": "Incorrect. Passive/honorific form.", "trapCategory": "formation"},
                    {"text": "しませんでした", "isCorrect": False, "reason": "Incorrect. Past negative ('did not do'), contradicting future/plan '今晩'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the polite affirmative masu-form of the irregular verb する?"
        },
        {
            "id": "g1-l3-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating that you do not watch television on weekdays.",
            "question": "平日はテレビを（　　）。",
            "translation": "I do not watch TV on weekdays.",
            "options": ["見ません", "見ます", "見ないです", "見ませんでした"],
            "correctIndex": 0,
            "grammarPointId": "g1-l3-masu-form",
            "grammarPointTitle": "〜ます / 〜ません (Polite Non-Past Affirmative & Negative)",
            "explanation": {
                "overall": "Polite non-past negation replaces -masu with -masen -> 見ません.",
                "options": [
                    {"text": "見ません", "isCorrect": True, "reason": "Correct. Standard polite non-past negative form.", "trapCategory": "formation"},
                    {"text": "見ます", "isCorrect": False, "reason": "Incorrect. Affirmative ('I watch').", "trapCategory": "meaning"},
                    {"text": "見ないです", "isCorrect": False, "reason": "Incorrect. Less formal hybrid form; standard Genki I polite textbook form is 〜ません.", "trapCategory": "formation"},
                    {"text": "見ませんでした", "isCorrect": False, "reason": "Incorrect. Past negative ('did not watch'), but sentence describes habitual weekday behavior.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Form the polite non-past negative of 見る."
        },
        {
            "id": "g1-l3-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating that you read the morning newspaper. Direct object relationship.",
            "question": "毎朝、新聞（　　）読みます。",
            "translation": "I read the newspaper every morning.",
            "options": ["を", "で", "に", "へ"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-2",
            "grammarPointTitle": "動詞の活用・語順・助詞",
            "explanation": {
                "overall": "The particle を marks the direct object of a transitive action (what is being read).",
                "options": [
                    {"text": "を", "isCorrect": True, "reason": "Correct. Marks direct object of 読みます.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で marks location of action or instrument, not direct object.", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に marks time, target, or destination, not the object read.", "trapCategory": "meaning"},
                    {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ marks direction of movement.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the direct object of a transitive verb?"
        },
        {
            "id": "g1-l3-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating the physical location where the dynamic action of studying takes place.",
            "question": "図書館（　　）日本語を勉強します。",
            "translation": "I study Japanese at the library.",
            "options": ["で", "に", "を", "へ"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-2",
            "grammarPointTitle": "動詞の活用・語順・助詞",
            "explanation": {
                "overall": "The particle で marks the setting/location where a dynamic activity occurs (勉強する occurs at 図書館).",
                "options": [
                    {"text": "で", "isCorrect": True, "reason": "Correct. Marks location of dynamic activity.", "trapCategory": "formation"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に marks location of existence (with あります/います) or destination of motion, not dynamic study action.", "trapCategory": "meaning"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. を marks direct object; you do not study the library itself.", "trapCategory": "meaning"},
                    {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ indicates direction of motion verbs (行く/来る), not study activity.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the location where a dynamic action takes place?"
        },
        {
            "id": "g1-l3-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating destination of movement towards Tokyo with verb 行く.",
            "question": "週末、東京（　　）行きます。",
            "translation": "I will go to Tokyo this weekend.",
            "options": ["に", "で", "を", "から"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-2",
            "grammarPointTitle": "動詞の活用・語順・助詞",
            "explanation": {
                "overall": "The particles に and へ mark the destination or goal of motion verbs (行く, 来る, 帰る).",
                "options": [
                    {"text": "に", "isCorrect": True, "reason": "Correct. Marks goal/destination of motion verb 行きます.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で marks means of transit (電車で) or activity place, not destination.", "trapCategory": "meaning"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. Tokyo is not a direct object being acted on.", "trapCategory": "meaning"},
                    {"text": "から", "isCorrect": False, "reason": "Incorrect. から indicates origin ('from Tokyo'), reversing the sentence direction.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the goal/destination of motion verbs like 行く?"
        },
        {
            "id": "g1-l3-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Specifying an exact clock time when you wake up in the morning.",
            "question": "私は毎朝六時半（　　）起きます。",
            "translation": "I wake up at 6:30 every morning.",
            "options": ["に", "で", "を", "（助詞なし）"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-3",
            "grammarPointTitle": "時間のに・頻度の副詞",
            "explanation": {
                "overall": "Specific time points containing numbers (six-thirty, Sundays, May 5th) take the particle に.",
                "options": [
                    {"text": "に", "isCorrect": True, "reason": "Correct. Specific numerical clock times require に.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で does not mark specific time points.", "trapCategory": "meaning"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. Time is not a direct object.", "trapCategory": "formation"},
                    {"text": "（助詞なし）", "isCorrect": False, "reason": "Incorrect. Numerical clock times require に in standard Japanese.", "trapCategory": "formation"}
                ]
            },
            "hint": "Do specific clock times with numbers take particle に?"
        },
        {
            "id": "g1-l3-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Talking about an action happening today. The word is 今日.",
            "question": "（　　）友達と晩ご飯を食べます。",
            "translation": "Today I will eat dinner with my friend.",
            "options": ["今日", "今日に", "今日で", "今日を"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-3",
            "grammarPointTitle": "時間のに・頻度の副詞",
            "explanation": {
                "overall": "Relative time words (今日, あした, 昨日, 毎日, 今晩) do NOT take the particle に in Japanese.",
                "options": [
                    {"text": "今日", "isCorrect": True, "reason": "Correct. Relative time words stand alone as adverbial time phrases without に.", "trapCategory": "formation"},
                    {"text": "今日に", "isCorrect": False, "reason": "Incorrect. Overgeneralizing に to relative time words is a frequent learner mistake.", "trapCategory": "formation"},
                    {"text": "今日で", "isCorrect": False, "reason": "Incorrect. で implies 'ending as of today', altering the meaning.", "trapCategory": "meaning"},
                    {"text": "今日を", "isCorrect": False, "reason": "Incorrect. 今日 cannot be a direct object here.", "trapCategory": "formation"}
                ]
            },
            "hint": "Does the relative time word 今日 take particle に?"
        },
        {
            "id": "g1-l3-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating that you frequently/often listen to music.",
            "question": "私は（　　）音楽を聞きます。",
            "translation": "I often listen to music.",
            "options": ["よく", "あまり", "ぜんぜん", "まったく"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-3",
            "grammarPointTitle": "時間のに・頻度の副詞",
            "explanation": {
                "overall": "よく means 'often/frequently' and pairs with affirmative predicates. あまり and ぜんぜん pair with negative predicates.",
                "options": [
                    {"text": "よく", "isCorrect": True, "reason": "Correct. Frequency adverb 'often', pairs with affirmative verbs.", "trapCategory": "formation"},
                    {"text": "あまり", "isCorrect": False, "reason": "Incorrect. あまり requires a negative verb (あまり聞きません).", "trapCategory": "formation"},
                    {"text": "ぜんぜん", "isCorrect": False, "reason": "Incorrect. ぜんぜん requires a negative verb (ぜんぜん聞きません).", "trapCategory": "formation"},
                    {"text": "まったく", "isCorrect": False, "reason": "Incorrect. まったく requires a negative verb in standard usage.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which frequency adverb meaning 'often' pairs naturally with affirmative verbs?"
        },
        {
            "id": "g1-l3-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Stating that you rarely / not very often drink coffee.",
            "question": "私は（　　）コーヒーを飲みません。",
            "translation": "I do not drink coffee very often / rarely drink coffee.",
            "options": ["あまり", "よく", "いつも", "たくさん"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-3-3",
            "grammarPointTitle": "時間のに・頻度の副詞",
            "explanation": {
                "overall": "あまり + negative verb means 'not much / not very often'.",
                "options": [
                    {"text": "あまり", "isCorrect": True, "reason": "Correct. Polarity-sensitive frequency adverb paired with negative verb.", "trapCategory": "formation"},
                    {"text": "よく", "isCorrect": False, "reason": "Incorrect. よく pairs with affirmative verbs ('often drinks').", "trapCategory": "formation"},
                    {"text": "いつも", "isCorrect": False, "reason": "Incorrect. いつも means 'always', clashing with negative habitual negation.", "trapCategory": "meaning"},
                    {"text": "たくさん", "isCorrect": False, "reason": "Incorrect. たくさん means 'a lot' and takes affirmative.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which adverb pairs with negative verbs to mean 'not very often'?"
        },
        {
            "id": "g1-l3-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 3",
            "type": "multiple-choice",
            "context": "Politely inviting a classmate to have lunch together at noon.",
            "question": "明日、一緒に昼ご飯を食べ（　　）。",
            "translation": "Won't you eat lunch together with me tomorrow? / Would you like to have lunch tomorrow?",
            "options": ["ませんか", "ますか", "ましょう", "てください"],
            "correctIndex": 0,
            "grammarPointId": "g1-l3-masenka-invitation",
            "grammarPointTitle": "〜ませんか (Polite Invitation: Won't You? / Would You Like To?)",
            "explanation": {
                "overall": "〜ませんか is the standard polite formula for extending an invitation, politely giving the listener room to decline.",
                "options": [
                    {"text": "ませんか", "isCorrect": True, "reason": "Correct. Polite invitation form ('Won't you...?').", "trapCategory": "context"},
                    {"text": "ますか", "isCorrect": False, "reason": "Incorrect. 〜ますか simply asks whether the person eats lunch, rather than inviting them.", "trapCategory": "meaning"},
                    {"text": "ましょう", "isCorrect": False, "reason": "Incorrect. 〜ましょう is a direct suggestion ('let's eat') rather than a polite invitation asking their willingness.", "trapCategory": "meaning"},
                    {"text": "てください", "isCorrect": False, "reason": "Incorrect. 〜てください is a request ('please eat'), not an invitation to join.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the polite grammatical pattern for inviting someone to do an activity together?"
        }
    ])

    # ------------------ LESSON 4 ------------------
    exercises.extend([
        {
            "id": "g1-l4-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Describing the contents of a study room. The item is a dictionary (inanimate object).",
            "question": "机の上に辞書が（　　）。",
            "translation": "There is a dictionary on the desk.",
            "options": ["あります", "います", "します", "です"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-4-4",
            "grammarPointTitle": "あります・います",
            "explanation": {
                "overall": "あります is used for the existence of inanimate objects, plants, and non-moving items. Dictionaries are inanimate.",
                "options": [
                    {"text": "あります", "isCorrect": True, "reason": "Correct. Inanimate existence verb.", "trapCategory": "formation"},
                    {"text": "います", "isCorrect": False, "reason": "Incorrect. います is reserved for animate, sentient living beings (people, animals).", "trapCategory": "meaning"},
                    {"text": "します", "isCorrect": False, "reason": "Incorrect. します means 'to do', not exist.", "trapCategory": "meaning"},
                    {"text": "です", "isCorrect": False, "reason": "Incorrect. '辞書がです' is incomplete; existence at a location requires あります.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which verb expresses the existence of inanimate items like books and desks?"
        },
        {
            "id": "g1-l4-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Looking into the classroom and noticing a cat sleeping on the floor. Animate animal.",
            "question": "教室に猫が（　　）。",
            "translation": "There is a cat in the classroom.",
            "options": ["います", "あります", "します", "きます"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-4-4",
            "grammarPointTitle": "あります・います",
            "explanation": {
                "overall": "います is used for the existence of sentient animate beings such as humans and animals.",
                "options": [
                    {"text": "います", "isCorrect": True, "reason": "Correct. Animate existence verb for animals and people.", "trapCategory": "formation"},
                    {"text": "あります", "isCorrect": False, "reason": "Incorrect. あります is only for inanimate objects.", "trapCategory": "meaning"},
                    {"text": "します", "isCorrect": False, "reason": "Incorrect. します means 'to do'.", "trapCategory": "meaning"},
                    {"text": "きます", "isCorrect": False, "reason": "Incorrect. きます means 'to come'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which verb expresses the existence of living creatures like cats and people?"
        },
        {
            "id": "g1-l4-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Specifying the location where the university bookstore exists.",
            "question": "大学の近く（　　）本屋があります。",
            "translation": "There is a bookstore near the university.",
            "options": ["に", "で", "を", "へ"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-4-4",
            "grammarPointTitle": "あります・います",
            "explanation": {
                "overall": "The particle に marks the location of existence when paired with あります or います (Place に Noun が あります/います).",
                "options": [
                    {"text": "に", "isCorrect": True, "reason": "Correct. Marks location of existence with あります/います.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で marks location of action, not static existence.", "trapCategory": "meaning"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. Location is not a direct object.", "trapCategory": "formation"},
                    {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ marks direction of movement.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks location of existence with あります/います?"
        },
        {
            "id": "g1-l4-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Telling someone their smartphone is on top of the dining table.",
            "question": "テーブルの（　　）にスマホがありますよ。",
            "translation": "Your smartphone is on top of the table.",
            "options": ["上", "下", "中", "後ろ"],
            "correctIndex": 0,
            "grammarPointId": "g1-l4-location-words",
            "grammarPointTitle": "位置の名詞 (Spatial Postpositions: 上・下・前・後ろ・中・隣・近く・間)",
            "explanation": {
                "overall": "上 (うえ) means on/above/on top of. Connected to the reference noun with の (テーブルの上).",
                "options": [
                    {"text": "上", "isCorrect": True, "reason": "Correct. Spatial position 'on top of'.", "trapCategory": "meaning"},
                    {"text": "下", "isCorrect": False, "reason": "Incorrect. 下 means 'under/beneath'.", "trapCategory": "meaning"},
                    {"text": "中", "isCorrect": False, "reason": "Incorrect. 中 means 'inside'.", "trapCategory": "meaning"},
                    {"text": "後ろ", "isCorrect": False, "reason": "Incorrect. 後ろ means 'behind'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which spatial noun means 'on top of'?"
        },
        {
            "id": "g1-l4-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Searching for a wallet and finding it enclosed inside the backpack.",
            "question": "かばんの（　　）に財布があります。",
            "translation": "The wallet is inside the bag.",
            "options": ["中", "前", "間", "隣"],
            "correctIndex": 0,
            "grammarPointId": "g1-l4-location-words",
            "grammarPointTitle": "位置の名詞 (Spatial Postpositions: 上・下・前・後ろ・中・隣・近く・間)",
            "explanation": {
                "overall": "中 (なか) means 'inside' an enclosed container or space.",
                "options": [
                    {"text": "中", "isCorrect": True, "reason": "Correct. Spatial position 'inside'.", "trapCategory": "meaning"},
                    {"text": "前", "isCorrect": False, "reason": "Incorrect. 前 means 'in front of'.", "trapCategory": "meaning"},
                    {"text": "間", "isCorrect": False, "reason": "Incorrect. 間 requires two reference points (A と B の間).", "trapCategory": "formation"},
                    {"text": "隣", "isCorrect": False, "reason": "Incorrect. 隣 means 'next to' (same category side-by-side).", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which spatial word means 'inside'?"
        },
        {
            "id": "g1-l4-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Giving directions. The bank is positioned between the department store and the station.",
            "question": "銀行はデパート（　　）駅の間です。",
            "translation": "The bank is between the department store and the station.",
            "options": ["と", "の", "に", "で"],
            "correctIndex": 0,
            "grammarPointId": "g1-l4-location-words",
            "grammarPointTitle": "位置の名詞 (Spatial Postpositions: 上・下・前・後ろ・中・隣・近く・間)",
            "explanation": {
                "overall": "The pattern for 'between A and B' is 'A と B の間'. Particle と connects the two flanking entities.",
                "options": [
                    {"text": "と", "isCorrect": True, "reason": "Correct. Connects flanking entities: A と B の間.", "trapCategory": "formation"},
                    {"text": "の", "isCorrect": False, "reason": "Incorrect. 'デパートの駅' would mean the department store's station.", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に cannot connect two nouns.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で cannot connect two nouns.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you connect the two entities in 'between A and B'?"
        },
        {
            "id": "g1-l4-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Reporting yesterday's completed activities. The verb is 勉強する.",
            "question": "きのう、図書館で五時間（　　）。",
            "translation": "Yesterday, I studied for five hours at the library.",
            "options": ["勉強しました", "勉強します", "勉強でした", "勉強しません"],
            "correctIndex": 0,
            "grammarPointId": "g1-l4-past-forms-deshita",
            "grammarPointTitle": "〜ました・〜ませんでした・〜でした (Polite Past Tense of Verbs & Copula)",
            "explanation": {
                "overall": "〜ました is the polite past affirmative form of verbs. きのう anchors the sentence in the past.",
                "options": [
                    {"text": "勉強しました", "isCorrect": True, "reason": "Correct. Polite past affirmative form of 勉強する.", "trapCategory": "formation"},
                    {"text": "勉強します", "isCorrect": False, "reason": "Incorrect. Non-past form contradicts 'きのう'.", "trapCategory": "meaning"},
                    {"text": "勉強でした", "isCorrect": False, "reason": "Incorrect. Treats 勉強 as a noun with copula でした, but cannot take location で without dynamic verb predicate.", "trapCategory": "formation"},
                    {"text": "勉強しません", "isCorrect": False, "reason": "Incorrect. Non-past negative.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the polite past affirmative ending for verbs?"
        },
        {
            "id": "g1-l4-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Stating that you did not watch TV yesterday due to exams.",
            "question": "きのうは忙しかったですから、テレビを（　　）。",
            "translation": "Because I was busy yesterday, I did not watch television.",
            "options": ["見ませんでした", "見ません", "見ました", "見なかったです"],
            "correctIndex": 0,
            "grammarPointId": "g1-l4-past-forms-deshita",
            "grammarPointTitle": "〜ました・〜ませんでした・〜でした (Polite Past Tense of Verbs & Copula)",
            "explanation": {
                "overall": "〜ませんでした is the polite past negative ending for verbs.",
                "options": [
                    {"text": "見ませんでした", "isCorrect": True, "reason": "Correct. Polite past negative form of 見る.", "trapCategory": "formation"},
                    {"text": "見ません", "isCorrect": False, "reason": "Incorrect. Non-past negative ('do not watch').", "trapCategory": "meaning"},
                    {"text": "見ました", "isCorrect": False, "reason": "Incorrect. Affirmative ('I watched').", "trapCategory": "meaning"},
                    {"text": "見なかったです", "isCorrect": False, "reason": "Incorrect. Colloquial hybrid; Genki I standard polite verb past negative is 〜ませんでした.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the standard polite past negative ending for verbs?"
        },
        {
            "id": "g1-l4-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Stating what day of the week yesterday was. Noun predicate.",
            "question": "きのうは日曜日（　　）。",
            "translation": "Yesterday was Sunday.",
            "options": ["でした", "です", "ありました", "ます"],
            "correctIndex": 0,
            "grammarPointId": "g1-l4-past-forms-deshita",
            "grammarPointTitle": "〜ました・〜ませんでした・〜でした (Polite Past Tense of Verbs & Copula)",
            "explanation": {
                "overall": "でした is the polite past affirmative form of the copula です for noun predicates.",
                "options": [
                    {"text": "でした", "isCorrect": True, "reason": "Correct. Polite past copula for nouns.", "trapCategory": "formation"},
                    {"text": "です", "isCorrect": False, "reason": "Incorrect. Non-past copula ('is Sunday').", "trapCategory": "meaning"},
                    {"text": "ありました", "isCorrect": False, "reason": "Incorrect. あります is existence verb ('Sunday existed'), not the copula.", "trapCategory": "formation"},
                    {"text": "ます", "isCorrect": False, "reason": "Incorrect. ます only attaches to verb stems, not nouns.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the polite past form of the copula です for noun predicates?"
        },
        {
            "id": "g1-l4-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Explaining that the day before yesterday was not a holiday.",
            "question": "おとといは休み（　　）。",
            "translation": "The day before yesterday was not a day off.",
            "options": ["じゃなかったです", "じゃないです", "でした", "くないでした"],
            "correctIndex": 0,
            "grammarPointId": "g1-l4-past-forms-deshita",
            "grammarPointTitle": "〜ました・〜ませんでした・〜でした (Polite Past Tense of Verbs & Copula)",
            "explanation": {
                "overall": "じゃなかったです (or じゃありませんでした) is the polite past negative form of the copula for nouns.",
                "options": [
                    {"text": "じゃなかったです", "isCorrect": True, "reason": "Correct. Polite past negative form of copula for nouns.", "trapCategory": "formation"},
                    {"text": "じゃないです", "isCorrect": False, "reason": "Incorrect. Non-past negative ('is not a day off').", "trapCategory": "meaning"},
                    {"text": "でした", "isCorrect": False, "reason": "Incorrect. Affirmative ('was a day off').", "trapCategory": "meaning"},
                    {"text": "くないでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical hybrid construction.", "trapCategory": "formation"}
                ]
            },
            "hint": "Form the polite past negative of the noun predicate 休みです."
        },
        {
            "id": "g1-l4-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "At the stationery store, buying both a pen and a notebook.",
            "question": "ペン（　　）ノートを買いました。",
            "translation": "I bought a pen and a notebook.",
            "options": ["と", "も", "や", "に"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-4-5",
            "grammarPointTitle": "時間・数量・と",
            "explanation": {
                "overall": "The particle と connects nouns in an exhaustive list ('A and B').",
                "options": [
                    {"text": "と", "isCorrect": True, "reason": "Correct. Exhaustive noun connector 'and'.", "trapCategory": "formation"},
                    {"text": "も", "isCorrect": False, "reason": "Incorrect. も would require ペンもノートも買いました.", "trapCategory": "formation"},
                    {"text": "や", "isCorrect": False, "reason": "Incorrect. や is non-exhaustive ('things like A and B'), introduced in later chapters.", "trapCategory": "meaning"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に cannot connect two nouns in a coordinate noun phrase.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which particle connects nouns to mean 'and'?"
        },
        {
            "id": "g1-l4-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 4",
            "type": "multiple-choice",
            "context": "Describing how long you waited for Mary at the coffee shop.",
            "question": "喫茶店でメアリーさんを（　　）待ちました。",
            "translation": "I waited for Mary at the coffee shop for one hour.",
            "options": ["一時間", "一時間に", "一時間で", "一時間を"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-4-5",
            "grammarPointTitle": "時間・数量・と",
            "explanation": {
                "overall": "Duration expressions (like 一時間, 三十分) stand directly as adverbs without any particle.",
                "options": [
                    {"text": "一時間", "isCorrect": True, "reason": "Correct. Duration nouns stand adverbially without particles.", "trapCategory": "formation"},
                    {"text": "一時間に", "isCorrect": False, "reason": "Incorrect. に marks frequency per unit (e.g. 一週間に一回), not total elapsed duration.", "trapCategory": "formation"},
                    {"text": "一時間で", "isCorrect": False, "reason": "Incorrect. で indicates time limit ('within one hour').", "trapCategory": "meaning"},
                    {"text": "一時間を", "isCorrect": False, "reason": "Incorrect. Duration is not the grammatical direct object of 待つ.", "trapCategory": "formation"}
                ]
            },
            "hint": "Do duration expressions like 'for one hour' take particle に?"
        }
    ])

    # ------------------ LESSON 5 ------------------
    exercises.extend([
        {
            "id": "g1-l5-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Stating that the food at the school cafeteria is not expensive.",
            "question": "学食の食べ物は（　　）。",
            "translation": "The food at the cafeteria is not expensive.",
            "options": ["高くないです", "高いじゃないです", "高くないでした", "高かったです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "い-adjective non-past negative: drop final い and append くないです (or くありません) -> 高くないです.",
                "options": [
                    {"text": "高くないです", "isCorrect": True, "reason": "Correct. い-adjective negative rule: -i -> -kunai desu.", "trapCategory": "formation"},
                    {"text": "高いじゃないです", "isCorrect": False, "reason": "Incorrect. じゃないです cannot be attached to an い-adjective without dropping い and using colloquialism; textbook grammar strictly requires くないです.", "trapCategory": "formation"},
                    {"text": "高くないでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical hybrid past form.", "trapCategory": "formation"},
                    {"text": "高かったです", "isCorrect": False, "reason": "Incorrect. Past affirmative ('was expensive').", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the non-past negative conjugation rule for い-adjectives?"
        },
        {
            "id": "g1-l5-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Talking about the winter weather yesterday. It was very cold.",
            "question": "きのうはとても（　　）。",
            "translation": "Yesterday was very cold.",
            "options": ["寒かったです", "寒いでした", "寒いです", "寒くないです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "い-adjective past affirmative: drop final い and append かったです -> 寒かったです.",
                "options": [
                    {"text": "寒かったです", "isCorrect": True, "reason": "Correct. い-adjective past affirmative: -i -> -katta desu.", "trapCategory": "formation"},
                    {"text": "寒いでした", "isCorrect": False, "reason": "Incorrect. Major learner mistake: でした cannot attach directly to plain い-adjective.", "trapCategory": "formation"},
                    {"text": "寒いです", "isCorrect": False, "reason": "Incorrect. Present tense contradicts 'きのう'.", "trapCategory": "meaning"},
                    {"text": "寒くないです", "isCorrect": False, "reason": "Incorrect. Present negative ('is not cold').", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do you form the past affirmative of an い-adjective?"
        },
        {
            "id": "g1-l5-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Reviewing a movie watched last weekend that turned out boring.",
            "question": "その映画はあまり（　　）。",
            "translation": "That movie was not very interesting.",
            "options": ["面白くなかったです", "面白いじゃなかったです", "面白くないでした", "面白かったです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "い-adjective past negative: drop final い and append くなかったです -> 面白くなかったです.",
                "options": [
                    {"text": "面白くなかったです", "isCorrect": True, "reason": "Correct. い-adjective past negative: -i -> -kunakatta desu.", "trapCategory": "formation"},
                    {"text": "面白いじゃなかったです", "isCorrect": False, "reason": "Incorrect. じゃなかった attaches to nouns and な-adjectives, never い-adjectives.", "trapCategory": "formation"},
                    {"text": "面白くないでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical formation.", "trapCategory": "formation"},
                    {"text": "面白かったです", "isCorrect": False, "reason": "Incorrect. Affirmative ('was interesting'), clashing with 'あまり'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the past negative ending for an い-adjective?"
        },
        {
            "id": "g1-l5-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Stating that yesterday's weather was good. Adjective is いい.",
            "question": "きのうの天気は（　　）。",
            "translation": "Yesterday's weather was good.",
            "options": ["よかったです", "いいでした", "いかったです", "いくなかったです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "The adjective いい is irregular: all conjugations use the base よ- (よくない, よかった, よくなかった).",
                "options": [
                    {"text": "よかったです", "isCorrect": True, "reason": "Correct. Past affirmative of irregular いい is よかったです.", "trapCategory": "formation"},
                    {"text": "いいでした", "isCorrect": False, "reason": "Incorrect. いい cannot take でした directly.", "trapCategory": "formation"},
                    {"text": "いかったです", "isCorrect": False, "reason": "Incorrect. Overgeneralizing from ii without base shift to yo-.", "trapCategory": "formation"},
                    {"text": "いくなかったです", "isCorrect": False, "reason": "Incorrect. Ungrammatical stem.", "trapCategory": "formation"}
                ]
            },
            "hint": "Remember that the irregular adjective いい shifts to よ- in all conjugated forms."
        },
        {
            "id": "g1-l5-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Describing your apartment's neighborhood. It is bustling and noisy, not quiet.",
            "question": "私のアパートの周りは（　　）。",
            "translation": "My apartment's neighborhood is not quiet.",
            "options": ["静かじゃないです", "静かじゃない", "静かいくないです", "静かでした"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "な-adjectives conjugate exactly like noun predicates in polite sentences: 静かじゃないです / 静かじゃありません.",
                "options": [
                    {"text": "静かじゃないです", "isCorrect": True, "reason": "Correct. Polite non-past negative for な-adjectives.", "trapCategory": "formation"},
                    {"text": "静かいくないです", "isCorrect": False, "reason": "Incorrect. な-adjectives do not conjugate with -kunai desu.", "trapCategory": "formation"},
                    {"text": "静かじゃない", "isCorrect": False, "reason": "Incorrect. Casual short form, lacking polite です.", "trapCategory": "formation"},
                    {"text": "静かでした", "isCorrect": False, "reason": "Incorrect. Past affirmative ('was quiet').", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do な-adjectives conjugate in polite negative sentences?"
        },
        {
            "id": "g1-l5-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "A student was absent last week due to illness, but has recovered.",
            "question": "先週は病気でしたが、今は（　　）。",
            "translation": "I was sick last week, but now I am healthy / fine.",
            "options": ["元気です", "元気なです", "元気でした", "元気じゃないです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "In predicate position, a な-adjective drops な and takes です (元気です). It never keeps な before です (*元気なです).",
                "options": [
                    {"text": "元気です", "isCorrect": True, "reason": "Correct. Predicate form drops な: 元気 + です.", "trapCategory": "formation"},
                    {"text": "元気なです", "isCorrect": False, "reason": "Incorrect. な is only used before nouns (元気な人), never before です.", "trapCategory": "formation"},
                    {"text": "元気でした", "isCorrect": False, "reason": "Incorrect. Past tense contradicts '今は' (now).", "trapCategory": "meaning"},
                    {"text": "元気じゃないです", "isCorrect": False, "reason": "Incorrect. Negative contradicts recovery context.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Do な-adjectives keep the syllable な immediately before です in predicate position?"
        },
        {
            "id": "g1-l5-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Modifying a noun with a な-adjective: 'a quiet town'.",
            "question": "ここはとても（　　）町ですね。",
            "translation": "This is a very quiet town, isn't it?",
            "options": ["静かな", "静か", "静かに", "静かだ"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "When a な-adjective directly modifies a following noun, it must attach な (静かな町).",
                "options": [
                    {"text": "静かな", "isCorrect": True, "reason": "Correct. Pre-noun adnominal form requires な.", "trapCategory": "formation"},
                    {"text": "静か", "isCorrect": False, "reason": "Incorrect. Cannot omit な when modifying a noun.", "trapCategory": "formation"},
                    {"text": "静かに", "isCorrect": False, "reason": "Incorrect. 静かに is adverbial ('quietly'), modifying a verb, not a noun.", "trapCategory": "formation"},
                    {"text": "静かだ", "isCorrect": False, "reason": "Incorrect. だ cannot modify a noun directly.", "trapCategory": "formation"}
                ]
            },
            "hint": "What particle connects a な-adjective to the noun it modifies?"
        },
        {
            "id": "g1-l5-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Modifying a noun with an い-adjective: 'an interesting movie'.",
            "question": "きのう、（　　）映画を見ました。",
            "translation": "Yesterday, I watched an interesting movie.",
            "options": ["面白い", "面白な", "面白くて", "面白かったの"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-6",
            "grammarPointTitle": "い形容詞・な形容詞",
            "explanation": {
                "overall": "い-adjectives directly modify nouns in their plain form without adding な or の (面白い映画).",
                "options": [
                    {"text": "面白い", "isCorrect": True, "reason": "Correct. い-adjectives modify nouns directly.", "trapCategory": "formation"},
                    {"text": "面白な", "isCorrect": False, "reason": "Incorrect. い-adjectives never take な.", "trapCategory": "formation"},
                    {"text": "面白くて", "isCorrect": False, "reason": "Incorrect. て-form is used for linking predicates, not direct pre-noun modification.", "trapCategory": "formation"},
                    {"text": "面白かったの", "isCorrect": False, "reason": "Incorrect. Colloquial nominalization error.", "trapCategory": "formation"}
                ]
            },
            "hint": "How does an い-adjective modify a noun directly?"
        },
        {
            "id": "g1-l5-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Expressing your affection for animals. Target of liking is cats.",
            "question": "私は猫（　　）大好きです。",
            "translation": "I love cats / I like cats very much.",
            "options": ["が", "を", "に", "で"],
            "correctIndex": 0,
            "grammarPointId": "g1-l5-suki-kirai",
            "grammarPointTitle": "好き（な） / 嫌い（な） (Expressing Likes and Dislikes with が)",
            "explanation": {
                "overall": "好き and 嫌い are な-adjectives in Japanese. The object of affection/dislike is marked by particle が, NOT を.",
                "options": [
                    {"text": "が", "isCorrect": True, "reason": "Correct. The target of 好き / 嫌い / 上手 / 下手 takes が.", "trapCategory": "formation"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. Frequent English interference error; 好き is an adjective, not a transitive verb.", "trapCategory": "formation"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に does not mark the target of liking.", "trapCategory": "meaning"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で does not mark the target of liking.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the object of affection with 好き and 大好き?"
        },
        {
            "id": "g1-l5-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Stating that today you are extremely busy with three exams.",
            "question": "今日は試験が三つありますから、（　　）忙しいです。",
            "translation": "Because I have three exams today, I am very busy.",
            "options": ["とても", "あまり", "ぜんぜん", "すこしも"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-5-7",
            "grammarPointTitle": "数え方・数量の位置",
            "explanation": {
                "overall": "とても ('very') modifies affirmative adjectives. あまり, ぜんぜん, and すこしも require negative predicates.",
                "options": [
                    {"text": "とても", "isCorrect": True, "reason": "Correct. Degree adverb 'very', pairs with affirmative predicate.", "trapCategory": "formation"},
                    {"text": "あまり", "isCorrect": False, "reason": "Incorrect. あまり requires a negative predicate (あまり忙しくないです).", "trapCategory": "formation"},
                    {"text": "ぜんぜん", "isCorrect": False, "reason": "Incorrect. ぜんぜん requires a negative predicate.", "trapCategory": "formation"},
                    {"text": "すこしも", "isCorrect": False, "reason": "Incorrect. すこしも requires a negative predicate ('not in the least').", "trapCategory": "formation"}
                ]
            },
            "hint": "Which degree adverb meaning 'very' modifies affirmative adjectives?"
        },
        {
            "id": "g1-l5-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Suggesting to your study group that you take a short break together.",
            "question": "ちょっと（　　）。",
            "translation": "Let's rest a little.",
            "options": ["休みましょう", "休んでください", "休むです", "休みますか"],
            "correctIndex": 0,
            "grammarPointId": "g1-l5-mashou-ka",
            "grammarPointTitle": "〜ましょう / 〜ましょうか (Volitional Suggestion: Let's / Shall We?)",
            "explanation": {
                "overall": "〜ましょう replaces -masu to propose a mutual action ('let's do...').",
                "options": [
                    {"text": "休みましょう", "isCorrect": True, "reason": "Correct. Volitional proposal: -mashou ('let's rest').", "trapCategory": "context"},
                    {"text": "休んでください", "isCorrect": False, "reason": "Incorrect. 〜てください is a request directed at the listener, not a shared suggestion.", "trapCategory": "meaning"},
                    {"text": "休むです", "isCorrect": False, "reason": "Incorrect. Plain verb cannot attach です directly.", "trapCategory": "formation"},
                    {"text": "休みますか", "isCorrect": False, "reason": "Incorrect. Simply asks if someone rests.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the polite ending for proposing a mutual action ('let's...')?"
        },
        {
            "id": "g1-l5-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 5",
            "type": "multiple-choice",
            "context": "Offering assistance to an elderly person struggling with heavy luggage.",
            "question": "その荷物をお持ち（　　）。",
            "translation": "Shall I carry that luggage for you?",
            "options": ["しましょうか", "しませんか", "してください", "しましょう"],
            "correctIndex": 0,
            "grammarPointId": "g1-l5-mashou-ka",
            "grammarPointTitle": "〜ましょう / 〜ましょうか (Volitional Suggestion: Let's / Shall We?)",
            "explanation": {
                "overall": "〜ましょうか is used by a speaker offering to perform an action or assistance for the listener ('shall I...?').",
                "options": [
                    {"text": "しましょうか", "isCorrect": True, "reason": "Correct. Offers speaker assistance: 'Shall I do...?'", "trapCategory": "context"},
                    {"text": "しませんか", "isCorrect": False, "reason": "Incorrect. 〜ませんか invites the listener to participate, not offering speaker service.", "trapCategory": "meaning"},
                    {"text": "してください", "isCorrect": False, "reason": "Incorrect. Requests the other person to carry it.", "trapCategory": "meaning"},
                    {"text": "しましょう", "isCorrect": False, "reason": "Incorrect. Statement 'let's do it', omitting the offer particle か.", "trapCategory": "context"}
                ]
            },
            "hint": "Which ending is used when offering your assistance to someone: 'Shall I...?'"
        }
    ])

    # ------------------ LESSON 6 ------------------
    exercises.extend([
        {
            "id": "g1-l6-ex-1",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Conjugating Ru-verb 食べる into te-form to make a polite request.",
            "question": "どうぞ、（　　）ください。",
            "translation": "Please go ahead and eat.",
            "options": ["食べて", "食べりて", "食べで", "食べって"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-te-kudasai",
            "grammarPointTitle": "〜てください (Polite Request: Please Do)",
            "explanation": {
                "overall": "For Ru-verbs (stem ending in -e or -i, like 食べる), drop -ru and append -te -> 食べて.",
                "options": [
                    {"text": "食べて", "isCorrect": True, "reason": "Correct. Ru-verb rule: drop -ru and add -te.", "trapCategory": "formation"},
                    {"text": "食べりて", "isCorrect": False, "reason": "Incorrect. Overgeneralizing U-verb rule.", "trapCategory": "formation"},
                    {"text": "食べで", "isCorrect": False, "reason": "Incorrect. Ru-verbs never take voiced -de.", "trapCategory": "formation"},
                    {"text": "食べって", "isCorrect": False, "reason": "Incorrect. Double consonant error.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the te-form of the Ru-verb 食べる?"
        },
        {
            "id": "g1-l6-ex-2",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Conjugating U-verb 待つ (ends in つ) into te-form: 'Please wait a moment'.",
            "question": "ちょっと（　　）ください。",
            "translation": "Please wait a moment.",
            "options": ["待って", "待ちて", "待いて", "待んで"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-te-kudasai",
            "grammarPointTitle": "〜てください (Polite Request: Please Do)",
            "explanation": {
                "overall": "U-verbs ending in う, つ, or る conjugate with a small っ: つ -> って (待つ -> 待って).",
                "options": [
                    {"text": "待って", "isCorrect": True, "reason": "Correct. U-verb rule for う/つ/る -> って.", "trapCategory": "formation"},
                    {"text": "待ちて", "isCorrect": False, "reason": "Incorrect. Regular stem concatenation error.", "trapCategory": "formation"},
                    {"text": "待いて", "isCorrect": False, "reason": "Incorrect. Confusing with く -> いて rule.", "trapCategory": "formation"},
                    {"text": "待んで", "isCorrect": False, "reason": "Incorrect. Confusing with む/ぶ/ぬ -> んで rule.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do U-verbs ending in う, つ, and る conjugate into te-form?"
        },
        {
            "id": "g1-l6-ex-3",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Conjugating U-verb 飲む (ends in む) into te-form: 'Please drink some warm tea'.",
            "question": "温かいお茶を（　　）ください。",
            "translation": "Please drink some warm tea.",
            "options": ["飲んで", "飲みて", "飲って", "飲いで"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-te-kudasai",
            "grammarPointTitle": "〜てください (Polite Request: Please Do)",
            "explanation": {
                "overall": "U-verbs ending in む, ぶ, or ぬ conjugate with voiced んで: む -> んで (飲む -> 飲んで).",
                "options": [
                    {"text": "飲んで", "isCorrect": True, "reason": "Correct. U-verb rule for む/ぶ/ぬ -> んで.", "trapCategory": "formation"},
                    {"text": "飲みて", "isCorrect": False, "reason": "Incorrect. Unassimilated stem error.", "trapCategory": "formation"},
                    {"text": "飲って", "isCorrect": False, "reason": "Incorrect. Small tsu rule applies to う/つ/る, not む.", "trapCategory": "formation"},
                    {"text": "飲いで", "isCorrect": False, "reason": "Incorrect. Voiced -ide applies to ぐ (泳ぐ -> 泳いで).", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the te-form of U-verbs ending in む, ぶ, and ぬ?"
        },
        {
            "id": "g1-l6-ex-4",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Conjugating U-verb 書く (ends in く) into te-form: 'Please write your name here'.",
            "question": "ここに名前を（　　）ください。",
            "translation": "Please write your name here.",
            "options": ["書いて", "書きて", "書って", "書いで"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-te-kudasai",
            "grammarPointTitle": "〜てください (Polite Request: Please Do)",
            "explanation": {
                "overall": "U-verbs ending in く conjugate into いて (書く -> 書いて).",
                "options": [
                    {"text": "書いて", "isCorrect": True, "reason": "Correct. U-verb rule for く -> いて.", "trapCategory": "formation"},
                    {"text": "書きて", "isCorrect": False, "reason": "Incorrect. Unassimilated stem error.", "trapCategory": "formation"},
                    {"text": "書って", "isCorrect": False, "reason": "Incorrect. Small tsu rule belongs to う/つ/る.", "trapCategory": "formation"},
                    {"text": "書いで", "isCorrect": False, "reason": "Incorrect. -ide is for voiced ぐ, but 書く is unvoiced.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the te-form of an U-verb ending in く?"
        },
        {
            "id": "g1-l6-ex-5",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Conjugating the irregular exception verb 行く into te-form.",
            "question": "窓口へ（　　）ください。",
            "translation": "Please go to the service counter.",
            "options": ["行って", "行いて", "行きりて", "行んで"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-6-8",
            "grammarPointTitle": "て形・順序・禁止",
            "explanation": {
                "overall": "行く is the sole exception to the く -> いて rule: it conjugates with a small っ -> 行って (NOT いいて).",
                "options": [
                    {"text": "行って", "isCorrect": True, "reason": "Correct. Famous irregular exception: 行く -> 行って.", "trapCategory": "formation"},
                    {"text": "行いて", "isCorrect": False, "reason": "Incorrect. Regularizing exception mistake (Genki I explicitly warns against いいて).", "trapCategory": "formation"},
                    {"text": "行きりて", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "行んで", "isCorrect": False, "reason": "Incorrect. む/ぶ/ぬ ending rule.", "trapCategory": "formation"}
                ]
            },
            "hint": "Remember the famous exception rule for the verb 行く in te-form!"
        },
        {
            "id": "g1-l6-ex-6",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Asking someone to come to your office tomorrow. The verb is くる (irregular).",
            "question": "あした、私のオフィスに（　　）ください。",
            "translation": "Please come to my office tomorrow.",
            "options": ["きて", "こて", "くりて", "きって"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-6-8",
            "grammarPointTitle": "て形・順序・禁止",
            "explanation": {
                "overall": "The irregular verb くる conjugates into きて in te-form (stem shifts from ku to ki).",
                "options": [
                    {"text": "きて", "isCorrect": True, "reason": "Correct. Irregular te-form of くる is きて.", "trapCategory": "formation"},
                    {"text": "こて", "isCorrect": False, "reason": "Incorrect. Irregular vowel shift error.", "trapCategory": "formation"},
                    {"text": "くりて", "isCorrect": False, "reason": "Incorrect. Treats くる as a regular verb.", "trapCategory": "formation"},
                    {"text": "きって", "isCorrect": False, "reason": "Incorrect. きって is the te-form of 切る (to cut), not くる.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the irregular te-form of くる?"
        },
        {
            "id": "g1-l6-ex-7",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Politely requesting that the teacher speak a little more slowly.",
            "question": "先生、もう少しゆっくり（　　）ください。",
            "translation": "Teacher, please speak a little more slowly.",
            "options": ["話して", "話す", "話します", "話した"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-te-kudasai",
            "grammarPointTitle": "〜てください (Polite Request: Please Do)",
            "explanation": {
                "overall": "〜てください requires the verb in its te-form (話す -> 話して).",
                "options": [
                    {"text": "話して", "isCorrect": True, "reason": "Correct. Te-form of 話す is 話して.", "trapCategory": "formation"},
                    {"text": "話す", "isCorrect": False, "reason": "Incorrect. Plain non-past cannot attach ください.", "trapCategory": "formation"},
                    {"text": "話します", "isCorrect": False, "reason": "Incorrect. Masu-form cannot attach ください.", "trapCategory": "formation"},
                    {"text": "話した", "isCorrect": False, "reason": "Incorrect. Past ta-form cannot attach ください.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which verb form attaches to ください to make a polite request?"
        },
        {
            "id": "g1-l6-ex-8",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Asking a museum guide for permission to take a photograph.",
            "question": "ここで写真を撮っ（　　）ですか。",
            "translation": "May I take a photo here?",
            "options": ["てもいい", "てはいけない", "てください", "てはいけません"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-te-mo-ii",
            "grammarPointTitle": "〜てもいいですか (Asking for & Granting Permission: May I?)",
            "explanation": {
                "overall": "〜てもいいですか is the polite grammatical structure for asking permission ('may I do...?').",
                "options": [
                    {"text": "てもいい", "isCorrect": True, "reason": "Correct. Permission structure: 〜てもいいですか.", "trapCategory": "context"},
                    {"text": "てはいけない", "isCorrect": False, "reason": "Incorrect. 〜てはいけない expresses prohibition ('you must not').", "trapCategory": "meaning"},
                    {"text": "てください", "isCorrect": False, "reason": "Incorrect. 〜てください makes a request to the listener, not asking permission for oneself.", "trapCategory": "meaning"},
                    {"text": "てはいけません", "isCorrect": False, "reason": "Incorrect. Strong prohibition, unnatural in an inquiry.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What is the grammatical pattern for asking permission: 'May I do...?'"
        },
        {
            "id": "g1-l6-ex-9",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Library rule reminder: students are strictly prohibited from eating or drinking in the reading room.",
            "question": "ここで飲食をし（　　）。",
            "translation": "You must not eat or drink here.",
            "options": ["てはいけません", "てもいいです", "てください", "たいです"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-6-8",
            "grammarPointTitle": "て形・順序・禁止",
            "explanation": {
                "overall": "〜てはいけません expresses strong rules or prohibitions ('must not / not allowed to').",
                "options": [
                    {"text": "てはいけません", "isCorrect": True, "reason": "Correct. Prohibition formula: te-form + は + いけません.", "trapCategory": "context"},
                    {"text": "てもいいです", "isCorrect": False, "reason": "Incorrect. Expresses permission ('you may eat'), opposite of rule.", "trapCategory": "meaning"},
                    {"text": "てください", "isCorrect": False, "reason": "Incorrect. Requests eating.", "trapCategory": "meaning"},
                    {"text": "たいです", "isCorrect": False, "reason": "Incorrect. Desiderative ('I want to eat').", "trapCategory": "meaning"}
                ]
            },
            "hint": "What grammatical formula expresses strict prohibition ('you must not...')?"
        },
        {
            "id": "g1-l6-ex-10",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Describing a sequence of morning actions: woke up at 6:00, ate breakfast, and then went to school.",
            "question": "朝六時に起き（　　）、朝ご飯を食べ（　　）、学校へ行きました。",
            "translation": "I woke up at 6:00, ate breakfast, and went to school.",
            "options": ["て・て", "ます・ます", "て・ます", "た・た"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-6-8",
            "grammarPointTitle": "て形・順序・禁止",
            "explanation": {
                "overall": "The te-form connects two or more verbs in chronological sequence. Tense is determined entirely by the final verb in the sentence (行きました).",
                "options": [
                    {"text": "て・て", "isCorrect": True, "reason": "Correct. Te-form links sequential actions; final predicate governs sentence tense.", "trapCategory": "formation"},
                    {"text": "ます・ます", "isCorrect": False, "reason": "Incorrect. Masu-forms cannot coordinate clauses sequentially inside a sentence.", "trapCategory": "formation"},
                    {"text": "て・ます", "isCorrect": False, "reason": "Incorrect. Mixing te-form with uncoordinated masu-form.", "trapCategory": "formation"},
                    {"text": "た・た", "isCorrect": False, "reason": "Incorrect. Direct juxtaposition of past ta-forms without conjunctions is ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which verb form connects multiple actions in chronological sequence?"
        },
        {
            "id": "g1-l6-ex-11",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "Explaining the cause for studying tonight: because there is an exam tomorrow.",
            "question": "あしたテストがあります（　　）、今晩勉強します。",
            "translation": "Because I have a test tomorrow, I will study tonight.",
            "options": ["から", "ので", "けど", "のに"],
            "correctIndex": 0,
            "grammarPointId": "g1-l6-kara-reason",
            "grammarPointTitle": "〜から (Stating Reasons / Because - Clause Linker)",
            "explanation": {
                "overall": "The clause particle から connects an explanation/reason clause to its resulting situation: [Reason] から、[Result].",
                "options": [
                    {"text": "から", "isCorrect": True, "reason": "Correct. Genki I Lesson 6 reason conjunction [Reason] から、[Result].", "trapCategory": "formation"},
                    {"text": "ので", "isCorrect": False, "reason": "Incorrect. ので is introduced in later lessons and does not follow polite です/ます in basic Genki I grammar.", "trapCategory": "formation"},
                    {"text": "けど", "isCorrect": False, "reason": "Incorrect. けど indicates contrast ('although'), not cause.", "trapCategory": "meaning"},
                    {"text": "のに", "isCorrect": False, "reason": "Incorrect. のに indicates grievance/frustrated contrast ('even though').", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle attaches to a clause to mean 'because / therefore'?"
        },
        {
            "id": "g1-l6-ex-12",
            "bookId": "genki-1",
            "chapter": "Lesson 6",
            "type": "multiple-choice",
            "context": "You notice your friend's window is open and it is chilly outside. You offer to close it.",
            "question": "寒そうですね。窓を閉め（　　）。",
            "translation": "You look cold. Shall I close the window for you?",
            "options": ["ましょうか", "てください", "てはいけません", "てもいいですか"],
            "correctIndex": 0,
            "grammarPointId": "added-g1-6-8",
            "grammarPointTitle": "て形・順序・禁止",
            "explanation": {
                "overall": "〜ましょうか offers the speaker's own initiative to perform a helpful action for the listener ('shall I close...?').",
                "options": [
                    {"text": "ましょうか", "isCorrect": True, "reason": "Correct. Offers speaker action for listener's benefit.", "trapCategory": "context"},
                    {"text": "てください", "isCorrect": False, "reason": "Incorrect. Asks the other person to close it.", "trapCategory": "meaning"},
                    {"text": "てはいけません", "isCorrect": False, "reason": "Incorrect. Prohibits closing the window.", "trapCategory": "meaning"},
                    {"text": "てもいいですか", "isCorrect": False, "reason": "Incorrect. Asks permission for oneself, but lacks the helpful offer nuance of 〜ましょうか.", "trapCategory": "context"}
                ]
            },
            "hint": "What is the polite phrase for offering your own action for the listener's comfort?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_exercises_l2_to_l6()
    print(f"Generated {len(ex_list)} exercises across Lessons 2 to 6.")
    
    # Load existing Lesson 1 exercises
    with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)
    
    # Filter to only keep Lesson 1 (so we don't duplicate on re-run)
    l1_exercises = [x for x in existing if x['chapter'] == 'Lesson 1']
    combined = l1_exercises + ex_list
    
    with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(combined)} exercises to c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json")
