# Bunpou Atlas

Local React revision app for Genki I/II (3rd edition) and Shin Kanzen Master N3/N2 Bunpou.

Run `start-platform.bat`, or run `npm.cmd run dev` here and open http://127.0.0.1:5174. Kanji Atlas uses the separate port 5173.

The app now loads **370 revision cards**, **376 Japanese examples**, and **218 multiple-choice questions**. Counts refer to cards, not unique grammar forms: related patterns can share a card, and supplementary comparisons overlap textbook notes.

| Source | Revision cards | Sections represented |
| --- | ---: | ---: |
| Genki I | 51 | 12 lessons |
| Genki II | 52 | 11 lessons |
| SKM N3 Bunpou | 80 | 12 main chapters, 10 form reviews, 4 sentence-ordering and 10 passage sections |
| SKM N2 Bunpou | 117 | 26 main chapters, 7 form reviews, 3 sentence-ordering and 12 passage sections |
| Supplementary comparisons | 70 | Outside verified textbook mapping |

Use **4 Books** for textbook order and section-start page references, or search/filter the full list. Ctrl/Cmd+K opens search. Completion is explicit and stays in local storage. Quiz choices are shuffled deterministically with their explanations. Dotted words support hover, keyboard focus, and click; Escape dismisses the tooltip.

## Verification and limits

The supplied PDFs in `C:\Users\devyk\Downloads\にほんご` were used to inspect tables of contents and selected grammar pages. Catalog page references identify the **start of the section**, not the exact page of every pattern. The additions are original concise revision notes and examples, not transcribed textbook explanations or exercises. All listed sections have notes, but this is **not an exhaustive page-by-page reproduction or a claim that every textbook subpoint has an individual card**.

The 152 added cards have explanations, connection rules and example translations; they do not yet have authored multiple-choice quizzes or word-by-word hover annotations. Existing annotations cover selected words, not every word. Level labels are study groupings, not an official JLPT grammar syllabus. Structural tests cannot establish that every Japanese explanation or distractor is linguistically perfect.

## Maintenance

- Live content: `src/data/studyPoints.json` and `src/data/bookSources.json`.
- Reviewed baseline: `content/base-reviewed.json`.
- Additions: `content/expansion.tsv` (eight pipe-delimited fields per row).
- Regenerate live content and catalog: `python -X utf8 scripts/assemble-content.py`.
- Validate: `npm.cmd test`, `npm.cmd run build`, `npm.cmd run lint`.
- First-time browser tests: `npx.cmd playwright install chromium`.

The old `book*.ts` and `stream*.ts` content modules are retained as historical inputs but are no longer the app's content source. Do not use the old generation scripts to overwrite the reviewed dataset. `scripts/review-content.py` records the initial targeted corrections; subsequent editorial changes belong in the reviewed baseline or expansion file.

See `REPAIR-REPORT.md` for the audit changes. The pre-repair backup is `audit/before-repair.zip`; section counts are reproducible in `audit/coverage.json`.
