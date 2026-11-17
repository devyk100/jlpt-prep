import os
os.environ['OMP_THREAD_LIMIT']='1'
import fitz,pytesseract,json
from PIL import Image
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
base=Path(r'C:\Users\devyk\Downloads\にほんご');out=Path('audit/books');out.mkdir(parents=True,exist_ok=True)
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
paths={'g1':next(base.rglob('Genki Textbook 1 - 3rd Edition.pdf')),'g2':base/'Genki Textbook 2 - 3rd Edition.pdf','n3':next(base.rglob('*N3-Bunpou.pdf')),'n2':next(base.rglob('*N2-Bunpou.pdf'))}
work=[]
for key,pages in {'g1':range(14,19),'g2':range(12,19),'n3':range(5,10),'n2':range(3,8)}.items():
 d=fitz.open(paths[key])
 for p in pages:
  f=out/f'{key}-{p}.png';d[p-1].get_pixmap(matrix=fitz.Matrix(2,2)).save(f);work.append(f)
def ocr(p):
 s=pytesseract.image_to_string(Image.open(p),lang='jpn',config='--tessdata-dir C:/JLPT/kanji-atlas/data/book-audit/tessdata --psm 3');p.with_suffix('.txt').write_text(s,encoding='utf-8');return p.name
with ThreadPoolExecutor(max_workers=3) as pool:
 for result in pool.map(ocr,work):print(result,flush=True)
(out/'paths.json').write_text(json.dumps({k:str(v) for k,v in paths.items()},ensure_ascii=False),encoding='utf-8')
