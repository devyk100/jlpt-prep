use crate::ai::{AiExplanation, FallbackAiClient};
use crate::capture::{capture_screen_region, get_screen_dimensions};
use crate::config::AppConfig;
use crate::dictionary::{GrammarNote, LocalDictionary, ParsedWord};
use crate::history::{HistoryEntry, HistoryManager};
use crate::hotkeys::{HotKeyEvent, HotkeyManager};
use crate::ocr::NativeOcrEngine;
use eframe::egui::{
    self, Align, Color32, CornerRadius, Layout, RichText, Sense, Stroke, Vec2, ViewportCommand,
};
use std::sync::{Arc, Mutex};
use std::thread;

#[derive(Clone)]
pub struct CaptureResult {
    pub text: String,
    pub words: Vec<ParsedWord>,
    pub grammar: Vec<GrammarNote>,
    pub total_ms: f64,
}

pub struct YomiFlowApp {
    pub config: AppConfig,
    pub hotkeys: HotkeyManager,
    pub ocr: Arc<NativeOcrEngine>,
    pub dict: Arc<LocalDictionary>,
    pub history: Arc<HistoryManager>,
    pub latest_result: Arc<Mutex<Option<CaptureResult>>>,
    pub ai_explanation: Arc<Mutex<Option<Result<AiExplanation, String>>>>,
    pub is_capturing: Arc<Mutex<bool>>,
    pub is_requesting_ai: Arc<Mutex<bool>>,

    // UI state
    pub is_expanded: bool,
    pub show_region_settings: bool,
    pub status_message: String,
}

impl YomiFlowApp {
    pub fn new(cc: &eframe::CreationContext<'_>) -> Self {
        let fonts = egui::FontDefinitions::default();
        cc.egui_ctx.set_fonts(fonts);

        let config = AppConfig::load();
        let hotkeys = HotkeyManager::new();
        let ocr = Arc::new(NativeOcrEngine::new());
        let dict = Arc::new(LocalDictionary::new());
        let history = Arc::new(HistoryManager::new());
        let latest_result = Arc::new(Mutex::new(None));
        let ai_explanation = Arc::new(Mutex::new(None));
        let is_capturing = Arc::new(Mutex::new(false));
        let is_requesting_ai = Arc::new(Mutex::new(false));

        Self {
            config,
            hotkeys,
            ocr,
            dict,
            history,
            latest_result,
            ai_explanation,
            is_capturing,
            is_requesting_ai,
            is_expanded: false,
            show_region_settings: false,
            status_message: "Press F8 to capture Japanese dialogue".to_string(),
        }
    }

    pub fn trigger_capture(&self, ctx: egui::Context) {
        let is_cap = self.is_capturing.clone();
        {
            let mut busy = is_cap.lock().unwrap();
            if *busy {
                return;
            }
            *busy = true;
        }

        // Reset previous AI explanation for new dialogue
        *self.ai_explanation.lock().unwrap() = None;

        let region = self.config.region.clone();
        let ocr = self.ocr.clone();
        let dict = self.dict.clone();
        let history = self.history.clone();
        let result_store = self.latest_result.clone();

        let api_key = self.config.deepseek_api_key.clone();
        let auto_ai = self.config.auto_ai_explain;
        let ai_store = self.ai_explanation.clone();
        let is_ai_req = self.is_requesting_ai.clone();
        let endpoint = self.config.deepseek_endpoint.clone();
        let model = self.config.deepseek_model.clone();

        thread::spawn(move || {
            match capture_screen_region(&region) {
                Ok((img, cap_ms)) => {
                    let (text, _lines, ocr_ms) = ocr.recognize(&img);
                    let words = dict.parse_sentence(&text);
                    let grammar = dict.detect_grammar(&text);
                    let total_ms = cap_ms + ocr_ms;

                    // Automatically record to persistent history
                    if !text.trim().is_empty() {
                        let token_surfaces: Vec<String> = words
                            .iter()
                            .filter(|w| !w.is_punct)
                            .map(|w| w.surface.clone())
                            .collect();

                        let entry = HistoryEntry {
                            timestamp: chrono_now_string(),
                            original: text.clone(),
                            translation: String::new(),
                            tokens: token_surfaces,
                        };
                        history.append(&entry);
                    }

                    let res = CaptureResult {
                        text: text.clone(),
                        words,
                        grammar,
                        total_ms,
                    };

                    *result_store.lock().unwrap() = Some(res);

                    // Auto-trigger AI explanation if API key is provided
                    if auto_ai && !api_key.trim().is_empty() && !text.trim().is_empty() {
                        *is_ai_req.lock().unwrap() = true;
                        let mut client = FallbackAiClient::new(api_key);
                        client.endpoint = endpoint;
                        client.model = model;

                        let clean_text = text.clone();
                        let ctx_clone = ctx.clone();
                        thread::spawn(move || {
                            let ai_res = client.explain(&clean_text);
                            *ai_store.lock().unwrap() = Some(ai_res);
                            *is_ai_req.lock().unwrap() = false;
                            ctx_clone.request_repaint();
                        });
                    }
                }
                Err(err) => {
                    eprintln!("[Capture Error] {}", err);
                }
            }

            *is_cap.lock().unwrap() = false;
            ctx.request_repaint();
        });
    }

