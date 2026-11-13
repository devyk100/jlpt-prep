# YomiFlow (読みフロー)
**Universal Japanese Immersion Assistant for Windows 11**

YomiFlow is a high-performance, lightweight, always-available Japanese immersion companion designed to run seamlessly alongside games (Persona 5 Royal, Genshin Impact, Final Fantasy VII Remake, Visual Novels), streaming services, and desktop applications.

---

## Key Features
- **Instant Global Screen Capture**: Sub-3ms Win32 GDI capture of any game or video region with DPI awareness.
- **Lightning-Fast Japanese OCR**: 15ms native Windows 11 OCR engine recognizes kana, kanji, dialogue boxes, and punctuation.
- **Always-on-Top Floating Overlay**: Minimal translucent glassmorphism interface that floats above games without stealing keyboard or gamepad focus.
- **Dual Visual Modes**:
  - **Compact Mode**: Displays recognized Japanese dialogue with natural translations.
  - **Expanded Mode**: Full morphological breakdown, base forms, kanji decomposition, grammar notes, and nuance.
- **Global Keyboard Shortcuts**:
  - `F8`: Instant Screen Capture & OCR / Explanation
  - `F9`: Toggle Overlay Visibility
  - `F10`: Toggle Compact / Expanded Mode
  - `F11`: Save to Vocabulary History
  - `Esc`: Dismiss / Minimize
- **Configurable Region Presets**: Easily adjust capture bounding boxes for game dialogue boxes or subtitles.
- **Privacy First**: 100% local capture, local OCR, and local dictionary parsing. Cloud LLM is used only as an optional fallback when requested.

---

## Architecture
- **Desktop Host**: Python 3.14 + Microsoft Edge WebView2 (`pywebview`).
- **Frontend**: React 19, TypeScript, Tailwind CSS, Vite.
- **Screen Capture**: Native Win32 GDI BitBlt (`backend/capture.py`).
- **OCR Engine**: Windows 11 Native Japanese Media OCR (`backend/ocr_engine.py` & `backend/ocr_worker.ps1`).
- **NLP Tokenizer**: SudachiPy (`sudachidict_core`).
- **Storage**: Local SQLite database for vocabulary and sentence history.
- **LLM Engine**: Provider abstraction supporting Gemini, DeepSeek, and OpenAI-compatible endpoints.

---

## Quick Start

### Prerequisites
- Windows 11 (with Japanese Language Pack installed for Windows OCR)
- Python 3.10+
- Node.js 20+

### Setup
1. **Install Frontend Dependencies & Build**:
   ```bash
   npm install
   npm run build
   ```

2. **Install Python Dependencies**:
   ```bash
   python -m pip install pywebview keyboard sudachipy sudachidict_core pillow
   ```

3. **Run YomiFlow**:
   ```bash
   python -m backend.app
   ```

---

## Configuration
Settings are stored in `config.json` in the root directory. You can configure:
- `capture_region`: `{ "x": 0, "y": 700, "width": 1920, "height": 380 }`
- `shortcuts`: Configurable hotkeys (F8, F9, F10, etc.)
- `opacity`: Background transparency (0.2 to 1.0)
- `llm_provider`: Gemini, DeepSeek, or OpenAI (with API key)
