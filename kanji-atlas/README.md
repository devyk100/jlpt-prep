# Kanji Atlas

A local React + Vite revision page. All characters appear together in four sections: **N5, N4, N3, N2**. The initial grid contains only kanji, with no selected card. Hover or keyboard-focus a character for meanings, on/kun readings and associated vocabulary. Click/tap to pin the scrollable card. Escape or clicking outside closes it.

## Start

Double-click `start.cmd`, or run from this folder:

```powershell
npm.cmd install
npm.cmd run dev -- --port 5173
```

Open http://127.0.0.1:5173. Keep the server running while studying. Node.js 20.19+ or 22.12+ is required by Vite. `npm.cmd run build` creates the production build; `npm.cmd run preview` serves it.

Compact grid fits more characters on screen. All four sections are always on the same scrolling page. Search matches characters, meanings, readings and vocabulary. Click a kanji to pin it while writing a distinction or mnemonic. Notes save in browser localStorage; use Export my notes for a JSON backup. Browser, origin and port determine where notes are stored; clearing browser data removes them.

## Content and honest limits

The grid now contains **1,111 kanji plus the iteration mark 々**: 85 N5, 174 N4, 403 N3 and 450 N2 characters. The original OpenJLPT snapshot contained 1,038 kanji. A full comparison of the supplied Genki publisher list and SKM N3/N2 kanji study lists added 73 missing kanji and 々. See [BOOK-AUDIT.md](BOOK-AUDIT.md) for exact scope, counts and PDF pages. Cards include expandable textbook references.

Vocabulary is drawn from 4,741 OpenJLPT N5–N2 entries. No N1 vocabulary is imported. Each card includes every matching vocabulary entry, including alternative spellings, sorted from easier to harder levels, then by length and reading. These are source-level labels, not an exam guarantee. Some characters have fewer than four matching words; eight kanji have no matches (諸 翌 兆 殿 冊 匹 隻 洪). Cards explicitly identify these gaps. The kanji coverage audit does not certify every vocabulary reading, definition, level or frequency. See `data/coverage.json`.

Genki I/II are not exact N5/N4 lists, and current JLPT levels do not have definitive published character lists. Existing community placements remain; additions use approximate textbook-based placements documented in each card. All 1,046 SKM N2 study-list kanji are included, along with 65 original community-list characters outside that book's selection. This is not an exact Kanji Study app export.

The data has not been exhaustively linguistically reviewed. Four observed source issues were corrected in `data/corrections.json`: the reading-dependent senses of 一日, a 四日 typo, 日にち spelling/gloss, and the misleading “new moon” gloss for 三日月. The original snapshot remains in `data/` for comparison. Kunyomi dots indicate the boundary before okurigana; hyphens mark affix readings.

## Sources and licence

Contains adapted data from OpenJLPT, [JMdict](https://www.edrdg.org/jmdict/j_jmdict.html) and [KANJIDIC2](https://www.edrdg.org/wiki/KANJIDIC_Project.html) (Electronic Dictionary Research and Development Group), and [Jonathan Waller’s JLPT lists](https://www.tanos.co.uk/jlpt/). Original snapshots also contain Tatoeba examples; the app omits examples. Full upstream attribution is in `data/NOTICE.md`, licence in `data/LICENSE`, and metadata in `data/meta.json`. Derived `src/kanji.json` and corrections are licensed **CC BY-SA 4.0**. Changes: subset to N5–N2, join vocabulary by character/alternate spelling, omit unused fields, sort and apply documented corrections.

All study data is bundled, so no dictionary API is needed at runtime. Optional Google Fonts fall back to installed Japanese fonts when offline.

## Maintain / verify

```powershell
python -X utf8 scripts/prepare-data.py --offline # rebuild from bundled snapshots
npm.cmd run check                            # coverage, joins, readings, N1 exclusion
npm.cmd run build
```

To deliberately refresh the upstream snapshot, omit `--offline`. This downloads current OpenJLPT main; inspect changes and the coverage report before relying on the updated data. The checked-in lockfile pins application dependencies.
