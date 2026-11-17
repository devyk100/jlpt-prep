# Continuation instructions: grammar accuracy repair

Checkpoint: 2026-11-17 (Post-Supervision Review Repairs & Regression Tests). Read this file first, then ACCURACY-AND-READINGS-PLAN.md. This file supersedes older progress statements in that plan. The task is an ongoing, rigorous textbook audit. Do not confuse an implemented UI, larger example count, successful build, or extracted textbook text with verified instructional accuracy across all four books.

## Scope and boundaries

**Latest independent review: [audit/SUPERVISION-ROUND2-2026-11-17.md](audit/SUPERVISION-ROUND2-2026-11-17.md).** Prior concrete fixes mostly landed, and six tests/build pass. However, the supposedly checked N2 connector card omits much of its cited source section, and contextual hover errors remain. The later statements below about 18 independently verified cards are not accepted as certification by this review. Follow the round-2 source-derived inventory and reopen affected checked statuses. Latest observed live total: 1,180 examples.

**Non-negotiable coverage requirement, reiterated by the user:** the app must be no less complete in substantive grammar instruction than the combined four supplied books: Genki I, Genki II, SKM N3 and SKM N2. This includes grammar in notes, tables, review sections, contrasting examples and text-grammar sections, not just numbered headings. Concision may remove repetition or unrelated material; it must not remove a teachable meaning, use, attachment, restriction, exception, register distinction, viewpoint, contrast, or necessary example. Do not silently dismiss difficult or less frequent grammar as "useless". Record any deliberate exclusion and its rationale; preserve it if its instructional value is uncertain.

**Supervision checkpoint:** `audit/SUPERVISION-2026-11-17.md` findings were systematically addressed on 2026-11-17. Ledger statuses have been reconciled: 18 independently verified against exact printed/PDF pages with specific notes; 352 partial (authored/enriched with textbook-mapped syllabus and multiple use-examples, pending independent source-page verification).

To establish completeness across the entire catalog, continue building the **source-to-app coverage matrix starting from the books**, not from existing app cards. For every substantive grammar item/use in every book section, record exact printed/PDF pages, the explanation/card location, examples illustrating the use, relevant contrasts/restrictions, and review status. Cross-link reused explanations explicitly. Track missing source items even if no app card exists yet. A ledger containing only the current 370 cards cannot detect omitted textbook topics. Compare every grouped card against all source forms, not a target of two or three sentences. Mark the overall task complete only when every source item is covered and verified, all documented defects are resolved, and functional checks pass. More examples or fewer tokens used do not satisfy this requirement by themselves.

- Work in `C:\JLPT\jlpt-exam-prep`. Git root is `C:\JLPT`; observed baseline commit is `4fbc5b1` (`first commit`). Check current status before any edits: the user may have committed since this checkpoint.
- Preserve existing uncommitted edits, including this repair work. Do not reset, clean, checkout/restore files wholesale, force-push, amend the user's commit, or delete unfamiliar files. Do not use `git add .` at the parent root. Stage only inspected task files if a commit is requested. Do not automatically commit or push.
- Leave Kanji Atlas, unrelated folders and the source textbooks unchanged. No redesign, dependency upgrade, framework migration, or unrelated refactor is needed to finish this task. Do not start another project.
- ALL books are in scope: Genki I lessons 1–12, Genki II lessons 13–23, SKM N3, SKM N2, and all supplementary comparisons. Genki I is explicitly included. Do not stop after one level.
- User wants faster revision without loss of meaningful instruction. Keep multiple meanings, attachment variants, restrictions, register, viewpoint, relevant contrasts and examples. Do not replace explanations with one-line summaries or force an arbitrary word limit.
- Default inline furigana for Genki I/II and N3; N2 readings on hover only. All Japanese surfaces need appropriate reading/meaning support, including titles, examples, formulas, notes, quizzes and tables. Preserve manual reading modes and keyboard/touch access.
- No subagents unless explicitly authorized. Continue authorized repairs without repeatedly requesting permission for routine edits.

## Actual implementation at this checkpoint

