import pymupdf as fitz,json
from PIL import Image,ImageDraw
from pathlib import Path
out=Path('data/book-audit'); paths=json.loads((out/'paths.json').read_text(encoding='utf-8'))
for key in ['skm3','skm2']:
 doc=fitz.open(paths[key])
 ranges=[list(range(4,13)),list(range(100, min(len(doc),145))) if key=='skm3' else list(range(175,220))]
 for batch,nums in enumerate(ranges):
  sheet=Image.new('RGB',(1000,((len(nums)+4)//5)*300),'#ddd');draw=ImageDraw.Draw(sheet)
  for j,n in enumerate(nums):
   pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(.4,.4));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((195,275));x=j%5*200;y=j//5*300;sheet.paste(im,(x,y+20));draw.text((x,y),str(n),fill='black')
  sheet.save(out/f'{key}-contact-{batch}.jpg')
