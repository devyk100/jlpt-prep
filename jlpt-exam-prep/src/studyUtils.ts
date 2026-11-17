import type { ExampleSentence, QuizQuestion, WordToken } from './types';
export function alignSentence(sentence: ExampleSentence): { text: string; token?: WordToken }[] {
  const parts: { text: string; token?: WordToken }[] = [];
  const tokens = [...sentence.tokens].filter(t => t.word).sort((a, b) => b.word.length - a.word.length);
  let cursor = 0;
  while (cursor < sentence.japanese.length) {
    const token = tokens.find(t => sentence.japanese.startsWith(t.word, cursor));
    if (token) { parts.push({ text: token.word, token }); cursor += token.word.length; }
    else { const last = parts.at(-1); if (last && !last.token) last.text += sentence.japanese[cursor]; else parts.push({ text: sentence.japanese[cursor] }); cursor++; }
  }
  return parts;
}
export function orderQuestion(question: QuizQuestion): QuizQuestion {
  let seed = [...question.id].reduce((n, c) => Math.imul(n ^ c.charCodeAt(0), 16777619) >>> 0, 2166136261);
  const indices = question.options.map((_, i) => i);
  for (let i = indices.length - 1; i > 0; i--) { seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; const j = seed % (i + 1); [indices[i], indices[j]] = [indices[j], indices[i]]; }
  return { ...question, options: indices.map(i => question.options[i]), explanations: indices.map(i => question.explanations[i]), correctIndex: indices.indexOf(question.correctIndex) };
}
