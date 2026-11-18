import { test, expect } from '@playwright/test';

test.describe('Genki I Lessons 1–12 End-to-End Study Readiness', () => {
  test('Genki I Lesson 1: Learn desk displays all 4 cards, table, and disclosure controls', async ({ page }) => {
    await page.goto('/learn/g1-l1-wa-desu');
    await expect(page.getByText('320 points', { exact: true })).toBeVisible();
    await expect(page.getByText('Identify or describe a topic: as for X, it is Y.').first()).toBeVisible();
    await expect(page.locator('[data-source-text*="私はアリゾナ大学の学生です"]').first()).toBeVisible();

    // Translation should be hidden by default
    await expect(page.getByText('I am a student at the University of Arizona.')).not.toBeVisible();
    await page.getByRole('button', { name: 'Show meaning' }).first().click();
    await expect(page.getByText('I am a student at the University of Arizona.')).toBeVisible();

    // Direct route to time-and-age card to verify master table
    await page.goto('/learn/g1-l1-time-and-age');
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
    await expect(page.locator('[data-source-text*="Time"]').first()).toBeVisible();
    await expect(page.locator('[data-source-text*="4時 = よじ"]').first()).toBeVisible();
  });

  test('Genki I Lesson 1: Practice mode loads exact 12 questions, handles grading and assistance', async ({ page }) => {
    await page.goto('/practice/genki-1/Lesson%201');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();
    await expect(page.getByText('First day of class.')).toBeVisible();
    await expect(page.locator('[data-source-text*="私（　　）キム・ソラです"]').first()).toBeVisible();

    const correctOptBtn = page.locator('button').filter({ has: page.locator('[data-source-text="は"]') }).first();
    await correctOptBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
    await expect(page.getByText("The particle は (pronounced wa) sets up the topic of discourse")).toBeVisible();
  });

  test('Genki I Lesson 2: Practice mode loads exact 12 questions with visible context', async ({ page }) => {
    await page.goto('/practice/genki-1/Lesson%202');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();
    await expect(page.getByText('Speaker holds a small black umbrella')).toBeVisible();
  });

  test('Genki I Lesson 3: Verb conjugation matrix renders and practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/added-g1-3-2');
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
    await expect(page.locator('[data-source-text*="The Three Verb Groups"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%203');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();
    await expect(page.getByText('Talking about daily breakfast habits')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="食べます"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
    await expect(page.getByText('Ru-verb').first()).toBeVisible();
  });

  test('Genki I Lesson 4: Existence verbs and spatial practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/added-g1-4-4');
    await expect(page.locator('[data-source-text*="あります・います"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%204');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="あります"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 5: Adjective matrix renders and practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/added-g1-5-6');
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
    await expect(page.locator('[data-source-text*="Adjective Conjugation Matrix"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%205');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="高くないです"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 6: Te-form matrix renders and practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/added-g1-6-8');
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
    await expect(page.locator('[data-source-text*="Te-Form"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%206');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="食べて"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 7: Resultant state ~teiru and physical descriptions practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/added-g1-7-9');
    await expect(page.locator('[data-source-text*="〜ている"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%207');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="読んでいます"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 8: Short forms matrix renders and practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/added-g1-8-11');
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
    await expect(page.locator('[data-source-text*="Plain / Short Forms"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%208');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="ないで"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 9: Past plain forms and mou/mada practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/g1-l9-mou-mada');
    await expect(page.locator('[data-source-text*="もう〜ました"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%209');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="読んだ"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 10: Comparison structures and tsumori practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/g1-l10-tsumori');
    await expect(page.locator('[data-source-text*="〜つもりだ"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%2010');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ hasText: 'のほうが・より' });
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 11: Tai desire and past experience practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/g1-l11-tai-desire');
    await expect(page.locator('[data-source-text*="〜たい"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%2011');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="行きたい"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki I Lesson 12: Advice, obligation and node practice loads exact 12 questions', async ({ page }) => {
    await page.goto('/learn/added-g1-12-19');
    await expect(page.locator('[data-source-text*="〜ほうがいい"]').first()).toBeVisible();

    await page.goto('/practice/genki-1/Lesson%2012');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="行った"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });
});
