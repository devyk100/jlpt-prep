# Grammar accuracy and reading-support plan

Updated: 2026-11-17. Working project: C:\JLPT\jlpt-exam-prep.

**Start continuation with [CONTINUE-HERE.md](CONTINUE-HERE.md).** It contains the current operating instructions, Git boundaries, authoritative file pipeline, per-card review procedure, known defects, and completion gates. Historical checkpoints below must not override its current state.

**Latest user requirement:** substantive grammar coverage must be at least as complete as all four supplied books combined, including Genki I. Remove only repetition/unrelated material, never instructional nuance. Establish this using a textbook-to-app item/use matrix, including notes, tables and review sections; auditing existing cards alone cannot find missing topics. See `audit/SUPERVISION-2026-11-17.md` for the supervision findings on the subsequent enrichment work. Current live total is 1,173 examples; larger counts do not establish equivalence to the books.

## Latest checkpoint — supersedes historical status below

The user explicitly reiterated **Genki I too**. Audit all 12 Genki I lessons with the same depth required for Genki II, SKM N3, SKM N2 and supplementary comparisons. Do not treat introductory grammar as obvious or exempt it from source verification. Include topic omission, noun predicates, particles, conjugation, tense/aspect, attachment, contextual interpretations, and the distinct uses of each pattern. Check examples, translations, quizzes and hover readings as well as explanations.

Current live inventory: **370 cards, 1,178 examples, 218 quizzes**.
- Genki I: 51 cards / 161 examples (avg 3.2 per card)
- Genki II: 52 cards / 165 examples (avg 3.2 per card)
- N3 textbook: 80 cards / 268 examples (avg 3.4 per card)
- N2 textbook: 117 cards / 379 examples (avg 3.2 per card; main chapters 1–26, Form reviews A–G, Part 2, and Part 3 all live; Form review C enriched with 7 use-examples, Part 3 Ch. 10 enriched with 5 use-examples)
- Supplementary: 70 cards / 205 examples (avg 2.9 per card; all 39 previous singletons enriched; nominalization and punctuality repaired on ni-kurabete)
- **Zero single-sentence cards remaining across all 370 cards.**
- **Zero unknown kanji terms in `audit/reading-unresolved.json`** across 4,792 spans.
- `audit/card-review.json` reconciled: 18 independently page-verified cards with specific evidence notes; 352 partial (authored/enriched with syllabus mapping and multi-use examples, awaiting independent visual page audits).

Supervision pass 2026-11-17 repairs applied: contextual tokenization logic distinguishing minute counters (じゅっぷん/さんじゅっぷん) from sufficiency (じゅうぶん/じゅうぶんに), homograph filtering for particles (くらい/ぐらい), unambiguous N2 quiz options for skm2-c9-ni-oujite, authentic examples for classical forms (added-n2-c-118) and text connectors (added-n2-p3-10-150). All 6 Playwright tests passed (20.9s), including contextual annotation regressions. Production build passed (1.12s, 0 errors). Full textbook-by-textbook source verification remains an active ongoing process.

## User requirements (preserve these)

The app should make textbook grammar faster to revise without losing important distinctions, restrictions, register or practical use. Do not claim full verification merely because every section has a card. The user explicitly asks to check inaccurate and overcompressed explanations, including XはYです, and make Japanese patterns such as に限る readable without a separate lookup.

Latest preference: **Genki I/II and N3 show furigana above Japanese by default; N2 does not show it above, but readings and concise meanings remain available on hover.** Give one or two relevant meanings, not long dictionary dumps. Keep optional manual reading controls. Hover must also work with focus/tap where appropriate.

User authorized editing this project. Do not modify unrelated C:\JLPT files or the source textbooks. No subagents unless explicitly authorized. Existing root Git deletions predate this work; leave them alone.

## Current baseline

370 cards, 376 examples, 218 quizzes. 300 cards mapped to 107 textbook sections; 70 supplementary comparisons. 152 added cards have no quizzes and currently no word annotations. Existing annotations are sparse. Live content comes from src/data/studyPoints.json, generated from content/base-reviewed.json + content/expansion.tsv (pipe-delimited despite extension) by scripts/assemble-content.py. Book catalog comes from src/data/bookSources.json. Old book*.ts / stream*.ts modules are not live content.

Prior fixes: complete Japanese sentence rendering; deterministic answer/explanation shuffle; seven duplicate question IDs resolved; catalog mappings corrected; desktop/mobile tooltip portal; keyboard search/dialogs; grammar server port5174, separate from Kanji Atlas5173. Four Playwright tests and production build passed before this new task. See REPAIR-REPORT.md for limitations, not a guarantee of linguistic perfection.

## Work order and acceptance criteria

