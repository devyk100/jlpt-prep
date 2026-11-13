import os
import sys
import time
import json
import threading
from collections import deque
from pathlib import Path
import webview
import keyboard

from backend.config import ConfigManager
from backend.capture import capture_screen_region, get_screen_dimensions, image_to_base64_data_uri
from backend.ocr_engine import WindowsOCREngine
from backend.nlp_engine import JapaneseNLPEngine
from backend.storage import StorageManager
from backend.llm_provider import LLMProvider

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / "dist"
INDEX_HTML = DIST_DIR / "index.html"


class YomiFlowAPI:
    def __init__(self, app_state):
        self.state = app_state

    def get_screen_dimensions(self):
        w, h = get_screen_dimensions()
        return {"width": w, "height": h}

    def get_config(self):
        return self.state.config_mgr.config

    def save_config(self, new_config):
        success = self.state.config_mgr.save(new_config)
        self.state.llm_provider.update_config(new_config)
        self.state.setup_shortcuts()
        return {"success": success}

    def capture_and_process(self, force_refresh=False):
        """
        Main end-to-end action: captures the screen region, runs OCR,
        morphological segmentation, dictionary parsing, and optional AI explanation.
        """
        cfg = self.state.config_mgr.config
        capture_cfg = cfg.get("capture", {})
        x = int(capture_cfg.get("x", 200))
        y = int(capture_cfg.get("y", 720))
        w = int(capture_cfg.get("width", 1520))
        h = int(capture_cfg.get("height", 280))

        # 1. Screen capture
        img, capture_ms = capture_screen_region(x, y, w, h)

        # 2. Japanese OCR
        ocr_res = self.state.ocr_engine.recognize(img, force_refresh=force_refresh)
        ocr_ms = ocr_res.get("latency_ms", 0.0)
        text = ocr_res.get("text", "")
        lines = ocr_res.get("lines", [])
        is_cached = ocr_res.get("is_cached", False)

        tokens = []
        kanji = []
        nlp_ms = 0.0
        explanation = None

        if text:
            # 3. Morphological analysis
            t_nlp0 = time.perf_counter()
            nlp_data = self.state.nlp_engine.analyze_sentence(text)
            nlp_ms = (time.perf_counter() - t_nlp0) * 1000.0
            tokens = nlp_data.get("tokens", [])
            kanji = nlp_data.get("kanji", [])

            # Update rolling context
            if not is_cached and text not in self.state.context_buffer:
                self.state.context_buffer.append(text)

            # 4. Optional LLM invocation
            if cfg.get("llm", {}).get("enabled", False) and self.state.llm_provider.is_configured():
                prev_lines = list(self.state.context_buffer)[:-1]
                explanation = self.state.llm_provider.explain_sentence(text, prev_lines, nlp_data)

            # 5. Persist to SQLite history
            profile_name = capture_cfg.get("profile", "Screen Capture")
            trans_str = explanation.get("natural_translation", "") if explanation else ""
            self.state.storage.add_entry(
                japanese=text,
                translation=trans_str,
                source=profile_name,
                vocabulary=tokens,
                grammar=explanation.get("grammar_notes", []) if explanation else []
            )

        payload = {
            "text": text,
            "lines": lines,
            "tokens": tokens,
            "kanji": kanji,
            "explanation": explanation,
            "capture_ms": round(capture_ms, 2),
            "ocr_ms": round(ocr_ms, 2),
            "nlp_ms": round(nlp_ms, 2),
            "total_ms": round(capture_ms + ocr_ms + nlp_ms, 2),
            "is_cached": is_cached,
            "timestamp": time.strftime("%H:%M:%S")
        }

        # Dispatch event to UI so frontend state updates immediately
        self.state.dispatch_ui_event("yomiflow-captured", payload)
        return payload

    def explain_with_ai(self, sentence: str):
        prev_lines = list(self.state.context_buffer)
        explanation = self.state.llm_provider.explain_sentence(sentence, prev_lines)
        return explanation

    def test_region_capture(self, x: int, y: int, width: int, height: int):
        """Captures region and returns base64 image data URI for UI preview."""
        img, ms = capture_screen_region(int(x), int(y), int(width), int(height))
        data_uri = image_to_base64_data_uri(img, format="JPEG", quality=80)
        return {
            "data_uri": data_uri,
            "width": img.width,
            "height": img.height,
            "latency_ms": round(ms, 2)
        }

    def get_history(self, limit=50, offset=0, search=""):
        return self.state.storage.get_history(limit=int(limit), offset=int(offset), search=search)

    def toggle_favorite(self, entry_id: int):
        return self.state.storage.toggle_favorite(int(entry_id))

    def delete_history_entry(self, entry_id: int):
        self.state.storage.delete_entry(int(entry_id))
        return {"success": True}

    def clear_history(self):
        self.state.storage.clear_history()
        return {"success": True}

    def resize_window(self, width: int, height: int):
        if self.state.window:
            self.state.window.resize(int(width), int(height))
        return {"success": True}

    def hide_window(self):
        if self.state.window:
            self.state.window.hide()
        return {"success": True}

    def show_window(self):
        if self.state.window:
            self.state.window.show()
        return {"success": True}

    def minimize_window(self):
        if self.state.window:
            self.state.window.minimize()
        return {"success": True}