    pub fn trigger_ai_explanation(&self, ctx: egui::Context, text: String) {
        let is_req = self.is_requesting_ai.clone();
        {
            let mut busy = is_req.lock().unwrap();
            if *busy {
                return;
            }
            *busy = true;
        }

        let ai_store = self.ai_explanation.clone();
        let mut client = FallbackAiClient::new(self.config.deepseek_api_key.clone());
        client.endpoint = self.config.deepseek_endpoint.clone();
        client.model = self.config.deepseek_model.clone();

        thread::spawn(move || {
            let res = client.explain(&text);
            *ai_store.lock().unwrap() = Some(res);
            *is_req.lock().unwrap() = false;
            ctx.request_repaint();
        });
    }
}

fn chrono_now_string() -> String {
    format!("captured_{}", std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map(|d| d.as_secs()).unwrap_or(0))
}

impl eframe::App for YomiFlowApp {
    fn clear_color(&self, _visuals: &egui::Visuals) -> [f32; 4] {
        [0.0, 0.0, 0.0, 0.0]
    }

    fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {
        let ctx = ui.ctx().clone();

        // 1. Continuous Always-On-Top enforcement in egui and OS DWM
        crate::capture::force_window_topmost("YomiFlow");
        ctx.send_viewport_cmd(ViewportCommand::WindowLevel(egui::WindowLevel::AlwaysOnTop));

        // 2. Process Hotkey Events
        while let Ok(evt) = self.hotkeys.receiver.try_recv() {
            match evt {
                HotKeyEvent::Capture => {
                    self.trigger_capture(ctx.clone());
                }
                HotKeyEvent::ToggleVisibility => {
                    ctx.send_viewport_cmd(ViewportCommand::Visible(true));
                    ctx.send_viewport_cmd(ViewportCommand::WindowLevel(egui::WindowLevel::AlwaysOnTop));
                    crate::capture::force_window_topmost("YomiFlow");
                }
                HotKeyEvent::ToggleMode => {
                    self.is_expanded = !self.is_expanded;
                    let target_h = if self.is_expanded { 540.0 } else { 190.0 };
                    ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(660.0, target_h)));
                }
                HotKeyEvent::Dismiss => {
                    ctx.send_viewport_cmd(ViewportCommand::Minimized(true));
                }
            }
        }

        // Handle Escape to minimize when overlay is focused
        if ui.input(|i| i.key_pressed(egui::Key::Escape)) {
            ctx.send_viewport_cmd(ViewportCommand::Minimized(true));
        }

        let is_capturing_now = *self.is_capturing.lock().unwrap();
        let is_ai_running = *self.is_requesting_ai.lock().unwrap();
        let current_res = self.latest_result.lock().unwrap().clone();
        let current_ai = self.ai_explanation.lock().unwrap().clone();

        // === SLEEK GAMING GLASSMORPHISM FRAME ===
        let alpha = (self.config.opacity.clamp(0.4, 1.0) * 255.0) as u8;
        let bg_color = Color32::from_rgba_premultiplied(12, 16, 26, alpha);
        let border_stroke = Stroke::new(1.0, Color32::from_rgba_premultiplied(244, 63, 94, 85));

        let panel_frame = egui::Frame::new()
            .fill(bg_color)
            .stroke(border_stroke)
            .corner_radius(CornerRadius::same(14))
            .inner_margin(egui::Margin::symmetric(14, 10));

        panel_frame.show(ui, |ui| {
            // === HEADER BAR (Draggable HUD) ===
            ui.horizontal(|ui| {
                // 1. Move Grip Handle
                let drag_btn = ui.add(
                    egui::Button::new(
                        RichText::new("⠿ MOVE")
                            .size(10.5)
                            .strong()
                            .color(Color32::from_rgb(226, 232, 240)),
                    )
                    .fill(Color32::from_rgba_premultiplied(255, 255, 255, 28))
                    .stroke(Stroke::new(1.0, Color32::from_rgba_premultiplied(255, 255, 255, 45)))
                    .corner_radius(CornerRadius::same(6))
                    .sense(Sense::click_and_drag()),
                );
                if drag_btn.is_pointer_button_down_on() || drag_btn.drag_started() || drag_btn.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                // 2. Neon Brand Title (also draggable)
                let title_lbl = ui.add(
                    egui::Label::new(
                        RichText::new("⚡ YomiFlow")
                            .strong()
                            .size(13.5)
                            .color(Color32::from_rgb(251, 113, 133)),
                    )
                    .sense(Sense::click_and_drag())
                );
                if title_lbl.is_pointer_button_down_on() || title_lbl.drag_started() || title_lbl.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                let sub_lbl = ui.add(
                    egui::Label::new(
                        RichText::new("読みフロー")
                            .size(11.0)
                            .color(Color32::from_rgb(148, 163, 184)),
                    )
                    .sense(Sense::click_and_drag())
                );
                if sub_lbl.is_pointer_button_down_on() || sub_lbl.drag_started() || sub_lbl.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                // Performance Latency Badge
                if let Some(ref res) = current_res {
                    ui.add(
                        egui::Label::new(
                            RichText::new(format!("{:.1}ms", res.total_ms))
                                .size(10.5)
                                .color(Color32::from_rgb(52, 211, 153)),
                        )
                    );
                } else if is_capturing_now {
                    ui.label(
                        RichText::new("Scanning...")
                            .size(11.0)
                            .color(Color32::from_rgb(251, 191, 36)),
                    );
                }

                // 3. Middle empty space as drag area
                let remaining_w = (ui.available_width() - 280.0).max(10.0);
                let (_, empty_drag) = ui.allocate_exact_size(Vec2::new(remaining_w, 24.0), Sense::click_and_drag());
                if empty_drag.is_pointer_button_down_on() || empty_drag.drag_started() || empty_drag.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                // Right-aligned Action Buttons
                ui.with_layout(Layout::right_to_left(Align::Center), |ui| {
                    // Minimize button
                    if ui.button(RichText::new("🗕").size(12.0).color(Color32::from_rgb(148, 163, 184)))
                        .on_hover_text("Minimize Overlay (Esc)").clicked()
                    {
                        ctx.send_viewport_cmd(ViewportCommand::Minimized(true));
                    }

                    // Mode Toggle (F10)
                    let mode_lbl = if self.is_expanded { "▲ Compact" } else { "▼ Breakdown" };
                    let btn_mode = ui.add(
                        egui::Button::new(RichText::new(mode_lbl).size(11.0).color(Color32::WHITE))
                            .fill(Color32::from_rgb(30, 41, 59))
                            .corner_radius(CornerRadius::same(6)),
                    );
                    if btn_mode.on_hover_text("Toggle Detailed Breakdown (F10)").clicked() {
                        self.is_expanded = !self.is_expanded;
                        let target_h = if self.is_expanded { 540.0 } else { 190.0 };
                        ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(660.0, target_h)));
                    }

                    // Settings button
                    let reg_lbl = if self.show_region_settings { "Close ⚙" } else { "⚙ Settings" };
                    let btn_set = ui.add(
                        egui::Button::new(RichText::new(reg_lbl).size(11.0).color(Color32::from_rgb(253, 230, 138)))
                            .fill(Color32::from_rgb(120, 53, 15))
                            .corner_radius(CornerRadius::same(6)),
                    );
                    if btn_set.clicked() {
                        self.show_region_settings = !self.show_region_settings;
                        if self.show_region_settings && !self.is_expanded {
                            self.is_expanded = true;
                            ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(660.0, 540.0)));
                        }
                    }

                    // Capture button (F8)
                    let btn_cap = ui.add(
                        egui::Button::new(
                            RichText::new("📷 Capture (F8)")
                                .color(Color32::WHITE)
                                .strong()
                                .size(11.0),
                        )
                        .fill(Color32::from_rgb(225, 29, 72))
                        .corner_radius(CornerRadius::same(6)),
                    );
                    if btn_cap.clicked() {
                        self.trigger_capture(ctx.clone());
                    }
                });
            });

            ui.add_space(4.0);
            ui.separator();
            ui.add_space(4.0);

            // === MAIN RECOGNIZED DIALOGUE ===
            if let Some(ref res) = current_res {
                if res.text.trim().is_empty() {
                    ui.vertical_centered(|ui| {
                        ui.add_space(8.0);
                        ui.label(RichText::new("No Japanese dialogue text found in capture box.").color(Color32::from_rgb(148, 163, 184)));
                        ui.label(RichText::new("Press F8 in game or adjust capture area with ⚙ Settings.").size(11.0).color(Color32::from_rgb(100, 116, 139)));
                        ui.add_space(6.0);
                    });
                } else {
                    // Display Interactive Japanese Sentence
                    ui.horizontal_wrapped(|ui| {
                        for word in &res.words {
                            if word.is_punct {
                                ui.label(RichText::new(&word.surface).size(18.0).color(Color32::from_rgb(100, 116, 139)));
                            } else if !word.meaning.is_empty() || !word.kanji_breakdown.is_empty() {
                                // Rich hover tooltip showing reading, base form, meaning, and kanji
                                let mut tip = format!("Word: {}", word.surface);
                                if !word.reading.is_empty() {
                                    tip.push_str(&format!("  [{}]", word.reading));
                                }
                                if word.base_form != word.surface {
                                    tip.push_str(&format!(" (base: {})", word.base_form));
                                }
                                if !word.meaning.is_empty() {
                                    tip.push_str(&format!("\nMeaning: {}", word.meaning));
                                }
                                for k in &word.kanji_breakdown {
                                    tip.push_str(&format!("\n • {} ({}): {}", k.character, k.onyomi, k.meaning));
                                }

                                let chip = ui.add(
                                    egui::Button::new(
                                        RichText::new(&word.surface)
                                            .size(18.0)
                                            .strong()
                                            .color(Color32::from_rgb(255, 241, 242)),
                                    )
                                    .fill(Color32::from_rgba_premultiplied(244, 63, 94, 25))
                                    .stroke(Stroke::new(1.0, Color32::from_rgba_premultiplied(251, 113, 133, 90)))
                                    .corner_radius(CornerRadius::same(5))
                                    .sense(Sense::click()),
                                ).on_hover_text(tip);

                                if chip.clicked() {
                                    if !self.is_expanded {
                                        self.is_expanded = true;
                                        ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(660.0, 540.0)));
                                    }
                                }
                            } else {
                                ui.label(RichText::new(&word.surface).size(18.0).color(Color32::from_rgb(241, 245, 249)));
                            }
                        }
                    });

                    // Quick Action Bar
                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        if ui.button(RichText::new("📋 Copy").size(10.5)).clicked() {
                            ui.ctx().copy_text(res.text.clone());
                            self.status_message = "Copied Japanese line to clipboard!".to_string();
                        }

                        if ui.button(RichText::new("⭐ Export Anki").size(10.5)).clicked() {
                            match self.history.export_anki_tsv("yomiflow_anki_export.txt") {
                                Ok(n) => self.status_message = format!("Exported {} cards to yomiflow_anki_export.txt", n),
                                Err(e) => self.status_message = format!("Export error: {}", e),
                            }
                        }

                        // Fallback AI button
                        let ai_lbl = if is_ai_running { "✨ Analyzing Nuance..." } else { "✨ AI Nuance & Grammar" };
                        let btn_ai = ui.add(
                            egui::Button::new(
                                RichText::new(ai_lbl).size(10.5).color(Color32::from_rgb(199, 210, 254))
                            )
                            .fill(Color32::from_rgb(49, 46, 129))
                            .corner_radius(CornerRadius::same(5)),
                        );
                        if btn_ai.clicked() && !is_ai_running {
                            if !self.is_expanded {
                                self.is_expanded = true;
                                ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(660.0, 540.0)));
                            }
                            self.trigger_ai_explanation(ctx.clone(), res.text.clone());
                        }

                        let non_punct_count = res.words.iter().filter(|w| !w.is_punct).count();
                        ui.label(
                            RichText::new(format!("{} words", non_punct_count))
                                .size(10.5)
                                .color(Color32::from_rgb(148, 163, 184)),
                        );

                        if !self.status_message.is_empty() {
                            ui.label(RichText::new(&self.status_message).size(10.5).color(Color32::from_rgb(251, 191, 36)));
                        }
                    });
                }
            } else {
                ui.vertical_centered(|ui| {
                    ui.add_space(14.0);
                    ui.label(RichText::new("🎮 Ready to capture Japanese dialogue.").strong().size(13.5).color(Color32::from_rgb(241, 245, 249)));
                    ui.label(RichText::new("Press F8 anywhere in your game to scan subtitles & dialogue instantly.").size(11.5).color(Color32::from_rgb(148, 163, 184)));
                    ui.add_space(8.0);
                });
            }

            // === EXPANDED BREAKDOWN / SETTINGS DRAWER ===
            if self.is_expanded {
                ui.add_space(6.0);
                ui.separator();
                ui.add_space(4.0);

                if self.show_region_settings {
                    // === SETTINGS PANEL ===
                    ui.label(RichText::new("Overlay Settings & Capture Box").strong().color(Color32::from_rgb(251, 113, 133)));
                    ui.add_space(4.0);

                    ui.horizontal(|ui| {
                        ui.label("Snap Window:");
                        if ui.button("📍 Top Left").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(100.0, 80.0)));
                            self.config.window_x = Some(100.0);
                            self.config.window_y = Some(80.0);
                            self.config.save();
                        }
                        if ui.button("📍 Top Center").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(450.0, 80.0)));
                            self.config.window_x = Some(450.0);
                            self.config.window_y = Some(80.0);
                            self.config.save();
                        }
                        if ui.button("📍 Center").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(450.0, 260.0)));
                            self.config.window_x = Some(450.0);
                            self.config.window_y = Some(260.0);
                            self.config.save();
                        }
                        if ui.button("📍 Bottom Subtitles").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(350.0, 520.0)));
                            self.config.window_x = Some(350.0);
                            self.config.window_y = Some(520.0);
                            self.config.save();
                        }
                    });

                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        ui.label("Capture Preset:");
                        if ui.button("Bottom Subtitles (1080p)").clicked() {
                            self.config.region = crate::config::CaptureRegion { x: 200, y: 720, width: 1520, height: 280 };
                            self.config.save();
                        }
                        if ui.button("Persona 5 Royal").clicked() {
                            self.config.region = crate::config::CaptureRegion { x: 350, y: 700, width: 1220, height: 260 };
                            self.config.save();
                        }
                        if ui.button("Fullscreen").clicked() {
                            let (sw, sh) = get_screen_dimensions();
                            self.config.region = crate::config::CaptureRegion { x: 0, y: 0, width: sw, height: sh };
                            self.config.save();
                        }
                    });

                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        ui.label("Box X:");
                        ui.add(egui::DragValue::new(&mut self.config.region.x).speed(5));
                        ui.label("Box Y:");
                        ui.add(egui::DragValue::new(&mut self.config.region.y).speed(5));
                        ui.label("Width:");
                        ui.add(egui::DragValue::new(&mut self.config.region.width).speed(5).range(100..=3840));
                        ui.label("Height:");
                        ui.add(egui::DragValue::new(&mut self.config.region.height).speed(5).range(50..=2160));
                    });

                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        ui.label("Overlay Opacity:");
                        if ui.add(egui::Slider::new(&mut self.config.opacity, 0.4..=1.0)).changed() {
                            self.config.save();
                        }

                        ui.checkbox(&mut self.config.auto_ai_explain, "Auto-run AI on capture");
                    });

                    ui.add_space(6.0);
                    ui.separator();
                    ui.add_space(4.0);

                    ui.label(RichText::new("DeepSeek / OpenAI API Key (Instant Dialogue Nuance):").strong().size(11.0).color(Color32::from_rgb(165, 180, 252)));
                    ui.horizontal(|ui| {
                        ui.add(egui::TextEdit::singleline(&mut self.config.deepseek_api_key).password(true).hint_text("sk-...")).on_hover_text("Stored locally in config.json");
                        if ui.button("💾 Save Key").clicked() {
                            self.config.save();
                            self.status_message = "API key saved!".to_string();
                            self.show_region_settings = false;
                        }
                    });
                } else if let Some(ref res) = current_res {
                    egui::ScrollArea::vertical().max_height(310.0).show(ui, |ui| {
                        // === MODULE 1: AI LINGUISTIC BREAKDOWN ===
                        if is_ai_running {
                            ui.group(|ui| {
                                ui.horizontal(|ui| {
                                    ui.label(RichText::new("🤖 DeepSeek is analyzing conversational tone, slang & nuance...").color(Color32::from_rgb(199, 210, 254)));
                                });
                            });
                            ui.add_space(4.0);
                        } else if let Some(ref ai_res) = current_ai {
                            match ai_res {
                                Ok(expl) => {
                                    let card_frame = egui::Frame::new()
                                        .fill(Color32::from_rgba_premultiplied(24, 27, 50, 230))
                                        .stroke(Stroke::new(1.0, Color32::from_rgba_premultiplied(99, 102, 241, 140)))
                                        .corner_radius(CornerRadius::same(8))
                                        .inner_margin(egui::Margin::same(10));

                                    card_frame.show(ui, |ui| {
                                        ui.horizontal(|ui| {
                                            ui.label(RichText::new("🤖 AI Dialogue Translation & Nuance").strong().size(12.0).color(Color32::from_rgb(165, 180, 252)));
                                        });
                                        ui.add_space(2.0);

                                        // Natural Translation
                                        ui.label(RichText::new(format!("\"{}\"", expl.translation)).strong().size(14.0).color(Color32::WHITE));

                                        // Conversational Nuance
                                        if !expl.nuance.is_empty() {
                                            ui.add_space(2.0);
                                            ui.horizontal(|ui| {
                                                ui.label(RichText::new("🔥 Nuance:").strong().color(Color32::from_rgb(253, 224, 71)));
                                                ui.label(RichText::new(&expl.nuance).color(Color32::from_rgb(254, 240, 138)).size(12.0));
                                            });
                                        }

                                        // Grammar Breakdown
                                        if !expl.grammar.is_empty() {
                                            ui.add_space(2.0);
                                            ui.horizontal(|ui| {
                                                ui.label(RichText::new("🧩 Grammar:").strong().color(Color32::from_rgb(110, 231, 183)));
                                                ui.label(RichText::new(&expl.grammar).color(Color32::from_rgb(209, 250, 229)).size(12.0));
                                            });
                                        }
                                    });
                                    ui.add_space(6.0);
                                }
                                Err(err) => {
                                    ui.label(RichText::new(format!("AI Note: {}", err)).color(Color32::from_rgb(248, 113, 113)).size(11.5));
                                    ui.add_space(4.0);
                                }
                            }
                        } else if self.config.deepseek_api_key.trim().is_empty() {
                            // Friendly callout to add API key
                            let banner_frame = egui::Frame::new()
                                .fill(Color32::from_rgba_premultiplied(30, 27, 45, 180))
                                .stroke(Stroke::new(1.0, Color32::from_rgba_premultiplied(251, 191, 36, 90)))
                                .corner_radius(CornerRadius::same(6))
                                .inner_margin(egui::Margin::symmetric(10, 6));

                            banner_frame.show(ui, |ui| {
                                ui.horizontal(|ui| {
                                    ui.label(RichText::new("🔑 Tip: Add your DeepSeek API key in ⚙ Settings to get instant natural translations, slang nuance, and tone analysis.").size(11.0).color(Color32::from_rgb(253, 230, 138)));
                                });
                            });
                            ui.add_space(6.0);
                        }

                        // === MODULE 2: DETECTED GRAMMAR PATTERNS ===
                        if !res.grammar.is_empty() {
                            ui.label(RichText::new("Detected Grammar & Conjugation Patterns").strong().color(Color32::from_rgb(192, 132, 252)));
                            ui.add_space(2.0);
                            for g in &res.grammar {
                                ui.horizontal(|ui| {
                                    ui.label(RichText::new(g.pattern).strong().color(Color32::from_rgb(216, 180, 254)));
                                    ui.label(RichText::new(format!("— {}", g.meaning)).color(Color32::WHITE).size(12.0));
                                });
                                ui.label(RichText::new(g.explanation).size(11.0).color(Color32::from_rgb(148, 163, 184)));
                                ui.add_space(2.0);
                            }
                            ui.add_space(4.0);
                            ui.separator();
                            ui.add_space(4.0);
                        }

                        // === MODULE 3: INSTANT WORD & KANJI BREAKDOWN ===
                        ui.label(RichText::new("Offline Word & Kanji Breakdown").strong().color(Color32::from_rgb(251, 113, 133)));
                        ui.add_space(4.0);

                        for word in &res.words {
                            if word.is_punct {
                                continue;
                            }
                            ui.horizontal(|ui| {
                                // Word Surface
                                ui.label(RichText::new(&word.surface).strong().size(14.0).color(Color32::WHITE));

                                // Kana reading
                                if !word.reading.is_empty() {
                                    ui.label(RichText::new(format!("[{}]", word.reading)).size(12.0).color(Color32::from_rgb(252, 211, 77)));
                                }

                                // Base form (if inflected)
                                if word.base_form != word.surface && !word.base_form.is_empty() {
                                    ui.label(RichText::new(format!("(base: {})", word.base_form)).size(11.0).color(Color32::from_rgb(192, 132, 252)));
                                }

                                // English definition
                                if !word.meaning.is_empty() {
                                    ui.label(RichText::new(&word.meaning).size(12.0).color(Color32::from_rgb(226, 232, 240)));
                                }

                                // Component Kanji breakdown
                                for k in &word.kanji_breakdown {
                                    ui.label(
                                        RichText::new(format!("{} [{}]: {}", k.character, k.onyomi, k.meaning))
                                            .size(11.0)
                                            .color(Color32::from_rgb(251, 146, 60)),
                                    );
                                }
                            });
                            ui.separator();
                        }
                    });
                }
            }
        });
    }
}
