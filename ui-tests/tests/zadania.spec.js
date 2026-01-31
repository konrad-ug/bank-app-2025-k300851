// @ts-check
import { test, expect } from '@playwright/test';
import { HomePage } from '../pages/HomePage';

test('Zadanie 1', async ({ page }) => {
  await page.goto('https://mfi.ug.edu.pl/');
  await page.locator("//nav//a[text()='Pracownicy']").click();
  await page.locator("//div[@id='views-bootstrap-prezentacja-w-kategorii-terminy-blok-poddzialy']//a[contains(text(), 'Skład osobowy')]").click();
  await page.locator("//input[@id='edit-combine']").click()

  await page.locator("//input[@id='edit-combine']").clear()
  await page.locator("//input[@id='edit-combine']").fill("sołtys")
  await page.locator("//button[@id='edit-submit-pracownik-szukaj']").click()
  await page.locator("//button[@id='edit-submit-pracownik-szukaj']").click()

  await expect(page.getByText("mgr Konrad Sołtys")).toBeVisible()
  await page.getByText("mgr Konrad Sołtys").click()

  await expect(page.locator(`//strong[contains(text(), "Nr pokoju")]/..`)).toContainText("Nr pokoju: 4.19")

});

test('Zadanie 2', async ({ page }) => {
  const fullName = "mgr Konrad Sołtys"

    const home = new HomePage(page)
    await home.goto()
    const employees = await home.clickEmployees()
    const search = await employees.clickSkladOsobowy()
    await search.searchEmployee(fullName)
    await search.resultShouldContains(fullName)
    const details = await search.selectEmployee(fullName)
    await details.roomShouldContains("Nr pokoju: 4.19")
})

test('Zadanie 3', async ({ page }) => {
  const fullName = "mgr Anna Baran"

    const home = new HomePage(page)
    await home.goto()
    const employees = await home.clickEmployees()
    const search = await employees.clickSkladOsobowy()
    await search.searchEmployee(fullName)
    await search.resultShouldContains(fullName)
    const details = await search.selectEmployee(fullName)
    await details.jednoskaShouldContains("Instytut Fizyki Doświadczalnej")
})

