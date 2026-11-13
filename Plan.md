# Project: YomiFlow — Universal Japanese Immersion Assistant

## 1. Project Vision

Build a high-performance, lightweight, always-available Japanese immersion companion for Windows 11.

The application should work alongside virtually any application displaying Japanese text:

- Netflix and other streaming platforms.
- YouTube and other browser-based video websites.
- Japanese games, including Persona 5 Royal, Final Fantasy VII Remake and Genshin Impact.
- Visual novels and JRPGs.
- Local video players.
- Other desktop applications displaying Japanese text.

The primary interaction should be extremely simple:

1. I am watching a video or playing a game.
2. I encounter Japanese dialogue or text that I don't understand.
3. I press a configurable global keyboard shortcut.
4. YomiFlow immediately captures the relevant screen content.
5. It extracts the Japanese text and provides a detailed explanation.
6. A floating overlay displays the results without forcing me to switch applications.
7. The encountered vocabulary and sentences are logged in the background for future Anki export.

The application must prioritize speed, low resource consumption, accuracy and minimal interaction.

This is NOT intended to be another conventional Japanese-learning application. It is a universal screen-aware Japanese reading assistant.

---

# 2. Core Product Requirements

## A. Always-available floating overlay

This is the most important UI requirement.

Build an always-on-top floating window that remains available above games, browsers, video players and other applications.

Requirements:

- Always-on-top window.
- Transparent or translucent background.
- Minimal, modern interface.
- Resizable and repositionable.
- Configurable opacity.
- Global keyboard shortcuts.
- Ability to hide/show instantly.
- Ability to temporarily become click-through.
- Ability to interact with vocabulary and explanations when activated.
- Remember its previous position, dimensions and preferences.
- Avoid stealing focus from the currently active game or video.
- Support high-DPI displays and Windows scaling.

The application should have two visual states:

**Compact mode**
- Displays the current Japanese sentence.
- Displays its natural English translation.
- Shows a loading indicator while processing.
- Provides a button to expand the explanation.

**Expanded mode**
- Displays the full vocabulary breakdown.
- Shows furigana.
- Explains kanji and compound words.
- Displays phrase-level meanings.
- Explains grammar and sentence structure.
- Shows contextual nuance.
- Allows vocabulary to be saved.

The overlay should not obscure the entire screen. It should be a compact, well-designed panel.

The overlay must not disappear when the user switches between applications.

## B. Global keyboard shortcuts

Implement configurable system-wide keyboard shortcuts.

Default suggestions:

- F8: Capture current screen and explain Japanese text.
- F9: Toggle overlay visibility.
- F10: Toggle compact/expanded mode.
- F11: Save current sentence and vocabulary.
- Escape: Close or minimize the expanded overlay.

Allow the user to change these shortcuts in settings.

The capture shortcut must work even when another application has keyboard focus, provided Windows and the active application permit global shortcut registration.

Avoid interfering with common game controls. Detect shortcut registration conflicts and allow the user to configure alternatives.

---

# 3. Screen Capture and Text Extraction

The application must support multiple capture strategies.

Do not assume every application exposes subtitles through accessible DOM elements.

Implement a modular capture architecture.

## A. Universal screen capture

Use Windows Graphics Capture APIs, preferably through a suitable Rust/Windows API integration.

Requirements:

- Capture the active application window.
- Capture a user-selected screen region.
- Support full-screen capture as a fallback.
- Support multiple monitors.
- Preserve Japanese text clarity.
- Handle DPI scaling correctly.
- Avoid unnecessary full-resolution image processing.
- Provide a screenshot preview during initial region configuration.

The user should be able to define a preferred Japanese text capture region.

For example, when playing Persona 5 Royal, the user can select the dialogue box area.

Remember this region for subsequent sessions.

Provide optional automatic window-specific capture profiles.

## B. OCR engine

Evaluate and integrate:

1. PaddleOCR with Japanese recognition.
2. Windows OCR as a lightweight fallback.
3. An ONNX Runtime-based OCR implementation if it offers better performance and deployment characteristics.

Prefer local OCR.

Use hardware acceleration where beneficial, including CUDA or DirectML where supported.

Do not make an NVIDIA GPU mandatory.

