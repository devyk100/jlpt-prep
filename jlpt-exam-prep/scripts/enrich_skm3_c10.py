import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
BASE_REVIEWED_PATH = ROOT / "content/base-reviewed.json"
CHAPTER_EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"
OVERRIDES_PATH = ROOT / "content/reading-overrides.json"

# 1. Update Reading Overrides
overrides = json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
needed_overrides = {
    "気象庁": {"reading": "きしょうちょう", "meaning": "Japan Meteorological Agency"},
    "未明": {"reading": "みめい", "meaning": "early dawn / before daybreak"},
    "看板": {"reading": "かんばん", "meaning": "signboard / billboard"},
    "目先": {"reading": "めさき", "meaning": "near future / immediate short-term"},
    "購入率": {"reading": "こうにゅうりつ", "meaning": "purchase rate"},
    "急上昇": {"reading": "きゅうじょうしょう", "meaning": "rapid surge / sharp rise"},
    "指示文書": {"reading": "しじぶんしょ", "meaning": "written instructions / directives"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Chapter 10
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

c10_exercises = [
    {
        "id": "skm3-c10-q1",
        "chapterId": "skm3-c10",
        "question": "借りた本は、汚したり破いたりせず大切に扱う（　）。",
        "options": [
            "べきだ",
            "べきではない",
            "たらどうか",
            "によると"
        ],
        "correctIndex": 0,
        "explanation": "【正解: べきだ】\n「動詞辞書形＋べきだ」は、法律や規則ではなく話者の道徳観・倫理観に基づく「そうするのが人間として当然だ」という強い義務・当為を表します。\n\n【選択肢解説】\n1. べきだ (正解): 「大切に扱うのが当然だ」という道徳的義務。\n2. べきではない (不正解): 否定の当為になり意味が矛盾。\n3. たらどうか (不正解): 軽い提案に留まり、普遍的な道徳の提示として弱い。\n4. によると (不正解): 情報源の提示。"
    },
    {
        "id": "skm3-c10-q2",
        "chapterId": "skm3-c10",
        "question": "（試験監督の指示文書）「名前と受験番号をHBの鉛筆で記入（　）。」",
        "options": [
            "すること",
            "しろ",
            "すべきだ",
            "したらどうか"
        ],
        "correctIndex": 0,
        "explanation": "【正解: すること】\n「動詞辞書形＋こと」は、規則・申込書・試験問題・注意書きなどの書面において受験者・利用者に命令・指示を与える標準的な書面指示表現です。\n\n【選択肢解説】\n1. すること (正解): 書面における指示・規則の伝達。\n2. しろ (不正解): 乱暴な男性口頭命令形であり公的試験文書に不適切。\n3. すべきだ (不正解): 道徳的当為。\n4. したらどうか (不正解): 任意の助言になり試験指示として不適切。"
    },
    {
        "id": "skm3-c10-q3",
        "chapterId": "skm3-c10",
        "question": "（サッカーの試合中）監督がベンチから「前へボールを（　）！」と大声で叫んだ。",
        "options": [
            "出せ",
            "出すな",
            "出すこと",
            "出すべきだ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 出せ】\nスポーツの試合中や緊急時において、指導者や選手が直接発する強い命令には「動詞命令形（出せ）」が用いられます。\n\n【選択肢解説】\n1. 出せ (正解): 動詞I型（五段）の命令形（出す→出せ）。\n2. 出すな (不正解): 禁止（出すな）になり攻撃の指示と逆。\n3. 出すこと (不正解): 静的な書面指示表現。\n4. 出すべきだ (不正解): 熟考する道徳的表現で緊迫した試合中に不自然。"
    },
    {
        "id": "skm3-c10-q4",
        "chapterId": "skm3-c10",
        "question": "彼と喧嘩したままなのは辛いでしょ？一度自分から素直に謝って（　）？",
        "options": [
            "みたらどう",
            "みるな",
            "みるべきだ",
            "みること"
        ],
        "correctIndex": 0,
        "explanation": "【正解: みたらどう】\n「動詞て形＋みたらどう（ですか）」は、悩んでいる相手に対して「一度〜してみてはどうですか」と優しく背中を押す助言・提案表現です。\n\n【選択肢解説】\n1. みたらどう (正解): 親身な助言・提案（謝ってみたらどう？）。\n2. みるな (不正解): 禁止。\n3. みるべきだ (不正解): 押しつけがましい強い道徳的義務。\n4. みること (不正解): 書面規則。"
    },
    {
        "id": "skm3-c10-q5",
        "chapterId": "skm3-c10",
        "question": "気象庁の発表（　）、大型の台風が明日の未明に九州地方へ上陸する見込みだ。",
        "options": [
            "によると",
            "に反して",
            "に沿って",
            "につれて"
        ],
        "correctIndex": 0,
        "explanation": "【正解: によると】\n「情報源（気象庁の発表）＋によると」は、公式な機関やニュースを根拠として客観的な予測や伝聞情報を伝える定番表現です。\n\n【選択肢解説】\n1. によると (正解): 情報源の引用。\n2. に反して (不正解): 逆らうこと。\n3. に沿って (不正解): 方針や道に沿うこと。\n4. につれて (不正解): 比例的変化。"
    },
    {
        "id": "skm3-c10-q6",
        "chapterId": "skm3-c10",
        "question": "（工事現場のフェンスの看板）「危険！関係者以外、絶対に中へ（　）。」",
        "options": [
            "入るな",
            "入ろ",
            "入ること",
            "入るべきだ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 入るな】\n看板や掲示板で危険区域への立ち入りを厳格に禁じる場合、「動詞辞書形＋な（入るな）」という直接的な禁止表現が使われます。\n\n【選択肢解説】\n1. 入るな (正解): 看板・標識における直接の禁止表現。\n2. 入ろ (不正解): 誤った活用形。\n3. 入ること (不正解): 「入れ」という命令になり危険。\n4. 入るべきだ (不正解): 「入るのが当然だ」になり大事故。"
    },
    {
        "id": "skm3-c10-q7",
        "chapterId": "skm3-c10",
        "question": "あんなに一生懸命手伝ってくれた友人に対して、あんな失礼な態度は取る（　）。",
        "options": [
            "べきではなかった",
            "べきだった",
            "取るな",
            "取ること"
        ],
        "correctIndex": 0,
        "explanation": "【正解: べきではなかった】\n「動詞辞書形＋べきではなかった」は、過去に行ってしまった不適切な行為を振り返り、「あんなことをするべきではなかった」と深く後悔・反省する表現です。\n\n【選択肢解説】\n1. べきではなかった (正解): 過去の不当な行為に対する反省・後悔。\n2. べきだった (不正解): 「失礼な態度を取るのが当然だった」になり意味が破綻。\n3. 取るな (不正解): 現在の禁止。\n4. 取ること (不正解): 書面命令。"
    },
    {
        "id": "skm3-c10-q8",
        "chapterId": "skm3-c10",
        "question": "他人のやり方に文句ばかり言っていないで、そんなに言うなら自分で（　）どうか。",
        "options": [
            "やってみたら",
            "やるべきだ",
            "やるな",
            "やること"
        ],
        "correctIndex": 0,
        "explanation": "【正解: やってみたら】\n「動詞て形＋みたらどうか」は親切な提案だけでなく、不満ばかり口にする相手に対し「そこまで言うなら自分でやってみたらどうか」ととがめる（批判・反駁する）強い語気でも使われます。\n\n【選択肢解説】\n1. やってみたら (正解): 相手をとがめる提案（自分でやってみたらどうか）。\n2. やるべきだ (不正解): 「〜どうか」と接続しない。\n3. やるな (不正解): 禁止。\n4. やること (不正解): 書面規則。"
    },
    {
        "id": "skm3-c10-q9",
        "chapterId": "skm3-c10",
        "question": "企業は目先の利益だけでなく、地球環境の保護にも積極的に投資（　）。",
        "options": [
            "すべきだ",
            "するな",
            "したらどうか",
            "によると"
        ],
        "correctIndex": 0,
        "explanation": "【正解: すべきだ】\n企業の社会的責任や倫理的な責務を主張する文脈では、「する→すべきだ／するべきだ」が最も論理的で格調高い表現です。\n\n【選択肢解説】\n1. すべきだ (正解): 「する」のべきだ形（すべきだ／するべきだ）。\n2. するな (不正解): 投資するなという禁止になり逆。\n3. したらどうか (不正解): 軽い提案に留まり論文・社説の論調として弱い。\n4. によると (不正解): 情報源の引用。"
    },
    {
        "id": "skm3-c10-q10",
        "chapterId": "skm3-c10",
        "question": "子供の頃、母から「夜遅くまでゲームを（　）」と厳しく叱られたものだ。",
        "options": [
            "するな",
            "しろ",
            "すべきだ",
            "したらどうか"
        ],
        "correctIndex": 0,
        "explanation": "【正解: するな】\n親や先生からの強い禁止命令を直接引用文として引用符に入れる場合、「〜するな」が最も生き生きとした表現です。\n\n【選択肢解説】\n1. するな (正解): 禁止の直接引用（ゲームをするな、と叱られた）。\n2. しろ (不正解): 命令（ゲームをしろ）になり叱られた文脈と矛盾。\n3. すべきだ (不正解): 論文調。\n4. したらどうか (不正解): 優しい提案。"
    },
    {
        "id": "skm3-c10-q11",
        "chapterId": "skm3-c10",
        "question": "（寮の規則）「夜10時以降は、他の部屋の迷惑になるような大きな音を（　）。」",
        "options": [
            "出さないこと",
            "出すな",
            "出すべきだ",
            "出したらどうか"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 出さないこと】\n規則や規約などの書面において、禁止事項を公的に通達するには「動詞ない形＋こと（出さないこと）」を用います。\n\n【選択肢解説】\n1. 出さないこと (正解): 書面規約における公的な禁止指示。\n2. 出すな (不正解): 乱暴な口頭命令で規約文書には不向き。\n3. 出すべきだ (不正解): 音を出すべきだになり大迷惑。\n4. 出したらどうか (不正解): 任意の助言。"
    },
    {
        "id": "skm3-c10-q12",
        "chapterId": "skm3-c10",
        "question": "業界の最新調査レポート（　）、若者の間で紙の本の購入率が急上昇しているそうだ。",
        "options": [
            "によれば",
            "にしたがって",
            "に比べて",
            "にしては"
        ],
        "correctIndex": 0,
        "explanation": "【正解: によれば】\n「情報源（調査レポート）＋によれば」は、公的な調査や報告書を引用して「〜そうだ」などの伝聞につなげる正確な表現です。\n\n【選択肢解説】\n1. によれば (正解): 調査レポートを情報源として引用（レポートによれば〜そうだ）。\n2. にしたがって (不正解): 規則に従う、または変化に伴う推移。\n3. に比べて (不正解): 比較。\n4. にしては (不正解): 評価の意外性。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-c10"]
exercises_data.extend(c10_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(c10_exercises)} exercises for SKM N3 Chapter 10!")

# 3. Enrich base-reviewed.json for Chapter 10 cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-u9-beki-da": {
        "title": "〜べきだ / 〜べきではない / 〜べきだった (Moral Duty & Past Regret)",
        "connection": "動辞書形 + べきだ / べきではない / べきだった (する irregular: すべきだ or するべきだ)",
        "nuance": "【Shin Kanzen Master N3 p. 47 正式規則】「〜するのが当然だ／〜したほうがいい。〜してはいけない。」法律や規則ではなく、話者の良識・道徳観・社会的倫理に基づく判断。「〜べきだった」の過去形は、過去に行わなかった（あるいは行ってしまった）事柄に対する後悔や反省（責める気持ち）を表す。",
        "keyTakeaway": "Expresses moral obligation or personal ethical judgment ('ought to / should'). The past form 〜べきだった conveys deep regret or self-reproach for past failure.",
        "sentences": [
            {
                "id": "skm3-u9-beki-da::s-skm3-10-1",
                "japanese": "約束はどんなことがあっても守るべきだ。",
                "english": "One ought to keep one's promises, no matter what happens.",
                "literal": "Promise what happened even-if keep ought-to is.",
                "tokens": [{"word": "守るべきだ", "meaning": "ought to keep", "reading": "まもるべきだ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 47 verbatim sentence 1: universal moral principle."
            },
            {
                "id": "skm3-u9-beki-da::s-skm3-10-2",
                "japanese": "言うべきことは、相手に遠慮せずはっきり言ったほうがいい。",
                "english": "What ought to be said should be stated clearly without holding back.",
                "literal": "Say ought-to things, to-other-party without-hesitation clearly say better.",
                "tokens": [{"word": "言うべきこと", "meaning": "things that ought to be said", "reading": "いうべきこと", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 47 verbatim sentence 2: noun modification with 〜べき."
            },
            {
                "id": "skm3-u9-beki-da::s-skm3-10-3",
                "japanese": "あんなひどいことを言うべきではなかったと、深く反省している。",
                "english": "I deeply regret having said such an awful thing; I truly should not have said it.",
                "literal": "That terrible thing say ought-not-was that, deeply reflecting.",
                "tokens": [{"word": "言うべきではなかった", "meaning": "should not have said", "reading": "いうべきではなかった", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 47 verbatim sentence 3: past regret and self-reproach."
            },
            {
                "id": "skm3-u9-beki-da::s-skm3-10-4",
                "japanese": "子供の教育のために、親はもっと本を読むべきだ。",
                "english": "For the sake of their children's education, parents ought to read more books.",
                "literal": "Children's education for, parents more books read ought-to.",
                "tokens": [{"word": "読むべきだ", "meaning": "ought to read", "reading": "よむべきだ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 47 verbatim sentence 4: parental role responsibility."
            }
        ]
    },
    "skm3-u10-ni-yoru-to": {
        "title": "〜によると / 〜によれば (According to Source of Information)",
        "connection": "情報源名詞 + によると / によれば（文末呼応：〜そうだ、〜ということだ、〜とのことだ、〜らしい）",
        "nuance": "【Shin Kanzen Master N3 pp. 36 & 46 正式規則】情報源（ニュース、天気予報、調査、他者の発言等）を示して伝聞・客観的推量を述べる公的表現。文末には「〜そうだ」「〜ということだ」「〜とのことだ」などの伝聞表現が呼応する。",
        "keyTakeaway": "Cites authoritative source of information ('according to [forecast, report, person]'). Standard in formal journalism and reports.",
        "sentences": [
            {
                "id": "skm3-u10-ni-yoru-to::s-skm3-10-1",
                "japanese": "天気予報によると、明日の夕方から関東地方全域で大雪になるそうだ。",
                "english": "According to the weather forecast, heavy snow will reportedly blanket the entire Kanto region starting tomorrow evening.",
                "literal": "Weather forecast according-to, tomorrow evening-from Kanto entire heavy-snow become reportedly.",
                "tokens": [{"word": "天気予報によると", "meaning": "according to weather forecast", "reading": "てんきよほうによると", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 36 verbatim sentence 4: meteorological citation."
            },
            {
                "id": "skm3-u10-ni-yoru-to::s-skm3-10-2",
                "japanese": "気象庁の発表によると、大型の台風が明日の未明に九州地方へ上陸する見込みだ。",
                "english": "According to the announcement from the Meteorological Agency, a large typhoon is expected to make landfall in Kyushu at dawn tomorrow.",
                "literal": "Meteorological Agency announcement according-to, large typhoon tomorrow dawn Kyushu land expected.",
                "tokens": [{"word": "発表によると", "meaning": "according to announcement", "reading": "はっぴょうによると", "pos": "Grammar"}],
                "nuanceNote": "Official governmental bulletin citation."
            },
            {
                "id": "skm3-u10-ni-yoru-to::s-skm3-10-3",
                "japanese": "業界の最新調査レポートによれば、若者の間で紙の本の購入率が急上昇しているそうだ。",
                "english": "According to the industry's latest survey report, the purchase rate of paper books is reportedly surging among young people.",
                "literal": "Industry latest report according-to, youth paper book purchase-rate surging reportedly.",
                "tokens": [{"word": "レポートによれば", "meaning": "according to report", "reading": "れぽーとによれば", "pos": "Grammar"}],
                "nuanceNote": "Statistical research citation with 〜によれば."
            },
            {
                "id": "skm3-u10-ni-yoru-to::s-skm3-10-4",
                "japanese": "田中さんの話によれば、部長は来月転勤するらしい。",
                "english": "According to what Tanaka said, the department manager will apparently transfer next month.",
                "literal": "Tanaka talk according-to, manager next-month transfer apparently.",
                "tokens": [{"word": "話によれば", "meaning": "according to what was said", "reading": "はなしによれば", "pos": "Grammar"}],
                "nuanceNote": "Eyewitness account citation paired with 〜らしい."
            }
        ]
    },
    "added-n3-10-56": {
        "title": "命令・禁止・〜こと (Imperatives, Prohibitions & Written Directives)",
        "connection": "動詞命令形（書け、見ろ、しろ、来い） | 動辞書形 + な（禁止） | 動辞書形 / ない形 + こと（書面指示）",
        "nuance": "【Shin Kanzen Master N3 p. 46 正式規則】\n1.「命令形・禁止（〜な）」: 男性が多く使う強い直接命令・禁止。スポーツの掛け声（走れ！）、道路標識（止まれ、入るな）、間接引用（〜しろ／〜なと言われた）で使用。\n2.「〜こと・〜ないこと」: 主に学校・職場・試験・申込書・注意書き等の書面において指示・規則を伝達する標準文末。",
        "keyTakeaway": "Threefold imperative structure: (1) Strong spoken imperative; (2) Direct prohibition (V-dict + な); (3) Standard formal written instructions on notices and exams (V-dict/ない + こと).",
        "sentences": [
            {
                "id": "added-n3-10-56::s-skm3-10-1",
                "japanese": "監督がベンチから「走れ、走れ！」と大声で叫んだ。",
                "english": "The coach shouted loudly from the bench: 'Run! Run!'",
                "literal": "Coach bench from 'Run, run!' loud-voice-with shouted.",
                "tokens": [{"word": "走れ", "meaning": "Run!", "reading": "はしれ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 46 verbatim sentence 1: sports coaching imperative."
            },
            {
                "id": "added-n3-10-56::s-skm3-10-2",
                "japanese": "父は医者から「酒を飲むな」ときつく言われた。",
                "english": "Father was sternly told by his doctor not to drink alcohol.",
                "literal": "Father doctor by 'Alcohol drink-not' strictly told-was.",
                "tokens": [{"word": "飲むな", "meaning": "do not drink!", "reading": "のむな", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 46 verbatim sentence 6: quoted direct prohibition."
            },
            {
                "id": "added-n3-10-56::s-skm3-10-3",
                "japanese": "試験中は携帯電話の電源を必ず切ること。遅刻した場合は入室を認めない。",
                "english": "During the examination, be sure to switch off mobile phones. Anyone arriving late will not be admitted.",
                "literal": "Exam-during phone power definitely turn-off thing. Late-if entry not-admit.",
                "tokens": [{"word": "切ること", "meaning": "must turn off", "reading": "きること", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 46 verbatim sentence 1 (written notice): formal written instruction."
            },
            {
                "id": "added-n3-10-56::s-skm3-10-4",
                "japanese": "申込書を書く前に、以下の注意事項をよく読むこと。",
                "english": "Before filling out the application form, read the following instructions carefully.",
                "literal": "Application write before, following notes well read thing.",
                "tokens": [{"word": "読むこと", "meaning": "must read", "reading": "よむこと", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 46 verbatim sentence 2 (application rubric): formal written directive."
            }
        ]
    },
    "added-n3-10-57": {
        "title": "〜たらどうか (Suggestions, Recommendations & Mild Reproach)",
        "connection": "動たら形 + どうか / どうですか / どう",
        "nuance": "【Shin Kanzen Master N3 p. 47 正式規則】「〜することを勧める。」相手に柔らかく助言・提案する。『〜たらどうですか』の形。相手がなぜそうしないのかと不満を持ち、責める・とがめる気持ちを込めて使うこともある（『文句があるなら自分でやってみたらどうか』）。",
        "keyTakeaway": "Suggests a course of action ('why don't you try X?'). Can also convey mild impatience or reproach toward a complainer.",
        "sentences": [
            {
                "id": "added-n3-10-57::s-skm3-10-1",
                "japanese": "体の調子が心配なら、一度病院で精密検査を受けてみたらどうですか。",
                "english": "If you are concerned about your physical condition, why don't you get a detailed checkup at the hospital?",
                "literal": "Body condition worried if, once hospital detailed-checkup receive-try why-not.",
                "tokens": [{"word": "受けてみたらどうですか", "meaning": "why don't you try getting", "reading": "うけてみたらどうですか", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 47 verbatim sentence 1: caring medical recommendation."
            },
            {
                "id": "added-n3-10-57::s-skm3-10-2",
                "japanese": "他人のやり方に文句ばかり言っていないで、自分でやってみたらどうか。",
                "english": "Instead of constantly complaining about how others do things, why don't you try doing it yourself?",
                "literal": "Others' way complaint only saying without, yourself try-doing why-not.",
                "tokens": [{"word": "やってみたらどうか", "meaning": "why don't you try doing it yourself", "reading": "やってみたらどうか", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 47 verbatim sentence 4: critical reproach and challenge."
            },
            {
                "id": "added-n3-10-57::s-skm3-10-3",
                "japanese": "一人で悩んでいないで、先輩や上司に相談してみたらどう？",
                "english": "Instead of agonizing alone, why don't you consult a senior colleague or your boss?",
                "literal": "Alone worrying without, senior or boss consult-try why-not?",
                "tokens": [{"word": "相談してみたらどう", "meaning": "why not try consulting", "reading": "そうだんしてみたらどう", "pos": "Grammar"}],
                "nuanceNote": "Colloquial friendly advice."
            },
            {
                "id": "added-n3-10-57::s-skm3-10-4",
                "japanese": "そんなに疲れているなら、今日は少し休んだらどうですか。",
                "english": "If you are that exhausted, why don't you rest a little today?",
                "literal": "That-much tired if, today a-little rest-if why-not.",
                "tokens": [{"word": "休んだらどうですか", "meaning": "why don't you rest", "reading": "やすんだらどうですか", "pos": "Grammar"}],
                "nuanceNote": "Gentle restorative counsel."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Chapter 10 cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

c10_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 10",
        "exactPrintedPages": "p. 47",
        "exactPdfPages": "p. 70",
        "grammarItem": "〜べきだ / 〜べきではない / 〜べきだった (Moral Duty & Past Regret)",
        "instructionalDetails": "V-辞書形 + べきだ/べきではない (する→すべきだ/するべきだ); moral/ethical duty based on speaker conscience; past form 〜べきだった expresses deep regret and self-reproach.",
        "cardId": "skm3-u9-beki-da",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u9-beki-da::s-skm3-10-1",
            "skm3-u9-beki-da::s-skm3-10-2",
            "skm3-u9-beki-da::s-skm3-10-3",
            "skm3-u9-beki-da::s-skm3-10-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 47 (PDF p. 70). Verified Section 3 moral obligation semantics, past regret rules, and formation with すべきだ."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 10",
        "exactPrintedPages": "p. 46",
        "exactPdfPages": "p. 69",
        "grammarItem": "〜によると / 〜によれば (According to Source of Information)",
        "instructionalDetails": "Source Noun + によると/によれば; pairs with evidential/hearsay endings (〜そうだ, 〜とのことだ, 〜らしい); formal journalistic and objective citation.",
        "cardId": "skm3-u10-ni-yoru-to",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u10-ni-yoru-to::s-skm3-10-1",
            "skm3-u10-ni-yoru-to::s-skm3-10-2",
            "skm3-u10-ni-yoru-to::s-skm3-10-3",
            "skm3-u10-ni-yoru-to::s-skm3-10-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 36 & p. 46 (PDF p. 59 & p. 69). Verified formal attribution function and pairing with hearsay predicates."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 10",
        "exactPrintedPages": "p. 46",
        "exactPdfPages": "p. 69",
        "grammarItem": "命令・禁止・〜こと (Imperatives, Prohibitions & Written Directives)",
        "instructionalDetails": "V-imperative (書け, 見ろ, しろ, 来い); V-dict + な (prohibition); V-dict/ない + こと (formal written directives on rules and examination papers).",
        "cardId": "added-n3-10-56",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-10-56::s-skm3-10-1",
            "added-n3-10-56::s-skm3-10-2",
            "added-n3-10-56::s-skm3-10-3",
            "added-n3-10-56::s-skm3-10-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 46 (PDF p. 69). Verified Section 1 spoken imperatives/prohibitions and Section 2 written rubric directives with 〜こと."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 10",
        "exactPrintedPages": "p. 47",
        "exactPdfPages": "p. 70",
        "grammarItem": "〜たらどうか (Suggestions, Recommendations & Mild Reproach)",
        "instructionalDetails": "V-たら + どうか / どうですか / どう; gentle advice recommending a course of action; also used critically to challenge a complainer ('why don't you do it yourself?').",
        "cardId": "added-n3-10-57",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-10-57::s-skm3-10-1",
            "added-n3-10-57::s-skm3-10-2",
            "added-n3-10-57::s-skm3-10-3",
            "added-n3-10-57::s-skm3-10-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 47 (PDF p. 70). Verified Section 4 gentle advice and critical reproach usage."
    }
]

existing_card_ids = {e.get("cardId") for e in c10_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(c10_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Chapter 10 in source coverage matrix! Total certified rows: {len(matrix)}")
