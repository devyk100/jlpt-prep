import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {q['id']: q for q in exercises}

# We will define updates for Form Review A, B, C, D, E, F, G
updates = {}

# ==================== Form Review A (12 qs) ====================
updates['skm2-p1-form-review-a-q1'] = {
    'context': 'Formal diplomatic summit convening at prestigious conference venues.',
    'translation': 'This fiscal year International Environmental Summit was held grandly at the Kyoto International Conference Center.',
    'overall': '公式な催事や儀礼が挙行される場所・舞台を示す硬い表現には「〜において」を用います。',
    'options': [
        {'text': 'において', 'isCorrect': True, 'reason': '【正解】名詞「国際会議場」に接続し、公式行事や式典が行われる場所を格調高く表す「〜において」が最適です。', 'trapCategory': ''},
        {'text': 'に先立って', 'isCorrect': False, 'reason': '【不正解】「〜に先立って」は時間の前後関係（〜の前に）を表すため、開催場所を示す名詞「国際会議場」に接続して場所を表すことはできません。', 'trapCategory': 'meaning'},
        {'text': 'につれて', 'isCorrect': False, 'reason': '【不正解】「〜につれて」は一方の変化に伴う他方の変化を表すため、サミットの開催場所を指定する文脈には不適です。', 'trapCategory': 'meaning'},
        {'text': 'に際して', 'isCorrect': False, 'reason': '【不正解】「〜に際して」は特別な機会や行動のタイミング（開始に際して）を表す表現であり、物理的な開催場所を直接提示する用法はありません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-a-q2'] = {
    'context': 'Prerequisite environmental impact survey preceding industrial operations.',
    'translation': 'Prior to the commencement of operations at the new factory, an environmental assessment survey of the surrounding region was conducted meticulously.',
    'overall': '新工場の稼働開始という重大な事業に先立つ準備措置を表す「〜に先立って」を用います。',
    'options': [
        {'text': 'に先立って', 'isCorrect': True, 'reason': '【正解】「稼働開始に先立って（開始する前にあらかじめ）」と、重要行事・事業の開始前に行う前提措置を表す表現です。', 'trapCategory': ''},
        {'text': 'において', 'isCorrect': False, 'reason': '【不正解】「稼働開始において」とすると稼働の時点・場面そのものを表すことになり、開始前に行う「事前調査」の文脈と矛盾します。', 'trapCategory': 'meaning'},
        {'text': 'にこたえて', 'isCorrect': False, 'reason': '【不正解】「〜にこたえて」は要望や期待に応じる表現であり、事業の開始という事態に接続して時期の前提を表すことはできません。', 'trapCategory': 'meaning'},
        {'text': 'に基づいて', 'isCorrect': False, 'reason': '【不正解】「〜に基づいて」は基準や根拠（データに基づいて）を表すため、稼働開始という時間的契機には接続できません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-a-q3'] = {
    'context': 'Technological transformation of industrial structures by AI in contemporary society.',
    'translation': 'The progress of artificial intelligence technology in contemporary society is transforming all industrial structures.',
    'overall': '「現代社会における（進歩）」と、時代や領域における事態の存在を名詞修飾する「〜における」を用います。',
    'options': [
        {'text': 'における', 'isCorrect': True, 'reason': '【正解】時代や領域を表す名詞「現代社会」に接続し、後ろの名詞「進歩」を連体修飾する「〜における」が最適です。', 'trapCategory': ''},
        {'text': 'に先立つ', 'isCorrect': False, 'reason': '【不正解】「〜に先立つ」は時間的前後関係を表す連体形であり、「現代社会に先立つ進歩（現代社会の前の進歩）」では意味が通りません。', 'trapCategory': 'meaning'},
        {'text': 'にわたる', 'isCorrect': False, 'reason': '【不正解】「〜にわたる」は時間や空間全体の広がり（長年にわたる）を表すため、「現代社会」という時代・場の指定には合いません。', 'trapCategory': 'meaning'},
        {'text': 'にこたえる', 'isCorrect': False, 'reason': '【不正解】「〜にこたえる」は期待や要望への呼応を表すため、「現代社会にこたえる進歩」では意味が破綻します。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-a-q4'] = {
    'context': 'Explanatory briefing for trial volunteers held prior to clinical drug trials.',
    'translation': 'Prior to the start of clinical trials for the new drug, a detailed advance briefing was held for clinical trial volunteers.',
    'overall': '臨床試験の開始に先立って行われる事前説明会を表す中立的連用形「〜に先立ち」を用います。',
    'options': [
        {'text': 'に先立ち', 'isCorrect': True, 'reason': '【正解】重要行事の開始前に先行して行う準備行動を中立的に述べる連用形「〜に先立ち（＝に先立って）」が最適です。', 'trapCategory': ''},
        {'text': 'において', 'isCorrect': False, 'reason': '【不正解】「開始において説明会が行われた」とすると開始時点と説明会が同時になり、治験の前に行う「事前説明」という趣旨に反します。', 'trapCategory': 'meaning'},
        {'text': 'に沿って', 'isCorrect': False, 'reason': '【不正解】「〜に沿って」は方針や計画に従うことを表すため、臨床試験の「開始」という時点には適合しません。', 'trapCategory': 'meaning'},
        {'text': 'に即して', 'isCorrect': False, 'reason': '【不正解】「〜に即して」は事実や規範に適合させること（事実に即して）を表すため、時間的な先行関係を示す文脈には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-a-q5'] = {
    'context': 'Literary history: the narrative literature of the Heian period as a remarkable pinnacle.',
    'translation': 'In the history of literature, the narrative literature of the Heian period boasts an exceptionally noteworthy pinnacle.',
    'overall': '文学の歴史という分野・領域における位置付けを表す「〜において」を用います。',
    'options': [
        {'text': 'において', 'isCorrect': True, 'reason': '【正解】学問・歴史の分野や範囲を指定し、「文学の歴史において…特筆すべき精華を誇る」と格調高く位置づける表現です。', 'trapCategory': ''},
        {'text': 'に先立って', 'isCorrect': False, 'reason': '【不正解】「〜に先立って」は事前の準備行動を表すため、歴史的分野の指定には使用できません。', 'trapCategory': 'meaning'},
        {'text': 'をめぐって', 'isCorrect': False, 'reason': '【不正解】「〜をめぐって」は対立や議論の争点（法改正をめぐって）を表すため、歴史的評価を述べる文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'に対して', 'isCorrect': False, 'reason': '【不正解】「〜に対して」は対象への働きかけや対比を表すため、「文学の歴史に対して…精華を誇る」では意味が成立しません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-a-q6'] = {
    'context': 'Special stage greeting by director and cast prior to national film premiere.',
    'translation': 'Prior to the simultaneous nationwide premiere of the movie, a special stage greeting by the director and lead actors was held.',
    'overall': '映画の全国一斉公開という本番に先立って行われた特別イベントを表す「〜に先立って」を用います。',
    'options': [
        {'text': 'に先立って', 'isCorrect': True, 'reason': '【正解】映画公開という公式行事の前に先行して実施された舞台挨拶を表す時間的先行表現「〜に先立って」が最適です。', 'trapCategory': ''},
        {'text': 'において', 'isCorrect': False, 'reason': '【不正解】「全国公開において」とすると公開期間中の出来事になり、公開前に行われる事前イベントの文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'にわたって', 'isCorrect': False, 'reason': '【不正解】「〜にわたって」は空間や時間の全体的継続（3日間にわたって）を表すため、特定行事の先行関係には使えません。', 'trapCategory': 'meaning'},
        {'text': 'に際して', 'isCorrect': False, 'reason': '【不正解】「〜に際して」は機会の直前直後の関連事項を表しますが、公開前に独立したイベントとして先行開催した事実には「に先立って」が最も明確です。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-a-q7'] = {
    'context': 'Educational technology: tablet adoption in classrooms aiding individualized learning.',
    'translation': 'The introduction of tablet terminals in educational settings is contributing to the realization of individualized, optimized learning.',
    'overall': '「教育の現場における（導入）」と、活動の舞台・領域における事象を名詞修飾する「〜における」を用います。',
    'options': [
        {'text': 'における', 'isCorrect': True, 'reason': '【正解】場所・領域「教育の現場」に接続し、後ろの名詞「導入」を修飾する連体表現「〜における」が最適です。', 'trapCategory': ''},
        {'text': 'に先立つ', 'isCorrect': False, 'reason': '【不正解】「〜に先立つ」は時間的前後関係を表すため、「教育現場に先立つ導入」では意味が破綻します。', 'trapCategory': 'meaning'},
        {'text': 'にこたえる', 'isCorrect': False, 'reason': '【不正解】「〜にこたえる」は要望への対応を表す動詞連体形であり、「教育の現場にこたえる導入」では意味が通りません。', 'trapCategory': 'meaning'},
        {'text': 'にわたる', 'isCorrect': False, 'reason': '【不正解】「〜にわたる」は規模や期間の広がりを表すため、教育の現場という場の指定には不適合です。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-a-q8'] = {
    'context': 'Thorough situational analysis by department leaders preceding business plan formulation.',
    'translation': 'Prior to formulating the business plan for the new fiscal year, a thorough situational analysis was conducted by leaders of each department.',
    'overall': '事業計画の策定という重大な作業の前提として先行して行われた分析を表す「〜に先立ち」を用います。',
    'options': [
        {'text': 'に先立ち', 'isCorrect': True, 'reason': '【正解】事業計画策定という主要タスクに先立って行われた現状分析を格調高く述べる「〜に先立ち」が最適です。', 'trapCategory': ''},
        {'text': 'において', 'isCorrect': False, 'reason': '【不正解】「策定において」とすると策定の最中の出来事になり、策定の前に行う「事前分析」の文脈とずれます。', 'trapCategory': 'meaning'},
        {'text': 'をめぐり', 'isCorrect': False, 'reason': '【不正解】「〜をめぐり」は議論や対立の争点を表すため、先行する分析ステップを述べる文意になりません。', 'trapCategory': 'meaning'},
        {'text': 'にわたり', 'isCorrect': False, 'reason': '【不正解】「〜にわたり」は範囲や期間全体の広がりを表すため、時間的先行関係の提示には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-a-q9'] = {
    'context': 'Historical analysis: modern state-building in the Meiji period accepting Western systems.',
    'translation': 'The process of modern state-building in the Meiji era was the rapid adoption of various Western systems.',
    'overall': '明治時代という歴史的時代区分における事象を名詞修飾する「〜における」を用います。',
    'options': [
        {'text': 'における', 'isCorrect': True, 'reason': '【正解】時代を表す名詞「明治時代」に接続し、後ろの名詞「プロセス」を連体修飾する「〜における」が最も適切です。', 'trapCategory': ''},
        {'text': 'に先立つ', 'isCorrect': False, 'reason': '【不正解】「明治時代に先立つプロセス（明治時代より前のプロセス）」となってしまい、明治時代そのものの近代化を述べる歴史的文脈に反します。', 'trapCategory': 'meaning'},
        {'text': 'にわたる', 'isCorrect': False, 'reason': '【不正解】「〜にわたる」は時間の長さ（10年間にわたる）を表すため、時代名「明治時代」の連体修飾には「における」を用います。', 'trapCategory': 'formation'},
        {'text': 'にこたえる', 'isCorrect': False, 'reason': '【不正解】期待に応じる動詞連体形であり、時代の歴史的事態を修飾する用法はありません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-a-q10'] = {
    'context': 'Final safety verification completed prior to launching the large space telescope.',
    'translation': 'Prior to the launch of the large space telescope, the final safety verification was completed at the ground control center.',
    'overall': '大型望遠鏡の打ち上げという重大イベントに先立って行われた最終安全確認を表す「〜に先立って」を用います。',
    'options': [
        {'text': 'に先立って', 'isCorrect': True, 'reason': '【正解】宇宙望遠鏡の打ち上げという重要行事の前に完了させる前提行動を表す「〜に先立って」が最適です。', 'trapCategory': ''},
        {'text': 'において', 'isCorrect': False, 'reason': '【不正解】「打ち上げにおいて安全確認が完了した」とすると打ち上げの最中に完了したことになり、発射前の確認という趣旨に反します。', 'trapCategory': 'meaning'},
        {'text': 'にこたえて', 'isCorrect': False, 'reason': '【不正解】要望に応じる表現であり、発射手順の安全確認文脈には使えません。', 'trapCategory': 'meaning'},
        {'text': 'に基づいて', 'isCorrect': False, 'reason': '【不正解】基準やデータに基づく表現であり、時間的先行関係を表すことはできません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-a-q11'] = {
    'context': 'Role of dialogue and mutual understanding in the peaceful resolution of international conflicts.',
    'translation': 'In the peaceful resolution of international conflicts, the role played by dialogue and mutual understanding is extremely significant.',
    'overall': '国際紛争の平和的解決という目標・課題領域における役割を指摘する「〜において」を用います。',
    'options': [
        {'text': 'において', 'isCorrect': True, 'reason': '【正解】事態や課題の領域「平和的解決」に接続し、その場面・局面における重要性を論じる格調高い「〜において」が最適です。', 'trapCategory': ''},
        {'text': 'に先立って', 'isCorrect': False, 'reason': '【不正解】「〜に先立って」は事前行動を表すため、「平和的解決に先立って役割が大きい」では論理が破綻します。', 'trapCategory': 'syntax'},
        {'text': 'にわたって', 'isCorrect': False, 'reason': '【不正解】「〜にわたって」は範囲全体の広がりを表すため、課題領域の指定には合いません。', 'trapCategory': 'meaning'},
        {'text': 'に即して', 'isCorrect': False, 'reason': '【不正解】「〜に即して」は実態や規則に沿うことを表すため、「平和的解決に即して役割が大きい」では日本語として不成立です。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-a-q12'] = {
    'context': 'Late-night preparatory negotiations held between foreign ministers prior to official summit agenda.',
    'translation': 'Prior to the official agenda of the summit meeting, advance working-level discussions between the foreign ministers of both countries took place late into the night.',
    'overall': '首脳会談の公式日程に先立って行われた外相間の事前協議を表す「〜に先立ち」を用います。',
    'options': [
        {'text': 'に先立ち', 'isCorrect': True, 'reason': '【正解】公式首脳会談という重大イベントの開始前に先行して行われた事前事務レベル協議を表す「〜に先立ち」が最適です。', 'trapCategory': ''},
        {'text': 'において', 'isCorrect': False, 'reason': '【不正解】「公式日程において協議が行われた」とすると公式会談の中で事前協議を行ったことになり、事前折衝という文脈と矛盾します。', 'trapCategory': 'meaning'},
        {'text': 'をめぐり', 'isCorrect': False, 'reason': '【不正解】「〜をめぐり」は対立する争点を表すため、公式日程を争って協議したという意味になってしまいます。', 'trapCategory': 'meaning'},
        {'text': 'にわたり', 'isCorrect': False, 'reason': '【不正解】「〜にわたり」は期間や範囲全体の広がりを表すため、先行関係の提示には使えません。', 'trapCategory': 'meaning'}
    ]
}

print("Form Review A defined.")

# ==================== Form Review B (12 qs) ====================
updates['skm2-p1-form-review-b-q1'] = {
    'context': 'Concession of calendar spring while severe freezing winter cold persists in northern mountains.',
    'translation': 'Although it is said that the first day of spring has passed on the calendar, severe midwinter cold below freezing still continues in the mountains of the northern country.',
    'overall': '暦の上では春という事実を認めつつも、厳しい寒さが続いている逆接・譲歩には「〜とはいいながら」を用います。',
    'options': [
        {'text': 'とはいいながら', 'isCorrect': True, 'reason': '【正解】「立春を過ぎたとはいいながら（事実として認めつつも）」と、前節の事実と相反する厳しい寒さが続く逆接・譲歩を表す表現です。', 'trapCategory': ''},
        {'text': 'からすると', 'isCorrect': False, 'reason': '【不正解】「〜からすると」は判断の根拠（様子からすると）を表すため、「立春を過ぎたからすると、寒さが続いている」では因果関係が成り立ちません。', 'trapCategory': 'syntax'},
        {'text': 'から見ると', 'isCorrect': False, 'reason': '【不正解】「〜から見ると」は立場や視点（専門家から見ると）を表すため、事実に対する逆接の譲歩文脈には使えません。', 'trapCategory': 'meaning'},
        {'text': 'からいえば', 'isCorrect': False, 'reason': '【不正解】「〜から言えば」は判断基準や着眼点（安全性から言えば）を表すため、事実と食い違う逆接関係には接続できません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-b-q2'] = {
    'context': 'Concluding high drug efficacy and safety based on experimental and observational data.',
    'translation': 'Judging from the experimental data and observation results up to now, it can be concluded that the new drug efficacy and safety are extremely high.',
    'overall': '実験データと観測結果という客観的な根拠に基づいて結論を導く「〜からすると」を用います。',
    'options': [
        {'text': 'からすると', 'isCorrect': True, 'reason': '【正解】「実験データと観測結果からすると（それらを客観的根拠として判断すると）」と結論を導く表現です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】「〜とはいいながら」は逆接・譲歩を表すため、データから素直に高評価を結論づける順接の論理に合いません。', 'trapCategory': 'meaning'},
        {'text': 'とはいえ', 'isCorrect': False, 'reason': '【不正解】「〜とはいえ」は「確かに〜であるが」という逆接を表すため、データに基づく客観的結論の文脈と矛盾します。', 'trapCategory': 'meaning'},
        {'text': 'というより', 'isCorrect': False, 'reason': '【不正解】「〜というより」は言い換えや修正を表すため、判断の根拠を示す文脈には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-b-q3'] = {
    'context': 'High expert appraisal of an ancient ruin excavation as the discovery of the century.',
    'translation': 'Viewed from the perspective of specialists, this excavation of ancient ruins is highly evaluated as the great discovery of the century.',
    'overall': '専門家の見地という特定の立場・視覚から下された高い評価を述べる「〜から見ると」を用います。',
    'options': [
        {'text': 'から見ると', 'isCorrect': True, 'reason': '【正解】「専門家の見地から見ると（その視点・専門的立場に立って評価すれば）」と評価主体・視座を提示する表現です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】譲歩の逆接表現であり、専門家の視点から下された評価を述べる文脈に適合しません。', 'trapCategory': 'meaning'},
        {'text': 'とはいっても', 'isCorrect': False, 'reason': '【不正解】「〜とはいっても」は「〜であるとしても実際は…」という制限・逆接を表すため、肯定的な評価の理由づけに合いません。', 'trapCategory': 'meaning'},
        {'text': 'といえば', 'isCorrect': False, 'reason': '【不正解】「〜といえば」は連想や話題の取り上げ（日本の花といえば桜だ）を表すため、視座からの評価には「から見ると」を用います。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-b-q4'] = {
    'context': 'Reproach that lacking fundamental business etiquette is problematic, even acknowledging one is a trainee.',
    'translation': 'Even though acknowledging that one is a new hire still in training, having acquired no basic business manners whatsoever is a serious problem.',
    'overall': '研修中の新人であることを認めつつも、マナーが全くないことを厳しく非難する「〜とはいいながら」を用います。',
    'options': [
        {'text': 'とはいいながら', 'isCorrect': True, 'reason': '【正解】「研修中の新人であることは認めるが、それにしても…」と事情を認めつつ強い非難・苦言を呈する「〜とはいいながら」が最適です。', 'trapCategory': ''},
        {'text': 'からすると', 'isCorrect': False, 'reason': '【不正解】「新人からすると（新人の立場からすれば）」とすると、マナーがないことを新人の立場から弁護するような不自然な文になります。', 'trapCategory': 'meaning'},
        {'text': 'から見れば', 'isCorrect': False, 'reason': '【不正解】「新人から見れば」は新人の視点を表すため、指導側が新人のマナー不足を批判・問題視する文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'からいって', 'isCorrect': False, 'reason': '【不正解】「新人からいって」は日本語として不自然であり、事情を認めつつ非難する逆接構文には「とはいいながら」を用います。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-b-q5'] = {
    'context': 'Receiving an impression of a sincere young man judging from outward appearance and attire.',
    'translation': 'Judging from his outward appearance and the atmosphere of his attire, one receives the impression of an earnest and sincere young man.',
    'overall': '外見や服装という観察可能な手がかり・根拠に基づいて人物像を推し量る「〜からすると」を用います。',
    'options': [
        {'text': 'からすると', 'isCorrect': True, 'reason': '【正解】外見や服装という目撃可能な手がかり・根拠に基づいて印象を判断する「〜からすると」が最も適切です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】譲歩の逆接表現であり、外見から素直に印象を抱く文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'とはいえ', 'isCorrect': False, 'reason': '【不正解】逆接の接続表現であり、判断の根拠を示す文脈には使えません。', 'trapCategory': 'meaning'},
        {'text': 'というより', 'isCorrect': False, 'reason': '【不正解】訂正・言い換えを表す表現であり、印象判断の根拠提示には不適です。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-b-q6'] = {
    'context': 'Educational perspective: thrusting young children into extreme exam competition inflicts undue stress.',
    'translation': 'Speaking from an educational perspective, entangling young children in excessive entrance exam competition inflicts undue stress on their minds.',
    'overall': '教育的見地という着眼点・評価基準を提示して警鐘を鳴らす「〜から言えば」を用います。',
    'options': [
        {'text': 'から言えば', 'isCorrect': True, 'reason': '【正解】「教育的見地から言えば（教育という専門的判断基準に基づいて論じるならば）」と着眼点・評価基準を提示する表現です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】逆接の譲歩表現であり、教育的観点から意見を述べる文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'とはいえ', 'isCorrect': False, 'reason': '【不正解】「〜とはいえ」は逆接の接続表現であり、見地を提示する表現になりません。', 'trapCategory': 'meaning'},
        {'text': 'というより', 'isCorrect': False, 'reason': '【不正解】言い換えを表す表現であり、判断基準の提示には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-b-q7'] = {
    'context': 'Concession of recession while pointing out some IT companies continue expanding profits.',
    'translation': 'While acknowledging that it is a recession, not all companies are struggling with deficits, and some IT enterprises are actually expanding earnings.',
    'overall': '不況という一般的な通念を認めつつ、業績を伸ばす企業もあるという例外的事実を述べる「〜とはいいながら」を用います。',
    'options': [
        {'text': 'とはいいながら', 'isCorrect': True, 'reason': '【正解】「不況であることは事実だが、そうとはいっても全てが…ではない」と、一般通念を認めつつ例外的事実を述べる「〜とはいいながら」が最適です。', 'trapCategory': ''},
        {'text': 'からすると', 'isCorrect': False, 'reason': '【不正解】「不況からすると」は根拠を表すため、「赤字ではない企業もある」という逆接の事実と論理が矛盾します。', 'trapCategory': 'syntax'},
        {'text': 'から見ると', 'isCorrect': False, 'reason': '【不正解】「不況から見ると」という視点表現は不自然であり、譲歩逆接の文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'からいえば', 'isCorrect': False, 'reason': '【不正解】基準の提示表現であり、不況という状況に対する逆接の例外提示には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-b-q8'] = {
    'context': 'Accident reconstruction: tire tracks indicate the vehicle entered the curve at ferocious speed.',
    'translation': 'Judging from the trajectory of tire skid marks left at the accident scene, it is considered that the vehicle entered the curve at fierce speed.',
    'overall': '現場のタイヤ痕という物的根拠を手がかりとして事故状況を推論する「〜からすると」を用います。',
    'options': [
        {'text': 'からすると', 'isCorrect': True, 'reason': '【正解】現場の物証（タイヤ痕）を手がかりとして事故原因・状況を論理的に推論する「〜からすると」が最適です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】逆接の譲歩表現であり、物証から素直に速度超過を推論する事故分析文脈に反します。', 'trapCategory': 'meaning'},
        {'text': 'とはいえ', 'isCorrect': False, 'reason': '【不正解】逆接表現であり、推論の根拠を示す表現には使えません。', 'trapCategory': 'meaning'},
        {'text': 'というより', 'isCorrect': False, 'reason': '【不正解】言い換え表現であり、科学的痕跡に基づく推論の提示には不適です。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-b-q9'] = {
    'context': 'Consumer standpoint: successive food price hikes deal a severe blow to household finances.',
    'translation': 'Looked at from the standpoint of consumers, successive food price hikes deal a severe blow to household budgets.',
    'overall': '消費者という当事者の視座・立場に立って値上げの影響を論じる「〜から見ると」を用います。',
    'options': [
        {'text': 'から見ると', 'isCorrect': True, 'reason': '【正解】「消費者の立場から見ると（その立場に身を置いて判断すれば）」と、特定の関係者の視座からの見解を述べる表現です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】逆接の譲歩表現であり、消費者の立場からの切実な被害実態を述べる文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'とはいっても', 'isCorrect': False, 'reason': '【不正解】逆接・制限表現であり、評価主体の視座を示す表現になりません。', 'trapCategory': 'meaning'},
        {'text': 'といえば', 'isCorrect': False, 'reason': '【不正解】話題の連想提示であり、立場からの評価を述べる構文には「から見ると」を用います。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-b-q10'] = {
    'context': 'Moral reproof: insulting appearances is inexcusable even claiming it was just a joke.',
    'translation': 'No matter how much it may be said to be a joke, remarks insulting another person appearance or background are absolutely inexcusable.',
    'overall': 'いくら冗談だと言い訳しても絶対に許されないという強い非難を表す「いくら〜とはいいながら」を用います。',
    'options': [
        {'text': 'とはいいながら', 'isCorrect': True, 'reason': '【正解】「いくら冗談とはいいながら（冗談だと言い訳するにしても）」と、弁明を一旦認めつつも絶対に許容できない一線を越えた言動を強く非難する表現です。', 'trapCategory': ''},
        {'text': 'からすると', 'isCorrect': False, 'reason': '【不正解】「冗談からすると」は根拠を表すため、「断じて許されない」という倫理的非難文脈と呼応しません。', 'trapCategory': 'syntax'},
        {'text': 'から見ると', 'isCorrect': False, 'reason': '【不正解】立場・視座を表すため、「いくら冗談…」という副詞「いくら」との呼応構文になりません。', 'trapCategory': 'syntax'},
        {'text': 'からいえば', 'isCorrect': False, 'reason': '【不正解】基準を表す表現であり、「いくら〜とはいいながら」という極端な譲歩の呼応表現には使えません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-b-q11'] = {
    'context': 'Sociolinguistic observation: youth language shows a tendency to prioritize communication efficiency.',
    'translation': 'Judging from recent youth language usage, a tendency to prioritize communication efficiency to an extreme degree can be observed.',
    'overall': '若者の言葉遣いという観察事実を手がかりとして社会的傾向を指摘する「〜からすると」を用います。',
    'options': [
        {'text': 'からすると', 'isCorrect': True, 'reason': '【正解】「若者の言葉遣いからすると（それを言語的データ・根拠として分析すると）」と社会言語学的な傾向を指摘する表現です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】逆接の譲歩表現であり、言語実態から客観的傾向を分析・指摘する文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'とはいえ', 'isCorrect': False, 'reason': '【不正解】逆接の接続詞的表現であり、判断の根拠となる名詞句に接続できません。', 'trapCategory': 'meaning'},
        {'text': 'というより', 'isCorrect': False, 'reason': '【不正解】訂正・言い換え表現であり、分析のデータ根拠を示す表現には不適です。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-b-q12'] = {
    'context': 'Infrastructure safety priority: replacing aging bridges allows not a moment of delay.',
    'translation': 'Speaking from the standpoint of ensuring safety, the early replacement construction of the aging bridge does not permit a single moment of delay.',
    'overall': '安全性の確保という最優先の判断基準に照らし、工事の緊急性を訴える「〜から言えば」を用います。',
    'options': [
        {'text': 'から言えば', 'isCorrect': True, 'reason': '【正解】「安全性の確保から言えば（安全という最重要の判断基準に照らして論じるならば）」と判断基準を前面に掲げて急務を訴える表現です。', 'trapCategory': ''},
        {'text': 'とはいいながら', 'isCorrect': False, 'reason': '【不正解】逆接の譲歩表現であり、安全確保の基準から工事の緊急性を説く文脈に反します。', 'trapCategory': 'meaning'},
        {'text': 'とはいえ', 'isCorrect': False, 'reason': '【不正解】逆接表現であり、基準・観点を提示する表現には使えません。', 'trapCategory': 'meaning'},
        {'text': 'というより', 'isCorrect': False, 'reason': '【不正解】言い換え表現であり、判断基準の提示には不適です。', 'trapCategory': 'meaning'}
    ]
}

print("Form Review B defined.")

# ==================== Form Review C (12 qs) ====================
updates['skm2-p1-form-review-c-q1'] = {
    'context': 'Moral condemnation: insulting an innocent citizen publicly is an unforgivable grave offense in a law-governed nation.',
    'translation': 'The act of insulting an innocent citizen in front of the public is a grave offense that can never be forgiven in a state governed by law.',
    'overall': '古文否定連体形「許されざる（決して許すことができない）」として名詞「重大な過失」を修飾します。',
    'options': [
        {'text': 'ざる', 'isCorrect': True, 'reason': '【正解】動詞未然形「許され」に接続し、「許されざる重大な過失（絶対に許すことができない過失）」と名詞を格調高く修飾する古典文法由来の否定表現です。', 'trapCategory': ''},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「許されるべし」は「当然許されるべきだ」という肯定の義務を表すため、侮辱行為を断罪する文脈と正反対になります。', 'trapCategory': 'meaning'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「〜まい」は否定の意志・推量（終止形）であり、名詞「重大な過失」を連体修飾することはできません。', 'trapCategory': 'formation'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】「せよ」は命令形であり、名詞を修飾する連体用法としては成立しません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-c-q2'] = {
    'context': 'Civic responsibility: as a mature citizen, one ought to take responsibility for one words and actions.',
    'translation': 'As a mature citizen constituting society, one ought to always bear responsibility for one own speech and conduct.',
    'overall': '成熟した市民としての当然の道義的義務を命じる格調高い「〜べし」を用います。',
    'options': [
        {'text': 'べし', 'isCorrect': True, 'reason': '【正解】動詞終止形「持つ」に接続し、「責任を持つべし（持つべきだ）」と市民としての当然の義務・規範を格調高く力強く表す表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「ざる」は否定連体形であり、「持つざる」という接続は文法的に不成立です。', 'trapCategory': 'formation'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「持つまい」とすると「責任を持つつもりはない」という否定意志になり、市民の責任を説く文脈に反します。', 'trapCategory': 'meaning'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】「せよ」は「する」の命令形であり、動詞辞書形「持つ」の後ろには接続できません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-c-q3'] = {
    'context': 'Unyielding resolution: no matter what criticism one faces, I will never abandon speaking the truth.',
    'translation': 'No matter how severe the criticism and slander I may be exposed to, I will never abandon speaking the truth.',
    'overall': 'どんな批判にも屈せず真実を語ることを絶対に諦めないという固い否定意志「〜まい」を用います。',
    'options': [
        {'text': 'まい', 'isCorrect': True, 'reason': '【正解】動詞一段「諦める」の未然・辞書形に接続し、「決して諦めまい（絶対に諦めないぞ）」と話者の不退転の強い否定意志を表す表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「ざる」は連体形であり、文末で話者の決意を述べる終止用法としては使えません。', 'trapCategory': 'formation'},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「諦めるべし」は「諦めるべきだ」という義務になり、「真実を語ることを諦めるべきだ」となって文意が破綻します。', 'trapCategory': 'meaning'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】命令形であり、自分自身の強い決意表明には使えません。', 'trapCategory': 'modality'}
    ]
}

updates['skm2-p1-form-review-c-q4'] = {
    'context': 'Reflecting deeply on past mistakes while taking a step forward into a new future.',
    'translation': 'While carving past errors deeply into one heart and reflecting upon them, one takes a step forward toward a new future.',
    'overall': '過去の反省と未来への前進という二つの動作が並行する文語的表現「〜つつ」を用います。',
    'options': [
        {'text': 'つつ', 'isCorrect': True, 'reason': '【正解】動詞ます形「反省し」に接続し、「反省しつつ（反省しながら同時に）」と二つの行動を並行して行う古風で格調高い同時進行表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「ざる」は未然形接続の否定であり、「反省せざる」の形でなければ文法的に成立せず、また反省しないという意味になってしまいます。', 'trapCategory': 'formation'},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「べし」は終止形・命令であり、前文をつなぐ連用接続としては使えません。', 'trapCategory': 'syntax'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】否定意志・否定推量の終止形であり、後文「一歩を踏み出す」へ接続することはできません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-c-q5'] = {
    'context': 'Examination room instruction: examinees must strictly follow proctor instructions and refrain from whispering.',
    'translation': 'Examinees entering the examination hall, strictly follow the proctors instructions and please refrain from chatting.',
    'overall': '公式な試験規定として受験生に私語の厳禁を促す格式ある命令・指示表現「〜たまえ」を用います。',
    'options': [
        {'text': 'たまえ', 'isCorrect': True, 'reason': '【正解】動詞ます形「慎み」に接続し、「慎みたまえ（慎みなさい）」と公的・公式な規則として指示・命令する格式ある表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「ざる」は否定連体形であり、命令文の文末述語にはなれません。', 'trapCategory': 'formation'},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「べし」は動詞終止形に接続するため（慎むべし）、ます形語幹「慎み」には直接接続できません。', 'trapCategory': 'formation'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】否定推量・否定意志であり、受験生に対する行動の指示命令にはなりません。', 'trapCategory': 'modality'}
    ]
}

updates['skm2-p1-form-review-c-q6'] = {
    'context': 'Forced confession: confronted with airtight evidence, one cannot help but admit one guilt.',
    'translation': 'Having been confronted with such flawless material evidence, one cannot help but admit one own guilt.',
    'overall': '「自らの容疑を認めざるを得ない（認めないわけにはいかない）」という慣用句「〜ざるを得ない」を用います。',
    'options': [
        {'text': 'ざる', 'isCorrect': True, 'reason': '【正解】動詞未然形「認め」に接続し、「〜ざるを得ない（やむを得ず〜しなければならない）」を構成する古典否定連体形です。', 'trapCategory': ''},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「認めるべしを得ない」という日本語表現は文法的に存在しません。', 'trapCategory': 'formation'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「認めるまいを得ない」という慣用句は存在しません。', 'trapCategory': 'formation'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】命令形であり、「〜を得ない」という構文を形成できません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-c-q7'] = {
    'context': 'Uncontrollable hazards spawned alongside great technological advances.',
    'translation': 'While the progress of science and technology brought immense blessings to humankind, it simultaneously created dangers that are difficult to control.',
    'overall': '制御することが極めて困難である性質を格調高く名詞修飾する「〜がたき」を用います。',
    'options': [
        {'text': 'がたき', 'isCorrect': True, 'reason': '【正解】動詞ます形「制御し」に接続し、「制御しがたき（制御するのが極めて困難な）」と名詞「危険性」を格調高く連体修飾する古典文法由来の表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「制御せざる危険性」は「制御しない危険性」になり、制御が心理的・客観的に極めて困難であるというニュアンスになりません。', 'trapCategory': 'nuance'},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「制御すべし危険性」は「制御すべき危険性」であり、すでに生み出された危険そのものの厄介な性質を表す形容修飾に合いません。', 'trapCategory': 'meaning'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】否定推量形式であり、名詞を直接連体修飾することはできません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-c-q8'] = {
    'context': 'High-certainty deduction: that honest man could not possibly commit treacherous deceit against comrades.',
    'translation': 'There is no way that that honest and straightforward man could ever commit the betrayal of deliberately deceiving innocent comrades.',
    'overall': '「〜はずはあるまい（絶対に〜であるはずがない）」と、強い確信をもって事態の可能性を否定する「あるまい」を用います。',
    'options': [
        {'text': 'あるまい', 'isCorrect': True, 'reason': '【正解】「〜はずはあるまい（絶対に〜なはずがない）」と、強い確信をもって事態の可能性を否定する古風な否定推量表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「はずはざる」という日本語は文法的に破綻しています。', 'trapCategory': 'formation'},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「はずはあるべし」は肯定推量になり、「はずがない」という強い否定の確信に反します。', 'trapCategory': 'meaning'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】命令形であり、「はずは…」に続く述語として不成立です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-c-q9'] = {
    'context': 'Moral imperative: national supreme leaders must abandon personal greed and devote themselves to citizen welfare.',
    'translation': 'Those who occupy the position of supreme leader of state affairs must discard private interests and constantly devote themselves to the welfare of the nation and its citizens.',
    'overall': '最高指導者の当然の義務・規範を格調高く命じる「〜べし」を用います。',
    'options': [
        {'text': 'べし', 'isCorrect': True, 'reason': '【正解】動詞終止形「尽くす」に接続し、「尽くすべし（尽くさなければならない）」と最高指導者の当然の義務・規範を格調高く命じる表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「尽くすざる」という接続は文法的に成立しません。', 'trapCategory': 'formation'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「尽くすまい」は「尽くさないつもりだ」という否定意志になり、指導者の義務を説く文脈と正反対になります。', 'trapCategory': 'meaning'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】動詞「尽くす」の辞書形の後ろに重ねて接続することはできません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-c-q10'] = {
    'context': 'Defiant resolve: we will never yield to aggressors threatening sovereign borders by force.',
    'translation': 'Against aggressors who seek to threaten the sovereignty and territorial integrity of our homeland by military force, we will resolutely never submit.',
    'overall': '侵略者に対して断固として屈服しないという強い否定の決意を表す「〜するまい」を用います。',
    'options': [
        {'text': 'するまい', 'isCorrect': True, 'reason': '【正解】サ変動詞「屈する」に接続し、「断固として屈するまい（絶対に屈服しないぞ）」と強い否定の決意を表す表現です。', 'trapCategory': ''},
        {'text': 'すべし', 'isCorrect': False, 'reason': '【不正解】「屈すべし」とすると「屈服するべきだ」となり、侵略者に立ち向かう抗戦の決意と真逆になります。', 'trapCategory': 'meaning'},
        {'text': 'せざる', 'isCorrect': False, 'reason': '【不正解】「屈せざる」は連体形であり、文末の決意表明として終止できません。', 'trapCategory': 'formation'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】「屈せよ（屈服しろ）」という命令になり、自らの不屈の決意を述べる文脈に合いません。', 'trapCategory': 'modality'}
    ]
}

updates['skm2-p1-form-review-c-q11'] = {
    'context': 'Forced vigilance: with variant threats lingering, one has no choice but to keep guards unslackened.',
    'translation': 'As the threat of new mutated strains has not completely vanished, one cannot help but remain compelled to refrain from slackening vigilance.',
    'overall': '変異株の脅威が残る以上、警戒を緩めないわけにはいかないという「〜ざるを得ない」を用います。',
    'options': [
        {'text': 'ざる', 'isCorrect': True, 'reason': '【正解】動詞一段「緩める」の未然形「緩め」に接続し、「緩めざるを得ない（緩めないわけにはいかない）」と社会的強制による警戒継続を表す表現です。', 'trapCategory': ''},
        {'text': 'べし', 'isCorrect': False, 'reason': '【不正解】「緩めるべしを得ない」という表現は文法的に存在しません。', 'trapCategory': 'formation'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】「緩めるまいを得ない」という表現は文法的に存在しません。', 'trapCategory': 'formation'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】命令形であり、「〜を得ない」という構文に組み込めません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-c-q12'] = {
    'context': 'Historical praise: his monumental achievement is a miracle that ought to be passed down through generations.',
    'translation': 'The great feat he achieved is a miracle that ought to be handed down through generations in the history of modern science.',
    'overall': '後世に語り継ぐ価値がある奇跡であることを当然性・評価を込めて修飾する「〜べき」を用います。',
    'options': [
        {'text': 'べき', 'isCorrect': True, 'reason': '【正解】動詞終止形「語り継ぐ」に接続し、「後世に語り継ぐべき奇跡（語り継ぐ価値がある奇跡）」と名詞「奇跡」を連体修飾する当然性・価値評価の表現です。', 'trapCategory': ''},
        {'text': 'ざる', 'isCorrect': False, 'reason': '【不正解】「語り継ぐざる」という接続は成立せず、また否定になってしまいます。', 'trapCategory': 'formation'},
        {'text': 'まい', 'isCorrect': False, 'reason': '【不正解】否定推量形式であり、奇跡を称えて継承を推奨する文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'せよ', 'isCorrect': False, 'reason': '【不正解】命令形であり、名詞「奇跡」を連体修飾することはできません。', 'trapCategory': 'formation'}
    ]
}

print("Form Review C defined.")
