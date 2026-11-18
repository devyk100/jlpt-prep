# READ FIRST: completion contract for the digital grammar textbook

Owner requirement consolidated 2026-11-17 after repeated supervision failures. This is the authoritative task instruction document for the next implementation model. It supersedes conflicting progress claims in CONTINUE-HERE.md, earlier handoffs and ../AUDIT_PROGRESS_AND_ACTION_PLAN.md. Preserve later explicit user instructions. Read the entire file before editing.

## 1. Deliverable and autonomy

Finish a self-contained grammar learning application covering the substantive grammar instruction in the user's exact Genki I third edition, Genki II third edition, SKM N3 Bunpou and SKM N2 Bunpou PDFs. The user intends to study ONLY from this app. Their objective is faster, sustained study without typing Japanese into dictionaries, consulting separate answer keys, or discovering omissions themselves.

Do the authorized work, verify it and continue through all four books. Do not return after writing a plan, adding a few examples, wiring a table, extracting OCR, or finishing one chapter. Do not repeatedly ask whether to continue. If a genuine external blocker prevents a particular step, state the exact blocker, preserve its pending status, and continue independent work. Do not invent missing evidence. At a session limit, leave an exact continuation checkpoint rather than claim completion.

Keep three experiences: Learn (full teaching), Practice (assessment without answer leakage), Revision (compact summaries/comparisons). A summary is not a substitute for a lesson. Preserve source tables, notes, meaningful examples, contrasts, formation, exceptions, register, perspective, and text-grammar instruction. Remove only genuine redundancy/unrelated content. Do not discard a meaningful distinction as 'low yield' or 'useless'.

## 2. Hard boundaries and prohibited shortcuts

- Work inside C:\JLPT\jlpt-exam-prep. Git root is C:\JLPT. Inspect status first and preserve user changes. Do not reset, clean, force-push, amend user commits, or broadly stage the parent repository. Do not commit/push without authorization.
- Do not edit source PDFs, Kanji Atlas, unrelated projects or system configuration. No unrelated framework migration, dependency upgrade, database deployment or Git LFS repair. Local-network/shared-database work is a later phase, not a reason to delay these repairs.
- No subagents without explicit authorization. Do not replace required source review with another model's unchecked assurances.
- Never claim completeness from chapter/card/example counts, zero unknown tokens, keyword matches, or passing tests.
- Never use generated IDs/chapter metadata as evidence of textbook placement.
- Never soften a test or replace an assertion with a weaker one just to make the suite green. Diagnose product errors first. Legitimate test changes must retain the intended behavioral requirement and have a recorded reason.
- Never silently replace an unavailable chapter's practice with unrelated questions.
- Never mark a source item checked merely because it was authored, OCRed or linked to a section-start page.
- Never remove data needed by the learner just to simplify the UI. Hide optional help through controls instead.
- Do not spend repeated turns optimizing OCR/GPU infrastructure. Reuse existing extraction caches; extraction is an aid, not the deliverable.

## 3. Evidence snapshot: actual supervision findings to reproduce

These observations are dated, not immutable counts. Re-measure current state before fixing; record before/after evidence.

- Live content: 315 cards / 1,063 examples at the latest inspection.
- Practice: 309 questions, all multiple choice: Genki I 144, Genki II 110, N3 40, N2 15. These counts do not establish textbook-equivalent coverage.
- Coverage matrix: 22 rows, no Genki II rows, 11 links to nonexistent live card IDs.
- Browser reproduction: /practice/genki-1/Lesson%201 displayed 1 / 48 because substring filtering included Lessons 10–12.
- Browser reproduction: /practice/skm-n2/Part%201%20%C2%B7%20Chapter%203 displayed 1 / 309 and began with a Genki I self-introduction because no-match fallback returned all exercises.
- Answered a question, refreshed, and the submitted answer disappeared.
- Practice generator coverage: 414 distinct kanji-containing question spans were absent from annotations.json. build-annotations.py scanned lessons/tables but not chapterExercises.json; AnnotatedText requires an exact span match.
- Existing 12 tests passed (58.9 seconds) despite those defects. Build passed WITH a bundle-size warning. The audit document's 'zero warnings' claim was not reproduced.

## 4. Mandatory engineering repairs — complete these before large content expansion

### A. Exact chapter selection and honest unavailable state

Location: App.tsx currentChapterExercises. Replace substring matching with stable exact book+section identity. Display names are not identifiers. Normalize old routes through explicit compatibility mappings if necessary.

Remove fallback to the entire dataset. A missing section displays a clear unavailable/pending message, with optional explicit navigation to available practice. Never show unrelated questions under the requested title. Malformed/unknown routes must not silently impersonate another book.

