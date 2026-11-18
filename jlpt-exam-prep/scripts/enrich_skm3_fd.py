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
    "初詣": {"reading": "はつもうで", "meaning": "first shrine visit of the New Year"},
    "湧き水": {"reading": "わきみず", "meaning": "spring water / natural wellspring"},
    "澄み切って": {"reading": "すみきって", "meaning": "crystal clear / serene and pure"},
    "望遠鏡": {"reading": "ぼうえんきょう", "meaning": "telescope"},
    "改装工事": {"reading": "かいそうこうじ", "meaning": "renovation work / remodeling"},
    "日差し": {"reading": "ひざし", "meaning": "sunlight / rays of the sun"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Form Review D
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

fd_exercises = [
    {
        "id": "skm3-fd-q1",
        "chapterId": "skm3-fd",
        "question": "外国人観光客にも展示内容がよく（　）ように、多言語の音声ガイドを用意した。",
        "options": [
            "分かる",
            "分かろう",
            "分かった",
            "分ければ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 分かる】\n目的を表す「〜ように」の前には、無意志動詞（可能動詞・自動詞・「分かる」などの状態動詞、または否定形）が来ます。\n\n【選択肢解説】\n1. 分かる (正解): 無意志・状態動詞「分かる」＋ように（目的）。\n2. 分かろう (不正解): 意向形不適合。\n3. 分かった (不正解): 過去形不適合。\n4. 分ければ (不正解): 条件形不適合。"
    },
    {
        "id": "skm3-fd-q2",
        "chapterId": "skm3-fd",
        "question": "真冬だというのに、日差しがポカポカしてまるで春が（　）ようだ。",
        "options": [
            "来た",
            "来るの",
            "来て",
            "来れば"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 来た】\n「まるで〜ようだ」は比喩を表し、真冬の暖かさを「まるで春が来たかのようだ」と形容します。普通形過去（来た）が接続します。\n\n【選択肢解説】\n1. 来た (正解): 比喩構文（まるで春が来たようだ）。\n2. 来るの (不正解): 「の」の過剰挿入。\n3. 来て (不正解): て形不適合。\n4. 来れば (不正解): 条件形。"
    },
    {
        "id": "skm3-fd-q3",
        "chapterId": "skm3-fd",
        "question": "健康診断の後、担当の医師から「毎日30分は散歩を（　）」ようにと厳しく指導された。",
        "options": [
            "する",
            "しろ",
            "しよう",
            "した"
        ],
        "correctIndex": 0,
        "explanation": "【正解: する】\n「動詞辞書形／ない形＋ように（言う・頼む・指導する）」は、他者に指示や命令・要求を伝える間接指示構文です。\n\n【選択肢解説】\n1. する (正解): 辞書形＋ようにと指導された（間接指示）。\n2. しろ (不正解): 命令形とし「ように」を重ねるのは不自然。\n3. しよう (不正解): 意向形不適合。\n4. した (不正解): 過去形不適合。"
    },
    {
        "id": "skm3-fd-q4",
        "chapterId": "skm3-fd",
        "question": "初詣の神社で、家族全員が今年一年健康で無事に（　）ようにと手を合わせた。",
        "options": [
            "過ごせます",
            "過ごす",
            "過ごそう",
            "過ごした"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 過ごせます】\n神仏への祈願や祝福の表現では、「〜ますように」の形で丁寧な祈りを表します（無事に過ごせますように）。\n\n【選択肢解説】\n1. 過ごせます (正解): 可能動詞ます形＋ように（祈願の定番形式）。\n2. 過ごす (不正解): 祈願の語調として弱く不自然。\n3. 過ごそう (不正解): 意向形不適合。\n4. 過ごした (不正解): 過去形不適合。"
    },
    {
        "id": "skm3-fd-q5",
        "chapterId": "skm3-fd",
        "question": "後で大事な連絡事項を（　）ように、手帳にしっかりメモを取っておいた。",
        "options": [
            "忘れない",
            "忘れる",
            "忘れよう",
            "忘れた"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 忘れない】\n「動詞ない形＋ように」は、好ましくない結果を回避するための目的節を作ります（忘れないようにメモを取る）。\n\n【選択肢解説】\n1. 忘れない (正解): 「忘れないように（回避目的）」。\n2. 忘れる (不正解): 忘れるためにメモを取ることになり矛盾。\n3. 忘れよう (不正解): 意向形不適合。\n4. 忘れた (不正解): 過去形不適合。"
    },
    {
        "id": "skm3-fd-q6",
        "chapterId": "skm3-fd",
        "question": "皆様も（　）ように、来月からオフィスの改装工事が始まります。",
        "options": [
            "ご存知の",
            "ご存知な",
            "ご存知に",
            "ご存知で"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ご存知の】\n「ご存知のように」は「相手もすでに知っている既知の情報」を前提として切り出す定番の挨拶・前置き表現です（名詞＋のように）。\n\n【選択肢解説】\n1. ご存知の (正解): 「ご存知のように（すでにご承知の通り）」。\n2. ご存知な (不正解): 助詞接続誤り。\n3. ご存知に (不正解): 助詞接続誤り。\n4. ご存知で (不正解): 助詞接続誤り。"
    },
    {
        "id": "skm3-fd-q7",
        "chapterId": "skm3-fd",
        "question": "山の湧き水は、まるで（　）のように冷たくて澄み切っていた。",
        "options": [
            "氷",
            "冷凍庫",
            "冬",
            "雪だるま"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 氷】\n「氷のように冷たい」は冷たさを極度に強調する日本語の最も自然な比喩表現です。\n\n【選択肢解説】\n1. 氷 (正解): 「氷のように冷たい（比喩）」。\n2. 冷凍庫 (不正解): 比喩として不自然。\n3. 冬 (不正解): 比喩として焦点がぼやける。\n4. 雪だるま (不正解): 不自然。"
    },
    {
        "id": "skm3-fd-q8",
        "chapterId": "skm3-fd",
        "question": "遠くの景色がはっきりと（　）ように、望遠鏡のピントを丁寧に合わせた。",
        "options": [
            "見える",
            "見る",
            "見よう",
            "見た"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 見える】\n目的の「ように」の前には無意志の可能動詞（見える）を用います。意志動詞「見る」を使う場合は「見るために」となります。\n\n【選択肢解説】\n1. 見える (正解): 無意志可能動詞「見える」＋ように（目的）。\n2. 見る (不正解): 意志動詞であり、「見るようにピントを合わせる」は文法的に誤り（正しくは「見るために」）。\n3. 見よう (不正解): 意向形不可。\n4. 見た (不正解): 過去形不可。"
    },
    {
        "id": "skm3-fd-q9",
        "chapterId": "skm3-fd",
        "question": "先生は生徒たちに、宿題を明日の朝一番に（　）ように指示した。",
        "options": [
            "提出する",
            "提出しろ",
            "提出しよう",
            "提出した"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 提出する】\n間接指示の構文「動詞辞書形＋ように指示する」です。\n\n【選択肢解説】\n1. 提出する (正解): 動詞辞書形＋ように指示した（間接指示）。\n2. 提出しろ (不正解): 命令形との重複不可。\n3. 提出しよう (不正解): 意向形不可。\n4. 提出した (不正解): 過去形不可。"
    },
    {
        "id": "skm3-fd-q10",
        "chapterId": "skm3-fd",
        "question": "毎日シャドーイングの練習を続けたおかげで、自然なスピードの日本語が（　）ようになった。",
        "options": [
            "聞き取れる",
            "聞き取る",
            "聞き取ろう",
            "聞き取れ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 聞き取れる】\n能力の変化（〜できるようになる）を表す場合、動詞可能形＋ようになる（聞き取れるようになった）を用います。\n\n【選択肢解説】\n1. 聞き取れる (正解): 可能動詞「聞き取れる」＋ようになった（能力獲得の変化）。\n2. 聞き取る (不正解): 意志動詞では習慣変化になり能力向上を表せない。\n3. 聞き取ろう (不正解): 意向形不可。\n4. 聞き取れ (不正解): 命令形。"
    },
    {
        "id": "skm3-fd-q11",
        "chapterId": "skm3-fd",
        "question": "風邪を（　）ように、帰宅後はすぐに手洗いとうがいを徹底している。",
        "options": [
            "ひかない",
            "ひく",
            "ひこう",
            "ひいた"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ひかない】\n「風邪をひかないように」は、予防・回避の目的を表す定番の表現です。\n\n【選択肢解説】\n1. ひかない (正解): 「風邪をひかないように（予防目的）」。\n2. ひく (不正解): 意味が逆。\n3. ひこう (不正解): 意向形不可。\n4. ひいた (不正解): 過去形不可。"
    },
    {
        "id": "skm3-fd-q12",
        "chapterId": "skm3-fd",
        "question": "彼は歩き方や話し方が、本当にお父さん（　）そっくりだ。",
        "options": [
            "のように",
            "にとって",
            "として",
            "に対して"
        ],
        "correctIndex": 0,
        "explanation": "【正解: のように】\n「名詞＋のように＋そっくりだ」で、類似性・比況（まるで父親のように似ている）を表します。\n\n【選択肢解説】\n1. のように (正解): 比況・類似（お父さんのようにそっくりだ）。\n2. にとって (不正解): 評価の視点。\n3. として (不正解): 資格・役割。\n4. に対して (不正解): 対象。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-fd"]
exercises_data.extend(fd_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(fd_exercises)} exercises for SKM N3 Form Review D!")

# 3. Enrich base-reviewed.json for Form Review D cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-u7-you-ni-purpose": {
        "title": "〜ように (Purpose Clause: Non-Volitional Objective)",
        "connection": "動詞無意志形（可能動詞、自動詞、「分かる」等）/ 動詞ない形 + ように",
        "nuance": "【Shin Kanzen Master N3 pp. 70-71 正式規則】後ろの行為を行う目的を表す（〜という状態が実現するように）。\n【重要文法規則】前に来る動詞は話者の直接的な意志でコントロールできない「無意志動詞（聞こえる、見える、分かる、合格できる）」または「動詞ない形（忘れないように、遅れないように）」に限定される。意志的動作動詞（買う、行く、読む）が来る場合は「〜ために」を用いる。",
        "keyTakeaway": "Expresses non-volitional purpose ('so that X becomes possible / so that X does not happen'). Requires potential/intransitive/negative verbs before ように. Contrast with volitional 〜ために.",
        "sentences": [
            {
                "id": "skm3-u7-you-ni-purpose::s-skm3-fd-1",
                "japanese": "後ろの席の人にもよく聞こえるように、マイクの音量を上げてください。",
                "english": "Please turn up the microphone volume so that people in the back seats can hear well too.",
                "literal": "Back-of seats people-to-also well can-hear so-that, mic volume please-raise.",
                "tokens": [{"word": "聞こえるように", "meaning": "so that it can be heard", "reading": "きこえるように", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 71 verbatim sentence: non-volitional verb 聞こえる expressing auditory objective."
            },
            {
                "id": "skm3-u7-you-ni-purpose::s-skm3-fd-2",
                "japanese": "忘れないように、手帳にしっかりメモを取っておいた。",
                "english": "I took careful notes in my planner so as not to forget.",
                "literal": "Forget-not so-that, notebook-in carefully notes took.",
                "tokens": [{"word": "忘れないように", "meaning": "so as not to forget", "reading": "わすれないように", "pos": "Grammar"}],
                "nuanceNote": "V-ない + ように for negative avoidance purpose."
            },
            {
                "id": "skm3-u7-you-ni-purpose::s-skm3-fd-3",
                "japanese": "日本語の新聞が読めるように、毎日漢字を一生懸命勉強している。",
                "english": "I study kanji diligently every day so that I can read Japanese newspapers.",
                "literal": "Japanese newspapers can-read so-that, every-day kanji diligently studying.",
                "tokens": [{"word": "読めるように", "meaning": "so that I can read", "reading": "よめるように", "pos": "Grammar"}],
                "nuanceNote": "Potential verb 読める indicating acquired language objective."
            },
            {
                "id": "skm3-u7-you-ni-purpose::s-skm3-fd-4",
                "japanese": "電車に遅れないように、早く家を出ました。",
                "english": "I left home early so that I would not be late for the train.",
                "literal": "Train-to late-not so-that, early house left.",
                "tokens": [{"word": "遅れないように", "meaning": "so as not to be late", "reading": "おくれたないように", "pos": "Grammar"}],
                "nuanceNote": "Punctual transit avoidance objective."
            }
        ]
    },
    "added-n3-d-62": {
        "title": "「よう」の整理 D: ようだ・ように (Metaphor, Premise, Indirect Directive & Prayer)",
        "connection": "名詞 + のようだ / のように | 普通形 + ようだ / ように | 動詞辞書形 / ない形 + ように（言う・指示する） | 動詞ます形 + ように（祈願）",
        "nuance": "【Shin Kanzen Master N3 pp. 70-71 正式規則】文法形式の整理 D：「よう」のつく文法形式の多面的一括整理。\n1.「比喩・比況・例示」: ①比喩（春が来たようだ / 氷のように冷たい）；②比況（人間の骨のように、鉄筋が必要だ / 想像したように）；③例示（日本のように四季がある国）。\n2.「既知情報の前置き」: ご存知のように、前にお話ししたように。\n3.「祈願・願望」: 試験に合格しますように、早く元気になりますように。\n4.「要求・間接命令」: 携帯電話を使わないように / 明日早く来るように言われた。",
        "keyTakeaway": "Systematizes the 4 distinct functional domains of よう: (1) Metaphor and simile (〜のようだ/ように); (2) Shared premise intro (ご存知のように); (3) Indirect command/directive (〜ように言う); (4) Earnest prayer/blessing (〜ますように).",
        "sentences": [
            {
                "id": "added-n3-d-62::s-skm3-fd-1",
                "japanese": "真冬だというのに、日差しがポカポカしてまるで春が来たようだ。",
                "english": "Even though it is the dead of winter, the sunlight is pleasantly warm, making it feel just as if spring has arrived.",
                "literal": "Midwinter although, sunlight warm truly spring arrived like-is.",
                "tokens": [{"word": "春が来たようだ", "meaning": "as if spring has arrived", "reading": "はるがきたようだ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 70 verbatim sentence 1: まるで〜ようだ simile."
            },
            {
                "id": "added-n3-d-62::s-skm3-fd-2",
                "japanese": "皆様もご存知のように、来月からオフィスの改装工事が始まります。",
                "english": "As you are all well aware, office renovation work will commence next month.",
                "literal": "Everyone also knowing like-is, next-month-from office renovation starts.",
                "tokens": [{"word": "ご存知のように", "meaning": "as you all know", "reading": "ごぞんじのように", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 71 verbatim sentence 1: introductory premise of shared knowledge."
            },
            {
                "id": "added-n3-d-62::s-skm3-fd-3",
                "japanese": "先生から、宿題は明日の朝一番に提出するようにと言われた。",
                "english": "I was instructed by the teacher to submit the homework first thing tomorrow morning.",
                "literal": "Teacher-from, homework tomorrow's morning-first submit so-that told-was.",
                "tokens": [{"word": "提出するように", "meaning": "to submit it", "reading": "ていしゅつするように", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 71 verbatim sentence 3: indirect command with 〜ように言う."
            },
            {
                "id": "added-n3-d-62::s-skm3-fd-4",
                "japanese": "今年一年、家族全員が健康で無事に過ごせますように。",
                "english": "May our entire family spend this year in good health and safety.",
                "literal": "This-year one-year, family all healthy safely spend may-it-be.",
                "tokens": [{"word": "過ごせますように", "meaning": "may we spend it", "reading": "すごせますように", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 71 verbatim sentence 1 (Section 3): sacred prayer formula 〜ますように."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Form Review D cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

fd_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review D",
        "exactPrintedPages": "p. 71",
        "exactPdfPages": "p. 94",
        "grammarItem": "〜ように (Purpose Clause: Non-Volitional Objective)",
        "instructionalDetails": "Non-volitional verb (potential, intransitive, state verb) / V-ない + ように; expresses purpose towards which action is directed; strict contrast with volitional 〜ために.",
        "cardId": "skm3-u7-you-ni-purpose",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u7-you-ni-purpose::s-skm3-fd-1",
            "skm3-u7-you-ni-purpose::s-skm3-fd-2",
            "skm3-u7-you-ni-purpose::s-skm3-fd-3",
            "skm3-u7-you-ni-purpose::s-skm3-fd-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 71 (PDF p. 94). Verified non-volitional verb constraint before purpose ように and authentic listening/note-taking examples."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review D",
        "exactPrintedPages": "pp. 70-71",
        "exactPdfPages": "pp. 93-94",
        "grammarItem": "「よう」の整理 D: ようだ・ように (Metaphor, Premise, Indirect Directive & Prayer)",
        "instructionalDetails": "Fourfold operational spectrum of よう: (1) Metaphor and comparison (〜のようだ/ように); (2) Shared knowledge premise (ご存知のように); (3) Indirect imperative/command (〜ように言う); (4) Earnest prayer/wishing formula (〜ますように).",
        "cardId": "added-n3-d-62",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-d-62::s-skm3-fd-1",
            "added-n3-d-62::s-skm3-fd-2",
            "added-n3-d-62::s-skm3-fd-3",
            "added-n3-d-62::s-skm3-fd-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 70-71 (PDF pp. 93-94). Verified 4 operational domains of grammatical forms using よう."
    }
]

existing_card_ids = {e.get("cardId") for e in fd_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(fd_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Form Review D in source coverage matrix! Total certified rows: {len(matrix)}")
