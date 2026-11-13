export interface Token {
  surface: string;
  base_form: string;
  reading_kata: string;
  reading_hira: string;
  part_of_speech: string;
  raw_pos: string[];
  conjugation_type: string;
  conjugation_form: string;
  is_punctuation: boolean;
  kanji: string[];
}

export interface Explanation {
  original?: string;
  natural_translation?: string;
  literal_translation?: string;
  vocabulary?: Array<{
    surface: string;
    reading: string;
    base_form: string;
    meaning: string;
    part_of_speech: string;
    conjugation: string;
  }>;
  grammar_notes?: string[];
  nuance?: string;
  uncertainty?: string[];
  error?: string;
}

export interface CapturePayload {
  text: string;
  lines: string[];
  tokens: Token[];
  kanji: string[];
  explanation: Explanation | null;
  capture_ms: number;
  ocr_ms: number;
  nlp_ms: number;
  total_ms: number;
  is_cached: boolean;
  timestamp: string;
}

export interface AppConfig {
  version: string;
  capture: {
    x: number;
    y: number;
    width: number;
    height: number;
    profile: string;
    profiles: Record<string, { x: number; y: number; width: number; height: number }>;
  };
  shortcuts: {
    capture: string;
    toggle_overlay: string;
    toggle_mode: string;
    save_history: string;
    dismiss: string;
  };
  overlay: {
    compact: boolean;
    opacity: number;
    always_on_top: boolean;
    click_through: boolean;
    width: number;
    height: number;
    expanded_height: number;
    theme: string;
  };
  ocr: {
    engine: string;
    language: string;
    auto_detect_change: boolean;
    normalize_cjk_spaces: boolean;
  };
  llm: {
    enabled: boolean;
    provider: string;
    model: string;
    api_key: string;
    base_url: string;
    temperature: number;
  };
}

export interface HistoryEntry {
  id: number;
  timestamp: string;
  japanese: string;
  translation: string;
  source: string;
  vocabulary: Token[];
  grammar: string[];
  is_favorite: boolean;
  exported_anki: boolean;
}

// Global declaration for pywebview API
declare global {
  interface Window {
    pywebview?: {
      api: {
        get_screen_dimensions(): Promise<{ width: number; height: number }>;
        get_config(): Promise<AppConfig>;
        save_config(config: AppConfig): Promise<{ success: boolean }>;
        capture_and_process(force_refresh?: boolean): Promise<CapturePayload>;
        explain_with_ai(sentence: string): Promise<Explanation>;
        test_region_capture(x: number, y: number, width: number, height: number): Promise<{
          data_uri: string;
          width: number;
          height: number;
          latency_ms: number;
        }>;
        get_history(limit?: number, offset?: number, search?: string): Promise<HistoryEntry[]>;
        toggle_favorite(entry_id: number): Promise<boolean>;
        delete_history_entry(entry_id: number): Promise<{ success: boolean }>;
        clear_history(): Promise<{ success: boolean }>;
        resize_window(width: number, height: number): Promise<{ success: boolean }>;
        hide_window(): Promise<{ success: boolean }>;
        show_window(): Promise<{ success: boolean }>;
        minimize_window(): Promise<{ success: boolean }>;
      };
    };
  }
}
