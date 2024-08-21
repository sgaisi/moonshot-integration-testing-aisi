import { test, expect } from '../fixtures/base-test';

test.beforeEach(async ({ homePage }) => {
    await homePage.goto();
});

test('Get Started', async ({ homePage, page }) => {
    await page.getByText('Get Started').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/benchmarking/session/new'));
});

test('Start Red Teaming', async ({ homePage, page }) => {
    await page.getByText('Start Red Teaming').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/redteaming/sessions/new'));
});

test('Run Benchmarks', async ({ homePage, page }) => {
    await page.getByText('Run Benchmarks').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/benchmarking/session/new'));
});

test('Select Recipes', async ({ homePage, page }) => {
    await page.getByText('Select Recipes').click();
    await expect.soft(page).toHaveURL(new RegExp('^http://127.0.0.1:3000/benchmarking/cookbooks/new'));
});