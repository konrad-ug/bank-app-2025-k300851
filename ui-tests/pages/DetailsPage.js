import { expect, Locator, Page } from '@playwright/test';


export class DetailsPage {
    /**
     * 
     * @param {Page} page 
     */
    constructor(page) {
        this.page = page
        this.roomDetails = page.locator(`//strong[contains(text(), "Nr pokoju")]/..`)
        this.jednostkaDetails = page.locator("//div[@id='node-pracownik-full-group-jednostka-stanowisko']")
    }

    async roomShouldContains(text) {
        await expect(this.roomDetails).toContainText(text)
        return this
    }

    async jednoskaShouldContains(text) {
        await expect(this.jednostkaDetails).toContainText(text)
        return this
    }
}
