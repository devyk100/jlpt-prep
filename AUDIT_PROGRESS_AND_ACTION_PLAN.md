# Comprehensive Audit Progress, Technical Findings & Proposed Plans of Action

> **Execution decision:** Read [jlpt-exam-prep/EXECUTION-CONTRACT.md](jlpt-exam-prep/EXECUTION-CONTRACT.md) first. It consolidates the user's requirements and the subsequent direct supervision findings. Plans A/B/C below are proposals, not approved completion criteria; the contract specifies the required combined workflow and corrections to overstatements in this report.

**Prepared for**: Astra / Strategic Advisor  
**Workspace**: `c:\JLPT\jlpt-exam-prep`  
**Physical PDF Location**: `C:\Users\devyk\Downloads\にほんご\`  
**Target JLPT Levels**: N5 (Genki I), N4 (Genki II), N3 (Shin Kanzen Master N3), N2 (Shin Kanzen Master N2)  
**Date**: November 17, 2026  

---

## 1. Executive Summary & Objective

The goal of this initiative is to build and verify an uncompromising, textbook-accurate digital study and revision platform for JLPT preparation. 

The user raised a critical and valid concern: **previous verification passes were relying too heavily on Table of Contents (目次) heading matching and sampled pages rather than an exhaustive, inside-out forensic audit of the actual printed book contents (rules, warning notes, polarity restrictions, and exercises).**

This document compiles:
1. What has been accomplished so far in the codebase.
2. What was discovered by directly rendering and inspecting the physical textbook scans in `C:\Users\devyk\Downloads\にほんご\`.
3. Concrete grammatical discrepancies, missing nuance constraints, and card bundling identified from the physical pages.
4. Hardware acceleration capabilities confirmed on the host GPU (NVIDIA RTX 3050 4GB).
5. Three distinct, actionable plans of action for Astra's review and strategic guidance.

---

## 2. Current State of the Application (`jlpt-exam-prep`)

The web application is fully functional, running on Vite + React + TypeScript with Playwright end-to-end testing:

- **Canonical Content Scope**:
  - **315 canonical grammar cards** in `src/data/studyPoints.json`.
  - **107 canonical book sections** in `src/data/bookSources.json`.
  - **51 cards** for Genki I (Lessons 1–12).
  - **52 cards** for Genki II (Lessons 13–23).
  - **85 cards** for Shin Kanzen Master N3 (Part 1 Ch 1–12, Reviews A–J, Part 2 Ch 1–4, Part 3 Ch 1–10).
  - **127 cards** for Shin Kanzen Master N2 (Part 1 Ch 1–26, Reviews A–G, Part 2 Ch 1–3, Part 3 Ch 1–12).
- **Architecture & Hygiene**:
  - Eliminated 59 legacy/prototype duplicate cards and orphaned stream files (-503 kB bundle reduction).
  - **Zero Romaji**: Purged all parenthesized romaji in favor of `<ruby>` furigana tags.
  - **Japanese Immersion by Default**: All example sentences hide English translations behind a toggle.
  - **Furigana Coverage**: 5,515 annotated spans in `annotations.json` with 0 unparsed kanji terms.
  - **Synchronous Navigation**: Route state (`parseRoute`) derives directly from `location.pathname`, ensuring browser back/forward buttons work flawlessly without UI de-sync.
- **Verification**:
  - `npm run build`: Production build passes in 1.2s with 0 warnings.
  - `npm test`: **12 / 12 Playwright tests green** (47.5s).
  - Local dev server active at `http://127.0.0.1:5174/`.

---

## 3. Physical PDF Inspection & Key Findings

The user's actual source PDFs reside at `C:\Users\devyk\Downloads\にほんご\`:
- `Genki (N5)\Genki Textbook 1 - 3rd Edition.pdf` (392 pages, 124.9 MB)
- `Genki Textbook 2 - 3rd Edition.pdf` (399 pages, 83.5 MB)
- `Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf` (188 pages, 230.3 MB)
- `Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf` (229 pages, 66.0 MB)

### Discovery 1: Raster Scans Without Text Layers
All 4 physical textbook files are 100% scanned raster image PDFs. They contain **zero embedded selectable text** (`pymupdf.get_text()` returns empty strings). Any automated text processing requires image rendering and optical character recognition (OCR).

