import React, { useState } from 'react';
import { Settings, X, Check, Key, Sliders, ShieldCheck, Sparkles } from 'lucide-react';
import { AppConfig } from '../types';

interface SettingsModalProps {
  config: AppConfig | null;
  onSaveConfig: (newConfig: AppConfig) => void;
  onClose: () => void;
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  config,
  onSaveConfig,
  onClose
}) => {
  const [provider, setProvider] = useState<string>(config?.llm.provider ?? 'deepseek');
  const [model, setModel] = useState<string>(config?.llm.model ?? 'deepseek-chat');
  const [apiKey, setApiKey] = useState<string>(config?.llm.api_key ?? '');
  const [baseUrl, setBaseUrl] = useState<string>(config?.llm.base_url ?? 'https://api.deepseek.com/v1');
  const [llmEnabled, setLlmEnabled] = useState<boolean>(config?.llm.enabled ?? false);

  const [opacity, setOpacity] = useState<number>(config?.overlay.opacity ?? 0.94);
  const [alwaysOnTop, setAlwaysOnTop] = useState<boolean>(config?.overlay.always_on_top ?? true);

  const [captureKey, setCaptureKey] = useState<string>(config?.shortcuts.capture ?? 'f8');
  const [toggleKey, setToggleKey] = useState<string>(config?.shortcuts.toggle_overlay ?? 'f9');
  const [modeKey, setModeKey] = useState<string>(config?.shortcuts.toggle_mode ?? 'f10');

  const handleProviderSelect = (newProv: string) => {
    setProvider(newProv);
    if (newProv === 'deepseek') {
      setModel('deepseek-chat');
      setBaseUrl('https://api.deepseek.com/v1');
    } else if (newProv === 'gemini') {
      setModel('gemini-2.5-flash');
      setBaseUrl('');
    } else if (newProv === 'openai_compatible') {
      setModel('gpt-4o-mini');
      setBaseUrl('https://api.openai.com/v1');
    }
  };

  const handleSave = () => {
    if (!config) return;
    const updated: AppConfig = {
      ...config,
      shortcuts: {
        ...config.shortcuts,
        capture: captureKey,
        toggle_overlay: toggleKey,
        toggle_mode: modeKey
      },
      overlay: {
        ...config.overlay,
        opacity,
        always_on_top: alwaysOnTop
      },
      llm: {
        ...config.llm,
        enabled: llmEnabled,
        provider,
        model,
        api_key: apiKey,
        base_url: baseUrl
      }
    };
    onSaveConfig(updated);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4">
      <div className="w-full max-w-lg bg-neutral-900 border border-white/10 rounded-xl shadow-2xl overflow-hidden flex flex-col text-neutral-200">
        {/* Header */}
        <div className="flex items-center justify-between px-4 py-2.5 border-b border-white/10 bg-neutral-800/50">
          <div className="flex items-center gap-2 text-rose-400 font-semibold text-sm">
            <Settings className="w-4 h-4" />
            <span>YomiFlow Settings</span>
          </div>
          <button onClick={onClose} className="p-1 hover:text-white rounded hover:bg-white/10">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-4 flex flex-col gap-4.5 max-h-[75vh] overflow-y-auto text-xs">
          {/* Shortcuts section */}
          <div className="flex flex-col gap-2 p-3 rounded-lg bg-white/5 border border-white/5">
            <span className="font-semibold text-white flex items-center gap-1.5">
              <Sliders className="w-3.5 h-3.5 text-rose-400" />
              Global Keyboard Shortcuts
            </span>
            <div className="grid grid-cols-3 gap-2 mt-1">
              <div className="flex flex-col gap-1">
                <span className="text-[10px] text-neutral-400">Capture Screen</span>
                <input
                  type="text"
                  value={captureKey}
                  onChange={(e) => setCaptureKey(e.target.value.toLowerCase())}
                  className="bg-neutral-800 border border-white/10 rounded px-2 py-1 text-center font-mono text-rose-300 font-bold uppercase"
                />
              </div>
              <div className="flex flex-col gap-1">
                <span className="text-[10px] text-neutral-400">Toggle Overlay</span>
                <input
                  type="text"
                  value={toggleKey}
                  onChange={(e) => setToggleKey(e.target.value.toLowerCase())}
                  className="bg-neutral-800 border border-white/10 rounded px-2 py-1 text-center font-mono text-white font-bold uppercase"
                />
              </div>
              <div className="flex flex-col gap-1">
                <span className="text-[10px] text-neutral-400">Compact / Expand</span>
                <input
                  type="text"
                  value={modeKey}
                  onChange={(e) => setModeKey(e.target.value.toLowerCase())}
                  className="bg-neutral-800 border border-white/10 rounded px-2 py-1 text-center font-mono text-white font-bold uppercase"
                />
              </div>
            </div>
          </div>

          {/* Overlay Appearance */}
          <div className="flex flex-col gap-2 p-3 rounded-lg bg-white/5 border border-white/5">
            <span className="font-semibold text-white">Overlay Appearance</span>
            <div className="flex items-center justify-between mt-1">
              <span className="text-neutral-400">Background Opacity</span>
              <div className="flex items-center gap-2">
                <input
                  type="range"
                  min="0.5"
                  max="1.0"
                  step="0.02"
                  value={opacity}
                  onChange={(e) => setOpacity(parseFloat(e.target.value))}
                  className="w-28 accent-rose-500"
                />
                <span className="font-mono text-[11px] text-neutral-300 w-8">{Math.round(opacity * 100)}%</span>
              </div>
            </div>
            <div className="flex items-center justify-between pt-1 border-t border-white/5">
              <span className="text-neutral-400">Always On Top</span>
              <input
                type="checkbox"
                checked={alwaysOnTop}
                onChange={(e) => setAlwaysOnTop(e.target.checked)}
                className="accent-rose-500 w-4 h-4 cursor-pointer"
              />
            </div>
          </div>

          {/* LLM Fallback Provider */}
          <div className="flex flex-col gap-2.5 p-3 rounded-lg bg-white/5 border border-white/5">
            <div className="flex items-center justify-between">
              <span className="font-semibold text-white flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
                AI Nuance & Context Engine (Fallback)
              </span>
              <label className="flex items-center gap-1.5 text-[11px] text-neutral-300 cursor-pointer">
                <input
                  type="checkbox"
                  checked={llmEnabled}
                  onChange={(e) => setLlmEnabled(e.target.checked)}
                  className="accent-indigo-500 w-3.5 h-3.5"
                />
                <span>Auto Explain on Capture</span>
              </label>
            </div>

            <p className="text-[10px] text-neutral-400 leading-normal">
              Local OCR and Japanese dictionary analysis run instantly at 0 cost. The LLM is used as a fallback for deep nuance, implied subjects, and colloquial expressions.
            </p>

            <div className="grid grid-cols-2 gap-2 mt-1">
              <div className="flex flex-col gap-1">
                <span className="text-neutral-400">Provider</span>
                <select
                  value={provider}
                  onChange={(e) => handleProviderSelect(e.target.value)}
                  className="bg-neutral-800 border border-white/10 rounded-lg px-2 py-1.5 text-white"
                >
                  <option value="deepseek">DeepSeek (Cheapest ~$0.14/M tokens)</option>
                  <option value="gemini">Google Gemini (Gemini 2.5 Flash / Free Tier)</option>
                  <option value="openai_compatible">OpenAI Compatible / Local Ollama</option>
                </select>
              </div>

              <div className="flex flex-col gap-1">
                <span className="text-neutral-400">Model Name</span>
                <input
                  type="text"
                  value={model}
                  onChange={(e) => setModel(e.target.value)}
                  className="bg-neutral-800 border border-white/10 rounded-lg px-2 py-1.5 text-white font-mono"
                />
              </div>
            </div>

            <div className="flex flex-col gap-1 mt-1">
              <div className="flex items-center justify-between">
                <span className="text-neutral-400 flex items-center gap-1">
                  <Key className="w-3 h-3 text-amber-400" />
                  API Key
                </span>
                <span className="text-[10px] text-emerald-400 flex items-center gap-1">
                  <ShieldCheck className="w-3 h-3" />
                  Stored locally only
                </span>
              </div>
              <input
                type="password"
                placeholder={provider === 'gemini' ? 'AIzaSy...' : 'sk-...'}
                value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                className="bg-neutral-800 border border-white/10 rounded-lg px-2.5 py-1.5 text-white font-mono"
              />
            </div>

            {provider === 'openai_compatible' && (
              <div className="flex flex-col gap-1">
                <span className="text-neutral-400">Base URL</span>
                <input
                  type="text"
                  placeholder="https://api.openai.com/v1"
                  value={baseUrl}
                  onChange={(e) => setBaseUrl(e.target.value)}
                  className="bg-neutral-800 border border-white/10 rounded-lg px-2.5 py-1.5 text-white font-mono"
                />
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className="flex items-center justify-end gap-2 px-4 py-2.5 border-t border-white/10 bg-neutral-800/30">
          <button
            onClick={onClose}
            className="px-3 py-1.5 text-neutral-400 hover:text-white text-xs rounded transition"
          >
            Cancel
          </button>
          <button
            onClick={handleSave}
            className="flex items-center gap-1.5 px-3.5 py-1.5 bg-rose-500 hover:bg-rose-600 text-white font-medium text-xs rounded-lg transition active:scale-95 shadow-lg shadow-rose-500/20"
          >
            <Check className="w-3.5 h-3.5" />
            <span>Save Settings</span>
          </button>
        </div>
      </div>
    </div>
  );
};
