import sources from './bookSources.json';
export interface BookSource {
  id: string;
  name: string;
  level: 'N5' | 'N4' | 'N3' | 'N2';
  description: string;
  sections: { name: string; grammarIds: string[] }[];
}
export const BOOK_SOURCES = sources as BookSource[];
