import React from 'react';
import {
  Search,
  BookmarkCheck,
  Table,
  Library,
  Compass,
  BookOpen,
  CheckCircle2
} from 'lucide-react';

export type StudyMode = 'learn' | 'practice' | 'revision';

interface Props {
  activeMode: StudyMode;
  onModeChange: (mode: StudyMode) => void;
  selectedFilter: 'all' | 'N5' | 'N4' | 'N3' | 'N2';
  onFilterChange: (f: 'all' | 'N5' | 'N4' | 'N3' | 'N2') => void;
  seamlessFlowMode: boolean;
  onToggleSeamlessFlow: () => void;
  furiganaMode: 'book' | 'all' | 'hover' | 'off';
  onChangeFuriganaMode: (mode: 'book' | 'all' | 'hover' | 'off') => void;
  onOpenSearch: () => void;
  onOpenMistakeBank: () => void;
  onOpenTablesModal: () => void;
  onOpenBookCatalog: () => void;
  mistakeCount: number;
}

export const Topbar: React.FC<Props> = ({
  activeMode,
  onModeChange,
  selectedFilter,
  onFilterChange,
  seamlessFlowMode,
  onToggleSeamlessFlow,
  furiganaMode,
  onChangeFuriganaMode,
  onOpenSearch,
  onOpenMistakeBank,
  onOpenTablesModal,
  onOpenBookCatalog,
  mistakeCount
}) => {
  return (
    <header className="min-h-16 py-2 flex-wrap px-4 sm:px-8 border-b border-[#dfded3] bg-[#f6f4edf5] sticky top-0 z-40 backdrop-blur-md flex items-center justify-between gap-4">
      {/* Brand Mark (Inspired by Kanji Atlas) */}
      <div className="flex items-center gap-3">
        <div className="w-[38px] h-[38px] border border-[#b8bfb0] bg-[#fffef9] flex items-center justify-center font-serif-ja text-[24px] text-[#283b35] select-none shrink-0">
          文
        </div>
        <div>
          <span className="font-semibold text-[17px] tracking-tight text-[#283b35] block leading-tight">
            Bunpou Atlas
          </span>
          <small className="block text-[9px] tracking-wider text-[#788278] font-medium uppercase">
            N5 · N4 · N3 · N2 Digital Textbook
          </small>
        </div>
      </div>

      {/* Primary Activity Mode Switcher: Learn | Practice | Revision */}
      <nav aria-label="Activity Modes" className="flex items-center rounded-md border border-[#cfcebe] bg-[#fffef9] p-0.5 text-xs">
        <button
          onClick={() => onModeChange('learn')}
          className={`flex items-center gap-1.5 px-3 py-1 rounded transition-all ${
            activeMode === 'learn'
              ? 'bg-[#467b6b] text-white font-semibold shadow-xs'
              : 'text-[#617066] hover:text-[#283b35]'
          }`}
          title="Digital textbook lesson study"
        >
          <BookOpen className="w-3.5 h-3.5" />
          <span>Learn (学習)</span>
        </button>

        <button
          onClick={() => onModeChange('practice')}
          className={`flex items-center gap-1.5 px-3 py-1 rounded transition-all ${
            activeMode === 'practice'
              ? 'bg-[#467b6b] text-white font-semibold shadow-xs'
              : 'text-[#617066] hover:text-[#283b35]'
          }`}
          title="Chapter-level exercises without answer leakage"
        >
          <CheckCircle2 className="w-3.5 h-3.5" />
          <span>Practice (練習)</span>
        </button>

        <button
          onClick={() => onModeChange('revision')}
          className={`flex items-center gap-1.5 px-3 py-1 rounded transition-all ${
            activeMode === 'revision'
              ? 'bg-[#467b6b] text-white font-semibold shadow-xs'
              : 'text-[#617066] hover:text-[#283b35]'
          }`}
          title="Master tables & summary sheets"
        >
          <Table className="w-3.5 h-3.5" />
          <span>Revision (暗記表)</span>
        </button>
      </nav>

      {/* Level Filter Quick Jump (in Learn mode) */}
      <nav className="hidden xl:flex items-center gap-1 bg-[#edebe0] p-1 rounded-md">
        {(['all', 'N5', 'N4', 'N3', 'N2'] as const).map(lvl => {
          const isSelected = selectedFilter === lvl;
          const label = lvl === 'all' ? 'Continuous Flow' : lvl;

          return (
            <button
              key={lvl}
              onClick={() => onFilterChange(lvl)}
              className={`px-3 py-1 rounded text-xs transition-colors ${
                isSelected
                  ? 'bg-[#ffffff] text-[#283b35] font-semibold shadow-xs'
                  : 'text-[#617066] hover:text-[#283b35]'
              }`}
            >
              {label}
            </button>
          );
        })}
      </nav>

      {/* Right Controls */}
      <div className="flex items-center gap-2">
        {/* Quick Search */}
        <button
          onClick={onOpenSearch}
          title="Search grammar (Ctrl+K)"
          className="flex items-center gap-1.5 px-2.5 py-1.5 rounded border border-[#cfcebe] bg-[#fffef9] hover:bg-[#edece1] text-xs text-[#283b35] transition-colors"
        >
          <Search className="w-3.5 h-3.5 text-[#788278]" />
          <span className="hidden sm:inline">Search</span>
          <kbd className="hidden lg:inline text-[9px] px-1 py-0.2 rounded bg-[#ebe9dc] text-[#788278] font-mono">
            ⌘K
          </kbd>
        </button>

        {/* 4 Books Explorer */}
        <button
          onClick={onOpenBookCatalog}
          title="View Canonical Books Coverage"
          className="flex items-center gap-1.5 px-2.5 py-1.5 rounded border border-[#cfcebe] bg-[#fffef9] hover:bg-[#edece1] text-xs text-[#283b35] transition-colors"
        >
          <Library className="w-3.5 h-3.5 text-[#5a7884]" />
          <span className="hidden sm:inline">4 Books</span>
        </button>

        {/* Cheat Tables */}
        <button
          onClick={onOpenTablesModal}
          title="Must-Memorize Mug-Up Tables"
          className="flex items-center gap-1.5 px-2.5 py-1.5 rounded border border-[#cfcebe] bg-[#fffef9] hover:bg-[#edece1] text-xs text-[#283b35] transition-colors"
        >
          <Table className="w-3.5 h-3.5 text-[#8f7142]" />
          <span className="hidden sm:inline">Cheat Tables</span>
        </button>

        {/* Mistake Bank */}
        <button
          onClick={onOpenMistakeBank}
          title="Review Weak Points"
          className="relative p-1.5 rounded border border-[#cfcebe] bg-[#fffef9] hover:bg-[#edece1] text-[#283b35] transition-colors"
        >
          <BookmarkCheck className="w-4 h-4 text-[#788278]" />
          {mistakeCount > 0 && (
            <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-[#967065] text-white text-[9px] font-bold flex items-center justify-center">
              {mistakeCount}
            </span>
          )}
        </button>

        {/* Furigana Mode Switcher */}
        <div className="flex items-center rounded border border-[#cfcebe] bg-[#fffef9] p-0.5 text-xs">
          <button
            onClick={() => onChangeFuriganaMode('book')}
            title="Textbook readings: Genki/N3 above; N2 on hover"
            aria-pressed={furiganaMode === 'book'}
            className={`px-2 py-0.5 rounded ${furiganaMode === 'book' ? 'bg-[#467b6b] text-white' : ''}`}
          >
            Book
          </button>
          <button
            onClick={() => onChangeFuriganaMode('all')}
            className={`px-2 py-0.5 rounded transition-all ${
              furiganaMode === 'all'
                ? 'bg-[#467b6b] text-white font-medium'
                : 'text-[#617066] hover:text-[#283b35]'
            }`}
            title="Always show Furigana"
          >
            All
          </button>
          <button
            onClick={() => onChangeFuriganaMode('hover')}
            className={`px-2 py-0.5 rounded transition-all ${
              furiganaMode === 'hover'
                ? 'bg-[#467b6b] text-white font-medium'
                : 'text-[#617066] hover:text-[#283b35]'
            }`}
            title="Show Furigana on hover only"
          >
            Hover
          </button>
          <button
            onClick={() => onChangeFuriganaMode('off')}
            className={`px-2 py-0.5 rounded transition-all ${
              furiganaMode === 'off'
                ? 'bg-[#467b6b] text-white font-medium'
                : 'text-[#617066] hover:text-[#283b35]'
            }`}
            title="Hide Furigana"
          >
            Off
          </button>
        </div>

        {/* Flow Mode Toggle */}
        <button
          onClick={onToggleSeamlessFlow}
          title={seamlessFlowMode ? 'Flow Mode Active (Level borders blurred)' : 'Level View Active (Explicit N5-N2 labels)'}
          className={`flex items-center gap-1 px-2.5 py-1.5 rounded text-xs transition-colors border ${
            seamlessFlowMode
              ? 'bg-[#467b6b] text-white border-[#467b6b] font-medium'
              : 'border-[#cfcebe] bg-[#fffef9] text-[#617066] hover:text-[#283b35]'
          }`}
        >
          <Compass className="w-3.5 h-3.5" />
          <span className="hidden md:inline">
            {seamlessFlowMode ? 'Flow' : 'Levels'}
          </span>
        </button>
      </div>
    </header>
  );
};

export default Topbar;
