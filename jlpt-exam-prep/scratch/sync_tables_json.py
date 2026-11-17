import json

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. teFormMatrix
te = data['teFormMatrix']
te['rows'][0]['cells'] = ['買う, 待つ, 取る', '買って, 待って, 取って', '買った, 待った, 取った', 'う・つ・る → って / った (促音便: 小さい「っ」+ て)']
te['rows'][0]['note'] = 'Classic rhythm: "u, tsu, ru" becomes "tte"'

te['rows'][1]['cells'] = ['飲む, 遊ぶ, 死ぬ', '飲んで, 遊んで, 死んで', '飲んだ, 遊んだ, 死んだ', 'む・ぶ・ぬ → んで / んだ (撥音便: 濁音の「で」)']
te['rows'][1]['note'] = 'Voiced consonants always take で, not て.'

te['rows'][2]['cells'] = ['書く, 泳ぐ', '書いて, 泳いで', '書いた, 泳いだ', 'く → いて, ぐ → いで (イ音便: い + て/で)']
te['rows'][2]['note'] = 'CRITICAL EXCEPTION: 行く は「いいて」にならず、「行って・行った」と促音便になります。'

te['rows'][3]['cells'] = ['話す, 出す', '話して, 出して', '話した, 出した', 'す → して / した']
te['rows'][3]['note'] = 'Behaves cleanly like polite shimasu.'

te['rows'][4]['label'] = 'Group 2: る (一段動詞)'
te['rows'][4]['cells'] = ['食べる, 見る, 起きる', '食べて, 見て, 起きて', '食べた, 見た, 起きた', 'る を取って「て・た」を付ける']
te['rows'][4]['note'] = 'Vowel before る is usually e or i (たべ・み).'

te['rows'][5]['label'] = 'Group 3: Irregular (変格動詞)'
te['rows'][5]['cells'] = ['する, 来る', 'して, 来て', 'した, 来た', '不規則活用: 来る は「来て（きて）・来た（きた）」と読みが変化します。']
te['rows'][5]['note'] = 'Notice 来る changes reading to 「き」 in て/た form: 来て（きて）, 来た（きた）.'

# 2. genki1TimeAndAgeMatrix
time_age = data['genki1TimeAndAgeMatrix']
time_age['rows'][1]['note'] = 'Mnemonic: 1, 3, 4, 6, 8, 10 は半濁音の「ぷん」になります。'
time_age['rows'][2]['cells'][1] = '⚠️ 1歳 = いっさい, 8歳 = はっさい, 10歳 = じゅっさい (じっさい), 20歳 = はたち (二十歳)'
time_age['rows'][2]['note'] = '20歳 は「はたち（二十歳）」と読み、後ろに「さい」は付きません。'

# 3. genki1AdjectivesMatrix
adj = data['genki1AdjectivesMatrix']
adj['rows'][0]['cells'][0] = '高いです'
adj['rows'][0]['note'] = '⚠️ THE IRREGULAR "GOOD": いい は「良い（よい）」から変化します。否定: よくないです, 過去: よかったです, 過去否定: よくなかったです。「いくない」は誤り ❌!'
adj['rows'][1]['cells'][0] = '静かです'
adj['rows'][1]['cells'][2] = '静かでした'

# 4. genki2TransitiveIntransitiveMatrix
trans = data['genki2TransitiveIntransitiveMatrix']
trans['rows'][5]['note'] = '「入る（はいる）」は一段動詞の形ですが、五段（う動詞）活用です。'

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated mugUpTables.json successfully!')
