import React, { useState, useMemo } from 'react';
import { orderQuestion } from '../studyUtils';
import type { QuizQuestion } from '../types';
import { Check, X, HelpCircle, Bookmark, BookmarkCheck, Lightbulb } from 'lucide-react';

interface Props {
  question: QuizQuestion;
  onAnswerSaved?: (questionId: string, isCorrect: boolean, chosenIndex: number) => void;
  isFlagged?: boolean;
  onToggleFlag?: (questionId: string) => void;
}

export const QuizCard: React.FC<Props> = ({
  question: originalQuestion,
  onAnswerSaved,
  isFlagged = false,
  onToggleFlag
}) => {
  const question = useMemo(() => orderQuestion(originalQuestion), [originalQuestion]);
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
  const [isRevealed, setIsRevealed] = useState(false);

  const handleSelect = (idx: number) => {
    if (isRevealed) return;
    setSelectedIndex(idx);
    setIsRevealed(true);

    const isCorrect = idx === question.correctIndex;
    if (onAnswerSaved) {
      onAnswerSaved(question.id, isCorrect, idx);
    }
  };

  const handleReset = () => {
    setSelectedIndex(null);
    setIsRevealed(false);
  };

  const isUserCorrect = selectedIndex === question.correctIndex;

  return (
    <div className="rounded-lg bg-[#fffef9] border border-[#dfded3] p-5 transition-colors">
      {/* Question Header & Bookmark */}
      <div className="flex items-start justify-between gap-3 mb-2.5">
        <div className="flex items-center gap-2">
          <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-[#edebe0] text-[#617066]">
            Check
          </span>
          <span className="text-xs text-[#788278]">{question.grammarFocus}</span>
        </div>

        {onToggleFlag && (
          <button
            onClick={() => onToggleFlag(question.id)}
            title={isFlagged ? 'Remove from Weak Points' : 'Flag to Weak Points'}
            className={`p-1 rounded transition-colors ${
              isFlagged ? 'text-[#8f7142]' : 'text-[#8a9485] hover:text-[#283b35]'
            }`}
          >
            {isFlagged ? <BookmarkCheck className="w-4 h-4" /> : <Bookmark className="w-4 h-4" />}
          </button>
        )}
      </div>

      {/* Japanese Question Prompt */}
      <div className="font-serif-ja text-base sm:text-lg font-bold text-[#1e2d26] leading-relaxed mb-1">
        {question.question}
      </div>

      {/* English Meaning Prompt */}
      <div className="text-xs text-[#788278] mb-4 italic">
        "{question.translation}"
      </div>

      {/* Options List */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-4">
        {question.options.map((opt, idx) => {
          let btnStyle = 'border-[#dfded3] bg-[#faf9f5] hover:bg-[#edece1] text-[#283b35]';

          if (isRevealed) {
            if (idx === question.correctIndex) {
              btnStyle = 'border-[#467b6b] bg-[#eef4ec] text-[#2e4d3a] font-semibold';
            } else if (idx === selectedIndex) {
              btnStyle = 'border-[#a85a4a] bg-[#f7efed] text-[#7a3b30] font-semibold';
            } else {
              btnStyle = 'opacity-40 border-[#dfded3] bg-[#f5f4ed] text-[#8a9485]';
            }
          }

          return (
            <button
              key={`${question.id}-opt-${idx}`}
              onClick={() => handleSelect(idx)}
              disabled={isRevealed}
              className={`flex items-center justify-between p-2.5 rounded border text-left text-xs sm:text-sm transition-colors ${btnStyle}`}
            >
              <div className="flex items-center gap-2">
                <span className="w-5 h-5 rounded bg-[#e8e7dc] flex items-center justify-center text-[10px] font-bold text-[#617066]">
                  {idx + 1}
                </span>
                <span className="font-medium">{opt}</span>
              </div>

              {isRevealed && idx === question.correctIndex && (
                <Check className="w-4 h-4 text-[#467b6b] shrink-0" />
              )}
              {isRevealed && idx === selectedIndex && idx !== question.correctIndex && (
                <X className="w-4 h-4 text-[#a85a4a] shrink-0" />
              )}
            </button>
          );
        })}
      </div>

      {/* Result & Deep Option Explanations */}
      {isRevealed && (
        <div className="space-y-2.5 pt-3 border-t border-[#dfded3] text-xs">
          {/* Banner */}
          <div className={`p-2.5 rounded flex items-center justify-between gap-3 ${
            isUserCorrect
              ? 'bg-[#eef4ec] text-[#2e4d3a] border border-[#cfded0]'
              : 'bg-[#f7efed] text-[#7a3b30] border border-[#e8d2cc]'
          }`}>
            <span className="font-semibold">
              {isUserCorrect ? 'Correct! Well recognized.' : 'Incorrect. Notice the rule below:'}
            </span>

            <button
              onClick={handleReset}
              className="text-[11px] font-semibold underline underline-offset-2 hover:opacity-80"
            >
              Retry
            </button>
          </div>

          {/* Golden Rule Hint */}
          {question.ruleHint && (
            <div className="p-2.5 rounded bg-[#fbf8f0] text-[#5c4a28] border border-[#d8d0ba] flex items-start gap-2">
              <Lightbulb className="w-3.5 h-3.5 text-[#8f7142] shrink-0 mt-0.5" />
              <div>
                <span className="font-bold">Rule: </span>
                <span>{question.ruleHint}</span>
              </div>
            </div>
          )}

          {/* 4-Way Analysis of Options */}
          <div className="space-y-1.5 mt-2">
            <div className="text-[10px] font-bold text-[#788278] uppercase tracking-wider">
              Option Breakdown
            </div>

            <div className="space-y-1.5">
              {question.explanations.map((exp, idx) => {
                const isThisCorrect = idx === question.correctIndex;
                const wasChosen = idx === selectedIndex;

                return (
                  <div
                    key={`${question.id}-exp-${idx}`}
                    className={`p-2 rounded border text-xs leading-relaxed ${
                      isThisCorrect
                        ? 'bg-[#eef4ec] border-[#cfded0] text-[#2e4d3a]'
                        : wasChosen
                        ? 'bg-[#f7efed] border-[#e8d2cc] text-[#7a3b30]'
                        : 'bg-[#faf9f5] border-[#e8e7dc] text-[#617066]'
                    }`}
                  >
                    <span className="font-semibold mr-1">
                      {idx + 1}. {exp.text} — {isThisCorrect ? 'Correct: ' : 'Wrong: '}
                    </span>
                    <span>{exp.reason}</span>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