My laptop has:
- NVIDIA RTX 3050 Laptop GPU, 4 GB VRAM.
- Intel 12th-generation processor.
- 16 GB RAM.
- Windows 11.

The application must also work on systems without dedicated GPUs.

OCR should:
- Recognize Japanese kana and kanji.
- Preserve punctuation.
- Handle vertical and horizontal Japanese text where supported.
- Recognize dialogue boxes and subtitles.
- Handle multiple text lines.
- Return text with confidence scores and bounding boxes.
- Distinguish Japanese text from irrelevant interface elements where possible.

## C. Browser integration

Implement an optional browser extension or browser integration.

Support Chromium-based browsers initially.

Where technically and legally permitted, extract actual subtitle text from browser video players instead of performing OCR.

This is particularly useful for Netflix and YouTube.

Requirements:
- Detect Japanese subtitle text.
- Pass subtitle text to the desktop application.
- Preserve subtitle timing.
- Avoid duplicate extraction.
- Fall back to screen OCR when direct extraction is unavailable.

Never assume Netflix's internal player exposes subtitle text through a stable public interface.

Do not attempt to circumvent DRM or protected media restrictions.

The browser integration should be optional. The desktop application must remain useful without it.

## D. Game compatibility

Support ordinary screen capture without modifying game processes.

Do not use:
- DLL injection.
- Process memory modification.
- Game executable modification.
- Anti-cheat bypasses.
- Unnecessary game hooks.

Prefer Windows Graphics Capture.

If an application prevents capture or renders protected content as a black screen, communicate this limitation and provide an alternative workflow.

---

# 4. Intelligent OCR Pipeline

The application should not repeatedly send identical images to OCR or AI.

Implement an efficient text acquisition pipeline.

Suggested workflow:

1. Capture the configured region at a modest background sampling rate.
2. Compare the new frame with the previous frame.
3. Detect whether the text region has changed.
4. Run OCR only when necessary.
5. Normalize the extracted Japanese text.
6. Detect duplicate sentences.
7. Maintain the latest recognized dialogue.
8. Keep a short rolling history of previous dialogue lines.

The global shortcut should use the most recently recognized text whenever that text is sufficiently recent and reliable.

If the cached OCR is stale or unavailable, capture and process a fresh frame immediately.

Provide an option to force a fresh capture.

Implement debouncing and duplicate detection.

Avoid translating the same sentence repeatedly.

Do not continuously invoke an LLM in the background.

The LLM should only be invoked when requested, unless the user explicitly enables automatic translation.

---

# 5. Japanese NLP and Dictionary Engine

This component must operate locally and provide near-instant results.

Do not use an LLM for ordinary dictionary lookups.

Integrate a Japanese morphological analyzer such as SudachiPy or an equivalent solution.

Support:
- Word segmentation.
- Lemmatization.
- Part-of-speech identification.
- Kana readings.
- Conjugation identification.
- Compound word detection.
- Phrase recognition.

## A. Dictionary integration

Use established Japanese dictionary resources.

Prioritize:

- JMdict for Japanese-English vocabulary.
- KANJIDIC for individual kanji.
- Japanese frequency information.
- Pitch accent dictionaries where available.
- Grammar pattern references where licensing permits.

Investigate Yomitan-compatible dictionary formats to reuse existing dictionaries.

Respect individual dictionary licenses and attribution requirements.

Implement local indexing and caching.

## B. Word-level explanation

For every recognized sentence, provide:

- Original word.
- Reading in hiragana.
- Base form.
- English meanings.
- Part of speech.
- Conjugation information.
- Relevant grammatical role.
- Kanji composition where useful.

For example:

言われても

- Reading: いわれても
- Base form: 言う
- Meaning: Even if someone tells me.
- Components: 言う → 言われる (passive) → 言われても (passive + ても).
- Grammar: Passive form followed by ても.

## C. Compound words and kanji decomposition

This is an important feature.

When encountering complex Japanese words, explain the kanji individually.

For example:

情報処理

- 情: feelings, circumstances; common reading じょう.
- 報: report, information; common reading ほう.
- 処: deal with, handle; common reading しょ.
- 理: reason, logic; common reading り.

Combined meaning: Information processing.

