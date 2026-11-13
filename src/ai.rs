use serde::{Deserialize, Serialize};
use windows::core::{HSTRING, Result as WinResult};
use windows::Foundation::Uri;
use windows::Web::Http::{HttpClient, HttpStringContent};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AiExplanation {
    pub translation: String,
    pub nuance: String,
    pub grammar: String,
}

pub struct FallbackAiClient {
    pub api_key: String,
    pub endpoint: String,
    pub model: String,
}

impl FallbackAiClient {
    pub fn new(api_key: String) -> Self {
        Self {
            api_key,
            endpoint: "https://api.deepseek.com/chat/completions".to_string(),
            model: "deepseek-chat".to_string(),
        }
    }

    pub fn explain(&self, japanese_text: &str) -> Result<AiExplanation, String> {
        if self.api_key.trim().is_empty() {
            return Err("DeepSeek/OpenAI API key not set. Configure it in ⚙ Settings.".to_string());
        }

        let system_prompt = "You are a Japanese immersion linguistic tutor for games and visual novels. \
Respond in concise JSON with these exact fields: \
\"translation\": natural English translation, \
\"nuance\": conversational tone, implied emotion, slang, or character personality, \
\"grammar\": breakdown of key verb forms or particles.";

        let user_prompt = format!("Analyze this Japanese line: \"{}\"", japanese_text);

        let req_body = serde_json::json!({
            "model": self.model,
            "messages": [
                { "role": "system", "content": system_prompt },
                { "role": "user", "content": user_prompt }
            ],
            "temperature": 0.3,
            "response_format": { "type": "json_object" }
        });

        let json_payload = req_body.to_string();

        let response_text = self.send_winrt_post(&self.endpoint, &json_payload)
            .map_err(|e| format!("Network/WinRT error: {:?}", e))?;

        // Parse DeepSeek / OpenAI chat completion response
        let v: serde_json::Value = serde_json::from_str(&response_text)
            .map_err(|e| format!("Failed to parse API response: {}", e))?;

        if let Some(err) = v.get("error") {
            let msg = err.get("message").and_then(|m| m.as_str()).unwrap_or("Unknown error");
            return Err(format!("API Error: {}", msg));
        }

        let content_str = v["choices"][0]["message"]["content"]
            .as_str()
            .ok_or_else(|| "Missing message content in API response".to_string())?;

        let parsed: serde_json::Value = serde_json::from_str(content_str)
            .map_err(|e| format!("Failed to parse inner JSON: {}", e))?;

        Ok(AiExplanation {
            translation: parsed["translation"].as_str().unwrap_or("").to_string(),
            nuance: parsed["nuance"].as_str().unwrap_or("").to_string(),
            grammar: parsed["grammar"].as_str().unwrap_or("").to_string(),
        })
    }

    fn send_winrt_post(&self, url: &str, body: &str) -> WinResult<String> {
        let uri = Uri::CreateUri(&HSTRING::from(url))?;
        let client = HttpClient::new()?;

        let content = HttpStringContent::CreateFromString(&HSTRING::from(body))?;
        
        // Add Authorization header
        let auth_val = format!("Bearer {}", self.api_key.trim());
        let headers = client.DefaultRequestHeaders()?;
        headers.Append(&HSTRING::from("Authorization"), &HSTRING::from(&auth_val))?;

        let response = client.PostAsync(&uri, &content)?.join()?;
        let resp_content = response.Content()?;
        let body_str = resp_content.ReadAsStringAsync()?.join()?;

        Ok(body_str.to_string())
    }
}
