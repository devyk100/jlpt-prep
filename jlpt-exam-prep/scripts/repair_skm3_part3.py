import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

# Load questions from dump
dump = json.load(open(ROOT / "scratch/skm3_part3_dump.json", encoding="utf-8"))

# Dictionary of semantic repairs for all 108 questions in SKM N3 Part 3 (Chapters 2 to 10)
REPAIRS_P3 = {}

# ---------------------------------------------------------------------------
# Chapter 2: 時制・〜ている (Tense & Aspect) - pp. 118–121
# ---------------------------------------------------------------------------
ch2_data = [
    ("skm3-p3-c2-q1", 
     "When the train arrived at the station, a large crowd of passengers was waiting on the platform.",
     "ホーム上の過去時点での継続状態の描写。",
     {"待つ": "非過去の辞書形は未来や習慣を表すため、過去の到着時の継続情景に合いません。",
      "待とう": "話者の意志・勧誘形であり、第三者である乗客の客観的状態の描写に反します。",
      "待てば": "仮定条件形であり、文末を締めくくる主節述語になれません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q2",
     "Before coming to Japan, I mastered basic hiragana and katakana in advance.",
     "前項動作の未完了を表す辞書形接続（〜前に）。",
     {"来た": "「〜前に」の前は動作がまだ実現していないため過去形タ形は接続できません。",
      "来ている": "状態継続形であり、「来る」という移動の未完了時点を示す形になりません。",
      "来よう": "意志形であり、時間を規定する「前に」に直接接続できません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q3",
     "After arriving in Japan, I toured ancient temples in Kyoto and Nara.",
     "前項動作の完了を表すタ形接続（〜後で）。",
     {"来る": "「〜後で」の前は先行動作がすでに完了しているため辞書形は不適切です。",
      "来ている": "現在進行・状態を表す形であり、完了動作を前提とする「後で」に合いません。",
      "来れば": "仮定条件形であり、確定した過去の事実順序を導く接続になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q4",
     "When I looked outside the window, snow was quietly continuing to fall.",
     "観察時点において目の前に広がっていた継続状態。",
     {"降り続く": "非過去形はこれからの事態を示し、過去の知覚時点（見ると）の情景と時制が衝突します。",
      "降り続くはずだ": "客観的推量・確信表現であり、直接目撃した視覚的描写に合いません。",
      "降り続くだろう": "主観的推量表現であり、目の前の事実目撃の描写には不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q5",
     "While waiting for a friend at the cafe, I read through one entire book.",
     "継続的動作・期間を表す接続（〜間に）。",
     {"待った": "「間に」の前は継続中の状態を表す必要があるため、瞬間完了のタ形は不適切です。",
      "待とう": "意志形であり、期間を示す「間に」に接続できません。",
      "待てば": "条件形であり、時間の幅を示す副詞節を作れません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q6",
     "When I returned home, dinner was already completely prepared and placed on the table.",
     "帰宅時にすでに出来上がっていた結果状態の描写。",
     {"できる": "非過去形はこれから完成することを意味し、「すでに」と過去の事態に矛盾します。",
      "できよう": "意志・推量形であり、目の前に存在する料理の描写に合いません。",
      "できれば": "仮定条件形であり、文末の叙述述語になり得ません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q7",
     "While listening to the professor's lecture, I took detailed notes in my notebook.",
     "主動作と並行して行われる付帯動作（〜ながら）。",
     {"聞きながら": "正解です（マス形語幹＋ながら）。",
      "聞くながら": "「ながら」は動詞マス形語幹に接続するため、辞書形接続は文法的に破綻します。",
      "聞いたながら": "過去形タ形に「ながら」を接続することはできず非文です。",
      "聞いているながら": "進行形テイル形に「ながら」を接続することはできず文法誤りです。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q8",
     "When I woke up this morning, the morning sun was brilliantly shining.",
     "起床した過去の瞬間における継続状態描写。",
     {"輝く": "非過去基本形は未来や習慣を表すため、過去の目撃時点の情景描写になりません。",
      "輝こう": "意志形であり、自然現象の太陽の客観描写に反します。",
      "輝けば": "条件形であり、過去の完了した文を締めくくる述語になれません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q9",
     "Before going to bed, I always make sure to drink a glass of warm water.",
     "就寝前の習慣的行動における辞書形接続（〜前に）。",
     {"寝た": "「前に」の直前は動作未完了のため、完了過去のタ形は使えません。",
      "寝ている": "状態継続形であり、就寝という動作の直前を示す形になりません。",
      "寝よう": "意志形であり、時間の先行関係を表す「前に」に直接接続できません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q10",
     "After finishing work, I plan to stop by the gym for light exercise.",
     "先行動作の完了を表すタ形接続（〜後で）。",
     {"終わる": "「後で」の前は先行動作が完了している必要があるため、辞書形は接続できません。",
      "終わっている": "結果状態を表す形であり、「完了した直後」の順序関係を規定する形として不自然です。",
      "終われば": "仮定条件形であり、確定的な時間の後続関係を表す文末に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q11",
     "The moment I opened the door, a pleasantly refreshing breeze blew into the entranceway.",
     "直前先行動作の完了（〜た瞬間）。",
     {"開ける": "「瞬間」の直前でドアを開ける動作が完了しているため、非過去辞書形は使えません。",
      "開けている": "動作の途中にあり、開放が完了した瞬間という時間的ピンポイントに合いません。",
      "開けよう": "意志形であり、物理的出来事の継起関係を表す「瞬間」に接続できません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121"),

    ("skm3-p3-c2-q12",
     "Just as I was about to go out, rain suddenly began to pour down in torrents.",
     "外出の直前段階を表す形式（〜ようとした時）。",
     {"出かけた": "「出かけた時」だとすでに外に出ていることになり、「出かけようとした時（直前）」の意図とずれます。",
      "出かける": "直前の意志・切迫感を表す「〜ようとする」の構文になりません。",
      "出かけている": "外出中の状態継続になり、降雨に邪魔されて出かけられなかった文脈に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 2 (時制・〜ている), pp. 118–121")
]

for qid, trans, ctx, opt_map, evid in ch2_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 3: 自他動詞 (Transitive & Intransitive Verbs) - pp. 122–123
# ---------------------------------------------------------------------------
ch3_data = [
    ("skm3-p3-c3-q1",
     "A strong wind blew through, and a large branch of the tree in the garden broke.",
     "自然現象による客観的破損（主格「枝が」）。",
     {"折った": "他動詞（人間による意図的破壊）であり、「枝が」という自然発生の主格に合いません。",
      "折らせた": "使役形であり、「風が人に折らせた」という不自然な文脈になります。",
      "折れさせた": "自動詞の使役形で、不要な強制・許可のニュアンスが生じ不自然です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q2",
     "During the major cleanup, my hand accidentally slipped and I ended up breaking a precious vase.",
     "人為的過失による破損（目的格「花瓶を」）。",
     {"割れて": "自動詞であり、助詞「を」を伴う直接目的語をとることができません。",
      "壊れて": "自動詞であり、「花瓶を壊れてしまった」という格支配にならず非文です。",
      "倒れて": "自動詞であり、「花瓶を」という他動詞目的格に接続できません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q3",
     "In order to air out the room, I opened the window wide.",
     "意図的な換気動作（目的格「窓を」）。",
     {"開いた": "自動詞であり、「窓を」という他動詞目的語をとることができません。",
      "開かれた": "受身形であり、話者自身が主語となって意図的に行う能動文節に合いません。",
      "開けさせた": "使役形であり、自分が開ける文脈で「誰かに開けさせた」とするのは不適です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q4",
     "When you press the button, the front door opens automatically.",
     "機械の自動的・無意志的動作（主格「ドアが」）。",
     {"開ける": "他動詞であり、「ドアが」という主格に対して他動詞を用いると格衝突を起こします。",
      "開けられる": "可能形または受身形であり、機械が自然に開く無意志動作の記述に合いません。",
      "開かせる": "使役形であり、ドアに対して使役を命じるのは不自然です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q5",
     "I noticed that the strap of my bag had snapped, so I took it in for repair.",
     "自然発生的な破損状態（主格「ひもが」）。",
     {"切った": "他動詞（刃物等で意図的に切断する）であり、自然に切れていた文脈に合いません。",
      "切られた": "受身形（他人に切られた）であり、経年劣化による自然破損の描写に合いません。",
      "切らせた": "使役形であり、話者が誰かに切らせた意味になり破綻します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q6",
     "With scissors, I carefully cut the wrapping ribbon to just the right length.",
     "ハサミを用いた意図的切断（目的格「リボンを」）。",
     {"切れた": "自動詞であり、助詞「を」を伴う目的語「リボンを」をとることができません。",
      "切れさせた": "使役形であり、自分がハサミで切る単純な動作に対して過剰です。",
      "切られた": "受身形であり、話者が能動的に長さを整える文脈に反します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q7",
     "Because a traffic accident occurred, the movement of vehicles on the expressway came to a halt.",
     "事故による客観的停止（主格「動きが」）。",
     {"止めた": "他動詞であり、「動きが」という自動詞主格に他動詞を直接結ぶと非文になります。",
      "止められた": "受身形であり、車の流れが止まった客観的交通状況の記述に合いません。",
      "止まらせた": "使役形であり、事故が意図的に止まらせたような擬人化になり不自然です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q8",
     "The police officer raised their hand and halted oncoming cars.",
     "警察官による意図的制止（目的格「車を」）。",
     {"止まった": "自動詞であり、「車を」という直接目的格をとることができません。",
      "止まられた": "迷惑受身形になり、警察官が能動的に交通整理を行う文脈に矛盾します。",
      "止まらせた": "使役形であり、通常の交通整理動作「車を止めた」よりも不自然に回りくどい表現です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q9",
     "Because of an electrical outage, the room lights went out all at once.",
     "停電による客観的消灯（主格「電気が」）。",
     {"消した": "他動詞（人間がスイッチを切って消す）であり、「電気が」という自然消滅に合いません。",
      "消された": "受身形であり、他者によって消された文脈ではなく停電が原因であるため不適です。",
      "消えさせた": "使役形であり、停電が電気に消えさせたという不自然な表現になります。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q10",
     "Before going to sleep, I made sure to turn off all the lights in the room.",
     "就寝前の意図的消灯動作（目的格「電気を」）。",
     {"消えた": "自動詞であり、「電気を」という目的格助詞をとることができません。",
      "消えられた": "迷惑受身形であり、自分で確認して消す積極的行動に反します。",
      "消えさせた": "使役形であり、「電気を消した」という直接動作に対して不自然です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q11",
     "The heavy iron gate in the courtyard had begun to rust over the years and had become ruined.",
     "自然劣化による破損状態（主格「門が」）。",
     {"壊した": "他動詞（誰かが故意・過失で壊す）であり、「門が壊れた」自然損耗に合いません。",
      "壊された": "受身形（他人に壊された）であり、経年劣化の文脈に反します。",
      "壊れさせた": "使役形であり、主語「門が」と使役述語の意味関係が破綻します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123"),

    ("skm3-p3-c3-q12",
     "I dropped my smartphone onto the concrete pavement and broke the screen.",
     "落下による過失破壊（目的格「画面を」）。",
     {"壊れた": "自動詞であり、「画面を」という他動詞目的格助詞をとることができません。",
      "壊れさせた": "使役形であり、通常の過失動作「壊してしまった」に比べて極めて不自然です。",
      "壊された": "受身形であり、自分が落として壊した文脈で他者に壊されたことになり破綻します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 3 (自他動詞), pp. 122–123")
]

for qid, trans, ctx, opt_map, evid in ch3_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 4: 〜ていく・〜てくる (Directional & Temporal Progression) - pp. 124–127
# ---------------------------------------------------------------------------
ch4_data = [
    ("skm3-p3-c4-q1",
     "From the summit of the mountain, a flock of birds flew away toward the distant city.",
     "話者の位置（山頂）から遠方へ離れていく移動（飛んでいった）。",
     {"きた": "接近を表す補助動詞であり、山頂から遠くの街へ離れる動きに矛盾します。",
      "こなかった": "否定過去形であり、実際に鳥が飛び去った客観描写に合いません。",
      "きそうだ": "様態推量であり、目の前の過去の実際の飛行行動の記述になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q2",
     "From the distant horizon, a single ship came approaching toward here.",
     "遠方から話者のいる視点位置へ接近する移動（近づいてきた）。",
     {"いった": "遠ざかる移動を表すため、「こちらに向かって」という接近の向きに矛盾します。",
      "いかない": "否定現在形であり、接近してきた確定事実の叙述になりません。",
      "いくだろう": "推量形であり、目撃された船の接近の客観描写に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q3",
     "It was a clear blue sky until a moment ago, but dark clouds suddenly began to spread and it turned dark.",
     "過去から現在・変化の出現へ向けて生じる推移（暗くなってきた）。",
     {"暗くなっていった": "話者の観察視点から遠ざかる変化になり、急激に目の前が暗くなる臨場感に合いません。",
      "暗くならなかった": "暗くなった事実と直接矛盾する否定形です。",
      "暗くなりそうだ": "直前の推量形であり、すでに暗くなった結果描写に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q4",
     "From now into the future, global environmental problems are predicted to grow increasingly severe.",
     "現在から未来へ向けて進行していく推移（深刻化していく）。",
     {"深刻化してきた": "過去から現在までの蓄積を表すため、「これからの将来」という未来予測に矛盾します。",
      "深刻化してこない": "否定形であり、問題悪化を警告する文脈と真逆になります。",
      "深刻化してこよう": "不自然な使役推量複合で非文です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q5",
     "The Japanese language skills that I have studied diligently up until now will surely be useful.",
     "過去から現在に至るまでの学習の継続・蓄積（勉強してきた）。",
     {"勉強していった": "基準点から未来・遠方へ離れる表現であり、「これまで」の蓄積に合いません。",
      "勉強していかない": "否定表現であり、これまでの努力の継続事実と矛盾します。",
      "勉強していくはずだ": "未来に向けた推量であり、「これまで」という過去の継続事実に反します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q6",
     "Even after entering the workforce, I intend to continue studying foreign languages.",
     "未来に向けて継続していく意志（勉強し続けていく）。",
     {"勉強し続けてきた": "過去から現在までの完了を表すため、「社会人になってからも」という未来計画に反します。",
      "勉強し続けてこない": "否定形であり、継続の決意と矛盾します。",
      "勉強し続けてこよう": "不自然な意志複合形であり、未来への継続意欲に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q7",
     "Having caught a cold, around evening my throat started hurting and I began to develop a fever.",
     "身体的症状・変化の出現（熱が出てきた）。",
     {"出ていった": "熱が体から抜け出て消失した意味になり、高熱で苦しむ文脈と真逆になります。",
      "出なかった": "発熱しなかったことになり、風邪が悪化した文脈と矛盾します。",
      "出そうだ": "直前の兆候推量であり、夕方に実際に熱が出た確定叙述に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q8",
     "With the rapid spread of smartphones, traditional public telephone booths have gradually vanished from the streets.",
     "過去から現在にかけて消失していった推移（消えていった）。",
     {"消えてきた": "「消える」という消失動詞に「〜てくる」をつけると出現のニュアンスと衝突します。",
      "消えてこなかった": "公衆電話が現在も減っていないことになり、社会事実と矛盾します。",
      "消えてきそうだ": "未来の推量形であり、すでに過去から減少した事実の叙述になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q9",
     "I brought a famous local souvenir pastry from my hometown and distributed it to everyone in the office.",
     "離れた場所から話者のいる現在地へ携えて移動（持ってきた）。",
     {"持っていった": "話者のいる場所から外部へ運び去る表現であり、オフィスで配る文脈に合いません。",
      "持ってこなかった": "持ってこなかったら配ることができないため論理矛盾です。",
      "持っていくだろう": "未来の推量であり、すでに配った過去の動作に反します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q10",
     "Because it is going to rain tomorrow, make sure to take your umbrella with you when leaving.",
     "話者のいる現在地から外出先へ携えて移動（持っていきなさい）。",
     {"持ってきなさい": "話者のいる場所へ持参させる指示になり、外出先へ持たせる指示に反します。",
      "持ってこないで": "傘を持たないよう指示することになり、降雨への配慮と矛盾します。",
      "持っていかないで": "傘を持たずに濡れさせる指示になり文脈に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q11",
     "Recently, the temperature has gradually dropped, and chilly days have increased.",
     "過去から現在にかけて冷え込みが顕在化してきた推移（寒くなってきた）。",
     {"寒くなっていった": "観察者の視点から遠ざかる表現になり、現在の寒さの実感に合いません。",
      "寒くならなかった": "温暖なままであったことになり、「肌寒い日が増えた」と矛盾します。",
      "寒くなりそうだ": "これからの推量であり、すでに寒い日が増えている現状描写に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127"),

    ("skm3-p3-c4-q12",
     "As societies continue to age in the future, the working population will decline progressively.",
     "未来に向けて減少が継続していく推移（減少していくだろう）。",
     {"減少してきただろう": "過去の推量になり、「今後高齢化が進むにつれて」という未来予測に反します。",
      "減少してこないだろう": "人口が減少しない推量になり、少子高齢化の社会予測と矛盾します。",
      "減少してきたはずだ": "過去の完了事実に対する確信になり、未来の予測に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 4 (〜ていく・〜てくる), pp. 124–127")
]

for qid, trans, ctx, opt_map, evid in ch4_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 5: 受身・使役・使役受身 (Voice & Viewpoint Consistency) - pp. 128–129
# ---------------------------------------------------------------------------
ch5_data = [
    ("skm3-p3-c5-q1",
     "Inside the crowded train, someone stepped on my foot, and it hurt so much I couldn't even make a sound.",
     "見知らぬ他者から被害を受けた迷惑受身（足を踏まれて）。",
     {"せて": "使役形であり、「自分が他人に足を踏ませた」という不条理な意味になります。",
      "させられて": "使役受身形であり、他人に強制されて足を踏んだ意味になり誤りです。",
      "られて": "五段動詞「踏む」の受身形は未然形「踏ま」＋「れる」であり、「踏まられて」は文法破綻です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q2",
     "When I was a child, my mother forced me to eat vegetables I hated every day, which I truly disliked.",
     "親から強制されて不本意に行わされた使役受身（食べさせられて）。",
     {"させて": "能動使役形であり、「母に野菜を食べさせて」自分が親に食べさせた意味になり破綻します。",
      "られて": "単純受身形であり、母から食べることを強制された不本意のニュアンスが出ません。",
      "て": "単純テ形であり、強制と苦痛の感情を表す文脈に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q3",
     "Because the president suddenly took ill, the executive managing director was made to take charge of the shareholder meeting.",
     "組織上の不可避な事情で代理を務めさせられた使役受身（務めさせられた）。",
     {"務められた": "尊敬または可能受身であり、社長不在に伴う強制・代理任務の使役性が落ちます。",
      "務めさせた": "他動使役形であり、専務が他人に務めさせたことになり文意が逆転します。",
      "務めていた": "単なる状態継続であり、急遽役目を負わされた受動的経緯を表せません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q4",
     "During the examination, when the supervisor stared right at me from next to my desk, I became nervous.",
     "監督者から視線を向けられた迷惑受身（見られて）。",
     {"見せて": "他動詞「見せる」であり、自分が答案を監督者に見せた意味になり文意がズレます。",
      "見させられて": "見させられた（強制的に見る）になり、自分が何者かを見せられた意味になり破綻します。",
      "見て": "能動形であり、監督者が自分を見た文脈で自分が主語として成立しません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q5",
     "My younger brother made our sister cry, so he was scolded severely by our mother.",
     "弟が母を泣かせた行為に対する他動使役（泣かせて）。",
     {"泣かれて": "迷惑受身であり、妹が泣いたことで弟が迷惑を受けた意味になり「母に怒られた」理由に合いません。",
      "泣かされて": "使役受身であり、弟が誰かに泣かされた意味になり叱責の因果が破綻します。",
      "泣いて": "自動詞であり、弟自身が泣いたことになってしまい叱られた理由になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q6",
     "Because my fever did not go down at all, the doctor had me undergo a thorough examination.",
     "医師から精密検査を受けるよう指示された使役受身（受けさせられた）。",
     {"受けて": "自発的な動作になり、医師の指示・判断で受けさせられた受動性が薄れます。",
      "受けさせて": "話者が医師に検査を受けさせた意味になり、主客が逆転して破綻します。",
      "受けられた": "可能形になり、医師に強いられて検査を受けた受身文脈になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q7",
     "I had my umbrella taken by mistake by someone at the restaurant entrance, so I had to walk home in the rain.",
     "所有物を他人に勝手に持ち去られた迷惑受身（間違えて持っていかれて）。",
     {"持っていって": "能動形であり、話者が自ら傘を持ち去ったことになり雨に濡れた理由と矛盾します。",
      "持っていかせて": "話者が他人に傘を持っていかせたことになり、被害の文脈に反します。",
      "持っていかされて": "他人に強制されて傘を持ち去った意味になり、取り違えの被害事実と合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q8",
     "When I was in high school, the physical education teacher made the entire class run 10 kilometers.",
     "教員が生徒全員に長距離走を強制した能動使役（走らせた）。",
     {"走られた": "迷惑受身であり、生徒が走って先生が困った意味になり破綻します。",
      "走らされた": "使役受身であり、生徒視点の「走らされた」となり、主語「体育の先生は」と格衝突します。",
      "走った": "自動詞能動形であり、先生自らが走ったことになり生徒に課した文脈とズレます。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q9",
     "Having my private diary read secretly by a friend made me feel exceptionally uncomfortable.",
     "秘密の日記を勝手に閲覧された迷惑受身（読まれて）。",
     {"読ませて": "使役形であり、自分が友人に日記を読ませたことになり「不快だった」感情と矛盾します。",
      "読まされて": "使役受身であり、誰かに強制されて日記を読んだ意味になり破綻します。",
      "読んで": "能動形であり、主語である話者自身が日記を読んだことになり文脈が成り立ちません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q10",
     "On the stage of the school festival, I was made to sing a solo in front of everyone by my senior.",
     "先輩から無理に指名されて歌わされた使役受身（歌わされた）。",
     {"歌われて": "迷惑受身であり、誰かが歌って自分が困った意味になりソロ独唱の文脈に合いません。",
      "歌わせて": "自分が先輩に歌わせた意味になり、上下関係と強制の方向が逆転します。",
      "歌って": "自発的能動形であり、嫌々引き受けた「先輩に〜」の文脈に反します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q11",
     "The director had the new employee review the meeting materials once more.",
     "上司が部下に再確認を指示した能動使役（確認させた）。",
     {"確認された": "受身形であり、新入社員が部長を確認したことになってしまい上下関係が崩壊します。",
      "確認させられた": "使役受身形であり、主語「部長は」と格支配（〜に〜させた）が一致しません。",
      "確認した": "部長自らが確認したことになり、指示対象「新入社員に」と整合しません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129"),

    ("skm3-p3-c5-q12",
     "When having one's name suddenly called out on a crowded street, anyone would be startled.",
     "不意に他者から名前を呼ばれる受身（名前を呼ばれたら）。",
     {"呼んだら": "自分が他人の名前を呼んだことになり、「誰でも驚く」という受動的驚きの文脈に合いません。",
      "呼ばせたら": "他人に名前を呼ばせたことになり、突然の出来事に対するリアクションになりません。",
      "呼んでいたら": "能動進行形であり、街中で驚く客観的シチュエーションに反します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 5 (受身・使役・使役受身), pp. 128–129")
]

for qid, trans, ctx, opt_map, evid in ch5_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 6: やる・くれる・もらう (Giving & Receiving Perspective) - pp. 130–133
# ---------------------------------------------------------------------------
ch6_data = [
    ("skm3-p3-c6-q1",
     "When I got lost and was in trouble, a kind police officer gave me a map from the police box.",
     "外部者（警察官）が話者（ウチ）に好意を与えた授受動詞（くれた）。",
     {"あげた": "話者から他者へ与える動詞であり、警察官から話者への授与に反します。",
      "もらった": "主語が「話者は」である必要があり、主語「警察官が」と格助詞の対応が破綻します。",
      "やった": "目下や動物に与える粗野な表現であり、警察官の行為に対して失礼かつ不適です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q2",
     "Because there was a difficult problem I could not solve by myself, I had a friend who is good at math explain it to me.",
     "話者が友人に依頼して教えてもらった授受動詞（教えてもらった）。",
     {"くれた": "主語が「友人が」である必要があり、「友人に」という相手格助詞と整合しません。",
      "あげた": "話者が友人に教えてあげた意味になり、自分が解けなかった前提と矛盾します。",
      "やった": "目下に教え与えるニュアンスになり、友人に助けてもらった文脈に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q3",
     "For my younger brother's birthday, I bought and gave him the soccer ball he had been wanting.",
     "話者が目下の弟に買い与えた授受動詞（買ってやった）。",
     {"くれた": "弟が話者に買い与えた意味になり、兄がプレゼントした文脈と逆転します。",
      "もらった": "弟に買ってもらったことになり、自分がプレゼントした前提と矛盾します。",
      "いただいた": "目上からの謙譲授受であり、実の弟に対して用いるのは極めて不自然です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q4",
     "Professor Tanaka kindly corrected the mistakes in my draft paper very meticulously.",
     "目上の先生が話者のために労をとってくださった尊敬授受（直してくださった）。",
     {"直していただいた": "主語が「私が」である必要があり、主語「田中先生が」と格が一致しません。",
      "直してあげた": "話者が先生に直してあげた上から目線の表現になり、極めて失礼です。",
      "直してくれた": "対等・目下向けの表現であり、指導教授に対して用いるには敬意が不足します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q5",
     "Because I didn't have enough money at hand, I had my friend lend me train fare.",
     "話者が友人に頼んでお金を借り受けた授受動詞（貸してもらった）。",
     {"貸してくれた": "主語が「友人が」である必要があり、「友人に」という格助詞と衝突します。",
      "貸してあげた": "話者が友人に貸したことになり、自分が手持ちのお金不足だった前提と矛盾します。",
      "貸してやった": "目下に貸し与える表現であり、友人に助けてもらった文意に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q6",
     "When I was sick in bed with a cold, my roommate cooked warm porridge for me.",
     "同居人が話者のために親切に行ってくれた授受動詞（作ってくれた）。",
     {"作ってあげた": "話者がルームメイトに作ったことになり、寝込んでいた自分が主客逆転します。",
      "作ってもらった": "主語が「私は」である必要があり、「ルームメイトが」という主格と合いません。",
      "作ってやった": "見下したニュアンスになり、看病してくれた相手に対する感謝の描写に反します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q7",
     "Every morning before going to work, I feed food to my pet dog.",
     "動物・ペットに餌を与える授受動詞（餌をやる）。",
     {"あげる": "人間対等の表現であり、伝統的文法において愛犬への給餌は「やる」が正統です。",
      "くれる": "愛犬が話者に餌をくれた意味になり主客が破綻します。",
      "もらう": "愛犬から餌をもらった意味になり意味が成立しません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q8",
     "At the job hunting consultation, the career counselor listened attentively to my worries.",
     "相談員が話者のために親身に傾聴してくれた授受動詞（聞いてくれた）。",
     {"聞いてあげた": "話者が相談員の悩みを聞いてあげたことになり、主客が完全に逆転します。",
      "聞いてもらった": "主語が「私は」である必要があり、主語「相談員が」と格が一致しません。",
      "聞いてやった": "目下に聞いてやる横柄な表現になり、カウンセラーの親切な対応描写に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q9",
     "I had the department manager check over the project proposal once more.",
     "話者が目上の部長に依頼して確認をいただいた謙譲授受（見ていただいた）。",
     {"見てくださった": "主語が「部長が」である必要があり、「部長に」という相手格と衝突します。",
      "見てあげた": "話者が上司の部長に見てあげた不敬な表現になり、絶対に不適切です。",
      "見てもらった": "同僚・目下向けの授受であり、組織の直属上司である部長に対する敬意が欠けます。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q10",
     "Seeing a tourist struggling with a heavy suitcase on the station stairs, I helped them carry it.",
     "困っている他者に対して親切に手助けしてあげた授受動詞（運んであげた）。",
     {"運んでくれた": "観光客が話者の荷物を運んでくれたことになり、親切をした文脈と逆転します。",
      "運んでもらった": "観光客に運んでもらったことになり、手助けをした事実と矛盾します。",
      "運んでやった": "見下した恩着せがましい響きがあり、旅人への善意の行動描写に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q11",
     "When moving apartments, I had my senior coworker help me with driving the small truck.",
     "話者が先輩にお願いしてトラックを運転してもらった授受動詞（運転してもらった）。",
     {"運転してくれた": "主語が「先輩が」である必要があり、「先輩に」という格助詞と整合しません。",
      "運転してあげた": "話者が先輩のために運転してあげた意味になり、助けを頼んだ前提と矛盾します。",
      "運転してやった": "目下の先輩（？）に運転してやる横柄な表現になり、人間関係を無視した非文です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133"),

    ("skm3-p3-c6-q12",
     "My host mother kindly packed a bento lunch for me every day with diverse nutritious ingredients.",
     "ホストマザーが話者の健康を思って作ってくださった恩恵授受（作ってくれた）。",
     {"作ってあげた": "留学生である話者がホストマザーに毎日作ってあげた意味になり文脈が逆転します。",
      "作ってもらった": "主語が「私は」である必要があり、主語「ホストマザーが」と格が一致しません。",
      "作ってやった": "目下に作ってやる尊大な語感になり、温かい家庭生活の回想に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 6 (やる・くれる・もらう), pp. 130–133")
]

for qid, trans, ctx, opt_map, evid in ch6_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 7: 指示詞 (Demonstratives: こ・そ・あ in Discourse) - pp. 134–137
# ---------------------------------------------------------------------------
ch7_data = [
    ("skm3-p3-c7-q1",
     "I bought a new smartphone yesterday. This one has exceptionally superior camera performance.",
     "話者が自ら直前に導入した身近な所有対象を指す近称指示詞（これ）。",
     {"あれ": "話者・聞き手双方の既知情報や遠い記憶を指す遠称であり、昨日買ったばかりの眼前事物に合いません。",
      "どれ": "疑問詞であり、特定の実物を指す指示代名詞として文脈が破綻します。",
      "そう": "文末推量・様態表現であり、名詞文の主語「〜は」の位置に置けません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q2",
     "'I went on a trip to Kyoto last week.' 'That sounds like a wonderful trip!'",
     "対話相手（聞き手領域）が直前に提示した話題を受ける中称指示詞（それ）。",
     {"これ": "話者自身の領域を指すため、相手が話した旅行の話題を受ける応答として不自然です。",
      "あれ": "双方が共通して知っている昔の思い出を指す語感になり、相手からの初耳報告に合いません。",
      "どれ": "選択の疑問詞であり、相手の旅行を評価する感嘆応答として機能しません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q3",
     "'Remember that small coffee shop we used to go to together back in college?' 'Ah, that place was wonderful!'",
     "話し手と聞き手双方が共有している遠い共通の思い出を指す遠称指示詞（あの店）。",
     {"この店": "目の前の眼前にある店を指すため、大学時代の昔の思い出話に合いません。",
      "その店": "相手だけが知っている話題を受ける指示詞になり、2人で一緒に通った共通記憶に反します。",
      "どの店": "疑問詞であり、懐かしい特定の思い出の店を指す文脈になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q4",
     "In this report, I shall consider modern environmental issues from the following three perspectives.",
     "文章の書き手がこれから後述・展開する内容を先取りして指す指示詞（次のように・これ）。",
     {"それら": "先行する既出の話題を指す語であり、これから後続で述べる3つの視点には使えません。",
      "あれら": "遠くの共通記憶を指す語であり、レポートの自発的展開提示に合いません。",
      "どれら": "不自然な疑問表現であり、書き手の分析枠組みの提示になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q5",
     "Global warming is progressing rapidly. As a measure against that, the promotion of renewable energy is required.",
     "文章の前文で述べられた先行事態・命題を受ける中称指示詞（それに対する）。",
     {"これに対する": "話者自身が今まさに引き起こしている身近な事態のように聞こえ、客観的地球環境論議として座りが悪いです。",
      "あれに対する": "遠い心理的距離が生じ、直前の文で言及した主要論点を受ける結束性が弱まります。",
      "どれに対する": "疑問詞になり、論理的な対策の提示文になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q6",
     "'Who is that tall gentleman standing over there?' 'Ah, he is the new director.'",
     "話者・聞き手双方の視界から離れた遠い位置にいる人物を指す遠称指示詞（あの方）。",
     {"この方": "話者のすぐ間近にいる人物を指すため、「あそこに立っている」という遠距離描写と衝突します。",
      "その方": "相手の手元・近辺にいる人物を指すため、双方が遠くに見ている人物に合いません。",
      "どの方": "疑問詞であり、相手からの具体的な質問に対する回答述語の特定人物として使えません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q7",
     "It was a truly tragic accident. I can never forget that terrifying shock even now.",
     "過去の強烈な体験・心理的距離のある過去の出来事を想起する指示詞（あの）。",
     {"この": "現在の目の前のショックになり、過去の事故の記憶を回想する文脈に合いません。",
      "その": "客観的事実の指示にとどまり、話者自身の生々しい個人的記憶の情動性が薄れます。",
      "どの": "疑問詞であり、特定の忘れられない衝撃を指す文脈になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q8",
     "We have introduced a new automated system. By means of this, work efficiency will increase dramatically.",
     "直前で自社が導入した新しいシステムを眼前・身近な手段として受ける指示詞（これによって）。",
     {"それによって": "客観的には可能ですが、自社が主体的に導入した新システムの直後では「これによって」が最も緊密に結束します。",
      "あれによって": "遠い過去や第三者のシステムのように聞こえ、自社の最新施策のアピールに反します。",
      "どれによって": "疑問詞であり、導入成果を説明する確定言明になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q9",
     "'I'm thinking of studying abroad in France next spring.' 'Oh, that is really splendid!'",
     "対話相手が打ち明けた計画・情報に対する相づち（それは）。",
     {"これは": "相手の話した内容に対して「これは」と受けると、相手の領域を侵犯して不自然です。",
      "あれは": "昔の既知の思い出になり、相手の未来の留学計画への驚き・共感の応答になりません。",
      "どれは": "非文であり、相づちとして機能しません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q10",
     "One day, a miraculous encounter occurred. On that day, my life took a major turn.",
     "物語・エッセイの中で、運命的な過去の特定の日をドラマチックに回想する指示詞（その日・あの日）。",
     {"この日": "現在の日や直近の眼前を指すため、物語的な過去の転機描写に合いません。",
      "その日": "正解です。直前に提示された「ある日」を文脈指示として確実に受けます。",
      "どの火": "同音異義語の漢字誤りかつ疑問詞で非文です。",
      "あの火": "火災の描写ではないため文脈に反します。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q11",
     "I want you to think carefully about the following proposition: What truly is happiness?",
     "これから述べる問いかけを後続提示する指示詞（次のこと・このこと）。",
     {"そのこと": "すでに前述された事柄を指すため、後続の「幸せとは何か」を予告する指示になりません。",
      "あのこと": "遠い過去の共通記憶を指すため、新しい普遍的問いの導入に合いません。",
      "どとのこと": "不自然な疑問連鎖で非文です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137"),

    ("skm3-p3-c7-q12",
     "He always speaks in a boastful manner, which makes those around him uncomfortable.",
     "直前文で述べられた人物の不快な振る舞い全体を客観的に受ける指示詞（それ）。",
     {"これ": "自分自身の行為のように聞こえてしまい、他人の自慢話を批判する客観視点になりません。",
      "あれ": "遠い過去の記憶になり、相手の恒常的な不快な言動を指摘する接続になりません。",
      "どれ": "選択の疑問詞であり、原因となる相手の行動全体を指せません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 7 (指示詞), pp. 134–137")
]

for qid, trans, ctx, opt_map, evid in ch7_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 8: 主題・助詞 (Topic & Focus: は vs が) - pp. 138–139
# ---------------------------------------------------------------------------
ch8_data = [
    ("skm3-p3-c8-q1",
     "Once upon a time, in a certain place, there lived a kind-hearted old man.",
     "昔話の冒頭で未知の登場人物を初めて物語世界に導入する現象描写主格（が）。",
     {"は": "すでに話題として成立している既知の情報（旧情報）を取り立てるため、物語冒頭の未知の人物導入に反します。",
      "を": "他動詞の目的格であり、自動詞「住んでいました」の主語になれません。",
      "に": "場所・相手格であり、居住動作を行う主体名詞「おじいさん」に結べません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q2",
     "Once upon a time, there lived an old man. That old man went to the mountain to gather firewood.",
     "前文ですでに導入され、既知となった主題を取り立てる助詞（は）。",
     {"が": "新情報を導入する格助詞であり、直前で導入済みの「そのおじいさん」に対して使うと不自然な排他強調になります。",
      "を": "目的格助詞であり、移動動作「山へ行った」の主体名詞に置けません。",
      "に": "帰着点助詞であり、動作主であるおじいさんに置くと非文になります。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q3",
     "Look, a rainbow has appeared over the distant mountains!",
     "目前に現れた自然現象の直接目撃・新情報発見の主格（が）。",
     {"は": "一般的な属性や主題判断を表すため、今まさに目の前に現れた虹の直接描写に合いません。",
      "を": "自動詞「出ている」に対して目的格「を」を用いると格支配が破綻します。",
      "で": "動作の場所・手段の助詞であり、出現した主体そのものを表せません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q4",
     "Speaking of whales, although they resemble fish, they are actually mammals that breathe with lungs.",
     "周知の生物種を主題として提示し、その本質的属性を解説する提示助詞（は）。",
     {"が": "目の前の個体発見（クジラが現れた）のように響き、クジラ一般の生物学的解説に合いません。",
      "を": "目的格助詞であり、文全体の主題提示節を作れません。",
      "に": "対象・帰着点助詞であり、文頭で解説のテーマを提示する機能がありません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q5",
     "Who broke this precious vase? Please be honest and come forward.",
     "疑問詞「だれ」が主語になる場合、主格助詞は必ず「が」を用いる（だれが）。",
     {"は": "「は」は既知の主題を取り立てるため、未知の対象である疑問詞「だれ」に直接接続できません（だれは×）。",
      "を": "目的格助詞であり、破壊動作を行った主体「だれ」に接続できません。",
      "に": "相手・間接目的格であり、能動動詞「割った」の主語になれません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q6",
     "'Which person is Mr. Tanaka?' 'The person wearing the black glasses is Mr. Tanaka.'",
     "特定の対象を特定・排他的に同定する指定文の主格（が）。",
     {"は": "主題文になり、「黒い眼鏡をかけている人は〜」だと眼鏡の人物についての属性解説になってしまい、指名特定に合いません。",
      "を": "目的格助詞であり、コピュラ文「〜です」の主語に置けません。",
      "で": "場所・手段助詞であり、人物そのものを指す主格になれません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q7",
     "My older brother likes sports, but my younger brother prefers quiet reading.",
     "2つの対象の相違を鮮明に対比させる取り立て助詞（は）。",
     {"が": "単純な主格提示になり、「兄は〜、弟は〜」という明確な対比関係が際立ちません。",
      "を": "自動詞文の主語に対して目的格助詞を用いることはできません。",
      "に": "対象格助詞であり、対比される2人の主語に置く形になりません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q8",
     "When the flowers in the garden bloom in spring, many bees come visiting.",
     "条件節・連体修飾節などの従属節内の主語には「が」を用いる（花が咲くと）。",
     {"は": "文全体の主題を作る助詞であり、「〜と」で括られた従属節内の主語に「は」を置くと文構造が破綻します。",
      "を": "自動詞「咲く」に対して目的格「を」を用いることは文法的に不可能です。",
      "で": "場所助詞であり、開花する主体の名詞「花」に接続できません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q9",
     "The place where the famous historical castle stands is on top of that hill over there.",
     "名詞「場所」を修飾する連体修飾節内部の主格（城が建っている）。",
     {"は": "連体修飾節の内部主語に「は」を置くことは原則としてできず、非文になります。",
      "を": "自動詞「建つ」に対して目的格「を」を用いると格支配に反します。",
      "で": "場所助詞であり、建っている主体「城」に結べません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q10",
     "I can understand English, but I cannot speak German at all.",
     "否定文において対比・限定を強調する取り立て助詞（ドイツ語は）。",
     {"が": "肯定文の可能対象には使えますが、否定文「全く話せません」では「は」を用いて対比・強調するのが自然です。",
      "を": "能力可能動詞「話せる」の否定に対して「を」を用いると対比の結束性が弱まります。",
      "で": "手段助詞であり、話せない言語の対象そのものを提示できません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q11",
     "The door opened, and a cold wind suddenly blew into the room.",
     "出来事の直接知覚・無意志的展開を描写する主格（風が吹き込んできた）。",
     {"は": "恒常的主題になり、突発的に吹き込んできた冷たい風の臨場感描写に合いません。",
      "を": "自動詞「吹き込む」に対して目的格「を」を置くことはできません。",
      "に": "風は動作主体であり、着点・相手助詞「に」は不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139"),

    ("skm3-p3-c8-q12",
     "Mount Fuji is the highest mountain in Japan and is world-renowned.",
     "広く知られた対象についての客観的事実・属性を述べる主題助詞（富士山は）。",
     {"が": "排他的指定（富士山こそが最高峰だ）のニュアンスが生じ、一般的な名峰紹介の文脈に合いません。",
      "を": "目的格助詞であり、文全体の主題主語に置くことはできません。",
      "に": "場所助詞であり、主語名詞に直接接続して主題文を作れません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 8 (主題・助詞), pp. 138–139")
]

for qid, trans, ctx, opt_map, evid in ch8_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 9: 接続表現 (Discourse Connectors & Conjunctions) - pp. 140–141
# ---------------------------------------------------------------------------
ch9_data = [
    ("skm3-p3-c9-q1",
     "Heavy snow continued to fall from last night. Therefore, the train schedules are significantly disrupted this morning.",
     "前文の原因から生じる論理的結果・因果関係を導く接続詞（そのため）。",
     {"しかし": "逆接接続詞であり、大雪から電車の乱れが生じる順当な因果関係に矛盾します。",
      "つまり": "要約・換言の接続詞であり、降雪の結果として生じた被害事態の導入に合いません。",
      "ところで": "話題転換の接続詞であり、原因と結果を緊密に結ぶべき文脈を断絶させます。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q2",
     "We practiced with all our might and faced the match. However, unfortunately we were defeated by a single point.",
     "前文の努力や期待に反する不本意な結果を導く逆接接続詞（しかし）。",
     {"したがって": "順接の帰結接続詞であり、全力で練習したから負けたという不条理な因果文になります。",
      "しかも": "累加・付加の接続詞であり、相反する敗北結果の導入に合いません。",
      "要するに": "要約接続詞であり、試合結果の逆接展開に不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q3",
     "The hotel had an outstanding view from the room. Furthermore, the cuisine was exquisite and the staff hospitality was top-notch.",
     "先行する長所にさらなる美点を付け加える累加接続詞（さらに・そのうえ）。",
     {"そのうえ": "正解です。長所に長所を重ねる累加接続詞です。",
      "けれども": "逆接接続詞であり、料理が美味しかったという追加の長所に矛盾します。",
      "なぜなら": "理由説明の接続詞であり、文末が「〜からだ」で結ばれていないため文法破綻します。",
      "あるいは": "選択接続詞であり、ホテルの魅力を併記する文脈に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q4",
     "I decided to refuse that proposal. The reason why is that the budget was too tight to ensure safety.",
     "前述の決定に対する根拠・理由を後述する接続詞（なぜなら）。",
     {"そのため": "結果を導く順接接続詞であり、文末「〜からだ」という理由文末と呼応しません。",
      "ただし": "条件・補足の接続詞であり、拒絶した直接の理由説明に合いません。",
      "すると": "継起・発見の接続詞であり、理由を述べる文脈に不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q5",
     "All participants agreed to the new proposal. That is to say, the project was officially approved.",
     "前述の全員賛成という事実を分かりやすく言い換える換言接続詞（つまり）。",
     {"しかし": "逆接接続詞であり、全員賛成と正式承認という論理的一致に反します。",
      "なぜなら": "理由説明の接続詞であり、承認という言い換え・結論に合いません。",
      "それどころか": "予想を上回る反対事態を述べる強調詞であり、承認の確認に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q6",
     "Let us conclude today's progress report here. By the way, how was the reception event yesterday?",
     "これまでの本題を打ち切り、新しい別の話題へ切り替える話題転換接続詞（ところで）。",
     {"したがって": "順接の論理的帰結であり、唐突に昨日の懇親会の話に飛ぶ文脈に反します。",
      "つまり": "要約接続詞であり、別の話題の懇親会を要約することになり破綻します。",
      "その結果": "因果関係接続詞であり、進捗報告の終了が原因で懇親会が開かれたわけではないため誤りです。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q7",
     "Admission to the museum is free for anyone. However, advanced reservations are required on weekends.",
     "原則を提示した上で、例外的な条件・制約を付け加える補足接続詞（ただし）。",
     {"そのため": "結果接続詞であり、無料だから予約が必要という因果関係になりません。",
      "つまり": "換言接続詞であり、土日要予約は「誰でも無料」の言い換えではないため誤りです。",
      "要するに": "要約接続詞であり、週末の特例制限の追加に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q8",
     "He not only excels in academic studies, but is also active as a soccer team captain.",
     "優れた長所にもう一つの卓越した実績を付加する累加接続詞（そのうえ・しかも）。",
     {"しかも": "正解です。学業優秀に加えて主将活躍を付加する累加接続です。",
      "だが": "逆接接続詞であり、主将としても活躍しているポジティブな追加に矛盾します。",
      "あるいは": "選択接続詞であり、両方を兼ね備えている文脈に反します。",
      "それとも": "二者択一の疑問接続詞であり、肯定的な事実記述に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q9",
     "Please pay the fee by credit card or bank transfer.",
     "二つ以上の手段・選択肢のいずれかを選ぶよう提示する選択接続詞（または・あるいは）。",
     {"または": "正解です。カード決済と銀行振込のどちらかを選択する助詞です。",
      "しかし": "逆接接続詞であり、支払方法の選択肢提示に合いません。",
      "したがって": "結果接続詞であり、振込がカード払いの帰結になる不条理が生じます。",
      "要するに": "要約接続詞であり、振込がカード払いの要約ではないため誤りです。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q10",
     "Sales this term declined 20% compared to the previous year. Consequently, our company had to drastically revise our plans.",
     "先行する業績悪化という原因から生じた不可避の帰結を導く接続詞（その結果・したがって）。",
     {"したがって": "正解です。客観的事実から導かれる方針転換の帰結を示します。",
      "けれども": "逆接接続詞であり、売上激減から方針見直しに至る順当な帰結に合いません。",
      "なぜなら": "理由説明接続詞であり、文末が原因句になっていないため文法破綻します。",
      "ところで": "話題転換接続詞であり、社運を分ける因果関係の文脈を切断してしまいます。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q11",
     "I pushed the doorbell at the entrance. Thereupon, a lively greeting came from inside the house.",
     "先行動作を行った直後に、次の事態が眼前で発生したことを導く継起接続詞（すると）。",
     {"すると": "正解です。インターホンを押した直後に返事が返ってきた継起を表します。",
      "しかし": "逆接接続詞であり、呼び鈴を押して返事がある当然の反応に合いません。",
      "したがって": "論理的帰結であり、チャイムの直後の自発的出来事の描写に合いません。",
      "つまり": "換言接続詞であり、返事がチャイムの言い換えではないため誤りです。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141"),

    ("skm3-p3-c9-q12",
     "He arrived 30 minutes late for the appointment. Furthermore, he didn't offer a single word of apology.",
     "悪い事態にさらに不快な態度が重なる否定的な累加接続詞（それどころか・そのうえ）。",
     {"そのうえ": "正解です。遅刻の上に謝罪もしないという悪質な重ね合わせを示します。",
      "したがって": "遅刻したから謝らなかったという不条理な因果関係になり破綻します。",
      "なぜなら": "理由接続詞であり、遅刻の理由を説明する文脈になっていないため誤りです。",
      "つまり": "換言接続詞であり、無謝罪が遅刻の言い換えではないため不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 9 (接続表現), pp. 140–141")
]

for qid, trans, ctx, opt_map, evid in ch9_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

# ---------------------------------------------------------------------------
# Chapter 10: 敬語と視点の一致 (Unified Style & Perspective) - pp. 142–145
# ---------------------------------------------------------------------------
ch10_data = [
    ("skm3-p3-c10-q1",
     "In this academic thesis, I attempted a detailed analysis regarding the reality of the digital divide in modern society.",
     "学術論文の常体（だ・である調）による文体統一（試みた）。",
     {"試みました": "敬体（デス・マス調）であり、論文全体の常体文体と混在して文体を乱します。",
      "試みてみた": "口語的な試行表現であり、フォーマルな論文の格調に合いません。",
      "試みちゃった": "くだけた俗語短縮形であり、学術文章として極めて不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q2",
     "Everyone, thank you very much for gathering here today despite your busy schedules.",
     "公のスピーチ・挨拶における丁寧体・敬体による統一（ございます）。",
     {"だ": "ぞんざいな常体であり、集まってくださった来賓・聴衆に対する礼儀を著しく欠きます。",
      "である": "論文調の硬い常体であり、対面のスピーチ挨拶として極めて不自然です。",
      "ぞ": "乱暴な男性口調の終助詞であり、公式挨拶の場に絶対にふさわしくありません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q3",
     "Excuse me, but did you say that Professor Suzuki will be absent from today's meeting?",
     "教授の出欠について尋ねる尊敬語表現（いらっしゃらない）。",
     {"いない": "先生に対して敬意のない平語であり、教授の欠席を伺う表現として不適切です。",
      "おられない": "西日本方言由来の表現であり、標準的な共通語の敬語テストでは「いらっしゃらない」が正解です。",
      "まいらない": "謙譲語（自分が行かない・来ない）であり、目上の先生の動作に用いると失礼です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q4",
     "(Customer service) 'Welcome! How many guests are in your party?'",
     "接客における来店客の人数を伺う敬語表現（何名様でいらっしゃいますか）。",
     {"何人ですか": "日常の砕けた会話表現であり、飲食店等の接客敬語として丁寧さが不足します。",
      "何人でおられますか": "接客敬語として不自然であり、尊敬の「いらっしゃいますか」が標準的です。",
      "何人でおいでですか": "悪くありませんが、「何名様」との呼応において「いらっしゃいますか」が最も格式正統です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q5",
     "Regarding that matter, I already delivered a thorough explanation to the department manager yesterday.",
     "社内で上司である部長に報告・説明を行った謙譲表現（ご説明申し上げました）。",
     {"ご説明になられました": "二重敬語かつ尊敬語であり、話者自身の行為を高める誤用です。",
      "説明してあげました": "上司に対して恩着せがましい表現であり、極めて無礼です。",
      "説明しちゃいました": "くだけた俗語表現であり、ビジネス報告の場に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q6",
     "(Formal business email) 'We would appreciate it if you could kindly confirm the attached estimation document.'",
     "ビジネスメールにおける相手への確認依頼表現（ご確認いただけますと幸甚に存じます）。",
     {"確認してください": "直接命令のニュアンスがあり、社外取引先へのメールとして失礼です。",
      "見てくれ": "親しい友人同士の命令形であり、公式ビジネス文書としてあり得ません。",
      "確認してごらん": "目下が目上に使う表現ではなく、大人が子供を促す口調で不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q7",
     "The director said that they would personally inspect the local factory in person tomorrow.",
     "役員・目上の人の視察動作に対する尊敬語（視察なさる）。",
     {"視察いたす": "謙譲語であり、目上の役員の視察動作に用いると主客が逆転します。",
      "視察してやる": "見下した粗野な表現であり、役員の行動描写に合いません。",
      "視察される": "受身助詞「れる」による軽微な尊敬より、直接の「なさる」が最も格調高いです。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q8",
     "(Telephone reception to outside caller) 'Yamada of our company will contact you again later.'",
     "社外の取引先に対して自社の身内（山田）の動作を述べる謙譲語（ご連絡差し上げます）。",
     {"ご連絡になられます": "身内を尊敬する誤りであり、社外に対して身内を高めるのは日本のビジネスマナー違反です。",
      "連絡してあげるそうです": "上から目線の表現であり、顧客に対する電話対応として不適切です。",
      "連絡するんだって": "伝聞のくだけた会話口調であり、代表電話の対応として失格です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q9",
     "In this report, based on questionnaire results, we summarize the main characteristics.",
     "常体（論文・公的報告書）で統一された文末（まとめる・まとめた）。",
     {"まとめます": "敬体（デス・マス調）であり、常体で統一された報告書の文体を乱します。",
      "まとめたんだ": "親しい会話の終助詞であり、報告書の文体にふさわしくありません。",
      "まとめちゃう": "くだけた俗語表現であり、公式レポートに絶対に不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q10",
     "Ladies and gentlemen, we truly thank you for visiting our facility today.",
     "館内放送における来館者に対する丁寧な感謝（お越しいただき）。",
     {"来させて": "使役形であり、施設側が客を無理に来させた意味になり破綻します。",
      "来てやって": "見下した恩着せがましい表現であり、来館者に対する接客放送にあり得ません。",
      "いらしてくれ": "くだけた友人同士の命令形であり、公式アナウンスとして不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q11",
     "The principal encouraged the graduating students warmly during the commencement ceremony.",
     "校長先生による卒業生への激励動作（激励なさった）。",
     {"激励いたした": "謙譲語であり、校長先生の動作を高める文脈で自分をへりくだる形になり誤りです。",
      "激励してやった": "粗野な表現であり、厳粛な卒業式の描写にふさわしくありません。",
      "激励しちゃった": "くだけた俗語表現であり、記念式典の記述として不適切です。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145"),

    ("skm3-p3-c10-q12",
     "I have listened carefully to all of your opinions and will consider them with utmost care.",
     "相手の貴重な意見を受け止めて検討する謙譲表現（拝聴いたしました）。",
     {"お聞きになられました": "二重敬語かつ尊敬語であり、話者自身の聴取行為を高めてしまう誤用です。",
      "聞いてあげました": "相手の意見を上から目線で聞いてやった表現になり、不適切です。",
      "聞いちゃいました": "くだけた俗語表現であり、改まったビジネス・対話の場に合いません。"},
     "Shin Kanzen Master N3 Bunpou, Part 3 Chapter 10 (敬語と視点の一致), pp. 142–145")
]

for qid, trans, ctx, opt_map, evid in ch10_data:
    REPAIRS_P3[qid] = {
        "trans": trans, "ctx": ctx, "opt_reasons": opt_map, "evid": evid
    }

print(f"Loaded {len(REPAIRS_P3)} semantic repairs for SKM N3 Part 3.")

updated = 0
for e in exercises:
    eid = e.get("id")
    if eid in REPAIRS_P3:
        r = REPAIRS_P3[eid]
        e["translation"] = r["trans"]
        e["context"] = r["ctx"]
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = r["evid"]
        
        # Update option explanations
        expl = e.get("explanation", {})
        if isinstance(expl, dict):
            for opt in expl.get("options", []):
                txt = opt.get("text", "")
                if opt.get("isCorrect"):
                    # keep correct rationale
                    continue
                else:
                    # Replace generic reason with specific reason
                    if txt in r["opt_reasons"]:
                        opt["reason"] = f"【不正解】{r['opt_reasons'][txt]}"
                    else:
                        # find best matching key
                        matched = False
                        for k, v in r["opt_reasons"].items():
                            if k in txt or txt in k:
                                opt["reason"] = f"【不正解】{v}"
                                matched = True
                                break
                        if not matched:
                            opt["reason"] = f"【不正解】文脈・文法関係（{txt}）において不適切です。"
        updated += 1

print(f"Updated {updated} exercises in SKM N3 Part 3.")

with open(EXERCISES_PATH, "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved updated chapterExercises.json successfully.")
