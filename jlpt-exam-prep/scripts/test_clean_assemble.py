import json, collections, re
from pathlib import Path

root = Path('c:/JLPT/jlpt-exam-prep')
p = json.loads((root / 'content/base-reviewed.json').read_text(encoding='utf8'))
pages = {
  'g1': dict(zip(map(str, range(1, 13)), [36, 56, 82, 102, 128, 146, 166, 186, 210, 230, 254, 272])),
  'g2': dict(zip(map(str, range(13, 24)), [22, 46, 70, 92, 114, 136, 160, 180, 206, 228, 250])),
  'n3': dict(zip(map(str, range(1, 13)), [16, 18, 22, 24, 30, 32, 36, 38, 44, 46, 50, 52])),
  'n2': dict(zip(map(str, range(1, 27)), [8, 12, 16, 20, 24, 30, 34, 38, 42, 46, 52, 56, 60, 64, 68, 74, 78, 82, 86, 90, 96, 100, 104, 108, 112, 116]))
}
for b, form, part2, part3 in [
  ('n3', [58, 62, 66, 70, 74, 80, 84, 88, 92, 96], [104, 106, 108, 110], [116, 118, 122, 124, 128, 130, 134, 136, 140, 142]),
  ('n2', [122, 124, 126, 128, 132, 134, 136], [140, 142, 146], [150, 154, 158, 162, 166, 170, 174, 178, 182, 186, 190, 194])
]:
  pages[b].update(dict(zip('ABCDEFGHIJ', form)))
  for part, nums in [(2, part2), (3, part3)]:
    pages[b].update({f'P{part}-{i+1}': n for i, n in enumerate(nums)})

meta = {
  'g1': ('genki-1', 'Genki I', 'N5'),
  'g2': ('genki-2', 'Genki II', 'N4'),
  'n3': ('skm-n3', 'Shin Kanzen Master N3', 'N3'),
  'n2': ('skm-n2', 'Shin Kanzen Master N2', 'N2')
}
fix = {
  'g1-l11-sugiru': '12',
  'skm3-u6-no-dakara-reality': '5',
  'skm3-u7-you-ni-purpose': 'D',
  'skm3-u7-you-ni-suru': '11',
  'skm3-u8-wake-niwa-ikanai': 'E',
  'skm3-u9-beki-da': '10',
  'skm3-u10-rashii': 'J',
  'skm3-u11-koto-ni-natte-iru': 'G',
  'skm2-c4-kagiri-dewa': '5',
  'skm2-c5-nomi-narazu': '6',
  'skm2-c5-bakari-ka': '6',
  'skm2-c6-ni-kansuru': '7',
  'skm2-c13-ni-kakete-wa': '7',
  'skm2-c18-dakeni': '17',
  'skm2-c19-monono': '14',
  'skm2-c21-ni-kimatte-iru': '22',
  'skm2-c21-ni-chigai-nai': '22',
  'skm2-c22-kaneru': '18',
  'skm2-c24-zaru-wo-enai': '25',
  'skm2-c26-te-itadaku': 'P3-7',
  'skm2-p2-mai': '24',
  'skm3-u4-ni-kurabete': '4',
  'skm3-u9-garu': '9',
  'skm3-u10-ni-yoru-to': '10',
  'skm3-fc-tokoro-datta': 'C',
  'skm3-fj-kimi': 'J',
  'skm3-fj-ppoi-personality': 'J',
  'skm3-fj-darake-flaws': 'J',
  'skm3-fj-gachi': 'J',
  'skm2-c10-nuki-de': '10',
  'skm2-c14-ippou-de': '14',
  'skm2-c17-wo-keiki-ni': '17',
  'skm2-c18-kara-koso': '18',
  'skm2-c25-te-wa-irarenai': '25',
  'skm2-p2-kko-nai': 'P2-1',
  'skm2-p2-kai-ga-aru': 'P2-1',
  'skm2-p2-wo-oite': 'P2-1',
  'skm2-p2-majiki': 'P2-2',
  'skm2-p2-bekarazu': 'P2-2',
}
sections = collections.defaultdict(lambda: collections.defaultdict(list))

def assign(x, b, s):
  assert s in pages[b], (x['id'], b, s)
  name = ('Lesson ' if b.startswith('g') else 'Part 1 · Chapter ') + s if s.isdigit() else (
    'Part ' + s[1] + ' · Chapter ' + s[3:] if s.startswith('P') else 'Part 1 · Form review ' + s
  )
  page = pages[b][s]
  offset = 8 if b.startswith('g') else 23 if b == 'n3' else 10
  x.update(
    book=meta[b][1],
    chapter=name,
    sourceReference=f'Section starts on printed p. {page} (PDF p. {page+offset}). Original revision notes; not a transcription.'
  )
  sections[b][s].append(x['id'])

for x in p:
  ident = x['id']
  if ident.startswith('added-'):
    parts = ident.split('-')
    b = parts[1]
    if parts[2].startswith('p'):
      s = f"{parts[2].upper()}-{parts[3]}"
    else:
      s = parts[2].upper()
    assign(x, b, s)
  else:
    b = next((b for prefix, b in [('g1-', 'g1'), ('g2-', 'g2'), ('skm3-', 'n3'), ('skm2-', 'n2')] if ident.startswith(prefix)), None)
    if not b:
      x.pop('book', None)
      x.pop('chapter', None)
      continue
    m = re.search(r'-(?:l|u|c)(\d+)-', ident)
    s = fix.get(ident) or (m[1] if m else 'J' if '-fj-' in ident else None)
    assert s, (ident, b)
    assign(x, b, s)

print("Total cards assigned:", len(p))
for b in meta:
  missing = set(pages[b]) - set(sections[b])
  print(f"{b}: {len(sections[b])} sections, missing: {missing}")
