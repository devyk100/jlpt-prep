import { test, expect } from '@playwright/test';

test.describe('Shin Kanzen Master N3 End-to-End Study Readiness', () => {

  test('SKM N3 Part 1 Chapter 1: Time Sequence Spectrum desk & practice 12 Qs', async ({ page }) => {
    // 1. Learn Desk
    await page.goto('/learn/skm3-u1-tokoro-da-phases');
    await expect(page.locator('[data-source-text*="〜ところだ"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    // 2. Practice Mode
    await page.goto('/practice/skm-n3/Part%201%20%C2%B7%20Chapter%201');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    // Answer Question 1 correctly: うちに
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="うちに"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('SKM N3 Form Review B: Compound Particles Matrix & practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/added-n3-b-60');
    await expect(page.locator('[data-source-text*="助詞の整理"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    await page.goto('/practice/skm-n3/Part%201%20%C2%B7%20Form%20review%20B');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: にとって
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="にとって"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('SKM N3 Form Review C & E: Nominalizers & Wake Quadruplets desk verification', async ({ page }) => {
    // Form Review C
    await page.goto('/learn/added-n3-c-61');
    await expect(page.locator('[data-source-text*="名詞化の整理"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    // Form Review E
    await page.goto('/learn/added-n3-e-63');
    await expect(page.locator('[data-source-text*="わけ」の整理"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  });

  test('SKM N3 Part 2 Chapter 1: Star-Mark (文の組み立て) rearrangement flow', async ({ page }) => {
    await page.goto('/practice/skm-n3/Part%202%20%C2%B7%20Chapter%201');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Verify Star-Mark Instructions banner is displayed
    await expect(page.getByText('★ Instructions:')).toBeVisible();
    await expect(page.getByText('Rearrange the 4 scrambled parts into correct grammatical sequence.')).toBeVisible();

    // Answer Question 1 Star position: 遅れる
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="遅れる"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('SKM N3 Part 3 Chapter 1: Discourse / Text Grammar (文章の文法) flow', async ({ page }) => {
    await page.goto('/practice/skm-n3/Part%203%20%C2%B7%20Chapter%201');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: からだ
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="からだ"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

});
