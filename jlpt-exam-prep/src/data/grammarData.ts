import type { GrammarPoint, StreamCategory } from '../types';
import points from './studyPoints.json';
import { STREAM_CATEGORIES } from './grammarStreams';
export const ALL_GRAMMAR_POINTS = points as GrammarPoint[];
export const GRAMMAR_BY_ID: Record<string, GrammarPoint> = Object.fromEntries(ALL_GRAMMAR_POINTS.map(p => [p.id, p]));
export const STREAMS: StreamCategory[] = STREAM_CATEGORIES;
export { MASTER_MUG_UP_TABLES } from './mugUpTables';
export { BOOK_SOURCES, type BookSource } from './bookCatalog';
