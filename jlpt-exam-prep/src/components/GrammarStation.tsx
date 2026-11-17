import React, { useState } from 'react';
import { GrammarPoint } from '../types';
import { SentenceCard } from './SentenceCard';
import { QuizCard } from './QuizCard';
import { MugUpTableView } from './MugUpTableView';
import {
  Lightbulb,
  ArrowRight,
  ArrowLeft,
  Sparkles,
  BookOpen,
  CheckCircle,
  HelpCircle,
  Compass,
  Table
} from 'lucide-react';

interface Props {
  point: GrammarPoint;
  allPoints: GrammarPoint[];
  onSelectPoint: (pointId: string) => void;
  furiganaMode: 'all' | 'hover' | 'off';
  seamlessFlowMode: boolean;
  onAnswerSaved: (questionId: string, isCorrect: boolean, chosenIndex: number) => void;
  flaggedMistakes: string[];
  onToggleFlag: (questionId: string) => void;
  onOpenTableModal?: (tableKey: string) => void;
}

export const GrammarStation: React.FC<Props> = ({
  point,
  allPoints,
  onSelectPoint,
  furiganaMode,
  seamlessFlowMode,
  onAnswerSaved,
  flaggedMistakes,
  onToggleFlag,
  onOpenTableModal
}) => {
  const [showFullTable, setShowFullTable] = useState(false);

  // Find next and previous points in the continuous journey
  const currentIndex = allPoints.findIndex(p => p.id === point.id);
  const prevPoint = currentIndex > 0 ? allPoints[currentIndex - 1] : null;
  const nextPoint = currentIndex < allPoints.length - 1 ? allPoints[currentIndex + 1] : null;

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-16 animate-in fade-in duration-200">
      {/* Station Header Card */}
      <div className="rounded-3xl bg-white dark:bg-slate-900 border border-slate-200/90 dark:border-slate-800 p-6 sm:p-8 shadow-sm relative overflow-hidden">
        {/* Subtle decorative background gradient */}
        <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-bl from-amber-500/10 via-indigo-500/5 to-transparent rounded-full blur-3xl pointer-events-none" />

        <div className="relative">
          {/* Level / Stream Tags */}
          <div className="flex flex-wrap items-center gap-2 mb-3">
            {!seamlessFlowMode ? (
              <span className={`px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider ${
                point.level === 'N2'
                  ? 'bg-rose-500/15 text-rose-600 dark:text-rose-400 border border-rose-500/20'
                  : point.level === 'N3'
                  ? 'bg-amber-500/15 text-amber-600 dark:text-amber-400 border border-amber-500/20'
                  : 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20'
              }`}>
                {point.level}
              </span>
            ) : (
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border border-indigo-500/20 flex items-center gap-1">
                <Compass className="w-3 h-3" />
                <span>Flow Orbit</span>
              </span>
            )}

            <span className="text-xs font-medium text-slate-500 dark:text-slate-400">
              {point.streamName}
            </span>

            {point.tags.map(tag => (
              <span key={tag} className="text-[0.68rem] px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400">
                #{tag}
              </span>
            ))}
          </div>

          {/* Grammar Title & Meaning */}
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-slate-50 tracking-tight mb-2">
            {point.title}
          </h1>

          <p className="text-base sm:text-lg text-slate-600 dark:text-slate-300 font-medium leading-relaxed">
            {point.meaning}
          </p>

          {/* Connection Formula (接続) */}
          <div className="mt-4 p-3 sm:p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/80">
            <div className="text-[0.68rem] font-bold text-slate-400 uppercase tracking-wider mb-1 flex items-center gap-1.5">
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              <span>Connection Formula (接続)</span>
            </div>
            <div className="text-sm sm:text-base font-semibold font-mono text-indigo-700 dark:text-indigo-300">
              {point.connection}
            </div>
          </div>

          {/* Deep Nuance Breakdown */}
          <div className="mt-4 text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
            <p>{point.nuance}</p>
          </div>

          {/* Golden Rule "Mug-Up" Callout Banner */}
          {point.keyTakeaway && (
            <div className="mt-5 p-3.5 rounded-2xl bg-amber-500/10 dark:bg-amber-950/30 border border-amber-500/30 text-amber-900 dark:text-amber-200 flex items-start gap-3">
              <div className="p-1.5 rounded-xl bg-amber-500 text-white shrink-0 mt-0.5 shadow-sm">
                <Lightbulb className="w-4 h-4" />
              </div>
              <div>
                <span className="font-bold text-xs sm:text-sm uppercase tracking-wide text-amber-800 dark:text-amber-300 mr-1.5">
                  Mug-Up Rule:
                </span>
                <span className="text-xs sm:text-sm font-medium">{point.keyTakeaway}</span>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Embedded High-Yield Mug-Up Table if available */}
      {point.table && (
        <div>
          <MugUpTableView table={point.table} />
        </div>
      )}

      {/* Annotated Example Sentences Section */}
      <div className="space-y-3">
        <div className="flex items-center justify-between px-1">
          <div className="flex items-center gap-2 text-sm font-bold text-slate-800 dark:text-slate-200">
            <BookOpen className="w-4 h-4 text-amber-500" />
            <span>Annotated Sentences</span>
            <span className="text-xs font-normal text-slate-400">
              (Hover/tap any word for readings and definitions)
            </span>
          </div>

          <span className="text-xs text-slate-400 font-medium">
            {point.sentences.length} {point.sentences.length === 1 ? 'example' : 'examples'}
          </span>
        </div>

        <div className="space-y-3">
          {point.sentences.map(sentence => (
            <SentenceCard
              key={sentence.id}
              sentence={sentence}
              furiganaMode={furiganaMode}
            />
          ))}
        </div>
      </div>

      {/* Post-Lesson Immediate Verification Quizzes */}
      {point.quiz && point.quiz.length > 0 && (
        <div className="space-y-3 pt-2">
          <div className="flex items-center justify-between px-1">
            <div className="flex items-center gap-2 text-sm font-bold text-slate-800 dark:text-slate-200">
              <CheckCircle className="w-4 h-4 text-emerald-500" />
              <span>Retention Check Quiz</span>
              <span className="text-xs font-normal text-slate-400">
                (Instant check with deep 4-way explanations)
              </span>
            </div>
          </div>

          <div className="space-y-4">
            {point.quiz.map(q => (
              <QuizCard
                key={q.id}
                question={q}
                onAnswerSaved={onAnswerSaved}
                isFlagged={flaggedMistakes.includes(q.id)}
                onToggleFlag={onToggleFlag}
              />
            ))}
          </div>
        </div>
      )}

      {/* Continuous Progression & Next Nuance Transition */}
      {/* Notice: No "You finished! Go close the tab" roadblock! Instead, smooth flow into next connected node. */}
      <div className="pt-6 border-t border-slate-200/80 dark:border-slate-800 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4">
        {prevPoint ? (
          <button
            onClick={() => onSelectPoint(prevPoint.id)}
            className="flex items-center justify-center gap-2 px-4 py-3 rounded-2xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-700 text-sm font-medium transition-all shadow-sm"
          >
            <ArrowLeft className="w-4 h-4" />
            <div className="text-left">
              <div className="text-[0.68rem] text-slate-400">Previous Point</div>
              <div className="font-semibold truncate max-w-[200px]">{prevPoint.title}</div>
            </div>
          </button>
        ) : <div />}

        {nextPoint ? (
          <button
            onClick={() => {
              onSelectPoint(nextPoint.id);
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
            className="flex items-center justify-center gap-3 px-6 py-3.5 rounded-2xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-white shadow-md hover:shadow-lg transition-all text-sm font-bold group"
          >
            <div className="text-right">
              <div className="text-[0.68rem] text-amber-100 uppercase tracking-wider">Flow to Next Nuance</div>
              <div className="font-extrabold truncate max-w-[220px]">{nextPoint.title}</div>
            </div>
            <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </button>
        ) : (
          <div className="text-xs text-slate-400 italic text-center sm:text-right">
            Continuous journey completed for this stream! Feel free to explore other orbits.
          </div>
        )}
      </div>
    </div>
  );
};

