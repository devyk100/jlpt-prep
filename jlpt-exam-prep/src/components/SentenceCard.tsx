import { AnnotatedText } from './AnnotatedText';
import React, { useState, useEffect } from 'react';
import type { ExampleSentence } from '../types';
import { Volume2, Eye, EyeOff, ChevronDown, ChevronUp, AlertCircle, Info } from 'lucide-react';

interface Props {
  sentence: ExampleSentence;
  furiganaMode: 'book' | 'all' | 'hover' | 'off';
  forceShowMeaning?: boolean;
}

export const SentenceCard: React.FC<Props> = ({
  sentence,
  furiganaMode,
  forceShowMeaning
}) => {
  const [showMeaning, setShowMeaning] = useState<boolean>(false);
  const [showLiteral, setShowLiteral] = useState<boolean>(false);
  const [showNuance, setShowNuance] = useState<boolean>(false);
  const [isPlaying, setIsPlaying] = useState(false);

  // Sync with batch toggle when explicitly toggled by user
  useEffect(() => {
    if (forceShowMeaning !== undefined) {
      setShowMeaning(forceShowMeaning);
    }
  }, [forceShowMeaning]);

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
    <div className="rounded-lg bg-[#fffef9] border border-[#dfded3] p-4 transition-colors space-y-3">
      {/* Category / Context tag (clean, does not reveal full sentence translation) */}
      {sentence.useLabel && (
        <div className="flex items-center gap-1.5">
          <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-[#eaf4ef] text-[#2d5247] border border-[#c4ded2]">
            {sentence.useLabel}
          </span>
        </div>
      )}

      {/* Japanese Sentence Display with Audio Button */}
      <div className="flex items-start justify-between gap-3">
        <div className="flex-1 font-serif-ja text-base sm:text-lg leading-loose text-[#1e2d26]">
          <AnnotatedText text={sentence.japanese} />
        </div>

        {/* Audio Speech Button */}
        <button
          type="button"
          onClick={playAudio}
          title="Listen to Japanese pronunciation"
          aria-label="Listen to Japanese pronunciation"
          className={`shrink-0 p-1.5 rounded transition-colors ${
            isPlaying
              ? 'bg-[#467b6b] text-white'
              : 'text-[#8a9485] hover:text-[#283b35] hover:bg-[#edece1]'
          }`}
        >
          <Volume2 className="w-4 h-4" />
        </button>
      </div>

      {/* Sentence Interaction Controls Bar */}
      <div className="flex flex-wrap items-center gap-2 pt-1 border-t border-[#f0eee4] text-xs">
        {/* Toggle Meaning Button */}
        <button
          type="button"
          onClick={() => setShowMeaning(prev => !prev)}
          aria-expanded={showMeaning}
          aria-controls={`meaning-${sentence.id}`}
          className={`flex items-center gap-1.5 px-2.5 py-1 rounded text-[11.5px] font-semibold transition-all ${
            showMeaning
              ? 'bg-[#edece1] text-[#283b35] border border-[#cfcebe]'
              : 'bg-[#fffef9] text-[#467b6b] border border-[#cfcebe] hover:bg-[#f6f5ef]'
          }`}
        >
          {showMeaning ? (
            <>
              <EyeOff className="w-3.5 h-3.5 text-[#788278]" />
              <span>Hide meaning</span>
            </>
          ) : (
            <>
              <Eye className="w-3.5 h-3.5 text-[#467b6b]" />
              <span>Show meaning</span>
            </>
          )}
        </button>

        {/* Nuance & Traps Button (if available) */}
        {(sentence.nuanceNote || sentence.trapAlert) && (
          <button
            type="button"
            onClick={() => setShowNuance(prev => !prev)}
            aria-expanded={showNuance}
            aria-controls={`nuance-${sentence.id}`}
            className="flex items-center gap-1 px-2 py-1 rounded text-[11px] font-medium text-[#617066] hover:text-[#283b35] hover:bg-[#edece1] transition-colors"
          >
            <Info className="w-3 h-3 text-[#788278]" />
            <span>{showNuance ? 'Hide notes' : 'Notes & Nuance'}</span>
            {showNuance ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
          </button>
        )}
      </div>

      {/* English Natural Translation (Revealed on request) */}
      {showMeaning && (
        <div
          id={`meaning-${sentence.id}`}
          className="p-3 rounded-md bg-[#faf9f5] border border-[#dfded3] text-xs sm:text-sm text-[#3b4841] leading-relaxed animate-in fade-in duration-150 space-y-2"
        >
          <div>
            <span className="font-semibold text-[#1e2d26] mr-1">Translation:</span>
            <span>{sentence.english}</span>
          </div>

          {/* Literal Breakdown Toggle (Separately controlled) */}
          {sentence.literal && (
            <div className="pt-2 border-t border-[#edebe0]">
              <button
                type="button"
                onClick={() => setShowLiteral(prev => !prev)}
                aria-expanded={showLiteral}
                className="text-[11px] font-semibold text-[#467b6b] hover:underline flex items-center gap-1"
              >
                <span>{showLiteral ? 'Hide literal breakdown' : 'Show literal breakdown'}</span>
                {showLiteral ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
              </button>

              {showLiteral && (
                <div className="mt-1 text-[11.5px] text-[#617066] italic bg-white p-2 rounded border border-[#dfded3]">
                  <span className="font-semibold text-[#283b35] not-italic mr-1">Literal:</span>
                  <AnnotatedText text={sentence.literal} />
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Nuance & Traps Drawer (Separately controlled) */}
      {showNuance && (
        <div
          id={`nuance-${sentence.id}`}
          className="p-3 rounded-md bg-[#fdfaf3] border border-[#d8d0ba] text-xs text-[#283b35] space-y-2 animate-in fade-in duration-150"
        >
          {sentence.nuanceNote && (
            <div>
              <span className="font-bold text-[#8f7142] mr-1">Usage Nuance:</span>
              <span><AnnotatedText text={sentence.nuanceNote} /></span>
            </div>
          )}

          {sentence.trapAlert && (
            <div className="pt-1.5 border-t border-[#edebe0] text-[#865a50] flex items-start gap-1.5">
              <AlertCircle className="w-3.5 h-3.5 shrink-0 mt-0.5 text-[#a85a4a]" />
              <div>
                <span className="font-bold">JLPT Trap Alert:</span>{' '}
                <span><AnnotatedText text={sentence.trapAlert} /></span>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default SentenceCard;
