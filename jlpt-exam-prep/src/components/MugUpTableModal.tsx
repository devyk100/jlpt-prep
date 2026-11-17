import { useModal } from '../useModal';
import React, { useState } from 'react';
import { MASTER_MUG_UP_TABLES } from '../data/mugUpTables';
import { MugUpTableView } from './MugUpTableView';
import { Table, X } from 'lucide-react';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  initialTableKey?: string;
}

export const MugUpTableModal: React.FC<Props> = ({ isOpen, onClose, initialTableKey }) => {
  const tableKeys = Object.keys(MASTER_MUG_UP_TABLES);
  const [selectedKey, setSelectedKey] = useState<string>(initialTableKey || tableKeys[0]);

  const dialogRef = useModal(isOpen, onClose);
  if (!isOpen) return null;

  const currentTable = MASTER_MUG_UP_TABLES[selectedKey] || MASTER_MUG_UP_TABLES[tableKeys[0]];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#283b3550] backdrop-blur-xs animate-in fade-in duration-100">
      <div
        ref={dialogRef} role="dialog" aria-modal="true" aria-label="Grammar tables"
        className="w-full max-w-4xl max-h-[90vh] bg-[#fffef9] rounded-lg shadow-2xl border border-[#c5cebc] flex flex-col overflow-hidden"
        onClick={e => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between p-4 border-b border-[#dfded3] bg-[#f9f8f2]">
          <div className="flex items-center gap-2">
            <Table className="w-4 h-4 text-[#8f7142]" />
            <h3 className="text-sm font-bold text-[#1e2d26]">
              High-Yield Mug-Up Matrices (暗記テーブル)
            </h3>
          </div>

          <button
            aria-label="Close dialog" onClick={onClose}
            className="p-1 rounded text-[#788278] hover:text-[#283b35]"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Table Selector Tabs */}
        <div className="flex items-center gap-1.5 p-2.5 bg-[#f5f4ec] border-b border-[#dfded3] overflow-x-auto scrollbar-none">
          {tableKeys.map(key => {
            const tbl = MASTER_MUG_UP_TABLES[key];
            const isSelected = key === selectedKey;

            return (
              <button
                key={key}
                onClick={() => setSelectedKey(key)}
                className={`px-3 py-1 rounded text-xs whitespace-nowrap transition-colors ${
                  isSelected
                    ? 'bg-[#467b6b] text-white font-semibold'
                    : 'bg-[#fffef9] text-[#617066] border border-[#dfded3] hover:bg-[#edece1]'
                }`}
              >
                {tbl.title.split(':')[0]}
              </button>
            );
          })}
        </div>

        {/* Content Table Scroll Area */}
        <div className="flex-1 overflow-y-auto p-5">
          <MugUpTableView table={currentTable} />
        </div>
      </div>
    </div>
  );
};
