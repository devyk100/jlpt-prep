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
    "暴風雨": {"reading": "ぼうふうう", "meaning": "rainstorm / windstorm"},
    "根元": {"reading": "ねもと", "meaning": "root / base of tree"},
    "未熟者": {"reading": "みじゅくもの", "meaning": "novice / greenhorn / inexperienced person"},
    "口ずさんで": {"reading": "くちずさんで", "meaning": "humming / singing to oneself"},
    "流し": {"reading": "ながし", "meaning": "sink (kitchen)"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Form Review A
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

fa_exercises = [
    {
        "id": "skm3-fa-q1",
        "chapterId": "skm3-fa",
        "question": "次の電車が来るまでまだ30分あるから、駅前のカフェでコーヒー（　）飲んで待とうか。",
        "options": [
            "でも",
            "こそ",
            "さえ",
            "しか"
        ],
        "correctIndex": 0,
        "explanation": "【正解: でも】\n「名詞＋でも」は提案・意志・勧誘の文において、「〜などを例示して控えめに提案する（コーヒーでもどう？）」という用法です。\n\n【選択肢解説】\n1. でも (正解): 提案・勧誘における例示の「でも」。\n2. こそ (不正解): 強い排他・区別の強調（コーヒーこそ飲むべきだ等）。\n3. さえ (不正解): 極端な例の提示。\n4. しか (不正解): 否定文と呼応（しか飲まない）。"
    },
    {
        "id": "skm3-fa-q2",
        "chapterId": "skm3-fa",
        "question": "今年（　）絶対にJLPT N3に合格してみせると、心に強く誓った。",
        "options": [
            "こそ",
            "でも",
            "まで",
            "くらい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: こそ】\n「名詞＋こそ」は「他のどれでもなく、まさにそれ」と区別して強く強調する表現です。「今年こそ合格する」という強い決意の定番表現です。\n\n【選択肢解説】\n1. こそ (正解): 強烈な焦点化・決意の強調（今年こそ）。\n2. でも (不正解): 譲歩・例示。\n3. まで (不正解): 範囲・終点。\n4. くらい (不正解): 程度の概数。"
    },
    {
        "id": "skm3-fa-q3",
        "chapterId": "skm3-fa",
        "question": "この問題はあまりに簡単すぎて、小学生（　）すぐに解ける。",
        "options": [
            "でさえ",
            "こそ",
            "しか",
            "だけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: でさえ】\n「名詞＋（で）さえ」は「極端な事例を挙げて、他のものは当然だ」と暗示する用法です。「小学生でさえ解ける（大人は当然解ける）」という文脈に合致します。\n\n【選択肢解説】\n1. でさえ (正解): 極端な例の提示（小学生でさえ解ける）。\n2. こそ (不正解): 排他的強調。\n3. しか (不正解): 否定呼応。\n4. だけ (不正解): 限定（小学生だけが解けるになり文脈破綻）。"
    },
    {
        "id": "skm3-fa-q4",
        "chapterId": "skm3-fa",
        "question": "激しい暴風雨で、頑丈な大木（　）根元から倒れてしまった。",
        "options": [
            "まで",
            "こそ",
            "だけ",
            "ほど"
        ],
        "correctIndex": 0,
        "explanation": "【正解: まで】\n「名詞＋まで」は「〜という意外なものにまで及ぶ」という範囲の拡大・意外性を強調する用法です。「頑丈な大木まで倒れた」という驚きを表します。\n\n【選択肢解説】\n1. まで (正解): 意外な及ぶ範囲の強調（大木まで倒れた）。\n2. こそ (不正解): 排他。\n3. だけ (不正解): 限定。\n4. ほど (不正解): 程度比較。"
    },
    {
        "id": "skm3-fa-q5",
        "chapterId": "skm3-fa",
        "question": "自分の食べた食器（　）、自分で流しに持って行って洗いなさい。",
        "options": [
            "くらい",
            "こそ",
            "しか",
            "さえ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: くらい】\n「名詞＋くらい／ぐらい」は「最低限これだけは」という軽い程度・最低限の行動水準を提示する用法です。\n\n【選択肢解説】\n1. くらい (正解): 最低限の基準（食器くらい洗いなさい）。\n2. こそ (不正解): 強調。\n3. しか (不正解): 否定呼応。\n4. さえ (不正解): 極端事例。"
    },
    {
        "id": "skm3-fa-q6",
        "chapterId": "skm3-fa",
        "question": "私（　）のような未熟者が、このような栄誉ある賞をいただいて恐縮です。",
        "options": [
            "なんか",
            "こそ",
            "さえ",
            "だけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: なんか】\n「名詞＋なんか」は自分自身を謙遜して低く評価したり、軽く見たりする感情を表す口語助詞です（私なんかのような未熟者）。\n\n【選択肢解説】\n1. なんか (正解): 謙遜・自己卑下（私なんか）。\n2. こそ (不正解): 自分を強調すると自画自賛になる。\n3. さえ (不正解): 極端事例。\n4. だけ (不正解): 限定。"
    },
    {
        "id": "skm3-fa-q7",
        "chapterId": "skm3-fa",
        "question": "あんな根拠のない噂話（　）、気にする必要は全くありませんよ。",
        "options": [
            "なんて",
            "こそ",
            "だけ",
            "まで"
        ],
        "correctIndex": 0,
        "explanation": "【正解: なんて】\n「名詞＋なんて」は「あんな価値のないもの」と対象を軽視・無視・低評価する感情を込めて提示する助詞です。\n\n【選択肢解説】\n1. なんて (正解): 軽視・不要の評価（噂話なんて気にするな）。\n2. こそ (不正解): 噂話こそ気にするべきだになり逆。\n3. だけ (不正解): 限定。\n4. まで (不正解): 範囲。"
    },
    {
        "id": "skm3-fa-q8",
        "chapterId": "skm3-fa",
        "question": "いつも助けてもらって感謝しています。こちら（　）お礼を言わなければなりません。",
        "options": [
            "こそ",
            "でも",
            "さえ",
            "まで"
        ],
        "correctIndex": 0,
        "explanation": "【正解: こそ】\n「こちらこそ」は相手からの感謝や挨拶に対し、「いいえ、まさにこちらのほうこそ」と排他的に強調して返す定番の敬語慣用句です。\n\n【選択肢解説】\n1. こそ (正解): 「こちらこそ」の決まり文句。\n2. でも (不正解): 提案・例示。\n3. さえ (不正解): 極端事例。\n4. まで (不正解): 範囲。"
    },
    {
        "id": "skm3-fa-q9",
        "chapterId": "skm3-fa",
        "question": "毎日同じオフィスで働いているのに、隣の人の名前（　）知らない。",
        "options": [
            "さえ",
            "こそ",
            "ほど",
            "だけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: さえ】\n「〜さえ知らない」は「最も基本的で知っていて当然の極端な事例すら知らない」という著しい不足を表します。\n\n【選択肢解説】\n1. さえ (正解): 極端な基本事例の提示（名前さえ知らない）。\n2. こそ (不正解): 肯定の強調。\n3. ほど (不正解): 程度。\n4. だけ (不正解): 限定。"
    },
    {
        "id": "skm3-fa-q10",
        "chapterId": "skm3-fa",
        "question": "挨拶（　）は、どんなに機嫌が悪くてもきちんとするべきだ。",
        "options": [
            "ぐらい",
            "こそ",
            "しか",
            "まで"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ぐらい】\n「挨拶ぐらいは」で「最低限マナーとしての挨拶くらいは行うべきだ」という最低限度の行為レベルを提示します。\n\n【選択肢解説】\n1. ぐらい (正解): 最低限の基準（挨拶ぐらいは）。\n2. こそ (不正解): 排他強調。\n3. しか (不正解): 否定呼応が必要。\n4. まで (不正解): 範囲。"
    },
    {
        "id": "skm3-fa-q11",
        "chapterId": "skm3-fa",
        "question": "食後に、もしよろしければ季節のフルーツ（　）召し上がりませんか。",
        "options": [
            "でも",
            "こそ",
            "さえ",
            "しか"
        ],
        "correctIndex": 0,
        "explanation": "【正解: でも】\n「名詞＋でも」は、相手に負担を感じさせないように「〜などをいかがですか」と柔らかく例示して勧める表現です。\n\n【選択肢解説】\n1. でも (正解): 柔らかい勧誘・例示（フルーツでも召し上がりませんか）。\n2. こそ (不正解): 強調。\n3. さえ (不正解): 極端事例。\n4. しか (不正解): 否定呼応。"
    },
    {
        "id": "skm3-fa-q12",
        "chapterId": "skm3-fa",
        "question": "その大ヒット曲は若者だけでなく、80歳のおじいちゃん（　）口ずさんでいる。",
        "options": [
            "まで",
            "こそ",
            "だけ",
            "しか"
        ],
        "correctIndex": 0,
        "explanation": "【正解: まで】\n「名詞＋まで」は通常想定されないような意外な層・人物にまで人気が及んでいることを表す用法です。\n\n【選択肢解説】\n1. まで (正解): 意外な及ぶ範囲（おじいちゃんまで歌っている）。\n2. こそ (不正解): 排他強調。\n3. だけ (不正解): 若者だけでなく〜だけ、は矛盾。\n4. しか (不正解): 否定呼応が必要。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-fa"]
exercises_data.extend(fa_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(fa_exercises)} exercises for SKM N3 Form Review A!")

# 3. Enrich base-reviewed.json for Form Review A
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "added-n3-a-59": {
        "title": "助詞の整理 A: こそ・さえ・でも・くらい・まで・など (Nuanced Particle Systematization)",
        "connection": "名詞 + こそ / さえ / でも / くらい(ぐらい) / まで / など(なんか・なんて)",
        "nuance": "【Shin Kanzen Master N3 pp. 58-59 正式規則】文法形式の整理 A：意味の広がりを持つ助詞の体系的整理。\n1.「〜こそ」: 区別の強調（今度こそ優勝する / これこそ探していた本だ）。\n2.「〜さえ」: 極端な例を出して、当然のことを暗示する（子供さえ知っている / 妹にさえ馬鹿にされた）。\n3.「〜でも」: ①提案・意志・依頼の例示（お茶でも飲みませんか）；②範囲の広さ・意外性の強調（子供でも分かる）。\n4.「〜くらい / ぐらい」: ①軽い程度・最低限の提示（これくらいのこと / お酒くらい飲める）；②同程度の例示（娘くらい背が伸びた）；③提案の文で控えめに案を示す（お菓子くらい食べたらどうですか）。\n5.「〜まで」: 意外な事態にまで及ぶ範囲の拡大（大木まで倒れた / おじいちゃんまで歌っている）。\n6.「〜など / なんか / なんて」: 例示・謙遜・軽視（私なんか / 噂話なんて）。",
        "keyTakeaway": "Systematizes nuanced JLPT N3 particles: こそ (resolute focus), さえ (extreme baseline), でも (soft proposal / broad extent), くらい (minimum baseline / approximation), まで (surprising scope extension), and など/なんか/なんて (disdain/modesty).",
        "sentences": [
            {
                "id": "added-n3-a-59::s-skm3-fa-1",
                "japanese": "今度こそ優勝したいと、選手全員が毎日猛練習を重ねている。",
                "english": "Every single athlete is intensely practicing day after day, determined that this time above all they will win the championship.",
                "literal": "This-time indeed championship-win want-to that, athletes all every-day practice doing.",
                "tokens": [{"word": "今度こそ", "meaning": "this time above all", "reading": "こんどこそ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 58 verbatim sentence 1: こそ for resolute differentiation."
            },
            {
                "id": "added-n3-a-59::s-skm3-fa-2",
                "japanese": "お茶でも飲みながら、次の旅行の計画を立てませんか。",
                "english": "Why don't we plan our next trip over tea or something?",
                "literal": "Tea or-something drinking while, next trip's plan make question?",
                "tokens": [{"word": "お茶でも", "meaning": "tea or something", "reading": "おちゃでも", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 58 verbatim sentence 3: でも for non-binding friendly suggestion."
            },
            {
                "id": "added-n3-a-59::s-skm3-fa-3",
                "japanese": "激しい暴風雨で、頑丈な大木まで根元から倒れてしまった。",
                "english": "In the violent storm, even the sturdy giant tree was uprooted from its base.",
                "literal": "Violent storm by, sturdy giant-tree even root-from fell.",
                "tokens": [{"word": "大木まで", "meaning": "even the giant tree", "reading": "たいぼくまで", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 59 verbatim sentence 1: まで for unexpected scope extension."
            },
            {
                "id": "added-n3-a-59::s-skm3-fa-4",
                "japanese": "自分の食べた食器くらい、自分で片付けなさい。",
                "english": "At the very least, put away the dishes you ate from yourself.",
                "literal": "Self's eaten dishes at-least, self-by clear-up.",
                "tokens": [{"word": "食器くらい", "meaning": "at least the dishes", "reading": "しょっきくらい", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 59 verbatim sentence 2: くらい for minimum baseline requirement."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched SKM N3 Form Review A card in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

fa_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review A",
        "exactPrintedPages": "pp. 58-59",
        "exactPdfPages": "pp. 81-82",
        "grammarItem": "助詞の整理 A: こそ・さえ・でも・くらい・まで・など (Nuanced Particle Systematization)",
        "instructionalDetails": "Comprehensive particle systematization: こそ (resolute focus), さえ (extreme minimum), でも (proposal/broad scope), くらい (minimum baseline/approximation), まで (unexpected inclusion), など/なんか/なんて (disdain/modesty).",
        "cardId": "added-n3-a-59",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-a-59::s-skm3-fa-1",
            "added-n3-a-59::s-skm3-fa-2",
            "added-n3-a-59::s-skm3-fa-3",
            "added-n3-a-59::s-skm3-fa-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 58-59 (PDF pp. 81-82). Verified comparative particle taxonomy, multiple functional senses, and authentic exercise patterns."
    }
]

existing_card_ids = {e.get("cardId") for e in fa_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(fa_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Form Review A in source coverage matrix! Total certified rows: {len(matrix)}")
