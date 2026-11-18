import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {q['id']: q for q in exercises}

# 1. skm3-p3-c2-q10
q = ex_map['skm3-p3-c2-q10']
q['translation'] = 'Around this time next week, we will probably be walking on the beach in Hawaii together.'
q['context'] = 'Predicting future continuous action at a specific time: walking on the beach in Hawaii next week.'
for opt in q['explanation']['options']:
    if opt['text'] == '歩いてあった':
        opt['reason'] = '【不正解】「〜てある」は他動詞に接続して意図的な準備・結果残存を表す構文であり、自動詞「歩く」には接続できません。また未来の情景を推測する文脈に合いません。'

# 2. skm3-p3-c4-q6
q = ex_map['skm3-p3-c4-q6']
q['translation'] = 'Due to the progression of falling birthrates and population aging, the working population will likely decrease even further from now on.'
q['context'] = 'Predicting future demographic trend continuing forward from now on.'
for opt in q['explanation']['options']:
    if opt['text'] == 'こないだろう':
        opt['reason'] = '【不正解】「減少してこないだろう」は話者のいる時点に向かってくる視点の否定推量であり、「今後さらに（未来に向かって）」という将来への推移予測には「〜ていくだろう」を用います。'

# 3. skm3-p3-c5-q11
q = ex_map['skm3-p3-c5-q11']
q['translation'] = 'My mother left work early in order to take my sick younger sister to the hospital.'
q['context'] = 'Mother leaving work early to personally escort her sick daughter to the hospital.'
for opt in q['explanation']['options']:
    if opt['text'] == 'いかせられる':
        opt['reason'] = '【不正解】使役受身形「連れて行かせられる」は「誰かに強制されて無理やり行かされる」という意味になり、母親が自らの意志で病気の娘を病院へ連れていくという文脈に合いません。'

# 4. skm3-p3-c10-q4
q = ex_map['skm3-p3-c10-q4']
q['translation'] = 'From the questionnaire survey results, shifts in consumer consciousness became clear.'
q['context'] = 'Formal analysis report describing survey findings in written plain form.'
for opt in q['explanation']['options']:
    if opt['text'] == 'なっちゃった':
        opt['reason'] = '【不正解】「〜ちゃった」は親しい日常会話で用いる口語短縮形（後悔・完了）であり、公式なアンケート分析報告の書面語として文体が著しく不適切です。'

# 5. skm3-p3-c10-q5
q = ex_map['skm3-p3-c10-q5']
q['translation'] = 'The report that should be submitted by tomorrow has already been completely finished.'
q['context'] = 'Polite business status report to a supervisor in desu/masu form.'
for opt in q['explanation']['options']:
    if opt['text'] == 'したのである':
        opt['reason'] = '【不正解】「〜のである」は論文や解説書で背景説明を行う書面語の常体終止であり、上司に対する丁寧な完了報告（敬体統一）の口頭・メール表現として不調和です。'

# 6. skm3-p3-c10-q8
q = ex_map['skm3-p3-c10-q8']
q['translation'] = 'The acceleration of the declining birthrate will undoubtedly deal a massive blow to the future pension system.'
q['context'] = 'Formal written essay analyzing future impacts of demographic aging in plain form.'
for opt in q['explanation']['options']:
    if opt['text'] == 'ちがいありません':
        opt['reason'] = '【不正解】論文・論説文の客観的分析（常体・である調）において、文末に敬体「ちがいありません」を用いると文体の一貫性が崩れます。'
    elif opt['text'] == 'ちがいないね':
        opt['reason'] = '【不正解】親しい相手に同意を求める終助詞「ね」を伴うくだけた口頭表現であり、将来の年金制度危機を論述する論説文体として不適切です。'
    elif opt['text'] == 'ちがいないよ':
        opt['reason'] = '【不正解】話し相手に情報を教え伝える終助詞「よ」を伴う親密な会話表現であり、フォーマルな論説の結びには適しません。'

# 7. skm3-p3-c10-q11
q = ex_map['skm3-p3-c10-q11']
q['translation'] = 'Regarding our company new service, are there any unclear points or questions?'
q['context'] = 'Polite customer inquiry email from a company.'
for opt in q['explanation']['options']:
    if opt['text'] == 'あるだろうか':
        opt['reason'] = '【不正解】「〜だろうか」は自問自答や読者への抽象的問いかけを表す常体表現であり、顧客に対する丁寧な問い合わせ（「ございますでしょうか」）として不適切です。'

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved all 7 Part 3 fixes.")
