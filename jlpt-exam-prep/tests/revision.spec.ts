import { test, expect } from '@playwright/test';
import raw from '../src/data/studyPoints.json' with { type: 'json' };
import sources from '../src/data/bookSources.json' with { type: 'json' };
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
  await catalog.getByRole('button').filter({ hasText: added.title }).click();
  await expect(page.getByText(added.sentences[0].japanese, { exact: true })).toBeVisible();
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
  await expect(sentenceLine).toHaveText(s.japanese);
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
  await page.getByRole('button', { name: `${question.correctIndex + 1} ${question.options[question.correctIndex]}`, exact: true }).click();
  await expect(page.getByText('Correct! Well recognized.', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: 'Retry', exact: true }).click();
  const wrong = (question.correctIndex + 1) % question.options.length;
  await page.getByRole('button', { name: `${wrong + 1} ${question.options[wrong]}`, exact: true }).click();
  await expect(page.getByText('Incorrect. Notice the rule below:', { exact: true })).toBeVisible();
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('bunpou_flagged_mistakes') || '[]'))).toContain(question.id);
  await page.reload();
  await expect(page.getByTitle('Remove from Weak Points')).toBeVisible();
  await page.setViewportSize({ width: 390, height: 844 });
  expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(390);
});
