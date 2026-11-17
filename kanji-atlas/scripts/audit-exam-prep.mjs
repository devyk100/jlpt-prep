import fs from 'node:fs';
import {build} from 'esbuild';
const root='C:/JLPT/jlpt-exam-prep';
const result=await build({stdin:{contents:`export * from '${root}/src/data/grammarData.ts'; export * from '${root}/src/data/bookGenki1.ts'; export * from '${root}/src/data/bookGenki2.ts'; export * from '${root}/src/data/bookSkmN3.ts'; export * from '${root}/src/data/bookSkmN2.ts';`,resolveDir:root,loader:'ts'},bundle:true,write:false,format:'esm',platform:'node'});
const data=await import('data:text/javascript;base64,'+Buffer.from(result.outputFiles[0].text).toString('base64'));
fs.mkdirSync('data/exam-prep-audit',{recursive:true});
fs.writeFileSync('data/exam-prep-audit/snapshot.json',JSON.stringify(data,null,2));
const points=data.ALL_GRAMMAR_POINTS;
const norm=s=>s.replace(/[\s、。！？,.!?「」『』]/g,'');
const report={exports:Object.fromEntries(Object.entries(data).map(([k,v])=>[k,Array.isArray(v)?v.length:Object.keys(v).length])),levels:{},duplicatePointIds:[],tokenMismatches:[],quizIssues:[],catalog:[]};
const ids=new Set();for(const p of points){report.levels[p.level]=(report.levels[p.level]||0)+1;if(ids.has(p.id))report.duplicatePointIds.push(p.id);ids.add(p.id);for(const s of p.sentences){const joined=s.tokens.map(t=>t.word).join('');if(norm(joined)!==norm(s.japanese))report.tokenMismatches.push({point:p.id,id:s.id,japanese:s.japanese,displayed:joined});}for(const q of p.quiz){if(q.options.length!==4||q.explanations.length!==q.options.length||q.explanations.some((e,i)=>e.text!==q.options[i]||e.isCorrect!==(i===q.correctIndex)))report.quizIssues.push({point:p.id,question:q});}}
for(const b of data.BOOK_SOURCES){let refs=b.sections.flatMap(s=>s.grammarIds);report.catalog.push({book:b.id,references:refs.length,available:refs.filter(id=>ids.has(id)).length,missing:refs.filter(id=>!ids.has(id))});}
fs.writeFileSync('data/exam-prep-audit/structural-report.json',JSON.stringify(report,null,2));
console.log(JSON.stringify({...report,tokenMismatches:report.tokenMismatches.slice(0,6),quizIssues:report.quizIssues.slice(0,2)},null,2));
