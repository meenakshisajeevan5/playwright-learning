from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/radio-button")
    page.get_by_label("Yes").click()
    expect(page.locator(".mt-3")).to_contain_text("Yes")
    page.get_by_label("Impressive").click()
    expect(page.locator(".mt-3")).to_contain_text("Impressive")
    page.wait_for_timeout(3000)
    browser.close()