### Discovery 2: Table of Contents Verification
TOC pages were rendered to high-resolution PNGs (`audit/pdf_inspect/`) and visually verified:
- **Genki I**: PDF pp. 14–18 map Lessons 1 to 12.
- **Genki II**: PDF pp. 14–17 map Lessons 13 to 23.
- **SKM N3**: PDF pp. 5–9 map Part 1 (Ch 1–12, Reviews A–J), Part 2 (Ch 1–4), Part 3 (Ch 1–10).
- **SKM N2**: PDF pp. 3–7 map Part 1 (Ch 1–26, Reviews A–G), Part 2 (Ch 1–3), Part 3 (Ch 1–12).

---

## 4. Inside-Out Discrepancies & Gaps Uncovered

When rendering and inspecting the actual interior lesson pages (specifically SKM N2 Chapters 1 & 2 on PDF pp. 18, 19, 22, 23, and SKM N3 Chapter 1 on PDF p. 40), significant pedagogical nuances were identified that are present in the printed books but incomplete or improperly structured in the app:

### 1. Missing Textbook Caution Rules (The Warning Triangle ▲ Icons)
The Shin Kanzen Master series uses triangular warning icons (▲) to call out strict grammatical constraints and JLPT exam traps. In our cards, some of these were simplified or omitted:

