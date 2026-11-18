import React, { useState, useMemo, useEffect, useRef } from 'react';
import { AnnotatedText } from './AnnotatedText';
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
  provenance?: 'source-derived' | 'adapted' | 'original';
  sourceEvidence?: string;
  reconstructedSentence?: string;
  scrambleOrder?: number[];
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

interface StoredPracticeAttempt {
  version: 2;
  attemptSeed: string;
  currentIndex: number;
  userAnswers: Record<string, number>;
  revealed: Record<string, boolean>;
  showHint: Record<string, boolean>;
  showTranslationHint: Record<string, boolean>;
  assistedAttempts: Record<string, boolean>;
  isCompleted: boolean;
}

// Pseudo-random number generator for stable, non-alphabetical shuffling
function seededRandom(seed: number) {
  let s = seed % 2147483647;
  if (s <= 0) s += 2147483646;
  return () => {
    s = (s * 16807) % 2147483647;
    return (s - 1) / 2147483646;
  };
}

function stringToSeed(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = (hash << 5) - hash + str.charCodeAt(i);
    hash |= 0;
  }
  return Math.abs(hash) || 1;
}

function computeShuffleOrder(exId: string, count: number, attemptSeed: string): number[] {
  const seed = stringToSeed(`${attemptSeed}::${exId}`);
  const rand = seededRandom(seed);
  const arr = Array.from({ length: count }, (_, i) => i);
  // Fisher-Yates shuffle
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
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
  const storageKey = `jlpt_practice_v2_${bookTitle}_${chapterTitle}`;

  // Attempt state initialized from localStorage if available
  const [attemptSeed, setAttemptSeed] = useState<string>(() => Date.now().toString());
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [userAnswers, setUserAnswers] = useState<Record<string, number>>({});
  const [revealed, setRevealed] = useState<Record<string, boolean>>({});
  const [showHint, setShowHint] = useState<Record<string, boolean>>({});
  const [showTranslationHint, setShowTranslationHint] = useState<Record<string, boolean>>({});
  const [assistedAttempts, setAssistedAttempts] = useState<Record<string, boolean>>({});
  const [isCompleted, setIsCompleted] = useState<boolean>(false);

  // Restore or initialize attempt on chapter change
  useEffect(() => {
    if (exercises.length === 0) return;

    try {
      const saved = localStorage.getItem(storageKey);
      if (saved) {
        const parsed: StoredPracticeAttempt = JSON.parse(saved);
        if (parsed.version === 2 && parsed.attemptSeed) {
          setAttemptSeed(parsed.attemptSeed);
          setCurrentIndex(Math.min(parsed.currentIndex || 0, exercises.length - 1));
          setUserAnswers(parsed.userAnswers || {});
          setRevealed(parsed.revealed || {});
          setShowHint(parsed.showHint || {});
          setShowTranslationHint(parsed.showTranslationHint || {});
          setAssistedAttempts(parsed.assistedAttempts || {});
          setIsCompleted(!!parsed.isCompleted);
          return;
        }
      }
    } catch {
      // Ignore parse failure, initialize cleanly
    }

    // New attempt
    const newSeed = Date.now().toString();
    setAttemptSeed(newSeed);
    setCurrentIndex(0);
    setUserAnswers({});
    setRevealed({});
    setShowHint({});
    setShowTranslationHint({});
    setAssistedAttempts({});
    setIsCompleted(false);
  }, [storageKey, exercises.length]);

  // Persist attempt to localStorage on every state update
  const persistAttempt = (
    updated: Partial<StoredPracticeAttempt>
  ) => {
    try {
      const stateToSave: StoredPracticeAttempt = {
        version: 2,
        attemptSeed,
        currentIndex,
        userAnswers,
        revealed,
        showHint,
        showTranslationHint,
        assistedAttempts,
        isCompleted,
        ...updated
      };
      localStorage.setItem(storageKey, JSON.stringify(stateToSave));
    } catch {
      // Storage quota or error; state still remains live
    }
  };

  const currentExercise = exercises[currentIndex];

  // Deterministic Fisher-Yates shuffle for options using attemptSeed + exercise.id
  const shuffledOptions = useMemo(() => {
    if (!currentExercise) return { options: [], correctIndex: 0, map: [] };

    const order = computeShuffleOrder(currentExercise.id, currentExercise.options.length, attemptSeed);
    const shuffledTexts = order.map(origIdx => currentExercise.options[origIdx]);
    const newCorrectIndex = order.indexOf(currentExercise.correctIndex);

    return {
      options: shuffledTexts,
      correctIndex: newCorrectIndex,
      map: order // map[shuffledIdx] = originalIndex
    };
  }, [currentExercise, attemptSeed]);

  const handleSelectOption = (shuffledIdx: number) => {
    if (!currentExercise || revealed[currentExercise.id]) return;

    const nextAnswers = { ...userAnswers, [currentExercise.id]: shuffledIdx };
    const nextRevealed = { ...revealed, [currentExercise.id]: true };

    setUserAnswers(nextAnswers);
    setRevealed(nextRevealed);
    persistAttempt({ userAnswers: nextAnswers, revealed: nextRevealed });
  };

  const handleNext = () => {
    if (currentIndex < exercises.length - 1) {
      const nextIdx = currentIndex + 1;
      setCurrentIndex(nextIdx);
      persistAttempt({ currentIndex: nextIdx });
    } else {
      setIsCompleted(true);
      persistAttempt({ isCompleted: true });
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      const prevIdx = currentIndex - 1;
      setCurrentIndex(prevIdx);
      persistAttempt({ currentIndex: prevIdx });
    }
  };

  const handleRestart = () => {
    const freshSeed = Date.now().toString();
    setAttemptSeed(freshSeed);
    setUserAnswers({});
    setRevealed({});
    setShowHint({});
    setShowTranslationHint({});
    setAssistedAttempts({});
    setCurrentIndex(0);
    setIsCompleted(false);

    try {
      localStorage.removeItem(storageKey);
    } catch {
      // Ignore
    }
  };

  const handleToggleHint = () => {
    if (!currentExercise) return;
    const nextShowHint = { ...showHint, [currentExercise.id]: !showHint[currentExercise.id] };
    const nextAssisted = { ...assistedAttempts, [currentExercise.id]: true };

    setShowHint(nextShowHint);
    setAssistedAttempts(nextAssisted);
    persistAttempt({ showHint: nextShowHint, assistedAttempts: nextAssisted });
  };

  const handleToggleTranslationHint = () => {
    if (!currentExercise) return;
    const nextShowTrans = { ...showTranslationHint, [currentExercise.id]: !showTranslationHint[currentExercise.id] };
    const nextAssisted = { ...assistedAttempts, [currentExercise.id]: true };

    setShowTranslationHint(nextShowTrans);
    setAssistedAttempts(nextAssisted);
    persistAttempt({ showTranslationHint: nextShowTrans, assistedAttempts: nextAssisted });
  };

  // Score calculation
  const { score, unassistedScore } = useMemo(() => {
    let correct = 0;
    let unassisted = 0;
    exercises.forEach(ex => {
      const chosen = userAnswers[ex.id];
      if (chosen !== undefined) {
        const order = computeShuffleOrder(ex.id, ex.options.length, attemptSeed);
        const originalChosen = order[chosen];
        if (originalChosen === ex.correctIndex) {
          correct += 1;
          if (!assistedAttempts[ex.id]) {
            unassisted += 1;
          }
        }
      }
    });
    return { score: correct, unassistedScore: unassisted };
  }, [exercises, userAnswers, assistedAttempts, attemptSeed]);

  // Honest Unavailable State: If no exercises exist for this chapter, display clear notice
  if (!currentExercise) {
    return (
      <div className="flex-1 bg-white p-8 flex flex-col items-center justify-center max-w-2xl mx-auto text-center space-y-5">
        <div className="w-12 h-12 rounded-full bg-[#f4f2e8] flex items-center justify-center text-[#8a7f60] mb-1">
          <BookOpen className="w-6 h-6" />
        </div>
        <div>
          <h2 className="text-lg font-bold text-[#1e2d26]">
            {bookTitle} · {chapterTitle} Practice
          </h2>
          <p className="text-sm text-[#788278] mt-2 leading-relaxed">
            Practice exercises for this specific section are currently in development and awaiting textbook source verification.
          </p>
        </div>

        {availableChapters && availableChapters.length > 0 && onSelectChapter && (
          <div className="p-4 rounded-lg bg-[#faf9f5] border border-[#dfded3] w-full text-left space-y-2 mt-2">
            <div className="text-xs font-bold text-[#467b6b] uppercase tracking-wider">
              Available Practice Chapters in Database:
            </div>
            <div className="flex flex-wrap gap-2 pt-1 max-h-48 overflow-y-auto">
              {availableChapters.map(ch => (
                <button
                  key={`${ch.bookTitle}::${ch.chapter}`}
                  onClick={() => onSelectChapter(ch.bookId, ch.chapter)}
                  className="px-2.5 py-1.5 rounded border border-[#cfcebe] bg-white text-xs font-medium text-[#283b35] hover:bg-[#edece1] transition-colors"
                >
                  {ch.bookTitle} · {ch.chapter} ({ch.count} Qs)
                </button>
              ))}
            </div>
          </div>
        )}

        <button
          onClick={onExitPractice}
          className="px-5 py-2.5 bg-[#467b6b] hover:bg-[#386255] text-white rounded text-xs font-semibold transition-colors"
        >
          Return to Textbook Study
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
                  <span className="block text-xs text-[#8f7142] mt-1 font-semibold">
                    ({unassistedScore} answered unassisted without hints)
                  </span>
                )}
              </p>
            </div>

            <div className="flex items-center justify-center gap-3 pt-2">
              <button
                onClick={handleRestart}
                className="flex items-center gap-1.5 px-4 py-2 rounded border border-[#cfcebe] bg-white text-xs font-semibold text-[#283b35] hover:bg-[#edece1] transition-colors"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>Retry Practice</span>
              </button>

              <button
                onClick={onExitPractice}
                className="flex items-center gap-1.5 px-5 py-2 rounded bg-[#467b6b] text-white text-xs font-semibold hover:bg-[#386255] transition-colors"
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
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="font-semibold uppercase tracking-wider text-[#467b6b]">
                    Question {currentIndex + 1}
                  </span>

                  {currentExercise.type === 'star-mark' && (
                    <span className="px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wider bg-[#fff2cc] text-[#855a00] border border-[#ffe599] rounded">
                      ★ Star-Mark (文の組み立て)
                    </span>
                  )}

                  {currentExercise.provenance && (
                    <span
                      className={`px-1.5 py-0.5 text-[10px] font-medium rounded border ${
                        currentExercise.provenance === 'source-derived'
                          ? 'bg-[#e8f4f8] text-[#1b4965] border-[#b8d8e8]'
                          : currentExercise.provenance === 'adapted'
                          ? 'bg-[#f3eef8] text-[#5e35b1] border-[#d1c4e9]'
                          : 'bg-[#f5f5f5] text-[#555] border-[#ddd]'
                      }`}
                      title={currentExercise.sourceEvidence || undefined}
                    >
                      {currentExercise.provenance === 'source-derived' ? 'Textbook Drill' : currentExercise.provenance === 'adapted' ? 'Adapted Drill' : 'Diagnostic Drill'}
                    </span>
                  )}
                </div>

                {currentExercise.hint && !isCurrentRevealed && (
                  <button
                    onClick={handleToggleHint}
                    className="flex items-center gap-1 text-[11px] text-[#8f7142] hover:underline cursor-pointer"
                  >
                    <Lightbulb className="w-3 h-3" />
                    <span>{showHint[currentExercise.id] ? 'Hide Hint' : 'Show Hint'}</span>
                  </button>
                )}
              </div>

              {/* Star-Mark Rearrangement Notice */}
              {currentExercise.type === 'star-mark' && (
                <div className="text-xs text-[#6e5414] bg-[#fef9e7] px-3.5 py-2 rounded border border-[#fae5a7] flex items-center gap-1.5">
                  <span className="font-bold">★ Instructions:</span>
                  <span>Rearrange the 4 scrambled parts into correct grammatical sequence. Select the option that belongs in the ★ position.</span>
                </div>
              )}

              {/* Opt-in Hint Display (Irreversibly marks attempt as assisted) */}
              {showHint[currentExercise.id] && !isCurrentRevealed && (
                <div className="p-3 rounded bg-[#fbf8f0] border border-[#d8d0ba] text-xs text-[#5c4a28] flex items-start gap-2">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-[#8f7142] bg-[#fbf3d5] px-1.5 py-0.5 rounded border border-[#d8c38a] shrink-0">
                    Assisted
                  </span>
                  <div>
                    <strong>Hint:</strong> {currentExercise.hint}
                  </div>
                </div>
              )}

              {/* Situational Context (Ensures question is answerable without English translation) */}
              {currentExercise.context && (
                <div className="text-xs text-[#526359] bg-[#f5f4ed] px-3.5 py-2 rounded border border-[#dfded3]">
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
                    onClick={handleToggleTranslationHint}
                    className="text-xs text-[#617066] hover:text-[#283b35] underline decoration-dotted flex items-center gap-1.5 transition-colors cursor-pointer"
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

              {/* Options Grid (Accessible non-nested option rows; word taps inside look up vocab without submitting) */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-2" role="group" aria-label="Answer options">
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
                      type="button"
                      key={`${currentExercise.id}-sopt-${sIdx}`}
                      disabled={isCurrentRevealed}
                      aria-pressed={selectedShuffledIndex === sIdx}
                      onClick={() => handleSelectOption(sIdx)}
                      className={`flex items-center justify-between p-3 rounded border text-left text-sm transition-colors cursor-pointer select-none focus-visible:outline-2 focus-visible:outline-[#467b6b] ${btnStyle}`}
                    >
                      <div className="flex items-center gap-2.5">
                        <span className="w-5 h-5 rounded bg-[#e8e7dc] flex items-center justify-center text-[11px] font-bold text-[#617066] shrink-0">
                          {sIdx + 1}
                        </span>
                        <span className="font-medium">
                          <AnnotatedText text={opt} />
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
                      className="flex items-center gap-1.5 px-3 py-1 bg-white border border-[#467b6b] text-[#2c5347] rounded font-semibold hover:bg-[#eaf4ef] transition-colors cursor-pointer"
                    >
                      <BookOpen className="w-3 h-3 text-[#467b6b]" />
                      <span>Review Lesson: {currentExercise.grammarPointTitle?.split(' (')[0] || 'Lesson'}</span>
                    </button>
                  </div>

                  {/* Reconstructed Sentence for Star-Mark Exercises */}
                  {currentExercise.type === 'star-mark' && currentExercise.reconstructedSentence && (
                    <div className="p-3.5 rounded bg-[#f1f6f3] text-[#244234] border border-[#bcd3c4] space-y-2">
                      <div className="font-bold text-[11px] uppercase tracking-wider flex items-center gap-1.5 text-[#3b6b55]">
                        <span>★ Reconstructed Complete Sentence</span>
                      </div>
                      <p className="font-serif-ja text-base sm:text-lg font-bold text-[#1e2d26] leading-relaxed">
                        <AnnotatedText text={currentExercise.reconstructedSentence} />
                      </p>
                      {Array.isArray(currentExercise.scrambleOrder) && (
                        <div className="text-xs text-[#3b6b55] flex items-center gap-1.5 flex-wrap pt-1 border-t border-[#d5e5db]">
                          <span className="font-semibold">Correct sequence:</span>
                          {currentExercise.scrambleOrder.map((pos, idx) => (
                            <span key={idx} className="flex items-center gap-1">
                              <span
                                className={`px-2 py-0.5 rounded font-bold text-xs ${
                                  idx === 2
                                    ? 'bg-[#ffe082] text-[#6d4c00] border border-[#ffca28]'
                                    : 'bg-white text-[#2e4d3a] border border-[#cfded0]'
                                }`}
                              >
                                Choice {pos} {idx === 2 ? '(★ Correct Answer)' : ''}
                              </span>
                              {idx < 3 && <span className="text-[#88a394]">→</span>}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                  )}

                  {/* Overall Sentence Rationale */}
                  <div className="p-3 rounded bg-[#fbf8f0] text-[#5c4a28] border border-[#d8d0ba]">
                    <div className="font-bold text-[11px] uppercase tracking-wider mb-1 flex items-center gap-1 text-[#8f7142]">
                      <Lightbulb className="w-3.5 h-3.5" />
                      <span>Sentence Rationale</span>
                    </div>
                    <p className="leading-relaxed">
                      <AnnotatedText
                        text={
                          typeof currentExercise.explanation === 'string'
                            ? currentExercise.explanation
                            : currentExercise.explanation?.overall || ''
                        }
                      />
                    </p>
                  </div>

                  {/* 4-Way Option Breakdown */}
                  {Array.isArray(currentExercise.explanation?.options) && (
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
                  )}
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
                    : 'border-[#cfcebe] bg-[#fffef9] hover:bg-[#edece1] text-[#283b35] cursor-pointer'
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
                    : 'bg-[#467b6b] text-white hover:bg-[#386255] shadow-xs cursor-pointer'
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