Do not produce misleading literal translations by simply concatenating kanji meanings.

Distinguish between:
- Individual kanji meanings.
- Actual lexical meaning of the compound.
- Historical etymology, only when supported by a reliable source.

Provide common readings and related vocabulary where useful.

Avoid overwhelming the user with every possible reading of every kanji.

---

# 6. AI Translation and Explanation Engine

Use DeepSeek API initially.

Implement an LLM-provider abstraction so other providers can be added later.

Possible providers:
- DeepSeek.
- OpenAI-compatible APIs.
- Gemini.
- Local models through Ollama, as an optional future feature.

Do not hardcode model names or pricing. Make the provider and model configurable.

Use an OpenAI-compatible client interface where possible.

API keys must be stored securely on the local machine. Never expose API keys in frontend JavaScript, logs, browser extensions or distributed application bundles.

## A. AI invocation

When the user presses F8:

1. Obtain the latest recognized Japanese sentence.
2. Retrieve preceding dialogue from the local rolling context buffer.
3. Retrieve the following line if available.
4. Retrieve local dictionary and morphological analysis results.
5. Send the sentence and relevant context to the configured LLM.
6. Parse the structured response.
7. Display the result in the overlay.

Do not send unnecessary screenshots to the LLM.

Send extracted text rather than images whenever possible.

Support manual correction of OCR output before translation.

## B. Required AI response

Every explanation should contain:

1. Original Japanese sentence.
2. Natural English translation.
3. Literal translation.
4. Vocabulary breakdown.
5. Important phrases and expressions.
6. Kanji breakdown for complex vocabulary.
7. Grammar explanations.
8. Sentence structure.
9. Contextual nuance.
10. Uncertainty warnings when appropriate.

### Example

Japanese:

そんなこと言われても困るんだけど。

Natural translation:

"I don't know what you expect me to do, even if you say that."

Vocabulary:

- そんなこと: Something like that.
- 言われても: Even if someone tells me.
- 困る: To be troubled; to be at a loss.
- んだけど: Explanatory ending followed by けど.

Grammar:

- 言われても = passive form of 言う + ても.
- んだけど = のだ contraction + けど.

Nuance:

Informal expression of discomfort or frustration. The speaker may be implying that the other person's request is unreasonable.

The explanation must be educational, concise and context-aware.

Do not blindly translate Japanese word by word.

Explain omitted subjects, omitted objects, implied meaning and casual speech where relevant.

Distinguish between literal meaning and contextual interpretation.

Do not hallucinate grammar rules or etymology.

If the available dialogue is insufficient, explicitly state that contextual interpretation is uncertain.

## C. Structured response

Require valid JSON output using a well-defined schema.

Suggested structure:

{
  "original": "",
  "natural_translation": "",
  "literal_translation": "",
  "vocabulary": [
    {
      "surface": "",
      "reading": "",
      "base_form": "",
      "meaning": "",
      "part_of_speech": "",
      "conjugation": "",
      "kanji_breakdown": []
    }
  ],
  "phrases": [],
  "grammar_notes": [],
  "sentence_structure": "",
  "nuance": "",
  "uncertainty": []
}

Validate the response before displaying it.

Handle malformed JSON, missing fields, timeouts and API errors gracefully.

Use low-temperature settings for consistent educational explanations.

Implement response caching based on sentence, context and model configuration.

---

# 7. Performance Requirements

Performance is a primary product requirement, not an optional optimization.

The application should feel instantaneous.

Target performance on my RTX 3050 / 16 GB RAM laptop:

- Global shortcut response: under 100 ms to initiate UI feedback.
- Cached OCR lookup: under 100 ms to display available results.
- Fresh OCR: target under 500 ms for a normal subtitle/dialogue region.
- Local dictionary lookup: target under 50 ms.
- Overlay rendering: target under 100 ms.
- AI response: show a loading state immediately; target under 2 seconds when the API/network permits, without promising a hard upper bound.

These are targets to benchmark, not guarantees.

Implement:

- Asynchronous OCR.
- Asynchronous API requests.
- Non-blocking UI.
- Local dictionary caching.
- Sentence caching.
- Debouncing.
- Text deduplication.
- Efficient image preprocessing.
- Lazy loading of dictionaries.
- Background database writes.
- Request cancellation.
- API timeout handling.
- A bounded OCR and dialogue queue.

