# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\revision.spec.ts >> catalog, keyboard search and complete sentence display
- Location: jlpt-exam-prep\tests\revision.spec.ts:28:1

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/", waiting until "load"

```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | import raw from '../src/data/studyPoints.json' with { type: 'json' };
  3   | import sources from '../src/data/bookSources.json' with { type: 'json' };
  4   | import annotations from '../src/data/annotations.json' with { type: 'json' };
  5   | import { alignSentence, orderQuestion } from '../src/studyUtils';
  6   | import type { GrammarPoint } from '../src/types';
  7   | const points = raw as GrammarPoint[];
  8   | test('all content links, sentences and shuffled answers remain intact', () => {
  9   |   expect(new Set(points.map(p => p.id)).size).toBe(points.length);
  10  |   const sentences = points.flatMap(p => p.sentences), questions = points.flatMap(p => p.quiz);
  11  |   expect(new Set(sentences.map(s => s.id)).size).toBe(sentences.length);
  12  |   expect(new Set(questions.map(q => q.id)).size).toBe(questions.length);
  13  |   for (const book of sources) for (const section of book.sections) {
  14  |     expect(section.grammarIds.length).toBeGreaterThan(0);
  15  |     for (const id of section.grammarIds) expect(points.find(p => p.id === id)?.book).toBe(book.name);
  16  |   }
  17  |   for (const sentence of sentences) expect(alignSentence(sentence).map(p => p.text).join('')).toBe(sentence.japanese);
  18  |   const positions = new Set<number>();
  19  |   for (const q of questions) {
  20  |     const shuffled = orderQuestion(q); positions.add(shuffled.correctIndex);
  21  |     expect(shuffled.options[shuffled.correctIndex]).toBe(q.options[q.correctIndex]);
  22  |     expect(shuffled.explanations.filter(e => e.isCorrect)).toHaveLength(1);
  23  |     shuffled.options.forEach((option, i) => { expect(shuffled.explanations[i].text).toBe(option); expect(shuffled.explanations[i].isCorrect).toBe(i === shuffled.correctIndex); });
  24  |     expect(orderQuestion(q)).toEqual(shuffled);
  25  |   }
  26  |   expect(positions.size).toBe(4);
  27  | });
  28  | test('catalog, keyboard search and complete sentence display', async ({ page }) => {
  29  |   const errors: string[] = []; page.on('pageerror', e => errors.push(e.message));
> 30  |   await page.goto('/');
      |              ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
  31  |   await expect(page.getByText(`${points.length} points`, { exact: true })).toBeVisible();
  32  |   await page.getByTitle('View Canonical Books Coverage').click();
  33  |   const catalog = page.getByRole('dialog');
  34  |   await expect(catalog).toBeVisible();
  35  |   for (const book of sources) {
  36  |     await catalog.getByRole('button', { name: book.level+' '+book.name, exact: true }).click();
  37  |     await expect(catalog.getByText(book.sections.at(-1)!.name, { exact: true })).toBeVisible();
  38  |   }
  39  |   const book = sources[3], lastId = book.sections.at(-1)!.grammarIds.at(-1)!;
  40  |   const added = points.find(p => p.id === lastId)!;
  41  |   await catalog.getByRole('button').filter({ hasText: added.meaning }).click();
  42  |   await expect(page.locator('[data-source-text]').filter({ hasText: added.sentences[0].english })).toHaveCount(0);
  43  |   expect(await page.locator('div.flex-1.leading-loose').first().evaluate(el => { const clone = el.cloneNode(true) as HTMLElement; clone.querySelectorAll('rt').forEach(n => n.remove()); return clone.textContent; })).toBe(added.sentences[0].japanese);
  44  |   await page.keyboard.press('Control+k');
  45  |   await expect(page.getByRole('dialog', { name: 'Search grammar' })).toBeVisible();
  46  |   await page.keyboard.press('Escape');
  47  |   await expect(page.getByRole('dialog')).toHaveCount(0);
  48  |   expect(errors).toEqual([]);
  49  | });
  50  | test('partial annotations preserve sentence and accessible tooltip', async ({ page }) => {
  51  |   const point = points.find(p => p.sentences.some(s => s.tokens.length > 0 && s.tokens.map(t => t.word).join('') !== s.japanese))!;
  52  |   await page.addInitScript(id => localStorage.setItem('bunpou_current_point_id', id), point.id);
  53  |   await page.goto('/');
  54  |   const s = point.sentences[0];
  55  |   const sentenceLine = page.locator('div.flex-1.leading-loose').first();
  56  |   expect(await sentenceLine.evaluate(el => { const clone = el.cloneNode(true) as HTMLElement; clone.querySelectorAll('rt').forEach(n => n.remove()); return clone.textContent; })).toBe(s.japanese);
  57  |   const trigger = sentenceLine.getByRole('button').first();
  58  |   await trigger.focus();
  59  |   await expect(page.getByRole('tooltip')).toBeVisible();
  60  |   const box = await page.getByRole('tooltip').boundingBox();
  61  |   expect(box!.x).toBeGreaterThanOrEqual(0); expect(box!.x+box!.width).toBeLessThanOrEqual(1280);
  62  |   await page.keyboard.press('Escape'); await expect(page.getByRole('tooltip')).toHaveCount(0);
  63  |   await page.setViewportSize({ width: 390, height: 844 });
  64  |   await trigger.scrollIntoViewIfNeeded();
  65  |   await trigger.click(); await expect(page.getByRole('tooltip')).toBeVisible();
  66  |   const small = await page.getByRole('tooltip').boundingBox(); expect(small!.x+small!.width).toBeLessThanOrEqual(390);
  67  | });
  68  | 
  69  | test('quiz grading and weak-point persistence match shuffled choices', async ({ page }) => {
  70  |   const point = points[0], question = orderQuestion(point.quiz[0]);
  71  |   await page.goto('/');
  72  |   await page.locator('button').filter({ has: page.locator('[data-source-text]').filter({ hasText: question.options[question.correctIndex] }) }).filter({ hasText: String(question.correctIndex + 1) }).first().click();
  73  |   await expect(page.getByText('Correct! Well recognized.', { exact: true })).toBeVisible();
  74  |   await page.getByRole('button', { name: 'Retry', exact: true }).click();
  75  |   const wrong = (question.correctIndex + 1) % question.options.length;
  76  |   await page.locator('button').filter({ has: page.locator('[data-source-text]').filter({ hasText: question.options[wrong] }) }).filter({ hasText: String(wrong + 1) }).first().click();
  77  |   await expect(page.getByText('Incorrect. Notice the rule below:', { exact: true })).toBeVisible();
  78  |   expect(await page.evaluate(() => JSON.parse(localStorage.getItem('bunpou_flagged_mistakes') || '[]'))).toContain(question.id);
  79  |   await page.reload();
  80  |   await expect(page.getByTitle('Remove from Weak Points')).toBeVisible();
  81  |   await page.setViewportSize({ width: 390, height: 844 });
  82  |   expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(390);
  83  | });
  84  | test('book-default readings and heading meanings work at N3 and N2', async ({ page }) => {
  85  |   await page.addInitScript(() => { if (!localStorage.getItem('bunpou_current_point_id')) localStorage.setItem('bunpou_current_point_id', 'skm3-u3-ni-kagiru'); });
  86  |   await page.goto('/');
  87  |   await expect(page.getByTitle('Textbook readings: Genki/N3 above; N2 on hover')).toHaveAttribute('aria-pressed', 'true');
  88  |   const h1 = page.locator('h1');
  89  |   await expect(h1.locator('rt').filter({ hasText: 'にかぎる' })).toBeVisible();
  90  |   await h1.getByRole('button').filter({ hasText: 'に限る' }).hover();
  91  |   await expect(page.getByRole('tooltip')).toContainText('nothing beats; best to');
  92  |   await expect(page.getByRole('tooltip')).toContainText('にかぎる');
  93  |   await page.keyboard.press('Escape');
  94  |   await page.evaluate(() => localStorage.setItem('bunpou_current_point_id', 'added-n2-5-77'));
  95  |   await page.reload();
  96  |   await expect(page.locator('h1 rt')).toHaveCount(0);
  97  |   await page.locator('h1').getByRole('button').filter({ hasText: 'に限り' }).hover();
  98  |   await expect(page.getByRole('tooltip')).toContainText('にかぎり');
  99  |   await page.keyboard.press('Escape');
  100 |   await page.getByTitle('Always show Furigana').click();
  101 |   await expect(page.locator('h1 rt').first()).toBeVisible();
  102 | });
  103 | 
  104 | test('contextual annotations distinguish minute expressions from sufficiency and particles from homographs', () => {
  105 |   const annMap = annotations as Record<string, Array<{ word: string; reading: string; meaning: string }>>;
  106 | 
  107 |   // 1. 三十分後 must be 30 minutes (さんじゅっぷんご), not sufficiency (じゅうぶん)
  108 |   const sanjuppunTokens = annMap['三十分後には着くと思います'];
  109 |   expect(sanjuppunTokens).toBeDefined();
  110 |   expect(sanjuppunTokens[0].word).toBe('三十分後');
  111 |   expect(sanjuppunTokens[0].reading).toBe('さんじゅっぷんご');
  112 |   expect(sanjuppunTokens[0].meaning).toContain('30 minutes');
  113 | 
  114 |   // 2. 十分 in 駅まで十分くらいかかります must be 10 minutes (じゅっぷん), and くらい must be approximation (not dark/gloomy)
  115 |   const juppunTokens = annMap['駅まで十分くらいかかります'];
  116 |   expect(juppunTokens).toBeDefined();
  117 |   const juppunTok = juppunTokens.find(t => t.word === '十分');
  118 |   expect(juppunTok).toBeDefined();
  119 |   expect(juppunTok?.reading).toBe('じゅっぷん');
  120 |   expect(juppunTok?.meaning).toContain('10 minutes');
  121 | 
  122 |   const kuraiTok = juppunTokens.find(t => t.word === 'くらい');
  123 |   expect(kuraiTok).toBeDefined();
  124 |   expect(kuraiTok?.reading).toBe('くらい');
  125 |   expect(kuraiTok?.meaning).toContain('approximately');
  126 |   expect(kuraiTok?.meaning).not.toContain('dark');
  127 | 
  128 |   // 3. 十分じゅっぷん must annotate 十分 as じゅっぷん
  129 |   const readingDemo = annMap['十分じゅっぷん'];
  130 |   expect(readingDemo).toBeDefined();
```