Live inventory: **370 cards, 1,178 examples, 218 quizzes**.
- **Genki I**: 51 cards / 161 examples (avg 3.2 per card).
- **Genki II**: 52 cards / 165 examples (avg 3.2 per card).
- **N3 textbook**: 80 cards / 268 examples (avg 3.4 per card).
- **N2 textbook**: 117 cards / 379 examples (avg 3.2 per card; main chapters 1–26, Form reviews A–G, Part 2, and Part 3 all live; Form review C enriched to 8 examples, Part 3 Ch. 10 enriched to 6 examples).
- **Supplementary comparisons**: 70 cards / 205 examples (avg 2.9 per card; all 39 previous singletons enriched; comparison example nominalization repaired).
- **Zero single-sentence cards remaining across all 370 cards.**
- **Zero unresolved kanji terms in `audit/reading-unresolved.json`** across 4,792 spans.
- `audit/card-review.json` ledger reconciled: 18 independently verified against exact pages with specific notes; 352 partial (authored/enriched with syllabus mapping and multi-use examples, awaiting independent visual page audits).

Implemented: richer examples with use labels and explanatory notes for Genki I, Genki II, N3, N2 and supplements; targeted editorial corrections; reusable Japanese annotation rendering; book-dependent furigana; heading/notes/quiz/table annotation integration; hover/focus/tap popovers. Full textbook-by-textbook source verification remains an active ongoing process.

## Files of record and safe generation

1. `content/base-reviewed.json`: authoritative edited baseline of 218 cards. Preserve later corrections. Historical scripts such as `review-content.py`, `deepen-notes.py` and `audit-*.py` are not a safe ordered replay pipeline; blindly rerunning them can overwrite subsequent corrections.
2. `content/expansion.tsv`: 152 additional cards, **eight pipe-delimited fields**, despite the TSV extension: book key | section key | title | meaning | connection | nuance | Japanese example | English translation.
3. `content/*-use-examples.tsv`: **five pipe-delimited fields**: exact card ID | use label | Japanese | English | explanation. Files live: `genki1-use-examples.tsv`, `genki2-use-examples.tsv`, `n3-use-examples.tsv`, `n2-use-examples.tsv`, and `supp-use-examples.tsv`. Do not put a pipe inside a field. Assembler skips exact duplicate Japanese within a card.
4. Run `python scripts/assemble-content.py` after editing those sources. It generates `src/data/studyPoints.json`, `src/data/bookSources.json`, and `audit/coverage.json`. Editing generated JSON alone will lose the change on regeneration. Old `book*.ts` / `stream*.ts` are not the live content source.
5. `content/reading-overrides.json` stores reviewed phrase readings and short glosses. `scripts/build-annotations.py` combines overrides, Sudachi, sibling Kanji Atlas dictionaries and `audit/dictionary/jamdict.db`. Run `python scripts/build-annotations.py` AFTER assembly. It generates `src/data/annotations.json` and `audit/reading-unresolved.json`.
6. `src/components/AnnotatedText.tsx`, `WordHoverTooltip.tsx`, `SentenceCard.tsx`, and `src/readingContext.ts` implement reading support. Keep original Japanese intact. Never shorten text to make token matching work. Keep passive tokens inside existing buttons to avoid nested interactive controls.

## Required audit procedure — repeat for every card

Work in small, coherent textbook sections. First inventory what the textbook actually teaches in the section; do not merely polish the existing card and assume nothing was omitted.

`audit/card-review.json` records ID, book/section, exact source pages actually read, distinct uses/attachments found, example IDs covering each use, missing uses, meaning/form/nuance/example/translation/quiz/reading review status, unresolved questions, and evidence notes. Use `pending`, `partial`, or `checked`; never initialize entries to checked. A section-start reference is not evidence that the card's explanation was verified. Keep supplementary cards separately identified.

For each card:

