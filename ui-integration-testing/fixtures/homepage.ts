import type { Page, Locator } from '@playwright/test';

export class HomePage {
  private readonly getStarted: Locator;
  private readonly redTeaming: Locator;
  private readonly benchmarks: Locator;
  private readonly recipes: Locator;

  constructor(public readonly page: Page) {
    this.getStarted = this.page.locator('');
    this.redTeaming = this.page.getByRole('listitem').nth(2);
    this.benchmarks = this.page.getByRole('listitem').nth(1);
    this.recipes = this.page.locator('');
  }

  async goto() {
    await this.page.goto('http://127.0.0.1:3000');
  }

  async goToTab(option: number) {
    switch (option) {
        case 2:
            await this.benchmarks.click();
            break;
        case 3:
            await this.redTeaming.click();
            break;
    }
  }
}