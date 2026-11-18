# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\study_flow.spec.ts >> Genki I Lessons 1–12 End-to-End Study Readiness >> Genki I Lesson 2: Practice mode loads exact 12 questions with visible context
- Location: jlpt-exam-prep\tests\study_flow.spec.ts:35:3

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/practice/genki-1/Lesson%202", waiting until "load"

```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | 
  3   | test.describe('Genki I Lessons 1–12 End-to-End Study Readiness', () => {
  4   |   test('Genki I Lesson 1: Learn desk displays all 4 cards, table, and disclosure controls', async ({ page }) => {
  5   |     await page.goto('/learn/g1-l1-wa-desu');
  6   |     await expect(page.getByText('320 points', { exact: true })).toBeVisible();
  7   |     await expect(page.getByText('Identify or describe a topic: as for X, it is Y.').first()).toBeVisible();
  8   |     await expect(page.locator('[data-source-text*="私はアリゾナ大学の学生です"]').first()).toBeVisible();
  9   | 
  10  |     // Translation should be hidden by default
  11  |     await expect(page.getByText('I am a student at the University of Arizona.')).not.toBeVisible();
  12  |     await page.getByRole('button', { name: 'Show meaning' }).first().click();
  13  |     await expect(page.getByText('I am a student at the University of Arizona.')).toBeVisible();
  14  | 
  15  |     // Direct route to time-and-age card to verify master table
  16  |     await page.goto('/learn/g1-l1-time-and-age');
  17  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  18  |     await expect(page.locator('[data-source-text*="Time"]').first()).toBeVisible();
  19  |     await expect(page.locator('[data-source-text*="4時 = よじ"]').first()).toBeVisible();
  20  |   });
  21  | 
  22  |   test('Genki I Lesson 1: Practice mode loads exact 12 questions, handles grading and assistance', async ({ page }) => {
  23  |     await page.goto('/practice/genki-1/Lesson%201');
  24  |     await expect(page.getByText('1 / 12')).toBeVisible();
  25  |     await expect(page.getByText('Question 1')).toBeVisible();
  26  |     await expect(page.getByText('First day of class.')).toBeVisible();
  27  |     await expect(page.locator('[data-source-text*="私（　　）キム・ソラです"]').first()).toBeVisible();
  28  | 
  29  |     const correctOptBtn = page.locator('button').filter({ has: page.locator('[data-source-text="は"]') }).first();
  30  |     await correctOptBtn.click();
  31  |     await expect(page.getByText('Correct!')).toBeVisible();
  32  |     await expect(page.getByText("The particle は (pronounced wa) sets up the topic of discourse")).toBeVisible();
  33  |   });
  34  | 
  35  |   test('Genki I Lesson 2: Practice mode loads exact 12 questions with visible context', async ({ page }) => {
> 36  |     await page.goto('/practice/genki-1/Lesson%202');
      |                ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
  37  |     await expect(page.getByText('1 / 12')).toBeVisible();
  38  |     await expect(page.getByText('Question 1')).toBeVisible();
  39  |     await expect(page.getByText('Speaker holds a small black umbrella')).toBeVisible();
  40  |   });
  41  | 
  42  |   test('Genki I Lesson 3: Verb conjugation matrix renders and practice loads exact 12 questions', async ({ page }) => {
  43  |     await page.goto('/learn/added-g1-3-2');
  44  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  45  |     await expect(page.locator('[data-source-text*="The Three Verb Groups"]').first()).toBeVisible();
  46  | 
  47  |     await page.goto('/practice/genki-1/Lesson%203');
  48  |     await expect(page.getByText('1 / 12')).toBeVisible();
  49  |     await expect(page.getByText('Question 1')).toBeVisible();
  50  |     await expect(page.getByText('Talking about daily breakfast habits')).toBeVisible();
  51  | 
  52  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="食べます"]') }).first();
  53  |     await optBtn.click();
  54  |     await expect(page.getByText('Correct!')).toBeVisible();
  55  |     await expect(page.getByText('Ru-verb').first()).toBeVisible();
  56  |   });
  57  | 
  58  |   test('Genki I Lesson 4: Existence verbs and spatial practice loads exact 12 questions', async ({ page }) => {
  59  |     await page.goto('/learn/added-g1-4-4');
  60  |     await expect(page.locator('[data-source-text*="あります・います"]').first()).toBeVisible();
  61  | 
  62  |     await page.goto('/practice/genki-1/Lesson%204');
  63  |     await expect(page.getByText('1 / 12')).toBeVisible();
  64  |     await expect(page.getByText('Question 1')).toBeVisible();
  65  | 
  66  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="あります"]') }).first();
  67  |     await optBtn.click();
  68  |     await expect(page.getByText('Correct!')).toBeVisible();
  69  |   });
  70  | 
  71  |   test('Genki I Lesson 5: Adjective matrix renders and practice loads exact 12 questions', async ({ page }) => {
  72  |     await page.goto('/learn/added-g1-5-6');
  73  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  74  |     await expect(page.locator('[data-source-text*="Adjective Conjugation Matrix"]').first()).toBeVisible();
  75  | 
  76  |     await page.goto('/practice/genki-1/Lesson%205');
  77  |     await expect(page.getByText('1 / 12')).toBeVisible();
  78  |     await expect(page.getByText('Question 1')).toBeVisible();
  79  | 
  80  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="高くないです"]') }).first();
  81  |     await optBtn.click();
  82  |     await expect(page.getByText('Correct!')).toBeVisible();
  83  |   });
  84  | 
  85  |   test('Genki I Lesson 6: Te-form matrix renders and practice loads exact 12 questions', async ({ page }) => {
  86  |     await page.goto('/learn/added-g1-6-8');
  87  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  88  |     await expect(page.locator('[data-source-text*="Te-Form"]').first()).toBeVisible();
  89  | 
  90  |     await page.goto('/practice/genki-1/Lesson%206');
  91  |     await expect(page.getByText('1 / 12')).toBeVisible();
  92  |     await expect(page.getByText('Question 1')).toBeVisible();
  93  | 
  94  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="食べて"]') }).first();
  95  |     await optBtn.click();
  96  |     await expect(page.getByText('Correct!')).toBeVisible();
  97  |   });
  98  | 
  99  |   test('Genki I Lesson 7: Resultant state ~teiru and physical descriptions practice loads exact 12 questions', async ({ page }) => {
  100 |     await page.goto('/learn/added-g1-7-9');
  101 |     await expect(page.locator('[data-source-text*="〜ている"]').first()).toBeVisible();
  102 | 
  103 |     await page.goto('/practice/genki-1/Lesson%207');
  104 |     await expect(page.getByText('1 / 12')).toBeVisible();
  105 |     await expect(page.getByText('Question 1')).toBeVisible();
  106 | 
  107 |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="読んでいます"]') }).first();
  108 |     await optBtn.click();
  109 |     await expect(page.getByText('Correct!')).toBeVisible();
  110 |   });
  111 | 
  112 |   test('Genki I Lesson 8: Short forms matrix renders and practice loads exact 12 questions', async ({ page }) => {
  113 |     await page.goto('/learn/added-g1-8-11');
  114 |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  115 |     await expect(page.locator('[data-source-text*="Plain / Short Forms"]').first()).toBeVisible();
  116 | 
  117 |     await page.goto('/practice/genki-1/Lesson%208');
  118 |     await expect(page.getByText('1 / 12')).toBeVisible();
  119 |     await expect(page.getByText('Question 1')).toBeVisible();
  120 | 
  121 |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="ないで"]') }).first();
  122 |     await optBtn.click();
  123 |     await expect(page.getByText('Correct!')).toBeVisible();
  124 |   });
  125 | 
  126 |   test('Genki I Lesson 9: Past plain forms and mou/mada practice loads exact 12 questions', async ({ page }) => {
  127 |     await page.goto('/learn/g1-l9-mou-mada');
  128 |     await expect(page.locator('[data-source-text*="もう〜ました"]').first()).toBeVisible();
  129 | 
  130 |     await page.goto('/practice/genki-1/Lesson%209');
  131 |     await expect(page.getByText('1 / 12')).toBeVisible();
  132 |     await expect(page.getByText('Question 1')).toBeVisible();
  133 | 
  134 |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="読んだ"]') }).first();
  135 |     await optBtn.click();
  136 |     await expect(page.getByText('Correct!')).toBeVisible();
```