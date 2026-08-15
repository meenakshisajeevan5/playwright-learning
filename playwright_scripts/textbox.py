from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/text-box")
    page.get_by_placeholder("Full Name").fill("Meenakshi Sajeevan")
    page.get_by_placeholder("name@example.com").fill("test@example.com")
    page.get_by_placeholder("Current Address").fill("123 Test Street")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#name")).to_contain_text("Meenakshi")
    page.wait_for_timeout(3000)
    browser.close()