class YomiFlowApp:
    def __init__(self):
        self.config_mgr = ConfigManager()
        self.ocr_engine = WindowsOCREngine()
        self.nlp_engine = JapaneseNLPEngine()
        self.storage = StorageManager()
        self.llm_provider = LLMProvider(self.config_mgr.config)
        self.context_buffer = deque(maxlen=10)
        self.window = None
        self.api = YomiFlowAPI(self)
        self._shortcut_hooks = []
        self._is_visible = True

    def dispatch_ui_event(self, event_name: str, data: dict):
        if self.window:
            try:
                json_str = json.dumps(data, ensure_ascii=False)
                script = f"window.dispatchEvent(new CustomEvent('{event_name}', {{ detail: {json_str} }}));"
                self.window.evaluate_js(script)
            except Exception as e:
                print(f"[IPC] Error dispatching event {event_name}: {e}")

    def trigger_capture_shortcut(self):
        """Called when F8 is pressed globally."""
        def run():
            # Show overlay if hidden
            if not self._is_visible and self.window:
                self.window.show()
                self._is_visible = True
            self.api.capture_and_process(force_refresh=True)

        threading.Thread(target=run, daemon=True).start()

    def trigger_toggle_overlay(self):
        """Called when F9 is pressed globally."""
        if self.window:
            if self._is_visible:
                self.window.hide()
                self._is_visible = False
            else:
                self.window.show()
                self._is_visible = True

    def trigger_toggle_mode(self):
        """Called when F10 is pressed globally."""
        self.dispatch_ui_event("yomiflow-toggle-mode", {})

    def trigger_save_history(self):
        """Called when F11 is pressed globally."""
        self.dispatch_ui_event("yomiflow-save-history", {})

    def trigger_dismiss(self):
        """Called when Escape is pressed."""
        self.dispatch_ui_event("yomiflow-dismiss", {})

    def setup_shortcuts(self):
        """Registers global shortcuts via keyboard library."""
        try:
            keyboard.unhook_all()
        except Exception:
            pass

        shortcuts = self.config_mgr.config.get("shortcuts", {})
        capture_key = shortcuts.get("capture", "f8")
        toggle_key = shortcuts.get("toggle_overlay", "f9")
        mode_key = shortcuts.get("toggle_mode", "f10")
        save_key = shortcuts.get("save_history", "f11")
        dismiss_key = shortcuts.get("dismiss", "esc")

        try:
            if capture_key:
                keyboard.add_hotkey(capture_key, self.trigger_capture_shortcut)
            if toggle_key:
                keyboard.add_hotkey(toggle_key, self.trigger_toggle_overlay)
            if mode_key:
                keyboard.add_hotkey(mode_key, self.trigger_toggle_mode)
            if save_key:
                keyboard.add_hotkey(save_key, self.trigger_save_history)
            if dismiss_key:
                keyboard.add_hotkey(dismiss_key, self.trigger_dismiss)
            print(f"[Shortcuts] Registered: Capture={capture_key}, Toggle={toggle_key}, Mode={mode_key}")
        except Exception as e:
            print(f"[Shortcuts] Warning: Failed to register hotkeys: {e}")

    def run(self):
        self.setup_shortcuts()

        cfg_overlay = self.config_mgr.config.get("overlay", {})
        width = int(cfg_overlay.get("width", 640))
        height = int(cfg_overlay.get("height", 240))
        on_top = bool(cfg_overlay.get("always_on_top", True))

        screen_w, screen_h = get_screen_dimensions()
        # Default position: bottom-center above game dialogue
        x_pos = (screen_w - width) // 2
        y_pos = screen_h - height - 120

        # Load dist/index.html
        url = str(INDEX_HTML) if INDEX_HTML.exists() else "http://localhost:1420"

        self.window = webview.create_window(
            title="YomiFlow",
            url=url,
            js_api=self.api,
            width=width,
            height=height,
            x=x_pos,
            y=y_pos,
            frameless=True,
            on_top=on_top,
            transparent=True,
            easy_drag=True
        )

        try:
            webview.start(debug=False)
        finally:
            self.ocr_engine.close()
            try:
                keyboard.unhook_all()
            except Exception:
                pass


if __name__ == "__main__":
    app = YomiFlowApp()
    app.run()
