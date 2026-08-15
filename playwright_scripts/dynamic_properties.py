from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/dynamic-properties")
    expect(page.get_by_role("button", name="Will enable 5 seconds")).to_be_enabled(timeout=10000)
    expect(page.get_by_role("button", name="Color Change")).to_be_visible(timeout=10000)
    expect(page.get_by_role("button", name="Visible After 5 Seconds")).to_be_visible(timeout=10000)
    page.wait_for_timeout(3000)
    browser.close()