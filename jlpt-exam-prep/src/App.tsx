import { ReadingContext } from './readingContext';
import React, { useState, useEffect, useMemo } from 'react';
import {
  ALL_GRAMMAR_POINTS,
  STREAMS,
  GRAMMAR_BY_ID
} from './data/grammarData';
import { Topbar, type StudyMode } from './components/Topbar';
import { SidebarPane } from './components/SidebarPane';
import { DeskPane } from './components/DeskPane';
import { ChapterPracticeView, type ChapterExerciseItem } from './components/ChapterPracticeView';
import { RevisionDeskView } from './components/RevisionDeskView';
import { SearchModal } from './components/SearchModal';
import { MugUpTableModal } from './components/MugUpTableModal';
import { MistakeBankModal } from './components/MistakeBankModal';
import { BookCatalogModal } from './components/BookCatalogModal';
import chapterExercisesRaw from './data/chapterExercises.json';
import type { QuizQuestion, JLPTLevel } from './types';

const chapterExercises = chapterExercisesRaw as ChapterExerciseItem[];

const STORAGE_KEYS = {
  CURRENT_POINT: 'bunpou_current_point_id',
  STUDIED_POINTS: 'bunpou_studied_points',
  FLAGGED_MISTAKES: 'bunpou_flagged_mistakes',
  FURIGANA_MODE: 'bunpou_reading_mode_v2',
  SEAMLESS_FLOW: 'bunpou_seamless_flow',
  FILTER: 'bunpou_selected_filter',
  STUDY_MODE: 'bunpou_study_mode'
};

