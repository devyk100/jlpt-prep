import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
BASE_PATH = ROOT / "content/base-reviewed.json"
CHAPTER_EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"

# 1. 12 Authentic Exercises for Form Review F
ff_exercises = [
    {
        "id": "skm3-ff-q1",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Habitual criticism: younger brother avoids homework and does nothing but play video games all day.",
        "question": "弟は宿題もしないで、一日中部屋でゲームを（　）ばかりいる。",
        "translation": "Without even doing his homework, my younger brother does nothing but play video games in his room all day long.",
        "options": ["して", "する", "した", "しようと"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「動詞て形＋ばかりいる」は、他の必要なことをせず『特定の行為だけを繰り返し行っている』ことに対する非難・批判の語感を伴う表現です（ゲームをしてばかりいる）。",
            "options": [
                {"text": "して", "isCorrect": True, "reason": "【正解】動詞て形＋ばかりいる（反復的熱中・非難の接続規則）。", "trapCategory": ""},
                {"text": "する", "isCorrect": False, "reason": "【不正解】辞書形＋ばかりいるという接続は文法的に存在しません。", "trapCategory": "formation"},
                {"text": "した", "isCorrect": False, "reason": "【不正解】た形＋ばかりいるは誤り（したばかりだ＝完了直後）。", "trapCategory": "formation"},
                {"text": "しようと", "isCorrect": False, "reason": "【不正解】意向形＋ばかりいるは非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What verb form connects directly to ばかりいる to express critical habitual indulgence?"
    },
    {
        "id": "skm3-ff-q2",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Worsening trend: surgery finished, but patient's physical stamina continues steadily to deteriorate.",
        "question": "手術後も容態は一向に改善せず、日を追うごとに悪化する（　）。",
        "translation": "Even after surgery the condition did not improve at all; with each passing day, it only continues steadily to worsen.",
        "options": ["ばかりだ", "ところだ", "わけだ", "ものだ"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「変化動詞の辞書形（悪化する、減る、下がる）＋ばかりだ」は、事態が悪い方向へ一方通行で変化し続けている傾向（一途をたどる）を表します。",
            "options": [
                {"text": "ばかりだ", "isCorrect": True, "reason": "【正解】変化動詞辞書形＋ばかりだ＝事態の一方的悪化傾向。", "trapCategory": ""},
                {"text": "ところだ", "isCorrect": False, "reason": "【不正解】悪化するところだ＝直前アスペクトとなり、現在進行中の継続的悪化傾向を表せません。", "trapCategory": "nuance"},
                {"text": "わけだ", "isCorrect": False, "reason": "【不正解】当然の論理的帰結となり、容態の不可解な継続悪化の文脈に合いません。", "trapCategory": "meaning"},
                {"text": "ものだ", "isCorrect": False, "reason": "【不正解】一般的な本質・慨嘆を表す表現であり、特定の患者の悪化推移には不適切です。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which pattern denotes an ongoing, steady momentum moving in a negative direction with change verbs?"
    },
    {
        "id": "skm3-ff-q3",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "All preparations ready: bags packed, train tickets purchased, only leaving remains.",
        "question": "荷造りも電車の切符の手配も完了した。あとは明日の朝（　）ばかりだ。",
        "translation": "Packing and train ticket arrangements are both complete. All that remains now is to depart tomorrow morning.",
        "options": ["出発する", "出発した", "出発して", "出発しよう"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「あとは＋動詞辞書形＋ばかりだ」は、すべての準備が整い『あとはその行為を行うだけの状態になっている』ことを表す慣用構文です。",
            "options": [
                {"text": "出発する", "isCorrect": True, "reason": "【正解】あとは＋辞書形＋ばかりだ（準備完了、残すは最終行動のみ）。", "trapCategory": ""},
                {"text": "出発した", "isCorrect": False, "reason": "【不正解】過去完了形となり、明日の朝という未来の行動と矛盾します。", "trapCategory": "formation"},
                {"text": "出発して", "isCorrect": False, "reason": "【不正解】て形＋ばかりだは接続違反です。", "trapCategory": "formation"},
                {"text": "出発しよう", "isCorrect": False, "reason": "【不正解】意向形＋ばかりだは非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "What form attaches to ばかりだ when expressing that everything is ready and only the final act remains?"
    },
    {
        "id": "skm3-ff-q4",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Subjective recency: speaker bought the phone two weeks ago, but feels it is brand new.",
        "question": "このスマートフォンは先週（　）ばかりなので、まだ使い方がよく分からない。",
        "translation": "I only just bought this smartphone last week, so I don't really know how to use it yet.",
        "options": ["買った", "買う", "買って", "買おう"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「動詞た形＋ばかりだ」は、話者の主観として『完了してからまだ間がない（直後・新しさの感覚）』を表します。「先週買ったばかり」のように、客観的に数日〜数週間経過していても主観的に新しければ使えます。",
            "options": [
                {"text": "買った", "isCorrect": True, "reason": "【正解】動詞た形＋ばかりだ＝主観的直後・完了したばかり。", "trapCategory": ""},
                {"text": "買う", "isCorrect": False, "reason": "【不正解】辞書形＋ばかりだと準備完了または悪化傾向の意味になり文脈不一致。", "trapCategory": "formation"},
                {"text": "買って", "isCorrect": False, "reason": "【不正解】買ってばかりいる（買い物中毒のように買い続けている）となり不適切。", "trapCategory": "formation"},
                {"text": "買おう", "isCorrect": False, "reason": "【不正解】意向形接続は非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which verb form denotes subjective recency (just finished / feels newly completed)?"
    },
    {
        "id": "skm3-ff-q5",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Escalating addition: incredible student can speak not only English, but also French and Chinese fluently.",
        "question": "彼女は英語が流暢な（　）、フランス語や中国語まで自在に操ることができる。",
        "translation": "Not only is she fluent in English, but she can even command French and Chinese with total ease.",
        "options": ["ばかりか", "ばかりで", "ばかりに", "ばかりかといって"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「〜ばかりか（〜ばかりでなく）」は、『Aだけでなく、さらに上回るBまでも』というエスカレートする添加・強調を表します（な形容詞は流暢な＋ばかりか）。",
            "options": [
                {"text": "ばかりか", "isCorrect": True, "reason": "【正解】な形容詞＋ばかりか＝〜だけでなく、さらにそれ以上にも。", "trapCategory": ""},
                {"text": "ばかりで", "isCorrect": False, "reason": "【不正解】中立限定の中止形となり、累加・エスカレートの文末「まで」と呼応しません。", "trapCategory": "context"},
                {"text": "ばかりに", "isCorrect": False, "reason": "【不正解】〜ばかりに＝『〜したことだけが原因で（悪い結果になった）』という遺憾の原因表現です。", "trapCategory": "meaning"},
                {"text": "ばかりかといって", "isCorrect": False, "reason": "【不正解】混種語で非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which pattern functions as an escalating additive marker: not only A, but even B?"
    },
    {
        "id": "skm3-ff-q6",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Contrast between たばかりだ vs たところだ: temporal objectivity vs subjective recency.",
        "question": "「今、電話してもいいですか」「すみません、今（　）ところなので、5分後にかけ直していただけますか」",
        "translation": "'Is it okay to talk on the phone now?' 'Sorry, I just stepped out of the bath right this very second, so could you please call back in 5 minutes?'",
        "options": ["お風呂から上がった", "お風呂から上がる", "お風呂から上がって", "お風呂から上がっている"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「〜たところだ」は時間的に『まさに今その瞬間、直前に行為が完了した』という客観的直前・直後アスペクトを表します。「今上がったところ（数秒・数十秒前の完了）」と即時呼応します。",
            "options": [
                {"text": "お風呂から上がった", "isCorrect": True, "reason": "【正解】動詞た形＋ところだ（まさに今直前完了のアスペクト）。", "trapCategory": ""},
                {"text": "お風呂から上がる", "isCorrect": False, "reason": "【不正解】辞書形＋ところだ＝これから入る直前となり、上がった後の文脈と正反対。", "trapCategory": "nuance"},
                {"text": "お風呂から上がって", "isCorrect": False, "reason": "【不正解】接続文法違反。", "trapCategory": "formation"},
                {"text": "お風呂から上がっている", "isCorrect": False, "reason": "【不正解】上がっているところだ＝動作進行中となり不自然。", "trapCategory": "nuance"}
            ]
        },
        "hint": "What pattern expresses the immediate split-second phase of having just stepped out right now?"
    },
    {
        "id": "skm3-ff-q7",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Dietary balance reproach: eating only meat and refusing vegetables.",
        "question": "お肉（　）食べていないで、野菜もしっかりバランスよく食べなさい。",
        "translation": "Don't eat only meat (to the exclusion of everything else); make sure to eat vegetables in a well-balanced manner too.",
        "options": ["ばかり", "だけ", "ほど", "くらい"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「名詞＋ばかり」は、対象が偏ってそればかりに集中している状態を表し、しばしば不満・小言・忠告の文脈を伴います。中立な限界を示す「だけ」に比べ、偏りへの批判的ニュアンスが明確です。",
            "options": [
                {"text": "ばかり", "isCorrect": True, "reason": "【正解】名詞＋ばかり（偏食・一方的偏りへの忠告・批判）。", "trapCategory": ""},
                {"text": "だけ", "isCorrect": False, "reason": "【不正解】中立的な客観的限定であり、「肉だけ食べないで」より「ばかり」が自然な偏り批判です。", "trapCategory": "nuance"},
                {"text": "ほど", "isCorrect": False, "reason": "【不正解】程度を表す助詞であり、選択肢の偏食を表せません。", "trapCategory": "meaning"},
                {"text": "くらい", "isCorrect": False, "reason": "【不正解】最低限・軽視を表す助詞であり不適です。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which particle conveys excessive bias/imbalance often accompanied by reproach or parental advice?"
    },
    {
        "id": "skm3-ff-q8",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Complaint culture: colleague does nothing but voice complaints and never acts.",
        "question": "彼はいつも不平不満（　）言って、自分からは何一つ改善しようとしない。",
        "translation": "He is always voicing nothing but complaints and discontent, without trying to improve a single thing himself.",
        "options": ["ばかり", "ほど", "など", "さえ"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「名詞＋ばかり＋動詞」で、その行為や対象ばかりに偏っていることへの強い批判を表します（不平不満ばかり言って）。",
            "options": [
                {"text": "ばかり", "isCorrect": True, "reason": "【正解】不平不満ばかり言って（偏った反復行動への批判）。", "trapCategory": ""},
                {"text": "ほど", "isCorrect": False, "reason": "【不正解】程度比較となり文脈に合いません。", "trapCategory": "meaning"},
                {"text": "など", "isCorrect": False, "reason": "【不正解】例示となり、文句ばかり言っているという集中的偏りが示せません。", "trapCategory": "nuance"},
                {"text": "さえ", "isCorrect": False, "reason": "【不正解】極端な例示（さえ）となり文意が通じません。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What particle directly follows nouns of discontent to emphasize constant one-sided complaining?"
    },
    {
        "id": "skm3-ff-q9",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Subjective recency across months: entered the company 3 months ago, still feels like a novice.",
        "question": "入社した（　）の頃は右も左も分からず、毎日が緊張の連続だった。",
        "translation": "Back when I had only just joined the company, I didn't know left from right, and every day was a continuous series of nerves.",
        "options": ["ばかり", "ところ", "わけ", "はず"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「動詞た形＋ばかりの＋名詞」は、行為が完了してまだ間がない時期を修飾します。「入社したばかりの頃」は、客観的には数ヶ月経過していても主観的に新米の時期を指す定番表現です（「入社したところの頃」とは言えません）。",
            "options": [
                {"text": "ばかり", "isCorrect": True, "reason": "【正解】た形＋ばかり＋の頃（主観的新鮮期の修飾表現）。", "trapCategory": ""},
                {"text": "ところ", "isCorrect": False, "reason": "【不正解】誤用トラップ！『ところ』は直前・直後の瞬間アスペクトであり、『ところの頃』という期間修飾はできません。", "trapCategory": "formation"},
                {"text": "わけ", "isCorrect": False, "reason": "【不正解】理由付けになり不適切。", "trapCategory": "meaning"},
                {"text": "はず", "isCorrect": False, "reason": "【不正解】推量になり不適切。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which pattern modifies の頃 (time/era) to mean 'back when I was still brand-new'?"
    },
    {
        "id": "skm3-ff-q10",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Severe addition: not only the driver, but also the passengers were injured.",
        "question": "事故により、運転手（　）同乗していた家族全員が怪我を負った。",
        "translation": "Due to the accident, not only the driver but also all the family members riding along suffered injuries.",
        "options": ["ばかりでなく", "ばかりだから", "ばかりなのに", "ばかりかといって"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「名詞＋ばかりでなく（ばかりか）」は、『〜だけでなく、その枠を超えてさらに〜も』という累加を表します（運転手ばかりでなく、同乗していた家族全員が）。",
            "options": [
                {"text": "ばかりでなく", "isCorrect": True, "reason": "【正解】名詞＋ばかりでなく（〜だけでなく、さらに他の対象も）。", "trapCategory": ""},
                {"text": "ばかりだから", "isCorrect": False, "reason": "【不正解】因果関係となり意味不明になります。", "trapCategory": "formation"},
                {"text": "ばかりなのに", "isCorrect": False, "reason": "【不正解】逆接助詞の誤接続です。", "trapCategory": "formation"},
                {"text": "ばかりかといって", "isCorrect": False, "reason": "【不正解】非文です。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which expression means 'not only [person A], but in addition [person B]'?"
    },
    {
        "id": "skm3-ff-q11",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Economic trend: inflation continues rising steadily, making household budgets tighter.",
        "question": "不況の長期化に伴い、生活必需品の物価は上がる（　）で、家計への負担が増大している。",
        "translation": "With the prolonged economic slump, the prices of daily necessities only continue to rise steadily, increasing the burden on household budgets.",
        "options": ["ばかり", "ところ", "わけ", "はず"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "「動詞辞書形＋ばかりで」は、事態が一方向に進展（特に悪化）し続けている継続的傾向を表します（上がるばかりで）。",
            "options": [
                {"text": "ばかり", "isCorrect": True, "reason": "【正解】変化動詞辞書形＋ばかりで（一途をたどる悪化傾向）。", "trapCategory": ""},
                {"text": "ところ", "isCorrect": False, "reason": "【不正解】アスペクトの誤用。", "trapCategory": "nuance"},
                {"text": "わけ", "isCorrect": False, "reason": "【不正解】『上がるわけで』は接続として破綻しています。", "trapCategory": "formation"},
                {"text": "はず", "isCorrect": False, "reason": "【不正解】推量となり文脈不一致。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which pattern combines with a change verb + で to show an uninterrupted trend causing distress?"
    },
    {
        "id": "skm3-ff-q12",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review F",
        "type": "multiple-choice",
        "context": "Comprehensive test of all 5 ばかり patterns: matching meaning to correct grammatical form.",
        "question": "「会議の資料の印刷も会場の設営も終わりました」「ご苦労様。これで（　）ばかりですね」",
        "translation": "'Printing the meeting materials and setting up the venue are both done.' 'Great job. Now all that remains is to wait for the attendees to arrive, right?'",
        "options": ["参加者の到着を待つ", "参加者の到着を待った", "参加者の到着を待って", "参加者の到着を待っている"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-f-64",
        "grammarPointTitle": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "explanation": {
            "overall": "準備がすべて整い、残すは最後の行動を待つだけという状態には「動詞辞書形＋ばかりだ（待つばかりですね）」を用います。",
            "options": [
                {"text": "参加者の到着を待つ", "isCorrect": True, "reason": "【正解】辞書形＋ばかりだ（あとは〜するだけの準備完了状態）。", "trapCategory": ""},
                {"text": "参加者の到着を待った", "isCorrect": False, "reason": "【不正解】待ったばかりだ＝完了したばかり、となり到着前の状況と矛盾します。", "trapCategory": "formation"},
                {"text": "参加者の到着を待って", "isCorrect": False, "reason": "【不正解】待ってばかりいる＝批判的熱中になり意味不明になります。", "trapCategory": "formation"},
                {"text": "参加者の到着を待っている", "isCorrect": False, "reason": "【不正解】接続文法違反。", "trapCategory": "formation"}
            ]
        },
        "hint": "What is the formula indicating all prep work is done, and only the final act remains?"
    }
]

# Update chapterExercises.json
existing_exs = json.load(open(CHAPTER_EXERCISES_PATH, encoding="utf-8"))
existing_exs = [x for x in existing_exs if x.get("chapter") != "Part 1 · Form review F" and x.get("chapterId") != "skm3-ff"]
existing_exs.extend(ff_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(existing_exs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with 12 exercises for SKM N3 Form Review F! Total: {len(existing_exs)}")

# 2. Enrich base-reviewed.json
base_cards = json.load(open(BASE_PATH, encoding="utf-8"))

card_enrichments = {
    "added-n3-f-64": {
        "title": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "meaning": "Comprehensive taxonomy of ばかり across five fundamental operational dimensions: exclusive bias (Nばかり), habitual indulgence with speaker reproach (V-てばかりいる), escalating addition (〜ばかりか・ばかりでなく), unidirectional worsening trend / ready-state (V-辞書形ばかりだ), and subjective recency (V-たばかりだ).",
        "formation": "①【偏り】N / V辞書形 ＋ ばかり\n②【批判的熱中】Vて ＋ ばかりいる\n③【累加】N / 普通形（Naな）＋ ばかりか・ばかりでなく\n④【一途・準備】V辞書形 ＋ ばかりだ\n⑤【主観的直後】Vた ＋ ばかりだ",
        "explanation": "【教科書体系的整理 (SKM N3 pp. 80-81)】\n1. 名詞＋ばかり / 動詞辞書形＋ばかり (偏り・過剰):\n   - ある事柄だけに偏って他の事柄をしない状態。しばしば偏食や偏った言動に対する不満・批判の気持ちを伴う（例: 肉ばかり食べる、文句ばかり言う）。\n2. 動詞て形＋ばかりいる (反復的熱中への非難):\n   - 他のやるべきことを放棄して、ある行為だけを繰り返し・継続して行っている様子を非難・叱責する（例: ゲームをしてばかりいる、怒ってばかりいる）。\n3. 〜ばかりか / 〜ばかりでなく (エスカレートする累加):\n   - 『Aだけでなく、それを超えてBまでも』と、さらに予想外・深刻な事柄が付け加わることを表す。\n4. 動詞辞書形＋ばかりだ (一途な変化推移 / 準備完了):\n   - (a) 変化動詞（悪化する、下がる、上がるなど）に接続し、事態が一方向に悪化し続ける推移を表す（例: 容態は悪化するばかりだ）。\n   - (b) 『あとは〜するばかりだ』の形で、すべての準備が整い最終行動を残すのみの状態を表す（例: あとは出発するばかりだ）。\n5. 動詞た形＋ばかりだ (主観的直後):\n   - 話者の主観において『その行為が完了してからまだ間がない』ことを表す。客観的物理時間（数分前）に限定される『〜たところだ』と異なり、話者の感覚次第で数週間・数ヶ月前の出来事にも使用可能（例: 先月入社したばかりだ）。",
        "examples": [
            {
                "japanese": "弟は宿題もしないで、一日中部屋でゲームをしてばかりいる。",
                "english": "Without even doing his homework, my younger brother does nothing but play video games in his room all day long.",
                "nuance": "V-てばかりいる expressing critical reproach toward continuous unproductive gaming."
            },
            {
                "japanese": "手術後も容態は一向に改善せず、日を追うごとに悪化するばかりだ。",
                "english": "Even after surgery the condition did not improve at all; with each passing day, it only continues steadily to worsen.",
                "nuance": "V-辞書形＋ばかりだ expressing continuous worsening momentum with change verb 悪化する."
            },
            {
                "japanese": "荷造りも切符の手配も完了した。あとは明日の朝出発するばかりだ。",
                "english": "Packing and ticket arrangements are both complete. All that remains now is to depart tomorrow morning.",
                "nuance": "あとは＋V-辞書形＋ばかりだ expressing that all preparations are set, leaving only departure."
            },
            {
                "japanese": "このスマートフォンは先週買ったばかりなので、まだ使い方がよく分からない。",
                "english": "I only just bought this smartphone last week, so I don't really know how to use it yet.",
                "nuance": "V-たばかりだ expressing subjective recency (bought a week ago, still felt as newly acquired)."
            },
            {
                "japanese": "彼女は英語が流暢なばかりか、フランス語や中国語まで自在に操ることができる。",
                "english": "Not only is she fluent in English, but she can even command French and Chinese with total ease.",
                "nuance": "〜ばかりか escalating addition adding further impressive multilingual capabilities."
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
print("Enriched Form Review F card in base-reviewed.json!")

# 3. Update source-coverage-matrix.json
matrix = json.load(open(MATRIX_PATH, encoding="utf-8"))

ff_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review F",
        "exactPrintedPages": "pp. 80-81",
        "exactPdfPages": "pp. 103-104",
        "grammarItem": "「ばかり」の使い方 F: ばかり・てばかりいる・ばかりか・ばかりだ・たばかりだ",
        "instructionalDetails": "Comprehensive taxonomy of ばかり across 5 operational domains: exclusive bias (Nばかり), habitual indulgence with reproach (Vてばかりいる), escalating addition (ばかりか), worsening trend / ready state (V辞書形ばかりだ), and subjective recency (Vたばかりだ vs Vたところだ).",
        "cardId": "added-n3-f-64",
        "exampleCount": 5,
        "exampleIds": [
            "added-n3-f-64::s-skm3-ff-1",
            "added-n3-f-64::s-skm3-ff-2",
            "added-n3-f-64::s-skm3-ff-3",
            "added-n3-f-64::s-skm3-ff-4",
            "added-n3-f-64::s-skm3-ff-5"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 80-81 (PDF pp. 103-104). Verified complete 5-way functional spectrum of ばかり and contrast with たところだ."
    }
]

existing_card_ids = {e.get("cardId") for e in ff_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(ff_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Form Review F in source coverage matrix! Total certified rows: {len(matrix)}")
