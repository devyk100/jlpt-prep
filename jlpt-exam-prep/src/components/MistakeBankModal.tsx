import { useModal } from '../useModal';
import React from 'react';
import type { QuizQuestion } from '../types';
import { QuizCard } from './QuizCard';
import { BookmarkCheck, X, Trash2 } from 'lucide-react';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  questions: QuizQuestion[];
  flaggedIds: string[];
  onToggleFlag: (questionId: string) => void;
  onAnswerSaved: (questionId: string, isCorrect: boolean, chosenIndex: number) => void;
  onClearAll: () => void;
}

export const MistakeBankModal: React.FC<Props> = ({
  isOpen,
  onClose,
  questions,
  flaggedIds,
  onToggleFlag,
  onAnswerSaved,
  onClearAll
}) => {
  const dialogRef = useModal(isOpen, onClose);
  if (!isOpen) return null;

  const flaggedQuestions = questions.filter(q => flaggedIds.includes(q.id));

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#283b3550] backdrop-blur-xs animate-in fade-in duration-100">
      <div
        ref={dialogRef} role="dialog" aria-modal="true" aria-label="Weak points"
        className="w-full max-w-2xl max-h-[90vh] bg-[#fffef9] rounded-lg shadow-2xl border border-[#c5cebc] flex flex-col overflow-hidden"
        onClick={e => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between p-4 border-b border-[#dfded3] bg-[#f9f8f2]">
          <div className="flex items-center gap-2">
            <BookmarkCheck className="w-4 h-4 text-[#8f7142]" />
            <h3 className="text-sm font-bold text-[#1e2d26]">
              Weak Points Drill (復習帳) — {flaggedQuestions.length} Questions
            </h3>
          </div>

          <div className="flex items-center gap-2">
            {flaggedQuestions.length > 0 && (
              <button
                onClick={onClearAll}
                className="text-xs text-[#a85a4a] hover:underline flex items-center gap-1"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>Clear All</span>
              </button>
            )}

            <button
              aria-label="Close dialog" onClick={onClose}
              className="p-1 rounded text-[#788278] hover:text-[#283b35]"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Content Area */}
        <div className="flex-1 overflow-y-auto p-5 space-y-4">
          {flaggedQuestions.length === 0 ? (
            <div className="p-12 text-center text-xs text-[#8a9485] space-y-1.5">
              <p className="font-semibold text-sm text-[#283b35]">No Flagged Mistakes</p>
              <p>Missed or bookmarked questions from your quizzes will appear here for practice.</p>
            </div>
          ) : (
            flaggedQuestions.map(q => (
              <QuizCard
                key={`bank-${q.id}`}
                question={q}
                onAnswerSaved={onAnswerSaved}
                isFlagged={true}
                onToggleFlag={onToggleFlag}
              />
            ))
          )}
        </div>
      </div>
    </div>
  );
};
