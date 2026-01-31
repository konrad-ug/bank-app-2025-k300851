import { expect, Locator, Page } from '@playwright/test';
import { EmployeesPage } from './EmployeesPage';


export class HomePage {
    /**
     * 
     * @param {Page} page 
     */
    constructor(page) {
        this.page = page
        this.employees = page.locator("//nav//a[text()='Pracownicy']")
    }

    async goto() {
        await this.page.goto('https://mfi.ug.edu.pl/');
        return this
    }

    async clickEmployees() {
        await this.employees.click()
        return new EmployeesPage(this.page)
    }
}