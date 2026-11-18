import json,re,collections,sqlite3,functools
from pathlib import Path
from sudachipy import dictionary,tokenizer
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT.parent/'kanji-atlas/data'
def hira(s):return ''.join(chr(ord(c)-96) if 'ァ'<=c<='ヶ' else c for c in s)
words=collections.defaultdict(list)
for level in ['n5','n4','n3','n2']:
 for item in json.loads((DATA/f'vocab-{level}.json').read_text(encoding='utf8')):
  for form in [item['word'],*item.get('other_forms',[])]:words[form].append(item)
db=sqlite3.connect(ROOT/'audit/dictionary/jamdict.db')
@functools.lru_cache(None)
def lookup(form,reading):
 entries=db.execute('SELECT idseq FROM Kanji WHERE text=? UNION SELECT idseq FROM Kana WHERE text=?',(form,form)).fetchall()
 is_pure_kana=re.search(r'[一-龯々]',form) is None
 if is_pure_kana:
  entries.sort(key=lambda eid:len(db.execute('SELECT text FROM Kanji WHERE idseq=?',(eid[0],)).fetchall()))
 for (eid,) in entries:
  readings=[r[0] for r in db.execute('SELECT text FROM Kana WHERE idseq=?',(eid,))]
  if reading not in readings:continue
  for (sid,) in db.execute('SELECT ID FROM Sense WHERE idseq=? ORDER BY ID',(eid,)):
   kr=[r[0] for r in db.execute('SELECT text FROM stagk WHERE sid=?',(sid,))]
   rr=[r[0] for r in db.execute('SELECT text FROM stagr WHERE sid=?',(sid,))]
   if (kr and form not in kr) or (rr and reading not in rr):continue
   gloss=[r[0] for r in db.execute("SELECT text FROM SenseGloss WHERE sid=? AND lang IN ('eng','en') LIMIT 2",(sid,))]
   if gloss:return '; '.join(gloss)
 return ''
t=dictionary.Dictionary().tokenizer(); points=json.loads((ROOT/'src/data/studyPoints.json').read_text(encoding='utf8'))
# Phrase-specific meanings take priority over literal word decomposition.
overrides={
 'に限る':['にかぎる','nothing beats; best to'], 'に限り':['にかぎり','limited to; only for'], 'に限って':['にかぎって','specifically; of all occasions/people'], 'とは限らない':['とはかぎらない','not necessarily; not always'],
 '限る':['かぎる','limit; restrict'], 'に過ぎない':['にすぎない','merely; no more than'], 'に違いない':['にちがいない','must be; surely'], 'に相違ない':['にそういない','must be; undoubtedly'], 'に決まっている':['にきまっている','bound to be; certainly'],
 'ざるを得ない':['ざるをえない','have no choice but to'], '得ない':['えない','cannot; impossible to'], '得る':['える','obtain; can (suffix)'], '一方':['いっぽう','one side; meanwhile'], '最中':['さいちゅう','in the middle of'], '末':['すえ','end; after a process'], '際して':['さいして','on the occasion of'],
 '私':['わたし','I; me'], 'は':['わ','topic marker (pronounced wa as a particle)'], 'へ':['え','toward (pronounced e as a particle)'], 'を':['を','object marker (pronounced o)'], 'が':['が','subject marker; but'], 'に':['に','at/to; target marker'], 'で':['で','at; by means of'], 'と':['と','and/with; quotation marker'], 'の':['の','noun link; nominalizer'], 'も':['も','also; even'], 'か':['か','question marker; or'], 'です':['です','polite ending: is/am/are'], 'だ':['だ','plain copula: is'], 'ます':['ます','polite verb ending'], 'ない':['ない','not; does not exist'], 'た':['た','past/completed form'], 'て':['て','linking te-form'], 'な':['な','na-adjective linker; prohibition after a verb'], 'ね':['ね','seeking agreement'], 'よ':['よ','informing/emphasizing'],
 '普通形':['ふつうけい','plain form'], '辞書形':['じしょけい','dictionary form'], '否定形':['ひていけい','negative form'], '意向形':['いこうけい','volitional form'], '命令形':['めいれいけい','imperative form'], '受身':['うけみ','passive'], '受け身':['うけみ','passive'], '使役':['しえき','causative'], '使役受身':['しえきうけみ','causative-passive'], '尊敬語':['そんけいご','honorific language'], '謙譲語':['けんじょうご','humble language'], '丁寧語':['ていねいご','polite language'], '接続':['せつぞく','connection; attachment'], '文末':['ぶんまつ','sentence ending'], '名詞':['めいし','noun'], '動詞':['どうし','verb'], '形容詞':['けいようし','adjective'], '副詞':['ふくし','adverb'], '助詞':['じょし','particle'], '形':['けい','form'], '節':['せつ','clause'], '主語':['しゅご','subject'], '述語':['じゅつご','predicate'], '文体':['ぶんたい','writing/speech style'], '自他':['じた','intransitive/transitive distinction'], '自動詞':['じどうし','intransitive verb'], '他動詞':['たどうし','transitive verb'],
 'くらい':['くらい','approximately; about; to the extent that'], 'ぐらい':['ぐらい','approximately; about; to the extent that'], 'ほど':['ほど','to the extent that; degree; about'], 'ばかり':['ばかり','only; just; approximately'],
 '一分':['いっぷん','1 minute'], '二分':['にふん','2 minutes'], '三分':['さんぷん','3 minutes'], '四分':['よんぷん','4 minutes'], '五分':['ごふん','5 minutes'], '六分':['ろっぷん','6 minutes'], '七分':['ななふん','7 minutes'], '八分':['はっぷん','8 minutes'], '九分':['きゅうふん','9 minutes'], '二十分':['にじゅっぷん','20 minutes'], '三十分':['さんじゅっぷん','30 minutes; half an hour'], '三十分後':['さんじゅっぷんご','30 minutes later; after 30 minutes'], '四十分':['よんじゅっぷん','40 minutes'], '五十分':['ごじゅっぷん','50 minutes'], '何分':['なんぷん','how many minutes'], '十分間':['じゅっぷんかん','for 10 minutes'], '八時十分':['はちじじゅっぷん','8:10; ten past eight'], '十分に':['じゅうぶんに','sufficiently; thoroughly; enough'], '十分な':['じゅうぶんな','sufficient; adequate; enough'],
 '十分':['__CONTEXTUAL__',''],
}
extra=ROOT/'content/reading-overrides.json'
if extra.exists():
 loaded=json.loads(extra.read_text(encoding='utf8'))
 if '十分' in loaded: del loaded['十分']
 overrides.update(loaded)
 overrides['十分']=['__CONTEXTUAL__','']
