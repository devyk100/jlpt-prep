# -*- coding: utf-8 -*-
"""
Compiles all unabridged textbook grammar points into typed TypeScript data files:
- src/data/bookGenki1.ts (Genki I Lessons 1–12)
- src/data/bookGenki2.ts (Genki II Lessons 13–23)
- src/data/bookSkmN3.ts (Shin Kanzen Master N3 Units 1–12 & Form Classifications)
- src/data/bookSkmN2.ts (Shin Kanzen Master N2 Chapters 1–26 & Part 2 Forms A–G)
And updates:
- src/data/grammarData.ts (Concatenates all 4 books + streams with unified lookup)
- src/data/bookCatalog.ts (Dynamic catalog mapping all sections to verified IDs)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'src' / 'data'
sys.path.append(str(ROOT / 'scripts'))

import data_full_genki1
import data_full_genki2
import data_full_skm_n3
import data_add_skm_n3
import data_full_skm_n2
import data_add_skm_n2

def dump_ts_array(var_name, points):
    json_str = json.dumps(points, ensure_ascii=False, indent=2)
    return f"""import type {{ GrammarPoint }} from '../types';

export const {var_name}: GrammarPoint[] = {json_str};
"""

def main():
    print("Collecting unabridged grammar datasets...")
    pts_g1 = data_full_genki1.get_full_genki1()
    pts_g2 = data_full_genki2.get_full_genki2()
    pts_n3 = data_full_skm_n3.get_full_skm_n3() + data_add_skm_n3.get_additional_skm_n3()
    pts_n2 = data_full_skm_n2.get_full_skm_n2() + data_add_skm_n2.get_additional_skm_n2()

    print(f"Writing bookGenki1.ts ({len(pts_g1)} points)...")
    (DATA_DIR / 'bookGenki1.ts').write_text(dump_ts_array('BOOK_GENKI1_POINTS', pts_g1), encoding='utf-8')

    print(f"Writing bookGenki2.ts ({len(pts_g2)} points)...")
    (DATA_DIR / 'bookGenki2.ts').write_text(dump_ts_array('BOOK_GENKI2_POINTS', pts_g2), encoding='utf-8')

    print(f"Writing bookSkmN3.ts ({len(pts_n3)} points)...")
    (DATA_DIR / 'bookSkmN3.ts').write_text(dump_ts_array('BOOK_SKM_N3_POINTS', pts_n3), encoding='utf-8')

    print(f"Writing bookSkmN2.ts ({len(pts_n2)} points)...")
    (DATA_DIR / 'bookSkmN2.ts').write_text(dump_ts_array('BOOK_SKM_N2_POINTS', pts_n2), encoding='utf-8')

    print("Updating grammarData.ts...")
    grammar_data_content = """import type { GrammarPoint, StreamCategory } from '../types';
import { STREAM_CATEGORIES } from './grammarStreams';
import { BOOK_GENKI1_POINTS } from './bookGenki1';
import { BOOK_GENKI2_POINTS } from './bookGenki2';
import { BOOK_SKM_N3_POINTS } from './bookSkmN3';
import { BOOK_SKM_N2_POINTS } from './bookSkmN2';
import { STREAM_GENKI_POINTS } from './streamGenki';
import { STREAM_TIME_POINTS } from './streamTime';
import { STREAM_CAUSALITY_POINTS } from './streamCausality';
import { STREAM_CONDITIONALS_POINTS } from './streamConditionals';
import { STREAM_LIMITS_POINTS } from './streamLimits';
import { STREAM_CONTRASTS_POINTS } from './streamContrasts';
import { STREAM_MODALITY_POINTS } from './streamModality';
import { STREAM_SOCIAL_POINTS } from './streamSocial';
import { STREAM_TRENDS_POINTS } from './streamTrends';
import { STREAM_TOPICS_POINTS } from './streamTopics';

export const ALL_GRAMMAR_POINTS: GrammarPoint[] = [
  ...BOOK_GENKI1_POINTS,
  ...BOOK_GENKI2_POINTS,
  ...STREAM_GENKI_POINTS,
  ...STREAM_TIME_POINTS,
  ...STREAM_CAUSALITY_POINTS,
  ...STREAM_CONDITIONALS_POINTS,
  ...STREAM_LIMITS_POINTS,
  ...STREAM_CONTRASTS_POINTS,
  ...STREAM_MODALITY_POINTS,
  ...STREAM_SOCIAL_POINTS,
  ...STREAM_TRENDS_POINTS,
  ...STREAM_TOPICS_POINTS,
  ...BOOK_SKM_N3_POINTS,
  ...BOOK_SKM_N2_POINTS
];

export const GRAMMAR_BY_ID: Record<string, GrammarPoint> = ALL_GRAMMAR_POINTS.reduce(
  (acc, point) => {
    acc[point.id] = point;
    return acc;
  },
  {} as Record<string, GrammarPoint>
);

export const STREAMS: StreamCategory[] = STREAM_CATEGORIES;

export { MASTER_MUG_UP_TABLES } from './mugUpTables';
export { BOOK_SOURCES, type BookSource } from './bookCatalog';
"""
    (DATA_DIR / 'grammarData.ts').write_text(grammar_data_content, encoding='utf-8')

    print("Generating comprehensive dynamic bookCatalog.ts...")
    points_by_id = {}

    for pts in [pts_g1, pts_g2, pts_n3, pts_n2]:
        for p in pts:
            points_by_id[p['id']] = p

    for f in DATA_DIR.glob('stream*.ts'):
        content = f.read_text(encoding='utf-8')
        id_matches = re.findall(r"id:\s*'([^']+)'", content)
        for gid in id_matches:
            if gid.startswith('s-') or gid.startswith('q-'):
                continue
            idx = content.find(f"id: '{gid}'")
            block = content[idx : idx + 600]
            lvl_m = re.search(r"level:\s*'([^']+)'", block)
            book_m = re.search(r"book:\s*'([^']+)'", block)
            chap_m = re.search(r"chapter:\s*'([^']+)'", block)
            title_m = re.search(r"title:\s*'([^']+)'", block)
            
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

    ts_catalog = f"""export interface BookSource {{
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
    (DATA_DIR / 'bookCatalog.ts').write_text(ts_catalog, encoding='utf-8')
    print("Compilation finished successfully!")
    print(f"Total points indexed across catalog: {len(points_by_id)}")

if __name__ == '__main__':
    main()
