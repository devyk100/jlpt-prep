import React, { useState, useEffect } from 'react';
import { Crop, X, Check, RefreshCw } from 'lucide-react';
import { AppConfig } from '../types';

interface RegionSelectorModalProps {
  config: AppConfig | null;
  onSaveConfig: (newConfig: AppConfig) => void;
  onClose: () => void;
}

export const RegionSelectorModal: React.FC<RegionSelectorModalProps> = ({
  config,
  onSaveConfig,
  onClose
}) => {
  const [x, setX] = useState<number>(config?.capture.x ?? 200);
  const [y, setY] = useState<number>(config?.capture.y ?? 720);
  const [width, setWidth] = useState<number>(config?.capture.width ?? 1520);
  const [height, setHeight] = useState<number>(config?.capture.height ?? 280);
  const [profile, setProfile] = useState<string>(config?.capture.profile ?? 'Bottom Dialogue');
  const [previewUri, setPreviewUri] = useState<string | null>(null);
  const [isLoadingPreview, setIsLoadingPreview] = useState(false);
  const [previewLatency, setPreviewLatency] = useState<number | null>(null);

  // Load preset coordinates when profile dropdown changes
  const handleProfileChange = (newProfile: string) => {
    setProfile(newProfile);
    if (config?.capture.profiles && config.capture.profiles[newProfile]) {
      const p = config.capture.profiles[newProfile];
      setX(p.x);
      setY(p.y);
      setWidth(p.width);
      setHeight(p.height);
    }
  };

  const handleTestCapture = async () => {
    if (!window.pywebview?.api) return;
    setIsLoadingPreview(true);
    try {
      const res = await window.pywebview.api.test_region_capture(x, y, width, height);
      setPreviewUri(res.data_uri);
      setPreviewLatency(res.latency_ms);
    } catch (e) {
      console.error('Test capture error:', e);
    } finally {
      setIsLoadingPreview(false);
    }
  };

  const handleSave = () => {
    if (!config) return;
    const updated: AppConfig = {
      ...config,
      capture: {
        ...config.capture,
        x,
        y,
        width,
        height,
        profile,
        profiles: {
          ...config.capture.profiles,
          [profile]: { x, y, width, height }
        }
      }
    };
    onSaveConfig(updated);
    onClose();
  };

  // Run test capture once on open
  useEffect(() => {
    handleTestCapture();
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4">
      <div className="w-full max-w-lg bg-neutral-900 border border-white/10 rounded-xl shadow-2xl overflow-hidden flex flex-col text-neutral-200">
        {/* Header */}
        <div className="flex items-center justify-between px-4 py-2.5 border-b border-white/10 bg-neutral-800/50">
          <div className="flex items-center gap-2 text-rose-400 font-semibold text-sm">
            <Crop className="w-4 h-4" />
            <span>Screen Capture Region Config</span>
          </div>
          <button onClick={onClose} className="p-1 hover:text-white rounded hover:bg-white/10">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Body */}
        <div className="p-4 flex flex-col gap-4 max-h-[75vh] overflow-y-auto text-xs">
          {/* Profile selector */}
          <div className="flex flex-col gap-1.5">
            <label className="text-neutral-400 font-medium">Capture Profile Preset</label>
            <select
              value={profile}
              onChange={(e) => handleProfileChange(e.target.value)}
              className="bg-neutral-800 border border-white/10 rounded-lg px-2.5 py-1.5 text-white focus:outline-none focus:border-rose-500"
            >
              {config?.capture.profiles &&
                Object.keys(config.capture.profiles).map((pKey) => (
                  <option key={pKey} value={pKey}>
                    {pKey} ({config.capture.profiles[pKey].width}x{config.capture.profiles[pKey].height})
                  </option>
                ))}
              <option value="Custom">Custom Region</option>
            </select>
          </div>

          {/* Coordinate inputs */}
          <div className="grid grid-cols-2 gap-3">
            <div className="flex flex-col gap-1">
              <label className="text-neutral-400">X (Left offset px)</label>
              <input
                type="number"
                value={x}
                onChange={(e) => setX(parseInt(e.target.value) || 0)}
                className="bg-neutral-800 border border-white/10 rounded-lg px-2.5 py-1.5 text-white font-mono"
              />
            </div>
            <div className="flex flex-col gap-1">
              <label className="text-neutral-400">Y (Top offset px)</label>
              <input
                type="number"
                value={y}
                onChange={(e) => setY(parseInt(e.target.value) || 0)}
                className="bg-neutral-800 border border-white/10 rounded-lg px-2.5 py-1.5 text-white font-mono"
              />
            </div>
            <div className="flex flex-col gap-1">
              <label className="text-neutral-400">Width (px)</label>
              <input
                type="number"
                value={width}
                onChange={(e) => setWidth(parseInt(e.target.value) || 100)}
                className="bg-neutral-800 border border-white/10 rounded-lg px-2.5 py-1.5 text-white font-mono"
              />
            </div>
            <div className="flex flex-col gap-1">
              <label className="text-neutral-400">Height (px)</label>
              <input
                type="number"
                value={height}
                onChange={(e) => setHeight(parseInt(e.target.value) || 50)}
                className="bg-neutral-800 border border-white/10 rounded-lg px-2.5 py-1.5 text-white font-mono"
              />
            </div>
          </div>

          {/* Live Preview Area */}
          <div className="flex flex-col gap-1.5">
            <div className="flex items-center justify-between text-neutral-400">
              <span className="font-medium">Live Region Preview</span>
              <button
                onClick={handleTestCapture}
                disabled={isLoadingPreview}
                className="flex items-center gap-1 text-[11px] text-rose-300 hover:text-white"
              >
                <RefreshCw className={`w-3 h-3 ${isLoadingPreview ? 'animate-spin' : ''}`} />
                <span>Refresh Capture</span>
                {previewLatency !== null && <span className="font-mono text-[10px]">({previewLatency}ms)</span>}
              </button>
            </div>

            <div className="w-full h-36 bg-black/60 rounded-lg border border-white/10 overflow-hidden flex items-center justify-center relative">
              {previewUri ? (
                <img
                  src={previewUri}
                  alt="Capture Region Preview"
                  className="w-full h-full object-contain"
                />
              ) : (
                <span className="text-neutral-500 italic">No preview available</span>
              )}
            </div>
            <p className="text-[10px] text-neutral-500">
              Ensure this box frames the game's dialogue box or video subtitles.
            </p>
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
            <span>Apply & Save Region</span>
          </button>
        </div>
      </div>
    </div>
  );
};
