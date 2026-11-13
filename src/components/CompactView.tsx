import React, { useState } from 'react';
import { Copy, Check, ChevronDown, Bot } from 'lucide-react';
import { Token, Explanation } from '../types';

interface CompactViewProps {
  text: string;
  tokens: Token[];
  explanation: Explanation | null;
  onExpand: () => void;
  onExplainWithAI: () => void;
  isAiLoading: boolean;
}

export const CompactView: React.FC<CompactViewProps> = ({
  text,
  tokens,
  explanation,
  onExpand,
  onExplainWithAI,
  isAiLoading
}) => {
  const [copied, setCopied] = useState(false);
  const [showFurigana, setShowFurigana] = useState(true);

  const handleCopy = () => {
    if (!text) return;
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  if (!text) {
    return (
      <div className="flex flex-col items-center justify-center p-6 text-neutral-400 text-center select-none">
        <p className="text-sm font-medium text-neutral-300">No Japanese text captured yet.</p>
        <p className="text-xs text-neutral-500 mt-1">
          Press <span className="text-rose-400 font-mono font-semibold">F8</span> anytime while playing a game or watching a video.
        </p>
      </div>
    );
  }

  // Translation priority: Natural AI translation -> morphological word preview
  const translationText =
    explanation?.natural_translation ||
    (tokens.length > 0
      ? tokens
          .filter((t) => !t.is_punctuation)
          .map((t) => `${t.base_form} (${t.reading_hira})`)
          .slice(0, 5)
          .join(' • ')
      : '');

  return (
    <div className="p-3.5 flex flex-col gap-2.5">
      {/* Top: Japanese Sentence with Ruby/Furigana */}
      <div className="flex items-start justify-between gap-3">
        <div className="text-lg leading-relaxed font-japanese font-medium text-white tracking-wide">
          {showFurigana && tokens.length > 0 ? (
            <div className="flex flex-wrap items-end gap-x-1 gap-y-2">
              {tokens.map((token, idx) => {
                const hasKanji = token.kanji.length > 0;
                return (
                  <span
                    key={idx}
                    className={`inline-flex flex-col items-center group cursor-pointer transition px-0.5 rounded ${
                      hasKanji ? 'hover:bg-rose-500/20 text-rose-100' : 'text-neutral-200'
                    }`}
                    title={`${token.surface} [${token.reading_hira}] — Base: ${token.base_form} (${token.part_of_speech})`}
                  >
                    {hasKanji && (
                      <span className="text-[10px] text-rose-300/80 font-normal leading-none mb-0.5 select-none font-mono">
                        {token.reading_hira}
                      </span>
                    )}
                    <span className="leading-tight">{token.surface}</span>
                  </span>
                );
              })}
            </div>
          ) : (
            <p className="text-base text-neutral-100">{text}</p>
          )}
        </div>

        {/* Action icons */}
        <div className="flex items-center gap-1 shrink-0">
          <button
            onClick={() => setShowFurigana(!showFurigana)}
            title="Toggle Furigana Readings"
            className={`px-1.5 py-0.5 text-[10px] font-mono rounded border transition ${
              showFurigana
                ? 'bg-rose-500/20 text-rose-300 border-rose-500/30'
                : 'bg-white/5 text-neutral-400 border-white/10 hover:text-white'
            }`}
          >
            ふりがな
          </button>

          <button
            onClick={handleCopy}
            title="Copy Japanese sentence"
            className="p-1 text-neutral-400 hover:text-white hover:bg-white/10 rounded transition"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
          </button>
        </div>
      </div>

      {/* Translation or Summary */}
      <div className="flex items-center justify-between gap-2 pt-1 border-t border-white/5">
        <p className="text-xs text-neutral-300 italic truncate max-w-[85%] font-sans">
          {translationText || 'Scanning text...'}
        </p>

        <div className="flex items-center gap-1 shrink-0">
          {!explanation?.natural_translation && (
            <button
              onClick={onExplainWithAI}
              disabled={isAiLoading}
              title="Explain Context & Nuance with AI"
              className="flex items-center gap-1 px-2 py-0.5 text-[10px] bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 rounded border border-indigo-500/30 transition disabled:opacity-50"
            >
              <Bot className="w-3 h-3" />
              <span>{isAiLoading ? 'Analyzing...' : 'AI Explain'}</span>
            </button>
          )}

          <button
            onClick={onExpand}
            className="flex items-center gap-0.5 px-2 py-0.5 text-[10px] bg-white/10 hover:bg-white/20 text-white rounded transition"
          >
            <span>Breakdown</span>
            <ChevronDown className="w-3 h-3" />
          </button>
        </div>
      </div>
    </div>
  );
};
