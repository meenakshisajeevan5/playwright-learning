from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option("2")
    expect(page.locator("#dropdown")).to_have_value("2")
    page.wait_for_timeout(3000)
    browser.close()