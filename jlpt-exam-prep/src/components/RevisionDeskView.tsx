import React, { useState } from 'react';
import { MASTER_MUG_UP_TABLES } from '../data/mugUpTables';
import { MugUpTableView } from './MugUpTableView';
import type { MugUpTable, JLPTLevel } from '../types';
import { Table, BookOpen, ArrowRight } from 'lucide-react';

interface TableMeta {
  key: string;
  table: MugUpTable;
  level: JLPTLevel;
  lessonId: string;
  lessonLabel: string;
}

const REVISION_TABLES_CATALOG: TableMeta[] = [
  {
    key: 'genki1TimeAndAgeMatrix',
    table: MASTER_MUG_UP_TABLES.genki1TimeAndAgeMatrix,
    level: 'N5',
    lessonId: 'g1-l1-time-and-age',
    lessonLabel: 'Genki I · Lesson 1 (Time & Age)'
  },
  {
    key: 'genki1VerbGroupsMatrix',
    table: MASTER_MUG_UP_TABLES.genki1VerbGroupsMatrix,
    level: 'N5',
    lessonId: 'added-g1-3-2',
    lessonLabel: 'Genki I · Lesson 3 (Verb Groups & Masu)'
  },
  {
    key: 'genki1AdjectivesMatrix',
    table: MASTER_MUG_UP_TABLES.genki1AdjectivesMatrix,
    level: 'N5',
    lessonId: 'g1-l5-adjectives',
    lessonLabel: 'Genki I · Lesson 5 (Adjectives Conjugation)'
  },
  {
    key: 'teFormMatrix',
    table: MASTER_MUG_UP_TABLES.teFormMatrix,
    level: 'N5',
    lessonId: 'added-g1-6-8',
    lessonLabel: 'Genki I · Lesson 6 (Te-Form Matrix)'
  },
  {
    key: 'genki1ShortFormsMatrix',
    table: MASTER_MUG_UP_TABLES.genki1ShortFormsMatrix,
    level: 'N5',
    lessonId: 'added-g1-8-12',
    lessonLabel: 'Genki I · Lessons 8 & 9 (Short Forms 普通形)'
  },
  {
    key: 'genki2PotentialMatrix',
    table: MASTER_MUG_UP_TABLES.genki2PotentialMatrix,
    level: 'N4',
    lessonId: 'added-g2-13-20',
    lessonLabel: 'Genki II · Lesson 13 (Potential Form 可能形)'
  },
  {
    key: 'givingReceivingMatrix',
    table: MASTER_MUG_UP_TABLES.givingReceivingMatrix,
    level: 'N4',
    lessonId: 'added-g2-14-22',
    lessonLabel: 'Genki II · Lessons 14 & 16 (Giving & Receiving 授受動詞)'
  },
  {
    key: 'genki2VolitionalMatrix',
    table: MASTER_MUG_UP_TABLES.genki2VolitionalMatrix,
    level: 'N4',
    lessonId: 'added-g2-15-24',
    lessonLabel: 'Genki II · Lesson 15 (Volitional Form 意向形)'
  },
  {
    key: 'conditionalsMatrix',
    table: MASTER_MUG_UP_TABLES.conditionalsMatrix,
    level: 'N4',
    lessonId: 'added-g2-17-28',
    lessonLabel: 'Genki II · Lesson 17 & SKM N3 Unit 2 (Conditionals: と・ば・たら・なら)'
  },
  {
    key: 'genki2TransitiveIntransitiveMatrix',
    table: MASTER_MUG_UP_TABLES.genki2TransitiveIntransitiveMatrix,
    level: 'N4',
    lessonId: 'added-g2-18-30',
    lessonLabel: 'Genki II · Lesson 18 (Transitive vs Intransitive 他動詞・自動詞)'
  },
  {
    key: 'keigoMatrix',
    table: MASTER_MUG_UP_TABLES.keigoMatrix,
    level: 'N4',
    lessonId: 'g2-l19-sonkeigo-verbs',
    lessonLabel: 'Genki II · Lessons 19 & 20 (Keigo Survival 敬語)'
  },
  {
    key: 'voiceMatrix',
    table: MASTER_MUG_UP_TABLES.voiceMatrix,
    level: 'N4',
    lessonId: 'added-g2-21-38',
    lessonLabel: 'Genki II · Lessons 21-23 (Voice Ladder: 受身・使役・使役受身)'
  },
  {
    key: 'timeSequenceSpectrum',
    table: MASTER_MUG_UP_TABLES.timeSequenceSpectrum,
    level: 'N3',
    lessonId: 'skm3-u1-tokoro-da-phases',
    lessonLabel: 'SKM N3 · Chapter 1 (Time Sequence Spectrum)'
  },
  {
    key: 'skmN2ClassicalRemnantsMatrix',
    table: MASTER_MUG_UP_TABLES.skmN2ClassicalRemnantsMatrix,
    level: 'N2',
    lessonId: 'added-n2-c-118',
    lessonLabel: 'SKM N2 · Form Review C (Classical Remnants: ず・まい・べし)'
  },
  {
    key: 'skmN2ConnectorsMatrix',
    table: MASTER_MUG_UP_TABLES.skmN2ConnectorsMatrix,
    level: 'N2',
    lessonId: 'added-n2-p3-10-150',
    lessonLabel: 'SKM N2 · Part 3 Chapter 10 (The 9 Discourse Connector Categories)'
  }
];

