import { test, expect } from '@playwright/test';
import raw from '../src/data/studyPoints.json' with { type: 'json' };
import sources from '../src/data/bookSources.json' with { type: 'json' };
import annotations from '../src/data/annotations.json' with { type: 'json' };
import { alignSentence, orderQuestion } from '../src/studyUtils';
import type { GrammarPoint } from '../src/types';
const points = raw as GrammarPoint[];
test('all content links, sentences and shuffled answers remain intact', () => {
  expect(new Set(points.map(p => p.id)).size).toBe(points.length);
  const sentences = points.flatMap(p => p.sentences), questions = points.flatMap(p => p.quiz);
  expect(new Set(sentences.map(s => s.id)).size).toBe(sentences.length);
  expect(new Set(questions.map(q => q.id)).size).toBe(questions.length);
  for (const book of sources) for (const section of book.sections) {
    expect(section.grammarIds.length).toBeGreaterThan(0);
    for (const id of section.grammarIds) expect(points.find(p => p.id === id)?.book).toBe(book.name);
  }
  for (const sentence of sentences) expect(alignSentence(sentence).map(p => p.text).join('')).toBe(sentence.japanese);
  const positions = new Set<number>();
  for (const q of questions) {
    const shuffled = orderQuestion(q); positions.add(shuffled.correctIndex);
    expect(shuffled.options[shuffled.correctIndex]).toBe(q.options[q.correctIndex]);
    expect(shuffled.explanations.filter(e => e.isCorrect)).toHaveLength(1);
    shuffled.options.forEach((option, i) => { expect(shuffled.explanations[i].text).toBe(option); expect(shuffled.explanations[i].isCorrect).toBe(i === shuffled.correctIndex); });
    expect(orderQuestion(q)).toEqual(shuffled);
  }
  expect(positions.size).toBe(4);
});
test('catalog, keyboard search and complete sentence display', async ({ page }) => {
  const errors: string[] = []; page.on('pageerror', e => errors.push(e.message));
  await page.goto('/');
  await expect(page.getByText('370 points', { exact: true })).toBeVisible();
  await page.getByTitle('View Canonical Books Coverage').click();
  const catalog = page.getByRole('dialog');
  await expect(catalog).toBeVisible();
  for (const book of sources) {
    await catalog.getByRole('button', { name: book.level+' '+book.name, exact: true }).click();
    await expect(catalog.getByText(book.sections.at(-1)!.name, { exact: true })).toBeVisible();
  }
  const book = sources[3], lastId = book.sections.at(-1)!.grammarIds.at(-1)!;
  const added = points.find(p => p.id === lastId)!;
  await catalog.getByRole('button').filter({ hasText: added.meaning }).click();
  await expect(page.locator('[data-source-text]').filter({ hasText: added.sentences[0].english })).toHaveCount(0);
  expect(await page.locator('div.flex-1.leading-loose').first().evaluate(el => { const clone = el.cloneNode(true) as HTMLElement; clone.querySelectorAll('rt').forEach(n => n.remove()); return clone.textContent; })).toBe(added.sentences[0].japanese);
  await page.keyboard.press('Control+k');
  await expect(page.getByRole('dialog', { name: 'Search grammar' })).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.getByRole('dialog')).toHaveCount(0);
  expect(errors).toEqual([]);
});
test('partial annotations preserve sentence and accessible tooltip', async ({ page }) => {
  const point = points.find(p => p.sentences.some(s => s.tokens.length > 0 && s.tokens.map(t => t.word).join('') !== s.japanese))!;
  await page.addInitScript(id => localStorage.setItem('bunpou_current_point_id', id), point.id);
  await page.goto('/');
  const s = point.sentences[0];
  const sentenceLine = page.locator('div.flex-1.leading-loose').first();
  expect(await sentenceLine.evaluate(el => { const clone = el.cloneNode(true) as HTMLElement; clone.querySelectorAll('rt').forEach(n => n.remove()); return clone.textContent; })).toBe(s.japanese);
  const trigger = sentenceLine.getByRole('button').first();
  await trigger.focus();
  await expect(page.getByRole('tooltip')).toBeVisible();
  const box = await page.getByRole('tooltip').boundingBox();
  expect(box!.x).toBeGreaterThanOrEqual(0); expect(box!.x+box!.width).toBeLessThanOrEqual(1280);
  await page.keyboard.press('Escape'); await expect(page.getByRole('tooltip')).toHaveCount(0);
  await page.setViewportSize({ width: 390, height: 844 });
  await trigger.scrollIntoViewIfNeeded();
  await trigger.click(); await expect(page.getByRole('tooltip')).toBeVisible();
  const small = await page.getByRole('tooltip').boundingBox(); expect(small!.x+small!.width).toBeLessThanOrEqual(390);
});

