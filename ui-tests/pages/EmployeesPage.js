import { expect, Locator, Page } from '@playwright/test';
import { SearchPage } from './SearchPage';


export class EmployeesPage {
    /**
     * 
     * @param {Page} page 
     */
    constructor(page) {
        this.page = page
        this.skladOsobowy = page.locator("//div[@id='views-bootstrap-prezentacja-w-kategorii-terminy-blok-poddzialy']//a[contains(text(), 'Skład osobowy')]")
    }

    async clickSkladOsobowy() {
        await this.skladOsobowy.click()
        return new SearchPage(this.page)
    }
}