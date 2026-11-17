from pathlib import Path
p=Path('src/data/grammarData.ts');s=p.read_text();s=s.replace("export const ALL_GRAMMAR_POINTS", "import { BOOK_GENKI1_POINTS } from './bookGenki1';\nimport { BOOK_GENKI2_POINTS } from './bookGenki2';\nimport { BOOK_SKM_N3_POINTS } from './bookSkmN3';\nimport { BOOK_SKM_N2_POINTS } from './bookSkmN2';\nimport { EXPANDED_POINTS } from './expandedPoints';\n\nexport const ALL_GRAMMAR_POINTS");s=s.replace('  ...STREAM_GENKI_POINTS,','  ...BOOK_GENKI1_POINTS,\n  ...BOOK_GENKI2_POINTS,\n  ...BOOK_SKM_N3_POINTS,\n  ...BOOK_SKM_N2_POINTS,\n  ...EXPANDED_POINTS,\n  ...STREAM_GENKI_POINTS,');s=s.replace("export { BOOK_SOURCES, type BookSource } from './bookCatalog';", "export { BOOK_SOURCES, type BookSource } from './bookCatalog';")
p.write_text(s)
p=Path('src/data/expandedPoints.ts');p.write_text("import type { GrammarPoint } from '../types';\nexport const EXPANDED_POINTS: GrammarPoint[] = [];\n")
for p in Path('src/components').glob('*.tsx'):
 s=p.read_text();s=s.replace(".title.split(' ')[0]", ".title.split(' (')[0]");p.write_text(s)
p=Path('src/App.tsx');s=p.read_text();anchor='  // Sync to localStorage';s=s.replace(anchor,"""  useEffect(() => {
    const shortcut = (event: KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
        event.preventDefault(); setIsSearchOpen(open => !open);
      }
    };
    window.addEventListener('keydown', shortcut);
    return () => window.removeEventListener('keydown', shortcut);
  }, []);

"""+anchor);s=s.replace('<DeskPane\n','<DeskPane\n          key={currentPoint.id}\n');p.write_text(s)
p=Path('src/components/SearchModal.tsx');s=p.read_text();s=s.replace("      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {\n        e.preventDefault();\n        onClose();\n      }\n",'');p.write_text(s)
p=Path('src/components/SentenceCard.tsx');s=p.read_text();s=s.replace("import type { ExampleSentence }", "import { alignSentence } from '../studyUtils';\nimport type { ExampleSentence }");s=s.replace('{sentence.tokens.map((token, idx) => (','{alignSentence(sentence).map((part, idx) => part.token ? (').replace('token={token}','token={part.token}').replace('          ))}', '          ) : <span key={`${sentence.id}-text-${idx}`}>{part.text}</span>)}',1);s=s.replace('flex-1 flex flex-wrap items-baseline gap-y-1.5 leading-loose','flex-1 leading-loose');p.write_text(s)
p=Path('src/components/QuizCard.tsx');s=p.read_text();s=s.replace("import React, { useState }", "import React, { useState, useMemo }");s=s.replace("import type { QuizQuestion }", "import { orderQuestion } from '../studyUtils';\nimport type { QuizQuestion }");s=s.replace('  question,\n  onAnswerSaved','  question: originalQuestion,\n  onAnswerSaved');s=s.replace('  const [selectedIndex', '  const question = useMemo(() => orderQuestion(originalQuestion), [originalQuestion]);\n  const [selectedIndex',1);p.write_text(s)
p=Path('vite.config.ts');s=p.read_text().replace('  plugins:', "  server: { host: '127.0.0.1', port: 5174, strictPort: true },\n  plugins:");p.write_text(s)
Path('start-platform.bat').write_text('@echo off\ncd /d "%~dp0"\necho Starting Bunpou Atlas at http://127.0.0.1:5174\nnpm.cmd run dev -- --open\npause\n')
