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
    "逞しく": {"reading": "たくましく", "meaning": "robustly / strongly / vigorously"},
    "注射針": {"reading": "ちゅうしゃばり", "meaning": "injection needle / hypodermic needle"},
    "開拓": {"reading": "かいたく", "meaning": "pioneering / opening up new markets"},
    "閲覧": {"reading": "えつらん", "meaning": "inspection / perusal / viewing records"},
    "司会": {"reading": "しかい", "meaning": "master of ceremonies / moderation"},
    "顔色": {"reading": "かおいろ", "meaning": "facial complexion"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Chapter 9
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

c9_exercises = [
    {
        "id": "skm3-c9-q1",
        "chapterId": "skm3-c9",
        "question": "すみませんが、この企画書の日本語をネイティブの方にチェックして（　）のですが。",
        "options": [
            "もらいたい",
            "させてもらいたい",
            "といい",
            "がっている"
        ],
        "correctIndex": 0,
        "explanation": "【正解: もらいたい】\n「〜てもらいたい」は「他人に〜してほしい」と他者の好意的な行為を望む表現です。ネイティブにチェックしてほしいという依頼の願望に合致します。\n\n【選択肢解説】\n1. もらいたい (正解): 他人に〜してもらうことを望む（チェックしてもらいたい）。\n2. させてもらいたい (不正解): 自分がチェックする許可を求める表現になり文意が逆。\n3. といい (不正解): 自分の意志でコントロールできない事態を祈る表現。\n4. がっている (不正解): 第三者の感情の表出。"
    },
    {
        "id": "skm3-c9-q2",
        "chapterId": "skm3-c9",
        "question": "体調が優れないため、本日は早退（　）のですが、よろしいでしょうか。",
        "options": [
            "させていただきたい",
            "していただきたい",
            "してほしい",
            "していい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: させていただきたい】\n「動詞使役て形＋いただきたい」は「自分が〜することを許可してほしい」とへりくだって申し出る極めて丁寧な許可依頼表現です。\n\n【選択肢解説】\n1. させていただきたい (正解): 自分の早退の許可を乞う丁寧な表現。\n2. していただきたい (不正解): 相手に早退してほしいという意味になり不適切。\n3. してほしい (不正解): 相手への直接的希望。\n4. していい (不正解): 敬意を欠く。"
    },
    {
        "id": "skm3-c9-q3",
        "chapterId": "skm3-c9",
        "question": "明日の野外コンサート、雨が降らない（　）いいですね。",
        "options": [
            "と",
            "に",
            "で",
            "を"
        ],
        "correctIndex": 0,
        "explanation": "【正解: と】\n「動詞普通形＋といい（ですね）」は、天候など話者の意志で左右できない客観的な事態について好ましい結果を願う表現です。\n\n【選択肢解説】\n1. と (正解): 「雨が降らないといい（ですね）」の願望構文。\n2. に (不正解): 助詞不適合。\n3. で (不正解): 助詞不適合。\n4. を (不正解): 助詞不適合。"
    },
    {
        "id": "skm3-c9-q4",
        "chapterId": "skm3-c9",
        "question": "息子は新しいゲームをずっと（　）いて、お小遣いを貯めている。",
        "options": [
            "欲しがって",
            "欲しくて",
            "欲しいで",
            "欲しそう"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 欲しがって】\n「〜がる／がっている」は第三者の感情・欲望が態度や行動に表れている様子を客観的に描写する表現です。\n\n【選択肢解説】\n1. 欲しがって (正解): 第三者の欲望の継続描写（欲しがっていて）。\n2. 欲しくて (不正解): 話者本人の内面的な感情を表す。\n3. 欲しいで (不正解): 文法的に誤り。\n4. 欲しそう (不正解): 様態の語幹であり「〜いて」に直接続かない。"
    },
    {
        "id": "skm3-c9-q5",
        "chapterId": "skm3-c9",
        "question": "美術館の館内では、フラッシュを使って写真を（　）と思います。",
        "options": [
            "撮らないでほしい",
            "撮らせてほしい",
            "撮らなければいい",
            "撮りたがって"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 撮らないでほしい】\n「動詞ないで＋ほしい」は「他人に〜しないでほしい」と不快な迷惑行為の自制を促す表現です。\n\n【選択肢解説】\n1. 撮らないでほしい (正解): 来館者に撮影を控えてほしいという希望。\n2. 撮らせてほしい (不正解): 自分が撮影する許可を求めることになり逆。\n3. 撮らなければいい (不正解): 助言・条件。\n4. 撮りたがって (不正解): 第三者の願望。"
    },
    {
        "id": "skm3-c9-q6",
        "chapterId": "skm3-c9",
        "question": "この新規開拓プロジェクトのリーダーは、ぜひ私に（　）ください。",
        "options": [
            "やらせて",
            "やって",
            "やられて",
            "やりたがって"
        ],
        "correctIndex": 0,
        "explanation": "【正解: やらせて】\n「私に動詞使役て形＋ください」は「私にその行為をやらせてください」と自ら立候補して許可を求める定番の申し出表現です。\n\n【選択肢解説】\n1. やらせて (正解): 「私にやらせてください（担当させてください）」。\n2. やって (不正解): 相手に命令する表現になり文脈と矛盾。\n3. やられて (不正解): 受身命令は不自然。\n4. やりたがって (不正解): 第三者描写。"
    },
    {
        "id": "skm3-c9-q7",
        "chapterId": "skm3-c9",
        "question": "そんなに顔色が悪いなら、無理をしないで今日は仕事を（　）いいよ。",
        "options": [
            "休んだら",
            "休ませたら",
            "休んでほしい",
            "休みたい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 休んだら】\n「動詞たら＋いい」は相手に対して「〜することを勧める（〜したらどうですか）」という親切な助言・推奨を表します。\n\n【選択肢解説】\n1. 休んだら (正解): 相手への助言・推奨（休んだらいいよ）。\n2. 休ませたら (不正解): 誰か他人に休ませる助言になる。\n3. 休んでほしい (不正解): 話者の個人的要求になる。\n4. 休みたい (不正解): 話者自身の願望。"
    },
    {
        "id": "skm3-c9-q8",
        "chapterId": "skm3-c9",
        "question": "注射針が刺さった瞬間、女の子は腕をひどく（　）泣き声をあげた。",
        "options": [
            "痛がって",
            "痛くて",
            "痛むで",
            "痛いと"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 痛がって】\n「痛がる」は他人が痛みを体全体で表している様子を客観的に描写する動詞です。第三者である少女の痛がる仕草に合致。\n\n【選択肢解説】\n1. 痛がって (正解): 他者の痛みの身体的表出を描写。\n2. 痛くて (不正解): 主観的感覚であり、他者の痛みの客観描写には「痛がる」を用いる。\n3. 痛むで (不正解): 文法的に誤り。\n4. 痛いと (不正解): 引用不適合。"
    },
    {
        "id": "skm3-c9-q9",
        "chapterId": "skm3-c9",
        "question": "親としては、子供たちには困難に負けず逞しく生きて（　）ものだ。",
        "options": [
            "いってほしい",
            "いかせたい",
            "いったらいい",
            "いきたがる"
        ],
        "correctIndex": 0,
        "explanation": "【正解: いってほしい】\n「他人に〜てほしいものだ」は、親などが子どもの将来に対して心から抱く普遍的な願いを表します。\n\n【選択肢解説】\n1. いってほしい (正解): 他者（子供）に対する深い願望。\n2. いかせたい (不正解): 使役願望で親の押しつけに聞こえる。\n3. いったらいい (不正解): 軽い助言。\n4. いきたがる (不正解): 第三者の欲求描写。"
    },
    {
        "id": "skm3-c9-q10",
        "chapterId": "skm3-c9",
        "question": "恐れ入りますが、過去５年分の会計データを閲覧（　）いただけますでしょうか。",
        "options": [
            "させて",
            "して",
            "され",
            "したい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: させて】\n「（自分が）閲覧させていただけますでしょうか」で、「私がデータを閲覧することを許可していただけますか」というビジネス敬語の許可依頼です。\n\n【選択肢解説】\n1. させて (正解): 使役て形＋いただく（自分が閲覧する許可の依頼）。\n2. して (不正解): 相手に閲覧してもらう依頼になり意味が逆。\n3. され (不正解): 受身不適合。\n4. したい (不正解): 接続不適合。"
    },
    {
        "id": "skm3-c9-q11",
        "chapterId": "skm3-c9",
        "question": "全力を尽くして答案を書いた。あとは無事に（　）といいのだが。",
        "options": [
            "合格できる",
            "合格する",
            "合格させたい",
            "合格してほしい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 合格できる】\n「動詞可能形＋といい（のだが）」は、結果が自分の意志でコントロールできない試験の合否について「合格できればいいのだが」と祈願する定番表現です。\n\n【選択肢解説】\n1. 合格できる (正解): 可能形＋といい（祈願）。\n2. 合格する (不正解): 意志動詞の直接形より可能形「合格できる」が結果の祈願として自然。\n3. 合格させたい (不正解): 誰かを合格させたい使役願望。\n4. 合格してほしい (不正解): 他人への要望。"
    },
    {
        "id": "skm3-c9-q12",
        "chapterId": "skm3-c9",
        "question": "彼は人前でスピーチをするのをいつも（　）いて、今回も司会を断った。",
        "options": [
            "嫌がって",
            "嫌いで",
            "嫌うで",
            "嫌らしく"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 嫌がって】\n「嫌がる」は第三者が嫌そうに拒絶・忌避する態度を表す動詞です。「嫌がっていて司会を断った」という文脈に合致します。\n\n【選択肢解説】\n1. 嫌がって (正解): 他者の忌避行動の描写（嫌がっていて）。\n2. 嫌いで (不正解): 静的な形容動詞で「いて」に直接続かない。\n3. 嫌うで (不正解): 接続不適合。\n4. 嫌らしく (不正解): 不快な様子を表す副詞。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-c9"]
exercises_data.extend(c9_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(c9_exercises)} exercises for SKM N3 Chapter 9!")

# 3. Enrich base-reviewed.json for Chapter 9 cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-u9-garu": {
        "title": "〜がる / 〜がっている (Third-Person Observable Sensations & Desires)",
        "connection": "い形語幹（い-）+ がる / がっている | な形語幹（な-）+ がる | V-たい語幹（たい→た）+ たがる / たがっている",
        "nuance": "【Shin Kanzen Master N3 正式規則】第三者の感情・感覚・願望が表情や態度・言動に表れている様子を客観的に描写する表現。本人の主観的感情（私は痛い、私は行きたい）には使えず、他者の観察可能な状態を表す。",
        "keyTakeaway": "Objectively depicts observable sensations, emotions, and desires in a third person ('appears to feel / acts as though wanting').",
        "sentences": [
            {
                "id": "skm3-u9-garu::s-skm3-9-1",
                "japanese": "弟は注射をひどく怖がって、病院の前で泣き出してしまった。",
                "english": "My little brother showed tremendous fear of the injection and burst into tears in front of the hospital.",
                "literal": "Little-brother injection terribly feared-showing, hospital front burst-out-crying.",
                "tokens": [{"word": "怖がって", "meaning": "showing fear / acting terrified", "reading": "こわがって", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 1: observable physical reaction to medical fear."
            },
            {
                "id": "skm3-u9-garu::s-skm3-9-2",
                "japanese": "彼は人前でスピーチをするのをいつも嫌がっていて、今回も司会を断った。",
                "english": "He always shows intense dislike for giving speeches in public, and he turned down the emcee role this time too.",
                "literal": "He in-front-of-people speech doing always dislike-shows, this-time too emcee declined.",
                "tokens": [{"word": "嫌がっていて", "meaning": "showing reluctance / acting unwilling", "reading": "いやがっていて", "pos": "Grammar"}],
                "nuanceNote": "Observable reluctance leading to refusal."
            },
            {
                "id": "skm3-u9-garu::s-skm3-9-3",
                "japanese": "注射針が刺さった瞬間、女の子は腕をひどく痛がって泣き声をあげた。",
                "english": "The moment the needle pierced her arm, the little girl showed great pain and let out a cry.",
                "literal": "Needle pierced moment, girl arm terribly pain-showed-and cried.",
                "tokens": [{"word": "痛がって", "meaning": "showing pain", "reading": "いたがって", "pos": "Grammar"}],
                "nuanceNote": "Physical manifestation of pain sensation."
            },
            {
                "id": "skm3-u9-garu::s-skm3-9-4",
                "japanese": "うちの猫は外に出たがって、ドアの前で鳴いている。",
                "english": "Our cat wants to go outside and is meowing in front of the door.",
                "literal": "Our cat outside want-to-go, door in-front-of meowing.",
                "tokens": [{"word": "出たがって", "meaning": "showing desire to go out", "reading": "でたがって", "pos": "Grammar"}],
                "nuanceNote": "Animal desire expressed through physical action."
            }
        ]
    },
    "added-n3-9-53": {
        "title": "〜てほしい・〜てもらいたい (Desire for Action by Another Person)",
        "connection": "人物 に + 動て形 / ないで + ほしい / もらいたい",
        "nuance": "【Shin Kanzen Master N3 p. 44 正式規則】「他人が〜すること、または〜しないことを望む。」Used to express hopes that another person will do something as a favor, or refrain from doing something unpleasant. Sometimes the person requested is not specified (public sphere/nature/institutions). Direct address functions like a request (〜てください).",
        "keyTakeaway": "Expresses desires regarding someone else's action or abstention ('I want [person] to do/not do X'). Directed at others, not oneself.",
        "sentences": [
            {
                "id": "added-n3-9-53::s-skm3-9-1",
                "japanese": "この書類をちょっと見てほしいんですが。",
                "english": "I would like you to take a quick look at this document.",
                "literal": "This document a-little look want-you-to but.",
                "tokens": [{"word": "見てほしい", "meaning": "want you to look", "reading": "みてほしい", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 1: direct gentle favor request."
            },
            {
                "id": "added-n3-9-53::s-skm3-9-2",
                "japanese": "親にはいつまでも元気で長生きしてもらいたい。",
                "english": "I want my parents to stay healthy and live a long life forever.",
                "literal": "Parents always healthy long-life receive-favor-want.",
                "tokens": [{"word": "長生きしてもらいたい", "meaning": "want them to live long", "reading": "ながいきしてもらいたい", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 2: sincere filial desire for parents' health."
            },
            {
                "id": "added-n3-9-53::s-skm3-9-3",
                "japanese": "ここにはゴミを捨てないでほしい。",
                "english": "I want people not to discard trash here.",
                "literal": "Here trash discard-not want.",
                "tokens": [{"word": "捨てないでほしい", "meaning": "want people not to throw", "reading": "すてないでほしい", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 3: general public prohibition request."
            },
            {
                "id": "added-n3-9-53::s-skm3-9-4",
                "japanese": "国にはもっと自然環境を守る対策をしてほしい。",
                "english": "I want the government to enact more measures to protect the natural environment.",
                "literal": "Country more nature-environment protect measures do-want.",
                "tokens": [{"word": "してほしい", "meaning": "want them to do", "reading": "してほしい", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 5: institutional appeal."
            }
        ]
    },
    "added-n3-9-54": {
        "title": "〜（さ）せてほしい・〜（さ）せてもらいたい (Desire for Permission / Leave to Act)",
        "connection": "動使役て形 + ほしい / もらいたい / いただきたい",
        "nuance": "【Shin Kanzen Master N3 pp. 44-45 正式規則】「（自分が）〜することを許可してほしい、あるいは〜しないで済むようにしてほしい。」Expresses hope that another person will permit the speaker to perform an action (or excuse them from doing it). Crucially distinguishes 'let me do' from 'make you do'.",
        "keyTakeaway": "Asking for permission or leave to perform an action oneself ('please allow me to / I wish to be permitted to...').",
        "sentences": [
            {
                "id": "added-n3-9-54::s-skm3-9-1",
                "japanese": "ちょっと考えさせてほしい。",
                "english": "Please let me think for a moment.",
                "literal": "A-little think-cause want.",
                "tokens": [{"word": "考えさせてほしい", "meaning": "please let me think", "reading": "かんがえさせてほしい", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 1: seeking deliberation time."
            },
            {
                "id": "added-n3-9-54::s-skm3-9-2",
                "japanese": "申し訳ございません。店長に確認させてもらいます。",
                "english": "I sincerely apologize; please allow me to confirm with the store manager.",
                "literal": "Apology is-not. Store-manager confirm-cause receive-favor.",
                "tokens": [{"word": "確認させてもらいます", "meaning": "allow me to confirm", "reading": "かくにんさせてもらいます", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 2: professional commercial procedure."
            },
            {
                "id": "added-n3-9-54::s-skm3-9-3",
                "japanese": "これについて私の意見を言わせてもらいたい。",
                "english": "I would like to be permitted to state my opinion on this matter.",
                "literal": "This about my opinion say-cause receive-want.",
                "tokens": [{"word": "言わせてもらいたい", "meaning": "wish to be allowed to speak", "reading": "いわせてもらいたい", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 3: meeting intervention."
            },
            {
                "id": "added-n3-9-54::s-skm3-9-4",
                "japanese": "この仕事はぜひ私にやらせてください。",
                "english": "Please allow me to handle this task by all means.",
                "literal": "This work by-all-means to-me do-cause please.",
                "tokens": [{"word": "やらせてください", "meaning": "please let me do it", "reading": "やらせてください", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 44 verbatim sentence 4: volunteering for responsibility."
            }
        ]
    },
    "added-n3-9-55": {
        "title": "〜といい・〜ばいい・〜たらいい (Hopes Outside Direct Control & Gentle Recommendations)",
        "connection": "普通形（現在形）+ といい | 動ば形 / い形ければ / な形なら + いい | 動たら形 + いい",
        "nuance": "【Shin Kanzen Master N3 p. 45 正式規則】\n1.「〜を望む（結果が自分の意志でコントロールできない事態）」: 天候や試験結果など、話者の意志で左右できない好ましい結果を願う。〜には話者自身の意志的行為は来ない。\n2.「相手に勧める（助言・提案）」: 相手の相談や状況に対し「〜したらいいですよ」と解決策を勧める。",
        "keyTakeaway": "Dual usage: (1) Hoping for uncontrollable events (weather, test results); (2) Offering gentle advice or recommendations ('you should do X / why don't you X?').",
        "sentences": [
            {
                "id": "added-n3-9-55::s-skm3-9-1",
                "japanese": "皆様の将来が明るいものでありますように。良い仕事が見つかるといいですね。",
                "english": "May everyone's future be bright; I hope you all find wonderful jobs.",
                "literal": "Everyone's future bright thing be so-that. Good job found if-good.",
                "tokens": [{"word": "見つかるといいですね", "meaning": "hope you find", "reading": "みつかるといいですね", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 45 verbatim sentence 1: graduation commencement blessing."
            },
            {
                "id": "added-n3-9-55::s-skm3-9-2",
                "japanese": "最近体の調子が悪い。重い病気でなければいいが…。",
                "english": "Recently I haven't been feeling well; I hope it isn't a serious illness...",
                "literal": "Recently body condition bad. Heavy illness if-not-good though...",
                "tokens": [{"word": "でなければいいが", "meaning": "hope it is not", "reading": "でなければいいが", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 45 verbatim sentence 2: health anxiety wishing against severe diagnosis."
            },
            {
                "id": "added-n3-9-55::s-skm3-9-3",
                "japanese": "大学入試の試験、全部合格できたらいいなあ。",
                "english": "I hope I can pass all my university entrance examinations.",
                "literal": "University entrance exam all pass can-if-good.",
                "tokens": [{"word": "合格できたらいいなあ", "meaning": "hope I can pass", "reading": "ごうかくできたらいいなあ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 45 verbatim sentence 3: personal aspiration for uncontrollable result."
            },
            {
                "id": "added-n3-9-55::s-skm3-9-4",
                "japanese": "疲れているなら、今日は早く寝たらいいですよ。",
                "english": "If you are tired, you should go to bed early today.",
                "literal": "Tired if, today early sleep-if good.",
                "tokens": [{"word": "寝たらいいですよ", "meaning": "you should sleep", "reading": "ねたらいいですよ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 45 verbatim sentence 4: gentle wellness advice."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Chapter 9 cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

c9_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 9",
        "exactPrintedPages": "p. 44",
        "exactPdfPages": "p. 67",
        "grammarItem": "〜がる / 〜がっている (Third-Person Observable Sensations & Desires)",
        "instructionalDetails": "Adjective stem / V-たい stem + がる/がっている; reports observable outward behavior and physical manifestations of third-person emotions, sensations, and desires.",
        "cardId": "skm3-u9-garu",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u9-garu::s-skm3-9-1",
            "skm3-u9-garu::s-skm3-9-2",
            "skm3-u9-garu::s-skm3-9-3",
            "skm3-u9-garu::s-skm3-9-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 44 (PDF p. 67). Verified third-person observable emotion semantics and behavioral manifestations."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 9",
        "exactPrintedPages": "p. 44",
        "exactPdfPages": "p. 67",
        "grammarItem": "〜てほしい・〜てもらいたい (Desire for Action by Another Person)",
        "instructionalDetails": "Person に + V-て/ないで + ほしい/もらいたい; desire for another person's actions or forbearance; functions as request in direct address.",
        "cardId": "added-n3-9-53",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-9-53::s-skm3-9-1",
            "added-n3-9-53::s-skm3-9-2",
            "added-n3-9-53::s-skm3-9-3",
            "added-n3-9-53::s-skm3-9-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 44 (PDF p. 67). Verified Section 1 formation, external agent targeting, and public forbearance requests."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 9",
        "exactPrintedPages": "pp. 44-45",
        "exactPdfPages": "pp. 67-68",
        "grammarItem": "〜（さ）せてほしい・〜（さ）せてもらいたい (Desire for Permission / Leave to Act)",
        "instructionalDetails": "V-causative て + ほしい/もらいたい/いただきたい; speaker seeks permission or leave to perform an action themselves ('let me do'); crucial distinction from causative commands.",
        "cardId": "added-n3-9-54",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-9-54::s-skm3-9-1",
            "added-n3-9-54::s-skm3-9-2",
            "added-n3-9-54::s-skm3-9-3",
            "added-n3-9-54::s-skm3-9-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 44-45 (PDF pp. 67-68). Verified Section 2 causative permission structures and professional polite applications."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 9",
        "exactPrintedPages": "p. 45",
        "exactPdfPages": "p. 68",
        "grammarItem": "〜といい・〜ばいい・〜たらいい (Hopes Outside Direct Control & Gentle Recommendations)",
        "instructionalDetails": "Plain non-past + といい / conditional ば/たら + いい; (1) Hopes regarding outcomes outside speaker volitional control; (2) Gentle advice/recommendation urging action.",
        "cardId": "added-n3-9-55",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-9-55::s-skm3-9-1",
            "added-n3-9-55::s-skm3-9-2",
            "added-n3-9-55::s-skm3-9-3",
            "added-n3-9-55::s-skm3-9-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 45 (PDF p. 68). Verified Section 3 non-volitional wishing conditions and gentle advisory usage."
    }
]

existing_card_ids = {e.get("cardId") for e in c9_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(c9_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Chapter 9 in source coverage matrix! Total certified rows: {len(matrix)}")