test('quiz grading and weak-point persistence match shuffled choices', async ({ page }) => {
  const point = points[0], question = orderQuestion(point.quiz[0]);
  await page.goto('/');
  await page.locator('button').filter({ has: page.locator('[data-source-text]').filter({ hasText: question.options[question.correctIndex] }) }).filter({ hasText: String(question.correctIndex + 1) }).first().click();
  await expect(page.getByText('Correct! Well recognized.', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: 'Retry', exact: true }).click();
  const wrong = (question.correctIndex + 1) % question.options.length;
  await page.locator('button').filter({ has: page.locator('[data-source-text]').filter({ hasText: question.options[wrong] }) }).filter({ hasText: String(wrong + 1) }).first().click();
  await expect(page.getByText('Incorrect. Notice the rule below:', { exact: true })).toBeVisible();
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('bunpou_flagged_mistakes') || '[]'))).toContain(question.id);
  await page.reload();
  await expect(page.getByTitle('Remove from Weak Points')).toBeVisible();
  await page.setViewportSize({ width: 390, height: 844 });
  expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(390);
});
test('book-default readings and heading meanings work at N3 and N2', async ({ page }) => {
  await page.addInitScript(() => { if (!localStorage.getItem('bunpou_current_point_id')) localStorage.setItem('bunpou_current_point_id', 'skm3-u3-ni-kagiru'); });
  await page.goto('/');
  await expect(page.getByTitle('Textbook readings: Genki/N3 above; N2 on hover')).toHaveAttribute('aria-pressed', 'true');
  const h1 = page.locator('h1');
  await expect(h1.locator('rt').filter({ hasText: 'にかぎる' })).toBeVisible();
  await h1.getByRole('button').filter({ hasText: 'に限る' }).hover();
  await expect(page.getByRole('tooltip')).toContainText('nothing beats; best to');
  await expect(page.getByRole('tooltip')).toContainText('にかぎる');
  await page.keyboard.press('Escape');
  await page.evaluate(() => localStorage.setItem('bunpou_current_point_id', 'gp-ni-kagiri'));
  await page.reload();
  await expect(page.locator('h1 rt')).toHaveCount(0);
  await page.locator('h1').getByRole('button').filter({ hasText: 'に限り' }).hover();
  await expect(page.getByRole('tooltip')).toContainText('にかぎり');
  await page.keyboard.press('Escape');
  await page.getByTitle('Always show Furigana').click();
  await expect(page.locator('h1 rt').first()).toBeVisible();
});

test('contextual annotations distinguish minute expressions from sufficiency and particles from homographs', () => {
  const annMap = annotations as Record<string, Array<{ word: string; reading: string; meaning: string }>>;

  // 1. 三十分後 must be 30 minutes (さんじゅっぷんご), not sufficiency (じゅうぶん)
  const sanjuppunTokens = annMap['三十分後には着くと思います'];
  expect(sanjuppunTokens).toBeDefined();
  expect(sanjuppunTokens[0].word).toBe('三十分後');
  expect(sanjuppunTokens[0].reading).toBe('さんじゅっぷんご');
  expect(sanjuppunTokens[0].meaning).toContain('30 minutes');

  // 2. 十分 in 駅まで十分くらいかかります must be 10 minutes (じゅっぷん), and くらい must be approximation (not dark/gloomy)
  const juppunTokens = annMap['駅まで十分くらいかかります'];
  expect(juppunTokens).toBeDefined();
  const juppunTok = juppunTokens.find(t => t.word === '十分');
  expect(juppunTok).toBeDefined();
  expect(juppunTok?.reading).toBe('じゅっぷん');
  expect(juppunTok?.meaning).toContain('10 minutes');

  const kuraiTok = juppunTokens.find(t => t.word === 'くらい');
  expect(kuraiTok).toBeDefined();
  expect(kuraiTok?.reading).toBe('くらい');
  expect(kuraiTok?.meaning).toContain('approximately');
  expect(kuraiTok?.meaning).not.toContain('dark');

  // 3. 十分じゅっぷん must annotate 十分 as じゅっぷん
  const readingDemo = annMap['十分じゅっぷん'];
  expect(readingDemo).toBeDefined();
  expect(readingDemo[0].word).toBe('十分');
  expect(readingDemo[0].reading).toBe('じゅっぷん');

  // 4. Adverbial 十分 in 十分説明したつもりでしたが must be じゅうぶん
  const advTokens = annMap['十分説明したつもりでしたが'];
  expect(advTokens).toBeDefined();
  expect(advTokens[0].word).toBe('十分');
  expect(advTokens[0].reading).toBe('じゅうぶん');
  expect(advTokens[0].meaning).toContain('sufficient');

  // 5. N2 quiz skm2-c9-ni-oujite must have unambiguous question and distractors
  const oujitePoint = points.find(p => p.id === 'skm2-c9-ni-oujite');
  expect(oujitePoint).toBeDefined();
  const q = oujitePoint!.quiz[0];
  expect(q.options[q.correctIndex]).toBe('に応じて');
  expect(q.question).toContain('基本給が決定されます');
  expect(q.translation).toBe('Basic salary is determined in accordance with experience and ability.');
  expect(q.options).toEqual(['に応じて', 'にわたって', 'に際して', 'にあたって']);
});

