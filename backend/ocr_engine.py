import subprocess
import os
import sys
import time
import json
import re
import tempfile
import threading
from pathlib import Path
from PIL import Image

class WindowsOCREngine:
    def __init__(self):
        self.lock = threading.Lock()
        self.proc = None
        self.script_path = Path(__file__).resolve().parent / "ocr_worker.ps1"
        self.temp_file = Path(tempfile.gettempdir()) / "yomiflow_ocr_frame.png"
        self.last_image_hash = None
        self.last_result = None
        self._start_worker()

    def _start_worker(self):
        if self.proc is not None:
            try:
                self.proc.kill()
            except Exception:
                pass

        cmd = [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-File", str(self.script_path)
        ]

        # Hide console window
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0  # SW_HIDE

        self.proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=startupinfo,
            text=True,
            encoding="utf-8"
        )

        # Wait for "READY"
        try:
            line = self.proc.stdout.readline().strip()
            if line != "READY":
                print(f"[OCR] Warning: Unexpected init line: {line}")
            else:
                print("[OCR] Windows Native Japanese OCR worker ready.")
        except Exception as e:
            print(f"[OCR] Error starting OCR worker: {e}")

    def normalize_japanese_text(self, text: str) -> str:
        """
        Cleans up OCR noise, normalizes spaces between Japanese kana/kanji,
        and standardizes full-width/half-width symbols.
        """
        if not text:
            return ""

        # Remove spaces between Japanese characters (Kanji, Hiragana, Katakana)
        # Regex matches space between two CJK characters
        cjk_regex = r'([\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3000-\u303F])\s+([\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3000-\u303F])'
        prev = ""
        while prev != text:
            prev = text
            text = re.sub(cjk_regex, r'\1\2', text)

        # Clean trailing whitespace per line
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines)

    def recognize(self, image: Image.Image, force_refresh=False) -> dict:
        """
        Performs OCR on the given PIL Image.
        Returns dict with:
          - text: normalized Japanese text
          - lines: list of lines
          - latency_ms: OCR execution time
          - is_cached: whether the result was from frame deduplication
        """
        with self.lock:
            # Check frame deduplication (skip OCR if frame is identical to previous)
            img_bytes = image.tobytes()
            current_hash = hash(img_bytes)

            if not force_refresh and current_hash == self.last_image_hash and self.last_result:
                cached = self.last_result.copy()
                cached["is_cached"] = True
                cached["latency_ms"] = 0.5
                return cached

            t0 = time.perf_counter()

            # Save frame to disk for WinRT BitmapDecoder
            image.save(self.temp_file, format="PNG")
            path_str = str(self.temp_file.resolve())

            # Send path to worker
            if self.proc is None or self.proc.poll() is not None:
                print("[OCR] Worker dead. Restarting...")
                self._start_worker()

            try:
                self.proc.stdin.write(path_str + "\n")
                self.proc.stdin.flush()
                resp_line = self.proc.stdout.readline().strip()
                if not resp_line:
                    raise RuntimeError("Empty response from OCR worker")

                data = json.loads(resp_line)
                if "error" in data:
                    print(f"[OCR Worker Error] {data['error']}")
                    return {
                        "text": "",
                        "lines": [],
                        "error": data["error"],
                        "latency_ms": (time.perf_counter() - t0) * 1000.0,
                        "is_cached": False
                    }

                raw_text = data.get("text", "")
                raw_lines = data.get("lines", [])
                normalized_text = self.normalize_japanese_text(raw_text)

                result = {
                    "text": normalized_text,
                    "lines": [self.normalize_japanese_text(l) for l in raw_lines],
                    "raw_text": raw_text,
                    "latency_ms": (time.perf_counter() - t0) * 1000.0,
                    "is_cached": False
                }

                self.last_image_hash = current_hash
                self.last_result = result
                return result

            except Exception as e:
                print(f"[OCR] Exception during recognition: {e}")
                self._start_worker()
                return {
                    "text": "",
                    "lines": [],
                    "error": str(e),
                    "latency_ms": (time.perf_counter() - t0) * 1000.0,
                    "is_cached": False
                }

    def close(self):
        with self.lock:
            if self.proc:
                try:
                    self.proc.stdin.write("EXIT\n")
                    self.proc.stdin.flush()
                    self.proc.wait(timeout=2)
                except Exception:
                    self.proc.kill()
                try:
                    if self.proc.stdin:
                        self.proc.stdin.close()
                    if self.proc.stdout:
                        self.proc.stdout.close()
                    if self.proc.stderr:
                        self.proc.stderr.close()
                except Exception:
                    pass
                self.proc = None
            if self.temp_file.exists():
                try:
                    self.temp_file.unlink()
                except Exception:
                    pass
