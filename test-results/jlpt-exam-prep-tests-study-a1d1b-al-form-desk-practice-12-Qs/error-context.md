# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\study_flow_g2.spec.ts >> Genki II Lessons 13–23 End-to-End Study Readiness >> Genki II Lesson 15: Volitional form desk & practice 12 Qs
- Location: jlpt-exam-prep\tests\study_flow_g2.spec.ts:35:3

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/learn/g2-l15-volitional-form", waiting until "load"

```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | 
  3   | test.describe('Genki II Lessons 13–23 End-to-End Study Readiness', () => {
  4   | 
  5   |   test('Genki II Lesson 13: Potential forms desk & practice 12 Qs', async ({ page }) => {
  6   |     // 1. Learn Desk
  7   |     await page.goto('/learn/g2-l13-potential');
  8   |     await expect(page.locator('[data-source-text*="可能形"]').first()).toBeVisible();
  9   |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  10  | 
  11  |     // 2. Practice Mode
  12  |     await page.goto('/practice/genki-2/Lesson%2013');
  13  |     await expect(page.getByText('1 / 12')).toBeVisible();
  14  |     await expect(page.getByText('Question 1')).toBeVisible();
  15  | 
  16  |     // Answer Question 1 correctly: 読めます
  17  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="読めます"]') }).first();
  18  |     await optBtn.click();
  19  |     await expect(page.getByText('Correct!')).toBeVisible();
  20  |   });
  21  | 
  22  |   test('Genki II Lesson 14: Hoshii and Giving/Receiving practice 12 Qs', async ({ page }) => {
  23  |     await page.goto('/learn/g2-l14-hoshii');
  24  |     await expect(page.locator('[data-source-text*="ほしい"]').first()).toBeVisible();
  25  | 
  26  |     await page.goto('/practice/genki-2/Lesson%2014');
  27  |     await expect(page.getByText('1 / 12')).toBeVisible();
  28  | 
  29  |     // Answer Question 1: が
  30  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="が"]') }).first();
  31  |     await optBtn.click();
  32  |     await expect(page.getByText('Correct!')).toBeVisible();
  33  |   });
  34  | 
  35  |   test('Genki II Lesson 15: Volitional form desk & practice 12 Qs', async ({ page }) => {
> 36  |     await page.goto('/learn/g2-l15-volitional-form');
      |                ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
  37  |     await expect(page.locator('[data-source-text*="意向形"]').first()).toBeVisible();
  38  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  39  | 
  40  |     await page.goto('/practice/genki-2/Lesson%2015');
  41  |     await expect(page.getByText('1 / 12')).toBeVisible();
  42  | 
  43  |     // Answer Question 1: 行こう
  44  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="行こう"]') }).first();
  45  |     await optBtn.click();
  46  |     await expect(page.getByText('Correct!')).toBeVisible();
  47  |   });
  48  | 
  49  |   test('Genki II Lesson 16: Hoping and Toki tense practice 12 Qs', async ({ page }) => {
  50  |     await page.goto('/learn/g2-l16-to-ii-hoping');
  51  |     await expect(page.locator('[data-source-text*="〜といい"]').first()).toBeVisible();
  52  | 
  53  |     await page.goto('/practice/genki-2/Lesson%2016');
  54  |     await expect(page.getByText('1 / 12')).toBeVisible();
  55  | 
  56  |     // Answer Question 1: といい
  57  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="といい"]') }).first();
  58  |     await optBtn.click();
  59  |     await expect(page.getByText('Correct!')).toBeVisible();
  60  |   });
  61  | 
  62  |   test('Genki II Lesson 17: Conditionals and Hearsay practice 12 Qs', async ({ page }) => {
  63  |     await page.goto('/learn/g2-l17-hearsay-sou-desu');
  64  |     await expect(page.locator('[data-source-text*="〜そうです"]').first()).toBeVisible();
  65  | 
  66  |     await page.goto('/practice/genki-2/Lesson%2017');
  67  |     await expect(page.getByText('1 / 12')).toBeVisible();
  68  | 
  69  |     // Answer Question 1: そうです
  70  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="そうです"]') }).first();
  71  |     await optBtn.click();
  72  |     await expect(page.getByText('Correct!')).toBeVisible();
  73  |   });
  74  | 
  75  |   test('Genki II Lesson 18: Transitive/Intransitive pairs desk & practice 12 Qs', async ({ page }) => {
  76  |     await page.goto('/learn/g2-l18-transitive-intransitive');
  77  |     await expect(page.locator('[data-source-text*="自動詞 vs 他動詞"]').first()).toBeVisible();
  78  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  79  | 
  80  |     await page.goto('/practice/genki-2/Lesson%2018');
  81  |     await expect(page.getByText('1 / 12')).toBeVisible();
  82  | 
  83  |     // Answer Question 1: 開いています
  84  |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="開いています"]') }).first();
  85  |     await optBtn.click();
  86  |     await expect(page.getByText('Correct!')).toBeVisible();
  87  |   });
  88  | 
  89  |   test('Genki II Lesson 19: Sonkeigo honorifics desk & practice 12 Qs', async ({ page }) => {
  90  |     await page.goto('/learn/g2-l19-sonkeigo-verbs');
  91  |     await expect(page.locator('[data-source-text*="尊敬語"]').first()).toBeVisible();
  92  |     await expect(page.getByText('Mug-Up Matrix').first()).toBeVisible();
  93  | 
  94  |     await page.goto('/practice/genki-2/Lesson%2019');
  95  |     await expect(page.getByText('1 / 12')).toBeVisible();
  96  | 
  97  |     // Answer Question 1: お帰りになりました
  98  |     const optBtn = page.locator('div[role="group"] > button').filter({ has: page.locator('[data-source-text*="お帰りになりました"]') });
  99  |     await optBtn.click({ position: { x: 10, y: 10 } });
  100 |     await expect(page.getByText('Correct!')).toBeVisible();
  101 |   });
  102 | 
  103 |   test('Genki II Lesson 20: Kenjougo humble speech practice 12 Qs', async ({ page }) => {
  104 |     await page.goto('/learn/added-g2-20-34');
  105 |     await expect(page.locator('[data-source-text*="丁重語・謙譲語"]').first()).toBeVisible();
  106 | 
  107 |     await page.goto('/practice/genki-2/Lesson%2020');
  108 |     await expect(page.getByText('1 / 12')).toBeVisible();
  109 | 
  110 |     // Answer Question 1: 伺います
  111 |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="伺います"]') }).first();
  112 |     await optBtn.click();
  113 |     await expect(page.getByText('Correct!')).toBeVisible();
  114 |   });
  115 | 
  116 |   test('Genki II Lesson 21: Passive voice & te-aru desk & practice 12 Qs', async ({ page }) => {
  117 |     await page.goto('/learn/g2-l21-te-aru');
  118 |     await expect(page.locator('[data-source-text*="〜てある"]').first()).toBeVisible();
  119 | 
  120 |     await page.goto('/practice/genki-2/Lesson%2021');
  121 |     await expect(page.getByText('1 / 12')).toBeVisible();
  122 | 
  123 |     // Answer Question 1: 書いてあります
  124 |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="書いてあります"]') }).first();
  125 |     await optBtn.click();
  126 |     await expect(page.getByText('Correct!')).toBeVisible();
  127 |   });
  128 | 
  129 |   test('Genki II Lesson 22: Causative & ba conditional desk & practice 12 Qs', async ({ page }) => {
  130 |     await page.goto('/learn/g2-l22-ba-conditional');
  131 |     await expect(page.locator('[data-source-text*="〜ば"]').first()).toBeVisible();
  132 | 
  133 |     await page.goto('/practice/genki-2/Lesson%2022');
  134 |     await expect(page.getByText('1 / 12')).toBeVisible();
  135 | 
  136 |     // Answer Question 1: 押せば
```