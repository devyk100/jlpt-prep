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
    pub status_message: String,
}

impl YomiFlowApp {
    pub fn new(cc: &eframe::CreationContext<'_>) -> Self {
        let fonts = egui::FontDefinitions::default();
        cc.egui_ctx.set_fonts(fonts);

        // Dark theme: eliminate default harsh borders and white strokes
        let mut visuals = egui::Visuals::dark();
        visuals.window_stroke = Stroke::NONE;
        visuals.widgets.noninteractive.bg_stroke = Stroke::NONE;
        visuals.widgets.inactive.bg_stroke = Stroke::NONE;
        visuals.widgets.hovered.bg_stroke = Stroke::NONE;
        visuals.widgets.active.bg_stroke = Stroke::NONE;
        visuals.widgets.open.bg_stroke = Stroke::NONE;
        cc.egui_ctx.set_visuals(visuals);

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
            status_message: String::new(),
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

        // Reset previous AI explanation for new capture
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
    format!(
        "captured_{}",
        std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .map(|d| d.as_secs())
            .unwrap_or(0)
    )
}

fn draw_subtle_divider(ui: &mut egui::Ui) {
    ui.add_space(3.0);
    let rect = ui.available_rect_before_wrap();
    ui.painter().line_segment(
        [
            egui::pos2(rect.min.x, rect.min.y),
            egui::pos2(rect.max.x, rect.min.y),
        ],
        Stroke::new(1.0, Color32::from_rgba_premultiplied(51, 65, 85, 90)),
    );
    ui.add_space(3.0);
}

impl eframe::App for YomiFlowApp {
    fn clear_color(&self, _visuals: &egui::Visuals) -> [f32; 4] {
        [0.0, 0.0, 0.0, 0.0]
    }

    fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {
        let ctx = ui.ctx().clone();

        // 1. Always-on-top, borderless DWM, and exclude from capture
        crate::capture::force_window_topmost("YomiFlow");
        crate::capture::remove_windows_dwm_borders("YomiFlow");
        crate::capture::exclude_window_from_capture("YomiFlow");
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
                    let target_h = if self.is_expanded { 500.0 } else { 180.0 };
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

        // === SLEEK OBSIDIAN SLATE HUD FRAME ===
        let alpha = (self.config.opacity.clamp(0.4, 1.0) * 255.0) as u8;
        let bg_color = Color32::from_rgba_premultiplied(10, 14, 23, alpha);
        let border_stroke = Stroke::new(1.0, Color32::from_rgba_premultiplied(51, 65, 85, 140));

        let panel_frame = egui::Frame::new()
            .fill(bg_color)
            .stroke(border_stroke)
            .corner_radius(CornerRadius::same(12))
            .inner_margin(egui::Margin::symmetric(14, 10));

        panel_frame.show(ui, |ui| {
            // === HEADER BAR (Entire Bar is Smoothly Draggable) ===
            ui.horizontal(|ui| {
                // Left: Sleek Brand Title + Status Pill
                let title_resp = ui.add(
                    egui::Label::new(
                        RichText::new("⚡ YomiFlow")
                            .strong()
                            .size(13.5)
                            .color(Color32::from_rgb(56, 189, 248)),
                    )
                    .sense(Sense::click_and_drag()),
                );
                if title_resp.is_pointer_button_down_on() || title_resp.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                if let Some(ref res) = current_res {
                    let lat_resp = ui.add(
                        egui::Label::new(
                            RichText::new(format!("{:.1}ms", res.total_ms))
                                .size(10.5)
                                .color(Color32::from_rgb(52, 211, 153)),
                        )
                        .sense(Sense::click_and_drag()),
                    );
                    if lat_resp.is_pointer_button_down_on() || lat_resp.dragged() {
                        ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                    }
                } else if is_capturing_now {
                    ui.label(
                        RichText::new("Scanning...")
                            .size(10.5)
                            .color(Color32::from_rgb(251, 191, 36)),
                    );
                }

                // Middle: Flexible Drag Space
                let remaining_w = (ui.available_width() - 170.0).max(10.0);
                let (_, empty_drag) = ui.allocate_exact_size(Vec2::new(remaining_w, 22.0), Sense::click_and_drag());
                if empty_drag.is_pointer_button_down_on() || empty_drag.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                // Right: Minimal Action Icons
                ui.with_layout(Layout::right_to_left(Align::Center), |ui| {
                    // Minimize icon
                    if ui.add(
                        egui::Button::new(RichText::new("—").size(12.0).color(Color32::from_rgb(148, 163, 184)))
                            .fill(Color32::TRANSPARENT)
                            .stroke(Stroke::NONE),
                    ).on_hover_text("Minimize Overlay (Esc)").clicked() {
                        ctx.send_viewport_cmd(ViewportCommand::Minimized(true));
                    }

                    // Settings / Drawer Toggle
                    let gear_color = if self.is_expanded {
                        Color32::from_rgb(56, 189, 248)
                    } else {
                        Color32::from_rgb(148, 163, 184)
                    };
                    if ui.add(
                        egui::Button::new(RichText::new("⚙").size(13.0).color(gear_color))
                            .fill(Color32::TRANSPARENT)
                            .stroke(Stroke::NONE),
                    ).on_hover_text("Settings & Detailed Breakdown (F10)").clicked() {
                        self.is_expanded = !self.is_expanded;
                        let target_h = if self.is_expanded { 500.0 } else { 180.0 };
                        ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(660.0, target_h)));
                    }

                    // Copy Icon
                    if ui.add(
                        egui::Button::new(RichText::new("📋").size(12.0).color(Color32::from_rgb(148, 163, 184)))
                            .fill(Color32::TRANSPARENT)
                            .stroke(Stroke::NONE),
                    ).on_hover_text("Copy Japanese line to clipboard").clicked() {
                        if let Some(ref res) = current_res {
                            ui.ctx().copy_text(res.text.clone());
                            self.status_message = "Copied to clipboard!".to_string();
                        }
                    }

                    // Scan Icon (F8)
                    if ui.add(
                        egui::Button::new(
                            RichText::new("📷 Scan (F8)")
                                .size(11.0)
                                .strong()
                                .color(Color32::WHITE),
                        )
                        .fill(Color32::from_rgb(225, 29, 72))
                        .corner_radius(CornerRadius::same(5)),
                    ).clicked() {
                        self.trigger_capture(ctx.clone());
                    }
                });
            });

            draw_subtle_divider(ui);

            // === MAIN RECOGNIZED DIALOGUE ===
            if let Some(ref res) = current_res {
                if res.text.trim().is_empty() {
                    ui.vertical_centered(|ui| {
                        ui.add_space(8.0);
                        ui.label(RichText::new("No Japanese dialogue found in capture area.").color(Color32::from_rgb(148, 163, 184)));
                        ui.label(RichText::new("Press F8 anywhere in game or adjust capture area with ⚙").size(11.0).color(Color32::from_rgb(100, 116, 139)));
                        ui.add_space(6.0);
                    });
                } else {
                    // 1. Japanese Dialogue (Fluid typography, natural kerning, zero button boxes)
                    ui.add_space(2.0);
                    ui.horizontal_wrapped(|ui| {
                        ui.spacing_mut().item_spacing = Vec2::new(1.0, 3.0);
                        for word in &res.words {
                            if word.is_punct {
                                ui.label(RichText::new(&word.surface).size(21.0).color(Color32::from_rgb(148, 163, 184)));
                            } else {
                                let label = egui::Label::new(
                                    RichText::new(&word.surface)
                                        .size(21.0)
                                        .strong()
                                        .color(Color32::from_rgb(248, 250, 252)),
                                )
                                .sense(Sense::hover().union(Sense::click()));

                                let resp = ui.add(label);

                                // Subtle cyan underline when hovered
                                if resp.hovered() {
                                    ui.painter().line_segment(
                                        [
                                            egui::pos2(resp.rect.left(), resp.rect.bottom() - 1.0),
                                            egui::pos2(resp.rect.right(), resp.rect.bottom() - 1.0),
                                        ],
                                        Stroke::new(2.0, Color32::from_rgb(56, 189, 248)),
                                    );
                                }

                                // Floating Rich Yomitan Tooltip Card
                                let resp = resp.on_hover_ui(|ui| {
                                    let card_frame = egui::Frame::new()
                                        .fill(Color32::from_rgb(15, 23, 42))
                                        .stroke(Stroke::new(1.0, Color32::from_rgb(51, 65, 85)))
                                        .corner_radius(CornerRadius::same(8))
                                        .inner_margin(egui::Margin::symmetric(10, 8));

                                    card_frame.show(ui, |ui| {
                                        ui.horizontal(|ui| {
                                            ui.label(RichText::new(&word.surface).size(18.0).strong().color(Color32::from_rgb(56, 189, 248)));
                                            if !word.reading.is_empty() {
                                                ui.label(RichText::new(format!("【{}】", word.reading)).size(15.0).color(Color32::from_rgb(251, 191, 36)));
                                            }
                                            if word.base_form != word.surface && !word.base_form.is_empty() {
                                                ui.label(RichText::new(format!("(base: {})", word.base_form)).size(11.5).color(Color32::from_rgb(192, 132, 252)));
                                            }
                                        });

                                        if !word.meaning.is_empty() {
                                            ui.add_space(2.0);
                                            ui.label(RichText::new(&word.meaning).size(13.0).color(Color32::from_rgb(241, 245, 249)));
                                        }

                                        if !word.kanji_breakdown.is_empty() {
                                            ui.add_space(4.0);
                                            for k in &word.kanji_breakdown {
                                                ui.horizontal(|ui| {
                                                    ui.label(RichText::new(k.character.to_string()).strong().size(13.0).color(Color32::from_rgb(251, 146, 60)));
                                                    let on_str = if !k.onyomi.is_empty() { format!("[{}]", k.onyomi) } else { String::new() };
                                                    ui.label(RichText::new(format!("{} {}", on_str, k.meaning)).size(11.5).color(Color32::from_rgb(203, 213, 225)));
                                                });
                                            }
                                        }
                                    });
                                });

                                if resp.clicked() {
                                    self.is_expanded = !self.is_expanded;
                                    let target_h = if self.is_expanded { 500.0 } else { 180.0 };
                                    ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(660.0, target_h)));
                                }
                            }
                        }
                    });

                    // 2. Immediate English Translation (Directly in Compact Mode!)
                    ui.add_space(4.0);
                    if let Some(Ok(ref expl)) = current_ai {
                        if let Some(ref corr) = expl.corrected_japanese {
                            if corr.trim() != res.text.trim() {
                                ui.horizontal(|ui| {
                                    ui.label(RichText::new("✨ Clean:").size(11.5).color(Color32::from_rgb(251, 191, 36)));
                                    ui.label(RichText::new(corr).size(13.0).strong().color(Color32::from_rgb(241, 245, 249)));
                                });
                            }
                        }
                        ui.label(
                            RichText::new(format!("“{}”", expl.translation))
                                .size(13.5)
                                .italics()
                                .color(Color32::from_rgb(147, 197, 253)),
                        );
                    } else if is_ai_running {
                        ui.label(
                            RichText::new("✨ Analyzing dialogue nuance with AI...")
                                .size(12.5)
                                .italics()
                                .color(Color32::from_rgb(147, 197, 253)),
                        );
                    } else {
                        // Offline synthesized gloss from 466,247-word JMdict
                        let glosses: Vec<&str> = res.words
                            .iter()
                            .filter(|w| !w.is_punct && !w.meaning.is_empty())
                            .map(|w| {
                                let first_part = w.meaning.split(';').next().unwrap_or(w.meaning.as_str());
                                first_part.split(',').next().unwrap_or(first_part).trim()
                            })
                            .collect();
                        if !glosses.is_empty() {
                            ui.label(
                                RichText::new(format!("Gloss: {}", glosses.join(" • ")))
                                    .size(13.0)
                                    .italics()
                                    .color(Color32::from_rgb(147, 197, 253)),
                            );
                        }
                    }
                }
            } else {
                ui.vertical_centered(|ui| {
                    ui.add_space(12.0);
                    ui.label(RichText::new("🎮 Ready to capture Japanese dialogue.").strong().size(13.5).color(Color32::from_rgb(241, 245, 249)));
                    ui.label(RichText::new("Press F8 anywhere in game to capture dialogue subtitles instantly.").size(11.5).color(Color32::from_rgb(148, 163, 184)));
                    ui.add_space(8.0);
                });
            }

