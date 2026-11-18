import { ReadingContext } from './readingContext';
import React, { useState, useEffect, useMemo } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import {
  ALL_GRAMMAR_POINTS,
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

function parseRoute(pathname: string, hash: string): {
  mode?: StudyMode;
  pointId?: string;
  practiceTarget?: { bookId: string; bookTitle: string; chapter: string };
  isExplicitRoute: boolean;
} {
  const path = (hash.startsWith('#/') ? hash.slice(1) : pathname).replace(/\/+$/, '') || '/';

  if (path === '/revision') {
    return { mode: 'revision', isExplicitRoute: true };
  }

  if (path.startsWith('/practice')) {
    const parts = path.split('/').filter(Boolean); // ['practice', bookId, chapter]
    if (parts.length >= 3) {
      const bookId = parts[1];
      const chapter = decodeURIComponent(parts.slice(2).join('/'));
      const bookTitle =
        bookId === 'genki-1'
          ? 'Genki I'
          : bookId === 'genki-2'
          ? 'Genki II'
          : bookId === 'skm-n3'
          ? 'Shin Kanzen Master N3'
          : 'Shin Kanzen Master N2';
      return {
        mode: 'practice',
        practiceTarget: { bookId, bookTitle, chapter },
        isExplicitRoute: true
      };
    }
    return { mode: 'practice', isExplicitRoute: true };
  }

  if (path.startsWith('/learn/')) {
    const pointId = path.slice('/learn/'.length);
    if (pointId && GRAMMAR_BY_ID[pointId]) {
      return { mode: 'learn', pointId, isExplicitRoute: true };
    }
  }

  return { isExplicitRoute: false };
}

export function App() {
  const location = useLocation();
  const navigate = useNavigate();

  // Initial Route Check
  const initialRoute = useMemo(() => {
    return parseRoute(location.pathname, location.hash);
  }, []);

  // Activity Mode: Learn | Practice | Revision
  const [studyMode, setStudyMode] = useState<StudyMode>(() => {
    if (initialRoute.isExplicitRoute && initialRoute.mode) {
      return initialRoute.mode;
    }
    return (localStorage.getItem(STORAGE_KEYS.STUDY_MODE) as StudyMode) || 'learn';
  });

  const [practiceTarget, setPracticeTarget] = useState<{
    bookId: string;
    bookTitle: string;
    chapter: string;
  }>(() => {
    if (initialRoute.practiceTarget) {
      return initialRoute.practiceTarget;
    }
    return {
      bookId: 'genki-1',
      bookTitle: 'Genki I',
      chapter: 'Lesson 1'
    };
  });

  // Navigation & Filter state
  const [selectedFilter, setSelectedFilter] = useState<'all' | 'N5' | 'N4' | 'N3' | 'N2'>(() => {
    return (localStorage.getItem(STORAGE_KEYS.FILTER) as 'all' | 'N5' | 'N4' | 'N3' | 'N2') || 'all';
  });

  const [searchQuery, setSearchQuery] = useState('');

  // Selected Point ID
  const [currentPointId, setCurrentPointId] = useState<string>(() => {
    if (initialRoute.pointId && GRAMMAR_BY_ID[initialRoute.pointId]) {
      return initialRoute.pointId;
    }
    const saved = localStorage.getItem(STORAGE_KEYS.CURRENT_POINT);
    if (saved && GRAMMAR_BY_ID[saved]) return saved;
    return ALL_GRAMMAR_POINTS[0].id;
  });

  // Active route derived dynamically from URL
  const currentRoute = useMemo(() => {
    return parseRoute(location.pathname, location.hash);
  }, [location.pathname, location.hash]);

  // Derived effective mode, target, and point ID (always 100% synchronous with URL)
  const effectiveStudyMode: StudyMode = currentRoute.isExplicitRoute && currentRoute.mode
    ? currentRoute.mode
    : studyMode;

  const effectivePracticeTarget = currentRoute.isExplicitRoute && currentRoute.practiceTarget
    ? currentRoute.practiceTarget
    : practiceTarget;

  const effectivePointId = currentRoute.isExplicitRoute && currentRoute.mode === 'learn' && currentRoute.pointId && GRAMMAR_BY_ID[currentRoute.pointId]
    ? currentRoute.pointId
    : currentPointId;

  const currentPoint = useMemo(() => {
    return GRAMMAR_BY_ID[effectivePointId] || ALL_GRAMMAR_POINTS[0];
  }, [effectivePointId]);

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

  // Sync state when location changes (browser Back / Forward navigation)
  useEffect(() => {
    const route = parseRoute(location.pathname, location.hash);
    if (route.isExplicitRoute) {
      if (route.mode) {
        setStudyMode(route.mode);
      }
      if (route.mode === 'learn' && route.pointId && GRAMMAR_BY_ID[route.pointId]) {
        setCurrentPointId(route.pointId);
      }
      if (route.mode === 'practice' && route.practiceTarget) {
        setPracticeTarget(route.practiceTarget);
      }
    } else {
      // Reverted back to root '/'
      setStudyMode('learn');
      const saved = localStorage.getItem(STORAGE_KEYS.CURRENT_POINT);
      if (saved && GRAMMAR_BY_ID[saved]) {
        setCurrentPointId(saved);
      }
    }
  }, [location.pathname, location.hash]);

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
    setStudyMode('learn');
    if (location.pathname !== `/learn/${pointId}`) {
      navigate(`/learn/${pointId}`);
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
    navigate(`/practice/${bookId}/${encodeURIComponent(chapter)}`);
  };

  // Navigate to Lesson from practice or revision
  const handleNavigateToLesson = (lessonId: string) => {
    handleSelectPoint(lessonId);
  };

  // Handle Mode Change from Topbar
  const handleModeChange = (newMode: StudyMode) => {
    setStudyMode(newMode);
    if (newMode === 'learn') {
      navigate(`/learn/${currentPointId}`);
    } else if (newMode === 'practice') {
      navigate(`/practice/${practiceTarget.bookId}/${encodeURIComponent(practiceTarget.chapter)}`);
    } else if (newMode === 'revision') {
      navigate('/revision');
    }
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

  // Filter practice exercises for target (exact bookId and exact chapter match; NO fallback to unrelated exercises)
  const currentChapterExercises = useMemo(() => {
    const targetBook = effectivePracticeTarget.bookId;
    const targetChapter = effectivePracticeTarget.chapter.trim().toLowerCase();
    return chapterExercises.filter(
      ex => ex.bookId === targetBook && ex.chapter.trim().toLowerCase() === targetChapter
    );
  }, [effectivePracticeTarget]);

  // Aggregate available practice chapters
  const availablePracticeChapters = useMemo(() => {
    const map = new Map<string, { bookId: string; bookTitle: string; chapter: string; count: number }>();
    chapterExercises.forEach(ex => {
      const key = `${ex.bookId}::${ex.chapter}`;
      const existing = map.get(key);
      if (existing) {
        existing.count += 1;
      } else {
        const bookTitle =
          ex.bookId === 'genki-1'
            ? 'Genki I'
            : ex.bookId === 'genki-2'
            ? 'Genki II'
            : ex.bookId === 'skm-n3'
            ? 'Shin Kanzen Master N3'
            : 'Shin Kanzen Master N2';
        map.set(key, { bookId: ex.bookId, bookTitle, chapter: ex.chapter, count: 1 });
      }
    });
    return Array.from(map.values());
  }, []);

  return (
    <ReadingContext.Provider value={{ mode: furiganaMode, level: currentPoint.level }}>
      <div className="min-h-screen bg-[#f6f5ef] text-[#24332c] flex flex-col font-sans">
        {/* Clean Topbar Header */}
        <Topbar
          activeMode={effectiveStudyMode}
          onModeChange={handleModeChange}
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
            currentPointId={effectivePointId}
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
          {effectiveStudyMode === 'learn' && (
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

          {effectiveStudyMode === 'practice' && (
            <ChapterPracticeView
              exercises={currentChapterExercises}
              bookTitle={effectivePracticeTarget.bookTitle}
              chapterTitle={effectivePracticeTarget.chapter}
              availableChapters={availablePracticeChapters}
              onSelectChapter={(bookId, chapter) => {
                const bookTitle =
                  bookId === 'genki-1'
                    ? 'Genki I'
                    : bookId === 'genki-2'
                    ? 'Genki II'
                    : bookId === 'skm-n3'
                    ? 'Shin Kanzen Master N3'
                    : 'Shin Kanzen Master N2';
                setPracticeTarget({ bookId, bookTitle, chapter });
                navigate(`/practice/${bookId}/${encodeURIComponent(chapter)}`);
              }}
              onNavigateToLesson={handleNavigateToLesson}
              onExitPractice={() => {
                setStudyMode('learn');
                navigate(`/learn/${effectivePointId}`);
              }}
            />
          )}

          {effectiveStudyMode === 'revision' && (
            <RevisionDeskView
              onNavigateToLesson={handleNavigateToLesson}
              onExitRevision={() => {
                setStudyMode('learn');
                navigate(`/learn/${currentPointId}`);
              }}
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