Acceptance tests:
1. Genki I Lesson 1 contains only Lesson 1 items; no Lessons 10/11/12.
2. N3/N2 Chapter 1 does not include Chapters 10–19.
3. An unavailable chapter displays zero substituted questions.
4. Heading, selected chapter, question ownership and progress denominator agree.
5. Back/forward/direct routes preserve the correct chapter.

### B. Persist practice attempts and assistance accurately

ChapterPracticeView currently stores answers/index in component state. Persist active attempt identity, book/section, exercise IDs, stable option order, answers, reveal state, index, and assistance history. A local versioned storage solution is sufficient now; do not block this on cross-device SQLite work. Recover safely if content changes or stored data is malformed.

Every answer-revealing hint must set an irreversible assisted flag for that attempt, including the ordinary Show Hint button, not only translation hints. Hiding the hint must not erase assistance. Do not classify ordinary non-revealing vocabulary lookup as assistance indiscriminately; classify help according to what the question assesses.

Use a real shuffle with stable option identities. Current alphabetical sorting is not a shuffle. Keep order fixed within/resuming an attempt. Do not require an order change every retry: a valid shuffle can repeat. Restart creates a new attempt without corrupting prior results.

Acceptance tests: answer/reload/resume; leave/re-enter; hint/show/hide/submit; correct and assisted score separation; option/explanation alignment after shuffle; content-version migration; retry reset. Do not expose answers from another attempt.

### C. Make every exercise answerable without optional help

Separate essential task context from optional sentence translation. Hiding the English exposed under-specified items:

- g1-l1-ex-3: スミスさんは留学生（　　）。 Options ですか / ですね / ですよ / でした. Without an explicit task/context, multiple completions work. Supply a situation or instruction that selects the intended meaning; do not call alternatives ungrammatical merely because they are not the intended answer.
- g1-l1-ex-5: 東京は今、午前（　　）時です。 Intended number four appeared only in the hidden English. A reading exercise must visibly specify the written number or target expression.
- g1-l1-ex-2: investigate the rejection of 私は日本語です in the explicit major-selection context. Do not teach that は always creates literal identity or that contextual topic omission is compulsory. Evaluate natural contextual alternatives, then rewrite for uniqueness.

Review ALL questions, not just these IDs. Insert every option into the whole sentence. Review Japanese, necessary context, translation, keyed answer, each distractor explanation and lesson link together. Reject no valid alternative without a stated contextual reason. Distinguish preferred, grammatical, pragmatically odd and impossible. Do not make normal users reveal an 'assisted' hint just to learn the task.

### D. Complete annotation coverage and touch interaction

Include all displayed Japanese in chapter exercises: question, context where applicable, options, feedback and explanations. Include new tables/lesson surfaces. Validate exact reconstruction and kanji coverage; manually inspect contextual meanings separately.

Do not mistake zero unresolved tokens for correctness. Review compound verbs, suffixes, auxiliary forms, counters, dates, homographs and constructions. Known historical failures: 食べ切る interpreted as literal cut; minute 十分 interpreted as sufficient; conditional なら glossed only as 'is'; calendar 上では glossed as after doing.

On phones, tapping a word in an answer option must not submit the answer. Current passive tokens inside option buttons lack an independent tap lookup action. Design separate accessible lookup/selection controls without nested buttons. Confirm with touch-emulated browser tests, not desktop hover alone. Preserve keyboard support. Stylus hover is an optional capability; finger input must work regardless.

A question testing a word's reading/meaning must not reveal the answer through automatic ruby/tooltips without marking explicit help as assisted. Provide exercise-level disclosure policy. Resolve reading level from the active lesson/exercise, not whichever learning card happened to be selected before entering practice.

### E. Correct table placement and table data ownership

Observed live mismatches: potential table attached to added-g2-13-20 (そうです: appearance); volitional table on added-g2-15-24 (ておく); transitive/intransitive table on added-g2-18-30 (てしまう). A related reference may be useful, but it cannot replace primary placement on the actual topic.

The adjective mapping targets nonexistent g1-l5-adjectives; no Genki I Lesson 5 card had the adjective table. Validate every mapping target and table key and fail generation on invalid required links. Review semantic relevance, not only existence.

There are TS and JSON master-table representations. Establish one authoritative source with a reproducible generation path; prevent stale parallel versions from giving different tables in Learn and Revision. Verify the displayed data in both modes.

