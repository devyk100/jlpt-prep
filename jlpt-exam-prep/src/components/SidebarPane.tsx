import { AnnotatedText } from './AnnotatedText';
import React, { useMemo } from 'react';
import type { GrammarPoint } from '../types';
import { Search, CheckCircle, Check, Book } from 'lucide-react';

interface Props {
  points: GrammarPoint[];
  currentPointId: string;
  onSelectPoint: (pointId: string) => void;
  studiedPoints: Record<string, boolean>;
  onToggleCompleted: (pointId: string) => void;
  onResetStudied?: () => void;
  searchQuery: string;
  onSearchChange: (q: string) => void;
  selectedFilter: 'all' | 'N5' | 'N4' | 'N3' | 'N2';
  onFilterChange: (f: 'all' | 'N5' | 'N4' | 'N3' | 'N2') => void;
  seamlessFlowMode: boolean;
}

export const SidebarPane: React.FC<Props> = ({
  points,
  currentPointId,
  onSelectPoint,
  studiedPoints,
  onToggleCompleted,
  onResetStudied,
  searchQuery,
  onSearchChange,
  selectedFilter,
  onFilterChange,
  seamlessFlowMode
}) => {
  // Filter points based on search query and level filter
  const filteredPoints = useMemo(() => {
    return points.filter(pt => {
      // Level filter
      if (selectedFilter !== 'all' && pt.level !== selectedFilter) {
        return false;
      }
      // Query filter
      if (searchQuery.trim() !== '') {
        const q = searchQuery.toLowerCase();
        return (
          pt.title.toLowerCase().includes(q) ||
          pt.meaning.toLowerCase().includes(q) ||
          pt.connection.toLowerCase().includes(q) ||
          (pt.book && pt.book.toLowerCase().includes(q)) ||
          (pt.tags ? pt.tags.some(t => t.toLowerCase().includes(q)) : false)
        );
      }
      return true;
    });
  }, [points, selectedFilter, searchQuery]);

  const studiedCount = useMemo(() => {
    return filteredPoints.filter(p => studiedPoints[p.id]).length;
  }, [filteredPoints, studiedPoints]);

  return (
    <aside className="w-full md:w-[360px] lg:w-[390px] shrink-0 border-r border-[#dfded3] bg-[#f8f7f1] flex flex-col h-[38vh] md:h-[calc(100vh-64px)] md:sticky md:top-16">
      {/* Top Filter & Search Controls */}
      <div className="p-3.5 border-b border-[#dfded3] space-y-2.5 bg-[#f5f4ed]">
        {/* Search Input */}
        <div className="flex items-center gap-2 px-3 py-1.5 rounded-md border border-[#cfcebe] bg-[#fffef9] text-sm text-[#283b35] focus-within:border-[#467b6b] transition-colors">
          <Search className="w-3.5 h-3.5 text-[#8a9485] shrink-0" />
          <input
            type="text"
            value={searchQuery}
            onChange={e => onSearchChange(e.target.value)}
            placeholder="Search grammar, reading, meaning..."
            className="w-full bg-transparent border-none outline-none text-xs text-[#283b35] placeholder:text-[#9da292]"
          />
          {searchQuery && (
            <button
              onClick={() => onSearchChange('')}
              className="text-[10px] text-[#8a9485] hover:text-[#283b35]"
            >
              Clear
            </button>
          )}
        </div>

        {/* Level / Source Tabs */}
        <div className="flex items-center gap-1">
          {(['all', 'N5', 'N4', 'N3', 'N2'] as const).map(lvl => {
            const isSelected = selectedFilter === lvl;
            const label = lvl === 'all' ? 'All (Flow)' : lvl;

            return (
              <button
                key={lvl}
                onClick={() => onFilterChange(lvl)}
                className={`flex-1 py-1 text-center rounded text-xs transition-colors ${
                  isSelected
                    ? 'bg-[#467b6b] text-white font-semibold'
                    : 'bg-[#ebe9dd] text-[#617066] hover:bg-[#e0decb]'
                }`}
              >
                {label}
              </button>
            );
          })}
        </div>

        {/* Counts summary */}
        <div className="flex items-center justify-between text-[11px] text-[#788278] px-0.5">
          <span>{filteredPoints.length} points</span>
          <div className="flex items-center gap-1.5">
            <span>{studiedCount} marked completed</span>
            {studiedCount > 0 && onResetStudied && (
              <button
                type="button"
                onClick={onResetStudied}
                className="text-[10px] text-[#8a9485] hover:text-[#9e3a3a] underline ml-0.5"
                title="Reset all marked completed points back to uncompleted"
              >
                Reset
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Grammar Points List */}
      <div className="flex-1 overflow-y-auto divide-y divide-[#e8e7dc] p-1.5 space-y-0.5">
        {filteredPoints.length === 0 ? (
          <div className="p-8 text-center text-xs text-[#8a9485]">
            No matching grammar points found.
          </div>
        ) : (
          filteredPoints.map(pt => {
            const isCurrent = pt.id === currentPointId;
            const isStudied = studiedPoints[pt.id];

            return (
              <div
                role="button" tabIndex={0}
                onKeyDown={e => { if (e.target === e.currentTarget && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); onSelectPoint(pt.id); } }}
                key={pt.id}
                onClick={() => onSelectPoint(pt.id)}
                className={`w-full text-left p-3 rounded-md transition-all flex items-start justify-between gap-2.5 ${
                  isCurrent
                    ? 'bg-[#ffffff] border border-[#b8bfb0] shadow-xs text-[#283b35]'
                    : 'hover:bg-[#edece1] text-[#33423b] border border-transparent'
                }`}
              >
                <div className="min-w-0 flex-1">
                  {/* Title & Level Tag */}
                  <div className="flex items-baseline gap-2 mb-1">
                    <span className="font-serif-ja text-[15px] font-semibold text-[#1e2d26] leading-loose">
                      <AnnotatedText text={pt.title.split(' (')[0]} level={pt.level} passive />
                    </span>
                    {!seamlessFlowMode && (
                      <span className={`text-[9px] px-1.5 py-0.2 rounded font-semibold uppercase ${
                        pt.level === 'N2' ? 'bg-[#f0e8e4] text-[#865a50]' :
                        pt.level === 'N3' ? 'bg-[#f4efe4] text-[#8f7142]' :
                        pt.level === 'N4' ? 'bg-[#e5ecf0] text-[#4d6a78]' :
                        'bg-[#e6eee3] text-[#4d6b47]'
                      }`}>
                        {pt.level}
                      </span>
                    )}
                  </div>

                  {/* Core English Meaning */}
                  <div className="text-[11.5px] text-[#617066] line-clamp-1 leading-snug">
                    {pt.meaning}
                  </div>

                  {/* Book source tag if present */}
                  {pt.book && (
                    <div className="text-[10px] text-[#8b9588] mt-1 flex items-center gap-1">
                      <Book className="w-2.5 h-2.5 shrink-0 opacity-70" />
                      <span className="truncate">{pt.book} · {pt.chapter}</span>
                    </div>
                  )}
                </div>

                {/* Explicit Completion Indicator (Click to toggle) */}
                <span
                  role="button"
                  tabIndex={0}
                  onClick={(e) => {
                    e.stopPropagation();
                    onToggleCompleted(pt.id);
                  }}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault();
                      e.stopPropagation();
                      onToggleCompleted(pt.id);
                    }
                  }}
                  title={isStudied ? "Marked as completed (Click to unmark)" : "Not completed (Click to mark completed)"}
                  className="shrink-0 p-1 -m-1 rounded hover:bg-[#e0ded0] transition-colors cursor-pointer"
                >
                  {isStudied ? (
                    <div className="w-4 h-4 rounded-full bg-[#467b6b] hover:bg-[#386255] text-white flex items-center justify-center transition-colors">
                      <Check className="w-2.5 h-2.5 stroke-[3]" />
                    </div>
                  ) : (
                    <div className="w-4 h-4 rounded-full border border-[#cfcebe] hover:border-[#467b6b] hover:bg-[#eef5f1] transition-colors" />
                  )}
                </span>
              </div>
            );
          })
        )}
      </div>
    </aside>
  );
};

