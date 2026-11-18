import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

FR_PAGES = {
    "a": "pp. 128–129", "b": "pp. 130–131", "c": "pp. 132–133",
    "d": "pp. 134–135", "e": "pp. 136–137", "f": "pp. 138–139",
    "g": "pp. 140–141"
}

# 84 semantic repairs for SKM N2 Part 1 Form Reviews A–G
REPAIRS_FR = {
    # === Form Review A (pp. 128–129): 助詞・格助詞の機能 ===
    "skm2-p1-form-review-a-q1": ("This fiscal year's International Environmental Summit was held grandly at the Kyoto International Conference Center.",
     "Formal diplomatic summit convening at prestigious conference venues.",
     {"にあたって": "事前準備を表すため、開催地を公的に示す場所格「において」に合いません。", "に際して": "機会指定であり、物理的開催場所の提示に不適です。", "にかけて": "おおよその範囲を表すため、特定の開催地の指定に合いません。"}),
    "skm2-p1-form-review-a-q2": ("Prior to the commencement of operations at the new factory, an environmental assessment survey of the surrounding region was conducted meticulously.",
     "Prerequisite environmental impact survey preceding industrial operations.",
     {"に際して": "開始の機会そのものを表すため、「それに先んじて行う事前点検」には「に先立って」が最適です。", "を契機に": "偶発的なきっかけを表すため、計画的な事前調査に不適です。", "に従って": "比例変化を表すため、先行する準備措置に合いません。"}),
    "skm2-p1-form-review-a-q3": ("According to reliable sources, the merger negotiations between the two major banks are making rapid progress behind closed doors.",
     "Financial market intelligence reporting secretive corporate merger negotiations.",
     {"に対して": "対象を表すため、情報源・根拠を提示する「によると」に合いません。", "にとって": "立場を表すため、外部情報の引用に不適です。", "をめぐって": "争乱を表すため、信頼できる筋からの情報引用になりません。"}),
    "skm2-p1-form-review-a-q4": ("In contrast to his older brother who possesses an outgoing personality with many friends, his younger brother is introverted and prefers quiet solitude.",
     "Direct psychological contrast between an outgoing and introverted sibling.",
     {"によって": "原因や手段を表すため、二人の性格の鮮明な対比には「に対して」が最適です。", "について": "話題を表すため、対照的な二人の個性の比較に不適です。", "にとって": "個人の評価基準を表すため、客観的な人物対比に合いません。"}),
    "skm2-p1-form-review-a-q5": ("Through the newly constructed high-speed railway, intercity transit time was slashed in half.",
     "Infrastructure upgrades cutting intercity travel times in half.",
     {"に対して": "対象を表すため、劇的な時間短縮をもたらした手段・原因には「によって」が最適です。", "について": "話題を表すため、交通インフラがもたらした成果に不適です。", "にとって": "立場を表すため、客観的な所要時間短縮に合いません。"}),
    "skm2-p1-form-review-a-q6": ("Regarding consumer behavior shifts in modern youth, the marketing department compiled a detailed research report.",
     "Corporate demographic research on youth consumption patterns.",
     {"によって": "手段を表すため、研究・分析のテーマ・対象の提示には「について（の）」が最適です。", "に対して": "対立・反発を表すため、客観的調査テーマの提示に不適です。", "にとって": "立場を表すため、市場分析の対象指定に合いません。"}),
    "skm2-p1-form-review-a-q7": ("For foreign researchers, learning Japanese business customs is an indispensable step toward workplace adaptation.",
     "Professional workplace adaptation challenges from an expatriate standpoint.",
     {"について": "話題を表すため、評価・判断の主体の立場を示す「にとって」に合いません。", "に対して": "対立・態度を表すため、「誰の目から見て不可欠か」という立場提示に不適です。", "によって": "手段を表すため、主観的必要性の評価基準になりません。"}),
    "skm2-p1-form-review-a-q8": ("A heated debate unfolded among participants surrounding the revision of the environmental protection bylaws.",
     "Civic deliberations regarding environmental regulatory revisions.",
     {"にこたえて": "要求に応じることを表すため、賛否両論の対立する議論の争点には「をめぐって」が最適です。", "に基づいて": "法規準拠を表すため、議論の対立軸の提示に不適です。", "を問わず": "条件不問を表すため、討議の中心テーマの指定に合いません。"}),
    "skm2-p1-form-review-a-q9": ("In response to the fervent requests of students, the university library extended its opening hours until midnight during exam week.",
     "Academic library extending opening hours in response to student requests.",
     {"をめぐって": "争乱を表すため、学生の熱心な要望に応えて時間を延長する親切な措置に合いません。", "に基づいて": "客観的規則を表すため、学生の切実な声に耳を傾けて「応える」対応に不適です。", "を問わず": "不問を表すため、要望に応答する因果関係になりません。"}),
    "skm2-p1-form-review-a-q10": ("Based upon experimental data verified multiple times, the research team published their groundbreaking academic findings.",
     "Publishing academic findings firmly based on verified empirical data.",
     {"をもとに": "創作素材を表すため、厳密な科学的実験データの検証に基づく立脚点には「に基づいて」が最適です。", "に反して": "背くことを表すため、実証データに裏打ちされた画期的発表に矛盾します。", "にそって": "手順遵守を表すため、データから論理的結論を導く根拠に合いません。"}),
    "skm2-p1-form-review-a-q11": ("Along the quiet path stretching beside the river, cherry blossoms in full bloom form a magnificent floral tunnel.",
     "Cherry blossom tunnel along a tranquil riverside pathway.",
     {"に基づいて": "データ根拠を表すため、川の物理的な線に沿って続く桜並木には「にそって」が最適です。", "をもとに": "創作素材を表すため、地理的な路の形状に沿った情景に不適です。", "に反して": "背くことを表すため、川沿いに続く並木の美しい光景に合いません。"}),
    "skm2-p1-form-review-a-q12": ("Defying pre-match predictions by all experts, the rookie team achieved an unprecedented upset victory.",
     "Rookie underdog team defying expert predictions to win.",
     {"に基づいて": "予測通りの結果を表すため、下馬評を覆して勝った番狂わせに矛盾します。", "をもとに": "素材を表すため、事前の専門家予測の裏切りに合いません。", "にそって": "予測通り進行したことになり、劇的な大逆転劇に真逆になります。"}),

    # === Form Review B (pp. 130–131): 複合格助詞・接続機能 ===
    "skm2-p1-form-review-b-q1": ("Although the calendar has passed the official beginning of spring, freezing winter chills below zero continue in the northern mountains.",
     "Sub-zero winter conditions persisting despite official spring calendar dates.",
     {"からすると": "推量の根拠を表すため、立春を過ぎたのに寒いという譲歩の逆接には「とはいいながら」が最適です。", "にしたがって": "比例変化を表すため、暦と実際の気温の齟齬に不適です。", "に際して": "機会指定であり、暦と寒さの逆接関係に合いません。"}),
    "skm2-p1-form-review-b-q2": ("Judging from experimental data and observation findings up to now, the efficacy and safety of the new drug can be concluded as exceptionally high.",
     "Deducing clinical efficacy and safety from trial data and observations.",
     {"とはいいながら": "逆接を表すため、データから判断して高いと結論づける肯定推論には「からすると」が最適です。", "に反して": "背くことを表すため、データと結論の一致に矛盾します。", "にともなって": "事象の付随を表すため、科学的データに基づく客観的判断の導出に不適です。"}),
    "skm2-p1-form-review-b-q3": ("In parallel with the advance of globalization, interdependence among world nations has deepened to historic levels.",
     "International interdependence deepening in parallel with globalization.",
     {"からすると": "判断の推量根拠を表すため、グローバル化の進展という時代の大きな流れの並行には「にともなって」が最適です。", "とはいいながら": "逆接を表すため、グローバル化と相互依存深化の順接推移に矛盾します。", "に反して": "背くことを表すため、時代の大きな潮流と整合しません。"}),
    "skm2-p1-form-review-b-q4": ("Judged from the perspective of cost efficiency, this old machinery should be replaced with state-of-the-art models immediately.",
     "Evaluating immediate machinery upgrades through a cost-efficiency lens.",
     {"からすると": "正解です。費用対効果という判断基準・視点から見て更新すべきと判定します。", "とはいいながら": "逆接を表すため、コスト面からの合理的な提案に合いません。", "にともなって": "付随変化を表すため、評価基準からの判断提示に不適です。", "に反して": "背くことを表すため、コスト効率に叶った更新提案に矛盾します。"}),
    "skm2-p1-form-review-b-q5": ("Although I understand in my head that studying every day is vital, I cannot help slacking off on holidays.",
     "Mental awareness of study importance conceded against holiday slacking.",
     {"からすると": "判断の推量根拠を表すため、頭では分かっているのにサボってしまう心理的葛藤には「とはいいながら」が最適です。", "にともなって": "付随変化を表すため、自覚と行動のギャップに不適です。", "にしたがって": "比例変化を表すため、休日に怠惰になる逆接に合いません。"}),
    "skm2-p1-form-review-b-q6": ("Accompanying the sharp population decline, maintaining local train transit lines in rural areas has become a critical challenge.",
     "Rural transit lines facing viability crises accompanying population drops.",
     {"とはいいながら": "逆接を表すため、人口減少に伴って路線維持が難しくなる直接の因果関係には「にともなって」が最適です。", "からすると": "判断基準を表すため、過疎化という社会現象から派生した問題に不適です。", "に反して": "背くことを表すため、人口減少と維持難の必然性に矛盾します。"}),
    "skm2-p1-form-review-b-q7": ("Judging from his confident speech and body language, his job interview must undoubtedly have been a success.",
     "Deducing interview success from confident speech and posture.",
     {"とはいいながら": "逆接を表すため、自信に満ちた態度から面接成功を推し量る「からすると」に合いません。", "にともなって": "付随変化を表すため、様子を手掛かりとする推量に不適です。", "に反して": "背くことを表すため、態度と面接成果の合致に矛盾します。"}),
    "skm2-p1-form-review-b-q8": ("Although modern society has grown tremendously convenient, on the flip side spiritual loneliness has increased.",
     "Spiritual loneliness increasing although modern society became convenient.",
     {"からすると": "判断根拠を表すため、便利になったものの孤独が深まったという譲歩には「とはいいながら」が最適です。", "にともなって": "客観的な付随を表しますが、文明の便利さと心の孤独という逆接の深みには「とはいいながら」が格調高くなります。", "に反して": "背くことを表すため、二面性の譲歩に合いません。"}),
    "skm2-p1-form-review-b-q9": ("Accompanying corporate restructuring, the workforce was reorganized and modern digital equipment was deployed.",
     "Corporate restructuring accompanying digital equipment deployment.",
     {"とはいいながら": "逆接を表すため、組織改革に伴って機材が導入された一連の改革措置には「にともなって」が最適です。", "からすると": "判断推量根拠を表すため、全社的施策の連動に不適です。", "にしたがって": "比例変化を表すため、事業再編の一斉措置に合いません。"}),
    "skm2-p1-form-review-b-q10": ("Judging from this ancient map, a large castle existed in this area about 400 years ago.",
     "Deducing a historic castle's existence 400 years ago from an ancient map.",
     {"とはいいながら": "逆接を表すため、古地図という歴史的証拠から推論する「からすると」に合いません。", "にともなって": "付随変化を表すため、文献からの歴史的推論に不適です。", "に反して": "背くことを表すため、地図に描かれた情報の解読に矛盾します。"}),
    "skm2-p1-form-review-b-q11": ("Although advanced AI technology is remarkably innovative, establishing human ethical guidelines must not be neglected.",
     "AI innovation admitted although ethical guidelines remain imperative.",
     {"からすると": "判断根拠を表すため、技術革新を認めつつ倫理確立を促す譲歩には「とはいいながら」が最適です。", "にともなって": "付随を表しますが、倫理の怠慢を戒める強い譲歩の逆接に「とはいいながら」が合致します。", "に反して": "背くことを表すため、AI技術の革新性と倫理要請の対峙に合いません。"}),
    "skm2-p1-form-review-b-q12": ("Accompanying sudden changes in the global weather climate, torrential downpours and droughts have occurred frequently worldwide.",
     "Frequent severe downpours and droughts accompanying global climate shifts.",
     {"とはいいながら": "逆接を表すため、気候変動に伴って異常気象が多発する直接の因果関係には「にともなって」が最適です。", "からすると": "個人の推量根拠を表すため、地球規模の気象変動と災害の連動に不適です。", "にしたがって": "比例変化を表すため、世界各地での異常気象の頻発という付随事象に合いません。"}),

    # === Form Review C (pp. 132–133): 文語的表現・硬い形式 ===
    "skm2-p1-form-review-c-q1": ("Publicly insulting an innocent citizen in front of crowds is a grave misconduct that can never be forgiven in a state ruled by law.",
     "Unforgivable violation: publicly insulting an innocent citizen in a lawful state.",
     {"べし": "義務を表すため、名詞を修飾する連体否定「許されざる（許すことができない）」に合いません。", "まじき": "身分としてあるまじき行為を責める語であり、「許されまじき」より「許されざる過失」が正統な慣用句です。", "べき": "肯定の義務になり、「断じて許されない」という完全否定の趣旨と真逆になります。"}),
    "skm2-p1-form-review-c-q2": ("As a mature citizen comprising society, one ought to possess firm responsibility for one's speech and actions at all times.",
     "Moral duty: mature citizens ought to take firm responsibility for speech and actions.",
     {"ざる": "否定を表すため、責任を持つべきという積極的な義務に矛盾します。", "まじき": "禁止・不当を表すため、自らの言動に責任を持つ当然の義務に合いません。", "べし": "正解です。硬い書面語で「責任を持つべし（持つべきだ）」と倫理的規範を宣言します。"}),
    "skm2-p1-form-review-c-q3": ("Disclosing confidential information entrusted by a patient is misconduct that must never be committed by a physician.",
     "Medical ethics: disclosing patient confidential data is conduct never to be done.",
     {"ざる": "単なる否定になり、医師としての倫理的許容限度を絶対に超えているという「あるまじき行為」に合いません。", "べし": "肯定の義務になり、情報漏洩を命じることになって破綻します。", "べき": "肯定義務を表すため、医師としてあってはならない重大背信の断罪に不適です。"}),
    "skm2-p1-form-review-c-q4": ("Facing acute environmental collapse, politicians cannot afford to idly look on without enacting immediate regulations.",
     "Political responsibility: politicians cannot afford to idly spectate environmental collapse.",
     {"ざる": "単なる否定になり、「座視しているわけにはいかない」という許されざる傍観の告発に「座視すべからざる」が適合します。", "まじき": "身分不当を表すため、事態の切迫した禁止に不適です。", "べし": "肯定義務になり、傍観を命じることになり真逆になります。"}),
    "skm2-p1-form-review-c-q5": ("A teacher accepting bribes from students' parents is an intolerable crime utterly unacceptable for an educator.",
     "Academic corruption: accepting bribes from parents is behavior unacceptable for educators.",
     {"ざる": "単なる否定連体になり、「教育者として絶対に許されない」という立場規定の糾弾には「あるまじき犯罪」が最適です。", "べし": "肯定義務になり、賄賂受領を命じることになって破綻します。", "べき": "肯定義務を表すため、教育者の倫理的堕落の告発に合いません。"}),
    "skm2-p1-form-review-c-q6": ("Even when confronted with formidable difficulties, people who challenge ideals must never lose their indomitable spirit.",
     "Resilience duty: people challenging ideals must never lose an indomitable spirit.",
     {"ざる": "単なる否定になり、「不撓不屈の精神を失うべからず」という強い戒めに「べからず」が合致します。", "まじき": "身分不当を表すため、挑戦者の心構えの戒律に不適です。", "べし": "肯定義務になり、精神を失えと命じることになり破綻します。"}),
    "skm2-p1-form-review-c-q7": ("Fabricating experimental research data in an academic paper is an outrageous deed completely unacceptable for a scholar.",
     "Scientific integrity: fabricating research data is a deed unacceptable for a scholar.",
     {"ざる": "単なる否定になり、「学者として絶対にあってはならない」という身分倫理の断罪には「あるまじき暴挙」が最適です。", "べし": "肯定義務になり、捏造を命じることになって破綻します。", "べき": "肯定義務を表すため、学術不正の告発に合いません。"}),
    "skm2-p1-form-review-c-q8": ("In a country ruled by law, unlawful abuse of state authority is a tyranny that can never be tolerated.",
     "Rule of law: unlawful abuse of state power is tyranny that can never be tolerated.",
     {"べし": "肯定義務になり、国家権力の濫用を容認することになり真逆になります。", "まじき": "身分不当を表す語であり、「決して許されない暴挙」には連体否定「許されざる暴挙」が正統です。", "べき": "肯定義務を表すため、横暴の完全否定に合いません。"}),
    "skm2-p1-form-review-c-q9": ("Those who guide people in judicial courts must preserve absolute fairness and maintain an attitude of strict impartiality.",
     "Judicial integrity: judges in courts must preserve strict impartiality.",
     {"ざる": "否定を表すため、厳正中立を守るべきという肯定の義務に矛盾します。", "まじき": "禁止を表すため、裁判官としての至高の規範宣言に合いません。", "べし": "正解です。「厳正中立を保持すべし」と司法の重い職責を格調高く宣言します。"}),
    "skm2-p1-form-review-c-q10": ("Abandoning passenger rescue and fleeing ahead of others during a shipwreck is conduct utterly unacceptable for a ship captain.",
     "Maritime duty: fleeing before passengers during shipwrecks is unacceptable for captains.",
     {"ざる": "単なる否定になり、「船長として絶対にあってはならない」というプロの責務の放棄には「あるまじき行為」が最適です。", "べし": "肯定義務になり、逃亡を命じることになって破綻します。", "べき": "肯定義務を表すため、船長の職責放棄の断罪に合いません。"}),
    "skm2-p1-form-review-c-q11": ("When visiting traditional solemn sacred grounds, do not enter with irreverent, frivolous attitudes.",
     "Sacred sanctuary etiquette: do not enter with irreverent, frivolous attitudes.",
     {"ざる": "単なる否定になり、「入るべからず（立ち入るな）」という厳格な古風の禁止には「べからず」が最適です。", "まじき": "身分不当を表すため、神聖な場所への立ち入り禁止看板に不適です。", "べし": "肯定義務になり、不敬な態度での侵入を促すことになり真逆になります。"}),
    "skm2-p1-form-review-c-q12": ("Violating fundamental human rights through discrimination and persecution is a grave sin that can never be permitted by human society.",
     "Universal human rights: persecuting human rights is a grave sin never to be permitted.",
     {"べし": "肯定義務になり、人権侵害の重罪を肯定することになり破綻します。", "まじき": "身分不当を表す語であり、「人類社会として断じて許されない罪過」には連体否定「許されざる罪過」が最適です。", "べき": "肯定義務を表すため、差別の断罪に合いません。"}),

    # === Form Review D (pp. 134–135): 「こと」「もの」の整理 ===
    "skm2-p1-form-review-d-q1": ("Throughout his 30 years of tenure, he faithfully served the company without being late or absent even once.",
     "Unblemished attendance record: 30 years without being late or absent even once.",
     {"ことに": "感情の強調（驚いたことに）を表すため、遅刻欠勤を一切しないという動作の否定継続には「ことなく」が最適です。", "ことだから": "人柄からの推量を表すため、勤務態度の事実叙述に不適です。", "ものだから": "個人の言い訳を表すため、30年間の勤勉の称賛に合いません。"}),
    "skm2-p1-form-review-d-q2": ("To my great surprise, my beloved car that had been stolen yesterday was found completely unharmed in the station parking lot.",
     "Astonishing relief: stolen car found completely unharmed in station parking.",
     {"ことなく": "動作の非発生を表すため、「驚いたことに」という話者の心情の強調提示に合いません。", "ことだから": "人柄の推量を表すため、盗難車の発見という劇的な出来事の感嘆に不適です。", "ものだから": "言い訳を表すため、奇跡的な無事発見の喜びに合いません。"}),
    "skm2-p1-form-review-d-q3": ("Knowing his earnest and meticulous character, he will surely prepare documents perfectly by tomorrow's deadline.",
     "Character certainty: knowing his earnest character, he will finish files perfectly.",
     {"ことだから": "正解です。相手の普段の信頼できる人柄を根拠として確信を述べる「彼のことだから」です。", "ことに": "感情の強調を表すため、人柄からの推量に合いません。", "ことなく": "動作の否定を表すため、人柄の提示に不適です。", "ものだから": "言い訳を表すため、他者への信頼の言明になりません。"}),
    "skm2-p1-form-review-d-q4": ("The marathon runner sprinted past the finish line at full power without yielding to fatigue until the very end.",
     "Marathon finish: sprinting across the finish line without yielding to fatigue.",
     {"ことに": "心情強調を表すため、疲労に負けずに走り抜いた動作の様態には「ことなく」が最適です。", "ことだから": "人柄推量を表すため、レース終盤の奮闘描写に不適です。", "ものだから": "言い訳を表すため、アスリートの気迫の完走に合いません。"}),
    "skm2-p1-form-review-d-q5": ("How delightful it was: the project that had faced consecutive difficulties achieved its goals with flying colors.",
     "Triumphant relief: difficult project overcoming setbacks to achieve goals.",
     {"ことなく": "動作の否定を表すため、「嬉しいことに」という感情の主観的提示には合いません。", "ことだから": "人柄を表すため、プロジェクト達成の喜びに不適です。", "ものだから": "言い訳を表すため、目標達成の快挙の報告に合いません。"}),
    "skm2-p1-form-review-d-q6": ("Knowing a cheerful person like her, she is bound to liven up today's social gathering brightly.",
     "Social atmosphere certainty: knowing her cheerful self, she will liven up the party.",
     {"ことだから": "正解です。「明るい彼女のことだから」と人柄を取り立てて確信を述べます。", "ことに": "心情強調を表すため、人柄の提示に合いません。", "ことなく": "動作の否定を表すため、彼女の明るさの言及に不適です。", "ものだから": "言い訳を表すため、他者の長所への信頼に合いません。"}),
    "skm2-p1-form-review-d-q7": ("The ship sailed smoothly through the ocean without encountering any stormy weather or accidents.",
     "Smooth ocean navigation: sailing steadily without storms or accidents.",
     {"ことに": "感情を表すため、荒天に遭わない客観的航海の描写には「ことなく」が最適です。", "ことだから": "人柄推量を表すため、船舶の航行に不適です。", "ものだから": "言い訳を表すため、順風満帆な航海の叙述に合いません。"}),
    "skm2-p1-form-review-d-q8": ("To my great regret, our proposal that had been polished over months was defeated in the final selection.",
     "Bittersweet regret: proposal polished over months defeated at final selection.",
     {"ことなく": "動作の否定を表すため、「悔しいことに」という無念の心情の強調には「ことに」が最適です。", "ことだから": "人柄を表すため、選考落選の無念に合いません。", "ものだから": "言い訳を表すため、悔しさを込めた客観的結果の報告に不適です。"}),
    "skm2-p1-form-review-d-q9": ("Knowing a cautious, meticulous individual like him, he must undoubtedly have prepared an alternative contingency plan.",
     "Planning prudence certainty: knowing his cautious self, he prepared backups.",
     {"ことだから": "正解です。「慎重な彼のことだから」と几帳面な性格から予備計画の存在を確信します。", "ことに": "感情強調を表すため、人柄からの推量に合いません。", "ことなく": "動作の否定を表すため、性格の提示に不適です。", "ものだから": "言い訳を表すため、他者の用意周到さへの信頼に合いません。"}),
    "skm2-p1-form-review-d-q10": ("The veteran technician inspected precision parts meticulously without overlooking even the slightest flaw.",
     "Artisan vigilance: inspecting precision parts without missing the slightest flaw.",
     {"ことに": "感情を表すため、傷を見逃さない徹底した検品の様態には「ことなく」が最適です。", "ことだから": "人柄推量を表すため、精密検査の動作描写に不適です。", "ものだから": "言い訳を表すため、職人の卓越した技術に合いません。"}),
    "skm2-p1-form-review-d-q11": ("To our great fortune, just when the rain began pouring, a vacant taxi happened to stop right in front of us.",
     "Serendipitous timing: vacant taxi pulling up right as heavy rain started.",
     {"ことなく": "動作の否定を表すため、「幸いなことに」という好運の感謝の強調には「ことに」が最適です。", "ことだから": "人柄を表すため、タクシーの偶然の出現に合いません。", "ものだから": "言い訳を表すため、幸運な出来事の叙述に不適です。"}),
    "skm2-p1-form-review-d-q12": ("Knowing a person of unyielding determination like him, he will never retreat until he reaches his goals.",
     "Indomitable grit certainty: knowing his grit, he will not retreat until reaching goals.",
     {"ことだから": "正解です。「不屈の彼のことだから」と強靭な精神力から決して諦めない姿勢を確信します。", "ことに": "感情強調を表すため、人柄の提示に合いません。", "ことなく": "動作の否定を表すため、人物評価の文頭に不適です。", "ものだから": "言い訳を表すため、不屈の闘志への称賛に合いません。"}),

    # === Form Review E (pp. 136–137): 「わけ」「ところ」の整理 ===
    "skm2-p1-form-review-e-q1": ("It is completely natural that it is so freezing outside. Powder snow is dancing down outside the window, after all.",
     "Logical conclusion: freezing outdoor cold naturally explained by falling snow.",
     {"わけだ": "正解です。目の前で雪が降っている事実から「寒いのも当然だ」と納得する論理的帰結です。", "わけがない": "完全否定を表すため、外が寒い現実の納得に矛盾します。", "わけではない": "部分否定を表すため、寒さの当然性の説明に合いません。", "ところだった": "寸前の回避を表すため、現に雪が降っている情景に不適です。"}),
    "skm2-p1-form-review-e-q2": ("Because their facial features and voice tone are spitting images of each other, they are often mistaken for twins by first-time acquaintances.",
     "Mistaken identity origin: identical voice and face causing twin mix-ups.",
     {"ところから": "正解です。顔や声がそっくりだという事実・手掛かりから双子と間違えられる由来を示します。", "わけがない": "不可能性を表すため、双子に間違えられる理由説明に合いません。", "どころか": "反駁対比を表すため、似ているから間違えられる因果関係に不適です。", "ばかりに": "後悔の理由を表すため、客観的な人違いの由来に合いません。"}),
    "skm2-p1-form-review-e-q3": ("An experienced veteran who has undergone arduous training for years would never make such a rudimentary blunder.",
     "Expert reliability: experienced veterans would never make rudimentary blunders.",
     {"わけがない": "正解です。長年の鍛錬を積んだベテランが初歩的ミスをするはずがないという論理的完全否定です。", "わけだ": "当然の納得を表すため、ミスをするはずがないという否定に合いません。", "わけではない": "部分否定になり、ベテランの絶対的な技術への信頼が薄れます。", "ところだった": "寸前の回避を表すため、ミスの不可能性の断定に不適です。"}),
    "skm2-p1-form-review-e-q4": ("Because I was walking while staring down at my smartphone, I came within a hair's breadth of colliding with a utility pole.",
     "Close call avoided: narrowly averting collision with a utility pole while texting.",
     {"ところだった": "正解です。「もう少しで電柱にぶつかるところだった」と危機一髪の回避を表します。", "わけだ": "当然の帰結を表すため、寸前で回避した事故の描写に合いません。", "わけがない": "不可能性を表すため、危うくぶつかりそうになった臨場感に不適です。", "わけではない": "部分否定であり、歩きスマホの危機一髪の体験に合いません。"}),
    "skm2-p1-form-review-e-q5": ("It is not that I dislike Japanese cuisine, but I simply struggle with raw fish like sashimi.",
     "Dietary clarification: enjoying Japanese food overall while struggling with sashimi.",
     {"わけではない": "正解です。「和食が嫌いなわけではない」と柔らかく部分否定して留保します。", "わけだ": "当然の帰結を表すため、自分の好みの慎重な留保に合いません。", "わけがない": "完全否定になり、刺身が苦手である実態と矛盾します。", "ところだった": "寸前の回避を表すため、食の好みの説明に不適です。"}),
    "skm2-p1-form-review-e-q6": ("Because the lake water is transparent to the bottom like crystal, this place has been known as 'Mirror Lake' since olden times.",
     "Toponymic origin: crystal transparency leading to the name 'Mirror Lake'.",
     {"ところから": "正解です。水が澄み切っているという客観的事実から「鏡湖」と名付けられた由来を示します。", "わけがない": "不可能性を表すため、湖の命名由来に合いません。", "どころか": "対比反駁を表すため、透明な水面からの命名の因果に不適です。", "ばかりに": "後悔を表すため、名所の美しい由来説明に合いません。"}),
    "skm2-p1-form-review-e-q7": ("You practiced studying 10 hours a day for months. No wonder you passed with flying colors; it makes absolute sense.",
     "Natural validation: scoring top marks after 10-hour daily study makes total sense.",
     {"わけだ": "正解です。「1日10時間猛勉強したのだからトップ合格するのも当然だ」と納得します。", "わけがない": "合格の不可能性になり、猛勉強の成果の祝福と真逆になります。", "わけではない": "部分否定になり、トップ合格の快挙の納得に合いません。", "ところだった": "寸前の回避になり、現に合格した喜びに不適です。"}),
    "skm2-p1-form-review-e-q8": ("I almost hit 'Send' on the confidential email without noticing that I had mistyped the recipient address.",
     "Near catastrophe avoided: almost sending confidential emails to wrong recipients.",
     {"ところだった": "正解です。「誤送信するところだった」と重大な情報漏洩の寸前回避を表します。", "わけだ": "当然の帰結を表すため、危うく送信しそうになった焦燥感に合いません。", "わけがない": "不可能性を表すため、あわや大事故の生々しい体験に不適です。", "わけではない": "部分否定であり、宛先間違いの寸前回避の描写になりません。"}),
    "skm2-p1-form-review-e-q9": ("A top-tier restaurant praised by gourmets worldwide would never serve stale, poor-quality seafood.",
     "Gastronomic standard: world-renowned restaurants would never serve stale seafood.",
     {"わけがない": "正解です。世界の美食家が絶賛する店で古い食材を出すはずがないという絶対否定です。", "わけだ": "当然の肯定になり、まずい料理を出すことになって破綻します。", "わけではない": "部分否定になり、名店の徹底した品質管理の確信に合いません。", "ところだった": "寸前の回避を表すため、食材の鮮度保証に不適です。"}),
    "skm2-p1-form-review-e-q10": ("Because the historical warrior took shelter from rain in this pine tree, this ancient tree has been revered as 'Rain-Shelter Pine'.",
     "Historic botanical origin: sacred pine revered after sheltering an ancient warrior.",
     {"ところから": "正解です。雨宿りをしたという史実・伝承の起源から「雨宿りの松」と呼ばれた由来を示します。", "わけがない": "不可能性を表すため、名木の由来説明に合いません。", "どころか": "対比を表すため、雨宿り伝説からの命名に不適です。", "ばかりに": "後悔を表すため、御神木の由緒ある歴史に合いません。"}),
    "skm2-p1-form-review-e-q11": ("It is not that I cannot afford to purchase this luxury coat, but I decided against it considering how often I would wear it.",
     "Prudent purchasing: passing on luxury coats based on wear utility, not budget inability.",
     {"わけではない": "正解です。「買えないわけではない」と金銭的余裕はあるが着用頻度を考慮した賢明な部分否定です。", "わけだ": "当然の帰結を表すため、買い控えの理由説明に合いません。", "わけがない": "完全否定になり、資金はあるという前提と矛盾します。", "ところだった": "寸前の回避を表すため、冷静な判断の留保に不適切です。"}),
    "skm2-p1-form-review-e-q12": ("Because I missed stepping on the slick frozen winter road, I came within inches of falling over backwards.",
     "Winter safety near-fall: almost slipping backwards on slick frozen roads.",
     {"ところだった": "正解です。「後ろに転倒するところだった」と転びそうになった危機の回避を描写します。", "わけだ": "当然の帰結になり、転倒を免れた安堵に合いません。", "わけがない": "不可能性を表すため、ツルツル道路での足滑りの臨場感に不適です。", "わけではない": "部分否定であり、スリップ事故の回避描写になりません。"}),

    # === Form Review F (pp. 138–139): 接続助詞・並立・限定の整理 ===
    "skm2-p1-form-review-f-q1": ("Even though it is a holiday morning, my mother is constantly nagging, telling me to clean the room, go shopping, and so forth.",
     "Holiday morning annoyance: mother constantly nagging with chore checklists.",
     {"だの／だの": "正解です。あれこれ不満を込めて雑多な用事を並列列挙する「〜だの〜だの」です。", "やら／やら": "客観的な取り散らかりを表すことが多く、不満の小言の列挙には「だの」が最適です。", "なり／なり": "選択の提案（〜なり〜なりしろ）になり、母の小言の列挙に合いません。", "とか／とか": "中立的な例示になり、休日なのに小言を言われてうんざりする語気が出ません。"}),
    "skm2-p1-form-review-f-q2": ("Those who can enjoy the benefits of today's special discount sale are exclusively customers who completed prior membership registration.",
     "Promotional eligibility restricted exclusively to pre-registered members.",
     {"のみ": "正解です。「お客様のみです」と公式の格調高い限定を明示します。", "ばかり": "過剰や偏りを表すため、会員限定の恩恵の厳正な規定に合いません。", "だけ": "日常会話的であり、公的なセール規定の格式には「のみ」が最も品位があります。", "さえ": "極端な例示を表すため、対象者の限定規定に不適切です。"}),
    "skm2-p1-form-review-f-q3": ("If you have concerns about the proposal, propose alternatives yourself or consult seniors, instead of just remaining silent.",
     "Constructive problem-solving: proposing alternatives or consulting mentors.",
     {"なり／なり": "正解です。「代案を出すなり先輩に相談するなり」と同種の解決策を選択肢として促します。", "だの／だの": "不満の列挙になり、前向きな行動の提案に合いません。", "やら／やら": "困惑の並列になり、自分で選んで行動すべき選択肢の提示に不適です。", "とか／とか": "日常の軽い例示になり、アドバイスとしての引き締まった提案になりません。"}),
    "skm2-p1-form-review-f-q4": ("Because the room was cluttered with books, clothes, and various items scattered all over the floor, there was hardly any space to step.",
     "Cluttered room chaos: books and clothes strewn all over the floor.",
     {"やら／やら": "正解です。雑多なものが散乱して収拾がつかない混乱状態の列挙「本やら服やら」です。", "だの／だの": "不満の文句の列挙になり、物の乱雑な散乱描写に合いません。", "なり／なり": "選択の提案になり、床に散らばった物の状態描写に不適です。", "のみ": "限定を表すため、色々なものが散乱している情景に矛盾します。"}),
    "skm2-p1-form-review-f-q5": ("His daily diet consists solely of hamburgers and ramen; he doesn't eat vegetables at all, so his health is concerning.",
     "Unhealthy dietary imbalance: eating exclusively fast food without vegetables.",
     {"ばかり": "正解です。特定の好物だけに偏って食べ続ける不健全な偏食を批判的に表す「ばかり」です。", "のみ": "中立的な限定であり、野菜を食べない偏食への呆れ・懸念のニュアンスが出ません。", "さえ": "極端な例示になり、偏食の継続習慣の描写に合いません。", "だの": "並立列挙になり、ハンバーガーとラーメンに偏る生活に不適です。"}),
    "skm2-p1-form-review-f-q6": ("He keeps offering endless excuses, saying the weather was bad, the train was delayed, and other complaints.",
     "Endless excuse-making: grumbling about weather and delayed transit.",
     {"だの／だの": "正解です。不満や言い訳をあれこれ並べ立てる態度を批判する「〜だの〜だの」です。", "やら／やら": "混乱した状況を表すため、自己保身の言い訳の並列に合いません。", "なり／なり": "選択提案になり、言い訳を並べる批判に不適です。", "とか／とか": "中立的な伝聞になり、呆れて聞き流す言い訳の列挙に合いません。"}),
    "skm2-p1-form-review-f-q7": ("In this strict corporate competition, what counts in the end is exclusively actual achievements, not eloquent speeches.",
     "Meritocratic reality: strict corporate competition rewards actual achievements alone.",
     {"のみ": "正解です。「実績のみである」と弁舌を排した厳正な成果主義の限定を断定します。", "ばかり": "偏りを表すため、実績だけが評価される厳格な判定に合いません。", "さえ": "極端例になり、評価の唯一基準の限定に不適です。", "だの": "並立になり、実績の絶対性の断定に合いません。"}),
    "skm2-p1-form-review-f-q8": ("If you have free time on the weekend, try reading in the library or exercising lightly to refresh your mind.",
     "Weekend leisure advice: read in libraries or exercise lightly to refresh.",
     {"なり／なり": "正解です。「読書するなり運動するなり」と有意義な過ごし方の選択肢を提示します。", "だの／だの": "不満の列挙になり、心地よい休日のリフレッシュ提案に合いません。", "やら／やら": "困惑の並立になり、自発的な休日の選択に不適です。", "のみ": "限定を表すため、選択肢の提示になりません。"}),
    "skm2-p1-form-review-f-q9": ("After moving into the new apartment, with unpacking boxes and completing administrative paperwork, I was overwhelmed with busyness.",
     "Post-move overwhelm: frantic unpacking boxes and administrative paperwork.",
     {"やら／やら": "正解です。引っ越し直後の雑多な用事に追われてんてこ舞いな状況を「〜やら〜やら」で表します。", "だの／だの": "人の発言の不満列挙になり、身辺の多忙な事態に合いません。", "なり／なり": "選択の提案になり、現実に忙殺された回想に不適です。", "ばかり": "偏りを表すため、雑多な作業の複合に合いません。"}),
    "skm2-p1-form-review-f-q10": ("He sits in front of the television all day long doing nothing but playing video games without studying at all.",
     "Chronic indolence: gaming all day long in front of the TV without studying.",
     {"ばかり": "正解です。ゲームばかりして勉強しない怠惰な態度を批判的に描写する「ばかり」です。", "のみ": "公式な限定であり、親や教師が嘆く偏った怠慢行動に合いません。", "さえ": "極端例示になり、ゲームに耽溺する日常に不適です。", "なり": "選択提案になり、勉強放棄の批判に合いません。"}),
    "skm2-p1-form-review-f-q11": ("He is always grumbling complaints, saying the job is tough, the salary is low, and other grievances.",
     "Chronic workplace dissatisfaction: grumbling over tough workloads and low salary.",
     {"だの／だの": "正解です。愚痴や不満を並べ立てる辟易した態度を咎める「〜だの〜だの」です。", "やら／やら": "客観的な散らかりになり、本人の文句の並列に合いません。", "なり／なり": "選択提案になり、後ろ向きな愚痴の列挙に不適です。", "とか／とか": "中立的な例示になり、愚痴への苛立ちのトーンが出ません。"}),
    "skm2-p1-form-review-f-q12": ("When you fall ill alone, with high fever and chills, and nobody to bring meals, helpless loneliness strikes.",
     "Vulnerability of solo illness: fever, chills, and lack of care multiplying helplessness.",
     {"やら／やら": "正解です。一人暮らしで病気の際、熱や寒気など不安要素が重なる心細さを「〜やら〜やら」で表します。", "だの／だの": "他人の不満の小言になり、病気の苦境描写に合いません。", "なり／なり": "選択提案になり、病床の孤独の心理に不適です。", "ばかり": "偏りを表すため、多様な苦難の重なりに合いません。"}),

    # === Form Review G (pp. 140–141): 敬語・終助詞・総合語用論 ===
    "skm2-p1-form-review-g-q1": ("Instead of easily conforming to others' opinions, one ought to act in accordance with one's own conscience.",
     "Ethical integrity: one ought to act aligned with conscience rather than conformity.",
     {"たがる": "第三者の願望を表すため、人間としての普遍的な道徳的義務の言明に合いません。", "まい": "否定の意志を表すため、良心に従うべきという肯定の規範に矛盾します。", "っこない": "能力の絶対否定になり、良心に従った行動の義務に不適切です。"}),
    "skm2-p1-form-review-g-q2": ("My younger sister is very timid by nature, and when night falls, she shows intense reluctance to go to the bathroom alone.",
     "Childhood fear of the dark: younger sister reluctant to visit bathrooms alone at night.",
     {"べき": "義務を表すため、妹の怖がりな性格から生じる行きたがらない心理に合いません。", "まい": "話者の否定意志になり、第三者の妹の行動傾向の客観的描写に不適です。", "っこない": "能力否定になり、妹の心理的躊躇の描写に合いません。"}),
    "skm2-p1-form-review-g-q3": ("To repay the kindness of my mentor who guided me over years, I resolved never to repeat dishonorable blunders like this again.",
     "Repaying mentorship: resolving never to repeat dishonorable blunders.",
     {"べき": "一般的な義務を表しますが、「二度と繰り返すまい」と固く誓う一人称の強い否定意志には「まい」が最適です。", "たがる": "第三者の願望になり、自己の不退転の誓いに合いません。", "っこない": "能力否定になり、恩義に応える道徳的決意に不適です。"}),
    "skm2-p1-form-review-g-q4": ("Confronting this dense 1000-page academic dictionary, there is no chance that an amateur could memorize it completely in a single day.",
     "Memorization impossibility: amateurs cannot possibly memorize a 1000-page lexicon in one day.",
     {"べき": "義務を表すため、1日で暗記することの絶対的不可能性の断定に合いません。", "まい": "話者の否定意志になり、客観的能力の限界の指摘に不適です。", "たがる": "願望の表出になり、暗記できるはずがないという能力否定に合いません。"}),
    "skm2-p1-form-review-g-q5": ("As medical professionals responsible for human lives, physicians ought to perform surgery with absolute focus at all times.",
     "Surgical accountability: surgeons ought to operate with absolute focus.",
     {"まい": "否定意志になり、真剣に執刀すべき当然の義務と真逆になります。", "たがる": "第三者の願望になり、医師の崇高な職責の宣言に合いません。", "っこない": "能力否定になり、集中すべき義務の諭しに不適です。"}),
    "skm2-p1-form-review-g-q6": ("He harbors intense pride in his work, and whenever difficulties arise, he shows stubborn reluctance to ask others for help.",
     "Artisan pride: stubborn reluctance to seek external assistance when challenged.",
     {"べき": "義務を表すため、他人に頼りたがらない本人の頑固なプライドの描写に合いません。", "まい": "一人称の否定意志になり、彼の普段の行動傾向の客観的叙述に不適です。", "っこない": "能力否定になり、助けを求めることを嫌がる心理に合いません。"}),
    "skm2-p1-form-review-g-q7": ("I am resolved never to allow valuable experiences gained through failures to go to waste in my future career.",
     "Career resilience: resolved never to let hard-won lessons from failure go to waste.",
     {"べき": "客観的な助言になり、「無駄にすまい」と心に強く誓う話者自身の強い意志には「まい」が最適です。", "たがる": "第三者の願望になり、自己の固い決意表明に合いません。", "っこない": "能力否定になり、失敗を糧にする前向きな誓約に不適です。"}),
    "skm2-p1-form-review-g-q8": ("Faced with that athletic powerhouse school boasting consecutive national titles, a newly formed weak team stands zero chance of winning.",
     "Sports asymmetry: a newly formed rookie team stands zero chance against champions.",
     {"べき": "義務を表すため、実力差による勝敗の客観的な絶対的不可能性に合いません。", "まい": "否定意志になり、勝ち目がないという客観的判定に不適です。", "たがる": "願望の表出になり、勝てるはずがないという能力否定に合いません。"}),
    "skm2-p1-form-review-g-q9": ("In democratic societies, mass media reporting ought to maintain absolute fairness without yielding to political powers.",
     "Fourth estate duty: democratic journalism ought to preserve fairness independent of power.",
     {"まい": "否定意志になり、公正を守るべきというジャーナリズムの義務と矛盾します。", "たがる": "願望になり、報道機関の社会的公器としての責務宣言に合いません。", "っこない": "能力否定になり、報道の独立性を保つべき義務の要請に不適です。"}),
    "skm2-p1-form-review-g-q10": ("Children always show strong eagerness to try out newly bought toys immediately.",
     "Childhood excitement: showing intense eagerness to play with new toys right away.",
     {"べき": "義務を表すため、新しいおもちゃに目を輝かせて遊びたがる子供の自然な心理に合いません。", "まい": "否定意志になり、子供の無邪気な好奇心と真逆になります。", "っこない": "能力否定になり、遊びたがる子供の行動描写に不適です。"}),
    "skm2-p1-form-review-g-q11": ("Seeing how deeply worried my parents were, I resolved never to cause them pain through irresponsible conduct again.",
     "Filial resolution: resolved never to cause parents worry through reckless conduct.",
     {"べき": "客観的義務になり、「二度と心配をかけるまい」と親の前で誓う痛切な一人称の意志には「まい」が最適です。", "たがる": "第三者の願望になり、自らの反省の誓約に合いません。", "っこない": "能力否定になり、心配をかけないという自省の決意に不適です。"}),
    "skm2-p1-form-review-g-q12": ("Given such heavy snow accumulation that the railway tracks are completely buried, commuter trains stand zero chance of running today.",
     "Railway paralysis: trains stand zero chance of running with tracks buried under snow.",
     {"べき": "義務を表すため、線路が埋まって運行できるはずがないという物理的不可能性に合いません。", "まい": "意志になり、自然災害による運行不能の客観的現実に不適です。", "たがる": "願望になり、電車の運行可能性の完全否定に合いません。"}),
}

