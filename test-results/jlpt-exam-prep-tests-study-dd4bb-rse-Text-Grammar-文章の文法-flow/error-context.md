# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\study_flow_n2.spec.ts >> Shin Kanzen Master N2 End-to-End Study Readiness >> SKM N2 Practice Mode: Part 3 Chapter 1 Discourse / Text Grammar (文章の文法) flow
- Location: jlpt-exam-prep\tests\study_flow_n2.spec.ts:68:3

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/practice/skm-n2/Part%203%20%C2%B7%20Chapter%201", waiting until "load"

```

# Test source

```ts
  1  | import { test, expect } from '@playwright/test';
  2  | 
  3  | test.describe('Shin Kanzen Master N2 End-to-End Study Readiness', () => {
  4  | 
  5  |   test('SKM N2 Learn Desk: Newly verified cards (反面, くせに, ことから, わけではない, 次第では)', async ({ page }) => {
  6  |     // 1. 反面
  7  |     await page.goto('/learn/skm2-c14-hanmen');
  8  |     await expect(page.locator('[data-source-text*="〜反面"]').first()).toBeVisible();
  9  | 
  10 |     // 2. くせに
  11 |     await page.goto('/learn/skm2-c15-kuse-ni');
  12 |     await expect(page.locator('[data-source-text*="〜くせに"]').first()).toBeVisible();
  13 | 
  14 |     // 3. ことから
  15 |     await page.goto('/learn/skm2-c17-koto-kara');
  16 |     await expect(page.locator('[data-source-text*="〜ことから"]').first()).toBeVisible();
  17 | 
  18 |     // 4. わけではない
  19 |     await page.goto('/learn/skm2-c17-wake-de-wa-nai');
  20 |     await expect(page.locator('[data-source-text*="〜わけではない"]').first()).toBeVisible();
  21 | 
  22 |     // 5. 次第では
  23 |     await page.goto('/learn/skm2-c20-shidai-de-wa');
  24 |     await expect(page.locator('[data-source-text*="〜次第では"]').first()).toBeVisible();
  25 |   });
  26 | 
  27 |   test('SKM N2 Learn Desk: High-Yield Matrices (Form Reviews A–D)', async ({ page }) => {
  28 |     // Review A: Inception & Turning Point Matrix
  29 |     await page.goto('/learn/added-n2-a-116');
  30 |     await expect(page.locator('[data-source-text*="〜において"]').first()).toBeVisible();
  31 |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  32 | 
  33 |     // Review B: Evidential Evaluation Matrix
  34 |     await page.goto('/learn/added-n2-b-117');
  35 |     await expect(page.locator('[data-source-text*="〜とはいいながら"]').first()).toBeVisible();
  36 |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  37 | 
  38 |     // Review C: Classical Remnants Matrix
  39 |     await page.goto('/learn/added-n2-c-118');
  40 |     await expect(page.locator('[data-source-text*="古い形"]').first()).toBeVisible();
  41 |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  42 |   });
  43 | 
  44 |   test('SKM N2 Practice Mode: Part 1 Chapter 1 practice loads 12 Qs and grades correctly', async ({ page }) => {
  45 |     await page.goto('/practice/skm-n2/Part%201%20%C2%B7%20Chapter%201');
  46 |     await expect(page.getByText('1 / 12')).toBeVisible();
  47 |     await expect(page.getByText('Question 1')).toBeVisible();
  48 | 
  49 |     // Answer Question 1: にあたって
  50 |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="にあたって"]') });
  51 |     await optBtn.click({ position: { x: 10, y: 10 } });
  52 |     await expect(page.getByText('Correct!')).toBeVisible();
  53 |   });
  54 | 
  55 |   test('SKM N2 Practice Mode: Part 2 Chapter 1 Star-Mark (文の組み立て) rearrangement flow', async ({ page }) => {
  56 |     await page.goto('/practice/skm-n2/Part%202%20%C2%B7%20Chapter%201');
  57 |     await expect(page.getByText('1 / 12')).toBeVisible();
  58 | 
  59 |     // Verify Star-Mark Instructions banner
  60 |     await expect(page.getByText('★ Instructions:')).toBeVisible();
  61 | 
  62 |     // Answer Question 1 Star position: 短期間で開発
  63 |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="短期間で開発"]') });
  64 |     await optBtn.click({ position: { x: 10, y: 10 } });
  65 |     await expect(page.getByText('Correct!')).toBeVisible();
  66 |   });
  67 | 
  68 |   test('SKM N2 Practice Mode: Part 3 Chapter 1 Discourse / Text Grammar (文章の文法) flow', async ({ page }) => {
> 69 |     await page.goto('/practice/skm-n2/Part%203%20%C2%B7%20Chapter%201');
     |                ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
  70 |     await expect(page.getByText('1 / 12')).toBeVisible();
  71 | 
  72 |     // Answer Question 1: なぜなら
  73 |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="なぜなら"]') });
  74 |     await optBtn.click({ position: { x: 10, y: 10 } });
  75 |     await expect(page.getByText('Correct!')).toBeVisible();
  76 |   });
  77 | 
  78 | });
  79 | 
```