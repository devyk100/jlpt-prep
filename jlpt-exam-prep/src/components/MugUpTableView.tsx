import React from 'react';
import type { MugUpTable } from '../types';
import { Table } from 'lucide-react';

interface Props {
  table: MugUpTable;
}

export const MugUpTableView: React.FC<Props> = ({ table }) => {
  return (
    <div className="rounded-lg border border-[#dfded3] bg-[#faf9f5] p-4 my-4">
      <div className="flex items-start gap-2 mb-2.5">
        <Table className="w-4 h-4 text-[#8f7142] shrink-0 mt-0.5" />
        <div>
          <h4 className="text-sm font-bold text-[#1e2d26] flex items-center gap-2">
            <span>{table.title}</span>
            <span className="text-[9px] px-1.5 py-0.2 rounded bg-[#ebe8db] text-[#6e5831] font-semibold uppercase">
              Mug-Up Matrix
            </span>
          </h4>
          {table.subtitle && (
            <p className="text-xs text-[#788278] mt-0.5 leading-snug">
              {table.subtitle}
            </p>
          )}
        </div>
      </div>

      {/* Table Container */}
      <div className="overflow-x-auto rounded border border-[#dfded3] bg-[#fffef9]">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="bg-[#f2efe6] border-b border-[#dfded3] text-[#4d5b52]">
              {table.columns.map((col, idx) => (
                <th key={`col-${idx}`} className="p-2.5 font-semibold first:pl-3 last:pr-3 whitespace-nowrap">
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-[#eceae0]">
            {table.rows.map((row, rIdx) => (
              <tr key={`row-${rIdx}`} className="hover:bg-[#f6f4ec] transition-colors">
                <td className="p-2.5 pl-3 font-semibold text-[#6e5831] whitespace-nowrap">
                  {row.label}
                  {row.note && (
                    <div className="text-[10px] font-normal text-[#8a9485] mt-0.5">
                      {row.note}
                    </div>
                  )}
                </td>
                {row.cells.map((cell, cIdx) => (
                  <td key={`cell-${rIdx}-${cIdx}`} className="p-2.5 text-[#283b35] leading-relaxed">
                    {cell}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
