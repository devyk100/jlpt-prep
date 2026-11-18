import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {e['id']: e for e in exercises}

# 1. Update g2-l16-ex-3 prompt and options for absolute linguistic precision
ex_16_3 = ex_map['g2-l16-ex-3']
ex_16_3['question'] = "出かけ（　　）、鍵をかけます。"
ex_16_3['options'] = ["る時", "た時", "ている時", "て時"]
ex_16_3['correctIndex'] = 0
ex_16_3['explanation']['options'] = [
    {
        "text": "る時",
        "isCorrect": True,
        "reason": "Correct. V-る時 indicates that the main clause action (locking the door) occurs BEFORE or at the start of departing (出かける時、鍵をかけます).",
        "trapCategory": "meaning"
    },
    {
        "text": "た時",
        "isCorrect": False,
        "reason": "Incorrect. V-た時 (出かけた時) indicates that the action occurs AFTER having already left and gone outside. One locks the house door from inside before stepping out.",
        "trapCategory": "meaning"
    },
    {
        "text": "ている時",
        "isCorrect": False,
        "reason": "Incorrect. 出かけている時 describes the continuous state of being away/out of the house during the entire outing, at which point locking the entry door from inside has long passed.",
        "trapCategory": "meaning"
    },
    {
        "text": "て時",
        "isCorrect": False,
        "reason": "Incorrect. Te-forms cannot attach directly to the noun 時 (*出かけて時 is ungrammatical; connective te-forms cannot modify nouns).",
        "trapCategory": "formation"
    }
]

# 2. Fix sync and option ordering for g2-l19-ex-12
ex_19_12 = ex_map['g2-l19-ex-12']
ex_19_12['options'] = ["休み", "休みな", "休みの", "休むの"]
ex_19_12['correctIndex'] = 2
ex_19_12['explanation']['options'] = [
    {
        "text": "休み",
        "isCorrect": False,
        "reason": "Incorrect. 休み is a noun meaning 'day off'. When a noun modifies the noun-like auxiliary はず, it must connect using the genitive particle の (休みのはず). Placing a bare noun directly before はず (*休みはず) is ungrammatical.",
        "trapCategory": "formation"
    },
    {
        "text": "休みな",
        "isCorrect": False,
        "reason": "Incorrect. The connector な is used when な-adjectives modify はず (e.g. 暇なはず). 休み is a noun, not a な-adjective, so *休みなはず is ungrammatical.",
        "trapCategory": "formation"
    },
    {
        "text": "休みの",
        "isCorrect": True,
        "reason": "Correct. 休み is a noun; nouns require the particle の to attach to the noun-like suffix はず (休みの[はずです] = should be off / expected to be off).",
        "trapCategory": "formation"
    },
    {
        "text": "休むの",
        "isCorrect": False,
        "reason": "Incorrect. Verbs modify はず directly with their plain/short form (休むはず). Inserting an extra nominalizer particle の (*休むのはず) is grammatically invalid.",
        "trapCategory": "formation"
    }
]

