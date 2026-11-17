"""Reproduce the coverage audit from visually checked local-book transcriptions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
AUDIT = DATA / 'book-audit'
def read(name):
    return json.loads((AUDIT / name).read_text(encoding='utf-8'))
def write(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
def charset(pages):
    return set(''.join(''.join(pages.values()).split()))

genki = read('genki-kanji.json')
n3pages = read('skm3-lesson-pages.json')
prereqpages = read('skm3-prerequisite-pages.json')
n2pages = read('skm2-kanji-pages.json')
n3, prereq, n2 = map(charset, [n3pages, prereqpages, n2pages])
assert len(genki) == 317 and len(set(genki)-{'々'}) == 316
assert len(prereq) == 300 and len(n3) == 442
assert len(prereq & n3) == 88 and len(n3-prereq) == 354
assert len(prereq | n3) == 654
assert len(n2) == 1046 and sum(len(''.join(s.split())) for s in n2pages.values()) == 1046
# An independent check of the book's explicit selection rule (PDF p.9):
# 1,023 pre-2010 level 2-or-easier kanji, plus 28, minus five.
legacy=read('kanji-data-crosscheck.json')
old={c for c,k in legacy.items() if k.get('jlpt_old') in [2,3,4]}
add=set('隠炎壊株義及驚系嫌洪護災士氏就症証属態帳提統派博訳羊養離')
remove=set('掘耕脂双零')
assert len(old)==1023 and n2==(old|add)-remove

original={k['character']:k for n in [5,4,3,2] for k in json.loads((DATA/f'kanji-n{n}.json').read_text(encoding='utf-8'))}
references={}
def ref(c,label):
    references.setdefault(c,[])
    if label not in references[c]: references[c].append(label)
for c,g in genki.items():
    ref(c,f"{g['book']} · lesson {g['lesson']} (3rd-edition publisher kanji list)")
for page,chars in prereqpages.items():
    for c in chars: ref(c,f'SKM N3 · N5/N4 prerequisite list · booklet p.{int(page)-121} (PDF p.{page})')
for page,chars in n3pages.items():
    for c in chars: ref(c,f'SKM N3 · lesson {int(page)-123} · booklet p.{int(page)-121} (PDF p.{page})')
ordinal=0
for page,chars in n2pages.items():
    for c in ''.join(chars.split()):
        ordinal+=1
        ref(c,f'SKM N2 · kanji no.{ordinal} · booklet p.{int(page)-133} (PDF p.{page})')

metadata={k['character']:k for k in read('dictionary-additional-kanji.json')}
supplements=[]
missing=sorted((set(genki)|prereq|n3|n2)-set(original)-{'々'})
for c in missing:
    if c in genki or c in prereq:
        level='N4'
        basis='Added from Genki II / SKM N3 prerequisite coverage; N4 is an approximate study placement.'
    elif c in n3:
        level='N3'
        basis='Added from SKM N3 lesson coverage; community lists may assign a different level.'
    else:
        level='N2'
        basis='Added from the SKM N2 study list; community lists may assign a different level.'
    k=metadata[c]
    supplements.append({key:k[key] for key in ['character','strokes','freq','onyomi','kunyomi','meanings']} | {'level':level,'levelBasis':basis})
supplements.append({'character':'々','level':'N5','strokes':3,'freq':None,'onyomi':[],'kunyomi':[],
    'meanings':['kanji repetition mark (not a kanji)','repeats the preceding kanji; pronunciation depends on the word'],
    'levelBasis':'Genki I lesson 12; placed with foundational revision. This is a symbol, not an independent kanji.'})
write(DATA/'book-supplements.json',supplements)
write(DATA/'book-references.json',references)
report={'checkedOn':'2026-11-16','method':'Visual transcription of numbered study lists, with count/overlap checks and an independent check of the SKM N2 selection rule.',
    'sources':read('paths.json'),
    'genki':{'entries':317,'kanji':316,'missingBefore':sorted(set(genki)-set(original))},
    'skmN3':{'prerequisites':300,'lessonKanji':442,'revisitedPrerequisites':88,'newKanji':354,'cumulative':654,'missingBefore':sorted((prereq|n3)-set(original))},
    'skmN2':{'cumulative':1046,'missingBefore':sorted(n2-set(original)),'originalGridOutsideThisBook':sorted(set(original)-n2)},
    'addedKanji':missing,'addedSymbol':'々','expectedGridKanji':len(original)+len(missing),'expectedGridEntries':len(original)+len(missing)+1,
    'limits':['Kanji coverage audit, not a word-by-word verification of every dictionary gloss or all textbook vocabulary.', 'Genki I/II are not exact N5/N4 lists. Existing community placements are retained; added entries use documented approximate textbook-based placements.', 'Original grid entries outside the SKM N2 selection remain available.']}
write(AUDIT/'report.json',report)
print(f'PASS: Genki 316 kanji + 々; SKM N3 654 cumulative; SKM N2 1046. Added {len(missing)} kanji + 々.')
