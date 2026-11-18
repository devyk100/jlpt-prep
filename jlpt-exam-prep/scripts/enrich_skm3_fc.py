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
    "赤の他人": {"reading": "あかのたにん", "meaning": "complete stranger / total outsider"},
    "口座番号": {"reading": "こうざばんごう", "meaning": "bank account number"},
    "一桁": {"reading": "ひとけた", "meaning": "single digit / one column"},
    "小刻み": {"reading": "こざみ", "meaning": "in small rapid increments / finely trembling"},
    "流れ星": {"reading": "ながれぼし", "meaning": "shooting star / meteor"},
    "電柱": {"reading": "でんちゅう", "meaning": "utility pole / telephone pole"},
    "有機野菜": {"reading": "ゆうきやさい", "meaning": "organic vegetables"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Form Review C
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

fc_exercises = [
    {
        "id": "skm3-fc-q1",
        "chapterId": "skm3-fc",
        "question": "夜空を見上げたら、きれいな流れ星がすーっと流れていく（　）を見た。",
        "options": [
            "の",
            "こと",
            "もの",
            "ところ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: の】\n直接的な知覚動詞（見る、聞こえる、感じる）で知覚される動作・光景を名詞化する場合、「の」のみが使われ、「こと」は使えません。\n\n【選択肢解説】\n1. の (正解): 知覚動詞「見る」の対象となる具体的光景の名詞化。\n2. こと (不正解): 抽象的概念の名詞化であり、直接知覚の「見る」には不適合。\n3. もの (不正解): 具体的物体そのものを指す。\n4. ところ (不正解): 場面・局面。"
    },
    {
        "id": "skm3-fc-q2",
        "chapterId": "skm3-fc",
        "question": "私の長年の夢は、世界中を旅してたくさんの人々と交流する（　）です。",
        "options": [
            "こと",
            "の",
            "もの",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: こと】\n「〜は…ことだ」の文型で、夢・希望・目標・特徴などの「内容」を説明・定義する場合、「こと」のみが使われ、「の」は使えません。\n\n【選択肢解説】\n1. こと (正解): 夢・目標の内容定義構文（夢は〜ことだ）。\n2. の (不正解): 内容定義の文末に「〜のだ」は使えない。\n3. もの (不正解): 具体的物体。\n4. わけ (不正解): 理由。"
    },
    {
        "id": "skm3-fc-q3",
        "chapterId": "skm3-fc",
        "question": "改札口まで全力で走ったおかげで間に合ったが、もう少しで終電に（　）ところだった。",
        "options": [
            "乗り遅れる",
            "乗り遅れた",
            "乗り遅れよう",
            "乗り遅れて"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 乗り遅れる】\n「もう少しで／危うく＋動詞辞書形＋ところだった」は「もう少しで好ましくない事態になりそうだったが、間一髪で回避された」という九死に一生のニアミスを表します。\n\n【選択肢解説】\n1. 乗り遅れる (正解): 動詞辞書形＋ところだった（危機一髪の回避）。\n2. 乗り遅れた (不正解): 過去形接続は「〜たところだ（したばかり）」になり意味が崩壊。\n3. 乗り遅れよう (不正解): 意向形不適合。\n4. 乗り遅れて (不正解): て形不適合。"
    },
    {
        "id": "skm3-fc-q4",
        "chapterId": "skm3-fc",
        "question": "銀行の窓口に並ばずに、24時間スマホで送金できる（　）は本当に便利だ。",
        "options": [
            "の",
            "こと",
            "もの",
            "ところ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: の】\n「〜のは（便利だ・危険だ・大変だ・難しい）」のように、ある行為・事態に対する話者の感情や評価を形容詞で述べる場合、「の」が極めて自然です。\n\n【選択肢解説】\n1. の (正解): 行為・事態の形容詞評価（送金できるのは便利だ）。\n2. こと (不正解): 論文調の抽象的な概念名詞化で日常的な便利さの評価には硬すぎる。\n3. もの (不正解): 具体的物体。\n4. ところ (不正解): 局面。"
    },
    {
        "id": "skm3-fc-q5",
        "chapterId": "skm3-fc",
        "question": "私が日本語の勉強を始めた（　）は、高校１年生の夏休みのことでした。",
        "options": [
            "の",
            "こと",
            "もの",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: の】\n「〜のは…だ」という分裂文（強調構文）において、時間・場所・理由などの情報を強調して提示する場合、「の」のみが使われます。\n\n【選択肢解説】\n1. の (正解): 強調構文（始めたのは高校の夏休みのことだった）。\n2. こと (不正解): 「始めたことは夏休みのことだった」は不自然。\n3. もの (不正解): 具体的物体。\n4. わけ (不正解): 理由。"
    },
    {
        "id": "skm3-fc-q6",
        "chapterId": "skm3-fc",
        "question": "スマホを見ながら歩いていたので、危うく電柱に（　）ところだった。",
        "options": [
            "ぶつかる",
            "ぶつかった",
            "ぶつかろう",
            "ぶつかって"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ぶつかる】\n「危うく＋動詞辞書形＋ところだった」で「危うく電柱にぶつかりそうになった（直前で避けた）」というニアミスを表します。\n\n【選択肢解説】\n1. ぶつかる (正解): 辞書形＋ところだった（衝突寸前で回避）。\n2. ぶつかった (不正解): 過去形は不可。\n3. ぶつかろう (不正解): 意向形不可。\n4. ぶつかって (不正解): て形不可。"
    },
    {
        "id": "skm3-fc-q7",
        "chapterId": "skm3-fc",
        "question": "真夏の暑い午後なので、自販機で何か冷たい（　）を買って飲もう。",
        "options": [
            "もの",
            "こと",
            "の",
            "ところ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: もの】\n具体的で形のある有形物（冷たい飲み物など）を指す場合は「もの」を用います。\n\n【選択肢解説】\n1. もの (正解): 具体的・物理的な飲食物（冷たいもの）。\n2. こと (不正解): 抽象的事柄・事実。\n3. の (不正解): 文脈上「冷たいもの」が標準。\n4. ところ (不正解): 場所・局面。"
    },
    {
        "id": "skm3-fc-q8",
        "chapterId": "skm3-fc",
        "question": "静かな夜、隣の部屋で男女が大声で激しく言い争っている（　）が聞こえた。",
        "options": [
            "の",
            "こと",
            "もの",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: の】\n聴覚の知覚動詞「聞こえる」の主語節には、「の」のみが接続します（言い争っているのが聞こえた）。\n\n【選択肢解説】\n1. の (正解): 知覚動詞「聞こえる」と呼応する「の」。\n2. こと (不正解): 抽象的思考には使えるが直接の聴覚知覚には使えない。\n3. もの (不正解): 具体的物体。\n4. わけ (不正解): 理由。"
    },
    {
        "id": "skm3-fc-q9",
        "chapterId": "skm3-fc",
        "question": "このレストランの最大の特徴は、有機野菜のみを使用している（　）だ。",
        "options": [
            "こと",
            "の",
            "もの",
            "ところ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: こと】\n「特徴は〜ことだ」で、名詞「特徴」の内容を説明する述部には「こと」を用います。\n\n【選択肢解説】\n1. こと (正解): 特徴の内容説明（特徴は〜ことだ）。\n2. の (不正解): 「特徴は〜のだ」は誤り。\n3. もの (不正解): 具体的物体。\n4. ところ (不正解): 局面。"
    },
    {
        "id": "skm3-fc-q10",
        "chapterId": "skm3-fc",
        "question": "振込先の口座番号を一桁押し間違えて、赤の他人に送金する（　）だった。",
        "options": [
            "ところ",
            "わけ",
            "はず",
            "もの"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ところ】\n「動詞辞書形＋ところだった」で、もう少しで重大な過失（誤送金）を犯す寸前だったが直前で気がついて防いだことを表します。\n\n【選択肢解説】\n1. ところ (正解): 「送金するところだった（寸前で回避）」。\n2. わけ (不正解): 理由・当然。\n3. はず (不正解): 予測。\n4. もの (不正解): 物体。"
    },
    {
        "id": "skm3-fc-q11",
        "chapterId": "skm3-fc",
        "question": "外国語を学ぶ上で、ネイティブ並みの自然な発音を身につける（　）は極めて難しい。",
        "options": [
            "の",
            "もの",
            "ところ",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: の】\n「〜のは（難しい・簡単だ・楽しい・重要だ）」のように、動作に対する主観的難易度・評価を述べる主語節には「の」が最も自然です。\n\n【選択肢解説】\n1. の (正解): 難易度評価（身につけるのは極めて難しい）。\n2. もの (不正解): 具体的物体。\n3. ところ (不正解): 局面。\n4. わけ (不正解): 理由。"
    },
    {
        "id": "skm3-fc-q12",
        "chapterId": "skm3-fc",
        "question": "ベッドに入ってウトウトしていたら、家全体が小刻みに揺れる（　）を感じた。",
        "options": [
            "の",
            "こと",
            "もの",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: の】\n皮膚感覚や身体感覚を表す知覚動詞「感じる」の対象には、「の」を用います（揺れるのを感じた）。\n\n【選択肢解説】\n1. の (正解): 知覚動詞「感じる」と呼応する「の」。\n2. こと (不正解): 思考・概念の「感じる」ではなく直接の振動感覚には「の」。\n3. もの (不正解): 具体的物体。\n4. わけ (不正解): 理由。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-fc"]
exercises_data.extend(fc_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(fc_exercises)} exercises for SKM N3 Form Review C!")

# 3. Enrich base-reviewed.json for Form Review C cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-fc-tokoro-datta": {
        "title": "〜ところだった (On the Very Verge Of / Narrowly Averted Near-Miss)",
        "connection": "動詞辞書形 + ところだった（呼応副詞：もう少しで、危うく、一歩間違えれば）",
        "nuance": "【Shin Kanzen Master N3 正式規則】もう少しで重大な事故や好ましくない結果になりそうだったが、間一髪のところで発生せずに済んだことを表す。「もう少しで…ところだった」「危うく…ところだった」の形で呼応し、危機を回避した安堵感や反省を込めて言う。",
        "keyTakeaway": "Expresses that a disastrous or undesirable outcome almost happened, but was narrowly averted in the nick of time ('I almost / was on the very brink of...').",
        "sentences": [
            {
                "id": "skm3-fc-tokoro-datta::s-skm3-fc-1",
                "japanese": "足元が滑って、危うく階段から転がり落ちるところだった。",
                "english": "My footing slipped, and I came within a hair's breadth of tumbling down the stairs.",
                "literal": "Footing slipped, narrowly stairs-from tumble-down verge-was.",
                "tokens": [{"word": "転がり落ちるところだった", "meaning": "was on the verge of tumbling down", "reading": "ころがりおちるところだった", "pos": "Grammar"}],
                "nuanceNote": "Near-miss tumbling accident averted."
            },
            {
                "id": "skm3-fc-tokoro-datta::s-skm3-fc-2",
                "japanese": "改札口まで全力で走ったおかげで、もう少しで終電に乗り遅れるところだったが間に合った。",
                "english": "Thanks to sprinting all the way to the ticket gate, although I almost missed the last train, I managed to catch it.",
                "literal": "Ticket-gate until full-power sprinted thanks-to, a-little-more last-train miss verge-was but caught.",
                "tokens": [{"word": "乗り遅れるところだった", "meaning": "almost missed", "reading": "のりおくれるところだった", "pos": "Grammar"}],
                "nuanceNote": "Narrow train boarding escape."
            },
            {
                "id": "skm3-fc-tokoro-datta::s-skm3-fc-3",
                "japanese": "スマホを見ながら歩いていたので、危うく電柱にぶつかるところだった。",
                "english": "Because I was walking while staring at my smartphone, I almost walked right into a utility pole.",
                "literal": "Smartphone looking walking-was because, narrowly pole bump verge-was.",
                "tokens": [{"word": "ぶつかるところだった", "meaning": "almost collided", "reading": "ぶつかるところだった", "pos": "Grammar"}],
                "nuanceNote": "Inattentive walking near-collision."
            },
            {
                "id": "skm3-fc-tokoro-datta::s-skm3-fc-4",
                "japanese": "振込先の口座番号を一桁押し間違えて、赤の他人に送金するところだった。",
                "english": "I mistyped one digit of the recipient's bank account number and almost wired money to a complete stranger.",
                "literal": "Transfer-destination account-number one-digit mis-typed, stranger transfer verge-was.",
                "tokens": [{"word": "送金するところだった", "meaning": "almost wired money", "reading": "そうきんするところだった", "pos": "Grammar"}],
                "nuanceNote": "Near financial error averted at confirmation."
            }
        ]
    },
    "added-n3-c-61": {
        "title": "名詞化の整理 C: 「こと」と「の」 (Nominalizers: Abstract Content vs Sensory Perception)",
        "connection": "普通形 + こと (抽象的内容・定義・規則) | 普通形 + の (直接知覚・形容詞評価・強調分裂文) | 具体的実体 + もの",
        "nuance": "【Shin Kanzen Master N3 pp. 66-67 正式規則】文法形式の整理 C：「こと」と「の」の使い分け。\n1.「こと」のみ使用:\n  a)「〜は…ことだ」で内容・定義を説明（夢は漫画家になることだ / 特徴は手を使わないことだ）。\n  b) 文法形式: 〜ことがある / 〜ことにする / 〜ことになる / 〜ことはない / 〜こと（規則・指示）。\n2.「の」のみ使用:\n  a) 知覚動詞（見る、聞こえる、感じる）で直接知覚する具体的光景（鳥が飛ぶのを見た / 家が揺れるのを感じた）。\n  b)「〜のは（便利だ・危険だ・大変だ・難しい）」と形容詞で行為・事態を評価する文。\n  c) 強調分裂文（初めて会ったのは５年前だ）。\n3.「もの」: 具体的で形のある有形物（冷たいものが飲みたい）。",
        "keyTakeaway": "Systematic distinction between nominalizers: こと is required for definitions ('my dream is X') and fixed grammar formulas; の is strictly required for direct sensory perceptions (見る/聞こえる/感じる) and evaluative adjectives ('doing X is convenient/difficult').",
        "sentences": [
            {
                "id": "added-n3-c-61::s-skm3-fc-1",
                "japanese": "私の将来の夢は、世界で活躍する漫画家になることだ。",
                "english": "My future dream is to become a manga artist active worldwide.",
                "literal": "My future dream, world-in active manga-artist become thing is.",
                "tokens": [{"word": "なることだ", "meaning": "is to become", "reading": "なることだ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 66 verbatim sentence 1: こと defines the content of a noun (夢は〜ことだ)."
            },
            {
                "id": "added-n3-c-61::s-skm3-fc-2",
                "japanese": "夜空を見上げたら、きれいな流れ星がすーっと流れていくのを見た。",
                "english": "Looking up at the night sky, I saw a beautiful shooting star streak across.",
                "literal": "Night-sky looked-up, beautiful shooting-star streaking-away saw.",
                "tokens": [{"word": "流れていくのを見た", "meaning": "saw it streaking across", "reading": "ながれていくのをみた", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 67 verbatim sentence 1: の strictly required with sensory perception verb 見る."
            },
            {
                "id": "added-n3-c-61::s-skm3-fc-3",
                "japanese": "24時間いつでもスマホで買い物ができるのは、本当に便利だ。",
                "english": "Being able to shop on a smartphone 24 hours a day is truly convenient.",
                "literal": "24-hours anytime smartphone shopping can-do is truly convenient.",
                "tokens": [{"word": "できるのは", "meaning": "being able to do is", "reading": "できるのは", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 67 verbatim sentence 2: の evaluated by adjective 便利だ."
            },
            {
                "id": "added-n3-c-61::s-skm3-fc-4",
                "japanese": "真夏の暑い午後なので、自販機で何か冷たいものを買って飲もう。",
                "english": "Since it is a scorching midsummer afternoon, let's buy something cold from the vending machine to drink.",
                "literal": "Midsummer hot afternoon because, vending-machine something cold thing buy-and drink.",
                "tokens": [{"word": "冷たいもの", "meaning": "something cold", "reading": "つめたいもの", "pos": "Grammar"}],
                "nuanceNote": "もの refers to tangible concrete objects."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Form Review C cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

fc_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review C",
        "exactPrintedPages": "p. 66",
        "exactPdfPages": "p. 89",
        "grammarItem": "〜ところだった (On the Very Verge Of / Narrowly Averted Near-Miss)",
        "instructionalDetails": "V-dict + ところだった; pairs with もう少しで or 危うく; indicates an undesirable near-miss crisis that was averted at the last fraction of a second.",
        "cardId": "skm3-fc-tokoro-datta",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-fc-tokoro-datta::s-skm3-fc-1",
            "skm3-fc-tokoro-datta::s-skm3-fc-2",
            "skm3-fc-tokoro-datta::s-skm3-fc-3",
            "skm3-fc-tokoro-datta::s-skm3-fc-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 66 (PDF p. 89). Verified near-miss semantics, pairing with 危うく/もう少しで, and non-occurrence of the event."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review C",
        "exactPrintedPages": "pp. 66-67",
        "exactPdfPages": "pp. 89-90",
        "grammarItem": "名詞化の整理 C: 「こと」と「の」 (Nominalizers: Abstract Content vs Sensory Perception)",
        "instructionalDetails": "Comparative systematization: こと for noun definition (〜は…ことだ) and grammar formulas; の for direct sensory perception (見る, 聞こえる, 感じる) and adjective evaluations (〜のは便利だ/難しい); もの for tangible physical objects.",
        "cardId": "added-n3-c-61",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-c-61::s-skm3-fc-1",
            "added-n3-c-61::s-skm3-fc-2",
            "added-n3-c-61::s-skm3-fc-3",
            "added-n3-c-61::s-skm3-fc-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 66-67 (PDF pp. 89-90). Verified nominalizer distinction rules across 4 operational domains."
    }
]

existing_card_ids = {e.get("cardId") for e in fc_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(fc_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Form Review C in source coverage matrix! Total certified rows: {len(matrix)}")