Audit tables linguistically: verb group exceptions, potential が/を nuance, giving/receiving perspective, conditional restrictions, transitive/intransitive pair limits, honorific roles. Do not turn simplifications into universal rules. Do not shrink tables unreadably on phones; allow contained horizontal scrolling.

## 5. Japanese-first disclosure is mandatory

Keep normal grammar explanations visible. Japanese examples are visible; sentence translations, literal translations and optional explanatory paraphrases start hidden. One Show meaning action reveals only that sentence. Keep literal breakdown separately optional. Revealing a word must not reveal the sentence. Preserve focus/scroll position. Reset disclosure appropriately when changing lessons or starting new exercises, not on every tooltip interaction.

Translation essential to a specific explanatory comparison may be visible in that explanation. Do not use this exception as blanket justification to show every translation. Inspect use labels and notes for accidental paraphrase leakage.

Genki I/II and N3 default to inline furigana; N2 defaults to hover/tap readings. Meaning visibility is independent. Translation hints in practice are optional; necessary task instructions stay visible. After answering, show useful grammatical feedback, but do not automatically force a full translation unless needed for that explanation. Hidden content must also be hidden appropriately from accessibility APIs.

## 6. Source audit method — replaces Plans A/B/C as originally proposed

Use a complete source manifest plus chapter-by-chapter implementation. Extract in the background only where helpful. Start implementation in learning order: Genki I, Genki II, N3, N2. No N2-only 'exam traps' detour as a substitute for the user's foundations.

Manifest must cover relevant teaching pages, tables, notes, review material, chapter exercises, sentence-order/star questions, text-grammar exercises, mock/review assessment and answer keys. Do not assume 55/180 explanation pages defines the scope. Record exact source boundaries and reasons for exclusions.

Reuse the existing OCR under audit/source-text and existing rendered pages. Verify edition/ISBN and printed-to-PDF offsets from the actual files; scan offsets are not guaranteed for online versions. OCR can miss small caution marks, ruby, columns, negation, punctuation and table relationships. Render and inspect uncertain or consequential passages. An automated keyword diff locates candidates; it cannot certify equivalence. Never claim 'guaranteed zero blind spots'.

Distinguish hard formation rules, restrictions on the specific sense, usage tendencies, register preferences and contextual interpretations. The quoted 最中に warning says unforeseen interruptions OFTEN follow, not that all other continuations are prohibited. The quoted ばかりだ warning describes a negative tendency, not a license to reject every other context. Preserve the source's strength of claim. Check the Japanese carefully before writing English rules.

Source-to-app matrix rows must identify a substantive item/use even when no app card exists. Store source pages actually reviewed, formation/restrictions, table requirements, lesson IDs, example IDs, exercise coverage, missing work and evidence. Null/unimplemented links are honest; invented IDs are not. Validate all implemented references. Empty missingWork is not certification. Distinguish section range from pages actually checked.

The current 22-row matrix and 11 broken links must be repaired, then expanded to ALL four books. Existing checked flags require re-examination where evidence is incomplete. Do not initialize newly generated rows as checked.

## 7. Pedagogical structure and coverage

One distinct construction should be clearly identifiable. Related senses can be explicit subsections: うちに A/B can share a lesson with separate instruction/examples/practice. うちに and ようとしている need separate topics. Simultaneous つつ and concessive つつも need distinct teaching at their proper locations and a comparison link. Do not split solely to inflate counts or bundle solely to reduce them.

Every lesson must teach meaning, formation, important uses, exceptions, register/viewpoint, contrasts and prerequisites as applicable. Include original natural examples demonstrating distinct cases. Do not satisfy a minimum count with near-identical sentences. Chapter links/notes must let the learner understand without opening the PDF.

Consolidate duplicates semantically, not by title alone. Preserve unique correct explanations, examples, quizzes and source associations. A useful synthesis is Revision material with links, not a duplicate primary lesson. Inspect deleted/merged content against prior Git data for lost unique instruction; do not restore erroneous material blindly. Preserve/migrate progress and legacy links when IDs change.

Do not infer 'authentic textbook chapter' from a generated ID or assign a plausible section-start reference and call it verified. Locate the actual instruction first. Supplementary material may remain useful but must not impersonate verified book coverage.

## 8. Practice equivalence, not just question counts

Inventory the actual source exercise groups and their instructional purpose. The user's 10–20 recollection is not a fixed quota. Provide sufficient varied practice per chapter and cumulative review across chapters. Do not claim the current 309 multiple-choice questions replace all exercise types.

Implement the formats needed by the sources: contextual choices, conjugation, constrained completion, dialogue, sentence ordering including ★ placement, and passage/text-grammar tasks. Star-ordering must support tap and keyboard; drag is optional. Feedback must show the complete sentence, starred segment and why the ordering works.

