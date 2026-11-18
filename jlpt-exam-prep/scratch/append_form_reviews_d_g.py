import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {q['id']: q for q in exercises}

updates = {}

# ==================== Form Review D (12 qs) ====================
updates['skm2-p1-form-review-d-q1'] = {
    'context': 'Nostalgic yearning: how deeply one yearned for family warmth when falling ill in a foreign land.',
    'translation': 'When falling sick alone in a foreign land unable even to see family faces, how intensely I yearned for the warmth of my hometown!',
    'overall': '「どんなに〜ことか！」と、過去の病床における切実な恋しさを強く詠嘆します。',
    'options': [
        {'text': 'ことか', 'isCorrect': True, 'reason': '【正解】程度副詞「どんなに」と呼応し、「どんなに恋しかったことか！」と心情の強烈さを深く詠嘆する表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「〜ことだ」は助言・忠告を表すため、過去の体験の感慨・詠嘆には使えません。', 'trapCategory': 'meaning'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】「〜ことに」は文頭で話者の感情を添える副詞的用法（嬉しいことに）であり、文末の詠嘆述語にはなれません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】「〜ことなく」は「〜しないで」という付帯状況を表すため、文末の述語として成立しません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-d-q2'] = {
    'context': 'Language learning advice: if you truly want to improve conversational fluency, you should speak proactively with native speakers.',
    'translation': 'If you truly want to improve your foreign language conversation skills, you should actively speak with native speakers without being shy.',
    'overall': '会話力向上のための確実な助言として「〜ことだ」を用います。',
    'options': [
        {'text': 'ことだ', 'isCorrect': True, 'reason': '【正解】「会話力を上達させたいなら…話すことだ」と、望ましい行動を助言・忠告する表現「〜ことだ」が最適です。', 'trapCategory': ''},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】「〜ことか」は詠嘆を表すため、条件「〜なら」に対する助言には合いません。', 'trapCategory': 'modality'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】感情強調の副詞的接続であり、文末で助言を述べる述語になりません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】否定の連用修飾表現であり、行動を促す文末述語になりません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-d-q3'] = {
    'context': 'Great relief: fortunately, all hikers who lost their way were discovered safely by the rescue party.',
    'translation': 'Fortunately, all the hikers who lost their way in the mountain and almost met with disaster were safely discovered by the rescue team.',
    'overall': '文頭で「幸運なことに（幸いにも）」と話者の感情的評価を述べる表現を用います。',
    'options': [
        {'text': 'ことに', 'isCorrect': True, 'reason': '【正解】形容詞語幹「幸運な」に接続し、「幸運なことに（幸いなことに）」と後続の文全体に感情的評価を添える副詞的表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「幸運なことだ」は文末の断定述語であり、文頭で後続節を修飾する連用形としては使えません。', 'trapCategory': 'syntax'},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】詠嘆の終止表現であり、文頭の接続句として不成立です。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】動詞未然形に接続して動作の否定を表すため、ナ形容詞「幸運な」には接続できません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-d-q4'] = {
    'context': 'Marathon perseverance: running through the grueling marathon without uttering a single complaint.',
    'translation': 'Without uttering weak complaints even once along the way, he ran through the grueling full marathon giving it his all to the very end.',
    'overall': '「一度も弱音を吐くことなく（弱音を吐かないで）」と動作の不随伴・不実施を表す「〜ことなく」を用います。',
    'options': [
        {'text': 'ことなく', 'isCorrect': True, 'reason': '【正解】動詞辞書形「吐く」に接続し、「弱音を吐くことなく（一度も弱音を吐かないで）」と付帯状況を表す表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】助言を表す終止述語であり、後文の動詞「走り抜いた」へ接続する連用修飾になりません。', 'trapCategory': 'syntax'},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】文末の詠嘆表現であり、文中の連用節を形成することはできません。', 'trapCategory': 'syntax'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】感情評価の表現であり、「弱音を吐くことに走り抜いた」では日本語として意味が通りません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-d-q5'] = {
    'context': 'Joyful surprise: receiving an unexpected heartfelt letter from an old friend after years of silence.',
    'translation': 'Suddenly receiving a heartfelt letter from an old friend with whom contact had lapsed for years, how intensely delighted I was!',
    'overall': '「どれほど嬉しかったことか！」と、予期せぬ旧友からの便りに対する深い喜びを詠嘆します。',
    'options': [
        {'text': 'ことか', 'isCorrect': True, 'reason': '【正解】程度副詞「どれほど」と呼応し、「どれほど嬉しかったことか！」と心からの喜びの大きさを詠嘆する表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】助言を表す表現であり、過去の自分の感情の詠嘆には使えません。', 'trapCategory': 'meaning'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】文頭の副詞的感情表現であり、文末感嘆文の述語にはなれません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】否定の連用表現であり、文末述語として不適です。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-d-q6'] = {
    'context': 'Wondrous preservation: curiously, letters buried in a time capsule decades ago had not faded at all.',
    'translation': 'Strangely enough, the letters inside the time capsule buried decades ago had not faded in color at all.',
    'overall': '「不思議なことに（奇妙なことに）」と、不可思議な事実に対して感情的評価を添える「〜ことに」を用います。',
    'options': [
        {'text': 'ことに', 'isCorrect': True, 'reason': '【正解】ナ形容詞語幹「不思議な」に接続し、「不思議なことに」と文頭で心情・実感を提示する表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】文末の助言・評価述語であり、文頭の連用修飾句にはなれません。', 'trapCategory': 'syntax'},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】詠嘆の終止表現であり、文頭に置くことはできません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】動詞接続の否定表現であり、ナ形容詞「不思議な」には接続できません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-d-q7'] = {
    'context': 'Information security advice: if you wish to protect vital company secrets, you should never connect to external public networks.',
    'translation': 'If you want to protect crucial confidential company information, you should never connect to external public networks.',
    'overall': '情報セキュリティの忠告として「〜絶対に接続しないことだ」を用います。',
    'options': [
        {'text': 'ことだ', 'isCorrect': True, 'reason': '【正解】動詞否定形「接続しない」に接続し、「絶対に接続しないことだ」と禁止・忠告を述べる表現「〜ないことだ」が最適です。', 'trapCategory': ''},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】詠嘆の表現であり、条件「〜なら」に対する禁止忠告には合いません。', 'trapCategory': 'modality'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】感情強調表現であり、助言の文末述語になりません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】連用修飾表現であり、文末を締めくくる述語にはなれません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-d-q8'] = {
    'context': 'Independent mastery: completely acquiring a complex programming language without borrowing anyone help.',
    'translation': 'Without borrowing anyone help, she completely mastered the difficult programming language all by herself.',
    'overall': '「誰の助けも借りることなく（全く借りないで）」と他者に頼らない自立的達成を表す「〜ことなく」を用います。',
    'options': [
        {'text': 'ことなく', 'isCorrect': True, 'reason': '【正解】動詞辞書形「借りる」に接続し、「助けも借りることなく（全く借りないで自力で）」と付帯状況を表す表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】助言表現であり、過去の自力達成「習得した」を修飾する連用句になりません。', 'trapCategory': 'syntax'},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】詠嘆の終止表現であり、文中の連用修飾節を形成できません。', 'trapCategory': 'syntax'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】感情評価表現であり、「借りることに習得した」では日本語として不成立です。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-d-q9'] = {
    'context': 'Astonishing discovery: to everyone surprise, a famous painting missing for years was found in an attic.',
    'translation': 'To everyone amazement, the famous masterpiece missing for many years was miraculously discovered in the attic of an old folk house.',
    'overall': '「驚いたことに（驚くべきことに）」と、予期せぬ名画の発見に対する驚きを文頭で提示する「〜ことに」を用います。',
    'options': [
        {'text': 'ことに', 'isCorrect': True, 'reason': '【正解】感情動詞タ形「驚いた」に接続し、「驚いたことに」と文頭で話者の心情的評価を提示する表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】「驚いたことだ」は文末の感慨述語であり、文頭で後続節を修飾する連用表現になりません。', 'trapCategory': 'syntax'},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】文末詠嘆表現であり、文頭に置くことはできません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】動作の不実施を表す表現であり、驚きの心情を添える文脈に合いません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-d-q10'] = {
    'context': 'Empathy with war bereaved: how deep the sorrow of those who lost all family members to war.',
    'translation': 'How immeasurable must have been the grief of those who had all their beloved family members torn away by the atrocities of war!',
    'overall': '「いかばかりであったことか！」と、戦争遺族の計り知れない悲痛に対して深く詠嘆します。',
    'options': [
        {'text': 'ことか', 'isCorrect': True, 'reason': '【正解】程度表現「いかばかり」と呼応し、「いかばかりであったことか！」と他者の深い悲しみに寄り添って詠嘆する表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】助言表現であり、過去の悲惨な境遇への詠嘆には使えません。', 'trapCategory': 'meaning'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】文頭の副詞的感情表現であり、文末感嘆文の述語にはなれません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】否定の連用表現であり、文末述語として不適です。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-d-q11'] = {
    'context': 'Health advice: upon receiving re-examination results, one should consult a specialist immediately.',
    'translation': 'If a re-examination verdict was issued in your health checkup, you should immediately receive an examination by a specialist without leaving it unattended.',
    'overall': '健診結果を受けた相手への忠告として「すぐに診察を受けることだ」を用います。',
    'options': [
        {'text': 'ことだ', 'isCorrect': True, 'reason': '【正解】動詞辞書形「受ける」に接続し、「診察を受けることだ（受けるのが最善だ）」と相手に助言する表現です。', 'trapCategory': ''},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】詠嘆表現であり、再検査通知に対する健康指導のアドバイスになりません。', 'trapCategory': 'modality'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】感情強調の副詞的接続であり、助言の述語になりません。', 'trapCategory': 'syntax'},
        {'text': 'ことなく', 'isCorrect': False, 'reason': '【不正解】否定連用修飾であり、文末述語として不成立です。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-d-q12'] = {
    'context': 'Resolute independence: striding forward along one chosen path without being misled by irresponsible criticisms.',
    'translation': 'Without being swayed by irresponsible criticisms from those around him, he strode forward with conviction along the path he believed in.',
    'overall': '「批判に惑わされることなく（全く惑わされないで）」と意志を貫く姿勢を表す「〜ことなく」を用います。',
    'options': [
        {'text': 'ことなく', 'isCorrect': True, 'reason': '【正解】動詞受身形「惑わされる」に接続し、「惑わされることなく（一切惑わされないで）」と不随伴の連用修飾を行う表現です。', 'trapCategory': ''},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】助言表現であり、過去の行動「突き進んだ」を修飾する連用節になりません。', 'trapCategory': 'syntax'},
        {'text': 'ことか', 'isCorrect': False, 'reason': '【不正解】詠嘆の終止表現であり、文中の連用節を形成できません。', 'trapCategory': 'syntax'},
        {'text': 'ことに', 'isCorrect': False, 'reason': '【不正解】感情評価表現であり、「惑わされることに突き進んだ」では日本語として意味が成立しません。', 'trapCategory': 'meaning'}
    ]
}

# ==================== Form Review E (12 qs) ====================
updates['skm2-p1-form-review-e-q1'] = {
    'context': 'Logical natural consequence: having practiced desperately for hours daily, it is completely natural that he won first place.',
    'translation': 'Since he practiced desperately for hours every single day, it is completely natural that he won first prize in the competition.',
    'overall': '必死の練習という明白な原因から導かれる必然的・当然の帰結を表す「〜わけだ」を用います。',
    'options': [
        {'text': 'わけだ', 'isCorrect': True, 'reason': '【正解】「〜のだから…優勝したのは当然のわけだ（当然の成り行きだ・道理だ）」と納得のいく因果的帰結を述べる表現です。', 'trapCategory': ''},
        {'text': 'わけではない', 'isCorrect': False, 'reason': '【不正解】「〜わけではない」は部分否定（優勝したとは限らない）になり、必死の練習を称賛して優勝を当然とする文脈と矛盾します。', 'trapCategory': 'meaning'},
        {'text': 'わけがない', 'isCorrect': False, 'reason': '【不正解】「〜わけがない」は強い否定（優勝するはずがない）になり、優勝の事実に反します。', 'trapCategory': 'meaning'},
        {'text': 'ところだ', 'isCorrect': False, 'reason': '【不正解】「〜ところだ」は直前・進行・直後の時間局面を表すため、「当然の〜」という論理的道理の述語にはなりません。', 'trapCategory': 'syntax'}
    ]
}

updates['skm2-p1-form-review-e-q2'] = {
    'context': 'Partial negation: living in Japan for 10 years does not mean one is knowledgeable about every custom.',
    'translation': 'Just because one has lived in Japan for ten years does not necessarily mean that one is well-versed in all Japanese culture and customs.',
    'overall': '「〜からといって…精通しているわけではない（必ずしもそうとは言えない）」と部分否定する表現を用います。',
    'options': [
        {'text': 'わけではない', 'isCorrect': True, 'reason': '【正解】「〜からといって…わけではない」の呼応構文で、「10年住んでいても全てを知り尽くしているとは限らない」と全面的一致を部分否定する表現です。', 'trapCategory': ''},
        {'text': 'わけだ', 'isCorrect': False, 'reason': '【不正解】「精通しているわけだ」と肯定すると、「10年住んでいるからといって（＝たとえそうであっても）」という逆接の前提と論理が破綻します。', 'trapCategory': 'syntax'},
        {'text': 'わけがない', 'isCorrect': False, 'reason': '【不正解】「精通しているわけがない（精通しているはずがない）」は全面否定になり、10年住んでいる人の知識を不自然に全否定してしまいます。', 'trapCategory': 'nuance'},
        {'text': 'ところだ', 'isCorrect': False, 'reason': '【不正解】時間的局面を表す表現であり、真偽判断の部分否定構文を形成できません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-e-q3'] = {
    'context': 'Strong impossibility negation: that honest man could never commit the crime of embezzling public funds.',
    'translation': 'There is no possibility whatsoever that someone so honest and sincere would commit misconduct such as deliberately embezzling company funds.',
    'overall': '人柄への信頼から「そんな不正を働くわけがない（絶対にあり得ない）」と強く否定します。',
    'options': [
        {'text': 'わけがない', 'isCorrect': True, 'reason': '【正解】「あれほど真面目な彼が…不正を働くわけがない（絶対に働くはずがない）」と、強い確信をもって可能性を全否定する表現です。', 'trapCategory': ''},
        {'text': 'わけだ', 'isCorrect': False, 'reason': '【不正解】「不正を働くわけだ」と肯定すると、真面目な彼が横領を犯すのが当然だということになり、文意が破綻します。', 'trapCategory': 'meaning'},
        {'text': 'わけではない', 'isCorrect': False, 'reason': '【不正解】「〜わけではない」は部分否定（働くとは限らない）であり、「絶対にあり得ない」という話者の強い否定の確信には弱すぎます。', 'trapCategory': 'nuance'},
        {'text': 'ところだ', 'isCorrect': False, 'reason': '【不正解】時間的局面を表す表現であり、可能性の強い否定には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-e-q4'] = {
    'context': 'Discovery upon action: conducting detailed precision examinations revealed an extremely tiny early-stage lesion.',
    'translation': 'Upon carefully conducting the latest precision examination, an extremely tiny lesion in its early stages was discovered.',
    'overall': '検査を行った結果として新しい病変が発見された契機を表す「〜たところ」を用います。',
    'options': [
        {'text': 'ところ', 'isCorrect': True, 'reason': '【正解】動詞タ形「行った」に接続し、「行ったところ（検査してみた結果、…が発見された）」と行為の契機・結果の発見を表す表現です。', 'trapCategory': ''},
        {'text': 'わけ', 'isCorrect': False, 'reason': '【不正解】「行ったわけ、発見された」という接続は日本語として文法的に成立しません。', 'trapCategory': 'syntax'},
        {'text': 'こと', 'isCorrect': False, 'reason': '【不正解】「行ったこと、発見された」では行為の契機・発見を表す接続表現になりません。', 'trapCategory': 'syntax'},
        {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】「行ったもの、発見された」という接続は不成立です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-e-q5'] = {
    'context': 'Deducing the suspect vehicle from the matching footprints and tire tracks at the scene.',
    'translation': 'From the fact that the characteristics of the footprints and tire marks left at the scene matched, the police identified the suspect car.',
    'overall': '物的証拠の特徴が一致したという端緒・根拠から特定に至った経緯を表す「〜ところから」を用います。',
    'options': [
        {'text': 'ところから', 'isCorrect': True, 'reason': '【正解】動詞タ形「一致した」に接続し、「一致したところから（それが直接のきっかけ・根拠となって）」と判断や特定の端緒を表す表現です。', 'trapCategory': ''},
        {'text': 'わけから', 'isCorrect': False, 'reason': '【不正解】「わけから」という日本語表現は文法的に存在しません。', 'trapCategory': 'formation'},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】文末の助言表現であり、原因・端緒を表す接続句になりません。', 'trapCategory': 'syntax'},
        {'text': 'ものから', 'isCorrect': False, 'reason': '【不正解】口語の言い訳表現（〜ものだから）であり、警察の科学捜査の端緒を述べる客観的文体として不適切です。', 'trapCategory': 'register'}
    ]
}

updates['skm2-p1-form-review-e-q6'] = {
    'context': 'Realization of cause: discovering why it was noisy outside—construction had begun next door.',
    'translation': 'I wondered why it was so noisy outside, and it turned out that construction work on a new apartment building had begun in the vacant lot next door.',
    'overall': '外が騒がしかった理由を理解し、「工事が始まったわけだ（だからうるさかったのか）」と納得する「〜わけだ」を用います。',
    'options': [
        {'text': 'わけだ', 'isCorrect': True, 'reason': '【正解】「外が騒がしいと思ったら…工事が始まったわけだ（道理でうるさいはずだ）」と、理由が判明して合点・納得する表現です。', 'trapCategory': ''},
        {'text': 'わけではない', 'isCorrect': False, 'reason': '【不正解】「工事が始まったわけではない」とすると、工事は始まっていないことになり、騒音の理由が説明できません。', 'trapCategory': 'meaning'},
        {'text': 'ところだ', 'isCorrect': False, 'reason': '【不正解】「始まったところだ」は時間的直後を表せますが、「外が騒がしいと思ったら…」という理由判明・納得の呼応には「わけだ」が最適です。', 'trapCategory': 'nuance'},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】助言を表す表現であり、騒音の理由判明の文脈に合いません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-e-q7'] = {
    'context': 'Partial negation: he is normally gentle, but it does not mean he never gets angry at unreasonable insults.',
    'translation': 'While he is normally quiet and gentle, it does not mean that he never gets angry at unreasonable insults.',
    'overall': '普段は温厚でも「全く怒らないわけではない（怒ることもある）」と部分否定する「〜わけではない」を用います。',
    'options': [
        {'text': 'わけではない', 'isCorrect': True, 'reason': '【正解】「全く怒らないわけではない（時には激しく怒ることもある）」と、全否定を和らげて例外の存在を示す部分否定表現です。', 'trapCategory': ''},
        {'text': 'わけだ', 'isCorrect': False, 'reason': '【不正解】「全く怒らないわけだ」とすると、侮辱されても一切怒らないことになり、対比文「普段は温厚だが…」の逆接の文意に反します。', 'trapCategory': 'meaning'},
        {'text': 'わけがない', 'isCorrect': False, 'reason': '【不正解】「全く怒らないわけがない（絶対に怒るに決まっている）」は二重否定による強い肯定断定になり、控えめな人柄描写のトーンとずれます。', 'trapCategory': 'nuance'},
        {'text': 'ところだ', 'isCorrect': False, 'reason': '【不正解】時間的局面を表す表現であり、心情・反応の部分否定には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-e-q8'] = {
    'context': 'Absolute negation of possibility: that genius who aced previous exams could never fail a basic quiz.',
    'translation': 'Knowing that genius who scored perfect marks on the previous exam, there is no way he would fail this basic short quiz.',
    'overall': '満点を取った天才なのだから「不合格になるわけがない（絶対にあり得ない）」と全否定します。',
    'options': [
        {'text': 'わけがない', 'isCorrect': True, 'reason': '【正解】「満点を取った天才的な彼のことだから…不合格になるわけがない（落ちるはずがない）」と可能性を力強く全否定する表現です。', 'trapCategory': ''},
        {'text': 'わけだ', 'isCorrect': False, 'reason': '【不正解】「不合格になるわけだ」とすると落ちることが当然だということになり、満点を取った天才という前提と矛盾します。', 'trapCategory': 'meaning'},
        {'text': 'わけではない', 'isCorrect': False, 'reason': '【不正解】「〜わけではない」は部分否定（落ちるとは限らない）であり、「絶対に落ちない」という確信には弱すぎます。', 'trapCategory': 'nuance'},
        {'text': 'ところだ', 'isCorrect': False, 'reason': '【不正解】時間的局面を表す表現であり、能力・可能性の強い否定には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-e-q9'] = {
    'context': 'Fruitful discovery: upon consulting the teacher for advice, one received a splendid hint solving long troubles.',
    'translation': 'When I consulted my teacher seeking advice, I was able to receive a marvelous hint that resolved my longstanding troubles.',
    'overall': '先生に相談してみた結果として素晴らしいヒントが得られたという「〜たところ」を用います。',
    'options': [
        {'text': 'ところ', 'isCorrect': True, 'reason': '【正解】動詞タ形「相談した」に接続し、「相談したところ（相談してみた結果、…をもらえた）」と行為の結果生じた事態を表す表現です。', 'trapCategory': ''},
        {'text': 'わけ', 'isCorrect': False, 'reason': '【不正解】「相談したわけ、もらえた」という接続は日本語として不成立です。', 'trapCategory': 'syntax'},
        {'text': 'こと', 'isCorrect': False, 'reason': '【不正解】「相談したこと、もらえた」では行為の契機・結果を表す接続表現になりません。', 'trapCategory': 'syntax'},
        {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】名詞「もの」を単独で接続して結果節をつなぐ用法はありません。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-e-q10'] = {
    'context': 'Uncovering ancient trade routes from investigating place-name origins in old literature.',
    'translation': 'From investigating the origins of place names recorded in ancient literature, the reality of ancient trade routes became clear.',
    'overall': '地名の由来を調査したことが直接の手がかり・きっかけとなって交易路が解明された「〜ところから」を用います。',
    'options': [
        {'text': 'ところから', 'isCorrect': True, 'reason': '【正解】動詞タ形「調査した」に接続し、「調査したところから（その調査結果がきっかけとなって）」と学術的発見の端緒・根拠を表す表現です。', 'trapCategory': ''},
        {'text': 'わけから', 'isCorrect': False, 'reason': '【不正解】「わけから」という日本語表現は文法的に存在しません。', 'trapCategory': 'formation'},
        {'text': 'ことだ', 'isCorrect': False, 'reason': '【不正解】助言を表す終止形述語であり、発見の端緒を導く接続句にはなれません。', 'trapCategory': 'syntax'},
        {'text': 'ものから', 'isCorrect': False, 'reason': '【不正解】口語の言い訳形式であり、学術調査の経緯を述べる文体に不適です。', 'trapCategory': 'register'}
    ]
}

updates['skm2-p1-form-review-e-q11'] = {
    'context': 'Partial negation: being on a strict diet does not mean one has come to dislike sweets.',
    'translation': 'Just because I am on a strict dietary restriction does not mean that I have come to dislike sweet desserts.',
    'overall': '食事制限中だからといって「嫌いになったわけではない（甘い物は今でも好きだ）」と部分否定します。',
    'options': [
        {'text': 'わけではない', 'isCorrect': True, 'reason': '【正解】「〜からといって…わけではない」の呼応で、「制限中だが嫌いになったのではない（食べたい気持ちはある）」と理由から導かれる誤解を打ち消す表現です。', 'trapCategory': ''},
        {'text': 'わけだ', 'isCorrect': False, 'reason': '【不正解】「嫌いになったわけだ」とすると本当に嫌いになったことになり、「からといって」という逆接条件節と呼応しません。', 'trapCategory': 'syntax'},
        {'text': 'わけがない', 'isCorrect': False, 'reason': '【不正解】「嫌いになったわけがない」は強い全否定（嫌いになるはずがない）であり、「嫌いになったわけではない」という柔らかい弁明には「わけではない」が自然です。', 'trapCategory': 'nuance'},
        {'text': 'ところだ', 'isCorrect': False, 'reason': '【不正解】時間的局面を表す表現であり、心情の部分否定には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-e-q12'] = {
    'context': 'Social/moral inhibition: with the 5 PM deadline imminent, one cannot afford to postpone submission any further.',
    'translation': 'With the deadline approaching at 5 PM this evening, I cannot possibly postpone the submission any further.',
    'overall': '夕方5時の締め切りを前に「これ以上先延ばしにするわけにはいかない（絶対に提出しなければならない）」と義務を主張します。',
    'options': [
        {'text': 'わけにはいかない', 'isCorrect': True, 'reason': '【正解】動詞辞書形「先延ばしにする」に接続し、「社会的義務・期限の制約からこれ以上の延期は許されない」と行動の制約を述べる表現です。', 'trapCategory': ''},
        {'text': 'わけがない', 'isCorrect': False, 'reason': '【不正解】「先延ばしにするわけがない」は可能性の否定（先延ばしにするはずがない）になり、「締め切りが迫っているから先延ばしできない」という話者の義務意識とずれます。', 'trapCategory': 'nuance'},
        {'text': 'わけではない', 'isCorrect': False, 'reason': '【不正解】「〜わけではない」は部分否定（先延ばしにするとは限らない）であり、期限厳守の切迫した決意には合いません。', 'trapCategory': 'nuance'},
        {'text': 'ところではない', 'isCorrect': False, 'reason': '【不正解】「〜どころではない」は「そんな状況ではない」という余裕の不在を表しますが、社会的義務・制約による禁止には「〜わけにはいかない」が最も正確です。', 'trapCategory': 'nuance'}
    ]
}

# ==================== Form Review F (12 qs) ====================
updates['skm2-p1-form-review-f-q1'] = {
    'context': 'Rebuking endless excuses: stop listing complaints like being busy or tired and finish the job.',
    'translation': 'Without constantly lining up complaints like being busy or being tired, finish the assigned work quickly.',
    'overall': '「忙しいだの疲れただの」と不満や言い訳を批判的・うんざりした態度で並べる「〜だの〜だの」を用います。',
    'options': [
        {'text': 'だの／だの', 'isCorrect': True, 'reason': '【正解】「忙しいだの疲れただの」の形で、不満や言い訳をうんざりした感情を込めて例示・列挙する表現です。', 'trapCategory': ''},
        {'text': 'のみ／のみ', 'isCorrect': False, 'reason': '【不正解】「のみ」は限定（〜だけ）を表すため、「忙しいのみ疲れたのみ」という並立表現は文法的に破綻しています。', 'trapCategory': 'formation'},
        {'text': 'やら／やら', 'isCorrect': False, 'reason': '【不正解】「〜やら〜やら」は雑多な事態が次々に起きて混乱・困惑する様子を表し、本人の言い訳を批判するニュアンス（〜だの）とは異なります。', 'trapCategory': 'nuance'},
        {'text': 'など／など', 'isCorrect': False, 'reason': '【不正解】「忙しいなど疲れたなど」という重ね方は日本語として不自然であり、不満の列挙には「だの／だの」が適切です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-f-q2'] = {
    'context': 'Strict investigatory scope: detailed hearing investigation targeting eyewitnesses only.',
    'translation': 'In order to investigate the truth of the accident, a detailed hearing investigation targeting eyewitnesses only was conducted.',
    'overall': '調査対象を目撃者だけに厳密に限定する硬い表現「〜のみ」を用います。',
    'options': [
        {'text': 'のみ', 'isCorrect': True, 'reason': '【正解】名詞「目撃者」に接続し、「目撃者のみを対象とした（目撃者だけに限定した）」と調査範囲を厳格に限定する硬い表現です。', 'trapCategory': ''},
        {'text': 'だの', 'isCorrect': False, 'reason': '【不正解】不満や言い訳を列挙する表現であり、公的な調査対象の限定には使えません。', 'trapCategory': 'meaning'},
        {'text': 'やら', 'isCorrect': False, 'reason': '【不正解】雑多な例示・困惑を表す表現であり、厳密な対象限定を示すことはできません。', 'trapCategory': 'meaning'},
        {'text': 'ばかり', 'isCorrect': False, 'reason': '【不正解】「目撃者ばかり」とすると「目撃者がたくさんいる」という多量・概括のニュアンスになり、対象を厳格に限定する公式文書の文体として「のみ」が最も適切です。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-f-q3'] = {
    'context': 'Barbecue canceled due to chaotic bad weather: raining, blowing wind, and total mess.',
    'translation': 'What with the rain falling and the wind blowing, the outdoor barbecue we had been looking forward to on the weekend ended up canceled.',
    'overall': '雨が降ったり風が吹いたりと雑多な悪天候に見舞われて収拾がつかない状態を表す「〜やら〜やら」を用います。',
    'options': [
        {'text': 'やら／やら', 'isCorrect': True, 'reason': '【正解】「雨が降るやら風が吹くやら」の形で、予期せぬ悪条件が重なって困惑・混乱している様子を表すのに最適です。', 'trapCategory': ''},
        {'text': 'だの／だの', 'isCorrect': False, 'reason': '【不正解】「〜だの〜だの」は人の身勝手な不満や言い訳を批判的に並べ立てる表現であり、自然の天候被害の描写には使いません。', 'trapCategory': 'nuance'},
        {'text': 'のみ／のみ', 'isCorrect': False, 'reason': '【不正解】限定表現であり、天候の雑多な悪化要因を並べる表現になりません。', 'trapCategory': 'formation'},
        {'text': 'など／など', 'isCorrect': False, 'reason': '【不正解】動詞辞書形に重ねて「降るなど吹くなど」とする並立は不自然であり、「やら／やら」が適切です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-f-q4'] = {
    'context': 'Corporate turnaround strategy: the sole means to overcome crisis is cost reduction and innovation only.',
    'translation': 'The sole means to overcome this unprecedented financial crisis is thorough cost reduction and technological innovation only.',
    'overall': '危機克服の手段を「経費削減と技術革新のみ」と唯一・限定的に提示する「〜のみ」を用います。',
    'options': [
        {'text': 'のみ', 'isCorrect': True, 'reason': '【正解】名詞句「経費削減と技術革新」に接続し、「それだけが唯一の手段である」と格調高く厳格に限定する表現です。', 'trapCategory': ''},
        {'text': 'だの', 'isCorrect': False, 'reason': '【不正解】不満の列挙表現であり、経営再建の唯一の手段を断定する文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'やら', 'isCorrect': False, 'reason': '【不正解】混乱・雑多な例示表現であり、手段の厳密な限定には使えません。', 'trapCategory': 'meaning'},
        {'text': 'ばかり', 'isCorrect': False, 'reason': '【不正解】「技術革新ばかりである」とすると「技術革新でいっぱいだ」という偏りの意味になり、「それだけが唯一の手段だ」という厳格な限定には「のみ」が最適です。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-f-q5'] = {
    'context': 'Dodging duties with trivial excuses: claiming headaches and feverishness to push tasks onto others.',
    'translation': 'Making up excuses like having a headache or feeling feverish, he always pushes troublesome duty tasks onto others.',
    'overall': '頭が痛いだの熱っぽいだのと、身勝手な言い訳を並べ立てるのを批判する「〜だの〜だの」を用います。',
    'options': [
        {'text': 'だの／だの', 'isCorrect': True, 'reason': '【正解】「頭が痛いだの熱っぽいだの」と、仕事をサボるための都合の良い言い訳を批判的に並べ立てる表現です。', 'trapCategory': ''},
        {'text': 'のみ／のみ', 'isCorrect': False, 'reason': '【不正解】「のみ」は限定を表すため、言い訳を並立して述べる表現にはなりません。', 'trapCategory': 'formation'},
        {'text': 'やら／やら', 'isCorrect': False, 'reason': '【不正解】「〜やら〜やら」は困惑・混乱を表すため、本人が作為的に言い訳を並べる行為を批判するニュアンスに合いません。', 'trapCategory': 'nuance'},
        {'text': 'など／など', 'isCorrect': False, 'reason': '【不正解】イ形容詞語幹に「など／など」を重ねて言い訳を非難する用法は日本語として不自然です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-f-q6'] = {
    'context': 'Strict institutional entry requirement: government-issued photo ID only is recognized as valid.',
    'translation': 'For admission procedures to this institute, government-issued photo identification only is recognized as valid.',
    'overall': '入館手続きの有効書類を公的身分証明書だけに限定する公式な「〜のみ」を用います。',
    'options': [
        {'text': 'のみ', 'isCorrect': True, 'reason': '【正解】「身分証明書のみが有効と認められます」と、規則や公式手続きにおいて例外を許さず厳格に限定する表現です。', 'trapCategory': ''},
        {'text': 'だの', 'isCorrect': False, 'reason': '【不正解】不満の列挙表現であり、公的規則の記述として完全に破綻します。', 'trapCategory': 'meaning'},
        {'text': 'やら', 'isCorrect': False, 'reason': '【不正解】例示・困惑の表現であり、厳格な必要条件の限定には使えません。', 'trapCategory': 'meaning'},
        {'text': 'ばかり', 'isCorrect': False, 'reason': '【不正解】「身分証明書ばかりが有効」では不自然であり、単一の有効資格を公式に限定するには「のみ」を用います。', 'trapCategory': 'register'}
    ]
}

updates['skm2-p1-form-review-f-q7'] = {
    'context': 'Criticizing ungrateful diners: complaining about bland seasoning or small portions after someone cooked with care.',
    'translation': 'Complaining that the seasoning is bland or that the portion is too small, it is rude to nitpick at food prepared with devoted care.',
    'overall': '「味付けが薄いだの量が少なすぎるだの」と、料理への無礼な文句を批判的に並べる「〜だの〜だの」を用います。',
    'options': [
        {'text': 'だの／だの', 'isCorrect': True, 'reason': '【正解】せっかく作ってもらった料理に対して細かな不満を次々に並べ立ててケチをつける態度を非難する表現です。', 'trapCategory': ''},
        {'text': 'のみ／のみ', 'isCorrect': False, 'reason': '【不正解】限定表現であり、文句の列挙には使えません。', 'trapCategory': 'formation'},
        {'text': 'やら／やら', 'isCorrect': False, 'reason': '【不正解】「〜やら〜やら」は困惑・混乱を表すため、相手の身勝手なケチつけを非難する文脈には「だの／だの」が適切です。', 'trapCategory': 'nuance'},
        {'text': 'など／など', 'isCorrect': False, 'reason': '【不正解】不平不満を批判的に並べる構文として不自然です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-f-q8'] = {
    'context': 'Lifelong noble devotion: the sole purpose he pursued was quest for truth and service to humanity only.',
    'translation': 'The sole purpose he continued pursuing in life was the search for truth and service to all humanity only.',
    'overall': '生涯をかけた目的を「真理の探求と奉仕のみ」と格調高く限定する「〜のみ」を用います。',
    'options': [
        {'text': 'のみ', 'isCorrect': True, 'reason': '【正解】「唯一の目的は…奉仕のみであった」と、崇高な人生の目的を純粋にそれだけに限定する格調高い表現です。', 'trapCategory': ''},
        {'text': 'だの', 'isCorrect': False, 'reason': '【不正解】不満の列挙表現であり、崇高な人生の信条を語る文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'やら', 'isCorrect': False, 'reason': '【不正解】例示・混乱の表現であり、唯一の目的の限定には不適です。', 'trapCategory': 'meaning'},
        {'text': 'ばかり', 'isCorrect': False, 'reason': '【不正解】「奉仕ばかりであった」とすると「奉仕で占められていた」という傾向を表しますが、「唯一の目的は…のみであった」という唯一性の限定構文には「のみ」が最適です。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-f-q9'] = {
    'context': 'Reproaching blame-shifters: do not blame others making excuses like bad weather or sluggish turnout.',
    'translation': 'Without complaining that the weekend weather was bad or that spectator turnout was sluggish, do not blame the event failure entirely on others.',
    'overall': '「天気が悪いだの集まりが鈍いだの」と、失敗の原因を他人のせいにする言い訳の列挙を咎める「〜だの〜だの」を用います。',
    'options': [
        {'text': 'だの／だの', 'isCorrect': True, 'reason': '【正解】イベント失敗の言い訳としてあれこれ不満を並べ立てる無責任な態度を非難する表現「〜だの〜だの」が最適です。', 'trapCategory': ''},
        {'text': 'のみ／のみ', 'isCorrect': False, 'reason': '【不正解】限定表現であり、言い訳の並立には使えません。', 'trapCategory': 'formation'},
        {'text': 'やら／やら', 'isCorrect': False, 'reason': '【不正解】「〜やら〜やら」は混乱を表すため、他人に責任を押し付ける言い訳を非難する文脈には「だの／だの」が合致します。', 'trapCategory': 'nuance'},
        {'text': 'など／など', 'isCorrect': False, 'reason': '【不正解】言い訳を批判的に並べる構文として不自然です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-f-q10'] = {
    'context': 'Tournament qualification requirement: advancing to finals is permitted for the group-stage winners only.',
    'translation': 'Those who can advance to the final tournament of this competition are the winners only who fought through the grueling preliminary league at the top.',
    'overall': '決勝進出の資格を予選首位通過者だけに厳格に限定する公式な「〜のみ」を用います。',
    'options': [
        {'text': 'のみ', 'isCorrect': True, 'reason': '【正解】名詞「勝者」に接続し、「勝ち抜いた勝者のみである」と大会規定の厳格な資格限定を宣言する表現です。', 'trapCategory': ''},
        {'text': 'だの', 'isCorrect': False, 'reason': '【不正解】不満の列挙表現であり、大会規則の記述として破綻します。', 'trapCategory': 'meaning'},
        {'text': 'やら', 'isCorrect': False, 'reason': '【不正解】例示・困惑の表現であり、資格の厳密な限定には使えません。', 'trapCategory': 'meaning'},
        {'text': 'ばかり', 'isCorrect': False, 'reason': '【不正解】「勝者ばかりである」とすると「勝者ばかりが揃っている」という意味になり、進出資格の厳密な限定になりません。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-f-q11'] = {
    'context': 'Rebuking petty fashion critics: complaining that someone style is outdated or shoes do not match is petty.',
    'translation': 'Complaining that someone clothes sense is outdated or that shoes do not match, meddling in others fashion in detail is not good.',
    'overall': '「センスが古いだの靴が合っていないだの」と他人の服装に細かくケチをつける行為を非難する「〜だの〜だの」を用います。',
    'options': [
        {'text': 'だの／だの', 'isCorrect': True, 'reason': '【正解】他人のファッションに対してあれこれと細かい不満・批判を並べ立てる余計な口出しを批判する表現です。', 'trapCategory': ''},
        {'text': 'のみ／のみ', 'isCorrect': False, 'reason': '【不正解】限定表現であり、不満の列挙には使えません。', 'trapCategory': 'formation'},
        {'text': 'やら／やら', 'isCorrect': False, 'reason': '【不正解】「〜やら〜やら」は困惑を表すため、批判的なケチつけの列挙には「だの／だの」が適切です。', 'trapCategory': 'nuance'},
        {'text': 'など／など', 'isCorrect': False, 'reason': '【不正解】文脈として不自然です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-f-q12'] = {
    'context': 'Philosophical definition of liberty: true freedom is acquired when one can control one desires by reason only.',
    'translation': 'When humans can acquire true freedom is only at the time when they can control their own desires through reason.',
    'overall': '真の自由を獲得できる瞬間を理性で欲望を制御できた時だけに限定する格調高い「〜時のみ」を用います。',
    'options': [
        {'text': 'のみ', 'isCorrect': True, 'reason': '【正解】時を表す名詞句「時」に接続し、「コントロールできた時のみである」と哲学的真理の成立条件を厳格に限定する表現です。', 'trapCategory': ''},
        {'text': 'だの', 'isCorrect': False, 'reason': '【不正解】不満の列挙表現であり、哲学的な条件定義の文脈に合いません。', 'trapCategory': 'meaning'},
        {'text': 'やら', 'isCorrect': False, 'reason': '【不正解】例示・混乱の表現であり、厳密な条件限定には使えません。', 'trapCategory': 'meaning'},
        {'text': 'ばかり', 'isCorrect': False, 'reason': '【不正解】「時ばかりである」では意味が通じず、唯一の契機を限定するには「のみ」を用います。', 'trapCategory': 'syntax'}
    ]
}

# ==================== Form Review G (12 qs) ====================
updates['skm2-p1-form-review-g-q1'] = {
    'context': 'Moral conviction: one ought to act according to one own conscience rather than easily conforming to others.',
    'translation': 'Rather than easily conforming to other people opinions, one ought to act according to one own conscience.',
    'overall': '安易な同調を戒め、良心に従って行動するのが当然の道義的義務であると主張する「〜べきだ」を用います。',
    'options': [
        {'text': 'べき', 'isCorrect': True, 'reason': '【正解】サ変動詞「行動する」に接続し、「行動するべきだ」と個人の主体的な道義的責任・行動規範を強く主張する表現です。', 'trapCategory': ''},
        {'text': 'たがる', 'isCorrect': False, 'reason': '【不正解】「〜たがる」は第三者の希望（行動したがる）を表すため、一人称・一般的な道徳規範の主張には使えません。', 'trapCategory': 'meaning'},
        {'text': 'そうだ', 'isCorrect': False, 'reason': '【不正解】伝聞・様態の表現であり、「良心に従って行動するべきだ」という主観的信念の主張になりません。', 'trapCategory': 'meaning'},
        {'text': 'つもり', 'isCorrect': False, 'reason': '【不正解】「行動するつもりだ」は自分の個人的計画を表すため、他者や一般市民への道義的指針の提示になりません。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-g-q2'] = {
    'context': 'Third-person timidity: younger sister is very fearful and reluctant to go to the toilet alone at night.',
    'translation': 'My younger sister is very fearful by nature, and when night comes, she is reluctant to go to the toilet alone.',
    'overall': '三人称の妹の心理的傾向・嫌がる様子を客観的に描写する「〜たがらない」を用います。',
    'options': [
        {'text': 'たがらない', 'isCorrect': True, 'reason': '【正解】三人称の主語「妹」の感情・欲求の否定（〜したがらない）を外部から観察して述べる正しい文末表現です。', 'trapCategory': ''},
        {'text': 'たくない', 'isCorrect': False, 'reason': '【不正解】「〜たくない」は原則として話者自身（一人称）の内面的な希望の否定であり、三人称主語「妹は…行きたくない」と客観叙述の平叙文で結ぶのは不自然です。', 'trapCategory': 'syntax'},
        {'text': 'つもりだ', 'isCorrect': False, 'reason': '【不正解】「〜つもりだ」は意志・意図を表すため、怖くて行けないという感情的傾向の描写に合いません。', 'trapCategory': 'meaning'},
        {'text': 'ようとしない', 'isCorrect': False, 'reason': '【不正解】「行こうとしない」も頑固な拒絶として使えますが、選択肢の「行き（ます形語幹）」には直接接続できず、動詞志向形（行こうとしない）が必要です。', 'trapCategory': 'formation'}
    ]
}

updates['skm2-p1-form-review-g-q3'] = {
    'context': 'Universal truth about hasty cramming: superficial knowledge acquired overnight is utterly useless in the real test.',
    'translation': 'Even if you rush to pull an all-nighter right before the exam, superficial makeshift knowledge is of naturally no use in the actual test.',
    'overall': '一夜漬けの知識など本番では役に立たないという普遍的な心理・真理の性質を述べる「〜ものだ」を用います。',
    'options': [
        {'text': 'もの', 'isCorrect': True, 'reason': '【正解】「何の役にも立たないものだ」の形で、物事の本質的性質や一般的な理致・教訓を感慨を込めて述べる表現です。', 'trapCategory': ''},
        {'text': 'べき', 'isCorrect': False, 'reason': '【不正解】義務を表すため、「役に立たないべきだ（役に立たない義務がある）」では意味が破綻します。', 'trapCategory': 'meaning'},
        {'text': 'こと', 'isCorrect': False, 'reason': '【不正解】「役にも立たないことだ」では助言になり、一夜漬けが無駄になるという客観的真理の提示になりません。', 'trapCategory': 'nuance'},
        {'text': 'つもり', 'isCorrect': False, 'reason': '【不正解】意図を表すため、知識の効用の真理を述べる文脈に合いません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q4'] = {
    'context': 'Observation of hidden anxiety: looking calm on the surface, he seems uncontrollably anxious inside before exam results.',
    'translation': 'Although he appears calm and composed on the outside, on the inside he seems uncontrollably anxious ahead of his first-choice acceptance announcement.',
    'overall': '内心の抑えきれない不安の感情を表す「不安でたまらない（ようだ）」を用います。',
    'options': [
        {'text': 'たまらない', 'isCorrect': True, 'reason': '【正解】感情形容動詞「不安で」に接続し、「不安でたまらない（我慢できないほど不安だ）」と強烈な内心の動揺を表す表現です。', 'trapCategory': ''},
        {'text': 'べき', 'isCorrect': False, 'reason': '【不正解】義務を表すため、「不安でべき」という接続は文法的に破綻しています。', 'trapCategory': 'formation'},
        {'text': 'ものだ', 'isCorrect': False, 'reason': '【不正解】一般則を表すため、個別の人物の合格発表前の切迫した心情描写には「たまらない」を用います。', 'trapCategory': 'nuance'},
        {'text': 'つもりだ', 'isCorrect': False, 'reason': '【不正解】意図を表すため、「不安なつもりだ」では意味が通りません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q5'] = {
    'context': 'Diplomatic advice: if you truly want to deepen friendly relations with other nations, you should respect each other history.',
    'translation': 'If you truly want to deepen friendly relations with other countries, you should respect each other history and traditions.',
    'overall': '国家間友好を深めるための最善の忠告・指針として「〜ことだ」を用います。',
    'options': [
        {'text': 'こと', 'isCorrect': True, 'reason': '【正解】「友好関係を深化させたいなら…尊重することだ」と、条件節「〜たいなら」に呼応して最善の助言を述べる表現「〜ことだ」が最適です。', 'trapCategory': ''},
        {'text': 'べき', 'isCorrect': False, 'reason': '【不正解】「尊重するべきだ」も義務として使えますが、条件「深化させたいなら」という目標達成への助言構文には「〜ことだ」が最も典型的に呼応します。', 'trapCategory': 'nuance'},
        {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】「〜ものだ」は一般的真理を表し、個別の条件達成のための助言には「ことだ」を用います。', 'trapCategory': 'nuance'},
        {'text': 'たがる', 'isCorrect': False, 'reason': '【不正解】三人称の希望表現であり、助言の文末述語になりません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q6'] = {
    'context': 'Third-person eager desire: younger brother bought a new game and is eager to play with it engrossed from morning to night.',
    'translation': 'My younger brother had a new game bought for him and is eager to play with it absorbed from morning till night.',
    'overall': '三人称の弟が夢中で遊びたがっている生き生きとした様子を描写する「〜たがっている」を用います。',
    'options': [
        {'text': 'たがっている', 'isCorrect': True, 'reason': '【正解】三人称「弟」が新しいゲームで遊びたいという強い欲求を行動に表している様子を客観的に叙述する表現です。', 'trapCategory': ''},
        {'text': 'たい', 'isCorrect': False, 'reason': '【不正解】「〜たい」は話者自身（一人称）の内面的希望を表すため、平叙文で三人称の弟の行動描写に用いるのは文法上不自然です。', 'trapCategory': 'syntax'},
        {'text': 'つもりだ', 'isCorrect': False, 'reason': '【不正解】本人の主観的計画であり、他者から見た「夢中で遊んでいる」という感情の発露の描写に合いません。', 'trapCategory': 'nuance'},
        {'text': 'べきだ', 'isCorrect': False, 'reason': '【不正解】義務を表すため、「弟は朝から晩まで遊ぶべきだ」では意味が破綻します。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q7'] = {
    'context': 'Moral expectation for youth: as young people, they should never be complacent with status quo and challenge higher goals.',
    'translation': 'As young people, they ought to boldly challenge higher goals without being complacent with the status quo.',
    'overall': '「若者たるもの…果敢に挑戦するべきだ」と、若者の身分・立場に伴う当然の倫理的責任を強く主張します。',
    'options': [
        {'text': 'べき', 'isCorrect': True, 'reason': '【正解】「若者たるもの…」の呼応で、若者としての当然の義務や望ましい行動規範を力強く主張する「〜べきだ」が最適です。', 'trapCategory': ''},
        {'text': 'たがる', 'isCorrect': False, 'reason': '【不正解】三人称の欲求表現であり、社会通念に基づく行動規範の主張には使えません。', 'trapCategory': 'meaning'},
        {'text': 'そうだ', 'isCorrect': False, 'reason': '【不正解】伝聞・様態であり、自立した主張の文体になりません。', 'trapCategory': 'meaning'},
        {'text': 'つもりだ', 'isCorrect': False, 'reason': '【不正解】個人的計画を表すため、若者全体に対する社会的規範の主張に合いません。', 'trapCategory': 'nuance'}
    ]
}

updates['skm2-p1-form-review-g-q8'] = {
    'context': 'Universal human sentiment: as people age, they naturally recall with nostalgia the innocent days of their youth.',
    'translation': 'Every human being naturally recalls with nostalgia the innocent days of their youth as they grow older.',
    'overall': '加齢に伴う人間の普遍的な心理的傾向を表す「人間誰しも…思い出すものだ」を用います。',
    'options': [
        {'text': 'もの', 'isCorrect': True, 'reason': '【正解】「人間誰しも…思い出すものだ」の呼応で、年を重ねた人間の普遍的な心理・本質的性質を感慨を込めて述べる表現です。', 'trapCategory': ''},
        {'text': 'こと', 'isCorrect': False, 'reason': '【不正解】助言を表すため、自然に湧き上がる郷愁の心理的普遍則には「ものだ」を用います。', 'trapCategory': 'nuance'},
        {'text': 'べき', 'isCorrect': False, 'reason': '【不正解】義務を表すため、「昔を思い出す義務がある」となり不自然です。', 'trapCategory': 'meaning'},
        {'text': 'つもり', 'isCorrect': False, 'reason': '【不正解】個人的意志を表すため、全人類共通の感情の真理に合いません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q9'] = {
    'context': 'Reported hearsay: a friend still seems to be studying languages late into the night without giving up study abroad dreams.',
    'translation': 'My friend has not given up his dream of studying abroad, and it seems that he is still continuing his language studies late into the night even now.',
    'overall': '間接的な情報や噂を手がかりに、友人の現在の行動を客観的に推量・伝聞する「〜ているらしい」を用います。',
    'options': [
        {'text': 'ているらしい', 'isCorrect': True, 'reason': '【正解】動詞連用形「続け」に接続し、「今でも勉強を続けているらしい」と第三者の継続的行動を控えめに推量・伝聞する表現です。', 'trapCategory': ''},
        {'text': 'たい', 'isCorrect': False, 'reason': '【不正解】「〜たい」は一人称の希望であり、平叙文で友人の現在の行動事実の推量として結ぶことはできません。', 'trapCategory': 'syntax'},
        {'text': 'つもりだ', 'isCorrect': False, 'reason': '【不正解】「〜つもりだ」は話者自身の意図を表すため、他人の現在の勉強事実を報告する文脈に合いません。', 'trapCategory': 'nuance'},
        {'text': 'べきだ', 'isCorrect': False, 'reason': '【不正解】義務を表すため、「今でも夜遅くまで勉強を続けるべきだ」では友人の努力の現状を報告する文意とずれます。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q10'] = {
    'context': 'Lifelong health advice: if you wish to maintain a healthy body, you should keep balanced meals and moderate exercise in mind.',
    'translation': 'If you want to maintain a healthy body for a lifetime, you should keep a daily balanced diet and moderate exercise in mind.',
    'overall': '生涯の健康維持のための確実な助言として「〜ことだ」を用います。',
    'options': [
        {'text': 'こと', 'isCorrect': True, 'reason': '【正解】「健康的な体を維持したいなら…心がけることだ」と、条件「〜たいなら」に対して最善の生活習慣を助言する表現です。', 'trapCategory': ''},
        {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】「〜ものだ」は一般的真理を表し、相手に対する生活指導のアドバイスには「ことだ」を用います。', 'trapCategory': 'nuance'},
        {'text': 'べき', 'isCorrect': False, 'reason': '【不正解】「心がけるべきだ」も強い義務として可能ですが、条件節「〜たいなら」と呼応する親切な助言には「〜ことだ」が最も自然です。', 'trapCategory': 'nuance'},
        {'text': 'たがる', 'isCorrect': False, 'reason': '【不正解】三人称の欲求表現であり、助言の述語になりません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q11'] = {
    'context': 'Professional ethics: betraying client trust by breaking promises is strictly an act that ought never be forgiven.',
    'translation': 'Treacherous conduct such as reneging on promises and betraying client trust is strictly something that ought never to be forgiven as a business professional.',
    'overall': '顧客の信頼を裏切る背信行為は断じて許されるべきではないという倫理的禁止「〜べきではない」を用います。',
    'options': [
        {'text': 'べき', 'isCorrect': True, 'reason': '【正解】動詞受身形「許される」に接続し、「断じて許されるべきではない」と社会的正義・職業倫理に反する行為を強く禁止・断罪する表現です。', 'trapCategory': ''},
        {'text': 'もの', 'isCorrect': False, 'reason': '【不正解】「許されるものではない」も使えますが、「ビジネスパーソンとして断じて…」という強い職業倫理規範には「べきではない」が最適です。', 'trapCategory': 'nuance'},
        {'text': 'こと', 'isCorrect': False, 'reason': '【不正解】「許されることではない」よりも道義的義務の禁止としては「べきではない」が直接的に合致します。', 'trapCategory': 'nuance'},
        {'text': 'つもり', 'isCorrect': False, 'reason': '【不正解】意図を表すため、倫理的規範の禁止文脈には使えません。', 'trapCategory': 'meaning'}
    ]
}

updates['skm2-p1-form-review-g-q12'] = {
    'context': 'Universal truth of child-rearing: children naturally grow up looking at their parents backs rather than parents words.',
    'translation': 'Children are beings that naturally grow up looking at their parents backs rather than their parents words.',
    'overall': '子どもの成長という普遍的な人間的真理・本質を述べる「子どもというものは…育つものだ」を用います。',
    'options': [
        {'text': 'もの', 'isCorrect': True, 'reason': '【正解】主語「子どもというものは」と呼応し、「育つものだ」と教育・人間心理の普遍的な真理を感慨を込めて述べる表現です。', 'trapCategory': ''},
        {'text': 'こと', 'isCorrect': False, 'reason': '【不正解】「育つことだ」では助言になり、普遍的な真理を述べる呼応構文になりません。', 'trapCategory': 'nuance'},
        {'text': 'べき', 'isCorrect': False, 'reason': '【不正解】義務を表すため、「育つべきだ」では子どもの心理的真理の描写に合いません。', 'trapCategory': 'meaning'},
        {'text': 'つもり', 'isCorrect': False, 'reason': '【不正解】意図を表すため、普遍的真理の提示には不適です。', 'trapCategory': 'meaning'}
    ]
}

# Now apply all updates to exercises
count_updated = 0
for qid, upd in updates.items():
    if qid in ex_map:
        q = ex_map[qid]
        q['context'] = upd['context']
        q['translation'] = upd['translation']
        exp = q.setdefault('explanation', {})
        exp['overall'] = upd['overall']
        exp['options'] = upd['options']
        q['options'] = [o['text'] for o in upd['options']]
        q['correctIndex'] = next(i for i, o in enumerate(upd['options']) if o['isCorrect'])
        count_updated += 1

print(f"Applied updates to {count_updated} exercises.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully.")
