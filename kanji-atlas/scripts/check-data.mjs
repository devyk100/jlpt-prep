import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const read = p => JSON.parse(readFileSync(new URL('../'+p,import.meta.url),'utf8'));
const entries=read('src/kanji.json');
const levels=['N5','N4','N3','N2'];
const vocab=new Map(levels.flatMap(l=>read(`data/vocab-${l.toLowerCase()}.json`)).map(w=>[w.id,w]));
const fixes=read('data/corrections.json');
assert.equal(new Set(entries.map(k=>k.character)).size,entries.length);
for(const level of levels) {
  const original=read(`data/kanji-${level.toLowerCase()}.json`);
  const originalChars=new Set(original.map(k=>k.character));
  assert.deepEqual(entries.filter(k=>k.level===level && originalChars.has(k.character)).map(k=>k.character),original.map(k=>k.character));
}
for(const k of entries) {
  assert.ok(k.meanings.length && k.meanings.every(Boolean));
  assert.equal(new Set(k.words.map(w=>w.id)).size,k.words.length);
  for(const w of k.words) {
    const source={...vocab.get(w.id),...fixes[w.id]};
    assert.ok(w.word.includes(k.character));
    assert.ok(levels.includes(w.level));
    assert.ok(w.reading && w.meanings.length && w.meanings.every(Boolean));
    assert.equal(w.level,source.level);
    assert.equal(w.reading,source.reading);
    assert.ok([source.word,...(source.other_forms||[])].includes(w.word));
  }
}
assert.equal(entries.find(k=>k.character==='伺').words[0].word,'伺う');
assert.equal(entries.find(k=>k.character==='日').words.find(w=>w.id==='50b6055d9b').word,'日にち');
const allChars=new Set(entries.map(k=>k.character));
for(const file of ['skm2-kanji-pages.json','skm3-lesson-pages.json','skm3-prerequisite-pages.json']) {
  for(const c of Object.values(read('data/book-audit/'+file)).join('').replace(/\s/g,'')) assert.ok(allChars.has(c),`Missing textbook kanji: ${c}`);
}
for(const c of Object.keys(read('data/book-audit/genki-kanji.json'))) assert.ok(allChars.has(c),`Missing Genki character: ${c}`);
assert.equal(entries.length,1112);
assert.ok(entries.find(k=>k.character==='授').bookReferences.some(r=>r.includes('Genki II')));
console.log(`PASS: ${entries.length} unique entries; complete audited Genki/SKM coverage; all vocabulary matched to N5–N2 source entries, with readings and meanings.`);
