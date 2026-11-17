import React, { useState, useEffect, useRef } from 'react';
import { createRoot } from 'react-dom/client';
import entries from './kanji.json';
import './style.css';

const levels = ['N5','N4','N3','N2'];
const loadNotes = () => { try { const data=JSON.parse(localStorage.getItem('kanji-atlas-notes') || '{}'); return data && typeof data==='object' && !Array.isArray(data) ? Object.fromEntries(Object.entries(data).filter(([,v])=>typeof v==='string')) : {}; } catch { return {}; } };
function App() {
  const [active, setActive] = useState(null);
  const [pinned, setPinned] = useState(false);
  const [position, setPosition] = useState({top:100,left:100});
  const [query, setQuery] = useState('');
  const [size, setSize] = useState('comfortable');
  const [notes, setNotes] = useState(loadNotes);
  const [saveError, setSaveError] = useState(false);
  const [sources, setSources] = useState(false);
  const timer = useRef();
  const card = useRef();
  const lastTile = useRef();
  const restoringFocus = useRef(false);
  const close = () => {clearTimeout(timer.current); setActive(null); setPinned(false);};
  useEffect(() => {
    function key(e) { if(e.key === 'Escape') {close(); restoringFocus.current=true; lastTile.current?.focus({preventScroll:true}); restoringFocus.current=false;} }
    function outside(e) { if(!e.target.closest('.detail') && !e.target.closest('.tile')) close(); }
    document.addEventListener('keydown', key);
    document.addEventListener('pointerdown', outside);
    return () => {document.removeEventListener('keydown',key); document.removeEventListener('pointerdown',outside);};
  }, []);
  useEffect(() => {
    const adjust = () => { if(active && lastTile.current) place(lastTile.current); };
    window.addEventListener('resize',adjust); window.addEventListener('scroll',adjust,{passive:true});
    return () => {window.removeEventListener('resize',adjust);window.removeEventListener('scroll',adjust);};
  }, [active]);
  function place(tile) {
    const rect = tile.getBoundingClientRect();
    const width = Math.min(370,window.innerWidth-24);
    const height = Math.min(570,window.innerHeight-24);
    let left = rect.right + 12;
    if(left+width > window.innerWidth-12) left = rect.left-width-12;
    left = Math.max(12,Math.min(left,window.innerWidth-width-12));
    setPosition({left,top:Math.max(12,Math.min(rect.top-24,window.innerHeight-height-12))});
  }
  function show(k, tile, pin=false) {
    if(restoringFocus.current) return;
    clearTimeout(timer.current);
    if(pinned && !pin) return;
    lastTile.current=tile; place(tile); setActive(k); setPinned(pin);
    if(active?.character !== k.character && card.current) card.current.scrollTop=0;
  }
  function leave() { if(!pinned) timer.current=setTimeout(() => setActive(null),180); }
  function save(value) {
    const next = {...notes,[active.character]:value}; setNotes(next);
    try {localStorage.setItem('kanji-atlas-notes',JSON.stringify(next));setSaveError(false);} catch {setSaveError(true);}
  }
  const q = query.trim().toLowerCase();
  const filtered = entries.filter(k => !q || [k.character,...k.meanings,...k.onyomi,...k.kunyomi,...k.words.flatMap(w=>[w.word,w.reading,...w.meanings])].join(' ').toLowerCase().includes(q));
  function exportNotes() {
    const url=URL.createObjectURL(new Blob([JSON.stringify(notes,null,2)],{type:'application/json'}));
    const a=document.createElement('a'); a.href=url;a.download='kanji-atlas-notes.json';a.click();URL.revokeObjectURL(url);
  }
  return <>
    <header className="topbar">
      <a className="brand" href="#top"><span className="brand-mark" lang="ja">字</span><span>Kanji atlas<small>N5 → N2 / RECALL FIRST</small></span></a>
      <nav aria-label="Jump to level">{levels.map(l=><a key={l} href={'#'+l}>{l}</a>)}</nav>
      <div className="tools"><label className="search"><span aria-hidden="true">⌕</span><input aria-label="Search kanji, meaning or vocabulary" placeholder="Find a kanji…" value={query} onChange={e=>{setQuery(e.target.value);close();}}/>{query&&<button aria-label="Clear search" onClick={()=>setQuery('')}>×</button>}</label><button className="size-button" onClick={()=>setSize(size==='compact'?'comfortable':'compact')} aria-pressed={size==='compact'} title="Toggle compact grid">{size==='compact'?'Larger grid':'Compact grid'}</button></div>
    </header>
    <main id="top" className={size}>
      <div className="intro"><p>Look. Recall. <span>Hover to check.</span></p><span>{filtered.length.toLocaleString()} characters · Click to pin & write notes</span></div>
      {levels.map((level,index)=>{const group=filtered.filter(k=>k.level===level);return <section id={level} key={level} className={'level level-'+level} aria-labelledby={'heading-'+level}>
        <div className="section-heading"><h1 id={'heading-'+level}>{level}</h1><span className="count">{group.length} characters</span><span className="section-line"/><span className="section-index">0{index+1}</span></div>
        <div className="grid">{group.map(k=><button key={k.character} lang="ja" className={'tile '+(active?.character===k.character?'active':'')} aria-label={k.character} aria-haspopup="dialog" aria-expanded={active?.character===k.character} onMouseEnter={e=>show(k,e.currentTarget)} onMouseLeave={leave} onFocus={e=>show(k,e.currentTarget)} onBlur={leave} onClick={e=>show(k,e.currentTarget,true)}>{k.character}</button>)}</div>
        {group.length===0 && <p className="empty">No matching kanji in {level}.</p>}
      </section>})}
      <footer><span>Levels are approximate study groupings.</span><button onClick={()=>setSources(!sources)} aria-expanded={sources}>Sources & coverage {sources?'−':'+'}</button><button onClick={exportNotes}>Export my notes ↓</button></footer>
      {sources && <aside className="sources"><h2>Checked against your books</h2><p>1,111 kanji plus the repetition mark 々. Includes all 316 kanji + 々 in the Genki third-edition publisher list, all 654 cumulative kanji in SKM N3, and all 1,046 in SKM N2’s numbered study list. The book check added 73 missing kanji. Each matched card includes its book/lesson or page reference.</p><p>The four sections are approximate study placements, not official exam boundaries. Existing community labels are retained; added characters use Genki/SKM coverage to determine a study section. Genki I and II do not map exactly to N5 and N4. The original 65 characters outside SKM N2’s particular list are also retained.</p><p>This verifies kanji-list coverage, not every vocabulary definition or every word in the books. Vocabulary uses entries labelled N5–N2 in the dictionary source, including alternate spellings; some characters have fewer than four matches or none. Easier entries appear first. A word’s level can differ from its characters’ levels, and a level tag does not verify the frequency of every spelling variant.</p><p>Dictionary data adapted from <a href="https://github.com/evanclan/OpenJLPT" target="_blank" rel="noreferrer">OpenJLPT</a>, using <a href="https://www.edrdg.org/" target="_blank" rel="noreferrer">JMdict & KANJIDIC2 (EDRDG)</a> and <a href="https://www.tanos.co.uk/jlpt/" target="_blank" rel="noreferrer">Jonathan Waller’s lists</a>. Dictionary-derived data is <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noreferrer">CC BY-SA 4.0</a>. Textbook references identify your local books; their original text and scans are not part of the app. Full audit details are in BOOK-AUDIT.md. Notes stay in this browser; export them for a backup.</p></aside>}
    </main>
    {active && <aside className={'detail '+(pinned?'pinned':'')} style={position} role="dialog" aria-label={active.character+' study card'} onMouseEnter={()=>clearTimeout(timer.current)} onMouseLeave={leave} onFocus={()=>clearTimeout(timer.current)}>
      <div className="card-toolbar"><span className={'badge '+active.level}>{active.level}</span><span>{pinned?'PINNED · YOUR STUDY NOTE':'HOVER PREVIEW'}</span><button aria-label={pinned?'Unpin card':'Pin card'} onClick={()=>setPinned(!pinned)}>{pinned?'Unpin':'Pin'}</button><button aria-label="Close card" onClick={close}>×</button></div>
      <div className="card-scroll" ref={card} key={active.character}>
        <div className="kanji-definition"><span lang="ja" className="hero-kanji">{active.character}</span><div><h2>{active.meanings.join('; ')}</h2><span>{active.strokes} strokes</span></div></div>
        <div className="readings"><span>ON</span><p lang="ja">{active.onyomi.join('・')||'—'}</p><span>KUN</span><p lang="ja">{active.kunyomi.join('・')||'—'}</p></div>
        <div className="vocab-heading"><h3>Words to recall</h3><span>{active.words.length} · N5–N2</span></div>
        {active.words.length<4 && <p className="coverage">{active.words.length?`Only ${active.words.length} matching ${active.words.length===1?'entry':'entries'} in this source’s N5–N2 list.`:'No matching vocabulary in this source’s N5–N2 list.'}</p>}
        <div className="words">{active.words.map(w=><div className="word" key={w.id}><div><span className="word-form" lang="ja">{w.word}</span><span className="word-reading" lang="ja">{w.reading}</span><span className="word-level">{w.level}</span></div><p>{w.meanings.join('; ')}</p></div>)}</div>
        <details className="book-references"><summary>Book coverage & level basis</summary><p>{active.levelBasis}</p>{active.bookReferences.length ? <ul>{active.bookReferences.map(r=><li key={r}>{r}</li>)}</ul> : <p>Not in the checked textbook kanji lists; retained from the community list.</p>}</details>
        <label className="note-label">My distinction / short note<textarea placeholder="A mnemonic, a similar kanji, a distinction…" value={notes[active.character]||''} onFocus={()=>setPinned(true)} onChange={e=>save(e.target.value)} /></label><p className="save-status">{saveError?'Could not save in this browser. Export your notes to keep them.':'Saved locally in this browser.'}</p>
      </div>
      <div className="card-bottom">{pinned?'Click another kanji to switch · Esc to close':'Scroll for more · Click a kanji to pin'}</div>
    </aside>}
  </>;
}
createRoot(document.getElementById('root')).render(<App/>);
