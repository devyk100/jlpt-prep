# Kanji book coverage audit — 16 November 2026

The grid contains every character in the checked Genki and Shin Kanzen Master kanji lists. This is a character-coverage audit, not a certification of every vocabulary gloss or a transcription of all textbook vocabulary.

| Source | Checked list | Unique coverage |
|---|---|---:|
| Genki third edition publisher kanji sheet | Entire one-page lesson list, Genki I and II | 316 kanji + 々 |
| SKM N3 Kanji | Lessons 1–25: PDF 124–148; prerequisites: PDF 149–156 | 654 kanji cumulatively |
| SKM N2 Kanji | Numbered list 1–1046: PDF 134–139 | 1,046 kanji cumulatively |

All PDF page numbers are one-based file pages, which can differ from printed book pages. Exact source paths are in `data/book-audit/paths.json`. The Genki reference is the supplied `genki-3rd_kanji_E.pdf`, rather than inferred JLPT levels.

The SKM N3 main lessons contain 443 appearances / 442 unique kanji: 354 new characters plus 88 revisited prerequisites. Its prerequisite list contains 300. Their union is 654, matching the introduction on PDF page 9. The N2 transcription has 1,046 unique characters and was independently checked against its PDF-page-9 selection rule: 1,023 legacy N2-or-easier characters, plus 28, minus 5. The independently obtained legacy metadata reproduces the exact set. OCR aided inspection; visually checked study lists are authoritative, not raw OCR or the scratch N3 index extraction.

## Changes made

The original 1,038-character grid omitted three Genki kanji (授 案 結) and 々; 21 of SKM N3's cumulative set; and 73 of SKM N2's set. These gaps overlap. Added kanji:

仮価保修健博及司善器基壁壊士嫌宙就展属帳康張志応恵態批拡授提操故救整暑暖条株案検標氏泣洪派災炎独狭率環異症看第節系級結統羊義製訳証評護賃較隠離養驚

The result is **1,111 kanji plus 々**, with no removal of the original 65 characters outside SKM N2's selection. Additions are placed approximately: five at N4, sixteen at N3 and fifty-two at N2; 々 at N5. These placements reflect earlier textbook coverage, not an official JLPT classification. Existing placements were retained. Genki lesson references and SKM lesson/list numbers appear in each applicable card.

Dictionary metadata for the added characters came from the same OpenJLPT dictionary data, even where its community level assigned a character to N1. This does not import any N1 vocabulary. Vocabulary still comes exclusively from the bundled N5–N2 snapshot; eight kanji currently have no matching words and many have fewer than four. Do not interpret the coverage pass as a guarantee about vocabulary completeness or level.

## Reproduce

Run `python -X utf8 scripts/audit-books.py`, then `python -X utf8 scripts/prepare-data.py --offline`, then `npm.cmd run check`. All pass. `npm.cmd run build` also passes, with Vite's bundle-size warning because dictionary data is bundled. Browser inspection confirmed 1,112 tiles, N5→N2 order, no initially open card, and functioning added-character references.

The machine report is `data/book-audit/report.json`; transcriptions, source references, supplemental metadata and legacy-set comparison are retained in `data/`. Original books and pre-existing project folders were not edited.
