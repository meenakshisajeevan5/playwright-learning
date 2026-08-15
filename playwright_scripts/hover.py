from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.get_by_alt_text("User Avatar").nth(1).hover()
    expect(page.get_by_text("View profile").nth(1)).to_be_visible()
    page.wait_for_timeout(3000)
    browser.close()