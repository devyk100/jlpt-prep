import React, { useState } from 'react';
import type { GrammarPoint } from '../types';
import { SentenceCard } from './SentenceCard';
import { QuizCard } from './QuizCard';
import { MugUpTableView } from './MugUpTableView';
import {
  BookOpen,
  CheckCircle,
  CheckCircle2,
  Circle,
  Check,
  Lightbulb,
  ArrowRight,
  ArrowLeft,
  Bookmark,
  BookmarkCheck,
  Compass,
  Sparkles
} from 'lucide-react';

interface Props {
  point: GrammarPoint;
  allPoints: GrammarPoint[];
  onSelectPoint: (pointId: string) => void;
  isCompleted: boolean;
  onToggleCompleted: (pointId: string) => void;
  furiganaMode: 'all' | 'hover' | 'off';
  seamlessFlowMode: boolean;
  onAnswerSaved: (questionId: string, isCorrect: boolean, chosenIndex: number) => void;
  flaggedMistakes: string[];
  onToggleFlag: (questionId: string) => void;
}

export const DeskPane: React.FC<Props> = ({
  point,
  allPoints,
  onSelectPoint,
  isCompleted,
  onToggleCompleted,
  furiganaMode,
  seamlessFlowMode,
  onAnswerSaved,
  flaggedMistakes,
  onToggleFlag
}) => {
  // Find previous and next points
  const currentIndex = allPoints.findIndex(p => p.id === point.id);
  const prevPoint = currentIndex > 0 ? allPoints[currentIndex - 1] : null;
  const nextPoint = currentIndex < allPoints.length - 1 ? allPoints[currentIndex + 1] : null;

  return (
    <div className="flex-1 min-w-0 bg-[#ffffff] md:h-[calc(100vh-64px)] overflow-y-auto">
      <div className="max-w-3xl mx-auto px-6 sm:px-10 py-8 space-y-8">
        {point.sourceReference && <p className="text-xs text-[#617066]">{point.sourceReference}</p>}
        {/* Source Reference & Metadata Header */}
        <div className="border-b border-[#dfded3] pb-5">
          <div className="flex flex-wrap items-center justify-between gap-3 mb-2.5">
            <div className="flex items-center gap-2 text-xs text-[#788278]">
              {point.book && (
                <span className="font-semibold text-[#467b6b]">
                  {point.book} · {point.chapter}
                </span>
              )}
              {point.book && <span>·</span>}
              <span>{point.streamName}</span>
            </div>

            <div className="flex items-center gap-2">
              {/* Explicit Completion Button */}
              <button
                type="button"
                onClick={() => onToggleCompleted(point.id)}
                className={`flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-medium transition-all ${
                  isCompleted
                    ? 'bg-[#eaf4ef] border border-[#467b6b] text-[#2c5347]'
                    : 'bg-[#fffef9] border border-[#cfcebe] text-[#617066] hover:border-[#467b6b] hover:text-[#283b35]'
                }`}
                title={isCompleted ? "Marked as completed (Click to unmark)" : "Not completed (Click to mark completed)"}
              >
                {isCompleted ? (
                  <>
                    <CheckCircle2 className="w-3.5 h-3.5 text-[#467b6b]" />
                    <span className="font-semibold">Completed</span>
                  </>
                ) : (
                  <>
                    <Circle className="w-3.5 h-3.5 text-[#9aa496]" />
                    <span>Mark Completed</span>
                  </>
                )}
              </button>

              {!seamlessFlowMode && (
                <span className={`text-[10px] px-2 py-0.5 rounded font-bold uppercase tracking-wider ${
                  point.level === 'N2' ? 'bg-[#f0e8e4] text-[#865a50]' :
                  point.level === 'N3' ? 'bg-[#f4efe4] text-[#8f7142]' :
                  point.level === 'N4' ? 'bg-[#e5ecf0] text-[#4d6a78]' :
                  'bg-[#e6eee3] text-[#4d6b47]'
                }`}>
                  {point.level}
                </span>
              )}
            </div>
          </div>

          {/* Large Japanese Pattern Heading */}
          <h1 className="font-serif-ja text-3xl sm:text-4xl font-bold text-[#1e2d26] tracking-tight mb-2">
            {point.title}
          </h1>

          {/* English Meaning */}
          <p className="text-base sm:text-lg text-[#55645a] font-normal leading-relaxed">
            {point.meaning}
          </p>

          {/* Connection Formula (接続) */}
          <div className="mt-4 p-3.5 rounded border border-[#dfded3] bg-[#faf9f5]">
            <div className="text-[10px] font-semibold text-[#8a9485] uppercase tracking-wider mb-1">
              接続 (Connection Formula)
            </div>
            <div className="font-mono text-sm font-semibold text-[#2f4f4f]">
              {point.connection}
            </div>
          </div>
        </div>

        {/* Detailed Grammatical Nuance & Explanation */}
        <section className="space-y-3">
          <h2 className="text-xs font-bold text-[#788278] uppercase tracking-wider">
            Grammar Nuance & Usage Notes
          </h2>
          <div className="text-sm text-[#2d3a33] leading-relaxed space-y-2">
            <p>{point.nuance}</p>
          </div>

          {/* Mug-Up Golden Rule Callout */}
          {point.keyTakeaway && (
            <div className="p-3.5 rounded border border-[#d8d0ba] bg-[#fbf8f0] text-[#5c4a28] flex items-start gap-2.5 text-xs sm:text-sm">
              <Lightbulb className="w-4 h-4 text-[#8f7142] shrink-0 mt-0.5" />
              <div>
                <span className="font-bold mr-1.5">Mug-Up Rule:</span>
                <span>{point.keyTakeaway}</span>
              </div>
            </div>
          )}
        </section>

        {/* High-Yield Mug-Up Table (if present) */}
        {point.table && (
          <section>
            <MugUpTableView table={point.table} />
          </section>
        )}

        {/* Annotated Example Sentences */}
        <section className="space-y-3">
          <div className="flex items-center justify-between">
            <h2 className="text-xs font-bold text-[#788278] uppercase tracking-wider flex items-center gap-1.5">
              <BookOpen className="w-3.5 h-3.5 text-[#467b6b]" />
              <span>Example Sentences ({point.sentences.length})</span>
            </h2>
            <span className="text-[11px] text-[#8a9485]">
              Hover words for readings & definitions
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
        </section>

        {/* Retention Check Quiz */}
        {point.quiz && point.quiz.length > 0 && (
          <section className="space-y-3 pt-4 border-t border-[#dfded3]">
            <h2 className="text-xs font-bold text-[#788278] uppercase tracking-wider flex items-center gap-1.5">
              <CheckCircle className="w-3.5 h-3.5 text-[#467b6b]" />
              <span>Retention Check Quiz</span>
            </h2>

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
          </section>
        )}

        {/* Explicit Milestone Completion Card */}
        <div className={`p-4 rounded-lg border flex flex-col sm:flex-row sm:items-center justify-between gap-3 transition-all ${
          isCompleted
            ? 'bg-[#f2f7f4] border-[#9ec4b0]'
            : 'bg-[#faf9f5] border-[#dfded3]'
        }`}>
          <div>
            <div className="text-xs font-bold text-[#1e2d26] flex items-center gap-1.5">
              {isCompleted ? (
                <>
                  <CheckCircle2 className="w-4 h-4 text-[#467b6b]" />
                  <span>Rule Marked as Completed</span>
                </>
              ) : (
                <>
                  <Circle className="w-4 h-4 text-[#8a9485]" />
                  <span>Status: In Progress</span>
                </>
              )}
            </div>
            <div className="text-[11.5px] text-[#617066] mt-0.5">
              {isCompleted
                ? 'You have explicitly marked this grammar rule as completed. Click anytime to unmark it.'
                : 'This rule is in-progress. It will not be marked as completed until you explicitly click below.'}
            </div>
          </div>

          <button
            type="button"
            onClick={() => onToggleCompleted(point.id)}
            className={`px-4 py-2 rounded text-xs font-semibold transition-all shrink-0 flex items-center justify-center gap-1.5 ${
              isCompleted
                ? 'bg-[#ffffff] border border-[#467b6b] text-[#2c5347] hover:bg-[#e6f1ec]'
                : 'bg-[#467b6b] hover:bg-[#386255] text-white shadow-xs'
            }`}
          >
            {isCompleted ? (
              <>
                <Check className="w-3.5 h-3.5 text-[#467b6b]" />
                <span>Completed (Click to Unmark)</span>
              </>
            ) : (
              <>
                <Check className="w-3.5 h-3.5" />
                <span>Mark as Completed</span>
              </>
            )}
          </button>
        </div>

        {/* Bottom Continuous Flow Navigation */}
        <div className="pt-8 pb-12 border-t border-[#dfded3] flex items-center justify-between gap-4">
          {prevPoint ? (
            <button
              onClick={() => {
                onSelectPoint(prevPoint.id);
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="flex items-center gap-2 px-3.5 py-2 rounded border border-[#dfded3] bg-[#fffef9] hover:bg-[#f6f4ed] text-xs text-[#283b35] transition-colors"
            >
              <ArrowLeft className="w-3.5 h-3.5 text-[#788278]" />
              <div className="text-left">
                <span className="text-[10px] text-[#8a9485] block">Previous</span>
                <span className="font-semibold truncate max-w-[150px] sm:max-w-[180px] block font-serif-ja">
                  {prevPoint.title.split(' (')[0]}
                </span>
              </div>
            </button>
          ) : <div />}

          {nextPoint ? (
            <button
              onClick={() => {
                onSelectPoint(nextPoint.id);
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="flex items-center gap-2.5 px-4 py-2 rounded bg-[#467b6b] hover:bg-[#3b685a] text-white text-xs font-semibold shadow-xs transition-colors"
            >
              <div className="text-right">
                <span className="text-[10px] text-[#d1e0d9] block">Next Grammar</span>
                <span className="font-bold truncate max-w-[160px] sm:max-w-[200px] block font-serif-ja">
                  {nextPoint.title.split(' (')[0]}
                </span>
              </div>
              <ArrowRight className="w-4 h-4" />
            </button>
          ) : (
            <div className="text-xs text-[#8a9485] italic">
              End of list
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

