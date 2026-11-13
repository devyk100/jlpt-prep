import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app import YomiFlowApp

class TestAPIIntegration(unittest.TestCase):
    def test_api_full_workflow(self):
        app = YomiFlowApp()
        api = app.api

        # 1. Config check
        cfg = api.get_config()
        self.assertIn("capture", cfg)
        self.assertIn("shortcuts", cfg)

        # 2. Dimensions check
        dims = api.get_screen_dimensions()
        self.assertGreater(dims["width"], 0)
        self.assertGreater(dims["height"], 0)

        # 3. Test Region Capture preview
        prev = api.test_region_capture(100, 100, 400, 150)
        self.assertTrue(prev["data_uri"].startswith("data:image/jpeg;base64,"))
        self.assertGreater(len(prev["data_uri"]), 100)
        print(f"[Integration] Region preview generated in {prev['latency_ms']} ms")

        # 4. Capture & Process
        result = api.capture_and_process(force_refresh=True)
        self.assertIn("total_ms", result)
        self.assertIn("capture_ms", result)
        self.assertIn("ocr_ms", result)
        print(f"[Integration] Full capture & process round-trip completed in {result['total_ms']} ms")

        # 5. History retrieval
        hist = api.get_history(limit=5)
        self.assertIsInstance(hist, list)

        # Clean up
        app.ocr_engine.close()


if __name__ == "__main__":
    unittest.main()