The overlay must remain responsive while OCR and AI requests are running.

Never freeze the game or the desktop UI.

Measure CPU, RAM, GPU VRAM and processing latency.

Provide a performance diagnostics screen.

Avoid unnecessarily running the GPU continuously.

---

# 8. Background Logging and Vocabulary History

Every recognized sentence should optionally be recorded locally.

The application must maintain a searchable history.

For each entry, store:

- Original Japanese sentence.
- OCR confidence.
- Recognized timestamp.
- Application/window source.
- Game or website profile, if identified.
- Previous dialogue context.
- AI translation, if requested.
- Vocabulary tokens.
- Dictionary meanings.
- Grammar explanations, if requested.
- Whether the entry has been exported to Anki.

Use SQLite for persistent local storage.

Implement:
- Duplicate detection.
- Search by Japanese word.
- Search by English meaning.
- Filter by date.
- Filter by application/game.
- Filter by vocabulary.
- Mark as favourite.
- Delete individual entries.
- Bulk deletion.
- Export and backup.

Do not automatically send the complete history to any external service.

All historical data should remain local unless explicitly exported or sent for an AI request.

Provide controls to disable background logging and to clear history.

---

# 9. Anki Integration

Implement AnkiConnect integration as an optional feature.

The user should be able to save:
- Individual vocabulary.
- Complete sentences.
- Phrases.
- Kanji-related vocabulary.

Create configurable Anki note templates.

Suggested vocabulary card:

Front:
Japanese word and reading.

Back:
- Meaning.
- Original sentence.
- Natural translation.
- Kanji breakdown.
- Audio, if available.

Suggested sentence card:

Front:
Original Japanese sentence.

Back:
- Natural translation.
- Vocabulary breakdown.
- Grammar notes.
- Context.

Support:
- Configurable deck selection.
- Configurable note type.
- Duplicate detection.
- Batch export.
- Export selected entries only.
- CSV/JSON fallback when Anki is unavailable.

Do not force the user to save every unfamiliar word.

---

# 10. User Interface and Experience

Use a polished, minimalist interface.

Suggested technology:
- Tauri 2.
- React.
- TypeScript.
- Tailwind CSS.
- A lightweight component library such as shadcn/ui.

Main overlay:

Compact view:
- Japanese sentence.
- English translation.
- Expand button.
- Loading/error indicator.

Expanded view:
- Vocabulary.
- Phrase meanings.
- Furigana.
- Kanji decomposition.
- Grammar.
- Nuance.
- Save buttons.

Additional desktop screens:

1. Dashboard.
2. Reading history.
3. Vocabulary history.
4. Anki export.
5. Dictionary management.
6. AI provider configuration.
7. OCR configuration.
8. Capture region configuration.
9. Keyboard shortcuts.
10. Performance diagnostics.

Use a clean dark theme by default, with a light theme option.

Avoid clutter and unnecessary animations.

The overlay should be optimized for reading while gaming.

---

# 11. Privacy and Compatibility

This application processes content from other applications.

Implement privacy-first defaults.

- OCR locally wherever possible.
- Never upload complete screenshots by default.
- Send only extracted text and necessary context to AI providers.
- Do not record microphone audio.
- Do not record video.
- Do not capture passwords or sensitive text intentionally.
- Allow the user to pause capture.
- Show a clear capture-active indicator.
- Store API keys securely.
- Provide a complete data deletion option.

For browser integration, respect website policies and protected media restrictions.

For games, use external screen capture rather than process injection or memory modification.

Do not attempt to bypass anti-cheat or DRM systems.

---

# 12. Architecture and Code Organization

Use a modular architecture with clear separation between:

- Desktop shell.
- Overlay UI.
- Capture subsystem.
- OCR subsystem.
- Japanese NLP subsystem.
- Dictionary subsystem.
- Translation provider subsystem.
- Context management.
- SQLite storage.
- Anki integration.
- Browser integration.
- Settings and configuration.

Prefer Rust for desktop-specific functionality and performance-sensitive capture/overlay operations.

Use Python for OCR/NLP integration only where it provides a meaningful advantage.

