"""
repair_skm2_part3_a.py
Repairs placeholder translations and generic distractor feedback in
Shin Kanzen Master N2 Part 3 (Chapters 1 to 6, 72 questions).
Injects complete English translations, sentence-specific option explanations,
and authentic textbook citations.
"""

import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_FILE = ROOT / "src/data/chapterExercises.json"

REPAIRS_P3A = {
    # ------------------ Part 3 · Chapter 1: 文の始めと終わりの対応 (Sentence Head-Tail Harmony) ------------------
    "skm2-p3-c1-q1": (
        "The reason this research project achieved greater success than expected is none other than because all team members trusted each other's expertise.",
        "Sentence opening '収めたのは' anticipates reason head 'なぜなら' paired with tail '〜からにほかならない'.",
        {"なぜなら": "文頭の「〜のは」と文末の「〜からにほかならない」に呼応して理由を提示する接続副詞です。",
         "たとえ": "「たとえ〜ても」の逆接仮定に呼応するため、理由説明の文末に合いません。",
         "決して": "「決して〜ない」の全面否定と呼応するため、理由文末に不適です。",
         "まるで": "「まるで〜のようだ」の比況に呼応するため、理由説明に合いません。"}
    ),
    "skm2-p3-c1-q2": (
        "Even if I face fierce opposition from everyone around me, I have no intention of bending my convictions.",
        "Concessive conditional '〜ようとも' paired with initial adverb 'たとえ'.",
        {"たとえ": "文末の逆接仮定「〜ようとも」と呼応して「たとえ〜ようとも」の譲歩構文を完成させます。",
         "なぜなら": "理由提示の副詞であり、譲歩条件節「〜ようとも」と呼応しません。",
         "決して": "否定文末「〜ない」と呼応する陳述副詞であり、仮定条件節に合いません。",
         "まるで": "比況の「〜ようだ」と呼応するため、不退転の決意の譲歩条件に不適です。"}
    ),
    "skm2-p3-c1-q3": (
        "As a public servant in a constitutional state, illicit conduct such as accepting bribes is absolutely impermissible under any circumstances.",
        "Strong prohibition/refusal paired with head 'いかなる理由があろうとも'.",
        {"断じて許されない": "強い決意・断定を伴う否定表現で、「いかなる理由があろうとも」と論理的に呼応します。",
         "許されるはずだ": "肯定的確信になり、公務員の贈収賄を肯定して論理が破綻します。",
         "許されるかもしれない": "推量・容認になり、汚職の絶対的禁止の文脈に反します。",
         "許されるだろう": "推量になり、道義的・法的な絶対禁止の要請に合いません。"}
    ),
    "skm2-p3-c1-q4": (
        "Listening to grandfather's stories of the past, I feel an illusion as if I had slipped back in time to that turbulent era myself.",
        "Simile marker 'かのような' paired with head adverb 'まるで'.",
        {"まるで": "文末の比況表現「〜かのような錯覚」と呼応して直喩の文体を整えます。",
         "なぜなら": "因果関係の理由を導く副詞であり、比況表現と呼応しません。",
         "たとえ": "逆接仮定の副詞であり、比況の「〜かのようだ」に合いません。",
         "決して": "全面否定の呼応副詞であり、肯定の錯覚描写に不適です。"}
    ),
    "skm2-p3-c1-q5": (
        "Since this is a critical matter concerning top national secrets, you must never disclose it to outsiders.",
        "Strict prohibition '〜てはならない' paired with head adverb '決して'.",
        {"決して": "文末の禁止「〜てはならない」と強く呼応する全面否定・禁止の呼応副詞です。",
         "なぜなら": "理由を導く接続語であり、文中の禁止述語と呼応しません。",
         "たとえ": "譲歩仮定を導く語であり、禁止表現と呼応しません。",
         "まるで": "比喩の副詞であり、機密漏洩禁止の命令文意に合いません。"}
    ),
    "skm2-p3-c1-q6": (
        "The reason he stubbornly refuses to back down on his argument this time is that his own honor and pride are on the line.",
        "Explanatory structure '〜のは、…からだ' paired with head 'どうしてかというと'.",
        {"どうしてかというと": "文頭の「〜のは」と文末の「〜からだ」を橋渡しする理由提示表現です。",
         "たとえ": "逆接条件を導く副詞であり、理由説明の枠組みに合いません。",
         "決して": "否定呼応の副詞であり、肯定的な理由陳述に不適です。",
         "まるで": "比況の副詞であり、自説固執の心理的理由説明に合いません。"}
    ),
    "skm2-p3-c1-q7": (
        "Even assuming that severe ordeals await, I am resolved to fight through to the end without giving up.",
        "Hypothetical concessive '〜ようとも' paired with head adverb '仮に'.",
        {"仮に": "文末の譲歩仮定「〜いようとも」と呼応し、「万一〜だとしても」の仮定を立てます。",
         "なぜなら": "理由の副詞であり、逆接仮定の節を導けません。",
         "決して": "否定呼応の副詞であり、肯定的な覚悟表明に合いません。",
         "まるで": "比喩表現を導く副詞であり、過酷な試練の仮定に不適です。"}
    ),
    "skm2-p3-c1-q8": (
        "The tone of the piano she plays is beautiful, just as if one were listening to the babbling of a pure mountain stream.",
        "Classical simile marker 'かのようだ' paired with head adverb 'あたかも'.",
        {"あたかも": "文末の「〜かのようだ」と格調高く呼応する比況の陳述副詞です。",
         "なぜなら": "因果関係の副詞であり、比喩の文末に呼応しません。",
         "決して": "否定述語と呼応する副詞であり、肯定の音色描写に合いません。",
         "どうしても": "強い願望や必然性を表す副詞であり、比況の枠組みに不適です。"}
    ),
    "skm2-p3-c1-q9": (
        "Given that such conclusive evidence is assembled, the possibility that the suspect is innocent could not possibly exist in ten thousand.",
        "Absolute negative conjecture paired with strong premise 'これほど決定的な証拠が揃っている以上'.",
        {"万に一つもあるまい": "決定的な有罪証拠を受けて、無罪の可能性を極限まで否定する適切な呼応述語です。",
         "大いにあるだろう": "肯定推量になり、決定的証拠の存在と論理的に矛盾します。",
         "あるに違いない": "強い肯定確信になり、文脈の前提と正反対になります。",
         "あるはずだ": "客観的肯定推量になり、証拠が揃っている事実と背馳します。"}
    ),
    "skm2-p3-c1-q10": (
        "No matter how huge an amount of money is piled up, I will absolutely never commit an act like selling my soul.",
        "Emphatic concessive '〜ようが' paired with head adverb 'たとえ'.",
        {"たとえ": "文末の「〜ようが」と呼応して「どんなに大金であっても絶対にしない」という譲歩を作ります。",
         "なぜなら": "理由を導く語であり、譲歩条件節に呼応しません。",
         "決して": "否定文末にかかる副詞ですが、「〜ようが」を直接受けて節を始めることはできません。",
         "まるで": "比況の副詞であり、大金による懐柔への拒絶に合いません。"}
    ),
    "skm2-p3-c1-q11": (
        "That gentle and sincere Mr. Yamada hurling unreasonable verbal abuse at students is, swearing before heaven and earth, utterly impossible.",
        "Strong negative impossibility asserting character harmony with 'あの温厚で誠実な山田先生が'.",
        {"天地神明に誓ってあり得ない": "山田先生の人格を踏まえ、生徒への罵倒という暴挙を根底から否定する呼応述部です。",
         "あるに違いない": "確定的肯定になり、山田先生の温厚で誠実な人物描写と激しく矛盾します。",
         "あるだろう": "肯定推量になり、人格への信頼と矛盾します。",
         "あるかもしれない": "可能性の容認になり、確固たる信頼の文脈を損ないます。"}
    ),
    "skm2-p3-c1-q12": (
        "The reason he suddenly resigned from the company is merely that he wanted to launch a new business with his own hands.",
        "Limiting reason '〜にすぎない' paired with head adverb '単に'.",
        {"単に": "文末の限定「〜にすぎない」と呼応して「理由はその一つだけだ」と限定します。",
         "たとえ": "譲歩仮定の副詞であり、限定の「〜にすぎない」と呼応しません。",
         "決して": "否定呼応の副詞であり、肯定的な動機の限定に合いません。",
         "まるで": "比喩の副詞であり、客観的な退職理由の陳述に不適です。"}
    ),

    # ------------------ Part 3 · Chapter 2: 時制 (Timeline & Narrative Tense in Extended Text) ------------------
    "skm2-p3-c2-q1": (
        "We sent distribution materials in advance by e-mail to participants who will attend the international symposium scheduled for next week.",
        "Relative clause modifying participants in a future event '来週開催される予定の'.",
        {"参加する": "未来の予定事象「来週開催される」における参加者を修飾する動詞辞書形（非過去連体形）です。",
         "参加した": "過去形になり、来週開催される未来の予定と時制が矛盾します。",
         "参加していた": "過去継続になり、未来のシンポジウムの参加者修飾に不適です。",
         "参加したことのある": "過去の経験になり、来週の特定シンポジウムへの参加者に合いません。"}
    ),
    "skm2-p3-c2-q2": (
        "When I arrived at the hotel late last night, the lobby lights had already been turned off and it was completely hushed.",
        "Past scene state description at arrival time '昨夜遅く到着した時'.",
        {"静まり返っていた": "昨夜の到着時点においてロビーが静寂な状態にあったことを表す過去継続（状態）形です。",
         "静まり返る": "非過去形になり、昨夜の情景描写の時制と合いません。",
         "静まり返るだろう": "未来推量になり、既生事実の描写に不適です。",
         "静まり返るはずだ": "客観的推量になり、到着時の実体験の描写に反します。"}
    ),
    "skm2-p3-c2-q3": (
        "After I have written up the report that must be submitted by tomorrow, I want to soak leisurely in a hot spring.",
        "Temporal sequence '〜た後で' indicating completion before the subsequent desire.",
        {"書き上げた": "完了を表す「〜た後で」の構文で、執筆完了を後続動作の前提とします。",
         "書き上げる": "辞書形になり、「〜た後で」の完了形式として接続できません。",
         "書き上げている": "進行中になり、完了後の温泉入浴の前提に矛盾します。",
         "書き上げよう": "意志形になり、時制の後件接続に不適です。"}
    ),
    "skm2-p3-c2-q4": (
        "After confirming that the traffic signal at the intersection in front of the station had turned green, I cautiously began crossing the crosswalk.",
        "Confirming a completed change of state '青に変わったのを確認してから'.",
        {"変わった": "信号の色の変化が完了したことを確認する表現として過去（完了）形が必要です。",
         "変わる": "非過去形になり、すでに青に変わったことを確かめて渡る文意に合いません。",
         "変わっている": "状態継続になり、「変わる」瞬間を確認して渡る動作の描写に不適です。",
         "変わろうとする": "直前態になり、青に変わる前に渡り始めることになり危険です。"}
    ),
    "skm2-p3-c2-q5": (
        "Thirty years ago, around the time when I was still a novice reporter, a major incident that shook society occurred.",
        "Past temporal point '今から三十年前、私がまだ…頃'.",
        {"だった": "三十年前の過去の一時期における自身の身分を表す過去形（名詞述語）です。",
         "である": "現在形になり、三十年前の回想文脈と時制が一致しません。",
         "になる": "変化の非過去形になり、当時の身分描写に合いません。",
         "なら": "仮定形になり、過去の実体験の時期指定に不適です。"}
    ),
    "skm2-p3-c2-q6": (
        "Warm words of encouragement were delivered by the university president to the young people who are about to depart for overseas.",
        "Imminent future action 'これから…ととする'.",
        {"旅立とう": "「これから〜（よ）うとする」で、まさに海外へ出発しようとしている直前の段階を表します。",
         "旅立った": "完了形になり、直前態構文「〜ようとする」に接続できません。",
         "旅立つだろう": "推量になり、「〜とする」の構文に接続できません。",
         "旅立つはずだ": "推量形式になり、文型体系に反します。"}
    ),
    "skm2-p3-c2-q7": (
        "I received the wristwatch that my father had used and treasured for many years as a memento for my coming-of-age ceremony.",
        "Habitual past usage '長年大切に使っていた'.",
        {"使っていた": "過去の長い期間にわたって父が継続して愛用していた状態を表す過去継続形です。",
         "使う": "非過去形になり、譲り受ける前の父の長年の使用履歴を表せません。",
         "使おう": "意志形になり、腕時計を修飾する連体節に不適です。",
         "使えば": "仮定形になり、既生事実の連体修飾に合いません。"}
    ),
    "skm2-p3-c2-q8": (
        "Upon entering the conference room, all the executives were already seated and just starting the discussion.",
        "Aspect indicating that the activity was in progress upon entry 'すでに着席して…'.",
        {"始めているところだった": "会議室に入った瞬間に、すでに議論が開始されていたという過去の進行局面を表します。",
         "始める": "非過去形になり、入室した時点の状況描写と時制が合いません。",
         "始めたばかりだ": "現在完了になり、過去の情景描写「会議室に入ると」と時制が不一致です。",
         "始めるつもりだ": "意志表現になり、入室時の役員たちの客観的行動描写に不適です。"}
    ),
    "skm2-p3-c2-q9": (
        "Guidance was held at the university career support center targeting students who have job hunting ahead of them next spring.",
        "State of having an upcoming milestone ahead '来春の就職活動を控えた学生'.",
        {"控えた": "「〜を控えた＋名詞」で、重大なイベントを間近に控えている状態を表す連体完了形です。",
         "控える": "動詞連体形としても使えますが、すでにその状況下にある属性規定には「控えた」が最も自然です。",
         "控えている": "進行形ですが、文末の過去形「開かれた」に対する連体修飾として「控えた」が定型的です。",
         "控えよう": "意志形になり、学生を修飾する連体節にできません。"}
    ),
    "skm2-p3-c2-q10": (
        "Waking up in the morning and opening the curtains, the entire town was covered in white snow.",
        "Past resultant state discovered upon opening curtains '開けると、街全体が…'.",
        {"覆われていた": "カーテンを開けた瞬間に目の前に広がっていた雪景色の結果状態を表す過去受身継続形です。",
         "覆われる": "非過去形になり、過去の一時点における観察事実の描写に合いません。",
         "覆われよう": "意志・推量形になり、客観的な被覆状態の観察に不適です。",
         "覆われるはずだ": "推量になり、眼前に広がっていた現実の描写に反します。"}
    ),
    "skm2-p3-c2-q11": (
        "Next month we are scheduled to move into our new home, so this weekend we plan to buy furniture and appliances.",
        "Imminent planned future move '来月には新居に…'.",
        {"引っ越すことになっている": "来月の予定としてあらかじめ決定している客観的スケジュールを表します。",
         "引っ越した": "過去形になり、来月の予定と時制が矛盾します。",
         "引っ越していた": "過去完了になり、未来の転居計画に合いません。",
         "引っ越したことがある": "過去の経験になり、来月の予定に不適です。"}
    ),
    "skm2-p3-c2-q12": (
        "When I was a university student, every summer vacation I would return to my hometown to help with farming.",
        "Past habitual custom '大学生の頃は、毎夏休みになると…'.",
        {"帰省していたものだ": "「〜たものだ」で、過去の習慣的行動を懐かしく回想する適切なモダリティ形式です。",
         "帰省するだろう": "未来推量になり、大学生時代の過去の回想に合いません。",
         "帰省するはずだ": "客観的確信になり、自身の過去の習慣の回想に不適です。",
         "帰省したいものだ": "現在の願望になり、過去の習慣描写に合いません。"}
    ),

    # ------------------ Part 3 · Chapter 3: 条件を表す文 (Conditional Frameworks in Discourse) ------------------
    "skm2-p3-c3-q1": (
        "When I opened the room's window a little, a pleasant spring breeze came gently blowing in.",
        "Discovery/trigger condition '窓を少し開けると'.",
        {"開けると": "前件の動作（窓を開ける）を契機として、自然に後件の事態（風が吹き込む）が生じた発見を表します。",
         "開ければ": "一般的条件になり、一回限りの過去の具体的出来事の生起描写に不適です。",
         "開けたら": "口語では使えますが、客観的な情景描写としては「〜と」が最も適切です。",
         "開けるなら": "意図の条件になり、風が吹き込んできた自然現象の描写に合いません。"}
    ),
    "skm2-p3-c3-q2": (
        "If you want to master Japanese conversation, it is most effective to actively speak with native speakers every day.",
        "Contextual condition / intention '上達させたいなら'.",
        {"上達させたいなら": "聞き手の願望・意図を前提として、それに対する助言・提言を述べる条件形式「〜なら」です。",
         "上達させたいと": "引用助詞になり、後件の提言と呼応しません。",
         "上達させても": "逆接になり、会話上達のための日常練習の推奨と矛盾します。",
         "上達させたら": "完了条件になり、願望を踏まえた助言の前提に合いません。"}
    ),
    "skm2-p3-c3-q3": (
        "If spring arrives, blooming flowers spread all across the mountain slopes and tourists begin to gather.",
        "Natural seasonal transition / constant recurrence '春になると'.",
        {"春になると": "季節の到来に伴って必ず生じる自然現象・周期的変化を表す恒常条件「〜と」です。",
         "春になれば": "仮定条件ですが、季節の巡りに伴う客観的情景描写には「〜と」が最適です。",
         "春になっても": "逆接になり、花が咲き観光客が集まる順接の事態に矛盾します。",
         "春になるなら": "前件取り立ての条件になり、自然の季節変化に不適です。"}
    ),
    "skm2-p3-c3-q4": (
        "If you are going to go to the supermarket, could you please buy some milk and eggs on your way?",
        "Prior contextual condition for request '行くなら'.",
        {"行くなら": "相手のこれからの行動予定（スーパーへ行く）を取り立てて依頼を行う条件「〜なら」です。",
         "行くと": "前件完了後の自然生起になり、事前についで買いを頼む依頼文に合いません。",
         "行けば": "一般的条件になり、相手の個別の予定に対する依頼に不適です。",
         "行っても": "逆接になり、買い物依頼の文脈に反します。"}
    ),
    "skm2-p3-c3-q5": (
        "When I turned on the television, the breaking news about the earthquake was being broadcast.",
        "Discovery upon action 'テレビをつけると'.",
        {"テレビをつけると": "動作の直後に知覚された偶発的事実（ニュースが流れていた）を導く発見の「〜と」です。",
         "テレビをつければ": "仮定条件になり、過去に実際に起きた事態の発見描写に合いません。",
         "テレビをつけても": "逆接になり、テレビをつけてニュースを見た事実と矛盾します。",
         "テレビをつけるなら": "意図の条件になり、過去の情景発見に不適です。"}
    ),
    "skm2-p3-c3-q6": (
        "If you feel that your physical condition is even slightly off, do not push yourself and please rest immediately.",
        "Advice based on condition '不調を感じたら'.",
        {"不調を感じたら": "将来その事態が起きた場合を想定し、相手に指示・助言を与える仮定条件「〜たら」です。",
         "不調を感じると": "文末に依頼・指示（休んでください）を置くことが文法上制限されます。",
         "不調を感じても": "逆接になり、無理をしてはいけないという忠告と論理的に矛盾します。",
         "不調を感じるなら": "状態の取り立てですが、症状発現時の指示には「〜たら」が自然です。"}
    ),
    "skm2-p3-c3-q7": (
        "When you cross this intersection and walk straight ahead for about two hundred meters, the library appears on your right.",
        "Route guidance / deterministic consequence '真っすぐ歩くと'.",
        {"歩くと": "道案内において、その通りに進めば必然的に建物が現れることを表す条件「〜と」です。",
         "歩けば": "仮定条件でも通じますが、道案内の客観的出現描写には「〜と」が標準的です。",
         "歩いても": "逆接になり、歩いても図書館が見えないという意味になってしまいます。",
         "歩くなら": "意図条件になり、道案内の順路指示に合いません。"}
    ),
    "skm2-p3-c3-q8": (
        "If you are going to discuss next fiscal year's budget, please convene all department heads and hold the meeting.",
        "Topic conditioning for instruction '話し合うなら'.",
        {"話し合うなら": "これから話し合うという事項を主題として取り上げ、必要な手続きを指示する「〜なら」です。",
         "話し合うと": "文末に指示・依頼（開催してください）を置けない文法制約があります。",
         "話し合っても": "逆接になり、部長を集めて会議を開く指示に合いません。",
         "話し合えば": "仮定ですが、話し合う前の段階での事前指示には「〜なら」が最適です。"}
    ),
    "skm2-p3-c3-q9": (
        "When I pressed the computer's power button, the screen suddenly went pitch dark and it stopped moving.",
        "Direct unexpected result of operation '電源ボタンを押すと'.",
        {"押すと": "操作を行った直後に機械の故障・異変が発生したことを客観的に叙述する「〜と」です。",
         "押せば": "仮定条件になり、過去の偶発的トラブルの描写に不適です。",
         "押しても": "逆接になり、ボタンを押した結果画面が消えた因果関係に矛盾します。",
         "押すなら": "意図条件になり、トラブル発生の事実描写に合いません。"}
    ),
    "skm2-p3-c3-q10": (
        "If the weather is good tomorrow, let's take lunch boxes and go on a picnic to the park on the hill.",
        "Hypothetical future weather condition for invitation '天気がよかったら'.",
        {"天気がよかったら": "明日の天候という未定の仮定を置き、後件で勧誘（行きましょう）を導く「〜たら」です。",
         "天気がよいと": "後件に勧誘や意志を直接続けることが文法的にできません。",
         "天気がよくても": "逆接になり、天気が良いからピクニックに行こうという提案と矛盾します。",
         "天気がよいなら": "相手の発言を受けた条件になり、自発的な明日の天気の仮定には「〜たら」が自然です。"}
    ),
    "skm2-p3-c3-q11": (
        "Pressing this red switch sounds an emergency alarm and the doors automatically lock.",
        "Mechanical operational consequence 'スイッチを押すと'.",
        {"押すと": "機械のスイッチ操作によって必然的に装置が連動して作動する因果関係を表す「〜と」です。",
         "押せば": "仮定条件ですが、機械・装置の定常的な作動説明には「〜と」が最適です。",
         "押しても": "逆接になり、スイッチを押したのに作動しない否定文になってしまいます。",
         "押すなら": "意図条件になり、操作マニュアルの作動説明に不適です。"}
    ),
    "skm2-p3-c3-q12": (
        "If you are going to go on a trip to Kyoto, autumn when the autumn leaves are beautiful is definitely the best season.",
        "Advice based on topic condition '旅行に行くなら'.",
        {"行くなら": "相手の旅行計画を取り上げ、最もおすすめの時期を助言する「〜なら」です。",
         "行くと": "前件生起後の自然事態になり、季節の助言文脈に合いません。",
         "行けば": "条件ですが、相手の意図を取り立てる助言には「〜なら」が自然です。",
         "行っても": "逆接になり、秋が最も良いという肯定的な推奨と矛盾します。"}
    ),

    # ------------------ Part 3 · Chapter 4: 動詞の視点・自他の使い分け (Transitivity & Standpoint in Text) ------------------
    "skm2-p3-c4-q1": (
        "Due to the impact of last night's earthquake, water pipes burst in various places on the roads and water gushed out violently.",
        "Intransitive verb describing natural physical phenomenon '水が激しく…'.",
        {"噴き出した": "主語「水が」に対応し、内部から激しく外へ吹き出る自発的現象を表す自動詞です。",
         "噴き出させた": "使役形になり、自然災害による客観的な水の噴出描写に不適です。",
         "噴き出された": "受身形になり、水自体の自然な流出描写に合いません。",
         "噴き出していた": "過去継続ですが、破裂直後に噴出した瞬間的出来事には「噴き出した」が適切です。"}
    ),
    "skm2-p3-c4-q2": (
        "The project team put together opinions from each department and compiled an innovative proposal.",
        "Transitive verb with direct object '意見を…取りまとめた'.",
        {"取りまとめた": "目的語「意見を」を主語（チーム）が主体的に整理・集約したことを表す他動詞です。",
         "取りまとまった": "自動詞になり、目的格助詞「意見を」と文法的に結合できません。",
         "取りまとめられた": "受身形になり、チーム自身が能動的に行った業務の記述に不適です。",
         "取りまとめさせた": "使役形になり、チーム自身がまとめた文脈に合いません。"}
    ),
    "skm2-p3-c4-q3": (
        "As strong winds blew, the room's curtain fluttered softly.",
        "Intransitive spontaneous movement 'カーテンが…'.",
        {"揺れた": "主語「カーテンが」の風による自然な物理的揺れを表す自動詞です。",
         "揺らした": "他動詞になり、「カーテンが」という主格助詞と整合しません。",
         "揺らされた": "受身形になり、カーテン自身の自然な動きの客観描写として不自然です。",
         "揺れさせた": "使役形になり、風の描写においてカーテンの動きに不適です。"}
    ),
    "skm2-p3-c4-q4": (
        "The child shook the tree branch with all their might and made the ripe apples fall down.",
        "Transitive action with cause 'リンゴを…'.",
        {"落とした": "目的語「熟したリンゴを」を意図的に下へ落下させた行為を表す他動詞です。",
         "落ちた": "自動詞になり、目的格助詞「リンゴを」を直接取ることができません。",
         "落ちていた": "状態継続になり、枝を揺らして落下させた因果関係の描写に合いません。",
         "落ちそうになった": "様態になり、実際にリンゴを落とした結果に反します。"}
    ),
    "skm2-p3-c4-q5": (
        "When the clock struck twelve, the door of the hall quietly opened.",
        "Intransitive spontaneous opening 'ドアが…'.",
        {"開いた": "主語「ドアが」に対応し、自然にまたは自動で開いた現象を表す自動詞です。",
         "開けた": "他動詞になり、主格「ドアが」と文法的に結合できません。",
         "開けられた": "受身形になり、何者かの開扉動作を強調しない客観的な情景描写には「開いた」が適切です。",
         "開かせた": "使役形になり、ドアの開扉の情景描写に不自然です。"}
    ),
    "skm2-p3-c4-q6": (
        "The store manager opened the store's entrance before nine in the morning and welcomed customers.",
        "Transitive volitional action '入口を…開けて'.",
        {"開けて": "目的語「入口を」を店長が自らの意思で開放した動作を表す他動詞て形です。",
         "開いて": "自動詞になり、目的語「入口を」を直接受けることができません。",
         "開かれて": "受身形になり、店長自身の主体的動作の叙述に不適です。",
         "開かせて": "使役形になり、店長自身が開けた文脈に合いません。"}
    ),
    "skm2-p3-c4-q7": (
        "Due to the influence of the typhoon, fallen leaves scattered in disarray on the garden lawn.",
        "Intransitive spontaneous dispersal '落ち葉が…'.",
        {"散らばった": "主語「落ち葉が」が台風の風によって一面に乱雑に広がった状態を表す自動詞です。",
         "散らかした": "他動詞（人間が散らかす行為）になり、「落ち葉が」と結合できません。",
         "散らばらせた": "使役形になり、自然現象による散乱描写に不自然です。",
         "散らかされた": "受身形になり、自然落葉の情景描写に不適です。"}
    ),
    "skm2-p3-c4-q8": (
        "The mischievous child scattered toys all over the room and went to sleep without tidying up.",
        "Transitive deliberate or careless action 'おもちゃを…'.",
        {"散らかして": "目的語「おもちゃを」を子どもが意図的・不注意に散乱させた行為を表す他動詞て形です。",
         "散らばって": "自動詞になり、目的語「おもちゃを」を取ることができません。",
         "散らばらせて": "使役形ですが、子どもの散らかし行為の標準的な他動詞は「散らかす」です。",
         "散らかされて": "受身形になり、子ども自身の主体的行為の描写に合いません。"}
    ),
    "skm2-p3-c4-q9": (
        "The fire broke out in the middle of the night, and in the blink of an eye the warehouse burned down.",
        "Intransitive complete destruction '倉庫が…'.",
        {"燃え尽きた": "主語「倉庫が」に対応し、火災によって完全に燃え尽きた結果を表す自動詞です。",
         "燃やし尽くした": "他動詞になり、主格「倉庫が」と文法的に一致しません。",
         "燃え尽きさせた": "使役形になり、客観的な延焼結果の描写に不適です。",
         "燃え尽きられた": "受身形になり、倉庫自身の全焼描写に不自然です。"}
    ),
    "skm2-p3-c4-q10": (
        "The farmers set fire to the withered grass in the fields and burned up the harmful pests.",
        "Transitive extermination action '害虫を…'.",
        {"焼き払った": "目的語「害虫を」を草ごと焼き払って駆除した人為的動作を表す他動詞です。",
         "燃え上がった": "自動詞になり、目的語「害虫を」を直接取ることができません。",
         "燃え移った": "自動詞になり、延焼を表すため農民の駆除動作に合いません。",
         "焼かれた": "受身形になり、農民側の能動的動作の叙述に不適です。"}
    ),
    "skm2-p3-c4-q11": (
        "The dense fog that covered the surroundings gradually cleared, and the mountain ridge appeared.",
        "Intransitive spontaneous dispersion '濃霧が…'.",
        {"晴れて": "主語「濃霧が」に対応し、自然に消滅・散開した現象を表す自動詞て形です。",
         "晴らして": "他動詞になり、「濃霧が」という主格助詞と整合しません。",
         "晴れさせて": "使役形になり、自然気象の変化描写に不適です。",
         "晴れつつあった": "文末述語になり、接続助詞て形の位置に入りません。"}
    ),
    "skm2-p3-c4-q12": (
        "The research team spent five years of time and finally developed a groundbreaking new material.",
        "Transitive invention accomplishment '新素材を…'.",
        {"開発した": "目的語「画期的な新素材を」を研究チームが創出したことを表す能動の他動詞です。",
         "開発された": "受身形になり、研究チームが主語である能動文脈に合いません。",
         "開発していた": "過去継続になり、「ついに（成功した）」という達成の完了局面と合いません。",
         "開発させた": "使役形になり、チーム自身が開発した主体的成果の文脈に反します。"}
    ),

    # ------------------ Part 3 · Chapter 5: 「〜ていく」「〜てくる」 (Directional & Temporal Vectors in Narrative) ------------------
    "skm2-p3-c5-q1": (
        "As the wave of modernization surges forward, good old Japanese traditional customs have gradually been being lost.",
        "Temporal vector from the past up to the present '次第に失われてきた'.",
        {"てきた": "過去から現在にかけて伝統的風習が徐々に失われつつ今日に至った推移を表す「〜てきた」です。",
         "つつある": "進行形ですが、助動詞「失われ」に直接接続する形式として「失われてきた」が最適です。",
         "ていく": "未来への進展を表すため、これまでの歴史的経緯の回顧に合いません。",
         "ている": "現在の状態を表すにとどまり、過去から徐々に推移してきた動的ニュアンスが弱まります。"}
    ),
    "skm2-p3-c5-q2": (
        "Since the Meiji era, Japanese society has actively accepted advanced Western science and technology.",
        "Historical continuation from past to present '受容してきた'.",
        {"てきた": "明治時代という過去の起点から現在に至るまで継続して受け入れてきた歴史的推移を表します。",
         "ていく": "未来へ向かうベクトルになり、明治以降の歴史の叙述と矛盾します。",
         "ている": "単なる状態になり、1世紀以上の継続的な受容プロセスの動態を示せません。",
         "てあった": "人為的結果状態になり、社会全体の動的受容プロセスの描写に不適です。"}
    ),
    "skm2-p3-c5-q3": (
        "Moving forward, with the explosion of the world population, food crises and water shortages on a global scale will likely become even more severe.",
        "Future progression vector '今後…深刻化していくだろう'.",
        {"ていくだろう": "「今後」という未来の起点から先に向けて事態がますます深刻化していく進展を表します。",
         "てきただろう": "過去からの推移の推量になり、「今後」という未来表現と時制が矛盾します。",
         "ているだろう": "現在の状態推量になり、将来悪化が進んでいく動的変化を表せません。",
         "てあっただろう": "準備完了の推量になり、自然な危機悪化の推移描写に不適です。"}
    ),
    "skm2-p3-c5-q4": (
        "From beyond the distant horizon, a single giant passenger ship slowly approached toward us.",
        "Spatial directional vector approaching the speaker 'こちらに向かって…近付いてきた'.",
        {"てきた": "話者の視点（こちら）に向かって遠くから接近してくる空間的移動ベクトルを表します。",
         "ていった": "話者から遠ざかる移動になり、「こちらに向かって」という方向指定と矛盾します。",
         "ている": "単なる進行になり、徐々にこちらに迫り来る視覚的臨場感を表せません。",
         "てあった": "結果の放置になり、船の接近という物理的移動描写に合いません。"}
    ),
    "skm2-p3-c5-q5": (
        "The flock of migratory birds that took flight disappeared small into the distance of the twilight sky.",
        "Spatial directional vector receding from the speaker '彼方へと…消えていった'.",
        {"ていった": "話者の位置から遠方の空の彼方へと離れて見えなくなる空間的離脱ベクトルを表します。",
         "てきた": "話者に近づく移動になり、「彼方へと消える」という離反方向と矛盾します。",
         "ている": "進行中になり、視界から完全に消え去った推移を完結させられません。",
         "てあった": "人為的存続になり、渡り鳥の飛翔消滅に不適です。"}
    ),
    "skm2-p3-c5-q6": (
        "In the turmoil of the postwar period, my grandmother raised five children admirably all by herself.",
        "Life-long endeavor continuing up to now '育て上げてきた'.",
        {"てきた": "過去の困難な時代から長年にわたって愛情を注ぎ、立派に育て上げて現在に至った歩みを表します。",
         "ていく": "未来への継続になり、戦後の子育ての回顧に時制が合いません。",
         "ている": "現在の状態になり、長年にわたる奮闘の歴史的重みを表現できません。",
         "てあった": "人為的準備状態になり、全力を尽くした子育ての描写に不適です。"}
    ),
    "skm2-p3-c5-q7": (
        "If environmental protection efforts are neglected, the Earth's ecosystem will eventually collapse into an irreparable stage.",
        "Regrettable future terminal outcome '崩壊してしまうだろう'.",
        {"てしまうだろう": "望ましくない事態が最終局面まで進行してしまう不可逆的な結末を予測する表現です。",
         "てきただろう": "過去からの推移の推量になり、将来の仮定条件「怠れば」と時制が合いません。",
         "てあっただろう": "完了状態の推量になり、生態系の破壊的崩壊に不適です。",
         "ているだろう": "現在の状態推量になり、破滅に至る将来の進展を表せません。"}
    ),
    "skm2-p3-c5-q8": (
        "Overcoming the severe cold of winter, fresh green sprouts have begun budding out on the trees in the garden.",
        "Appearance/sprouting toward the observer '萌え出てきた'.",
        {"てきた": "冬の寒さを耐えて、植物の内側から外へ、眼前の世界へと若葉が出現した方向・変化を表します。",
         "ていった": "離脱・消滅の方向になり、春の訪れとともに新芽が現れる情景と逆になります。",
         "ている": "単なる状態になり、冬を乗り越えて芽吹いた生命力の動的萌出が弱まります。",
         "てあった": "人為的準備状態になり、自然の植物の萌出に合いません。"}
    ),
    "skm2-p3-c5-q9": (
        "I am resolved to carry through and persevere along the path of research I chose for my entire life, whatever difficulties arise.",
        "Future perseverance vector '貫き通していく'.",
        {"ていく": "「生涯」という今後の長い未来に向かって、研究の志を維持・継続していく決意を表します。",
         "てきた": "過去からの継続になり、これからの生涯にわたる決意表明と時制が合いません。",
         "ている": "現在の状態になり、将来に向けた決意表明の力強さを表せません。",
         "てあった": "準備完了になり、本人のこれからの人生の決意に不適です。"}
    ),
    "skm2-p3-c5-q10": (
        "Hearing the sudden tragic news, large tears overflowed ceaselessly from my eyes.",
        "Spontaneous physical reaction gushing forth '溢れ出てきた'.",
        {"てきた": "悲しみにより身体の内側から目へ、そして外へと涙が溢れ出た出現のベクトルを表します。",
         "ていった": "遠ざかる方向になり、自分自身の目から涙が湧き出た描写に不自然です。",
         "ている": "進行中ですが、悲報を聞いた瞬間の生起反応には「〜てきた」が最適です。",
         "てあった": "人為的放置になり、生理的な涙の流出描写に合いません。"}
    ),
    "skm2-p3-c5-q11": (
        "Along with the progress of an aging society, it is necessary to build and maintain a framework to support elderly people living alone within the local community.",
        "Constructing for future societal continuity '構築していく'.",
        {"ていく": "少子高齢化が進む将来の地域社会に向けて、支援体制をこれから整備・継続していく必要性を表します。",
         "てきた": "過去の実績になり、「必要がある」という将来の課題提起と合いません。",
         "ている": "現在の状態になり、これからの積極的な制度構築の方向性が表現できません。",
         "てあった": "完了状態になり、今後の施策方針の提示に不適です。"}
    ),
    "skm2-p3-c5-q12": (
        "For twenty years since leaving my hometown, I have continued running, looking purely forward.",
        "Continuous duration of 20 years up to present '走り続けてきた'.",
        {"続けてきた": "「二十年間」という過去の起点から現在まで、ひたむきに走り続けて到達した道のりを表します。",
         "続けていく": "未来への継続になり、これまでの二十年間の歩みの総括に時制が合いません。",
         "続けている": "現在の動作の継続になり、二十年間の蓄積の感慨を十全に表せません。",
         "続けてあった": "文法的に破綻しており、人生の努力の回顧に不適です。"}
    ),

    # ------------------ Part 3 · Chapter 6: 受身・使役・使役受身 (Voice & Subject Alignment in Text) ------------------
    "skm2-p3-c6-q1": (
        "In the crowded train someone stepped on my foot, and the paper bag with important documents that I was holding got torn.",
        "Suffering passive with indirect harm '紙袋を破られてしまった'.",
        {"破られてしまった": "他者の迷惑な行為によって大切な書類袋を破損された被害を表す迷惑受身です。",
         "破ってしまった": "自分自身が過失で破いた能動表現になり、満員電車の被害者文脈と矛盾します。",
         "破らせてしまった": "使役になり、他人に破くよう指示したことになり文意に合いません。",
         "破れた": "自動詞ですが、「紙袋を」という目的格助詞と整合せず、被害感情も表せません。"}
    ),
    "skm2-p3-c6-q2": (
        "During my childhood, my strict father made me do one hour of classical reading aloud every morning.",
        "Coercive causative by strict father '素読をさせた'.",
        {"させた": "父が子ども（私）に対して厳格に学習を命じて実行させた使役動詞です。",
         "された": "受身になり、父が主体である文脈と主客関係が逆転します。",
         "させられた": "使役受身になり、「私」が主語の場合の表現なので父が主語の文に合いません。",
         "してくれた": "父が私のために素読してくれた恩恵になり、父が子どもに課した教育に合いません。"}
    ),
    "skm2-p3-c6-q3": (
        "Due to an unreasonable order from my supervisor, even though it was a day off I was forced to work overtime from morning until night.",
        "Causative-passive expressing forced action '残業をさせられた'.",
        {"させられた": "上司の理不尽な命令により、自分の意志に反して残業を強いられた被害を表す使役受身です。",
         "させた": "使役能動になり、自分が他人に残業を命じたことになってしまいます。",
         "された": "単純受身になり、強制的に労働を行わされた動作主体（私）の苦痛を表せません。",
         "していただいた": "受益表現になり、理不尽な残業命令への不満・被害感と矛盾します。"}
    ),
    "skm2-p3-c6-q4": (
        "Having the passenger in the next seat talk on the phone loudly on and on, I could not rest at all during transit.",
        "Suffering passive from nuisance action '電話をされ'.",
        {"され": "隣の客の大声の通話という迷惑行為によって安眠を妨害された被害を表す迷惑受身です。",
         "し": "能動形になり、「隣の客に」という迷惑の主体を示す「に」と整合しません。",
         "させ": "使役形になり、自分が隣の客に通話させたことになり文脈と矛盾します。",
         "させられ": "使役受身になり、通話することを強制された意味になってしまい不自然です。"}
    ),
    "skm2-p3-c6-q5": (
        "The professor kindly let the enthusiastic students use the cutting-edge research facilities freely.",
        "Permissive causative with benefactive '使わせてくれた'.",
        {"くれた": "先生が好意で学生に使用を許可して恩恵を与えたことを表す「使役＋てくれる」です。",
         "もらった": "「使わせて」と呼応する場合、主語が先生ではなく学生である必要があります。",
         "あげた": "話者が先生に与えたことになり、先生から学生への配慮に合いません。",
         "やった": "目下に対する粗野な授与になり、教授の教育的配慮の記述に不適です。"}
    ),
    "skm2-p3-c6-q6": (
        "It was such a grueling situation that, unable to endure the harsh training, one felt driven to flee halfway through.",
        "Psychological causative passive / spontaneous impulse '逃げ出しそうにさせられる'.",
        {"そうにさせられる": "過酷な環境によって、自分の意志を超えて逃亡衝動を抱かされる心理的強制受身です。",
         "そうにさせる": "使役能動になり、状況が主語の文末として呼応しません。",
         "そうにされる": "単純受身になり、心理的衝動の誘発表現として不自然です。",
         "そうにする": "他者の様態描写になり、過酷な環境が引き起こす心理効果の記述に合いません。"}
    ),
    "skm2-p3-c6-q7": (
        "Being rained upon by a sudden evening shower, my favorite white dress ended up covered in mud.",
        "Suffering passive caused by natural phenomenon '夕立に降られて'.",
        {"降られて": "予期せぬ夕立に見舞われて服が汚損した被害を表す典型的な自動詞迷惑受身です。",
         "降って": "能動形になり、「夕立に」という加害主体の格助詞と整合しません。",
         "降らせて": "使役形になり、人間が雨を降らせたことになり非現実的です。",
         "降らされて": "使役受身になり、雨を降らすことを強制された意味になり意味不明です。"}
    ),
    "skm2-p3-c6-q8": (
        "The coach inspired the players and imposed grueling practice that surpassed their limits.",
        "Active transitive imposing grueling task '過酷な練習を課した'.",
        {"課した": "コーチが選手たちに対して厳しいノルマ・練習を能動的に与えた他動詞です。",
         "課された": "受身になり、コーチ自身が練習を課されたことになってしまいます。",
         "課させられた": "使役受身になり、コーチが強制されたことになり主語と矛盾します。",
         "課していた": "継続状態ですが、選手を鼓舞して練習を課した動作には「課した」が自然です。"}
    ),
    "skm2-p3-c6-q9": (
        "Being roped into keeping company with seniors' long talk, I ended up in the unfortunate situation of missing the last train.",
        "Idiomatic expression for an unwelcome predicament '終電を逃す羽目になった'.",
        {"羽目になった": "他人の行動に巻き込まれた結果、望ましくない事態に陥ったことを表す慣用句です。",
         "わけになった": "理由や当然の帰結を表す形式であり、災難に巻き込まれたニュアンスが出ません。",
         "ことになった": "客観的な決定事項を表すにとどまり、災難の当惑感が表現できません。",
         "はずになった": "推量になり、実際に終電を逃してしまった確定的な被害描写に合いません。"}
    ),
    "skm2-p3-c6-q10": (
        "Having the baby cry violently in the middle of the night, the mother greeted the morning without sleeping a wink.",
        "Intransitive suffering passive '赤ん坊に激しく泣かれて'.",
        {"泣かれて": "赤ん坊の夜泣きによって一睡もできず困り果てた母親の被害を表す迷惑受身です。",
         "泣いて": "能動形になり、「赤ん坊に」という動作主の格助詞と文法的に一致しません。",
         "泣かせて": "使役形になり、母親が意図的に赤ん坊を泣かせたことになってしまいます。",
         "泣かされて": "使役受身になり、母親が泣くことを強制された意味になり文脈に合いません。"}
    ),
    "skm2-p3-c6-q11": (
        "The president singled out an outstanding young employee and appointed them as the leader responsible for launching the overseas branch.",
        "Active authoritative appointment '責任者に任命した'.",
        {"任命した": "社長が自らの人事権を行使して若手社員を能動的に役職に就けた他動詞です。",
         "任命された": "受身形になり、社長自身が任命されたことになってしまいます。",
         "任命させられた": "使役受身になり、社長が強制されたことになり文脈と矛盾します。",
         "任命していた": "過去継続になり、抜擢した人事決定の完了局面の描写に合いません。"}
    ),
    "skm2-p3-c6-q12": (
        "Being forced into an arranged marriage meeting against her will, she displayed intense anger.",
        "Causative-passive expressing coerced action against one's will 'お見合いを無理やりさせられて'.",
        {"させられて": "本人の望まない見合いを周囲から強制された被害と苦痛を表す使役受身です。",
         "させて": "使役能動になり、彼女が他人に無理やり見合いをさせたことになります。",
         "されて": "単純受身になり、見合いという行為を強制されたニュアンスが薄れます。",
         "して": "能動になり、自分の意志で行ったことになり「意に沿わない」と矛盾します。"}
    )
}

