import React from 'react';
import data from '../data/annotations.json';
import { WordHoverTooltip } from './WordHoverTooltip';
import { useReadingMode } from '../readingContext';
import type { JLPTLevel, WordToken } from '../types';
const annotations = data as Record<string, WordToken[]>;
export function AnnotatedText({ text, level, passive = false }: { text: string; level?: JLPTLevel; passive?: boolean }) {
  const mode = useReadingMode(level);
  return <span data-source-text={text}>{text.split(/([一-龯々〆ヵヶぁ-んァ-ヶー]+)/u).map((span, i) => {
    const tokens = annotations[span];
    if (!tokens) return <React.Fragment key={i}>{span}</React.Fragment>;
    return <React.Fragment key={i}>{tokens.map((token, j) => token.meaning ? <WordHoverTooltip key={j} token={token} furiganaMode={mode} passive={passive} /> : <span key={j}>{token.word}</span>)}</React.Fragment>;
  })}</span>;
}