pattern=re.compile(r'[一-龯々〆ヵヶぁ-んァ-ヶー]+')
spans=set()
def walk(value):
 if isinstance(value,str):spans.update(pattern.findall(value))
 elif isinstance(value,list):
  for x in value:walk(x)
 elif isinstance(value,dict):
  for k,v in value.items():
   if k not in ['tokens','id','tags','sourceReference','book','chapter','streamId','streamName']:walk(v)
walk(points)
if (ROOT/'src/data/chapterExercises.json').exists():
 walk(json.loads((ROOT/'src/data/chapterExercises.json').read_text(encoding='utf8')))
if (ROOT/'src/data/mugUpTables.json').exists():
 walk(json.loads((ROOT/'src/data/mugUpTables.json').read_text(encoding='utf8')))
if (ROOT/'src/data/mugUpTables.ts').exists():
 spans.update(pattern.findall((ROOT/'src/data/mugUpTables.ts').read_text(encoding='utf8')))
unknown=collections.Counter(); annotation={}; overridekeys=sorted((k for k in overrides if k not in {"られ"}),key=len,reverse=True)
def segment(text):
 out=[];i=0
 while i<len(text):
  key=next((k for k in overridekeys if len(k)>1 and text.startswith(k,i)),None)
  if key:
   if key=='十分':
    rest=text[i+2:]
    if rest.startswith('に'):
     out.append({'word':'十分に','reading':'じゅうぶんに','meaning':'sufficiently; thoroughly; enough'});i+=3;continue
    elif rest.startswith('な'):
     out.append({'word':'十分な','reading':'じゅうぶんな','meaning':'sufficient; adequate; enough'});i+=3;continue
    elif any(rest.startswith(w) for w in ['くらい','ぐらい','かかる','かかり','かかって','かかった','後','間','前','待つ','歩く','走る','以内','程度','弱','強','じゅっぷん']) or (i>0 and text[i-1] in '一二三四五六七八九十時'):
     out.append({'word':'十分','reading':'じゅっぷん','meaning':'10 minutes; ten minutes'});i+=2;continue
    elif rest.startswith('じゅうぶん'):
     out.append({'word':'十分','reading':'じゅうぶん','meaning':'sufficient; enough'});i+=2;continue
    elif any(rest.startswith(w) for w in ['説明','準備','注意','考慮','理解','承知','検討','話し合','お気','よい','満足']):
     out.append({'word':'十分','reading':'じゅうぶん','meaning':'sufficiently; thoroughly; fully'});i+=2;continue
    else:
     out.append({'word':'十分','reading':'じゅうぶん','meaning':'sufficient; enough'});i+=2;continue
   reading,meaning=overrides[key];out.append({'word':key,'reading':reading,'meaning':meaning});i+=len(key);continue
  # Tokenize to the next grammar override, keeping morphology intact otherwise.
  end=min([j for j in range(i+1,len(text)) if any(text.startswith(k,j) for k in overridekeys if len(k)>1)]+[len(text)])
  chunk=text[i:end]
  for m in t.tokenize(chunk,tokenizer.Tokenizer.SplitMode.C):
   surface=m.surface();reading=hira(m.reading_form());base=m.dictionary_form();norm=m.normalized_form()
   auxiliary={'だ':'copula/linking form: is','です':'polite copula/ending','ます':'polite verb ending','た':'past/completed form','ない':'negative: not','ぬ':'negative: not (formal/older form)','ず':'negative: without doing','たい':'want to do','れる':'passive/potential auxiliary','られる':'passive/potential/honorific auxiliary','せる':'causative: make/let','させる':'causative: make/let','う':'volitional/conjecture ending','よう':'volitional ending','まい':'negative intention/conjecture','べし':'should; ought to','そうだ':'appearance/hearsay auxiliary','らしい':'apparently; characteristic of'}
   if m.part_of_speech()[0]=='助動詞':
    if surface=='なら':
     out.append({'word':'なら','reading':'なら','meaning':'if; in the case of (conditional)'});continue
    elif surface in ('だろ','だろう'):
     out.append({'word':surface,'reading':'だろう','meaning':'probably; conjecture copula'});continue
    elif surface in ('でし','でしょう'):
     out.append({'word':surface,'reading':'でしょう','meaning':'probably; polite conjecture copula'});continue
    elif base in auxiliary:
     out.append({'word':surface,'reading':reading,'meaning':auxiliary[base]});continue
   if m.part_of_speech()[1]=='非自立可能':
    if base=='切る':
     out.append({'word':surface,'reading':reading,'meaning':'finish completely; do to the very end; exhaustively'});continue
    elif base=='きれる':
     out.append({'word':surface,'reading':reading,'meaning':'can finish completely'});continue
    elif base=='通す':
     out.append({'word':surface,'reading':reading,'meaning':'persist in doing to the end; do all the way through'});continue
    elif base=='抜く':
     out.append({'word':surface,'reading':reading,'meaning':'persevere through to the end; endure completely'});continue
    elif base=='直す':
     out.append({'word':surface,'reading':reading,'meaning':'do again; redo; start over'});continue
   if surface=='上':
    prev_words=[x['word'] for x in out[-2:]]
    if 'の' in prev_words:
     domain_match=any(w in text for w in ['暦','法律','書類','計算','理論','制度','統計','立場','歴史'])
     if domain_match:
      out.append({'word':'上','reading':'うえ','meaning':'according to; from the standpoint of; in terms of'});continue
     else:
      out.append({'word':'上','reading':'うえ','meaning':'top; above; surface'});continue
    elif 'た' in prev_words:
     out.append({'word':'上','reading':'うえ','meaning':'upon; after doing'});continue
   if surface in overrides:
    reading,gloss=overrides[surface];out.append({'word':surface,'reading':reading,'meaning':gloss});continue
   candidates=words.get(surface,[]) or words.get(base,[]) or words.get(norm,[])
   if surface==base:matching=[v for v in candidates if hira(v['reading'])==reading];candidates=matching
   gloss='; '.join(candidates[0]['meanings'][:2]) if candidates else ''
   if not gloss:
    basereading=hira(''.join(x.reading_form() for x in t.tokenize(base,tokenizer.Tokenizer.SplitMode.C)))
    gloss=lookup(surface,reading) or lookup(base,basereading) or lookup(norm,basereading)
   if not gloss and re.search('[一-龯々]',surface):unknown[(surface,reading,base)]+=1
   out.append({'word':surface,'reading':reading,'meaning':gloss})
  i=end
 return out
for span in sorted(spans):annotation[span]=segment(span)
(ROOT/'src/data/annotations.json').write_text(json.dumps(annotation,ensure_ascii=False,separators=(',',':')),encoding='utf8')
(ROOT/'audit/reading-unresolved.json').write_text(json.dumps([dict(word=k[0],reading=k[1],base=k[2],occurrences=v) for k,v in unknown.most_common()],ensure_ascii=False,indent=2),encoding='utf8')
print('spans',len(spans),'unknown kanji terms',len(unknown));print('\n'.join(f'{k}: {v}' for k,v in unknown.most_common(120)))