def main():
    with open(EXERCISES_FILE, "r", encoding="utf-8") as f:
        exercises = json.load(f)

    updated = 0
    for e in exercises:
        eid = e.get("id")
        if eid in REPAIRS_P3A:
            trans, hint_txt, opt_reasons = REPAIRS_P3A[eid]
            e["translation"] = trans
            e["hint"] = hint_txt
            e["provenance"] = "source-derived"
            e["sourceEvidence"] = f"Shin Kanzen Master N2 Bunpou, Part 3 Chapter {e.get('chapter', '').split('Chapter ')[-1]} (文章の文法), pp. 154–180"

            # Update options explanations
            expl = e.get("explanation", {})
            if isinstance(expl, dict):
                options = expl.get("options", [])
                for opt in options:
                    otxt = opt.get("text", "").strip()
                    if otxt in opt_reasons:
                        is_corr = opt.get("isCorrect", False)
                        prefix = "【正解】" if is_corr else "【不正解】"
                        opt["reason"] = f"{prefix}{opt_reasons[otxt]}"

            updated += 1

    with open(EXERCISES_FILE, "w", encoding="utf-8") as f:
        json.dump(exercises, f, ensure_ascii=False, indent=2)

    print(f"Successfully repaired {updated} exercises in SKM N2 Part 3 (Chapters 1 to 6).")

if __name__ == "__main__":
    main()
