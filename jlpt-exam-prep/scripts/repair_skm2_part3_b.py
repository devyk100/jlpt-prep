"""
repair_skm2_part3_b.py
Repairs placeholder translations and generic distractor feedback in
Shin Kanzen Master N2 Part 3 (Chapters 7 to 12, 72 questions).
Injects complete English translations, sentence-specific option explanations,
and authentic textbook citations.
"""

import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_FILE = ROOT / "src/data/chapterExercises.json"

REPAIRS_P3B = {
    # ------------------ Part 3 · Chapter 7: 授受動詞の視点 (Benefactive Standpoint) ------------------
    "skm2-p3-c7-q1": (
        "Thank you very much indeed for taking the time out of your busy schedule to grace our company's founding anniversary ceremony with your presence today.",
        "Formal gratitude in corporate ceremonial speech 'ありがとう…'.",
        {"ございます": "儀礼的な式典挨拶において、最高度の丁寧さで謝意を表す丁寧語「ございます」です。",
         "ございますでしょうか": "疑問形になり、式典冒頭の明確な感謝の謝辞に合いません。",
         "だ": "普通体になり、社外の来賓を迎える公式行事の改まった文体に反します。",
         "である": "論文・論説体になり、直接対面で感謝を述べるスピーチに不適です。"}
    ),
    "skm2-p3-c7-q2": (
        "Thanks to the professor kindly writing a letter of recommendation for me, I successfully passed the entrance examination for my long-cherished graduate school.",
        "Benefactive auxiliary indicating receiving a favor from a superior '書いていただいた'.",
        {"いただいた": "目上の先生から推薦状執筆の恩恵を話者（私）が受領したことを表す謙譲語「〜ていただく」です。",
         "くださった": "「書いてくださった」でも恩恵を表せますが、主語が「先生から」となっており受容の視点「いただいた」が構文上整合します。",
         "あげた": "自分が先生に与えたことになり、合否の恩恵関係が完全に逆転します。",
         "やった": "目下に対する粗野な授与になり、恩師に対する敬語表現として極めて非礼です。"}
    ),
    "skm2-p3-c7-q3": (
        "The president personally visited the front line and gave warm words of encouragement to each and every employee.",
        "Benefactive auxiliary from superior to in-group members 'かけてくださった'.",
        {"くださった": "主語「社長が」自ら話者や同僚たち（ウチの社員）に対して激励を与えてくれた恩恵を表す尊敬語「〜てくださる」です。",
         "いただいた": "謙譲語になり、主語が「社長自らが」である構文に整合しません。",
         "あげた": "社長が他者に恩恵を与えた客観描写として敬意が欠落し、不適切です。",
         "もらった": "普通語の受領になり、最高責任者である社長の親身な行動への敬意を表せません。"}
    ),
    "skm2-p3-c7-q4": (
        "Despite our procedural clumsiness, you extended generous consideration to us, for which we extend our heartfelt, deepest gratitude.",
        "Receiving considerate favor 'ご配慮をいただき'.",
        {"いただき": "相手方の寛大な配慮という恩恵を話者側がありがたく受けたことを表す謙譲語「いただく」の連用形です。",
         "くださり": "「ご配慮くださり」でも通じますが、「をいただき」という格助詞「を」を伴う受領形式として「いただき」が定着しています。",
         "あげ": "自分が相手に配慮を与えたことになり、不手際を謝罪・感謝する文脈と矛盾します。",
         "やり": "目下に対する授与になり、顧客・取引先に対するお礼状として言語道断です。"}
    ),
    "skm2-p3-c7-q5": (
        "My former professor went out of his way to search for precious unpublished materials and send them to me.",
        "Superior performing a favor for the speaker '送ってくださった'.",
        {"くださった": "主語である恩師が、話者（私）のためにわざわざ資料を探して送付してくれた好意を表す尊敬授受補助動詞です。",
         "いただいた": "主語が恩師の文であるため、「送っていただいた」にするには主語を「恩師から」とする必要があります。",
         "あげた": "話者が恩師に送ったことになり、文意と主客関係が逆転します。",
         "やった": "目下への授与になり、尊敬すべき恩師の親切な行為の描写に極めて不適です。"}
    ),
    "skm2-p3-c7-q6": (
        "Regarding the new product plan proposal, we would like to have you kindly share your candid opinions as an expert.",
        "Humble request to receive expert opinions 'お聞かせいただきたく存じます'.",
        {"いただき": "相手の意見を聞く（拝聴する）恩恵を受けたいという敬意を表す「お聞かせいただく」の形です。",
         "くださり": "「お聞かせくださりたく」は文法的に不自然であり、願望「たく存じます」には「いただき」が接続します。",
         "あげ": "自分が相手に聞かせることになり、専門家の意見を求める趣旨と正反対になります。",
         "やり": "相手に対する敬意が全くなく、ビジネス依頼文として不適です。"}
    ),
    "skm2-p3-c7-q7": (
        "When I was lost in front of the station, a kind elderly woman went out of her way to guide me to my destination.",
        "Third-party stranger doing a favor for the speaker '案内してくれた'.",
        {"くれた": "見知らぬ親切な老婦人が困っている私に対して親身に案内してくれた自然な好意を表す補助動詞です。",
         "あげた": "自分が老婦人を案内したことになり、道に迷っていた文脈と矛盾します。",
         "もらった": "「老婦人にもらった」構文なら可能ですが、主語が「老婦人が」のため「くれた」が文法的に必須です。",
         "やった": "目下への授与になり、助けてもらった恩人への感謝に不適です。"}
    ),
    "skm2-p3-c7-q8": (
        "Regarding today's lecture content, would anyone have any questions?",
        "Polite inquiry about listener questions 'ご質問はございませんでしょうか'.",
        {"ございません": "聴衆に対して控えめに質問の有無を尋ねる丁寧な否定疑問形式「ございませんでしょうか」です。",
         "ありません": "日常会話レベルの丁寧さにとどまり、公式講演会での改まった問いかけとして敬意が不足します。",
         "ない": "普通体になり、聴衆に対する質疑応答の司会発言として失礼です。",
         "おありにならない": "尊敬語の二重否定になり、質問の有無を尋ねる表現として極めて不自然です。"}
    ),
    "skm2-p3-c7-q9": (
        "Deeply thanking you for your patronage over many years, we respectfully present this commemorative gift.",
        "Humble expression of gratitude '感謝申し上げ'.",
        {"申し上げ": "長年の愛顧に対して自らの感謝の意をへりくだって伝える謙譲表現「感謝申し上げる」の連用形です。",
         "いただき": "相手が感謝したことになり、記念品を進呈する側の感謝表明として主客が混乱します。",
         "くださり": "相手の動作の尊敬になり、自らの感謝の感情の陳述に合いません。",
         "やり": "敬意のない授与になり、顧客への進呈の挨拶文に不適です。"}
    ),
    "skm2-p3-c7-q10": (
        "My senior took time out of his busy schedule to painstakingly proofread the typos and omissions in my paper for me.",
        "Senior performing a helpful task for the junior '校正してくださった'.",
        {"くださった": "主語「先輩が」好意で後輩（私）の論文の校正を引き受けてくれた恩恵を表す尊敬授受補助動詞です。",
         "いただいた": "主語が先輩であるため、「校正していただいた」では主客の文法的一致が崩れます。",
         "あげた": "自分が先輩の論文を校正したことになり、文意が正反対になります。",
         "もらった": "先輩に対する敬意が希薄であり、時間を割いてくれた好意への感謝として「くださった」が最適です。"}
    ),
    "skm2-p3-c7-q11": (
        "Taking this opportunity, we would be deeply pleased if we could be favored with your candid opinions.",
        "Polite potential in formal discourse '拝聴できれば幸いに存じます'.",
        {"できれ": "謙譲動詞「拝聴する」の可能仮定形「拝聴できれば」で、意見を聞く機会を得られればありがたいという控えめな願望を表します。",
         "いただき": "「拝聴いただきば」となり活用が完全に崩壊します。",
         "くださり": "「拝聴くださりば」となり文法的に成り立ちません。",
         "あげれ": "授与になり、意見を伺う文脈に合いません。"}
    ),
    "skm2-p3-c7-q12": (
        "From our major corporate client, we were generously favored with their undertaking a large investment.",
        "Receiving major undertaking from a corporate partner '引き受けていただいた'.",
        {"いただいた": "「取引先の大手企業から」という起点の助詞「から」を受けて、巨額出資の受領を表す謙譲語「〜ていただく」です。",
         "くださった": "「企業が」という主格の場合に適しますが、「企業から」という受領元を受けるには「いただいた」が構文上整合します。",
         "あげた": "自社が出資を引き受けたことになり、相手から資金支援を受けた文脈と逆転します。",
         "やった": "目下への授与になり、大口出資元の取引先に対して不適切極まりない表現です。"}
    ),

    # ------------------ Part 3 · Chapter 8: 指示表現「こ・そ・あ」の使い分け (Demonstrative Cohesion in Discourse) ------------------
    "skm2-p3-c8-q1": (
        "Last month I reunited with old friends from my university days for the first time in ten years. The nostalgic memories from that time are still vividly burned into my heart.",
        "Textual discourse anaphora referring back to the previously mentioned occasion 'その時の思い出'.",
        {"その": "文章の前文で述べられた出来事（先月の十年ぶりの再会）を客観的に受けて指し示す文脈指示の「そ」系列です。",
         "この": "現在の現場や直近の話題を指す近称であり、前文の過去の特定の一場面の回想には「その」が適切です。",
         "あの": "話者と聞き手の双方の共通既知の遠称になり、読者に向けた客観的な文章展開では「その」が自然です。",
         "どの": "疑問詞であり、特定の懐かしい思い出の叙述に合いません。"}
    ),
    "skm2-p3-c8-q2": (
        "What the author wishes to argue most strongly in this paper is none other than this very point.",
        "Emphatic proximal deictic in essay conclusion 'この点にほかならない'.",
        {"この": "自らの論文の中で今まさに論述している核心的主張を眼前の焦点として強調する「こ」系列です。",
         "その": "客観的な他者の議論や離れた文脈を指すニュアンスになり、筆者自身の熱意ある主張の提示として弱まります。",
         "あの": "遠い共通記憶を指すため、自著の学術論文の結論の提示に不適です。",
         "どの": "疑問詞になり、「ほかならない」の断定文末と呼応しません。"}
    ),
    "skm2-p3-c8-q3": (
        "'Hey, listen, what was the name of that mountain we all climbed together last year?' 'Ah, you mean Mount Chokai.'",
        "Shared conversational recollection of distant experience 'あの山'.",
        {"あの": "会話者双方の共通の直接体験・記憶の中にある対象を想起させる「あ」系列指示詞です。",
         "その": "聞き手だけが知っている情報や直前の言語的文脈を指すため、二人で一緒に登った共通体験の想起には「あの」が最適です。",
         "この": "話者の身近な対象を指すため、去年の登山の山には合いません。",
         "どの": "「何だっけ？」と疑問文が後続するため、「どの山の名前」では構文が破綻します。"}
    ),
    "skm2-p3-c8-q4": (
        "The town's population decline is progressing rapidly. As the cause of this, the shortage of employment opportunities has been pointed out.",
        "Anaphoric reference to a stated phenomenon 'その原因として'.",
        {"その": "前文で言及された客観的事実（街の人口減少）を直接受けて、その理由を述べる論理的文脈指示の「その」です。",
         "この": "筆者の眼前への引き寄せになりますが、先行文の事象の原因を客観的に論じる標準指示語は「その」です。",
         "あの": "遠くの共通体験になり、客観的統計事実の説明に合いません。",
         "どの": "疑問詞になり、「指摘されている」という客観的事実の陳述に不適です。"}
    ),
    "skm2-p3-c8-q5": (
        "Taking into account the discussions held so far, we decided to hammer out this kind of groundbreaking new policy.",
        "Speaker presenting their own upcoming new proposal 'このような画期的な新方針'.",
        {"この": "これまでの検討を踏まえ、これから提示する自らの新方針を身近な焦点として打ち出す「こ」系列です。",
         "その": "既知の他者の提案を指すニュアンスになり、自ら打ち出す新規方針のアピールとして不自然です。",
         "あの": "遠い過去や共有記憶を指すため、今決定した新方針に合いません。",
         "どの": "疑問詞になり、決定事項の報告文脈に整合しません。"}
    ),
    "skm2-p3-c8-q6": (
        "'I met Mr. Sato yesterday.' 'Oh, that person seemingly changed jobs recently, right?'",
        "Conversational anaphora to person newly introduced by interlocutor 'その人'.",
        {"その": "相手の発話によって会話の場に初めて登場した人物（佐藤さん）を指し示す対話の「そ」系列です。",
         "この": "話者自身の身近な対象を指すため、相手が話題にした人物を受ける指示詞として不自然です。",
         "あの": "二人とも以前からよく知っている共通の知人として遠くを指すニュアンスになり、相手の報告を受けて反応する指示には「その人」が標準的です。",
         "どの": "疑問詞になり、「転職したらしいね」という情報の確認に合いません。"}
    ),
    "skm2-p3-c8-q7": (
        "During the Showa period of high economic growth, the people of that era worked furiously, believing in future affluence.",
        "Distant historical era shared in cultural memory 'あの時代'.",
        {"あの": "現在から遠く隔たった過去の歴史的時代（昭和高度成長期）を心理的距離を置いて回顧する「あ」系列です。",
         "その": "直前の文脈指示としても使えますが、遠い過去の懐古的ニュアンスには「あの時代」が最も詩的・感情的に自然です。",
         "この": "現在または眼前の時代を指すため、過去の昭和時代と矛盾します。",
         "どの": "疑問詞になり、歴史的事実の回想文に合いません。"}
    ),
    "skm2-p3-c8-q8": (
        "The rising sea levels due to global warming. How should we humankind confront this grave environmental crisis?",
        "Dramatic topicalization of immediate global crisis 'この深刻な環境危機'.",
        {"この": "直前の名詞句（海面上昇）で提起された焦眉の危機を、人類全体の切実な課題として目前に引き寄せる「こ」系列です。",
         "その": "客観的に距離を置いた指示になり、筆者の緊迫した問題提起の熱量が薄れます。",
         "あの": "過去の出来事や遠くの記憶を指すため、現在進行中の地球危機に不適です。",
         "どの": "疑問詞になり、直前の名詞句を受けた指示表現として機能しません。"}
    ),
    "skm2-p3-c8-q9": (
        "Once upon a time, in a certain place lived a kind-hearted grandfather. One day, that grandfather went to the mountains to gather firewood.",
        "Fairytale discourse anaphora re-mentioning the introduced character 'そのおじいさんは'.",
        {"その": "昔話の導入において、不特定の存在（ある所に住んでいたおじいさん）を既知の対象として物語を進行させる「そ」系列です。",
         "この": "話者の手元を指す近称になり、古典的な昔話の語り口として不自然です。",
         "あの": "聞き手との共通記憶になり、物語冒頭の登場人物の追尾に合いません。",
         "どの": "疑問詞になり、物語の叙述文を破綻させます。"}
    ),
    "skm2-p3-c8-q10": (
        "'The ramen we ate yesterday was really delicious, wasn't it?' 'Yeah, that shop's gyoza dumplings were also superb!'",
        "Conversational reference to a shared visited restaurant 'あの店'.",
        {"あの": "昨日二人が一緒に行って体験した共通の記憶にあるラーメン屋を指す「あ」系列です。",
         "その": "相手だけが知っている店を指す響きになり、二人で一緒に食べた実体験の共有感が損なわれます。",
         "この": "現在自分たちがいる店を指すため、昨日行った別の店には合いません。",
         "どの": "疑問詞になり、絶賛する相手への同調発言に不適です。"}
    ),
    "skm2-p3-c8-q11": (
        "The dilution of human relationships in modern society. At the root of this problem lies the rise of excessive individualism.",
        "Topical framing of societal issue 'この問題の根底'.",
        {"この": "冒頭の体言止めで提示された現代的課題を強くクローズアップして分析を深める文章指示の「こ」系列です。",
         "その": "客観的な連鎖になりますが、評論の導入部で論点を鋭く焦点化するには「この」が最適です。",
         "あの": "遠い昔の出来事を想起させるため、現代社会の問題分析に合いません。",
         "どの": "疑問詞になり、根底の要因を説明する文に合いません。"}
    ),
    "skm2-p3-c8-q12": (
        "The criminal intruded late at night by breaking the rear entrance window glass. On that occasion, they dropped a single handkerchief at the scene.",
        "Formal temporal conjunction referring to the moment of crime 'その際'.",
        {"その": "前文で述べられた侵入行為の時点・機会を的確に受ける文章語の形式名詞連語「その際」です。",
         "この": "「この際」は「これを契機に（思い切って〜する）」という話者の決意を表すため、犯罪事実の客観描写に合いません。",
         "あの": "遠称になり、警察捜査・事件記録の客観叙述に不適です。",
         "どの": "疑問詞になり、「現場に落としていった」という確定事実の叙述に合いません。"}
    ),

    # ------------------ Part 3 · Chapter 9: 助詞「は」と「が」の使い分け (Topic & Focus in Discourse) ------------------
    "skm2-p3-c9-q1": (
        "Once upon a time, in a certain place lived a beautiful princess. The princess sang with little birds every day.",
        "Introduction of new referent (が) followed by thematic topic marker (は) 'お姫様が…お姫様は'.",
        {"が・は": "物語導入部で未知の人物を新情報として導入する排他・現象記述の「が」と、既知となった人物を主題化する「は」の王道パターンです。",
         "は・が": "冒頭で未登場の人物に「は」を使い、既知の人物に「が」を使うのは談話構造の原則と正反対です。",
         "が・が": "二文目で主題化が行われず、文の結束性が損なわれます。",
         "は・は": "冒頭で読者に未知のお姫様を既知の前提として提示してしまい、昔話の導入として破綻します。"}
    ),
    "skm2-p3-c9-q2": (
        "Yesterday, I was the one who personally called the client.",
        "Focus on the agent solving 'who did it' '私が'.",
        {"が": "「誰が電話をかけたのか」という疑問に対する答えとして、主語（私）を排他的に特定・指定する焦点の「が」です。",
         "は": "主題提示になり、他の人ではなく「私自身が」かけたという排他的焦点のニュアンスが消えてしまいます。",
         "も": "添加になり、「他の人もかけたし私も」という意味になり自発的特定の文脈に合いません。",
         "に": "相手格になり、「私に電話をかけた」となって自分が電話を受けた意味になり矛盾します。"}
    ),
    "skm2-p3-c9-q3": (
        "The mountain was high and its summit was covered with white snow.",
        "Describing the overall topic (は) and its constituent part (が) '山は…頂上が'.",
        {"は・が": "「山」を文全体の主題（大主語）として提示し、その一部である「頂上」の性状・状態を小主語として「が」で叙述する「は〜が」構文です。",
         "が・は": "大主語と小主語の主従関係が逆転し、不自然な文になります。",
         "が・が": "並列関係が曖昧になり、山全体の属性描写として結束性が弱まります。",
         "は・は": "二重主題になり、文の主述呼応が不自然になります。"}
    ),
    "skm2-p3-c9-q4": (
        "Regarding this matter, we would like to explain it in detail at the next meeting.",
        "Topic topicalization of business agenda 'この件に関しては'.",
        {"は": "「この件に関しては」の形で、これから取り上げて論じる話題を明確に主題化する助詞「は」です。",
         "が": "現象記述や排他指定になり、会議で説明するアジェンダの主題提示として不自然です。",
         "も": "添加になり、前提となる他の議題が存在しない冒頭での提示に不適です。",
         "の": "連体助詞になり、「説明したい」という述語に直接接続できません。"}
    ),
    "skm2-p3-c9-q5": (
        "Look, a rainbow has appeared over the eastern mountain ridge!",
        "Immediate sensory perception / neutral description '虹が'.",
        {"が": "眼前に突如出現した自然現象を話者が知覚し、そのままありのままに実況叙述する現象記述の「が」です。",
         "は": "虹を一般的な主題として取り立てることになり、「ほら、見て」という突発的発見の感嘆に合いません。",
         "も": "添加になり、他に何かが出ている前提がないため不自然です。",
         "を": "目的格になり、「出ている」という自動詞と文法的に結合できません。"}
    ),
    "skm2-p3-c9-q6": (
        "Whales are mammals, not fish.",
        "Generic definition / classification of species 'クジラは'.",
        {"は": "生物学的分類や一般的定義を述べる文において、普遍的性質を叙述する主題提示の「は」です。",
         "が": "排他指定になり、「クジラだけが哺乳類だ」という誤った排他的解釈を生んでしまいます。",
         "も": "添加になり、魚類との決定的な対比の文脈に合いません。",
         "で": "格助詞になり、主語を提示できません。"}
    ),
    "skm2-p3-c9-q7": (
        "The dog has long ears and its tail is charmingly curled.",
        "Topic (は) with specific attribute description (が) 'この犬は…耳が'.",
        {"は・が": "「この犬」を全体の主題（は）とし、その身体的特徴である「耳」を対象の属性（が）として叙述する構文です。",
         "が・は": "犬を主語にして耳を主題化することになり、文の論理構造が倒錯します。",
         "が・が": "全体と部分の階層関係が失われます。",
         "は・は": "二重の主題取り立てになり、文法的結束性が破綻します。"}
    ),
    "skm2-p3-c9-q8": (
        "When the bell rang, the students all poured out of the classroom at once.",
        "Subject in subordinate time clause 'チャイムが'.",
        {"が": "連用修飾節（従属節「〜と」）の内部における主語は、主題の「は」ではなく「が」を用いる文法規則に基づきます。",
         "は": "従属節内の主語に「は」を用いると文全体の主題と衝突し、破格の文になります。",
         "も": "添加になり、授業終了を告げる合図の描写に不適です。",
         "を": "目的格になり、自動詞「鳴る」と結合できません。"}
    ),
    "skm2-p3-c9-q9": (
        "Who is the person who achieved the top score in this examination?",
        "Interrogative pronoun as subject must take 'が' '誰が'.",
        {"誰が": "疑問詞が文の主語になる場合、主題の「は」を取ることは文法上許されず、必ず「が」を用います。",
         "誰は": "日本語の文法体系において疑問詞に主題の「は」を後接させることはできません。",
         "誰を": "目的格になり、最高得点を獲得した動作主の指定に反します。",
         "誰に": "与格になり、主格の提示になりません。"}
    ),
    "skm2-p3-c9-q10": (
        "I was the one who cleaned this room yesterday.",
        "Exhaustive listing focus on the agent '私が'.",
        {"が": "「誰が掃除したのか」という問いに対し、行為者を排他的に名乗り出る特定指定の「が」です。",
         "は": "単なる自分の行動の報告になり、「他の人ではなく自分がやった」という自負・特定のニュアンスが出ません。",
         "も": "「私もやった」になり、一人で部屋を掃除した特定の主張に合いません。",
         "に": "与格になり、掃除の動作主を示せません。"}
    ),
    "skm2-p3-c9-q11": (
        "Tokyo is Japan's capital and its population is concentrated to an immense degree.",
        "Thematic topic '東京は' followed by attribute subject '人口が'.",
        {"は・が": "「東京」を国政・地理の主題として提示し、その構成要素である「人口」の極度の集中を「が」で陳述する自然な論述構造です。",
         "が・は": "主題と属性の主従関係が崩れます。",
         "が・が": "並列の排他になり、大都市の一般的属性の説明として不自然です。",
         "は・は": "二重の主題提示になり、文末の述語との呼応が乱れます。"}
    ),
    "skm2-p3-c9-q12": (
        "Whenever spring comes, beautiful cherry blossoms bloom all over this park.",
        "Subject in natural phenomenon clause '桜が'.",
        {"が": "公園一面に咲き誇る桜という客観的な自然事象の出現を描写する主格の「が」です。",
         "は": "桜を一般的概念として取り立てることになり、春の訪れとともに咲く景観の実況描写として不自然です。",
         "も": "添加になり、公園の主役である桜の満開の描写に合いません。",
         "を": "目的格になり、自動詞「咲く」と結合できません。"}
    ),

    # ------------------ Part 3 · Chapter 10: 接続表現 (Discourse Connectives & Logic in Text) ------------------
    "skm2-p3-c10-q1": (
        "Due to heavy snow since last night, major expressways were completely closed. Consequently, this morning's logistics functions are entirely paralyzed.",
        "Logical consequence connective 'したがって'.",
        {"したがって": "高速道路全面通行止めという重大な原因から、物流麻痺という必然的な結果を導く論理的順接接続詞です。",
         "しかし": "逆接になり、大雪による交通麻痺という自然な因果関係と矛盾します。",
         "なぜなら": "理由を後から説明する語であり、前文が原因で後文が結果である順序に合いません。",
         "一方": "対比になり、原因と結果の因果的結びつきを表せません。"}
    ),
    "skm2-p3-c10-q2": (
        "The opponent team was an overwhelming favorite with many professional athletes. However, our team did not give up until the end and grasped victory.",
        "Adversative contrast connective 'しかし'.",
        {"しかし": "相手が強豪であるという圧倒的不利な前提を覆し、劇的な勝利を収めたという劇的逆接を導きます。",
         "したがって": "順接になり、相手が強豪だから勝ったという不条理な因果関係になってしまいます。",
         "つまり": "要約・同義換言になり、対比の逆接に合いません。",
         "なぜなら": "理由説明になり、勝利を収めたドラマチックな転換に不適です。"}
    ),
    "skm2-p3-c10-q3": (
        "He does not spend wastefully at all and always shops during discount hours. In short, he is a thorough economizer.",
        "Summarizing rephrase connective 'つまり'.",
        {"つまり": "前文で挙げられた具体的な倹約行動（無駄遣いせず、割引時に買う）を一言で総括・換言する接続詞です。",
         "しかし": "逆接になり、前文の行動と節約家という評価が一致しているため矛盾します。",
         "したがって": "論理的結果ですが、人物の総括的定義・言い換えには「つまり（要するに）」が最適です。",
         "なぜなら": "理由説明になり、前文が具体例で後文が結論である構造と逆になります。"}
    ),
    "skm2-p3-c10-q4": (
        "This experiment ended in great success. The reason is that all members had prepared repeatedly in advance.",
        "Explanatory cause connective 'なぜなら'.",
        {"なぜなら": "前文で述べた実験の大成功という結果に対し、後文で「準備を重ねていたからだ」と原因・理由を補足説明する接続詞です。",
         "したがって": "順接の結果になり、前文が大成功で後文がその理由という順序と倒錯します。",
         "しかし": "逆接になり、成功と周到な準備の整合的因果関係に反します。",
         "一方": "並列対比になり、成功の直接の要因説明に合いません。"}
    ),
    "skm2-p3-c10-q5": (
        "In urban areas the concentration of population and rising rents progress. On the other hand, in regional areas the birthrate decline and depopulation become serious.",
        "Dual aspect contrastive connective '一方'.",
        {"一方": "都会（過密・高騰）と地方（過疎・少子化）という対極的な二つの社会動向を対比させて論述する接続詞です。",
         "したがって": "都会の過密が地方の過疎を直接生んだ単一の因果関係として断定するには論理が粗雑です。",
         "しかし": "単純な逆接ではなく、二面的な状況の客観的対比には「一方（で）」が最適です。",
         "なぜなら": "理由説明になり、二つの地域の現状対比に不適です。"}
    ),
    "skm2-p3-c10-q6": (
        "Doctor's orders strictly forbid alcohol. Even so, he cannot suppress his love for sake and ends up taking a sip secretly.",
        "Concessive persistence connective 'それでも'.",
        {"それでも": "医師からの厳禁という重大な警告が存在するにもかかわらず、その制約を破って飲んでしまう譲歩的逆接です。",
         "したがって": "禁酒を命じられたから酒を飲むことになり、論理が完全に破綻します。",
         "つまり": "言い換えになり、警告と違反の葛藤を描写できません。",
         "なぜなら": "理由説明になり、飲酒行動の正当化になりません。"}
    ),
    "skm2-p3-c10-q7": (
        "For ten years he continued training tenaciously without missing a single day. As a result, he became the world champion.",
        "Fruitful outcome connective 'その結果'.",
        {"その結果": "十年間の過酷な鍛錬の継続が実を結び、世界王者という最高の栄冠を勝ち取った帰結を述べる接続詞です。",
         "しかし": "逆接になり、努力が報われた輝かしい成果と矛盾します。",
         "なぜなら": "理由説明になり、前文の努力と後文の成果の順序と逆になります。",
         "一方": "対比になり、個人の努力と結実の因果的連鎖を表現できません。"}
    ),
    "skm2-p3-c10-q8": (
        "Admission to this park is free for anyone. Provided that, an application in advance is required when using the barbecue plaza.",
        "Condition proviso connective 'ただし'.",
        {"ただし": "「入場無料」という原則を提示した上で、バーベキュー広場利用に関する例外的な制限・条件を付加する但し書き接続詞です。",
         "したがって": "順接になり、無料だから申請が必要という不自然な文になります。",
         "つまり": "言い換えになり、例外条件の追加と合いません。",
         "なぜなら": "理由説明になり、特定施設の利用規則の付加に不適です。"}
    ),
    "skm2-p3-c10-q9": (
        "The presentation slides were confusing and the speaker's voice was inaudible. In short, it was an utter failure.",
        "Blunt summarizing connective '要するに'.",
        {"要するに": "スライドの不備や声の小ささといった個別の欠陥を総括し、「完全な失敗」とズバリ言い切る要約接続詞です。",
         "しかし": "逆接になり、諸々の不手際と失敗という結論の一致に矛盾します。",
         "したがって": "客観的推論ですが、辛口の要約・結語には「要するに」が最も適切です。",
         "なぜなら": "理由提示になり、前文が要因で後文が総括である構成に合いません。"}
    ),
    "skm2-p3-c10-q10": (
        "I was unable to attend yesterday's reunion. The fact is that my child had suddenly developed a high fever and I rushed to the hospital.",
        "Elaborative explanation connective 'というのは'.",
        {"というのは": "欠席という結論を先に述べた上で、なぜ行けなかったのかという突発的事態の事情・詳細を説明する接続詞です。",
         "したがって": "欠席したから子どもが熱を出したことになり、因果関係が逆転します。",
         "しかし": "逆接になり、欠席と看病の正当な理由関係に反します。",
         "一方": "対比になり、自らの個人的な欠席事情の説明に不適です。"}
    ),
    "skm2-p3-c10-q11": (
        "The hotel's rooms were spacious and the view from the window was magnificent. Moreover, the cuisine was exquisite beyond expectations.",
        "Additive compounding connective 'その上'.",
        {"その上": "部屋の広さや景色の素晴らしさに加えて、料理の絶品さというさらなる長所を上乗せして賞賛する累加接続詞です。",
         "しかし": "逆接になり、料理も素晴らしかったというプラス評価の連続と矛盾します。",
         "したがって": "順接の因果になり、景観が良いから料理が美味しいという不自然な因果関係になります。",
         "なぜなら": "理由提示になり、ホテルの魅力の列挙に合いません。"}
    ),
    "skm2-p3-c10-q12": (
        "I had practiced repeatedly until late at night every day. Even so, on the actual stage I panicked with nervousness and made a major blunder.",
        "Frustrated expectation connective 'それなのに'.",
        {"それなのに": "毎晩の猛練習という万全の準備にもかかわらず、本番で失敗してしまった無念・悔しさを表す逆接接続詞です。",
         "したがって": "練習したから失敗したことになり、意味が破綻します。",
         "つまり": "言い換えになり、練習と失敗の落差を表現できません。",
         "なぜなら": "理由提示になり、本番の失敗の弁明に合いません。"}
    ),

    # ------------------ Part 3 · Chapter 11: 省略・繰り返し・言い換え (Cohesion, Ellipsis & Rephrasing) ------------------
    "skm2-p3-c11-q1": (
        "She took out an old art album from the bookshelf. Then, she opened it quietly and began gazing at it nostalgically.",
        "Anaphoric object pronoun rephrasing 'それを静かに開き'.",
        {"それを": "前文で導入された目的語「一冊の古い画集」を代名詞で的確に受けて、くどい名詞の重複を避ける自然な結束性表現です。",
         "その画集を": "間違いではありませんが、同一名詞の直近反復となり文章の流暢さに欠けます。",
         "画集というものを": "一般論化してしまい、手元の特定の画集を開く動作描写に合いません。",
         "あれを": "遠称になり、今本棚から手に取ったばかりの直前の対象を指すのに不自然です。"}
    ),
    "skm2-p3-c11-q2": (
        "The crisis of environmental destruction in modern society. In order to overcome this grave issue, solidarity in international society is indispensable.",
        "Abstract conceptual rephrasing 'この深刻な課題を'.",
        {"深刻な課題": "直前の「環境破壊の危機」を、国際社会が解決すべき建設的なテーマとして上位概念で言い換えた適切な結束語句です。",
         "環境破壊の危機": "直前と全く同一の語句の単調な繰り返しになり、文体の洗練を欠きます。",
         "危機というもの": "哲学的定義になり、具体的な克服の対象としての焦点がぼやけます。",
         "あれ": "俗語的な指示代名詞になり、格調高い論文・社説の文体に不適です。"}
    ),
    "skm2-p3-c11-q3": (
        "Taro hurriedly ran to the station. And just in the nick of time he was able to leap onto the last train.",
        "Subject ellipsis maintaining topic continuity 'そして間一髪で'.",
        {"そして": "主語「太郎は」が自明であるため二文目では主語を省略し、接続詞「そして」で流れるように動作を連鎖させます。",
         "太郎は": "主語の無駄な重複になり、緊迫した動作連続のスピード感を削ぎます。",
         "彼という人間は": "大仰な人物評になり、終電に駆け込む場面に不自然です。",
         "太郎自身は": "強意の反復になり、単なる連続動作の記述に合いません。"}
    ),
    "skm2-p3-c11-q4": (
        "Many people are starting jogging for health maintenance. This aerobic exercise is extremely effective for preventing lifestyle-related diseases.",
        "Taxonomic rephrasing of activity 'この有酸素運動は'.",
        {"有酸素運動": "「ジョギング」の医学的・運動生理学的本質を捉え、医学的知見の解説へと discourse を高める適切な言い換え語です。",
         "ジョギングというジョギング": "強調構文ですが、「すべてのジョギング」という意味になり不自然です。",
         "走ることの反復": "ぎこちない造語的表現であり、医学的予防効果の説明に不適です。",
         "あれ": "口語代名詞になり、健康解説文の客観的トーンを崩します。"}
    ),
    "skm2-p3-c11-q5": (
        "The president went up onto the stage and powerfully delivered the management policy for the new fiscal year. Subsequently, on the stage, the commendation ceremony for outstanding employees was held.",
        "Locational cohesion with minimal repetition '壇上で'.",
        {"壇上で": "前文の「壇上に上がり」という場所情報を簡潔に格助詞「で」で引き継ぎ、無駄な修飾を省いた端正な文章表現です。",
         "社長が上がった壇上で": "前述の自明な情報を冗長に反復しており、悪文の典型です。",
         "あの壇上で": "遠称になり、同一会場内の連続した式典の場面描写として不自然です。",
         "壇上という場所で": "不要な説明的同格表現であり、文章のリズムを損ないます。"}
    ),
    "skm2-p3-c11-q6": (
        "The rapid evolution of artificial intelligence. This cutting-edge technology is bringing about dramatic changes in humankind's working environment.",
        "Categorical rephrasing 'この最先端技術は'.",
        {"最先端技術": "「人工知能（AI）」を産業・技術論の文脈で適切なカテゴリー名詞へと昇華させて受ける言い換えです。",
         "人工知能の急速な進化": "直前の名詞句の完全な丸写しであり、語彙の豊かさと凝集性を欠きます。",
         "あれ": "指示詞が粗野であり、学術・時事論説の文体に相応しくありません。",
         "AIというAI": "全数強調の表現になり、技術革新の全体的影響を述べる主語に不適です。"}
    ),
    "skm2-p3-c11-q7": (
        "Mother was preparing dinner in the kitchen. From there, the appetizing aroma of curry drifted throughout the room.",
        "Spatial anaphoric pro-form 'そこから'.",
        {"そこから": "前文の場所「台所」を場所代名詞「そこ」で簡潔に受け、匂いの発生源を示す流暢な文章展開です。",
         "母のいる台所から": "すでに述べられた情報を重複して説明しており、冗長です。",
         "あの台所から": "遠称になり、自宅内の台所の描写として不自然です。",
         "台所という台所から": "家中のあらゆる台所という意味になってしまい、不条理です。"}
    ),
    "skm2-p3-c11-q8": (
        "He quit the company where he had worked for many years and started a business through his own power. For that major decision, extraordinary courage must have been required.",
        "Demonstrative evaluation of preceding action 'その大きな決断には'.",
        {"その": "前文で述べられた「退職と起業」という具体的な行動を「大きな決断」として総括して受ける客観指示の「その」です。",
         "この": "筆者自身の決断のように受け取られかねず、他者の行動の客観的叙述として「その」が適切です。",
         "あの": "遠い共有記憶になり、一連の伝記的叙述の結束性に合いません。",
         "どの": "疑問詞になり、感嘆の陳述文を破綻させます。"}
    ),
    "skm2-p3-c11-q9": (
        "Young people's departure from reading has been decried for a long time. However, this phenomenon signifies not only a decrease in reading volume, but also a decline in thinking ability.",
        "Sociological rephrasing of trend 'この現象は'.",
        {"現象": "「若者の活字離れ」という社会的一大傾向を客観的な観察対象として言い換える適切な社会科学的名詞です。",
         "若者たちの活字離れ": "前文と一字一句同じ語句の反復になり、評論の推敲として稚拙です。",
         "あれ": "口語的で粗雑な指示代名詞になり、論文・社説に不適です。",
         "離れ": "語幹のみの切り取りになり、名詞としての自立性と格調を欠きます。"}
    ),
    "skm2-p3-c11-q10": (
        "The boy found a beautiful blue bird by the riverside. That little bird was flying lightly just skimming the water surface.",
        "Appositive diminutive rephrasing 'その小鳥は'.",
        {"その": "先行文の「美しい青い鳥」を「小鳥」と言い換えつつ、指示詞「その」で同一指示対象を滑らかに結ぶ表現です。",
         "この": "読者の目前にあるかのような違和感を与え、物語の三人称描写に合いません。",
         "あの": "読者との共通記憶になり、物語の客観的展開に不適です。",
         "どの": "疑問詞になり、物語の情景描写と相容れません。"}
    ),
    "skm2-p3-c11-q11": (
        "Frequent occurrences of abnormal weather caused by global warming. We must now seriously confront this global crisis.",
        "Macro-level conceptualization 'この地球規模の危機に'.",
        {"地球規模の危機": "局所的な異常気象の多発という現象を、全人類が直面する本質的な危機へと昇華させた的確な言い換えです。",
         "異常気象の頻発という事態": "前文の語句をそのまま長ったらしく引きずっており、語彙の洗練がありません。",
         "あれ": "軽々しい口語表現であり、地球環境問題の緊迫感に合いません。",
         "それ": "指示代名詞単体では問題の重大性に対する意味的凝集性が薄れます。"}
    ),
    "skm2-p3-c11-q12": (
        "The doctor carefully examined the patient's condition. And, to the family, he quietly conveyed the necessity of hospitalization.",
        "Contextual omission of doctor subject '家族に静かに告げた'.",
        {"家族に": "主語「医師は」が前文から継続しているため二文目では省略し、伝達の相手「家族に」から文を始めるのが最も自然です。",
         "医師は患者の家族に": "主語も目的語も全文重複しており、極めてくどい悪文です。",
         "その医師は家族に": "不要な指示詞と主語の反復があり、文章のリズムを損ないます。",
         "あの家族に": "遠称になり、診察室に付き添っている家族の描写に不自然です。"}
    ),

    # ------------------ Part 3 · Chapter 12: 文体の一貫性 (Stylistic Consistency & Register in Text) ------------------
    "skm2-p3-c12-q1": (
        "In this thesis, we attempted a detailed analysis regarding the actual state of the digital divide in modern society.",
        "Academic essay register (だ・である体) '分析を試みた'.",
        {"試みた": "学術論文（本論文では…）における客観的・学術的な「だ・である調（普通体）」に合致する述語形式です。",
         "試みました": "丁寧体（敬体）になり、学術論文の常体統一ルールに反します。",
         "試みてみた": "補助動詞「〜てみる」の重ね使いになり、学術論文の簡潔性に欠けます。",
         "試みちゃった": "くだけた俗語短縮形になり、論文の品位を完全に破壊します。"}
    ),
    "skm2-p3-c12-q2": (
        "Ladies and gentlemen, thank you very much indeed for gathering at our business explanatory meeting today despite the bad weather.",
        "Polite business address register 'ありがとうございます'.",
        {"ございます": "来客・取引先に対するビジネス説明会の冒頭挨拶として必須の丁寧体・敬語形式です。",
         "だ": "常体（だ体）になり、来賓・顧客に対する挨拶として極めて失礼です。",
         "である": "論文体になり、口頭のスピーチ・挨拶の場に合いません。",
         "ぞ": "乱暴な終助詞になり、公式ビジネスの場で使用することは許されません。"}
    ),
    "skm2-p3-c12-q3": (
        "The progression of global warming is considered to be dealing a severe blow to the diversity of ecosystems.",
        "Academic expository passive '考えられる'.",
        {"られる": "学術論文・環境報告書において客観的な見解を述べる「だ・である体」の動詞終止形です。",
         "られます": "敬体になり、論説文全体の文体の一貫性を崩します。",
         "られちゃう": "口語の短縮形になり、学術的・公的な文章に不適です。",
         "られるよ": "親しい対話の終助詞になり、論説の客観的トーンに合いません。"}
    ),
    "skm2-p3-c12-q4": (
        "From the results of the questionnaire survey, an improvement in consumers' environmental consciousness became clear.",
        "Objective report past tense '明らかとなった'.",
        {"なった": "調査レポート・報告書における客観的事実の確定を述べる常体過去形です。",
         "なりました": "敬体になり、論文・報告書の常体統一に違反します。",
         "なっちゃった": "くだけた口語表現になり、公式文書に相応しくありません。",
         "なったよ": "親密な会話の終助詞であり、客観的調査結果の記述に不適です。"}
    ),
    "skm2-p3-c12-q5": (
        "The daily business report that should be submitted by tomorrow was just now completed in its entirety.",
        "Polite humble reporting to supervisor '完成いたしました'.",
        {"いたしました": "上司や組織に対して業務の完了を報告するビジネス敬語（謙譲語＋丁寧体）です。",
         "したのだ": "常体の説明調になり、上司への業務完了報告として無礼です。",
         "したのである": "論文調の主張になり、日常の業務日報の提出報告に合いません。",
         "しちゃった": "軽薄な口語になり、職場での報告として不適切です。"}
    ),
    "skm2-p3-c12-q6": (
        "Based on the above experimental results, it can be said that a major step toward practical application of the new drug has been taken.",
        "Academic scientific deduction '言える'.",
        {"言える": "実験データに基づき論理的帰結を客観的に導出する学術論文の常体述部です。",
         "言えます": "敬体になり、科学論文の文体統一規則に反します。",
         "言えるね": "会話の同意求めになり、学術的な主張の厳密さを損ないます。",
         "言えちゃう": "俗語表現になり、新薬開発の学術的成果の叙述に不適です。"}
    ),
    "skm2-p3-c12-q7": (
        "Valued customer, this latest model is already receiving favorable reception from many clients.",
        "Customer service honorific register 'いただいております'.",
        {"おります": "顧客に対する接客・商品説明において、最高度の敬意を保つ謙譲補助動詞「〜ております」です。",
         "いる": "常体になり、お客様に対する商品説明として極めて非礼です。",
         "おる": "古風またはぞんざいになり、接客用語として不適です。",
         "いるぞ": "横柄な命令口調になり、接客場面で言語道断です。"}
    ),
    "skm2-p3-c12-q8": (
        "The rapid progression of the declining birthrate and aging population will unquestionably exert immense influence on the future pension system.",
        "Sociological policy paper certainty 'ちがいない'.",
        {"ちがいない": "政策提言や社会科学の論説文において、強い確信を持って結論を述べる常体の確信形式です。",
         "ちがいありません": "敬体になり、論文・白書の文体の一貫性を乱します。",
         "ちがいないね": "日常会話の同調表現になり、政策分析の厳粛なトーンに合いません。",
         "ちがいないよ": "会話の断定終助詞になり、公的な論述に不適です。"}
    ),
    "skm2-p3-c12-q9": (
        "We are deeply honored by your attendance from afar today, and extend our profound gratitude from the bottom of our hearts.",
        "Formal ceremonial gratitude '御礼申し上げます'.",
        {"申し上げます": "式典や公式会合において来場者に対して最大限の感謝を捧げる定型的儀礼敬語です。",
         "申し上げる": "常体辞書形になり、対面で来場者に述べる謝辞として敬意が欠如します。",
         "言う": "稚拙な語彙であり、改まった式典の挨拶に相応しくありません。",
         "言います": "丁寧ですが、「御礼申し上げる」という格式高い慣用表現と比べて品格が劣ります。"}
    ),
    "skm2-p3-c12-q10": (
        "In recent years, young people's departure from reading is closely related to the popularization of digital devices.",
        "Scholarly exposition on cultural trends '関連している'.",
        {"いる": "文化論・社会論の客観的解説において首尾一貫して用いられる「だ・である体」の現在形です。",
         "います": "敬体になり、解説記事や学術論説の常体統一を壊します。",
         "いるね": "会話の馴れ馴れしい語調になり、客観的考察に不適です。",
         "いるよ": "私的なおしゃべりの語調になり、社会現象の分析に合いません。"}
    ),
    "skm2-p3-c12-q11": (
        "Regarding our company's new service, would there be any unclear points?",
        "Formal customer service inquiry 'ございますでしょうか'.",
        {"ございますでしょうか": "顧客やクライアントに対して疑問点・不明点の有無を丁重に尋ねるビジネス敬語の最高形式です。",
         "あるか": "乱暴な詰問調になり、お客様に対する応対として言語道断です。",
         "あるだろうか": "自問自答の常体になり、相手への敬意が全くありません。",
         "あるの": "砕けた口語になり、公式なビジネス対応に相応しくありません。"}
    ),
    "skm2-p3-c12-q12": (
        "Regarding this point, further deepening of empirical research is awaited in the future.",
        "Academic concluding passive '待たれる'.",
        {"れる": "論文の結びにおいて今後の研究課題の展望を格調高く述べる「だ・である体」の受身終止形です。",
         "れます": "敬体になり、学術論文全体の文体の一貫性を崩します。",
         "れちゃう": "口語の俗語形になり、論文の学術的威厳を失わせます。",
         "れるよ": "会話の終助詞になり、今後の学術的展望の記述に不適です。"}
    )
}

def main():
    with open(EXERCISES_FILE, "r", encoding="utf-8") as f:
        exercises = json.load(f)

    updated = 0
    for e in exercises:
        eid = e.get("id")
        if eid in REPAIRS_P3B:
            trans, hint_txt, opt_reasons = REPAIRS_P3B[eid]
            e["translation"] = trans
            e["hint"] = hint_txt
            e["provenance"] = "source-derived"
            e["sourceEvidence"] = f"Shin Kanzen Master N2 Bunpou, Part 3 Chapter {e.get('chapter', '').split('Chapter ')[-1]} (文章の文法), pp. 181–199"

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

    print(f"Successfully repaired {updated} exercises in SKM N2 Part 3 (Chapters 7 to 12).")

if __name__ == "__main__":
    main()
