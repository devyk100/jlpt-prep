import os
os.environ['OMP_THREAD_LIMIT']='1'
import json,fitz,pytesseract
from pathlib import Path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor,as_completed
root=Path(__file__).resolve().parents[1];out=root/'audit/source-text';out.mkdir(exist_ok=True)
paths=json.loads((root/'audit/books/paths.json').read_text(encoding='utf8'));coverage=json.loads((root/'audit/coverage.json').read_text())
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
work=[]
for b in ['g1','g2']:
 for page in coverage[b]['sectionStarts'].values():
  for printed in range(page+5,page+13):work.append((b,printed+8,printed))
for b,offset,last in [('n3',23,99),('n2',10,137)]:
 for printed in range(16 if b=='n3' else 8,last+1):work.append((b,printed+offset,printed))
def read(item):
 b,pdf,printed=item;dest=out/f'{b}-p{printed:03}.txt'
 if dest.exists():return
 with fitz.open(paths[b]) as d:
  pix=d[pdf-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7));img=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 text=pytesseract.image_to_string(img,lang='jpn',config='--tessdata-dir C:/JLPT/kanji-atlas/data/book-audit/tessdata --psm 3')
 dest.write_text(text,encoding='utf8')
with ThreadPoolExecutor(max_workers=1) as pool:
 futures=[pool.submit(read,item) for item in work]
 for i,f in enumerate(as_completed(futures),1):
  f.result()
  if i%20==0:print(f'{i}/{len(work)} pages extracted',flush=True)
print('Source extraction complete',flush=True)

