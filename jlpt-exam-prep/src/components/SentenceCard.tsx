import React, { useState } from 'react';
import { alignSentence } from '../studyUtils';
import type { ExampleSentence } from '../types';
import { WordHoverTooltip } from './WordHoverTooltip';
import { Volume2, ChevronDown, ChevronUp, AlertCircle, Info } from 'lucide-react';

interface Props {
  sentence: ExampleSentence;
  furiganaMode: 'all' | 'hover' | 'off';
}

export const SentenceCard: React.FC<Props> = ({ sentence, furiganaMode }) => {
  const [showNuance, setShowNuance] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);

  const playAudio = () => {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(sentence.japanese);
    utterance.lang = 'ja-JP';
    utterance.rate = 0.9;

    utterance.onstart = () => setIsPlaying(true);
    utterance.onend = () => setIsPlaying(false);
    utterance.onerror = () => setIsPlaying(false);

    window.speechSynthesis.speak(utterance);
  };

  return (
    <div className="rounded-lg bg-[#fffef9] border border-[#dfded3] p-4 transition-colors">
      {/* Top Sentence Line with Audio & Japanese Tokens */}
      <div className="flex items-start justify-between gap-3">
        <div className="flex-1 leading-loose text-[#24332c]">
          {alignSentence(sentence).map((part, idx) => part.token ? (
            <WordHoverTooltip
              key={`${sentence.id}-tok-${idx}`}
              token={part.token}
              furiganaMode={furiganaMode}
            />
          ) : <span key={`${sentence.id}-text-${idx}`}>{part.text}</span>)}
        </div>

        {/* Audio Speech Button */}
        <button
          onClick={playAudio}
          title="Listen to Japanese pronunciation"
          className={`shrink-0 p-1.5 rounded transition-colors ${
            isPlaying
              ? 'bg-[#467b6b] text-white'
              : 'text-[#8a9485] hover:text-[#283b35] hover:bg-[#edece1]'
          }`}
        >
          <Volume2 className="w-4 h-4" />
        </button>
      </div>

      {/* English Natural Translation */}
      <div className="mt-2 text-xs sm:text-sm text-[#55645a] leading-relaxed">
        {sentence.english}
      </div>

      {/* Nuance & Trap Toggle Button */}
      {(sentence.nuanceNote || sentence.literal || sentence.trapAlert) && (
        <div className="mt-2.5 pt-2 border-t border-[#f0eee4]">
          <button
            onClick={() => setShowNuance(prev => !prev)}
            className="flex items-center gap-1 text-[11px] font-medium text-[#467b6b] hover:text-[#31574b] transition-colors"
          >
            <Info className="w-3 h-3" />
            <span>{showNuance ? 'Hide Sentence Nuances' : 'Sentence Nuance & Traps'}</span>
            {showNuance ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
          </button>

          {/* Expanded Breakdown Drawer */}
          {showNuance && (
            <div className="mt-2 space-y-1.5 p-2.5 rounded bg-[#f8f7f0] text-xs border border-[#e2e0d5] text-[#283b35]">
              {sentence.literal && (
                <div className="text-[#617066]">
                  <span className="font-semibold text-[#283b35]">Literal: </span>
                  <span className="italic">{sentence.literal}</span>
                </div>
              )}

              {sentence.nuanceNote && (
                <div>
                  <span className="font-semibold text-[#467b6b]">Nuance: </span>
                  <span>{sentence.nuanceNote}</span>
                </div>
              )}

              {sentence.trapAlert && (
                <div className="text-[#865a50] flex items-start gap-1.5 pt-1 border-t border-[#edebe0]">
                  <AlertCircle className="w-3.5 h-3.5 shrink-0 mt-0.5 text-[#a85a4a]" />
                  <div>
                    <span className="font-semibold">JLPT Trap: </span>
                    <span>{sentence.trapAlert}</span>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