1. **Document and preserve state** — this file. Update status and exact commands/results at each milestone.
2. **Targeted source-page comparison and editorial review.** Read actual explanations, not only contents pages. For each reviewed card retain meaning, attachment, scope, register/person restrictions, a useful contrast, and examples that expose the distinction. Separate a strong tendency from an absolute grammar rule. Correct related quiz explanations and takeaway fields too; do not leave contradicting old text elsewhere. Do not bulk soften legitimate restrictions without evidence.
3. **Reading/meaning data pipeline.** Use local Sudachi morphological analysis for contextual inflected readings plus existing N5–N2 vocabulary dictionaries and reviewed phrase overrides. Prioritize grammar-pattern meanings (に限る = nothing beats / best to), rather than translating its kanji literally. Match dictionary reading to avoid homographs. Never present a kanji component gloss as a word definition. Log uncovered/ambiguous terms; resolve high-frequency and all heading cases manually. Preserve original Japanese exactly. Add source attribution for derived dictionary data.
4. **Reusable annotated-text renderer.** Apply to headings, connection formulas, explanation Japanese, examples, comparisons, quiz prompts/explanations, and tables. Cover catalog/list headings too where feasible without nested interactive buttons. Use exact span segmentation, not greedy replacement that invents readings or drops characters. Existing sentence-specific annotations can override dictionary annotations. Keep punctuation/English untouched.
5. **Book-default display policy.** Add a clear Book/default mode: N5/N4/N3 inline furigana, N2 hover only. Ensure saved old defaults do not silently prevent the requested behavior. Explicit All/Hover/Off preferences may remain user choices; hover meanings should always work. N2 must still expose the reading when hovered. Context must reflect each card's level, including search/catalog results.
6. **Validation.** All heading kanji should have readings and usable glosses. Every example should retain exact Japanese. Review homographs (私, 方, 上, 下, 生, 行う, 人気, 一日, etc.), inflections and grammatical uses. Test に限る at N3 and に限り at N2, source-aware defaults, manual toggles, heading hover, quiz accessibility, no nested buttons or viewport overflow. Retain old regression tests. Run npm.cmd test and npm.cmd run build. Report what was actually checked; structural tests do not prove all linguistic content correct.
7. **Document and deliver.** Record exact source pages checked, edited cards, annotation coverage/unresolved cases, tests and remaining limitations. Keep this file current for handoff. Do not call every textbook page verified unless every page was checked.

## Findings already confirmed in this task

- DeskPane renders point.title, connection and nuance as plain strings. Only SentenceCard used WordHoverTooltip, so headings have no reading/meaning support.
- XはYです card omits the textbook's central point about context allowing topic omission, and noun number/articles. Its formula prematurely combines nouns/adjectives without clarifying their different behavior. Needs a fuller but concise explanation.
- Actual source inspected visually: Genki I printed pp41–42 (PDF49–50): noun+です, context/topic omission, は pronounced わ, particles after noun phrases, noun article/number behavior, question か. Images audit/books/review-g1-49.png and -50.png.
- Actual source inspected visually: SKM N3 printed pp22–23 (PDF45–46): degree comparisons and に限る. に限る attaches to noun / dictionary verb / negative verb and states a subjective best choice. Contrast with restrictive に限り and denial とは限らない. Images audit/books/review-n3-45.png and -46.png.
- Automated scan of baseline found remaining exaggerated absolutes in meanings/takeaways/notes (e.g. 間 is 100% / 間に a single moment; しか always means insufficient; にかけては unmatched supremacy; 末に note says あげく 100% disastrous; honorifics strictly for superiors). Review these substantively.
- Sudachi is installed and usable. It returns 私=ワタクシ in a sample where わたし is preferred, so reviewed overrides/context handling are required. Do not trust its output blindly.

## Sources and tools

Source paths: audit/books/paths.json. PDFs under C:\Users\devyk\Downloads\にほんご. Genki printed page +8 = PDF; N3 +23; N2 +10. PDF skill read this task. PyMuPDF installed; render pages for visual checking. Tesseract and Japanese traineddata were used earlier; see scripts/inspect-bunpou.py.

Local dictionaries: C:\JLPT\kanji-atlas\data\vocab-n5.json through vocab-n2.json. Records have word, reading, meanings, other_forms. Kanji records have character, meanings, readings; do not substitute kanji readings for compound readings. Data NOTICE.md/LICENSE beside them: OpenJLPT with JMdict/KANJIDIC2, CC BY-SA4.0. Preserve attribution and license for derivatives. sudachipy installed with dictionary.

Browser tests: @playwright/test installed locally; Chromium downloaded. npm.cmd test launches isolated Vite5175. npm.cmd run dev serves5174. Previous dev unified exec session51568 may still run. Screenshot capture stalled once; functional browser tests work. Do not claim screenshot review if capture fails.

## Status / next action

