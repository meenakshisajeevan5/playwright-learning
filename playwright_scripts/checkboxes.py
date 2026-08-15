from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    checkboxes.nth(0).check()
    checkboxes.nth(1).uncheck()
    page.wait_for_timeout(3000)
    browser.close()