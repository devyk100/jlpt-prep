# Supervision review — 2026-11-17

Scope: independent, targeted review of the current files after the subsequent model's enrichment. This is a sample review, not a full audit of the four books. No content or application code was changed during this supervision pass; findings are left explicit for repair. Git remains uncommitted; existing work is preserved.

## Confirmed progress

- Live data contains 370 cards and 1,173 examples, matching the updated handoff. N2 and supplementary enrichment are now present.
- Ledger contains 370 entries: 41 checked, 324 partial, 5 pending. These are recorded labels, not independent certifications.
- Generated annotations reconstruct every stored Japanese span exactly (zero mismatches). This checks text preservation, not meaning/reading accuracy.
- Production build passed; bundle-size warning remains. All five Playwright browser tests passed (23.0 seconds). The linguistic defects below survive these functional tests, demonstrating why source and semantic review remain necessary.

## Findings that block accepting linguistic completion

### 1. Incorrect contextual readings and meanings remain despite zero unresolved terms

Evidence: `src/data/annotations.json`:

- `三十分後には着くと思います` splits 三 + 十分 and assigns 十分 `じゅうぶん`, meaning sufficient. Here 三十分 is thirty minutes (`さんじゅっぷん` or `さんじっぷん`), not sufficiency.
- `駅まで十分くらいかかります` assigns 十分 `じゅうぶん` and くらい "dark; gloomy". Here the meaning is approximately ten minutes: 十分 `じゅっぷん`/`じっぷん`, くらい approximation.
- `十分じゅっぷん` also annotates its 十分 portion as `じゅうぶん`, contradicting the reading printed next to it.

Required repair: handle contextual counters and grammatical particles, inspect all occurrences of affected forms, regenerate annotations, and add regression checks distinguishing minute expressions from sufficient/enough. A global override for 十分 is insufficient. Do not certify a reading merely because its dictionary lookup returns a value.

### 2. Repaired N2 quiz still has an acceptable distractor and a stale translation

Card `skm2-c9-ni-oujite`, quiz `q-skm2-9-2`: the sentence offers training menus according to the customer's age/fitness. Option 応じて is marked wrong because it supposedly must modify the following noun. However, in the complete sentence, `年齢や体力に応じてトレーニングメニューをご提案します` can modify ご提案します adverbially. There is no stated constraint forcing attributive modification. This defeats single-answer grading.

Its English still says "We will make a plan suited to the budget," which does not match the rewritten Japanese.

Required repair: rewrite the item so the intended answer is uniquely required, evaluate all options in the whole sentence, and update the translation and every explanation together. Do not declare 応じて ungrammatical solely because a noun follows it.

### 3. Supplementary comparison example contradicts its own formula

`content/supp-use-examples.tsv`, card `skm3-u4-ni-kurabete`, use label "Comparison of options": `電車で行くのは、車で行くに比べて時間が正確だ。`

The note teaches verb clause + のに比べて, but the sentence omits の after 車で行く; its punctuality wording is awkward too. Repair the whole sentence naturally, preserving the intended comparison (for example, nominalize both modes of travel and compare predictability of arrival time). Inspect the other new examples instead of assuming labels establish grammatical correctness.

### 4. Grouped N2 coverage is still incomplete, and one use label is misleading

Visually inspected SKM N2 printed p.126 / PDF p.136; rendered evidence: `audit/books/supervision-n2-p126.png`. This source page contrasts old forms, including both negative conjecture and negative intention with まい, simultaneous/concessive/progressive uses of つつ-related patterns, and にせよ. It also includes べし-derived forms.

Card `added-n2-c-118` names ず・ざる・まい・つつ・せよ but has no せよ example. Its new まい example demonstrates determination only. Its example `将来の進路について悩みつつも、日々の勉強を続けている。` is labeled "Formal simultaneous action" although つつも here expresses concession. The original source distinguishes those functions.

Some forms may be taught elsewhere in the app; that does not excuse a grouped review card silently omitting the distinctions it claims to review. Either provide the missing use explanations/examples or explicit links to complete coverage, and verify against the source-to-app matrix. Check べし-derived forms too rather than relying on the shorter app heading.

Another sampled grouped card, `added-n2-p3-10-150`, has two ただし examples and one したがって example. This sample is not proof that the source's complete connector coverage is represented. Inspect the actual source pages and inventory all connectors before closing that section.

### 5. Ledger evidence does not support its certification claims

All 41 checked entries use the same generic evidence note claiming direct visual/OCR inspection. The ledger stores section-start references but no exact reviewed-page field, source-derived use inventory or use-to-example mapping. Partial entries routinely mark examples/translation/reading checked, while the sampled defects above remain.

This does not prove no review occurred; it means the stored evidence cannot substantiate the claimed review. Do not use the 41 checked entries as a reliable completion total. Attach actual page evidence and item-level checks, reopen affected dimensions, and distinguish "authored/enriched" from "independently checked". An empty missingUses list must not mean complete unless the source inventory was actually compared.

## Required next work

1. Repair the concrete sentence, quiz and annotation defects above, and add meaningful regressions.
2. Build the source-to-app coverage matrix for ALL four books, including notes, review tables and text-grammar sections. The user's standard is substantive coverage no less than the books, not the presence of every chapter or an average example count.
3. Reconcile ledger statuses with evidence; retain uncertainties explicitly. Inspect all new batches, especially grouped forms and repeated claims of exclusivity/absolute restrictions.
4. Regenerate live data and annotations, rerun tests/build, and report exactly what has been checked and what remains.

Verdict: substantive progress, but not acceptable as a completed grammar-accuracy or textbook-equivalence audit.
