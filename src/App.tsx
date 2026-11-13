import { useState, useEffect, useCallback } from 'react';
import { OverlayHeader } from './components/OverlayHeader';
import { CompactView } from './components/CompactView';
import { ExpandedView } from './components/ExpandedView';
import { RegionSelectorModal } from './components/RegionSelectorModal';
import { HistoryModal } from './components/HistoryModal';
import { SettingsModal } from './components/SettingsModal';
import { CapturePayload, AppConfig } from './types';

export function App() {
  const [config, setConfig] = useState<AppConfig | null>(null);
  const [isExpanded, setIsExpanded] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isAiLoading, setIsAiLoading] = useState(false);
  const [captureData, setCaptureData] = useState<CapturePayload | null>(null);

  // Modals
  const [isRegionOpen, setIsRegionOpen] = useState(false);
  const [isHistoryOpen, setIsHistoryOpen] = useState(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);

  // Load config on mount
  useEffect(() => {
    const initConfig = async () => {
      if (window.pywebview?.api) {
        try {
          const cfg = await window.pywebview.api.get_config();
          setConfig(cfg);
        } catch (e) {
          console.error('Failed to load initial config:', e);
        }
      }
    };
    initConfig();
  }, []);

  // Window resize sync with mode change
  const updateWindowSize = useCallback(
    async (expanded: boolean) => {
      if (!window.pywebview?.api) return;
      const width = config?.overlay.width ?? 640;
      const height = expanded
        ? (config?.overlay.expanded_height ?? 580)
        : (config?.overlay.height ?? 240);
      try {
        await window.pywebview.api.resize_window(width, height);
      } catch (e) {
        console.error('Failed to resize window:', e);
      }
    },
    [config]
  );

  const toggleExpand = () => {
    setIsExpanded((prev) => {
      const next = !prev;
      updateWindowSize(next);
      return next;
    });
  };

  // Main capture action
  const handleCapture = async () => {
    if (!window.pywebview?.api || isProcessing) return;
    setIsProcessing(true);
    try {
      const res = await window.pywebview.api.capture_and_process(true);
      setCaptureData(res);
    } catch (e) {
      console.error('Capture failed:', e);
    } finally {
      setIsProcessing(false);
    }
  };

  // Explain with AI
  const handleExplainWithAI = async () => {
    if (!window.pywebview?.api || !captureData?.text || isAiLoading) return;
    setIsAiLoading(true);
    try {
      const expl = await window.pywebview.api.explain_with_ai(captureData.text);
      setCaptureData((prev) => (prev ? { ...prev, explanation: expl } : null));
    } catch (e) {
      console.error('AI explanation error:', e);
    } finally {
      setIsAiLoading(false);
    }
  };

  // Minimize
  const handleMinimize = async () => {
    if (window.pywebview?.api) {
      await window.pywebview.api.minimize_window();
    }
  };

  // Event Listeners for global shortcuts dispatched from Python
  useEffect(() => {
    const onCaptured = (e: Event) => {
      const detail = (e as CustomEvent).detail as CapturePayload;
      setCaptureData(detail);
      setIsProcessing(false);
    };

    const onToggleMode = () => {
      toggleExpand();
    };

    const onSaveHistory = () => {
      console.log('Sentence saved to history via shortcut');
    };

    const onDismiss = () => {
      handleMinimize();
    };

    window.addEventListener('yomiflow-captured', onCaptured);
    window.addEventListener('yomiflow-toggle-mode', onToggleMode);
    window.addEventListener('yomiflow-save-history', onSaveHistory);
    window.addEventListener('yomiflow-dismiss', onDismiss);

    return () => {
      window.removeEventListener('yomiflow-captured', onCaptured);
      window.removeEventListener('yomiflow-toggle-mode', onToggleMode);
      window.removeEventListener('yomiflow-save-history', onSaveHistory);
      window.removeEventListener('yomiflow-dismiss', onDismiss);
    };
  }, [toggleExpand]);

  const opacityVal = config?.overlay.opacity ?? 0.94;

  return (
    <div className="w-screen h-screen p-1.5 flex flex-col box-border font-sans antialiased select-none overflow-hidden">
      {/* Translucent Glassmorphism Overlay Container */}
      <div
        className="w-full h-full flex flex-col rounded-xl border border-white/10 shadow-2xl backdrop-blur-xl transition-all duration-200 overflow-hidden"
        style={{
          backgroundColor: `rgba(18, 18, 22, ${opacityVal})`
        }}
      >
        {/* Header Bar */}
        <OverlayHeader
          isExpanded={isExpanded}
          onToggleExpand={toggleExpand}
          onCapture={handleCapture}
          onOpenRegion={() => setIsRegionOpen(true)}
          onOpenHistory={() => setIsHistoryOpen(true)}
          onOpenSettings={() => setIsSettingsOpen(true)}
          onMinimize={handleMinimize}
          isProcessing={isProcessing}
          latencyMs={captureData ? captureData.total_ms : undefined}
          isCached={captureData?.is_cached}
        />

        {/* View Mode: Compact vs Expanded */}
        <div className="flex-1 overflow-hidden flex flex-col">
          <CompactView
            text={captureData?.text ?? ''}
            tokens={captureData?.tokens ?? []}
            explanation={captureData?.explanation ?? null}
            onExpand={toggleExpand}
            onExplainWithAI={handleExplainWithAI}
            isAiLoading={isAiLoading}
          />

          {isExpanded && (
            <ExpandedView
              tokens={captureData?.tokens ?? []}
              kanji={captureData?.kanji ?? []}
              explanation={captureData?.explanation ?? null}
              onSaveHistory={() => {}}
            />
          )}
        </div>
      </div>

      {/* Modals */}
      {isRegionOpen && (
        <RegionSelectorModal
          config={config}
          onSaveConfig={(updated) => {
            setConfig(updated);
            window.pywebview?.api?.save_config(updated);
          }}
          onClose={() => setIsRegionOpen(false)}
        />
      )}

      {isHistoryOpen && <HistoryModal onClose={() => setIsHistoryOpen(false)} />}

      {isSettingsOpen && (
        <SettingsModal
          config={config}
          onSaveConfig={(updated) => {
            setConfig(updated);
            window.pywebview?.api?.save_config(updated);
          }}
          onClose={() => setIsSettingsOpen(false)}
        />
      )}
    </div>
  );
}

export default App;