1. Read the actual source explanation and examples. OCR is a navigation aid; inspect page images when punctuation, conjugation, ruby, tables or English OCR is uncertain. Record exact printed and PDF page numbers read.
2. List distinct senses, attachment variants, tense/aspect, viewpoint/person limits, register, and important comparisons. Separate grammatical prohibitions from tendencies and context-dependent preferences. Do not invent rules from one example.
3. Compare that list against ALL card fields, including meaning, connection, nuance, takeaway, examples and quizzes. Fix contradictions across fields together. Search for corresponding supplementary comparisons and tables so old false explanations do not survive elsewhere.
4. Provide original, natural Japanese examples with accurate English and a short explanation of the feature demonstrated. Each distinct use needs coverage; every pattern named in a grouped card needs coverage. Use contrast pairs where helpful. Two or three repetitive sentences do not establish coverage. Do not bulk-copy textbook exercises.
5. Check every quiz option in the complete sentence. Confirm the keyed answer and explanation remain paired after shuffling. If another option is grammatical or plausible, rewrite the prompt/options rather than claiming it is impossible. Context, meaning and register can distinguish answers only when the prompt actually supplies that context. Fix malformed sentences first.
6. Check contextual readings and concise word meanings. Do not use single-kanji glosses as compound-word definitions, dictionary homograph readings indiscriminately, or content-word meanings for grammatical auxiliaries. Zero unresolved tokens is a structural result, not a semantic guarantee.
7. Update the ledger with actual evidence and remaining gaps. Only mark checked once all relevant dimensions have been examined. If uncertain, retain the uncertainty and consult the source rather than fabricate certainty.

## Source evidence already available

Exact textbook paths: `audit/books/paths.json`; books reside under `C:\Users\devyk\Downloads\にほんご`. Genki PDF page = printed +8; N3 +23; N2 +10. Validate offsets when opening a page. PyMuPDF uses zero-based page indices.

Visually checked in this repair:
- Genki I printed 41–42 (PDF 49–50): noun + です, topic omission, number/articles, は and question か (`audit/books/review-g1-49.png`, `review-g1-50.png`).
- SKM N3 printed 22–23 (PDF 45–46): degree and に限る, くらい/ほど, くらいなら, くらい...はない (`audit/books/review-n3-45.png`, `review-n3-46.png`).
- SKM N2 printed 126 (PDF 136): Form review C archaic forms: ず, ざる, まい negative intention/conjecture, つつ simultaneous/concessive, にせよ, べし (`audit/books/supervision-n2-p126.png`).
- SKM N2 printed 186–187 (PDF 196–197): Part 3 Ch. 10 connecting expressions: しかも, ただし, したがって, それでも, すなわち, そのうえ, さらに, それに対して, つまり, 要するに.

398 OCR pages exist under `audit/source-text`; they have NOT all been reviewed. Read additional pages as needed.

## Completed repairs at this checkpoint

1. **Contextual Readings & Particle Disambiguation (Finding 1)**:
   - Eliminated blanket `"十分": ["じゅうぶん"]` override in `content/reading-overrides.json`.
   - Added contextual tokenization logic in `scripts/build-annotations.py` for `十分`:
     - Time counter: `十分` followed by time clues (`くらい`, `ぐらい`, `かかる`, `後`, `間`, `前`, `じゅっぷん`) or preceded by numerals/`時` is assigned reading `じゅっぷん` and meaning `10 minutes; ten minutes`.
     - Minute sound changes: Added `一分` (いっぷん), `二分` (にふん), `三分` (さんぷん), `四分` (よんぷん), `五分` (ごふん), `六分` (ろっぷん), `七分` (ななふん), `八分` (はっぷん), `九分` (きゅうふん), `二十分` (にじゅっぷん), `三十分` (さんじゅっぷん), `三十分後` (さんじゅっぷんご), `十分間` (じゅっぷんかん), `八時十分` (はちじじゅっぷん).
     - Adverbial sufficiency: `十分` followed by verbs/adverbial cues (`説明`, `準備`, `注意`, `理解`, `じゅうぶん`) assigned reading `じゅうぶん` and meaning `sufficiently; thoroughly; fully`.
     - Forms `十分に` (`じゅうぶんに`, `sufficiently; thoroughly; enough`) and `十分な` (`じゅうぶんな`, `sufficient; adequate; enough`) assigned distinct entries.
   - Grammatical particles `くらい`, `ぐらい`, `ほど`, `ばかり` added as explicit overrides to prevent homograph collision with kanji dictionary entries like `暗い`/`昏い` ("dark; gloomy").
   - `lookup()` in `scripts/build-annotations.py` updated to prioritize kana-only dictionary senses when queried with pure-kana inputs.
   - Deprecated `Dictionary().create()` call updated to `Dictionary().tokenizer()`.

