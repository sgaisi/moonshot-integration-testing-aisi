import {test,expect} from '@playwright/test';

test('Get Started', async ({ page }) => {
    await page.goto('http://127.0.0.1:3000');
    await page.getByText('Get Started').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/benchmarking/session/new'));
});

test('Start Red Teaming', async ({page }) => {
    await page.goto('http://127.0.0.1:3000');
    await page.getByText('Start Red Teaming').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/redteaming/sessions/new'));
});

test('Run Benchmarks', async ({page }) => {
    await page.goto('http://127.0.0.1:3000');
    await page.getByText('Run Benchmarks').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/benchmarking/session/new'));
});

test('Select Recipes', async ({page }) => {
    await page.goto('http://127.0.0.1:3000');
    await page.getByText('Select Recipes').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/benchmarking/cookbooks/new'));
});