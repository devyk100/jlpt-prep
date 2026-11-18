import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {e['id']: e for e in exercises}

correct_repairs = {
    ('g2-l13-ex-9', '三回'): "Correct. Expressing frequency per time period follows the formula [Time Period] に [Number of times] without an extra particle (一日に三回 = three times a day).",
    ('g2-l15-ex-3', 'しよう'): "Correct. The informal/plain volitional form of irregular verb する is しよう (今晩、宿題をしよう = Let's do homework tonight).",
    ('g2-l16-ex-2', 'といい'): "Correct. Wishing someone good luck in polite conversational style uses [Verb-dict] + といいですね (合格するといいですね = I hope you pass).",
    ('g2-l17-ex-4', 'なくて'): "Correct. The permission pattern for not doing an action ('you don't have to...') is [Verb-ない stem] + なくてもいい (来なくてもいいですよ).",
    ('g2-l17-ex-10', '難しかった'): "Correct. Hearsay 〜そうです attaches to the plain short form of adjectives (難しかったそうです = I heard that it was difficult).",
    ('g2-l18-ex-8', 'でしまい'): "Correct. The completion auxiliary 〜てしまう attached to 読んで (読んでしまいました) expresses thoroughly finishing the entire book in one day.",
    ('g2-l22-ex-7', '行かせました'): "Correct. Causative voice: the father had/made Ken (けんに) go on an errand to do shopping (買い物に行かせました).",
    ('g2-l13-ex-11', 'だし・だし'): "Correct. Listing multiple qualities for な-adjectives requires だし (上手だし、親切だし).",
    ('g2-l14-ex-12', 'を'): "Correct. While the adjective ほしい takes が, the derived verb ほしがる describes third-person outward desire and strictly marks its object with を (コートをほしがっています).",
    ('g2-l16-ex-12', 'のために'): "Correct. Performing a helpful favor for someone else's sake uses のために (ゆいのために買い物に行ってあげました).",
    ('g2-l17-ex-12', '来る'): "Correct. The conjunction 前に ('before doing X') strictly takes the non-past dictionary form of the verb (来る前に), even when narrating past events.",
    ('g2-l21-ex-12', '言わないで'): "Correct. Expressing a request for someone not to do something ('I want you not to...') requires the negative te-form 〜ないでほしい (言わないでほしいです).",
    ('skm3-c7-q4', 'という'): "【正解】「〜という」は歴史的記録や文献・古文書などの典拠に基づく伝聞・伝承を厳粛に伝える書き言葉の文末表現です（建てられたという）。",
    ('skm3-c7-q11', 'とか'): "【正解】「〜とかで」は「〜という話・噂を聞いたということで」と、人づてに聞いた不確実な伝聞理由を接続する慣用表現です（導入されるとかで）。",
    ('skm3-c10-q6', '入るな'): "【正解】「動詞辞書形＋な」は看板や標識で立ち入りを直接禁止する禁止形です（入るな）。",
    ('skm3-c10-q10', 'するな'): "【正解】「動詞辞書形＋な」は強い直接的禁止を表す命令調の引用（油断をするなと監督から言われた）です。",
    ('skm3-c10-q11', '出さないこと'): "【正解】「動詞ない形＋こと」は規則や注意書きで禁止・規律を提示する公式な表現です（出さないこと）。",
    ('skm3-fb-q1', 'にとって'): "【正解】「名詞＋にとって」は話者や評価者の判断基準・視点（〜の視点から見て）を表します（私にとって）。",
    ('skm3-fb-q5', 'について'): "【正解】「名詞＋について」は思考や発話・調査の対象・主題（〜をテーマとして）を表します（伝統文化について）。",
    ('skm3-fb-q7', 'にとって'): "【正解】「名詞＋にとって」は主体・立場から見た評価（留学生の立場から見て）を表します（留学生にとって）。",
    ('skm3-fb-q9', 'として'): "【正解】「名詞＋として」は資格・立場・名目（日本代表という立場で）を表します（日本代表として）。",
    ('skm3-fb-q11', 'によって'): "【正解】「名詞＋によって」は災害や外的要因による直接的な原因・理由を表します（台風によって停電が発生した）。",
    ('skm3-fi-q4', '決して'): "【正解】「決して」は文末の強い禁止・否定（〜てはいけない / 〜ない）と呼応して絶対的な決意・禁止を表します（決して誰にも話してはいけない）。",
    ('skm3-fi-q7', 'せいぜい'): "【正解】「せいぜい」は最大に見積もってもその程度にすぎないという上限の評価（せいぜい一万円くらい）を表します。",
    ('skm3-fi-q11', '必ずしも'): "【正解】「必ずしも」は文末の部分否定（〜とは限らない）と呼応して「常にそうであるとは言えない」という部分否定を成立させます（必ずしも質が良いとは限らない）。",
    ('skm3-p2-c4-q3', '海外のファンの'): "【正解（★・3番目）】「〜の間でも」に接続する名詞句修飾として★の位置（3番目）に入ります。",
    ('skm3-p3-c1-q7', 'とは限らない'): "【正解】「〜からといって…とは限らない」は「その理由があるからといって必ずしもそうなるわけではない」という部分否定の呼応表現です。"
}

count = 0
for (eid, text), new_reason in correct_repairs.items():
    ex = ex_map[eid]
    for opt in ex.get('explanation', {}).get('options', []):
        if opt.get('text') == text and opt.get('isCorrect'):
            opt['reason'] = new_reason
            count += 1

print(f"Fixed {count} corrupted correct reasons!")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
