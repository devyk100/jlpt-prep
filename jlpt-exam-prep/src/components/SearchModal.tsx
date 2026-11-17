import { AnnotatedText } from './AnnotatedText';
import { useModal } from '../useModal';
import React, { useState, useEffect, useRef } from 'react';
import type { GrammarPoint } from '../types';
import { Search, X, ArrowRight } from 'lucide-react';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  allPoints: GrammarPoint[];
  onSelectPoint: (pointId: string, streamId?: string) => void;
  seamlessFlowMode: boolean;
}

export const SearchModal: React.FC<Props> = ({
  isOpen,
  onClose,
  allPoints,
  onSelectPoint,
  seamlessFlowMode
}) => {
  const [query, setQuery] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 50);
    } else {
      setQuery('');
    }
  }, [isOpen]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) onClose();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  const dialogRef = useModal(isOpen, onClose);
  if (!isOpen) return null;

  const filtered = query.trim() === ''
    ? allPoints.slice(0, 10)
    : allPoints.filter(p => {
        const q = query.toLowerCase();
        return (
          p.title.toLowerCase().includes(q) ||
          p.meaning.toLowerCase().includes(q) ||
          p.connection.toLowerCase().includes(q) ||
          p.level.toLowerCase().includes(q) ||
          (p.book && p.book.toLowerCase().includes(q)) ||
          p.tags.some(t => t.toLowerCase().includes(q))
        );
      });

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-16 sm:pt-24 p-4 bg-[#283b3550] backdrop-blur-xs animate-in fade-in duration-100">
      <div
        ref={dialogRef} role="dialog" aria-modal="true" aria-label="Search grammar"
        className="w-full max-w-xl bg-[#fffef9] rounded-lg shadow-2xl border border-[#c5cebc] overflow-hidden"
        onClick={e => e.stopPropagation()}
      >
        {/* Search Header Input */}
        <div className="flex items-center gap-2.5 p-3.5 border-b border-[#dfded3] bg-[#f9f8f2]">
          <Search className="w-4 h-4 text-[#788278] shrink-0" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder="Search grammar, reading, or English meaning..."
            className="flex-1 bg-transparent border-none outline-none text-[#283b35] placeholder:text-[#9da292] text-sm"
          />
          {query && (
            <button
              onClick={() => setQuery('')}
              className="p-1 text-[#788278] hover:text-[#283b35]"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
          <button
            aria-label="Close dialog" onClick={onClose}
            className="text-[10px] font-mono px-2 py-0.5 rounded border border-[#dfded3] bg-[#f0eee4] text-[#617066]"
          >
            ESC
          </button>
        </div>

        {/* Results List */}
        <div className="max-h-[60vh] overflow-y-auto divide-y divide-[#eeeFe7] p-2">
          {filtered.length === 0 ? (
            <div className="p-8 text-center text-xs text-[#8a9485]">
              No matching grammar points found for "{query}".
            </div>
          ) : (
            filtered.map(pt => (
              <div
                key={pt.id}
                onClick={() => {
                  onSelectPoint(pt.id, pt.streamId);
                  onClose();
                }}
                className="flex items-center justify-between p-2.5 rounded hover:bg-[#f2efe6] cursor-pointer transition-colors group"
              >
                <div className="space-y-0.5 pr-3 min-w-0">
                  <div className="flex items-center gap-2">
                    <span className="font-serif-ja font-semibold text-sm text-[#1e2d26] group-hover:text-[#467b6b]">
                      <AnnotatedText text={pt.title.split(' (')[0]} level={pt.level} passive />
                    </span>
                    {!seamlessFlowMode && (
                      <span className="text-[9px] px-1.5 py-0.2 rounded font-semibold uppercase bg-[#edebe0] text-[#617066]">
                        {pt.level}
                      </span>
                    )}
                    {pt.book && (
                      <span className="text-[10px] text-[#8a9485]">
                        {pt.book}
                      </span>
                    )}
                  </div>
                  <div className="text-xs text-[#617066] truncate">
                    {pt.meaning}
                  </div>
                </div>

                <ArrowRight className="w-3.5 h-3.5 text-[#8a9485] group-hover:text-[#467b6b] shrink-0" />
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};
