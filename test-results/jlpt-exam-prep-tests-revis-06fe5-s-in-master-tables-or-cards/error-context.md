# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\revision.spec.ts >> no parenthesized romaji pronunciations in master tables or cards
- Location: jlpt-exam-prep\tests\revision.spec.ts:311:1

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/", waiting until "load"

```

# Test source

```ts
  212 |   expect(c118Point).toBeDefined();
  213 |   expect(c118Point!.sentences.length).toBeGreaterThanOrEqual(9);
  214 |   const c118Labels = c118Point!.sentences.map(s => s.useLabel || '');
  215 |   expect(c118Labels.some(l => l.includes('ざる'))).toBe(true);
  216 |   expect(c118Labels.some(l => l.includes('まい'))).toBe(true);
  217 |   expect(c118Labels.some(l => l.includes('ではあるまいか'))).toBe(true);
  218 |   expect(c118Labels.some(l => l.includes('つつある'))).toBe(true);
  219 |   expect(c118Labels.some(l => l.includes('せよ'))).toBe(true);
  220 |   expect(c118Labels.some(l => l.includes('べき'))).toBe(true);
  221 | });
  222 | 
  223 | test('mode separation: in-lesson tables, leakage-free chapter practice, and revision desk', async ({ page }) => {
  224 |   await page.goto('/');
  225 | 
  226 |   // 1. Select Genki I Lesson 1 Time & Age card from the sidebar
  227 |   await page.locator('[role="button"]').filter({ hasText: '時間' }).first().click();
  228 |   await expect(page.getByRole('heading', { name: 'High-Yield Lesson Table' })).toBeVisible();
  229 |   await expect(page.getByRole('heading', { level: 4 }).filter({ hasText: 'Reading Matrix' })).toBeVisible();
  230 | 
  231 |   // 2. Search and select Genki I Lesson 6 Te-form card using sidebar search
  232 |   await page.getByPlaceholder('Search grammar, reading, meaning...').fill('Connect actions');
  233 |   await page.locator('[role="button"]').filter({ hasText: 'Connect actions' }).first().click();
  234 |   await expect(page.getByRole('heading', { name: 'High-Yield Lesson Table' })).toBeVisible();
  235 |   await expect(page.getByRole('heading', { level: 4 }).filter({ hasText: 'Conjugation Matrix' })).toBeVisible();
  236 | 
  237 |   // 3. Switch to Practice Mode via Topbar
  238 |   await page.getByRole('button', { name: /Practice \(練習\)/ }).click();
  239 |   await expect(page.getByText('Question 1')).toBeVisible();
  240 | 
  241 |   // Ensure target grammar name is NOT exposed in the question prompt before answering
  242 |   await expect(page.locator('h1').filter({ hasText: 'X は Y です' })).toHaveCount(0);
  243 | 
  244 |   // Answer question 1 and verify deep feedback
  245 |   const optButton = page.locator('.grid button').filter({ hasText: 'は' }).first();
  246 |   await optButton.click();
  247 |   await expect(page.getByText('Sentence Rationale')).toBeVisible();
  248 |   await expect(page.getByText('Option Breakdown')).toBeVisible();
  249 |   await expect(page.getByRole('button', { name: /Review Lesson:/ })).toBeVisible();
  250 | 
  251 |   // 4. Switch to Revision Mode via Topbar
  252 |   await page.getByRole('button', { name: /Revision \(暗記表\)/ }).click();
  253 |   await expect(page.getByText('Revision & Master "Mug-Up" Tables')).toBeVisible();
  254 |   await expect(page.getByRole('button', { name: /Jump to Lesson in Textbook/ }).first()).toBeVisible();
  255 | });
  256 | 
  257 | test('default Japanese-only examples, independent translation disclosure, and translation-leak-free practice', async ({ page }) => {
  258 |   await page.goto('/');
  259 | 
  260 |   // 1. Open Genki I Lesson 1 first lesson card
  261 |   await page.locator('[role="button"]').filter({ hasText: 'X は Y です' }).first().click();
  262 | 
  263 |   // Verify Japanese examples are visible while English translations are hidden by default
  264 |   const showMeaningButtons = page.getByRole('button', { name: 'Show meaning' });
  265 |   await expect(showMeaningButtons.first()).toBeVisible();
  266 |   const count = await showMeaningButtons.count();
  267 |   expect(count).toBeGreaterThanOrEqual(2);
  268 | 
  269 |   // Translations should NOT be visible yet
  270 |   await expect(page.getByText('Translation:').first()).not.toBeVisible();
  271 | 
  272 |   // 2. Click "Show meaning" on the first sentence only
  273 |   await showMeaningButtons.first().click();
  274 |   await expect(page.getByText('Translation:').first()).toBeVisible();
  275 |   await expect(page.getByRole('button', { name: 'Hide meaning' }).first()).toBeVisible();
  276 | 
  277 |   // The second sentence must still remain hidden
  278 |   const remainingShowMeaning = page.getByRole('button', { name: 'Show meaning' });
  279 |   await expect(remainingShowMeaning.first()).toBeVisible();
  280 | 
  281 |   // 3. Switch to Practice Mode
  282 |   await page.getByRole('button', { name: /Practice \(練習\)/ }).click();
  283 |   await expect(page.getByText('Question 1')).toBeVisible();
  284 | 
  285 |   // Verify prompt translation is hidden by default before answering
  286 |   await expect(page.getByText('I am Sora Kim. I am Korean.')).not.toBeVisible();
  287 |   const hintBtn = page.getByRole('button', { name: /Show Translation Hint/ });
  288 |   await expect(hintBtn).toBeVisible();
  289 | 
  290 |   // Click translation hint to test opt-in assisted attempt
  291 |   await hintBtn.click();
  292 |   await expect(page.getByText('I am Sora Kim. I am Korean.')).toBeVisible();
  293 |   await expect(page.getByRole('button', { name: /Hide Translation Hint/ })).toBeVisible();
  294 | 
  295 |   // Select the correct option and verify feedback + assisted marker
  296 |   const optButton = page.locator('.grid button').filter({ hasText: 'は' }).first();
  297 |   await optButton.click();
  298 |   await expect(page.getByText('Assisted')).toBeVisible();
  299 |   await expect(page.getByText('Sentence Meaning:')).toBeVisible();
  300 |   await expect(page.getByText('Sentence Rationale')).toBeVisible();
  301 | 
  302 |   // 4. Verify chapter switcher dropdown allows seamless chapter switching
  303 |   await page.getByLabel('Select chapter practice').selectOption({ label: 'Genki I · Lesson 2 (12 Qs)' });
  304 |   await expect(page.getByText('Question 1')).toBeVisible();
  305 |   const optKore = page.locator('.grid button').filter({ hasText: 'これ' }).first();
  306 |   await expect(optKore).toBeVisible();
  307 |   await optKore.click();
  308 |   await expect(page.getByText('Sentence Rationale')).toBeVisible();
  309 | });
  310 | 
  311 | test('no parenthesized romaji pronunciations in master tables or cards', async ({ page }) => {
> 312 |   await page.goto('/');
      |              ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
  313 |   await page.getByRole('button', { name: /Revision \(暗記表\)/ }).click();
  314 |   await expect(page.getByText('Revision & Master "Mug-Up" Tables')).toBeVisible();
  315 | 
  316 |   // Click Te-Form switcher button to view Te-Form table
  317 |   await page.getByRole('button', { name: /The Te-Form/ }).click();
  318 |   await expect(page.getByRole('heading', { level: 4, name: /The Te-Form/ })).toBeVisible();
  319 | 
  320 |   // Check page content for forbidden romaji pronunciations
  321 |   const pageContent = await page.content();
  322 |   expect(pageContent).not.toMatch(/\(matsu\)/i);
  323 |   expect(pageContent).not.toMatch(/\(kau\)/i);
  324 |   expect(pageContent).not.toMatch(/\(nomu\)/i);
  325 |   expect(pageContent).not.toMatch(/\(taberu\)/i);
  326 |   expect(pageContent).not.toMatch(/\(kuru\)/i);
  327 |   expect(pageContent).not.toMatch(/\(iku\)/i);
  328 |   expect(pageContent).not.toMatch(/\(shinu\)/i);
  329 |   expect(pageContent).not.toMatch(/\(asobu\)/i);
  330 |   expect(pageContent).not.toMatch(/\(kaku\)/i);
  331 |   expect(pageContent).not.toMatch(/\(oyogu\)/i);
  332 |   expect(pageContent).not.toMatch(/\(hanasu\)/i);
  333 |   expect(pageContent).not.toMatch(/\(dasu\)/i);
  334 |   expect(pageContent).not.toMatch(/\(takai desu\)/i);
  335 |   expect(pageContent).not.toMatch(/\(shizuka desu\)/i);
  336 |   expect(pageContent).not.toMatch(/\(hatachi\)/i);
  337 |   expect(pageContent).not.toMatch(/\(pun\)/i);
  338 | 
  339 |   // Verify ruby annotation renders kanji with furigana without romaji
  340 |   const table = page.locator('#teFormMatrix table').first();
  341 |   await expect(table).toBeVisible();
  342 |   const textWithoutRuby = await table.evaluate(el => {
  343 |     const clone = el.cloneNode(true) as HTMLElement;
  344 |     clone.querySelectorAll('rt').forEach(n => n.remove());
  345 |     return clone.textContent || '';
  346 |   });
  347 |   expect(textWithoutRuby).toContain('買う, 待つ, 取る');
  348 |   expect(textWithoutRuby).not.toContain('(kau)');
  349 |   expect(textWithoutRuby).not.toContain('(matsu)');
  350 | });
  351 | 
  352 | test('browser back and forward routing works without exiting the app', async ({ page }) => {
  353 |   await page.goto('/');
  354 | 
  355 |   // 1. Select another grammar point
  356 |   await page.locator('[role="button"]').filter({ hasText: '時間' }).first().click();
  357 |   await expect(page).toHaveURL(/\/learn\/g1-l1-time-and-age/);
  358 | 
  359 |   // 2. Switch to Practice mode
  360 |   await page.getByRole('button', { name: /Practice \(練習\)/ }).click();
  361 |   await expect(page).toHaveURL(/\/practice\//);
  362 |   await expect(page.getByText('Question 1')).toBeVisible();
  363 | 
  364 |   // 3. Switch to Revision mode
  365 |   await page.getByRole('button', { name: /Revision \(暗記表\)/ }).click();
  366 |   await expect(page).toHaveURL(/\/revision/);
  367 |   await expect(page.getByText('Revision & Master "Mug-Up" Tables')).toBeVisible();
  368 | 
  369 |   // 4. Press browser Back button -> should return to Practice mode
  370 |   await page.goBack();
  371 |   await expect(page).toHaveURL(/\/practice\//);
  372 |   await expect(page.getByText('Question 1')).toBeVisible();
  373 | 
  374 |   // 5. Press browser Back button again -> should return to the Time & Age lesson
  375 |   await page.goBack();
  376 |   await expect(page).toHaveURL(/\/learn\/g1-l1-time-and-age/);
  377 |   await expect(page.getByRole('heading', { level: 1 }).filter({ hasText: '時間' })).toBeVisible();
  378 | 
  379 |   // 6. Press browser Forward button -> should advance back to Practice mode
  380 |   await page.goForward();
  381 |   await expect(page).toHaveURL(/\/practice\//);
  382 |   await expect(page.getByText('Question 1')).toBeVisible();
  383 | 
  384 |   // 7. Direct URL navigation to Revision mode
  385 |   await page.goto('/revision');
  386 |   await expect(page.getByText('Revision & Master "Mug-Up" Tables')).toBeVisible();
  387 | });
  388 | 
  389 | test('comprehensive N3 and N2 synthesis master tables and level filters in revision desk', async ({ page }) => {
  390 |   await page.goto('/revision');
  391 |   await expect(page.getByText('Revision & Master "Mug-Up" Tables')).toBeVisible();
  392 | 
  393 |   const filterBar = page.getByTestId('revision-level-filters');
  394 | 
  395 |   // 1. Verify "All (28)" filter pill exists and shows all 28 tables
  396 |   await expect(filterBar.getByRole('button', { name: 'All (28)' })).toBeVisible();
  397 |   await expect(page.getByText('28 master tables & synthesis reference sheets')).toBeVisible();
  398 | 
  399 |   // 2. Filter by N3: 9 tables
  400 |   await filterBar.getByRole('button', { name: 'N3', exact: true }).click();
  401 |   await expect(page.getByText('9 master tables & synthesis reference sheets')).toBeVisible();
  402 |   // Check that N3 synthesis tables exist
  403 |   await expect(page.getByText('Core Compound Particles Matrix')).toBeVisible();
  404 |   await expect(page.getByText('Nominalizers Triad Matrix')).toBeVisible();
  405 |   await expect(page.getByText('The 4 わけ Quadruplets Decoded')).toBeVisible();
  406 |   await expect(page.getByText('The Decision & Custom Grid')).toBeVisible();
  407 |   await expect(page.getByText('Adverb & Sentence-Ending Collocations')).toBeVisible();
  408 |   await expect(page.getByText('Suffix Transformation Matrix')).toBeVisible();
  409 |   await expect(page.getByText('Spatiotemporal Direction Matrix')).toBeVisible();
  410 | 
  411 |   // 3. Filter by N2: 7 tables
  412 |   await filterBar.getByRole('button', { name: 'N2', exact: true }).click();
```