import json
import re
from pathlib import Path

data_dir = Path('c:/JLPT/jlpt-exam-prep/src/data')

# 1. Load all points
points_by_id = {}

# From bookGenki1, bookGenki2, bookSkmN3, bookSkmN2
for f in ['bookGenki1.ts', 'bookGenki2.ts', 'bookSkmN3.ts', 'bookSkmN2.ts']:
    content = (data_dir / f).read_text(encoding='utf-8')
    raw_json = content[content.index('= [') + 2 : content.rindex('];') + 1]
    pts = json.loads(raw_json)
    for p in pts:
        points_by_id[p['id']] = p

# From stream files
for f in data_dir.glob('stream*.ts'):
    content = f.read_text(encoding='utf-8')
    id_matches = re.findall(r'id:\s*\'([^\']+)\'', content)
    for gid in id_matches:
        if gid.startswith('s-') or gid.startswith('q-'):
            continue
        idx = content.find(f"id: '{gid}'")
        block = content[idx : idx + 600]
        lvl_m = re.search(r'level:\s*\'(N[2-5])\'', block)
        book_m = re.search(r'book:\s*\'([^\']+)\'', block)
        chap_m = re.search(r'chapter:\s*\'([^\']+)\'', block)
        title_m = re.search(r'title:\s*\'([^\']+)\'', block)
        
        lvl = lvl_m.group(1) if lvl_m else 'N3'
        book = book_m.group(1) if book_m else ('Shin Kanzen Master ' + lvl if lvl in ['N3', 'N2'] else ('Genki I' if lvl == 'N5' else 'Genki II'))
        chap = chap_m.group(1) if chap_m else 'Core Grammar'
        title = title_m.group(1) if title_m else gid
        
        points_by_id[gid] = {
            'id': gid,
            'title': title,
            'level': lvl,
            'book': book,
            'chapter': chap
        }

print(f"Total points mapped: {len(points_by_id)}")

# Organize into 4 books
books_data = [
    {
        'id': 'genki-1',
        'name': 'Genki I (3rd Ed.)',
        'level': 'N5',
        'description': 'Elementary Japanese I covering foundational sentence structures, verb classes, te-form, and basic relations (Lessons 1–12).',
        'filter_func': lambda p: p.get('level') == 'N5' or 'Genki I' in p.get('book', '')
    },
    {
        'id': 'genki-2',
        'name': 'Genki II (3rd Ed.)',
        'level': 'N4',
        'description': 'Elementary Japanese II bridging to intermediate: potential, favor transactions, passive, causative, and keigo (Lessons 13–23).',
        'filter_func': lambda p: p.get('level') == 'N4' or 'Genki II' in p.get('book', '')
    },
    {
        'id': 'skm-n3',
        'name': 'Shin Kanzen Master N3 Bunpou',
        'level': 'N3',
        'description': 'Comprehensive N3 grammar organized into 10 communicative categories and form classifications A–J.',
        'filter_func': lambda p: p.get('level') == 'N3' or 'N3' in p.get('book', '')
    },
    {
        'id': 'skm-n2',
        'name': 'Shin Kanzen Master N2 Bunpou',
        'level': 'N2',
        'description': 'The definitive N2 grammar manual covering all 26 core thematic chapters and supplementary functional expressions.',
        'filter_func': lambda p: p.get('level') == 'N2' or 'N2' in p.get('book', '')
    }
]

catalog_sources = []
for b in books_data:
    book_pts = [p for p in points_by_id.values() if b['filter_func'](p)]
    # Group by chapter/section
    chap_groups = {}
    for p in book_pts:
        chap = p.get('chapter', 'General Syllabus')
        chap_groups.setdefault(chap, []).append(p['id'])
    
    sections = []
    for chap_name, gids in sorted(chap_groups.items()):
        sections.append({
            'name': chap_name,
            'grammarIds': gids
        })
    
    catalog_sources.append({
        'id': b['id'],
        'name': b['name'],
        'level': b['level'],
        'description': b['description'],
        'sections': sections
    })

# Dump bookCatalog.ts
ts_out = f"""export interface BookSource {{
  id: string;
  name: string;
  level: 'N5' | 'N4' | 'N3' | 'N2';
  description: string;
  sections: {{
    name: string;
    grammarIds: string[];
  }}[];
}}

export const BOOK_SOURCES: BookSource[] = {json.dumps(catalog_sources, ensure_ascii=False, indent=2)};
"""

(data_dir / 'bookCatalog.ts').write_text(ts_out, encoding='utf-8')
print("Successfully wrote dynamic bookCatalog.ts!")