- [x] Plan and source-page findings recorded.
- [x] Initial targeted editorial corrections persisted (20 full-card rewrites plus selected summaries; full audit remains in progress).
- [x] Annotation generator + reviewed overrides created. Uses Sudachi, OpenJLPT and extracted JMdict sqlite snapshot.
- [x] Renderer integrated and book-default preference implemented; browser validation still pending.
- [ ] Coverage audit + browser regressions pass.
- [ ] README/repair report and this handoff updated.

Next: make baseline editorial corrections, then build the annotation pipeline and inspect its unresolved-term report before wiring the UI. No implementation changes for this new task have been made yet (only source-page renderings and this plan).

## Continuation checkpoint (in progress)

Source extraction: scripts/extract-source-review.py running in unified exec session48771, 398 pages queued. Cached OCR at audit/source-text. This is evidence gathering, NOT completion of linguistic review.

New files: scripts/deepen-notes.py (already run; persists 20 full-card corrections), scripts/build-annotations.py, content/reading-overrides.json, src/data/annotations.json, src/readingContext.ts, src/components/AnnotatedText.tsx. App uses new reading preference key bunpou_reading_mode_v2 and Book mode default. All/N3 displays ruby; N2 hover only. Manual All/Hover/Off remain. WordHoverTooltip uses a span trigger to avoid nested HTML buttons; passive mode for catalog/search/quiz choices. Examples now render the full sentence through AnnotatedText instead of sparse old tokens.

Dictionary installation jamdict-data failed on Windows file locking. Downloaded its sdist through PyPI and directly decompressed jamdict.db.xz into audit/dictionary/jamdict.db. build-annotations.py queries it read-only. Need add license/provenance and avoid committing huge source database/archive. Upstream ftp.edrdg.org HTTPS had certificate mismatch; do not disable TLS checking.

Known tokenizer safeguards: manually override 富士山→ふじさん, 三千→さんぜん, 一日中→いちにちじゅう; private name readings; potential stems. Do not split inflected words at the auxiliary られ: removed it from pre-split phrase overrides, retaining per-morpheme gloss. Annotation audit should verify the remaining glosses, not only presence.

Last production build passed before latest small fixes. Old browser tests require adaptation because visible ruby text changes textContent. Use data-source-text on AnnotatedText and remove rt when comparing exact Japanese; do not weaken the requirement that complete original Japanese is rendered. New tests must validate book defaults and title hover. No new tests run yet.

User subsequently emphasized proper audits everywhere after identifying the study risk. Acknowledge previous readiness overstatement. Full source/quiz linguistic audit is not yet done; maintain a per-card ledger and do not claim it complete.

## User escalation: example and nuance coverage

User identified another major defect: most cards have only one example despite the books showing several distinct cases. A one-example-per-card summary is NOT sufficient. Rebuild coverage at the **individual use** level: each distinct meaning, attachment variant and relevant restriction gets an explained example; grouped cards need examples for every included pattern. Include contrast pairs where they teach a distinction. Original examples are acceptable; do not bulk-copy textbook exercises. Mere sentence counts are not an acceptance criterion.

Priority now N3: compare actual section explanations and examples. Already read source OCR N3 printed16–17, and visually inspected22–23. Chapter1 omits ところを/ところで/ところへ and the negative-form attachment in change-type うちに. Must add these alongside more examples. Then repeat through N3, Genki and N2. Full-content audit remains incomplete.

## Explicit user correction: ALL content, not only N3

**This requirement applies to Genki I, Genki II, SKM N3, SKM N2, and all supplementary comparison cards. N3 is only the first implementation batch. Do not stop after N3 or describe N3-only enrichment as fulfilling the task.**

For every live card, audit meaning, attachment, important uses, exclusions, register, implied viewpoint, contrasts, Japanese examples, translations, quiz wording, answer uniqueness, and every distractor explanation. Audit comparison tables and hover meanings/readings too. Section presence and automated test passes do not prove instructional accuracy or fidelity.

For every individual grammar use/pattern, provide enough varied, explained examples to cover its meaningful distinctions. A single generic example is inadequate where the book illustrates multiple uses. Grouped cards must cover EVERY included form with its own example(s), or be split into separate cards. Do not pad counts with repetitive sentences. Provide contrast pairs for commonly confused forms, explain what changes between them, and preserve the textbook's essential nuance while removing only material that does not aid understanding or use.

Current example work: content/n3-use-examples.tsv was just created. It contains original varied examples for early N3 chapters, with five pipe-delimited fields: card id | use label | Japanese | English | explanation. **It is not yet wired into assemble-content.py**, so these examples are not live yet. Continue this work for the remaining N3 cards, then every Genki/N2/supplementary card; update the per-card coverage ledger. Do not claim completion from minimum counts alone.
