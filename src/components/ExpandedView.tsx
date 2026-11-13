import React, { useState } from 'react';
import { BookOpen, Sparkles, Languages, Bookmark, Check } from 'lucide-react';
import { Token, Explanation } from '../types';

interface ExpandedViewProps {
  tokens: Token[];
  kanji: string[];
  explanation: Explanation | null;
  onSaveHistory: () => void;
}

export const ExpandedView: React.FC<ExpandedViewProps> = ({
  tokens,
  kanji,
  explanation,
  onSaveHistory
}) => {
  const [activeTab, setActiveTab] = useState<'vocab' | 'grammar' | 'kanji'>('vocab');
  const [saved, setSaved] = useState(false);

  const handleSave = () => {
    onSaveHistory();
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  };

  const contentTokens = tokens.filter((t) => !t.is_punctuation);

  return (
    <div className="flex flex-col h-full overflow-hidden px-3.5 pb-3 pt-1 border-t border-white/10">
      {/* Navigation tabs */}
      <div className="flex items-center justify-between border-b border-white/10 pb-1.5 mb-2.5">
        <div className="flex items-center gap-1.5 text-xs">
          <button
            onClick={() => setActiveTab('vocab')}
            className={`flex items-center gap-1 px-2.5 py-1 rounded-md font-medium transition ${
              activeTab === 'vocab'
                ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                : 'text-neutral-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>Vocabulary ({contentTokens.length})</span>
          </button>

          <button
            onClick={() => setActiveTab('grammar')}
            className={`flex items-center gap-1 px-2.5 py-1 rounded-md font-medium transition ${
              activeTab === 'grammar'
                ? 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30'
                : 'text-neutral-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>Grammar & Nuance</span>
          </button>

          <button
            onClick={() => setActiveTab('kanji')}
            className={`flex items-center gap-1 px-2.5 py-1 rounded-md font-medium transition ${
              activeTab === 'kanji'
                ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                : 'text-neutral-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <Languages className="w-3.5 h-3.5" />
            <span>Kanji ({kanji.length})</span>
          </button>
        </div>

        <button
          onClick={handleSave}
          title="Save Sentence & Tokens to History"
          className="flex items-center gap-1 px-2.5 py-1 text-xs font-medium bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 rounded-md border border-emerald-500/30 transition active:scale-95"
        >
          {saved ? <Check className="w-3.5 h-3.5" /> : <Bookmark className="w-3.5 h-3.5" />}
          <span>{saved ? 'Saved!' : 'Save'}</span>
        </button>
      </div>

      {/* Tab Content Container */}
      <div className="flex-1 overflow-y-auto pr-1">
        {/* Tab 1: Vocabulary Breakdown */}
        {activeTab === 'vocab' && (
          <div className="flex flex-col gap-2">
            {contentTokens.length === 0 ? (
              <p className="text-xs text-neutral-500 italic py-4 text-center">No vocabulary tokens detected.</p>
            ) : (
              contentTokens.map((tok, idx) => (
                <div
                  key={idx}
                  className="flex items-start justify-between p-2 rounded-lg bg-white/5 border border-white/5 hover:border-white/10 transition"
                >
                  <div className="flex flex-col gap-0.5">
                    <div className="flex items-baseline gap-2">
                      <span className="text-sm font-semibold text-white tracking-wide">{tok.surface}</span>
                      <span className="text-xs text-rose-300 font-mono">[{tok.reading_hira}]</span>
                      {tok.base_form !== tok.surface && (
                        <span className="text-[11px] text-neutral-400 font-mono">
                          Base: <strong className="text-neutral-200">{tok.base_form}</strong>
                        </span>
                      )}
                    </div>

                    <div className="flex flex-wrap items-center gap-1 text-[11px] text-neutral-400 mt-0.5">
                      <span className="px-1.5 py-0.2 rounded bg-neutral-800 text-neutral-300 border border-neutral-700">
                        {tok.part_of_speech}
                      </span>
                      {tok.conjugation_form && (
                        <span className="px-1.5 py-0.2 rounded bg-indigo-950 text-indigo-300 border border-indigo-800">
                          {tok.conjugation_form}
                        </span>
                      )}
                      {tok.conjugation_type && (
                        <span className="text-[10px] text-neutral-500">{tok.conjugation_type}</span>
                      )}
                    </div>
                  </div>

                  {tok.kanji.length > 0 && (
                    <div className="flex items-center gap-1 shrink-0">
                      {tok.kanji.map((k, ki) => (
                        <span
                          key={ki}
                          className="w-6 h-6 rounded bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs flex items-center justify-center font-japanese font-semibold"
                        >
                          {k}
                        </span>
                      ))}
                    </div>
                  )}
                </div>
              ))
            )}
          </div>
        )}

        {/* Tab 2: Grammar & Nuance */}
        {activeTab === 'grammar' && (
          <div className="flex flex-col gap-3 text-xs leading-relaxed">
            {explanation ? (
              <>
                {explanation.natural_translation && (
                  <div className="p-2.5 rounded-lg bg-neutral-800/60 border border-white/10">
                    <span className="text-[10px] uppercase font-semibold text-rose-400 block mb-0.5">
                      Natural English Translation
                    </span>
                    <p className="text-sm text-neutral-100 font-medium">"{explanation.natural_translation}"</p>
                  </div>
                )}

                {explanation.literal_translation && (
                  <div className="p-2.5 rounded-lg bg-neutral-800/40 border border-white/5">
                    <span className="text-[10px] uppercase font-semibold text-neutral-400 block mb-0.5">
                      Literal Meaning
                    </span>
                    <p className="text-xs text-neutral-300 italic">{explanation.literal_translation}</p>
                  </div>
                )}

                {explanation.grammar_notes && explanation.grammar_notes.length > 0 && (
                  <div className="p-2.5 rounded-lg bg-indigo-950/30 border border-indigo-500/20">
                    <span className="text-[10px] uppercase font-semibold text-indigo-300 block mb-1.5">
                      Grammar Notes & Structures
                    </span>
                    <ul className="list-disc list-inside space-y-1 text-neutral-200">
                      {explanation.grammar_notes.map((note, i) => (
                        <li key={i}>{note}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {explanation.nuance && (
                  <div className="p-2.5 rounded-lg bg-amber-950/20 border border-amber-500/20">
                    <span className="text-[10px] uppercase font-semibold text-amber-300 block mb-1">
                      Contextual Nuance & Tone
                    </span>
                    <p className="text-neutral-200">{explanation.nuance}</p>
                  </div>
                )}
              </>
            ) : (
              <div className="text-center py-6 text-neutral-400">
                <p>No AI explanation requested yet for this sentence.</p>
                <p className="text-[11px] text-neutral-500 mt-1">
                  Click <strong className="text-indigo-400">AI Explain</strong> or enable automatic AI analysis in Settings.
                </p>
              </div>
            )}
          </div>
        )}

        {/* Tab 3: Kanji Breakdown */}
        {activeTab === 'kanji' && (
          <div className="flex flex-col gap-2">
            {kanji.length === 0 ? (
              <p className="text-xs text-neutral-500 italic py-4 text-center">No kanji characters in this sentence.</p>
            ) : (
              <div className="grid grid-cols-2 gap-2">
                {kanji.map((k, idx) => (
                  <div
                    key={idx}
                    className="flex items-center gap-3 p-2.5 rounded-lg bg-white/5 border border-white/5"
                  >
                    <div className="w-10 h-10 rounded-lg bg-rose-500/10 border border-rose-500/20 text-rose-300 flex items-center justify-center text-xl font-japanese font-bold">
                      {k}
                    </div>
                    <div className="flex flex-col">
                      <span className="text-xs font-semibold text-white font-japanese">{k}</span>
                      <span className="text-[10px] text-neutral-400">Unicode U+{k.charCodeAt(0).toString(16).toUpperCase()}</span>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