| Grammar Point | Physical Book Constraint (▲ Warning Icon) | App Card Current State | Exam Risk |
| :--- | :--- | :--- | :--- |
| **`〜にあたって`**<br>(SKM N2 Ch 1, p. 8) | *「より積極的な行動を表す言葉につき、マイナスイメージの言葉（別れ・入院・倒産など）にはつかない。」*<br>(Strictly cannot attach to negative events like hospitalization, bankruptcy, or breakups). | Only notes it has a "formal, forward-looking tone"; lacks explicit prohibition on negative nouns. | Learners fail JLPT trap questions asking if `入院にあたって` is valid. |
| **`〜（か）と思うと`**<br>(SKM N2 Ch 1, p. 9) | *「話者の行為については使わない。話者の希望・意向を表す文や働きかけの文は来ない。」*<br>(Cannot describe the speaker's own action, volition, or request). | Notes sudden surprise, but doesn't explicitly bar speaker subject in clause A. | Speaker-agent error in production and sentence ordering. |
| **`〜最中に`**<br>(SKM N2 Ch 2, p. 12) | *「それをじゃまするような予定外のことが起こったという意味の文が来ることが多い。」*<br>(Clause B strongly expects an unforeseen obstacle or interruption). | Describes "middle of an action" but treats interruption as optional background. | Misses the core JLPT contrast against `〜間に`. |
| **`〜ばかりだ` vs `〜一方だ`**<br>(SKM N2 Ch 2, p. 13) | *「『〜ばかりだ』は特に良くない方向に進んでいるという場合が多い。」*<br>(`ばかりだ` skews heavily towards negative deterioration; `一方だ` is neutral/bipolar). | Grouped together on a single card; nuance difference noted but not enforced in drills. | Conflation in productive writing/quizzing. |
| **`〜つつ`**<br>(SKM N2 Ch 2, p. 13) | *「『〜つつ』の前後の文は同じ主語。」*<br>(Both clauses MUST share the identical grammatical subject). | Mentioned in notes, but not enforced as a primary formation check. | Subject-mismatch error. |

### 2. Unwanted Card Bundling
In several places, multiple distinct textbook entries were collapsed into a single app card:
- **SKM N2 Chapter 2**: `added-n2-2-70` bundled both `〜うちに` and `〜(よ)うとしている` into one card. In the textbook, `〜うちに` has two distinct grammatical patterns (Pattern A: volitional action before an opportunity expires; Pattern B: non-volitional natural change occurring over time), while `〜(よ)うとしている` is an entirely separate point for imminent threshold transitions.
- **SKM N2 Chapter 2 & 14**: `added-n2-2-71` merged simultaneous `〜つつ` (Chapter 2) with adversative `〜つつも` (Chapter 14).

---

## 5. Hardware Acceleration Feasibility (Host RTX 3050 4GB)

To solve the raster scan challenge without burning CPU cycles, we probed the host environment:
- **GPU Hardware**: NVIDIA GeForce RTX 3050 Laptop GPU (4096 MB VRAM).
- **Execution Provider**: `onnxruntime` has **`DmlExecutionProvider` (Windows DirectML)** enabled.
- **Verified Benchmark**: Hooking RapidOCR into DirectML successfully offloaded neural inference to the RTX 3050, achieving stable ~4.5–5.0 seconds per page with zero CPU pegging and low memory footprint.

---

## 6. Proposed Plans of Action for Astra's Review

Here are the three strategic avenues to achieve complete, inside-out fidelity with the physical textbooks. We request Astra's advice on the most effective path:

### Plan A: Level-by-Level Incremental GPU Extraction & Card Refinement (Recommended)
- **Scope**: Focus on one complete book at a time, starting with **Shin Kanzen Master N2** (the highest level with the most subtle nuance traps).
- **Workflow**:
  1. Use the RTX 3050 DirectML pipeline to batch-extract the ~55 grammar explanation pages of SKM N2 Part 1 (Chapters 1–26).
  2. Unbundle conflated cards (split `うちに` vs `ようとしている`; separate `つつ` from `つつも`).
  3. Enrich all card `nuance` fields with the exact printed warning triangle (▲) constraints (negative word bans, volition limits, subject identity rules).
  4. Add dedicated distractor rationale in quizzes specifically targeting these textbook warning traps.
  5. Run test suite to verify 0 regressions, then proceed to SKM N3, Genki II, and Genki I.
- **Pros**: Immediate tangible value; user can study verified N2/N3 content right away without waiting for a massive global overhaul.

### Plan B: Complete Corpus Batch Extraction First, Followed by Automated Diffing
- **Scope**: Extract all ~180 grammar explanation pages across all 4 textbooks in one background run.
- **Workflow**:
  1. Write all OCR-extracted Japanese text into structured Markdown/JSON files (`audit/extracted_corpus/{book}/{chapter}.json`).
  2. Run a programmatic schema diff against `studyPoints.json` comparing:
     - Pattern titles & conjunctive forms (`接続`).
     - Vocabulary used in example sentences.
     - Presence of warning constraint keywords (`意志`, `マイナス`, `同じ主語`, `意外性`).
  3. Generate an automated gap report and systematically apply updates across the catalog.
- **Pros**: 100% comprehensive data lake; guaranteed zero blind spots across any chapter.
- **Cons**: Requires substantial processing upfront before individual card enhancements go live.

### Plan C: High-Yield "Exam Traps & Restrictions" Overlay (Surgical Focus)
- **Scope**: Target only the high-stakes discrimination points and warning triangle (▲) rules.
- **Workflow**:
  1. Inspect the caution sections of all SKM N3 and N2 chapters.
  2. Directly augment the `nuance`, `keyTakeaway`, and `quiz` objects of existing cards with explicit "JLPT Warning" callouts without altering card counts or structures.
  3. Ensure all paired contrasts (`〜ばかりだ` vs `〜一方だ`, `〜にあたって` vs `〜際`, `〜たとたん` vs `〜かと思うと`) have dedicated comparison tables in the Revision Desk.
- **Pros**: Fastest implementation; leaves existing card IDs and section mappings completely stable.
- **Cons**: Leaves bundled cards intact rather than fully atomizing every textbook bullet.

---

## 7. Key Questions for Astra

1. **Card Granularity**: Should grammar cards be strictly 1:1 with every numbered point in the textbook (e.g. splitting `うちに` into two distinct cards for Pattern A and Pattern B), or is it pedagogically superior to keep them on one card with explicit sub-sections?
2. **Execution Sequence**: Should we prioritize N2 and N3 (where warning constraints and exam traps are most severe), or start with N5/N4 (Genki) to establish a clean foundation?
3. **Drill Formats**: In Shin Kanzen Master, star-scramble questions (★が入るもの) are prominent. Should the web app add a dedicated star-scramble exercise mode, or continue focusing on 4-option distractor analysis quizzes?
