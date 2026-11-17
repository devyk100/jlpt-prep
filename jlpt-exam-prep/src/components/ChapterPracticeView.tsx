import React, { useState, useMemo, useEffect } from 'react';
import { AnnotatedText } from './AnnotatedText';
import { orderQuestion } from '../studyUtils';
import type { QuizOptionExplanation } from '../types';
import {
  ArrowLeft,
  ArrowRight,
  Check,
  X,
  Lightbulb,
  BookOpen,
  RotateCcw,
  CheckCircle2,
  AlertCircle
} from 'lucide-react';

export interface ChapterExerciseItem {
  id: string;
  bookId: string;
  chapter: string;
  type: string;
  question: string;
  context?: string;
  translation: string;
  options: string[];
  correctIndex: number;
  grammarPointId: string;
  grammarPointTitle: string;
  explanation: {
    overall: string;
    options: {
      text: string;
      isCorrect: boolean;
      reason: string;
      trapCategory?: string;
    }[];
  };
  hint?: string;
}

interface Props {
  exercises: ChapterExerciseItem[];
  bookTitle: string;
  chapterTitle: string;
  availableChapters?: { bookId: string; bookTitle: string; chapter: string; count: number }[];
  onSelectChapter?: (bookId: string, chapter: string) => void;
  onNavigateToLesson: (grammarPointId: string) => void;
  onExitPractice: () => void;
}

