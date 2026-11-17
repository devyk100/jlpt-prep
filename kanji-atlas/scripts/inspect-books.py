import fitz,json
from pathlib import Path
base=Path('C:/Users/devyk/Downloads/にほんご')
out=Path('C:/JLPT/kanji-atlas/data/book-audit')
paths={'genki-list':base/'genki-3rd_kanji_E.pdf','genki1':base/'Genki (N5)'/'Genki Textbook 1 - 3rd Edition.pdf','genki2':base/'Genki Textbook 2 - 3rd Edition.pdf','skm3':base/'Shin Kanzen Master N3'/'Shin_Kanzen_Master_N3_Kanji.pdf','skm2':base/'Shin Kanzen Master N2'/'Shin_Kanzen_Masuta_N2-Kanji.pdf'}
for key,path in paths.items():
 doc=fitz.open(path)
 texts=[p.get_text() for p in doc]
 (out/f'{key}-text.json').write_text(json.dumps(texts,ensure_ascii=False),encoding='utf-8')
 print(key,len(doc),'text chars',sum(map(len,texts)), 'last pages',[(i+1,len(texts[i])) for i in range(max(0,len(doc)-8),len(doc))])
 for i in sorted(set([0,1,2,3,len(doc)-3,len(doc)-2,len(doc)-1])):
  if i<0 or i>=len(doc): continue
  page=doc[i]; page.get_pixmap(matrix=fitz.Matrix(1,1)).save(out/f'{key}-{i+1}.png')
(out/'paths.json').write_text(json.dumps({k:str(v) for k,v in paths.items()},ensure_ascii=False),encoding='utf-8')

