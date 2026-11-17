import React from 'react';
import type { StreamCategory } from '../types';
import {
  Compass,
  Search,
  BookmarkCheck,
  Table,
  Library,
  ChevronDown
} from 'lucide-react';

interface Props {
  streams: StreamCategory[];
  currentStreamId: string;
  onSelectStream: (streamId: string) => void;
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

export const Navbar: React.FC<Props> = ({
  streams,
  currentStreamId,
  onSelectStream,
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
    <header className="sticky top-0 z-40 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-b border-slate-200/80 dark:border-slate-800 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-4">
        {/* Brand Logo & Stream Switcher */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2">
            <div className="w-9 h-9 rounded-2xl bg-gradient-to-tr from-amber-500 to-amber-600 flex items-center justify-center text-white shadow-md shadow-amber-500/20 font-black text-lg">
              文
            </div>
            <div className="hidden sm:block">
              <span className="font-extrabold text-base tracking-tight text-slate-900 dark:text-white">
                Bunpou<span className="text-amber-500">Flow</span>
              </span>
              <span className="hidden md:inline-block ml-2 text-[0.68rem] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400 font-semibold">
                N5 → N2 Mastery
              </span>
            </div>
          </div>

          {/* Stream Selector Dropdown */}
          <div className="relative">
            <select
              value={currentStreamId}
              onChange={e => onSelectStream(e.target.value)}
              className="appearance-none pl-3 pr-8 py-1.5 rounded-xl text-xs sm:text-sm font-semibold bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-200 dark:border-slate-700 hover:bg-slate-200/70 dark:hover:bg-slate-700/70 cursor-pointer transition-colors max-w-[160px] sm:max-w-[220px] truncate"
            >
              {streams.map(stream => (
                <option key={stream.id} value={stream.id}>
                  {stream.title} ({stream.grammarIds.length})
                </option>
              ))}
            </select>
            <ChevronDown className="w-3.5 h-3.5 text-slate-400 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          </div>
        </div>

        {/* Right Controls */}
        <div className="flex items-center gap-2">
          {/* Quick Search */}
          <button
            onClick={onOpenSearch}
            title="Search grammar (Ctrl+K)"
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200/70 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 text-xs font-medium border border-slate-200/60 dark:border-slate-700 transition-colors"
          >
            <Search className="w-3.5 h-3.5 text-slate-400" />
            <span className="hidden md:inline">Search</span>
            <kbd className="hidden lg:inline text-[0.62rem] px-1 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-500 dark:text-slate-400 font-mono">
              ⌘K
            </kbd>
          </button>

          {/* 4 Books Explorer */}
          <button
            onClick={onOpenBookCatalog}
            title="Explore 4 Canonical Books (Genki I/II, SKM N3/N2)"
            className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-700 dark:text-indigo-300 text-xs font-semibold border border-indigo-500/20 transition-colors"
          >
            <Library className="w-3.5 h-3.5 text-indigo-500" />
            <span className="hidden sm:inline">4 Books</span>
          </button>

          {/* Mug-Up Tables Reference Library */}
          <button
            onClick={onOpenTablesModal}
            title="Open High-Yield Mug-Up Tables"
            className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-700 dark:text-amber-300 text-xs font-semibold border border-amber-500/20 transition-colors"
          >
            <Table className="w-3.5 h-3.5 text-amber-500" />
            <span className="hidden sm:inline">Cheat Tables</span>
          </button>

          {/* Mistake Bank Button */}
          <button
            onClick={onOpenMistakeBank}
            title="Review Flagged Weak Points"
            className="relative p-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200/70 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-colors"
          >
            <BookmarkCheck className="w-4 h-4 text-slate-500 dark:text-slate-400" />
            {mistakeCount > 0 && (
              <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-rose-500 text-white text-[0.62rem] font-bold flex items-center justify-center animate-pulse">
                {mistakeCount}
              </span>
            )}
          </button>

          {/* Furigana Mode Selector */}
          <div className="flex items-center rounded-xl bg-slate-100 dark:bg-slate-800 p-0.5 border border-slate-200/60 dark:border-slate-700 text-xs">
            <button
              onClick={() => onChangeFuriganaMode('all')}
              className={`px-2 py-1 rounded-lg font-medium transition-all ${
                furiganaMode === 'all'
                  ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs font-bold'
                  : 'text-slate-400 hover:text-slate-700 dark:hover:text-slate-200'
              }`}
              title="Show Furigana always"
            >
              All
            </button>
            <button
              onClick={() => onChangeFuriganaMode('hover')}
              className={`px-2 py-1 rounded-lg font-medium transition-all ${
                furiganaMode === 'hover'
                  ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs font-bold'
                  : 'text-slate-400 hover:text-slate-700 dark:hover:text-slate-200'
              }`}
              title="Show Furigana on hover only"
            >
              Hover
            </button>
            <button
              onClick={() => onChangeFuriganaMode('off')}
              className={`px-2 py-1 rounded-lg font-medium transition-all ${
                furiganaMode === 'off'
                  ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs font-bold'
                  : 'text-slate-400 hover:text-slate-700 dark:hover:text-slate-200'
              }`}
              title="Hide Furigana"
            >
              Off
            </button>
          </div>

          {/* Seamless Flow Toggle */}
          <button
            onClick={onToggleSeamlessFlow}
            title={
              seamlessFlowMode
                ? 'Seamless Flow Mode Active: Rigid level badges blurred to preserve continuous study flow.'
                : 'Standard Level View: Shows explicit N5/N4/N3/N2 badges.'
            }
            className={`flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl text-xs font-bold transition-all border ${
              seamlessFlowMode
                ? 'bg-indigo-500 text-white border-indigo-600 shadow-sm shadow-indigo-500/20'
                : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-700 hover:text-slate-900'
            }`}
          >
            <Compass className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">
              {seamlessFlowMode ? 'Flow Mode' : 'Level View'}
            </span>
          </button>
        </div>
      </div>
    </header>
  );
};
