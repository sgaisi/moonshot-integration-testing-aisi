import { test as base } from '@playwright/test';
import { HomePage } from '../fixtures/homepage';

// Extend base test by providing "homePage" functions and elements to test
// This new "test" can be used in multiple test files, and each of them will get the fixtures.
type MyFixtures = {
    homePage: HomePage;
};

export const test = base.extend<MyFixtures>({
    homePage: async ({ page }, use) => {
        await use(new HomePage(page));
    }
})

export { expect } from '@playwright/test'