test('supervision round 2 regressions: aspectual compounds, conditional mono nara, domain ue, and enriched N2 coverage', () => {
  const annMap = annotations as Record<string, Array<{ word: string; reading: string; meaning: string }>>;

  // 1. 食べ切りました must have completion meaning (not lexical "cut")
  const tabeTokens = annMap['一人で全部食べ切りました'];
  expect(tabeTokens).toBeDefined();
  const tabeKiri = tabeTokens.find(t => t.word.includes('切') || t.word === '食べ切りました');
  expect(tabeKiri).toBeDefined();
  expect(tabeKiri?.meaning).toContain('complete');
  expect(tabeKiri?.meaning).not.toBe('to cut');

  // 2. 過去に戻れるものなら must annotate ものなら as conditional if (not copula "is")
  const monoNaraTokens = annMap['過去に戻れるものなら'];
  expect(monoNaraTokens).toBeDefined();
  const monoNara = monoNaraTokens.find(t => t.word === 'ものなら');
  expect(monoNara).toBeDefined();
  expect(monoNara?.meaning).toContain('if');
  expect(monoNara?.meaning).not.toContain('copula');

  // 3. 暦の上では must annotate as on/according to the calendar (not "after doing")
  const koyomiTokens = annMap['暦の上では立春とはいうものの'];
  expect(koyomiTokens).toBeDefined();
  const koyomiUe = koyomiTokens.find(t => t.word.includes('上'));
  expect(koyomiUe).toBeDefined();
  expect(koyomiUe?.meaning).toContain('calendar');
  expect(koyomiUe?.meaning).not.toContain('after doing');

  // 4. 机の上に: 上 must mean top/above (not "in addition to")
  const deskTokens = annMap['机の上に飲みかけのお茶があります'];
  expect(deskTokens).toBeDefined();
  const ueTok = deskTokens.find(t => t.word === '上');
  expect(ueTok).toBeDefined();
  expect(ueTok?.meaning).toContain('top');
  expect(ueTok?.meaning).not.toContain('in addition to');

  // 5. 読み通しました must express reading completely through (not "overlook")
  const yomiTokens = annMap['読みかけの本を最後まで読み通しました'];
  expect(yomiTokens).toBeDefined();
  const yomiTooshi = yomiTokens.find(t => t.word.includes('通'));
  expect(yomiTooshi).toBeDefined();
  expect(yomiTooshi?.meaning).toContain('through');
  expect(yomiTooshi?.meaning).not.toContain('overlook');

  // 6. N2 Connector section added-n2-p3-10-150 has at least 20 examples covering all 9 functional groups
  const connPoint = points.find(p => p.id === 'added-n2-p3-10-150');
  expect(connPoint).toBeDefined();
  expect(connPoint!.sentences.length).toBeGreaterThanOrEqual(20);
  const connLabels = connPoint!.sentences.map(s => s.useLabel || '');
  expect(connLabels.some(l => l.includes('Addition') || l.includes('しかも'))).toBe(true);
  expect(connLabels.some(l => l.includes('Contrast') || l.includes('それに対して'))).toBe(true);
  expect(connLabels.some(l => l.includes('Alternative') || l.includes('あるいは'))).toBe(true);
  expect(connLabels.some(l => l.includes('choice') || l.includes('それとも'))).toBe(true);
  expect(connLabels.some(l => l.includes('cause') || l.includes('そのため'))).toBe(true);
  expect(connLabels.some(l => l.includes('conclusion') || l.includes('したがって'))).toBe(true);
  expect(connLabels.some(l => l.includes('reaction') || l.includes('そこで'))).toBe(true);
  expect(connLabels.some(l => l.includes('Triggered') || l.includes('すると'))).toBe(true);
  expect(connLabels.some(l => l.includes('transition') || l.includes('さて'))).toBe(true);
  expect(connLabels.some(l => l.includes('Digressive') || l.includes('ところで'))).toBe(true);

  // 7. N2 Classical form review added-n2-c-118 has at least 9 examples covering all classical families
  const c118Point = points.find(p => p.id === 'added-n2-c-118');
  expect(c118Point).toBeDefined();
  expect(c118Point!.sentences.length).toBeGreaterThanOrEqual(9);
  const c118Labels = c118Point!.sentences.map(s => s.useLabel || '');
  expect(c118Labels.some(l => l.includes('ざる'))).toBe(true);
  expect(c118Labels.some(l => l.includes('まい'))).toBe(true);
  expect(c118Labels.some(l => l.includes('ではあるまいか'))).toBe(true);
  expect(c118Labels.some(l => l.includes('つつある'))).toBe(true);
  expect(c118Labels.some(l => l.includes('せよ'))).toBe(true);
  expect(c118Labels.some(l => l.includes('べき'))).toBe(true);
});