print(f"Loaded {len(REPAIRS_FR)} semantic repairs for SKM N2 Part 1 Form Reviews A–G.")

updated = 0
for e in exercises:
    eid = e.get("id")
    if eid in REPAIRS_FR:
        trans, ctx, opt_map = REPAIRS_FR[eid]
        # determine review letter from id
        # id format: skm2-p1-form-review-a-q1
        letter = eid.split("form-review-")[1].split("-q")[0]
        evid = f"Shin Kanzen Master N2 Bunpou, Part 1 Form Review {letter.upper()}, Practice Drills, {FR_PAGES[letter]}"
        
        e["translation"] = trans
        e["context"] = ctx
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = evid
        
        # Repair options
        expl = e.get("explanation", {})
        if isinstance(expl, dict):
            for opt in expl.get("options", []):
                txt = opt.get("text", "")
                if opt.get("isCorrect"):
                    continue
                else:
                    if txt in opt_map:
                        opt["reason"] = f"【不正解】{opt_map[txt]}"
                    else:
                        matched = False
                        for k, v in opt_map.items():
                            if k in txt or txt in k:
                                opt["reason"] = f"【不正解】{v}"
                                matched = True
                                break
                        if not matched:
                            opt["reason"] = f"【不正解】文脈・文法関係（{txt}）において不適切です。"
        updated += 1

print(f"Updated {updated} exercises in SKM N2 Part 1 Form Reviews A–G.")

with open(EXERCISES_PATH, "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved updated chapterExercises.json successfully.")
