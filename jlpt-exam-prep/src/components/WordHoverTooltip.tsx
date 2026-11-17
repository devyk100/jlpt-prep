import React, { useState, useRef, useEffect, useId } from 'react';
import { createPortal } from 'react-dom';
import type { WordToken } from '../types';

export const WordHoverTooltip: React.FC<{ token: WordToken; furiganaMode: 'all' | 'hover' | 'off' }> = ({ token, furiganaMode }) => {
  const [open, setOpen] = useState(false);
  const [coords, setCoords] = useState({ top: 12, left: 12 });
  const trigger = useRef<HTMLButtonElement>(null);
  const popup = useRef<HTMLDivElement>(null);
  const timer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);
  const id = useId();
  const pinned = useRef(false);
  const position = () => {
    const rect = trigger.current?.getBoundingClientRect();
    if (!rect) return;
    const width = Math.min(280, window.innerWidth - 24);
    const height = popup.current?.offsetHeight || 170;
    const top = rect.bottom + height + 8 < window.innerHeight ? rect.bottom + 8 : Math.max(12, rect.top - height - 8);
    setCoords({ top, left: Math.max(12, Math.min(rect.left, window.innerWidth - width - 12)) });
  };
  const show = () => { clearTimeout(timer.current); position(); setOpen(true); };
  const hide = () => { timer.current = setTimeout(() => { if (!pinned.current) setOpen(false); }, 140); };
  useEffect(() => {
    if (!open) return;
    position();
    const close = () => { pinned.current = false; setOpen(false); };
    const scroll = (e: Event) => { if (!popup.current?.contains(e.target as Node)) close(); };
    const key = (e: KeyboardEvent) => { if (e.key === 'Escape') close(); };
    const outside = (e: PointerEvent) => { if (!trigger.current?.contains(e.target as Node) && !popup.current?.contains(e.target as Node)) close(); };
    window.addEventListener('resize', close); window.addEventListener('scroll', scroll, true);
    window.addEventListener('keydown', key); window.addEventListener('pointerdown', outside);
    return () => { window.removeEventListener('resize', close); window.removeEventListener('scroll', scroll, true); window.removeEventListener('keydown', key); window.removeEventListener('pointerdown', outside); };
  }, [open]);
  useEffect(() => () => clearTimeout(timer.current), []);
  const reading = furiganaMode !== 'off' && token.reading && token.reading !== token.word;
  return <>
    <button type="button" ref={trigger} aria-describedby={open ? id : undefined}
      onMouseEnter={show} onMouseLeave={hide} onFocus={show} onBlur={hide}
      onClick={() => { pinned.current = true; show(); }} className="inline border-b border-dotted border-[#9daa99] rounded-sm px-0.5 hover:bg-[#e7edde] focus-visible:outline-2 focus-visible:outline-[#467b6b]">
      <ruby>{token.word}{reading && furiganaMode === 'all' && <rt className="text-[10px]">{token.reading}</rt>}</ruby>
    </button>
    {open && createPortal(<div ref={popup} id={id} role="tooltip" onMouseEnter={show} onMouseLeave={hide}
      style={{ position: 'fixed', ...coords, width: 'min(280px, calc(100vw - 24px))', maxHeight: 'calc(100dvh - 24px)', overflowY: 'auto', zIndex: 1000 }}
      className="rounded-lg border border-[#bdcbb8] bg-[#fffef9] p-3 text-sm shadow-xl text-[#283b35]">
      <strong>{token.word}</strong>{reading && <span className="ml-2 text-xs">{token.reading}</span>}
      <p className="mt-1">{token.meaning}</p>{token.pos && <small>{token.pos}</small>}
      {token.nuance && <p className="mt-2 text-xs">{token.nuance}</p>}
    </div>, document.body)}
  </>;
};
