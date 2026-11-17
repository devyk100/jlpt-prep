import { AnnotatedText } from './AnnotatedText';
import { useModal } from '../useModal';
import React, { useState } from 'react';
import { BOOK_SOURCES } from '../data/bookCatalog';
import { GRAMMAR_BY_ID } from '../data/grammarData';
import { Library, X, ArrowRight, Book } from 'lucide-react';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  onSelectPoint: (pointId: string, streamId?: string) => void;
}

export const BookCatalogModal: React.FC<Props> = ({
  isOpen,
  onClose,
  onSelectPoint
}) => {
  const [selectedBookId, setSelectedBookId] = useState<string>(BOOK_SOURCES[0].id);

  const dialogRef = useModal(isOpen, onClose);
  if (!isOpen) return null;

  const currentBook = BOOK_SOURCES.find(b => b.id === selectedBookId) || BOOK_SOURCES[0];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#283b3550] backdrop-blur-xs animate-in fade-in duration-100">
      <div
        ref={dialogRef} role="dialog" aria-modal="true" aria-label="Textbook revision sections"
        className="w-full max-w-3xl max-h-[90vh] bg-[#fffef9] rounded-lg shadow-2xl border border-[#c5cebc] flex flex-col overflow-hidden"
        onClick={e => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between p-4 border-b border-[#dfded3] bg-[#f9f8f2]">
          <div className="flex items-center gap-2">
            <Library className="w-4 h-4 text-[#467b6b]" />
            <h3 className="text-sm font-bold text-[#1e2d26]">
              Textbook revision sections (Genki I/II · SKM N3/N2)
            </h3>
          </div>

          <button
            aria-label="Close textbook catalog"
            onClick={onClose}
            className="p-1 rounded text-[#788278] hover:text-[#283b35]"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* 4 Books Tab Selector */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-1.5 p-2.5 bg-[#f5f4ec] border-b border-[#dfded3]">
          {BOOK_SOURCES.map(book => {
            const isSelected = book.id === selectedBookId;
            return (
              <button
                key={book.id}
                onClick={() => setSelectedBookId(book.id)}
                className={`p-2 rounded text-left transition-colors border ${
                  isSelected
                    ? 'bg-[#ffffff] border-[#467b6b] text-[#283b35] font-semibold'
                    : 'bg-[#faf9f5] border-[#dfded3] text-[#617066] hover:bg-[#edece1]'
                }`}
              >
                <div className="text-[9px] uppercase font-bold text-[#788278]">{book.level}</div>
                <div className="text-xs truncate font-medium">{book.name}</div>
              </button>
            );
          })}
        </div>

        {/* Content Area */}
        <div className="flex-1 overflow-y-auto p-5 space-y-4">
          <p className="text-xs text-[#617066] leading-relaxed border-b border-[#eeeFe7] pb-3">
            <span className="font-semibold text-[#283b35]">{currentBook.name}</span> — {currentBook.description}
          </p>

          <div className="space-y-3">
            {currentBook.sections.map((sec, sIdx) => (
              <div key={`sec-${sIdx}`} className="rounded border border-[#e2e1d7] bg-[#fbfaf5] p-3">
                <div className="text-xs font-bold text-[#283b35] mb-2 flex items-center gap-1.5">
                  <Book className="w-3 h-3 text-[#467b6b]" />
                  <span>{sec.name}</span>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
                  {sec.grammarIds.map(id => {
                    const pt = GRAMMAR_BY_ID[id];
                    if (!pt) return null;

                    return (
                      <button
                        type="button"
                        key={id}
                        onClick={() => {
                          onSelectPoint(pt.id, pt.streamId);
                          onClose();
                        }}
                        className="flex items-center justify-between p-2 rounded border border-[#dfded3] bg-[#ffffff] hover:bg-[#f0f4ee] hover:border-[#467b6b] cursor-pointer transition-colors group"
                      >
                        <div className="truncate pr-2">
                          <span className="font-serif-ja text-xs font-semibold text-[#1e2d26] group-hover:text-[#467b6b] block truncate">
                            <AnnotatedText text={pt.title.split(' (')[0]} level={pt.level} passive />
                          </span>
                          <span className="text-[10.5px] text-[#788278] block truncate">
                            {pt.meaning}
                          </span>
                        </div>
                        <ArrowRight className="w-3 h-3 text-[#8a9485] group-hover:text-[#467b6b] shrink-0" />
                      </button>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
