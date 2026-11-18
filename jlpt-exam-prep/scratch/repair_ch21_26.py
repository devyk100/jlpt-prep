import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {q['id']: q for q in exercises}

# Dictionary of updates for Chapter 21 through 26
updates = {
    # ==================== Chapter 21 ====================
    'skm2-p1-c21-q1': {
        'context': 'Certainty of exam success knowing his tireless preparation.',
        'translation': 'Knowing how desperately he has poured in effort, he is bound to pass this actual exam without fail.',
        'overall': '話者の強い主観的確信や直感的な断定「絶対に〜に決まっている」を表す文脈には「〜に決まっている」を用います。',
        'options': [
            {'text': 'に決まっている', 'isCorrect': True, 'reason': '【正解】「彼のことだから絶対に…」という前提のもと、話者が確信をもって太鼓判を押す表現「〜に決まっている」が最も適切です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察可能な外見や状況からの推察（明かりが消えているところを見ると、留守とみえる）であり、本人の性格・努力を踏まえた話者の確信的な太鼓判には適しません。', 'trapCategory': 'nuance'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は将来好ましくない事態や事故が起きる客観的危険性を警告する表現であり、「合格する」という望ましい達成に用いるのは意味が矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は悪化や不祥事・失敗などの好ましくない事態を招く可能性を表すため、合格の確信に反します。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c21-q2': {
        'context': 'Forensic DNA evidence establishing suspect culpability beyond doubt.',
        'translation': 'Judging from the unshakeable fingerprints and DNA testing results left at the scene, he is undoubtedly the culprit.',
        'overall': '確たる客観的証拠に基づき論理的推量断定を行う文脈には「〜に相違ない」を用います。',
        'options': [
            {'text': 'に相違ない', 'isCorrect': True, 'reason': '【正解】DNA鑑定や指紋という客観的・確たる証拠に基づき、「〜に相違ない（間違いなく〜だ）」と論理的・断定的に推量するフォーマルな文脈に適合します。', 'trapCategory': ''},
            {'text': 'に決まっている', 'isCorrect': False, 'reason': '【不正解】「〜に決まっている」は話者の主観的・直感的な決めつけを表す日常的表現であり、科学捜査の客観的証拠から導く公的・論理的断定としては文体がくだけすぎています。', 'trapCategory': 'register'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は外見の様子から推し量る控えめな推察表現であり、動かぬ証拠から下される確固たる断定には弱すぎます。', 'trapCategory': 'nuance'},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は「〜ではないだろうか」と控えめに疑問や推量を投げかける表現であり、決定的な鑑定結果から犯人を特定する強い断定文脈に合いません。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c21-q3': {
        'context': 'Attributing a difficult project miracle success solely to constant daily diligence.',
        'translation': 'That he was able to miraculously make this difficult project a success is solely due to none other than his constant daily diligence.',
        'overall': '「〜のは…にほかならない」の呼応で、成功の唯一の決定打を力強く断定します。',
        'options': [
            {'text': 'にほかならない', 'isCorrect': True, 'reason': '【正解】「〜のは…にほかならない」の呼応構文で、「それ以外の何物でもなく、まさにそれだ」と真因や本質を力強く断定する表現です。', 'trapCategory': ''},
            {'text': 'に決まっている', 'isCorrect': False, 'reason': '【不正解】名詞「努力」に直接接続すると述語として「努力に決まっている（努力であるに違いない）」という話者の推量になり、「成功できたのは、ひとえに…」という原因特定の呼応構文になりません。', 'trapCategory': 'syntax'},
            {'text': 'に相違ない', 'isCorrect': False, 'reason': '【不正解】「〜に相違ない」は客観的データからの推量（〜であるに違いない）であり、「〜のは、ひとえに〜にほかならない」という唯一絶対の要因を断定・特定する構文には適合しません。', 'trapCategory': 'syntax'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】外見の様子からの推量表現であり、「成功できたのは…だ」という主語節に対して決定的な理由を述べる述語として成立しません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c21-q4': {
        'context': 'Deducing internal emotional agitation despite putting on a calm facade.',
        'translation': 'No matter how much he claims he is fine, on the inside he is bound to be deeply shaken and anxious.',
        'overall': '外面の平気な態度とは裏腹に、他者の内心の動揺を話者が確信をもって断定します。',
        'options': [
            {'text': 'に決まっている', 'isCorrect': True, 'reason': '【正解】本人の外面の言葉とは裏腹に、他者の内心の動揺に対して話者が「絶対にそうだ」と確信をもって断定・推量する表現です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は目に見える外部の様子からの推察であり、「内心は…」という外部から直接見えない心境を話者が主観的に決めつける文脈には適合しません。', 'trapCategory': 'nuance'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は将来起こりうる事故や危険への懸念・警告を表す表現であり、現在の他者の心理状態に対する推量断定には接続できません。', 'trapCategory': 'meaning'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は動詞ます形に接続して将来の悪影響の可能性（トラブルを引き起こしかねない）を表す表現であり、動詞テイル形「不安がっている」に接続して心理を推量する形式としては不成立です。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c21-q5': {
        'context': 'Declaring a magnificent monument to be the culmination of medieval master craftsmanship.',
        'translation': 'This magnificent structure is nothing other than the culmination of the extraordinary craft of skilled medieval master artisans.',
        'overall': '名工たちの卓越した技の結晶であることを力強く宣言・断定します。',
        'options': [
            {'text': 'にほかならない', 'isCorrect': True, 'reason': '【正解】歴史的建造物の本質・偉大さを「まさに名工たちの技の結晶そのものである」と力強く宣言・断定するフォーマルな論述表現です。', 'trapCategory': ''},
            {'text': 'に決まっている', 'isCorrect': False, 'reason': '【不正解】「結晶に決まっている」は話者の個人的・日常的な直感断定になり、建築遺物の歴史的・芸術的価値を厳かに論じる文体に合いません。', 'trapCategory': 'register'},
            {'text': 'に相違ない', 'isCorrect': False, 'reason': '【不正解】「〜に相違ない」は物的データからの推論（〜に違いない）であり、「〜は…の結晶にほかならない（他でもなくまさにそれだ）」という本質規定・礼賛の断定構文には「にほかならない」を用います。', 'trapCategory': 'nuance'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】外見観察に基づく控えめな推察であり、建造物の偉大な本質を堂々と述べる論説文として不適切です。', 'trapCategory': 'register'}
        ]
    },
    'skm2-p1-c21-q6': {
        'context': 'High-certainty deduction from character: the punctual Sato being late means an emergency must have occurred.',
        'translation': 'For that punctual Mr. Sato to be late for an appointment, an extraordinary unforeseen emergency must have occurred without a doubt.',
        'overall': '几帳面な人物の遅刻という確実な事実から、過去の緊急事態の発生を確信をもって推量します。',
        'options': [
            {'text': 'に違いない', 'isCorrect': True, 'reason': '【正解】几帳面な人物が遅刻したという確実な事実に基づいて、「よほどの事態が起きたはずだ」と確信をもって過去の事態を推量する表現です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察された様子から控えめに推測する表現であり、「よほどの事態が起きたに違いない」という人柄への強い信頼に基づく確信推量には弱すぎます。', 'trapCategory': 'nuance'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は将来起こる危険・被害を客観的に警告する表現であり、すでに発生した過去の事象「起きた」の推量には使えません。', 'trapCategory': 'tense'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は動詞ます形接続で将来の悪影響の可能性（事故を起こしかねない）を表すため、タ形「起きた」の後ろには接続できません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c21-q7': {
        'context': 'Forewarning that signing an opaque contract will inevitably cause severe trouble.',
        'translation': 'If you sign such an unreasonable and opaque contract, you are bound to be entangled in massive trouble later.',
        'overall': '不合理な契約への署名が必然的にトラブルを招くという自明の結末を強く断定・忠告します。',
        'options': [
            {'text': 'に決まっている', 'isCorrect': True, 'reason': '【正解】「〜ば…に決まっている」という条件に対して、火を見るより明らかな必然的結末を話者が確信をもって断定・忠告する表現です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察された事実から推し量る表現であり、仮定条件「署名すれば」に対する必然的結末の強い警告には適合しません。', 'trapCategory': 'syntax'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「巻き込まれる恐れがある」は客観的リスク評価の文体ですが、本問の「こんな不合理な契約書に署名すれば…（当然ひどい目に遭う）」という強い話し言葉の警告断定には「に決まっている」が最も自然です。', 'trapCategory': 'register'},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は「〜ではないだろうか」という控えめな問題提起であり、危険な契約に対する直接的で切迫した警告には合いません。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c21-q8': {
        'context': 'Attributing corporate turnaround solely to the power of fresh, unfettered ideas of new employees.',
        'translation': 'What saved the company from crisis was none other than the power of free and innovative thinking from the new employees.',
        'overall': '会社の危機を救った決定的な要因を「新入社員の発想の力」として唯一性をもって断定します。',
        'options': [
            {'text': 'にほかならない', 'isCorrect': True, 'reason': '【正解】「救ったのは…の力にほかならない」の呼応で、成功の決定打となった要因を他ならぬ唯一のものとして位置づける断定表現です。', 'trapCategory': ''},
            {'text': 'に決まっている', 'isCorrect': False, 'reason': '【不正解】名詞に直接接続すると個人的な当て推量（〜に決まっている）になり、企業の公式な功績評価や報告の文脈に合いません。', 'trapCategory': 'register'},
            {'text': 'に相違ない', 'isCorrect': False, 'reason': '【不正解】「〜に相違ない」は証拠に基づく推量（〜であるに違いない）であり、「〜のは…にほかならない」という主語節に対して決定的な要因を定義する述語として呼応しません。', 'trapCategory': 'syntax'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】推量形式であり、「危機を救ったのは…だ」という事実関係の断定的総括として成立しません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c21-q9': {
        'context': 'Deducing brake failure as the clear cause from corroborated eyewitness reports.',
        'translation': 'Since the eyewitness testimonies match so consistently, the cause of the accident was undoubtedly a brake failure.',
        'overall': '証言の一致という公的証拠に基づき、事故原因を論理的・断定的に推量します。',
        'options': [
            {'text': 'に相違ない', 'isCorrect': True, 'reason': '【正解】「〜以上」という前提のもと、複数の客観的証言の一致から「〜にあったことに相違ない」と論理的・公的に推論・断定する文脈に合致しています。', 'trapCategory': ''},
            {'text': 'に決まっている', 'isCorrect': False, 'reason': '【不正解】「〜に決まっている」は話者の主観的・直感的な決めつけを表し、客観的証言を分析して結論を下す事故調査のフォーマルな文脈には文体がくだけすぎています。', 'trapCategory': 'register'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は外見からの控えめな推察であり、「証言がこれほど一致している以上」という強力な根拠から導く断定には弱すぎます。', 'trapCategory': 'nuance'},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は控えめな疑問・意見提示であり、確定的な証言の一致から導く論理的帰結として曖昧すぎます。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c21-q10': {
        'context': 'Intuitive deduction that the child loves mother cooking from his enthusiastic eating.',
        'translation': 'Since he is eating with such obvious delight, he is bound to absolutely love his mother home cooking.',
        'overall': '目の前で美味しそうに食べている様子から、母親の料理が大好物であることを直感的に確信します。',
        'options': [
            {'text': 'に決まっている', 'isCorrect': True, 'reason': '【正解】「あんなに美味しそうに食べているのだから」という生き生きとした様子を目撃し、「大好きなに決まっている」と直感的に確信を述べる文脈に最適です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は客観的で改まった推察表現であり、家族の日常的な様子に対するくだけた親密な確信表明には「に決まっている」が自然です。', 'trapCategory': 'register'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は事故や病気などの危険の発生を警告する表現であり、「大好き」という肯定的な好意に対して用いるのは意味が矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は悪影響や不祥事を引き起こす危険性を表すため、好意の心情に接続できません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c21-q11': {
        'context': 'Philosophical declaration that science true goal is human welfare and peace.',
        'translation': 'The true purpose behind the rapid advancement of science and technology is none other than the aspiration for the welfare and peace of all humankind.',
        'overall': '科学技術の真の目的を全人類の平和と福祉への希求であると力強く宣言します。',
        'options': [
            {'text': 'にほかならない', 'isCorrect': True, 'reason': '【正解】「真の目的は…への希求にほかならない」の呼応で、理念や目的の唯一・最高の本質を力強く宣言・断定する論説文体です。', 'trapCategory': ''},
            {'text': 'に決まっている', 'isCorrect': False, 'reason': '【不正解】個人的な思い込み・決めつけの口語的ニュアンスになり、人類史的な崇高な理念を語る学術的・論説的文脈に調和しません。', 'trapCategory': 'register'},
            {'text': 'に相違ない', 'isCorrect': False, 'reason': '【不正解】「〜に相違ない」は客観的証拠からの推論（〜に違いない）であり、「真の目的は〜にほかならない（他でもなくこれだ）」という本質規定の断定には適しません。', 'trapCategory': 'nuance'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】外見観察に基づく控えめな推察であり、「真の目的は〜だ」という確信に満ちた主題提示と矛盾します。', 'trapCategory': 'register'}
        ]
    },
    'skm2-p1-c21-q12': {
        'context': 'Deductive certainty of an imminent violent storm from menacing atmospheric signs.',
        'translation': 'Given that dark clouds have gathered and gusts are raging, a severe storm is undoubtedly going to hit shortly.',
        'overall': '暗雲や突風という切迫した天候の兆候から、暴風雨の襲来を確信をもって推量します。',
        'options': [
            {'text': 'に違いない', 'isCorrect': True, 'reason': '【正解】「〜以上」という切迫した天候の兆候を根拠として、直後に起きる事態を確信をもって推量・断定する表現です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察から控えめに推測する表現であり、目前に迫る危機に対して切迫した確信を述べる文脈には弱すぎます。', 'trapCategory': 'nuance'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「襲来する恐れがある」は公的な気象警報などのリスク告知ですが、「〜以上、まもなく…」という目前の確実な事態に対する話者の確信推量としては「に違いない」が最適です。', 'trapCategory': 'register'},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は「〜ではないだろうか」という控えめな疑問・提起であり、目前に迫った暴風雨への切迫した判断には合いません。', 'trapCategory': 'modality'}
        ]
    },

    # ==================== Chapter 22 ====================
    'skm2-p1-c22-q1': {
        'context': 'Deducing sleep from darkened adjacent windows and complete silence.',
        'translation': 'Looking at how the lights next door are out and complete silence reigns, the resident appears to have gone to sleep already.',
        'overall': '外的な証拠・様子から推察して客観的推量を述べるには「〜とみえる」を用います。',
        'options': [
            {'text': 'とみえる', 'isCorrect': True, 'reason': '【正解】明かりが消えて静まり返っているという観察可能な様子から、客観的に控えめに推測する表現「〜とみえる」が文脈に最も合致します。', 'trapCategory': ''},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は論説文等で控えめに疑問や問題提起を行う表現であり、身近な日常の観察から就寝を推し量る文脈には文体が合いません。', 'trapCategory': 'register'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は将来の事故や災難などの好ましくない事態を警告する表現であり、「床に就いた（眠った）」という通常の行為の推測には使用できません。', 'trapCategory': 'meaning'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は悪影響や不祥事を引き起こす危険性を表す表現であり、また動詞タ形「床に就いた」の後ろには接続できません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c22-q2': {
        'context': 'Scholarly critique pondering whether digital excess distorts youth emotional growth.',
        'translation': 'Excessive digital dependency in modern society might bring about severe distortions in adolescents emotional growth, might it not?',
        'overall': '論文・演説において読者・聴衆に控えめに問題提起する表現には「〜のではあるまいか」を用います。',
        'options': [
            {'text': 'のではあるまいか', 'isCorrect': True, 'reason': '【正解】学術的・論説的な文脈において、「〜ではないだろうか」と読者や社会に向けて憂慮を込めて問題提起を行う「〜のではあるまいか」が最適です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は外見の観察証拠から推し量る表現であり、現代社会の構造的課題について警鐘を鳴らす論説の文体には調和しません。', 'trapCategory': 'nuance'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「もたらす恐れがある」も危険性を表せますが、文末の推量形式としての問題提起（〜ではないだろうか）という筆者の問いかけトーンには「のではあるまいか」が適合します。', 'trapCategory': 'modality'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は動詞ます形接続（もたらしかねない）であるため、辞書形「もたらす」には直接接続できません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c22-q3': {
        'context': 'Objective warning that neglecting demographic measures risks rural municipality extinction.',
        'translation': 'If drastic measures against population aging are neglected as is, there is a distinct danger that regional municipalities will become extinct.',
        'overall': '客観的に見て危険や破滅的結末が懸念される警告には「〜恐れがある」を用います。',
        'options': [
            {'text': '恐れがある', 'isCorrect': True, 'reason': '【正解】少子高齢化への放置が自治体消滅という重大な社会危機を招く客観的リスクを警告する公的文脈に「〜恐れがある」が最も適合します。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察された事実から控えめに推測する表現であり、政策放置に対する客観的な危機警告の論説には弱すぎます。', 'trapCategory': 'nuance'},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は「〜ではないか」という婉曲な疑問提起であり、公的な統計分析に基づく客観的危機の提示には「恐れがある」が適切です。', 'trapCategory': 'modality'},
            {'text': 'かねる', 'isCorrect': False, 'reason': '【不正解】「〜かねる」は心理的・立場的な困難による動作の拒絶（受け入れかねる）を表す動詞接続表現であり、事態の発生リスクを表す文脈には使えません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c22-q4': {
        'context': 'Warning that unauthorized removal of confidential corporate data could incur disciplinary dismissal.',
        'translation': 'If you take out confidential company data without permission, you could very well face the worst disciplinary dismissal.',
        'overall': '危険な行為が致命的な事態を招きかねない警告には「〜かねない」を用います。',
        'options': [
            {'text': 'かねない', 'isCorrect': True, 'reason': '【正解】動詞ます形「受け」に接続し、軽率な行為が「懲戒解雇」という破滅的な悪結果を引き起こす危険性を警告する「〜かねない」が最適です。', 'trapCategory': ''},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は動詞辞書形（受ける恐れがある）に接続するため、ます形語幹「受け」には直接接続できません。', 'trapCategory': 'formation'},
            {'text': 'かねる', 'isCorrect': False, 'reason': '【不正解】「〜かねる」は「自分の立場として〜できない」という丁寧な拒絶を表すため、「処分を受けかねる（処分を受けられない）」では意味が通りません。', 'trapCategory': 'meaning'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は外見の観察証拠からの推測であり、仮定条件「持ち出せば」に対する警告の帰結節としては成立しません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c22-q5': {
        'context': 'Deducing acute hunger from someone working hard all day without eating anything.',
        'translation': 'Looking at how he has been working earnestly since morning without eating a thing, he appears to be considerably hungry.',
        'overall': '観察した様子から控えめに客観的推量を述べるには「〜とみえる」を用います。',
        'options': [
            {'text': 'とみえる', 'isCorrect': True, 'reason': '【正解】「朝から何も口にせず懸命に働いているところを見ると」という客観的な観察事実に基づき、他人の状態を控えめに推し量る「〜とみえる」が最適です。', 'trapCategory': ''},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は論文等で社会的問題を提起する表現であり、目の前の人物の空腹を推し量る日常的観察には文体が合いません。', 'trapCategory': 'register'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は事故や病気などの将来の危険性を警告する表現であり、現在の生理的状態（空腹）の推測には不適です。', 'trapCategory': 'meaning'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は悪影響をもたらす動詞に接続する表現であり、名詞＋である「空腹である」には接続できません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c22-q6': {
        'context': 'Environmental warning questioning whether relentless human-centric exploitation permanently destroys Earth biosphere.',
        'translation': 'If we continue disorderly human-centered economic development, might we permanently destroy our irreplaceable global environment?',
        'overall': '地球環境の不可逆的破壊を危惧し、社会に向けて問いかける論説文には「〜のではあるまいか」を用います。',
        'options': [
            {'text': 'のではあるまいか', 'isCorrect': True, 'reason': '【正解】無秩序な開発への強い警鐘として、「破壊してしまうのではないだろうか」と読者に深く問いかける論説調の問題提起構文に合致しています。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は眼前で目撃した様子からの控えめな推察であり、地球規模の将来を憂慮するマクロな論説文体として不調和です。', 'trapCategory': 'nuance'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「破壊してしまう恐れがある」も文意としては通じますが、筆者の問いかけとしての反語的・問題提起的なニュアンス（〜のではあるまいか）と設問の選択肢構成から本問では問いかけ表現が意図されています。', 'trapCategory': 'modality'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は動詞ます形に接続するため、完了形「破壊してしまう」に直接重ねて接続することはできません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c22-q7': {
        'context': 'Public hazard alert that large earthquakes in dense wooden housing districts risk widespread conflagration.',
        'translation': 'In areas densely packed with aging wooden houses, there is a distinct danger that massive fires will spread once a major earthquake occurs.',
        'overall': '防災・安全上の重大な客観的リスクを社会に警告する表現には「〜恐れがある」を用います。',
        'options': [
            {'text': '恐れがある', 'isCorrect': True, 'reason': '【正解】木造家屋密集地域における火災延焼という、公共的・客観的な災害リスクを警告する文脈に「〜恐れがある」が最も自然に適合します。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察された事実から推測する表現であり、条件「ひとたび大地震が起きれば」に対する将来の災害リスク警告には適しません。', 'trapCategory': 'syntax'},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は主観的な問題提起や懸念の問いかけであり、都市防災の客観的なハザード警告としてはトーンがずれます。', 'trapCategory': 'register'},
            {'text': 'かねる', 'isCorrect': False, 'reason': '【不正解】「〜かねる」は動作主の心理的・立場的理由による拒絶を表すため、自然現象や災害の延焼には使用できません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c22-q8': {
        'context': 'Traffic hazard warning that smartphone distraction while driving could trigger catastrophic accidents.',
        'translation': 'Operating a smartphone while driving causes severe inattention and could very well trigger an irreversible major accident.',
        'overall': '運転中のスマホ操作という過失が致命的大事故を招く警告には「〜かねない」を用います。',
        'options': [
            {'text': 'かねない', 'isCorrect': True, 'reason': '【正解】動詞ます形「引き起こし」に接続し、危険な行為が取り返しのつかない大惨事を招く恐れがあることを強く警告する「〜かねない」が最適です。', 'trapCategory': ''},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は辞書形「引き起こす恐れがある」に接続するため、ます形語幹「引き起こし」には接続できません。', 'trapCategory': 'formation'},
            {'text': 'かねる', 'isCorrect': False, 'reason': '【不正解】「〜かねる」は「〜することができない」という意志的拒絶を表すため、大事故を引き起こすという危険事態の文脈には使えません。', 'trapCategory': 'meaning'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】外見観察からの推量であり、行為の危険性を訴える交通安全の忠告・警告文脈には不適合です。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c22-q9': {
        'context': 'Deducing severe emotional shock from someone silent, downcast posture.',
        'translation': 'Judging from how she keeps her head down without speaking to anyone, she appears to have been considerably shocked by the recent news.',
        'overall': '俯いて黙り込んでいる様子から、ショックの大きさを客観的に推察する「〜とみえる」を用います。',
        'options': [
            {'text': 'とみえる', 'isCorrect': True, 'reason': '【正解】「誰とも話さず俯いている様子からすると」という目撃可能な態度を手がかりに、他者の心理的衝撃を推し量る「〜とみえる」が最も適切です。', 'trapCategory': ''},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は論文調の問題提起であり、身近な個人の沈痛な様子を推察する日常的な観察文脈には硬すぎます。', 'trapCategory': 'register'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は将来起こりうる危険を警告する表現であり、すでに過去に発生した心理的ショック「受けた」には接続できません。', 'trapCategory': 'tense'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は将来の悪結果をもたらす動詞ます形接続（受けかねない）であるため、過去完了「受けた」の後ろには接続できません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c22-q10': {
        'context': 'Cultural policy proposition suggesting heritage preservation and tourism development truly thrive only in tandem.',
        'translation': 'Is it not true that the preservation of traditional culture and the promotion of tourism demonstrate their true value only when balanced in tandem?',
        'overall': '伝統文化の保護と観光の両立について、論説調で穏やかに問いかける「〜のではなかろうか」を用います。',
        'options': [
            {'text': 'のではなかろうか', 'isCorrect': True, 'reason': '【正解】文化行政・観光政策に関する論説文において、「〜ではないだろうか」と読者に穏やかに提言・問題提起を行う「〜のではなかろうか」が最も調和します。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は具体的な外見観察からの推測であり、文化論・政策論としての抽象的な提言には不適です。', 'trapCategory': 'nuance'},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は危険や災難への警告を表すため、「真の価値を発揮する」という望ましい肯定的な目標に用いるのは意味が矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は悪影響をもたらす危険性を表す表現であり、価値の発揮という肯定的な成果には使用できません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c22-q11': {
        'context': 'Official emergency alert: evacuation orders issued due to danger of massive flood from dike breaches.',
        'translation': 'Because there was a distinct danger of massive flooding occurring due to a dike rupture, an evacuation order was issued immediately.',
        'overall': '堤防決壊による洪水という客観的・公的な災害危険性を理由づける「〜恐れがある（ため）」を用います。',
        'options': [
            {'text': '恐れがある', 'isCorrect': True, 'reason': '【正解】行政による避難指示の発令理由として、洪水という重大な災害発生の客観的リスクを公的に説明する「〜恐れがある（ため）」が最適です。', 'trapCategory': ''},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察された様子からの推測表現であり、緊急の行政命令を正当化する公的根拠の記述として弱すぎます。', 'trapCategory': 'register'},
            {'text': 'ではあるまいか', 'isCorrect': False, 'reason': '【不正解】「〜ではあるまいか」は個人的な疑問・意見提示であり、避難指示という公式な行政処分の根拠節（〜ため）として文法・文体が合いません。', 'trapCategory': 'syntax'},
            {'text': 'かねる', 'isCorrect': False, 'reason': '【不正解】「〜かねる」は心理的・立場的理由による拒絶を表す動詞接続表現であり、自然災害の発生リスクを表す文脈には使えません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c22-q12': {
        'context': 'Workplace safety warning that sloppy controls could trigger a fatal incident.',
        'translation': 'If sloppy safety management continues as is, it could very well cause a fatal major incident someday.',
        'overall': '安全管理の怠慢が人命に関わる大惨事を招きうる警告には「〜かねない」を用います。',
        'options': [
            {'text': 'かねない', 'isCorrect': True, 'reason': '【正解】動詞ます形「起こし」に接続し、管理の杜撰さが致命的な事故・インシデントを引き起こす危険性を強く警告する「〜かねない」が最適です。', 'trapCategory': ''},
            {'text': '恐れがある', 'isCorrect': False, 'reason': '【不正解】「〜恐れがある」は辞書形「起こす恐れがある」に接続するため、ます形語幹「起こし」には接続できません。', 'trapCategory': 'formation'},
            {'text': 'かねる', 'isCorrect': False, 'reason': '【不正解】「〜かねる」は「〜できない」という能力・立場の拒絶を表すため、事故を起こす危険性の警告文脈には使えません。', 'trapCategory': 'meaning'},
            {'text': 'とみえる', 'isCorrect': False, 'reason': '【不正解】「〜とみえる」は観察された様子からの推測であり、仮定条件「続ければ」に対する警告の帰結節としては不適です。', 'trapCategory': 'syntax'}
        ]
    },

    # ==================== Chapter 23 ====================
    'skm2-p1-c23-q1': {
        'context': 'Universal human truth: parents naturally prioritize their children happiness.',
        'translation': 'Parents naturally pray first and foremost for their children happiness at all times.',
        'overall': '人間の本性や一般的な普遍的真理・本質を述べる表現には「〜ものだ」を用います。',
        'options': [
            {'text': 'もの', 'isCorrect': True, 'reason': '【正解】人間の親心という一般的な真理・普遍的な本質的性質を表す表現「〜ものだ」が最も適切です。', 'trapCategory': ''},
            {'text': 'というもの', 'isCorrect': False, 'reason': '【不正解】「〜というものだ」は「それこそがまさに〜というものだ」と特定の行為や事態に対して感情を込めて評価・共感する表現であり、一般的な親心の普遍則には「ものだ」が自然です。', 'trapCategory': 'nuance'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は「単に〜にすぎず大したものではない」と過小評価・限定する表現であり、普遍的な親の愛情に用いるのは不自然です。', 'trapCategory': 'meaning'},
            {'text': 'に越したことはない', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は「〜するのが最善だ・無難だ」という助言を表す表現であり、一般的な真理の感慨には合いません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q2': {
        'context': 'Natural altruism toward strangers exemplifying what true kindness is.',
        'translation': 'Reaching out naturally when seeing a stranger in distress—that is what true kindness is all about.',
        'overall': '「それこそが真の〜というものだ」と、特定の行為の本質を感情を込めて高く評価・肯定します。',
        'options': [
            {'text': 'というもの', 'isCorrect': True, 'reason': '【正解】「それこそが真の親切というものだ」の形で、目の前や話題に上がった具体的な行為を捉えて「これこそがまさにその本質だ」と強く共感・評価する表現です。', 'trapCategory': ''},
            {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】「親切ものだ」という接続は不自然であり、また特定の行為を捉えて「それこそが〜だ」と本質を定義・感慨する呼応には「というものだ」を用います。', 'trapCategory': 'syntax'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は限定・低評価を表すため、「それこそが真の親切だ」と称賛する文意と正反対になります。', 'trapCategory': 'meaning'},
            {'text': 'に越したことはない', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は事前の用心や予防の助言を表す表現であり、善行の本質を称える感慨文には合いません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q3': {
        'context': 'Clarifying that a statement is strictly personal opinion and not an official corporate stance.',
        'translation': 'My remarks this time are merely a personal opinion, and do not constitute an official stance representing the organization.',
        'overall': '「単に個人的な意見にすぎず、大それたものではない」と範囲を限定する「〜にすぎない」を用います。',
        'options': [
            {'text': 'にすぎず', 'isCorrect': True, 'reason': '【正解】「個人的な意見にすぎず、公式見解ではない」の対比で、自分の発言の範囲を限定し過大視を戒める表現「〜にすぎない（て形：にすぎず）」が最適です。', 'trapCategory': ''},
            {'text': 'というもので', 'isCorrect': False, 'reason': '【不正解】「〜というものだ」は事態の本質への強い共感・感慨を表す表現であり、自分の発言を限定・縮小する対比文脈には適合しません。', 'trapCategory': 'nuance'},
            {'text': 'に越したことはなく', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は用心・最善の忠告を表すため、発言の範囲を説明する文脈には使えません。', 'trapCategory': 'meaning'},
            {'text': 'べきではなく', 'isCorrect': False, 'reason': '【不正解】「〜べきではない」は義務や禁止を表すため、「意見べきではなく」という名詞接続としても文法的に不成立です。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c23-q4': {
        'context': 'Travel safety advice: researching local emergency contacts in advance is the safest approach.',
        'translation': 'If you are going on an overseas trip, there is nothing better than researching local safety conditions and emergency contacts in advance.',
        'overall': '海外旅行時の事前準備として「〜しておくに越したことはない（それが最善だ）」と助言します。',
        'options': [
            {'text': 'に越したことはない', 'isCorrect': True, 'reason': '【正解】旅行前の用心や安全対策として、「もちろんそうしておくのが一番安全で最善だ」と勧める表現「〜に越したことはない」が最も適切です。', 'trapCategory': ''},
            {'text': 'ものだ', 'isCorrect': False, 'reason': '【不正解】「〜ものだ」は一般的真理や道徳的教訓を表し、「旅行に行くなら事前に調べておくのが無難だ・最善だ」という用心・助言のニュアンスには「に越したことはない」が適合します。', 'trapCategory': 'nuance'},
            {'text': 'というものだ', 'isCorrect': False, 'reason': '【不正解】「〜というものだ」は特定の事態への感慨・共感を述べる表現であり、事前の安全対策を促す忠告には合いません。', 'trapCategory': 'nuance'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は限定・低評価を表すため、「調べておくことにすぎない」では意味が通りません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q5': {
        'context': 'Professional ethics: as a member of society, one must strictly observe agreed appointments and deadlines.',
        'translation': 'As a working professional, one must strictly observe agreed times and deadlines.',
        'overall': '社会人としての当然の義務や倫理的責任を強く主張するには「〜べきだ」を用います。',
        'options': [
            {'text': 'べき', 'isCorrect': True, 'reason': '【正解】「社会人たるもの…守るべきだ」の呼応で、社会的立場に伴う当然の義務・倫理的責務を力強く主張する表現です。', 'trapCategory': ''},
            {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】「〜ものだ」も一般的な教訓として使えますが、「社会人たるもの…」という強い身分・立場規範の呼応には義務・当然性を表す「べきだ」が最も自然です。', 'trapCategory': 'nuance'},
            {'text': 'というもの', 'isCorrect': False, 'reason': '【不正解】動詞辞書形「守る」に「というものだ」を直接接続して義務・規範を述べる表現としては文法・文体上不適切です。', 'trapCategory': 'formation'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は限定・軽視を表すため、社会人としての厳格な義務を説く文脈に矛盾します。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q6': {
        'context': 'Empathetic human emotion: shedding tears when witnessing others misfortune is truly natural.',
        'translation': 'To shed tears upon witnessing others misfortune is what truly natural human emotion is all about.',
        'overall': '他者の不幸に涙することが人間として真に自然な感情の本質であることを力説します。',
        'options': [
            {'text': 'というもの', 'isCorrect': True, 'reason': '【正解】「〜のは…というものだ」の構文で、「それこそがまさに人間の自然な感情というものだ」と事態の本質を力強く肯定・共感する表現です。', 'trapCategory': ''},
            {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】名詞「感情」に直接「ものだ」を接続することはできず、「感情というものだ」とする必要があります。', 'trapCategory': 'formation'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は「大したことではない」という過小評価になり、人間の温かい感情の本質を称える文脈と反します。', 'trapCategory': 'meaning'},
            {'text': 'に越したことはない', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は用心・助言の表現であり、自然な感情の本質を語る文脈には合いません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q7': {
        'context': 'Philosophical observation: even cutting-edge machines are merely lumps of iron without proper human operation.',
        'translation': 'No matter how cutting-edge a machine may be, unless humans operate it correctly, it is merely a lump of iron.',
        'overall': '「正しく操作しなければ単なる鉄の塊にすぎない」と限定・過小評価する表現を用います。',
        'options': [
            {'text': 'にすぎない', 'isCorrect': True, 'reason': '【正解】「単なる…にすぎない（ただ〜であるだけでそれ以上のものではない）」の呼応で、最新機械でも操作次第で無価値になると限定する表現です。', 'trapCategory': ''},
            {'text': 'というものだ', 'isCorrect': False, 'reason': '【不正解】「単なる鉄の塊というものだ」では感慨の強調になり、「単なる…」という過小評価の限定構文（にすぎない）と呼応しません。', 'trapCategory': 'syntax'},
            {'text': 'ものだ', 'isCorrect': False, 'reason': '【不正解】名詞「塊」に「ものだ」を直接接続することはできず、また「単なる〜」との呼応としても不成立です。', 'trapCategory': 'formation'},
            {'text': 'に越したことはない', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は用心・最善の助言を表すため、機械の本質を限定する文脈には使えません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q8': {
        'context': 'Disaster preparedness advice: it is always best to secure extra emergency food and drinking water.',
        'translation': 'As preparation for disaster times, there is nothing better than securing an ample supply of emergency food and drinking water.',
        'overall': '災害への備えとして「多めに確保しておくのに越したことはない」と最善の用心を助言します。',
        'options': [
            {'text': 'に越したことはない', 'isCorrect': True, 'reason': '【正解】防災対策として「多ければ多いほど安心で最善だ」という常識的な用心を勧める「〜に越したことはない」が最適です。', 'trapCategory': ''},
            {'text': 'ものだ', 'isCorrect': False, 'reason': '【不正解】「〜ものだ」は一般的真理を表しますが、「非常食は多めに確保しておくのが一番無難だ」という用心の助言には「に越したことはない」が合致します。', 'trapCategory': 'nuance'},
            {'text': 'というものだ', 'isCorrect': False, 'reason': '【不正解】「〜というものだ」は事態への感慨・共感を述べる表現であり、防災準備の助言には合いません。', 'trapCategory': 'nuance'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は限定・低評価を表すため、「確保しておくことにすぎない」では意味が通りません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q9': {
        'context': 'Life lesson for youth: one should boldly try challenges without fearing failure while young.',
        'translation': 'While one is young, one should boldly take on challenges without fearing failure.',
        'overall': '若者に対する一般的・道徳的な教訓・助言として「〜してみるものだ」を用います。',
        'options': [
            {'text': 'もの', 'isCorrect': True, 'reason': '【正解】目上の者や社会通念から「若いうちは〜するものだ」と一般的真理・人生の教訓として助言・激励する表現です。', 'trapCategory': ''},
            {'text': 'というもの', 'isCorrect': False, 'reason': '【不正解】「〜というものだ」は「それこそがまさに〜だ」という特定の事態に対する感慨・共感であり、一般的な教訓助言には「ものだ」を用います。', 'trapCategory': 'nuance'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は過小評価・限定を表すため、果敢な挑戦を促す激励の文脈に反します。', 'trapCategory': 'meaning'},
            {'text': 'に越したことはない', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は用心・リスク回避の助言を表すため、若者の果敢な挑戦を説く人生論には調和しません。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c23-q10': {
        'context': 'Moral obligation: upon witnessing illicit misconduct, one should muster courage and disclose the facts.',
        'translation': 'Since you witnessed an illicit act, you should muster courage and disclose the facts.',
        'overall': '不正を目撃した以上、勇気を出して公表するのが道義的・社会的当然の義務であると主張します。',
        'options': [
            {'text': 'べき', 'isCorrect': True, 'reason': '【正解】「〜以上、…公表するべきだ」の呼応で、正義や道義に基づく社会的義務・当然の行動を力強く主張する表現です。', 'trapCategory': ''},
            {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】「〜ものだ」は一般的な普遍的真理を表しますが、個別の不正目撃に対する具体的な道義的行動の要求には「べきだ」が適切です。', 'trapCategory': 'nuance'},
            {'text': 'というもの', 'isCorrect': False, 'reason': '【不正解】動詞辞書形に直接接続して行動の義務を促す用法はありません。', 'trapCategory': 'formation'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は限定・軽視を表すため、重大な不正告発の決断を促す文脈に矛盾します。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q11': {
        'context': 'Life philosophy: losing one health leaves one with nothing, no matter how rich one becomes.',
        'translation': 'No matter how rich you become, losing your health means losing everything—that is what life truly is.',
        'overall': '健康を損なっては元も子もないという事態の本質を深く実感・感慨を込めて肯定します。',
        'options': [
            {'text': 'というもの', 'isCorrect': True, 'reason': '【正解】「元も子もないというものだ」の慣用的な表現で、「健康を失えば全てが無意味になる、それこそが真理だ」と事態の本質を強く共感・評価する表現です。', 'trapCategory': ''},
            {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】慣用句「元も子もない」の後ろに直接「ものだ」を続けるより、「元も子もないというものだ」とするのが自然な評価表現です。', 'trapCategory': 'syntax'},
            {'text': 'にすぎない', 'isCorrect': False, 'reason': '【不正解】「〜にすぎない」は限定・低評価を表すため、人生の根本的な戒めを述べる文脈に合いません。', 'trapCategory': 'meaning'},
            {'text': 'に越したことはない', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は「〜が最善だ」という助言を表すため、「元も子もない」という損失状態に接続できません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c23-q12': {
        'context': 'Practical wisdom: linguistic knowledge without actual use is merely symbols inside one head.',
        'translation': 'No matter how much language knowledge you have, unless you actually use it, it is merely symbols inside your head.',
        'overall': '使わなければ単なる記号にすぎないと限定・過小評価する表現を用います。',
        'options': [
            {'text': 'にすぎない', 'isCorrect': True, 'reason': '【正解】「いくら…あっても、実際に使わなければ単なる…にすぎない」の呼応で、実践を伴わない知識を「ただの記号にすぎない」と限定する表現です。', 'trapCategory': ''},
            {'text': 'というものだ', 'isCorrect': False, 'reason': '【不正解】「単なる記号というものだ」では感慨の強調になり、実践なき知識の無力さを限定する「にすぎない」が最適です。', 'trapCategory': 'nuance'},
            {'text': 'ものだ', 'isCorrect': False, 'reason': '【不正解】名詞「記号」に「ものだ」を直接接続することは文法的にできません。', 'trapCategory': 'formation'},
            {'text': 'に越したことはない', 'isCorrect': False, 'reason': '【不正解】「〜に越したことはない」は用心・助言を表すため、知識の実態を限定評価する文脈には使えません。', 'trapCategory': 'meaning'}
        ]
    },

    # ==================== Chapter 24 ====================
    'skm2-p1-c24-q1': {
        'context': 'Study advice: if you want to improve Japanese listening dramatically, you should listen to real news daily.',
        'translation': 'If you want to dramatically improve your Japanese listening comprehension, you should listen to authentic news even a little bit every day.',
        'overall': '相手に対して「〜するのが一番良い・〜しなさい」と間接的に強い助言を行う「〜ことだ」を用います。',
        'options': [
            {'text': 'こと', 'isCorrect': True, 'reason': '【正解】「〜したいなら…ことだ」の形で、目標達成のための最善の忠告・助言を述べる表現「〜ことだ」が最適です。', 'trapCategory': ''},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「〜(よ)うではないか」は「一緒に〜しよう」という周囲への呼びかけ・勧誘であり、「あなたが〜したいなら」という個人への助言文脈には合いません。', 'trapCategory': 'modality'},
            {'text': 'ことはない', 'isCorrect': False, 'reason': '【不正解】「〜ことはない」は「〜する必要はない」という不要を表すため、「毎日ニュースを聴く必要はない」となり、聴解力向上の助言と矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「〜まい」は否定の意志や否定推量を表すため、毎日の学習を勧める文意になりません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c24-q2': {
        'context': 'Call to corporate solidarity: now facing difficult challenges, let us all join forces together as employees!',
        'translation': 'Now that we are facing difficult challenges, let all employees join forces and unite together as one!',
        'overall': '集団や仲間に対して「皆で一緒に〜しよう！」と力強く呼びかける勧誘表現「〜(よ)うではないか」を用います。',
        'options': [
            {'text': 'ようではないか', 'isCorrect': True, 'reason': '【正解】「社員全員が一丸となって力を合わせようではないか！」と、困難を乗り越えるために全員へ熱く結束を呼びかける勧誘表現です。', 'trapCategory': ''},
            {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「〜ことだ」は個人への助言・忠告の表現であり、文末感嘆符を伴って集団に一丸の行動を呼びかける勧誘には使えません。', 'trapCategory': 'modality'},
            {'text': 'ことはない', 'isCorrect': False, 'reason': '【不正解】「〜ことはない」は「〜する必要はない」という意味になり、力を合わせる呼びかけと正反対になります。', 'trapCategory': 'meaning'},
            {'text': 'まいか', 'isCorrect': False, 'reason': '【不正解】「〜まいか」は「〜ないだろうか」という疑問・控えめな推量であり、力強い決起の呼びかけには「〜(よ)うではないか」を用います。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c24-q3': {
        'context': 'Comforting someone in distress: since the counterpart fault is clear, you do not need to blame yourself.',
        'translation': 'Since the other party fault is obvious, there is no need for you to blame yourself and agonize over it.',
        'overall': '相手に対して「その必要はないから気にしないで」と励ます表現「〜ことはない」を用います。',
        'options': [
            {'text': 'ことはない', 'isCorrect': True, 'reason': '【正解】「相手の過失は明白なのだから…思い悩むことはない（悩む必要はない）」と、不要を告げて相手を安心させる表現です。', 'trapCategory': ''},
            {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「思い悩むことだ」とすると「思い悩み続けなさい」という助言になり、無実の相手を慰める文脈に著しく矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「〜(よ)うではないか」は勧誘の呼びかけであり、「あなたが思い悩む」という相手の自責を慰める文脈に合いません。', 'trapCategory': 'modality'},
            {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「〜まい」は話者の否定の意志（二度と行くまい）を表すため、相手への慰め・助言には使えません。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c24-q4': {
        'context': 'Strong negative determination: after such humiliating betrayal, I will never be fooled by that man sweet words again.',
        'translation': 'Having experienced such a humiliating betrayal, I will never again be deceived by that man sweet words.',
        'overall': '「二度と〜するまい（絶対に〜しない）」という話者の固い否定の決意を述べる表現を用います。',
        'options': [
            {'text': 'るまい', 'isCorrect': True, 'reason': '【正解】動詞一段「騙される」の未然・辞書形に接続し、「二度と騙されるまい（二度と騙されるものか）」と強い否定の決意を表す表現です。', 'trapCategory': ''},
            {'text': 'ることだ', 'isCorrect': False, 'reason': '【不正解】「騙されることだ」とすると「騙されなさい」という助言になってしまい、裏切りへの怒りと決意の文脈に反します。', 'trapCategory': 'meaning'},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「〜(よ)うではないか」は勧誘の呼びかけであり、自分自身の拒絶の決意には使えません。', 'trapCategory': 'modality'},
            {'text': 'ることはない', 'isCorrect': False, 'reason': '【不正解】「騙されることはない」は「騙される可能性・必要性はない」という客観判断になり、「二度と…」という話者自身の固い主観的意志表明になりません。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c24-q5': {
        'context': 'Health advice: if you want to maintain health, you should refrain from overeating and lead a regular life.',
        'translation': 'If you want to maintain your health, you should refrain from overeating and lead a regular, orderly lifestyle.',
        'overall': '健康維持のための忠告として「〜ことだ（〜するのがよい）」を用います。',
        'options': [
            {'text': 'こと', 'isCorrect': True, 'reason': '【正解】「健康を維持したいなら…規則正しい生活を送ることだ」と、望ましい生活習慣を促す助言表現です。', 'trapCategory': ''},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「〜(よ)うではないか」は集団への呼びかけであり、「あなたが健康を維持したいなら」という個人の条件設定に合いません。', 'trapCategory': 'modality'},
            {'text': 'ことはない', 'isCorrect': False, 'reason': '【不正解】「規則正しい生活を送ることはない（送る必要はない）」となり、健康指導の意図と正反対になります。', 'trapCategory': 'meaning'},
            {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】否定の意志・推量であり、生活習慣の指導文脈に合いません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c24-q6': {
        'context': 'Social aspiration: for the children who bear the future, let us build a peaceful and prosperous society!',
        'translation': 'For the children who carry the future, let us build up a peaceful and prosperous society together!',
        'overall': '子どもたちの未来のために社会を築こうと周囲へ呼びかける「〜(よ)うではないか」を用います。',
        'options': [
            {'text': 'ようではないか', 'isCorrect': True, 'reason': '【正解】動詞連用形「築き上げ」に接続し、「築き上げようではないか！」と崇高な目標に向けて協力を呼びかける勧誘表現です。', 'trapCategory': ''},
            {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「〜ことだ」は個人への助言であり、文末感嘆符を伴って公衆に結束を訴える演説調の呼びかけには使えません。', 'trapCategory': 'modality'},
            {'text': 'ことはない', 'isCorrect': False, 'reason': '【不正解】「築き上げることはない」は否定表現になり、子どもたちのために社会を築くという目標と矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'まいか', 'isCorrect': False, 'reason': '【不正解】「〜まいか」は否定推量や疑念を表すため、前向きな力強いスローガンには「〜(よ)うではないか」が適合します。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c24-q7': {
        'context': 'Reassuring a colleague: it was merely a minor calculation error, so you do not need to be so deeply downcast.',
        'translation': 'It was merely a trivial calculation mistake, so there is no need for you to be so deeply downcast.',
        'overall': '些細なミスなのだから「そんなに落ち込むことはない（必要はない）」と励ます表現を用います。',
        'options': [
            {'text': 'ことはない', 'isCorrect': True, 'reason': '【正解】「些細なミスにすぎないのだから…落ち込むことはない」と、相手の過度な落胆を慰め、思い詰める必要がないことを伝える表現です。', 'trapCategory': ''},
            {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「落ち込むことだ」では「深刻に落ち込みなさい」という命令・助言になり、同僚への慰めの文脈と正反対になります。', 'trapCategory': 'meaning'},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「落ち込もうではないか」という勧誘になり、落ち込むことを勧める不自然な文になります。', 'trapCategory': 'meaning'},
            {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「〜まい」は自分の否定意志を表すため、相手への助言・慰めの文脈には使えません。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c24-q8': {
        'context': 'Resolute determination: no matter how bitter the trials ahead, I will never whine and give up midway.',
        'translation': 'No matter what bitter trials may await, I will never utter weak complaints and give up midway.',
        'overall': 'どんな試練があっても決して挫折しないという固い否定の決意を表す「〜まい」を用います。',
        'options': [
            {'text': 'るまい', 'isCorrect': True, 'reason': '【正解】サ変動詞「挫折する」に接続し、「挫折するまい（絶対に挫折しないぞ）」と試練に立ち向かう強い否定意志を表す表現です。', 'trapCategory': ''},
            {'text': 'ることだ', 'isCorrect': False, 'reason': '【不正解】「挫折することだ」では「挫折しなさい」という助言になり、試練に耐えて前進する文脈と矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「挫折しようではないか」という勧誘になり、途中で諦めることを勧める意味になってしまいます。', 'trapCategory': 'meaning'},
            {'text': 'ることはない', 'isCorrect': False, 'reason': '【不正解】「挫折することはない」は客観的な可能性の否定であり、「どんなに苦しい試練が待ち受けていようとも…」という話者自身の悲壮な決意表明には「〜まい」が最適です。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c24-q9': {
        'context': 'Exam strategy advice: if aiming for a high score, you should thoroughly review mistakes and overcome weaknesses.',
        'translation': 'If you are aiming for a high score on the exam, you should thoroughly review the questions you missed and overcome your weaknesses.',
        'overall': '高得点を狙う受験生への確実な助言として「〜ことだ」を用います。',
        'options': [
            {'text': 'こと', 'isCorrect': True, 'reason': '【正解】「高得点を狙うなら…克服することだ」と、試験対策の最善の方法を指導・忠告する表現です。', 'trapCategory': ''},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「〜(よ)うではないか」は集団への呼びかけであり、「あなたが狙うなら」という個人条件節に合いません。', 'trapCategory': 'modality'},
            {'text': 'ことはない', 'isCorrect': False, 'reason': '【不正解】「克服することはない（克服する必要はない）」となり、勉強のアドバイスとして破綻します。', 'trapCategory': 'meaning'},
            {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】否定の意志表現であり、弱点克服を促す指導文脈に合いません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c24-q10': {
        'context': 'Civic call to action: to protect local safety, let all residents carry out crime-prevention patrols together!',
        'translation': 'In order to protect local community safety, let all residents carry out crime-prevention patrols together!',
        'overall': '地域安全のために住民全員へ防犯パトロールの実施を呼びかける「〜(よ)うではないか」を用います。',
        'options': [
            {'text': 'ようではないか', 'isCorrect': True, 'reason': '【正解】サ変動詞語幹「実施し」に接続し、「実施しようではないか！」と住民全体へ共同の防犯活動を力強く呼びかける勧誘表現です。', 'trapCategory': ''},
            {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「〜ことだ」は個人への助言であり、地域住民全体への一斉の行動呼びかけには文体が合いません。', 'trapCategory': 'modality'},
            {'text': 'ことはない', 'isCorrect': False, 'reason': '【不正解】「実施することはない」は「実施する必要はない」という意味になり、安全対策の文脈に反します。', 'trapCategory': 'meaning'},
            {'text': 'まいか', 'isCorrect': False, 'reason': '【不正解】「〜まいか」は否定推量や躊躇を表すため、住民への積極的な結束の呼びかけには「〜(よ)うではないか」が適切です。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c24-q11': {
        'context': 'Reassuring a client: since specialists will support you kindly, you do not need to worry needlessly alone.',
        'translation': 'Since specialists will kindly support you, there is no need for you to worry needlessly all by yourself.',
        'overall': '専門家がサポートしてくれるのだから「余計な心配をすることはない（必要はない）」と安心させます。',
        'options': [
            {'text': 'ることはない', 'isCorrect': True, 'reason': '【正解】サ変動詞「心配する」に接続し、「余計な心配をすることはない（する必要はない）」と不要を告げて安心させる表現です。', 'trapCategory': ''},
            {'text': 'ることだ', 'isCorrect': False, 'reason': '【不正解】「心配することだ」とすると「余計な心配をしなさい」という助言になり、専門家の支援がある文脈と矛盾します。', 'trapCategory': 'meaning'},
            {'text': 'ようではないか', 'isCorrect': False, 'reason': '【不正解】「心配しようではないか」という勧誘になり、心配することを勧める不自然な文になります。', 'trapCategory': 'meaning'},
            {'text': 'るまい', 'isCorrect': False, 'reason': '【不正解】「〜まい」は話者の否定意志を表すため、相手に対する慰め・アドバイスには使えません。', 'trapCategory': 'modality'}
        ]
    },
    'skm2-p1-c24-q12': {
        'context': 'Unyielding study pledge: until I fulfill the dream of passing my target school, I will never abandon my exam studies.',
        'translation': 'Until I fulfill my dream of passing my target school, I will never abandon my exam studies under any circumstances.',
        'overall': '合格の夢を果たすまで絶対に受験勉強を投げ出さないという不退転の決意を表す「〜まい」を用います。',
        'options': [
            {'text': 'すまい', 'isCorrect': True, 'reason': '【正解】動詞五段「投げ出す」に接続し、「絶対に投げ出すまい（絶対に投げ出さないぞ）」と強い否定の決意を表す表現です。', 'trapCategory': ''},
            {'text': 'すことだ', 'isCorrect': False, 'reason': '【不正解】「投げ出すことだ」では「投げ出しなさい」という助言になり、合格を目指す決意の文脈と正反対になります。', 'trapCategory': 'meaning'},
            {'text': 'そうではないか', 'isCorrect': False, 'reason': '【不正解】「投げ出そうではないか」という勧誘になり、勉強を諦めることを勧める意味になってしまいます。', 'trapCategory': 'meaning'},
            {'text': 'すことはない', 'isCorrect': False, 'reason': '【不正解】「投げ出すことはない」は「投げ出す必要はない」という客観的な言明であり、夢に向かって自分自身を奮い立たせる主観的決意表明には「〜まい」が最適です。', 'trapCategory': 'nuance'}
        ]
    },

    # ==================== Chapter 25 ====================
    'skm2-p1-c25-q1': {
        'context': 'Severe pre-presentation anxiety causing uncontrollably rapid heartbeats.',
        'translation': 'Right before the crucial presentation, my heart was pounding so violently from extreme nerves that I could not bear it.',
        'overall': '生理的・身体的衝動や強烈な感情が抑えきれない状態を表す「〜てたまらない」を用います。',
        'options': [
            {'text': 'たまらない', 'isCorrect': True, 'reason': '【正解】心臓の激しい鼓動や過度の緊張という肉体的・感情的苦痛が限界に達し「〜てたまらない（我慢できないほどだ）」と訴える表現です。', 'trapCategory': ''},
            {'text': 'いられない', 'isCorrect': False, 'reason': '【不正解】「〜てはいられない」は「〜している状況ではない」という行動の制約を表すため、心臓の鼓動という生理現象には接続できません。', 'trapCategory': 'syntax'},
            {'text': 'ざるを得ない', 'isCorrect': False, 'reason': '【不正解】「〜ざるを得ない」は「やむを得ず〜する」という意志的行動の強制を表すため、心臓の自然な鼓動には使えません。', 'trapCategory': 'meaning'},
            {'text': 'ならない', 'isCorrect': False, 'reason': '【不正解】「〜てならない」は自然と心に湧き上がる感情や漠然とした予感（気になってならない）に多く用いられ、心臓の激しい身体的苦痛には「たまらない」が最も自然です。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c25-q2': {
        'context': 'Deep emotional isolation returning to an empty room upon first living alone.',
        'translation': 'When I returned to an empty room after starting to live alone for the first time, I felt uncontrollably lonely.',
        'overall': '一人暮らしの部屋で自然と心に湧き上がって抑えられない寂しさを表す「〜てならなかった」を用います。',
        'options': [
            {'text': 'ならなかった', 'isCorrect': True, 'reason': '【正解】「寂しくてならなかった」の形で、内面から自然と止めどなく湧き上がる孤独感・情緒的感情を表すのに最適な表現です。', 'trapCategory': ''},
            {'text': 'いられなかった', 'isCorrect': False, 'reason': '【不正解】「〜てはいられない」は行動の中止・着手を表すため、「寂しくていられなかった」という感情表現としては成立しません。', 'trapCategory': 'syntax'},
            {'text': 'ざるを得なかった', 'isCorrect': False, 'reason': '【不正解】「〜ざるを得ない」は動詞未然形に接続してやむを得ず行う行動を表すため、イ形容詞「寂しくて」には接続できません。', 'trapCategory': 'formation'},
            {'text': 'かねなかった', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は悪影響をもたらす危険性を表す動詞接続表現であり、感情形容詞には接続できません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c25-q3': {
        'context': 'Painful corporate restructuring: severe business deterioration forced the management to execute layoffs.',
        'translation': 'Because company performance deteriorated severely, as a bitter decision we were forced to embark on staff reductions.',
        'overall': '業績悪化という不可避の状況により、苦渋の決断としてやむを得ず行動せざるを得ない状態を表します。',
        'options': [
            {'text': 'らざるを得ない', 'isCorrect': True, 'reason': '【正解】動詞五段「踏み切る」の未然形に接続し、「やむを得ず人員削減に踏み切らざるを得ない」と外部的強制による苦渋の選択を表す表現です。', 'trapCategory': ''},
            {'text': 'てはいられない', 'isCorrect': False, 'reason': '【不正解】「〜てはいられない」は「のんびり〜している場合ではない」という意味であり、「人員削減に踏み切ってはいられない」では削減をしないという意味になり文脈に反します。', 'trapCategory': 'meaning'},
            {'text': 'ずにはいられない', 'isCorrect': False, 'reason': '【不正解】「〜ずにはいられない」は感情や自然な衝動を抑えきれずに思わずしてしまう個人的行動を表すため、経営上の苦渋の組織決定には「ざるを得ない」を用います。', 'trapCategory': 'nuance'},
            {'text': 'てたまらない', 'isCorrect': False, 'reason': '【不正解】「〜てたまらない」は欲求や身体的感覚の我慢できなさを表すため、公式な人員削減の決断には使えません。', 'trapCategory': 'register'}
        ]
    },
    'skm2-p1-c25-q4': {
        'context': 'Acute thirst after strenuous exercise under blazing summer heat.',
        'translation': 'Because it was after intense exercise under the blazing sun, I wanted cold water so desperately I could not bear it.',
        'overall': '猛暑での運動後の強烈な渇き・欲求を表す「〜たくてたまらない」を用います。',
        'options': [
            {'text': 'たまらない', 'isCorrect': True, 'reason': '【正解】「冷たい水が飲みたくてたまらない」の形で、身体的な強い欲求や喉の渇きが我慢できない状態を自然に表す表現です。', 'trapCategory': ''},
            {'text': 'いられない', 'isCorrect': False, 'reason': '【不正解】「〜てはいられない」は行動の制約を表す表現であり、「飲みたくていられない」という欲求表現としては文法的に不成立です。', 'trapCategory': 'formation'},
            {'text': 'ざるを得ない', 'isCorrect': False, 'reason': '【不正解】「〜ざるを得ない」はやむを得ない義務的行動を表すため、「飲まざるを得ない」なら可能ですが、「飲みたくて」という希望形には接続できません。', 'trapCategory': 'formation'},
            {'text': 'ならない', 'isCorrect': False, 'reason': '【不正解】「〜てならない」は心理的な不安や予感・愛惜などに使われ、身体的・生理的な渇望（〜たくて…）には「たまらない」が最も適切です。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c25-q5': {
        'context': 'Incessant filial worry over elderly parents health back in one hometown.',
        'translation': 'I cannot help but feel deeply worried about the health condition of my elderly parents whom I left back in my hometown.',
        'overall': '高齢の両親の健康が自然と気にかかり、心から拭い去ることができない不安を表す「心配でならない」を用います。',
        'options': [
            {'text': 'ならない', 'isCorrect': True, 'reason': '【正解】「心配でならない」の形で、抑えようとしても内面から自然と湧き上がってくる心理的感情・懸念を表すのに最も適した表現です。', 'trapCategory': ''},
            {'text': 'いられない', 'isCorrect': False, 'reason': '【不正解】「〜てはいられない」は行動を継続できないことを表す表現であり、「心配でいられない」という感情表現としては成立しません。', 'trapCategory': 'syntax'},
            {'text': 'ざるを得ない', 'isCorrect': False, 'reason': '【不正解】動詞未然形に接続してやむを得ず行う動作を表すため、ナ形容詞語幹＋で「心配で」には接続できません。', 'trapCategory': 'formation'},
            {'text': 'かねない', 'isCorrect': False, 'reason': '【不正解】「〜かねない」は悪影響を引き起こす危険性を表す動詞ます形接続表現であり、感情形容詞には接続できません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c25-q6': {
        'context': 'Pre-exam urgency: with the examination right around the corner, one cannot afford to just fool around.',
        'translation': 'With the exam right around the corner, there is no way one can afford to just fool around.',
        'overall': '目前の試験という緊迫した状況下で「遊んでばかりはいられない（そんな場合ではない）」と行動を戒めます。',
        'options': [
            {'text': 'ばかりはいられない', 'isCorrect': True, 'reason': '【正解】「遊んでばかりはいられないはずがない」の文脈で、事態の切迫性から「のんびりと遊んでいる場合ではない」と行動の制約を強く述べる表現です。', 'trapCategory': ''},
            {'text': 'ずにはいられない', 'isCorrect': False, 'reason': '【不正解】「〜ずにはいられない」は感情や衝動を抑えきれずに思わずしてしまうことを表すため、「試験直前だから思わず遊んでしまう」という意味になり不適切です。', 'trapCategory': 'meaning'},
            {'text': 'ざるを得ない', 'isCorrect': False, 'reason': '【不正解】「〜ざるを得ない」はやむを得ず行動することであり、テ形「遊んで」の後ろに直接接続することはできません。', 'trapCategory': 'formation'},
            {'text': 'てたまらない', 'isCorrect': False, 'reason': '【不正解】「遊んでたまらない」は日本語として不成立であり、切迫した試験前の戒めの文脈に合いません。', 'trapCategory': 'formation'}
        ]
    },
    'skm2-p1-c25-q7': {
        'context': 'Overwhelming emotional distress watching tragic disaster zone footage on television.',
        'translation': 'Watching the tragic reality of the disaster area on television, I could not help feeling my heart wrench in agony.',
        'overall': '悲惨な光景を見て、胸が締め付けられる感情が抑えきれず思わず込み上げた状態を表します。',
        'options': [
            {'text': 'せずにはいられなかった', 'isCorrect': True, 'reason': '【正解】サ変動詞「思いがする」に接続し、「胸が締め付けられる思いがせずにはいられなかった（自然と胸が締め付けられて抑えられなかった）」と激しい感情の衝動を表します。', 'trapCategory': ''},
            {'text': 'していられなかった', 'isCorrect': False, 'reason': '【不正解】「〜していられない」は動作を続けられないことを表すため、心に自然と湧き上がる情緒的衝動の描写には適合しません。', 'trapCategory': 'nuance'},
            {'text': 'せざるを得なかった', 'isCorrect': False, 'reason': '【不正解】「〜ざるを得ない」は義務的・強制的に選択した行動を表すため、自然に湧き上がる悲痛な感情には使えません。', 'trapCategory': 'meaning'},
            {'text': 'してたまらなかった', 'isCorrect': False, 'reason': '【不正解】「思いがしてたまらなかった」も感情を表せますが、悲惨な光景に心を動かされて「思わず〜してしまう」という情緒的抑止不能の呼応には「〜ずにはいられない」が最適です。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c25-q8': {
        'context': 'Confronted with undeniable objective evidence, one is compelled to frankly acknowledge one fault.',
        'translation': 'Having been confronted with objective evidence, I am compelled to frankly acknowledge my fault.',
        'overall': '客観的証拠という動かぬ事実を突きつけられ、もはや自らの過失を認めざるを得ない状況を表します。',
        'options': [
            {'text': 'ざるを得ない', 'isCorrect': True, 'reason': '【正解】動詞一段「認める」の未然形に接続し、「やむを得ず認めざるを得ない（言い逃れができず認めるしかない）」と社会的・客観的強制による行動を表す表現です。', 'trapCategory': ''},
            {'text': 'てはいられない', 'isCorrect': False, 'reason': '【不正解】「〜てはいられない」は「〜している場合ではない」という意味であり、「認めてはいられない」では認めないという意味になり証拠を突きつけられた文脈に反します。', 'trapCategory': 'meaning'},
            {'text': 'ずにはいられない', 'isCorrect': False, 'reason': '【不正解】「〜ずにはいられない」は個人的な感情や生理的衝動を抑えられないことを表すため、証拠に基づく論理的・やむを得ない過失の自認には「ざるを得ない」を用います。', 'trapCategory': 'nuance'},
            {'text': 'てならない', 'isCorrect': False, 'reason': '【不正解】「〜てならない」は心に湧き上がる感情を表すため、過失を認めるという意志的行為には使えません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c25-q9': {
        'context': 'Ecstatic joy upon meeting a long-idolized star in person.',
        'translation': 'To be able to meet my favorite idol whom I had admired for years in person, I was so happy I could hardly stand it.',
        'overall': '憧れのアイドルに会えた狂喜・嬉しさが抑えきれない状態を表す「嬉しくてしかたがない」を用います。',
        'options': [
            {'text': 'しかたがない', 'isCorrect': True, 'reason': '【正解】「嬉しくてしかたがない（嬉しくてたまらない）」の形で、感情が極限まで高まり自分では抑えようがない喜びを素直に表す表現です。', 'trapCategory': ''},
            {'text': 'いられない', 'isCorrect': False, 'reason': '【不正解】「〜てはいられない」は行動を継続できないことを表すため、「嬉しくていられない」という感情表現としては成立しません。', 'trapCategory': 'syntax'},
            {'text': 'ざるを得ない', 'isCorrect': False, 'reason': '【不正解】「〜ざるを得ない」はやむを得ない義務的行動を表す動詞接続表現であり、イ形容詞「嬉しくて」には接続できません。', 'trapCategory': 'formation'},
            {'text': 'ならない', 'isCorrect': False, 'reason': '【不正解】「嬉しくてならない」は文法的には可能ですが、「アイドルに直接会えて嬉しい」という爆発的な個人的喜びには「しかたがない / たまらない」が最も生き生きと合致します。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c25-q10': {
        'context': 'Nagging suspicion that some hidden scheme lurks behind an inexplicable personnel transfer.',
        'translation': 'With this inexplicable personnel transfer, I cannot help feeling that there is some hidden scheme behind it.',
        'overall': '「裏に策略があるような気がしてならない」と、拭い去れない漠然とした疑念・予感を述べる表現を用います。',
        'options': [
            {'text': 'ならない', 'isCorrect': True, 'reason': '【正解】「〜気がしてならない」の慣用的な呼応構文で、頭から払いのけようとしても自然と疑念や懸念が湧き上がってくる心理状態を表す最適な表現です。', 'trapCategory': ''},
            {'text': 'いられない', 'isCorrect': False, 'reason': '【不正解】「〜気がしていられない」という日本語表現は成立せず、行動の制約を表す用法とも合いません。', 'trapCategory': 'syntax'},
            {'text': 'ざるを得ない', 'isCorrect': False, 'reason': '【不正解】動詞未然形接続の義務的行動表現であり、「気がして」というテ形の後ろには接続できません。', 'trapCategory': 'formation'},
            {'text': 'たまらない', 'isCorrect': False, 'reason': '【不正解】「〜気がしてたまらない」は不自然であり、漠然とした予感や疑念の継続には「〜気がしてならない」の呼応が鉄則です。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c25-q11': {
        'context': 'Moral indignation: learning of such serious corruption, one cannot afford to stand by and overlook it.',
        'translation': 'Since I learned of such grave wrongdoing, I cannot simply stand by in silence and overlook it.',
        'overall': '重大な不正を知った以上、「黙って見過ごしてはいられない（そんな放置は許されない）」と正義感から行動の必要性を主張します。',
        'options': [
            {'text': 'はいられない', 'isCorrect': True, 'reason': '【正解】「見過ごしてはいられない（黙って見ていることはできない）」と、道義的・社会的良心から傍観し続けることが許されない状況を述べる表現です。', 'trapCategory': ''},
            {'text': 'ずにはいられない', 'isCorrect': False, 'reason': '【不正解】「見過ごさずにはいられない」とすると「思わず見過ごしてしまう」という意味になり、不正を告発しようとする文意と正反対になります。', 'trapCategory': 'meaning'},
            {'text': 'ざるを得ない', 'isCorrect': False, 'reason': '【不正解】動詞未然形接続（見過ごさざるを得ない）であるため、テ形「見過ごして」には接続できません。また意味としても「やむを得ず見過ごす」となり文脈に反します。', 'trapCategory': 'formation'},
            {'text': 'てならない', 'isCorrect': False, 'reason': '【不正解】「〜てならない」は心に湧き上がる感情を表すため、不正を見過ごすという行動の是非を述べる文脈には使えません。', 'trapCategory': 'meaning'}
        ]
    },
    'skm2-p1-c25-q12': {
        'context': 'Universal emotional resonance: nobody could help shedding tears at the emotional climax of the movie.',
        'translation': 'At the emotional climax of the movie, there was nobody who could help shedding tears.',
        'overall': '映画の感動的な場面で、涙を流さずにはいられない（思わず涙を流してしまう）観客の抑えきれない情緒を表します。',
        'options': [
            {'text': 'さずにはいられない', 'isCorrect': True, 'reason': '【正解】動詞五段「流す」の未然形に接続し、「涙を流さずにはいられない（感動で思わず涙が溢れてしまう）」と感情の強烈な高まりを表す表現です。', 'trapCategory': ''},
            {'text': 'していられない', 'isCorrect': False, 'reason': '【不正解】「〜していられない」は動作の継続を拒む表現であり、「涙を流していられない人はいなかった」では「泣いている場合ではない人はいなかった」となり文意が破綻します。', 'trapCategory': 'meaning'},
            {'text': 'せざるを得ない', 'isCorrect': False, 'reason': '【不正解】「〜ざるを得ない」は義務・強制による行動を表すため、映画の自然な感動による涙の描写には不適切です。', 'trapCategory': 'nuance'},
            {'text': 'してたまらない', 'isCorrect': False, 'reason': '【不正解】「涙を流してたまらない」という日本語は成立せず、感動で思わず泣いてしまう表現には「〜ずにはいられない」を用います。', 'trapCategory': 'formation'}
        ]
    },

    # ==================== Chapter 26 ====================
    'skm2-p1-c26-q1': {
        'context': 'Deep heartfelt wish: wanting to visit the nostalgic mountains and rivers of one hometown just once more before life ends.',
        'translation': 'Before concluding my life, I want to visit those nostalgic mountains and rivers of my hometown just once more.',
        'overall': '人生の終焉を前に、心から願う切実な望みを表す「〜たいものだ」を用います。',
        'options': [
            {'text': 'たいもの', 'isCorrect': True, 'reason': '【正解】動詞連用形「訪れ」に接続し、「訪れたいものだ」と心から深く願う切実な願望を述べる表現です。', 'trapCategory': ''},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「〜ないものか」は実現の難しい事態を希求する独白表現であり、「訪れたいものだ」という自己の直接的な願望文脈には「たいものだ」を用います。', 'trapCategory': 'modality'},
            {'text': 'ものがある', 'isCorrect': False, 'reason': '【不正解】「〜ものがある」は「〜という感じが強く認められる」という感慨・評価を表すため、自己の願望には使えません。', 'trapCategory': 'meaning'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は感嘆・詠嘆（どんなに〜ことか）を表す表現であり、願望の述語としては成立しません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q2': {
        'context': 'Global environmental prayer: could the world not somehow unite together and halt this escalating climate crisis?',
        'translation': 'Could the international community not somehow unite together and halt this escalating global warming crisis?',
        'overall': '実現が困難な事態に対して「どうにか〜できないだろうか」と切実に願う「〜ないものか」を用います。',
        'options': [
            {'text': 'ないものか', 'isCorrect': True, 'reason': '【正解】動詞可能形否定「食い止められない」に接続し、「どうにか食い止められないものか（なんとかして食い止めたい）」と困難な事態の実現を切望する表現です。', 'trapCategory': ''},
            {'text': 'たいものだ', 'isCorrect': False, 'reason': '【不正解】「〜たいものだ」は話者自身の直接的行動の願望に多く用いられ、「世界がどうにか…食い止めたいものだ」とするより、事態の実現を願う「〜ないものか」が文法的に自然です。', 'trapCategory': 'syntax'},
            {'text': 'ものがある', 'isCorrect': False, 'reason': '【不正解】「〜ものがある」は感慨を表す表現であり、困難な危機の解決を切望する問いかけには使えません。', 'trapCategory': 'meaning'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は「どんなに〜ことか」という程度への詠嘆を表すため、解決策を切望する文意に合いません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q3': {
        'context': 'Deep emotional admiration for someone unyielding fortitude in the face of adversity.',
        'translation': 'In his indomitable spirit that never yields to adversity, there is truly something profound that everyone should deeply emulate.',
        'overall': '逆境に負けない不屈の精神力に対して「深く見習うべきものがある（強く感じられる）」と感慨を込めて評価します。',
        'options': [
            {'text': 'ものがある', 'isCorrect': True, 'reason': '【正解】「見習うべきものがある」の形で、「深く心に響く強い要素が認められる」と他者の精神的価値を高く評価・感慨する表現です。', 'trapCategory': ''},
            {'text': 'たいものだ', 'isCorrect': False, 'reason': '【不正解】「見習うべき」の後ろに直接「たいものだ」を重ねることはできず、文末の感慨表現として「ものがある」が適合します。', 'trapCategory': 'syntax'},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「〜ないものか」は実現の希求を表すため、現に目の前にある精神力の偉大さを称える文脈には合いません。', 'trapCategory': 'meaning'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は程度副詞（どんなに・どれほど）と呼応する詠嘆表現であり、「見習うべき〜」に直接接続して評価を述べる述語にはなりません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q4': {
        'context': 'Poignant recollection: when falling sick all alone in a foreign land, how intensely one yearned for family warmth!',
        'translation': 'When falling ill all alone in a foreign land, how intensely I yearned for the warmth of my family!',
        'overall': '「どんなに〜ことか（どれほど〜だったことだろう）」と過去の強烈な感慨・心情の程度を詠嘆します。',
        'options': [
            {'text': 'ことか', 'isCorrect': True, 'reason': '【正解】程度副詞「どんなに」と呼応し、「どんなに恋しかったことか！」と過去の孤独な病床での家族への強い恋しさを深く詠嘆する表現です。', 'trapCategory': ''},
            {'text': 'ものか', 'isCorrect': False, 'reason': '【不正解】「〜ものか」は強い否定（二度と行くものか）を表すため、家族の温もりへの切実な愛惜の詠嘆に合いません。', 'trapCategory': 'meaning'},
            {'text': 'たいものだ', 'isCorrect': False, 'reason': '【不正解】過去形「恋しかった」の後ろに直接「たいものだ」を接続することはできず、過去の感慨には「〜ことか」を用います。', 'trapCategory': 'formation'},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「〜ないものか」は未来への希求を表すため、過去の体験に対する詠嘆には使えません。', 'trapCategory': 'tense'}
        ]
    },
    'skm2-p1-c26-q5': {
        'context': 'Peaceful lifestyle aspiration: wanting to escape frantic modern life and live leisurely on a southern island.',
        'translation': 'Away from modern society chased by time, I would truly love to live leisurely on a southern island.',
        'overall': '時間に追われる日常を離れ、南の島で暮らしてみたいという憧れの願望を表す「〜てみたいものだ」を用います。',
        'options': [
            {'text': 'みたいもの', 'isCorrect': True, 'reason': '【正解】動詞テ形「暮らして」に接続し、「暮らしてみたいものだ」と非日常の憧れの生活に対する心からの願望を述べる表現です。', 'trapCategory': ''},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「暮らしてないものか」という接続は不自然であり、自分自身の憧れの生活体験を願う文脈には「みたいものだ」を用います。', 'trapCategory': 'syntax'},
            {'text': 'ものがある', 'isCorrect': False, 'reason': '【不正解】「〜ものがある」は客観的性質への感慨を表すため、自分の将来の願望には使えません。', 'trapCategory': 'meaning'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は程度への詠嘆を表すため、願望の述語としては成立しません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q6': {
        'context': 'Humanitarian prayer: could a cure to save people suffering from intractable diseases not somehow be developed as soon as possible?',
        'translation': 'Could a miracle cure to save people suffering from intractable diseases not somehow be developed as quickly as possible?',
        'overall': '難病の特効薬が一日も早く開発されることを切に希求する「〜ないものだろうか」を用います。',
        'options': [
            {'text': 'ないものだろうか', 'isCorrect': True, 'reason': '【正解】受身動詞「開発され」に接続し、「一日も早く開発されないものだろうか（なんとか開発されてほしい）」と困難な課題の実現を切望する表現です。', 'trapCategory': ''},
            {'text': 'たいものだろうか', 'isCorrect': False, 'reason': '【不正解】「〜たいものだろうか」という表現は日本語として不自然であり、受身主語「特効薬が」に対する願望形式としても破綻します。', 'trapCategory': 'formation'},
            {'text': 'ものがあるだろうか', 'isCorrect': False, 'reason': '【不正解】感慨の反語的疑問になり、特効薬の早期開発を切望する人道的な文脈に合いません。', 'trapCategory': 'meaning'},
            {'text': 'ことだろうか', 'isCorrect': False, 'reason': '【不正解】程度への詠嘆・疑問になり、「一日も早く」という切実な願いの文脈に適合しません。', 'trapCategory': 'nuance'}
        ]
    },
    'skm2-p1-c26-q7': {
        'context': 'Aesthetic reverence: in the weathered stone Buddha enduring decades, there is something sublimely breathtaking.',
        'translation': 'In the weathered stone Buddha that has endured decades of time, there is truly something sublime that leaves one speechless.',
        'overall': '風化した石仏の佇まいに認められる崇高な迫力への感慨を表す「〜ものがある」を用います。',
        'options': [
            {'text': 'ものがある', 'isCorrect': True, 'reason': '【正解】ナ形容詞連体形「崇高な」に接続し、「崇高なものがある（深く心を打つ崇高さを強く感じる）」と感慨を述べる表現です。', 'trapCategory': ''},
            {'text': 'たいものだ', 'isCorrect': False, 'reason': '【不正解】「崇高なたいものだ」という接続は文法的に不成立であり、自己の願望でもありません。', 'trapCategory': 'formation'},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「崇高なないものか」という接続は成立せず、事態の希求でもありません。', 'trapCategory': 'formation'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は文末感嘆詞であり、「崇高なことか」では文末の述語として意味が成立しません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q8': {
        'context': 'Profound empathy: how unfathomable the grief of those who had their beloved families torn away by the atrocities of war!',
        'translation': 'How immeasurable must have been the grief of those whose beloved families were taken away by the atrocities of war!',
        'overall': '戦争で家族を奪われた人々の計り知れない悲痛に対して「いかばかりであったことか！」と深く詠嘆します。',
        'options': [
            {'text': 'ことか', 'isCorrect': True, 'reason': '【正解】疑問・程度表現「いかばかり（どれほど）」と呼応し、「いかばかりであったことか！」と他者の計り知れない深い悲しみに寄り添って詠嘆する表現です。', 'trapCategory': ''},
            {'text': 'ものか', 'isCorrect': False, 'reason': '【不正解】「〜ものか」は強い否定を表すため、遺族の悲痛を否定する不適切な意味になってしまいます。', 'trapCategory': 'meaning'},
            {'text': 'たいものだ', 'isCorrect': False, 'reason': '【不正解】過去の悲痛に対して自己の願望表現「たいものだ」を用いるのは文法・文意ともに不成立です。', 'trapCategory': 'formation'},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】未来の実現を願う希求表現であり、過去の悲惨な事実に対する詠嘆には使えません。', 'trapCategory': 'tense'}
        ]
    },
    'skm2-p1-c26-q9': {
        'context': 'Bucket list dream: wanting to gaze down upon the shining blue Earth from a space station just once.',
        'translation': 'Just once would be enough—I would truly love to gaze down upon the shining blue Earth from a space station.',
        'overall': '宇宙ステーションから地球を眺めてみたいという生涯の夢・願望を表す「〜てみたいものだ」を用います。',
        'options': [
            {'text': 'みたいもの', 'isCorrect': True, 'reason': '【正解】動詞テ形「眺めて」に接続し、「眺めてみたいものだ」と非日常の壮大な夢に対する強い願望を表す表現です。', 'trapCategory': ''},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「眺めてないものか」という接続は不自然であり、自分自身の直接的な体験願望には「みたいものだ」を用います。', 'trapCategory': 'syntax'},
            {'text': 'ものがある', 'isCorrect': False, 'reason': '【不正解】「〜ものがある」は対象の性質への感慨を表すため、自分自身の行動の願望には適しません。', 'trapCategory': 'meaning'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は程度への詠嘆を表すため、願望文の述語としては成立しません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q10': {
        'context': 'Wistful desire: is there not some marvelous idea lying around somewhere to relieve this chronic traffic congestion?',
        'translation': 'Is there not some marvelous idea lying around somewhere to relieve this chronic traffic congestion?',
        'overall': '慢性的な渋滞を解消する名案を切望し、「どこかに転がっていないものか」と自問・希求します。',
        'options': [
            {'text': 'いないものか', 'isCorrect': True, 'reason': '【正解】動詞テイル形否定「転がっていない」に接続し、「どこかに転がっていないものか（なんとか名案が見つからないか）」と解決策を切望する独白表現です。', 'trapCategory': ''},
            {'text': 'たいものか', 'isCorrect': False, 'reason': '【不正解】「転がっていたいものか」という日本語は意味が通じず、名案の存在を希求する文脈に合いません。', 'trapCategory': 'formation'},
            {'text': 'ものがあるか', 'isCorrect': False, 'reason': '【不正解】反語的疑問になり、渋滞解消の名案を願う文意と合いません。', 'trapCategory': 'meaning'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は程度への詠嘆を表すため、解決策の出現を希求する問いかけには使えません。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q11': {
        'context': 'Artistic awe: in the posthumous work of a genius painter who died young, there is something overwhelmingly soul-stirring.',
        'translation': 'In the posthumous masterpiece of the genius painter who died young, there is truly something overwhelming that shakes the viewer soul.',
        'overall': '夭折の天才画家の遺作に認められる圧倒的な迫力への感慨を表す「〜ものがある」を用います。',
        'options': [
            {'text': 'ものがある', 'isCorrect': True, 'reason': '【正解】連体修飾句「圧倒的な」に接続し、「圧倒的なものがある（見る者を圧倒する凄みが強く感じられる）」と芸術的迫力への深い感慨を述べる表現です。', 'trapCategory': ''},
            {'text': 'たいものだ', 'isCorrect': False, 'reason': '【不正解】「圧倒的なたいものだ」という接続は文法的に不成立であり、自己の願望でもありません。', 'trapCategory': 'formation'},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「圧倒的なないものか」という接続は成立せず、事態の希求でもありません。', 'trapCategory': 'formation'},
            {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「圧倒的なことか」では文末の述語として意味が成立せず、対象の性質を評価する述語には「ものがある」を用います。', 'trapCategory': 'syntax'}
        ]
    },
    'skm2-p1-c26-q12': {
        'context': 'Profound relief: when receiving a letter from a close friend with whom contact had lapsed for years, how immensely relieved one felt!',
        'translation': 'When receiving a letter from a dear friend with whom all contact had been cut for years, how immensely relieved I felt!',
        'overall': '「どれほど安堵したことか！」と、長年の音信不通の末の便りに接した深い安堵の心情を詠嘆します。',
        'options': [
            {'text': 'ことか', 'isCorrect': True, 'reason': '【正解】程度副詞「どれほど」と呼応し、「どれほど安堵したことか！」と心からの安堵の大きさを強く詠嘆する表現です。', 'trapCategory': ''},
            {'text': 'ものか', 'isCorrect': False, 'reason': '【不正解】「〜ものか」は強い否定を表すため、親友からの便りへの安堵感を否定する不適切な意味になります。', 'trapCategory': 'meaning'},
            {'text': 'たいものだ', 'isCorrect': False, 'reason': '【不正解】過去形「安堵した」の後ろに直接「たいものだ」を接続することはできず、過去の感慨には「〜ことか」を用います。', 'trapCategory': 'formation'},
            {'text': 'ないものか', 'isCorrect': False, 'reason': '【不正解】「〜ないものか」は未来への希求を表すため、過去の体験の詠嘆には使えません。', 'trapCategory': 'tense'}
        ]
    }
}

count_updated = 0
for qid, upd in updates.items():
    if qid in ex_map:
        q = ex_map[qid]
        q['context'] = upd['context']
        q['translation'] = upd['translation']
        exp = q.setdefault('explanation', {})
        exp['overall'] = upd['overall']
        exp['options'] = upd['options']
        # Also ensure options array matches text
        q['options'] = [o['text'] for o in upd['options']]
        q['correctIndex'] = next(i for i, o in enumerate(upd['options']) if o['isCorrect'])
        count_updated += 1

print(f"Total exercises updated: {count_updated}")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully.")