Do not introduce multiple backend processes unnecessarily.

Evaluate whether the OCR/NLP components can be deployed as local native libraries or a single persistent service rather than spawning Python processes repeatedly.

Use typed interfaces between components.

Implement structured logging and error handling.

Keep secrets out of source control.

Provide an .env.example file.

Provide a reproducible Windows build process.

Include dependency and model download instructions.

Respect open-source dependency licenses.

---

# 13. Implementation Plan

Do not attempt to implement every feature in a single untested step.

Work incrementally.

### Phase 1: Functional MVP

Build:
- Windows desktop application.
- Always-on-top overlay.
- Global keyboard shortcut.
- Manual screen-region selection.
- Screen capture.
- Japanese OCR.
- Display recognized Japanese text.

Acceptance test:
Open Persona 5 Royal, select its dialogue region, press F8 and display the recognized Japanese text in the overlay.

### Phase 2: Japanese dictionary

Build:
- Sudachi or equivalent Japanese morphological analysis.
- JMdict integration.
- Kanji dictionary integration.
- Word segmentation.
- Readings.
- Word-level meanings.
- Kanji breakdown.

Acceptance test:
Recognize a Japanese sentence and display clickable vocabulary with definitions without making an AI API request.

### Phase 3: AI explanation

Build:
- DeepSeek provider integration.
- Configurable API key and model.
- Context-aware translation.
- Structured JSON output.
- Vocabulary and phrase explanations.
- Grammar and nuance explanations.
- Response caching.

Acceptance test:
Press F8 on a recognized sentence and display its complete educational explanation.

### Phase 4: Background history

Build:
- SQLite storage.
- Dialogue history.
- Vocabulary history.
- Search and filters.
- Duplicate detection.
- AnkiConnect integration.
- CSV/JSON export.

Acceptance test:
Read several sentences, restart the application and verify that all logged entries remain available.

### Phase 5: Universal compatibility

Build and test:
- Persona 5 Royal.
- Final Fantasy VII Remake.
- Genshin Impact.
- Netflix.
- YouTube.
- Local video players.
- General browser content.

Add browser integration where feasible.

Implement application-specific capture profiles.

Acceptance test:
The same global shortcut and overlay workflow should work across different supported applications without requiring the user to change their normal workflow.

### Phase 6: Performance and polish

Optimize:
- Capture latency.
- OCR latency.
- Dictionary latency.
- AI request latency.
- RAM usage.
- CPU usage.
- GPU usage.
- Startup time.

Test multiple resolutions and Windows scaling configurations.

Verify that the overlay remains responsive while the user is playing games.

---

# 14. Development Instructions for Antigravity

You are acting as the senior software architect and implementation agent.

Follow these instructions:

1. Inspect the existing workspace before creating files.
2. If this is a new project, establish the repository structure and document architectural decisions.
3. Evaluate dependencies for compatibility with Windows 11.
4. Do not assume a library supports a feature merely because its documentation mentions a similar feature.
5. Verify the APIs and integration points before committing to them.
6. Prefer stable, actively maintained libraries.
7. Avoid unnecessary dependencies.
8. Implement one phase at a time.
9. Build and run the application after each major implementation stage.
10. Write tests for important processing components.
11. Do not leave placeholder implementations while claiming a phase is complete.
12. Do not silently substitute a slower or less capable implementation.
13. Document known compatibility limitations.
14. Keep the application functional when the AI provider is unavailable.
15. Keep dictionary lookup functional without an internet connection.
16. Make all API-dependent functionality optional and configurable.
17. Never hardcode credentials.
18. Maintain a README with installation, configuration, architecture and development instructions.
19. Maintain a DEVELOPMENT.md file tracking completed features, outstanding work and known bugs.
20. Before implementing a major architectural change, explain the tradeoffs and justify the decision.

If a feature cannot be implemented reliably, explain why and provide the closest safe alternative.

Do not spend excessive time producing architectural documents without building a working application.

**Start with Phase 1.** Establish the project, implement the Windows capture and overlay foundation, run it, and demonstrate the first working end-to-end capture workflow before proceeding to subsequent phases.

The ultimate objective is a fast, reliable, always-available Japanese immersion assistant that works across my entire Windows desktop environment.