# 3. Comprehensive repairs across Genki II (Lessons 13-23)
g2_repairs = {
    ('g2-l13-ex-3', 1): "Incorrect. Repeating ので consecutively in coordinate clauses (*美味しいので、静かなので、この店が好きです) is stylistically unacceptable and grammatically avoided for listing parallel reasons. Multiple reasons are listed using the pattern 〜し、〜し (美味しいし、静かだし).",
    ('g2-l13-ex-7', 2): "Incorrect. The conjectural/appearance suffix 〜そう (looks like) attaches to い-adjectives by dropping the final -い from the stem (美味しそう). Retaining an adverbial -く (*美味しくそう) is morphologically invalid.",
    ('g2-l13-ex-8', 2): "Incorrect. The irregular adjective いい (good) drops -い and shifts to the irregular stem よさ before 〜そう (よさそう, 'looks good'). It never inflects from base い- (*いくそう).",
    ('g2-l13-ex-9', 0): "Incorrect. Expressing frequency per time period follows the formula [Time Period] に [Number of times] without an additional particle after the frequency numeral (一日に三度). Inserting で (*一日に三度で) is grammatically invalid.",
    ('g2-l13-ex-10', 2): "Incorrect. 来る (くる) is an irregular verb. Its potential form is 来られる (こられる / これる in spoken Japanese). *きれます is an erroneous Godan-style conjugation that does not exist.",
    ('g2-l13-ex-11', 0): "Incorrect. Attaching the reason particle し directly to a な-adjective stem without the copula だ (*上手し) is strictly ungrammatical. な-adjectives require だ before し (上手だし、親切だし).",
    ('g2-l13-ex-12', 1): "Incorrect. きれい is a な-adjective (きれいな), not an い-adjective. Conjectural appearance suffix 〜そう attaches to な-adjectives by appending directly to the stem without inflecting to -く (*きれくそう is ungrammatical; the correct form is きれいそう).",
    ('g2-l14-ex-2', 1): "Incorrect. ほしがる is a Godan verb describing outward signs of desire. In polite non-past style, it conjugates into the continuous aspect 〜ほしがっています (or past 〜ほしがっていました). Attaching copula でした directly to the dictionary form (*ほしがるでした) is ungrammatical.",
    ('g2-l14-ex-5', 1): "Incorrect. The advice/recommendation formula 'how about doing X?' requires the conditional past ta-ra form 〜たらどうですか (相談したらどうですか). The conditional form 〜ば (*相談すればどうですか) does not form this conversational suggestion pattern.",
    ('g2-l14-ex-5', 2): "Incorrect. The contextual conditional なら does not form the suggestion pattern 〜たらどうですか (*相談するならどうですか). Giving advice to do an action uses the conditional past form たら.",
    ('g2-l14-ex-12', 0): "Incorrect. While the adjective ほしい takes the particle が to mark the desired item, the derived verb ほしがる is an active transitive verb and strictly marks its object with を (新しいコートをほしがっています; *コートがほしがっている is ungrammatical).",
    ('g2-l15-ex-1', 2): "Incorrect. 行った is the plain past form ('went'). Making an enthusiastic suggestion or invitation to go together ('Let's go!') requires the informal volitional form 行こう (or polite 行きましょう).",
    ('g2-l15-ex-2', 2): "Incorrect. 食べた is the plain past form ('ate'). Proposing to eat lunch together ('Let's eat!') requires the volitional form 食べよう.",
    ('g2-l15-ex-3', 0): "Incorrect. する is an irregular verb whose informal volitional form is しよう. It does not conjugate as an Ichidan verb (*すよう).",
    ('g2-l15-ex-3', 1): "Incorrect. The volitional form of する is しよう. *そう is a non-existent verb stem.",
    ('g2-l15-ex-3', 2): "Incorrect. Irregular verb する forms volitional しよう, not *しろう (which confuses volitional with imperative しろ).",
    ('g2-l15-ex-5', 1): "Incorrect. The intention pattern '〜ようと思います' (I think I will...) requires the volitional form of the verb (行こうと思います). Polite past 行きました cannot precede と思います to express intention.",
    ('g2-l15-ex-5', 2): "Incorrect. 行かない is the plain negative form ('not go'). Expressing an intention to go buy juice requires the affirmative volitional form 行こう.",
    ('g2-l15-ex-7', 2): "Incorrect. 〜ていく denotes performing an action and moving away. Asking someone to open the window for the speaker's benefit requires the benefactive request form 開けてくれませんか / 開けてください, not 開けていってください.",
    ('g2-l15-ex-8', 2): "Incorrect. 会う is a Godan verb ending in -う; its te-form is 会って, not *会いて. Furthermore, relative clauses modifying nouns require plain past 会った (昨日会った人), not a connective te-form.",
    ('g2-l15-ex-10', 0): "Correct. In casual spoken Japanese, the sequence 〜ておく regularly contracts into 〜とく (買っておく -> 買っとく). Appended to 買っ-, it forms the colloquial contraction 買っとくね.",
    ('g2-l15-ex-10', 1): "Incorrect. While 買っておく is the standard full uncontracted form, the prompt specifically asks for the colloquial spoken contraction (縮約形), which contracts 〜ておく into 〜とく (買っとく).",
    ('g2-l15-ex-10', 2): "Incorrect. *買っおき is morphologically incomplete; attaching bare stem おき directly to geminate 買っ- is ungrammatical.",
    ('g2-l15-ex-10', 3): "Incorrect. *買ったき is non-existent; the spoken contraction of 〜ておく is 〜とく (買っとく).",
    ('g2-l16-ex-2', 0): "Incorrect. Wishing someone good luck in conversational formula ('I hope you pass!') uses [Verb-ば / と / たら] いいですね. With dictionary form 合格する, particle と is required (合格するといいですね); たら requires the past stem 合格したら.",
    ('g2-l16-ex-5', 2): "Incorrect. 〜ていただく expresses receiving a favor from a superior or outside person ('I received the favor of someone doing X'). When the speaker (私) is the one performing the favor for a friend (友達に傘を貸して...), the giving auxiliary 〜てあげました is required.",
    ('g2-l16-ex-7', 2): "Incorrect. 〜てやる is used for giving favors to animals, plants, or significantly younger family members/subordinates. Using it for a classmate or friend like Mary is socially rude and inappropriate.",
    ('g2-l16-ex-12', 0): "Incorrect. The motion verb phrase 買い物に行く does not take a human person with particle に (*ゆいに買い物に行く). When performing a helpful errand for someone else's benefit, the beneficiary must be marked with のために (ゆいのために買い物に行ってあげました).",
    ('g2-l17-ex-2', 2): "Incorrect. Hearsay 〜そうだ (I heard that...) attaches to the plain dictionary form of predicates, including copula だ for な-adjectives (静かだそうだ). The connective te-form で (*静かでそうだ) cannot attach hearsay そうだ.",
    ('g2-l17-ex-4', 0): "Incorrect. The permission pattern for not doing an action ('you don't have to...') is 〜なくてもいいです. The phrase *〜ないでもいい is non-standard colloquial phrasing not accepted in standard textbook grammar.",
    ('g2-l17-ex-4', 2): "Incorrect. Classical/archaic negative continuative 〜ず (*来ずもいい) cannot form the modern conversational permission pattern 〜なくてもいい.",
    ('g2-l17-ex-5', 1): "Incorrect. Conjunction し coordinates reasons or parallel qualities. Marking a direct hearsay report ('I heard that Ken is getting married next month') requires the hearsay marker そうです (結婚するそうです).",
    ('g2-l17-ex-7', 2): "Incorrect. 間に means 'while / during the interval that...'. Brushing one's teeth occurs before going to bed, requiring the temporal prepositional pattern 前に (寝る前に), not during sleep.",
    ('g2-l17-ex-8', 2): "Incorrect. The pattern expressing 'after doing X' is [Verb-て] から. Combining negative continuative しないで with から (*宿題をしないでから) is ungrammatical; the sentence expresses doing homework first, then gaming (宿題をしてから).",
    ('g2-l17-ex-10', 0): "Incorrect. Hearsay 〜そうです attaches to the plain form of adjectives (難しかったそうです for past). The adverbial form 難しく cannot attach hearsay そうです.",
    ('g2-l17-ex-12', 0): "Incorrect. In standard Japanese, the time conjunction 前に ('before doing X') strictly requires the non-past dictionary form of the verb (日本へ来る前に), even when describing an event in the past. Using the past form (*来た前に) is ungrammatical.",
    ('g2-l18-ex-1', 2): "Incorrect. 開ける is a transitive verb meaning someone actively opens something. When a door opens on its own due to wind (風で), the intransitive verb 開く (開きました) is required.",
    ('g2-l18-ex-5', 1): "Incorrect. The conditional connector と attaches to the dictionary form (勉強すると), not to the hypothetical -e stem (*すれと). Furthermore, the idiomatic pattern for retrospective regret is strictly 〜ばよかった (勉強すればよかったです).",
    ('g2-l18-ex-5', 2): "Incorrect. Contextual conditional なら attaches to nouns or dictionary forms (勉強するなら), never to the conditional ba-stem (*すれなら).",
    ('g2-l18-ex-6', 2): "Incorrect. Classical/archaic negative continuative 〜ず cannot form the retrospective regret pattern (*買わずよかったです). Expressing negative regret ('I shouldn't have done') requires the conditional negative ending なければ (買わなければよかったです).",
    ('g2-l18-ex-7', 1): "Incorrect. 〜てみる denotes attempting or trying an action to see what happens. Dropping a phone and breaking the screen is an unintended, regrettable accident, requiring the completion/regret auxiliary 〜てしまいました (割ってしまいました).",
    ('g2-l18-ex-8', 0): "Incorrect. 〜ておく denotes doing an action in advance for future convenience. Finishing an entire book in one day because it was interesting describes total completion, which takes 〜てしまう (読んでしまいました).",
    ('g2-l18-ex-8', 1): "Incorrect. 〜てみる expresses a trial action ('try reading'). Finishing all the pages in a single day expresses complete thorough action, which takes the completion auxiliary 〜てしまう.",
    ('g2-l18-ex-8', 2): "Incorrect. 〜ている indicates continuous ongoing action or state. Finishing the whole book completely requires the completion auxiliary 〜てしまいました.",
    ('g2-l18-ex-10', 2): "Incorrect. 落ちていました describes a past continuous state or action in progress ('was falling'). Stating the completed momentary event of the wallet dropping out of the pocket takes simple past 落ちました.",
    ('g2-l19-ex-3', 1): "Incorrect. 申し上げる is a humble verb (謙譲語) used by the speaker to lower their own actions. When describing the speech of a respected superior (社長, company president), the honorific verb おっしゃいました (尊敬語) must be used.",
    ('g2-l19-ex-4', 1): "Incorrect. 見ました is neutral polite language (丁寧語). When asking a professor (先生) about their own action, respect requires the honorific verb ご覧になりました (尊敬語).",
    ('g2-l19-ex-4', 2): "Incorrect. The verb 見る is a single-mora stem and has the dedicated suppletive honorific verb ご覧になる (ご覧になりました). Regular formulaic honorific prefixing お+stem+になる does not apply to 見る; *お見になる is an ungrammatical overgeneralization.",
    ('g2-l19-ex-6', 2): "Incorrect. When thanking a professor or superior for writing a letter of recommendation, the respectful humble auxiliary くださって (先生が書いてくださって) or いただき is required; casual もらって is socially inappropriate.",
    ('g2-l19-ex-10', 1): "Incorrect. In respectful honorific speech (尊敬語), the verb 知っている has the dedicated suppletive form ご存じです. *ご知りですか incorrectly attempts to apply the prefix ご- to a native Japanese verb stem.",
    ('g2-l19-ex-10', 2): "Incorrect. While passive forms can function as light honorifics, 知る has the dedicated high-respect suppletive expression ご存じです (ご存じですか). *ご知られですか is an invalid hybrid.",
    ('g2-l20-ex-6', 2): "Incorrect. An embedded question ('whether Ken is coming tomorrow or not') requires the question particle か (来るかどうか / 来るか). The nominalizer こと turns a clause into a general noun fact, which cannot be followed by 分かりません to indicate uncertainty.",
    ('g2-l20-ex-7', 1): "Incorrect. The naming/quotative appositive pattern 'a [noun] called [Name]' follows the formula [Name] という [Noun] (「吾輩は猫である」という小説). Inserting the nominalizer particle の (*というの小説) is ungrammatical before a noun.",
    ('g2-l20-ex-7', 2): "Incorrect. The quotative particle と attaches to the verb いう (という); it does not take a な-adjective marker な (*というな小説).",
    ('g2-l20-ex-8', 2): "Incorrect. The suffix 〜やすい indicates ease of use ('easy to use'). The appearance suffix 〜そう indicates outward impression ('looks like'), which does not fit describing the functional ease of an electronic dictionary.",
    ('g2-l20-ex-10', 2): "Incorrect. The compound verb auxiliary 〜やすい inflects exactly like an い-adjective. Its polite past affirmative is 分かりやすかったです. Attaching copula でした directly to the non-past stem (*分かりやすいでした) is an ungrammatical hybrid.",
    ('g2-l21-ex-3', 1): "Incorrect. Specifying the time point at which a momentary event occurs (a package arrived) while a continuous state was ongoing requires 間に (寝ている間に). *時で is grammatically invalid to mark an event's time.",
    ('g2-l21-ex-4', 1): "Incorrect. Specifying a concurrent continuous duration ('throughout the time I was waiting') requires 間 (待っている間). *時で is an ungrammatical particle combination.",
    ('g2-l21-ex-4', 2): "Incorrect. The simultaneous action marker ながら attaches directly to the pre-masu stem of a verb (待ちながら); appending に (*ながらに) to mark time duration is ungrammatical.",
    ('g2-l21-ex-7', 2): "Incorrect. The suffering passive (迷惑受身) caused by natural rain falling takes the passive form 降られて (雨に降られて). The causative-passive form 降らされて means 'being forced to make rain fall', which is semantically nonsensical.",
    ('g2-l21-ex-9', 2): "Incorrect. Making a change of state to an adjective using する ('make something clean') requires adverbial inflection: な-adjectives take に (綺麗にする -> 綺麗にしましょう). The te-form で cannot mark the target state of する.",
    ('g2-l21-ex-12', 0): "Incorrect. Expressing a request for someone not to do something ('I want you not to tell anyone') requires the negative te-form 〜ないで followed by ほしい (言わないでほしいです). The conjunction 〜なくて expresses reasons/causes and cannot be used with ほしい (*言わなくてほしい is ungrammatical).",
    ('g2-l22-ex-1', 2): "Incorrect. The automatic/natural result of an operating machine or physical mechanism ('if you press this button, water comes out') requires the natural consequence conditional と (押すと). Contextual conditional なら is used for topics, advice, or suggestions, not mechanical cause-and-effect.",
    ('g2-l22-ex-2', 0): "Correct. For Ichidan/Ru-verbs like 食べる, the conditional 〜ば is formed by dropping -る and adding -れば (食べれば).",
    ('g2-l22-ex-2', 1): "Incorrect. While 〜たら is a conditional form, it uses the past stem (食べた -> 食べたら) and is not the 〜ば conditional form targeted by this drill.",
    ('g2-l22-ex-2', 2): "Incorrect. Appending bare ば directly to the stem (*食べば) is an ungrammatical error; Ichidan verbs strictly require -れば, whereas bare -ば applies only after the -e vowel of Godan verbs like 飲めば.",
    ('g2-l22-ex-2', 3): "Incorrect. Appending ると creates the と-conditional (食べると), not the requested 〜ば conditional form.",
    ('g2-l22-ex-3', 1): "Incorrect. The te-form なくて expresses cause or sequential negative action ('not doing and...'). A negative conditional requirement ('unless you hurry / if you don't hurry, you will miss the train') requires 〜なければ (急がなければ).",
    ('g2-l22-ex-3', 2): "Incorrect. The negative continuative prefix ず cannot form a conditional clause (*急がず、電車に間に合いません). Expressing 'if you don't hurry' requires the negative conditional form 急がなければ.",
    ('g2-l22-ex-5', 1): "Incorrect. When the adversative conjunction のに follows a noun or な-adjective in non-past affirmative, it takes な (日曜日なのに). Placing particle の before のに (*日曜日ののに) creates an ungrammatical stuttering particle duplicate.",
    ('g2-l22-ex-7', 0): "Incorrect. Passive/honorific 行かれました does not fit the causative structure where father initiates the action and assigns Ken (けんに) as the agent to go shopping. Causative 行かせました is required.",
    ('g2-l22-ex-7', 1): "Incorrect. Simple active 行きました ignores the agent relationship where father had Ken (けんに) do the errand. The causative form 行かせました is required.",
    ('g2-l22-ex-8', 1): "Incorrect. Asking for permission to introduce oneself ('Please let me introduce myself') requires the causative request form させてください (自己紹介をさせてください). *されさせて is a garbled non-existent voice combination.",
    ('g2-l22-ex-8', 2): "Incorrect. 〜てあげてください asks the listener to do a favor for someone else. When asking the listener for permission to let oneself speak, the polite causative request 〜させてください is required.",
    ('g2-l22-ex-10', 2): "Incorrect. The metaphorical simile 'a person like an angel' requires the simile noun/adjective よう (天使のような人). Suffix 〜そう indicates conjectural appearance based on direct visual evidence and cannot attach directly to a noun to create a simile (*天使のそうな人).",
    ('g2-l23-ex-1', 1): "Incorrect. Concessive condition 'even if it rains tomorrow, the match will be held' requires 〜ても (降っても). The hypothetical conditional 〜ば (降れば) means 'if it rains', which contradicts holding the game regardless of rain.",
    ('g2-l23-ex-2', 2): "Incorrect. Concessive condition for い-adjectives ('even if it is a little expensive') is formed with 〜くても (高くても). Bare past tense 高かった cannot connect concessively to express 'even if'.",
    ('g2-l23-ex-3', 1): "Incorrect. Deciding on a personal rule or course of action ('I decided to jog every morning') uses the decision formula 〜ことにする (ジョギングすることにしました). Noun はず expresses objective expectation or certainty, which cannot combine with にしました.",
    ('g2-l23-ex-3', 2): "Incorrect. わけ expresses logical reasoning or justification ('that is why / naturally'). It does not form a decision expression with にする (*ジョギングするわけにしました).",
    ('g2-l23-ex-5', 2): "Incorrect. 〜ことにしている expresses a personal habit or personal rule determined by oneself (e.g. 'I make it a rule to drink green tea'). A corporate transfer decided by one's organization or company is an external organizational decision, which requires 〜ことになっている (転勤することになっています).",
    ('g2-l23-ex-6', 1): "Incorrect. Simple passive 歌われました would mean the song was sung by the senior. Being coerced by a senior (先輩に) into singing against one's preference requires the causative-passive voice: 歌わせられました (or 歌わされました).",
    ('g2-l23-ex-6', 2): "Incorrect. Simple active 歌いました does not convey that the speaker was pressured or coerced by the senior (先輩に) to perform, missing the causative-passive nuance (歌わせられました).",
    ('g2-l23-ex-7', 1): "Incorrect. Passive/potential 食べられました means 'was able to eat' or 'was eaten'. Being pressured or forced to eat disliked bell peppers by parents requires the causative-passive form 食べさせられました.",
    ('g2-l23-ex-7', 2): "Incorrect. Simple active 食べました fails to express the involuntary coercion of being made to eat disliked food by parents, which requires the causative-passive 食べさせられました.",
    ('g2-l23-ex-10', 1): "Incorrect. The method/manner suffix 〜方 (かた) attaches directly to the pre-masu stem of a verb (読み方). 読ま is the negative stem (読まない), which cannot attach 方 (*読ま方).",
    ('g2-l23-ex-10', 2): "Incorrect. The suffix 〜方 requires the pre-masu stem (読み方). 読ん is the te-form / ta-form nasalized stem, which cannot attach 方 (*読ん方).",
    ('g2-l23-ex-12', 1): "Incorrect. The suffix 〜方 (how to do / manner of) attaches exclusively to the pre-masu stem of the verb (使い -> 使い方). The te-form cannot precede 方 (*使って方 is ungrammatical)."
}

for (eid, opt_idx), new_reason in g2_repairs.items():
    ex = ex_map[eid]
    ex['explanation']['options'][opt_idx]['reason'] = new_reason

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Successfully applied Genki II repairs!")
