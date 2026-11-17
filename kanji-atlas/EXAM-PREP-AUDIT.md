# Bunpou Atlas / jlpt-exam-prep audit — 16 November 2026

**Result: the project builds, but it is not ready to be treated as a verified Genki / SKM grammar reference.** The most serious problems are inaccessible textbook content, incomplete displayed Japanese, ambiguous quiz marking and inaccurate absolute rules. No files in `C:\JLPT\jlpt-exam-prep` were edited. Findings and build output are stored here instead.

## Scope and checks

Read the application, component logic, data aggregation, textbook catalog and generation scripts. Bundled the TypeScript data in memory to examine all 59 live points and all 163 separate textbook points. Checked IDs, catalog references, sentence/token agreement and live quiz option/explanation consistency. Read the live grammar rules and quizzes for semantic problems. Compared selected disputed claims and coverage against the actual supplied Genki and SKM **Bunpou** scans, separately from the kanji audit. This does **not** certify every sentence or every explanation in the 163 dormant textbook records; those need a further line-by-line editorial pass before activation.

TypeScript checking passed (`tsc -p tsconfig.app.json --noEmit --incremental false`). Vite production build passed, with its output redirected to this folder. A browser preview confirmed the 59-point count, truncated first sentence, empty/misassigned textbook sections and broken Ctrl+K shortcut. These are observed defects, not assumptions based on the producing model.

## 1. High: textbook datasets are absent from the live app

`src/data/grammarData.ts:13` aggregates only the ten stream arrays. `bookGenki1.ts`, `bookGenki2.ts`, `bookSkmN3.ts`, and `bookSkmN2.ts` are not imported. The live app exposes 59 points: N5=8, N4=11, N3=20, N2=20. Separate textbook files contain 32+26+47+58=163 records, none loaded through this aggregator. This is not necessarily 222 distinct grammatical constructions: multiple records overlap in topic.

`BookCatalogModal.tsx:84` silently returns null for missing IDs. Consequently:

| Catalog tab | Referenced entries | Actually available | Missing references |
|---|---:|---:|---:|
| Genki I | 77 | 19 | 58 |
| Genki II | 37 | 11 | 26 |
| SKM N3 Bunpou | 67 | 20 | 47 |
| SKM N2 Bunpou | 78 | 20 | 58 |

Counts are per tab, so shared references are counted more than once. Repair by choosing a canonical dataset, reconciling duplicate topics and validating every catalog ID. Simply importing the dormant files would expose the sentence defects described next.

## 2. High: displayed Japanese is incomplete

`SentenceCard.tsx:34` displays only `sentence.tokens`, whereas audio uses the full `sentence.japanese` and translation comes from `sentence.english`. Seven of 64 live examples differ after punctuation and whitespace normalization. Examples:

| Point | Full Japanese | Text actually displayed |
|---|---|---|
| genki1-wa-desu | 私はカリフォルニア大学の留学生です。 | 私は留学生です |
| genki1-te-iru | 姉は東京のIT企業に勤めています。 | 姉は東京勤めています |
| genki2-kanoukei | 漢字が難しくて、新聞をすらすら読むことができません（読めません）。 | 漢字新聞読めません |

The second and third examples remove grammatical connections. Every one of the **164 examples in the dormant textbook files** also fails this reconstruction check. Their token lists are vocabulary highlights, not complete tokenization. Keep the complete Japanese visible and map annotations to spans, or supply a complete token sequence. Do not activate those files unchanged. All seven live mismatches are retained in `data/exam-prep-audit/structural-report.json`.

## 3. High: quizzes can reject defensible answers

These require rewriting, not merely changing the answer index:

- `streamContrasts.ts:101–114`, わりに/にしては: option `のわりに` already supplies の, yet the rejection says the prompt lacks の. Inserting that option produces precisely the `半年のわりに` form the explanation calls for. Add context that genuinely distinguishes the alternatives, or accept both.
- `streamCausality.ts:189–209`, おかげ/せい: the prompt already ends in `騒音の`, so option `ために` produces `騒音のために`. The rejection acknowledges this grammatical form. Blame is a useful nuance, but the existing sentence does not make the neutral causal option ungrammatical. Use a distractor that is actually invalid for the intended question.
- `streamModality.ts`, はず quiz: the explanation explicitly admits `であるはず` is grammatically possible, then marks it wrong for formality without specifying a register requirement in the prompt.
- `streamTime.ts`, とき quiz: the explanation assumes a departure airport, but the prompt only says an airport duty-free shop. A destination/return context is not excluded. State the timing explicitly before contrasting 行く and 行った.

All 59 live questions have four options and structurally consistent answer flags/explanation ordering. Those structural checks pass; they do not establish that only one option is linguistically acceptable.

## 4. High: overgeneralized grammar rules