interface Props {
  onNavigateToLesson: (lessonId: string) => void;
  onExitRevision: () => void;
}

export const RevisionDeskView: React.FC<Props> = ({
  onNavigateToLesson,
  onExitRevision
}) => {
  const [selectedKey, setSelectedKey] = useState<string>(REVISION_TABLES_CATALOG[0].key);
  const [levelFilter, setLevelFilter] = useState<'all' | 'N5' | 'N4' | 'N3' | 'N2'>('all');

  const filteredTables = REVISION_TABLES_CATALOG.filter(item => {
    if (levelFilter === 'all') return true;
    return item.level === levelFilter;
  });

  const currentMeta =
    REVISION_TABLES_CATALOG.find(t => t.key === selectedKey) || filteredTables[0] || REVISION_TABLES_CATALOG[0];

  return (
    <div className="flex-1 min-w-0 bg-[#ffffff] md:h-[calc(100vh-64px)] overflow-y-auto">
      <div className="max-w-4xl mx-auto px-6 sm:px-10 py-8 space-y-6">
        {/* Header */}
        <div className="border-b border-[#dfded3] pb-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Table className="w-4 h-4 text-[#467b6b]" />
              <h1 className="text-lg font-bold text-[#1e2d26]">
                Revision & Master "Mug-Up" Tables
              </h1>
            </div>
            <p className="text-xs text-[#788278]">
              High-yield conjugation matrices and cross-chapter synthesis sheets.
            </p>
          </div>

          {/* Level Filter Tabs */}
          <div className="flex items-center gap-1 bg-[#edebe0] p-1 rounded-md self-start sm:self-auto">
            {(['all', 'N5', 'N4', 'N3', 'N2'] as const).map(lvl => (
              <button
                key={lvl}
                onClick={() => setLevelFilter(lvl)}
                className={`px-2.5 py-1 rounded text-xs transition-colors ${
                  levelFilter === lvl
                    ? 'bg-white text-[#283b35] font-semibold shadow-xs'
                    : 'text-[#617066] hover:text-[#283b35]'
                }`}
              >
                {lvl === 'all' ? 'All' : lvl}
              </button>
            ))}
          </div>
        </div>

        {/* Horizontal Table Switcher */}
        <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-thin">
          {filteredTables.map(item => {
            const isSelected = item.key === currentMeta.key;
            return (
              <button
                key={item.key}
                onClick={() => setSelectedKey(item.key)}
                className={`px-3 py-1.5 rounded-md text-xs whitespace-nowrap shrink-0 border transition-all ${
                  isSelected
                    ? 'bg-[#467b6b] text-white border-[#467b6b] font-semibold shadow-xs'
                    : 'bg-[#faf9f5] border-[#dfded3] text-[#617066] hover:bg-[#edece1] hover:text-[#283b35]'
                }`}
              >
                <span className="opacity-75 mr-1">[{item.level}]</span>
                <span>{item.table.title.split(':')[0]}</span>
              </button>
            );
          })}
        </div>

        {/* Selected Table Container */}
        {currentMeta && (
          <div className="space-y-4">
            {/* Table Action Bar */}
            <div className="flex items-center justify-between p-3 rounded-lg bg-[#faf9f5] border border-[#dfded3]">
              <div className="flex items-center gap-2 text-xs text-[#617066]">
                <BookOpen className="w-3.5 h-3.5 text-[#467b6b]" />
                <span>Primary Lesson: <strong>{currentMeta.lessonLabel}</strong></span>
              </div>

              <button
                onClick={() => onNavigateToLesson(currentMeta.lessonId)}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded bg-white border border-[#467b6b] text-[#2c5347] text-xs font-semibold hover:bg-[#eaf4ef] transition-colors"
              >
                <span>Jump to Lesson in Textbook</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>

            {/* Render High-Yield Table */}
            <div className="rounded-lg border border-[#dfded3] bg-white p-4">
              <MugUpTableView table={currentMeta.table} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
