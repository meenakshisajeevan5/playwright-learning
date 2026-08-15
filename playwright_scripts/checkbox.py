from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.locator(".rc-tree-switcher").first.click()
    page.get_by_role("checkbox", name="Select Desktop").check()
    expect(page.locator("#result")).to_contain_text("desktop")
    page.wait_for_timeout(3000)
    browser.close()