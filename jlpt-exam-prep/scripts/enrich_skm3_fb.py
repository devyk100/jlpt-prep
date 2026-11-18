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
    "招聘": {"reading": "しょうへい", "meaning": "invitation / summoning a guest"},
    "文豪": {"reading": "ぶんごう", "meaning": "literary giant / master writer"},
    "雑煮": {"reading": "ぞうに", "meaning": "zoni / new year soup with mochi"},
    "内向的": {"reading": "ないこうてき", "meaning": "introverted / quiet"},
    "消費動向": {"reading": "しょうひどうこう", "meaning": "consumer spending trends"},
    "鉄道網": {"reading": "てつどうもう", "meaning": "railway network"},
    "麻痺": {"reading": "まひ", "meaning": "paralysis / gridlock"},
    "仕立て": {"reading": "じたて", "meaning": "prepared with / tailored / flavored with"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Form Review B
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

fb_exercises = [
    {
        "id": "skm3-fb-q1",
        "chapterId": "skm3-fb",
        "question": "日本語学習者（　）、漢字の習得は避けて通れない最大の難関の一つだ。",
        "options": [
            "にとって",
            "として",
            "について",
            "に対して"
        ],
        "correctIndex": 0,
        "explanation": "【正解: にとって】\n「名詞＋にとって」は「〜の立場から考えると・〜から見れば…だ」という評価・判断の基準となる視点・立場を提示する表現です。\n\n【選択肢解説】\n1. にとって (正解): 評価の基準となる視点（学習者にとって難関だ）。\n2. として (不正解): 資格・役割（学習者として）。\n3. について (不正解): 話題（学習者についての本など）。\n4. に対して (不正解): 態度を向ける対象。"
    },
    {
        "id": "skm3-fb-q2",
        "chapterId": "skm3-fb",
        "question": "彼は環境問題の専門家（　）、国連の国際シンポジウムに招聘された。",
        "options": [
            "として",
            "にとって",
            "によって",
            "について"
        ],
        "correctIndex": 0,
        "explanation": "【正解: として】\n「名詞＋として」は「〜という立場・資格・役割・名目で」を表します。専門家という資格で招聘されたという文脈に合致します。\n\n【選択肢解説】\n1. として (正解): 立場・資格の提示（専門家として）。\n2. にとって (不正解): 評価の基準。\n3. によって (不正解): 手段・原因。\n4. について (不正解): 話題。"
    },
    {
        "id": "skm3-fb-q3",
        "chapterId": "skm3-fb",
        "question": "小説『坊っちゃん』は、明治時代の文豪・夏目漱石（　）執筆された。",
        "options": [
            "によって",
            "に対して",
            "にとって",
            "として"
        ],
        "correctIndex": 0,
        "explanation": "【正解: によって】\n無生物主語の受身文において、創作・執筆・発見・発明の動作主（作者・開発者）を提示するには「名詞＋によって」を用います。\n\n【選択肢解説】\n1. によって (正解): 受身文における創作の動作主（夏目漱石によって執筆された）。\n2. に対して (不正解): 態度や行為の対象。\n3. にとって (不正解): 評価の視点。\n4. として (不正解): 役割。"
    },
    {
        "id": "skm3-fb-q4",
        "chapterId": "skm3-fb",
        "question": "店員はどんなに無理なクレームを言ってくる客（　）も、冷静に対応した。",
        "options": [
            "に対して",
            "にとって",
            "として",
            "について"
        ],
        "correctIndex": 0,
        "explanation": "【正解: に対して】\n「名詞＋に対して」は、行為や態度・感情を向ける対象（客に対して対応する）を表します。\n\n【選択肢解説】\n1. に対して (正解): 態度や対応を向ける対象（客に対しても冷静に対応）。\n2. にとって (不正解): 評価の基準。\n3. として (不正解): 資格・役割。\n4. について (不正解): 話題。"
    },
    {
        "id": "skm3-fb-q5",
        "chapterId": "skm3-fb",
        "question": "本日のゼミでは、日本の伝統芸能である歌舞伎の歴史（　）発表いたします。",
        "options": [
            "について",
            "として",
            "にとって",
            "によって"
        ],
        "correctIndex": 0,
        "explanation": "【正解: について】\n「名詞＋について」は話す・聞く・調べる・発表するなどの話題・テーマを提示する表現です（歴史について発表する）。\n\n【選択肢解説】\n1. について (正解): 発表や研究のテーマ・話題（歴史について発表）。\n2. として (不正解): 資格・役割。\n3. にとって (不正解): 評価の基準。\n4. によって (不正解): 手段・原因。"
    },
    {
        "id": "skm3-fb-q6",
        "chapterId": "skm3-fb",
        "question": "お正月の雑煮の味付けは、地域（　）味噌仕立てだったり醤油仕立てだったり様々だ。",
        "options": [
            "によって",
            "にとって",
            "として",
            "について"
        ],
        "correctIndex": 0,
        "explanation": "【正解: によって】\n「名詞＋によって＋違う／様々だ」は、条件や基準に応じて変化・差異があること（多様性）を表します。\n\n【選択肢解説】\n1. によって (正解): 条件に応じた相違・多様性（地域によって様々だ）。\n2. にとって (不正解): 評価の視点。\n3. として (不正解): 役割。\n4. について (不正解): 話題。"
    },
    {
        "id": "skm3-fb-q7",
        "chapterId": "skm3-fb",
        "question": "他人にはガラクタに見えるかもしれないが、私（　）かけがえのない宝物だ。",
        "options": [
            "にとって",
            "として",
            "に対して",
            "について"
        ],
        "correctIndex": 0,
        "explanation": "【正解: にとって】\n「私にとって」は話者自身の主観的価値評価の基準を表し、「私から見れば宝物だ」という文脈に合致します。\n\n【選択肢解説】\n1. にとって (正解): 価値評価の基準（私にとって宝物だ）。\n2. として (不正解): 役割。\n3. に対して (不正解): 対象。\n4. について (不正解): 話題。"
    },
    {
        "id": "skm3-fb-q8",
        "chapterId": "skm3-fb",
        "question": "兄が社交的で友人が多いの（　）、弟は内向的で一人で読書を好む。",
        "options": [
            "に対して",
            "にとって",
            "として",
            "によって"
        ],
        "correctIndex": 0,
        "explanation": "【正解: に対して】\n「文＋の＋に対して」は、２つの異なる人物や事物の対照的な性質を対比する構文です（兄が社交的なのに対して、弟は内向的だ）。\n\n【選択肢解説】\n1. に対して (正解): ２つの実体の対比（〜のに対して）。\n2. にとって (不正解): 評価の視点。\n3. として (不正解): 役割。\n4. によって (不正解): 原因・手段。"
    },
    {
        "id": "skm3-fb-q9",
        "chapterId": "skm3-fb",
        "question": "最近は紙の辞書を持ち歩かず、スマートフォンを電子辞書代わり（　）活用している。",
        "options": [
            "として",
            "にとって",
            "に対して",
            "について"
        ],
        "correctIndex": 0,
        "explanation": "【正解: として】\n「名詞＋として」は「〜の役割・機能として代用する」という名目・役割を表します（辞書代わりとして活用する）。\n\n【選択肢解説】\n1. として (正解): 代用の機能・役割の提示（辞書代わりとして）。\n2. にとって (不正解): 評価の視点。\n3. に対して (不正解): 対象。\n4. について (不正解): 話題。"
    },
    {
        "id": "skm3-fb-q10",
        "chapterId": "skm3-fb",
        "question": "増税方針が発表されると、世論調査では政府の経済政策（　）批判が急増した。",
        "options": [
            "に対する",
            "にとっての",
            "としての",
            "によった"
        ],
        "correctIndex": 0,
        "explanation": "【正解: に対する】\n「名詞＋に対する＋名詞」は、批判・要望・態度などが向けられる客体を修飾する名詞修飾形です（政策に対する批判）。\n\n【選択肢解説】\n1. に対する (正解): 名詞修飾形（政策に対する批判）。\n2. にとっての (不正解): 評価基準の修飾。\n3. としての (不正解): 資格修飾。\n4. によった (不正解): 文法的に不自然。"
    },
    {
        "id": "skm3-fb-q11",
        "chapterId": "skm3-fb",
        "question": "昨晩の激しい大雪（　）、今朝の首都圏の鉄道網は完全に麻痺した。",
        "options": [
            "によって",
            "にとって",
            "として",
            "に対して"
        ],
        "correctIndex": 0,
        "explanation": "【正解: によって】\n「名詞＋によって」は客観的な自然災害や客観的出来事が原因となって大きな影響が生じたことを表します（大雪によって麻痺した）。\n\n【選択肢解説】\n1. によって (正解): 客観的原因・理由（大雪によって）。\n2. にとって (不正解): 評価の視点。\n3. として (不正解): 資格。\n4. に対して (不正解): 態度を向ける対象。"
    },
    {
        "id": "skm3-fb-q12",
        "chapterId": "skm3-fb",
        "question": "マーケティング部門では、若者の消費動向（　）詳細なアンケート調査を実施した。",
        "options": [
            "についての",
            "にとっての",
            "としての",
            "に対する"
        ],
        "correctIndex": 0,
        "explanation": "【正解: についての】\n「名詞＋についての＋名詞」は、調査・研究・議論の内容・テーマを名詞修飾する表現です（消費動向についてのアンケート調査）。\n\n【選択肢解説】\n1. についての (正解): テーマを修飾する「についての＋名詞」。\n2. にとっての (不正解): 評価視点の修飾。\n3. としての (不正解): 資格修飾。\n4. に対する (不正解): 対象修飾。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-fb"]
exercises_data.extend(fb_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(fb_exercises)} exercises for SKM N3 Form Review B!")

# 3. Enrich base-reviewed.json for Form Review B
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "added-n3-b-60": {
        "title": "助詞の整理 B: について・に対して・によって・にとって・として (Compound Postposition Systematization)",
        "connection": "名詞 + について(の) / に対して(に対する) / によって(による) / にとって(の) / として(の)",
        "nuance": "【Shin Kanzen Master N3 pp. 62-63 正式規則】文法形式の整理 B：助詞のような働きをする機能表現の体系的分類。\n1.「〜について」: 話題・研究・思考の対象（〜の内容、〜に関係のある）。\n2.「〜に対して」: ①行為・態度・感情を向ける対象；②２つの実体の対比（〜のに対して）。\n3.「〜によって」: ①受身文の創作・発明の動作主（〜によって書かれた）；②手段・方法；③客観的原因・理由；④対応・多様性（〜によって違う）。\n4.「〜にとって」: 評価・判断の基準となる立場（〜の立場から考えると…だ。形容詞述語が多い）。\n5.「〜として」: 立場・資格・役割・名目（〜の資格で、〜の代用として）。",
        "keyTakeaway": "Systematizes essential compound postpositions: について (topic/theme), に対して (target of attitude / contrast), によって (passive agent / means / cause / variation), にとって (evaluating perspective), and として (capacity/role).",
        "sentences": [
            {
                "id": "added-n3-b-60::s-skm3-fb-1",
                "japanese": "日本の教育制度の歴史について、詳しく調べてレポートを書いた。",
                "english": "I investigated the history of Japan's educational system in detail and wrote a report about it.",
                "literal": "Japan's education-system's history about, in-detail investigated-and report wrote.",
                "tokens": [{"word": "歴史について", "meaning": "about the history", "reading": "れきしについて", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 62 verbatim sentence 1: について marking research topic."
            },
            {
                "id": "added-n3-b-60::s-skm3-fb-2",
                "japanese": "店員はお客様に対して、常に丁寧な言葉遣いと笑顔で接するべきだ。",
                "english": "Store clerks ought to always treat customers with polite language and a smile.",
                "literal": "Clerk customers toward, always polite language and smile-with treat ought-to.",
                "tokens": [{"word": "お客様に対して", "meaning": "toward customers", "reading": "おきゃくさまにたいして", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 62 verbatim sentence 1 (Section 2): に対して marking target of attitude."
            },
            {
                "id": "added-n3-b-60::s-skm3-fb-3",
                "japanese": "日本に住む留学生にとって、物価の高さや家賃の負担は重大な問題だ。",
                "english": "For international students living in Japan, high prices and the burden of rent are grave problems.",
                "literal": "Japan-in living international-students for, prices highness rent burden grave problem.",
                "tokens": [{"word": "留学生にとって", "meaning": "for international students", "reading": "りゅうがくせいにとって", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 63 verbatim sentence 1: にとって marking evaluating standpoint."
            },
            {
                "id": "added-n3-b-60::s-skm3-fb-4",
                "japanese": "彼は環境問題の専門家として、国際会議に招かれて基調講演を行った。",
                "english": "As an environmental expert, he was invited to the international conference and delivered the keynote address.",
                "literal": "He environment-problem expert as, international-conference invited keynote-speech gave.",
                "tokens": [{"word": "専門家として", "meaning": "as an expert", "reading": "せんもんかとして", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 63 verbatim sentence 2: として marking status and capacity."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched SKM N3 Form Review B card in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

fb_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review B",
        "exactPrintedPages": "pp. 62-63",
        "exactPdfPages": "pp. 85-86",
        "grammarItem": "助詞の整理 B: について・に対して・によって・にとって・として (Compound Postposition Systematization)",
        "instructionalDetails": "Comprehensive compound particle taxonomy: について (theme/content), に対して (target of attitude / contrast), によって (passive agent / means / cause / variation), にとって (evaluating perspective), として (capacity/role).",
        "cardId": "added-n3-b-60",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-b-60::s-skm3-fb-1",
            "added-n3-b-60::s-skm3-fb-2",
            "added-n3-b-60::s-skm3-fb-3",
            "added-n3-b-60::s-skm3-fb-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 62-63 (PDF pp. 85-86). Verified 5 compound postpositions, semantic contrasts, noun-modifying forms (〜に対する, 〜にとっての, 〜としての), and exercise drills."
    }
]

existing_card_ids = {e.get("cardId") for e in fb_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(fb_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Form Review B in source coverage matrix! Total certified rows: {len(matrix)}")
