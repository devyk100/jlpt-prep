import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
BASE_PATH = ROOT / "content/base-reviewed.json"
CHAPTER_EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"

# 1. 12 Authentic Exercises for Form Review H
fh_exercises = [
    {
        "id": "skm3-fh-q1",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Discovery upon opening window: speaker opened window and unexpectedly discovered snow covering the street outside.",
        "question": "朝起きて窓を（　）、外は一面の銀世界になっていた。",
        "translation": "When I woke up in the morning and opened the window, I discovered that outside had turned into a blanket of snow.",
        "options": ["開けると", "開ければ", "開けるなら", "開けるように"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞辞書形＋と」は、ある動作を行った直後に『意外な先行状態や新しい事実に気が付く（発見・気付き）』用法を持ちます。後件は話者の意志動作ではなく、すでに生起していた客観的状態を表す過去形（〜ていた）が多用されます。",
            "options": [
                {"text": "開けると", "isCorrect": True, "reason": "【正解】動詞辞書形＋と（動作直後の意外な発見・気づき）。", "trapCategory": ""},
                {"text": "開ければ", "isCorrect": False, "reason": "【不正解】「〜ば」の後件には過去の事実・確定した出来事（〜ていた）を直接置くことはできません。", "trapCategory": "formation"},
                {"text": "開けるなら", "isCorrect": False, "reason": "【不正解】「なら」は文脈の話題化・助言であり、過去の発見には使えません。", "trapCategory": "meaning"},
                {"text": "開けるように", "isCorrect": False, "reason": "【不正解】目的表現となり文脈不一致。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which conditional pattern connects to a past-tense surprise discovery (...ていた) upon taking an action?"
    },
    {
        "id": "skm3-fh-q2",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Unexpected arrival state: when speaker arrived at the platform, the train had already departed.",
        "question": "急いで駅のホームに（　）、乗るはずだった電車はすでに出発していた。",
        "translation": "When I hurried to the station platform, the train I was supposed to take had already departed.",
        "options": ["着いたら", "着けば", "着くなら", "着くように"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞た形＋ら」は、ある場所に着いた・動作を完了した直後に『すでに対象の状態が変わっていたことに気が付く』発見用法を表します（「〜ば」は過去の事実発見には使えません）。",
            "options": [
                {"text": "着いたら", "isCorrect": True, "reason": "【正解】動詞た形＋ら（動作後の意外な事実・先行状況の発見）。", "trapCategory": ""},
                {"text": "着けば", "isCorrect": False, "reason": "【不正解】「〜ば」の後件に過去形（出発していた）を置くことは文法的に不可。", "trapCategory": "formation"},
                {"text": "着くなら", "isCorrect": False, "reason": "【不正解】条件提示・意図表現となり、過去の発見に合いません。", "trapCategory": "meaning"},
                {"text": "着くように", "isCorrect": False, "reason": "【不正解】目的表現。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What pattern expresses arriving at a destination only to discover an already transpired situation?"
    },
    {
        "id": "skm3-fh-q3",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Accidental occurrence during action: while taking an evening stroll, rain suddenly began to pour.",
        "question": "公園を（　）ていると、突然雷が鳴って激しい雨が降り出した。",
        "translation": "While I was strolling through the park, thunder suddenly roared and heavy rain began to pour down.",
        "options": ["散歩し", "散歩する", "散歩した", "散歩すれば"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞て形＋いると（ていたら）」は、ある動作を行っている最中に『偶然・思いがけず予想外の出来事が発生する』偶発的生起を表します。後件は話者の意志動作ではなく、無意志の出来事が来ます。",
            "options": [
                {"text": "散歩し", "isCorrect": True, "reason": "【正解】散歩していると（継続動作中の偶発的出来事の発生）。", "trapCategory": ""},
                {"text": "散歩する", "isCorrect": False, "reason": "【不正解】散歩するとていると、となり接続文法が破綻しています。", "trapCategory": "formation"},
                {"text": "散歩した", "isCorrect": False, "reason": "【不正解】過去形接続不可。", "trapCategory": "formation"},
                {"text": "散歩すれば", "isCorrect": False, "reason": "【不正解】ば＋ているとは非文。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which aspectual construction (〜ていると) marks an unforeseen event occurring midway through an ongoing action?"
    },
    {
        "id": "skm3-fh-q4",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Immediate consecutive action by same subject: colleague entered the room and immediately collapsed onto the couch without saying a word.",
        "question": "彼は部屋に（　）と、何も言わずにソファに倒れ込んだ。",
        "translation": "The moment he entered the room, he collapsed onto the couch without saying a single word.",
        "options": ["入る", "入った", "入れば", "入るなら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞辞書形＋と」は、同一の主語が『ある動作を完了した直後、間髪を入れずに次の動作を行う』即時連続動作を表します（前件と後件の主語は同一）。",
            "options": [
                {"text": "入る", "isCorrect": True, "reason": "【正解】動詞辞書形＋と（同一主語による即時連続動作）。", "trapCategory": ""},
                {"text": "入った", "isCorrect": False, "reason": "【不正解】「〜たと」という接続形は現代語文法に存在しません。", "trapCategory": "formation"},
                {"text": "入れば", "isCorrect": False, "reason": "【不正解】「〜ば」の後件に過去の一回的意志動作（倒れ込んだ）は置けません。", "trapCategory": "formation"},
                {"text": "入るなら", "isCorrect": False, "reason": "【不正解】文脈不一致。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What pattern expresses an instantaneous sequence of actions executed by the same subject?"
    },
    {
        "id": "skm3-fh-q5",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Parallel correlative addition: popular bistro offers both delicious cuisine and reasonable pricing.",
        "question": "駅前の新しいビストロは、料理（　）おいしければ値段（　）手頃で、連日大盛況だ。",
        "translation": "The new bistro in front of the station has both delicious food and reasonable prices, drawing huge crowds every day.",
        "options": ["も・も", "は・は", "が・が", "も・が"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「名詞も＋動詞ば／い形ければ／な形なら＋名詞も」は、『〜も〜だし、〜も〜だ（双方が兼ね備わっている）』という並立・累加を表す定番構文です。",
            "options": [
                {"text": "も・も", "isCorrect": True, "reason": "【正解】名詞も…ければ、名詞も…（二つの好条件の並立呼応）。", "trapCategory": ""},
                {"text": "は・は", "isCorrect": False, "reason": "【不正解】対比助詞の重複となり、並立累加構文になりません。", "trapCategory": "formation"},
                {"text": "が・が", "isCorrect": False, "reason": "【不正解】主格助詞の連続で並立呼応になりません。", "trapCategory": "formation"},
                {"text": "も・が", "isCorrect": False, "reason": "【不正解】後件助詞が「も」と呼応していません。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which correlative particle repeats twice in the pattern 'A も ...ば, B も...'?"
    },
    {
        "id": "skm3-fh-q6",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Discovery of unexpected subject: different subject constraint in discovery と.",
        "question": "カーテンを開けると、庭で小鳥たちが（　）。",
        "translation": "When I opened the curtains, little birds were chirping happily in the garden.",
        "options": ["楽しそうに鳴いていた", "楽しそうに鳴くつもりだ", "楽しそうに鳴きなさい", "楽しそうに鳴くべきだ"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "発見用法「〜と」では、前件の主語（話者）と後件の主語（小鳥たち）が異なり、後件には過去の継続状態（〜ていた）が来ます。命令・意志・当為表現を後件に置くことはできません。",
            "options": [
                {"text": "楽しそうに鳴いていた", "isCorrect": True, "reason": "【正解】過去の客観的発見状態を表す「〜ていた」。", "trapCategory": ""},
                {"text": "楽しそうに鳴くつもりだ", "isCorrect": False, "reason": "【不正解】小鳥の意志推量になり文脈破綻。", "trapCategory": "meaning"},
                {"text": "楽しそうに鳴きなさい", "isCorrect": False, "reason": "【不正解】命令文は「と」の後件に置けません。", "trapCategory": "formation"},
                {"text": "楽しそうに鳴くべきだ", "isCorrect": False, "reason": "【不正解】当為表現は置けません。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What verbal predicate naturally completes a discovery sentence indicating an ongoing scene observed?"
    },
    {
        "id": "skm3-fh-q7",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Result outcome: taking the prescribed medicine resulted in the high fever abating.",
        "question": "医師から処方された解熱剤を（　）、夜にはすっかり熱が下がった。",
        "translation": "When I took the fever reducer prescribed by the doctor, my fever came down completely by nighttime.",
        "options": ["飲んだら", "飲めば", "飲むなら", "飲むと"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞た形＋ら」は、ある行為を行った結果として『予期された、または予想以上の好転・結果が起きた』因果結果の発生を表します（過去の事実生起には「〜ば」不可）。",
            "options": [
                {"text": "飲んだら", "isCorrect": True, "reason": "【正解】動詞た形＋ら（行為の結果、事態が起きたことを表す過去生起用法）。", "trapCategory": ""},
                {"text": "飲めば", "isCorrect": False, "reason": "【不正解】後件に過去の一回的事実（熱が下がった）を置くことはできません。", "trapCategory": "formation"},
                {"text": "飲むなら", "isCorrect": False, "reason": "【不正解】前提条件になり、すでに飲んだ結果の文脈に合いません。", "trapCategory": "meaning"},
                {"text": "飲むと", "isCorrect": False, "reason": "【不正解】「〜と」は即時変化または一般的な恒常法則に向いており、数時間後の解熱には「たら」が最も自然です。", "trapCategory": "nuance"}
            ]
        },
        "hint": "Which conditional pattern connects an action in the past to an outcome that transpires later in the evening?"
    },
    {
        "id": "skm3-fh-q8",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Correlative negative parallel: in the midst of depression, speaker has neither appetite nor desire to go outside.",
        "question": "体調を崩して以来、食欲も（　）、外出しようという気力も湧かない。",
        "translation": "Since falling ill, I have neither an appetite, nor do I feel any energy to go outside.",
        "options": ["なければ", "ないと", "ないなら", "なくて"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「名詞も＋なければ（動詞ない形＋なければ）、名詞も＋ない」で、『〜もなければ〜もない（二重の否定並立）』を表します。",
            "options": [
                {"text": "なければ", "isCorrect": True, "reason": "【正解】も…なければ、も…ない（定番の二重否定並立構文）。", "trapCategory": ""},
                {"text": "ないと", "isCorrect": False, "reason": "【不正解】並立相関構文として呼応しません。", "trapCategory": "formation"},
                {"text": "ないなら", "isCorrect": False, "reason": "【不正解】条件推量となり並立の文脈に合いません。", "trapCategory": "meaning"},
                {"text": "なくて", "isCorrect": False, "reason": "【不正解】「もなくて」は相関並立として不自然です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What is the canonical negative form in 'A も [form], B もない'?"
    },
    {
        "id": "skm3-fh-q9",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Proportional increase: the more deeply you analyze this problem, the more complex it reveals itself to be.",
        "question": "この課題は、深く（　）掘り下げるほど、新たな謎が見つかる。",
        "translation": "The more deeply you dig into this topic, the more new mysteries you uncover.",
        "options": ["掘り下げれば", "掘り下げると", "掘り下げるなら", "掘り下げたら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞ば形＋動詞辞書形＋ほど」は、『〜すればするほど（一方の度合いが高まるにつれて他方も進む）』という比例変化を表す厳格な構文です。",
            "options": [
                {"text": "掘り下げれば", "isCorrect": True, "reason": "【正解】動詞ば形＋辞書形＋ほど（比例相関構文）。", "trapCategory": ""},
                {"text": "掘り下げると", "isCorrect": False, "reason": "【不正解】「〜と…ほど」という相関構文は存在しません。", "trapCategory": "formation"},
                {"text": "掘り下げるなら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"},
                {"text": "掘り下げたら", "isCorrect": False, "reason": "【不正解】口語的崩れ表現であり、教科書の正統比例構文では「ば」が必須です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What is the textbook conditional form preceding 'Verb-dict + ほど'?"
    },
    {
        "id": "skm3-fh-q10",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Unexpected meeting while doing: ran into high school teacher while shopping at the department store.",
        "question": "デパートで買い物を（　）、偶然高校時代の担任の先生にお会いした。",
        "translation": "While I was shopping at the department store, I accidentally ran into my high school homeroom teacher.",
        "options": ["していたら", "すれば", "するなら", "したところ"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞て形＋いたら」は、ある行為の継続中に『偶然・予期せぬ出会いや出来事が発生した』偶発的遭遇を表します（「〜ば」は過去の一回的事実遭遇に使えません）。",
            "options": [
                {"text": "していたら", "isCorrect": True, "reason": "【正解】動詞て形＋いたら（動作継続中の偶然の出会い・出来事）。", "trapCategory": ""},
                {"text": "すれば", "isCorrect": False, "reason": "【不正解】過去の事実出来事には使えません。", "trapCategory": "formation"},
                {"text": "するなら", "isCorrect": False, "reason": "【不正解】仮定前提となり、過去の出来事の描写に合いません。", "trapCategory": "meaning"},
                {"text": "したところ", "isCorrect": False, "reason": "【不正解】「買い物したところ、お会いした」は不自然（継続中の遭遇には「していたら」）。", "trapCategory": "nuance"}
            ]
        },
        "hint": "Which pattern marks an accidental encounter taking place during an ongoing activity?"
    },
    {
        "id": "skm3-fh-q11",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Contextual advice: if you are going to climb Mount Fuji, you should prepare warm thermal clothing.",
        "question": "富士山に（　）、夏でも防寒着をしっかり準備していったほうがいいですよ。",
        "translation": "If you are going to climb Mount Fuji, you had better prepare warm thermal clothing even in the summer.",
        "options": ["登るなら", "登ると", "登ったら", "登れば"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "相手の意図・予定（富士山に登る予定）を話題に取り上げて助言・忠告を行う場合、「動詞辞書形＋なら」を用います（「と」や「ば」の後件に助言・忠告「〜ほうがいい」を直接置くことは制限されます）。",
            "options": [
                {"text": "登るなら", "isCorrect": True, "reason": "【正解】相手の予定・意向を取り上げて助言する「〜なら」。", "trapCategory": ""},
                {"text": "登ると", "isCorrect": False, "reason": "【不正解】「〜と」の後件に助言・働きかけ（〜ほうがいい）は置けません。", "trapCategory": "formation"},
                {"text": "登ったら", "isCorrect": False, "reason": "【不正解】「登ったら準備しろ」だと時系列が逆転してしまいます（登る前に準備が必要）。", "trapCategory": "nuance"},
                {"text": "登れば", "isCorrect": False, "reason": "【不正解】意志動詞の「ば」の後件に助言・忠告は置けません。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which conditional particle takes an opponent's future intent as premise and permits advice prior to the act?"
    },
    {
        "id": "skm3-fh-q12",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review H",
        "type": "multiple-choice",
        "context": "Immediate action: secretary received incoming phone call and immediately began taking notes.",
        "question": "秘書は受話器を（　）と、素早く手元のメモ帳にペンを走らせた。",
        "translation": "The moment the secretary picked up the receiver, she swiftly ran her pen across her notepad.",
        "options": ["取る", "取った", "取れば", "取るなら"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-h-66",
        "grammarPointTitle": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "explanation": {
            "overall": "「動詞辞書形＋と」は、同一主語（秘書）が受話器を取る動作に間髪入れずメモを取る即時連続動作を表す典型構文です。",
            "options": [
                {"text": "取る", "isCorrect": True, "reason": "【正解】動詞辞書形＋と（同一主語による即時連続描写）。", "trapCategory": ""},
                {"text": "取った", "isCorrect": False, "reason": "【不正解】「〜たと」という接続は非文です。", "trapCategory": "formation"},
                {"text": "取れば", "isCorrect": False, "reason": "【不正解】過去の一回的連続動作には使えません。", "trapCategory": "formation"},
                {"text": "取るなら", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What pattern expresses an instant trigger-reaction sequence performed by the same subject?"
    }
]

# Update chapterExercises.json
existing_exs = json.load(open(CHAPTER_EXERCISES_PATH, encoding="utf-8"))
existing_exs = [x for x in existing_exs if x.get("chapter") != "Part 1 · Form review H" and x.get("chapterId") != "skm3-fh"]
existing_exs.extend(fh_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(existing_exs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with 12 exercises for SKM N3 Form Review H! Total: {len(existing_exs)}")

# 2. Enrich base-reviewed.json
base_cards = json.load(open(BASE_PATH, encoding="utf-8"))

card_enrichments = {
    "added-n3-h-66": {
        "title": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "meaning": "Systematic taxonomy of non-hypothetical operational usages of conditional markers: unexpected discovery of preexisting state (V-と / V-たら ...ていた), accidental occurrence midway (V-ていると / ていたら), outcome generation, immediate consecutive action by same subject (V-dict と), and correlative parallel addition (Aも...ば, Bも...).",
        "formation": "①【発見】V辞書形＋と / Vた＋ら（主語不一致、後件〜ていた）\n②【偶発】Vている＋と / てい＋たら（後件無意志・意外な出来事）\n③【即時連続】V辞書形＋と（同一主語・間髪を入れない連続動作）\n④【並立相関】Nも＋ば（ければ／なら）＋Nも\n⑤【助言前提】V辞書形＋なら（事前助言・忠告）",
        "explanation": "【教科書規則と本質的機能 (SKM N3 pp. 88-89)】\n1. 仮定条件を超えた4大特殊用法:\n   - 発見 (Discovery): 動作を行った結果、以前から存在していた意外な事実に気づく。主語は前件と後件で異なり、後件は過去形（〜ていた）になる（例: 窓を開けると、外は雪だった）。※「〜ば」はこの用法に使用不可！\n   - 偶発的生起 (Accidental Occurrence): 行為の最中に思いがけない出来事が起きる（例: 散歩をしていると、突然雨が降り出した）。\n   - 即時連続 (Instant Sequence): 同一主語が前件の直後に素早く次の行動を起こす（例: 彼は部屋に入ると、すぐに倒れ込んだ）。\n   - 並立相関 (Correlative Addition): 「も…ば…も」で二つの好条件や悪条件を並立して強調する（例: 料理もおいしければ、値段も安い）。\n2. 助言・忠告の制約:\n   - 相手の意図に対する助言には「〜なら」を用いる（登るなら準備しろ）。「と」や意志動詞の「ば」の後件には助言・命令を置くことはできない。",
        "examples": [
            {
                "japanese": "朝起きて窓を開けると、外は一面の銀世界になっていた。",
                "english": "When I woke up in the morning and opened the window, I discovered that outside had turned into a blanket of snow.",
                "nuance": "V-dict＋と marking sudden discovery of preexisting winter snow outside."
            },
            {
                "japanese": "急いで駅のホームに着いたら、乗るはずだった電車はすでに出発していた。",
                "english": "When I hurried to the station platform, the train I was supposed to take had already departed.",
                "nuance": "V-た＋ら marking discovery that the train had already left."
            },
            {
                "japanese": "公園を散歩していると、突然雷が鳴って激しい雨が降り出した。",
                "english": "While I was strolling through the park, thunder suddenly roared and heavy rain began to pour down.",
                "nuance": "V-ていると marking an unforeseen event occurring midway through action."
            },
            {
                "japanese": "彼は部屋に入ると、何も言わずにソファに倒れ込んだ。",
                "english": "The moment he entered the room, he collapsed onto the couch without saying a single word.",
                "nuance": "V-dict＋と expressing immediate consecutive action by same subject."
            },
            {
                "japanese": "駅前の新しいビストロは、料理もおいしければ値段も手頃で、連日大盛況だ。",
                "english": "The new bistro in front of the station has both delicious food and reasonable prices, drawing huge crowds every day.",
                "nuance": "Aも...ければ Bも... correlative parallel addition highlighting dual merits."
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
print("Enriched Form Review H card in base-reviewed.json!")

# 3. Update source-coverage-matrix.json
matrix = json.load(open(MATRIX_PATH, encoding="utf-8"))

fh_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review H",
        "exactPrintedPages": "pp. 88-89",
        "exactPdfPages": "pp. 111-112",
        "grammarItem": "「ば・たら・なら・と」の特別な使い方 H: 発見・偶発・即時連続・並立",
        "instructionalDetails": "Non-hypothetical operational spectrum of conditional markers: discovery with subject discordance (V-と/たら ...ていた; strict ban on 〜ば), accidental event during ongoing action (V-ていると), immediate consecutive action with subject concordance (V-dict と), correlative parallel addition (も...ば...も), and topical advice with なら.",
        "cardId": "added-n3-h-66",
        "exampleCount": 5,
        "exampleIds": [
            "added-n3-h-66::s-skm3-fh-1",
            "added-n3-h-66::s-skm3-fh-2",
            "added-n3-h-66::s-skm3-fh-3",
            "added-n3-h-66::s-skm3-fh-4",
            "added-n3-h-66::s-skm3-fh-5"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 88-89 (PDF pp. 111-112). Verified textbook taxonomy of conditional forms beyond hypothesis: discovery, accidental occurrence, immediate succession, and parallel listing."
    }
]

existing_card_ids = {e.get("cardId") for e in fh_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(fh_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Form Review H in source coverage matrix! Total certified rows: {len(matrix)}")
