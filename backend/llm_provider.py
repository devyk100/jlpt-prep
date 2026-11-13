import json
import urllib.request
import urllib.error
from typing import Optional

class LLMProvider:
    def __init__(self, config: dict):
        self.config = config.get("llm", {})
        self.cache = {}

    def update_config(self, config: dict):
        self.config = config.get("llm", {})

    def is_configured(self) -> bool:
        provider = self.config.get("provider", "deepseek")
        api_key = self.config.get("api_key", "").strip()
        return bool(api_key)

    def explain_sentence(self, sentence: str, context_lines: list[str] = None, nlp_data: dict = None) -> dict:
        """
        Requests context-aware explanation from the configured LLM provider.
        Returns structured JSON dict.
        """
        if not sentence or not sentence.strip():
            return {"error": "Empty sentence"}

        sentence = sentence.strip()

        # Cache check
        if sentence in self.cache:
            return self.cache[sentence]

        provider = self.config.get("provider", "deepseek").lower()
        api_key = self.config.get("api_key", "").strip()

        if not api_key:
            return {
                "original": sentence,
                "natural_translation": "[AI translation unconfigured - enter API key in Settings]",
                "literal_translation": "",
                "vocabulary": [],
                "grammar_notes": [],
                "nuance": "Local dictionary and morphological analysis active. Configure DeepSeek or Gemini API in settings for AI explanations.",
                "uncertainty": []
            }

        prompt = self._build_prompt(sentence, context_lines, nlp_data)

        try:
            if provider == "gemini":
                result = self._call_gemini(prompt, api_key)
            elif provider in ("deepseek", "openai", "openai_compatible"):
                result = self._call_openai_compatible(prompt, api_key)
            else:
                result = self._call_openai_compatible(prompt, api_key)

            self.cache[sentence] = result
            return result
        except Exception as e:
            print(f"[LLM] Error calling provider {provider}: {e}")
            return {
                "original": sentence,
                "natural_translation": f"API Error: {str(e)}",
                "literal_translation": "",
                "vocabulary": [],
                "grammar_notes": [],
                "nuance": "Check your API key and network connection in Settings.",
                "uncertainty": [str(e)]
            }

    def _build_prompt(self, sentence: str, context_lines: list[str] = None, nlp_data: dict = None) -> str:
        ctx_str = "\n".join(context_lines) if context_lines else "None provided"
        
        system_instruction = (
            "You are an expert Japanese linguist and immersion assistant. Analyze the Japanese dialogue line "
            "encountered in a game or video. Explain omitted context, natural English nuances, and grammar breakdown. "
            "Output strictly valid JSON matching this schema:\n"
            "{\n"
            '  "original": string,\n'
            '  "natural_translation": string,\n'
            '  "literal_translation": string,\n'
            '  "vocabulary": [\n'
            '    {"surface": string, "reading": string, "base_form": string, "meaning": string, "part_of_speech": string, "conjugation": string}\n'
            '  ],\n'
            '  "grammar_notes": [string],\n'
            '  "nuance": string,\n'
            '  "uncertainty": [string]\n'
            "}"
        )

        user_content = (
            f"Preceding Dialogue Context:\n{ctx_str}\n\n"
            f"Current Japanese Sentence:\n{sentence}\n\n"
            "Respond ONLY with valid JSON."
        )

        return f"{system_instruction}\n\n{user_content}"

    def _call_openai_compatible(self, prompt: str, api_key: str) -> dict:
        base_url = self.config.get("base_url", "https://api.deepseek.com/v1").rstrip("/")
        model = self.config.get("model", "deepseek-chat")
        
        url = f"{base_url}/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a Japanese immersion assistant. Always output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            "temperature": float(self.config.get("temperature", 0.2)),
            "response_format": {"type": "json_object"} if "deepseek" in base_url or "openai" in base_url else None
        }

        # Filter out None values
        payload = {k: v for k, v in payload.items() if v is not None}

        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=12) as response:
            res_body = response.read().decode("utf-8")
            data = json.loads(res_body)
            content = data["choices"][0]["message"]["content"]
            # Clean possible markdown fence
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            return json.loads(content.strip())

    def _call_gemini(self, prompt: str, api_key: str) -> dict:
        model = self.config.get("model", "gemini-2.5-flash")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": float(self.config.get("temperature", 0.2)),
                "responseMimeType": "application/json"
            }
        }

        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=12) as response:
            res_body = response.read().decode("utf-8")
            data = json.loads(res_body)
            text_resp = data["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(text_resp.strip())
