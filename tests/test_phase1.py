import os
import sys
import unittest
import time
from PIL import Image, ImageDraw, ImageFont

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.config import ConfigManager
from backend.capture import capture_screen_region, get_screen_dimensions
from backend.ocr_engine import WindowsOCREngine
from backend.nlp_engine import JapaneseNLPEngine
from backend.storage import StorageManager


class TestPhase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_mgr = ConfigManager()
        cls.ocr = WindowsOCREngine()
        cls.nlp = JapaneseNLPEngine()
        cls.storage = StorageManager()

    @classmethod
    def tearDownClass(cls):
        cls.ocr.close()

    def test_01_screen_dimensions(self):
        w, h = get_screen_dimensions()
        print(f"\n[Test] Screen Dimensions: {w}x{h}")
        self.assertGreater(w, 0)
        self.assertGreater(h, 0)

    def test_02_gdi_capture_latency(self):
        img, ms = capture_screen_region(100, 100, 600, 200)
        print(f"[Test] Win32 GDI BitBlt Capture Latency: {ms:.2f} ms (Size: {img.size})")
        self.assertIsNotNone(img)
        self.assertEqual(img.size, (600, 200))
        self.assertLess(ms, 50.0, "Screen capture exceeded 50ms")

    def test_03_windows_japanese_ocr(self):
        # Create Japanese dialogue sample: 言われても困るんだけど。
        test_text = "言われても困るんだけど。"
        img = Image.new("RGB", (640, 120), color=(20, 20, 20))
        d = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("msgothic.ttc", 36)
        except Exception:
            font = None
        d.text((30, 35), test_text, fill=(255, 255, 255), font=font)

        res = self.ocr.recognize(img, force_refresh=True)
        print(f"[Test] Windows Native OCR Result: '{res.get('text')}' (Latency: {res.get('latency_ms'):.1f} ms)")

        self.assertIn("困る", res.get("text", ""))
        self.assertLess(res.get("latency_ms", 999), 500.0, "OCR latency exceeded 500ms target")

    def test_04_japanese_nlp_analysis(self):
        sentence = "言われても困るんだけど。"
        nlp_res = self.nlp.analyze_sentence(sentence)
        tokens = nlp_res.get("tokens", [])
        base_forms = [t["base_form"] for t in tokens]
        print(f"[Test] NLP Base Forms: {base_forms}")

        self.assertIn("言う", base_forms)
        self.assertIn("困る", base_forms)

    def test_05_storage_persistence(self):
        entry_id = self.storage.add_entry(
            japanese="言われても困るんだけど。",
            translation="I don't know what you expect me to do, even if you say that.",
            source="Test Suite"
        )
        self.assertGreater(entry_id, 0)

        history = self.storage.get_history(limit=5)
        found = any(h["japanese"] == "言われても困るんだけど。" for h in history)
        self.assertTrue(found)
        print(f"[Test] SQLite Storage Entry Verified (ID: {entry_id})")


if __name__ == "__main__":
    unittest.main()
