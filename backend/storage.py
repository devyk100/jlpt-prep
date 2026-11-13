import sqlite3
import json
import time
from pathlib import Path
from contextlib import contextmanager

DB_PATH = Path(__file__).resolve().parent.parent / "yomiflow.db"

class StorageManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = Path(db_path)
        self._init_db()

    @contextmanager
    def _connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def _init_db(self):
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    japanese TEXT NOT NULL,
                    translation TEXT DEFAULT '',
                    source TEXT DEFAULT 'Screen Capture',
                    vocabulary_json TEXT DEFAULT '[]',
                    grammar_json TEXT DEFAULT '[]',
                    is_favorite INTEGER DEFAULT 0,
                    exported_anki INTEGER DEFAULT 0
                )
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_history_timestamp ON history(timestamp DESC)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_history_japanese ON history(japanese)
            """)
            conn.commit()

    def add_entry(self, japanese: str, translation: str = "", source: str = "Screen Capture",
                  vocabulary: list = None, grammar: list = None) -> int:
        if not japanese or not japanese.strip():
            return -1

        japanese = japanese.strip()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        vocab_json = json.dumps(vocabulary or [], ensure_ascii=False)
        gram_json = json.dumps(grammar or [], ensure_ascii=False)

        with self._connection() as conn:
            cursor = conn.cursor()
            # Deduplicate against the very latest logged sentence to prevent spam
            cursor.execute("SELECT id, japanese FROM history ORDER BY id DESC LIMIT 1")
            last = cursor.fetchone()
            if last and last["japanese"] == japanese:
                cursor.execute("""
                    UPDATE history SET timestamp = ?, translation = COALESCE(NULLIF(?, ''), translation)
                    WHERE id = ?
                """, (timestamp, translation, last["id"]))
                conn.commit()
                return last["id"]

            cursor.execute("""
                INSERT INTO history (timestamp, japanese, translation, source, vocabulary_json, grammar_json)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (timestamp, japanese, translation, source, vocab_json, gram_json))
            conn.commit()
            return cursor.lastrowid

    def get_history(self, limit: int = 50, offset: int = 0, search: str = "") -> list:
        with self._connection() as conn:
            cursor = conn.cursor()
            if search and search.strip():
                query = f"%{search.strip()}%"
                cursor.execute("""
                    SELECT id, timestamp, japanese, translation, source, vocabulary_json, grammar_json, is_favorite, exported_anki
                    FROM history
                    WHERE japanese LIKE ? OR translation LIKE ?
                    ORDER BY id DESC LIMIT ? OFFSET ?
                """, (query, query, limit, offset))
            else:
                cursor.execute("""
                    SELECT id, timestamp, japanese, translation, source, vocabulary_json, grammar_json, is_favorite, exported_anki
                    FROM history
                    ORDER BY id DESC LIMIT ? OFFSET ?
                """, (limit, offset))

            rows = cursor.fetchall()
            results = []
            for r in rows:
                results.append({
                    "id": r["id"],
                    "timestamp": r["timestamp"],
                    "japanese": r["japanese"],
                    "translation": r["translation"],
                    "source": r["source"],
                    "vocabulary": json.loads(r["vocabulary_json"] or "[]"),
                    "grammar": json.loads(r["grammar_json"] or "[]"),
                    "is_favorite": bool(r["is_favorite"]),
                    "exported_anki": bool(r["exported_anki"])
                })
            return results

    def toggle_favorite(self, entry_id: int) -> bool:
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE history SET is_favorite = 1 - is_favorite WHERE id = ?", (entry_id,))
            conn.commit()
            cursor.execute("SELECT is_favorite FROM history WHERE id = ?", (entry_id,))
            res = cursor.fetchone()
            return bool(res["is_favorite"]) if res else False

    def delete_entry(self, entry_id: int):
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM history WHERE id = ?", (entry_id,))
            conn.commit()

    def clear_history(self):
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM history")
            conn.commit()
