import React from 'react';
import { GrammarPoint } from '../types';
import { Check, Circle } from 'lucide-react';

interface Props {
  points: GrammarPoint[];
  currentPointId: string;
  onSelectPoint: (pointId: string) => void;
  studiedPoints: Record<string, boolean>;
  seamlessFlowMode: boolean;
}

export const StreamTimeline: React.FC<Props> = ({
  points,
  currentPointId,
  onSelectPoint,
  studiedPoints,
  seamlessFlowMode
}) => {
  return (
    <div className="overflow-x-auto py-2 px-1 scrollbar-none">
      <div className="flex items-center gap-1.5 min-w-max">
        {points.map((pt, idx) => {
          const isCurrent = pt.id === currentPointId;
          const isStudied = studiedPoints[pt.id];

          return (
            <button
              key={pt.id}
              onClick={() => onSelectPoint(pt.id)}
              className={`flex items-center gap-2 px-3 py-1.5 rounded-xl text-xs font-medium transition-all duration-150 border ${
                isCurrent
                  ? 'bg-amber-500 text-white border-amber-600 shadow-sm shadow-amber-500/20 font-bold scale-[1.02]'
                  : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800'
              }`}
            >
              <span className={`w-4 h-4 rounded-full flex items-center justify-center text-[0.62rem] ${
                isCurrent
                  ? 'bg-white text-amber-600 font-extrabold'
                  : isStudied
                  ? 'bg-emerald-500 text-white'
                  : 'bg-slate-200 dark:bg-slate-800 text-slate-500'
              }`}>
                {isStudied ? <Check className="w-2.5 h-2.5 stroke-[3]" /> : idx + 1}
              </span>

              <span className="truncate max-w-[130px] sm:max-w-[160px]">
                {pt.title.split(' (')[0]}
              </span>

              {!seamlessFlowMode && (
                <span className={`text-[0.62rem] px-1 py-0.2 rounded font-semibold ${
                  isCurrent
                    ? 'bg-amber-600 text-white'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-400'
                }`}>
                  {pt.level}
                </span>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
};

