import { test, expect } from '@playwright/test';

test.describe('Genki II Lessons 13–23 End-to-End Study Readiness', () => {

  test('Genki II Lesson 13: Potential forms desk & practice 12 Qs', async ({ page }) => {
    // 1. Learn Desk
    await page.goto('/learn/g2-l13-potential');
    await expect(page.locator('[data-source-text*="可能形"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    // 2. Practice Mode
    await page.goto('/practice/genki-2/Lesson%2013');
    await expect(page.getByText('1 / 12')).toBeVisible();
    await expect(page.getByText('Question 1')).toBeVisible();

    // Answer Question 1 correctly: 読めます
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="読めます"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 14: Hoshii and Giving/Receiving practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l14-hoshii');
    await expect(page.locator('[data-source-text*="ほしい"]').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2014');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: が
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="が"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 15: Volitional form desk & practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l15-volitional-form');
    await expect(page.locator('[data-source-text*="意向形"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2015');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: 行こう
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="行こう"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 16: Hoping and Toki tense practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l16-to-ii-hoping');
    await expect(page.locator('[data-source-text*="〜といい"]').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2016');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: といい
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="といい"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 17: Conditionals and Hearsay practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l17-hearsay-sou-desu');
    await expect(page.locator('[data-source-text*="〜そうです"]').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2017');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: そうです
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="そうです"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 18: Transitive/Intransitive pairs desk & practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l18-transitive-intransitive');
    await expect(page.locator('[data-source-text*="自動詞 vs 他動詞"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2018');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: 開いています
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="開いています"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 19: Sonkeigo honorifics desk & practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l19-sonkeigo-verbs');
    await expect(page.locator('[data-source-text*="尊敬語"]').first()).toBeVisible();
    await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2019');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: お帰りになりました
    const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text*="お帰りになりました"]') });
    await optBtn.click({ position: { x: 10, y: 10 } });
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 20: Kenjougo humble speech practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/added-g2-20-34');
    await expect(page.locator('[data-source-text*="丁重語・謙譲語"]').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2020');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: 伺います
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="伺います"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 21: Passive voice & te-aru desk & practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l21-te-aru');
    await expect(page.locator('[data-source-text*="〜てある"]').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2021');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: 書いてあります
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="書いてあります"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 22: Causative & ba conditional desk & practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l22-ba-conditional');
    await expect(page.locator('[data-source-text*="〜ば"]').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2022');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: 押せば
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="押せば"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

  test('Genki II Lesson 23: Causative-Passive & temo desk & practice 12 Qs', async ({ page }) => {
    await page.goto('/learn/g2-l23-temo-even-if');
    await expect(page.locator('[data-source-text*="〜ても / 〜でも"]').first()).toBeVisible();

    await page.goto('/practice/genki-2/Lesson%2023');
    await expect(page.getByText('1 / 12')).toBeVisible();

    // Answer Question 1: ても
    const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="ても"]') }).first();
    await optBtn.click();
    await expect(page.getByText('Correct!')).toBeVisible();
  });

});