export const ChapterPracticeView: React.FC<Props> = ({
  exercises,
  bookTitle,
  chapterTitle,
  availableChapters,
  onSelectChapter,
  onNavigateToLesson,
  onExitPractice
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState<Record<string, number>>({});
  const [revealed, setRevealed] = useState<Record<string, boolean>>({});
  const [showHint, setShowHint] = useState<Record<string, boolean>>({});
  const [showTranslationHint, setShowTranslationHint] = useState<Record<string, boolean>>({});
  const [assistedAttempts, setAssistedAttempts] = useState<Record<string, boolean>>({});
  const [isCompleted, setIsCompleted] = useState(false);

  // Reset question index and state when chapter changes
  useEffect(() => {
    setCurrentIndex(0);
    setUserAnswers({});
    setRevealed({});
    setShowHint({});
    setShowTranslationHint({});
    setAssistedAttempts({});
    setIsCompleted(false);
  }, [bookTitle, chapterTitle]);

  const currentExercise = exercises[currentIndex];

  // Shuffle options consistently
  const shuffledOptions = useMemo(() => {
    if (!currentExercise) return { options: [], correctIndex: 0, map: [] };
    // Deterministic seed based on id
    const opts = currentExercise.options.map((opt, origIdx) => ({
      text: opt,
      origIdx,
      isCorrect: origIdx === currentExercise.correctIndex
    }));
    // deterministic shuffle
    const shuffled = [...opts].sort((a, b) => (a.text > b.text ? 1 : -1));
    const newCorrect = shuffled.findIndex(o => o.isCorrect);
    return {
      options: shuffled.map(o => o.text),
      correctIndex: newCorrect,
      map: shuffled.map(o => o.origIdx)
    };
  }, [currentExercise]);

  const handleSelectOption = (shuffledIdx: number) => {
    if (revealed[currentExercise.id]) return;

    setUserAnswers(prev => ({ ...prev, [currentExercise.id]: shuffledIdx }));
    setRevealed(prev => ({ ...prev, [currentExercise.id]: true }));
  };

  const handleNext = () => {
    if (currentIndex < exercises.length - 1) {
      setCurrentIndex(prev => prev + 1);
    } else {
      setIsCompleted(true);
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(prev => prev - 1);
    }
  };

  const handleRestart = () => {
    setUserAnswers({});
    setRevealed({});
    setShowHint({});
    setShowTranslationHint({});
    setAssistedAttempts({});
    setCurrentIndex(0);
    setIsCompleted(false);
  };

  // Score calculation
  const { score, unassistedScore } = useMemo(() => {
    let correct = 0;
    let unassisted = 0;
    exercises.forEach(ex => {
      const chosen = userAnswers[ex.id];
      if (chosen !== undefined) {
        // Find which original index this chosen was
        const opts = ex.options.map((opt, origIdx) => ({
          text: opt,
          origIdx,
          isCorrect: origIdx === ex.correctIndex
        }));
        const shuffled = [...opts].sort((a, b) => (a.text > b.text ? 1 : -1));
        if (shuffled[chosen]?.isCorrect) {
          correct += 1;
          if (!assistedAttempts[ex.id]) {
            unassisted += 1;
          }
        }
      }
    });
    return { score: correct, unassistedScore: unassisted };
  }, [exercises, userAnswers, assistedAttempts]);

  if (!currentExercise) {
    return (
      <div className="flex-1 bg-white p-8 flex flex-col items-center justify-center">
        <p className="text-sm text-[#788278]">No practice exercises found for this section yet.</p>
        <button
          onClick={onExitPractice}
          className="mt-4 px-4 py-2 bg-[#467b6b] text-white rounded text-xs font-semibold"
        >
          Return to Textbook
        </button>
      </div>
    );
  }

  const isCurrentRevealed = !!revealed[currentExercise.id];
  const selectedShuffledIndex = userAnswers[currentExercise.id];
  const isUserCorrect = selectedShuffledIndex === shuffledOptions.correctIndex;

  return (
    <div className="flex-1 min-w-0 bg-[#ffffff] md:h-[calc(100vh-64px)] overflow-y-auto">
      <div className="max-w-3xl mx-auto px-6 sm:px-10 py-8 space-y-6">
        {/* Practice Top Navigation Bar */}
        <div className="flex items-center justify-between border-b border-[#dfded3] pb-4">
          <button
            onClick={onExitPractice}
            className="flex items-center gap-1.5 text-xs font-semibold text-[#467b6b] hover:text-[#2d5247] transition-colors"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span>Back to Textbook Study</span>
          </button>

          <div className="text-center">
            {availableChapters && availableChapters.length > 1 && onSelectChapter ? (
              <div className="flex items-center justify-center gap-1.5">
                <select
                  aria-label="Select chapter practice"
                  value={`${bookTitle}::${chapterTitle}`}
                  onChange={e => {
                    const [b, c] = e.target.value.split('::');
                    const target = availableChapters.find(ch => ch.bookTitle === b && ch.chapter === c);
                    if (target) {
                      onSelectChapter(target.bookId, target.chapter);
                    }
                  }}
                  className="text-xs font-bold text-[#1e2d26] bg-[#faf9f5] border border-[#cfcebe] rounded px-2.5 py-1 focus:outline-none focus:border-[#467b6b] cursor-pointer"
                >
                  {availableChapters.map(ch => (
                    <option key={`${ch.bookTitle}::${ch.chapter}`} value={`${ch.bookTitle}::${ch.chapter}`}>
                      {ch.bookTitle} · {ch.chapter} ({ch.count} Qs)
                    </option>
                  ))}
                </select>
              </div>
            ) : (
              <span className="text-xs font-bold text-[#1e2d26]">
                {bookTitle} · {chapterTitle} Practice
              </span>
            )}
            <div className="text-[10px] text-[#788278] mt-0.5">
              Target grammar hidden to test active recall
            </div>
          </div>

          <div className="text-xs font-semibold text-[#617066]">
            {currentIndex + 1} / {exercises.length}
          </div>
        </div>

        {/* Completion Screen */}
        {isCompleted ? (
          <div className="p-8 rounded-lg border border-[#dfded3] bg-[#faf9f5] text-center space-y-6">
            <CheckCircle2 className="w-12 h-12 text-[#467b6b] mx-auto" />
            <div>
              <h2 className="text-xl font-bold text-[#1e2d26] mb-1">
                Chapter Practice Completed!
              </h2>
              <p className="text-sm text-[#617066]">
                You scored <span className="font-bold text-[#467b6b]">{score}</span> out of{' '}
                <span className="font-bold">{exercises.length}</span> (
                {Math.round((score / exercises.length) * 100)}%)
                {unassistedScore < score && (
                  <span className="block text-xs text-[#8f7142] mt-1">
                    ({unassistedScore} answered unassisted without translation hint)
                  </span>
                )}
              </p>
            </div>

            <div className="flex items-center justify-center gap-3 pt-2">
              <button
                onClick={handleRestart}
                className="flex items-center gap-1.5 px-4 py-2 rounded border border-[#cfcebe] bg-white text-xs font-semibold text-[#283b35] hover:bg-[#edece1]"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>Retry Practice</span>
              </button>

              <button
                onClick={onExitPractice}
                className="flex items-center gap-1.5 px-5 py-2 rounded bg-[#467b6b] text-white text-xs font-semibold hover:bg-[#386255]"
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>Return to Lessons</span>
              </button>
            </div>
          </div>
        ) : (
          /* Exercise Card */
          <div className="space-y-6">
            {/* Progress Bar */}
            <div className="w-full bg-[#edebe0] h-1.5 rounded-full overflow-hidden">
              <div
                className="bg-[#467b6b] h-full transition-all duration-300"
                style={{ width: `${((currentIndex + 1) / exercises.length) * 100}%` }}
              />
            </div>

            <div className="p-6 rounded-lg border border-[#dfded3] bg-[#fffef9] shadow-xs space-y-5">
              {/* Question Number and Hint Toggle */}
              <div className="flex items-center justify-between text-xs text-[#788278]">
                <span className="font-semibold uppercase tracking-wider text-[#467b6b]">
                  Question {currentIndex + 1}
                </span>

                {currentExercise.hint && !isCurrentRevealed && (
                  <button
                    onClick={() =>
                      setShowHint(prev => ({
                        ...prev,
                        [currentExercise.id]: !prev[currentExercise.id]
                      }))
                    }
                    className="flex items-center gap-1 text-[11px] text-[#8f7142] hover:underline"
                  >
                    <Lightbulb className="w-3 h-3" />
                    <span>{showHint[currentExercise.id] ? 'Hide Hint' : 'Show Hint'}</span>
                  </button>
                )}
              </div>

              {/* Opt-in Hint Display */}
              {showHint[currentExercise.id] && !isCurrentRevealed && (
                <div className="p-3 rounded bg-[#fbf8f0] border border-[#d8d0ba] text-xs text-[#5c4a28]">
                  <strong>Hint:</strong> {currentExercise.hint}
                </div>
              )}

              {/* Situational Context (does NOT give away the target grammar or answer) */}
              {currentExercise.context && (
                <div className="text-xs text-[#526359] bg-[#f5f4ed] px-3 py-1.5 rounded border border-[#dfded3]">
                  <span className="font-semibold text-[#283b35]">Context: </span>
                  <span>{currentExercise.context}</span>
                </div>
              )}

              {/* Japanese Question Prompt */}
              <div className="font-serif-ja text-xl sm:text-2xl font-bold text-[#1e2d26] leading-relaxed">
                <AnnotatedText text={currentExercise.question} />
              </div>

              {/* Translation Hint (Strictly hidden by default; opt-in assisted attempt) */}
              {!isCurrentRevealed ? (
                <div>
                  <button
                    type="button"
                    onClick={() => {
                      setShowTranslationHint(prev => ({
                        ...prev,
                        [currentExercise.id]: !prev[currentExercise.id]
                      }));
                      setAssistedAttempts(prev => ({
                        ...prev,
                        [currentExercise.id]: true
                      }));
                    }}
                    className="text-xs text-[#617066] hover:text-[#283b35] underline decoration-dotted flex items-center gap-1.5 transition-colors"
                  >
                    <Lightbulb className="w-3.5 h-3.5 text-[#8f7142]" />
                    <span>
                      {showTranslationHint[currentExercise.id]
                        ? 'Hide Translation Hint'
                        : '💡 Show Translation Hint (Assisted Attempt)'}
                    </span>
                  </button>
                  {showTranslationHint[currentExercise.id] && (
                    <div className="mt-2 text-xs sm:text-sm text-[#5c4a28] italic bg-[#faf8ee] p-2.5 rounded border border-[#e5deca]">
                      "<AnnotatedText text={currentExercise.translation} />"
                    </div>
                  )}
                </div>
              ) : (
                <div className="text-xs sm:text-sm text-[#4a584f] italic bg-[#f5f7f5] p-2.5 rounded border border-[#cfded0]">
                  <span className="font-semibold not-italic text-[#2d5247]">Sentence Meaning: </span>
                  "<AnnotatedText text={currentExercise.translation} />"
                  {assistedAttempts[currentExercise.id] && (
                    <span className="ml-2 text-[10px] font-semibold uppercase tracking-wider text-[#8f7142] bg-[#fbf3d5] px-1.5 py-0.5 rounded border border-[#d8c38a]">
                      Assisted
                    </span>
                  )}
                </div>
              )}

              {/* Options Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-2">
                {shuffledOptions.options.map((opt, sIdx) => {
                  let btnStyle = 'border-[#dfded3] bg-[#faf9f5] hover:bg-[#edece1] text-[#283b35]';

                  if (isCurrentRevealed) {
                    if (sIdx === shuffledOptions.correctIndex) {
                      btnStyle = 'border-[#467b6b] bg-[#eef4ec] text-[#2e4d3a] font-semibold';
                    } else if (sIdx === selectedShuffledIndex) {
                      btnStyle = 'border-[#a85a4a] bg-[#f7efed] text-[#7a3b30] font-semibold';
                    } else {
                      btnStyle = 'opacity-40 border-[#dfded3] bg-[#f5f4ed] text-[#8a9485]';
                    }
                  }

                  return (
                    <button
                      key={`${currentExercise.id}-sopt-${sIdx}`}
                      onClick={() => handleSelectOption(sIdx)}
                      disabled={isCurrentRevealed}
                      className={`flex items-center justify-between p-3 rounded border text-left text-sm transition-colors ${btnStyle}`}
                    >
                      <div className="flex items-center gap-2.5">
                        <span className="w-5 h-5 rounded bg-[#e8e7dc] flex items-center justify-center text-[11px] font-bold text-[#617066]">
                          {sIdx + 1}
                        </span>
                        <span className="font-medium">
                          <AnnotatedText text={opt} passive />
                        </span>
                      </div>

                      {isCurrentRevealed && sIdx === shuffledOptions.correctIndex && (
                        <Check className="w-4 h-4 text-[#467b6b] shrink-0" />
                      )}
                      {isCurrentRevealed && sIdx === selectedShuffledIndex && sIdx !== shuffledOptions.correctIndex && (
                        <X className="w-4 h-4 text-[#a85a4a] shrink-0" />
                      )}
                    </button>
                  );
                })}
              </div>

              {/* Deep Explanatory Feedback (Only revealed after selection) */}
              {isCurrentRevealed && (
                <div className="space-y-3 pt-4 border-t border-[#dfded3] text-xs">
                  {/* Status Banner */}
                  <div
                    className={`p-3 rounded flex items-center justify-between gap-3 ${
                      isUserCorrect
                        ? 'bg-[#eef4ec] text-[#2e4d3a] border border-[#cfded0]'
                        : 'bg-[#f7efed] text-[#7a3b30] border border-[#e8d2cc]'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      {isUserCorrect ? (
                        <CheckCircle2 className="w-4 h-4 text-[#467b6b]" />
                      ) : (
                        <AlertCircle className="w-4 h-4 text-[#a85a4a]" />
                      )}
                      <span className="font-bold text-sm">
                        {isUserCorrect ? 'Correct!' : 'Incorrect'}
                      </span>
                    </div>

                    {/* Direct Jump Link back to Lesson */}
                    <button
                      onClick={() => onNavigateToLesson(currentExercise.grammarPointId)}
                      className="flex items-center gap-1.5 px-3 py-1 bg-white border border-[#467b6b] text-[#2c5347] rounded font-semibold hover:bg-[#eaf4ef] transition-colors"
                    >
                      <BookOpen className="w-3 h-3 text-[#467b6b]" />
                      <span>Review Lesson: {currentExercise.grammarPointTitle.split(' (')[0]}</span>
                    </button>
                  </div>

                  {/* Overall Sentence Rationale */}
                  <div className="p-3 rounded bg-[#fbf8f0] text-[#5c4a28] border border-[#d8d0ba]">
                    <div className="font-bold text-[11px] uppercase tracking-wider mb-1 flex items-center gap-1 text-[#8f7142]">
                      <Lightbulb className="w-3.5 h-3.5" />
                      <span>Sentence Rationale</span>
                    </div>
                    <p className="leading-relaxed">
                      <AnnotatedText text={currentExercise.explanation.overall} />
                    </p>
                  </div>

                  {/* 4-Way Option Breakdown */}
                  <div className="space-y-1.5">
                    <div className="text-[10px] font-bold text-[#788278] uppercase tracking-wider">
                      Option Breakdown
                    </div>

                    {currentExercise.explanation.options.map((exp, origIdx) => {
                      const isCorrect = exp.isCorrect;
                      return (
                        <div
                          key={`${currentExercise.id}-exp-${origIdx}`}
                          className={`p-2 rounded border text-xs leading-relaxed ${
                            isCorrect
                              ? 'bg-[#eef4ec] border-[#cfded0] text-[#2e4d3a]'
                              : 'bg-[#faf9f5] border-[#e8e7dc] text-[#617066]'
                          }`}
                        >
                          <span className="font-semibold mr-1">
                            <AnnotatedText text={exp.text} /> — {isCorrect ? 'Correct: ' : 'Wrong: '}
                          </span>
                          <span><AnnotatedText text={exp.reason} /></span>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>

            {/* Bottom Stepper Navigation */}
            <div className="flex items-center justify-between pt-2">
              <button
                onClick={handlePrev}
                disabled={currentIndex === 0}
                className={`flex items-center gap-1 px-3 py-1.5 rounded text-xs border ${
                  currentIndex === 0
                    ? 'opacity-40 border-[#dfded3] text-[#8a9485] cursor-not-allowed'
                    : 'border-[#cfcebe] bg-[#fffef9] hover:bg-[#edece1] text-[#283b35]'
                }`}
              >
                <ArrowLeft className="w-3.5 h-3.5" />
                <span>Previous</span>
              </button>

              <button
                onClick={handleNext}
                disabled={!isCurrentRevealed}
                className={`flex items-center gap-1.5 px-4 py-2 rounded text-xs font-semibold transition-all ${
                  !isCurrentRevealed
                    ? 'bg-[#d8e3dc] text-[#8a9990] cursor-not-allowed'
                    : 'bg-[#467b6b] text-white hover:bg-[#386255] shadow-xs'
                }`}
              >
                <span>{currentIndex === exercises.length - 1 ? 'Finish Assessment' : 'Next Question'}</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