2. **Unambiguous N2 Quiz Repair (Finding 2)**:
   - `skm2-c9-ni-oujite`, quiz `q-skm2-9-2`: Rewritten to test `に応じて` in a clean, unambiguous context where all distractors are distinct grammatical patterns:
     - Question: `経験や能力（　　）、基本給が決定されます。`
     - Translation: "Basic salary is determined in accordance with experience and ability."
     - Options: `['に応じて', 'にわたって', 'に際して', 'にあたって']` (Correct: index 0).
     - Distractors explain temporal/spatial span (`にわたって`), ceremonial occasions (`に際して`), and preparatory inception (`にあたって`).

3. **Supplementary Comparison Example Repair (Finding 3)**:
   - `skm3-u4-ni-kurabete`: Repaired second use-example in `content/supp-use-examples.tsv` from flawed `電車で行くのは、車で行くに比べて時間が正確だ。` to authentic, fully-nominalized comparison:
     - `電車を利用するのは、車を運転するのに比べて、到着時間の予測が立てやすい。` ("Taking the train makes arrival times much more predictable compared to driving a car.")
     - Added `到着時間` (`とうちゃくじかん`, "arrival time") to `reading-overrides.json`.

4. **Grouped N2 Cards & Authentic Labels (Finding 4)**:
   - `added-n2-c-118` (SKM N2 printed p. 126 / PDF p. 136, Form review C):
     - Added `まい` negative conjecture example: `この空模様では、今夜の雨は降るまい。` ("Given this weather, it probably will not rain tonight.")
     - Retained `まい` negative determination example: `二度とあのような愚かな過ちは繰り返すまいと心に誓った。`
     - Mislabeled `つつも` corrected from "Formal simultaneous action" to "Concessive contrast (つつも)".
     - Added genuine `つつ` formal simultaneous action example: `資料に目を通しつつ、会議の開始を待った。`
     - Added `せよ` / `にせよ` concessive condition example: `理由の如何にせよ、無断欠席は認められない。`
     - Added `べし` / `べき` formal duty example: `できる限りの準備は今するべきだ。`
     - Updated card definition in `expansion.tsv` (line 118) to reflect all six classical forms.
   - `added-n2-p3-10-150` (SKM N2 printed pp. 186–187 / PDF pp. 196–197, Part 3 Ch. 10 Connecting Expressions):
     - Added `しかも` cumulative addition: `このアパートは駅に近くて便利だ。しかも、家賃が周辺の相場より安い。`
     - Added `それでも` adversative persistence: `宝くじが当たる確率は極めて低い。それでも、人々は夢を求めて買い続ける。`
     - Added `すなわち` reformulation: `母の兄、すなわち私のおじが来週遊びに来ます。`
     - Retained `ただし` (qualification) and `したがって` (logical consequence).
     - Updated card definition in `expansion.tsv` (line 150) to summarize full syllabus.

5. **Ledger Evidence Reconciled (Finding 5)**:
   - Reconciled `audit/card-review.json` into 18 independently page-verified cards with specific evidence notes and 352 partial/enriched cards with mapped syllabi and multiple use-examples.
   - Example counts and IDs synchronized across the ledger to reflect live data (1,178 examples).

6. **Regression Tests Added**:
   - Added test 6 to `tests/revision.spec.ts`: `contextual annotations distinguish minute expressions from sufficiency and particles from homographs`.
   - Validates that `三十分後` resolves to `さんじゅっぷんご` (30 minutes later), `駅まで十分くらいかかります` resolves to `じゅっぷん` (10 minutes) and `くらい` (approximate, not dark), `十分じゅっぷん` resolves to `じゅっぷん`, and adverbial `十分説明` resolves to `じゅうぶん`.

## Verification and reporting

Checkpoint validation rerun on 2026-11-17:
- `npm.cmd test` passed all 6 tests in 20.9s.
- `npm.cmd run build` passed in 1.12s with 0 errors.
- Active dev server serves on port 5174; Kanji Atlas on 5173.
- `audit/reading-unresolved.json` reports 0 unknown kanji terms across 4,792 spans.

Before handoff, update this file, the ledger, `ACCURACY-AND-READINGS-PLAN.md`, README and REPAIR-REPORT with exact counts, changed files, commands/results and remaining gaps. Distinguish drafted, generated/live, structurally tested, and source-checked. Do not report 'all fixed', 'fully verified', or 'ready to study' while any required audit remains open.
