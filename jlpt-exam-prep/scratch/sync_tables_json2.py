import json

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# genki1VerbGroupsMatrix
vgroups = data['genki1VerbGroupsMatrix']
vgroups['rows'][0]['cells'][0] = 'Ends in る preceded by an /i/ or /e/ sound (e.g. 食べる, 見る, 起きる: 直前が「い段」または「え段」)'
vgroups['rows'][1]['cells'][3] = '⚠️ LOOKS LIKE RU BUT IS AN U-VERB: 帰る（かえります）, 入る（はいります）, 知る（しります）, 走る（はしります）!'
vgroups['rows'][2]['note'] = '来（く）る は活用によって「来（き）ます」と読みが変化します。'

with open('jlpt-exam-prep/src/data/mugUpTables.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated mugUpTables.json vgroups successfully!')
