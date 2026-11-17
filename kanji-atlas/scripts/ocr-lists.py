import json,re,os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['OMP_THREAD_LIMIT']='1'
out=Path('data/book-audit')
def run(n):
 im=Image.open(out/f'skm2-{n}.png');im=im.crop((300,60,960,1220))
 txt=pytesseract.image_to_string(im,lang='jpn',config='--tessdata-dir C:/JLPT/kanji-atlas/data/book-audit/tessdata --psm 6')
 (out/f'skm2-{n}-ocr.txt').write_text(txt,encoding='utf-8')
 return n, [''.join(re.findall('[一-龯]',line)) for line in txt.splitlines() if re.search('[一-龯]',line)]
with ThreadPoolExecutor(max_workers=3) as ex:
 for n,rows in ex.map(run,range(134,140)): print(n,rows)

