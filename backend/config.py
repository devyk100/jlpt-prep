import os
import json
from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent.parent / "config.json"

DEFAULT_CONFIG = {
    "version": "1.0.0",
    "capture": {
        "x": 200,
        "y": 720,
        "width": 1520,
        "height": 280,
        "profile": "Bottom Dialogue",
        "profiles": {
            "Bottom Dialogue": {"x": 200, "y": 720, "width": 1520, "height": 280},
            "Persona 5 Royal": {"x": 350, "y": 700, "width": 1220, "height": 260},
            "Genshin Impact": {"x": 400, "y": 750, "width": 1120, "height": 240},
            "Fullscreen (1080p)": {"x": 0, "y": 0, "width": 1920, "height": 1080}
        }
    },
    "shortcuts": {
        "capture": "f8",
        "toggle_overlay": "f9",
        "toggle_mode": "f10",
        "save_history": "f11",
        "dismiss": "esc"
    },
    "overlay": {
        "compact": True,
        "opacity": 0.94,
        "always_on_top": True,
        "click_through": False,
        "width": 640,
        "height": 240,
        "expanded_height": 580,
        "theme": "dark"
    },
    "ocr": {
        "engine": "windows_media_ocr",
        "language": "ja",
        "auto_detect_change": True,
        "normalize_cjk_spaces": True
    },
    "llm": {
        "enabled": False,
        "provider": "deepseek",  # deepseek, gemini, openai_compatible
        "model": "deepseek-chat",
        "api_key": "",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.2
    }
}

class ConfigManager:
    def __init__(self, config_path=CONFIG_FILE):
        self.config_path = Path(config_path)
        self.config = self.load()

    def load(self):
        if not self.config_path.exists():
            self.save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Merge defaults for any missing keys
                merged = DEFAULT_CONFIG.copy()
                for k, v in data.items():
                    if isinstance(v, dict) and k in merged and isinstance(merged[k], dict):
                        merged[k] = {**merged[k], **v}
                    else:
                        merged[k] = v
                return merged
        except Exception as e:
            print(f"[Config] Error reading {self.config_path}: {e}. Using defaults.")
            return DEFAULT_CONFIG.copy()

    def save(self, config_data=None):
        if config_data is not None:
            self.config = config_data
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"[Config] Error writing {self.config_path}: {e}")
            return False

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()
