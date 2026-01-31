import { expect, Locator, Page } from '@playwright/test';
import { DetailsPage } from './DetailsPage';


export class SearchPage {
    /**
     * 
     * @param {Page} page 
     */
    constructor(page) {
        this.page = page
        this.searchInput = page.locator("//input[@id='edit-combine']")
        this.submitButton = page.locator("//button[@id='edit-submit-pracownik-szukaj']")
    }

    async searchEmployee(text) {
        await this.searchInput.click()
        await this.searchInput.clear()
        await this.searchInput.fill(text)
        await this.submitButton.click()
        await this.submitButton.click()
        return this
    }

    async resultShouldContains(text) {
        await expect(this.page.getByText(text)).toBeVisible()
        return this
    }

    async selectEmployee(text) {
        await this.page.getByText(text).click()
        return new DetailsPage(this.page)
    }
}
