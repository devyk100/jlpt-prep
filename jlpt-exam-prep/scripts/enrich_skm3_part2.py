import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
BASE_PATH = ROOT / "content/base-reviewed.json"
CHAPTER_EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"

# ==========================================
# 1. 48 Authentic Exercises for Part 2 (12 per chapter)
# ==========================================

p2_exercises = []

# --- Part 2 · Chapter 1: 引用 (Quotation & Citation Structure) ---
p2_c1_exercises = [
    {
        "id": "skm3-p2-c1-q1",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Indirect message relay: please tell manager that I will arrive 10 minutes late.",
        "question": "課長に、電車の遅延で10分ほど遅れる（　）伝えていただけますか。",
        "translation": "Could you please tell the section manager that I will be about 10 minutes late due to a train delay?",
        "options": ["と", "ように", "という", "そうで"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "「普通形＋と伝えてください」は、発言内容をそのまま間接引用して第三者に伝達する基本構造です。",
            "options": [
                {"text": "と", "isCorrect": True, "reason": "【正解】普通形＋と＋伝える（発言内容の間接引用）。", "trapCategory": ""},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】「〜ように伝える」は依頼・指示の伝達（来るように伝える）であり、「遅れると伝える」事実引用には「と」が自然。", "trapCategory": "nuance"},
                {"text": "という", "isCorrect": False, "reason": "【不正解】名詞を修飾する形であり、動詞「伝える」の直前には置けません。", "trapCategory": "formation"},
                {"text": "そうで", "isCorrect": False, "reason": "【不正解】様態・伝聞の中止形になり破綻。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which quotation particle directly links the reported statement clause to 伝えていただけますか?"
    },
    {
        "id": "skm3-p2-c1-q2",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Indirect imperative: doctor strictly told the patient to cut down on salt.",
        "question": "医師から、塩分を控えてできるだけ薄味の食事にする（　）強く言われた。",
        "translation": "I was strongly told by the doctor to cut down on salt and eat meals seasoned as lightly as possible.",
        "options": ["ように", "と", "ということ", "らしい"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "「動詞辞書形／ない形＋ように＋言う／指示する／頼む」は、指示・命令・要望の内容を間接的に引用する構文です。",
            "options": [
                {"text": "ように", "isCorrect": True, "reason": "【正解】動詞辞書形＋ように＋言われた（指示・命令の間接引用）。", "trapCategory": ""},
                {"text": "と", "isCorrect": False, "reason": "【不正解】「〜としきりに言われた」等も文脈によりあり得ますが、指示内容の伝達には「〜ように言う」が教科書の正統構文。", "trapCategory": "nuance"},
                {"text": "ということ", "isCorrect": False, "reason": "【不正解】名詞節になり、動詞「言われた」に接続できません。", "trapCategory": "formation"},
                {"text": "らしい", "isCorrect": False, "reason": "【不正解】推量表現になり破綻。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What formula conveys an indirect order or recommendation: Verb-dict + [?] + 言われた?"
    },
    {
        "id": "skm3-p2-c1-q3",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Direct speech boundary: colleague remarked 'Let's take a break' before stretching.",
        "question": "彼は「少し休憩しよう」（　）立ち上がり、大きく伸びをした。",
        "translation": "He stood up saying 'Let's take a little break', and stretched out broadly.",
        "options": ["と言って", "のように", "として", "ばかりに"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "かぎ括弧「 」内の直接発話を受ける引用句「〜と言って＋後続動作」の基本文型です。",
            "options": [
                {"text": "と言って", "isCorrect": True, "reason": "【正解】「発話」＋と言って＋動作（直接引用の連結）。", "trapCategory": ""},
                {"text": "のように", "isCorrect": False, "reason": "【不正解】直接発話の鍵括弧に比喩「のように」は不適切。", "trapCategory": "formation"},
                {"text": "として", "isCorrect": False, "reason": "【不正解】資格表現になり意味不明。", "trapCategory": "meaning"},
                {"text": "ばかりに", "isCorrect": False, "reason": "【不正解】因果関係表現になり不適。", "trapCategory": "formation"}
            ]
        },
        "hint": "What standard phrase closes a direct quote before continuing to the subsequent physical action?"
    },
    {
        "id": "skm3-p2-c1-q4",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Content-specifying noun modification: rumors that the pop star got married secretly.",
        "question": "あの人気歌手が極秘で結婚した（　）噂が、ネット上で急速に広がっている。",
        "translation": "Rumors that the popular singer got married in absolute secret are spreading rapidly on the internet.",
        "options": ["という", "ように", "と", "との"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "「普通形＋という＋名詞（噂、ニュース、知らせ、意見）」は、同格内容節を名詞に直結させる引用構造です。",
            "options": [
                {"text": "という", "isCorrect": True, "reason": "【正解】普通形＋という＋名詞（同格内容の引用修飾）。", "trapCategory": ""},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】噂の内容名詞を修飾できません。", "trapCategory": "formation"},
                {"text": "と", "isCorrect": False, "reason": "【不正解】名詞「噂」を直接修飾することはできません（名詞修飾には「という」）。", "trapCategory": "formation"},
                {"text": "との", "isCorrect": False, "reason": "【不正解】「結婚したとの噂」も一部許容されますが、普通形節の同格修飾では「という」が最も正統。", "trapCategory": "nuance"}
            ]
        },
        "hint": "What compound connects an entire informational clause directly to nouns like 噂 or 知らせ?"
    },
    {
        "id": "skm3-p2-c1-q5",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Official message transmission: according to the weather forecast, temperatures will plummet tomorrow.",
        "question": "天気予報によると、明日は全国的に真冬並みの寒さになる（　）。",
        "translation": "According to the weather forecast, it is reported that temperatures tomorrow will become midwinter-like nationwide.",
        "options": ["とのことだ", "ということ", "ように言う", "と決まっている"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "「〜によると＋普通形＋とのことだ（ということだ）」は、公的報道や信頼できる情報源からの伝聞引用を結ぶ定番文末です。",
            "options": [
                {"text": "とのことだ", "isCorrect": True, "reason": "【正解】〜によると…とのことだ（情報源と呼応する伝聞文末）。", "trapCategory": ""},
                {"text": "ということ", "isCorrect": False, "reason": "【不正解】文末として完結していません（「だ」が欠落）。", "trapCategory": "formation"},
                {"text": "ように言う", "isCorrect": False, "reason": "【不正解】指示伝達表現であり天気予報の伝聞に合いません。", "trapCategory": "meaning"},
                {"text": "と決まっている", "isCorrect": False, "reason": "【不正解】規則表現になり天候の伝達に不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which formal hearsay ending naturally matches the introductory source attribution 〜によると?"
    },
    {
        "id": "skm3-p2-c1-q6",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Quoted question inside sentence: I don't know whether he will attend or not.",
        "question": "彼が明日の懇親会に出席する（　）どうか、まだ返事をもらっていない。",
        "translation": "I have not yet received a reply as to whether or not he will attend tomorrow's social gathering.",
        "options": ["か", "と", "なら", "で"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "「普通形＋かどうか」は、二者択一の埋め込み疑問文（出席するかどうか）を引用節として主文に組み込む構文です。",
            "options": [
                {"text": "か", "isCorrect": True, "reason": "【正解】〜かどうか（埋め込み疑問引用節）。", "trapCategory": ""},
                {"text": "と", "isCorrect": False, "reason": "【不正解】「〜とどうか」は非文です。", "trapCategory": "formation"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】条件形になり「どうか」と呼応しません。", "trapCategory": "formation"},
                {"text": "で", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What embedded question marker pairs with どうか to formulate 'whether or not'?"
    },
    {
        "id": "skm3-p2-c1-q7",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Indirect inquiry: ask the clerk what time the store closes.",
        "question": "店員さんに、何時に閉店する（　）聞いてみましょう。",
        "translation": "Let's ask the store clerk what time the shop closes.",
        "options": ["か", "と", "ように", "なら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "疑問詞を含む節（何時に閉店するか）を引用して「聞く」などの動詞に接続する場合、節末に「か」を置きます。",
            "options": [
                {"text": "か", "isCorrect": True, "reason": "【正解】疑問詞節＋か＋聞いてみる（疑問引用の組み込み）。", "trapCategory": ""},
                {"text": "と", "isCorrect": False, "reason": "【不正解】「何時に閉店すると聞いてみる」は文法破綻。", "trapCategory": "formation"},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】指示伝達になり不適。", "trapCategory": "meaning"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What particle embeds an open question clause (何時...?) before the verb 聞いてみる?"
    },
    {
        "id": "skm3-p2-c1-q8",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Reported speech conviction: he insisted that he definitely did not take the money.",
        "question": "彼は「自分はお金を盗んでなどいない」（　）頑なに主張し続けた。",
        "translation": "He stubbornly continued to insist: 'I did not steal any money!'.",
        "options": ["と", "ように", "という", "なら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "主張動詞（主張する、訴える、強調する）の前で、主張内容の節を引用する助詞は「と」です。",
            "options": [
                {"text": "と", "isCorrect": True, "reason": "【正解】引用節＋と＋主張する。", "trapCategory": ""},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】命令・指示ではないため「ように」は不可。", "trapCategory": "nuance"},
                {"text": "という", "isCorrect": False, "reason": "【不正解】名詞修飾形のため動詞に接続不可。", "trapCategory": "formation"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which standard quotation particle marks the content of an adamant insistence (主張する)?"
    },
    {
        "id": "skm3-p2-c1-q9",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Prohibition directive: parents repeatedly told child never to speak to strangers.",
        "question": "両親は幼い頃から、知らない人には絶対について行かない（　）厳しく言い聞かせてきた。",
        "translation": "From when I was young, my parents strictly admonished me never to follow strangers.",
        "options": ["ように", "と", "こと", "なら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "「動詞ない形＋ように＋言い聞かせる／教える」は、禁止・教訓の内容を間接的に伝達する構文です。",
            "options": [
                {"text": "ように", "isCorrect": True, "reason": "【正解】動詞ない形＋ように＋言い聞かせる（教訓・指示の間接引用）。", "trapCategory": ""},
                {"text": "と", "isCorrect": False, "reason": "【不正解】「行かないと言い聞かせる」は不自然（教え諭す指示内容には「ように」が最適）。", "trapCategory": "nuance"},
                {"text": "こと", "isCorrect": False, "reason": "【不正解】名詞化になり動詞に直接接続不可。", "trapCategory": "formation"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What pattern expresses an indirect parental admonition: V-ない + [?] + 言い聞かせる?"
    },
    {
        "id": "skm3-p2-c1-q10",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Quotation of thought/judgment: thinking that it would probably rain, speaker took an umbrella.",
        "question": "今日は雨が降るだろう（　）思って、折りたたみ傘を持参した。",
        "translation": "Thinking that it would probably rain today, I brought along a folding umbrella.",
        "options": ["と", "ように", "という", "なら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "思考・判断動詞（思う、考える、感じる）の内部思考内容を引用する構文は「〜と思う」です。",
            "options": [
                {"text": "と", "isCorrect": True, "reason": "【正解】思考引用節＋と＋思う。", "trapCategory": ""},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】思考内容の引用に「ように」は使えません。", "trapCategory": "formation"},
                {"text": "という", "isCorrect": False, "reason": "【不正解】名詞修飾形のため動詞に接続不可。", "trapCategory": "formation"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What basic particle marks the internal thought content preceding the verb 思う?"
    },
    {
        "id": "skm3-p2-c1-q11",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Scrambled order reconstruction (星マーク問題): assembling quotation frame accurately.",
        "question": "先生は ★ 入る言葉として最も適切なものはどれか。「先生は 学生に （ 1 図書館で ） （ 2 ように ） （ 3 ★ ） （ 4 静かにする ） 言った。」",
        "translation": "Which word goes into the star position? (The teacher told the students to be quiet in the library.)",
        "options": ["静かにする", "図書館で", "ように", "言った"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "文の正しい順序は「先生は 学生に [図書館で (1)] [静かにする (4)] [ように (2)] 言った」。3番目の★に入るのは「静かにする (4)」です。",
            "options": [
                {"text": "静かにする", "isCorrect": True, "reason": "【正解】語順: 1 図書館で -> 4 静かにする (★) -> 2 ように -> 言った。", "trapCategory": ""},
                {"text": "図書館で", "isCorrect": False, "reason": "【不正解】1番目の要素です。", "trapCategory": "formation"},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】4番目の要素です。", "trapCategory": "formation"},
                {"text": "言った", "isCorrect": False, "reason": "【不正解】文末述語です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Reconstruct the sequence: Place + Manner/Action + ように + 言った."
    },
    {
        "id": "skm3-p2-c1-q12",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 1",
        "type": "multiple-choice",
        "context": "Indirect advice relay: told friend that they had better consult a specialist.",
        "question": "悩んでいる友人に、専門家に一度相談してみたほうがいい（　）助言した。",
        "translation": "I advised my troubled friend that they had better consult a specialist once.",
        "options": ["と", "ように", "という", "なら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-1-124",
        "grammarPointTitle": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "explanation": {
            "overall": "「〜ほうがいい＋と助言した」は、具体的な助言内容を引用して主節動詞「助言した」に接続する構文です。",
            "options": [
                {"text": "と", "isCorrect": True, "reason": "【正解】助言内容の節＋と＋助言した。", "trapCategory": ""},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】「〜ほうがいいように助言した」は語法破綻。", "trapCategory": "formation"},
                {"text": "という", "isCorrect": False, "reason": "【不正解】名詞修飾形のため不適。", "trapCategory": "formation"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What particle links a completed advice proposal (〜ほうがいい) to 助言した?"
    }
]

# --- Part 2 · Chapter 2: 名詞の説明 (Noun Modification & Relative Clauses) ---
p2_c2_exercises = [
    {
        "id": "skm3-p2-c2-q1",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Particle + の + Noun modification: letter addressed to teacher.",
        "question": "机の上に置いてあるのは、お世話になった高校の先生（　）手紙です。",
        "translation": "What is placed on the desk is a letter addressed to my high school teacher who took care of me.",
        "options": ["への", "にの", "での", "へのの"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "方向・宛先を表す助詞「へ」は「への＋名詞」の形で名詞を修飾できます（※助詞「に」は直接「にの」とは言えず、「への」または「に対する」を用います）。",
            "options": [
                {"text": "への", "isCorrect": True, "reason": "【正解】助詞「へ」＋の＋名詞（先生への手紙）。", "trapCategory": ""},
                {"text": "にの", "isCorrect": False, "reason": "【不正解】誤用トラップ！日本語では助詞「に」に直接「の」を付けて名詞修飾することはできません。", "trapCategory": "formation"},
                {"text": "での", "isCorrect": False, "reason": "【不正解】場所・手段の修飾になり、手紙の宛先を表せません。", "trapCategory": "meaning"},
                {"text": "へのの", "isCorrect": False, "reason": "【不正解】重複で非文。", "trapCategory": "formation"}
            ]
        },
        "hint": "Remember the crucial textbook constraint: 'に' cannot attach to 'の' to modify nouns; use 'への' instead!"
    },
    {
        "id": "skm3-p2-c2-q2",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Compound postposition + noun modification: master's thesis concerning global warming.",
        "question": "彼が学会で発表したのは、地球温暖化（　）修士論文だった。",
        "translation": "What he presented at the academic conference was a master's thesis concerning global warming.",
        "options": ["についての", "について", "にとっての", "としての"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "「〜について」が後ろの名詞（論文）を修飾する場合、必ず「〜についての＋名詞」の形になります。",
            "options": [
                {"text": "についての", "isCorrect": True, "reason": "【正解】〜について＋の＋名詞（名詞修飾形）。", "trapCategory": ""},
                {"text": "について", "isCorrect": False, "reason": "【不正解】連用修飾形であり、名詞「修士論文」を直接修飾できません。", "trapCategory": "formation"},
                {"text": "にとっての", "isCorrect": False, "reason": "【不正解】評価の基準者（地球温暖化にとっての論文）になり意味不明。", "trapCategory": "meaning"},
                {"text": "としての", "isCorrect": False, "reason": "【不正解】資格表現になり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What suffix must be appended to について to allow it to modify a following noun like 論文?"
    },
    {
        "id": "skm3-p2-c2-q3",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Na-adjective noun modification: quiet, serene library ideal for intensive study.",
        "question": "集中して本を読むには、このように（　）図書館が最も適している。",
        "translation": "For reading books with deep concentration, a quiet library like this is most suitable.",
        "options": ["静かな", "静かだ", "静かに", "静かの"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "な形容詞が名詞（図書館）を修飾する連体形は「語幹＋な（静かな図書館）」です。",
            "options": [
                {"text": "静かな", "isCorrect": True, "reason": "【正解】な形容詞連体形（静かな＋名詞）。", "trapCategory": ""},
                {"text": "静かだ", "isCorrect": False, "reason": "【不正解】終止形であり名詞を修飾できません。", "trapCategory": "formation"},
                {"text": "静かに", "isCorrect": False, "reason": "【不正解】連用修飾形（副詞形）のため名詞修飾不可。", "trapCategory": "formation"},
                {"text": "静かの", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What is the standard attributive form of a な-adjective preceding a noun?"
    },
    {
        "id": "skm3-p2-c2-q4",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Mimetics / Onomatopoeia + の + Noun modification: polished sparkling clean shoes.",
        "question": "就職活動のために靴を磨き上げ、（　）革靴を履いて面接に向かった。",
        "translation": "I polished my shoes for job hunting, and headed to the interview wearing sparkling clean leather shoes.",
        "options": ["ぴかぴかの", "ぴかぴかに", "ぴかぴかだ", "ぴかぴか"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "状態・様子を表すオノマトペ（ぴかぴか、ばらばら、さらさら）が名詞を修飾する場合、「オノマトペ＋の＋名詞」の形をとります。",
            "options": [
                {"text": "ぴかぴかの", "isCorrect": True, "reason": "【正解】オノマトペ＋の＋名詞（ぴかぴかの革靴）。", "trapCategory": ""},
                {"text": "ぴかぴかに", "isCorrect": False, "reason": "【不正解】副詞形であり名詞を直接修飾できません。", "trapCategory": "formation"},
                {"text": "ぴかぴかだ", "isCorrect": False, "reason": "【不正解】述語終止形のため不可。", "trapCategory": "formation"},
                {"text": "ぴかぴか", "isCorrect": False, "reason": "【不正解】助詞「の」が欠落しています。", "trapCategory": "formation"}
            ]
        },
        "hint": "How do mimetic state words like ぴかぴか modify a noun directly?"
    },
    {
        "id": "skm3-p2-c2-q5",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Relative clause with subject particle が: bread baked by grandmother.",
        "question": "祖母（　）焼いてくれた手作りのパンは、香ばしくて本当においしい。",
        "translation": "The homemade bread that my grandmother baked for me is fragrant and truly delicious.",
        "options": ["が", "は", "を", "に"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "名詞修飾節（連体修飾節）の内部主語は「が」で標示されます（「は」は文全体の主題に用いられ、修飾節内主語には原則「が」または「の」を用います）。",
            "options": [
                {"text": "が", "isCorrect": True, "reason": "【正解】名詞修飾節内の主語標示「が」（祖母が焼いてくれたパン）。", "trapCategory": ""},
                {"text": "は", "isCorrect": False, "reason": "【不正解】修飾節内部の主語に「は」を置くことは原則できません。", "trapCategory": "formation"},
                {"text": "を", "isCorrect": False, "reason": "【不正解】祖母を焼いたことになり意味崩壊。", "trapCategory": "meaning"},
                {"text": "に", "isCorrect": False, "reason": "【不正解】文意不調和。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What particle marks the grammatical subject inside an embedded relative clause?"
    },
    {
        "id": "skm3-p2-c2-q6",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Origin particle から + の + Noun: international student from overseas.",
        "question": "今学期から、海外（　）留学生が私たちのクラスに3名加わった。",
        "translation": "Starting this semester, three international students from overseas joined our class.",
        "options": ["からの", "から", "への", "までの"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "出発点・出所を表す助詞「から」が名詞（留学生）を修飾する場合、「からの＋名詞」を用います。",
            "options": [
                {"text": "からの", "isCorrect": True, "reason": "【正解】助詞「から」＋の＋名詞（海外からの留学生）。", "trapCategory": ""},
                {"text": "から", "isCorrect": False, "reason": "【不正解】「の」がないと名詞を直接修飾できません。", "trapCategory": "formation"},
                {"text": "への", "isCorrect": False, "reason": "【不正解】方向が逆転してしまいます。", "trapCategory": "meaning"},
                {"text": "までの", "isCorrect": False, "reason": "【不正解】終点修飾になり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which compound particle links an origin noun (海外) to a modified noun (留学生)?"
    },
    {
        "id": "skm3-p2-c2-q7",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Opposition attitude: opposing opinion toward plan A.",
        "question": "役員会では、A案（　）反対意見が相次ぎ、結論は次回に持ち越された。",
        "translation": "In the board meeting, opposing opinions toward Plan A emerged one after another, and the conclusion was carried over to the next meeting.",
        "options": ["に対する", "に対して", "についての", "にとっての"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "「〜に対して」が後ろの名詞（反対意見）を修飾する連体形は「〜に対する＋名詞」です。",
            "options": [
                {"text": "に対する", "isCorrect": True, "reason": "【正解】〜に対する＋名詞（対象への態度・意見の名詞修飾）。", "trapCategory": ""},
                {"text": "に対して", "isCorrect": False, "reason": "【不正解】連用形であり名詞を直接修飾できません。", "trapCategory": "formation"},
                {"text": "についての", "isCorrect": False, "reason": "【不正解】テーマ修飾であり、「反対意見」のような対決姿勢には「に対する」が自然。", "trapCategory": "nuance"},
                {"text": "にとっての", "isCorrect": False, "reason": "【不正解】視点基準であり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What is the attributive (noun-modifying) form of に対して preceding 反対意見?"
    },
    {
        "id": "skm3-p2-c2-q8",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Noun + という + Noun (Naming): novel called Botchan written by Soseki.",
        "question": "夏目漱石が書いた『坊っちゃん』（　）小説は、今でも多くの人に親しまれている。",
        "translation": "The novel called 'Botchan' written by Soseki Natsume is still beloved by many people today.",
        "options": ["という", "といった", "として", "についての"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "作品名や名称を紹介する「固有名称＋という＋普通名詞（『坊っちゃん』という小説）」の基本構文です。",
            "options": [
                {"text": "という", "isCorrect": True, "reason": "【正解】名称・作品名＋という＋名詞。", "trapCategory": ""},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】列挙表現（〜といった）であり、単独の作品名称には「という」を用います。", "trapCategory": "nuance"},
                {"text": "として", "isCorrect": False, "reason": "【不正解】連用形資格表現であり名詞修飾に不適。", "trapCategory": "formation"},
                {"text": "についての", "isCorrect": False, "reason": "【不正解】坊っちゃんを論じた別の小説という意味になり誤り。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What pattern links a specific proper title (『坊っちゃん』) to its category noun (小説)?"
    },
    {
        "id": "skm3-p2-c2-q9",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Simile noun modification: woman beautiful like an angel.",
        "question": "彼女は（　）美しい声で、聴衆全員を魅了した。",
        "translation": "She captivated the entire audience with a voice beautiful like an angel.",
        "options": ["天使のように", "天使のような", "天使のようで", "天使らしく"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "直後の形容詞「美しい」を修飾するため、副詞形（連用形）「天使のように＋美しい」が正解です（※「天使のような」だと直後の名詞を修飾する連体形になります）。",
            "options": [
                {"text": "天使のように", "isCorrect": True, "reason": "【正解】天使のように（連用修飾）＋美しい（形容詞）。", "trapCategory": ""},
                {"text": "天使のような", "isCorrect": False, "reason": "【不正解】連体形であり、「美しい」ではなく直接「声」にかかる場合は「天使のような声」となりますが、形容詞「美しい」の直前には連用形「〜ように」が必要。", "trapCategory": "formation"},
                {"text": "天使のようで", "isCorrect": False, "reason": "【不正解】中止形になり不調和。", "trapCategory": "formation"},
                {"text": "天使らしく", "isCorrect": False, "reason": "【不正解】本物の天使にふさわしくという意味になり比喩に合いません。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Notice that the next word is an adjective (美しい); which adverbial inflected form is required?"
    },
    {
        "id": "skm3-p2-c2-q10",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Past state noun modification: house where grandfather used to live.",
        "question": "これは、かつて祖父が長年（　）古い日本家屋です。",
        "translation": "This is an old Japanese-style house where my grandfather used to live for many years in the past.",
        "options": ["住んでいた", "住んでいる", "住む", "住めば"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "「かつて（過去に）」という時間副詞に呼応し、過去の継続状態を表す連体修飾形「住んでいた＋家屋」を用います。",
            "options": [
                {"text": "住んでいた", "isCorrect": True, "reason": "【正解】過去の継続的居住状態を表す連体形「住んでいた」。", "trapCategory": ""},
                {"text": "住んでいる", "isCorrect": False, "reason": "【不正解】現在形となり「かつて」と矛盾します。", "trapCategory": "nuance"},
                {"text": "住む", "isCorrect": False, "reason": "【不正解】非過去形となり過去の回想に合いません。", "trapCategory": "nuance"},
                {"text": "住めば", "isCorrect": False, "reason": "【不正解】仮定形であり名詞修飾不可。", "trapCategory": "formation"}
            ]
        },
        "hint": "What tense form naturally collocates with the retrospective adverb かつて (in the past)?"
    },
    {
        "id": "skm3-p2-c2-q11",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Scrambled order reconstruction (星マーク問題): assembling noun modification chain.",
        "question": "これは ★ 入る言葉として最も適切なものはどれか。「これは （ 1 先生が ） （ 2 推薦して ） （ 3 ★ ） （ 4 くださった ） 素晴らしい本です。」",
        "translation": "Which word goes into the star position? (This is a wonderful book that the teacher kindly recommended.)",
        "options": ["くださった", "先生が", "推薦して", "本です"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "正しい語順は「これは [先生が (1)] [推薦して (2)] [くださった (4)] (★) 素晴らしい本です」。3番目の★に入るのは「くださった (4)」です。",
            "options": [
                {"text": "くださった", "isCorrect": True, "reason": "【正解】語順: 1 先生が -> 2 推薦して -> 4 くださった (★) -> 素晴らしい本です。", "trapCategory": ""},
                {"text": "先生が", "isCorrect": False, "reason": "【不正解】1番目の要素です。", "trapCategory": "formation"},
                {"text": "推薦して", "isCorrect": False, "reason": "【不正解】2番目の要素です。", "trapCategory": "formation"},
                {"text": "本です", "isCorrect": False, "reason": "【不正解】主節の述語部分です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Construct the relative clause: Subject + Verb-て + くださった + Modified Noun."
    },
    {
        "id": "skm3-p2-c2-q12",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 2",
        "type": "multiple-choice",
        "context": "Role modification: qualifications and duties as team leader.",
        "question": "プロジェクトリーダー（　）役割を果たすため、毎日の進捗管理を徹底している。",
        "translation": "In order to fulfill my role as project leader, I am strictly enforcing daily progress management.",
        "options": ["としての", "として", "にとっての", "についての"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-2-125",
        "grammarPointTitle": "文の組み立て 2: 名詞の説明 (Noun Modification & Description)",
        "explanation": {
            "overall": "資格・立場を表す「〜として」が後ろの名詞（役割）を修飾する連体形は「〜としての＋名詞」です。",
            "options": [
                {"text": "としての", "isCorrect": True, "reason": "【正解】〜として＋の＋名詞（資格・立場の名詞修飾）。", "trapCategory": ""},
                {"text": "として", "isCorrect": False, "reason": "【不正解】連用形であり名詞を直接修飾できません。", "trapCategory": "formation"},
                {"text": "にとっての", "isCorrect": False, "reason": "【不正解】評価の視点になり「役割」の修飾に不適。", "trapCategory": "meaning"},
                {"text": "についての", "isCorrect": False, "reason": "【不正解】テーマ修飾になり資格の意味が消えます。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What is the noun-modifying attributive form of として preceding 役割?"
    }
]

# --- Part 2 · Chapter 3: 「という」・「といった」 (Naming, Content & Representative Listing) ---
p2_c3_exercises = [
    {
        "id": "skm3-p2-c3-q1",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Representative listing: science subjects such as mathematics, physics, and chemistry.",
        "question": "数学や物理、化学（　）理科系の科目は、論理的思考力を養うのに役立つ。",
        "translation": "Science subjects such as mathematics, physics, and chemistry are helpful for cultivating logical thinking skills.",
        "options": ["といった", "という", "としての", "について"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "「AやB、C＋といった＋包括名詞」は、複数の代表的な具体例を列挙して全体を包括する構文です。",
            "options": [
                {"text": "といった", "isCorrect": True, "reason": "【正解】代表例の列挙包括表現「〜といった＋包括名詞」。", "trapCategory": ""},
                {"text": "という", "isCorrect": False, "reason": "【不正解】単一の名称・同格内容の提示に向いており、複数の並列例示には「といった」が自然。", "trapCategory": "nuance"},
                {"text": "としての", "isCorrect": False, "reason": "【不正解】資格表現になり不適。", "trapCategory": "meaning"},
                {"text": "について", "isCorrect": False, "reason": "【不正解】名詞を直接修飾できません。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which pattern follows an enumeration of examples (AやB...) to introduce a general category noun?"
    },
    {
        "id": "skm3-p2-c3-q2",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Naming introducing unfamiliar entity: fruit called 'durian'.",
        "question": "東南アジアには、「ドリアン」（　）非常に強烈な匂いのする果物がある。",
        "translation": "In Southeast Asia, there is a fruit with an extremely intense odor called 'durian'.",
        "options": ["という", "といった", "について", "にとって"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "聞き手が知らないかもしれない事物や固有名詞を命名・紹介する構文は「名称＋という＋普通名詞」です。",
            "options": [
                {"text": "という", "isCorrect": True, "reason": "【正解】名称・名前の紹介（ドリアンという果物）。", "trapCategory": ""},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】複数例示の包括表現であり、単独名称の紹介には不自然。", "trapCategory": "nuance"},
                {"text": "について", "isCorrect": False, "reason": "【不正解】テーマ表現になり命名になりません。", "trapCategory": "meaning"},
                {"text": "にとって", "isCorrect": False, "reason": "【不正解】評価の視点。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What pattern introduces the name of a specific, unfamiliar object (ドリアン) to a category (果物)?"
    },
    {
        "id": "skm3-p2-c3-q3",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Explaining concept / definition: non-smoking means not smoking tobacco anywhere in the venue.",
        "question": "全館禁煙（　）ことは、会場内のどこでもタバコを吸ってはいけないということだ。",
        "translation": "The fact that the entire building is non-smoking means that you must not smoke tobacco anywhere in the venue.",
        "options": ["という", "といった", "としての", "について"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "「〜ということは、…ということだ」は、ある概念や規則の定義・意味内容を論理的に解説する代表的構文です。",
            "options": [
                {"text": "という", "isCorrect": True, "reason": "【正解】〜ということは、…ということだ（定義・内容説明の呼応構文）。", "trapCategory": ""},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】列挙表現のため定義文に不適。", "trapCategory": "meaning"},
                {"text": "としての", "isCorrect": False, "reason": "【不正解】資格表現。", "trapCategory": "meaning"},
                {"text": "について", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What particle compound pairs in the canonical definition frame: 〜ということ(は)...ということだ?"
    },
    {
        "id": "skm3-p2-c3-q4",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Representative color examples: dark colors such as black, navy, and dark brown.",
        "question": "就職活動の面接では、黒や紺（　）落ち着いた色のスーツを着用するのが一般的だ。",
        "translation": "In job hunting interviews, it is standard practice to wear a suit of a sober color such as black or navy.",
        "options": ["といった", "という", "にとって", "について"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "「黒や紺」という複数の具体例を挙げて後ろの「落ち着いた色」にまとめるため、「〜といった」が適切です。",
            "options": [
                {"text": "といった", "isCorrect": True, "reason": "【正解】複数具体例の列挙（黒や紺といった落ち着いた色）。", "trapCategory": ""},
                {"text": "という", "isCorrect": False, "reason": "【不正解】単一の名称指定になり、複数例示の包括には「といった」が自然。", "trapCategory": "nuance"},
                {"text": "にとって", "isCorrect": False, "reason": "【不正解】視点表現。", "trapCategory": "meaning"},
                {"text": "について", "isCorrect": False, "reason": "【不正解】連用形のため修飾不可。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which expression provides typical representative examples (such as black or navy)?"
    },
    {
        "id": "skm3-p2-c3-q5",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Informational notification: message that class is cancelled tomorrow.",
        "question": "学校の掲示板に、明日の午後の講義が休講になる（　）知らせが貼ってあった。",
        "translation": "On the school bulletin board, a notice was posted stating that tomorrow afternoon's lecture will be cancelled.",
        "options": ["という", "といった", "の", "について"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "「休講になる」という文の内容を「知らせ」という名詞に直結させる同格の「という」です（「休講になるの知らせ」とは言えません）。",
            "options": [
                {"text": "という", "isCorrect": True, "reason": "【正解】普通形＋という＋名詞（同格内容提示）。", "trapCategory": ""},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】例示列挙になり不適。", "trapCategory": "meaning"},
                {"text": "の", "isCorrect": False, "reason": "【不正解】動詞節に「の知らせ」と直接接続することはできません。", "trapCategory": "formation"},
                {"text": "について", "isCorrect": False, "reason": "【不正解】修飾不可。", "trapCategory": "formation"}
            ]
        },
        "hint": "What connector links a clausal statement directly to notification nouns like 知らせ?"
    },
    {
        "id": "skm3-p2-c3-q6",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "General belief / lore: it is widely said that green tea is good for preventing colds.",
        "question": "緑茶を毎日飲むことは、風邪の予防に効果的だ（　）言われている。",
        "translation": "It is widely said that drinking green tea every day is effective for preventing colds.",
        "options": ["と", "という", "ように", "なら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "「〜と言われている」は、世間の一般的な通念・社会の評価を伝える受身引用文です（名詞「効果的だ」のな形容詞語幹＋だ＋と＋言われている）。",
            "options": [
                {"text": "と", "isCorrect": True, "reason": "【正解】普通形＋と言われている（世評・通説の受身引用）。", "trapCategory": ""},
                {"text": "という", "isCorrect": False, "reason": "【不正解】「効果的だという言われている」は非文です。", "trapCategory": "formation"},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】指示伝達になり不適。", "trapCategory": "meaning"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What particle pairs with 言われている to state a widely received societal belief?"
    },
    {
        "id": "skm3-p2-c3-q7",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Listing household electrical appliances: refrigerator, washing machine, microwave oven.",
        "question": "冷蔵庫や洗濯機、電子レンジ（　）白物家電は、新生活を始める際の必需品だ。",
        "translation": "Major home appliances such as refrigerators, washing machines, and microwave ovens are necessities when starting a new life.",
        "options": ["といった", "という", "として", "についての"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "「AやB、C＋といった＋包括名詞（白物家電）」で、主要な電化製品の具体例を列挙して包括する構文です。",
            "options": [
                {"text": "といった", "isCorrect": True, "reason": "【正解】家電具体例の包括列挙（〜といった白物家電）。", "trapCategory": ""},
                {"text": "という", "isCorrect": False, "reason": "【不正解】単一名称指定になり不自然。", "trapCategory": "nuance"},
                {"text": "として", "isCorrect": False, "reason": "【不正解】資格表現になり不適。", "trapCategory": "meaning"},
                {"text": "についての", "isCorrect": False, "reason": "【不正解】テーマ修飾になり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which pattern summarizes a series of items (refrigerator, washing machine...) into an umbrella category?"
    },
    {
        "id": "skm3-p2-c3-q8",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Conveying impression: I got the impression that he was somewhat reluctant to accept.",
        "question": "彼の表情から、その提案をあまり快く思っていない（　）印象を受けた。",
        "translation": "From his facial expression, I got the impression that he did not view the proposal very favorably.",
        "options": ["という", "といった", "ように", "との"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "節の内容を抽象名詞「印象」に同格直結させる「普通形＋という＋印象」の構文です。",
            "options": [
                {"text": "という", "isCorrect": True, "reason": "【正解】節＋という＋印象（同格内容修飾）。", "trapCategory": ""},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】例示列挙になり不適。", "trapCategory": "meaning"},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】印象を直接修飾できません。", "trapCategory": "formation"},
                {"text": "との", "isCorrect": False, "reason": "【不正解】「という」が自然。", "trapCategory": "nuance"}
            ]
        },
        "hint": "What connector links a clause specifying an impression to the noun 印象?"
    },
    {
        "id": "skm3-p2-c3-q9",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Scrambled order reconstruction (星マーク問題): assembling という・といった structure.",
        "question": "週末は ★ 入る言葉として最も適切なものはどれか。「週末は （ 1 映画鑑賞 ） （ 2 といった ） （ 3 ★ ） （ 4 読書や ） 自宅でできる趣味を楽しんでいる。」",
        "translation": "Which word goes into the star position? (On weekends, I enjoy hobbies that can be done at home, such as reading and watching movies.)",
        "options": ["映画鑑賞", "といった", "読書や", "自宅でできる"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "正しい順序は「週末は [読書や (4)] [映画鑑賞 (1)] (★) [といった (2)] 自宅でできる趣味を楽しんでいる」。3番目の★に入るのは「映画鑑賞 (1)」です。",
            "options": [
                {"text": "映画鑑賞", "isCorrect": True, "reason": "【正解】語順: 4 読書や -> 1 映画鑑賞 (★) -> 2 といった -> 自宅でできる趣味。", "trapCategory": ""},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】4番目の要素です。", "trapCategory": "formation"},
                {"text": "読書や", "isCorrect": False, "reason": "【不正解】1番目の要素です。", "trapCategory": "formation"},
                {"text": "自宅でできる", "isCorrect": False, "reason": "【不正解】後続修飾部です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Arrange the list: Example 1 + や + Example 2 (★) + といった + Category."
    },
    {
        "id": "skm3-p2-c3-q10",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Explaining acronym: 'AI' stands for Artificial Intelligence.",
        "question": "「AI」（　）人工知能のことで、近年急速に社会の各分野で応用が進んでいる。",
        "translation": "'AI' refers to Artificial Intelligence, which has been applied rapidly across various sectors of society in recent years.",
        "options": ["とは", "ということは", "といった", "として"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "「言葉・用語＋とは、〜のことだ」は、ある用語や略語の定義・意味を提示する最重要の定義構文です。",
            "options": [
                {"text": "とは", "isCorrect": True, "reason": "【正解】用語＋とは、〜のことだ（定義・語義説明構文）。", "trapCategory": ""},
                {"text": "ということは", "isCorrect": False, "reason": "【不正解】文や命題の解釈に用いられ、単語の語義提示には「とは」が最も簡潔で自然。", "trapCategory": "nuance"},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】列挙になり不適。", "trapCategory": "meaning"},
                {"text": "として", "isCorrect": False, "reason": "【不正解】資格表現になり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What particle combination sets up a word or term (AI) to be defined by 〜のことだ?"
    },
    {
        "id": "skm3-p2-c3-q11",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Content of agreement / resolution: unanimous decision that all members will cooperate.",
        "question": "会議では、全員で一致団結して問題解決に当たる（　）合意が形成された。",
        "translation": "At the meeting, an agreement was reached that everyone would unite together as one and tackle resolving the issue.",
        "options": ["という", "といった", "ように", "について"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "合意・決議・約束の内容を名詞「合意」に同格直結させる構文は「普通形＋という＋名詞」です。",
            "options": [
                {"text": "という", "isCorrect": True, "reason": "【正解】合意内容の節＋という＋合意。", "trapCategory": ""},
                {"text": "といった", "isCorrect": False, "reason": "【不正解】例示になり不適。", "trapCategory": "meaning"},
                {"text": "ように", "isCorrect": False, "reason": "【不正解】直接修飾不可。", "trapCategory": "formation"},
                {"text": "について", "isCorrect": False, "reason": "【不正解】修飾不可。", "trapCategory": "formation"}
            ]
        },
        "hint": "What connector links the full resolution clause to the noun 合意 (agreement)?"
    },
    {
        "id": "skm3-p2-c3-q12",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 3",
        "type": "multiple-choice",
        "context": "Traditional cultural arts listing: tea ceremony, flower arrangement, calligraphy.",
        "question": "茶道や華道、書道（　）日本の伝統文化を体験するため、多くの外国人が訪れている。",
        "translation": "To experience Japanese traditional culture such as tea ceremony, flower arrangement, and calligraphy, many foreigners are visiting.",
        "options": ["といった", "という", "としての", "について"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-3-126",
        "grammarPointTitle": "文の組み立て 3: 「という」・「といった」",
        "explanation": {
            "overall": "複数の伝統芸能の例を挙げて「日本の伝統文化」にまとめるため、「〜といった」を用います。",
            "options": [
                {"text": "といった", "isCorrect": True, "reason": "【正解】茶道や華道、書道といった日本の伝統文化（代表的伝統芸能の包括列挙）。", "trapCategory": ""},
                {"text": "という", "isCorrect": False, "reason": "【不正解】複数並列例示に「という」は不自然。", "trapCategory": "nuance"},
                {"text": "としての", "isCorrect": False, "reason": "【不正解】資格表現。", "trapCategory": "meaning"},
                {"text": "について", "isCorrect": False, "reason": "【不正解】修飾不可。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which pattern groups traditional arts (tea ceremony, flower arrangement...) under the broader category 伝統文化?"
    }
]

# --- Part 2 · Chapter 4: 決まった形 (Fixed Correlative Syntactic Patterns) ---
p2_c4_exercises = [
    {
        "id": "skm3-p2-c4-q1",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Temporal / Spatial continuous span: heavy rain from midnight through dawn.",
        "question": "昨夜から今朝の明け方（　）、関東地方を中心に非常に激しい雨が降った。",
        "translation": "From last night through dawn this morning, extremely heavy rain fell primarily centered on the Kanto region.",
        "options": ["にかけて", "について", "に対して", "にとって"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「AからBにかけて」は、時間的・空間的なおおよその範囲・継続的スパン（昨夜から今朝の明け方にかけて）を表す決まった構文です。",
            "options": [
                {"text": "にかけて", "isCorrect": True, "reason": "【正解】〜から〜にかけて（時間・空間の継続的範囲）。", "trapCategory": ""},
                {"text": "について", "isCorrect": False, "reason": "【不正解】テーマ表現であり、範囲に合いません。", "trapCategory": "meaning"},
                {"text": "に対して", "isCorrect": False, "reason": "【不正解】対象・対比表現。", "trapCategory": "meaning"},
                {"text": "にとって", "isCorrect": False, "reason": "【不正解】評価の視点。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which fixed pattern pairs with 〜から to express an approximate continuous time/space span?"
    },
    {
        "id": "skm3-p2-c4-q2",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Treating / taking A as B: aiming for health first as our primary objective.",
        "question": "新年度のサークル活動は、「健康第一」（　）目標として、無理のないペースで進めます。",
        "translation": "In our club activities for the new academic year, taking 'Health First' as our objective, we will proceed at a reasonable pace.",
        "options": ["を", "に", "で", "が"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「名詞Aを名詞Bとして（とする／とした）」は、『AをBとみなして／位置づけて（健康第一を目標として）』という意味を表す固定構文です。",
            "options": [
                {"text": "を", "isCorrect": True, "reason": "【正解】〜を〜として（AをBと位置づける固定構文）。", "trapCategory": ""},
                {"text": "に", "isCorrect": False, "reason": "【不正解】助詞「に」では固定構文「〜を〜として」が成立しません。", "trapCategory": "formation"},
                {"text": "で", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"},
                {"text": "が", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What particle marks the object in the fixed frame: [Noun A] + [?] + [Noun B] として?"
    },
    {
        "id": "skm3-p2-c4-q3",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Escalating baseline: not only in Japan as a matter of course, but also highly acclaimed abroad.",
        "question": "このアニメ作品は、日本国内（　）海外でも熱狂的なファンを獲得している。",
        "translation": "This anime work has gained passionate fans not only domestically in Japan as a matter of course, but overseas as well.",
        "options": ["はもちろん", "はおろか", "のみならず", "ばかりに"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「名詞Aはもちろん（のこと）、Bも」は、『Aは当然として、さらに別のBも同様に』という意味を表す定番の累加構文です。",
            "options": [
                {"text": "はもちろん", "isCorrect": True, "reason": "【正解】Aはもちろん、Bも（当然の既知事項から他方への拡大）。", "trapCategory": ""},
                {"text": "はおろか", "isCorrect": False, "reason": "【不正解】N2の否定強調表現（AはおろかBさえ〜ない）であり、肯定の成功には使えません。", "trapCategory": "nuance"},
                {"text": "のみならず", "isCorrect": False, "reason": "【不正解】「のみならず」も類似ですが、N3の教科書固定形では「はもちろん」が正統。", "trapCategory": "nuance"},
                {"text": "ばかりに", "isCorrect": False, "reason": "【不正解】遺憾の原因表現となり意味不明。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What pattern expresses 'not only A as a given, but B likewise'?"
    },
    {
        "id": "skm3-p2-c4-q4",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Sole prerequisite: provided that we have health, we can overcome any obstacle.",
        "question": "どんなに貧しくても、体（　）健康であれば、何とか乗り越えていける。",
        "translation": "No matter how poor we may be, as long as our bodies are healthy (provided that sole prerequisite is met), we can manage to overcome it.",
        "options": ["さえ", "こそ", "でも", "だけ"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「名詞＋さえ＋条件形（ば／であれば）」は、『その唯一の条件さえ満たされれば、他はどうあれ十分だ』という最低限必須条件の固定構文です。",
            "options": [
                {"text": "さえ", "isCorrect": True, "reason": "【正解】体さえ健康であれば（さえ〜ば固定呼応構文）。", "trapCategory": ""},
                {"text": "こそ", "isCorrect": False, "reason": "【不正解】強調助詞であり、条件「ば」との必須呼応構文になりません。", "trapCategory": "nuance"},
                {"text": "でも", "isCorrect": False, "reason": "【不正解】例示助詞になり必須条件を表せません。", "trapCategory": "meaning"},
                {"text": "だけ", "isCorrect": False, "reason": "【不正解】客観的限定であり固定構文「さえ〜ば」のニュアンスに劣ります。", "trapCategory": "nuance"}
            ]
        },
        "hint": "Which particle pairs with conditional 〜ば to form the formula for the sole sufficient condition?"
    },
    {
        "id": "skm3-p2-c4-q5",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Repeating predicate concession: read it indeed, but didn't understand the deep content.",
        "question": "その学術論文を（　）ことは読んだが、内容が難解すぎて半分も理解できなかった。",
        "translation": "I read that academic paper indeed, but the content was far too difficult and I couldn't understand even half of it.",
        "options": ["読んだ", "読む", "読んで", "読めば"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「動詞た形＋ことは＋動詞た形＋が」は、同一動詞を反復して『確かに〜したことは事実だが、しかし…』という留保付き肯定譲歩を表す固定形です（後件が過去なら前件も過去形）。",
            "options": [
                {"text": "読んだ", "isCorrect": True, "reason": "【正解】読んだことは読んだが（過去の反復譲歩固定形）。", "trapCategory": ""},
                {"text": "読む", "isCorrect": False, "reason": "【不正解】後件が過去形「読んだが」のため、時制不一致。", "trapCategory": "formation"},
                {"text": "読んで", "isCorrect": False, "reason": "【不正解】て形＋ことは、は非文。", "trapCategory": "formation"},
                {"text": "読めば", "isCorrect": False, "reason": "【不正解】仮定形のため不適。", "trapCategory": "formation"}
            ]
        },
        "hint": "Match the tense of the repeated verb: [Verb-た] + ことは + [Verb-た] が."
    },
    {
        "id": "skm3-p2-c4-q6",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Proportional advancement: the more one practices conversation, the smoother Japanese becomes.",
        "question": "日本語の会話は、練習（　）練習するほど自然に話せるようになる。",
        "translation": "As for Japanese conversation, the more you practice, the more naturally you become able to speak.",
        "options": ["すれば", "すると", "するなら", "したら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「動詞ば形＋動詞辞書形＋ほど」は、『〜すればするほど（一方の進展に比例して他方も向上する）』という比例相関の固定構文です。",
            "options": [
                {"text": "すれば", "isCorrect": True, "reason": "【正解】練習すれば練習するほど（ば〜ほど固定構文）。", "trapCategory": ""},
                {"text": "すると", "isCorrect": False, "reason": "【不正解】相関構文になりません。", "trapCategory": "formation"},
                {"text": "するなら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"},
                {"text": "したら", "isCorrect": False, "reason": "【不正解】正統文法では「ば」を用います。", "trapCategory": "formation"}
            ]
        },
        "hint": "What is the canonical conditional form in the proportional correlative formula 'Verb-ば + Verb-dict + ほど'?"
    },
    {
        "id": "skm3-p2-c4-q7",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Spatial span: typhoons bringing stormy conditions from Kyushu through Shikoku.",
        "question": "大型の台風が接近しており、九州地方から四国地方（　）暴風雨に警戒が必要です。",
        "translation": "A large typhoon is approaching, and caution against storm conditions is required from the Kyushu region through the Shikoku region.",
        "options": ["にかけて", "において", "に際して", "に関して"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「地域Aから地域Bにかけて」は、空間的な連続的範囲（九州から四国にかけて）を表す固定構文です。",
            "options": [
                {"text": "にかけて", "isCorrect": True, "reason": "【正解】〜から〜にかけて（空間的連続範囲の固定形）。", "trapCategory": ""},
                {"text": "において", "isCorrect": False, "reason": "【不正解】場所標示（〜で）であり、範囲の終点には合いません。", "trapCategory": "meaning"},
                {"text": "に際して", "isCorrect": False, "reason": "【不正解】機会表現であり不適。", "trapCategory": "meaning"},
                {"text": "に関して", "isCorrect": False, "reason": "【不正解】テーマ表現であり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which pattern expresses continuous geographical coverage from region A through region B?"
    },
    {
        "id": "skm3-p2-c4-q8",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Correlative double parallel: this hotel offers both picturesque scenery and exquisite hot spring waters.",
        "question": "この温泉旅館は、窓からの眺め（　）よければ、お湯の泉質（　）最高だ。",
        "translation": "At this hot spring inn, both the view from the window is wonderful, and the quality of the hot spring water is superb.",
        "options": ["も・も", "は・は", "が・が", "も・が"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「名詞も＋動詞ば／い形ければ＋名詞も」は、『〜も〜だし、〜も〜だ』という二つの美点を並立して強調する固定構文です。",
            "options": [
                {"text": "も・も", "isCorrect": True, "reason": "【正解】眺めもよければ、泉質も最高だ（二重「も」の並立固定構文）。", "trapCategory": ""},
                {"text": "は・は", "isCorrect": False, "reason": "【不正解】対比重複になり並立になりません。", "trapCategory": "formation"},
                {"text": "が・が", "isCorrect": False, "reason": "【不正解】主格重複で固定呼応になりません。", "trapCategory": "formation"},
                {"text": "も・が", "isCorrect": False, "reason": "【不正解】後件に「も」が必要です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What correlative particle must appear in both slots of the 'A も ...ば, B も...' construction?"
    },
    {
        "id": "skm3-p2-c4-q9",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Organizational center: international research team centered on Japanese scholars.",
        "question": "日本人学者を中心（　）国際研究チームが、新種の深海生物を発見した。",
        "translation": "An international research team centered on Japanese scholars discovered a new species of deep-sea organism.",
        "options": ["とした", "として", "に", "で"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "後ろの名詞（国際研究チーム）を修飾するため、連体形「〜を中心とした＋名詞」が正解です（※「として」は述語を修飾する連用形）。",
            "options": [
                {"text": "とした", "isCorrect": True, "reason": "【正解】〜を中心とした＋名詞（名詞修飾連体形）。", "trapCategory": ""},
                {"text": "として", "isCorrect": False, "reason": "【不正解】連用形であり、名詞「国際研究チーム」を直接修飾できません。", "trapCategory": "formation"},
                {"text": "に", "isCorrect": False, "reason": "【不正解】助詞「に」単独では名詞修飾不可。", "trapCategory": "formation"},
                {"text": "で", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Notice that the next word is a noun (国際研究チーム); which attributive form of とする is required?"
    },
    {
        "id": "skm3-p2-c4-q10",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Scrambled order reconstruction (星マーク問題): assembling fixed patterns in order.",
        "question": "この映画は ★ 入る言葉として最も適切なものはどれか。「この映画は （ 1 大人から ） （ 2 こどもまで ） （ 3 ★ ） （ 4 幅広い層に ） 愛されている。」",
        "translation": "Which word goes into the star position? (This movie is loved by a wide range of people, from adults to children.)",
        "options": ["幅広い層に", "大人から", "こどもまで", "愛されている"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "正しい順序は「この映画は [大人から (1)] [こどもまで (2)] [幅広い層に (4)] (★) 愛されている」。3番目の★に入るのは「幅広い層に (4)」です。",
            "options": [
                {"text": "幅広い層に", "isCorrect": True, "reason": "【正解】語順: 1 大人から -> 2 こどもまで -> 4 幅広い層に (★) -> 愛されている。", "trapCategory": ""},
                {"text": "大人から", "isCorrect": False, "reason": "【不正解】1番目の要素です。", "trapCategory": "formation"},
                {"text": "こどもまで", "isCorrect": False, "reason": "【不正解】2番目の要素です。", "trapCategory": "formation"},
                {"text": "愛されている", "isCorrect": False, "reason": "【不正解】述語です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Combine the span: [A から] + [B まで] + [Target Audience に] + [Verb]."
    },
    {
        "id": "skm3-p2-c4-q11",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Reconstruction of repeating concession: expensive indeed, but worth every penny.",
        "question": "値段が ★ 入る言葉として最も適切なものはどれか。「値段が （ 1 高いことは ） （ 2 高いが ） （ 3 ★ ） （ 4 それだけの価値が ） 十分にある。」",
        "translation": "Which word goes into the star position? (Expensive indeed it is, but it has plenty of value to match that price.)",
        "options": ["それだけの価値が", "高いことは", "高いが", "十分にある"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "正しい順序は「値段が [高いことは (1)] [高いが (2)] [それだけの価値が (4)] (★) 十分にある」。3番目の★に入るのは「それだけの価値が (4)」です。",
            "options": [
                {"text": "それだけの価値が", "isCorrect": True, "reason": "【正解】語順: 1 高いことは -> 2 高いが -> 4 それだけの価値が (★) -> 十分にある。", "trapCategory": ""},
                {"text": "高いことは", "isCorrect": False, "reason": "【不正解】1番目の要素です。", "trapCategory": "formation"},
                {"text": "高いが", "isCorrect": False, "reason": "【不正解】2番目の要素です。", "trapCategory": "formation"},
                {"text": "十分にある", "isCorrect": False, "reason": "【不正解】述語部分です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Reconstruct the concession formula: [高いことは] + [高いが] + [Main clause subject] + [Predicate]."
    },
    {
        "id": "skm3-p2-c4-q12",
        "bookId": "skm-n3",
        "chapter": "Part 2 · Chapter 4",
        "type": "multiple-choice",
        "context": "Fixed pattern of extreme prerequisite: if only one has courage, one can open a path forward.",
        "question": "困難な道であっても、一歩踏み出す勇気（　）あれば、必ず道は開ける。",
        "translation": "Even on a difficult road, if only you have the courage to take a step forward, a path will surely open up.",
        "options": ["さえ", "こそ", "でも", "なら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-p2-4-127",
        "grammarPointTitle": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns)",
        "explanation": {
            "overall": "「名詞＋さえ＋動詞ば形（あれば）」は、必須の唯一条件を示す固定構文「勇気さえあれば」です。",
            "options": [
                {"text": "さえ", "isCorrect": True, "reason": "【正解】勇気さえあれば（さえ〜ば固定構文）。", "trapCategory": ""},
                {"text": "こそ", "isCorrect": False, "reason": "【不正解】強調助詞であり、条件形と固定ペアになりません。", "trapCategory": "nuance"},
                {"text": "でも", "isCorrect": False, "reason": "【不正解】例示助詞になり不適。", "trapCategory": "meaning"},
                {"text": "なら", "isCorrect": False, "reason": "【不正解】条件形「あれば」と重複して破綻。", "trapCategory": "formation"}
            ]
        },
        "hint": "What particle completes the fixed formula for a crucial prerequisite preceding あれば?"
    }
]

p2_exercises.extend(p2_c1_exercises)
p2_exercises.extend(p2_c2_exercises)
p2_exercises.extend(p2_c3_exercises)
p2_exercises.extend(p2_c4_exercises)

# Update chapterExercises.json
existing_exs = json.load(open(CHAPTER_EXERCISES_PATH, encoding="utf-8"))
p2_chapters = {"Part 2 · Chapter 1", "Part 2 · Chapter 2", "Part 2 · Chapter 3", "Part 2 · Chapter 4"}
existing_exs = [x for x in existing_exs if x.get("chapter") not in p2_chapters and not x.get("id", "").startswith("skm3-p2-")]
existing_exs.extend(p2_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(existing_exs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with 48 exercises for SKM N3 Part 2! Total: {len(existing_exs)}")

# ==========================================
# 2. Enrich base-reviewed.json
# ==========================================
base_cards = json.load(open(BASE_PATH, encoding="utf-8"))

card_enrichments = {
    "added-n3-p2-1-124": {
        "title": "文の組み立て 1: 引用 (Quotation & Citation Structure: と・ように言う・とのことだ)",
        "meaning": "Systematic mastery of quotation frames and reported speech structures: direct quotes in brackets, indirect statement transmission with と, indirect imperative/request transmission with ように言う, and formal source attribution with 〜とのことだ / ということだ.",
        "formation": "①【直接発話】「〜」と言って＋後続動作\n②【間接陳述】普通形 ＋ と伝える／主張する／思う\n③【間接指示】動詞辞書形／ない形 ＋ ように言う／指示する／頼む\n④【同格名詞】普通形 ＋ という ＋ 名詞（噂・知らせ・意見）\n⑤【公的伝聞】〜によると ＋ 普通形 ＋ とのことだ／ということだ",
        "explanation": "【教科書規則と文法体系 (SKM N3 pp. 104-105)】\n1. 引用助詞「と」と「ように」の決定的な違い:\n   - 「〜と伝えてください」: 発言した事実・内容をそのまま中立的に伝える（例: 遅れると伝える）。\n   - 「〜ように伝えてください」: 相手に行動を促す依頼・指示・命令の内容を伝える（例: 早く来るように伝える）。\n2. 同格内容の修飾:\n   - 節が名詞（噂、ニュース、知らせ）の内容を直接説明する場合、「という」を介して接続する（例: 結婚したという噂）。\n3. JLPT第2問（文の組み立て ★問題）攻略法:\n   - 発言内容節をひとまとまりにして「と」「ように」を特定し、主節の伝達動詞（言った、頼まれた）に繋げる。",
        "examples": [
            {
                "japanese": "課長に、電車の遅延で10分ほど遅れると伝えていただけますか。",
                "english": "Could you please tell the section manager that I will be about 10 minutes late due to a train delay?",
                "nuance": "普通形＋と伝える: Indirect factual statement transmission."
            },
            {
                "japanese": "医師から、塩分を控えてできるだけ薄味の食事にするように強く言われた。",
                "english": "I was strongly told by the doctor to cut down on salt and eat meals seasoned as lightly as possible.",
                "nuance": "動詞辞書形＋ように言われた: Indirect medical directive."
            },
            {
                "japanese": "あの人気歌手が極秘で結婚したという噂が、ネット上で急速に広がっている。",
                "english": "Rumors that the popular singer got married in absolute secret are spreading rapidly on the internet.",
                "nuance": "普通形＋という＋噂: Content-specifying appositive quotation."
            },
            {
                "japanese": "天気予報によると、明日は全国的に真冬並みの寒さになるとのことだ。",
                "english": "According to the weather forecast, it is reported that temperatures tomorrow will become midwinter-like nationwide.",
                "nuance": "〜によると…とのことだ: Formal objective hearsay attribution."
            }
        ]
    },
    "added-n3-p2-2-125": {
        "title": "文の組み立て 2: 名詞の説明 (Noun Modification & Description Structures)",
        "meaning": "Comprehensive rules of Japanese relative clause embedding and prenominal modification: verb/adjective clauses preceding nouns, particle compounds with の (への/からの/での), compound postposition modifiers (についての/に対する/としての), and mimetic modifiers with の.",
        "formation": "①【普通形連体修飾】普通形（Naな / Nの）＋ 名詞\n②【助詞＋の】助詞（へ／から／で／まで）＋ の ＋ 名詞 ※「にの」は不可！\n③【助詞相当語句】についての / に対する / としての / にとっての ＋ 名詞\n④【オノマトペ】状態副詞 ＋ の ＋ 名詞（ぴかぴかの靴、ばらばらの意見）",
        "explanation": "【教科書規則と文法体系 (SKM N3 pp. 106-107)】\n1. 日本語の厳格な修飾方向規則:\n   - 英語の関係代名詞（後ろから修飾）と異なり、日本語の名詞修飾語句は例外なく『修飾される名詞の前』に位置します。\n2. 助詞の名詞修飾制約:\n   - 助詞「に」は直接「にの」とは言えません。「先生への手紙」（宛先）、「先生に対する尊敬」（対象）などの代替形式をとります。\n3. 修飾節内部の主語標示:\n   - 連体修飾節内部の主語は「は」ではなく「が」または「の」で標示されます（例: 祖母が焼いてくれたパン）。",
        "examples": [
            {
                "japanese": "机の上に置いてあるのは、お世話になった高校の先生への手紙です。",
                "english": "What is placed on the desk is a letter addressed to my high school teacher who took care of me.",
                "nuance": "助詞「へ」＋の＋名詞: Directional recipient modification (avoiding *にの)."
            },
            {
                "japanese": "彼が学会で発表したのは、地球温暖化についての修士論文だった。",
                "english": "What he presented at the academic conference was a master's thesis concerning global warming.",
                "nuance": "〜について＋の＋名詞: Thematic topic modifying master's thesis."
            },
            {
                "japanese": "役員会では、A案に対する反対意見が相次ぎ、結論は次回に持ち越された。",
                "english": "In the board meeting, opposing opinions toward Plan A emerged one after another, and the conclusion was carried over to the next meeting.",
                "nuance": "〜に対する＋名詞: Opposition attitude modifying opinion."
            },
            {
                "japanese": "就職活動のために靴を磨き上げ、ぴかぴかの革靴を履いて面接に向かった。",
                "english": "I polished my shoes for job hunting, and headed to the interview wearing sparkling clean leather shoes.",
                "nuance": "オノマトペ＋の＋名詞: Sparkling mimetic state modifying leather shoes."
            }
        ]
    },
    "added-n3-p2-3-126": {
        "title": "文の組み立て 3: 「という」・「といった」 (Naming, Content & Representative Listing)",
        "meaning": "Systematic taxonomy of という and といった in clausal sentence architecture: naming proper entities (〜という), conveying propositional content/news, defining terms (〜ということは…ということだ / 〜とは…のことだ), and grouping representative series under an umbrella category (〜といった).",
        "formation": "①【名称紹介】固有名称 ＋ という ＋ 普通名詞\n②【内容提示】普通形 ＋ という ＋ 名詞（知らせ・噂・印象・合意）\n③【定義・説明】用語 ＋ とは、〜のことだ / 〜ということは、…ということだ\n④【代表例示包括】例A や 例B ＋ といった ＋ 包括名詞",
        "explanation": "【教科書規則と文法体系 (SKM N3 pp. 108-109)】\n1. 「という」vs「といった」の明確な機能分担:\n   - 「という」: 単一の名称の命名・紹介、または節の具体的・同格内容の提示に用いる。\n   - 「といった」: 複数の代表的な具体例を挙げ、後ろの包括カテゴリー名詞（科目、色、家電、伝統文化）にまとめる。\n2. 定義の構文フレーム:\n   - 「用語＋とは、〜のことだ」は略語・専門用語の字義説明の黄金パターン。\n   - 「〜ということは、…ということだ」は命題・標語の実質的意味を解釈する定番パターン。",
        "examples": [
            {
                "japanese": "数学や物理、化学といった理科系の科目は、論理的思考力を養うのに役立つ。",
                "english": "Science subjects such as mathematics, physics, and chemistry are helpful for cultivating logical thinking skills.",
                "nuance": "AやB＋といった＋包括名詞: Representative listing under general category."
            },
            {
                "japanese": "東南アジアには、「ドリアン」という非常に強烈な匂いのする果物がある。",
                "english": "In Southeast Asia, there is a fruit with an extremely intense odor called 'durian'.",
                "nuance": "名称＋という＋普通名詞: Introducing the name of an entity."
            },
            {
                "japanese": "全館禁煙ということは、会場内のどこでもタバコを吸ってはいけないということだ。",
                "english": "The fact that the entire building is non-smoking means that you must not smoke tobacco anywhere in the venue.",
                "nuance": "〜ということは、…ということだ: Canonical definition framework."
            },
            {
                "japanese": "茶道や華道、書道といった日本の伝統文化を体験するため、多くの外国人が訪れている。",
                "english": "To experience Japanese traditional culture such as tea ceremony, flower arrangement, and calligraphy, many foreigners are visiting.",
                "nuance": "Representative cultural arts grouped under 日本の伝統文化."
            }
        ]
    },
    "added-n3-p2-4-127": {
        "title": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns & Paired Formulas)",
        "meaning": "Mastery of fixed, two-part correlative grammatical constructions in Japanese syntax: continuous span (〜から〜にかけて), purposeful regard (〜を〜として/とする/とした), universal baseline expansion (〜はもちろん), sufficient prerequisite (〜さえ〜ば), repeating concession (〜ことは〜が), and proportional change (〜ば〜ほど).",
        "formation": "①【範囲】A から B にかけて\n②【位置づけ】A を B として / とした ＋ 名詞\n③【累加】A はもちろん、B も\n④【必須条件】N さえ V-ば\n⑤【反復譲歩】V-た ことは V-た が\n⑥【比例】V-ば V-辞書形 ほど\n⑦【二重並立】N も V-ば、N も V",
        "explanation": "【教科書規則と文法体系 (SKM N3 pp. 110-111)】\n1. 固定構文（決まった形）の不可分性:\n   - これらの構文は、前文の特定助詞（から、を、さえ、ことは）が、後文の特定形式（にかけて、として、ば、が）と不可分に結びついています。\n2. JLPT星マーク問題（文の組み立て）必勝法:\n   - 4つの選択肢の中に固定ペアの断片（例: 「から」と「にかけて」、「を」と「として」）を見つけたら、まずそのブロックを即座に結合してから、主語・述語の枠組みに配置します。",
        "examples": [
            {
                "japanese": "昨夜から今朝の明け方にかけて、関東地方を中心に非常に激しい雨が降った。",
                "english": "From last night through dawn this morning, extremely heavy rain fell primarily centered on the Kanto region.",
                "nuance": "〜から〜にかけて: Approximate continuous temporal span."
            },
            {
                "japanese": "新年度のサークル活動は、「健康第一」を目標として、無理のないペースで進めます。",
                "english": "In our club activities for the new academic year, taking 'Health First' as our objective, we will proceed at a reasonable pace.",
                "nuance": "〜を〜として: Taking A as objective B."
            },
            {
                "japanese": "このアニメ作品は、日本国内はもちろん海外でも熱狂的なファンを獲得している。",
                "english": "This anime work has gained passionate fans not only domestically in Japan as a matter of course, but overseas as well.",
                "nuance": "〜はもちろん…も: Baseline taken for granted, expanding to external scope."
            },
            {
                "japanese": "どんなに貧しくても、体さえ健康であれば、何とか乗り越えていける。",
                "english": "No matter how poor we may be, as long as our bodies are healthy (provided that sole prerequisite is met), we can manage to overcome it.",
                "nuance": "〜さえ〜ば: Absolute sufficient prerequisite formula."
            }
        ]
    }
}

for c in base_cards:
    if c["id"] in card_enrichments:
        data = card_enrichments[c["id"]]
        c["title"] = data["title"]
        c["meaning"] = data["meaning"]
        c["formula"] = data["formation"]
        c["explanation"] = data["explanation"]
        c["examples"] = data["examples"]

BASE_PATH.write_text(json.dumps(base_cards, ensure_ascii=False, indent=2), encoding="utf-8")
print("Enriched all 4 Part 2 cards in base-reviewed.json!")

# ==========================================
# 3. Update source-coverage-matrix.json
# ==========================================
matrix = json.load(open(MATRIX_PATH, encoding="utf-8"))

p2_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 2 · Chapter 1",
        "exactPrintedPages": "pp. 104-105",
        "exactPdfPages": "pp. 127-128",
        "grammarItem": "文の組み立て 1: 引用 (Quotation & Citation Structure)",
        "instructionalDetails": "Structural quotation frames: direct speech brackets with 言って, indirect speech with と伝える/思う, indirect imperatives with ように言う, content-specifying という, and formal transmission with とのことだ.",
        "cardId": "added-n3-p2-1-124",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-p2-1-124::s-skm3-p2-1",
            "added-n3-p2-1-124::s-skm3-p2-2",
            "added-n3-p2-1-124::s-skm3-p2-3",
            "added-n3-p2-1-124::s-skm3-p2-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 104-105 (PDF pp. 127-128). Verified sentence reconstruction frames for direct quotes, indirect statements, indirect commands (ように), and source reporting."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 2 · Chapter 2",
        "exactPrintedPages": "pp. 106-107",
        "exactPdfPages": "pp. 129-130",
        "grammarItem": "文の組み立て 2: 名詞の説明 (Noun Modification & Description Structures)",
        "instructionalDetails": "Prenominal relative clause syntax: verb/adjective clauses preceding nouns, particle compounds with の (への/からの/での; strict ban on *にの), compound postposition modifiers (についての/に対する/としての), and mimetic state modifiers with の.",
        "cardId": "added-n3-p2-2-125",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-p2-2-125::s-skm3-p2-5",
            "added-n3-p2-2-125::s-skm3-p2-6",
            "added-n3-p2-2-125::s-skm3-p2-7",
            "added-n3-p2-2-125::s-skm3-p2-8"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 106-107 (PDF pp. 129-130). Verified strict Japanese prenominal modification rules, particle compound attachments, and relative clause internal subject marking with が."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 2 · Chapter 3",
        "exactPrintedPages": "pp. 108-109",
        "exactPdfPages": "pp. 131-132",
        "grammarItem": "文の組み立て 3: 「という」・「といった」 (Naming, Content & Representative Listing)",
        "instructionalDetails": "Clausal sentence architecture: naming entities (固有名称＋という), conveying propositional content (知らせ/噂＋という), formal definition frames (〜とは…のことだ), and representative example listing under general categories (AやB＋といった＋包括名詞).",
        "cardId": "added-n3-p2-3-126",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-p2-3-126::s-skm3-p2-9",
            "added-n3-p2-3-126::s-skm3-p2-10",
            "added-n3-p2-3-126::s-skm3-p2-11",
            "added-n3-p2-3-126::s-skm3-p2-12"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 108-109 (PDF pp. 131-132). Verified functional boundary between singular naming/content (という) and umbrella category listing (といった)."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 2 · Chapter 4",
        "exactPrintedPages": "pp. 110-111",
        "exactPdfPages": "pp. 133-134",
        "grammarItem": "文の組み立て 4: 決まった形 (Fixed Syntactic Patterns & Paired Formulas)",
        "instructionalDetails": "Mastery of fixed correlative pairs: continuous span (〜から〜にかけて), objective regard (〜を〜として/とする/とした), baseline expansion (〜はもちろん), prerequisite (〜さえ〜ば), repeating concession (〜ことは〜が), and proportional increase (〜ば〜ほど).",
        "cardId": "added-n3-p2-4-127",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-p2-4-127::s-skm3-p2-13",
            "added-n3-p2-4-127::s-skm3-p2-14",
            "added-n3-p2-4-127::s-skm3-p2-15",
            "added-n3-p2-4-127::s-skm3-p2-16"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 110-111 (PDF pp. 133-134). Verified all 7 core two-part fixed correlative frames for scrambled sentence assembly in JLPT Question 2."
    }
]

existing_card_ids = {e.get("cardId") for e in p2_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(p2_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Part 2 in source coverage matrix! Total certified rows: {len(matrix)}")
