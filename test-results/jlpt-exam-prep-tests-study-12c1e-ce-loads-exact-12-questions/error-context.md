# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\study_flow.spec.ts >> Genki I Lessons 1–12 End-to-End Study Readiness >> Genki I Lesson 11: Tai desire and past experience practice loads exact 12 questions
- Location: jlpt-exam-prep\tests\study_flow.spec.ts:152:3

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/learn/g1-l11-tai-desire", waiting until "load"

```

# Test source

```ts
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
  137 |   });
  138 | 
  139 |   test('Genki I Lesson 10: Comparison structures and tsumori practice loads exact 12 questions', async ({ page }) => {
  140 |     await page.goto('/learn/g1-l10-tsumori');
  141 |     await expect(page.locator('[data-source-text*="〜つもりだ"]').first()).toBeVisible();
  142 | 
  143 |     await page.goto('/practice/genki-1/Lesson%2010');
  144 |     await expect(page.getByText('1 / 12')).toBeVisible();
  145 |     await expect(page.getByText('Question 1')).toBeVisible();
  146 | 
  147 |     const optBtn = page.locator('button').filter({ hasText: 'のほうが・より' });
  148 |     await optBtn.click();
  149 |     await expect(page.getByText('Correct!')).toBeVisible();
  150 |   });
  151 | 
  152 |   test('Genki I Lesson 11: Tai desire and past experience practice loads exact 12 questions', async ({ page }) => {
> 153 |     await page.goto('/learn/g1-l11-tai-desire');
      |                ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
  154 |     await expect(page.locator('[data-source-text*="〜たい"]').first()).toBeVisible();
  155 | 
  156 |     await page.goto('/practice/genki-1/Lesson%2011');
  157 |     await expect(page.getByText('1 / 12')).toBeVisible();
  158 |     await expect(page.getByText('Question 1')).toBeVisible();
  159 | 
  160 |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="行きたい"]') }).first();
  161 |     await optBtn.click();
  162 |     await expect(page.getByText('Correct!')).toBeVisible();
  163 |   });
  164 | 
  165 |   test('Genki I Lesson 12: Advice, obligation and node practice loads exact 12 questions', async ({ page }) => {
  166 |     await page.goto('/learn/added-g1-12-19');
  167 |     await expect(page.locator('[data-source-text*="〜ほうがいい"]').first()).toBeVisible();
  168 | 
  169 |     await page.goto('/practice/genki-1/Lesson%2012');
  170 |     await expect(page.getByText('1 / 12')).toBeVisible();
  171 |     await expect(page.getByText('Question 1')).toBeVisible();
  172 | 
  173 |     const optBtn = page.locator('button').filter({ has: page.locator('[data-source-text="行った"]') }).first();
  174 |     await optBtn.click();
  175 |     await expect(page.getByText('Correct!')).toBeVisible();
  176 |   });
  177 | });
  178 | 
```