For multiple choice, explain every option in context. For written/constrained input accept legitimate variants. Do not claim naive string equality establishes correctness of arbitrary Japanese. Keep target headings/formulas/lesson answer hints hidden before assessment. Guided checks can remain inside lessons but are not the chapter assessment.

## 9. Completion gates and required evidence

Work in complete chapter batches after the engineering blockers in section 4. A chapter is complete only when all are true:

1. Its source manifest and item/use inventory are complete.
2. All substantive items map to actual teaching, required tables and examples.
3. Prerequisites and related topics are accessible without duplicate/confusing primary entries.
4. Every explanation, example and translation has been checked; uncertainty is resolved or explicitly pending.
5. Exercise coverage/format matches the source's instructional breadth, with valid feedback.
6. Readings/glosses and disclosure policies are verified on lesson and practice surfaces.
7. Actual browser navigation, touch lookup, progress persistence and assessment selection pass.
8. Ledger evidence records exactly what was reviewed. No required missing rows remain.

Whole-task completion requires these gates for ALL four books. It does not follow from the sum of sampled checks. Do not call the app 'ready as the sole textbook' while required chapters remain partial. Completed chapters may be identified individually with their evidence.

Run appropriate regression tests and npm.cmd run build. Add tests for the observed failures: exact chapter membership, no fallback, invalid mapping rejection, annotation coverage including exercises, independent translation controls, hint scoring, refresh/resume, touch lookup vs selection, and appropriate reading level in practice. Test content semantics/source coverage separately. Record warnings accurately; do not hide them by changing thresholds solely to claim zero warnings.

## 10. Safe content pipeline and checkpointing

Before edits inspect current scripts and actual file formats. Known authoritative sources: content/base-reviewed.json; content/expansion.tsv (8 PIPE-delimited fields); content/*-use-examples.tsv (5 PIPE-delimited fields); content/reading-overrides.json. Determine and document authoritative chapter-exercise/table sources as part of the repairs. Do not edit generated studyPoints.json alone.

Normal sequence after applicable edits: python scripts/assemble-content.py; python scripts/build-annotations.py; npm.cmd test; npm.cmd run build. Do not blindly rerun historical editorial scripts; they may overwrite later corrections. Run generation validations before claiming the output is live. Keep code/content changes reviewable in coherent batches.

At every milestone record: exact files and source pages reviewed, source items found, defects fixed, test commands/results, open defects, next chapter/item. Maintain a dated execution log and update the source matrix/ledger. Do not overwrite historical reports with success claims; append evidence of resolution. User should not have to discover the next missing lesson or keep prompting.

## 11. Online editions: optional accelerator, not a blocker

Search performed on 2026-11-17 found publisher digital listings:
- GENKI I third edition: https://store.jtpublishing.co.jp/en/products/1730
- GENKI II third edition: https://store.jtpublishing.co.jp/en/products/1732
- SKM N3 grammar digital edition: https://www.3anet.co.jp/np/resrcs/360472/ (publisher labels it paid/registration required).
- SKM N2 official contents/product reference: https://www.3anet.co.jp/np/books/3602/

The GENKI publisher explicitly describes subscription access through its reading website and states that these e-books cannot be downloaded or used offline. Its listing is therefore not a downloadable EPUB source. No suitable downloadable EPUB covering all exact editions was established in this search; SKM N2 grammar's official product page alone does not establish an accessible digital edition. Do not claim an online reader is an extractable EPUB. Verify edition, language, coverage and access format before substituting any source. Public previews/contents can help navigation, not replace full interior review. Do not purchase subscriptions or alter accounts on the user's behalf without authorization. The user explicitly permits proceeding with existing PDFs if better sources are unavailable; do so without delay. Existing files plus OCR/page inspection are sufficient to continue.

## 12. Immediate next actions, in order

1. Read this contract and inspect current Git state; reproduce section 4 failures against current code.
2. Fix exact practice routing/no fallback, attempt persistence, assistance tracking and option ordering; add behavioral regressions.
3. Audit question context/uniqueness, annotation input coverage, exercise disclosure policies and touch selection/lookup separation.
4. Validate table targets and repair placements and canonical table ownership.
5. Repair the matrix links, inventory all source sections, and finish Genki I Lesson 1 end to end as the method-validation batch.
6. Continue autonomously through remaining Genki I, Genki II, N3 and N2 chapters, applying the same gates. Do not stop after the validation batch.
7. Deliver a truthful final evidence summary only after required work is actually done; otherwise provide a precise continuation checkpoint.
