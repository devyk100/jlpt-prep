# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: jlpt-exam-prep\tests\revision.spec.ts >> comprehensive N3 and N2 synthesis master tables and level filters in revision desk
- Location: jlpt-exam-prep\tests\revision.spec.ts:389:1

# Error details

```
Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
Call log:
  - navigating to "/revision", waiting until "load"

```

# Test source

```ts
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
  312 |   await page.goto('/');
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
> 390 |   await page.goto('/revision');
      |              ^ Error: page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL
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
  413 |   await expect(page.getByText('7 master tables & synthesis reference sheets')).toBeVisible();
  414 |   await expect(page.getByText('Inception & Turning Point Matrix')).toBeVisible();
  415 |   await expect(page.getByText('Evidential Evaluation from Nouns Matrix')).toBeVisible();
  416 |   await expect(page.getByText('Classical Remnants & Archaic Literary Forms')).toBeVisible();
  417 |   await expect(page.getByText('The Advanced こと Constructions Matrix')).toBeVisible();
  418 |   await expect(page.getByText('Double Negatives & Compelled Action Matrix')).toBeVisible();
  419 |   await expect(page.getByText('Sentence-Ending Constraints & Epistemic Stance Matrix')).toBeVisible();
  420 |   await expect(page.locator('#skmN2ConnectorsMatrix')).toBeVisible();
  421 | 
  422 |   // 4. Test "Jump to Lesson in Textbook" navigation from a newly added table
  423 |   await filterBar.getByRole('button', { name: 'N3', exact: true }).click();
  424 |   const jumpBtn = page.locator('#skmN3CompoundParticlesMatrix').getByRole('button', { name: /Jump to Lesson in Textbook/ });
  425 |   await jumpBtn.click();
  426 |   await expect(page).toHaveURL(/\/learn\/added-n3-b-60/);
  427 |   await expect(page.locator('h1')).toBeVisible();
  428 |   // The table is also embedded in the textbook lesson view!
  429 |   await expect(page.getByRole('heading', { name: 'High-Yield Lesson Table' })).toBeVisible();
  430 |   await expect(page.locator('table').first()).toBeVisible();
  431 | });
  432 | 
  433 | test('practice mode section 4 engineering repairs: exact chapter matching, honest empty state, attempt persistence, irreversible assistance, and touch separation', async ({ page }) => {
  434 |   // 1. Exact chapter matching: Genki I Lesson 1 has exactly 12 questions
  435 |   await page.goto('/practice/genki-1/Lesson%201');
  436 |   await expect(page.getByText('1 / 12')).toBeVisible();
  437 |   await expect(page.getByText('Question 1')).toBeVisible();
  438 | 
  439 |   // 2. Honest unavailable state for empty/unregistered chapter
  440 |   await page.goto('/practice/genki-1/Lesson%20999');
  441 |   await expect(page.getByText('Genki I · Lesson 999 Practice')).toBeVisible();
  442 |   await expect(page.getByText('Practice exercises for this specific section are currently in development')).toBeVisible();
  443 |   const returnBtn = page.getByRole('button', { name: 'Return to Textbook Study' });
  444 |   await expect(returnBtn).toBeVisible();
  445 | 
  446 |   // 3. Practice attempt persistence
  447 |   await page.goto('/practice/genki-1/Lesson%201');
  448 |   await expect(page.getByText('1 / 12')).toBeVisible();
  449 | 
  450 |   // Select option 1 for Question 1
  451 |   const firstOption = page.locator('.grid button').first();
  452 |   await firstOption.click();
  453 |   await expect(page.getByText('Sentence Rationale')).toBeVisible();
  454 | 
  455 |   // Reload page and verify state persisted
  456 |   await page.reload();
  457 |   await expect(page.getByText('1 / 12')).toBeVisible();
  458 |   await expect(page.getByText('Sentence Rationale')).toBeVisible();
  459 | 
  460 |   // 4. Irreversible assistance tracking
  461 |   // Advance to Question 2
  462 |   await page.getByRole('button', { name: /Next Question/ }).click();
  463 |   await expect(page.getByText('2 / 12')).toBeVisible();
  464 | 
  465 |   // Click Show Hint or Show Translation Hint
  466 |   const hintToggle = page.locator('button').filter({ hasText: /Show Hint|Show Translation Hint/ }).first();
  467 |   await hintToggle.click();
  468 |   await expect(page.getByText('Assisted').first()).toBeVisible();
  469 | 
  470 |   // Answer question 2
  471 |   await page.locator('.grid button').first().click();
  472 |   await expect(page.getByText('Sentence Rationale')).toBeVisible();
  473 |   // Feedback must display Assisted tag
  474 |   await expect(page.getByText('Assisted').first()).toBeVisible();
  475 | 
  476 |   // 5. Touch lookup vs selection separation
  477 |   // Advance to Question 3
  478 |   await page.getByRole('button', { name: /Next Question/ }).click();
  479 |   await expect(page.getByText('3 / 12')).toBeVisible();
  480 | 
  481 |   // Find a word token inside an option button or question sentence
  482 |   const wordSpan = page.locator('.grid button').first().locator('ruby').first();
  483 |   if (await wordSpan.count() > 0) {
  484 |     await wordSpan.click();
  485 |     // Tooltip must appear in portal
  486 |     const tooltip = page.locator('[role="tooltip"]');
  487 |     await expect(tooltip).toBeVisible();
  488 |     // Question must still NOT be answered (Sentence Rationale not visible)
  489 |     await expect(page.getByText('Sentence Rationale')).toHaveCount(0);
  490 |   }
```