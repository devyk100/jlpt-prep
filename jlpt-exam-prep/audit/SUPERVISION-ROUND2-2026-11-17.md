# Supervision round 2 — 2026-11-17

This is a targeted follow-up, not a complete book audit. Application/content files were inspected without rewriting them. Current live count is 370 cards / 1,180 examples, not the handoff's 1,178. Six browser tests pass (26.5 seconds), including the new counter/quiz regressions; production build passes with a bundle-size warning.

## Confirmed repairs from round 1

- Minute readings in the previously identified 三十分後 and 十分くらい examples now have the correct contextual readings/glosses. Approximation くらい is no longer glossed as dark in that sample.
- The に応じて quiz now tests salary determined according to experience/ability, with an aligned translation and distractors that do not reproduce the prior adverbial/attributive ambiguity.
- The comparison example was rewritten with nominalization.
- Form review C now includes negative conjecture, simultaneous つつ, concession つつも, にせよ and べき examples. The former simultaneous label on the つつも example was corrected.
- Ledger evidence notes are more specific, and most entries are partial. These are improvements, but checked labels still cannot be accepted without source-complete verification.

## High priority: a purportedly checked source section is materially incomplete

Card `added-n2-p3-10-150` is marked checked in every applicable ledger dimension, has missingUses=[], and claims inspection of SKM N2 printed pp.186–187 / PDF pp.196–197. I visually inspected those actual pages in this round. Evidence images: `audit/books/supervision2-n2-p186.png` and `audit/books/supervision2-n2-p187.png`.

The source section explicitly organizes connectors by discourse function and teaches the following groups. Use this as the beginning of a source-derived inventory, not as a substitute for reading the explanations/examples:

| Function | Expressions on these source pages |
| --- | --- |
| Add points | しかも、そのうえ、さらに、そればかりか、そればかりでなく |
| Compare | それに対して、一方 |
| Alternative possibility / question choice | あるいは、それとも |
| Result, conclusion, response, ensuing event, synthesis | そのため、したがって、そこで、すると、このように、こうして |
| Reason/background | なぜなら、というのは |
| Contrary to expectation / persistence | だが、ところが、それなのに、それでも |
| Restatement, summary, analogy | つまり、要するに、いわば |
| Exception/qualification/supplement | ただし、もっとも、なお |
| Move discussion forward / change subject | さて、ところで |

The app card explains only しかも、ただし、それでも、したがって、すなわち. Adding examples for that existing five-item list did not audit the source section. For example, the difference between あるいは and それとも, between そこで and すると, and between さて and ところで is instructional content, not disposable repetition.

A search of all live cards' title/meaning/connection/nuance/takeaway fields found no mentions of あるいは、それとも、このように、こうして、というのは、要するに、いわば、もっとも、なお. Hits for すると/さて/ところで were unrelated compound patterns such as とすると, はさておき and temporal ところで. A raw substring hit therefore cannot establish connector coverage. This search does not assert absence from every incidental sentence or separate UI table; it establishes that the checked card does not supply the source instruction and the current ledger does not map equivalent instruction elsewhere.

**Required repair:** reopen this card's overall/source/coverage status. Inventory all source uses above, inspect their distinct explanations on p.187, and create appropriate linked cards or sections with explanations and use-specific examples. Map any genuinely equivalent existing coverage explicitly. Preserve useful すなわち material as additional content; do not use it to stand in for missing source items. Do not mark checked after merely reaching a target number of examples.

## Form review C still needs completion before certification

The earlier source image of printed p.126 explicitly includes progressive つつある and conjectural ではあるまいか, as well as the other classical-form families. `added-n2-c-118` still omits these from its own explanation/use examples, and its ledger supplies no cross-link to coverage elsewhere. The app may cover some elsewhere; the review must identify and link that coverage rather than silently omit it. Check all rows of the source table. The new example `この空模様では、今夜の雨は降るまい。` also deserves naturalness revision: `今夜は雨が降るまい` is clearer for the intended weather conjecture.

## Contextual hover problems remain beyond the specifically patched sentences

From current generated annotations:

- `一人で全部食べ切りました`: 切り is glossed "to cut" although 食べ切る here means finish eating/eat all. Annotate the compound or its completion suffix appropriately.
- `一人でできるものなら`: なら is glossed "copula/linking form: is"; this conditional construction needs an if/conditional meaning, preferably as a grammar phrase.
- `暦の上では立春とはいうものの`: 上で is glossed "after doing; in doing," but this is "according to/on the calendar". The same spelling has multiple grammatical uses.

These are counterexamples to treating dictionary matches or zero unresolved entries as adequate hover verification. Audit compound predicates, conditional forms and context-sensitive phrases throughout, including Genki, rather than adding only the exact previous failing strings.

## Next model's execution requirements

1. Read this report and the actual source pages. Reopen the affected checked entries; do not keep claiming the supervision findings are completely addressed.
2. Start the source-to-app matrix with the connector section above. For each source use, record exact pages, card IDs, explanation location, example IDs, contrast/restriction checks, and missing work. Do not generate the matrix solely from existing cards or use labels.
3. Extend the same source-first method to every section of all four books, including Genki I. New textbook items with no current card must appear as missing matrix rows.
4. Fix and test contextual hover handling beyond hardcoded sample strings. Preserve exact Japanese text and source-aware display defaults.
5. Reconcile live counts and ledger example IDs after assembly. Report checked pages/uses and remaining work, not a blanket completion claim based on automated checks.

Verdict: the previous concrete fixes mostly landed, but substantive textbook coverage and semantic annotation correctness remain open. The newly checked connector card is a clear failure of the user's no-loss requirement.
