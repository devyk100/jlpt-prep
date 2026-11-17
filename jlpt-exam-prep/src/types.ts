export type JLPTLevel = 'N5' | 'N4' | 'N3' | 'N2';

export interface WordToken {
  word: string;
  reading?: string; // Hiragana / Katakana
  romaji?: string;
  meaning: string;
  pos?: string; // Part of speech (e.g., Verb, Noun, Particle, Adjective)
  nuance?: string; // Optional word-level nuance or JLPT tip
}

export interface ExampleSentence {
  id: string;
  tokens: WordToken[];
  japanese: string;
  english: string;
  literal?: string;
  nuanceNote?: string; // Why this sentence uses this grammar, subtle tone
  trapAlert?: string; // What would make this sentence ungrammatical
}

export interface MugUpTable {
  title: string;
  subtitle?: string;
  columns: string[];
  rows: {
    label: string;
    cells: string[];
    note?: string;
  }[];
}

export interface QuizOptionExplanation {
  text: string;
  isCorrect: boolean;
  reason: string; // Exhaustive reason why it's right or why it's wrong
  trapDetail?: string; // e.g. "Violates volition rule", "Wrong conjugation stem"
}

export interface QuizQuestion {
  id: string;
  question: string; // Sentence with （　　）
  translation: string;
  options: string[];
  correctIndex: number;
  explanations: QuizOptionExplanation[];
  grammarFocus: string;
  ruleHint: string;
}

export interface GrammarPoint {
  id: string;
  title: string; // e.g. "〜最中に (さいちゅうに)"
  meaning: string; // e.g. "In the middle of doing (interrupted!)"
  level: JLPTLevel;
  book?: string; // e.g. "Genki I", "Genki II", "Shin Kanzen Master N3", "Shin Kanzen Master N2"
  sourceReference?: string;
  chapter?: string; // e.g. "Lesson 6 (Te-form)", "Chapter 1: とき (Time)"
  streamId: string;
  streamName: string;
  connection: string; // 接続: V-ている + 最中に / N + の最中に
  nuance: string; // Deep explanation of nuances and contexts
  keyTakeaway: string; // "Mug-Up" golden rule
  comparisonNote?: string; // Contrasted with another point (e.g. 最中 vs うちに)
  table?: MugUpTable;
  sentences: ExampleSentence[];
  quiz: QuizQuestion[];
  nextPointId?: string; // For seamless flow
  prevPointId?: string;
  tags: string[];
}

export interface StreamCategory {
  id: string;
  title: string;
  japaneseTitle: string;
  description: string;
  iconName: string;
  grammarIds: string[];
}

export interface UserProgress {
  studiedPoints: Record<string, boolean>; // pointId -> boolean
  quizResults: Record<string, { answered: boolean; correct: boolean; chosenIndex: number }>;
  flaggedMistakes: string[]; // questionIds
  furiganaMode: 'all' | 'hover' | 'off';
  seamlessFlowMode: boolean; // if true, hides rigid level badges to keep flow state
}