            // === EXPANDED SETTINGS & BREAKDOWN DRAWER ===
            if self.is_expanded {
                draw_subtle_divider(ui);

                egui::ScrollArea::vertical().max_height(300.0).show(ui, |ui| {
                    // === DRAWER SECTION 1: AI NUANCE & GRAMMAR ===
                    if let Some(ref res) = current_res {
                        if let Some(ref ai_res) = current_ai {
                            match ai_res {
                                Ok(expl) => {
                                    let card_frame = egui::Frame::new()
                                        .fill(Color32::from_rgba_premultiplied(20, 26, 43, 230))
                                        .stroke(Stroke::new(1.0, Color32::from_rgba_premultiplied(99, 102, 241, 140)))
                                        .corner_radius(CornerRadius::same(8))
                                        .inner_margin(egui::Margin::same(10));

                                    card_frame.show(ui, |ui| {
                                        ui.label(RichText::new("🤖 AI Dialogue Translation & Nuance").strong().size(12.0).color(Color32::from_rgb(165, 180, 252)));
                                        ui.add_space(2.0);
                                        ui.label(RichText::new(format!("\"{}\"", expl.translation)).strong().size(14.0).color(Color32::WHITE));

                                        if !expl.nuance.is_empty() {
                                            ui.add_space(2.0);
                                            ui.horizontal(|ui| {
                                                ui.label(RichText::new("🔥 Nuance:").strong().color(Color32::from_rgb(253, 224, 71)));
                                                ui.label(RichText::new(&expl.nuance).color(Color32::from_rgb(254, 240, 138)).size(12.0));
                                            });
                                        }

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
                        } else if !self.config.deepseek_api_key.trim().is_empty() && !is_ai_running {
                            if ui.button(RichText::new("✨ Request AI Nuance & Grammar").size(11.0).color(Color32::from_rgb(199, 210, 254))).clicked() {
                                self.trigger_ai_explanation(ctx.clone(), res.text.clone());
                            }
                            ui.add_space(4.0);
                        }

                        // === DRAWER SECTION 2: DETECTED GRAMMAR PATTERNS ===
                        if !res.grammar.is_empty() {
                            ui.label(RichText::new("Detected Grammar Patterns").strong().color(Color32::from_rgb(192, 132, 252)));
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
                        }

                        // === DRAWER SECTION 3: WORD & KANJI BREAKDOWN LIST ===
                        ui.horizontal(|ui| {
                            ui.label(RichText::new("Vocabulary Breakdown").strong().color(Color32::from_rgb(56, 189, 248)));
                            ui.with_layout(Layout::right_to_left(Align::Center), |ui| {
                                if ui.button(RichText::new("⭐ Export Anki").size(10.5)).clicked() {
                                    match self.history.export_anki_tsv("yomiflow_anki_export.txt") {
                                        Ok(n) => self.status_message = format!("Exported {} cards to yomiflow_anki_export.txt", n),
                                        Err(e) => self.status_message = format!("Export error: {}", e),
                                    }
                                }
                            });
                        });
                        ui.add_space(2.0);

                        for word in &res.words {
                            if word.is_punct {
                                continue;
                            }
                            ui.horizontal(|ui| {
                                ui.label(RichText::new(&word.surface).strong().size(13.5).color(Color32::WHITE));
                                if !word.reading.is_empty() {
                                    ui.label(RichText::new(format!("[{}]", word.reading)).size(11.5).color(Color32::from_rgb(252, 211, 77)));
                                }
                                if word.base_form != word.surface && !word.base_form.is_empty() {
                                    ui.label(RichText::new(format!("(base: {})", word.base_form)).size(11.0).color(Color32::from_rgb(192, 132, 252)));
                                }
                                if !word.meaning.is_empty() {
                                    ui.label(RichText::new(&word.meaning).size(12.0).color(Color32::from_rgb(226, 232, 240)));
                                }
                            });
                        }
                        ui.add_space(6.0);
                        draw_subtle_divider(ui);
                    }

                    // === DRAWER SECTION 4: CAPTURE SETTINGS & API KEY ===
                    ui.label(RichText::new("Overlay & Capture Box Settings").strong().color(Color32::from_rgb(251, 191, 36)));
                    ui.add_space(4.0);

                    ui.horizontal(|ui| {
                        ui.label("Snap Position:");
                        if ui.button("Top Left").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(100.0, 80.0)));
                            self.config.window_x = Some(100.0);
                            self.config.window_y = Some(80.0);
                            self.config.save();
                        }
                        if ui.button("Top Center").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(450.0, 80.0)));
                            self.config.window_x = Some(450.0);
                            self.config.window_y = Some(80.0);
                            self.config.save();
                        }
                        if ui.button("Bottom Subtitles").clicked() {
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
                        ui.label("W:");
                        ui.add(egui::DragValue::new(&mut self.config.region.width).speed(5).range(100..=3840));
                        ui.label("H:");
                        ui.add(egui::DragValue::new(&mut self.config.region.height).speed(5).range(50..=2160));
                    });

                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        ui.label("Opacity:");
                        if ui.add(egui::Slider::new(&mut self.config.opacity, 0.4..=1.0)).changed() {
                            self.config.save();
                        }
                        ui.checkbox(&mut self.config.auto_ai_explain, "Auto-run AI on capture");
                    });

                    ui.add_space(6.0);
                    ui.label(RichText::new("DeepSeek / OpenAI API Key:").strong().size(11.0).color(Color32::from_rgb(165, 180, 252)));
                    ui.horizontal(|ui| {
                        ui.add(egui::TextEdit::singleline(&mut self.config.deepseek_api_key).password(true).hint_text("sk-...")).on_hover_text("Stored locally in config.json");
                        if ui.button("💾 Save Key").clicked() {
                            self.config.save();
                            self.status_message = "API key saved!".to_string();
                        }
                    });
                });
            }
        });
    }
}
