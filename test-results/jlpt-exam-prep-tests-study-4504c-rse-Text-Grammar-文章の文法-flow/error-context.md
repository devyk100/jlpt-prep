# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\study_flow_n3.spec.ts >> Shin Kanzen Master N3 End-to-End Study Readiness >> SKM N3 Part 3 Chapter 1: Discourse / Text Grammar (文章の文法) flow
- Location: jlpt-exam-prep\tests\study_flow_n3.spec.ts:62:3

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/practice/skm-n3/Part%203%20%C2%B7%20Chapter%201", waiting until "load"

```

# Test source

```ts
  1  | import { test, expect } from '@playwright/test';
  2  | 
  3  | test.describe('Shin Kanzen Master N3 End-to-End Study Readiness', () => {
  4  | 
  5  |   test('SKM N3 Part 1 Chapter 1: Time Sequence Spectrum desk & practice 12 Qs', async ({ page }) => {
  6  |     // 1. Learn Desk
  7  |     await page.goto('/learn/skm3-u1-tokoro-da-phases');
  8  |     await expect(page.locator('[data-source-text*="〜ところだ"]').first()).toBeVisible();
  9  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  10 | 
  11 |     // 2. Practice Mode
  12 |     await page.goto('/practice/skm-n3/Part%201%20%C2%B7%20Chapter%201');
  13 |     await expect(page.getByText('1 / 12')).toBeVisible();
  14 |     await expect(page.getByText('Question 1')).toBeVisible();
  15 | 
  16 |     // Answer Question 1 correctly: うちに
  17 |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="うちに"]') });
  18 |     await optBtn.click({ position: { x: 10, y: 10 } });
  19 |     await expect(page.getByText('Correct!')).toBeVisible();
  20 |   });
  21 | 
  22 |   test('SKM N3 Form Review B: Compound Particles Matrix & practice 12 Qs', async ({ page }) => {
  23 |     await page.goto('/learn/added-n3-b-60');
  24 |     await expect(page.locator('[data-source-text*="助詞の整理"]').first()).toBeVisible();
  25 |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  26 | 
  27 |     await page.goto('/practice/skm-n3/Part%201%20%C2%B7%20Form%20review%20B');
  28 |     await expect(page.getByText('1 / 12')).toBeVisible();
  29 | 
  30 |     // Answer Question 1: にとって
  31 |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="にとって"]') });
  32 |     await optBtn.click({ position: { x: 10, y: 10 } });
  33 |     await expect(page.getByText('Correct!')).toBeVisible();
  34 |   });
  35 | 
  36 |   test('SKM N3 Form Review C & E: Nominalizers & Wake Quadruplets desk verification', async ({ page }) => {
  37 |     // Form Review C
  38 |     await page.goto('/learn/added-n3-c-61');
  39 |     await expect(page.locator('[data-source-text*="名詞化の整理"]').first()).toBeVisible();
  40 |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  41 | 
  42 |     // Form Review E
  43 |     await page.goto('/learn/added-n3-e-63');
  44 |     await expect(page.locator('[data-source-text*="わけ」の整理"]').first()).toBeVisible();
  45 |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  46 |   });
  47 | 
  48 |   test('SKM N3 Part 2 Chapter 1: Star-Mark (文の組み立て) rearrangement flow', async ({ page }) => {
  49 |     await page.goto('/practice/skm-n3/Part%202%20%C2%B7%20Chapter%201');
  50 |     await expect(page.getByText('1 / 12')).toBeVisible();
  51 | 
  52 |     // Verify Star-Mark Instructions banner is displayed
  53 |     await expect(page.getByText('★ Instructions:')).toBeVisible();
  54 |     await expect(page.getByText('Rearrange the 4 scrambled parts into correct grammatical sequence.')).toBeVisible();
  55 | 
  56 |     // Answer Question 1 Star position: 遅れる
  57 |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="遅れる"]') });
  58 |     await optBtn.click({ position: { x: 10, y: 10 } });
  59 |     await expect(page.getByText('Correct!')).toBeVisible();
  60 |   });
  61 | 
  62 |   test('SKM N3 Part 3 Chapter 1: Discourse / Text Grammar (文章の文法) flow', async ({ page }) => {
> 63 |     await page.goto('/practice/skm-n3/Part%203%20%C2%B7%20Chapter%201');
     |                ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
  64 |     await expect(page.getByText('1 / 12')).toBeVisible();
  65 | 
  66 |     // Answer Question 1: からだ
  67 |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text="からだ"]') });
  68 |     await optBtn.click({ position: { x: 10, y: 10 } });
  69 |     await expect(page.getByText('Correct!')).toBeVisible();
  70 |   });
  71 | 
  72 | });
  73 | 
```