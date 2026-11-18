import { test, expect } from '@playwright/test';

test.describe('Shin Kanzen Master N2 End-to-End Study Readiness', () => {

  test('SKM N2 Learn Desk: Newly verified cards (反面, くせに, ことから, わけではない, 次第では)', async ({ page }) => {
    // 1. 反面
    await page.goto('/learn/skm2-c14-hanmen');
    await expect(page.locator('[data-source-text*="〜反面"]').first()).toBeVisible();

    // 2. くせに
    await page.goto('/learn/skm2-c15-kuse-ni');
    await expect(page.locator('[data-source-text*="〜くせに"]').first()).toBeVisible();

    // 3. ことから
    await page.goto('/learn/skm2-c17-koto-kara');
    await expect(page.locator('[data-source-text*="〜ことから"]').first()).toBeVisible();

    // 4. わけではない
    await page.goto('/learn/skm2-c17-wake-de-wa-nai');
    await expect(page.locator('[data-source-text*="〜わけではない"]').first()).toBeVisible();

    // 5. 次第では
    await page.goto('/learn/skm2-c20-shidai-de-wa');
    await expect(page.locator('[data-source-text*="〜次第では"]').first()).toBeVisible();
  });

  test('SKM N2 Learn Desk: High-Yield Matrices (Form Reviews A–D)', async ({ page }) => {
    // Review A: Inception & Turning Point Matrix
    await page.goto('/learn/added-n2-a-116');
    await expect(page.locator('[data-source-text*="〜において"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    // Review B: Evidential Evaluation Matrix
    await page.goto('/learn/added-n2-b-117');
    await expect(page.locator('[data-source-text*="〜とはいいながら"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    // Review C: Classical Remnants Matrix
    await page.goto('/learn/added-n2-c-118');
    await expect(page.locator('[data-source-text*="古い形"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  });

  test('SKM N2 Practice Mode: Part 1 Chapter 1 practice loads 12 Qs and grades correctly', async ({ page }) => {
    await page.goto('/practice/skm-n2/Part%201%20%C2%B7%20Chapter%201');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    // Answer Question 1: にあたって
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="にあたって"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('SKM N2 Practice Mode: Part 2 Chapter 1 Star-Mark (文の組み立て) rearrangement flow', async ({ page }) => {
    await page.goto('/practice/skm-n2/Part%202%20%C2%B7%20Chapter%201');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Verify Star-Mark Instructions banner
    await expect(page.getByText('★ Instructions:')).toBeVisible();

    // Answer Question 1 Star position: 短期間で開発
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="短期間で開発"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('SKM N2 Practice Mode: Part 3 Chapter 1 Discourse / Text Grammar (文章の文法) flow', async ({ page }) => {
    await page.goto('/practice/skm-n2/Part%203%20%C2%B7%20Chapter%201');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: なぜなら
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="なぜなら"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

});
