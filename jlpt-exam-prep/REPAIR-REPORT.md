# Repair report — 17 November 2026

The original app displayed 59 cards. Another 163 textbook cards existed in source files but were not loaded. Four entries without support in the inspected book sections were excluded from the revised baseline; they remain recorded in `audit/excluded-unsubstantiated.json`. The revised app combines 218 baseline cards with 152 additions.

## Content and catalog

- Replaced the broken mixed catalog with exact book membership and ordered section mappings. Genki II is no longer accidentally included under Genki I.
- Corrected misplaced entries, including Genki すぎる (lesson 12), SKM N3 のだから (5), ようにする (11), べき (10), and SKM N2 かねる (18), ものの (14), だけに (17), に違いない (22), ざるを得ない (25).
- Unsubstantiated book assignments are supplementary notes, without a textbook page claim.
- Added concise notes for missing Genki grammar, SKM patterns, form reviews, sentence construction and passage-level grammar. All 107 catalog sections have content.
- Corrected targeted false absolutes and misleading explanations about ので requests, 最中 interruptions, あまり, あげく, conditional clauses, giving/receiving, intention and nominal modification. Reworked malformed or ambiguous quiz items identified in the audit. The transformation is recorded in `scripts/review-content.py`.
- Removed the inaccurate README claim of 125 points being 100% verified. Coverage is section-level and includes grouped patterns; it is not proof that every textbook subpoint is individually covered.

## App behavior

- Renders the entire Japanese sentence, preserving unannotated text and punctuation.
- Keeps shuffled options, correct answers and explanations aligned; formerly every correct answer occupied the first position.
- Namespaces seven colliding legacy quiz IDs to avoid merging unrelated weak points. Old flags retain their first legacy match; ambiguous historical intent cannot be reconstructed.
- Keeps full Japanese/comparison titles; fixes Ctrl/Cmd+K search and resets the study pane on navigation.
- Hover cards use a viewport-constrained portal, keyboard focus and click support. Clicked cards remain open until dismissal. Internal tooltip scrolling stays usable.
- Dialogs support Escape, keyboard focus containment and return focus to the previous control. Catalog cards are actual buttons.
- Improves narrow-screen layout and separates grammar port 5174 from Kanji Atlas port 5173.

## Verification

Playwright tests cover all catalog references, unique sentence/quiz IDs, exact reconstruction of every Japanese example, deterministic shuffle alignment, all four correct-answer positions, browser catalog navigation, keyboard search, desktop/mobile tooltip placement, and runtime errors on the tested flows. TypeScript and Vite production build pass. Lint has no errors, with legacy/style warnings documented by its output.

Sources inspected are the local Genki 3rd edition and SKM Bunpou PDFs. OCR and rendered table-of-contents evidence remain under `audit/books`; the earlier findings are in `../kanji-atlas/EXAM-PREP-AUDIT.md`. No claim is made that automated checks validate every linguistic nuance. Added cards currently provide original notes and examples without new multiple-choice questions or complete word annotations.
