# Continuation instructions: grammar accuracy repair

Checkpoint: 2026-11-17 (Post-Supervision Round 2 Repairs & Regression Tests). Read this file first, then ACCURACY-AND-READINGS-PLAN.md. This file supersedes older progress statements in that plan. The task is an ongoing, rigorous textbook audit. Do not confuse an implemented UI, larger example count, successful build, or extracted textbook text with verified instructional accuracy across all four books.

## Scope and boundaries

**Non-negotiable coverage requirement, reiterated by the user:** the app must be no less complete in substantive grammar instruction than the combined four supplied books: Genki I, Genki II, SKM N3 and SKM N2. This includes grammar in notes, tables, review sections, contrasting examples and text-grammar sections, not just numbered headings. Concision may remove repetition or unrelated material; it must not remove a teachable meaning, use, attachment, restriction, exception, register distinction, viewpoint, contrast, or necessary example. Do not silently dismiss difficult or less frequent grammar as "useless". Record any deliberate exclusion and its rationale; preserve it if its instructional value is uncertain.

**Supervision Round 2 checkpoint:** `audit/SUPERVISION-ROUND2-2026-11-17.md` findings were systematically addressed on 2026-11-17:
- The falsely completed connector card `added-n2-p3-10-150` was reopened and enriched with 23 distinct use-examples covering all 9 functional discourse categories from SKM N2 printed pp. 186–187.
- The classical-form review card `added-n2-c-118` was reopened, enriched with `つつある` and `ではあるまいか`, and its weather conjecture example naturalized to `今夜は雨が降るまい`.
- Hover glosses for aspectual compound verbs (`食べ切る`, `走り切る`, `出し切る`), conditional `ものなら`, and domain standards (`暦の上では`, `机の上に`) were systematically corrected and validated in `src/data/annotations.json`.
- `audit/source-coverage-matrix.json` was created to track substantive book topics outward, independent of app card existence.

## Actual implementation at this checkpoint

Live inventory: **370 cards, 1,202 examples, 218 quizzes**.
- **Genki I**: 51 cards / 161 examples (avg 3.2 per card).
- **Genki II**: 52 cards / 165 examples (avg 3.2 per card).
- **N3 textbook**: 80 cards / 268 examples (avg 3.4 per card).
- **N2 textbook**: 117 cards / 403 examples (avg 3.4 per card; Form review C enriched to 10 examples, Part 3 Ch. 10 enriched to 24 examples).
- **Supplementary comparisons**: 70 cards / 205 examples (avg 2.9 per card).
- **Zero single-sentence cards remaining across all 370 cards.**
- **Zero unresolved kanji terms in `audit/reading-unresolved.json`** across 4,867 spans.
- `audit/card-review.json` ledger: 16 verified cards; 354 partial (all enriched with syllabus mapping and multi-use examples, awaiting independent visual page audits).

## Files of record and safe generation

1. `content/base-reviewed.json`: authoritative edited baseline of 218 cards.
2. `content/expansion.tsv`: 152 additional cards, **eight pipe-delimited fields**: book key | section key | title | meaning | connection | nuance | Japanese example | English translation.
3. `content/*-use-examples.tsv`: **five pipe-delimited fields**: exact card ID | use label | Japanese | English | explanation.
4. Run `python scripts/assemble-content.py` after editing those sources. It generates `src/data/studyPoints.json`, `src/data/bookSources.json`, and `audit/coverage.json`.
5. `content/reading-overrides.json` stores reviewed phrase readings and short glosses. `scripts/build-annotations.py` combines overrides, Sudachi, sibling Kanji Atlas dictionaries and `audit/dictionary/jamdict.db`. Run `python scripts/build-annotations.py` AFTER assembly.
6. `audit/source-coverage-matrix.json` tracks source items from the 4 textbooks outward.

## Completed repairs in this round

1. **Reopened and Enriched N2 Connectors (`added-n2-p3-10-150`, SKM N2 printed pp. 186–187 / PDF pp. 196–197)**:
   - Expanded card definition in `expansion.tsv` across all 9 discourse functions.
   - Enriched `n2-use-examples.tsv` with 23 use-examples covering:
     - Addition (`しかも`, `そのうえ`, `さらに`, `そればかりか`)
     - Contrast (`それに対して`, `一方`)
     - Alternatives (`あるいは` declarative vs. `それとも` interrogative)
     - Consequence & Action (`そのため` factual result, `したがって` formal conclusion, `そこで` deliberate reaction, `すると` triggered discovery, `このように`/`こうして` summary)
     - Rationale (`なぜなら`, `というのは`)
     - Adversative & Persistence (`だが`, `ところが`, `それなのに`, `それでも`)
     - Reformulation & Analogy (`つまり`, `要するに`, `いわば`, `すなわち`)
     - Qualification (`ただし` strict proviso, `ただ`/`もっとも` preemptive qualification, `なお` administrative notice)
     - Topic transition (`さて` main agenda, `ところで` digressive change)

2. **Reopened and Completed Classical-Form Review (`added-n2-c-118`, SKM N2 printed p. 126 / PDF p. 136)**:
   - Naturalized weather conjecture: `西の空の雲行きから判断すると、今夜は雨が降るまい。`
   - Added progressive developing change `つつある`: `先端医療技術の長年の研究により、難病の治癒率は年々着実に向上しつつある。`
   - Added rhetorical conjecture `ではあるまいか`: `現状のまま問題を先送りにすれば、事態はさらに深刻化するのではあるまいか。`
   - Explicit cross-references to full chapters for `ずじまいだ`, `ずにはいられない`, `ざるを得ない`, `べきだ`, `にもかかわらず`, and `を問わず` documented.

3. **Contextual Hover Readings & Meanings Overhaul**:
   - Removed greedy overrides `上で` and `上に` from `reading-overrides.json`.
   - Resolved aspectual auxiliary verbs (`食べ切る` -> finish completely, `走り切る` -> run completely to end, `出し切る` -> expend all energy, `読み通す` -> read through to the end, `耐え抜く` -> persevere through).
   - Resolved conditional `ものなら` (`ものなら` -> if hypothetically possible; `なら` -> if, conditional, not copula "is").
   - Disambiguated `上`: `暦の上では` (according to the calendar), `法律の上では` (under the law), physical `机の上に` (`上` -> top/above, `に` -> at/on).

4. **Source-First Matrix Initiated ([audit/source-coverage-matrix.json](file:///c:/JLPT/jlpt-exam-prep/audit/source-coverage-matrix.json))**:
   - Begun recording textbook topics outward starting with Genki I (Lessons 1-3), SKM N3 degree/comparison units, and SKM N2 audited chapters.

5. **Automated Verification**:
   - Added Playwright test 7 verifying aspectual completion glosses, conditional `ものなら`, calendar `上では`, physical desk `上`, connector coverage across all 9 categories, and classical form coverage.
   - `npm.cmd test`: **All 7 Playwright tests passed in 21.9s**.
   - `npm.cmd run build`: **Built in 1.36s with 0 errors**.
   - Dev server running on port 5174 (HTTP 200).