- `streamCausality.ts:12` says commands/invitations such as てください require から. This blanket rule is false: ので can soften a request. The [Japan Foundation explanation of ので](https://www.jpf.go.jp/j/urawa/j_rsorcs/textbook/setsumei_pdf/setsumei16_5.pdf) explicitly discusses volitional second clauses and gives a polite request example. The project's dormant Genki record also describes ので as suitable for polite requests, contradicting the live rule.
- `streamTime.ts:247` says 最中に **always** implies interruption and the second clause **must** be an unexpected event. Supplied SKM N2 Bunpou, printed p.12 / PDF p.22, says that such a continuation is **often** used. Preserve that frequency distinction. Its definition is being right in the middle of an action; interruption is not the definition itself.
- Several other live claims deserve editorial review, including emotion-only あまり, categorical rejection of おられます, overly rigid には/に限って contrasts and precise percentage ranges for かもしれない. They are not independently certified by this audit. Do not turn stylistic tendencies into universal grammatical prohibitions.

## 5. High: quiz scores can be gamed without learning

Every live quiz uses `correctIndex: 0`: selecting the first option gives 59/59. Dormant files also strongly favor the first option (159 of 163). `QuizCard.tsx` preserves source option order. Shuffle options together with their explanations using stable question-level mappings, or balance answer positions in authored data. Verify meaning and distractor quality before randomization.

## 6. Medium: book attribution and chapter mapping are unreliable

`scripts/map_books.py:54` uses `'Genki I' in book`, which also matches **Genki II**. The generated Genki I catalog consequently contains lessons 13–23. Browser inspection confirms those headings and Genki II entries appear under Genki I. Use exact identifiers, not substring matching.

`bookGenki1.ts:2301–2306` places すぎる in lesson 11. The supplied Genki I third-edition contents, printed p.10 / PDF p.18, and explanation, printed p.278 / PDF p.286, place it in **lesson 12**. The same contents include ほうがいいです, which has no dedicated live point or Genki I book record. Thus even fixing imports would not establish complete book coverage.

Some SKM-associated live points have no book/chapter metadata and get assigned from their level by the generator. A JLPT level is not evidence of membership in a particular textbook. SKM N3 and N2 contents include sentence-composition and discourse grammar sections beyond the thematic point selections. The README's complete/canonical coverage impression is therefore unjustified. Build an explicit book/page/section mapping and a missing-content ledger before claiming completeness.

## 7. Medium: advertised search shortcut closes search

`SearchModal.tsx:34–36` calls `onClose()` on Ctrl/Cmd+K, even when closed. No corresponding opening handler exists in Topbar/App. Browser test confirmed Ctrl+K leaves search closed. Move the shortcut to the owner of `isSearchOpen` and toggle/open there; retain Escape for closing.

## 8. Medium: hover accessibility and positioning

`WordHoverTooltip.tsx` uses non-focusable spans without keyboard focus handlers. Keyboard-only users cannot reach the word annotations. Click toggles visibility without calculating coordinates; `coords` starts at (0,0), so touch interaction without a preceding mouse-enter can position a tooltip offscreen. Positions are not clamped to viewport edges. The Off mode hides ruby but still reveals reading inside an opened tooltip; clarify whether that matches the intended preference. These are source-level findings; touch behavior was not device-tested.

## 9. Lower priority: labeling and launch behavior

`SidebarPane.tsx:148`, `SearchModal.tsx:111` and `BookCatalogModal.tsx:97` use `title.split(' ')[0]`, producing labels such as **The**, **Giving**, and **X**, obscuring the grammar being navigated. Supply a dedicated short Japanese title.

`start-platform.bat` opens port 5173 before Vite starts. If that port is occupied (for example by Kanji Atlas), Vite may choose another port and the browser opens the wrong app. Specify a distinct strict port and open the actual ready server address. This collision is a predictable launch issue, not a tested alteration of the user's running server.

## 10. Documentation overstates verification

`README.md:9` claims 125 points and “100% verified.” Neither the live count (59) nor separate textbook-file count (163) matches 125. The data and language defects above contradict the verification claim. Replace it with measured scope, source/page references, actual counts and known gaps.

## Evidence and repair order

1. Reconcile canonical data and catalog mappings; create explicit textbook coverage records.
2. Preserve complete Japanese and correctly align hover spans.
3. Edit rules and ambiguous questions against source pages; review dormant content before importing it.
4. Balance/shuffle answers, repair search and tooltip accessibility, then retest persistence and navigation.
5. Update claims only after the content review is complete.

Machine artifacts: `snapshot.json`, `structural-report.json`, `all-data-stats.json`, `live-content.txt` and a separately built preview under `data/exam-prep-audit/`. Reproduce live structural checks with `node scripts/audit-exam-prep.mjs` from this project. PDF screenshots used for checking remain locally in that audit directory; they are not shipped in the application bundle.

Sources inspected: `C:\Users\devyk\Downloads\にほんご\Genki (N5)\Genki Textbook 1 - 3rd Edition.pdf`; the SKM N3 `Shin_Kanzen_Master_N3-Bunpou.pdf` and N2 `Shin_Kanzen_Masuta_N2-Bunpou.pdf` in their respective folders. Genki II's dormant dataset was structurally checked, but its entire textbook was not page-by-page reconciled in this grammar audit. No exhaustive semantic certification is claimed.
