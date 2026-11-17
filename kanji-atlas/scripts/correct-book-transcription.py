import json
from pathlib import Path
p=Path('data/book-audit/skm2-kanji-pages.json');d=json.loads(p.read_text(encoding='utf-8'))
fixes={'134':{'牛魚':'牛去魚','県験':'県険験','語工':'語口工','好考校':'好考行校','高合国':'高号国'},'135':{'非渡貫':'非疲費','父部服':'父部風服','洋練様':'洋様','営央':'営王央','議客泣':'議客究泣','局玉軍':'局玉具軍'},'136':{'婦普並':'婦普平並'},'137':{'官看巻':'官巻看'},'138':{'順処署暑':'順準処署','臣申辛':'臣辛','積接':'積績接','善祖想':'善祖','像憎僧蔵':'像憎蔵'},'139':{'符富武':'符富膚武'}}
for page,changes in fixes.items():
 for a,b in changes.items():
  assert a in d[page],a
  d[page]=d[page].replace(a,b)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
s=''.join(''.join(d.values()).split());print({k:len(''.join(v.split())) for k,v in d.items()});print('total',len(s),'unique',len(set(s)))
