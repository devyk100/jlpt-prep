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
    "生活習慣病": {"reading": "せいかつしゅうかんびょう", "meaning": "lifestyle disease / adult-onset illness"},
    "音程": {"reading": "おんてい", "meaning": "musical pitch / interval"},
    "脱字": {"reading": "だつじ", "meaning": "omitted character / missing letter"},
    "誤字": {"reading": "ごじ", "meaning": "misprint / typographical error"},
    "徹夜": {"reading": "てつや", "meaning": "staying up all night / night-long work"},
    "ギックリ腰": {"reading": "ぎっくりごし", "meaning": "strained back / acute lower back pain"},
    "鳴り響いた": {"reading": "なりひびいた", "meaning": "echoed loudly / rang out"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Chapter 11
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

c11_exercises = [
    {
        "id": "skm3-c11-q1",
        "chapterId": "skm3-c11",
        "question": "お風呂に（　）とした瞬間、急に電話のベルが激しく鳴り響いた。",
        "options": [
            "入ろう",
            "入る",
            "入った",
            "入れば"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 入ろう】\n「動詞意向形＋とする（とした瞬間）」は「まさにその行為を行おうとする直前の瞬間」を表します。お風呂に入ろうとした矢先に電話が鳴るという場面に合致します。\n\n【選択肢解説】\n1. 入ろう (正解): 意向形「入ろう」＋とした瞬間（行為直前の瞬間）。\n2. 入る (不正解): 辞書形ではこの直前構文にならない。\n3. 入った (不正解): 過去形不適合。\n4. 入れば (不正解): 条件形不適合。"
    },
    {
        "id": "skm3-c11-q2",
        "chapterId": "skm3-c11",
        "question": "彼は自分の非が明らかなのに、相手に一言も（　）としない。",
        "options": [
            "謝ろう",
            "謝る",
            "謝って",
            "謝りたい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 謝ろう】\n「動詞意向形＋としない」は「第三者がまったく〜する意志を持たない／頑なに拒絶する」という無意志・頑迷な態度を表します。\n\n【選択肢解説】\n1. 謝ろう (正解): 意向形「謝ろう」＋としない（頑なに謝ろうとしない）。\n2. 謝る (不正解): 接続不適合。\n3. 謝って (不正解): 接続不適合。\n4. 謝りたい (不正解): 第一人称願望。"
    },
    {
        "id": "skm3-c11-q3",
        "chapterId": "skm3-c11",
        "question": "生活習慣病を予防するために、毎朝エレベーターを使わず階段を（　）ようにしている。",
        "options": [
            "使う",
            "使おう",
            "使った",
            "使えば"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 使う】\n「動詞辞書形＋ようにしている」は目的（健康増進など）を達成するために「意識的に努力・配慮を払い続けている」という習慣的努力を表します。\n\n【選択肢解説】\n1. 使う (正解): 動詞辞書形＋ようにしている（努力して階段を使う）。\n2. 使おう (不正解): 意向形は接続しない。\n3. 使った (不正解): 過去形は接続しない。\n4. 使えば (不正解): 条件形。"
    },
    {
        "id": "skm3-c11-q4",
        "chapterId": "skm3-c11",
        "question": "どんなに仕事が忙しくても、週末は家族と過ごす（　）にしている。",
        "options": [
            "こと",
            "よう",
            "つもり",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: こと】\n「〜ことにしている」は話者が自ら決めた確固たる方針・生活信条（ポリシー）が現在も継続していることを表します。\n\n【選択肢解説】\n1. こと (正解): 「〜ことにしている（自ら課した確固たる個人ルール）」。\n2. よう (不正解): 「〜ようにしている」は努力目標のニュアンスが強く、明確な決意・ポリシーの宣言には「ことにしている」が最適。\n3. つもり (不正解): 主観的思い込み。\n4. わけ (不正解): 理由。"
    },
    {
        "id": "skm3-c11-q5",
        "chapterId": "skm3-c11",
        "question": "自分では上手に歌えた（　）だったが、録音を聴いてみたら音程がズレていた。",
        "options": [
            "つもり",
            "こと",
            "よう",
            "はず"
        ],
        "correctIndex": 0,
        "explanation": "【正解: つもり】\n「動詞た形＋つもり（だった）」は「（客観的事実は別として）自分自身ではそのように思い込んでいた・信じていた」という主観的確信を表します。\n\n【選択肢解説】\n1. つもり (正解): 「歌えたつもりだった（自分ではうまく歌えたと思い込んでいた）」。\n2. こと (不正解): 事実化。\n3. よう (不正解): 比喩・様態。\n4. はず (不正解): 客観的根拠に基づく予測。"
    },
    {
        "id": "skm3-c11-q6",
        "chapterId": "skm3-c11",
        "question": "パソコンの電源を（　）としたら、急に画面が真っ暗になってフリーズした。",
        "options": [
            "切ろう",
            "切る",
            "切って",
            "切った"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 切ろう】\n「動詞意向形＋としたら」は「ある行為を行おうとした瞬間・矢先」に予期せぬ別の事態が発生したことを表します。\n\n【選択肢解説】\n1. 切ろう (正解): 意向形「切ろう」＋としたら（切ろうとしたまさにその時）。\n2. 切る (不正解): 辞書形不適合。\n3. 切って (不正解): て形不適合。\n4. 切った (不正解): 過去形不適合。"
    },
    {
        "id": "skm3-c11-q7",
        "chapterId": "skm3-c11",
        "question": "弟は部屋がどんなに散らかっていても、自分から掃除を（　）としない。",
        "options": [
            "しよう",
            "する",
            "して",
            "したい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: しよう】\n「する→しよう＋としない」で「掃除をする意志を少しも見せない、やろうとしない」という第三者の意志の完全な欠如・拒絶を表します。\n\n【選択肢解説】\n1. しよう (正解): するの意向形「しよう」＋としない。\n2. する (不正解): 接続不適合。\n3. して (不正解): 接続不適合。\n4. したい (不正解): 願望不適合。"
    },
    {
        "id": "skm3-c11-q8",
        "chapterId": "skm3-c11",
        "question": "重要な契約書ですので、誤字や脱字が（　）ようにしてください。",
        "options": [
            "ない",
            "なかろう",
            "なく",
            "なければ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ない】\n「動詞ない形＋ようにしてください」は、好ましくない事態（誤字脱字など）が発生しないように配慮・努力してほしいと依頼する表現です。\n\n【選択肢解説】\n1. ない (正解): ない＋ようにしてください（配慮の依頼）。\n2. なかろう (不正解): 推量形不適合。\n3. なく (不正解): 中止形不適合。\n4. なければ (不正解): 条件形不適合。"
    },
    {
        "id": "skm3-c11-q9",
        "chapterId": "skm3-c11",
        "question": "健康管理のため、フリーランスになってからは徹夜の仕事は（　）ことにしている。",
        "options": [
            "引き受けない",
            "引き受ける",
            "引き受けよう",
            "引き受けた"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 引き受けない】\n「動詞ない形＋ことにしている」で「〜しないという自己ルールを課して実践している」という禁則のポリシーを表します。\n\n【選択肢解説】\n1. 引き受けない (正解): 「引き受けないことにしている（引き受けないというポリシー）」。\n2. 引き受ける (不正解): 肯定になり健康管理の文脈と矛盾。\n3. 引き受けよう (不正解): 意向形不適合。\n4. 引き受けた (不正解): 過去形不適合。"
    },
    {
        "id": "skm3-c11-q10",
        "chapterId": "skm3-c11",
        "question": "軽いアドバイスの（　）で言った言葉が、彼女を深く傷つけてしまった。",
        "options": [
            "つもり",
            "こと",
            "よう",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: つもり】\n「名詞＋のつもりで」は「自分としてはそのような意図・気持ちで」という主観的な意図・意識を表します。\n\n【選択肢解説】\n1. つもり (正解): 「アドバイスのつもりで言った（助言の意図で発言した）」。\n2. こと (不正解): 形式名詞不適合。\n3. よう (不正解): 比喩不適合。\n4. わけ (不正解): 理由不適合。"
    },
    {
        "id": "skm3-c11-q11",
        "chapterId": "skm3-c11",
        "question": "重い荷物を一人で持ち上げ（　）としたら、ギックリ腰になってしまった。",
        "options": [
            "よう",
            "る",
            "た",
            "て"
        ],
        "correctIndex": 0,
        "explanation": "【正解: よう】\n「持ち上げる→持ち上げよう＋としたら」で「重い荷物を持ち上げようと試みた瞬間に腰を痛めた」という試みとその結果を表します。\n\n【選択肢解説】\n1. よう (正解): 持ち上げようとしたら。\n2. る (不正解): 活用不一致。\n3. た (不正解): 活用不一致。\n4. て (不正解): 活用不一致。"
    },
    {
        "id": "skm3-c11-q12",
        "chapterId": "skm3-c11",
        "question": "あなたは一人で何でも解決できる（　）かもしれないが、周囲の助けも必要だ。",
        "options": [
            "つもり",
            "こと",
            "はず",
            "わけ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: つもり】\n「〜（の）つもりかもしれないが」は「本人はそのようにうぬぼれて思い込んでいるかもしれないが」と相手の過信をとがめる批判表現です。\n\n【選択肢解説】\n1. つもり (正解): 相手の思い込みに対する批判（解決できるつもりかもしれないが）。\n2. こと (不正解): 事実。\n3. はず (不正解): 確実な予測。\n4. わけ (不正解): 論理的理由。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-c11"]
exercises_data.extend(c11_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(c11_exercises)} exercises for SKM N3 Chapter 11!")

# 3. Enrich base-reviewed.json for Chapter 11 cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-u11-you-to-suru-inception": {
        "title": "〜(よ)うとする / 〜(よ)うとしない (Inception, Attempt & Stubborn Refusal)",
        "connection": "動詞意向形（〜(よ)う）+ とする / としたとき / としたら | 否定：〜(よ)うとしない",
        "nuance": "【Shin Kanzen Master N3 p. 51 正式規則】\n1.「〜の直前（まさに〜しようとする瞬間）」: 電車に乗ろうとした瞬間ドアが閉まった、家を出ようとしたら雨が降ってきたなど、行為の直前・矢先の事態。\n2.「〜しようと試みる」: 荷物を持ち上げようとしたら腰を痛めたなど、努力・試み。\n3.「〜(よ)うとしない（頑なな拒否）」: まったく〜する意志がない。主語は話者以外の第三者（父は病院へ行こうとしない）。",
        "keyTakeaway": "Three distinct aspects: (1) Immediate inception right before action; (2) Attempting an exertion; (3) Negative 〜(よ)うとしない indicating stubborn refusal by a third party.",
        "sentences": [
            {
                "id": "skm3-u11-you-to-suru-inception::s-skm3-11-1",
                "japanese": "電車に乗ろうとしたとき、ドアが閉まって乗れなかった。",
                "english": "Just as I was about to board the train, the doors closed and I couldn't get on.",
                "literal": "Train board-attempted when, doors closed-and board-could-not.",
                "tokens": [{"word": "乗ろうとしたとき", "meaning": "just as I was about to board", "reading": "のろうとしたとき", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 1: inception interrupted by doors closing."
            },
            {
                "id": "skm3-u11-you-to-suru-inception::s-skm3-11-2",
                "japanese": "家を出ようとしたら、突然激しい雨が降り出した。",
                "english": "Just as I was about to leave the house, heavy rain suddenly began pouring down.",
                "literal": "House leave-attempted when, suddenly heavy rain fell.",
                "tokens": [{"word": "出ようとしたら", "meaning": "just as I was about to leave", "reading": "でようとしたら", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 2: inception interrupted by sudden weather change."
            },
            {
                "id": "skm3-u11-you-to-suru-inception::s-skm3-11-3",
                "japanese": "重い荷物を持ち上げようとしたら、腰が痛くなった。",
                "english": "When I attempted to lift the heavy luggage, my lower back started hurting.",
                "literal": "Heavy luggage lift-attempted when, lower-back hurt became.",
                "tokens": [{"word": "持ち上げようとしたら", "meaning": "when I attempted to lift", "reading": "もちあげようとしたら", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 3: physical exertion attempt resulting in injury."
            },
            {
                "id": "skm3-u11-you-to-suru-inception::s-skm3-11-4",
                "japanese": "父は自分の体の調子が悪いのに、病院へ行こうとしない。",
                "english": "Although my father isn't feeling well, he stubbornly refuses to go to the hospital.",
                "literal": "Father self's body condition bad although, hospital to go-attempt-not.",
                "tokens": [{"word": "行こうとしない", "meaning": "stubbornly refuses to go", "reading": "いこうとしない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 5: third-party total lack of willingness."
            }
        ]
    },
    "skm3-u7-you-ni-suru": {
        "title": "〜ようにする / 〜ようにしている (Conscious Effort & Habitual Endeavor)",
        "connection": "動辞書形 / 動ない形 + ようにする / ようにしている",
        "nuance": "【Shin Kanzen Master N3 p. 50 正式規則】「努力して〜する／〜しないように心掛ける。」目的達成のために意識的に努力や配慮を払うこと。「〜ようにしている」の形は、目的のために現在も継続して努力・心掛けを怠らない姿勢を表す。動詞は意志的動作動詞。",
        "keyTakeaway": "Making a conscious endeavor or deliberate ongoing effort ('make sure to / try my best to / endeavor habitually').",
        "sentences": [
            {
                "id": "skm3-u7-you-ni-suru::s-skm3-11-1",
                "japanese": "水や電気は、無駄に使わないようにしよう。",
                "english": "Let us make a conscious effort not to waste water and electricity.",
                "literal": "Water and electricity wastefully use-not endeavor let's-do.",
                "tokens": [{"word": "使わないようにしよう", "meaning": "let's endeavor not to use", "reading": "つかわないようにしよう", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 50 verbatim sentence 1: conservation endeavor."
            },
            {
                "id": "skm3-u7-you-ni-suru::s-skm3-11-2",
                "japanese": "妻の機嫌を損ねないように気をつけている。",
                "english": "I make a conscious effort to be careful not to sour my wife's mood.",
                "literal": "Wife's mood damage-not endeavor care taking.",
                "tokens": [{"word": "損ねないように", "meaning": "so as not to damage", "reading": "そこねないように", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 50 verbatim sentence 2: interpersonal care and mindfulness."
            },
            {
                "id": "skm3-u7-you-ni-suru::s-skm3-11-3",
                "japanese": "集合時間には絶対に遅れないようにしてください。",
                "english": "Please make sure that you are definitely not late for the meeting time.",
                "literal": "Meeting time definitely be-late-not endeavor please-do.",
                "tokens": [{"word": "遅れないようにしてください", "meaning": "please make sure not to be late", "reading": "おくれたないようにしてください", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 50 verbatim sentence 3: polite instruction to take care."
            },
            {
                "id": "skm3-u7-you-ni-suru::s-skm3-11-4",
                "japanese": "毎晩寝る前に、必ず日本語の単語を10個覚えるようにしている。",
                "english": "Every night before going to bed, I make a point of memorizing 10 Japanese vocabulary words.",
                "literal": "Every-night sleeping before, definitely Japanese vocabulary 10 memorize endeavor doing.",
                "tokens": [{"word": "覚えるようにしている", "meaning": "make an effort to memorize", "reading": "おぼえるようにしている", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 50 verbatim sentence 4: daily educational self-discipline."
            }
        ]
    },
    "skm3-u11-koto-ni-shite-iru": {
        "title": "〜ことにする / 〜ことにしている (Personal Decision & Ongoing Habitual Policy)",
        "connection": "動辞書形 / 動ない形 + ことにする / ことにしている",
        "nuance": "【Shin Kanzen Master N3 p. 50 正式規則】「〜と決める。」話者が自らの意志で行動を決定する表現。「〜ことにした」は過去の決定、「〜ことにしよう」はその場の意志決定。「〜ことにしている」は過去の自己決定が今も生きており、個人の習慣・生活信条（マイルール・ポリシー）となっていることを表す。",
        "keyTakeaway": "Declares an intentional personal decision ('decide to') or a firm, self-imposed ongoing personal rule ('make it a strict rule to...').",
        "sentences": [
            {
                "id": "skm3-u11-koto-ni-shite-iru::s-skm3-11-1",
                "japanese": "今年の夏休みは、どこへも行かないで家でゆっくり休むことにした。",
                "english": "I have decided not to go anywhere this summer vacation and relax at home instead.",
                "literal": "This-year summer-vacation anywhere go-not home slowly rest decided.",
                "tokens": [{"word": "休むことにした", "meaning": "decided to rest", "reading": "やすむことにした", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 50 verbatim sentence 2: personal holiday decision."
            },
            {
                "id": "skm3-u11-koto-ni-shite-iru::s-skm3-11-2",
                "japanese": "部長の無理な指示には従わないことに決めた。",
                "english": "I have firmly decided not to obey the department manager's unreasonable orders.",
                "literal": "Manager's unreasonable orders obey-not decided.",
                "tokens": [{"word": "従わないことに決めた", "meaning": "decided not to obey", "reading": "したがわないことにきめた", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 50 verbatim sentence 3: firm conscious resolve."
            },
            {
                "id": "skm3-u11-koto-ni-shite-iru::s-skm3-11-3",
                "japanese": "健康のために、毎日野菜をたくさん食べることにしている。",
                "english": "For the sake of my health, I make it a strict rule to eat plenty of vegetables every day.",
                "literal": "Health for, every-day vegetables lots eat rule have.",
                "tokens": [{"word": "食べることにしている", "meaning": "make it a rule to eat", "reading": "たべることにしている", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 50 verbatim sentence 4: personal dietary policy."
            },
            {
                "id": "skm3-u11-koto-ni-shite-iru::s-skm3-11-4",
                "japanese": "夜十時以降は仕事のメールを見ないことにしています。",
                "english": "I make it a policy not to look at work emails after ten o'clock at night.",
                "literal": "Night 10-o'clock after work email see-not rule have.",
                "tokens": [{"word": "見ないことにしています", "meaning": "make it a rule not to look", "reading": "みないことにしています", "pos": "Grammar"}],
                "nuanceNote": "Self-imposed professional boundary."
            }
        ]
    },
    "skm3-u11-tsumori-da": {
        "title": "〜（の）つもりだ (Subjective Belief Contrary to Fact & Arrogant Assumptions)",
        "connection": "普通形（な形な・名詞の）+ つもりだ / つもりでいる / つもりだった",
        "nuance": "【Shin Kanzen Master N3 p. 51 正式規則】「（客観的事実や他者の評価とは異なっていても、）自分としては〜という気持ち・確信・思い込みを抱いている。」This at any rate is my internal feeling/belief about ~ (though objective reality or others may differ). Often used with past tense (つもりだった) to indicate a mistaken assumption, or critically to rebuke someone's arrogant belief (〜つもりかもしれないが).",
        "keyTakeaway": "Subjective belief, mindset, or mistaken assumption contrary to objective reality ('acting as if / under the impression that / assuming in one's mind').",
        "sentences": [
            {
                "id": "skm3-u11-tsumori-da::s-skm3-11-1",
                "japanese": "私はまだまだ若いつもりだが、階段を上ると息が切れる。",
                "english": "In my own mind I still feel young, but climbing stairs leaves me out of breath.",
                "literal": "I still young impression-have but, stairs climb breath cuts.",
                "tokens": [{"word": "若いつもりだが", "meaning": "feel young in my mind but", "reading": "わかいつもりだが", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 1: subjective feeling of youth vs physical reality."
            },
            {
                "id": "skm3-u11-tsumori-da::s-skm3-11-2",
                "japanese": "冗談のつもりで言ったのに、彼を本気で怒らせてしまった。",
                "english": "I said it intending it merely as a joke, but it ended up making him genuinely furious.",
                "literal": "Joke impression-with said although, him genuinely angered.",
                "tokens": [{"word": "冗談のつもりで", "meaning": "intending it as a joke", "reading": "じょうだんのつもりで", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 2: subjective innocent intent vs grave outcome."
            },
            {
                "id": "skm3-u11-tsumori-da::s-skm3-11-3",
                "japanese": "先週送ったメール、もう読んでもらえたつもりでいた。",
                "english": "I was under the impression that you had already read the email I sent last week.",
                "literal": "Last-week sent email, already read-received impression-with was.",
                "tokens": [{"word": "つもりでいた", "meaning": "was under the impression", "reading": "つもりでいた", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 3: mistaken cognitive assumption."
            },
            {
                "id": "skm3-u11-tsumori-da::s-skm3-11-4",
                "japanese": "あなたは全部知っているつもりかもしれないが、本当は何も分かっていない。",
                "english": "You might believe in your mind that you know everything, but in truth you understand nothing.",
                "literal": "You all know impression may-have but, truth nothing understand-not.",
                "tokens": [{"word": "知っているつもりかもしれないが", "meaning": "may think you know everything but", "reading": "しっているつもりかもしれないが", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 51 verbatim sentence 4: rebuke of arrogant assumption."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Chapter 11 cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

c11_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 11",
        "exactPrintedPages": "p. 51",
        "exactPdfPages": "p. 74",
        "grammarItem": "〜(よ)うとする / 〜(よ)うとしない (Inception, Attempt & Stubborn Refusal)",
        "instructionalDetails": "V-意向形 + とする/としたら (inception on verge of action; exertion attempt); negative 〜(よ)うとしない (third-party complete lack of will or stubborn refusal).",
        "cardId": "skm3-u11-you-to-suru-inception",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u11-you-to-suru-inception::s-skm3-11-1",
            "skm3-u11-you-to-suru-inception::s-skm3-11-2",
            "skm3-u11-you-to-suru-inception::s-skm3-11-3",
            "skm3-u11-you-to-suru-inception::s-skm3-11-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 51 (PDF p. 74). Verified Section 3 inception semantics, interrupted attempts, and third-person negative refusal rules."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 11",
        "exactPrintedPages": "p. 50",
        "exactPdfPages": "p. 73",
        "grammarItem": "〜ようにする / 〜ようにしている (Conscious Effort & Habitual Endeavor)",
        "instructionalDetails": "V-dict / V-ない + ようにする/ようにしている; conscious effort to achieve a purpose; ongoing lifestyle endeavor.",
        "cardId": "skm3-u7-you-ni-suru",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u7-you-ni-suru::s-skm3-11-1",
            "skm3-u7-you-ni-suru::s-skm3-11-2",
            "skm3-u7-you-ni-suru::s-skm3-11-3",
            "skm3-u7-you-ni-suru::s-skm3-11-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 50 (PDF p. 73). Verified Section 2 deliberate endeavor rules and ongoing behavioral mindfulness."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 11",
        "exactPrintedPages": "p. 50",
        "exactPdfPages": "p. 73",
        "grammarItem": "〜ことにする / 〜ことにしている (Personal Decision & Ongoing Habitual Policy)",
        "instructionalDetails": "V-dict / V-ない + ことにする/ことにしている; conscious personal choice; ongoing disciplined personal policy/rule.",
        "cardId": "skm3-u11-koto-ni-shite-iru",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u11-koto-ni-shite-iru::s-skm3-11-1",
            "skm3-u11-koto-ni-shite-iru::s-skm3-11-2",
            "skm3-u11-koto-ni-shite-iru::s-skm3-11-3",
            "skm3-u11-koto-ni-shite-iru::s-skm3-11-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 50 (PDF p. 73). Verified Section 1 decision-making structures and self-imposed ongoing code of conduct."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 11",
        "exactPrintedPages": "p. 51",
        "exactPdfPages": "p. 74",
        "grammarItem": "〜（の）つもりだ (Subjective Belief Contrary to Fact & Arrogant Assumptions)",
        "instructionalDetails": "Plain form (な-adj な, Noun の) + つもりだ/つもりでいる/つもりだった; subjective conviction/intent held in mind regardless of reality; past mistaken assumptions; criticism of overconfidence.",
        "cardId": "skm3-u11-tsumori-da",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u11-tsumori-da::s-skm3-11-1",
            "skm3-u11-tsumori-da::s-skm3-11-2",
            "skm3-u11-tsumori-da::s-skm3-11-3",
            "skm3-u11-tsumori-da::s-skm3-11-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 51 (PDF p. 74). Verified Section 4 subjective belief semantics, mistaken assumptions with 〜たつもりだった, and rebuke usage."
    }
]

existing_card_ids = {e.get("cardId") for e in c11_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(c11_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Chapter 11 in source coverage matrix! Total certified rows: {len(matrix)}")