export function App() {
  // Activity Mode: Learn | Practice | Revision
  const [studyMode, setStudyMode] = useState<StudyMode>(() => {
    return (localStorage.getItem(STORAGE_KEYS.STUDY_MODE) as StudyMode) || 'learn';
  });

  const [practiceTarget, setPracticeTarget] = useState<{
    bookId: string;
    bookTitle: string;
    chapter: string;
  }>({
    bookId: 'genki-1',
    bookTitle: 'Genki I',
    chapter: 'Lesson 1'
  });

  // Navigation & Filter state
  const [selectedFilter, setSelectedFilter] = useState<'all' | 'N5' | 'N4' | 'N3' | 'N2'>(() => {
    return (localStorage.getItem(STORAGE_KEYS.FILTER) as 'all' | 'N5' | 'N4' | 'N3' | 'N2') || 'all';
  });

  const [searchQuery, setSearchQuery] = useState('');

  // Selected Point ID
  const [currentPointId, setCurrentPointId] = useState<string>(() => {
    const saved = localStorage.getItem(STORAGE_KEYS.CURRENT_POINT);
    if (saved && GRAMMAR_BY_ID[saved]) return saved;
    return ALL_GRAMMAR_POINTS[0].id;
  });

  const currentPoint = useMemo(() => {
    return GRAMMAR_BY_ID[currentPointId] || ALL_GRAMMAR_POINTS[0];
  }, [currentPointId]);

  // Studied Points state
  const [studiedPoints, setStudiedPoints] = useState<Record<string, boolean>>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEYS.STUDIED_POINTS);
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  // Flagged mistakes for Weak Points Bank
  const [flaggedMistakes, setFlaggedMistakes] = useState<string[]>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEYS.FLAGGED_MISTAKES);
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  // User Preferences
  const [furiganaMode, setFuriganaMode] = useState<'book' | 'all' | 'hover' | 'off'>(() => {
    return (localStorage.getItem(STORAGE_KEYS.FURIGANA_MODE) as 'book' | 'all' | 'hover' | 'off') || 'book';
  });

  const [seamlessFlowMode, setSeamlessFlowMode] = useState<boolean>(() => {
    const saved = localStorage.getItem(STORAGE_KEYS.SEAMLESS_FLOW);
    return saved !== null ? saved === 'true' : true;
  });

  // Modals state
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [isTablesOpen, setIsTablesOpen] = useState(false);
  const [isMistakesOpen, setIsMistakesOpen] = useState(false);
  const [isBooksOpen, setIsBooksOpen] = useState(false);

  useEffect(() => {
    const shortcut = (event: KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
        event.preventDefault();
        setIsSearchOpen(open => !open);
      }
    };
    window.addEventListener('keydown', shortcut);
    return () => window.removeEventListener('keydown', shortcut);
  }, []);

  // Sync to localStorage
  useEffect(() => {
    localStorage.setItem(STORAGE_KEYS.CURRENT_POINT, currentPointId);
  }, [currentPointId]);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEYS.STUDY_MODE, studyMode);
  }, [studyMode]);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEYS.FLAGGED_MISTAKES, JSON.stringify(flaggedMistakes));
  }, [flaggedMistakes]);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEYS.FURIGANA_MODE, furiganaMode);
  }, [furiganaMode]);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEYS.SEAMLESS_FLOW, String(seamlessFlowMode));
  }, [seamlessFlowMode]);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEYS.FILTER, selectedFilter);
  }, [selectedFilter]);

  // Handle selecting point
  const handleSelectPoint = (pointId: string) => {
    setCurrentPointId(pointId);
    if (studyMode !== 'learn') {
      setStudyMode('learn');
    }
  };

  // Start Chapter Practice
  const handleStartChapterPractice = (book: string, chapter: string) => {
    const bookId = book.toLowerCase().includes('genki i') && !book.toLowerCase().includes('genki ii')
      ? 'genki-1'
      : book.toLowerCase().includes('genki ii')
      ? 'genki-2'
      : book.toLowerCase().includes('n3')
      ? 'skm-n3'
      : 'skm-n2';

    setPracticeTarget({ bookId, bookTitle: book, chapter });
    setStudyMode('practice');
  };

  // Navigate to Lesson from practice or revision
  const handleNavigateToLesson = (lessonId: string) => {
    handleSelectPoint(lessonId);
    setStudyMode('learn');
  };

  // Explicit completion toggling (ONLY when user explicitly marks it)
  const handleToggleCompleted = (pointId: string) => {
    setStudiedPoints(prev => {
      const updated = { ...prev };
      if (updated[pointId]) {
        delete updated[pointId];
      } else {
        updated[pointId] = true;
      }
      localStorage.setItem(STORAGE_KEYS.STUDIED_POINTS, JSON.stringify(updated));
      return updated;
    });
  };

  const handleResetStudied = () => {
    if (window.confirm('Reset all marked completed points back to uncompleted?')) {
      setStudiedPoints({});
      localStorage.removeItem(STORAGE_KEYS.STUDIED_POINTS);
    }
  };

  // Handle Quiz Results
  const handleAnswerSaved = (questionId: string, isCorrect: boolean, _chosenIndex: number) => {
    if (!isCorrect) {
      setFlaggedMistakes(prev => (prev.includes(questionId) ? prev : [...prev, questionId]));
    }
  };

  const handleToggleFlag = (questionId: string) => {
    setFlaggedMistakes(prev =>
      prev.includes(questionId) ? prev.filter(id => id !== questionId) : [...prev, questionId]
    );
  };

  const handleClearAllMistakes = () => {
    setFlaggedMistakes([]);
  };

  // All quiz questions aggregate for mistake bank
  const allQuestions = useMemo(() => {
    const list: QuizQuestion[] = [];
    ALL_GRAMMAR_POINTS.forEach(pt => {
      if (pt.quiz) list.push(...pt.quiz);
    });
    return list;
  }, []);

  // Filter practice exercises for target
  const currentChapterExercises = useMemo(() => {
    const matched = chapterExercises.filter(
      ex => ex.bookId === practiceTarget.bookId && ex.chapter.toLowerCase().includes(practiceTarget.chapter.toLowerCase())
    );
    return matched.length > 0 ? matched : chapterExercises;
  }, [practiceTarget]);

  return (
    <ReadingContext.Provider value={{ mode: furiganaMode, level: currentPoint.level }}>
      <div className="min-h-screen bg-[#f6f5ef] text-[#24332c] flex flex-col font-sans">
        {/* Clean Topbar Header */}
        <Topbar
          activeMode={studyMode}
          onModeChange={setStudyMode}
          selectedFilter={selectedFilter}
          onFilterChange={setSelectedFilter}
          seamlessFlowMode={seamlessFlowMode}
          onToggleSeamlessFlow={() => setSeamlessFlowMode(prev => !prev)}
          furiganaMode={furiganaMode}
          onChangeFuriganaMode={setFuriganaMode}
          onOpenSearch={() => setIsSearchOpen(true)}
          onOpenMistakeBank={() => setIsMistakesOpen(true)}
          onOpenTablesModal={() => setIsTablesOpen(true)}
          onOpenBookCatalog={() => setIsBooksOpen(true)}
          mistakeCount={flaggedMistakes.length}
        />

        {/* Two-Pane Layout Container */}
        <div className="flex-1 flex flex-col md:flex-row w-full max-w-[1700px] mx-auto overflow-hidden">
          {/* Left Pane: Index, Filters & Search */}
          <SidebarPane
            points={ALL_GRAMMAR_POINTS}
            currentPointId={currentPointId}
            onSelectPoint={handleSelectPoint}
            studiedPoints={studiedPoints}
            onToggleCompleted={handleToggleCompleted}
            onResetStudied={handleResetStudied}
            searchQuery={searchQuery}
            onSearchChange={setSearchQuery}
            selectedFilter={selectedFilter}
            onFilterChange={setSelectedFilter}
            seamlessFlowMode={seamlessFlowMode}
          />

          {/* Right Pane: Active Mode View */}
          {studyMode === 'learn' && (
            <DeskPane
              key={currentPoint.id}
              point={currentPoint}
              allPoints={ALL_GRAMMAR_POINTS}
              onSelectPoint={handleSelectPoint}
              isCompleted={!!studiedPoints[currentPoint.id]}
              onToggleCompleted={handleToggleCompleted}
              furiganaMode={furiganaMode}
              seamlessFlowMode={seamlessFlowMode}
              onAnswerSaved={handleAnswerSaved}
              flaggedMistakes={flaggedMistakes}
              onToggleFlag={handleToggleFlag}
              onStartChapterPractice={handleStartChapterPractice}
            />
          )}

          {studyMode === 'practice' && (
            <ChapterPracticeView
              exercises={currentChapterExercises}
              bookTitle={practiceTarget.bookTitle}
              chapterTitle={practiceTarget.chapter}
              onNavigateToLesson={handleNavigateToLesson}
              onExitPractice={() => setStudyMode('learn')}
            />
          )}

          {studyMode === 'revision' && (
            <RevisionDeskView
              onNavigateToLesson={handleNavigateToLesson}
              onExitRevision={() => setStudyMode('learn')}
            />
          )}
        </div>

        {/* Modals */}
        <SearchModal
          isOpen={isSearchOpen}
          onClose={() => setIsSearchOpen(false)}
          allPoints={ALL_GRAMMAR_POINTS}
          onSelectPoint={handleSelectPoint}
          seamlessFlowMode={seamlessFlowMode}
        />

        <MugUpTableModal
          isOpen={isTablesOpen}
          onClose={() => setIsTablesOpen(false)}
        />

        <MistakeBankModal
          isOpen={isMistakesOpen}
          onClose={() => setIsMistakesOpen(false)}
          questions={allQuestions}
          flaggedIds={flaggedMistakes}
          onToggleFlag={handleToggleFlag}
          onAnswerSaved={handleAnswerSaved}
          onClearAll={handleClearAllMistakes}
        />

        <BookCatalogModal
          isOpen={isBooksOpen}
          onClose={() => setIsBooksOpen(false)}
          onSelectPoint={handleSelectPoint}
        />
      </div>
    </ReadingContext.Provider>
  );
}

export default App;
