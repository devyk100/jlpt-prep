import { createContext, useContext } from 'react';
import type { JLPTLevel } from './types';
export type ReadingMode = 'book' | 'all' | 'hover' | 'off';
export const ReadingContext = createContext<{ mode: ReadingMode; level: JLPTLevel }>({ mode: 'book', level: 'N3' });
export function useReadingMode(level?: JLPTLevel): 'all' | 'hover' | 'off' {
  const context = useContext(ReadingContext);
  return context.mode === 'book' ? ((level || context.level) === 'N2' ? 'hover' : 'all') : context.mode;
}
