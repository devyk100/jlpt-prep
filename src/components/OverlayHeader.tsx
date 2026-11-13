import React from 'react';
import { Camera, Maximize2, Minimize2, Crop, History, Settings, Minus, Sparkles } from 'lucide-react';

interface OverlayHeaderProps {
  isExpanded: boolean;
  onToggleExpand: () => void;
  onCapture: () => void;
  onOpenRegion: () => void;
  onOpenHistory: () => void;
  onOpenSettings: () => void;
  onMinimize: () => void;
  isProcessing: boolean;
  latencyMs?: number;
  isCached?: boolean;
}

export const OverlayHeader: React.FC<OverlayHeaderProps> = ({
  isExpanded,
  onToggleExpand,
  onCapture,
  onOpenRegion,
  onOpenHistory,
  onOpenSettings,
  onMinimize,
  isProcessing,
  latencyMs,
  isCached
}) => {
  return (
    <div
      className="flex items-center justify-between px-3 py-1.5 border-b border-white/10 select-none bg-neutral-900/60 backdrop-blur-md cursor-move rounded-t-xl"
      style={{ WebkitAppRegion: 'drag' } as React.CSSProperties}
    >
      {/* Left: Branding & Status */}
      <div className="flex items-center gap-2">
        <div className="flex items-center gap-1.5 font-semibold text-xs tracking-wide text-rose-400">
          <Sparkles className="w-3.5 h-3.5 text-rose-400 animate-pulse" />
          <span>YomiFlow</span>
          <span className="text-[10px] text-neutral-400 font-normal">読みフロー</span>
        </div>

        {latencyMs !== undefined && (
          <span
            className={`text-[10px] px-1.5 py-0.5 rounded-full font-mono font-medium ${
              isCached
                ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                : 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30'
            }`}
          >
            {isCached ? 'Cached' : `${latencyMs}ms`}
          </span>
        )}

        {isProcessing && (
          <span className="flex items-center gap-1 text-[10px] text-amber-300 animate-pulse bg-amber-500/20 px-1.5 py-0.5 rounded-full border border-amber-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-ping" />
            Scanning...
          </span>
        )}
      </div>

      {/* Right: Controls (non-draggable) */}
      <div
        className="flex items-center gap-1 text-neutral-400"
        style={{ WebkitAppRegion: 'no-drag' } as React.CSSProperties}
      >
        <button
          onClick={onCapture}
          disabled={isProcessing}
          title="Capture Screen Now (F8)"
          className="flex items-center gap-1 px-2 py-0.5 text-[11px] font-medium bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 hover:text-white rounded transition border border-rose-500/30 active:scale-95 disabled:opacity-50"
        >
          <Camera className="w-3 h-3" />
          <span>F8</span>
        </button>

        <button
          onClick={onOpenRegion}
          title="Configure Capture Region"
          className="p-1 hover:text-white hover:bg-white/10 rounded transition"
        >
          <Crop className="w-3.5 h-3.5" />
        </button>

        <button
          onClick={onOpenHistory}
          title="Reading History (F11 to save)"
          className="p-1 hover:text-white hover:bg-white/10 rounded transition"
        >
          <History className="w-3.5 h-3.5" />
        </button>

        <button
          onClick={onOpenSettings}
          title="Settings & LLM Configuration"
          className="p-1 hover:text-white hover:bg-white/10 rounded transition"
        >
          <Settings className="w-3.5 h-3.5" />
        </button>

        <div className="w-[1px] h-3 bg-white/20 mx-0.5" />

        <button
          onClick={onToggleExpand}
          title={isExpanded ? 'Compact View (F10)' : 'Expanded Breakdown (F10)'}
          className="p-1 hover:text-white hover:bg-white/10 rounded transition"
        >
          {isExpanded ? <Minimize2 className="w-3.5 h-3.5" /> : <Maximize2 className="w-3.5 h-3.5" />}
        </button>

        <button
          onClick={onMinimize}
          title="Minimize Overlay (Esc)"
          className="p-1 hover:text-white hover:bg-white/10 rounded transition"
        >
          <Minus className="w-3.5 h-3.5" />
        </button>
      </div>
    </div>
  );
};
